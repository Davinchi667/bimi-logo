"""evanhealy · spec welcome email 01 · "The oil & water lab sheet".
Source: brands/evanhealy/COPY.md (DRAFT, not final-checked) + DESIGN_INTENT.md (10 Oct 2026). Copy verbatim.
"""
from __future__ import annotations
import math, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "tools"))
from emailkit import Email, FontRegistry, shapes, MARGIN  # noqa: E402

BRAND = "evanhealy"
NAME = "evanhealy_welcome-01"
A = HERE / "assets"

fonts = FontRegistry()
fonts.substitute("Cochin", "Cormorant Garamond", weights=(400, 500, 600), italics=True)
fonts.substitute("proxima-nova", "Montserrat", weights=(400, 500, 600, 700))
fonts.google("IBM Plex Mono", weights=(400, 500))
fonts.google("Caveat", weights=(500,))
C, M, MONO, HAND = "Cormorant Garamond", "Montserrat", "IBM Plex Mono", "Caveat"

SAGE, DEEP, PAPER, BLACK, WHITE, COPPER, INK = "#5B7B5C", "#5A6F4F", "#F5F2ED", "#000000", "#FFFFFF", "#B87333", "#222222"
AMBER = "#E39A2C"
W = 600
LOGO_W, LOGO_H = 1134, 259


def logo(g, x, y, h, id="Logo"):
    w = h * LOGO_W / LOGO_H
    g.image(A / "logo_black.png", x, y, w, h, fit="contain", id=id)
    return w


def cta(g, x, y, label="SHOP THE OIL & WATER START", invert=False, where=""):
    """The one CTA shape: 320 x 52 rectangle, 0 radius, black (cream on the deep green), white caps, 2 px tracking."""
    return g.button(x, y, 320, 52, label, M, 14, 600, fill=PAPER if invert else BLACK, text_fill=BLACK if invert else WHITE,
                    rx=0, letter_spacing=2, id=f"CTA {label} {where}".strip())


def grid(g, x, y, w, h, step=8):
    gg = g.g("Lab grid")
    for gx in range(int(x), int(x + w) + 1, step):
        gg.line(gx, y, gx, y + h, stroke=SAGE, stroke_width=0.5, opacity=0.18)
    for gy in range(int(y), int(y + h) + 1, step):
        gg.line(x, gy, x + w, gy, stroke=SAGE, stroke_width=0.5, opacity=0.18)


def palm(g, cx, cy, size, state):
    """Line-drawn open palm; state 0 = merged golden sheen, 1 empty, 2 mist droplets, 3 mist + amber drop, 4 swirl."""
    s = size / 100
    d = (f"M{cx - 38 * s} {cy + 40 * s} C{cx - 46 * s} {cy} {cx - 36 * s} {cy - 36 * s} {cx - 22 * s} {cy - 34 * s} "
         f"C{cx - 16 * s} {cy - 52 * s} {cx - 2 * s} {cy - 52 * s} {cx + 2 * s} {cy - 34 * s} "
         f"C{cx + 10 * s} {cy - 50 * s} {cx + 24 * s} {cy - 46 * s} {cx + 24 * s} {cy - 28 * s} "
         f"C{cx + 34 * s} {cy - 38 * s} {cx + 46 * s} {cy - 30 * s} {cx + 42 * s} {cy - 12 * s} "
         f"C{cx + 50 * s} {cy - 4 * s} {cx + 46 * s} {cy + 30 * s} {cx + 30 * s} {cy + 44 * s} Z")
    g.path(d, fill=WHITE, stroke=INK, stroke_width=1.5, join="round")
    g.path(f"M{cx - 20 * s} {cy + 10 * s} Q{cx} {cy - 4 * s} {cx + 18 * s} {cy + 6 * s}", fill="none", stroke=INK, stroke_width=1, opacity=0.5)
    if state == 0:
        g.ellipse(cx, cy + 8 * s, 22 * s, 14 * s, fill=AMBER, opacity=0.55)
        g.ellipse(cx - 4 * s, cy + 4 * s, 9 * s, 5 * s, fill=WHITE, opacity=0.7)
    if state in (2, 3):
        for dx, dy in ((-12, 2), (4, -6), (14, 8), (-4, 12), (8, 16)):
            g.circle(cx + dx * s, cy + dy * s, 2.2 * s, fill="#BFD9E6", stroke="#8FB7CA", stroke_width=0.8)
    if state == 3:
        g.path(shapes.drop(cx + 2 * s, cy + 2 * s, 5 * s), fill=AMBER)
    if state == 4:
        g.path(f"M{cx - 14 * s} {cy + 6 * s} q14 -14 24 0 q-10 14 -24 0", fill=AMBER, opacity=0.5)
        g.path(f"M{cx - 8 * s} {cy + 4 * s} q8 -6 14 0", fill="none", stroke="#BFD9E6", stroke_width=2)


