# -*- coding: utf-8 -*-
"""
《小猫团子与老橘师傅的夜话：用生活常识串起西瓜书与深度学习》
生成 8 张猫咪师徒对话 + 日常生活例子的卡通 SVG 插画 (pic01 ~ pic08.svg)
"""
import os
import xml.etree.ElementTree as ET

ROOT = r'C:\Users\34684\Documents\notes-for-deep-learniung'
ASSETS = os.path.join(ROOT, 'assets')
os.makedirs(ASSETS, exist_ok=True)


def cat_avatar(cx, cy, r=28, role="laoju"):
    """
    绘制固定双主角猫咪头像：
    - role="tuanzi" (小猫团子：奶油白小猫，圆溜溜大眼睛，头顶小呆毛，负责好奇发问)
    - role="laoju"  (老橘师傅：暖橘色虎斑猫，戴小草帽/眼镜，温和笑眼，负责举生活例子解答)
    """
    if role == "tuanzi":
        fur, stroke, inner = "#FFF7ED", "#9A3412", "#FDA4AF"
    else:
        fur, stroke, inner = "#FB923C", "#9A3412", "#FDBA74"

    ear_l = f"{cx-int(r*0.85)},{cy-int(r*0.45)} {cx-int(r*0.95)},{cy-int(r*1.25)} {cx-int(r*0.25)},{cy-int(r*0.82)}"
    ear_r = f"{cx+int(r*0.85)},{cy-int(r*0.45)} {cx+int(r*0.95)},{cy-int(r*1.25)} {cx+int(r*0.25)},{cy-int(r*0.82)}"
    in_l = f"{cx-int(r*0.75)},{cy-int(r*0.55)} {cx-int(r*0.82)},{cy-int(r*1.08)} {cx-int(r*0.35)},{cy-int(r*0.78)}"
    in_r = f"{cx+int(r*0.75)},{cy-int(r*0.55)} {cx+int(r*0.82)},{cy-int(r*1.08)} {cx+int(r*0.35)},{cy-int(r*0.78)}"

    parts = [
        f'<polygon points="{ear_l}" fill="{fur}" stroke="{stroke}" stroke-width="2.5" stroke-linejoin="round"/>',
        f'<polygon points="{ear_r}" fill="{fur}" stroke="{stroke}" stroke-width="2.5" stroke-linejoin="round"/>',
        f'<polygon points="{in_l}" fill="{inner}"/>',
        f'<polygon points="{in_r}" fill="{inner}"/>',
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fur}" stroke="{stroke}" stroke-width="2.5"/>',
    ]

    ey = cy - int(r * 0.12)
    ex = int(r * 0.38)
    if role == "tuanzi":
        # 水汪汪好奇大眼睛
        parts.append(f'<circle cx="{cx-ex}" cy="{ey}" r="5.2" fill="#1E293B"/>')
        parts.append(f'<circle cx="{cx+ex}" cy="{ey}" r="5.2" fill="#1E293B"/>')
        parts.append(f'<circle cx="{cx-ex-1.8}" cy="{ey-1.8}" r="2.0" fill="#FFFFFF"/>')
        parts.append(f'<circle cx="{cx+ex-1.8}" cy="{ey-1.8}" r="2.0" fill="#FFFFFF"/>')
        # 小呆毛
        parts.append(f'<path d="M {cx} {cy-r} Q {cx+6} {cy-r-10} {cx+12} {cy-r-4}" fill="none" stroke="{stroke}" stroke-width="2.5" stroke-linecap="round"/>')
    else:
        # 老橘师傅额头虎斑纹 + 圆框眼镜
        parts.append(f'<line x1="{cx}" y1="{cy-r+3}" x2="{cx}" y2="{cy-int(r*0.55)}" stroke="{stroke}" stroke-width="3" stroke-linecap="round"/>')
        parts.append(f'<line x1="{cx-6}" y1="{cy-r+5}" x2="{cx-4}" y2="{cy-int(r*0.6)}" stroke="{stroke}" stroke-width="2.2" stroke-linecap="round"/>')
        parts.append(f'<line x1="{cx+6}" y1="{cy-r+5}" x2="{cx+4}" y2="{cy-int(r*0.6)}" stroke="{stroke}" stroke-width="2.2" stroke-linecap="round"/>')
        parts.append(f'<circle cx="{cx-ex}" cy="{ey}" r="4.2" fill="#1E293B"/>')
        parts.append(f'<circle cx="{cx+ex}" cy="{ey}" r="4.2" fill="#1E293B"/>')
        parts.append(f'<circle cx="{cx-ex}" cy="{ey}" r="8.5" fill="none" stroke="#78350F" stroke-width="2"/>')
        parts.append(f'<circle cx="{cx+ex}" cy="{ey}" r="8.5" fill="none" stroke="#78350F" stroke-width="2"/>')
        parts.append(f'<line x1="{cx-ex+8.5}" y1="{ey}" x2="{cx+ex-8.5}" y2="{ey}" stroke="#78350F" stroke-width="2"/>')

    ny = cy + int(r * 0.14)
    parts.append(f'<polygon points="{cx-4},{ny} {cx+4},{ny} {cx},{ny+5}" fill="#F43F5E"/>')
    parts.append(f'<path d="M {cx-7} {ny+7} Q {cx-3.5} {ny+11} {cx} {ny+6} Q {cx+3.5} {ny+11} {cx+7} {ny+7}" fill="none" stroke="#1E293B" stroke-width="2" stroke-linecap="round"/>')
    for dy in [-3, 3]:
        parts.append(f'<line x1="{cx-int(r*0.55)}" y1="{ny+dy}" x2="{cx-int(r*1.05)}" y2="{ny+dy*2}" stroke="#64748B" stroke-width="1.6" stroke-linecap="round"/>')
        parts.append(f'<line x1="{cx+int(r*0.55)}" y1="{ny+dy}" x2="{cx+int(r*1.05)}" y2="{ny+dy*2}" stroke="#64748B" stroke-width="1.6" stroke-linecap="round"/>')
    return "\n".join(parts)


