#!/usr/bin/env python3
"""Image prep for brand assets (Pillow + numpy + scipy, rembg when installed).

  image_prep.py download URL out.png            full-res download (Shopify size suffix stripped)
  image_prep.py cutout in.png out.png [--mode auto|rembg|white]   clean transparent cutout
  image_prep.py trim in.png out.png [--pad 0]   crop to non-transparent bbox
  image_prep.py crop in.png out.png --box x y w h
  image_prep.py textures in.jpg out_dir --size 300 --n 6   texture crops from a photo (busy, non-flat areas)
  image_prep.py fit in.png out.png --w 600 --h 400 [--mode cover|contain]

Library: download(), cutout(), defringe(), trim(), textures()
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import numpy as np
import requests
from PIL import Image, ImageFilter
from scipy import ndimage

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"}


def full_res_url(url: str) -> str:
    """Strip Shopify CDN size suffixes (_600x, _1024x1024, _small, @2x) so we get the master."""
    u = re.sub(r"_(\d+x\d*|\d*x\d+|pico|icon|thumb|small|compact|medium|large|grande|original|master)(_crop_\w+)?(@\dx)?(?=\.(jpg|jpeg|png|webp|gif))", "", url, flags=re.I)
    u = re.sub(r"([?&])(width|height)=\d+", r"\1", u)
    return u.rstrip("?&")


def download(url: str, out: str | Path) -> Path:
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    for candidate in (full_res_url(url), url):
        r = requests.get(candidate, headers=UA, timeout=60)
        if r.status_code == 200 and r.headers.get("content-type", "").startswith("image"):
            im = Image.open(__import__("io").BytesIO(r.content))
            if out.suffix.lower() in (".jpg", ".jpeg"):
                im.convert("RGB").save(out, quality=95)
            else:
                im.save(out)
            return out
    raise RuntimeError(f"could not download {url}")


def _white_matte(im: Image.Image, thresh: int = 235, soft: int = 18) -> Image.Image:
    """Alpha from near-white background connected to the border (flood fill),
    so white parts INSIDE the product survive."""
    rgb = np.asarray(im.convert("RGB")).astype(np.int16)
    lum = rgb.min(axis=2)
    near_white = lum >= thresh
    lab, n = ndimage.label(near_white)
    border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]])))
    border.discard(0)
    bg = np.isin(lab, list(border))
    bg = ndimage.binary_closing(bg, iterations=1)
    alpha = np.where(bg, 0, 255).astype(np.uint8)
    # soften the edge: within the soft band, fade by distance to white
    edge = ndimage.binary_dilation(bg, iterations=2) & ~bg
    fade = np.clip((255 - lum[edge]) * 255 / max(1, 255 - thresh + soft), 0, 255)
    alpha[edge] = fade.astype(np.uint8)
    out = im.convert("RGBA")
    out.putalpha(Image.fromarray(alpha))
    return out


def defringe(im: Image.Image, erode: int = 1) -> Image.Image:
    """Kill the white/light fringe on a cutout: erode alpha slightly and
    decontaminate edge colours toward the nearest opaque pixel."""
    im = im.convert("RGBA")
    a = np.asarray(im)[:, :, 3].astype(np.float32) / 255
    rgb = np.asarray(im)[:, :, :3].astype(np.float32)
    if erode:
        solid = a > 0.98
        er = ndimage.binary_erosion(solid, iterations=erode)
        a2 = ndimage.gaussian_filter(er.astype(np.float32), 0.7)
        a = np.minimum(a, np.maximum(a2, (a > 0.98) * 0 + a2))
        a = np.where(solid & ~er, a * 0.6, a)
    # colour decontamination: replace semi-transparent pixel colours with the nearest opaque colour
    opaque = a > 0.95
    if opaque.any():
        idx = ndimage.distance_transform_edt(~opaque, return_distances=False, return_indices=True)
        nearest = rgb[idx[0], idx[1]]
        semi = (a > 0) & ~opaque
        rgb[semi] = nearest[semi]
    out = np.dstack([rgb.clip(0, 255).astype(np.uint8), (a * 255).clip(0, 255).astype(np.uint8)])
    return Image.fromarray(out, "RGBA")


def cutout(src: str | Path, out: str | Path, mode: str = "auto") -> Path:
    im = Image.open(src)
    res = None
    if mode in ("auto", "rembg"):
        try:
            from rembg import remove
            res = remove(im.convert("RGBA"), alpha_matting=True, alpha_matting_foreground_threshold=240,
                         alpha_matting_background_threshold=10, alpha_matting_erode_size=8)
        except Exception as e:  # rembg missing or model download blocked
            if mode == "rembg":
                raise
            print(f"  rembg unavailable ({str(e)[:60]}), falling back to white matte", file=sys.stderr)
    if res is None:
        res = _white_matte(im)
    res = defringe(res)
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    res.save(out)
    return out


def trim(src, out, pad: int = 0) -> Path:
    im = Image.open(src).convert("RGBA")
    bbox = im.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
    if bbox:
        im = im.crop((max(0, bbox[0] - pad), max(0, bbox[1] - pad), min(im.width, bbox[2] + pad), min(im.height, bbox[3] + pad)))
    im.save(out)
    return Path(out)


def fit(src, out, w: int, h: int, mode: str = "cover") -> Path:
    im = Image.open(src)
    s = (max if mode == "cover" else min)(w / im.width, h / im.height)
    im = im.resize((max(1, round(im.width * s)), max(1, round(im.height * s))), Image.LANCZOS)
    if mode == "cover":
        l, t = (im.width - w) // 2, (im.height - h) // 2
        im = im.crop((l, t, l + w, t + h))
    im.save(out)
    return Path(out)


def textures(src, out_dir, size: int = 300, n: int = 6) -> list[Path]:
    """Pick the n busiest (highest local std-dev) non-overlapping size x size
    crops from a brand photo. Good for surfaces behind type."""
    im = Image.open(src).convert("RGB")
    if min(im.size) < size:
        s = size / min(im.size)
        im = im.resize((round(im.width * s) + 1, round(im.height * s) + 1))
    g = np.asarray(im.convert("L")).astype(np.float32)
    step = max(20, size // 4)
    cands = []
    for y in range(0, im.height - size + 1, step):
        for x in range(0, im.width - size + 1, step):
            blk = g[y:y + size, x:x + size]
            cands.append((float(blk.std()), x, y))
    cands.sort(reverse=True)
    picked, out = [], []
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for sd, x, y in cands:
        if any(abs(x - px) < size and abs(y - py) < size for px, py in picked):
            continue
        p = out_dir / f"texture_{len(out) + 1:02d}_std{sd:.0f}.jpg"
        im.crop((x, y, x + size, y + size)).save(p, quality=92)
        picked.append((x, y))
        out.append(p)
        if len(out) >= n:
            break
    return out


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("download"); s.add_argument("url"); s.add_argument("out")
    s = sub.add_parser("cutout"); s.add_argument("src"); s.add_argument("out"); s.add_argument("--mode", default="auto")
    s = sub.add_parser("trim"); s.add_argument("src"); s.add_argument("out"); s.add_argument("--pad", type=int, default=0)
    s = sub.add_parser("crop"); s.add_argument("src"); s.add_argument("out"); s.add_argument("--box", nargs=4, type=int, required=True)
    s = sub.add_parser("textures"); s.add_argument("src"); s.add_argument("out_dir"); s.add_argument("--size", type=int, default=300); s.add_argument("--n", type=int, default=6)
    s = sub.add_parser("fit"); s.add_argument("src"); s.add_argument("out"); s.add_argument("--w", type=int, required=True); s.add_argument("--h", type=int, required=True); s.add_argument("--mode", default="cover")
    a = ap.parse_args()
    if a.cmd == "download":
        print(download(a.url, a.out))
    elif a.cmd == "cutout":
        print(cutout(a.src, a.out, a.mode))
    elif a.cmd == "trim":
        print(trim(a.src, a.out, a.pad))
    elif a.cmd == "crop":
        x, y, w, h = a.box
        Image.open(a.src).crop((x, y, x + w, y + h)).save(a.out); print(a.out)
    elif a.cmd == "textures":
        for p in textures(a.src, a.out_dir, a.size, a.n):
            print(p)
    elif a.cmd == "fit":
        print(fit(a.src, a.out, a.w, a.h, a.mode))
