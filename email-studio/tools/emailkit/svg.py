"""Figma-safe SVG email builder.

Rules baked in (see CLAUDE.md "technical rules"):
  * every <g> gets a readable id (= Figma layer name)
  * text stays live <text>; never a <tspan> inside a <tspan>
    - mixed styles on one line  -> sibling <tspan>s in one <text>, each with its own x
    - multi-line                -> one <tspan> per line with its own x and y
    - curved text               -> one <text> per letter with rotate()
  * images are base64 data URIs, clipped with <clipPath>
  * stars / checks / arrows are paths (emailkit.shapes), never glyphs
  * font-family is the exact family name, font-weight is numeric
  * widths are measured with the real font file (emailkit.fonts)

Coordinates inside a section are local; sections are stacked with translate().

Motion modules: the brand build script exposes `build(state: dict) -> Email`.
A module reads its state with `state.get("M1", 0)`; state 0 is the finished
static frame. Register the band with `email.module(...)` so build_gif.py and
DELIVERY.md know where it is.
"""
from __future__ import annotations

import base64
import io
import math
import re
from dataclasses import dataclass, field
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image

from .fonts import FontRegistry, Font
from . import shapes

WIDTH = 600
MARGIN = 30


def _esc(s: str) -> str:
    return escape(str(s), {'"': "&quot;"})


def _num(v) -> str:
    if isinstance(v, float):
        s = f"{v:.2f}".rstrip("0").rstrip(".")
        return s if s else "0"
    return str(v)


def _attrs(**kw) -> str:
    parts = []
    for k, v in kw.items():
        if v is None or v == "":
            continue
        k = k.rstrip("_").replace("_", "-")
        parts.append(f'{k}="{_esc(_num(v))}"')
    return (" " + " ".join(parts)) if parts else ""


@dataclass
class Module:
    id: str
    name: str
    section: str
    y: int
    h: int
    states: int
    durations_ms: list[int]
    what_moves: str
    frame1: str
    assets: list[str] = field(default_factory=list)
    facts: list[str] = field(default_factory=list)
    tween_frames: int = 0   # extra interpolated frames between states (optional)

    @property
    def loop_ms(self) -> int:
        return sum(self.durations_ms)


