"""Font handling for the email builder.

- fetch Google Fonts as TTF into tools/fonts/cache (so the renderer and the
  measurer use the exact same file)
- measure string widths with fontTools (advance widths + kerning pairs when the
  font has a 'kern' table; GPOS kerning is approximated by the kern table only)
- register local TTF/OTF/WOFF files for proprietary brand fonts you have on disk
- build the @font-face CSS the renderer injects so Chromium renders the same
  font the measurer measured

Figma: Figma matches fonts by family name at import and silently falls back to
Inter for anything it doesn't have. Google Fonts are available in Figma, so
prefer them. `FontRegistry.figma_report()` lists every family used and whether
it is known to be a Google Font (via fonts.google.com metadata lookup).
"""
from __future__ import annotations

import io
import json
import os
import re
import urllib.parse
from dataclasses import dataclass, field
from pathlib import Path

import requests
from fontTools.ttLib import TTFont

HERE = Path(__file__).resolve().parent
CACHE = HERE.parent / "fonts" / "cache"
CACHE.mkdir(parents=True, exist_ok=True)

# An old Firefox UA makes the Google Fonts CSS API return TTF instead of woff2.
TTF_UA = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:1.0) Gecko/20100101 Firefox/1.0"
WOFF2_UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"

HEADERS = {"User-Agent": TTF_UA}


def _slug(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "", s)


@dataclass
class Font:
    family: str          # exact family name as written in font-family
    weight: int          # numeric weight
    style: str           # normal | italic
    path: Path           # TTF/OTF on disk
    source: str = "google"   # google | local
    _tt: TTFont | None = field(default=None, repr=False, compare=False)

    @property
    def tt(self) -> TTFont:
        if self._tt is None:
            self._tt = TTFont(str(self.path), lazy=True)
        return self._tt

    @property
    def upem(self) -> int:
        return self.tt["head"].unitsPerEm

    _cmap_cache: dict | None = field(default=None, repr=False, compare=False)
    _kern_cache: dict | None = field(default=None, repr=False, compare=False)

    def _cmap(self):
        if self._cmap_cache is None:
            self._cmap_cache = self.tt.getBestCmap()
        return self._cmap_cache

    def _kern(self):
        if self._kern_cache is None:
            pairs = {}
            if "kern" in self.tt:
                for sub in self.tt["kern"].kernTables:
                    if hasattr(sub, "kernTable"):
                        pairs.update(sub.kernTable)
            self._kern_cache = pairs
        return self._kern_cache

    def width(self, text: str, size: float, letter_spacing: float = 0.0) -> float:
        """Advance width of `text` at `size` px (letter_spacing in px per glyph)."""
        cmap = self._cmap()
        hmtx = self.tt["hmtx"]
        kern = self._kern()
        order = self.tt.getGlyphOrder()
        notdef = order[0] if order else ".notdef"
        total = 0
        prev = None
        for ch in text:
            g = cmap.get(ord(ch), notdef)
            try:
                total += hmtx[g][0]
            except KeyError:
                total += hmtx[notdef][0]
            if prev is not None:
                total += kern.get((prev, g), 0)
            prev = g
        px = total * size / self.upem
        if letter_spacing and text:
            px += letter_spacing * (len(text) - 1)
        return px

    def ascent(self, size: float) -> float:
        hhea = self.tt["hhea"]
        return hhea.ascent * size / self.upem

    def descent(self, size: float) -> float:
        hhea = self.tt["hhea"]
        return -hhea.descent * size / self.upem

    def cap_height(self, size: float) -> float:
        os2 = self.tt.get("OS/2")
        cap = getattr(os2, "sCapHeight", 0) or int(self.upem * 0.7)
        return cap * size / self.upem

    def x_height(self, size: float) -> float:
        os2 = self.tt.get("OS/2")
        xh = getattr(os2, "sxHeight", 0) or int(self.upem * 0.5)
        return xh * size / self.upem


