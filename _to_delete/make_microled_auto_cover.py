"""
PIL 程序化合成 MicroLED 车载驱动封面（汽车剪影 + HUD/前大灯/座舱 + 深色科技风）
依赖：仅系统 Python 自带 PIL
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

W, H = 1200, 750
OUT = r"D:/AI共享文件夹/nexlamp-website/images/blog-microled-automotive-hud-driver-cover.png"

# 颜色
BG = (10, 18, 38)
BG2 = (15, 32, 60)
ORANGE = (245, 158, 11)
ORANGE_HOT = (251, 191, 36)
BLUE = (59, 130, 246)
TEAL = (94, 234, 212)
WHITE = (255, 255, 255)
GRAY = (148, 163, 184)
DARK = (15, 23, 42)

# 创建底图
img = Image.new('RGB', (W, H), BG)
draw = ImageDraw.Draw(img)

# 1) 渐变背景
for y in range(H):
    ratio = y / H
    r = int(10 + ratio * 5)
    g = int(18 + ratio * 12)
    b = int(38 + ratio * 22)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# 2) 网格线（淡淡蓝）
for x in range(0, W, 60):
    draw.line([(x, 0), (x, H)], fill=(20, 30, 50))
for y in range(0, H, 60):
    draw.line([(0, y), (W, y)], fill=(20, 30, 50))

# 3) 右侧光晕（橙色）
for radius, alpha in [(400, 25), (250, 35), (140, 50)]:
    overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.ellipse([900 - radius, 100 - radius, 900 + radius, 100 + radius],
               fill=(245, 158, 11, alpha))
    overlay = overlay.filter(ImageFilter.GaussianBlur(80))
    img.paste(overlay, (0, 0), overlay)

# 4) 汽车轮廓剪影（左侧）
# 车顶
draw.polygon([(80, 480), (200, 380), (550, 380), (620, 480)],
             fill=(30, 41, 59))
# 车身
draw.rounded_rectangle((60, 470, 700, 580), radius=18, fill=(30, 41, 59))
# 车窗（前挡风+侧窗）
draw.polygon([(220, 395), (260, 460), (560, 460), (590, 395)], fill=(20, 30, 56))
# 大灯（左前）
draw.ellipse([80, 470, 145, 535], fill=(245, 158, 11))
# 大灯 + 像素阵列效果
for r in range(20, 0, -3):
    alpha = int(255 * (1 - r/20) * 0.8)
    od_img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(od_img).ellipse([112 - r, 502 - r, 112 + r, 502 + r], fill=(251, 191, 36, alpha))
    blur_img = od_img.filter(ImageFilter.GaussianBlur(5))
    img.paste(blur_img, (0, 0), blur_img)

# 灯内像素阵列（ADB 像素化效果）
draw.ellipse([110, 500, 116, 506], fill=(255, 255, 255))
draw.ellipse([118, 502, 124, 508], fill=(251, 191, 36))
draw.ellipse([100, 500, 106, 506], fill=(251, 191, 36))

# 尾灯（红色微光）
tail_img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
ImageDraw.Draw(tail_img).ellipse([690 - 15, 510 - 15, 690 + 15, 510 + 15], fill=(239, 68, 68, 200))
tail_blur = tail_img.filter(ImageFilter.GaussianBlur(8))
img.paste(tail_blur, (0, 0), tail_blur)

# 车轮
draw.ellipse([150, 580, 220, 640], fill=(15, 23, 42))
draw.ellipse([162, 590, 208, 628], fill=(71, 85, 105))
draw.ellipse([500, 580, 570, 640], fill=(15, 23, 42))
draw.ellipse([512, 590, 558, 628], fill=(71, 85, 105))

# 5) HUD抬头显示区域（车前上方投影）
hud_box = (100, 220, 540, 360)
draw.rounded_rectangle(hud_box, radius=10, outline=ORANGE, width=2)
# HUD内部线条
for i in range(0, 440, 8):
    alpha = int(120 - abs(i - 220) * 0.4)
    if alpha > 0:
        draw.line([(105, 220 + i), (535, 220 + i)], fill=(245, 158, 11, alpha))

# HUD 像素MicroLED方阵（示意）
for row in range(8):
    for col in range(28):
        x = 120 + col * 14
        y = 240 + row * 12
        color = ORANGE if (row + col) % 5 == 0 else (60, 80, 110)
        draw.rectangle([x, y, x+8, y+8], fill=color)

# 6) 右侧顶部 5道关卡面板
def card(x, y, w, h, label, value, sub, accent=ORANGE):
    draw.rounded_rectangle((x, y, x + w, y + h), radius=8,
                           fill=(15, 32, 60), outline=accent, width=1)
    try:
        font_lbl = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 14)
        font_val = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 18)
        font_sub = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 12)
    except Exception:
        font_lbl = ImageFont.load_default()
        font_val = ImageFont.load_default()
        font_sub = ImageFont.load_default()
    draw.text((x + 14, y + 12), label, fill=accent, font=font_lbl)
    draw.text((x + 14, y + 32), value, fill=WHITE, font=font_val)
    draw.text((x + 14, y + 60), sub, fill=GRAY, font=font_sub)

cards = [
    ("GATE 1", "AEC-Q100 魔鬼月考", "HTOL/HAST/TMCL · 12-18 个月"),
    ("GATE 2", "HUD 15000 cd/m²", "1ms 暗→全亮跳变 · 0.5% 电流精度"),
    ("GATE 3", "CAN-FD / 1000BASE-T1", "SecOC 防注入 · AutoSAR CP/AP"),
    ("GATE 4", "ISO 26262 ASIL-B/C/D", "双通道冗余 · DTTI < 100ms"),
    ("GATE 5", "15年 / 24万公里寿命", "+150℃结温红线 · 三防漆"),
]
y0 = 80
for i, (l, v, s) in enumerate(cards):
    card(760 + (i % 2) * 210, y0 + (i // 2) * 90, 200, 78, l, v, s)

# 7) 标题（顶部居中）
try:
    font_title = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 44)
    font_sub = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 18)
except Exception:
    font_title = ImageFont.load_default()
    font_sub = ImageFont.load_default()

title = "MicroLED 上车"
draw.text((76, 60), title, fill=WHITE, font=font_title)

# 副标题
sub1 = "车载 HUD · 座舱一体屏 · 自适应前大灯"
draw.text((80, 122), sub1, fill=ORANGE_HOT, font=font_sub)

# 第二行副标题
sub2 = "LED 驱动电源 · 5 道车规关"
draw.text((80, 146), sub2, fill=GRAY, font=font_sub)

# 8) 底部横条
draw.rectangle([0, 690, W, 750], fill=(15, 32, 60))
draw.line([(0, 690), (W, 690)], fill=ORANGE, width=2)
try:
    font_meta = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 14)
except Exception:
    font_meta = ImageFont.load_default()
draw.text((80, 705), "Diodes AL8866Q · AEC-Q100 Grade 1 · CISPR 25 Class 5 · ISO 26262",
          fill=GRAY, font=font_meta)
draw.text((80, 725), "nexlamp.com · 2026-08-21", fill=TEAL, font=font_meta)

img.save(OUT, optimize=True, quality=92)
print("OK:", OUT)