def dialogue_bar(q_text, a_text):
    """顶部固定师徒一问一答对话条，把上一章与这一章的知识顺畅串起来"""
    return f'''
  <rect x="24" y="16" width="952" height="78" rx="16" fill="#FEF3C7" stroke="#F59E0B" stroke-width="2"/>
  {cat_avatar(62, 55, r=23, role="tuanzi")}
  <text x="100" y="42" font-size="14.5" font-weight="bold" fill="#92400E">团子问：“{q_text}”</text>
  {cat_avatar(938, 55, r=23, role="laoju")}
  <text x="100" y="74" font-size="14.5" font-weight="bold" fill="#B45309">老橘答：“{a_text}”</text>
'''


def save_svg(name, content):
    path = os.path.join(ASSETS, name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip())
    ET.parse(path)
    print("Saved valid SVG:", name)


# ==============================================================================
# 第 1 幕：从菜场挑西瓜与医院看病说起（什么是特征、标签与模型？）
# ==============================================================================
save_svg('pic01-watermelon-stall.svg', f'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 410" width="100%" height="auto" font-family="Microsoft YaHei, PingFang SC, sans-serif">
  <rect width="1000" height="410" rx="22" fill="#FFFBEB" stroke="#F59E0B" stroke-width="3"/>
  {dialogue_bar(
      "老橘师傅，电脑既没有舌头也没见过西瓜，怎么猜出瓜甜不甜、邮件是不是广告呀？",
      "就像咱们去菜场买菜或医生看病！不用真咬一口，先把能看到的【日常线索】列成表格就行啦！"
  )}

  <g transform="translate(28, 110)">
    <rect width="296" height="276" rx="18" fill="#ECFDF5" stroke="#6EE7B7" stroke-width="2.5"/>
    <text x="148" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#065F46">① 生活中的观察线索（叫特征）</text>
    <circle cx="148" cy="138" r="58" fill="#22C55E" stroke="#15803D" stroke-width="3.5"/>
    <path d="M 120 86 Q 105 138 120 190" fill="none" stroke="#14532D" stroke-width="6" stroke-linecap="round"/>
    <path d="M 148 80 Q 135 138 148 196" fill="none" stroke="#14532D" stroke-width="6" stroke-linecap="round"/>
    <path d="M 176 86 Q 191 138 176 190" fill="none" stroke="#14532D" stroke-width="6" stroke-linecap="round"/>
    <text x="148" y="224" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#047857">挑西瓜看：外皮颜色、瓜蒂弯度、拍声</text>
    <text x="148" y="248" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#047857">挑房子看：面积大小、离地铁几分钟</text>
  </g>

  <g transform="translate(352, 110)">
    <rect width="296" height="276" rx="18" fill="#EFF6FF" stroke="#93C5FD" stroke-width="2.5"/>
    <text x="148" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#1E3A8A">② 过去的经验账本（叫训练集）</text>
    <rect x="22" y="48" width="252" height="54" rx="10" fill="#FFFFFF" stroke="#60A5FA" stroke-width="2"/>
    <text x="148" y="72" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#1E293B">1号瓜：青绿 + 蜷缩 + 清脆 ➔ 甜瓜 ✓</text>
    <text x="148" y="92" text-anchor="middle" font-size="12" fill="#64748B">（切开尝过的结果就叫“标签 y”）</text>

    <rect x="22" y="114" width="252" height="54" rx="10" fill="#FFFFFF" stroke="#60A5FA" stroke-width="2"/>
    <text x="148" y="138" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#1E293B">2号瓜：乌黑 + 蜷缩 + 清脆 ➔ 甜瓜 ✓</text>
    <text x="148" y="158" text-anchor="middle" font-size="12" fill="#64748B">（攒下 100 条真实记录给电脑看）</text>

    <rect x="22" y="180" width="252" height="74" rx="10" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="2"/>
    <text x="148" y="206" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#991B1B">3号瓜：浅白 + 硬挺 + 闷响 ➔ 生瓜 ✗</text>
    <text x="148" y="232" text-anchor="middle" font-size="13" font-weight="bold" fill="#DC2626">电脑的任务：从旧账本里摸清套路！</text>
  </g>

  <g transform="translate(676, 110)">
    <rect width="296" height="276" rx="18" fill="#FAF5FF" stroke="#D8B4FE" stroke-width="2.5"/>
    <text x="148" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#6B21A8">③ 总结出的经验公式（叫模型）</text>
    <rect x="24" y="52" width="248" height="128" rx="14" fill="#FFFFFF" stroke="#C084FC" stroke-width="2"/>
    <text x="148" y="84" text-anchor="middle" font-size="15" font-weight="bold" fill="#7E22CE">电脑自己悟出的打分卡：</text>
    <text x="148" y="114" text-anchor="middle" font-size="14" font-weight="bold" fill="#1E293B">总甜度 = 0.5×听声音 + 0.3×看瓜蒂</text>
    <text x="148" y="140" text-anchor="middle" font-size="14" font-weight="bold" fill="#1E293B">          + 0.2×看颜色</text>
    <text x="148" y="166" text-anchor="middle" font-size="12.5" fill="#64748B">（调整前面的比重数字，就叫“训练”）</text>
    <rect x="24" y="194" width="248" height="62" rx="12" fill="#F3E8FF" stroke="#A855F7" stroke-width="2"/>
    <text x="148" y="220" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#581C87">以后遇到没切开的新瓜，套进打分卡</text>
    <text x="148" y="242" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#581C87">一算就知道甜不甜，这就叫机器学习！</text>
  </g>
</svg>
''')


# ==============================================================================
# 第 2 幕：期末考试复习的三种境界（欠拟合、过拟合与泛化）
# ==============================================================================
save_svg('pic02-three-apprentices.svg', f'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 410" width="100%" height="auto" font-family="Microsoft YaHei, PingFang SC, sans-serif">
  <rect width="1000" height="410" rx="22" fill="#F8FAFC" stroke="#94A3B8" stroke-width="3"/>
  {dialogue_bar(
      "师傅，那我让电脑把过去 100 道旧题背得一字不差，明天考新题是不是就能拿满分啦？",
      "千万别！你想想咱们期末考试复习：连模拟卷上的苍蝇墨点都死背下来的人，上考场最容易考砸！"
  )}

  <g transform="translate(28, 110)">
    <rect width="296" height="276" rx="18" fill="#F1F5F9" stroke="#94A3B8" stroke-width="2.5"/>
    <text x="148" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#334155">① 偷懒只背“全选C”（欠拟合）</text>
    <rect x="24" y="48" width="248" height="128" rx="12" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <circle cx="55" cy="150" r="8" fill="#22C55E"/><circle cx="95" cy="105" r="8" fill="#22C55E"/>
    <circle cx="148" cy="78" r="8" fill="#22C55E"/><circle cx="200" cy="102" r="8" fill="#22C55E"/>
    <circle cx="240" cy="148" r="8" fill="#22C55E"/>
    <line x1="35" y1="132" x2="260" y2="112" stroke="#64748B" stroke-width="5" stroke-linecap="round"/>
    <rect x="20" y="190" width="256" height="72" rx="10" fill="#FFFFFF" stroke="#94A3B8" stroke-width="2"/>
    <text x="148" y="216" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#475569">生活例子：复习时连课本都不翻，</text>
    <text x="148" y="238" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#475569">不管什么题都一条直线蒙到底。</text>
    <text x="148" y="256" text-anchor="middle" font-size="13" font-weight="bold" fill="#DC2626">毛病：脑筋太死板（偏差 Bias 太高）</text>
  </g>

  <g transform="translate(352, 110)">
    <rect width="296" height="276" rx="18" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="2.5"/>
    <text x="148" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#991B1B">② 连试卷墨水点都死背（过拟合）</text>
    <rect x="24" y="48" width="248" height="128" rx="12" fill="#FFFFFF" stroke="#FECACA" stroke-width="2"/>
    <circle cx="55" cy="150" r="8" fill="#22C55E"/><circle cx="95" cy="105" r="8" fill="#22C55E"/>
    <circle cx="148" cy="78" r="8" fill="#22C55E"/>
    <circle cx="195" cy="156" r="9" fill="#B45309"/>
    <text x="195" y="171" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#92400E">印刷蹭的脏墨点</text>
    <circle cx="240" cy="148" r="8" fill="#22C55E"/>
    <path d="M 40 165 L 55 150 L 75 65 L 95 105 L 148 78 L 172 62 L 195 156 L 220 66 L 240 148" fill="none" stroke="#EF4444" stroke-width="3.8" stroke-linejoin="round"/>
    <rect x="20" y="190" width="256" height="72" rx="10" fill="#FFFFFF" stroke="#F87171" stroke-width="2"/>
    <text x="148" y="216" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#B91C1C">生活例子：背熟“第3题有脏墨点选B”，</text>
    <text x="148" y="238" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#B91C1C">模拟卷考100分，期末换新卷全错！</text>
    <text x="148" y="256" text-anchor="middle" font-size="13" font-weight="bold" fill="#B45309">毛病：死抠偶然噪点（方差 Var 爆炸）</text>
  </g>

  <g transform="translate(676, 110)">
    <rect width="296" height="276" rx="18" fill="#ECFDF5" stroke="#6EE7B7" stroke-width="2.5"/>
    <text x="148" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#065F46">③ 吃透解题大套路（恰当泛化）</text>
    <rect x="24" y="48" width="248" height="128" rx="12" fill="#FFFFFF" stroke="#A7F3D0" stroke-width="2"/>
    <circle cx="55" cy="150" r="8" fill="#22C55E"/><circle cx="95" cy="105" r="8" fill="#22C55E"/>
    <circle cx="148" cy="78" r="8" fill="#22C55E"/>
    <circle cx="195" cy="156" r="7" fill="#CBD5E1"/>
    <text x="195" y="140" text-anchor="middle" font-size="10.5" fill="#64748B">自动忽略脏墨点</text>
    <circle cx="240" cy="148" r="8" fill="#22C55E"/>
    <path d="M 45 156 Q 148 18 250 154" fill="none" stroke="#16A34A" stroke-width="5" stroke-linecap="round"/>
    <rect x="20" y="190" width="256" height="72" rx="10" fill="#FFFFFF" stroke="#34D399" stroke-width="2"/>
    <text x="148" y="216" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#047857">生活例子：看懂题目背后的真正规律，</text>
    <text x="148" y="238" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#047857">主动忽略印刷错字，考新题照样高分！</text>
    <text x="148" y="256" text-anchor="middle" font-size="13" font-weight="bold" fill="#15803D">黄金法则：抓大趋势、放过小杂音！</text>
  </g>
</svg>
''')


