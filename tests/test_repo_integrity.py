"""仓库完整性、资源链接、科学实测指标与前端语法自动化校验测试。"""

from __future__ import annotations

import json
import math
import pathlib
import re
import shutil
import subprocess
import tempfile
import warnings
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

import nbformat
import pytest

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
ASSETS_DIR = REPO_ROOT / "assets"
NOTEBOOKS_DIR = REPO_ROOT / "notebooks"
EXPERIMENTS_DIR = REPO_ROOT / "experiments"
README_PATH = REPO_ROOT / "README.md"
INDEX_PATH = REPO_ROOT / "index.html"
METRICS_PATH = EXPERIMENTS_DIR / "matlab_r2026a_metrics.json"

# HTML5 标准空元素（无需闭合标签）
HTML5_VOID_ELEMENTS = frozenset(
    {
        "area",
        "base",
        "br",
        "col",
        "embed",
        "hr",
        "img",
        "input",
        "link",
        "meta",
        "param",
        "source",
        "track",
        "wbr",
    }
)

PRIVATE_USER_PATH_RE = re.compile(
    r"([A-Za-z]:\\Users\\[^\s\"'<>]+|/Users/[^\s\"'<>]+|/home/[^\s\"'<>]+|[A-Za-z]:/Users/[^\s\"'<>]+)"
)
MD_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


class _StrictHtmlValidator(HTMLParser):
    """解析 HTML 文档，校验标签成对闭合、唯一 ID、关键 ARIA 属性并提取内联脚本与资源路径。"""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[tuple[str, int]] = []
        self.structure_errors: list[str] = []
        self.seen_ids: set[str] = set()
        self.duplicate_ids: list[str] = []
        self.local_refs: set[str] = set()
        self.roles: set[str] = set()
        self.aria_live_values: set[str] = set()
        self.inline_scripts: list[str] = []
        self._in_script = False
        self._script_chunks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag_lower = tag.lower()
        attr_map = {k.lower(): (v or "") for k, v in attrs}

        if "id" in attr_map and attr_map["id"]:
            elem_id = attr_map["id"]
            if elem_id in self.seen_ids:
                self.duplicate_ids.append(elem_id)
            self.seen_ids.add(elem_id)

        if "role" in attr_map and attr_map["role"]:
            self.roles.add(attr_map["role"])

        if "aria-live" in attr_map and attr_map["aria-live"]:
            self.aria_live_values.add(attr_map["aria-live"])

        for attr_name in ("src", "href"):
            val = attr_map.get(attr_name, "").strip()
            if val and not val.startswith(("http://", "https://", "#", "mailto:", "data:")):
                self.local_refs.add(val.split("?", 1)[0].split("#", 1)[0])

        if tag_lower == "script" and "src" not in attr_map:
            self._in_script = True
            self._script_chunks = []

        if tag_lower not in HTML5_VOID_ELEMENTS:
            self.stack.append((tag_lower, self.getpos()[0]))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        # 自闭合标签仅检查属性，不压入闭合栈
        tag_lower = tag.lower()
        if tag_lower in HTML5_VOID_ELEMENTS:
            self.handle_starttag(tag, attrs)

    def handle_data(self, data: str) -> None:
        if self._in_script:
            self._script_chunks.append(data)

    def handle_endtag(self, tag: str) -> None:
        tag_lower = tag.lower()
        if tag_lower == "script" and self._in_script:
            self.inline_scripts.append("".join(self._script_chunks))
            self._in_script = False
            self._script_chunks = []

        if tag_lower in HTML5_VOID_ELEMENTS:
            return

        if not self.stack:
            self.structure_errors.append(f"第 {self.getpos()[0]} 行出现多余闭合标签 </{tag_lower}>")
            return

        top_tag, start_line = self.stack.pop()
        if top_tag != tag_lower:
            self.structure_errors.append(
                f"标签错配：第 {start_line} 行打开 <{top_tag}>，第 {self.getpos()[0]} 行遇到 </{tag_lower}>"
            )


