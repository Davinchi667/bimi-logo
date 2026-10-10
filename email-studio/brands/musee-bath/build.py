"""Musee Bath · spec welcome email 01 · "The pastry chef's recipe card".
Source: brands/musee-bath/COPY.md + DESIGN_INTENT.md (10 Oct 2026). Copy verbatim.
"""
from __future__ import annotations
import math, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "tools"))
from emailkit import Email, FontRegistry, shapes, MARGIN  # noqa: E402

BRAND = "musee-bath"
NAME = "musee-bath_welcome-01"
A = HERE / "assets"

fonts = FontRegistry()
fonts.substitute("Canela-Thin-Web", "Cormorant Garamond", weights=(300, 400, 500), italics=True)
fonts.google("Poppins", weights=(400, 500, 600, 700))
fonts.google("Caveat", weights=(500, 600))
C, P, HAND = "Cormorant Garamond", "Poppins", "Caveat"

HOT, LIGHT, BLACK, INK, CREAM, WHITE, LAV = "#FF7BA7", "#FFC2D6", "#1A1A1A", "#333333", "#F5F5F5", "#FFFFFF", "#CBB5E3"
W = 600
LOGO_W, LOGO_H = 802, 613   # trimmed raster of the site SVG, measured at build


def logo(g, cx, y, h, id="Logo"):
    w = h * LOGO_W / LOGO_H
    g.image(A / "logo_black.png", cx - w / 2, y, w, h, fit="contain", id=id)


def cta(g, cx, y, label="SHOP DREAMWEAVER", where=""):
    """The one CTA shape: 300 x 52 pill, black, white caps, 1.5 px tracking, centred."""
    return g.button(cx - 150, y, 300, 52, label, P, 14, 600, fill=BLACK, text_fill=WHITE, rx=26, letter_spacing=1.5, id=f"CTA {label} {where}".strip())


def tub(g, x, y, w, h, fizz=0, balm="full"):
    """Drawn bath tub (side view) with water; fizz 0..3 adds rings and bubbles, tints lavender."""
    tint = {0: "#EAF3F8", 1: "#E6E2F2", 2: "#DCD0EE", 3: LAV}[fizz]
    wy = y + h * 0.42
    g.path(f"M{x} {wy} L{x + w} {wy} L{x + w - 14} {y + h} L{x + 14} {y + h} Z", fill=tint)
    g.path(f"M{x - 10} {wy - 10} H{x + w + 10} V{wy + 2} H{x - 10} Z", fill=WHITE, stroke=BLACK, stroke_width=1.5)   # rim
    g.path(f"M{x} {wy + 2} L{x + 14} {y + h} H{x + w - 14} L{x + w} {wy + 2}", fill="none", stroke=BLACK, stroke_width=1.5, join="round")
    g.line(x + 24, y + h, x + 24, y + h + 12, stroke=BLACK, stroke_width=1.5); g.line(x + w - 24, y + h, x + w - 24, y + h + 12, stroke=BLACK, stroke_width=1.5)
    g.path(f"M{x + w - 30} {wy - 10} V{y + 10} a10 10 0 0 1 20 0 V{y + 4}", fill="none", stroke=BLACK, stroke_width=1.5, cap="round")   # tap
    bx, by = x + w / 2, wy + 10
    if balm == "full":
        g.image(A / "balm_circle.png", bx - 30, by - 30, 60, 60, fit="contain", id="Balm in tub")
    elif balm == "half":
        g.image(A / "balm_circle.png", bx - 26, by - 14, 52, 52, fit="contain", clip_d=f"M{bx - 30} {by - 20} H{bx + 30} V{by + 12} H{bx - 30} Z", id="Balm half dissolved")
    for i in range(fizz):
        g.ellipse(bx, by + 14, 22 + i * 12, 6 + i * 3, fill="none", stroke=WHITE, stroke_width=1.5, opacity=0.9)
    import random
    rnd = random.Random(fizz)
    for _ in range(fizz * 5):
        g.circle(bx + rnd.uniform(-44, 44), wy - 4 - rnd.uniform(0, 26 + fizz * 8), rnd.uniform(1.5, 4), fill="none", stroke=BLACK, stroke_width=1, opacity=0.6)