# ==============================================================================
# 第 3 幕：平均工资被富翁拉高 & 搬家收行李箱（L2 vs L1 损失与 Lasso 断舍离）
# ==============================================================================
save_svg('pic03-gold-watermelon-scale.svg', f'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 410" width="100%" height="auto" font-family="Microsoft YaHei, PingFang SC, sans-serif">
  <rect width="1000" height="410" rx="22" fill="#FFFBEB" stroke="#F59E0B" stroke-width="3"/>
  {dialogue_bar(
      "师傅，那怎么让电脑别被那种‘印刷脏墨点’或者个别离谱的异常数据带偏呢？",
      "这就要选对算分尺子啦！你想想‘全班平均工资被首富拉高’和‘搬家收行李箱断舍离’这两个生活例子！"
  )}

  <g transform="translate(28, 110)">
    <rect width="460" height="276" rx="18" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="2.5"/>
    <text x="230" y="32" text-anchor="middle" font-size="16" font-weight="bold" fill="#991B1B">① 例子A：全班月薪5千，转来个亿万富翁！</text>
    <polygon points="210,196 250,196 230,158" fill="#64748B"/>
    <line x1="60" y1="118" x2="400" y2="184" stroke="#475569" stroke-width="7" stroke-linecap="round"/>
    <circle cx="105" cy="108" r="15" fill="#3B82F6"/><circle cx="145" cy="116" r="15" fill="#3B82F6"/><circle cx="185" cy="124" r="15" fill="#3B82F6"/>
    <text x="145" y="84" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#1D4ED8">9个普通同学：月薪5千</text>
    <circle cx="355" cy="138" r="32" fill="#FACC15" stroke="#CA8A04" stroke-width="3.5"/>
    <text x="355" y="143" text-anchor="middle" font-size="13" font-weight="bold" fill="#713F12">首富1亿!</text>

    <rect x="20" y="206" width="420" height="58" rx="10" fill="#FFFFFF" stroke="#F87171" stroke-width="2"/>
    <text x="230" y="229" text-anchor="middle" font-size="13" font-weight="bold" fill="#B91C1C">• 平方误差（L2，像算平均数）：被首富一把拉到“人均月薪一千万”！</text>
    <text x="230" y="251" text-anchor="middle" font-size="13" font-weight="bold" fill="#15803D">• 绝对值误差（L1，像排队看正中间的中位数）：中间同学还是稳稳5千！</text>
  </g>

  <g transform="translate(512, 110)">
    <rect width="460" height="276" rx="18" fill="#ECFDF5" stroke="#6EE7B7" stroke-width="2.5"/>
    <text x="230" y="32" text-anchor="middle" font-size="16" font-weight="bold" fill="#065F46">② 例子B：搬家只有一个小行李箱，怎么扔废话线索？</text>
    <rect x="24" y="52" width="412" height="68" rx="10" fill="#FFFFFF" stroke="#93C5FD" stroke-width="2"/>
    <text x="230" y="76" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#1E40AF">囤积癖整理法（L2 岭回归 Ridge：圆球约束）</text>
    <text x="230" y="102" text-anchor="middle" font-size="12.5" fill="#475569">啥旧玩意儿都舍不得扔！把 10 件衣服全缩成迷你小号塞进箱子，全留着小尾巴。</text>

    <rect x="24" y="132" width="412" height="128" rx="10" fill="#FFFFFF" stroke="#6EE7B7" stroke-width="2"/>
    <text x="230" y="156" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#065F46">断舍离整理法（L1 稀疏 Lasso：菱形尖角约束）</text>
    <text x="230" y="180" text-anchor="middle" font-size="12.5" fill="#047857">只留 2 件天天穿的真宝贝，把剩下 8 件三年不穿的噱头衣服直接清零扔掉！</text>
    <rect x="52" y="196" width="105" height="34" rx="8" fill="#DCFCE7" stroke="#16A34A" stroke-width="2"/>
    <text x="104" y="218" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#15803D">✓ 留：太阳日照</text>
    <rect x="176" y="196" width="110" height="34" rx="8" fill="#FEE2E2" stroke="#EF4444" stroke-width="2"/>
    <text x="231" y="218" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#DC2626">✗ 扔：老板星座=0</text>
    <rect x="304" y="196" width="110" height="34" rx="8" fill="#FEE2E2" stroke="#EF4444" stroke-width="2"/>
    <text x="359" y="218" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#DC2626">✗ 扔：货车尾号=0</text>
  </g>
</svg>
''')


# ==============================================================================
# 第 4 幕：医院挂号分诊台 vs. 把折纸抚平一刀剪（决策树 vs. 神经网络）
# ==============================================================================
save_svg('pic04-tofu-knife-vs-magic-dough.svg', f'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 410" width="100%" height="auto" font-family="Microsoft YaHei, PingFang SC, sans-serif">
  <rect width="1000" height="410" rx="22" fill="#F8FAFC" stroke="#94A3B8" stroke-width="3"/>
  {dialogue_bar(
      "师傅，要是生活中很多事不是直线呢？比如泡面水温太低泡不熟、太高又泡烂了，怎么判断呀？",
      "遇到这种拐弯的事，人类想出了两招：一招像医院分诊台连环问问题，另一招像折纸剪窗花！"
  )}

  <g transform="translate(28, 110)">
    <rect width="460" height="276" rx="18" fill="#EFF6FF" stroke="#93C5FD" stroke-width="2.5"/>
    <text x="230" y="32" text-anchor="middle" font-size="16" font-weight="bold" fill="#1E3A8A">① 医院分诊台一问一答（决策树：横竖切方块）</text>
    <rect x="30" y="50" width="400" height="140" rx="12" fill="#FFFFFF" stroke="#93C5FD" stroke-width="2"/>
    <path d="M 80 176 L 80 142 L 160 142 L 160 108 L 250 108 L 250 74 L 360 74" fill="none" stroke="#2563EB" stroke-width="4" stroke-dasharray="6,3"/>
    <circle cx="95" cy="94" r="10" fill="#3B82F6"/><circle cx="145" cy="80" r="10" fill="#3B82F6"/><circle cx="195" cy="78" r="10" fill="#3B82F6"/>
    <circle cx="135" cy="162" r="10" fill="#EF4444"/><circle cx="215" cy="136" r="10" fill="#EF4444"/><circle cx="305" cy="110" r="10" fill="#EF4444"/>
    <text x="315" y="166" text-anchor="middle" font-size="12" font-weight="bold" fill="#1D4ED8">只能切出横平竖直的楼梯格！</text>
    <rect x="20" y="202" width="420" height="60" rx="10" fill="#FFFFFF" stroke="#60A5FA" stroke-width="2"/>
    <text x="230" y="226" text-anchor="middle" font-size="13" font-weight="bold" fill="#1E40AF">生活例子：像查户口“发烧超38度吗？→肚子疼吗？”，每次只能单看</text>
    <text x="230" y="248" text-anchor="middle" font-size="13" font-weight="bold" fill="#1E40AF">一个指标横切或竖切一刀，遇到弯月牙只能剁出满地锯齿方块！</text>
  </g>

  <g transform="translate(512, 110)">
    <rect width="460" height="276" rx="18" fill="#FAF5FF" stroke="#D8B4FE" stroke-width="2.5"/>
    <text x="230" y="32" text-anchor="middle" font-size="16" font-weight="bold" fill="#6B21A8">② 把揉皱的折纸拉开抚平再剪（深度神经网络）</text>
    <rect x="26" y="50" width="166" height="140" rx="12" fill="#FFFFFF" stroke="#D8B4FE" stroke-width="2"/>
    <text x="109" y="72" text-anchor="middle" font-size="12" font-weight="bold" fill="#7E22CE">揉面/折纸前：拧成麻花</text>
    <path d="M 55 124 Q 109 76 162 124" fill="none" stroke="#3B82F6" stroke-width="8" stroke-linecap="round"/>
    <path d="M 55 138 Q 109 184 162 138" fill="none" stroke="#EF4444" stroke-width="8" stroke-linecap="round"/>

    <text x="230" y="112" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#9333EA">对折+拉开</text>
    <text x="230" y="134" text-anchor="middle" font-size="22" font-weight="bold" fill="#9333EA">➔</text>
    <text x="230" y="152" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#9333EA">(隐藏层)</text>

    <rect x="268" y="50" width="166" height="140" rx="12" fill="#FFFFFF" stroke="#D8B4FE" stroke-width="2"/>
    <text x="351" y="72" text-anchor="middle" font-size="12" font-weight="bold" fill="#15803D">拉开后：直剪刀一刀切！</text>
    <circle cx="305" cy="102" r="9" fill="#3B82F6"/><circle cx="305" cy="130" r="9" fill="#3B82F6"/><circle cx="305" cy="158" r="9" fill="#3B82F6"/>
    <line x1="351" y1="84" x2="351" y2="176" stroke="#16A34A" stroke-width="4" stroke-dasharray="5,3"/>
    <circle cx="395" cy="102" r="9" fill="#EF4444"/><circle cx="395" cy="130" r="9" fill="#EF4444"/><circle cx="395" cy="158" r="9" fill="#EF4444"/>

    <rect x="20" y="202" width="420" height="60" rx="10" fill="#FFFFFF" stroke="#C084FC" stroke-width="2"/>
    <text x="230" y="226" text-anchor="middle" font-size="13" font-weight="bold" fill="#6B21A8">生活例子：就像剪窗花！不用拿剪刀歪歪扭扭拐弯，先把画着图案</text>
    <text x="230" y="248" text-anchor="middle" font-size="13" font-weight="bold" fill="#6B21A8">的纸对折、抚平，让红蓝图案分列左右，最后直着剪一刀就全分开啦！</text>
  </g>
</svg>
''')