def _all_notebooks() -> list[pathlib.Path]:
    """返回根目录与 notebooks/ 目录下全部 Jupyter Notebook 路径。"""
    return sorted(list(REPO_ROOT.glob("*.ipynb")) + list(NOTEBOOKS_DIR.glob("*.ipynb")))


def test_notebooks_valid_nbformat_and_metadata() -> None:
    """校验全部 12 册 Jupyter Notebook 满足 nbformat 规范且无缺失 ID 警告。"""
    notebooks = _all_notebooks()
    root_nbs = sorted(REPO_ROOT.glob("*.ipynb"))
    chapter_nbs = sorted(NOTEBOOKS_DIR.glob("*.ipynb"))

    assert len(root_nbs) == 6, f"根目录应有 6 册基础笔记，实际为 {len(root_nbs)}"
    assert len(chapter_nbs) == 6, f"notebooks/ 应有 6 册实验课，实际为 {len(chapter_nbs)}"
    assert len(notebooks) == 12

    for nb_path in notebooks:
        raw = json.loads(nb_path.read_text(encoding="utf-8"))
        assert raw.get("nbformat") == 4, f"{nb_path.name} nbformat 版本异常"
        assert isinstance(raw.get("cells"), list) and len(raw["cells"]) > 0

        for idx, cell in enumerate(raw["cells"]):
            assert isinstance(cell.get("metadata"), dict), f"{nb_path.name} cell[{idx}] 缺少 metadata 字典"
            if cell.get("cell_type") == "code":
                assert "outputs" in cell, f"{nb_path.name} code cell[{idx}] 缺少 outputs"
                assert "execution_count" in cell, f"{nb_path.name} code cell[{idx}] 缺少 execution_count"

        # 严格校验 nbformat 结构，并将 MissingIDFieldWarning 视为错误
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            doc = nbformat.read(nb_path, as_version=4)
            nbformat.validate(doc)


def test_notebooks_have_no_broken_links_or_private_user_paths() -> None:
    """校验所有 Notebook 中的相对链接全部有效且不包含本机用户目录隐私路径。"""
    for nb_path in _all_notebooks():
        raw = json.loads(nb_path.read_text(encoding="utf-8"))
        for idx, cell in enumerate(raw.get("cells", [])):
            src = cell.get("source", [])
            src_text = "".join(src) if isinstance(src, list) else str(src)

            assert not PRIVATE_USER_PATH_RE.search(src_text), (
                f"{nb_path} cell[{idx}] 源码中残留个人绝对路径"
            )

            for link in MD_LINK_RE.findall(src_text):
                clean_link = link.strip().split("#", 1)[0].split("?", 1)[0]
                if not clean_link or clean_link.startswith(("http://", "https://", "mailto:")):
                    continue
                target = (nb_path.parent / clean_link).resolve()
                assert target.exists(), f"{nb_path} cell[{idx}] 存在死链：{link}"

            for output in cell.get("outputs", []):
                out_text = json.dumps(output, ensure_ascii=False)
                assert not PRIVATE_USER_PATH_RE.search(out_text), (
                    f"{nb_path} cell[{idx}] 输出中残留个人用户目录路径"
                )


