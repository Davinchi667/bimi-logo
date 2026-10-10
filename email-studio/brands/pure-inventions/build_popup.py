"""Pure Inventions · P0 signup popup (the missing front door), a separate 600 px frame.
Source: COPY.md P0 + DESIGN_INTENT.md M1. Copy verbatim.
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "tools"))
sys.path.insert(0, str(HERE))
from emailkit import Email, FontRegistry, shapes  # noqa: E402
from build import fonts, cta, dropper, L, R, BLUE, INK, WHITE, GREY, A  # noqa: E402

BRAND = "pure-inventions"
NAME = "pure-inventions_popup-P0"
OUT = "final/popup"
W, H = 600, 580
CHIPS = ["drink more water to stay hydrated all day", "support my immune system and wellness", "support my skin and beauty routine", "feel more relaxed and rested"]


def build(state: dict | None = None) -> Email:
    state = state or {}
    k = state.get("M1", 0)
    e = Email(fonts, name=NAME, bg="#000000")
    s = e.section("P0 Popup", H, bg="#000000")
    s.image(A / "popup_backdrop.jpg", 0, 0, W, H, fit="cover", id="Blurred homepage backdrop")
    s.rect(0, 0, W, H, fill="#000000", opacity=0.4)
    m1 = s.g("M1 Popup chips band")
    card = m1.g("Card")
    card.rrect(60, 70, 480, H - 90, 16, fill=WHITE)
    bt = card.g("Bottle", x=300, y=34, rotate=8)
    bt.image(A / "coconut_cut.png", -66, 0, 132, 148, fit="contain", id="Coconut bottle tilted")
    dropper(card, 318, -6, h=36)
    card.path(shapes.drop(319, 44, 4), fill=BLUE)
    card.text(300, 190, "TASTED US AT A SPA?", R, 14, 500, BLUE, anchor="middle", letter_spacing=2)
    card.text(300, 226, "What brings you to Pure Inventions?", L, 24, 500, INK, anchor="middle")
    card.text(100, 258, "I want to...", R, 15, 500, INK)
    cy = 272
    for i, chip in enumerate(CHIPS):
        filled = (i == 0 and k != 1)
        card.rrect(100, cy, 400, 32, 16, fill=BLUE if filled else "none", stroke=BLUE, stroke_width=1.5)
        card.text(300, cy + 21, chip, R, 14, 500 if filled else 400, WHITE if filled else INK, anchor="middle")
        cy += 38
    if k == 2:
        cur = card.g("Cursor")
        cur.path("M0 0 L0 16 L4 12 L7 19 L10 18 L7 11 L12 11 Z", fill=INK, stroke=WHITE, stroke_width=1, transform="translate(420 282)")
    if k in (0, 3):
        fld = card.g("Email field")
        fld.rect(100, cy + 8, 400, 34, fill=WHITE, stroke="#C9CFD4", stroke_width=1, rx=17)
        fld.text(118, cy + 30, "Your email", R, 14, 400, "#8A9299")
        cta(fld, 100, cy + 52, label="SEND ME MY FLAVOR PICKS", w=400, where="P0")
        fld.text(300, cy + 128, "Free Shipping Over $50.", R, 14, 400, INK, anchor="middle",
                 runs=[("Free Shipping Over $50. ", {}), ("No thanks", {"decoration": "underline", "fill": "#5E6870"})])
    e.module("M1", "Popup chips", "P0 Popup", 60, H - 70, states=3, durations_ms=[2800, 600, 600],
             what_moves="all four chips go to outline with no email field, a cursor taps chip 1 which fills blue, then the email field and button return",
             frame1="chip 1 filled, email field and button visible", assets=["Coconut bottle cut-out"], facts=["four homepage picker lines"])
    return e


if __name__ == "__main__":
    em = build({})
    print(em.save(HERE / "final" / f"{NAME}.svg"), em.height)
