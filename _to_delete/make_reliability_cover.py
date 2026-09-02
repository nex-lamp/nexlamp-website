# -*- coding: utf-8 -*-
"""PIL 合成封面图 - GB/T 33721+32481 国标升级"""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 750
BG = (10, 22, 40)
GRID = (26, 48, 80)
ACCENT = (126, 184, 255)      # 科技蓝
ACCENT2 = (255, 140, 90)      # 橙红警示
ACCENT3 = (160, 224, 160)     # 绿色合规
YELLOW = (255, 208, 90)
WHITE = (240, 245, 250)
DIM = (154, 168, 184)

# 字体路径
FONT_CANDIDATES = [
    r"C:\Windows\Fonts\msyhbd.ttc",
    r"C:\Windows\Fonts\msyh.ttc",
    r"C:\Windows\Fonts\simhei.ttf",
    r"C:\Windows\Fonts\simsun.ttc",
]
FONT_REG = [
    r"C:\Windows\Fonts\msyh.ttc",
    r"C:\Windows\Fonts\msyhbd.ttc",
    r"C:\Windows\Fonts\simhei.ttf",
    r"C:\Windows\Fonts\simsun.ttc",
]

def get_font(paths, size):
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except (OSError, IOError):
            continue
    return ImageFont.load_default()

font_h1 = get_font(FONT_CANDIDATES, 64)
font_h2 = get_font(FONT_CANDIDATES, 32)
font_h3 = get_font(FONT_CANDIDATES, 24)
font_reg = get_font(FONT_REG, 18)
font_small = get_font(FONT_REG, 16)

# 创建背景
img = Image.new('RGB', (W, H), BG)
draw = ImageDraw.Draw(img)

# 网格底纹
for x in range(0, W, 40):
    draw.line([(x, 0), (x, H)], fill=GRID, width=1)
for y in range(0, H, 40):
    draw.line([(0, y), (W, y)], fill=GRID, width=1)

# 渐变光晕（顶部右上）
glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
gdraw = ImageDraw.Draw(glow)
for i in range(50, 0, -1):
    alpha = int(255 * (1 - i/50) * 0.3)
    radius = i * 12
    cx, cy = W - 150, 150
    color = (*ACCENT, alpha)
    gdraw.ellipse([cx-radius, cy-radius, cx+radius, cy+radius], fill=color)
glow = glow.filter(ImageFilter.GaussianBlur(40))
img.paste(glow, (0, 0), glow)

# 渐变光晕（左下）
glow2 = Image.new('RGBA', (W, H), (0, 0, 0, 0))
g2d = ImageDraw.Draw(glow2)
for i in range(40, 0, -1):
    alpha = int(255 * (1 - i/40) * 0.2)
    radius = i * 14
    cx, cy = 200, H - 100
    color = (*ACCENT2, alpha)
    g2d.ellipse([cx-radius, cy-radius, cx+radius, cy+radius], fill=color)
glow2 = glow2.filter(ImageFilter.GaussianBlur(45))
img.paste(glow2, (0, 0), glow2)

draw = ImageDraw.Draw(img)

# 顶部品牌条
draw.rectangle([(0, 0), (W, 6)], fill=ACCENT)
draw.rectangle([(0, H-6), (W, H)], fill=ACCENT)

# 顶部 chip
chip_y = 50
draw.rectangle([(60, chip_y), (240, chip_y+30)], outline=ACCENT, width=2)
draw.text((75, chip_y+5), "GB/T 2026 NEW", fill=ACCENT, font=font_reg)

# 主标题
draw.text((60, 105), "11月1日", fill=ACCENT2, font=font_h1)
draw.text((60, 195), "两项LED国标同步升级", fill=WHITE, font=font_h1)

# 副标题（标准号）
sub_y = 320
draw.rectangle([(60, sub_y), (650, sub_y+44)], outline=ACCENT, width=2)
draw.text((80, sub_y+8), "GB/T 33721-2026", fill=WHITE, font=font_h2)
draw.text((360, sub_y+12), "可靠性试验方法", fill=DIM, font=font_reg)

sub2_y = 380
draw.rectangle([(60, sub2_y), (650, sub2_y+44)], outline=ACCENT, width=2)
draw.text((80, sub2_y+8), "GB/T 32481-2026", fill=WHITE, font=font_h2)
draw.text((360, sub2_y+12), "隧道LED灯具性能规范", fill=DIM, font=font_reg)

