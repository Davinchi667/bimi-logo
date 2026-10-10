#!/usr/bin/env python3
"""Rasterise an SVG (a brand logo, say) to a transparent PNG with Chromium.
  svg_to_png.py in.svg out.png --width 1200
Use when a logo SVG does not survive path extraction (fill rules, nested transforms, strokes)."""
import sys, io, re
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import render as R
from PIL import Image


def svg_to_png(src, out, width=1200):
    svg = Path(src).read_text()
    m = re.search(r'viewBox="([\d.\s-]+)"', svg)
    vb = [float(v) for v in m.group(1).split()] if m else [0, 0, 600, 200]
    h = int(width * vb[3] / vb[2])
    svg = re.sub(r'\swidth="[^"]*"', "", svg, count=1); svg = re.sub(r'\sheight="[^"]*"', "", svg, count=1)
    svg = svg.replace("<svg", f'<svg width="{width}" height="{h}"', 1)
    b = R._get_browser()
    ctx = b.new_context(viewport={"width": width, "height": h}, device_scale_factor=1)
    page = ctx.new_page()
    page.set_content(f"<html><body style='margin:0;background:transparent'>{svg}</body></html>")
    data = page.screenshot(type="png", omit_background=True, clip={"x": 0, "y": 0, "width": width, "height": h})
    ctx.close()
    Image.open(io.BytesIO(data)).save(out)
    return out


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(); ap.add_argument("src"); ap.add_argument("out"); ap.add_argument("--width", type=int, default=1200)
    a = ap.parse_args()
    try:
        print(svg_to_png(a.src, a.out, a.width))
    finally:
        R.close()
