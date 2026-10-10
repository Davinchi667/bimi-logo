"""Path data for icons that must never be glyphs (Figma drops/replaces glyph icons).

Every function returns an SVG path `d` string drawn in a box with its top-left
at (x, y) and the given size. Use with Group.path().
"""
from __future__ import annotations
import math


def star(x: float, y: float, size: float, inner: float = 0.5) -> str:
    """Five-point star inscribed in a size x size box."""
    cx, cy = x + size / 2, y + size / 2
    R = size / 2
    r = R * inner
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rad = R if i % 2 == 0 else r
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    return "M" + " L".join(f"{px:.2f} {py:.2f}" for px, py in pts) + " Z"


def half_star_clip(x: float, y: float, size: float) -> str:
    """Rect covering the left half of a star box (use as a clipPath for half stars)."""
    return f"M{x:.2f} {y:.2f} H{x + size / 2:.2f} V{y + size:.2f} H{x:.2f} Z"


def check(x: float, y: float, size: float) -> str:
    """Check mark stroke path (use stroke, fill none, stroke-linecap round)."""
    return (f"M{x + size * 0.18:.2f} {y + size * 0.55:.2f} "
            f"L{x + size * 0.42:.2f} {y + size * 0.78:.2f} "
            f"L{x + size * 0.84:.2f} {y + size * 0.26:.2f}")


def arrow_right(x: float, y: float, size: float) -> str:
    """Arrow pointing right: shaft + head, stroke path."""
    cy = y + size / 2
    return (f"M{x + size * 0.1:.2f} {cy:.2f} L{x + size * 0.9:.2f} {cy:.2f} "
            f"M{x + size * 0.58:.2f} {y + size * 0.2:.2f} L{x + size * 0.9:.2f} {cy:.2f} "
            f"L{x + size * 0.58:.2f} {y + size * 0.8:.2f}")


def arrow_left(x: float, y: float, size: float) -> str:
    cy = y + size / 2
    return (f"M{x + size * 0.9:.2f} {cy:.2f} L{x + size * 0.1:.2f} {cy:.2f} "
            f"M{x + size * 0.42:.2f} {y + size * 0.2:.2f} L{x + size * 0.1:.2f} {cy:.2f} "
            f"L{x + size * 0.42:.2f} {y + size * 0.8:.2f}")


def arrow_down(x: float, y: float, size: float) -> str:
    cx = x + size / 2
    return (f"M{cx:.2f} {y + size * 0.1:.2f} L{cx:.2f} {y + size * 0.9:.2f} "
            f"M{x + size * 0.2:.2f} {y + size * 0.58:.2f} L{cx:.2f} {y + size * 0.9:.2f} "
            f"L{x + size * 0.8:.2f} {y + size * 0.58:.2f}")


def chevron_right(x: float, y: float, size: float) -> str:
    return (f"M{x + size * 0.35:.2f} {y + size * 0.2:.2f} L{x + size * 0.65:.2f} {y + size * 0.5:.2f} "
            f"L{x + size * 0.35:.2f} {y + size * 0.8:.2f}")


def chevron_down(x: float, y: float, size: float) -> str:
    return (f"M{x + size * 0.2:.2f} {y + size * 0.38:.2f} L{x + size * 0.5:.2f} {y + size * 0.66:.2f} "
            f"L{x + size * 0.8:.2f} {y + size * 0.38:.2f}")


def plus(x: float, y: float, size: float) -> str:
    cx, cy = x + size / 2, y + size / 2
    return (f"M{cx:.2f} {y + size * 0.15:.2f} L{cx:.2f} {y + size * 0.85:.2f} "
            f"M{x + size * 0.15:.2f} {cy:.2f} L{x + size * 0.85:.2f} {cy:.2f}")


