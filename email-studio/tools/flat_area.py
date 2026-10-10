#!/usr/bin/env python3
"""Flat-area check: share of the email that is one flat colour, in 10 px blocks.

A block is flat when every channel's range inside it is <= `tol` (default 6 of
255). The brief wants under 60 % flat. Also writes an optional heatmap PNG
where flat blocks are greyed so you can see where the dead areas are.

  flat_area.py email_600.png [--heatmap out.png] [--block 10] [--tol 6]
Library: flat_ratio(path) -> (ratio, heatmap_image)
"""
from __future__ import annotations

import sys
import numpy as np
from PIL import Image

LIMIT = 0.60


def flat_ratio(path: str, block: int = 10, tol: int = 6):
    im = Image.open(path).convert("RGB")
    a = np.asarray(im).astype(np.int16)
    h, w, _ = a.shape
    H, W = h // block, w // block
    a = a[:H * block, :W * block]
    blocks = a.reshape(H, block, W, block, 3).transpose(0, 2, 1, 3, 4).reshape(H, W, block * block, 3)
    rng = blocks.max(axis=2) - blocks.min(axis=2)
    flat = (rng.max(axis=2) <= tol)
    ratio = float(flat.mean())
    heat = im.copy()
    arr = np.asarray(heat).copy()
    for by in range(H):
        for bx in range(W):
            if flat[by, bx]:
                sl = arr[by * block:(by + 1) * block, bx * block:(bx + 1) * block]
                arr[by * block:(by + 1) * block, bx * block:(bx + 1) * block] = (sl * 0.35 + np.array([255, 0, 120]) * 0.65).astype(np.uint8)
    # per-section-ish rows: report the worst 600px band
    rows_per_band = max(1, 600 // block)
    band_ratios = [float(flat[i:i + rows_per_band].mean()) for i in range(0, H, rows_per_band)]
    return ratio, Image.fromarray(arr), band_ratios


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("png")
    ap.add_argument("--heatmap")
    ap.add_argument("--block", type=int, default=10)
    ap.add_argument("--tol", type=int, default=6)
    a = ap.parse_args()
    r, heat, bands = flat_ratio(a.png, a.block, a.tol)
    if a.heatmap:
        heat.save(a.heatmap)
    print(f"flat area: {r * 100:.1f}% (limit {LIMIT * 100:.0f}%)  " + ("OK" if r < LIMIT else "TOO FLAT"))
    for i, b in enumerate(bands):
        print(f"  band {i + 1:02d} (y {i * 600}-{(i + 1) * 600}): {b * 100:.0f}%" + ("  <-- flat" if b >= LIMIT else ""))
    sys.exit(0 if r < LIMIT else 1)
