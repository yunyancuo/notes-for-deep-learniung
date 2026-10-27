# -*- coding: utf-8 -*-
"""
重绘《小猫团子与老橘师傅》八幕绘本插画（pic01 ~ pic08）。
风格：奶油纸底 + 粉彩色板 + 圆润猫咪角色，与个人主页阅读器同一套色板。
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.normpath(os.path.join(HERE, '..', 'assets'))
os.makedirs(ASSETS, exist_ok=True)

W, H = 1000, 410
INK = '#3A3F52'
MUTED = '#7A8092'
PAPER = '#FDFBF6'
ACC = '#8B80AE'
RED = '#D97A86'
BLUE = '#7FA8D9'
GREEN = '#6FAE82'
ORANGE = '#DFA25E'
CREAM = '#FBF6EC'

FONT = "'LXGW WenKai','WenKai','STKaiti','KaiTi','PingFang SC','Microsoft YaHei',sans-serif"


def paper():
    """纸底 + 细颗粒 + 四角小装饰"""
    s = [f'<rect width="{W}" height="{H}" rx="20" fill="{PAPER}"/>']
    s.append(f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="19" fill="none" stroke="#EAE3D8" stroke-width="2"/>')
    import random
    rng = random.Random(7)
    dots = []
    for _ in range(90):
        x, y = rng.uniform(8, W - 8), rng.uniform(8, H - 8)
        c = rng.choice(['#EFE9DD', '#F3EDE2', '#EDE6F2'])
        dots.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rng.uniform(0.8,1.6):.1f}" fill="{c}"/>')
    s.append(''.join(dots))
    # 右下角小星星
    s.append(f'<path d="M {W-46} {H-34} l 3 7 7 3 -7 3 -3 7 -3 -7 -7 -3 7 -3 z" fill="#E7E0D4"/>')
    s.append(f'<circle cx="{W-66}" cy="{H-22}" r="2.2" fill="#E7E0D4"/>')
    return ''.join(s)


def cat(cx, cy, r=30, role='tuanzi', mood='hi'):
    """团子（奶牛猫）与老橘师傅（橘猫）头像。mood: hi / think / smile"""
    if role == 'tuanzi':
        fur, patch, line = '#FFFFFF', '#4A4560', '#4A4560'
        inner = '#F3C9CD'
    else:
        fur, patch, line = '#F0B26B', '#D99A4E', '#8C6239'
        inner = '#E89B7C'

    e = []
    # 耳朵
    e.append(f'<path d="M {cx-r*0.82:.0f} {cy-r*0.50:.0f} Q {cx-r*1.05:.0f} {cy-r*1.30:.0f} {cx-r*0.30:.0f} {cy-r*0.86:.0f} Z" fill="{fur}" stroke="{line}" stroke-width="2.4" stroke-linejoin="round"/>')
    e.append(f'<path d="M {cx+r*0.82:.0f} {cy-r*0.50:.0f} Q {cx+r*1.05:.0f} {cy-r*1.30:.0f} {cx+r*0.30:.0f} {cy-r*0.86:.0f} Z" fill="{fur}" stroke="{line}" stroke-width="2.4" stroke-linejoin="round"/>')
    e.append(f'<path d="M {cx-r*0.70:.0f} {cy-r*0.62:.0f} Q {cx-r*0.80:.0f} {cy-r*1.02:.0f} {cx-r*0.45:.0f} {cy-r*0.78:.0f} Z" fill="{inner}"/>')
    e.append(f'<path d="M {cx+r*0.70:.0f} {cy-r*0.62:.0f} Q {cx+r*0.80:.0f} {cy-r*1.02:.0f} {cx+r*0.45:.0f} {cy-r*0.78:.0f} Z" fill="{inner}"/>')
    # 头
    e.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fur}" stroke="{line}" stroke-width="2.4"/>')
    # 奶牛猫斑块
    if role == 'tuanzi':
        e.append(f'<path d="M {cx+r*0.36:.0f} {cy-r*0.94:.0f} Q {cx+r*0.95:.0f} {cy-r*0.72:.0f} {cx+r*0.86:.0f} {cy-r*0.12:.0f} Q {cx+r*0.52:.0f} {cy-r*0.30:.0f} {cx+r*0.40:.0f} {cy-r*0.62:.0f} Z" fill="{patch}" opacity="0.88"/>')
        e.append(f'<path d="M {cx-r*0.98:.0f} {cy+r*0.28:.0f} Q {cx-r*0.62:.0f} {cy+r*0.42:.0f} {cx-r*0.70:.0f} {cy+r*0.78:.0f} Q {cx-r*0.95:.0f} {cy+r*0.66:.0f} {cx-r*0.98:.0f} {cy+r*0.28:.0f} Z" fill="{patch}" opacity="0.85"/>')
    else:
        # 橘猫条纹
        for i, dx in enumerate((-0.34, 0.0, 0.34)):
            x0 = cx + r * dx
            e.append(f'<path d="M {x0-4:.0f} {cy-r+4:.0f} Q {x0:.0f} {cy-r*0.62:.0f} {x0+4:.0f} {cy-r+4:.0f}" fill="none" stroke="{patch}" stroke-width="3" stroke-linecap="round"/>')
    # 眼睛
    ex = r * 0.38
    ey = cy - r * 0.08
    if mood == 'think':
        e.append(f'<path d="M {cx-ex-5:.0f} {ey:.0f} Q {cx-ex:.0f} {ey-5:.0f} {cx-ex+5:.0f} {ey:.0f}" fill="none" stroke="{line}" stroke-width="2.6" stroke-linecap="round"/>')
        e.append(f'<path d="M {cx+ex-5:.0f} {ey:.0f} Q {cx+ex:.0f} {ey-5:.0f} {cx+ex+5:.0f} {ey:.0f}" fill="none" stroke="{line}" stroke-width="2.6" stroke-linecap="round"/>')
    else:
        e.append(f'<ellipse cx="{cx-ex:.0f}" cy="{ey:.0f}" rx="4.6" ry="5.4" fill="{line}"/>')
        e.append(f'<ellipse cx="{cx+ex:.0f}" cy="{ey:.0f}" rx="4.6" ry="5.4" fill="{line}"/>')
        e.append(f'<circle cx="{cx-ex-1.6:.0f}" cy="{ey-1.9:.0f}" r="1.6" fill="#FFF"/>')
        e.append(f'<circle cx="{cx+ex-1.6:.0f}" cy="{ey-1.9:.0f}" r="1.6" fill="#FFF"/>')
    # 鼻子 + 嘴
    e.append(f'<path d="M {cx-3:.0f} {cy+r*0.22:.0f} h 6 l -3 3.4 z" fill="{inner}" stroke="{line}" stroke-width="1.2" stroke-linejoin="round"/>')
    if mood == 'smile' or role == 'laoju':
        e.append(f'<path d="M {cx-6:.0f} {cy+r*0.36:.0f} Q {cx:.0f} {cy+r*0.48:.0f} {cx+6:.0f} {cy+r*0.36:.0f}" fill="none" stroke="{line}" stroke-width="2" stroke-linecap="round"/>')
    else:
        e.append(f'<path d="M {cx:.0f} {cy+r*0.32:.0f} q 3 4 6 0" fill="none" stroke="{line}" stroke-width="2" stroke-linecap="round"/>')
    # 腮红
    e.append(f'<ellipse cx="{cx-r*0.62:.0f}" cy="{cy+r*0.22:.0f}" rx="4.4" ry="2.8" fill="{inner}" opacity="0.75"/>')
    e.append(f'<ellipse cx="{cx+r*0.62:.0f}" cy="{cy+r*0.22:.0f}" rx="4.4" ry="2.8" fill="{inner}" opacity="0.75"/>')
    # 胡须
    for sgn in (-1, 1):
        for dy in (-0.10, 0.06, 0.22):
            x1 = cx + sgn * r * 0.78
            x2 = cx + sgn * r * (1.22 if role == 'tuanzi' else 1.16)
            e.append(f'<line x1="{x1:.0f}" y1="{cy+r*dy:.0f}" x2="{x2:.0f}" y2="{cy+r*(dy-0.04):.0f}" stroke="{line}" stroke-width="1.3" stroke-linecap="round" opacity="0.65"/>')
    # 老橘师傅的小圆眼镜（挂在鼻梁）
    if role == 'laoju':
        e.append(f'<circle cx="{cx-ex:.0f}" cy="{ey:.0f}" r="9.5" fill="none" stroke="#6E7488" stroke-width="1.8"/>')
        e.append(f'<circle cx="{cx+ex:.0f}" cy="{ey:.0f}" r="9.5" fill="none" stroke="#6E7488" stroke-width="1.8"/>')
        e.append(f'<path d="M {cx-ex+9.5:.0f} {ey:.0f} h {2*ex-19:.0f}" stroke="#6E7488" stroke-width="1.8"/>')
    return ''.join(e)


def header(kicker, title, dialogue=None, tuanzi_text=None, lauju_text=None):
    """顶部标题条 + 可选的双猫对话气泡"""
    s = []
    y = 14
    s.append(f'<text x="42" y="{y+14}" font-size="11" letter-spacing="3" fill="{ACC}" font-family="{FONT}" font-weight="600">{kicker}</text>')
    s.append(f'<text x="42" y="{y+44}" font-size="24" fill="{INK}" font-family="{FONT}" font-weight="600">{title}</text>')
    s.append(f'<line x1="42" y1="{y+58}" x2="{W-42}" y2="{y+58}" stroke="#E5DECF" stroke-width="1.6" stroke-dasharray="1 6" stroke-linecap="round"/>')
    s.append(cat(880, 52, 30, 'tuanzi', 'hi'))
    s.append(cat(944, 60, 34, 'laoju', 'smile'))
    if dialogue:
        # 双猫对话条
        by = 92
        s.append(f'<rect x="42" y="{by}" width="916" height="64" rx="16" fill="#FFFFFF" opacity="0.75" stroke="#EBE4D6" stroke-width="1.4"/>')
        s.append(cat(76, by + 32, 20, 'tuanzi', 'hi'))
        s.append(f'<text x="110" y="{by+20}" font-size="12.5" fill="{INK}" font-family="{FONT}"><tspan font-weight="600">团子：</tspan>{tuanzi_text}</text>')
        s.append(cat(924, by + 38, 20, 'laoju', 'smile'))
        s.append(f'<text x="110" y="{by+46}" font-size="12.5" fill="#5A6070" font-family="{FONT}"><tspan font-weight="600" fill="{ACC}">老橘师傅：</tspan>{lauju_text}</text>')
    return ''.join(s)


def panel(x, y, w, h, num, title, fill='#FFFFFF', stroke='#EBE4D6'):
    """圆角内容卡片 + 步骤徽标"""
    s = []
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{fill}" stroke="{stroke}" stroke-width="1.6"/>')
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="none" stroke="#FFFFFF" stroke-width="3" opacity="0.55"/>')
    s.append(f'<circle cx="{x+24}" cy="{y+24}" r="12" fill="{ACC}"/>')
    s.append(f'<text x="{x+24}" y="{y+28.5}" font-size="13" fill="#FFFFFF" text-anchor="middle" font-family="{FONT}" font-weight="600">{num}</text>')
    s.append(f'<text x="{x+44}" y="{y+29}" font-size="15" fill="{INK}" font-family="{FONT}" font-weight="600">{title}</text>')
    return ''.join(s)


def wrap_text(text, limit):
    lines, cur = [], ''
    for ch in text:
        cur += ch
        if len(cur) >= limit:
            lines.append(cur)
            cur = ''
    if cur:
        lines.append(cur)
    return lines


def note(x, y, text, limit=16, size=12, color=None, lh=18):
    color = color or '#6A7080'
    lines = wrap_text(text, limit)
    s = []
    for i, ln in enumerate(lines):
        s.append(f'<text x="{x}" y="{y+i*lh}" font-size="{size}" fill="{color}" font-family="{FONT}">{ln}</text>')
    return ''.join(s)


def watermelon(cx, cy, r, ripe=0.8):
    """西瓜：深绿底色、弯曲瓜纹、小瓜藤"""
    s = []
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#CDE6BE" stroke="#5E8A53" stroke-width="2.8"/>')
    for k in (-0.62, -0.21, 0.21, 0.62):
        x0 = cx + r * k
        bend = r * 0.55 * (1 - abs(k))
        s.append(f'<path d="M {x0:.0f} {cy-r*0.88:.0f} Q {x0+bend:.0f} {cy:.0f} {x0:.0f} {cy+r*0.88:.0f}" fill="none" stroke="#5E8A53" stroke-width="{max(2.2, r*0.075):.1f}" stroke-linecap="round" opacity="0.9"/>')
    s.append(f'<path d="M {cx-r*0.14:.0f} {cy-r*0.94:.0f} q {r*0.14:.0f} {-r*0.22:.0f} {r*0.30:.0f} {-r*0.16:.0f}" fill="none" stroke="#7B6A4E" stroke-width="3.6" stroke-linecap="round"/>')
    s.append(f'<path d="M {cx+r*0.16:.0f} {cy-r*1.02:.0f} q {r*0.30:.0f} {-r*0.10:.0f} {r*0.34:.0f} {r*0.12:.0f} q {-r*0.16:.0f} {r*0.10:.0f} {-r*0.34:.0f} {-r*0.12:.0f} z" fill="#6FAE82"/>')
    s.append(f'<ellipse cx="{cx-r*0.42:.0f}" cy="{cy-r*0.46:.0f}" rx="{r*0.20:.0f}" ry="{r*0.11:.0f}" fill="#FFFFFF" opacity="0.6" transform="rotate(-24 {cx-r*0.42:.0f} {cy-r*0.46:.0f})"/>')
    return ''.join(s)


def spark(x, y, c='#E4D9F0', sc=1.0):
    return (f'<path d="M {x} {y-7*sc} l {1.8*sc} {5.2*sc} {5.2*sc} {1.8*sc} -{5.2*sc} {1.8*sc} -{1.8*sc} {5.2*sc} '
            f'-{1.8*sc} -{5.2*sc} -{5.2*sc} -{1.8*sc} {5.2*sc} -{1.8*sc} z" fill="{c}"/>')


# --------------------------------------------------------------------------
# pic01 买瓜与租房：特征 / 标签 / 模型
# --------------------------------------------------------------------------
def pic01():
    s = [paper()]
    s.append(header(
        'ACT 1 · 西瓜书第 1 章',
        '第一幕 · 去菜市场买西瓜，去城中村看房',
        dialogue=True,
        tuanzi_text='师傅，电脑没有舌头也没有眼睛，它怎么学会挑瓜和看房呀？',
        lauju_text='跟人一样：先看线索，再对答案，最后攒一张打分卡。'))

    top = 176
    ph = 212
    # 面板1 特征
    s.append(panel(42, top, 288, ph, '①', '看线索 · 特征 x', fill='#F6F9F3'))
    s.append(watermelon(118, top + 118, 46))
    s.append(note(186, top + 84, '瓜蒂弯不弯', 12))
    s.append(note(186, top + 106, '纹路清不清', 12))
    s.append(note(186, top + 128, '拍声脆不脆', 12))
    s.append(f'<line x1="196" y1="{top+138}" x2="196" y2="{top+150}" stroke="#C9D8C0" stroke-width="1.4"/>')
    s.append(note(186, top + 162, '看房：面积、地铁、朝向', 13, color='#8A909E'))
    # 面板2 标签
    s.append(panel(356, top, 288, ph, '②', '对答案 · 标签 y', fill='#FBF4F4'))
    # 三张记录小卡
    for i, (txt, good) in enumerate([('1 号瓜：脆 → 甜 ✓', True), ('2 号瓜：闷 → 生 ✗', False), ('3 号房：月租 2400', True)]):
        yy = top + 64 + i * 46
        s.append(f'<rect x="384" y="{yy}" width="232" height="34" rx="10" fill="#FFFFFF" stroke="#EAD9DB" stroke-width="1.4"/>')
        s.append(f'<circle cx="404" cy="{yy+17}" r="5" fill="{GREEN if good else RED}"/>')
        s.append(f'<text x="420" y="{yy+22}" font-size="13.5" fill="#565D6E" font-family="{FONT}">{txt}</text>')
    s.append(note(384, top + 198, '切开尝过的甜度、真实成交价，就是标准答案', 22, size=12))
    # 面板3 模型
    s.append(panel(670, top, 288, ph, '③', '攒经验 · 模型 f(x)', fill='#F5F3FA'))
    # 打分卡
    s.append(f'<rect x="700" y="{top+56}" width="228" height="104" rx="12" fill="#FFFFFF" stroke="#E2DCF0" stroke-width="1.5"/>')
    rows = [('拍声脆响', '+50', 0.9, RED), ('离地铁近', '+30', 0.55, BLUE), ('纹路清晰', '+20', 0.35, GREEN)]
    for i, (name, pts, w, c) in enumerate(rows):
        yy = top + 74 + i * 30
        s.append(f'<text x="712" y="{yy+6}" font-size="12.5" fill="#565D6E" font-family="{FONT}">{name}</text>')
        s.append(f'<rect x="812" y="{yy-4}" width="76" height="9" rx="4.5" fill="#EFECE6"/>')
        s.append(f'<rect x="812" y="{yy-4}" width="{76*w:.0f}" height="9" rx="4.5" fill="{c}"/>')
        s.append(f'<text x="798" y="{yy+5}" font-size="11.5" fill="{c}" text-anchor="end" font-family="{FONT}" font-weight="600">{pts}</text>')
    s.append(note(700, top + 186, '下次遇到没切开的瓜，照卡一算就打分', 22, size=12))
    s.append(spark(650, 168))
    s.append('</svg>')
    return ''.join(s)


# --------------------------------------------------------------------------
# 通用小元素
# --------------------------------------------------------------------------
def axis(x1, y, x2, label=None):
    s = [f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="#C9C2B4" stroke-width="1.6" stroke-linecap="round"/>']
    if label:
        s.append(f'<text x="{x2}" y="{y+16}" font-size="11" fill="{MUTED}" text-anchor="end" font-family="{FONT}">{label}</text>')
    return ''.join(s)


def mini_chart(x, y, w, h, pts, curve_path, curve_color=ACC, curve_w=2.6, dash=None, dots_c='#C9A0A8', dot_r=3.4):
    s = []
    s.append(f'<line x1="{x}" y1="{y+h}" x2="{x+w}" y2="{y+h}" stroke="#CFC8BA" stroke-width="1.5" stroke-linecap="round"/>')
    s.append(f'<line x1="{x}" y1="{y+h}" x2="{x}" y2="{y}" stroke="#CFC8BA" stroke-width="1.5" stroke-linecap="round"/>')
    for px, py in pts:
        s.append(f'<circle cx="{px:.0f}" cy="{py:.0f}" r="{dot_r}" fill="{dots_c}" stroke="#FFFFFF" stroke-width="1"/>')
    d = f' stroke-dasharray="{dash}"' if dash else ''
    s.append(f'<path d="{curve_path}" fill="none" stroke="{curve_color}" stroke-width="{curve_w}" stroke-linecap="round"{d}/>')
    return ''.join(s)


def car(cx, cy, c, sc=1.0, ring=False):
    s = []
    s.append(f'<g transform="translate({cx},{cy}) scale({sc})">')
    s.append(f'<rect x="-14" y="-10" width="28" height="14" rx="6" fill="{c}"/>')
    s.append(f'<path d="M -8 -10 q 4 -8 12 -8 q 6 0 8 8 z" fill="{c}"/>')
    s.append(f'<circle cx="-7" cy="5" r="3.4" fill="#4A4560"/>')
    s.append(f'<circle cx="7" cy="5" r="3.4" fill="#4A4560"/>')
    s.append(f'<rect x="-4" y="-7" width="10" height="5" rx="2" fill="#FFFFFF" opacity="0.75"/>')
    s.append('</g>')
    if ring:
        s.append(f'<circle cx="{cx}" cy="{cy-2}" r="17" fill="none" stroke="#C9A13B" stroke-width="2.2" stroke-dasharray="3 3"/>')
    return ''.join(s)


# --------------------------------------------------------------------------
# pic02 三种学生
# --------------------------------------------------------------------------
def pic02():
    import math, random
    s = [paper()]
    s.append(header(
        'ACT 2 · 西瓜书第 2 章',
        '第二幕 · 期末考试复习的三种同学',
        dialogue=True,
        tuanzi_text='把 15 道模拟题连印刷脏墨点都背下来，期末就能满分了吧？',
        lauju_text='背墨点的那位，模拟卷满分，新卷子当场不及格。'))

    top, ph = 176, 212
    xs = [56 + i * 12 for i in range(15)]
    rng = random.Random(3)

    def wave_y(px, base, amp):
        t = (px - 56) / 132.0
        return base - amp * math.sin(t * 2.6 * math.pi)

    pts = [(x, wave_y(x, top + 128, 34) + rng.uniform(-5, 5)) for x in xs]
    s.append(panel(42, top, 288, ph, '①', '全蒙 C · 欠拟合', fill='#F6F6F9'))
    s.append(mini_chart(70, top + 44, 232, 108, pts,
                        f'M 70 {top+128} L 302 {top+128}', curve_color=BLUE, dots_c='#C4BBD4'))
    s.append(f'<text x="70" y="{top+184}" font-size="12" fill="#6A7080" font-family="{FONT}">直尺画波浪：规律完全没摸着，错得很稳。</text>')
    s.append(panel(356, top, 288, ph, '②', '死背墨点 · 过拟合', fill='#FBF4F4'))
    xs2 = [x + 314 for x in xs]
    path2 = f'M {xs2[0]} {wave_y(xs2[0], top+128, 34):.0f} ' + ' '.join(f'L {x} {wave_y(x, top+128, 34):.0f}' for x in xs2)
    s.append(mini_chart(384, top + 44, 232, 108, [(px + 314, py) for px, py in pts], path2, curve_color=RED, dots_c='#D9A9B1'))
    s.append(f'<text x="384" y="{top+184}" font-size="12" fill="#6A7080" font-family="{FONT}">连脏墨点都背：模拟卷满分，新题全崩。</text>')
    s.append(panel(670, top, 288, ph, '③', '摸清规律 · 恰到好处', fill='#F4F8F3'))
    xs3 = [x + 628 for x in xs]
    path3 = f'M {xs3[0]} {wave_y(xs3[0], top+128, 34):.0f} ' + ' '.join(
        f'Q {x+6} {wave_y(x+6, top+128, 34):.0f} {min(x+12, 930)} {wave_y(min(x+12, 930), top+128, 34):.0f}' for x in xs3[:-1])
    s.append(mini_chart(698, top + 44, 232, 108, [(px + 628, py) for px, py in pts], path3, curve_color=GREEN, dots_c='#B9D2B4'))
    s.append(f'<text x="698" y="{top+184}" font-size="12" fill="#6A7080" font-family="{FONT}">只抓大规律：墨点只是巧合，新卷照样高分。</text>')
    s.append(spark(340, 168))
    s.append('</svg>')
    return ''.join(s)


# --------------------------------------------------------------------------
# pic03 首富与行李箱
# --------------------------------------------------------------------------
def pic03():
    s = [paper()]
    s.append(header(
        'ACT 3 · 西瓜书第 3 / 11 章',
        '第三幕 · 首富拉歪平均数，行李箱逼你断舍离',
        dialogue=True,
        tuanzi_text='亿万富翁转学进来，全班平均工资瞬间失真，怎么办？',
        lauju_text='别算平均，排排队看正中间；行李箱小一点，废话自己扔。'))

    top, ph = 176, 212
    s.append(panel(42, top, 288, ph, '①', '排排队 · L1 中位数', fill='#F4F8F3'))
    ax_y = top + 150
    s.append(axis(70, ax_y, 302))
    for i in range(9):
        cx = 84 + i * 14
        s.append(f'<circle cx="{cx}" cy="{ax_y-9}" r="6" fill="{BLUE}"/>')
        s.append(f'<circle cx="{cx}" cy="{ax_y-19}" r="4.6" fill="{BLUE}"/>')
        s.append(f'<line x1="{cx}" y1="{ax_y-14}" x2="{cx}" y2="{ax_y-11}" stroke="{BLUE}" stroke-width="3"/>')
    s.append(f'<circle cx="284" cy="{ax_y-9}" r="6" fill="{ORANGE}"/>')
    s.append(f'<circle cx="284" cy="{ax_y-19}" r="4.6" fill="{ORANGE}"/>')
    s.append(f'<line x1="284" y1="{ax_y-14}" x2="284" y2="{ax_y-11}" stroke="{ORANGE}" stroke-width="3"/>')
    s.append(f'<text x="284" y="{ax_y-30}" font-size="10.5" fill="#B77E36" text-anchor="middle" font-family="{FONT}">首富 1 个亿</text>')
    s.append(f'<line x1="168" y1="{ax_y+8}" x2="168" y2="{ax_y-32}" stroke="{GREEN}" stroke-width="2.2"/>')
    s.append(f'<text x="168" y="{ax_y-40}" font-size="11" fill="{GREEN}" text-anchor="middle" font-family="{FONT}" font-weight="600">中位数 5k</text>')
    s.append(f'<text x="70" y="{top+186}" font-size="12" fill="#6A7080" font-family="{FONT}">平均数被拉到一千万；正中间那位还是 5 千。</text>')

    s.append(panel(356, top, 288, ph, '②', '圆碗与尖谷 · L2 与 L1', fill='#F6F6F9'))
    bx, by = 438, top + 118
    s.append(f'<path d="M {bx-46} {by-26} Q {bx} {by+44} {bx+46} {by-26}" fill="none" stroke="#9A8FD0" stroke-width="3"/>')
    s.append(f'<circle cx="{bx}" cy="{by+16}" r="7" fill="{ACC}"/>')
    s.append(f'<text x="{bx}" y="{by+62}" font-size="11.5" fill="{MUTED}" text-anchor="middle" font-family="{FONT}">L2 圆碗 · 丝滑停底</text>')
    vx = 566
    s.append(f'<path d="M {vx-46} {by+22} L {vx} {by-20} L {vx+46} {by+22}" fill="none" stroke="{ORANGE}" stroke-width="3"/>')
    s.append(f'<circle cx="{vx-18}" cy="{by-4}" r="7" fill="{ORANGE}"/>')
    s.append(f'<path d="M {vx-32} {by+8} l 12 6 -12 6" fill="none" stroke="{RED}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')
    s.append(f'<path d="M {vx-4} {by+8} l -12 6 12 6" fill="none" stroke="{RED}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')
    s.append(f'<text x="{vx}" y="{by+62}" font-size="11.5" fill="{MUTED}" text-anchor="middle" font-family="{FONT}">L1 尖谷 · 步子大就横跳</text>')

    s.append(panel(670, top, 288, ph, '③', '小行李箱 · Lasso 稀疏', fill='#FBF4F4'))
    cx3, cy3 = 738, top + 118
    s.append(f'<circle cx="{cx3}" cy="{cy3}" r="34" fill="none" stroke="{BLUE}" stroke-width="2.4" stroke-dasharray="4 4"/>')
    for dx, dy in ((-16, 6), (6, -14), (18, 12), (-4, 22)):
        s.append(f'<circle cx="{cx3+dx}" cy="{cy3+dy}" r="4" fill="{BLUE}" opacity="0.8"/>')
    s.append(f'<text x="{cx3}" y="{cy3+58}" font-size="11.5" fill="{MUTED}" text-anchor="middle" font-family="{FONT}">圆包袱 · 啥都留一点</text>')
    dx4, dy4 = 852, top + 118
    s.append(f'<path d="M {dx4} {dy4-38} L {dx4+34} {dy4} L {dx4} {dy4+38} L {dx4-34} {dy4} Z" fill="none" stroke="{GREEN}" stroke-width="2.4"/>')
    for dx, dy in ((-10, 0), (8, -8)):
        s.append(f'<circle cx="{dx4+dx}" cy="{dy4+dy}" r="4" fill="{GREEN}"/>')
    for dx, dy in ((20, 16), (-24, 12), (4, 24)):
        s.append(f'<circle cx="{dx4+dx}" cy="{dy4+dy}" r="4" fill="none" stroke="#C9C2B4" stroke-width="1.6"/>')
        s.append(f'<line x1="{dx4+dx-3}" y1="{dy4+dy-3}" x2="{dx4+dx+3}" y2="{dy4+dy+3}" stroke="#C9C2B4" stroke-width="1.6"/>')
    s.append(f'<text x="{dx4}" y="{dy4+58}" font-size="11.5" fill="{MUTED}" text-anchor="middle" font-family="{FONT}">菱形箱 · 废话压成 0</text>')
    s.append('</svg>')
    return ''.join(s)


# --------------------------------------------------------------------------
# pic04 分诊台与折纸
# --------------------------------------------------------------------------
def pic04():
    import math, random
    s = [paper()]
    s.append(header(
        'ACT 4 · 西瓜书第 4 / 5 章',
        '第四幕 · 医院分诊台切豆腐，老奶奶折纸剪窗花',
        dialogue=True,
        tuanzi_text='两个弯月牙勾在一起，直线怎么都分不开，咋办？',
        lauju_text='有人横一刀竖一刀剁成方格；有人先把纸折好，再笔直一剪。'))

    top, ph = 176, 212
    rng = random.Random(11)
    m1, m2 = [], []
    for _ in range(24):
        t = math.pi * rng.random()
        m1.append((80 + 96 * math.cos(t) + rng.uniform(-3, 3), top + 128 - 58 * math.sin(t) + rng.uniform(-3, 3)))
        t2 = math.pi * rng.random()
        m2.append((176 + 96 * math.cos(t2) + rng.uniform(-3, 3), top + 158 - 58 * math.sin(t2) + rng.uniform(-3, 3)))

    s.append(panel(42, top, 288, ph, '①', '分诊台 · 横竖切', fill='#F6F6F9'))
    grid = ''
    for gx in range(5):
        grid += f'<line x1="{70+gx*58}" y1="{top+44}" x2="{70+gx*58}" y2="{top+196}" stroke="#D8D4E6" stroke-width="1.4"/>'
    for gy in range(4):
        grid += f'<line x1="{70}" y1="{top+44+gy*50}" x2="{302}" y2="{top+44+gy*50}" stroke="#D8D4E6" stroke-width="1.4"/>'
    s.append(grid)
    for px, py in m1:
        s.append(f'<circle cx="{px:.0f}" cy="{py:.0f}" r="3.6" fill="{RED}"/>')
    for px, py in m2:
        s.append(f'<circle cx="{px:.0f}" cy="{py:.0f}" r="3.6" fill="{BLUE}"/>')
    s.append(f'<text x="70" y="{top+200}" font-size="12" fill="#6A7080" font-family="{FONT}">只会顺着坐标轴剁：锯齿楼梯还切错。</text>')

    s.append(panel(356, top, 288, ph, '②', '老奶奶 · 先折后剪', fill='#FBF4F4'))
    fx, fy = 402, top + 52
    s.append(f'<rect x="{fx}" y="{fy}" width="196" height="112" rx="8" fill="#FBE9E4" stroke="#D9A9A0" stroke-width="1.6"/>')
    s.append(f'<path d="M {fx} {fy} L {fx+196} {fy+112}" stroke="#D9A9A0" stroke-width="1.4" stroke-dasharray="5 4"/>')
    s.append(f'<path d="M {fx+98} {fy} L {fx+98} {fy+112}" stroke="#D9A9A0" stroke-width="1.4" stroke-dasharray="5 4"/>')
    s.append(f'<path d="M {fx} {fy+56} L {fx+196} {fy+56}" stroke="#D9A9A0" stroke-width="1.4" stroke-dasharray="5 4"/>')
    s.append(f'<text x="{fx+98}" y="{fy+64}" font-size="12" fill="#B07066" text-anchor="middle" font-family="{FONT}">对折 · 再对折 · 抚平</text>')
    s.append(f'<path d="M {fx+210} {fy+28} l 26 20 -8 8 -26 -20 z" fill="#C9C2B4"/>')
    s.append(f'<circle cx="{fx+212}" cy="{fy+50}" r="4" fill="none" stroke="#8C8474" stroke-width="2.4"/>')
    s.append(f'<text x="384" y="{top+200}" font-size="12" fill="#6A7080" font-family="{FONT}">隐藏层折纸：把勾在一起的花样折到纸边上。</text>')

    s.append(panel(670, top, 288, ph, '③', '一刀开 · 窗花展开', fill='#F4F8F3'))
    cxx, cyy = 814, top + 118
    s.append(f'<line x1="{cxx-60}" y1="{cyy+34}" x2="{cxx+60}" y2="{cyy-6}" stroke="{INK}" stroke-width="2.4" stroke-dasharray="7 5"/>')
    for k in range(8):
        a = k * math.pi / 4
        px, py = cxx + 30 * math.cos(a), cyy - 4 + 26 * math.sin(a)
        s.append(f'<ellipse cx="{px:.0f}" cy="{py:.0f}" rx="16" ry="9" fill="#F3C9CD" stroke="#C98A94" stroke-width="1.4" transform="rotate({k*45} {px:.0f} {py:.0f})"/>')
    s.append(f'<circle cx="{cxx}" cy="{cyy-4}" r="9" fill="#FFFFFF" stroke="#C98A94" stroke-width="1.6"/>')
    s.append(f'<text x="698" y="{top+200}" font-size="12" fill="#6A7080" font-family="{FONT}">折好之后，一条直线分得干干净净。</text>')
    s.append(spark(340, 168))
    s.append('</svg>')
    return ''.join(s)


# --------------------------------------------------------------------------
# pic05 双黄线与颠铁锅
# --------------------------------------------------------------------------
def pic05():
    import random, math
    s = [paper()]
    s.append(header(
        'ACT 5 · 西瓜书第 6 章',
        '第五幕 · 马路中间画双黄线，大厨颠铁锅',
        dialogue=True,
        tuanzi_text='双黄线为什么只听最前排压线那几辆车的？',
        lauju_text='间隔要最宽；压线的车不动，后排全开走也不碍事。'))

    top, ph = 176, 212
    s.append(panel(42, top, 288, ph, '①', '最宽缓冲带 · 支持向量', fill='#F6F6F9'))
    s.append(f'<rect x="70" y="{top+44}" width="232" height="130" rx="10" fill="#F2F0E8"/>')
    for i in range(8):
        s.append(car(88 + i * 28, top + 72, RED, 0.9, ring=(2 <= i <= 4)))
    for i in range(8):
        s.append(car(88 + i * 28, top + 148, BLUE, 0.9, ring=(3 <= i <= 5)))
    s.append(f'<line x1="76" y1="{top+110}" x2="296" y2="{top+110}" stroke="{INK}" stroke-width="2.6"/>')
    s.append(f'<rect x="76" y="{top+92}" width="220" height="36" fill="{ACC}" opacity="0.14"/>')
    s.append(f'<line x1="76" y1="{top+92}" x2="296" y2="{top+92}" stroke="{ACC}" stroke-width="1.6" stroke-dasharray="5 4"/>')
    s.append(f'<line x1="76" y1="{top+128}" x2="296" y2="{top+128}" stroke="{ACC}" stroke-width="1.6" stroke-dasharray="5 4"/>')
    s.append(f'<text x="298" y="{top+66}" font-size="10.5" fill="#B77E36" text-anchor="end" font-family="{FONT}">金圈 = 压线车</text>')
    s.append(f'<text x="70" y="{top+196}" font-size="12" fill="#6A7080" font-family="{FONT}">后排车全部开回家，双黄线一毫米不动。</text>')

    s.append(panel(356, top, 288, ph, '②', '同心圆 · 分不开', fill='#FBF4F4'))
    ex, ey = 500, top + 118
    s.append(f'<ellipse cx="{ex}" cy="{ey}" rx="58" ry="50" fill="#F6EFE6" stroke="#D8CFC0" stroke-width="1.6"/>')
    s.append(f'<circle cx="{ex}" cy="{ey}" r="17" fill="{GREEN}"/>')
    for k in range(14):
        a = k * 2 * math.pi / 14
        s.append(f'<circle cx="{ex+40*math.cos(a):.0f}" cy="{ey+34*math.sin(a):.0f}" r="5.6" fill="{RED}"/>')
    s.append(f'<line x1="{ex-70}" y1="{ey-58}" x2="{ex+70}" y2="{ey+58}" stroke="{INK}" stroke-width="2" stroke-dasharray="6 5" opacity="0.3"/>')
    s.append(f'<text x="{ex}" y="{top+196}" font-size="12" fill="#6A7080" font-family="{FONT}">绿豆坐锅底，花生皮围外圈。</text>')

    s.append(panel(670, top, 288, ph, '③', '猛一颠 · 升维切开', fill='#F4F8F3'))
    fx, fy = 814, top + 120
    s.append(f'<ellipse cx="{fx}" cy="{fy+38}" rx="58" ry="14" fill="none" stroke="{GREEN}" stroke-width="2.6"/>')
    s.append(f'<ellipse cx="{fx}" cy="{fy+38}" rx="30" ry="7" fill="{GREEN}" opacity="0.35"/>')
    for k in range(14):
        a = k * 2 * math.pi / 14
        px, py = fx + 44 * math.cos(a), fy + 38 + 10 * math.sin(a)
        lift = 70 - 24 * math.sin(a) - 10 * math.cos(a) ** 2
        s.append(f'<line x1="{px:.0f}" y1="{py:.0f}" x2="{px:.0f}" y2="{py-lift:.0f}" stroke="#E0D8C8" stroke-width="1.2"/>')
        s.append(f'<circle cx="{px:.0f}" cy="{py-lift:.0f}" r="5.4" fill="{RED}"/>')
    s.append(f'<circle cx="{fx}" cy="{fy+38}" r="6" fill="{GREEN}"/>')
    s.append(f'<line x1="{fx-64}" y1="{fy+30}" x2="{fx+64}" y2="{fy+46}" stroke="{INK}" stroke-width="2.2"/>')
    s.append(f'<text x="{fx}" y="{top+196}" font-size="12" fill="#6A7080" font-family="{FONT}">一颠升空，硬纸板横插即分家。</text>')
    s.append(spark(650, 168))
    s.append('</svg>')
    return ''.join(s)


# --------------------------------------------------------------------------
# pic06 评委团与木匠
# --------------------------------------------------------------------------
def pic06():
    import random, math
    s = [paper()]
    s.append(header(
        'ACT 6 · 西瓜书第 8 章',
        '第六幕 · 歌手大赛评委团，木匠师徒接力',
        dialogue=True,
        tuanzi_text='找人商量，是各打各的求平均，还是排流水线补差价？',
        lauju_text='各治一种病：求平均消手抖，补差价消毛坯。'))

    top, ph = 176, 212
    rng = random.Random(9)
    s.append(panel(42, top, 288, ph, '①', '评委团 · 求平均降方差', fill='#F6F6F9'))
    base = top + 116
    for i in range(13):
        yy = base - 40 + rng.uniform(-24, 24)
        xx = 76 + i * 18
        s.append(f'<line x1="{xx}" y1="{base+30}" x2="{xx}" y2="{yy:.0f}" stroke="#B9C7E2" stroke-width="1.6"/>')
        s.append(f'<circle cx="{xx}" cy="{yy:.0f}" r="4" fill="{BLUE}" opacity="0.7"/>')
    s.append(f'<line x1="70" y1="{base+30}" x2="302" y2="{base+30}" stroke="#C9C2B4" stroke-width="1.4"/>')
    s.append(f'<path d="M 70 {base+18} Q 150 {base+6} 230 {base+16} T 302 {base+14}" fill="none" stroke="{INK}" stroke-width="2.6"/>')
    s.append(f'<text x="70" y="{top+186}" font-size="12" fill="#6A7080" font-family="{FONT}">浅柱是各评委的手抖分，粗线是平均：稳。</text>')

    s.append(panel(356, top, 288, ph, '②', '师徒接力 · 补差价', fill='#FBF4F4'))
    steps = [('大徒弟 · 斧头', 60, RED), ('二徒弟 · 木刨', 30, ORANGE), ('老师傅 · 砂纸', 10, GREEN)]
    for i, (name, pts, c) in enumerate(steps):
        yy = top + 60 + i * 46
        s.append(f'<rect x="384" y="{yy}" width="150" height="34" rx="10" fill="{c}" opacity="0.16"/>')
        s.append(f'<circle cx="404" cy="{yy+17}" r="9" fill="{c}"/>')
        s.append(f'<text x="420" y="{yy+22}" font-size="12.5" fill="#565D6E" font-family="{FONT}">{name}</text>')
        s.append(f'<text x="546" y="{yy+22}" font-size="13" fill="{c}" font-family="{FONT}" font-weight="600">+{pts} 分</text>')
    s.append(f'<text x="384" y="{top+196}" font-size="12.5" fill="{ACC}" font-family="{FONT}" font-weight="600">60 + 30 + 10 = 100 分，毛坯步步变精品。</text>')

    s.append(panel(670, top, 288, ph, '③', '残差 · 一棒比一棒小', fill='#F4F8F3'))
    bx6, by6, bw6, bh6 = 700, top + 46, 226, 68
    s.append(f'<line x1="{bx6}" y1="{by6+bh6}" x2="{bx6+bw6}" y2="{by6+bh6}" stroke="#CFC8BA" stroke-width="1.5"/>')
    path1 = f'M {bx6} {by6+bh6-8} ' + ' '.join(
        f'L {bx6+8+i*8:.0f} {by6+bh6-8-(18+24*math.sin(i*0.9))*rng.uniform(0.75,1.25):.0f}' for i in range(27))
    s.append(f'<path d="{path1}" fill="none" stroke="{RED}" stroke-width="2.2" stroke-linecap="round"/>')
    s.append(f'<text x="{bx6+bw6}" y="{by6-4}" font-size="11" fill="{RED}" text-anchor="end" font-family="{FONT}">+40 粗坯</text>')
    by7 = by6 + bh6 + 16
    s.append(f'<line x1="{bx6}" y1="{by7+34}" x2="{bx6+bw6}" y2="{by7+34}" stroke="#CFC8BA" stroke-width="1.5"/>')
    path2 = f'M {bx6} {by7+34} ' + ' '.join(
        f'L {bx6+8+i*8:.0f} {by7+34-(3+5*math.sin(i*1.7)):.0f}' for i in range(27))
    s.append(f'<path d="{path2}" fill="none" stroke="{GREEN}" stroke-width="2.2" stroke-linecap="round"/>')
    s.append(f'<text x="{bx6+bw6}" y="{by7+26}" font-size="11" fill="{GREEN}" text-anchor="end" font-family="{FONT}">+10 毛刺</text>')
    s.append(f'<text x="698" y="{top+196}" font-size="12" fill="#6A7080" font-family="{FONT}">拟合残差就是专门修坑，坑越修越小。</text>')
    s.append(spark(650, 168))
    s.append('</svg>')
    return ''.join(s)


# --------------------------------------------------------------------------
# pic07 体操队与橡皮筋
# --------------------------------------------------------------------------
def pic07():
    import random
    s = [paper()]
    s.append(header(
        'ACT 7 · 西瓜书第 9 章',
        '第七幕 · 开学第一天，操场分队风波',
        dialogue=True,
        tuanzi_text='没校服没名牌，电脑怎么把两个班分开？',
        lauju_text='圆规只会画正圆；会拉橡皮筋的才认得细长横队。'))

    top, ph = 176, 212
    rng = random.Random(21)
    rowA = [(80 + rng.uniform(-52, 52), top + 96 + rng.uniform(-7, 7)) for _ in range(20)]
    rowB = [(80 + rng.uniform(-52, 52), top + 160 + rng.uniform(-7, 7)) for _ in range(20)]

    s.append(panel(42, top, 288, ph, '①', '两列细长横队 · 没标签', fill='#F6F6F9'))
    for px, py in rowA:
        s.append(f'<circle cx="{px:.0f}" cy="{py:.0f}" r="4" fill="{RED}"/>')
    for px, py in rowB:
        s.append(f'<circle cx="{px:.0f}" cy="{py:.0f}" r="4" fill="{BLUE}"/>')
    s.append(f'<text x="70" y="{top+196}" font-size="12" fill="#6A7080" font-family="{FONT}">一班横着一排，二班也横着一排。</text>')

    rowA2 = [(px + 314, py) for px, py in rowA]
    rowB2 = [(px + 314, py) for px, py in rowB]
    rowA3 = [(px + 628, py) for px, py in rowA]
    rowB3 = [(px + 628, py) for px, py in rowB]

    s.append(panel(356, top, 288, ph, '②', '圆规画正圆 · 切错', fill='#FBF4F4'))
    for px, py in rowA2:
        s.append(f'<circle cx="{px:.0f}" cy="{py:.0f}" r="4" fill="{RED}"/>')
    for px, py in rowB2:
        s.append(f'<circle cx="{px:.0f}" cy="{py:.0f}" r="4" fill="{BLUE}"/>')
    s.append(f'<circle cx="394" cy="{top+96}" r="26" fill="none" stroke="{INK}" stroke-width="2.2"/>')
    s.append(f'<circle cx="464" cy="{top+160}" r="26" fill="none" stroke="{INK}" stroke-width="2.2"/>')
    s.append(f'<line x1="376" y1="{top+128}" x2="616" y2="{top+128}" stroke="{RED}" stroke-width="2.2" stroke-dasharray="6 5"/>')
    s.append(f'<text x="384" y="{top+196}" font-size="12" fill="#6A7080" font-family="{FONT}">正圆只认半径：两列队被拦腰劈成四段。</text>')

    s.append(panel(670, top, 288, ph, '③', '顺着队形 · 拉椭圆', fill='#F4F8F3'))
    for px, py in rowA3:
        s.append(f'<circle cx="{px:.0f}" cy="{py:.0f}" r="4" fill="{RED}"/>')
    for px, py in rowB3:
        s.append(f'<circle cx="{px:.0f}" cy="{py:.0f}" r="4" fill="{BLUE}"/>')
    s.append(f'<ellipse cx="708" cy="{top+96}" rx="64" ry="17" fill="none" stroke="{RED}" stroke-width="2.6"/>')
    s.append(f'<ellipse cx="708" cy="{top+160}" rx="64" ry="17" fill="none" stroke="{BLUE}" stroke-width="2.6"/>')
    s.append(f'<text x="698" y="{top+196}" font-size="12" fill="#6A7080" font-family="{FONT}">E 步猜人，M 步拉筋：14 轮严丝合缝。</text>')
    s.append(spark(650, 168))
    s.append('</svg>')
    return ''.join(s)


# --------------------------------------------------------------------------
# pic08 后厨传菜签
# --------------------------------------------------------------------------
def pic08():
    s = [paper()]
    s.append(header(
        'ACT 8 · 反向传播与自动求导',
        '第八幕 · 大饭店后厨，顺着传菜签倒查咸汤',
        dialogue=True,
        tuanzi_text='上百亿个旋钮，错了怎么一眨眼知道每个往哪拧？',
        lauju_text='每道工序记一笔局部倍数，从装盘工往回查一趟。'))

    top, ph = 176, 212
    s.append(panel(42, top, 288, ph, '①', '前向 · 做菜', fill='#F6F6F9'))
    stations = [('放盐 ×2', 84), ('高汤 +1', 156), ('装盘 ÷10', 228)]
    for name, sx in stations:
        s.append(f'<rect x="{sx}" y="{top+48}" width="66" height="40" rx="10" fill="{ACC}" opacity="0.14"/>')
        s.append(f'<text x="{sx+33}" y="{top+72}" font-size="11.5" fill="{ACC}" text-anchor="middle" font-family="{FONT}" font-weight="600">{name}</text>')
    s.append(f'<line x1="150" y1="{top+68}" x2="154" y2="{top+68}" stroke="{ACC}" stroke-width="2.2" stroke-linecap="round"/>')
    s.append(f'<line x1="222" y1="{top+68}" x2="226" y2="{top+68}" stroke="{ACC}" stroke-width="2.2" stroke-linecap="round"/>')
    s.append(f'<text x="70" y="{top+130}" font-size="12" fill="#6A7080" font-family="{FONT}">菜往前传：盐量 ×2，加汤底，装盘 ÷10。</text>')
    s.append(f'<text x="70" y="{top+152}" font-size="12" fill="#6A7080" font-family="{FONT}">传菜签上，每道工序都记下自己的倍数。</text>')
    s.append(f'<text x="70" y="{top+186}" font-size="12" fill="{ACC}" font-family="{FONT}" font-weight="600">这张签，就是「计算图」。</text>')

    s.append(panel(356, top, 288, ph, '②', '店长尝汤 · 太咸啦', fill='#FBF4F4'))
    bx, by = 470, top + 96
    s.append(f'<path d="M {bx-34} {by} q 0 34 34 34 q 34 0 34 -34 z" fill="#FFFFFF" stroke="#B9B0A0" stroke-width="2.4"/>')
    s.append(f'<ellipse cx="{bx}" cy="{by}" rx="34" ry="8" fill="#E8DFC9" stroke="#B9B0A0" stroke-width="1.6"/>')
    for k in range(3):
        s.append(f'<path d="M {bx-12+k*11} {by-14} q 3 -7 0 -12" fill="none" stroke="#C9C2B4" stroke-width="1.6" stroke-linecap="round"/>')
    s.append(cat(566, by + 6, 26, 'laoju', 'smile'))
    s.append(f'<text x="500" y="{by+66}" font-size="12" fill="{RED}" font-family="{FONT}" font-weight="600">要求 0.5，实测 0.76 —— 咸了！</text>')
    s.append(f'<text x="384" y="{top+186}" font-size="12" fill="#6A7080" font-family="{FONT}">笨办法让 100 个厨师挨个重做；聪明只查一趟。</text>')

    s.append(panel(670, top, 288, ph, '③', '反向 · 顺签倒查', fill='#F4F8F3'))
    gy = top + 84
    nodes = [('装盘 ÷10', 722), ('高汤 +1', 796), ('放盐 ×2', 872)]
    for i, (name, nx) in enumerate(nodes):
        s.append(f'<circle cx="{nx}" cy="{gy}" r="20" fill="#FFFFFF" stroke="{ORANGE if i == 2 else ACC}" stroke-width="2.2"/>')
        s.append(f'<text x="{nx}" y="{gy+4}" font-size="9.5" fill="#565D6E" text-anchor="middle" font-family="{FONT}">{name}</text>')
        if i < 2:
            x1 = nx + 21
            x2 = nodes[i + 1][1] - 21
            s.append(f'<line x1="{x1}" y1="{gy}" x2="{x2}" y2="{gy}" stroke="{ORANGE}" stroke-width="2"/>')
            s.append(f'<path d="M {x2} {gy} l -6 -4 v 8 z" fill="{ORANGE}"/>')
    s.append(f'<text x="797" y="{gy-30}" font-size="10.5" fill="{MUTED}" text-anchor="middle" font-family="{FONT}">局部导数沿签连乘（链式法则）</text>')
    s.append(f'<rect x="700" y="{gy+36}" width="216" height="30" rx="9" fill="{RED}" opacity="0.12"/>')
    s.append(f'<text x="808" y="{gy+56}" font-size="12" fill="{RED}" text-anchor="middle" font-family="{FONT}" font-weight="600">抓到 2 号师傅：dL/dx = -0.096</text>')
    s.append(f'<text x="698" y="{top+186}" font-size="12" fill="#6A7080" font-family="{FONT}">负号的意思：盐放多了，往回拧。</text>')
    s.append(spark(650, 168))
    s.append('</svg>')
    return ''.join(s)


BUILDERS = {1: pic01, 2: pic02, 3: pic03, 4: pic04, 5: pic05, 6: pic06, 7: pic07, 8: pic08}

if __name__ == '__main__':
    import sys
    nums = [int(a) for a in sys.argv[1:]] or list(BUILDERS)
    for n in nums:
        svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 410" font-family="sans-serif">' + BUILDERS[n]() 
        out = os.path.join(ASSETS, f'pic{n:02d}-new.svg')
        with open(out, 'w', encoding='utf-8') as f:
            f.write(svg)
        print('written', out)