class Group:
    def __init__(self, email: "Email", id: str, x: float = 0, y: float = 0,
                 opacity: float | None = None, clip: str | None = None, parent: "Group | None" = None):
        if not id or not str(id).strip():
            raise ValueError("every group needs a readable id")
        self.email = email
        self.id = str(id)
        self.x, self.y = x, y
        self.opacity = opacity
        self.clip = clip
        self.parent = parent
        self.children: list[str] = []

    # ---- nesting -----------------------------------------------------------
    def g(self, id: str, x: float = 0, y: float = 0, opacity: float | None = None, clip=None) -> "Group":
        """clip: a clipPath id, or a (x, y, w, h) box (local coords) to clip the group to.
        Clipped groups are exempt from the validator's margin rule (tickers, bleeds)."""
        if isinstance(clip, (tuple, list)):
            cx, cy, cw, ch = clip
            clip = self.email._clip(f"M{cx} {cy} H{cx + cw} V{cy + ch} H{cx} Z")
        child = Group(self.email, id, x, y, opacity, clip, parent=self)
        self.children.append(child)   # rendered lazily
        return child

    def raw(self, svg: str):
        self.children.append(svg)

    # ---- primitives --------------------------------------------------------
    def rect(self, x, y, w, h, fill="#000", rx=0, stroke=None, stroke_width=None, opacity=None, id=None, dash=None):
        self.raw(f"<rect{_attrs(id=id, x=x, y=y, width=w, height=h, rx=rx or None, fill=fill, stroke=stroke, stroke_width=stroke_width, opacity=opacity, stroke_dasharray=dash)}/>")

    def circle(self, cx, cy, r, fill="#000", stroke=None, stroke_width=None, opacity=None, id=None):
        self.raw(f"<circle{_attrs(id=id, cx=cx, cy=cy, r=r, fill=fill, stroke=stroke, stroke_width=stroke_width, opacity=opacity)}/>")

    def ellipse(self, cx, cy, rx, ry, fill="#000", stroke=None, stroke_width=None, opacity=None, id=None):
        self.raw(f"<ellipse{_attrs(id=id, cx=cx, cy=cy, rx=rx, ry=ry, fill=fill, stroke=stroke, stroke_width=stroke_width, opacity=opacity)}/>")

    def line(self, x1, y1, x2, y2, stroke="#000", stroke_width=1, dash=None, opacity=None, cap=None, id=None):
        self.raw(f"<line{_attrs(id=id, x1=x1, y1=y1, x2=x2, y2=y2, stroke=stroke, stroke_width=stroke_width, stroke_dasharray=dash, opacity=opacity, stroke_linecap=cap)}/>")

    def path(self, d, fill="none", stroke=None, stroke_width=None, cap=None, join=None, opacity=None, id=None, dash=None, transform=None):
        self.raw(f"<path{_attrs(id=id, d=d, fill=fill, stroke=stroke, stroke_width=stroke_width, stroke_linecap=cap, stroke_linejoin=join, opacity=opacity, stroke_dasharray=dash, transform=transform)}/>")

    def rrect(self, x, y, w, h, r, **kw):
        """Rounded rect as a path (lets you clip to it and reuse the d)."""
        self.path(shapes.rrect(x, y, w, h, r), **kw)

    # ---- text --------------------------------------------------------------
    def measure(self, text: str, family: str, size: float, weight: int = 400, letter_spacing: float = 0, style="normal") -> float:
        return self.email.fonts.get(family, weight, style).width(text, size, letter_spacing)

    def text(self, x, y, s, family, size, weight=400, fill="#000", anchor="start", letter_spacing=None,
             style="normal", opacity=None, id=None, runs=None, transform=None, decoration=None, upper=False):
        """One line of text. y is the BASELINE.

        runs: optional list of (string, overrides) where overrides may set family,
        size, weight, fill, style, letter_spacing, dy. Each run becomes a sibling
        <tspan> with its own x (measured), so Figma keeps the styling.
        """
        if upper:
            s = str(s).upper()
        base = dict(family=family, size=size, weight=weight, fill=fill, letter_spacing=letter_spacing, style=style)
        if runs is None:
            self.email._check_font(family, weight, style)
            self.raw(f"<text{_attrs(id=id, x=x, y=y, font_family=family, font_size=size, font_weight=weight, fill=fill, text_anchor=anchor if anchor != 'start' else None, letter_spacing=letter_spacing, font_style=style if style != 'normal' else None, opacity=opacity, transform=transform, text_decoration=decoration)}>{_esc(s)}</text>")
            return self.measure(s, family, size, weight, letter_spacing or 0, style)
        # mixed runs: compute total width for anchor, then place each run at its own x
        widths = []
        for rs, ov in runs:
            o = {**base, **ov}
            widths.append(self.measure(rs, o["family"], o["size"], o["weight"], o.get("letter_spacing") or 0, o.get("style", "normal")))
        total = sum(widths)
        cx = x - (total / 2 if anchor == "middle" else total if anchor == "end" else 0)
        parts = []
        for (rs, ov), w in zip(runs, widths):
            o = {**base, **ov}
            self.email._check_font(o["family"], o["weight"], o.get("style", "normal"))
            parts.append(f"<tspan{_attrs(x=cx, y=y + o.get('dy', 0), font_family=o['family'], font_size=o['size'], font_weight=o['weight'], fill=o['fill'], letter_spacing=o.get('letter_spacing'), font_style=o.get('style') if o.get('style', 'normal') != 'normal' else None, text_decoration=o.get('decoration'))}>{_esc(rs)}</tspan>")
            cx += w
        self.raw(f"<text{_attrs(id=id, font_family=family, font_size=size, font_weight=weight, fill=fill, opacity=opacity, transform=transform)}>{''.join(parts)}</text>")
        return total

    def wrap(self, s: str, family: str, size: float, width: float, weight: int = 400, letter_spacing: float = 0, style="normal") -> list[str]:
        """Greedy word wrap using measured widths. Honours explicit '\n'."""
        font = self.email.fonts.get(family, weight, style)
        lines: list[str] = []
        for para in str(s).split("\n"):
            words = para.split(" ")
            cur = ""
            for w in words:
                trial = (cur + " " + w).strip() if cur else w
                if font.width(trial, size, letter_spacing) <= width or not cur:
                    cur = trial
                else:
                    lines.append(cur)
                    cur = w
            lines.append(cur)
        return lines

    def text_block(self, x, y, s, family, size, width, weight=400, fill="#000", line_height=None, anchor="start",
                   letter_spacing=None, style="normal", opacity=None, id=None, max_lines=None, upper=False, lines=None) -> float:
        """Wrapped paragraph: one <text>, one <tspan> per line with its own x/y.
        y is the baseline of the first line. Returns the total height used
        (baseline of last line - y + line_height)."""
        if upper:
            s = str(s).upper()
        lh = line_height or round(size * 1.3)
        self.email._check_font(family, weight, style)
        if lines is None:
            lines = self.wrap(s, family, size, width, weight, letter_spacing or 0, style)
        if max_lines and len(lines) > max_lines:
            raise ValueError(f"text does not fit in {max_lines} lines at {size}px/{width}px: {s[:60]!r}")
        ax = x + (width / 2 if anchor == "middle" else width if anchor == "end" else 0)
        spans = "".join(f"<tspan{_attrs(x=ax, y=y + i * lh)}>{_esc(ln)}</tspan>" for i, ln in enumerate(lines))
        self.raw(f"<text{_attrs(id=id, font_family=family, font_size=size, font_weight=weight, fill=fill, text_anchor=anchor if anchor != 'start' else None, letter_spacing=letter_spacing, font_style=style if style != 'normal' else None, opacity=opacity)}>{spans}</text>")
        return len(lines) * lh

    def curved_text(self, cx, cy, r, s, family, size, weight=400, fill="#000", start_deg=-90, letter_spacing=2, id=None, inside=False):
        """Text on a circle: one <text> per letter rotated to the tangent (no textPath)."""
        font = self.email.fonts.get(family, weight)
        self.email._check_font(family, weight)
        g = self.g(id or f"Curved {s[:20]}")
        widths = [font.width(ch, size) + letter_spacing for ch in s]
        total = sum(widths)
        circumference = 2 * math.pi * r
        ang = start_deg - (total / circumference * 360) / 2
        for ch, w in zip(s, widths):
            ang += (w / 2 / circumference) * 360
            if ch.isspace():
                ang += (w / 2 / circumference) * 360
                continue
            rad = math.radians(ang)
            px, py = cx + r * math.cos(rad), cy + r * math.sin(rad)
            rot = ang + (270 if inside else 90)
            g.raw(f"<text{_attrs(x=px, y=py, font_family=family, font_size=size, font_weight=weight, fill=fill, text_anchor='middle', transform=f'rotate({rot:.2f} {px:.2f} {py:.2f})')}>{_esc(ch)}</text>")
            ang += (w / 2 / circumference) * 360
        return g

    # ---- images --------------------------------------------------------------
    def image(self, src, x, y, w, h, fit="cover", rx=0, clip_d=None, opacity=None, id=None, max_scale=2.0, quality=85, transform=None):
        """Embed an image (path, bytes or PIL.Image) as a base64 data URI.

        fit: 'cover' (slice) | 'contain' (meet) | 'stretch'.
        rx or clip_d: clip to a rounded rect or an arbitrary path.
        max_scale: resample the source so it is at most max_scale x the box
        (2 = retina) to keep the file small.
        """
        im = _open_image(src)
        has_alpha = im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info)
        target = (int(w * max_scale), int(h * max_scale))
        if fit == "cover":
            scale = max(target[0] / im.width, target[1] / im.height)
        elif fit == "contain":
            scale = min(target[0] / im.width, target[1] / im.height)
        else:
            scale = max(target[0] / im.width, target[1] / im.height)
        if scale < 1:
            im = im.resize((max(1, round(im.width * scale)), max(1, round(im.height * scale))), Image.LANCZOS)
        buf = io.BytesIO()
        if has_alpha:
            im.convert("RGBA").save(buf, "PNG", optimize=True)
            mime = "image/png"
        else:
            im.convert("RGB").save(buf, "JPEG", quality=quality, optimize=True, progressive=False)
            mime = "image/jpeg"
        href = f"data:{mime};base64," + base64.b64encode(buf.getvalue()).decode()
        par = {"cover": "xMidYMid slice", "contain": "xMidYMid meet", "stretch": "none"}[fit]
        clip_attr = None
        if clip_d or rx:
            cid = self.email._clip(clip_d or shapes.rrect(x, y, w, h, rx))
            clip_attr = f"url(#{cid})"
        self.raw(f"<image{_attrs(id=id, x=x, y=y, width=w, height=h, preserveAspectRatio=par, clip_path=clip_attr, opacity=opacity, href=href, transform=transform)}/>")
        self.email.assets.append(getattr(src, "name", None) or (str(src) if isinstance(src, (str, Path)) else "inline"))

    # ---- composites ----------------------------------------------------------
    def button(self, x, y, w, h, label, family, size=16, weight=700, fill="#000", text_fill="#fff", rx=0,
               stroke=None, stroke_width=None, arrow=False, letter_spacing=None, id=None, upper=False, shadow=None):
        """Rect + centred live text (+ optional arrow path). Returns the group."""
        g = self.g(id or f"CTA {label}")
        if shadow:   # hard offset shadow (dx, dy, colour)
            dx, dy, col = shadow
            g.rect(x + dx, y + dy, w, h, fill=col, rx=rx)
        g.rect(x, y, w, h, fill=fill, rx=rx, stroke=stroke, stroke_width=stroke_width)
        lab = label.upper() if upper else label
        tw = self.measure(lab, family, size, weight, letter_spacing or 0)
        font = self.email.fonts.get(family, weight)
        cap = font.cap_height(size)
        baseline = y + h / 2 + cap / 2
        aw = size * 0.9 if arrow else 0
        gap = 10 if arrow else 0
        tx = x + w / 2 - (aw + gap) / 2
        g.text(tx, baseline, lab, family, size, weight, text_fill, anchor="middle", letter_spacing=letter_spacing)
        if arrow:
            ax = tx + tw / 2 + gap
            g.path(shapes.arrow_right(ax, baseline - cap / 2 - aw / 2, aw), stroke=text_fill, stroke_width=max(1.5, size / 9), cap="round", join="round")
        return g

    def stars(self, x, y, rating=5.0, size=16, gap=3, fill="#111", empty="#D9D9D9", id=None):
        """Five star paths; partial fill for fractional rating via clipPath."""
        g = self.g(id or f"Stars {rating}")
        for i in range(5):
            sx = x + i * (size + gap)
            d = shapes.star(sx, y, size)
            full = rating >= i + 1
            frac = rating - i
            if full:
                g.path(d, fill=fill)
            elif 0 < frac < 1:
                g.path(d, fill=empty)
                cid = self.email._clip(f"M{sx} {y} H{sx + size * frac} V{y + size} H{sx} Z")
                g.raw(f"<path d=\"{d}\" fill=\"{fill}\" clip-path=\"url(#{cid})\"/>")
            else:
                g.path(d, fill=empty)
        return g

    def icon(self, kind, x, y, size, stroke="#000", stroke_width=2, fill="none", id=None):
        fn = getattr(shapes, kind)
        d = fn(x, y, size)
        if kind in ("star", "heart"):
            self.path(d, fill=stroke if fill == "none" else fill, id=id)
        else:
            self.path(d, fill="none", stroke=stroke, stroke_width=stroke_width, cap="round", join="round", id=id)

    def divider(self, y, kind="line", color="#000", x0=MARGIN, x1=WIDTH - MARGIN, stroke_width=1, id=None, **kw):
        if kind == "line":
            self.line(x0, y, x1, y, stroke=color, stroke_width=stroke_width, id=id)
        elif kind == "dashed":
            self.line(x0, y, x1, y, stroke=color, stroke_width=stroke_width, dash=kw.get("dash", "6 6"), id=id)
        elif kind == "dotted":
            self.line(x0, y, x1, y, stroke=color, stroke_width=kw.get("dot", 3), dash=f"0 {kw.get('dot', 3) * 2}", cap="round", id=id)
        elif kind == "zigzag":
            self.path(shapes.zigzag(x0, x1, y, kw.get("step", 8), kw.get("amp", 4)), stroke=color, stroke_width=stroke_width, join="round", id=id)
        elif kind == "wave":
            self.path(shapes.wave(x0, x1, y, kw.get("length", 40), kw.get("amp", 6)), stroke=color, stroke_width=stroke_width, id=id)
        elif kind == "scallop":
            self.path(shapes.scallop_edge(x0, x1, y, kw.get("bump", 10), kw.get("depth", 6), kw.get("down", True)), fill=kw.get("fill", color), id=id)
        else:
            raise ValueError(kind)

    # ---- render --------------------------------------------------------------
    def render(self) -> str:
        tr = f"translate({_num(self.x)} {_num(self.y)})" if (self.x or self.y) else None
        inner = "\n".join(c.render() if isinstance(c, Group) else c for c in self.children)
        return f"<g{_attrs(id=self.id, transform=tr, opacity=self.opacity, clip_path=f'url(#{self.clip})' if self.clip else None)}>\n{inner}\n</g>"