def test_readme_and_index_asset_and_notebook_links_exist() -> None:
    """校验 README.md 与 index.html 引用的全部资源与笔记本路径 100% 存在。"""
    readme_text = README_PATH.read_text(encoding="utf-8")
    readme_links = MD_LINK_RE.findall(readme_text)
    assert len(readme_links) > 0, "README.md 中未提取到任何链接"

    referenced_from_readme: set[pathlib.Path] = set()
    for link in readme_links:
        clean_link = link.strip().split("#", 1)[0].split("?", 1)[0]
        if not clean_link or clean_link.startswith(("http://", "https://", "mailto:")):
            continue
        target = (REPO_ROOT / clean_link).resolve()
        assert target.exists(), f"README.md 存在无效本地链接：{link}"
        referenced_from_readme.add(target)

    # 校验 index.html 静态标签与 spreads 内联数据中的全部 assets/* 和 notebooks/* 引用
    html_text = INDEX_PATH.read_text(encoding="utf-8")
    parser = _StrictHtmlValidator()
    parser.feed(html_text)
    parser.close()

    for ref in parser.local_refs:
        target = (REPO_ROOT / ref).resolve()
        assert target.exists(), f"index.html 存在无效资源引用：{ref}"

    spread_refs = re.findall(r'"((?:assets|notebooks)/[^"]+)"', html_text)
    assert len(spread_refs) >= 24, "index.html spreads 配置中资源引用数量异常偏少"

    referenced_assets: set[pathlib.Path] = set()
    referenced_notebooks: set[pathlib.Path] = set()
    for rel_path in spread_refs:
        target = (REPO_ROOT / rel_path).resolve()
        assert target.exists(), f"index.html spreads 引用不存在：{rel_path}"
        if rel_path.startswith("assets/"):
            referenced_assets.add(target)
        elif rel_path.startswith("notebooks/"):
            referenced_notebooks.add(target)

    # 全部 6 册实验课均应在 README 与前端绘本中可直达
    expected_chapter_nbs = {p.resolve() for p in NOTEBOOKS_DIR.glob("*.ipynb")}
    assert expected_chapter_nbs.issubset(referenced_notebooks), "index.html 未覆盖全部 6 册实验课"
    assert expected_chapter_nbs.issubset(referenced_from_readme), "README.md 未覆盖全部 6 册实验课"

    # 全部 18 个媒体文件均应被前端绘本完整使用
    expected_assets = {p.resolve() for p in ASSETS_DIR.iterdir() if p.is_file()}
    assert expected_assets == referenced_assets, (
        f"assets/ 文件与 index.html 引用不完全匹配：{expected_assets ^ referenced_assets}"
    )


def test_svg_assets_are_valid_xml_and_gifs_valid_header() -> None:
    """校验全部 SVG 为合法 XML 且具备 viewBox，全部 GIF 具备合法魔数文件头。"""
    svg_files = sorted(ASSETS_DIR.glob("*.svg"))
    gif_files = sorted(ASSETS_DIR.glob("*.gif"))

    assert len(svg_files) == 14, f"assets/ 应包含 14 个 SVG 文件，实际为 {len(svg_files)}"
    assert len(gif_files) == 4, f"assets/ 应包含 4 个 GIF 文件，实际为 {len(gif_files)}"

    for svg_path in svg_files:
        tree = ET.parse(svg_path)
        root = tree.getroot()
        assert root.tag.endswith("svg"), f"{svg_path.name} 根标签不是 <svg>"
        assert root.attrib.get("viewBox"), f"{svg_path.name} 缺少 viewBox 属性"

    for gif_path in gif_files:
        header = gif_path.read_bytes()[:6]
        assert header in (b"GIF89a", b"GIF87a"), f"{gif_path.name} 文件头不是合法 GIF：{header!r}"


def test_matlab_r2026a_metrics_json_integrity() -> None:
    """校验 MATLAB R2026a 实测指标文件结构与数值合理性。"""
    data = json.loads(METRICS_PATH.read_text(encoding="utf-8"))

    assert "R2026a" in data.get("matlab_version", "")
    assert isinstance(data.get("gpu_device"), str) and data["gpu_device"]

    dd = data["double_descent"]
    assert len(dd["p_list"]) == len(dd["mse_train"]) == len(dd["mse_test"]) == 4
    for key in ("p_list", "mse_train", "mse_test"):
        assert all(isinstance(v, (int, float)) and math.isfinite(v) for v in dd[key])

    salary = data["outlier_salary"]
    assert salary["l1_median_normal_k"] == salary["l1_median_with_tycoon_k"] == 5
    assert salary["l2_mean_with_tycoon_k"] > 1000

    clustering = data["clustering"]
    assert clustering["em_gmm_acc_pct"] > clustering["kmeans_acc_pct"]
    assert clustering["elbo_end"] > clustering["elbo_start"]


