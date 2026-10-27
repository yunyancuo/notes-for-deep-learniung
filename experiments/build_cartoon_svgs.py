# -*- coding: utf-8 -*-
"""
《橘猫店长的西瓜摊：给孩子的机器学习与深度学习绘本》
生成全套猫咪主题纯卡通 SVG 插画 (pic01 ~ pic08.svg)
每张图均包含带尖耳朵、胡须、表情的可爱猫咪角色与大字对话气泡，零复杂公式墙！
"""
import os
import xml.etree.ElementTree as ET

ROOT = r'C:\Users\34684\Documents\notes-for-deep-learniung'
ASSETS = os.path.join(ROOT, 'assets')
os.makedirs(ASSETS, exist_ok=True)


def cat_avatar(cx, cy, r=32, fur="#F97316", stroke="#9A3412", mood="happy", hat=None, glasses=False):
    """生成超可爱的 SVG 猫咪头像组件（带尖耳朵、粉耳廓、胡须、表情、可选草帽/安全帽/魔法帽/眼镜）"""
    # 左右尖耳朵坐标
    ear_l = f"{cx-int(r*0.85)},{cy-int(r*0.45)} {cx-int(r*0.95)},{cy-int(r*1.25)} {cx-int(r*0.25)},{cy-int(r*0.82)}"
    ear_r = f"{cx+int(r*0.85)},{cy-int(r*0.45)} {cx+int(r*0.95)},{cy-int(r*1.25)} {cx+int(r*0.25)},{cy-int(r*0.82)}"
    in_l = f"{cx-int(r*0.75)},{cy-int(r*0.55)} {cx-int(r*0.82)},{cy-int(r*1.08)} {cx-int(r*0.35)},{cy-int(r*0.78)}"
    in_r = f"{cx+int(r*0.75)},{cy-int(r*0.55)} {cx+int(r*0.82)},{cy-int(r*1.08)} {cx+int(r*0.35)},{cy-int(r*0.78)}"

    parts = [
        f'<polygon points="{ear_l}" fill="{fur}" stroke="{stroke}" stroke-width="2.5" stroke-linejoin="round"/>',
        f'<polygon points="{ear_r}" fill="{fur}" stroke="{stroke}" stroke-width="2.5" stroke-linejoin="round"/>',
        f'<polygon points="{in_l}" fill="#FDA4AF"/>',
        f'<polygon points="{in_r}" fill="#FDA4AF"/>',
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fur}" stroke="{stroke}" stroke-width="2.5"/>',
        # 额头虎斑纹
        f'<line x1="{cx}" y1="{cy-r+3}" x2="{cx}" y2="{cy-int(r*0.55)}" stroke="{stroke}" stroke-width="3" stroke-linecap="round"/>',
        f'<line x1="{cx-7}" y1="{cy-r+5}" x2="{cx-5}" y2="{cy-int(r*0.6)}" stroke="{stroke}" stroke-width="2.5" stroke-linecap="round"/>',
        f'<line x1="{cx+7}" y1="{cy-r+5}" x2="{cx+5}" y2="{cy-int(r*0.6)}" stroke="{stroke}" stroke-width="2.5" stroke-linecap="round"/>',
    ]

    # 眼睛
    ey = cy - int(r * 0.12)
    ex = int(r * 0.38)
    if mood == "sleep":
        parts.append(f'<path d="M {cx-ex-6} {ey} Q {cx-ex} {ey+6} {cx-ex+6} {ey}" fill="none" stroke="#1E293B" stroke-width="2.5" stroke-linecap="round"/>')
        parts.append(f'<path d="M {cx+ex-6} {ey} Q {cx+ex} {ey+6} {cx+ex+6} {ey}" fill="none" stroke="#1E293B" stroke-width="2.5" stroke-linecap="round"/>')
    elif mood == "shock":
        parts.append(f'<circle cx="{cx-ex}" cy="{ey}" r="6" fill="#FFFFFF" stroke="#1E293B" stroke-width="2"/>')
        parts.append(f'<circle cx="{cx+ex}" cy="{ey}" r="6" fill="#FFFFFF" stroke="#1E293B" stroke-width="2"/>')
        parts.append(f'<circle cx="{cx-ex}" cy="{ey}" r="2.5" fill="#1E293B"/>')
        parts.append(f'<circle cx="{cx+ex}" cy="{ey}" r="2.5" fill="#1E293B"/>')
    else:
        parts.append(f'<circle cx="{cx-ex}" cy="{ey}" r="4.5" fill="#1E293B"/>')
        parts.append(f'<circle cx="{cx+ex}" cy="{ey}" r="4.5" fill="#1E293B"/>')
        parts.append(f'<circle cx="{cx-ex-1.5}" cy="{ey-1.5}" r="1.5" fill="#FFFFFF"/>')
        parts.append(f'<circle cx="{cx+ex-1.5}" cy="{ey-1.5}" r="1.5" fill="#FFFFFF"/>')

    if glasses:
        parts.append(f'<circle cx="{cx-ex}" cy="{ey}" r="9" fill="none" stroke="#0F172A" stroke-width="2"/>')
        parts.append(f'<circle cx="{cx+ex}" cy="{ey}" r="9" fill="none" stroke="#0F172A" stroke-width="2"/>')
        parts.append(f'<line x1="{cx-ex+9}" y1="{ey}" x2="{cx+ex-9}" y2="{ey}" stroke="#0F172A" stroke-width="2"/>')

    # 粉色小鼻头 + W 型猫咪嘴 + 胡须
    ny = cy + int(r * 0.12)
    parts.append(f'<polygon points="{cx-4},{ny} {cx+4},{ny} {cx},{ny+5}" fill="#F43F5E"/>')
    parts.append(f'<path d="M {cx-8} {ny+7} Q {cx-4} {ny+12} {cx} {ny+6} Q {cx+4} {ny+12} {cx+8} {ny+7}" fill="none" stroke="#1E293B" stroke-width="2" stroke-linecap="round"/>')
    # 左右三根胡须
    for dy in [-3, 3]:
        parts.append(f'<line x1="{cx-int(r*0.55)}" y1="{ny+dy}" x2="{cx-int(r*1.08)}" y2="{ny+dy*2}" stroke="#475569" stroke-width="1.8" stroke-linecap="round"/>')
        parts.append(f'<line x1="{cx+int(r*0.55)}" y1="{ny+dy}" x2="{cx+int(r*1.08)}" y2="{ny+dy*2}" stroke="#475569" stroke-width="1.8" stroke-linecap="round"/>')

    # 帽子装饰
    if hat == "straw":
        parts.append(f'<ellipse cx="{cx}" cy="{cy-r+2}" rx="{int(r*1.15)}" ry="7" fill="#FDE047" stroke="#CA8A04" stroke-width="2"/>')
        parts.append(f'<path d="M {cx-int(r*0.65)} {cy-r+2} Q {cx} {cy-int(r*1.65)} {cx+int(r*0.65)} {cy-r+2} Z" fill="#FACC15" stroke="#CA8A04" stroke-width="2"/>')
    elif hat == "wizard":
        parts.append(f'<polygon points="{cx-int(r*0.9)},{cy-r+4} {cx+int(r*0.9)},{cy-r+4} {cx},{cy-int(r*2.0)}" fill="#7E22CE" stroke="#581C87" stroke-width="2"/>')
    elif hat == "chef":
        parts.append(f'<rect x="{cx-int(r*0.6)}" y="{cy-int(r*1.45)}" width="{int(r*1.2)}" height="{int(r*0.5)}" rx="8" fill="#FFFFFF" stroke="#94A3B8" stroke-width="2"/>')

    return "\n".join(parts)


