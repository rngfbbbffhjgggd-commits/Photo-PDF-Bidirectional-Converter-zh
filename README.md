# 图片转高质量 PDF（汉化版）

一个 Windows 桌面应用：把图片转成 PDF，也能把 PDF 页面转回图片。
本仓库是 **SagarBiswas-MultiHAT/Photo-PDF-Bidirectional-Converter** 的**汉化版**，
界面已全部翻译为中文，转换逻辑保持原样。原项目为 MIT 协议，版权归原作者所有。

## 功能

- **图片 → PDF**
  - **合并为单个 PDF（多页）**：所有图片合成一个 PDF，每张一页。
  - **每张图片单独一个 PDF**：每张图片各自生成一个 PDF。
  - 批量选择、排序（上移/下移）、按名称排序、移除、清空。
  - 质量与页面尺寸：自动/手动 DPI、按像素、A4/Letter、边距、嵌入方式、JPEG 质量。
  - 按 EXIF 自动旋转、可写入 PDF 元数据（标题/作者）。
- **PDF → 图片**：把 PDF 每页导出为 PNG 或 JPG，可设渲染 DPI。

## 界面语言

中文（本汉化版）。

## 运行环境

- Windows
- Python 3.8+
- 依赖：`Pillow`、`reportlab`、`img2pdf`、`PyMuPDF`

## 运行方式

```powershell
# 创建虚拟环境并安装依赖（首次）
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt

# 启动应用
.\.venv\Scripts\python.exe Photo-PDF-Bidirectional-Converter.py
```

Windows 下也可直接双击项目里的 `启动.bat`。

## 致谢

- 原作者 & 原项目：[SagarBiswas-MultiHAT/Photo-PDF-Bidirectional-Converter](https://github.com/SagarBiswas-MultiHAT/Photo-PDF-Bidirectional-Converter)
- 协议：MIT（详见 `LICENSE`）
