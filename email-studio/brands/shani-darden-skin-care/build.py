"""Shani Darden Skin Care · spec welcome email 01 · "The home-care card".
Source: brands/shani-darden-skin-care/COPY.md + DESIGN_INTENT.md (10 Oct 2026). Copy verbatim.
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "tools"))
from emailkit import Email, FontRegistry, shapes, MARGIN  # noqa: E402

BRAND = "shani-darden-skin-care"
NAME = "shani-darden-skin-care_welcome-01"
A = HERE / "assets"

fonts = FontRegistry()
fonts.substitute("Didot Display", "Playfair Display", weights=(400, 500), italics=True)
fonts.substitute("Maison Neue", "Inter", weights=(400, 500, 600, 700))
fonts.google("Caveat", weights=(500,))
D, I, HAND = "Playfair Display", "Inter", "Caveat"

BLACK, WHITE, SLATE, VIOLET, TEXT, OFF, RULE, CREAM = "#000000", "#FFFFFF", "#272D45", "#676986", "#4A474A", "#F4F4F6", "#E5E5E5", "#F7F6F2"
W = 600
_vb, *LOGO_PATHS = (A / "logo_paths.txt").read_text().splitlines()
LOGO_W, LOGO_H = 276.667, 46.333


def logo(g, x, y, h, fill=BLACK, id="Logo"):
    w = h * 6.041
    g.image(A / ("logo_black.png" if fill == BLACK else "logo_white.png"), x, y, w, h, fit="contain", id=id)
    return w


def cta(g, x, y, label="SHOP RETINOL REFORM", invert=False, where=""):
    """The one CTA shape: 320 x 52 rectangle, 0 radius, black (white on slate), caps, 2 px tracking."""
    return g.button(x, y, 320, 52, label, I, 14, 600, fill=WHITE if invert else BLACK, text_fill=BLACK if invert else WHITE,
                    rx=0, letter_spacing=2, id=f"CTA {label} {where}".strip())


def torn_card(g, x, y, w, h, fill=WHITE, seed=1):
    """Index-card note with a torn right edge and a slate rule on the left."""
    import random
    rnd = random.Random(seed)
    d = f"M{x} {y} H{x + w - 8}"
    yy = y
    while yy < y + h:
        step = rnd.uniform(6, 14)
        yy = min(y + h, yy + step)
        d += f" L{x + w - 8 + rnd.uniform(-5, 5):.1f} {yy:.1f}"
    d += f" H{x} Z"
    g.path(d, fill=fill, stroke=RULE, stroke_width=1)
    g.rect(x, y, 4, h, fill=SLATE)


def build(state: dict | None = None) -> Email:
    state = state or {}
    e = Email(fonts, name=NAME, bg=WHITE)
    k1, k2 = state.get("M1", 0), state.get("M2", 0)

    # ------------------------------------------------------------------ S1 Hero
    H1 = 620
    s = e.section("01 Hero", H1, bg=OFF)
    s.image(A / "grain_light.jpg", 0, 0, W, H1, fit="stretch", opacity=0.45, id="Grain S1")
    s.text(300, 23, "Free Ground Shipping On Orders Over $50", I, 14, 500, TEXT, anchor="middle", letter_spacing=1)
    s.line(0, 36, W, 36, stroke=RULE, stroke_width=1)
    lw = logo(s, 300 - 110, 60, 36.8, id="Logo black")
    s.text(300, 132, "RETINOL REFORM WITH 1% ENCAPSULATED RETINOL", I, 14, 600, VIOLET, anchor="middle", letter_spacing=2)
    hl = s.g("Headline")
    hl.text(300, 190, "Retinol, without", D, 50, 400, BLACK, anchor="middle")
    hl.text(300, 246, "the irritation.", D, 50, 400, BLACK, anchor="middle")
    s.text_block(MARGIN + 60, 284, "Powered by advanced encapsulation technology, this upgraded formula delivers 1% retinol more effectively, with less irritation.", I, 15, 420, 400, TEXT, line_height=22, anchor="middle", max_lines=4)
    s.line(200, 500, 400, 500, stroke=BLACK, stroke_width=1.5)
    s.image(A / "rr_product_cut.png", 262, 332, 76, 168, fit="contain", id="Retinol Reform bottle")
    s.stars(222, 522, 4.8, size=13, gap=2, fill=BLACK, empty="#C9C9CF", id="Stars hero")
    s.text(300, 558, "RATED 4.8 OUT OF 5 STARS · 118 REVIEWS", I, 14, 600, TEXT, anchor="middle", letter_spacing=1.5)
    cta(s, 140, 572 - 6, where="S1")

    # ------------------------------------------------------------------ S2 A note from Shani
    H2 = 290
    s2 = e.section("02 Note from Shani", H2, bg=WHITE)
    s2.image(A / "grain_light.jpg", 0, 0, W, 400, fit="stretch", opacity=0.3, id="Grain S2")
    s2.image(A / "shani_square_grey.jpg", MARGIN, 40, 200, 200, fit="cover", id="Shani portrait greyscale")
    hh = s2.text_block(254, 72, "“I developed Retinol Reform as a powerful yet gentle alternative to traditional retinoids. This upgraded formula pairs the latest encapsulated retinol technology with a skin-refining tripeptide and natural exfoliator to deliver real results: smoother, brighter, more youthful-looking skin, without the irritation.”",
                      D, 15, 316, 400, BLACK, line_height=22, style="italic")
    s2.text_block(254, 72 + hh + 12, "SHANI DARDEN · EXPERT ESTHETICIAN", I, 14, 316, 600, VIOLET, line_height=18, letter_spacing=1.5)
    H2 = max(H2, 72 + hh + 12 + 68)
    e.section_h["02 Note from Shani"] = H2; e.y = e.section_y["02 Note from Shani"] + H2
    s2.children[0] = f'<rect x="0" y="0" width="{W}" height="{H2}" fill="{WHITE}"/>'

    # ------------------------------------------------------------------ S3 Home-care card (slate)
    s3 = e.section("03 Home-care card", 10, bg=SLATE)
    s3.image(A / "grain_light.jpg", 0, 0, W, 1000, fit="stretch", opacity=0.14, id="Grain S3")
    card = s3.g("Home-care card")
    CX0, CX1, CY = 50, 550, 48
    face_idx = len(card.children)
    card.rect(CX0, CY, CX1 - CX0, 10, fill=CREAM)
    IX, IW = CX0 + 28, CX1 - CX0 - 56
    y = CY + 44
    card.text(IX, y, "HOME CARE · RETINOL REFORM", I, 14, 700, BLACK, letter_spacing=2)
    y += 12
    card.line(IX, y, IX + IW - 70, y, stroke=BLACK, stroke_width=1)
    y += 30
    hh = card.text_block(IX, y, "Start with 1-2 times per week and add a night each week to build tolerance.", D, 18, IW - 90, 400, BLACK, line_height=25, style="italic")
    y += hh + 12
    # M1 grid
    m1 = card.g("M1 Night grid band")
    weeks = [("WEEK 1", "2 nights", [1, 0, 0, 1, 0, 0, 0]), ("WEEK 2", "3 nights", [1, 0, 1, 0, 0, 1, 0]),
             ("WEEK 3", "4 nights", [1, 0, 1, 0, 1, 0, 1]), ("WEEK 4", "5 nights", [1, 1, 0, 1, 1, 0, 1])]
    filled_weeks = {0: 4, 1: 0, 2: 1, 3: 2, 4: 3}[k1]
    gx = IX + 96
    for i, dlab in enumerate("MTWTFSS"):
        m1.text(gx + i * 34 + 11, y, dlab, I, 14, 600, VIOLET, anchor="middle")
    y += 12
    grid_top = y
    for wi, (wk, n, nights) in enumerate(weeks):
        yy = y + 20 + wi * 40
        m1.text(IX, yy + 5, wk, I, 14, 700, BLACK, letter_spacing=1)
        for di, on in enumerate(nights):
            cx = gx + di * 34 + 11
            if on and wi < filled_weeks:
                m1.circle(cx, yy, 11, fill=SLATE)
            else:
                m1.circle(cx, yy, 11, fill="none", stroke=SLATE, stroke_width=1.5, opacity=0.9 if on else 0.45)
        m1.text(IX + IW, yy + 5, n, I, 14, 500, TEXT, anchor="end")
    y += 20 + 4 * 40
    e.module("M1", "Nights fill in", "03 Home-care card", grid_top - 22 + CY - CY, 4 * 40 + 36, states=5, durations_ms=[2200, 500, 500, 500, 1100],
             what_moves="the retinol nights fill in week by week: empty grid, week 1, weeks 1 and 2, weeks 1 to 3, then all four", frame1="all four weeks filled (2, 3, 4, 5 nights)", facts=["Shani's directions line"])
    m1_band_y = e.section_y["03 Home-care card"] + grid_top - 22
    e.modules[-1].y = m1_band_y
    card.text(IX, y, "Example schedule", I, 14, 400, VIOLET, style="italic")
    y += 22
    card.text(IX, y, "Then: Use as often as your skin can tolerate.", I, 15, 500, BLACK)
    y += 34
    card.text(IX, y, "HOW TO APPLY", I, 14, 700, BLACK, letter_spacing=2)
    y += 20
    hh = card.text_block(IX, y, "Apply in the PM after cleanser and toner/essence. Using 2-3 pumps, smooth onto dry face and neck. Gently tap into the under-eye area. Follow with moisturizer.", I, 14, IW, 400, TEXT, line_height=20)
    y += hh + 6
    hh = card.text_block(IX, y, "Caution: Do not use other AHA products on the same night. Do not use if pregnant or nursing.", I, 14, IW, 600, BLACK, line_height=20)
    y += hh + 20
    # margin note
    note = card.g("Margin note Libby K", x=IX, y=y, rotate=-2)
    note.rect(0, 0, IW, 10, fill="#FFF8D6", opacity=0.0)
    nh = note.text_block(14, 24, "“It's powerful enough that you still have to ease into using but works well with sensitive skin.”", HAND, 20, IW - 28, 500, BLACK, line_height=24)
    note.stars(14, 24 + nh + 2, 4, size=11, gap=2, fill=BLACK, empty="#D6D6DC", id="Stars Libby")
    note.text(84, 24 + nh + 12, "Libby K.", HAND, 18, 500, BLACK)
    note.children.insert(0, f'<rect x="0" y="0" width="{IW}" height="{24 + nh + 30}" fill="#FFF8D6"/>')
    note.children.insert(1, f'<rect x="{IW / 2 - 24}" y="-6" width="48" height="12" fill="{VIOLET}" opacity="0.5"/>')
    y += 24 + nh + 30 + 24
    cta(card, IX, y, label="START WITH THE TRAVEL SIZE, $30", where="S3")
    y += 52 + 30
    card_bottom = y
    card.children[face_idx] = f'<rect x="{CX0}" y="{CY}" width="{CX1 - CX0}" height="{card_bottom - CY}" fill="{CREAM}"/>'
    clipb = s3.g("Clipped travel bottle", x=CX1 - 60, y=CY - 14, rotate=10)
    clipb.image(A / "rr_product_cut.png", -14, 0, 28, 120, fit="contain", id="Travel bottle small")
    clipb.path(shapes.paperclip(-8, -12, 44, 16), fill="none", stroke="#8A8A8A", stroke_width=2.2, cap="round", join="round")
    s3.text(CX1 - 60, CY + 150, "TRAVEL SIZE (10 ML)", I, 14, 600, WHITE, anchor="middle", letter_spacing=0.5)
    S3H = card_bottom + 40
    e.section_h["03 Home-care card"] = S3H; e.y = e.section_y["03 Home-care card"] + S3H
    s3.children[0] = f'<rect x="0" y="0" width="{W}" height="{S3H}" fill="{SLATE}"/>'

    # ------------------------------------------------------------------ S4 Study row (white)
    H4 = 330
    s4 = e.section("04 Study row", H4, bg=WHITE)
    s4.image(A / "grain_light.jpg", 0, 0, W, H4, fit="stretch", opacity=0.3, id="Grain S4")
    s4.text(300, 52, "CLINICAL RESULTS", I, 14, 600, VIOLET, anchor="middle", letter_spacing=3)
    m2 = s4.g("M2 Count-up band")
    nums = {0: ["100%", "100%", "100%", "94%"], 1: ["0%", "0%", "0%", "0%"], 2: ["50%", "50%", "50%", "47%"]}[k2]
    caps = ["skin texture & smoothness", "skin tone evenness & brightness", "a renewed youthful look", "skin elasticity"]
    for i, (n, c) in enumerate(zip(nums, caps)):
        cx = 97 + i * 135
        m2.text(cx, 128, n, D, 44, 400, BLACK, anchor="middle")
        m2.text_block(cx - 62, 154, c, I, 14, 124, 500, TEXT, line_height=17, anchor="middle")
    e.module("M2", "Count-up", "04 Study row", 70, 130, states=3, durations_ms=[2400, 300, 300],
             what_moves="the four numbers count 0, half, then the printed values", frame1="100% · 100% · 100% · 94%", facts=["2-week study on 39 subjects, product page"])
    s4.line(MARGIN, 214, W - MARGIN, 214, stroke=BLACK, stroke_width=1)
    s4.text_block(MARGIN, 240, "100% of participants demonstrated an improvement in the appearance of skin texture & smoothness; skin tone evenness & brightness; a renewed youthful look. 94% of participants demonstrated an improvement in skin elasticity. Results were obtained in a 2-week clinical study conducted on 39 subjects ages 25-55.", I, 14, 540, 400, TEXT, line_height=19, anchor="middle")

    # ------------------------------------------------------------------ S5 Clients (off-white)
    s5 = e.section("05 Clients", 10, bg=OFF)
    s5.image(A / "grain_light.jpg", 0, 0, W, 1000, fit="stretch", opacity=0.45, id="Grain S5")
    rail = s5.g("Favorite features rail")
    rail.text_block(MARGIN, 60, "FAVORITE FEATURES · FROM 118 REVIEWS", I, 14, 170, 600, VIOLET, line_height=18, letter_spacing=1)
    feats = [("Easy To Use", 74), ("Gentle", 60), ("Non-Irritating", 46)]
    ry = 118
    for lab, n in feats:
        rail.text(MARGIN, ry, lab, I, 14, 500, BLACK)
        rail.text(MARGIN + 170, ry, str(n), I, 14, 700, BLACK, anchor="end")
        rail.rect(MARGIN, ry + 8, 170, 6, fill="none", stroke=SLATE, stroke_width=1)
        rail.rect(MARGIN, ry + 8, 170 * n / 118, 6, fill=SLATE)
        ry += 44
    rail.text_block(MARGIN, ry, "The review widget's own Favorite Features tallies.", I, 14, 170, 400, VIOLET, line_height=17, style="italic")
    reviews = [
        ("5 STARS", "“I've used many retinols and tretinoin formulas in my life, but this is by far, the best! I have sensitive skin and its so gentle but very effective.”", "Natty", 5),
        ("HOLY GRAIL", "“i'm scared of retinoids but this has completely changed my skin. i cannot live without it.”", "alyssa f. · Verified Buyer", 5),
        ("DO NOT HESITATE!", "“I also have issues with sensitivity and my skin can be very. reactive skin. ... I can tell you this is my absolute FAVORITE retinol product. I have had zero issues using it.”", "Kelly B. · Verified Buyer", 5),
        ("SENSITIVE SKIN THAT DOESN'T REACT TO THIS RETINOL", "“I was worried about trying Shani's retinol, but decided to try. I'm glad I did. My skin does not react negatively with this formula, and it's made my skin feel soft and clear.”", "Kathy M. · Verified Buyer", 5),
    ]
    NX, NW = 236, 334
    ny = 52
    notes = s5.g("Torn notes")
    for i, (title, quote, name, stars) in enumerate(reviews):
        nt = notes.g(f"Note {name.split(' ·')[0]}")
        inner = NW - 44
        tl = len(nt.wrap(title, I, 14, inner, 700, 0.5))
        ql = len(nt.wrap(quote, I, 14, inner, 400))
        nh = 26 + tl * 18 + 6 + ql * 19 + 10 + 20 + 16
        torn_card(nt, NX, ny, NW, nh, seed=i + 3)
        nt.stars(NX + 18, ny + 16, stars, size=11, gap=2, fill=BLACK, empty="#D6D6DC", id=f"Stars {name[:8]}")
        nt.text_block(NX + 18, ny + 44, title, I, 14, inner, 700, BLACK, line_height=18, letter_spacing=0.5)
        qy = ny + 44 + tl * 18 + 6
        nt.text_block(NX + 18, qy, quote, I, 14, inner, 400, TEXT, line_height=19)
        nt.text(NX + 18, qy + ql * 19 + 10, name, I, 14, 500, VIOLET)
        ny += nh + 18
    S5H = max(ny + 30, ry + 60)
    e.section_h["05 Clients"] = S5H; e.y = e.section_y["05 Clients"] + S5H
    s5.children[0] = f'<rect x="0" y="0" width="{W}" height="{S5H}" fill="{OFF}"/>'

    # ------------------------------------------------------------------ S6 Routine (slate)
    H6 = 440
    s6 = e.section("06 Routine", H6, bg=SLATE)
    s6.image(A / "grain_light.jpg", 0, 0, W, H6, fit="stretch", opacity=0.14, id="Grain S6")
    shelf = s6.g("Shelf")
    shelf.line(MARGIN, 300, 232, 300, stroke=WHITE, stroke_width=1.5)
    shelf.image(A / "hpc_cut.png", 118, 110, 64, 190, fit="contain", opacity=0.85, id="Hydration Peptide Cream jar")
    shelf.image(A / "rr_product_cut.png", 66, 90, 56, 210, fit="contain", id="Retinol Reform bottle S6")
    shelf.text(MARGIN, 330, "Hydration Peptide Cream · $60", I, 14, 500, WHITE)
    rx = 262
    s6.text(rx, 58, "COMPLETE YOUR ROUTINE WITH", I, 14, 600, WHITE, letter_spacing=2, opacity=0.85)
    hh = s6.text_block(rx, 92, "Follow with moisturizer. Shani pairs Retinol Reform with Hydration Peptide Cream.", I, 15, 308, 400, WHITE, line_height=22)
    y6 = 92 + hh + 14
    tog = s6.g("Size toggle")
    tog.rect(rx, y6, 308, 40, fill="none", stroke=WHITE, stroke_width=1)
    tog.rect(rx, y6, 154, 40, fill=WHITE)
    tog.text(rx + 77, y6 + 16, "FULL SIZE (30 ML)", I, 14, 600, SLATE, anchor="middle")
    tog.text(rx + 77, y6 + 31, "$75", I, 14, 700, SLATE, anchor="middle")
    tog.text(rx + 231, y6 + 16, "TRAVEL SIZE (10 ML)", I, 14, 500, WHITE, anchor="middle")
    tog.text(rx + 231, y6 + 31, "$30", I, 14, 700, WHITE, anchor="middle")
    y6 += 40 + 22
    perks = s6.g("Perks")
    for i, pk in enumerate(["Free Ground Shipping On Orders Over $50", "Pick 2 Free Samples with any order", "Subscribe & Save 10% + Free Shipping"]):
        yy = y6 + i * 30
        perks.line(rx, yy - 12, rx + 308, yy - 12, stroke=WHITE, stroke_width=1, opacity=0.35)
        perks.path(shapes.check(rx, yy - 4, 14), fill="none", stroke=WHITE, stroke_width=1.8, cap="round", join="round")
        perks.text(rx + 22, yy + 8, pk, I, 14, 500, WHITE)
    y6 += 3 * 30 + 4
    cta(s6, rx, y6, invert=True, where="S6")
    sp = s6.text_block(rx, y6 + 52 + 22, "Subscriptions: minimum 2 orders required before cancellation.", I, 14, 308, 400, WHITE, line_height=19, opacity=0.7)
    H6n = y6 + 52 + 22 + sp + 24
    e.section_h["06 Routine"] = H6n; e.y = e.section_y["06 Routine"] + H6n
    s6.children[0] = f'<rect x="0" y="0" width="{W}" height="{H6n}" fill="{SLATE}"/>'

    # ------------------------------------------------------------------ S7 Close + footer
    s7 = e.section("07 Close", 10, bg=WHITE)
    s7.image(A / "grain_light.jpg", 0, 0, W, 420, fit="stretch", opacity=0.3, id="Grain S7")
    hh = s7.text_block(MARGIN + 30, 70, "Maximizing results, minimizing hype, creating product that she couldn't find, and eliminating downtime, she built her Studio and her reputation as one of the most sought-after estheticians in the world.", D, 16, 480, 400, BLACK, line_height=25, anchor="middle")
    y7 = 70 + hh + 16
    cta(s7, 140, y7, where="S7")
    fy = y7 + 52 + 40
    ft = s7.g("Footer")
    ft.line(MARGIN, fy, W - MARGIN, fy, stroke=RULE, stroke_width=1)
    logo(ft, 300 - 70, fy + 26, 23.5, id="Logo footer")
    ft.text(300, fy + 76, "Shani Darden Skin Care · Facebook · Instagram · TikTok · YouTube · #skinbyshani", I, 12, 500, TEXT, anchor="middle")
    ft.text(300, fy + 98, "© SHANI DARDEN SKIN CARE 2026 · Unsubscribe any time.", I, 12, 400, TEXT, anchor="middle", letter_spacing=0.5)
    S7H = fy + 130
    e.section_h["07 Close"] = S7H; e.y = e.section_y["07 Close"] + S7H
    s7.children[0] = f'<rect x="0" y="0" width="{W}" height="{S7H}" fill="{WHITE}"/>'
    return e


if __name__ == "__main__":
    em = build({})
    print(em.save(HERE / "final" / f"{NAME}.svg"), em.height)