def save_svg(name, content):
    path = os.path.join(ASSETS, name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip())
    ET.parse(path)
    print("Saved valid Cat Cartoon SVG:", name)


# ==============================================================================
# 插画 1：橘猫店长胖虎的西瓜摊 —— 不切开肚皮，怎么猜瓜甜不甜？
# ==============================================================================
save_svg('pic01-watermelon-stall.svg', f'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 385" width="100%" height="auto" font-family="Microsoft YaHei, PingFang SC, sans-serif">
  <rect width="1000" height="385" rx="22" fill="#FFFBEB" stroke="#F59E0B" stroke-width="3"/>
  <rect x="24" y="18" width="952" height="46" rx="14" fill="#FEF3C7" stroke="#FBBF24" stroke-width="2"/>
  <text x="500" y="48" text-anchor="middle" font-size="20" font-weight="bold" fill="#92400E">第 1 页：橘猫店长“胖虎”的西瓜摊（隔着肚皮怎么猜瓜甜不甜？）</text>

  <!-- 左侧：拍肚皮的大西瓜 -->
  <g transform="translate(32, 82)">
    <rect width="295" height="278" rx="18" fill="#ECFDF5" stroke="#6EE7B7" stroke-width="2.5"/>
    <text x="147" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#065F46">① 小猫爪拍拍瓜肚皮</text>
    <circle cx="147" cy="150" r="68" fill="#22C55E" stroke="#15803D" stroke-width="4"/>
    <path d="M 114 90 Q 98 150 115 210" fill="none" stroke="#14532D" stroke-width="7" stroke-linecap="round"/>
    <path d="M 147 82 Q 134 150 147 218" fill="none" stroke="#14532D" stroke-width="7" stroke-linecap="round"/>
    <path d="M 180 90 Q 196 150 179 210" fill="none" stroke="#14532D" stroke-width="7" stroke-linecap="round"/>
    <path d="M 147 82 C 147 58, 174 56, 164 72 C 156 80, 176 78, 180 62" fill="none" stroke="#15803D" stroke-width="5" stroke-linecap="round"/>
    <circle cx="125" cy="142" r="7" fill="#1E293B"/><circle cx="169" cy="142" r="7" fill="#1E293B"/>
    <path d="M 134 158 Q 147 172 160 158" fill="none" stroke="#1E293B" stroke-width="3.5" stroke-linecap="round"/>
    <!-- 橘猫肉垫拍瓜 -->
    <ellipse cx="242" cy="118" rx="22" ry="16" fill="#FDBA74" stroke="#C2410C" stroke-width="2.5"/>
    <circle cx="232" cy="118" r="5" fill="#F43F5E"/><circle cx="244" cy="110" r="4" fill="#F43F5E"/><circle cx="252" cy="120" r="4" fill="#F43F5E"/>
    <text x="65" y="96" font-size="16" font-weight="bold" fill="#DC2626">啪！咚咚！</text>
    <text x="147" y="252" text-anchor="middle" font-size="14" font-weight="bold" fill="#047857">“猫爪拍一拍，声音脆脆响！”</text>
  </g>

  <!-- 中间：猫咪记账本 (三大特征) -->
  <g transform="translate(352, 82)">
    <rect width="295" height="278" rx="18" fill="#EFF6FF" stroke="#93C5FD" stroke-width="2.5"/>
    <text x="147" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#1E3A8A">② 记在猫咪账本上（叫特征）</text>
    <rect x="22" y="48" width="250" height="58" rx="12" fill="#FFFFFF" stroke="#60A5FA" stroke-width="2"/>
    <circle cx="52" cy="77" r="16" fill="#22C55E"/>
    <text x="82" y="72" font-size="15" font-weight="bold" fill="#1E293B">猫眼看颜色：绿油油</text>
    <text x="82" y="94" font-size="13" fill="#475569">青绿=1分，乌黑=2分，浅白=0分</text>

    <rect x="22" y="118" width="250" height="58" rx="12" fill="#FFFFFF" stroke="#60A5FA" stroke-width="2"/>
    <circle cx="52" cy="147" r="16" fill="#F59E0B"/>
    <text x="82" y="142" font-size="15" font-weight="bold" fill="#1E293B">猫爪摸尾巴：打卷儿</text>
    <text x="82" y="164" font-size="13" fill="#475569">蜷缩弯弯 = 熟透的大甜瓜！</text>

    <rect x="22" y="188" width="250" height="66" rx="12" fill="#FFFFFF" stroke="#60A5FA" stroke-width="2"/>
    <circle cx="52" cy="221" r="16" fill="#EC4899"/>
    <text x="82" y="214" font-size="15" font-weight="bold" fill="#1E293B">猫耳听回音：咚咚脆</text>
    <text x="82" y="236" font-size="13" fill="#475569">浊响 = 好瓜！闷响 = 生瓜蛋子！</text>
  </g>

  <!-- 右侧：戴草帽的橘猫店长胖虎 -->
  <g transform="translate(672, 82)">
    <rect width="295" height="278" rx="18" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="2.5"/>
    <text x="147" y="30" text-anchor="middle" font-size="16" font-weight="bold" fill="#991B1B">③ 橘猫店长“胖虎”的秘籍</text>
    {cat_avatar(147, 112, r=36, fur="#FB923C", stroke="#9A3412", mood="happy", hat="straw")}
    <rect x="18" y="166" width="258" height="94" rx="14" fill="#FFFFFF" stroke="#F87171" stroke-width="2.5"/>
    <text x="147" y="194" text-anchor="middle" font-size="14.5" font-weight="bold" fill="#DC2626">“本喵尝过 100 个西瓜后，</text>
    <text x="147" y="218" text-anchor="middle" font-size="14.5" font-weight="bold" fill="#DC2626">让电脑自己从账本里找规律，</text>
    <text x="147" y="242" text-anchor="middle" font-size="15" font-weight="bold" fill="#1E293B">这就叫【机器学习】喵！”</text>
  </g>
</svg>
''')


# ==============================================================================
# 插画 2：三只小猫学挑瓜 —— 直尺蓝猫小呆、背题奶牛猫小强、橘猫店长胖虎
# ==============================================================================
save_svg('pic02-three-apprentices.svg', f'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 400" width="100%" height="auto" font-family="Microsoft YaHei, PingFang SC, sans-serif">
  <rect width="1000" height="400" rx="22" fill="#F8FAFC" stroke="#94A3B8" stroke-width="3"/>
  <rect x="24" y="18" width="952" height="46" rx="14" fill="#E0F2FE" stroke="#38BDF8" stroke-width="2"/>
  <text x="500" y="48" text-anchor="middle" font-size="20" font-weight="bold" fill="#0369A1">第 2 页：三只小猫学挑瓜（为什么死记硬背的奶牛猫反而考砸了？）</text>

  <!-- 1. 蓝猫小呆 (欠拟合) -->
  <g transform="translate(28, 80)">
    <rect width="296" height="296" rx="18" fill="#F1F5F9" stroke="#94A3B8" stroke-width="2.5"/>
    {cat_avatar(60, 48, r=24, fur="#94A3B8", stroke="#334155", mood="happy")}
    <text x="182" y="44" text-anchor="middle" font-size="16" font-weight="bold" fill="#334155">蓝猫小呆：死抱直尺</text>
    <text x="182" y="64" text-anchor="middle" font-size="12.5" fill="#64748B">（一根筋 / 欠拟合）</text>

    <rect x="24" y="86" width="248" height="122" rx="12" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
    <circle cx="55" cy="180" r="8" fill="#22C55E"/><circle cx="95" cy="135" r="8" fill="#22C55E"/>
    <circle cx="148" cy="108" r="8" fill="#22C55E"/><circle cx="200" cy="132" r="8" fill="#22C55E"/>
    <circle cx="240" cy="178" r="8" fill="#22C55E"/>
    <line x1="35" y1="162" x2="260" y2="142" stroke="#64748B" stroke-width="5" stroke-linecap="round"/>

    <rect x="20" y="220" width="256" height="62" rx="10" fill="#FFFFFF" stroke="#94A3B8" stroke-width="2"/>
    <text x="148" y="244" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#475569">“喵！我不管弯不弯，只画直线！”</text>
    <text x="148" y="268" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#DC2626">诊断：脑筋太死板（偏差太高）</text>
  </g>

  <!-- 2. 奶牛猫小强 (过拟合) -->
  <g transform="translate(352, 80)">
    <rect width="296" height="296" rx="18" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="2.5"/>
    {cat_avatar(60, 48, r=24, fur="#E2E8F0", stroke="#0F172A", mood="shock", glasses=True)}
    <text x="182" y="44" text-anchor="middle" font-size="16" font-weight="bold" fill="#991B1B">奶牛猫小强：死背猫砂</text>
    <text x="182" y="64" text-anchor="middle" font-size="12.5" fill="#DC2626">（死记硬背 / 过拟合）</text>

    <rect x="24" y="86" width="248" height="122" rx="12" fill="#FFFFFF" stroke="#FECACA" stroke-width="2"/>
    <circle cx="55" cy="180" r="8" fill="#22C55E"/><circle cx="95" cy="135" r="8" fill="#22C55E"/>
    <circle cx="148" cy="108" r="8" fill="#22C55E"/>
    <circle cx="195" cy="186" r="9" fill="#B45309"/>
    <text x="195" y="202" text-anchor="middle" font-size="10.5" font-weight="bold" fill="#92400E">手抖粘的猫砂噪点</text>
    <circle cx="240" cy="178" r="8" fill="#22C55E"/>
    <path d="M 40 195 L 55 180 L 75 95 L 95 135 L 148 108 L 172 92 L 195 186 L 220 96 L 240 178" fill="none" stroke="#EF4444" stroke-width="3.8" stroke-linejoin="round"/>

    <rect x="20" y="220" width="256" height="62" rx="10" fill="#FFFFFF" stroke="#F87171" stroke-width="2"/>
    <text x="148" y="244" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#B91C1C">“连瓜皮粘的猫砂我都背下来啦！”</text>
    <text x="148" y="268" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#B45309">诊断：换个瓜摊全疯掉（方差爆炸）</text>
  </g>

  <!-- 3. 橘猫店长胖虎 (恰当泛化) -->
  <g transform="translate(676, 80)">
    <rect width="296" height="296" rx="18" fill="#ECFDF5" stroke="#6EE7B7" stroke-width="2.5"/>
    {cat_avatar(60, 50, r=24, fur="#FB923C", stroke="#9A3412", mood="happy", hat="straw")}
    <text x="182" y="44" text-anchor="middle" font-size="16" font-weight="bold" fill="#065F46">橘猫店长：顺势画彩虹</text>
    <text x="182" y="64" text-anchor="middle" font-size="12.5" fill="#047857">（抓大放小 / 泛化极佳）</text>

    <rect x="24" y="86" width="248" height="122" rx="12" fill="#FFFFFF" stroke="#A7F3D0" stroke-width="2"/>
    <circle cx="55" cy="180" r="8" fill="#22C55E"/><circle cx="95" cy="135" r="8" fill="#22C55E"/>
    <circle cx="148" cy="108" r="8" fill="#22C55E"/>
    <circle cx="195" cy="186" r="7" fill="#CBD5E1"/>
    <text x="195" y="170" text-anchor="middle" font-size="10.5" fill="#64748B">无视小猫砂</text>
    <circle cx="240" cy="178" r="8" fill="#22C55E"/>
    <path d="M 45 186 Q 148 45 250 184" fill="none" stroke="#16A34A" stroke-width="5" stroke-linecap="round"/>

    <rect x="20" y="220" width="256" height="62" rx="10" fill="#FFFFFF" stroke="#34D399" stroke-width="2"/>
    <text x="148" y="244" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#047857">“抓大趋势、忽略小猫砂才最准喵！”</text>
    <text x="148" y="268" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#15803D">满分：去哪个瓜摊都能挑中甜瓜！</text>
  </g>
</svg>
''')


