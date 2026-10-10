#!/usr/bin/env python3
"""Build every motion-module GIF and the full-email GIF from a brand build script.

The build script must expose `build(state: dict) -> Email`. Each module Mx reads
`state.get("Mx", 0)`; state 0 is the finished static frame. Modules are
registered on the Email with email.module(...), which gives the band (y, h),
the number of states and the per-state durations.

  build_gif.py brands/x/build.py --out brands/x/final/ --name x_welcome-01

Per module: gifs/<ID>_<name>.gif, 600 x h, frame 1 = static state (pixel-equal
to the static PNG band, checked), 3..8 held states, loop forever, about 1 MB,
hard max 2.5 MB (colours are reduced until it fits).
Full email: <name>_full.gif, frame 1 = complete static email, all module loops
on one common timeline (LCM of loop lengths, capped), 2.5 MB max.

Pillow writes only the changed rectangle per frame, so a module band on a
static canvas stays small.
"""
from __future__ import annotations

import importlib.util
import io
import math
import re
import sys
from functools import reduce
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops

sys.path.insert(0, str(Path(__file__).resolve().parent))
import render as R  # noqa: E402

MODULE_BUDGET = 1.0 * 1024 * 1024
HARD_MAX = 2.5 * 1024 * 1024
FULL_MAX = 2.5 * 1024 * 1024


def load_build(build_py: str):
    spec = importlib.util.spec_from_file_location("brand_build", build_py)
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(Path(build_py).resolve().parent))
    spec.loader.exec_module(mod)
    return mod


def _slug(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_")


def _quantize(frames: list[Image.Image], colors: int) -> list[Image.Image]:
    """Quantize all frames with ONE shared palette (built from a montage) so
    frame-to-frame diffs stay small and colours don't flicker."""
    montage_h = sum(f.height for f in frames)
    sample = Image.new("RGB", (frames[0].width, montage_h))
    y = 0
    for f in frames:
        sample.paste(f.convert("RGB"), (0, y))
        y += f.height
    if sample.height > 4000:
        sample = sample.resize((sample.width, 4000))
    pal = sample.quantize(colors=colors, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    return [f.convert("RGB").quantize(palette=pal, dither=Image.Dither.FLOYDSTEINBERG) for f in frames]


def save_gif(frames: list[Image.Image], durations: list[int], path: Path, budget: int, hard_max: int) -> int:
    """Save with a shared palette, shrinking the palette until under budget.
    Returns the byte size. Raises if it cannot get under hard_max."""
    path.parent.mkdir(parents=True, exist_ok=True)
    size = None
    for colors in (256, 192, 128, 96, 64, 48, 32):
        q = _quantize(frames, colors)
        buf = io.BytesIO()
        q[0].save(buf, "GIF", save_all=True, append_images=q[1:], duration=durations, loop=0,
                  optimize=True, disposal=1)
        size = buf.tell()
        if size <= budget:
            break
    if size > hard_max:
        raise RuntimeError(f"{path.name}: {size / 1e6:.2f} MB even at 32 colours (hard max {hard_max / 1e6} MB). "
                           "Shorten the loop, shrink the band or move less area per state.")
    path.write_bytes(buf.getvalue())
    return size


def _lcm(a, b):
    return a * b // math.gcd(a, b)


def build_all(build_py: str, out_dir: str, name: str, scale: int = 1, tick_ms: int = 100) -> dict:
    mod = load_build(build_py)
    static = mod.build({})
    fonts = static.fonts
    svg_static = static.to_svg()
    full_static = R.render_svg(svg_static, fonts, scale)
    out = Path(out_dir)
    (out / "gifs").mkdir(parents=True, exist_ok=True)
    report = {"modules": [], "full": None}

    # render every module state once (full canvas), crop the band
    bands: dict[str, list[Image.Image]] = {}
    for m in static.modules:
        frames = []
        for s in range(m.states):
            svg = static.to_svg() if s == 0 else mod.build({m.id: s}).to_svg()
            im = R.render_svg(svg, fonts, scale)
            band = im.crop((0, m.y * scale, im.width, (m.y + m.h) * scale)).convert("RGB")
            frames.append(band)
        # frame 1 must equal the static band pixel for pixel
        static_band = full_static.crop((0, m.y * scale, full_static.width, (m.y + m.h) * scale)).convert("RGB")
        diff = ImageChops.difference(frames[0], static_band).getbbox()
        if diff is not None:
            raise RuntimeError(f"{m.id}: frame 1 differs from the static design in box {diff}. State 0 must be the finished design.")
        # optional tween frames between held states (linear crossfade)
        seq, durs = [], []
        for i, f in enumerate(frames):
            seq.append(f)
            durs.append(m.durations_ms[i])
            if m.tween_frames:
                nxt = frames[(i + 1) % len(frames)]
                for t in range(1, m.tween_frames + 1):
                    a = t / (m.tween_frames + 1)
                    seq.append(Image.blend(f, nxt, a))
                    durs.append(40)
        gif_path = out / "gifs" / f"{m.id}_{_slug(m.name)}.gif"
        size = save_gif(seq, durs, gif_path, int(MODULE_BUDGET), int(HARD_MAX))
        bands[m.id] = frames
        report["modules"].append({"id": m.id, "name": m.name, "file": str(gif_path), "kb": round(size / 1024),
                                  "band": f"600x{m.h} at y={m.y}", "states": m.states, "loop_ms": m.loop_ms})
        print(f"  {m.id} {m.name}: {size / 1024:.0f} KB, {len(seq)} frames, loop {m.loop_ms} ms, band 600x{m.h} @ y={m.y}")

    # full-email GIF on a common timeline
    if static.modules:
        loops = [m.loop_ms for m in static.modules]
        common = reduce(_lcm, loops)
        if common > 12000:          # cap: cycle the longest loop a few times instead of a true LCM
            common = max(loops) * 2
        ticks = list(range(0, common, tick_ms))

        def state_at(m, t):
            t = t % m.loop_ms
            acc = 0
            for i, d in enumerate(m.durations_ms):
                acc += d
                if t < acc:
                    return i
            return m.states - 1

        frames, durs = [], []
        prev_key = None
        base = full_static.convert("RGB")
        for t in ticks:
            key = tuple(state_at(m, t) for m in static.modules)
            if key == prev_key:
                durs[-1] += tick_ms
                continue
            fr = base.copy()
            for m, s in zip(static.modules, key):
                if s:
                    fr.paste(bands[m.id][s], (0, m.y * scale))
            frames.append(fr)
            durs.append(tick_ms)
            prev_key = key
        if ImageChops.difference(frames[0], base).getbbox() is not None:
            raise RuntimeError("full GIF frame 1 is not the static email")
        full_path = out / f"{name}_full.gif"
        size = save_gif(frames, durs, full_path, int(FULL_MAX), int(FULL_MAX))
        report["full"] = {"file": str(full_path), "kb": round(size / 1024), "frames": len(frames), "loop_ms": common}
        print(f"  FULL: {size / 1024:.0f} KB, {len(frames)} frames, loop {common} ms, {full_static.width}x{full_static.height}")
    return report


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("build_py")
    ap.add_argument("--out", required=True)
    ap.add_argument("--name", required=True)
    a = ap.parse_args()
    try:
        build_all(a.build_py, a.out, a.name)
    finally:
        R.close()