def build(state: dict | None = None) -> Email:
    state = state or {}
    e = Email(fonts, name=NAME, bg=WHITE)
    k1, k2 = state.get("M1", 0), state.get("M2", 0)

    # ------------------------------------------------------------------ S1 Hero (light pink, doily edge)
    H1 = 640
    s = e.section("01 Hero", H1, bg=LIGHT)
    s.image(A / "grain_light.jpg", 0, 0, W, H1, fit="stretch", opacity=0.3, id="Grain S1")
    s.text(300, 24, "Free Shipping at $75!", P, 14, 600, BLACK, anchor="middle", letter_spacing=1)
    s.line(0, 38, W, 38, stroke=BLACK, stroke_width=1, opacity=0.15)
    logo(s, 300, 58, 64, id="Logo black")
    hl = s.g("Headline")
    hl.text(300, 190, "Bath recipes from", C, 50, 400, BLACK, anchor="middle")
    hl.text(300, 240, "a former pastry chef.", C, 50, 400, BLACK, anchor="middle")
    s.text_block(MARGIN + 60, 278, "Musee invites you to slow down and enjoy the sweet things in life like a warm bath.", P, 15, 420, 400, INK, line_height=22, anchor="middle", max_lines=3)
    stand = s.g("Cake stand")
    # balm in a circle sitting on a drawn cake stand
    stand.image(A / "balm_circle.png", 220, 326, 160, 160, fit="contain", id="Dreamweaver balm circle")
    stand.ellipse(300, 490, 120, 10, fill=WHITE, stroke=BLACK, stroke_width=2)
    stand.path("M292 500 V526 M308 500 V526", fill="none", stroke=BLACK, stroke_width=2)
    stand.ellipse(300, 530, 48, 7, fill=WHITE, stroke=BLACK, stroke_width=2)
    tag = s.g("Hanging tag")
    tag.line(410, 492, 436, 528, stroke=BLACK, stroke_width=1)
    tag.circle(448, 548, 30, fill=HOT, stroke=BLACK, stroke_width=1.2)
    tag.circle(448, 522, 2.5, fill="none", stroke=BLACK, stroke_width=1)
    tag.text(448, 545, "DREAMWEAVER", P, 14, 700, BLACK, anchor="middle", letter_spacing=-0.5)
    tag.text(448, 562, "$12", P, 14, 700, BLACK, anchor="middle")
    cta(s, 300, 566, where="S1")
    doily = s.g("Doily edge")
    doily.path(shapes.scallop_edge(0, W, H1 - 12, bump=24, depth=12, down=False), fill=CREAM)
    doily.rect(0, H1 - 12, W, 12, fill=CREAM)

    # ------------------------------------------------------------------ S2 Recipe card (cream)
    s2 = e.section("02 Recipe card", 10, bg=CREAM)
    s2.image(A / "ingredients.jpg", 0, 0, W, 900, fit="cover", opacity=0.14, id="Ingredients photo texture")
    card = s2.g("Recipe card", x=300, y=40, rotate=-2)
    CW, CX0 = 520, -260
    face_idx = len(card.children)
    card.rect(CX0 + 6, 6, CW, 10, fill=BLACK, opacity=0.1)
    card.rect(CX0, 0, CW, 10, fill=WHITE)
    card.rect(CX0, 0, CW, 44, fill=LIGHT)
    card.text(CX0 + 24, 29, "RECIPE NO. 1 · THE DREAMWEAVER BATH", P, 14, 700, BLACK, letter_spacing=1.5)
    LX, LW = CX0 + 24, 300
    y = 78
    card.text(LX, y, "Makes:", P, 14, 700, BLACK); card.text(LX + 62, y, "one warm bath", HAND, 20, 500, INK)
    y += 30
    card.text(LX, y, "Ingredients:", P, 14, 700, BLACK)
    y += 6
    hh = card.text_block(LX, y + 16, "Lavender Oil, Grapeseed Oil, Shea Nut Oil, Vitamin E Oil, French Lavender Essential Oil, Chamomile Essential Oil.", HAND, 20, LW, 500, INK, line_height=24)
    y += 16 + hh + 6
    card.text(LX, y, "Method:", P, 14, 700, BLACK)
    hh = card.text_block(LX, y + 22, "Draw a warm bath. Place balm in water. Soak in Life.", HAND, 22, LW, 600, INK, line_height=26)
    y += 22 + hh + 6
    card.text(LX, y, "Chef's note:", P, 14, 700, BLACK)
    hh = card.text_block(LX, y + 20, "Lull yourself to sleep with the soothing waters of calming chamomile and lavender oil- a wonderful way to end the day.", P, 14, LW, 400, INK, line_height=19, style="normal")
    y += 20 + hh + 10
    # ruled lines behind the text block (drawn first so they sit under)
    rules = []
    for ry in range(96, y, 24):
        rules.append(f'<line x1="{LX}" y1="{ry + 6}" x2="{LX + LW}" y2="{ry + 6}" stroke="#DADADA" stroke-width="1"/>')
    card.children[face_idx + 2:face_idx + 2] = rules
    # M1 tub on the right third
    m1 = card.g("M1 Fizz band")
    TX, TY = CX0 + 350, 90
    st = {0: (3, "half"), 1: (0, "full"), 2: (1, "full"), 3: (2, "half")}[k1]
    tub(m1, TX, TY, 140, 110, fizz=st[0], balm=st[1])
    # margin notes
    mn = card.g("Margin notes")
    my = 230
    mn.stars(TX, my, 5, size=10, gap=2, fill=BLACK, id="Stars Dr W")
    hh = mn.text_block(TX, my + 30, "“Everything one would want in a bath balm, as it smells divine, great quality, and good value too (largest balm I've ever seen).”", HAND, 18, 164, 500, INK, line_height=21)
    mn.text(TX, my + 30 + hh + 2, "Dr. W.", HAND, 18, 600, BLACK)
    my += 30 + hh + 30
    mn.stars(TX, my, 5, size=10, gap=2, fill=BLACK, id="Stars Gypsy831")
    hh = mn.text_block(TX, my + 30, "“Love the smell and the way it made my skin feel super soft!”", HAND, 18, 164, 500, INK, line_height=21)
    mn.text(TX, my + 30 + hh + 2, "Gypsy831", HAND, 18, 600, BLACK)
    y = max(y, my + 30 + hh + 24)
    card.line(LX, y, CX0 + CW - 24, y, stroke=BLACK, stroke_width=1, opacity=0.2)
    y += 18
    hh = card.text_block(LX, y, "Full list: Sodium Bicarbonate, Citric Acid, Lavender Oil, Grapeseed Oil, Shea Nut Oil, Fragrance Oil, Vitamin E Oil, Coloreze, French Lavender Essential Oil, Chamomile Essential Oil.", P, 14, CW - 48, 400, "#6B6B6B", line_height=18)
    y += hh + 20
    CH = y
    card.children[face_idx] = f'<rect x="{CX0 + 6}" y="6" width="{CW}" height="{CH}" fill="{BLACK}" opacity="0.1"/>'
    card.children[face_idx + 1] = f'<rect x="{CX0}" y="0" width="{CW}" height="{CH}" fill="{WHITE}"/>'
    corner = card.g("Low stock corner tag", x=CX0 + CW - 20, y=-6, rotate=8)
    corner.rect(-96, 0, 120, 44, fill=HOT)
    corner.text_block(-88, 18, "is low in stock! Order now before we sell out.", P, 14, 106, 600, BLACK, line_height=15)
    e.module("M1", "Fizz", "02 Recipe card", 40 + 70, 150, states=4, durations_ms=[1500, 600, 600, 900],
             what_moves="clear water with the whole balm, first fizz ring and faint lavender, more fizz and deeper lavender, then the half-dissolved balm in lavender water with a swirl", frame1="balm half dissolved, water lavender, bubbles", assets=["Dreamweaver balm circle crop"], facts=["product photo only"])
    S2H = 40 + CH + 50 + 52 + 40
    cta(s2, 300, 40 + CH + 50, label="SHOP DREAMWEAVER · $12", where="S2")
    e.section_h["02 Recipe card"] = S2H; e.y = e.section_y["02 Recipe card"] + S2H
    s2.children[0] = f'<rect x="0" y="0" width="{W}" height="{S2H}" fill="{CREAM}"/>'

    # ------------------------------------------------------------------ S3 Story (white)
    s3 = e.section("03 Story", 10, bg=WHITE)
    s3.image(A / "grain_light.jpg", 0, 0, W, 420, fit="stretch", opacity=0.25, id="Grain S3")
    s3.text(MARGIN, 52, "THE MUSEE STORY", P, 14, 600, HOT, letter_spacing=3)
    s3.text(MARGIN, 150, "M", C, 110, 400, HOT, id="Drop cap")
    body = "Leisha Pickering, a former pastry chef, founded Musee Bath in 2011 with a vision to care for her community by creating handcrafted products that would provide jobs and spread joy. Drawing from her expertise in working with high-quality ingredients, Leisha crafted a line of whimsical, luxurious bath products."
    lines = s3.wrap(body, P, 15, 440)
    first = lines[:3]; rest_text = " ".join(lines[3:])
    s3.text_block(MARGIN + 100, 96, " ".join(first), P, 15, 440, 400, INK, line_height=22, lines=first)
    hh = s3.text_block(MARGIN, 96 + 3 * 22, rest_text, P, 15, 540, 400, INK, line_height=22)
    y3 = 96 + 3 * 22 + hh + 10
    s3.line(MARGIN, y3, MARGIN + 60, y3, stroke=HOT, stroke_width=2)
    y3 += 34
    hh = s3.text_block(MARGIN, y3, "Musee proudly offers second-chance employment to women in recovery trying to rebuild their lives after incarceration and addiction.", C, 22, 540, 500, BLACK, line_height=28, style="italic")
    S3H = y3 + hh + 40
    e.section_h["03 Story"] = S3H; e.y = e.section_y["03 Story"] + S3H
    s3.children[0] = f'<rect x="0" y="0" width="{W}" height="{S3H}" fill="{WHITE}"/>'

    # ------------------------------------------------------------------ T Ticker (black)
    t = e.section("T Ticker", 40, bg=BLACK)
    band = t.g("M2 Ticker band", clip=(0, 0, W, 40))
    items = ["HANDCRAFTED AT OUR STUDIO IN MISSISSIPPI", "FOUNDED IN 2011", "FREE SHIPPING AT $75"]
    ws = [(ph, band.measure(ph, P, 14, 600, 1.5)) for ph in items]
    unit = sum(tw + 40 for _, tw in ws)
    x = 20 - unit / 6 * k2
    while x < W + unit:
        for ph, tw in ws:
            if -unit < x < W + 60:
                band.text(x, 25, ph, P, 14, 600, HOT, letter_spacing=1.5)
                band.circle(x + tw + 20, 20, 3, fill=HOT)
            x += tw + 40
    e.module("M2", "Ticker", "T Ticker", 0, 40, states=6, durations_ms=[250] * 6, what_moves="the three lines slide left one sixth of the loop per frame, seamless", frame1="HANDCRAFTED AT OUR STUDIO IN MISSISSIPPI · FOUNDED IN 2011 readable from the left", facts=["Dreamweaver page line", "homepage 2011", "shipping bar"])

    # ------------------------------------------------------------------ S4 Pastry case (hot pink)
    s4 = e.section("04 Pastry case", 10, bg=HOT)
    s4.image(A / "grain_light.jpg", 0, 0, W, 800, fit="stretch", opacity=0.18, id="Grain S4")
    case = s4.g("Glass case")
    CX, CY, CWd = 40, 110, 520
    case.rect(CX, CY, CWd, 10, fill="none", stroke=WHITE, stroke_width=2)   # frame, resized below
    frame_idx = len(case.children) - 1
    case.path(f"M{CX} {CY} Q{CX + CWd / 2} {CY - 70} {CX + CWd} {CY}", fill="none", stroke=WHITE, stroke_width=2)   # curved glass top
    sign = s4.g("Chalk sign", x=W - MARGIN - 70, y=30, rotate=6)
    sign.rect(-56, 0, 112, 36, fill=BLACK)
    sign.text(0, 23, "IN STOCK TODAY", HAND, 20, 600, WHITE, anchor="middle")
    s4.text(MARGIN, 52, "FRESH FROM THE STUDIO", P, 14, 700, BLACK, letter_spacing=2)
    items = [("steamers.jpg", "Sweet Orange & Sunflower Shower Steamers", "Relax in a refreshing shower, as sweet orange essential oil fills the air and invigorates your senses.", "$28"),
             ("eucalyptus.png", "Eucalyptus & Mint Mini Bath Salt Soak", "Pacific sea salt and Epsom salt, with eucalyptus and mint.", "$10"),
             ("foreveryoung.jpg", "Forever Young Therapy Bath Soak", "Experience the renewal of a jasmine and rosehip bath as rose clay brings a youthful glow to tired skin.", "$24"),
             ("ghost.png", "Ghost Boxed Bath Balm", "A little ghost, a lot of glow. Marshmallow & Whipped Cream, Surprise Inside.", "$12")]
    y4 = CY + 20
    shelf_h = []
    for row in range(2):
        rb = y4
        for col in range(2):
            img, name, desc, price = items[row * 2 + col]
            px = CX + 20 + col * 250
            it = case.g(f"Shelf item {name[:18]}")
            it.image(A / img, px, y4, 230, 120, fit="cover", rx=10, id=f"{name[:18]} photo")
            tent = it.g(f"Price tent {price}")
            tent.path(f"M{px + 10} {y4 + 102} L{px + 20} {y4 + 86} H{px + 112} L{px + 122} {y4 + 102} Z", fill=WHITE, stroke="#E6E6E6", stroke_width=1)
            tent.text(px + 66, y4 + 99, price, P, 14, 700, BLACK, anchor="middle")
            hh = it.text_block(px, y4 + 142, name, P, 14, 230, 700, BLACK, line_height=18)
            hh2 = it.text_block(px, y4 + 142 + hh + 2, desc, P, 14, 230, 400, BLACK, line_height=18)
            rb = max(rb, y4 + 142 + hh + 2 + hh2)
        y4 = rb + 16
        case.line(CX, y4, CX + CWd, y4, stroke=WHITE, stroke_width=2)
        shelf_h.append(y4)
        y4 += 24
    case_bottom = shelf_h[-1]
    case.children[frame_idx] = f'<rect x="{CX}" y="{CY}" width="{CWd}" height="{case_bottom - CY}" fill="none" stroke="{WHITE}" stroke-width="2"/>'
    cta(s4, 300, case_bottom + 36, label="SHOP THE BATH", where="S4")
    S4H = case_bottom + 36 + 52 + 40
    e.section_h["04 Pastry case"] = S4H; e.y = e.section_y["04 Pastry case"] + S4H
    s4.children[0] = f'<rect x="0" y="0" width="{W}" height="{S4H}" fill="{HOT}"/>'

    # ------------------------------------------------------------------ S5 Order spike (cream)
    s5 = e.section("05 Order spike", 10, bg=CREAM)
    s5.image(A / "grain_light.jpg", 0, 0, W, 1000, fit="stretch", opacity=0.3, id="Grain S5")
    s5.text(300, 60, "What customers ordered more of", C, 32, 400, BLACK, anchor="middle")
    tickets = [("No. 01", "SMELLS LIKE YOU ARE IN AN ORANGE GROVE", "“Every scent this company makes is wonderful! There isn't one I don't love!”", "Pattyt, Seattle, Washington", -3, 0),
               ("No. 02", "THE TEACHERS LOVED THEM!", "“I bought these as teacher gifts! They absolutely loved them!! They smelled amazing!”", "Drea E., Madison, MS", 2, 1),
               ("No. 03", "PLS MAKE MORE IN THIS SCENT", "“i would do anything if they would make more products in this scent please im begging”", "Nora", -2, 0),
               ("No. 04", "MY FAVORITE BATH SOAK!", "“My favorite way to unwind after a long day! I love the scent! This bath soak left my skin so soft and smooth.”", "Jessica, Hattiesburg, MS", 3, 1)]
    spike = s5.g("Spike")
    ty = 96
    tk = s5.g("Tickets")
    TW = 300
    for i, (num, title, quote, name, rot, side) in enumerate(tickets):
        tx = (MARGIN + 10) if side == 0 else (W - MARGIN - 10 - TW)
        g = tk.g(f"Ticket {num}", x=tx, y=ty, rotate=rot)
        tl = len(g.wrap(title, P, 14, TW - 36, 700, 0.5)); ql = len(g.wrap(quote, HAND, 19, TW - 36, 500))
        th = 44 + tl * 18 + 6 + ql * 22 + 10 + 22 + 14
        g.rect(4, 4, TW, th, fill=BLACK, opacity=0.08)
        g.rect(0, 0, TW, th, fill=WHITE, stroke="#E2E2E2", stroke_width=1)
        g.path(shapes.zigzag(0, TW, th, step=10, amp=3), stroke="#E2E2E2", stroke_width=1)
        g.text(TW - 14, 20, num, P, 14, 500, "#8A8A8A", anchor="end")
        g.stars(18, 12, 5, size=10, gap=2, fill=BLACK, id=f"Stars {num}")
        g.text_block(18, 44, title, P, 14, TW - 36, 700, BLACK, line_height=18, letter_spacing=0.5)
        qy = 44 + tl * 18 + 6
        g.text_block(18, qy, quote, HAND, 19, TW - 36, 500, INK, line_height=22)
        g.text(18, qy + ql * 22 + 10, name, P, 14, 500, HOT)
        # hole where the spike pierces it
        g.circle(TW / 2, 10, 3, fill=CREAM, stroke="#BBBBBB", stroke_width=1)
        ty += th - 26 + 36
    spike.line(300, 84, 300, ty + 10, stroke=BLACK, stroke_width=2.5)
    spike.ellipse(300, ty + 14, 44, 8, fill=BLACK)
    s5.children.insert(2, s5.children.pop(s5.children.index(spike)))   # spike behind tickets
    S5H = ty + 60
    e.section_h["05 Order spike"] = S5H; e.y = e.section_y["05 Order spike"] + S5H
    s5.children[0] = f'<rect x="0" y="0" width="{W}" height="{S5H}" fill="{CREAM}"/>'

    # ------------------------------------------------------------------ S6 Close + footer
    s6 = e.section("06 Close", 10, bg=LIGHT)
    s6.image(A / "grain_light.jpg", 0, 0, W, 460, fit="stretch", opacity=0.3, id="Grain S6")
    hh = s6.text_block(MARGIN, 72, "Wellness products that create joyful moments for the happiest you.", C, 28, 540, 400, BLACK, line_height=34, anchor="middle")
    y6 = 72 + hh + 10
    meter = s6.g("Free shipping meter")
    meter.line(120, y6 + 10, 480, y6 + 10, stroke=BLACK, stroke_width=1.5)
    meter.path(shapes.drop(480, y6 + 2, 6), fill=HOT)
    meter.text(480, y6 + 34, "$75", P, 14, 700, BLACK, anchor="middle")
    meter.text(300, y6 + 34, "Free Shipping at $75!", P, 14, 500, BLACK, anchor="middle")
    y6 += 56
    cta(s6, 300, y6, where="S6")
    fy = y6 + 52 + 40
    ft = s6.g("Footer")
    ft.rect(0, fy, W, 150, fill=WHITE)
    logo(ft, 300, fy + 22, 44, id="Logo footer")
    ft.text(300, fy + 92, "Musee Bath · Handcrafted at our studio in Mississippi", P, 12, 500, INK, anchor="middle")
    ft.text(300, fy + 110, "Store Locator · Corporate Gifting · Returns + Exchanges · Follow us", P, 12, 400, INK, anchor="middle")
    ft.text(300, fy + 130, "Copyright © 2026 Musee Bath · Unsubscribe", P, 12, 400, INK, anchor="middle", opacity=0.8)
    S6H = fy + 150
    e.section_h["06 Close"] = S6H; e.y = e.section_y["06 Close"] + S6H
    s6.children[0] = f'<rect x="0" y="0" width="{W}" height="{S6H}" fill="{LIGHT}"/>'
    return e


if __name__ == "__main__":
    em = build({})
    print(em.save(HERE / "final" / f"{NAME}.svg"), em.height)
