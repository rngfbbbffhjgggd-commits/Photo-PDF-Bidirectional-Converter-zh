# -*- coding: utf-8 -*-
"""生成一个醒目的「图片转PDF」桌面图标：蓝色渐变圆角底 + 白色纸张 + 红色 PDF 字标 + 折角。
输出：assets/app.ico（多尺寸）与 assets/app_preview.png（预览图）。"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BASE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(BASE, "assets")
os.makedirs(ASSETS, exist_ok=True)

S = 1024          # 高分辨率绘制
C1 = (37, 99, 235)     # #2563EB 蓝
C2 = (49, 46, 129)     # #312E81 深蓝紫
PAGE = (255, 255, 255, 255)
PDF_RED = (225, 29, 72)   # #E11D48 红
SHADOW = (30, 41, 59, 90)


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def rounded_mask(size, radius):
    m = Image.new("L", (size, size), 0)
    md = ImageDraw.Draw(m)
    md.rounded_rectangle([0, 0, size - 1, size - 1], radius=radius, fill=255)
    return m


# 1) 垂直渐变圆角背景
grad = Image.new("RGB", (S, S))
gd = ImageDraw.Draw(grad)
for y in range(S):
    t = y / (S - 1)
    gd.line([(0, y), (S, y)], fill=lerp(C1, C2, t))
back = Image.new("RGBA", (S, S))
back.paste(grad, (0, 0))
back.putalpha(rounded_mask(S, int(S * 0.22)))

draw = ImageDraw.Draw(back)

# 2) 纸张投影
page_w = int(S * 0.60)
page_h = int(S * 0.74)
px = (S - page_w) // 2
py = (S - page_h) // 2
shadow = Image.new("RGBA", (S, S), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.rounded_rectangle([px, py, px + page_w, py + page_h], radius=int(S * 0.05), fill=SHADOW)
shadow = shadow.filter(ImageFilter.GaussianBlur(S * 0.03))
back.alpha_composite(shadow)

# 3) 白色纸张（圆角）
draw.rounded_rectangle([px, py, px + page_w, py + page_h], radius=int(S * 0.05), fill=PAGE)

# 4) 顶部蓝色标题条
bar_h = int(page_h * 0.16)
draw.rounded_rectangle(
    [px, py, px + page_w, py + bar_h],
    radius=int(S * 0.05),
    fill=lerp(C1, C2, 0.2),
)

# 5) 折角（右下）
fold = int(page_w * 0.18)
fx = px + page_w
fy = py + page_h
draw.polygon([(fx - fold, fy), (fx, fy), (fx, fy - fold)], fill=(203, 213, 225, 255))  # 折角背面浅灰
draw.polygon([(fx - fold, fy - fold), (fx, fy - fold), (fx - fold, fy)], fill=(226, 232, 240, 255))  # 折痕亮面

# 6) PDF 字标（居中，红色粗体，带轻微投影）
latin_font = next((p for p in [
    r"C:\Windows\Fonts\arialbd.ttf",
    r"C:\Windows\Fonts\segoeuib.ttf",
] if os.path.exists(p)), None)
cjk_font = next((p for p in [
    r"C:\Windows\Fonts\msyhbd.ttc",
    r"C:\Windows\Fonts\msyh.ttc",
    r"C:\Windows\Fonts\simhei.ttf",
] if os.path.exists(p)), None)
big = ImageFont.truetype(latin_font, int(page_h * 0.34))
msg = "PDF"
bbox = draw.textbbox((0, 0), msg, font=big)
tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
tx = px + (page_w - tw) // 2 - bbox[0]
ty = py + int(page_h * 0.50) - th // 2 - bbox[1]
# 阴影
draw.text((tx + 6, ty + 6), msg, font=big, fill=(0, 0, 0, 40))
draw.text((tx, ty), msg, font=big, fill=PDF_RED)

# 7) 底部说明小字（中文，微软雅黑）
if cjk_font:
    small_font = ImageFont.truetype(cjk_font, int(page_h * 0.072))
    labels = ["图片", "转", "PDF"]
    lw = [draw.textlength(t, font=small_font) for t in labels]
    gap = int(S * 0.012)
    total = sum(lw) + gap * (len(labels) - 1)
    x0 = px + (page_w - total) // 2
    lab_y = py + int(page_h * 0.74)
    for t, w in zip(labels, lw):
        draw.text((x0, lab_y), t, font=small_font, fill=(100, 116, 139, 255))
        x0 += w + gap

# 8) 透明圆角外框裁切（确保角外透明）
final = Image.new("RGBA", (S, S))
final.paste(back, (0, 0), rounded_mask(S, int(S * 0.22)))

# 预览图 + 多尺寸 ICO
preview = final.resize((256, 256), Image.LANCZOS)
preview.save(os.path.join(ASSETS, "app_preview.png"))

ico = final.resize((256, 256), Image.LANCZOS)
ico.save(os.path.join(ASSETS, "app.ico"),
         format="ICO",
         sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
print("已生成：")
print(os.path.join(ASSETS, "app.ico"), os.path.getsize(os.path.join(ASSETS, "app.ico")), "bytes")
print(os.path.join(ASSETS, "app_preview.png"), os.path.getsize(os.path.join(ASSETS, "app_preview.png")), "bytes")
