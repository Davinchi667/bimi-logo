#!/usr/bin/env python3
"""Print the expected Figma layer tree of an email SVG: every <g> id with its
absolute y, height estimate, and counts of text/image children. Compare this
against what Figma shows after import (get_metadata) to catch dropped layers.

  svg_layers.py email.svg [--json]
"""
from __future__ import annotations
import json
import re
import sys
from lxml import etree

NS = "http://www.w3.org/2000/svg"


def _tr(el):
    m = re.search(r"translate\(\s*([-\d.]+)[ ,]+([-\d.]+)?\s*\)", el.get("transform", ""))
    return (float(m.group(1)), float(m.group(2) or 0)) if m else (0.0, 0.0)


def walk(el, ox=0.0, oy=0.0, depth=0, out=None):
    out = out if out is not None else []
    for g in el:
        if g.tag != f"{{{NS}}}g":
            continue
        dx, dy = _tr(g)
        ax, ay = ox + dx, oy + dy
        texts = [t for t in g.iter(f"{{{NS}}}text")]
        images = [i for i in g.iter(f"{{{NS}}}image")]
        words = sum(len("".join(t.itertext()).split()) for t in texts)
        out.append({"depth": depth, "id": g.get("id"), "x": ax, "y": ay, "texts": len(texts), "words": words, "images": len(images)})
        walk(g, ax, ay, depth + 1, out)
    return out


if __name__ == "__main__":
    svg = sys.argv[1]
    root = etree.parse(svg).getroot()
    rows = walk(root)
    if "--json" in sys.argv:
        print(json.dumps(rows, indent=1))
    else:
        for r in rows:
            print(f"{'  ' * r['depth']}{r['id']!s:40.40} y={r['y']:<6.0f} text={r['texts']:<3} words={r['words']:<4} img={r['images']}")
        print(f"{len(rows)} groups, {sum(r['texts'] for r in rows if r['depth'] == 0)} text elements, {sum(r['images'] for r in rows if r['depth'] == 0)} images")