# ==============================================================================
# 插画 3：天价金瓜大捣乱！算平均数的猫 vs 看排中间的猫
# ==============================================================================
save_svg('pic03-gold-watermelon-scale.svg', f'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 395" width="100%" height="auto" font-family="Microsoft YaHei, PingFang SC, sans-serif">
  <rect width="1000" height="395" rx="22" fill="#FFFBEB" stroke="#F59E0B" stroke-width="3"/>
  <rect x="24" y="18" width="952" height="46" rx="14" fill="#FEF3C7" stroke="#FBBF24" stroke-width="2"/>
  <text x="500" y="48" text-anchor="middle" font-size="20" font-weight="bold" fill="#92400E">第 3 页：天价金瓜大捣乱！为什么“算平均数”的小猫会被土豪金瓜骗走？</text>

  <!-- 左：算平方平均的奶牛猫被金瓜压翻 -->
  <g transform="translate(28, 80)">
    <rect width="460" height="292" rx="18" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="2.5"/>
    {cat_avatar(58, 46, r=22, fur="#E2E8F0", stroke="#0F172A", mood="shock")}
    <text x="255" y="42" text-anchor="middle" font-size="16.5" font-weight="bold" fill="#991B1B">① 平方算盘喵（L2损失）：被一颗金瓜拽上天！</text>

    <polygon points="210,212 250,212 230,172" fill="#64748B"/>
    <line x1="60" y1="132" x2="400" y2="198" stroke="#475569" stroke-width="8" stroke-linecap="round"/>
    <circle cx="95" cy="118" r="17" fill="#22C55E" stroke="#15803D" stroke-width="2.5"/>
    <circle cx="138" cy="126" r="17" fill="#22C55E" stroke="#15803D" stroke-width="2.5"/>
    <circle cx="180" cy="134" r="17" fill="#22C55E" stroke="#15803D" stroke-width="2.5"/>
    <text x="138" y="94" text-anchor="middle" font-size="13" font-weight="bold" fill="#15803D">普通瓜：10元一个</text>

    <circle cx="355" cy="150" r="36" fill="#FACC15" stroke="#CA8A04" stroke-width="4"/>
    <polygon points="330,115 342,96 355,110 368,96 380,115" fill="#F59E0B" stroke="#B45309" stroke-width="2"/>
    <text x="355" y="156" text-anchor="middle" font-size="14" font-weight="bold" fill="#713F12">1000元!</text>

    <rect x="24" y="226" width="412" height="50" rx="12" fill="#FFFFFF" stroke="#F87171" stroke-width="2"/>
    <text x="230" y="256" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#B91C1C">惨剧：把 1 个金瓜和 9 个普通瓜算平均，每个普通瓜都被标成 109 元喵！</text>
  </g>

  <!-- 右：橘猫店长排队找中间 + 菱形猫爪剪废话 -->
  <g transform="translate(512, 80)">
    <rect width="460" height="292" rx="18" fill="#ECFDF5" stroke="#6EE7B7" stroke-width="2.5"/>
    {cat_avatar(58, 46, r=22, fur="#FB923C", stroke="#9A3412", mood="happy", hat="straw")}
    <text x="255" y="42" text-anchor="middle" font-size="16.5" font-weight="bold" fill="#065F46">② 中位数算盘喵（L1）与专剪废话的“菱形猫爪”</text>

    <rect x="24" y="76" width="412" height="84" rx="12" fill="#FFFFFF" stroke="#6EE7B7" stroke-width="2"/>
    <text x="230" y="98" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#047857">秘诀 A（L1 绝对误差）：按价格排队，本喵只看站在正中间的瓜！</text>
    <circle cx="95" cy="132" r="14" fill="#22C55E"/><circle cx="150" cy="132" r="14" fill="#22C55E"/>
    <circle cx="210" cy="132" r="18" fill="#16A34A" stroke="#DC2626" stroke-width="3"/>
    <text x="210" y="137" text-anchor="middle" font-size="11" font-weight="bold" fill="#FFFFFF">10元</text>
    <circle cx="270" cy="132" r="14" fill="#22C55E"/>
    <circle cx="335" cy="132" r="18" fill="#FACC15" stroke="#CA8A04" stroke-width="2"/>
    <text x="335" y="136" text-anchor="middle" font-size="10" font-weight="bold" fill="#713F12">金瓜</text>
    <text x="392" y="136" font-size="12" font-weight="bold" fill="#64748B">(当它空气!)</text>

    <rect x="24" y="172" width="412" height="104" rx="12" fill="#FFFFFF" stroke="#6EE7B7" stroke-width="2"/>
    <text x="230" y="196" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#065F46">秘诀 B（Lasso 菱形尖角）：把瞎编的废话线索一爪子全挠成 0！</text>
    <polygon points="68,210 94,236 68,262 42,236" fill="#10B981" stroke="#047857" stroke-width="2.5"/>
    <text x="68" y="240" text-anchor="middle" font-size="11" font-weight="bold" fill="#FFFFFF">L1菱形</text>
    <rect x="114" y="216" width="92" height="36" rx="8" fill="#DCFCE7" stroke="#16A34A" stroke-width="2"/>
    <text x="160" y="239" text-anchor="middle" font-size="13" font-weight="bold" fill="#15803D">✓ 太阳光照</text>
    <rect x="220" y="216" width="96" height="36" rx="8" fill="#FEE2E2" stroke="#EF4444" stroke-width="2"/>
    <text x="268" y="239" text-anchor="middle" font-size="13" font-weight="bold" fill="#DC2626">✗ 店长星座</text>
    <rect x="328" y="216" width="92" height="36" rx="8" fill="#FEE2E2" stroke="#EF4444" stroke-width="2"/>
    <text x="374" y="239" text-anchor="middle" font-size="13" font-weight="bold" fill="#DC2626">✗ 货车尾号</text>
  </g>
</svg>
''')


# ==============================================================================
# 插画 4：方刀暹罗猫（决策树）vs. 揉面布偶猫魔法师（神经网络）
# ==============================================================================
save_svg('pic04-tofu-knife-vs-magic-dough.svg', f'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 395" width="100%" height="auto" font-family="Microsoft YaHei, PingFang SC, sans-serif">
  <rect width="1000" height="395" rx="22" fill="#F8FAFC" stroke="#94A3B8" stroke-width="3"/>
  <rect x="24" y="18" width="952" height="46" rx="14" fill="#F3E8FF" stroke="#C084FC" stroke-width="2"/>
  <text x="500" y="48" text-anchor="middle" font-size="20" font-weight="bold" fill="#6B21A8">第 4 页：只会切方块的暹罗猫（决策树）vs. 会揉毛线团的布偶猫（神经网络）</text>

  <!-- 左：暹罗猫方刀切豆腐 -->
  <g transform="translate(28, 80)">
    <rect width="460" height="292" rx="18" fill="#EFF6FF" stroke="#93C5FD" stroke-width="2.5"/>
    {cat_avatar(58, 46, r=22, fur="#D6D3D1", stroke="#44403C", mood="happy")}
    <text x="255" y="42" text-anchor="middle" font-size="16.5" font-weight="bold" fill="#1E3A8A">① 方刀暹罗猫（决策树）：刀子只能横着切、竖着切！</text>

    <rect x="34" y="76" width="392" height="142" rx="12" fill="#FFFFFF" stroke="#93C5FD" stroke-width="2"/>
    <path d="M 80 202 L 80 165 L 160 165 L 160 128 L 250 128 L 250 92 L 360 92" fill="none" stroke="#2563EB" stroke-width="4" stroke-dasharray="6,3"/>
    <circle cx="95" cy="112" r="11" fill="#3B82F6"/><circle cx="145" cy="98" r="11" fill="#3B82F6"/><circle cx="195" cy="96" r="11" fill="#3B82F6"/>
    <circle cx="135" cy="186" r="11" fill="#EF4444"/><circle cx="215" cy="158" r="11" fill="#EF4444"/><circle cx="305" cy="130" r="11" fill="#EF4444"/>
    <text x="322" y="188" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#1D4ED8">切出一堆锯齿楼梯喵！</text>

    <rect x="24" y="230" width="412" height="48" rx="12" fill="#FFFFFF" stroke="#60A5FA" stroke-width="2"/>
    <text x="230" y="259" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#1E40AF">“我的菜刀焊死在桌边啦！遇到弯弯的月牙，只能剁成锯齿方块喵！”</text>
  </g>

  <!-- 右：布偶猫魔法师揉面团 -->
  <g transform="translate(512, 80)">
    <rect width="460" height="292" rx="18" fill="#FAF5FF" stroke="#D8B4FE" stroke-width="2.5"/>
    {cat_avatar(58, 52, r=22, fur="#F8FAFC", stroke="#6B21A8", mood="happy", hat="wizard")}
    <text x="255" y="42" text-anchor="middle" font-size="16.5" font-weight="bold" fill="#6B21A8">② 魔法布偶猫（神经网络）：先把麻花拉开揉直！</text>

    <rect x="26" y="76" width="166" height="142" rx="12" fill="#FFFFFF" stroke="#D8B4FE" stroke-width="2"/>
    <text x="109" y="98" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#7E22CE">揉面之前：拧成麻花</text>
    <path d="M 55 150 Q 109 100 162 150" fill="none" stroke="#3B82F6" stroke-width="9" stroke-linecap="round"/>
    <path d="M 55 165 Q 109 212 162 165" fill="none" stroke="#EF4444" stroke-width="9" stroke-linecap="round"/>

    <text x="230" y="138" text-anchor="middle" font-size="13" font-weight="bold" fill="#9333EA">猫爪揉面</text>
    <text x="230" y="158" text-anchor="middle" font-size="22" font-weight="bold" fill="#9333EA">➔</text>
    <text x="230" y="176" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#9333EA">(隐藏层)</text>

    <rect x="268" y="76" width="166" height="142" rx="12" fill="#FFFFFF" stroke="#D8B4FE" stroke-width="2"/>
    <text x="351" y="98" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#15803D">揉面之后：一爪两断！</text>
    <circle cx="305" cy="126" r="10" fill="#3B82F6"/><circle cx="305" cy="156" r="10" fill="#3B82F6"/><circle cx="305" cy="186" r="10" fill="#3B82F6"/>
    <line x1="351" y1="108" x2="351" y2="204" stroke="#16A34A" stroke-width="4" stroke-dasharray="5,3"/>
    <circle cx="395" cy="126" r="10" fill="#EF4444"/><circle cx="395" cy="156" r="10" fill="#EF4444"/><circle cx="395" cy="186" r="10" fill="#EF4444"/>

    <rect x="24" y="230" width="412" height="48" rx="12" fill="#FFFFFF" stroke="#C084FC" stroke-width="2"/>
    <text x="230" y="259" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#6B21A8">“本喵先把纠缠在一起的月牙拉开排成两列，最后轻轻一划就分开啦！”</text>
  </g>
</svg>
''')


