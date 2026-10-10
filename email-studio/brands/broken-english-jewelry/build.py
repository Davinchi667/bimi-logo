"""Broken English Jewelry · spec welcome email 01 · "The ear map".
Source: brands/broken-english-jewelry/COPY.md + DESIGN_INTENT.md (10 Oct 2026). Copy verbatim.
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "tools"))
from emailkit import Email, FontRegistry, shapes, MARGIN  # noqa: E402

BRAND = "broken-english-jewelry"
NAME = "broken-english-jewelry_welcome-01"
A = HERE / "assets"

fonts = FontRegistry()
fonts.substitute("Frutiger Serif", "Halant", weights=(300, 400, 500))   # Halant is the serif the live site computes for h2
fonts.google("Open Sans", weights=(400, 500, 600, 700))
H, O = "Halant", "Open Sans"

WHITE, WARM, OFF, SAND, GOLD, GREY, BLACK = "#FFFFFF", "#FBFAF7", "#FAFAFA", "#E6DDCB", "#AB8C52", "#757575", "#000000"
INK = "#101820"
W = 600
URL = "https://brokenenglishjewelry.com/collections/the-ear-edit"
DESIGNERS = ["TROUVER", "FIAMETTA", "LIZZIE MANDLER", "PASCALE MONVOISIN", "HIROTAKA", "FOUNDRAE", "ANITA KO", "ENGELBERT"]

PINS = [  # (place, designer, name, metals, price, image, pin xy in the ear box, cumulative)
    ("Lobe", "TROUVER", "Half Paved Huggie 9.5mm - Yellow Gold", "14K yellow gold, pave white diamonds", "$590.00", "huggie_front_cut.png", (72, 338), "$590.00"),
    ("Second lobe", "FIAMETTA", "Emerald Cut Mini Stud Earring", "14K Yellow Gold, emerald", "$550.00", "emerald_stud_cut.png", (100, 322), "$1,140.00"),
    ("Upper lobe", "LIZZIE MANDLER", "Emerald Knife Edge Bar Stud Earring", "18K Yellow Gold, emerald, diamond", "$400.00", "knife_edge_cut.png", (124, 292), "$1,540.00"),
    ("Helix", "PASCALE MONVOISIN", "Diamond White Pierrot Earring", "9K Yellow Gold and White Gold, diamond", "$430.00", "pierrot_cut.png", (176, 160), "$1,970.00"),
    ("Upper helix", "HIROTAKA", "Bow Ear Cuff", "10K yellow gold", "$570.00", "bow_cuff_cut.png", (150, 62), "$2,540.00"),
]
EAR_PATHS = [  # jeweller's line sketch in a 200 x 380 box
    "M105 18 C160 8 198 50 196 115 C194 180 176 250 150 305 C133 340 105 372 72 368 C45 364 28 338 32 310 C35 285 48 272 55 255 C62 235 60 200 70 170 C76 150 82 128 92 110 C97 98 99 70 105 18",
    "M118 42 C160 42 178 82 174 128 C171 170 160 215 142 255",
    "M98 112 C120 126 140 160 145 200 C148 230 135 262 115 282",
    "M76 192 C90 198 96 214 92 234",
    "M112 204 C126 222 128 246 118 266",
]


def logo(g, cx, y, h, id="Logo"):
    w = h * 10.0
    g.image(A / "logo_black.png", cx - w / 2, y, w, h, fit="contain", id=id)


def cta(g, x, y, where=""):
    """The one CTA shape: 260 x 50 black rectangle, white Open Sans caps, 2 px tracking."""
    return g.button(x, y, 260, 50, "SHOP THE EAR EDIT", O, 14, 600, fill=BLACK, text_fill=WHITE, rx=0, letter_spacing=2, id=f"CTA SHOP THE EAR EDIT {where}".strip())


def diamond(g, cx, cy, r, fill):
    g.path(f"M{cx} {cy - r} L{cx + r} {cy} L{cx} {cy + r} L{cx - r} {cy} Z", fill=fill)


def build(state: dict | None = None) -> Email:
    state = state or {}
    e = Email(fonts, name=NAME, bg=WHITE)
    k1, k2, k3 = state.get("M1", 0), state.get("M2", 0), state.get("M3", 0)

    # ------------------------------------------------------------------ S1 Hero 480
    H1 = 490
    s = e.section("01 Hero", H1, bg=WARM)
    s.image(A / "grain_light.jpg", 0, 0, W, H1, fit="stretch", opacity=0.5, id="Grain S1")
    bar = s.g("Announcement bar")
    bar.rect(0, 0, W, 34, fill=WHITE); bar.line(0, 34, W, 34, stroke=SAND, stroke_width=1)
    bar.text(300, 22, "FREE GROUND SHIPPING + RETURNS ON U.S. ORDERS OVER $250", O, 14, 600, GOLD, anchor="middle", letter_spacing=1)
    logo(s, 300, 60, 22, id="Logo black")
    # M1 designer ticker strip
    tk = s.g("M1 Designer ticker band", clip=(0, 104, W, 32))
    tk.rect(0, 104, W, 32, fill=OFF); tk.line(0, 104, W, 104, stroke=SAND, stroke_width=1); tk.line(0, 136, W, 136, stroke=SAND, stroke_width=1)
    items = [(d, tk.measure(d, O, 14, 600, 3)) for d in DESIGNERS]
    unit = sum(tw + 40 for _, tw in items)
    x = 24 - unit / 6 * k1
    while x < W + unit:
        for d, tw in items:
            if -unit < x < W + 60:
                tk.text(x, 125, d, O, 14, 600, GOLD, letter_spacing=3)
                diamond(tk, x + tw + 20, 120, 4, GOLD)
            x += tw + 40
    e.module("M1", "Designer ticker", "01 Hero", 104, 32, states=6, durations_ms=[450] * 6,
             what_moves="the designer names slide left one sixth of the loop per frame, seamless", frame1="TROUVER · FIAMETTA · LIZZIE MANDLER lead, readable from the left", facts=["designer names from the Designers menu and product vendors"])
    s.text(MARGIN, 198, "THE EAR EDIT", O, 14, 600, GOLD, letter_spacing=3)
    hl = s.g("Headline")
    hl.text(MARGIN, 248, "Build the perfect", H, 46, 400, INK)
    hl.text(MARGIN, 298, "ear stack.", H, 46, 400, INK)
    s.text_block(MARGIN, 330, "Available as single earrings in several sizes. Start with one.", O, 15, 300, 400, INK, line_height=22, max_lines=3)
    s.text_block(MARGIN, 384, "GET 10% OFF* your first order of $250 or more.", O, 14, 300, 600, GOLD, line_height=20, max_lines=2)
    cta(s, MARGIN, 424, where="S1")
    s.image(A / "huggie_front_cut.png", 398, 172, 240, 303, fit="contain", id="Half Paved Huggie (cropped by the edge)")

    # ------------------------------------------------------------------ S2 The 10 percent and its terms 270
    H2 = 270
    s2 = e.section("02 The ten percent", H2, bg=SAND)
    s2.image(A / "grain_light.jpg", 0, 0, W, H2, fit="stretch", opacity=0.5, id="Grain S2")
    s2.text(MARGIN, 176, "10%", H, 110, 400, INK, id="Giant ten percent")
    col = s2.g("Terms column")
    cx = 258
    col.text(cx, 64, "GET 10% OFF*", O, 16, 700, INK, letter_spacing=1)
    y = 92
    y += col.text_block(cx, y, "Sign up for our newsletter to receive a discount code for first time customers.", O, 14, 312, 400, INK, line_height=20) + 8
    y += col.text_block(cx, y, "*Offer valid for orders $250 or more. Some exclusions may apply as not all pieces offer this discount.", O, 14, 312, 400, GREY, line_height=19) + 10
    col.text_block(cx, y, "Free Ground Shipping + Returns on U.S. orders over $250.", O, 14, 312, 600, INK, line_height=20)

    # ------------------------------------------------------------------ S3 The ear map
    s3 = e.section("03 Ear map", 10, bg=OFF)
    s3.image(A / "grain_light.jpg", 0, 0, W, 980, fit="stretch", opacity=0.5, id="Grain S3")
    s3.text(MARGIN, 52, "ONE EAR, FIVE SINGLES", O, 14, 600, GOLD, letter_spacing=3)
    s3.text(MARGIN, 96, "Mix classics, funky pieces,", H, 30, 400, INK)
    s3.text(MARGIN, 132, "and vintage.", H, 30, 400, INK)
    shown = {0: 5, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4}[k2]
    m2 = s3.g("M2 Ear map band")
    EX, EY = 36, 162
    ear = m2.g("Ear sketch", x=EX, y=EY)
    for d in EAR_PATHS:
        ear.path(d, fill="none", stroke=INK, stroke_width=1.5, cap="round", join="round")
    rows = m2.g("Pin labels")
    RX, RY0 = 300, 166
    order = [4, 3, 2, 1, 0]   # top row = upper helix, bottom row = lobe, so leaders never cross
    ry = RY0
    for ri, pi in enumerate(order):
        place, designer, name, metals, price, img, (px, py), cum = PINS[pi]
        on = pi < shown
        row = rows.g(f"Pin {pi + 1} {place}")
        ax, ay = EX + px, EY + py
        # leader + pin
        if on:
            row.line(ax, ay, RX - 10, ry + 30, stroke=GOLD, stroke_width=1)
            row.circle(ax, ay, 7, fill=WHITE, stroke=GOLD, stroke_width=1.5)
            row.text(ax, ay + 4, str(pi + 1), O, 14, 700, GOLD, anchor="middle")
            row.image(A / img, RX, ry, 60, 60, fit="contain", id=f"{name} cut-out")
        else:
            row.circle(ax, ay, 3, fill="none", stroke=SAND, stroke_width=1)
        tx = RX + 72
        row.text(tx, ry + 12, designer, O, 14, 600, GOLD, letter_spacing=1.5)
        hh = row.text_block(tx, ry + 32, name, H, 16, 198, 500, INK, line_height=19, max_lines=2)
        yy = ry + 32 + hh - 19 + 17
        hh2 = row.text_block(tx, yy, metals, O, 14, 198, 400, GREY, line_height=17, max_lines=2)
        yy += hh2 - 17 + 17
        row.text(tx, yy, price, O, 14, 600, INK)
        ry = yy + 16
        if ri < 4:
            rows.line(RX, ry, W - MARGIN, ry, stroke=SAND, stroke_width=1)
        ry += 16
    # running total as a receipt tally, under the ear
    rc = m2.g("Running total receipt")
    TX, TY, TW = 36, max(ry + 8, EY + 400), 220
    rc.line(TX, TY, TX + TW, TY, stroke=INK, stroke_width=1)
    rc.text(TX, TY + 20, "RUNNING TOTAL", O, 14, 600, INK, letter_spacing=2)
    ty = TY + 28
    for pi in range(5):
        ty += 20
        on = pi < shown
        rc.text(TX, ty, f"PIN {pi + 1} · {PINS[pi][0].upper()}", O, 14, 400 if on else 400, INK if on else "#C9C2B6", letter_spacing=0.5)
        rc.text(TX + TW, ty, PINS[pi][4] if on else "", O, 14, 500, INK, anchor="end")
    ty += 12
    rc.line(TX, ty, TX + TW, ty, stroke=INK, stroke_width=1, dash="2 3")
    ty += 22
    total = "$0.00" if shown == 0 else PINS[shown - 1][7]
    rc.text(TX, ty, "TOTAL", O, 14, 700, INK, letter_spacing=2)
    rc.text(TX + TW, ty, total, O, 16, 700, INK, anchor="end")
    ty += 26
    if shown >= 1:
        rc.path(shapes.check(TX, ty - 13, 15), fill="none", stroke=GOLD, stroke_width=2, cap="round", join="round")
    else:
        rc.rect(TX + 2, ty - 11, 11, 11, fill="none", stroke=SAND, stroke_width=1)
    rc.text(TX + 22, ty, "$250 or more: the 10% offer condition.", O, 14, 500, GOLD if shown >= 1 else GREY)
    ty += 8
    rc.line(TX, ty, TX + TW, ty, stroke=INK, stroke_width=1)
    band_bottom = max(ty + 10, ry)
    e.module("M2", "Ear map build", "03 Ear map", 150, band_bottom - 150, states=6, durations_ms=[3000, 600, 700, 700, 700, 700],
             what_moves="the ear outline stays; pins, leaders and cut-outs land one by one while the receipt adds each price and ticks the $250 line with the first piece",
             frame1="all five pins on, total $2,540.00, $250 ticked", assets=["five product cut-outs"], facts=["five .js prices", "Sold as a single", "$250 offer condition"])
    y3 = band_bottom + 26
    hh = s3.text_block(MARGIN, y3, "Studs and huggies are sold as a single. Prices as listed on brokenenglishjewelry.com on 10 Oct 2026. Some exclusions may apply as not all pieces offer this discount.", O, 14, 540, 400, GREY, line_height=19)
    y3 += hh + 18
    cta(s3, MARGIN, y3, where="S3")
    S3H = y3 + 50 + 48
    e.section_h["03 Ear map"] = S3H; e.y = e.section_y["03 Ear map"] + S3H
    s3.children[0] = f'<rect x="0" y="0" width="{W}" height="{S3H}" fill="{OFF}"/>'

    # ------------------------------------------------------------------ S4 Laura
    s4 = e.section("04 Laura", 10, bg=WHITE)
    s4.image(A / "grain_light.jpg", 0, 0, W, 480, fit="stretch", opacity=0.5, id="Grain S4")
    s4.line(MARGIN, 0, W - MARGIN, 0, stroke=SAND, stroke_width=1)
    q = s4.g("Quotes")
    y4 = 70
    hh = q.text_block(MARGIN, y4, "“Broken English is a language unto itself, synonymous with the laid-back luxury that defines how women wear their jewelry today.”", H, 24, 396, 400, INK, line_height=32)
    y4 += hh + 6
    q.text(MARGIN, y4, "- FOUNDER, LAURA FREEDMAN", O, 14, 600, GOLD, letter_spacing=2)
    y4 += 40
    hh = q.text_block(MARGIN, y4, "“A curated jewelry collection should be a real mix of classics, funky pieces, and vintage jewelry.”", H, 20, 396, 400, INK, line_height=27)
    y4 += hh
    rail = s4.g("Fact rail")
    rail.line(458, 60, 458, y4, stroke=SAND, stroke_width=1)
    rail.text_block(474, 86, "Established in 2006", O, 14, 96, 600, INK, line_height=18)
    rail.line(474, 130, 540, 130, stroke=SAND, stroke_width=1)
    rail.text_block(474, 158, "Boutiques in Los Angeles and New York", O, 14, 96, 400, INK, line_height=18)
    S4H = y4 + 44
    s4.line(MARGIN, S4H - 1, W - MARGIN, S4H - 1, stroke=SAND, stroke_width=1)
    e.section_h["04 Laura"] = S4H; e.y = e.section_y["04 Laura"] + S4H
    s4.children[0] = f'<rect x="0" y="0" width="{W}" height="{S4H}" fill="{WHITE}"/>'

    # ------------------------------------------------------------------ S5 Client Care (chat)
    H5 = 330
    s5 = e.section("05 Client Care", H5, bg=SAND)
    s5.image(A / "grain_light.jpg", 0, 0, W, H5, fit="stretch", opacity=0.5, id="Grain S5")
    s5.text(MARGIN, 52, "EXPERT ADVICE", O, 14, 600, GOLD, letter_spacing=3)
    m3 = s5.g("M3 Chat band")
    b1 = m3.g("Bubble incoming")
    b1.rrect(MARGIN, 76, 170, 44, 16, fill="#EDE8DF", stroke="#D8CDB8", stroke_width=1)
    b1.text(MARGIN + 20, 104, "Can't decide?", O, 16, 400, INK)
    if k3 == 2:
        td = m3.g("Typing dots")
        td.rrect(MARGIN, 134, 70, 36, 14, fill="#EDE8DF", stroke="#D8CDB8", stroke_width=1)
        for i in range(3):
            td.circle(MARGIN + 22 + i * 13, 152, 4, fill=GREY, opacity=0.5 + 0.25 * i)
    if k3 == 0:
        b2 = m3.g("Bubble reply")
        b2.rrect(170, 134, 400, 104, 16, fill=WHITE)
        b2.text_block(192, 164, "We have the best Client Care team ready to help you find your next obsession.", O, 15, 356, 400, INK, line_height=22, max_lines=3)
    e.module("M3", "Chat", "05 Client Care", 66, 184, states=3, durations_ms=[3600, 600, 800],
             what_moves="the question shows alone, typing dots appear, then the Client Care reply bubble lands", frame1="both bubbles visible", facts=["about page Client Care line"])
    s5.text(170, 282, "support@brokenenglishjewelry.com", O, 14, 600, INK, decoration="underline")

    # ------------------------------------------------------------------ S6 Laura's Picks
    s6 = e.section("06 Lauras Picks", 10, bg=WHITE)
    s6.image(A / "grain_light.jpg", 0, 0, W, 420, fit="stretch", opacity=0.5, id="Grain S6")
    s6.text(MARGIN, 52, "LAURA'S PICKS", O, 14, 600, GOLD, letter_spacing=3)
    picks = [("twister_cut.png", "MAGGOOSH", "Twister Maxi Earrings", "$440.00"),
             ("huggie_side_cut.png", "TROUVER", "Half Paved Huggie 9.5mm - Yellow Gold", "$590.00"),
             ("gummy_cut.png", "MAGGOOSH", "Gummy Pendant Necklace - Midnight & Dotted Silver", "$240.00")]
    bw = 170
    bottoms = []
    for i, (img, designer, name, price) in enumerate(picks):
        bx = MARGIN + i * (bw + 15)
        pg = s6.g(f"Pick {name[:20]}")
        pg.image(A / img, bx + 20, 76, bw - 40, 170, fit="contain", id=f"{name[:20]} cut-out")
        pg.text(bx, 272, designer, O, 14, 600, GOLD, letter_spacing=1.5)
        hh = pg.text_block(bx, 292, name, H, 16, bw, 500, INK, line_height=19)
        pg.text(bx, 292 + hh + 2, price, O, 14, 600, INK)
        bottoms.append(292 + hh + 2)
    S6H = max(bottoms) + 44
    e.section_h["06 Lauras Picks"] = S6H; e.y = e.section_y["06 Lauras Picks"] + S6H
    s6.children[0] = f'<rect x="0" y="0" width="{W}" height="{S6H}" fill="{WHITE}"/>'

    # ------------------------------------------------------------------ S7 Close + footer
    s7 = e.section("07 Close", 10, bg=WHITE)
    s7.image(A / "grain_light.jpg", 0, 0, W, 300, fit="stretch", opacity=0.5, id="Grain S7")
    s7.line(MARGIN, 0, W - MARGIN, 0, stroke=SAND, stroke_width=1)
    hh = s7.text_block(MARGIN, 72, "Jewels destined to become your most treasured heirlooms.", H, 26, 540, 400, INK, line_height=34, anchor="middle")
    y7 = 72 + hh + 4
    hh = s7.text_block(MARGIN, y7, "GET 10% OFF* your first order of $250 or more. *Some exclusions may apply.", O, 14, 540, 600, GOLD, line_height=20, anchor="middle")
    y7 += hh + 12
    cta(s7, 170, y7, where="S7")
    fy = y7 + 50 + 40
    ft = s7.g("Footer")
    ft.rect(0, fy, W, 140, fill=SAND)
    ft.image(A / "grain_light.jpg", 0, fy, W, 140, fit="stretch", opacity=0.5, id="Grain footer")
    logo(ft, 300, fy + 28, 16, id="Logo footer")
    ft.text_block(MARGIN, fy + 66, "Broken English · Los Angeles · New York · support@brokenenglishjewelry.com · Instagram · Facebook · Pinterest", O, 12, 540, 400, INK, line_height=16, anchor="middle")
    ft.text_block(MARGIN, fy + 104, "Can't see this email? View it in your browser. / No longer want to receive these emails? Unsubscribe.", O, 12, 540, 400, GREY, line_height=16, anchor="middle")
    S7H = fy + 140
    e.section_h["07 Close"] = S7H; e.y = e.section_y["07 Close"] + S7H
    s7.children[0] = f'<rect x="0" y="0" width="{W}" height="{S7H}" fill="{WHITE}"/>'
    return e


if __name__ == "__main__":
    em = build({})
    print(em.save(HERE / "final" / f"{NAME}.svg"), em.height)