def build(state: dict | None = None) -> Email:
    state = state or {}
    e = Email(fonts, name=NAME, bg=PAPER)
    k1, k2, k3 = state.get("M1", 0), state.get("M2", 0), state.get("M3", 0)

    # ------------------------------------------------------------------ S1 Hero (paper)
    H1 = 520
    s = e.section("01 Hero", H1, bg=PAPER)
    s.image(A / "grain_light.jpg", 0, 0, W, H1, fit="stretch", opacity=0.3, id="Grain S1")
    s.text(300, 23, "Free on orders over $75", M, 14, 500, INK, anchor="middle", letter_spacing=1)
    s.line(0, 36, W, 36, stroke=SAGE, stroke_width=1, opacity=0.4)
    logo(s, MARGIN, 60, 30, id="Logo black")
    s.image(A / "hydrosoul_still.jpg", 318, 108, 330, 330, fit="cover", clip_d=f"M318 108 H600 V438 H318 Z", id="HydroSoul with the copper still (coil off the edge)")
    hl = s.g("Headline")
    hl.text(MARGIN, 190, "Start with", C, 56, 500, BLACK)
    hl.text(MARGIN, 246, "oil & water.", C, 56, 500, BLACK)
    s.line(MARGIN, 266, MARGIN + 80, 266, stroke=SAGE, stroke_width=1.5)
    s.text_block(MARGIN, 300, "Our remarkable HydroSouls pressed together with oil serums, moisturize, hydrate, and nurture all skin without stripping the skin's protective barrier.", M, 15, 270, 400, INK, line_height=22, max_lines=7)
    cta(s, MARGIN, 450, where="S1")

    # ------------------------------------------------------------------ S2 Your code (sage)
    H2 = 420
    s2 = e.section("02 Your code", H2, bg=SAGE)
    s2.image(A / "grain_light.jpg", 0, 0, W, H2, fit="stretch", opacity=0.12, id="Grain S2")
    m1 = s2.g("M1 Popup replay band")
    m1.rect(70, 36, 460, 232, fill=WHITE)
    if k1 == 1:
        m1.text(300, 100, "UNLOCK 15% off your first purchase", C, 26, 500, BLACK, anchor="middle")
        m1.rect(110, 140, 380, 40, fill="none", stroke="#BBBBBB", stroke_width=1)
        m1.text(126, 165, "Email", M, 14, 400, "#8A8A8A")
        m1.rect(110, 196, 380, 44, fill="#CCCCCC")
        m1.text(300, 223, "GET MY 15% OFF CODE", M, 14, 600, WHITE, anchor="middle", letter_spacing=2)
    elif k1 == 2:
        m1.text(300, 100, "UNLOCK 15% off your first purchase", C, 26, 500, BLACK, anchor="middle")
        m1.rect(110, 140, 380, 40, fill="none", stroke="#BBBBBB", stroke_width=1)
        m1.text(126, 165, "Email", M, 14, 400, "#8A8A8A")
        m1.rect(110, 196, 380, 44, fill=BLACK)
        m1.text(300, 223, "GET MY 15% OFF CODE", M, 14, 600, WHITE, anchor="middle", letter_spacing=2)
    else:
        m1.text(300, 92, "UNLOCK 15% off your first purchase", C, 22, 500, "#888888", anchor="middle")
        m1.text_block(100, 134, "Use Code SEEKER15 for 15% off your first purchase", C, 26, 400, 500, BLACK, line_height=32, anchor="middle")
        m1.rect(170, 196, 260, 54, fill="none", stroke=SAGE, stroke_width=1.5, dash="6 5")
        m1.text(300, 216, "YOUR CODE", M, 14, 600, SAGE, anchor="middle", letter_spacing=2)
    e.module("M1", "Popup replay", "02 Your code", 36, 232, states=3, durations_ms=[2800, 600, 600],
             what_moves="the brand's popup replays: the UNLOCK view with an email field, the GET MY 15% OFF CODE button pressed, then the code view; the code itself stays live text outside the band", frame1="the code view with the dashed YOUR CODE box", facts=["Klaviyo popup V37uH9 wording"])
    s2.text(300, 240, "SEEKER15", MONO, 22, 500, BLACK, anchor="middle", letter_spacing=3, id="Live code")
    s2.text(300, 300, "Seasonal rituals are not eligible for additional discounts.", M, 14, 400, WHITE, anchor="middle", opacity=0.9)
    cta(s2, 140, 332, where="S2")

    # ------------------------------------------------------------------ S3 Lab sheet (paper with grid)
    s3 = e.section("03 Lab sheet", 10, bg=PAPER)
    grid(s3, 0, 0, W, 980)
    hdr = s3.g("Sheet header")
    hdr.rect(0, 0, W, 44, fill=WHITE, opacity=0.7); hdr.line(0, 44, W, 44, stroke=SAGE, stroke_width=1)
    hdr.text(MARGIN, 28, "PROTOCOL NO. 1 · OIL & WATER", M, 14, 700, BLACK, letter_spacing=3)
    hdr.text(W - MARGIN, 28, "SHEET 01", MONO, 14, 500, SAGE, anchor="end")
    steps = [("Mist", "Mist face with 5-10 sprays of hydrosol."), ("Mix", "Mix 1-3 drops of oil serum & a few more sprays of hydrosol in palm of hand."),
             ("Press", "Gently press infusion onto skin. Mist face with a few more sprays of hydrosol & press in again.")]
    TX = 56
    y = 92
    tube = s3.g("Copper tubing line")
    step_ys = []
    stg = s3.g("Steps")
    for i, (lab, txt) in enumerate(steps):
        step_ys.append(y)
        stg.circle(TX, y, 16, fill=PAPER, stroke=COPPER, stroke_width=2)
        stg.text(TX, y + 5, str(i + 1), MONO, 14, 500, COPPER, anchor="middle")
        stg.text(TX + 32, y + 5, lab.upper(), M, 14, 700, BLACK, letter_spacing=2)
        hh = stg.text_block(TX + 32, y + 28, txt, M, 15, 236, 400, INK, line_height=22)
        y += 28 + hh + 30
    tube.path(f"M{TX} {step_ys[0] + 16} V{step_ys[1] - 16} M{TX} {step_ys[1] + 16} V{step_ys[2] - 16} M{TX} {step_ys[2] + 16} V{y - 10} a10 10 0 0 0 10 10 H{TX + 60}", fill="none", stroke=COPPER, stroke_width=2.5, cap="round")
    # M2 palm (sits beside step 2/3)
    m2 = s3.g("M2 Press band")
    pstate = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}[k2]
    m2.rect(0, 0, W, 10, fill="none")
    pg = m2.g("Palm drawing")
    PX, PY = 460, step_ys[1] + 40
    palm(pg, PX, PY, 110, pstate)
    pg.text(PX, PY + 86, "mist · mix · press", HAND, 20, 500, SAGE, anchor="middle")
    e.module("M2", "Press", "03 Lab sheet", PY - 70, 176, states=5, durations_ms=[1400, 500, 500, 500, 700],
             what_moves="an empty palm, mist droplets land, one amber serum drop lands beside them, they swirl together, then rest as a golden sheen", frame1="oil and mist merged into a soft golden sheen in the palm", facts=["directions verbatim beside it"])
    # bottles with labels (framed photos, leader lines)
    y += 20
    bt = s3.g("Bottle labels")
    bt.image(A / "pomegranate.jpg", MARGIN, y, 120, 120, fit="cover", rx=8, id="Pomegranate Vitality Serum photo")
    bt.image(A / "hydrosoul_still_cut.png", 320, y - 6, 60, 128, fit="contain", id="Rose Geranium HydroSoul bottle")
    bt.line(MARGIN + 120, y + 30, 172, y + 30, stroke=COPPER, stroke_width=1); bt.circle(MARGIN + 120, y + 30, 2.5, fill=COPPER)
    bt.text(172, y + 20, "Pomegranate Vitality Serum", HAND, 20, 500, BLACK)
    h1_ = bt.text_block(172, y + 42, "Pomegranate, sea buckthorn berry, and rosehip seed oils", M, 14, 130, 400, INK, line_height=18)
    bt.text(172, y + 42 + h1_ + 8, "0.5 fl oz $48.99", MONO, 14, 500, BLACK)
    bt.line(380, y + 30, 400, y + 30, stroke=COPPER, stroke_width=1); bt.circle(380, y + 30, 2.5, fill=COPPER)
    bt.text(400, y + 20, "Rose Geranium", HAND, 20, 500, BLACK)
    bt.text(400, y + 40, "HydroSoul", HAND, 20, 500, BLACK)
    h2_ = bt.text_block(400, y + 62, "100% fresh plant hydrosol and nothing else", M, 14, 170, 400, INK, line_height=18)
    bt.text(400, y + 62 + h2_ + 8, "4 fl oz $31.99", MONO, 14, 500, BLACK)
    bt.text(400, y + 62 + h2_ + 28, "1 fl oz $10.99", MONO, 14, 500, BLACK)
    y += max(42 + h1_ + 8, 62 + h2_ + 28, 130) + 30
    s3.line(MARGIN, y, W - MARGIN, y, stroke=SAGE, stroke_width=1)
    y += 26
    s3.text(MARGIN, y, "4 fl oz HydroSoul + serum = $80.98. With SEEKER15: $68.83.", MONO, 14, 500, BLACK)
    y += 20
    s3.text(MARGIN, y, "Our math: 15% off $80.98, before shipping and tax.", MONO, 14, 400, SAGE)
    y += 32
    cta(s3, MARGIN, y, where="S3")
    S3H = y + 52 + 44
    e.section_h["03 Lab sheet"] = S3H; e.y = e.section_y["03 Lab sheet"] + S3H
    s3.children[0] = f'<rect x="0" y="0" width="{W}" height="{S3H}" fill="{PAPER}"/>'

    # ------------------------------------------------------------------ S4 Specimen labels (paper)
    s4 = e.section("04 Notes in the margin", 10, bg=PAPER)
    s4.image(A / "grain_light.jpg", 0, 0, W, 1000, fit="stretch", opacity=0.3, id="Grain S4")
    s4.text_block(MARGIN, 60, "What customers write about pressing it in", C, 30, 540, 500, BLACK, line_height=36)
    reviews = [("DECADENT", "Pomegranate Vitality Serum", "“I feel like I just left the spa after a deep relaxing facial after I press it in with hydrosol. Awesome.”", "Gloria P. · Verified Buyer"),
               ("LOVE THIS SERUM!", "Pomegranate Vitality Serum", "“I ordered the pomegranate vitality serum for my mature skin. It is very hydrating with the HydroSoul. The smell reminds me of being at a spa. Highly recommend!”", "Pam F. · Verified Buyer"),
               ("REFRESHING", "Rose Geranium HydroSoul", "“Light scent, perfect hydration a spritz before applying oils to face creates a perfect glow!”", "Dana H. · Verified Buyer"),
               ("LOVE THIS PRODUCT", "Rose Geranium HydroSoul", "“This is my go to along with the oil serum. There are other products on the market but I always return to these Hydrosoul and serum.”", "Maxine S. · Verified Buyer")]
    stem = s4.g("Rose geranium sprig")
    ty = 110
    tags = s4.g("Specimen labels")
    TW = 262
    for i, (title, prod, quote, name) in enumerate(reviews):
        side = i % 2
        tx = MARGIN if side == 0 else W - MARGIN - TW
        tg = tags.g(f"Label {name.split(' ·')[0]}")
        tl = len(tg.wrap(title, M, 14, TW - 32, 700, 0.5)); ql = len(tg.wrap(quote, M, 14, TW - 32, 400))
        th = 42 + tl * 18 + 18 + ql * 19 + 10 + 18 + 16
        tg.rect(tx, ty, TW, th, fill="#FBF9F5", stroke=SAGE, stroke_width=1)
        tg.circle(tx + TW / 2, ty + 2, 4, fill=COPPER)   # pin head
        tg.line(tx + TW / 2, ty + 2, tx + TW / 2, ty - 10, stroke=COPPER, stroke_width=1.2)
        tg.stars(tx + 16, ty + 22, 5, size=10, gap=2, fill=SAGE, id=f"Stars {name[:6]}")
        tg.text_block(tx + 16, ty + 54, title, M, 14, TW - 32, 700, BLACK, line_height=18, letter_spacing=0.5)
        tg.text(tx + 16, ty + 54 + tl * 18, prod.upper(), M, 14, 500, SAGE)
        qy = ty + 54 + tl * 18 + 18
        tg.text_block(tx + 16, qy, quote, M, 14, TW - 32, 400, INK, line_height=19)
        tg.text(tx + 16, qy + ql * 19 + 12, name, M, 14, 500, INK, opacity=0.8)
        # branch from the stem to the pin
        stem.path(f"M300 {ty + 12} Q{(300 + tx + TW / 2) / 2} {ty - 16} {tx + TW / 2} {ty - 10}", fill="none", stroke=SAGE, stroke_width=1.5)
        for j in range(3):
            lx = 300 + (-1 if side == 0 else 1) * (30 + j * 40); ly = ty - 10 - j * 4
            stem.path(f"M{lx} {ly} q-6 -10 2 -16 q8 6 -2 16", fill=SAGE, opacity=0.6)
        ty += th - 20 + 48
    stem.line(300, 96, 300, ty + 10, stroke=SAGE, stroke_width=2, cap="round")
    s4.children.insert(2, s4.children.pop(s4.children.index(stem)))
    ty += 26
    s4.text_block(MARGIN, ty, "Pomegranate Vitality Serum 4.8 from 153 reviews · Rose Geranium HydroSoul 4.92 from 147 reviews", MONO, 14, 540, 400, SAGE, line_height=19, anchor="middle")
    S4H = ty + 60
    e.section_h["04 Notes in the margin"] = S4H; e.y = e.section_y["04 Notes in the margin"] + S4H
    s4.children[0] = f'<rect x="0" y="0" width="{W}" height="{S4H}" fill="{PAPER}"/>'

    # ------------------------------------------------------------------ S5 Harvest Ritual (deep green)
    s5 = e.section("05 Harvest Ritual", 10, bg=DEEP)
    s5.image(A / "grain_light.jpg", 0, 0, W, 700, fit="stretch", opacity=0.12, id="Grain S5")
    s5.text_block(MARGIN, 52, "HARVEST RITUAL · NOURISH & SOOTHE AUTUMN SKIN", M, 14, 540, 600, PAPER, line_height=18, letter_spacing=2)
    hh = s5.text_block(MARGIN, 96, "Complete daily ritual to nurture, cocoon, cleanse, hydrate, moisturize & soothe autumn skin.", C, 20, 540, 400, PAPER, line_height=26, style="italic")
    y5 = 96 + hh + 16
    s5.image(A / "ritual_cut.png", MARGIN, y5, 250, 188, fit="contain", id="Harvest Ritual five products")
    m3 = s5.g("M3 Price rail band")
    RX = 300
    rail = [("Rose Cleansing Milk", "4 fl oz", "$38.99"), ("Tulsi (Holy Basil) HydroSoul", "4 fl oz", "$31.99"), ("Pomegranate Vitality Serum", "0.5 fl oz", "$48.99"),
            ("Neem Immortelle Purifying Infusion", "1 fl oz", "$38.99"), ("Wild Carrot Immortelle Eye Balm", "0.5 oz", "$28.50")]
    ry = y5 + 6
    for nm, sz, pr in rail:
        lines = m3.wrap(nm, MONO, 14, 200)
        m3.text_block(RX, ry + 12, nm, MONO, 14, 200, 400, PAPER, line_height=16, lines=lines)
        m3.text(W - MARGIN, ry + 12, pr, MONO, 14, 500, PAPER, anchor="end")
        m3.text(RX, ry + 12 + 16 * len(lines), sz, MONO, 14, 400, PAPER, opacity=0.7)
        ry += 16 * len(lines) + 16 + 8
    m3.line(RX, ry + 2, W - MARGIN, ry + 2, stroke=PAPER, stroke_width=1, opacity=0.6)
    ry += 24
    if k3 in (0, 2, 3):
        m3.text(RX, ry, "Separately:", MONO, 14, 400, PAPER)
        m3.text(W - MARGIN, ry, "$187.46", MONO, 15, 500, PAPER, anchor="end")
        if k3 in (0, 3):
            sw = m3.measure("$187.46", MONO, 15, 500)
            m3.line(W - MARGIN - sw - 2, ry - 5, W - MARGIN + 2, ry - 5, stroke=AMBER, stroke_width=2)
    ry += 14
    if k3 in (0, 3):
        m3.text(RX, ry + 40, "Harvest Ritual:", MONO, 14, 500, PAPER)
        m3.text(W - MARGIN, ry + 44, "$135", C, 46, 600, PAPER, anchor="end")
    rail_bottom = ry + 56
    e.module("M3", "Price rail", "05 Harvest Ritual", y5 - 4, rail_bottom - y5 + 8, states=4, durations_ms=[1600, 400, 400, 1100],
             what_moves="five lines only, then the $187.46 total appears, then the strike draws across it and $135 rises in", frame1="five lines, $187.46 struck, $135 large", facts=["five .js prices", "compare-at 18746 and price 13500"])
    y5b = max(rail_bottom, y5 + 188) + 24
    s5.stars(MARGIN, y5b, 4.8, size=12, gap=2, fill=PAPER, empty="#8A9A7F", id="Stars ritual")
    s5.text(MARGIN + 78, y5b + 10, "Rated 4.8 out of 5 stars · Based on 557 reviews", M, 14, 500, PAPER)
    y5b += 36
    hh = s5.text_block(MARGIN, y5b, "Seasonal rituals are not eligible for additional discounts. Individual items cannot be returned or exchanged.", M, 14, 540, 400, PAPER, line_height=19, opacity=0.85)
    y5b += hh + 18
    cta(s5, MARGIN, y5b, label="SHOP THE HARVEST RITUAL", invert=True, where="S5")
    S5H = y5b + 52 + 44
    e.section_h["05 Harvest Ritual"] = S5H; e.y = e.section_y["05 Harvest Ritual"] + S5H
    s5.children[0] = f'<rect x="0" y="0" width="{W}" height="{S5H}" fill="{DEEP}"/>'

    # ------------------------------------------------------------------ S6 ROC + footer (paper)
    s6 = e.section("06 Regenerative", 10, bg=PAPER)
    s6.image(A / "grain_light.jpg", 0, 0, W, 560, fit="stretch", opacity=0.3, id="Grain S6")
    sg = s6.g("ROC seal (drawn type)")
    sg.circle(100, 120, 66, fill="none", stroke=SAGE, stroke_width=1.5)
    sg.circle(100, 120, 58, fill="none", stroke=SAGE, stroke_width=1)
    sg.curved_text(100, 120, 46, "WORLD'S FIRST REGENERATIVE", M, 14, 500, SAGE, start_deg=-90, letter_spacing=0.2, id="Seal rim top")
    sg.curved_text(100, 120, 46, "ORGANIC® BEAUTY BRAND", M, 14, 500, SAGE, start_deg=90, letter_spacing=0.2, id="Seal rim bottom", inside=True)
    sg.text(100, 128, "ROC", C, 28, 600, SAGE, anchor="middle")
    hh = s6.text_block(196, 72, "After more than 25 years working alongside regenerative farmers, women's cooperatives, and plant stewards around the world, evanhealy has been awarded the designation of The World's First Regenerative Organic Certified® (ROC™) Beauty Brand, by the Regenerative Organic Alliance (ROA).", M, 14, 354, 400, INK, line_height=20)
    y6 = max(72 + hh, 216) + 24
    s6.line(MARGIN, y6, W - MARGIN, y6, stroke=SAGE, stroke_width=1, opacity=0.5)
    y6 += 30
    s6.text(MARGIN, y6, "Welcome to The Garden · Skin Salon & Shop | Carlsbad, CA", C, 19, 500, BLACK)
    y6 += 28
    cta(s6, MARGIN, y6, where="S6")
    fy = y6 + 52 + 40
    ft = s6.g("Footer")
    ft.rect(0, fy, W, 130, fill=WHITE)
    logo(ft, MARGIN, fy + 28, 22, id="Logo footer")
    ft.text(MARGIN, fy + 78, "evanhealy · Toll-Free (CAN/US): 1-888-335-0190 · Free Skin Consultation · Store Locator", M, 12, 500, INK)
    ft.text(MARGIN, fy + 100, "Free on orders over $75 · 45-day returns · © Copyright Plant Devas Inc · Unsubscribe", M, 12, 400, INK, opacity=0.8)
    S6H = fy + 130
    e.section_h["06 Regenerative"] = S6H; e.y = e.section_y["06 Regenerative"] + S6H
    s6.children[0] = f'<rect x="0" y="0" width="{W}" height="{S6H}" fill="{PAPER}"/>'
    return e


if __name__ == "__main__":
    em = build({})
    print(em.save(HERE / "final" / f"{NAME}.svg"), em.height)
