#!/usr/bin/env python3
"""One entry point for the studio.

  studio.py scrape URL [--brand slug] [--extra URL ...]      -> brands/<brand>/study/
  studio.py build brands/<brand>/build.py                    -> writes the SVG (build.py decides where)
  studio.py qa brands/<brand>/build.py                       -> build + validate + render + flat-area (+ layer list)
  studio.py gif brands/<brand>/build.py                      -> every module GIF + full-email GIF
  studio.py all brands/<brand>/build.py                      -> qa + gif
  studio.py test                                             -> runs `all` on tools/examples/demo_build.py

build.py must expose:  fonts (FontRegistry), build(state) -> Email, and
optionally BRAND (slug) and NAME (file stem, default <brand>_welcome-01).
Outputs go to brands/<BRAND>/final/.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
PY = sys.executable


def _load(build_py: str):
    sys.path.insert(0, str(HERE))
    from build_gif import load_build
    mod = load_build(build_py)
    brand = getattr(mod, "BRAND", Path(build_py).resolve().parent.name)
    name = getattr(mod, "NAME", f"{brand}_welcome-01")
    return mod, brand, name


def cmd_build(build_py: str):
    mod, brand, name = _load(build_py)
    em = mod.build({})
    out = ROOT / "brands" / brand / "final"
    p = em.save(out / f"{name}.svg")
    print(f"built {p} ({em.height}px, {len(em.sections)} sections, {len(em.modules)} modules, {p.stat().st_size / 1e6:.2f} MB)")
    return p, out, name, mod


def cmd_qa(build_py: str) -> bool:
    p, out, name, mod = cmd_build(build_py)
    ok = True
    r = subprocess.run([PY, str(HERE / "validate_svg.py"), str(p), "--fonts-from", build_py])
    ok &= r.returncode == 0
    subprocess.run([PY, str(HERE / "render.py"), str(p), "--out", str(out), "--fonts-from", build_py, "--name", name], check=True)
    r = subprocess.run([PY, str(HERE / "flat_area.py"), str(out / f"{name}_600.png"), "--heatmap", str(out / "review" / "flat_heatmap.png")])
    ok &= r.returncode == 0
    subprocess.run([PY, str(HERE / "svg_layers.py"), str(p)], stdout=open(out / "review" / "layers.txt", "w"))
    print(f"QA {'PASSED' if ok else 'FAILED'}: review slices in {out / 'review'}")
    return ok


def cmd_gif(build_py: str):
    mod, brand, name = _load(build_py)
    out = ROOT / "brands" / brand / "final"
    subprocess.run([PY, str(HERE / "build_gif.py"), build_py, "--out", str(out), "--name", name], check=True)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "scrape":
        sys.exit(subprocess.run([PY, str(HERE / "scrape_brand.py"), *args]).returncode)
    elif cmd == "build":
        cmd_build(args[0])
    elif cmd == "qa":
        sys.exit(0 if cmd_qa(args[0]) else 1)
    elif cmd == "gif":
        cmd_gif(args[0])
    elif cmd == "all":
        ok = cmd_qa(args[0])
        cmd_gif(args[0])
        sys.exit(0 if ok else 1)
    elif cmd == "test":
        ok = cmd_qa(str(HERE / "examples" / "demo_build.py"))
        cmd_gif(str(HERE / "examples" / "demo_build.py"))
        print("toolkit test finished" + ("" if ok else " (demo is intentionally plain; flat-area fails on it by design)"))
    else:
        print(__doc__)
        sys.exit(2)
