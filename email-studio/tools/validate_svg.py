#!/usr/bin/env python3
"""Validate an email SVG for Figma import and brief rules.

Fails (exit 1) on:
  * nested <tspan> (Figma drops ALL the text in that element)
  * <textPath> anywhere
  * a <g> without an id, or with a blank/auto id (g1, Group 3 ...)
  * glyph icons in text: ★ ☆ ✓ ✔ ✗ → ← ↑ ↓ ▶ ● ■ ♥ etc.
  * text under 14px outside a footer group (group id containing 'footer')
  * text that starts left of x=30 or ends right of x=570 (measured with the
    real font when it is in the registry; else estimated at 0.55em/char);
    text inside a clipped <g> (ticker, bleed) is exempt
  * <image> whose href is not a data: URI
  * font-weight that is not numeric; font-family missing on <text>
  * file over 6 MB
Warns on: duplicate group ids, text wider than its wrap width is not checked
here (the builder raises), em dashes in text, double spaces.

usage: validate_svg.py path.svg [--fonts-from build.py]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from lxml import etree

sys.path.insert(0, str(Path(__file__).resolve().parent))
from emailkit.fonts import FontRegistry  # noqa: E402

NS = "http://www.w3.org/2000/svg"
GLYPHS = set("★☆✓✔✗✘→←↑↓⇒⇐▶◀●■□♥♡•◆◇▲▼➜➔➤⭐✨")
MIN_TEXT = 14
MARGIN = 30
WIDTH = 600
MAX_BYTES = 6 * 1024 * 1024
AUTO_ID = re.compile(r"^(g|group|layer|rect|path)?\s*\d*$", re.I)


def _f(v, default=0.0):
    try:
        return float(str(v).replace("px", ""))
    except (TypeError, ValueError):
        return default


def _translate(el):
    t = el.get("transform", "")
    m = re.search(r"translate\(\s*([-\d.]+)[ ,]+([-\d.]+)?\s*\)", t)
    if not m:
        return 0.0, 0.0
    return float(m.group(1)), float(m.group(2) or 0)


def _abs_offset(el):
    x = y = 0.0
    p = el
    while p is not None:
        if p.tag == f"{{{NS}}}g":
            dx, dy = _translate(p)
            x += dx
            y += dy
        p = p.getparent()
    return x, y


def _clipped(el):
    p = el
    while p is not None:
        if p.tag == f"{{{NS}}}g" and p.get("clip-path"):
            return True
        p = p.getparent()
    return False


def _in_footer(el):
    p = el
    while p is not None:
        if p.tag == f"{{{NS}}}g" and "footer" in (p.get("id") or "").lower():
            return True
        p = p.getparent()
    return False


def _inherit(el, attr, default=None):
    p = el
    while p is not None:
        v = p.get(attr)
        if v is not None:
            return v
        p = p.getparent()
    return default


def validate(path: str, fonts: FontRegistry | None = None) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    p = Path(path)
    if p.stat().st_size > MAX_BYTES:
        errors.append(f"file is {p.stat().st_size / 1e6:.1f} MB (max 6 MB)")
    tree = etree.parse(str(p))
    root = tree.getroot()

    # structure
    for tp in root.iter(f"{{{NS}}}textPath"):
        errors.append(f"textPath at line {tp.sourceline}: use one <text> per letter with rotate()")
    for ts in root.iter(f"{{{NS}}}tspan"):
        if ts.getparent() is not None and ts.getparent().tag == f"{{{NS}}}tspan":
            errors.append(f"nested tspan at line {ts.sourceline} ({ts.text!r})")
    ids = {}
    for g in root.iter(f"{{{NS}}}g"):
        gid = g.get("id")
        if not gid or not gid.strip():
            errors.append(f"<g> without id at line {g.sourceline}")
        elif AUTO_ID.match(gid.strip()):
            errors.append(f"<g> with auto-looking id {gid!r} at line {g.sourceline}")
        else:
            ids.setdefault(gid, []).append(g.sourceline)
    for gid, lines in ids.items():
        if len(lines) > 1:
            warnings.append(f"duplicate group id {gid!r} at lines {lines}")
    for im in root.iter(f"{{{NS}}}image"):
        href = im.get("href") or im.get(f"{{http://www.w3.org/1999/xlink}}href") or ""
        if not href.startswith("data:"):
            errors.append(f"<image> at line {im.sourceline} is not embedded (href={href[:40]!r})")

    # text
    for t in root.iter(f"{{{NS}}}text"):
        fam = _inherit(t, "font-family")
        if not fam:
            errors.append(f"<text> without font-family at line {t.sourceline}")
        fw = _inherit(t, "font-weight", "400")
        if not re.fullmatch(r"\d{3}", str(fw)):
            errors.append(f"non-numeric font-weight {fw!r} at line {t.sourceline}")
        size = _f(_inherit(t, "font-size", "16"), 16)
        footer = _in_footer(t)
        pieces = []   # (text, x, size, weight, family, anchor, letter_spacing, style)
        spans = list(t.iter(f"{{{NS}}}tspan"))
        if spans:
            for s in spans:
                pieces.append((s.text or "", _f(s.get("x", t.get("x", "0"))), _f(s.get("font-size", size), size),
                               s.get("font-weight", fw), s.get("font-family", fam), _inherit(s, "text-anchor", "start"),
                               _f(_inherit(s, "letter-spacing", "0")), s.get("font-style", t.get("font-style", "normal"))))
        else:
            pieces.append((t.text or "", _f(t.get("x", "0")), size, fw, fam, t.get("text-anchor", "start"),
                           _f(t.get("letter-spacing", "0")), t.get("font-style", "normal")))
        all_text = "".join(pc[0] for pc in pieces)
        bad = [c for c in all_text if c in GLYPHS]
        if bad:
            errors.append(f"glyph icon(s) {''.join(sorted(set(bad)))!r} in text at line {t.sourceline}; draw as path")
        if "—" in all_text or "–" in all_text:
            warnings.append(f"dash in text at line {t.sourceline}: {all_text[:50]!r}")
        if "  " in all_text:
            warnings.append(f"double space at line {t.sourceline}: {all_text[:50]!r}")
        if not all_text.strip():
            warnings.append(f"empty <text> at line {t.sourceline}")
        if t.get("transform") and "rotate" in t.get("transform"):
            continue   # curved letters: margins are checked by eye
        if _clipped(t):
            continue   # inside a clipped group (ticker, bleed): overflow is intentional
        ox, _ = _abs_offset(t)
        for txt, x, sz, w, f, anchor, ls, st in pieces:
            if not txt.strip():
                continue
            if sz < MIN_TEXT and not footer:
                errors.append(f"text {sz}px (<{MIN_TEXT}) outside footer at line {t.sourceline}: {txt[:40]!r}")
            width = None
            if fonts is not None and f:
                try:
                    width = fonts.get(f, int(w), st if st in ("normal", "italic") else "normal").width(txt, sz, ls)
                except KeyError:
                    width = None
            if width is None:
                width = len(txt) * sz * 0.55 + ls * max(0, len(txt) - 1)
            ax = ox + x
            left = ax - (width / 2 if anchor == "middle" else width if anchor == "end" else 0)
            right = left + width
            if left < MARGIN - 0.5 or right > WIDTH - MARGIN + 0.5:
                errors.append(f"text past 30px margin (x {left:.0f}..{right:.0f}) at line {t.sourceline}: {txt[:40]!r}")
    return errors, warnings


def load_fonts_from_build(build_py: str) -> FontRegistry | None:
    import importlib.util
    spec = importlib.util.spec_from_file_location("brand_build", build_py)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if hasattr(mod, "fonts"):
        return mod.fonts
    if hasattr(mod, "build"):
        return mod.build({}).fonts
    return None


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("svg")
    ap.add_argument("--fonts-from", help="brand build.py exposing `fonts` or `build()` for exact widths")
    a = ap.parse_args()
    reg = load_fonts_from_build(a.fonts_from) if a.fonts_from else None
    errs, warns = validate(a.svg, reg)
    for w in warns:
        print("WARN ", w)
    for e in errs:
        print("ERROR", e)
    print(f"{len(errs)} errors, {len(warns)} warnings" + ("" if reg else " (widths estimated; pass --fonts-from for exact)"))
    sys.exit(1 if errs else 0)
