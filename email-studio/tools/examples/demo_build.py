"""Demo brand build: exercises every builder feature so the toolkit can be tested
without a real brand. Not a design reference. Run tools/studio.py test.

A real brand build lives at brands/<brand>/build.py and follows the same shape:
    fonts = FontRegistry(); fonts.google(...)
    def build(state: dict) -> Email
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from emailkit import Email, FontRegistry, shapes, MARGIN  # noqa: E402

BRAND = "_demo"
NAME = "demo_welcome-01"
fonts = FontRegistry()
fonts.google("Fraunces", weights=(400, 700, 900))
fonts.google("Inter", weights=(400, 500, 700))
DISPLAY, BODY = "Fraunces", "Inter"
INK, PAPER, ACCENT, SOFT = "#1B1B1B", "#F6F1E7", "#D64B2A", "#E8DFCF"


def _texture(seed=1, size=(600, 420)) -> Image.Image:
    """Procedural photo stand-in so the demo has a real raster image to embed."""
    rng = np.random.default_rng(seed)
    y, x = np.mgrid[0:size[1], 0:size[0]].astype(np.float32)
    base = 120 + 60 * np.sin(x / 70) * np.cos(y / 55) + rng.normal(0, 14, size[::-1])
    r = np.clip(base + 60, 0, 255)
    g = np.clip(base + 20 * np.sin(y / 30), 0, 255)
    b = np.clip(base - 40, 0, 255)
    return Image.fromarray(np.dstack([r, g, b]).astype(np.uint8), "RGB")


def build(state: dict | None = None) -> Email:
    state = state or {}
    e = Email(fonts, name="demo_welcome-01", bg=PAPER)

    # 01 Hero (image + display type + mixed-run line)
    s = e.section("01 Hero", 600, bg=PAPER)
    s.image(_texture(1), 0, 0, 600, 340, fit="cover", id="Hero photo")
    s.rect(0, 300, 600, 40, fill=PAPER)
    s.divider(300, kind="scallop", color=PAPER, bump=20, depth=10, down=False, x0=0, x1=600)
    s.text(MARGIN, 400, "Welcome to the", DISPLAY, 24, 400, INK)
    s.text(MARGIN, 456, "demo kitchen", DISPLAY, 56, 900, INK)
    s.text(MARGIN, 500, "Real copy goes here,", BODY, 16, 400, INK,
           runs=[("Real copy goes here, ", {}), ("word for word.", {"weight": 700, "fill": ACCENT})])
    s.button(MARGIN, 524, 220, 48, "Shop the range", BODY, 15, 700, fill=INK, text_fill=PAPER, rx=24, arrow=True)

    # 02 Ticker band (M1: 4 states, slides phrases)
    M1_PHRASES = ["Small batch", "Cold pressed", "Ships in 2 days", "Made in Lisbon"]
    s = e.section("02 Ticker", 56, bg=INK)
    k = state.get("M1", 0)
    x = MARGIN - k * 28
    g = s.g("M1 Ticker band", clip=(0, 0, 600, 56))
    for i in range(6):
        ph = M1_PHRASES[(i + k) % 4].upper()
        w = g.text(x, 35, ph, BODY, 14, 700, PAPER, letter_spacing=2)
        g.path(shapes.star(x + w + 14, 20, 14), fill=ACCENT)
        x += w + 42
    e.module("M1", "Ticker", "02 Ticker", 0, 56, states=4, durations_ms=[700, 700, 700, 700],
             what_moves="phrases slide left by one slot", frame1="phrase 1 leads", assets=[], facts=["phrases from copy"])

    # 03 Proof (stars as paths + wrapped quote)
    s = e.section("03 Proof", 300, bg=SOFT)
    s.stars(MARGIN, 40, 4.5, size=22, gap=4, fill=INK, empty="#BFB5A3")
    quote = "This is a wrapped multi-line quote that uses one tspan per line, each with its own x and y, so Figma keeps every line live and editable."
    h = s.text_block(MARGIN, 110, quote, DISPLAY, 26, 540, 400, INK, line_height=34)
    s.text(MARGIN, 110 + h + 20, "A real customer name, exactly as printed", BODY, 14, 500, "#5C5547")
    s.divider(280, kind="dashed", color=INK)

    # 04 Toggle (M2: 3 states, moving pill)
    s = e.section("04 Compare", 260, bg=PAPER)
    k2 = state.get("M2", 0)
    labels = ["Them", "Us", "Both"]
    g = s.g("M2 Toggle band")
    g.rrect(MARGIN, 40, 540, 56, 28, fill="#FFFFFF", stroke=INK, stroke_width=2)
    g.rrect(MARGIN + 4 + k2 * 177, 44, 174, 48, 24, fill=INK)
    for i, lab in enumerate(labels):
        g.text(MARGIN + 4 + i * 177 + 87, 78, lab, BODY, 16, 700, PAPER if i == k2 else INK, anchor="middle")
    bullets = [["Flat type", "No surface", "Stock photo"], ["Display moment", "Textured surface", "Real product"], ["Mixed", "Mixed", "Mixed"]][k2]
    for i, b in enumerate(bullets):
        g.icon("check", MARGIN, 128 + i * 36, 20, stroke=ACCENT, stroke_width=2.5)
        g.text(MARGIN + 32, 144 + i * 36, b, BODY, 16, 400, INK)
    e.module("M2", "Toggle", "04 Compare", 0, 260, states=3, durations_ms=[1200, 1200, 1200],
             what_moves="pill slides across three tabs, bullets swap", frame1="tab 1 selected", facts=["comparison from copy"])

    # 05 Curved text badge + CTA
    s = e.section("05 Badge", 300, bg=INK)
    s.circle(300, 120, 86, fill=ACCENT)
    s.curved_text(300, 120, 66, "SMALL BATCH  SMALL BATCH  ", BODY, 14, 700, PAPER, start_deg=-90, letter_spacing=3, id="Curved badge text")
    s.text(300, 128, "NEW", DISPLAY, 28, 900, PAPER, anchor="middle")
    s.button(300 - 130, 230, 260, 52, "Start here", BODY, 16, 700, fill=PAPER, text_fill=INK, rx=0, shadow=(5, 5, ACCENT))

    # 06 Footer (small text allowed)
    s = e.section("06 Footer", 140, bg=SOFT)
    s.text(300, 50, "Demo Brand, 1 Example Street, Lisbon", BODY, 12, 400, "#5C5547", anchor="middle")
    s.text(300, 72, "You are getting this because you signed up at demo.example", BODY, 12, 400, "#5C5547", anchor="middle")
    s.text(300, 100, "Unsubscribe", BODY, 12, 500, INK, anchor="middle", decoration="underline")
    return e


if __name__ == "__main__":
    em = build({})
    out = HERE.parent.parent / "brands" / "_demo" / "final"
    p = em.save(out / "demo_welcome-01.svg")
    print(p, em.height, "px", len(em.modules), "modules")