# ==============================================================================
# 第 5 幕：马路中间画最宽双黄线 & 颠铁锅筛花生米（SVM 最大间隔与核技巧升维）
# ==============================================================================
save_svg('pic05-border-guards-and-trampoline.svg', f'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 410" width="100%" height="auto" font-family="Microsoft YaHei, PingFang SC, sans-serif">
  <rect width="1000" height="410" rx="22" fill="#FFFBEB" stroke="#F59E0B" stroke-width="3"/>
  {dialogue_bar(
      "师傅，要是两拨东西本来就能用一条直线分开，随便画一条不就行了吗？干嘛还要学支持向量机（SVM）？",
      "你想想在马路中间画双黄线！贴着车轮画多危险？得在最前排那两辆车之间留出【最宽的安全带】！"
  )}

  <g transform="translate(28, 110)">
    <rect width="460" height="276" rx="18" fill="#ECFDF5" stroke="#6EE7B7" stroke-width="2.5"/>
    <text x="230" y="30" text-anchor="middle" font-size="15.5" font-weight="bold" fill="#065F46">① 马路画双黄线：只看最前排压线的那 3 辆车！</text>
    <rect x="30" y="46" width="400" height="146" rx="12" fill="#FFFFFF" stroke="#6EE7B7" stroke-width="2"/>
    <polygon points="175,46 245,46 285,192 215,192" fill="#FEF08A" opacity="0.7"/>
    <line x1="175" y1="46" x2="215" y2="192" stroke="#CA8A04" stroke-width="3" stroke-dasharray="6,4"/>
    <line x1="210" y1="46" x2="250" y2="192" stroke="#DC2626" stroke-width="4"/>
    <line x1="245" y1="46" x2="285" y2="192" stroke="#CA8A04" stroke-width="3" stroke-dasharray="6,4"/>

    <circle cx="80" cy="88" r="13" fill="#86EFAC"/><circle cx="105" cy="145" r="13" fill="#86EFAC"/><circle cx="65" cy="155" r="13" fill="#86EFAC"/>
    <text x="90" y="182" text-anchor="middle" font-size="11" fill="#15803D">后排几百辆车(全开走也不影响)</text>

    <circle cx="188" cy="92" r="15" fill="#22C55E" stroke="#DC2626" stroke-width="3.5"/>
    <circle cx="204" cy="158" r="15" fill="#22C55E" stroke="#DC2626" stroke-width="3.5"/>
    <circle cx="264" cy="120" r="15" fill="#EF4444" stroke="#DC2626" stroke-width="3.5"/>
    <text x="348" y="88" font-size="12" font-weight="bold" fill="#DC2626">★ 最前排压线车</text>
    <text x="348" y="106" font-size="11.5" fill="#991B1B">(叫支持向量)</text>
    <circle cx="375" cy="158" r="13" fill="#FCA5A5"/>

    <rect x="20" y="202" width="420" height="60" rx="10" fill="#FFFFFF" stroke="#34D399" stroke-width="2"/>
    <text x="230" y="226" text-anchor="middle" font-size="13" font-weight="bold" fill="#047857">生活常识：决定双黄线画在哪里的，永远只有紧贴路中间的那两三辆</text>
    <text x="230" y="248" text-anchor="middle" font-size="13" font-weight="bold" fill="#047857">前排车（支持向量）！排在后面堵车的几百辆车全开走，线也一毫米不歪！</text>
  </g>

  <g transform="translate(512, 110)">
    <rect width="460" height="276" rx="18" fill="#EFF6FF" stroke="#93C5FD" stroke-width="2.5"/>
    <text x="230" y="30" text-anchor="middle" font-size="15.5" font-weight="bold" fill="#1E3A8A">② 颠簸箕筛花生米：平地分不开，就往空中颠一下！</text>
    <rect x="26" y="46" width="166" height="146" rx="12" fill="#FFFFFF" stroke="#93C5FD" stroke-width="2"/>
    <text x="109" y="68" text-anchor="middle" font-size="12" font-weight="bold" fill="#1E40AF">盘子里：绿豆被花生皮包围</text>
    <circle cx="109" cy="130" r="44" fill="none" stroke="#EF4444" stroke-width="8" stroke-dasharray="10,7"/>
    <circle cx="98" cy="124" r="8" fill="#22C55E"/><circle cx="120" cy="124" r="8" fill="#22C55E"/><circle cx="109" cy="142" r="8" fill="#22C55E"/>

    <text x="228" y="108" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#EA580C">往上颠一锅</text>
    <text x="228" y="132" text-anchor="middle" font-size="22" font-weight="bold" fill="#EA580C">➔</text>
    <text x="228" y="152" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#EA580C">(核函数升维)</text>

    <rect x="264" y="46" width="170" height="146" rx="12" fill="#FFFFFF" stroke="#93C5FD" stroke-width="2"/>
    <text x="349" y="68" text-anchor="middle" font-size="12" font-weight="bold" fill="#15803D">飞到半空：拿纸板平着隔开！</text>
    <circle cx="322" cy="92" r="8" fill="#EF4444"/><circle cx="352" cy="88" r="8" fill="#EF4444"/><circle cx="382" cy="94" r="8" fill="#EF4444"/>
    <polygon points="282,124 416,112 426,130 292,142" fill="#38BDF8" opacity="0.65" stroke="#0284C7" stroke-width="2"/>
    <circle cx="325" cy="166" r="8" fill="#22C55E"/><circle cx="350" cy="172" r="8" fill="#22C55E"/><circle cx="378" cy="164" r="8" fill="#22C55E"/>

    <rect x="20" y="202" width="420" height="60" rx="10" fill="#FFFFFF" stroke="#60A5FA" stroke-width="2"/>
    <text x="230" y="226" text-anchor="middle" font-size="13" font-weight="bold" fill="#1E40AF">生活常识：就像大厨颠铁锅或者过年筛花生皮！平桌面上混成一圈分不</text>
    <text x="230" y="248" text-anchor="middle" font-size="13" font-weight="bold" fill="#1E40AF">开，往空中一颠加个“高度”（升成三维），拿硬纸板平着一插就彻底分开！</text>
  </g>
</svg>
''')


# ==============================================================================
# 第 6 幕：歌手大赛评委团 vs. 木匠师徒接力打磨（随机森林 vs. GBDT）
# ==============================================================================
save_svg('pic06-blindfold-vote-and-relay.svg', f'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 410" width="100%" height="auto" font-family="Microsoft YaHei, PingFang SC, sans-serif">
  <rect width="1000" height="410" rx="22" fill="#F8FAFC" stroke="#94A3B8" stroke-width="3"/>
  {dialogue_bar(
      "师傅，如果遇到特别难的大事，一个人拿不准，找一群人一起商量（集成学习）怎么配合最聪明？",
      "有两种完全不同的组队智慧：一种像歌手大赛请不同专业的评委同时打分；另一种像木匠师徒接力打家具！"
  )}

  <g transform="translate(28, 110)">
    <rect width="460" height="276" rx="18" fill="#ECFDF5" stroke="#6EE7B7" stroke-width="2.5"/>
    <text x="230" y="30" text-anchor="middle" font-size="15.5" font-weight="bold" fill="#065F46">① 随机森林：请各看各的评委同时打分，抵消手抖！</text>

    <rect x="26" y="48" width="122" height="140" rx="12" fill="#FFFFFF" stroke="#6EE7B7" stroke-width="2"/>
    <text x="87" y="82" text-anchor="middle" font-size="14" font-weight="bold" fill="#047857">🎵 音准评委</text>
    <text x="87" y="114" text-anchor="middle" font-size="12" fill="#475569">只听高音准不准</text>
    <text x="87" y="152" text-anchor="middle" font-size="13" font-weight="bold" fill="#15803D">打分：好听 ✓</text>

    <rect x="168" y="48" width="122" height="140" rx="12" fill="#FFFFFF" stroke="#6EE7B7" stroke-width="2"/>
    <text x="229" y="82" text-anchor="middle" font-size="14" font-weight="bold" fill="#047857">🥁 节奏评委</text>
    <text x="229" y="114" text-anchor="middle" font-size="12" fill="#475569">只听节拍稳不稳</text>
    <text x="229" y="152" text-anchor="middle" font-size="13" font-weight="bold" fill="#15803D">打分：好听 ✓</text>

    <rect x="310" y="48" width="122" height="140" rx="12" fill="#FFFFFF" stroke="#FCA5A5" stroke-width="2"/>
    <text x="371" y="82" text-anchor="middle" font-size="14" font-weight="bold" fill="#B91C1C">💃 台风评委</text>
    <text x="371" y="114" text-anchor="middle" font-size="12" fill="#475569">今天稍微看走眼</text>
    <text x="371" y="152" text-anchor="middle" font-size="13" font-weight="bold" fill="#DC2626">打分：一般 ✗</text>

    <rect x="20" y="202" width="420" height="60" rx="10" fill="#FFFFFF" stroke="#34D399" stroke-width="2"/>
    <text x="230" y="226" text-anchor="middle" font-size="13" font-weight="bold" fill="#065F46">生活常识：如果请 30 个一模一样的克隆人投票一点用都没有！必须让每</text>
    <text x="230" y="248" text-anchor="middle" font-size="13" font-weight="bold" fill="#065F46">个评委盯不同的点（随机抽特征），大家各自手抖的毛刺一平均就抵消了！</text>
  </g>

  <g transform="translate(512, 110)">
    <rect width="460" height="276" rx="18" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="2.5"/>
    <text x="230" y="30" text-anchor="middle" font-size="15.5" font-weight="bold" fill="#991B1B">② GBDT：木匠师徒排成一排，后一个人专补前一个人的差价！</text>

    <rect x="24" y="48" width="120" height="140" rx="12" fill="#FFFFFF" stroke="#FCA5A5" stroke-width="2"/>
    <text x="84" y="82" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#991B1B">🪓 1棒：大斧头</text>
    <text x="84" y="112" text-anchor="middle" font-size="12.5" fill="#475569">先砍出粗毛坯</text>
    <text x="84" y="142" text-anchor="middle" font-size="13" font-weight="bold" fill="#DC2626">完成了 60 分</text>
    <text x="84" y="168" text-anchor="middle" font-size="11.5" fill="#64748B">(还差 +40 分!)</text>

    <text x="156" y="122" text-anchor="middle" font-size="18" font-weight="bold" fill="#DC2626">+</text>

    <rect x="168" y="48" width="120" height="140" rx="12" fill="#FFFFFF" stroke="#FCA5A5" stroke-width="2"/>
    <text x="228" y="82" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#991B1B">🪚 2棒：木工刨</text>
    <text x="228" y="112" text-anchor="middle" font-size="12.5" fill="#475569">专刨剩下的坑洼</text>
    <text x="228" y="142" text-anchor="middle" font-size="13" font-weight="bold" fill="#EA580C">补上了 +30 分</text>
    <text x="228" y="168" text-anchor="middle" font-size="11.5" fill="#64748B">(还差 +10 分!)</text>

    <text x="300" y="122" text-anchor="middle" font-size="18" font-weight="bold" fill="#DC2626">+</text>

    <rect x="312" y="48" width="124" height="140" rx="12" fill="#FFFFFF" stroke="#86EFAC" stroke-width="2.5"/>
    <text x="374" y="82" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#15803D">✨ 3棒：细砂纸</text>
    <text x="374" y="112" text-anchor="middle" font-size="12.5" fill="#475569">磨平最后的毛刺</text>
    <text x="374" y="142" text-anchor="middle" font-size="13" font-weight="bold" fill="#16A34A">补完 +10 分</text>
    <text x="374" y="168" text-anchor="middle" font-size="12" font-weight="bold" fill="#15803D">合体 = 100分!</text>

    <rect x="20" y="202" width="420" height="60" rx="10" fill="#FFFFFF" stroke="#F87171" stroke-width="2"/>
    <text x="230" y="226" text-anchor="middle" font-size="13" font-weight="bold" fill="#991B1B">生活常识：就像写错题本！后面上场的人根本不用从零重做整张卷子，</text>
    <text x="230" y="248" text-anchor="middle" font-size="13" font-weight="bold" fill="#991B1B">只盯住上一个人没做对的“差价（残差）”一点点修补，越补越精准！</text>
  </g>
</svg>
''')