class FontRegistry:
    """Holds every font an email uses. One registry per build."""

    def __init__(self):
        self.fonts: dict[tuple[str, int, str], Font] = {}
        self.substitutes: dict[str, str] = {}   # brand font -> Google substitute used

    # ---- loading --------------------------------------------------------
    def google(self, family: str, weights=(400, 700), italics=False) -> list[Font]:
        """Download a Google Font family (TTF) into the cache and register it."""
        out = []
        for w in weights:
            styles = ["normal", "italic"] if italics else ["normal"]
            for st in styles:
                f = self._google_one(family, int(w), st)
                if f:
                    out.append(f)
        if not out:
            raise RuntimeError(f"Google Fonts has no '{family}' at weights {weights}")
        return out

    def _google_one(self, family: str, weight: int, style: str) -> Font | None:
        fn = CACHE / f"{_slug(family)}-{weight}{'i' if style == 'italic' else ''}.ttf"
        if not fn.exists():
            ital = 1 if style == "italic" else 0
            axis = f"ital,wght@{ital},{weight}" if style == "italic" else f"wght@{weight}"
            css_url = ("https://fonts.googleapis.com/css2?family="
                       + urllib.parse.quote(family) + f":{axis}&display=swap")
            r = requests.get(css_url, headers=HEADERS, timeout=30)
            if r.status_code != 200:
                return None
            urls = re.findall(r"url\((https://fonts\.gstatic\.com/[^)]+)\)", r.text)
            if not urls:
                return None
            # Prefer the latin subset if several ranges come back: the first
            # 'latin' block is normally last in the CSS. Take the last url.
            data = requests.get(urls[-1], headers=HEADERS, timeout=60).content
            if urls[-1].endswith(".woff2"):
                data = _woff2_to_ttf(data)
            fn.write_bytes(data)
        f = Font(family=family, weight=weight, style=style, path=fn, source="google")
        self.fonts[(family, weight, style)] = f
        return f

    def local(self, family: str, path: str | Path, weight: int = 400, style: str = "normal") -> Font:
        """Register a font file you already have (brand's proprietary font)."""
        p = Path(path)
        if p.suffix.lower() in (".woff", ".woff2"):
            data = p.read_bytes()
            data = _woff2_to_ttf(data) if p.suffix.lower() == ".woff2" else _woff_to_ttf(data)
            p2 = CACHE / f"{_slug(family)}-{weight}{'i' if style == 'italic' else ''}.ttf"
            p2.write_bytes(data)
            p = p2
        f = Font(family=family, weight=weight, style=style, path=p, source="local")
        self.fonts[(family, weight, style)] = f
        return f

    def substitute(self, brand_font: str, google_family: str, weights=(400, 700), italics=False) -> list[Font]:
        """Record that `brand_font` is proprietary and we render with `google_family`."""
        self.substitutes[brand_font] = google_family
        return self.google(google_family, weights, italics=italics)

    # ---- lookup ---------------------------------------------------------
    def get(self, family: str, weight: int = 400, style: str = "normal") -> Font:
        key = (family, int(weight), style)
        if key in self.fonts:
            return self.fonts[key]
        # nearest weight in same family
        cands = [f for (fam, w, st), f in self.fonts.items() if fam == family and st == style]
        if not cands:
            cands = [f for (fam, w, st), f in self.fonts.items() if fam == family]
        if not cands:
            raise KeyError(f"font '{family}' not loaded; call registry.google('{family}', weights=...) first")
        return min(cands, key=lambda f: abs(f.weight - int(weight)))

    def families(self) -> list[str]:
        return sorted({fam for (fam, _, _) in self.fonts})

    # ---- CSS for the renderer -----------------------------------------
    def font_face_css(self, as_data_uri: bool = False) -> str:
        css = []
        for (fam, w, st), f in self.fonts.items():
            if as_data_uri:
                import base64
                b64 = base64.b64encode(f.path.read_bytes()).decode()
                src = f"url(data:font/ttf;base64,{b64})"
            else:
                src = f"url(file://{f.path.resolve()})"
            css.append(
                f"@font-face{{font-family:'{fam}';font-weight:{w};font-style:{st};src:{src} format('truetype');}}"
            )
        return "\n".join(css)

    def figma_report(self) -> list[dict]:
        rows = []
        for fam in self.families():
            srcs = {f.source for (ff, _, _), f in self.fonts.items() if ff == fam}
            rows.append({
                "family": fam,
                "source": ",".join(sorted(srcs)),
                "in_figma_by_default": "google" in srcs,
                "substitute_for": [k for k, v in self.substitutes.items() if v == fam],
            })
        return rows


def _woff2_to_ttf(data: bytes) -> bytes:
    from fontTools.ttLib import woff2
    inp = io.BytesIO(data)
    out = io.BytesIO()
    woff2.decompress(inp, out)
    return out.getvalue()


def _woff_to_ttf(data: bytes) -> bytes:
    tt = TTFont(io.BytesIO(data))
    tt.flavor = None
    out = io.BytesIO()
    tt.save(out)
    return out.getvalue()


def google_font_exists(family: str) -> bool:
    """True if fonts.google.com serves this family."""
    url = "https://fonts.googleapis.com/css2?family=" + urllib.parse.quote(family) + "&display=swap"
    try:
        return requests.get(url, headers=HEADERS, timeout=20).status_code == 200
    except requests.RequestException:
        return False