def cross(x: float, y: float, size: float) -> str:
    return (f"M{x + size * 0.22:.2f} {y + size * 0.22:.2f} L{x + size * 0.78:.2f} {y + size * 0.78:.2f} "
            f"M{x + size * 0.78:.2f} {y + size * 0.22:.2f} L{x + size * 0.22:.2f} {y + size * 0.78:.2f}")


def heart(x: float, y: float, size: float) -> str:
    s = size
    return (f"M{x + s * 0.5:.2f} {y + s * 0.9:.2f} "
            f"C{x + s * 0.1:.2f} {y + s * 0.62:.2f} {x:.2f} {y + s * 0.42:.2f} {x + s * 0.08:.2f} {y + s * 0.27:.2f} "
            f"C{x + s * 0.17:.2f} {y + s * 0.1:.2f} {x + s * 0.4:.2f} {y + s * 0.1:.2f} {x + s * 0.5:.2f} {y + s * 0.28:.2f} "
            f"C{x + s * 0.6:.2f} {y + s * 0.1:.2f} {x + s * 0.83:.2f} {y + s * 0.1:.2f} {x + s * 0.92:.2f} {y + s * 0.27:.2f} "
            f"C{x + s:.2f} {y + s * 0.42:.2f} {x + s * 0.9:.2f} {y + s * 0.62:.2f} {x + s * 0.5:.2f} {y + s * 0.9:.2f} Z")


def circle(cx: float, cy: float, r: float) -> str:
    return (f"M{cx - r:.2f} {cy:.2f} a{r:.2f} {r:.2f} 0 1 0 {2 * r:.2f} 0 "
            f"a{r:.2f} {r:.2f} 0 1 0 {-2 * r:.2f} 0 Z")


def rrect(x: float, y: float, w: float, h: float, r: float) -> str:
    r = min(r, w / 2, h / 2)
    return (f"M{x + r:.2f} {y:.2f} H{x + w - r:.2f} A{r:.2f} {r:.2f} 0 0 1 {x + w:.2f} {y + r:.2f} "
            f"V{y + h - r:.2f} A{r:.2f} {r:.2f} 0 0 1 {x + w - r:.2f} {y + h:.2f} H{x + r:.2f} "
            f"A{r:.2f} {r:.2f} 0 0 1 {x:.2f} {y + h - r:.2f} V{y + r:.2f} A{r:.2f} {r:.2f} 0 0 1 {x + r:.2f} {y:.2f} Z")


def scallop_edge(x0: float, x1: float, y: float, bump: float = 10, depth: float = 6, down: bool = True) -> str:
    """Receipt / sticker scalloped edge as one path, bumps of width `bump`."""
    n = max(1, int((x1 - x0) // bump))
    bw = (x1 - x0) / n
    d = [f"M{x0:.2f} {y:.2f}"]
    for i in range(n):
        sx = x0 + i * bw
        dy = depth if down else -depth
        d.append(f"Q{sx + bw / 2:.2f} {y + dy * 2:.2f} {sx + bw:.2f} {y:.2f}")
    return " ".join(d)


def zigzag(x0: float, x1: float, y: float, step: float = 8, amp: float = 4) -> str:
    n = max(1, int((x1 - x0) // step))
    sw = (x1 - x0) / n
    pts = [f"M{x0:.2f} {y:.2f}"]
    for i in range(1, n + 1):
        pts.append(f"L{x0 + i * sw:.2f} {y + (amp if i % 2 else -amp):.2f}")
    return " ".join(pts)


def wave(x0: float, x1: float, y: float, length: float = 40, amp: float = 6) -> str:
    n = max(1, int((x1 - x0) // length))
    lw = (x1 - x0) / n
    d = [f"M{x0:.2f} {y:.2f}"]
    for i in range(n):
        sx = x0 + i * lw
        d.append(f"Q{sx + lw / 4:.2f} {y - amp:.2f} {sx + lw / 2:.2f} {y:.2f}")
        d.append(f"Q{sx + 3 * lw / 4:.2f} {y + amp:.2f} {sx + lw:.2f} {y:.2f}")
    return " ".join(d)