# ==============================================================================
# 插画 5：修马路的哨兵三花猫（支持向量）vs. 拍蹦床的大猫爪（核函数升维）
# ==============================================================================
save_svg('pic05-border-guards-and-trampoline.svg', f'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 395" width="100%" height="auto" font-family="Microsoft YaHei, PingFang SC, sans-serif">
  <rect width="1000" height="395" rx="22" fill="#FFFBEB" stroke="#F59E0B" stroke-width="3"/>
  <rect x="24" y="18" width="952" height="46" rx="14" fill="#FEF3C7" stroke="#FBBF24" stroke-width="2"/>
  <text x="500" y="48" text-anchor="middle" font-size="20" font-weight="bold" fill="#92400E">第 5 页：压线站岗的哨兵三花猫（SVM）与拍蹦床的大猫爪（核函数）</text>

  <!-- 左：哨兵猫修马路 -->
  <g transform="translate(28, 80)">
    <rect width="460" height="292" rx="18" fill="#ECFDF5" stroke="#6EE7B7" stroke-width="2.5"/>
    <text x="230" y="32" text-anchor="middle" font-size="16" font-weight="bold" fill="#065F46">① 只有前排压线的 3 只“哨兵猫”能决定马路怎么修！</text>

    <rect x="30" y="52" width="400" height="162" rx="12" fill="#FFFFFF" stroke="#6EE7B7" stroke-width="2"/>
    <polygon points="175,52 245,52 285,214 215,214" fill="#FEF08A" opacity="0.7"/>
    <line x1="175" y1="52" x2="215" y2="214" stroke="#CA8A04" stroke-width="3" stroke-dasharray="6,4"/>
    <line x1="210" y1="52" x2="250" y2="214" stroke="#DC2626" stroke-width="4"/>
    <line x1="245" y1="52" x2="285" y2="214" stroke="#CA8A04" stroke-width="3" stroke-dasharray="6,4"/>

    <!-- 后排睡大觉的猫咪 (可忽略) -->
    {cat_avatar(75, 95, r=18, fur="#86EFAC", stroke="#15803D", mood="sleep")}
    {cat_avatar(95, 165, r=18, fur="#86EFAC", stroke="#15803D", mood="sleep")}
    <text x="85" y="204" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#15803D">后排睡大觉喵(全回家也没影响)</text>

    <!-- 前排压线哨兵猫 (支持向量) -->
    {cat_avatar(186, 102, r=20, fur="#FB923C", stroke="#DC2626", mood="happy", hat="straw")}
    {cat_avatar(204, 174, r=20, fur="#FB923C", stroke="#DC2626", mood="happy", hat="straw")}
    {cat_avatar(265, 132, r=20, fur="#F87171", stroke="#991B1B", mood="happy", hat="straw")}
    <text x="335" y="88" font-size="12" font-weight="bold" fill="#DC2626">★ 压线哨兵喵</text>
    <text x="335" y="106" font-size="11" fill="#991B1B">(叫支持向量)</text>

    {cat_avatar(372, 168, r=18, fur="#FCA5A5", stroke="#991B1B", mood="sleep")}

    <rect x="24" y="226" width="412" height="52" rx="12" fill="#FFFFFF" stroke="#34D399" stroke-width="2"/>
    <text x="230" y="257" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#047857">结论：哪怕后排 90% 的睡懒觉猫咪全跑光，大马路也一毫米都不会歪喵！</text>
  </g>

  <!-- 右：拍蹦床的大猫爪 -->
  <g transform="translate(512, 80)">
    <rect width="460" height="292" rx="18" fill="#EFF6FF" stroke="#93C5FD" stroke-width="2.5"/>
    <text x="230" y="32" text-anchor="middle" font-size="16" font-weight="bold" fill="#1E3A8A">② 甜瓜被坏瓜围在圆圈里？大猫爪从蹦床底下拍一掌！</text>

    <rect x="26" y="52" width="166" height="162" rx="12" fill="#FFFFFF" stroke="#93C5FD" stroke-width="2"/>
    <text x="109" y="74" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#1E40AF">平地上：甜瓜被包围啦</text>
    <circle cx="109" cy="142" r="46" fill="none" stroke="#EF4444" stroke-width="8" stroke-dasharray="10,7"/>
    <circle cx="98" cy="136" r="9" fill="#22C55E"/><circle cx="120" cy="136" r="9" fill="#22C55E"/><circle cx="109" cy="154" r="9" fill="#22C55E"/>

    <text x="228" y="122" text-anchor="middle" font-size="13" font-weight="bold" fill="#EA580C">大猫爪</text>
    <text x="228" y="144" text-anchor="middle" font-size="22" font-weight="bold" fill="#EA580C">🐾➔</text>
    <text x="228" y="166" text-anchor="middle" font-size="12" font-weight="bold" fill="#EA580C">啪！震飞！</text>

    <rect x="264" y="52" width="170" height="162" rx="12" fill="#FFFFFF" stroke="#93C5FD" stroke-width="2"/>
    <text x="349" y="74" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#15803D">飞到半空：飞毯平切！</text>
    <circle cx="332" cy="98" r="9" fill="#22C55E"/><circle cx="352" cy="92" r="9" fill="#22C55E"/><circle cx="368" cy="100" r="9" fill="#22C55E"/>
    <polygon points="282,132 416,120 426,138 292,150" fill="#38BDF8" opacity="0.65" stroke="#0284C7" stroke-width="2"/>
    <circle cx="305" cy="176" r="8" fill="#EF4444"/><circle cx="348" cy="184" r="8" fill="#EF4444"/><circle cx="392" cy="174" r="8" fill="#EF4444"/>

    <rect x="24" y="226" width="412" height="52" rx="12" fill="#FFFFFF" stroke="#60A5FA" stroke-width="2"/>
    <text x="230" y="257" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#1E40AF">结论：二维平面切不开？加个高度变成三维，拿飞毯平平一插就搞定喵！</text>
  </g>
</svg>
''')


# ==============================================================================
# 插画 6：蒙眼摸瓜侦探猫（随机森林）vs. 改错题画画接力猫（GBDT）
# ==============================================================================
save_svg('pic06-blindfold-vote-and-relay.svg', f'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 395" width="100%" height="auto" font-family="Microsoft YaHei, PingFang SC, sans-serif">
  <rect width="1000" height="395" rx="22" fill="#F8FAFC" stroke="#94A3B8" stroke-width="3"/>
  <rect x="24" y="18" width="952" height="46" rx="14" fill="#DCFCE7" stroke="#4ADE80" stroke-width="2"/>
  <text x="500" y="48" text-anchor="middle" font-size="20" font-weight="bold" fill="#166534">第 6 页：三个臭皮匠顶个诸葛亮！蒙眼投票猫（随机森林）与接力画画猫（GBDT）</text>

  <!-- 左：随机森林 -->
  <g transform="translate(28, 80)">
    <rect width="460" height="292" rx="18" fill="#ECFDF5" stroke="#6EE7B7" stroke-width="2.5"/>
    <text x="230" y="32" text-anchor="middle" font-size="16" font-weight="bold" fill="#065F46">① 随机森林：每只侦探猫只看 1 个线索，大家一起举爪投票！</text>

    <rect x="26" y="54" width="122" height="152" rx="12" fill="#FFFFFF" stroke="#6EE7B7" stroke-width="2"/>
    {cat_avatar(87, 100, r=22, fur="#FB923C", stroke="#9A3412", mood="happy")}
    <text x="87" y="150" text-anchor="middle" font-size="13" font-weight="bold" fill="#047857">花纹侦探喵</text>
    <text x="87" y="172" text-anchor="middle" font-size="12" fill="#15803D">“只看条纹：甜!”</text>

    <rect x="168" y="54" width="122" height="152" rx="12" fill="#FFFFFF" stroke="#6EE7B7" stroke-width="2"/>
    {cat_avatar(229, 100, r=22, fur="#94A3B8", stroke="#334155", mood="happy")}
    <text x="229" y="150" text-anchor="middle" font-size="13" font-weight="bold" fill="#047857">听声侦探喵</text>
    <text x="229" y="172" text-anchor="middle" font-size="12" fill="#15803D">“只听声音：甜!”</text>

    <rect x="310" y="54" width="122" height="152" rx="12" fill="#FFFFFF" stroke="#FCA5A5" stroke-width="2"/>
    {cat_avatar(371, 100, r=22, fur="#E2E8F0", stroke="#0F172A", mood="shock", glasses=True)}
    <text x="371" y="150" text-anchor="middle" font-size="13" font-weight="bold" fill="#B91C1C">尾巴侦探喵</text>
    <text x="371" y="172" text-anchor="middle" font-size="12" fill="#DC2626">“我看走眼：不甜”</text>

    <rect x="24" y="222" width="412" height="54" rx="12" fill="#FFFFFF" stroke="#34D399" stroke-width="2"/>
    <text x="230" y="254" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#065F46">投票结果：2 票甜 vs 1 票不甜 = 甜瓜！就算 1 只猫看走眼也不怕喵！</text>
  </g>

  <!-- 右：GBDT 错题接力赛 -->
  <g transform="translate(512, 80)">
    <rect width="460" height="292" rx="18" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="2.5"/>
    <text x="230" y="32" text-anchor="middle" font-size="16" font-weight="bold" fill="#991B1B">② GBDT 接力画画猫：后面的猫咪专门替前面的猫“补差价”！</text>

    <rect x="24" y="54" width="120" height="152" rx="12" fill="#FFFFFF" stroke="#FCA5A5" stroke-width="2"/>
    {cat_avatar(84, 96, r=20, fur="#FB923C", stroke="#9A3412", mood="happy")}
    <text x="84" y="142" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#991B1B">第 1 棒：画绿圆</text>
    <text x="84" y="164" text-anchor="middle" font-size="13" font-weight="bold" fill="#DC2626">先猜 6 分甜</text>
    <text x="84" y="186" text-anchor="middle" font-size="11.5" fill="#64748B">(还差 +4 分!)</text>

    <text x="156" y="132" text-anchor="middle" font-size="18" font-weight="bold" fill="#DC2626">+</text>

    <rect x="168" y="54" width="120" height="152" rx="12" fill="#FFFFFF" stroke="#FCA5A5" stroke-width="2"/>
    {cat_avatar(228, 96, r=20, fur="#94A3B8", stroke="#334155", mood="happy")}
    <text x="228" y="142" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#991B1B">第 2 棒：添条纹</text>
    <text x="228" y="164" text-anchor="middle" font-size="13" font-weight="bold" fill="#EA580C">专补 +3 分</text>
    <text x="228" y="186" text-anchor="middle" font-size="11.5" fill="#64748B">(还差 +1 分!)</text>

    <text x="300" y="132" text-anchor="middle" font-size="18" font-weight="bold" fill="#DC2626">+</text>

    <rect x="312" y="54" width="124" height="152" rx="12" fill="#FFFFFF" stroke="#86EFAC" stroke-width="2.5"/>
    {cat_avatar(374, 96, r=20, fur="#FACC15", stroke="#CA8A04", mood="happy", hat="straw")}
    <text x="374" y="142" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#15803D">第 3 棒：画小尾</text>
    <text x="374" y="164" text-anchor="middle" font-size="13" font-weight="bold" fill="#16A34A">补完 +1 分</text>
    <text x="374" y="186" text-anchor="middle" font-size="12" font-weight="bold" fill="#15803D">合体 = 10 分!</text>

    <rect x="24" y="222" width="412" height="54" rx="12" fill="#FFFFFF" stroke="#F87171" stroke-width="2"/>
    <text x="230" y="254" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#991B1B">秘诀：6分 + 3分 + 1分 = 10分！每只猫只盯住上一棒剩下的错题改喵！</text>
  </g>
</svg>
''')