def test_index_html_structure_a11y_and_security() -> None:
    """校验 index.html 标签完整闭合、无重复 ID、具备核心 ARIA 属性且零危险 XSS 写入接口。"""
    html_text = INDEX_PATH.read_text(encoding="utf-8")
    parser = _StrictHtmlValidator()
    parser.feed(html_text)
    parser.close()

    assert not parser.structure_errors, f"HTML 结构异常：{parser.structure_errors}"
    assert not parser.stack, f"存在未闭合的 HTML 标签：{parser.stack}"
    assert not parser.duplicate_ids, f"存在重复 id 属性：{parser.duplicate_ids}"

    assert {"tablist", "tab", "tabpanel", "status"}.issubset(parser.roles), (
        f"缺少关键无障碍 ARIA role：{parser.roles}"
    )
    assert "polite" in parser.aria_live_values, "缺少 aria-live='polite' 实时播报区域"

    assert len(parser.inline_scripts) >= 1, "index.html 未检测到内联交互脚本"
    combined_js = "\n".join(parser.inline_scripts)
    # 剔除单行与多行注释后，检查是否出现潜在 XSS 危险调用
    js_without_comments = re.sub(r"/\*[\s\S]*?\*/|//[^\n]*", "", combined_js)
    dangerous_patterns = (
        (r"\.(?:innerHTML|outerHTML)\b", "innerHTML/outerHTML"),
        (r"\bdocument\.write\s*\(", "document.write("),
        (r"(?<![.\w])eval\s*\(", "eval("),
    )
    for pattern, label in dangerous_patterns:
        assert not re.search(pattern, js_without_comments), f"内联脚本包含潜在 XSS 风险调用：{label}"


def test_css_compatibility_and_responsive_guards() -> None:
    """校验样式表包含毛玻璃前缀与降级、移动端 dvh 视口适配及减少动态偏好支持。"""
    style_text = (REPO_ROOT / "style.css").read_text(encoding="utf-8")
    tokens_text = (REPO_ROOT / "tokens.css").read_text(encoding="utf-8")

    assert "-webkit-backdrop-filter" in style_text, "style.css 缺少 -webkit-backdrop-filter 前缀"
    assert "@supports not" in style_text, "style.css 缺少 backdrop-filter 不支持降级策略"
    assert "100dvh" in style_text, "style.css 缺少移动端 100dvh 视口高度兼容"
    assert "prefers-reduced-motion" in style_text, "style.css 缺少 prefers-reduced-motion 无障碍适配"
    assert '"Noto Sans SC"' in tokens_text, "tokens.css 缺少 Noto Sans SC 字体回退配置"


def test_index_inline_javascript_syntax_with_node() -> None:
    """提取 index.html 内联 JavaScript 并通过 node --check 校验语法 100% 合法。"""
    node_bin = shutil.which("node")
    if node_bin is None:
        pytest.skip("当前环境未安装 Node.js，跳过 node --check 校验")

    html_text = INDEX_PATH.read_text(encoding="utf-8")
    parser = _StrictHtmlValidator()
    parser.feed(html_text)
    parser.close()

    assert parser.inline_scripts, "未找到可校验的内联脚本"
    for idx, script_code in enumerate(parser.inline_scripts):
        with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as tmp:
            tmp.write(script_code)
            tmp_path = pathlib.Path(tmp.name)
        try:
            proc = subprocess.run(
                [node_bin, "--check", str(tmp_path)],
                capture_output=True,
                text=True,
                check=False,
            )
            assert proc.returncode == 0, f"内联脚本 #{idx} 语法检查失败：\n{proc.stderr}"
        finally:
            tmp_path.unlink(missing_ok=True)


def test_experiment_scripts_have_no_hardcoded_user_paths() -> None:
    """校验 experiments/*.py 不含硬编码本机用户绝对路径，保证跨平台可复现。"""
    py_files = sorted(EXPERIMENTS_DIR.glob("*.py"))
    assert len(py_files) >= 6
    for py_path in py_files:
        text = py_path.read_text(encoding="utf-8")
        assert not PRIVATE_USER_PATH_RE.search(text), f"{py_path.name} 包含硬编码用户绝对路径"
