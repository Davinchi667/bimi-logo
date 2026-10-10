#!/usr/bin/env python3
"""Lay every brand's final 600 px PNG side by side at one scale.
  batch_overview.py brands/BATCH_2026-10-10_overview.jpg [--scale 0.25] [--skip _demo,graza]"""
import sys, argparse
from pathlib import Path
from PIL import Image, ImageDraw
ROOT = Path(__file__).resolve().parent.parent
ap = argparse.ArgumentParser(); ap.add_argument("out"); ap.add_argument("--scale", type=float, default=0.25); ap.add_argument("--skip", default="_demo,graza")
a = ap.parse_args()
skip = set(a.skip.split(","))
pngs = []
for b in sorted((ROOT / "brands").iterdir()):
    if not b.is_dir() or b.name in skip: continue
    f = b / "final" / f"{b.name}_welcome-01_600.png"
    if f.exists(): pngs.append((b.name, Image.open(f).convert("RGB")))
w = int(600 * a.scale); pad = 16; label_h = 22
H = max(int(im.height * a.scale) for _, im in pngs) + label_h + 2 * pad
sheet = Image.new("RGB", (len(pngs) * (w + pad) + pad, H), "#D9D9D9"); d = ImageDraw.Draw(sheet)
for i, (name, im) in enumerate(pngs):
    x = pad + i * (w + pad)
    t = im.resize((w, int(im.height * a.scale)), Image.LANCZOS)
    sheet.paste(t, (x, pad + label_h)); d.text((x, pad + 4), f"{name}  {im.height}px", fill="#000")
sheet.save(a.out, quality=88); print(a.out, len(pngs), "brands", sheet.size)