# ==============================================================================
# 插画 7：圆规蓝猫（K-Means）vs. 魔法橡皮筋橘猫（EM 算法）
# ==============================================================================
save_svg('pic07-rubber-band-clustering.svg', f'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 395" width="100%" height="auto" font-family="Microsoft YaHei, PingFang SC, sans-serif">
  <rect width="1000" height="395" rx="22" fill="#FFFBEB" stroke="#F59E0B" stroke-width="3"/>
  <rect x="24" y="18" width="952" height="46" rx="14" fill="#FEF3C7" stroke="#FBBF24" stroke-width="2"/>
  <text x="500" y="48" text-anchor="middle" font-size="20" font-weight="bold" fill="#92400E">第 7 页：标签被大风刮跑啦！拿死板圆规的蓝猫 vs. 玩魔法橡皮筋的橘猫</text>

  <!-- 左：K-Means 死板正圆规 -->
  <g transform="translate(28, 80)">
    <rect width="460" height="292" rx="18" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="2.5"/>
    {cat_avatar(58, 46, r=22, fur="#94A3B8", stroke="#334155", mood="shock")}
    <text x="255" y="42" text-anchor="middle" font-size="16" font-weight="bold" fill="#991B1B">① 圆规蓝猫（K-Means）：只会画正圆圈，把长条冬瓜切错啦！</text>

    <rect x="30" y="72" width="400" height="142" rx="12" fill="#FFFFFF" stroke="#FCA5A5" stroke-width="2"/>
    <circle cx="155" cy="142" r="58" fill="#FEE2E2" opacity="0.65" stroke="#EF4444" stroke-width="3" stroke-dasharray="6,4"/>
    <circle cx="305" cy="142" r="58" fill="#DBEAFE" opacity="0.65" stroke="#3B82F6" stroke-width="3" stroke-dasharray="6,4"/>
    <circle cx="110" cy="112" r="9" fill="#EF4444"/><circle cx="170" cy="112" r="9" fill="#EF4444"/><circle cx="230" cy="112" r="9" fill="#EF4444"/>
    <circle cx="290" cy="112" r="9" fill="#3B82F6"/><circle cx="350" cy="112" r="9" fill="#3B82F6"/>
    <circle cx="110" cy="172" r="9" fill="#EF4444"/><circle cx="170" cy="172" r="9" fill="#EF4444"/>
    <circle cx="230" cy="172" r="9" fill="#3B82F6"/><circle cx="290" cy="172" r="9" fill="#3B82F6"/><circle cx="350" cy="172" r="9" fill="#3B82F6"/>
    <line x1="230" y1="78" x2="230" y2="206" stroke="#DC2626" stroke-width="3"/>

    <rect x="24" y="226" width="412" height="52" rx="12" fill="#FFFFFF" stroke="#F87171" stroke-width="2"/>
    <text x="230" y="257" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#B91C1C">毛病：圆规只能画正圆，把上下两条长长的冬瓜拦腰斩成左右两半喵！</text>
  </g>

  <!-- 右：EM 魔法橡皮筋 -->
  <g transform="translate(512, 80)">
    <rect width="460" height="292" rx="18" fill="#ECFDF5" stroke="#6EE7B7" stroke-width="2.5"/>
    {cat_avatar(58, 46, r=22, fur="#FB923C", stroke="#9A3412", mood="happy", hat="straw")}
    <text x="255" y="42" text-anchor="middle" font-size="16" font-weight="bold" fill="#065F46">② 橡皮筋橘猫（EM算法）：顺着瓜堆形状把橡皮筋拉长变扁！</text>

    <rect x="30" y="72" width="400" height="142" rx="12" fill="#FFFFFF" stroke="#6EE7B7" stroke-width="2"/>
    <ellipse cx="230" cy="112" rx="158" ry="24" fill="#DCFCE7" opacity="0.8" stroke="#16A34A" stroke-width="3.5"/>
    <ellipse cx="230" cy="172" rx="158" ry="24" fill="#FEF3C7" opacity="0.8" stroke="#D97706" stroke-width="3.5"/>
    <circle cx="110" cy="112" r="9" fill="#16A34A"/><circle cx="170" cy="112" r="9" fill="#16A34A"/><circle cx="230" cy="112" r="9" fill="#16A34A"/><circle cx="290" cy="112" r="9" fill="#16A34A"/><circle cx="350" cy="112" r="9" fill="#16A34A"/>
    <circle cx="110" cy="172" r="9" fill="#D97706"/><circle cx="170" cy="172" r="9" fill="#D97706"/><circle cx="230" cy="172" r="9" fill="#D97706"/><circle cx="290" cy="172" r="9" fill="#D97706"/><circle cx="350" cy="172" r="9" fill="#D97706"/>

    <rect x="24" y="226" width="412" height="52" rx="12" fill="#FFFFFF" stroke="#34D399" stroke-width="2"/>
    <text x="230" y="257" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#047857">聪明：第1步猜瓜归谁（E步），第2步拉长橡皮筋（M步），两排冬瓜完美分开！</text>
  </g>
</svg>
''')


# ==============================================================================
# 插画 8：猫咪蛋糕房捉虫记（反向传播 BP 与手搓 Autograd）
# ==============================================================================
save_svg('pic08-kitchen-whisper.svg', f'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 395" width="100%" height="auto" font-family="Microsoft YaHei, PingFang SC, sans-serif">
  <rect width="1000" height="395" rx="22" fill="#F8FAFC" stroke="#94A3B8" stroke-width="3"/>
  <rect x="24" y="18" width="952" height="46" rx="14" fill="#FEE2E2" stroke="#F87171" stroke-width="2"/>
  <text x="500" y="48" text-anchor="middle" font-size="20" font-weight="bold" fill="#991B1B">第 8 页：西瓜蛋糕做咸啦！猫咪厨房怎么靠“倒着喊一嗓子”抓出闯祸猫？（反向传播）</text>

  <!-- 上半部分：正向做蛋糕流水线 -->
  <g transform="translate(32, 78)">
    <rect width="936" height="128" rx="16" fill="#EFF6FF" stroke="#93C5FD" stroke-width="2.5"/>
    <text x="468" y="24" text-anchor="middle" font-size="15" font-weight="bold" fill="#1E3A8A">👉 第一趟（正向做蛋糕）：四只小猫排成流水线做西瓜蛋糕</text>

    <rect x="28" y="38" width="178" height="76" rx="12" fill="#FFFFFF" stroke="#60A5FA" stroke-width="2"/>
    {cat_avatar(64, 78, r=20, fur="#D6D3D1", stroke="#44403C", mood="happy", hat="chef")}
    <text x="142" y="72" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#1E293B">① 揉面喵</text>
    <text x="142" y="94" text-anchor="middle" font-size="11.5" fill="#047857">面粉刚刚好</text>

    <text x="228" y="82" text-anchor="middle" font-size="22" font-weight="bold" fill="#3B82F6">➔</text>

    <rect x="252" y="38" width="196" height="76" rx="12" fill="#FEF2F2" stroke="#EF4444" stroke-width="3"/>
    {cat_avatar(290, 78, r=20, fur="#E2E8F0", stroke="#0F172A", mood="shock", hat="chef")}
    <text x="372" y="72" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#DC2626">② 撒盐喵(闯祸!)</text>
    <text x="372" y="94" text-anchor="middle" font-size="11.5" font-weight="bold" fill="#B91C1C">爪子抖多撒 5 勺盐</text>

    <text x="470" y="82" text-anchor="middle" font-size="22" font-weight="bold" fill="#3B82F6">➔</text>

    <rect x="494" y="38" width="178" height="76" rx="12" fill="#FFFFFF" stroke="#60A5FA" stroke-width="2"/>
    {cat_avatar(530, 78, r=20, fur="#94A3B8", stroke="#334155", mood="happy", hat="chef")}
    <text x="608" y="72" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#1E293B">③ 烤箱喵</text>
    <text x="608" y="94" text-anchor="middle" font-size="11.5" fill="#047857">火候刚刚好</text>

    <text x="694" y="82" text-anchor="middle" font-size="22" font-weight="bold" fill="#3B82F6">➔</text>

    <rect x="718" y="38" width="192" height="76" rx="12" fill="#FFFBEB" stroke="#F59E0B" stroke-width="2.5"/>
    {cat_avatar(756, 78, r=20, fur="#FB923C", stroke="#9A3412", mood="shock", hat="straw")}
    <text x="840" y="72" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#B45309">④ 店长试吃喵</text>
    <text x="840" y="94" text-anchor="middle" font-size="12" font-weight="bold" fill="#DC2626">“呸呸！咸死本喵啦!”</text>
  </g>

  <!-- 下半部分：反向传播捉虫 -->
  <g transform="translate(32, 222)">
    <rect width="936" height="148" rx="16" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="2.5"/>
    <text x="468" y="28" text-anchor="middle" font-size="15.5" font-weight="bold" fill="#991B1B">👈 第二趟（反向传播 backward）：拿大喇叭从后往前倒着查账本，喊 1 嗓子就破案！</text>

    <path d="M 800 55 C 660 105, 500 105, 355 55" fill="none" stroke="#DC2626" stroke-width="5" stroke-dasharray="8,4"/>
    <polygon points="355,55 372,52 366,68" fill="#DC2626"/>
    <rect x="435" y="54" width="280" height="34" rx="10" fill="#DC2626"/>
    <text x="575" y="76" text-anchor="middle" font-size="13" font-weight="bold" fill="#FFFFFF">📣 反向传话：“查清啦！全是盐太多惹的祸！”</text>

    <rect x="28" y="98" width="880" height="38" rx="10" fill="#FFFFFF" stroke="#F87171" stroke-width="2"/>
    <text x="468" y="122" text-anchor="middle" font-size="13.5" font-weight="bold" fill="#7F1D1D">神奇对比：笨办法要让 10000 只厨师猫挨个重做一万次蛋糕；【反向传播】顺着小账本倒着喊 1 嗓子，全员立刻知道怎么改喵！</text>
  </g>
</svg>
''')