class Email:
    def __init__(self, fonts: FontRegistry, name: str = "welcome-01", width: int = WIDTH, bg: str = "#FFFFFF"):
        self.fonts = fonts
        self.name = name
        self.width = width
        self.bg = bg
        self.sections: list[Group] = []
        self.section_y: dict[str, int] = {}
        self.section_h: dict[str, int] = {}
        self.y = 0
        self._defs: list[str] = []
        self._clip_n = 0
        self.modules: list[Module] = []
        self.assets: list[str] = []
        self.fonts_used: set[tuple[str, int, str]] = set()
        self.notes: list[str] = []

    # sections ----------------------------------------------------------------
    def section(self, id: str, height: int, bg: str | None = None) -> Group:
        g = Group(self, id, 0, self.y)
        if bg:
            g.rect(0, 0, self.width, height, fill=bg, id=None)
        self.sections.append(g)
        self.section_y[id] = self.y
        self.section_h[id] = height
        self.y += int(height)
        return g

    @property
    def height(self) -> int:
        return self.y

    def _check_font(self, family, weight, style="normal"):
        self.fonts.get(family, weight, style)   # raises if not loaded
        self.fonts_used.add((family, int(weight), style))

    def _clip(self, d: str) -> str:
        self._clip_n += 1
        cid = f"clip{self._clip_n}"
        self._defs.append(f'<clipPath id="{cid}"><path d="{d}"/></clipPath>')
        return cid

    def gradient(self, id: str, stops: list[tuple[float, str]], x1=0, y1=0, x2=0, y2=1) -> str:
        """Linear gradient; returns 'url(#id)'. Figma imports linear gradients fine."""
        st = "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops)
        self._defs.append(f'<linearGradient id="{id}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">{st}</linearGradient>')
        return f"url(#{id})"

    def pattern_dots(self, id: str, color: str, size: int = 6, r: float = 1, bg: str | None = None) -> str:
        self._defs.append(f'<pattern id="{id}" width="{size}" height="{size}" patternUnits="userSpaceOnUse">'
                          + (f'<rect width="{size}" height="{size}" fill="{bg}"/>' if bg else "")
                          + f'<circle cx="{size/2}" cy="{size/2}" r="{r}" fill="{color}"/></pattern>')
        return f"url(#{id})"

    # motion ------------------------------------------------------------------
    def module(self, id: str, name: str, section: str, y_local: int, h: int, states: int, durations_ms,
               what_moves: str, frame1: str, assets=(), facts=(), tween_frames: int = 0) -> Module:
        if isinstance(durations_ms, int):
            durations_ms = [durations_ms] * states
        if len(durations_ms) != states:
            raise ValueError("one duration per state")
        if any(d < 120 for d in durations_ms):
            raise ValueError("no held state under 120 ms (brief 12)")
        if not 3 <= states <= 8:
            raise ValueError("3 to 8 held states per module (brief 12)")
        m = Module(id, name, section, self.section_y[section] + y_local, h, states, list(durations_ms),
                   what_moves, frame1, list(assets), list(facts), tween_frames)
        self.modules.append(m)
        return m

    # output -------------------------------------------------------------------
    def to_svg(self) -> str:
        body = "\n".join(s.render() for s in self.sections)
        defs = ("<defs>\n" + "\n".join(self._defs) + "\n</defs>\n") if self._defs else ""
        return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
                f'width="{self.width}" height="{self.height}" viewBox="0 0 {self.width} {self.height}">\n'
                f'{defs}<rect id="Canvas" width="{self.width}" height="{self.height}" fill="{self.bg}"/>\n'
                f'{body}\n</svg>\n')

    def save(self, path) -> Path:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(self.to_svg(), encoding="utf-8")
        return p

    def motion_spec_rows(self) -> list[dict]:
        return [{
            "ID": m.id, "Section": m.section, "What moves": m.what_moves, "Frame-1 state": m.frame1,
            "Band": f"600x{m.h} at y={m.y}", "States & timing": " / ".join(f"{d}ms" for d in m.durations_ms) + f" ({m.states} states, loop {m.loop_ms}ms)",
            "Assets": ", ".join(m.assets), "Facts used": ", ".join(m.facts),
        } for m in self.modules]


def _open_image(src) -> Image.Image:
    if isinstance(src, Image.Image):
        return src
    if isinstance(src, (bytes, bytearray)):
        return Image.open(io.BytesIO(src))
    return Image.open(src)
