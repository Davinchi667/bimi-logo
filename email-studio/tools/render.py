#!/usr/bin/env python3
"""Render an email SVG with Chromium (Playwright) using the exact font files.

  render.py email.svg --out final/ --fonts-from build.py [--name brand_welcome-01]

Writes  <name>_600.png, <name>_1200.png, review/slice_01.png ... (600 px tall
slices at 1x for close reading) and review/contact_sheet.png (all slices in a grid).

Library use: render_svg(svg_text, fonts, scale) -> PIL.Image
"""
from __future__ import annotations

import io
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from emailkit.fonts import FontRegistry  # noqa: E402

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

_pw = None
_browser = None


def _get_browser():
    global _pw, _browser
    if _browser is None:
        from playwright.sync_api import sync_playwright
        _pw = sync_playwright().start()
        try:
            _browser = _pw.chromium.launch()
        except Exception:
            _browser = _pw.chromium.launch(executable_path=CHROME)
    return _browser


def close():
    global _pw, _browser
    if _browser:
        _browser.close()
        _browser = None
    if _pw:
        _pw.stop()
        _pw = None


def _html(svg_text: str, fonts: FontRegistry | None, width: int, height: int) -> str:
    css = fonts.font_face_css(as_data_uri=True) if fonts else ""
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{css}"
            f"html,body{{margin:0;padding:0;background:#fff;}}svg{{display:block}}</style></head>"
            f"<body>{svg_text}</body></html>")


def _svg_size(svg_text: str) -> tuple[int, int]:
    import re
    w = re.search(r'<svg[^>]*\swidth="(\d+)', svg_text)
    h = re.search(r'<svg[^>]*\sheight="(\d+)', svg_text)
    return int(w.group(1)) if w else 600, int(h.group(1)) if h else 1000


def render_svg(svg_text: str, fonts: FontRegistry | None = None, scale: int = 1, clip=None) -> Image.Image:
    """Render SVG text to a PIL image at `scale` device pixels per CSS px.
    clip=(x, y, w, h) renders only that band (CSS px)."""
    w, h = _svg_size(svg_text)
    b = _get_browser()
    ctx = b.new_context(viewport={"width": w, "height": min(h, 4000)}, device_scale_factor=scale)
    page = ctx.new_page()
    page.set_content(_html(svg_text, fonts, w, h), wait_until="load")
    page.evaluate("document.fonts.ready")
    page.wait_for_timeout(150)
    kw = {"type": "png", "full_page": True}
    if clip:
        kw["clip"] = {"x": clip[0], "y": clip[1], "width": clip[2], "height": clip[3]}
        kw["full_page"] = True
    data = page.screenshot(**kw)
    ctx.close()
    return Image.open(io.BytesIO(data)).convert("RGBA")


def contact_sheet(im: Image.Image, slice_h: int = 600, cols: int = 4, thumb_w: int = 300) -> tuple[Image.Image, list[Image.Image]]:
    slices = []
    for y in range(0, im.height, slice_h):
        slices.append(im.crop((0, y, im.width, min(im.height, y + slice_h))))
    rows = math.ceil(len(slices) / cols)
    th = int(slice_h * thumb_w / im.width)
    pad = 16
    sheet = Image.new("RGB", (cols * (thumb_w + pad) + pad, rows * (th + pad + 18) + pad), "#DDDDDD")
    d = ImageDraw.Draw(sheet)
    for i, s in enumerate(slices):
        r, c = divmod(i, cols)
        x = pad + c * (thumb_w + pad)
        y = pad + r * (th + pad + 18)
        t = s.convert("RGB").resize((thumb_w, max(1, int(s.height * thumb_w / s.width))), Image.LANCZOS)
        sheet.paste(t, (x, y + 18))
        d.text((x, y + 2), f"slice {i + 1:02d}  y={i * slice_h}", fill="#000")
    return sheet, slices


def render_all(svg_path: str, out_dir: str, fonts: FontRegistry | None, name: str | None = None) -> dict:
    svg_text = Path(svg_path).read_text(encoding="utf-8")
    name = name or Path(svg_path).stem
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "review").mkdir(exist_ok=True)
    im1 = render_svg(svg_text, fonts, 1)
    im2 = render_svg(svg_text, fonts, 2)
    p1 = out / f"{name}_600.png"
    p2 = out / f"{name}_1200.png"
    im1.convert("RGB").save(p1, optimize=True)
    im2.convert("RGB").save(p2, optimize=True)
    sheet, slices = contact_sheet(im1)
    sheet.save(out / "review" / "contact_sheet.png")
    for i, s in enumerate(slices):
        s.convert("RGB").save(out / "review" / f"slice_{i + 1:02d}.png")
    return {"png_600": str(p1), "png_1200": str(p2), "height": im1.height, "slices": len(slices)}


if __name__ == "__main__":
    import argparse
    from validate_svg import load_fonts_from_build
    ap = argparse.ArgumentParser()
    ap.add_argument("svg")
    ap.add_argument("--out", required=True)
    ap.add_argument("--fonts-from")
    ap.add_argument("--name")
    a = ap.parse_args()
    reg = load_fonts_from_build(a.fonts_from) if a.fonts_from else None
    try:
        print(render_all(a.svg, a.out, reg, a.name))
    finally:
        close()