# 中部资讯
mid_y = 460
draw.text((60, mid_y), "· 18 项可靠性试验首次系统化写入国标", fill=WHITE, font=font_reg)
draw.text((60, mid_y+30), "· 驱动电源 BOM 升级: 105°C 长寿命电容 / 10kV 浪涌", fill=WHITE, font=font_reg)
draw.text((60, mid_y+60), "· 隧道 LED 7×24 不死机 · 光通维持寿命双曲线验证", fill=WHITE, font=font_reg)
draw.text((60, mid_y+90), "· 距离实施仅剩 60 天 — 工厂应对清单见正文", fill=YELLOW, font=font_reg)

# 右侧倒计时面板
panel_x, panel_y = 800, 105
panel_w, panel_h = 340, 230
draw.rectangle([(panel_x, panel_y), (panel_x+panel_w, panel_y+panel_h)], outline=ACCENT2, width=3)
# 面板填充（半透明橙红色蒙版）
overlay_panel = Image.new('RGBA', (panel_w, panel_h), (0, 0, 0, 0))
opd = ImageDraw.Draw(overlay_panel)
opd.rectangle([(0, 0), (panel_w, panel_h)], fill=(255, 140, 90, 40))
img.paste(overlay_panel, (panel_x, panel_y), overlay_panel)

draw = ImageDraw.Draw(img)

draw.text((panel_x+30, panel_y+25), "实施倒计时", fill=ACCENT2, font=font_h3)
draw.text((panel_x+30, panel_y+60), "60", fill=WHITE, font=ImageFont.truetype(FONT_CANDIDATES[0], 110))
draw.text((panel_x+200, panel_y+110), "天", fill=WHITE, font=font_h2)
draw.text((panel_x+30, panel_y+155), "2026 / 11 / 01", fill=YELLOW, font=font_h2)
draw.text((panel_x+30, panel_y+195), "全国标准信息公共服务平台", fill=DIM, font=font_small)

# 底部 logo
draw.text((60, H-60), "NEXLAMP", fill=ACCENT, font=font_h3)
draw.text((60, H-32), "LED 驱动电源 · 视角观察", fill=DIM, font=font_small)

# 底部右侧
draw.text((W-380, H-50), "nexlamp.com", fill=ACCENT, font=font_reg)
draw.text((W-380, H-28), "文章 ID: 2026-08-26-33721-32481", fill=DIM, font=font_small)

# 装饰电路元素（左下角）
circuit_y = H - 180
draw.line([(60, circuit_y), (220, circuit_y)], fill=ACCENT, width=2)
draw.line([(60, circuit_y+30), (180, circuit_y+30)], fill=ACCENT, width=2)
draw.line([(60, circuit_y+60), (240, circuit_y+60)], fill=ACCENT2, width=2)
# 节点
for (x, y) in [(140, circuit_y), (180, circuit_y+30), (200, circuit_y+60), (90, circuit_y), (90, circuit_y+60)]:
    draw.ellipse([(x-4, y-4), (x+4, y+4)], fill=ACCENT)

# 右上芯片轮廓
chip_x, chip_y2 = W-260, 35
chip_w, chip_h = 200, 60
draw.rectangle([(chip_x, chip_y2), (chip_x+chip_w, chip_y2+chip_h)], outline=ACCENT, width=1)
draw.rectangle([(chip_x-10, chip_y2+10), (chip_x-5, chip_y2+20)], fill=ACCENT)
draw.rectangle([(chip_x-10, chip_y2+30), (chip_x-5, chip_y2+40)], fill=ACCENT)
draw.rectangle([(chip_x-10, chip_y2+50), (chip_x-5, chip_y2+60)], fill=ACCENT)
draw.text((chip_x+15, chip_y2+5), "RELIABILITY", fill=ACCENT, font=font_small)
draw.text((chip_x+15, chip_y2+25), "DRIVER MCU", fill=WHITE, font=font_small)
draw.text((chip_x+15, chip_y2+45), "2026-11-01", fill=YELLOW, font=font_small)

# 保存
out = r"d:\AI共享文件夹\nexlamp-website\images\blog-gbt-33721-32481-reliability-cover.png"
img.save(out, "PNG", optimize=True)
print(f"OK: {out}")
print(f"Size: {W}x{H}")