# ==============================================================================
# 第 7 幕：操场广播体操分队与美食街圈地盘（K-Means vs. EM 算法）
# ==============================================================================
save_svg('pic07-rubber-band-clustering.svg', f'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 410" width="100%" height="auto" font-family="Microsoft YaHei, PingFang SC, sans-serif">
  <rect width="1000" height="410" rx="22" fill="#FFFBEB" stroke="#F59E0B" stroke-width="3"/>
  {dialogue_bar(
      "师傅，前面说的都有标准答案。要是去一个陌生地方，连名牌和标签都没有，怎么把大家自动分群呀？",
      "这叫无监督聚类！比如操场上两个班做广播体操没穿校服，用圆规画正圆会切错，得用能变形的橡皮筋！"
  )}

  <g transform="translate(28, 110)">
    <rect width="460" height="276" rx="18" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="2.5"/>
    <text x="230" y="30" text-anchor="middle" font-size="15.5" font-weight="bold" fill="#991B1B">① K-Means 算法：像插旗画正圆，把长条体操队拦腰切错！</text>
    <rect x="30" y="46" width="400" height="142" rx="12" fill="#FFFFFF" stroke="#FCA5A5" stroke-width="2"/>
    <circle cx="155" cy="116" r="56" fill="#FEE2E2" opacity="0.65" stroke="#EF4444" stroke-width="3" stroke-dasharray="6,4"/>
    <circle cx="305" cy="116" r="56" fill="#DBEAFE" opacity="0.65" stroke="#3B82F6" stroke-width="3" stroke-dasharray="6,4"/>
    <circle cx="110" cy="88" r="8" fill="#EF4444"/><circle cx="170" cy="88" r="8" fill="#EF4444"/><circle cx="230" cy="88" r="8" fill="#EF4444"/>
    <circle cx="290" cy="88" r="8" fill="#3B82F6"/><circle cx="350" cy="88" r="8" fill="#3B82F6"/>
    <circle cx="110" cy="144" r="8" fill="#EF4444"/><circle cx="170" cy="144" r="8" fill="#EF4444"/>
    <circle cx="230" cy="144" r="8" fill="#3B82F6"/><circle cx="290" cy="144" r="8" fill="#3B82F6"/><circle cx="350" cy="144" r="8" fill="#3B82F6"/>
    <line x1="230" y1="54" x2="230" y2="180" stroke="#DC2626" stroke-width="3"/>

    <rect x="20" y="200" width="420" height="62" rx="10" fill="#FFFFFF" stroke="#F87171" stroke-width="2"/>
    <text x="230" y="224" text-anchor="middle" font-size="13" font-weight="bold" fill="#B91C1C">生活例子：操场上明明是上下两横排长长的队伍，K-Means 只认到旗子</text>
    <text x="230" y="246" text-anchor="middle" font-size="13" font-weight="bold" fill="#B91C1C">的直线距离（正圆圈），结果一刀把两列长队硬生生劈成了左右两半！</text>
  </g>

  <g transform="translate(512, 110)">
    <rect width="460" height="276" rx="18" fill="#ECFDF5" stroke="#6EE7B7" stroke-width="2.5"/>
    <text x="230" y="30" text-anchor="middle" font-size="15.5" font-weight="bold" fill="#065F46">② EM 算法与高斯混合：先猜人、再顺着队形拉长橡皮筋！</text>
    <rect x="30" y="46" width="400" height="142" rx="12" fill="#FFFFFF" stroke="#6EE7B7" stroke-width="2"/>
    <ellipse cx="230" cy="88" rx="155" ry="22" fill="#DCFCE7" opacity="0.8" stroke="#16A34A" stroke-width="3.5"/>
    <ellipse cx="230" cy="144" rx="155" ry="22" fill="#FEF3C7" opacity="0.8" stroke="#D97706" stroke-width="3.5"/>
    <circle cx="110" cy="88" r="8" fill="#16A34A"/><circle cx="170" cy="88" r="8" fill="#16A34A"/><circle cx="230" cy="88" r="8" fill="#16A34A"/><circle cx="290" cy="88" r="8" fill="#16A34A"/><circle cx="350" cy="88" r="8" fill="#16A34A"/>
    <circle cx="110" cy="144" r="8" fill="#D97706"/><circle cx="170" cy="144" r="8" fill="#D97706"/><circle cx="230" cy="144" r="8" fill="#D97706"/><circle cx="290" cy="144" r="8" fill="#D97706"/><circle cx="350" cy="144" r="8" fill="#D97706"/>

    <rect x="20" y="200" width="420" height="62" rx="10" fill="#FFFFFF" stroke="#34D399" stroke-width="2"/>
    <text x="230" y="224" text-anchor="middle" font-size="13" font-weight="bold" fill="#047857">生活例子：就像鸡生蛋、蛋生鸡！第1步（E步）先猜每个人归哪队；第2步</text>
    <text x="230" y="246" text-anchor="middle" font-size="13" font-weight="bold" fill="#047857">（M步）顺着队形把橡皮筋拉成细长椭圆。来回调整几轮就完美贴合啦！</text>
  </g>
</svg>
''')


# ==============================================================================
# 第 8 幕：饭店一道汤做咸了，怎么顺着传菜签倒查一趟抓出撒盐师傅？（反向传播 BP）
# ==============================================================================
save_svg('pic08-kitchen-whisper.svg', f'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 410" width="100%" height="auto" font-family="Microsoft YaHei, PingFang SC, sans-serif">
  <rect width="1000" height="410" rx="22" fill="#F8FAFC" stroke="#94A3B8" stroke-width="3"/>
  {dialogue_bar(
      "师傅，最后一个问题！现在的深度学习大模型有几百亿个旋钮，算错一道题，怎么一眨眼就知道该拧哪个旋钮改错呀？",
      "你想想大饭店后厨！一道汤端上桌太咸了，不用让 100 个厨师挨个重做一锅，顺着【传菜签】从后往前倒查 1 趟就破案！"
  )}

  <g transform="translate(32, 108)">
    <rect width="936" height="122" rx="16" fill="#EFF6FF" stroke="#93C5FD" stroke-width="2.5"/>
    <text x="468" y="24" text-anchor="middle" font-size="15" font-weight="bold" fill="#1E3A8A">👉 第一趟（前向传播）：后厨流水线做汤，每个人都在传菜签上记一笔“我放了多少料”</text>

    <rect x="28" y="36" width="182" height="72" rx="12" fill="#FFFFFF" stroke="#60A5FA" stroke-width="2"/>
    <text x="119" y="64" text-anchor="middle" font-size="14" font-weight="bold" fill="#1E293B">① 切菜配菜工</text>
    <text x="119" y="88" text-anchor="middle" font-size="12" fill="#047857">传菜签：食材份量正常</text>

    <text x="232" y="78" text-anchor="middle" font-size="22" font-weight="bold" fill="#3B82F6">➔</text>

    <rect x="254" y="36" width="202" height="72" rx="12" fill="#FEF2F2" stroke="#EF4444" stroke-width="3"/>
    <text x="355" y="64" text-anchor="middle" font-size="14" font-weight="bold" fill="#DC2626">② 调味师傅（闯祸!）</text>
    <text x="355" y="88" text-anchor="middle" font-size="12" font-weight="bold" fill="#B91C1C">传菜签：手抖多撒了 5 勺盐</text>

    <text x="478" y="78" text-anchor="middle" font-size="22" font-weight="bold" fill="#3B82F6">➔</text>

    <rect x="500" y="36" width="182" height="72" rx="12" fill="#FFFFFF" stroke="#60A5FA" stroke-width="2"/>
    <text x="591" y="64" text-anchor="middle" font-size="14" font-weight="bold" fill="#1E293B">③ 炖汤看火工</text>
    <text x="591" y="88" text-anchor="middle" font-size="12" fill="#047857">传菜签：只管加热不放盐</text>

    <text x="704" y="78" text-anchor="middle" font-size="22" font-weight="bold" fill="#3B82F6">➔</text>

    <rect x="726" y="36" width="184" height="72" rx="12" fill="#FFFBEB" stroke="#F59E0B" stroke-width="2.5"/>
    <text x="818" y="64" text-anchor="middle" font-size="14" font-weight="bold" fill="#B45309">④ 店长尝第一口</text>
    <text x="818" y="88" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#DC2626">结果：“太咸啦！误差=3.6”</text>
  </g>

  <g transform="translate(32, 244)">
    <rect width="936" height="144" rx="16" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="2.5"/>
    <text x="468" y="26" text-anchor="middle" font-size="15.5" font-weight="bold" fill="#991B1B">👈 第二趟（反向传播 backward）：顺着传菜签从最后一道工序往回查，走 1 趟全员领到改错单！</text>

    <path d="M 800 52 C 660 98, 500 98, 355 52" fill="none" stroke="#DC2626" stroke-width="5" stroke-dasharray="8,4"/>
    <polygon points="355,52 372,49 366,65" fill="#DC2626"/>
    <rect x="430" y="50" width="290" height="32" rx="10" fill="#DC2626"/>
    <text x="575" y="71" text-anchor="middle" font-size="13" font-weight="bold" fill="#FFFFFF">📣 倒查传菜签：“找到啦！2号师傅下次少放盐！”</text>

    <rect x="24" y="92" width="888" height="40" rx="10" fill="#FFFFFF" stroke="#F87171" stroke-width="2"/>
    <text x="468" y="117" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#7F1D1D">生活常识：笨办法要让 100 个厨师挨个重做 100 锅汤才能试出谁放多了盐；【反向传播】顺着传菜签倒查 1 趟，哪怕一亿个旋钮也能同时算清责任！</text>
  </g>
</svg>
''')
