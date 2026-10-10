"""Big Shoulders Coffee · spec welcome email 01 · "This week's roast sheet".
Source: brands/big-shoulders-coffee/COPY.md + DESIGN_INTENT.md (10 Oct 2026). Copy verbatim.
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "tools"))
from emailkit import Email, FontRegistry, shapes, MARGIN  # noqa: E402

BRAND = "big-shoulders-coffee"
NAME = "big-shoulders-coffee_welcome-01"
A = HERE / "assets"

fonts = FontRegistry()
fonts.google("Poppins", weights=(400, 500, 600, 700, 800), italics=True)
fonts.google("IBM Plex Mono", weights=(400, 500, 600))
P, MONO = "Poppins", "IBM Plex Mono"

BLACK, ORANGE, WHITE = "#000000", "#F68B1E", "#FFFFFF"
CREAM, BROWN, RULE = "#F6E6C8", "#4A1E12", "#C9B497"
W = 600
COL_URL = "https://bigshoulderscoffee.com/products/colombia-popayan-reserve"

TICKER = ["FREE SHIPPING ON ALL ORDERS", "ROASTED FRESH MONDAY - FRIDAY", "CRAFTED IN CHICAGO, SAVORED EVERYWHERE"]


def cta(g, x, y, label="SHOP COLOMBIA", invert=False, w=232, where=""):
    """The one CTA shape: 56 px rectangle, 0 radius, orange / black text; inverted on orange."""
    return g.button(x, y, w, 56, label, P, 16, 700, fill=BLACK if invert else ORANGE,
                    text_fill=WHITE if invert else BLACK, rx=0, letter_spacing=1, id=f"CTA {label} {where}".strip())


def stars_row(g, x, y, n=5, size=12, fill=ORANGE, empty="#3A2A1C", rating=5.0, gap=2):
    g.stars(x, y, rating, size=size, gap=gap, fill=fill, empty=empty)
    return n * (size + gap) - gap


def build(state: dict | None = None) -> Email:
    state = state or {}
    e = Email(fonts, name=NAME, bg=BLACK)
    k1, k2, k3 = state.get("M1", 0), state.get("M2", 0), state.get("M3", 0)

    # ------------------------------------------------------------------ S1 Hero 480
    H1 = 480
    s = e.section("01 Hero", H1, bg=BLACK)
    s.image(A / "burlap_dark.jpg", 0, 36, W, H1 - 36, fit="cover", opacity=0.9, id="Surface burlap S1")
    # M1 ticker band (orange strip, black caps, seamless unit)
    band = s.g("M1 Ticker band", clip=(0, 0, W, 36))
    band.rect(0, 0, W, 36, fill=ORANGE)
    unit_w = 0
    items = []
    for ph in TICKER:
        tw = band.measure(ph, P, 14, 700, 1.5)
        items.append((ph, tw))
        unit_w += tw + 34
    shift = unit_w / 6 * k1
    x = 24 - shift
    while x < W + unit_w:
        for ph, tw in items:
            if -unit_w < x < W + 50:
                band.text(x, 23, ph, P, 14, 700, BLACK, letter_spacing=1.5)
                band.path(shapes.drop(x + tw + 17, 18, 4), fill=BLACK)
            x += tw + 34
    e.module("M1", "Ticker", "01 Hero", 0, 36, states=6, durations_ms=[400] * 6,
             what_moves="strip slides left one sixth of the phrase loop per frame, seamless",
             frame1="phrases flush left, fully readable", assets=[], facts=["three site lines"])
    # logo
    s.image(A / "logo_white_trim.png", MARGIN, 60, 112, 62, fit="contain", id="Logo white")
    # rating line
    stars_row(s, MARGIN, 146, size=14)
    s.text(MARGIN + 80, 158, "4.77 (From 125+ reviews)", P, 14, 500, WHITE)
    # headline (heavy caps, three lines so it clears the bag)
    hl = s.g("Headline")
    hl.text(MARGIN, 216, "NO NONSENSE COFFEE.", P, 40, 800, WHITE)
    hl.text(MARGIN, 262, "ROASTED FRESH", P, 40, 800, WHITE)
    hl.text(MARGIN, 308, "MONDAY - FRIDAY.", P, 40, 800, WHITE)
    s.text_block(MARGIN, 346, "Sustainably sourced coffee, roasted fresh each week and shipped straight to your door.",
                 P, 16, 268, 400, WHITE, line_height=23, opacity=0.8, max_lines=3)
    cta(s, MARGIN, 404, where="S1")

    # ------------------------------------------------------------------ S2 The 20% 280
    H2 = 280
    s = e.section("02 The 20 percent", H2, bg=ORANGE)
    s.text(MARGIN, 196, "20%", P, 132, 800, BLACK, letter_spacing=-4, id="Giant 20")
    col = s.g("Offer column")
    cx = 318
    col.text_block(cx, 92, "SIGN UP FOR SALES & SPECIAL OFFERS", MONO, 14, 252, 600, BLACK, line_height=18, letter_spacing=0.5, lines=["SIGN UP FOR SALES", "& SPECIAL OFFERS"])
    h = col.text_block(cx, 138, "First time subscribers get 20% off their first order.", P, 17, 252, 600, BLACK, line_height=23, max_lines=3)
    col.text(cx, 138 + h + 8, "Free Shipping On All Orders.", P, 15, 400, BLACK)
    cta(col, cx, 210, invert=True, w=232, where="S2")
    # the hero bag, drawn here so it paints over the orange band (bleeds 62 px into S2)
    s.image(A / "bag_cut.png", 330, -160, 270, 236, fit="contain", id="Hero bag (bleeds from S1)")

    # ------------------------------------------------------------------ S3 Roast sheet
    rows_top = 36
    s3 = e.section("03 Roast sheet", 850, bg=BLACK)   # height trimmed below
    sheet = s3.g("Cream sheet")
    SX0, SX1 = 24, 576
    LBL_X, VAL_X, VAL_R = 48, 172, 548
    sheet_h = [0]  # filled after layout; rect drawn first via placeholder we patch at the end
    sheet_rect_idx = len(sheet.children)
    sheet.rect(SX0, rows_top, SX1 - SX0, 10, fill=CREAM)   # placeholder, resized below
    sheet.image(A / "paper_grain.png", SX0, rows_top, SX1 - SX0, 10, fit="stretch", opacity=0.5, id="Paper grain S3")
    grain_idx = len(sheet.children) - 1
    body = sheet.g("Sheet rows")
    y = rows_top + 44
    body.text(LBL_X, y, "THIS WEEK'S ROAST SHEET", MONO, 14, 600, BROWN, letter_spacing=1)
    y += 46
    body.text(LBL_X, y, "Colombia", P, 46, 800, BROWN, letter_spacing=-1, id="Sheet headline")
    y += 26

    def row(label, value, width, lines_font=(P, 15, 400), gap_after=14, rule=True):
        nonlocal y
        y += 14
        body.text(LBL_X, y + 1, label, MONO, 14, 600, BROWN, letter_spacing=0.5)
        fam, sz, wt = lines_font
        hh = body.text_block(VAL_X, y, value, fam, sz, width, wt, BROWN, line_height=21)
        y += hh + gap_after - 21 + 8
        if rule:
            body.line(LBL_X, y, VAL_R, y, stroke=RULE, stroke_width=1)
        return y

    narrow = 386 - VAL_X          # beside the print
    wide = VAL_R - VAL_X
    row("COFFEE", "Colombia · 12oz $26.00 · 5lb $105.00", narrow)
    row("ORIGIN", "The Meseta de Popayán, a high Andean plateau between 1,500 and 2,070 meters above sea level.", narrow)
    row("GROWERS", "Cofinet works with roughly 65 dedicated growers in this region.", narrow)
    row("IN THE CUP", "Caramelized sugar, praline, brown sugar, and soft mandarin citrus in a smooth, balanced cup.", wide)

    # --- M2 band: ROAST sliders + GRIND chips
    band_top = y + 2
    m2 = body.g("M2 Roast and grind band")
    y += 30
    m2.text(LBL_X, y + 1, "ROAST", MONO, 14, 600, BROWN, letter_spacing=0.5)
    LX0, LX1 = 286, 450
    # marker positions as measured on the brand's Colombia tile (34 % and 24 % of the line)
    settled = (0.34, 0.24)
    if k2 == 1:
        pos = (0.0, 0.0)
    elif k2 == 2:
        pos = (0.17, 0.12)
    else:
        pos = settled
    for i, (l, r, p) in enumerate((("LIGHT ROAST", "DARK ROAST", pos[0]), ("TRADITIONAL", "INNOVATIVE", pos[1]))):
        yy = y + i * 30
        m2.text(VAL_X, yy + 1, l, MONO, 14, 500, BROWN)
        m2.text(VAL_R, yy + 1, r, MONO, 14, 500, BROWN, anchor="end")
        m2.line(LX0, yy - 4, LX1, yy - 4, stroke=BROWN, stroke_width=1.5)
        m2.path(shapes.drop(LX0 + (LX1 - LX0) * p, yy - 5, 6.5), fill=BROWN)
    y += 30 + 22
    m2.line(LBL_X, y, VAL_R, y, stroke=RULE, stroke_width=1)
    y += 30
    m2.text(LBL_X, y + 1, "GRIND", MONO, 14, 600, BROWN, letter_spacing=0.5)
    grinds = ["Whole Bean", "Automatic Drip", "French Press", "Espresso", "Chemex", "Pour Over"]
    lit = {0: 0, 1: 0, 2: 0, 3: 0, 4: 3, 5: 1, 6: 5}[k2]
    pw, ph, gap = 118, 30, 8
    for i, gname in enumerate(grinds):
        r_, c_ = divmod(i, 3)
        px, py = VAL_X + c_ * (pw + gap), y - 20 + r_ * (ph + 8)
        on = i == lit
        m2.rrect(px, py, pw, ph, 15, fill=ORANGE if on else "none", stroke=None if on else BROWN, stroke_width=None if on else 1.5)
        m2.text(px + pw / 2, py + 20, gname, P, 14, 600 if on else 500, BLACK if on else BROWN, anchor="middle")
    y += 18 + ph + 8 + 10
    band_h = y - band_top
    e.module("M2", "Roast sheet", "03 Roast sheet", band_top, band_h, states=7, durations_ms=[1500, 300, 300, 600, 600, 600, 600],
             what_moves="both drop markers slide in from the left and settle; the lit grind chip steps Whole Bean, Espresso, Automatic Drip, Pour Over",
             frame1="markers at the tile positions, Whole Bean lit", assets=["Colombia tile slider positions"],
             facts=["six grinds from the .js", "slider positions measured on the tile"])
    body.line(LBL_X, y, VAL_R, y, stroke=RULE, stroke_width=1)

    row("HOW IT BREWS", "As espresso, it's composed and sweet. As drip, it opens up elegant and steady. With milk, it turns into something comforting and luxurious.", wide)
    row("ROASTED BY", "Diego Guartan, head roaster. Crowned the 2025 US Coffee Roasting Champion.", wide - 118, rule=False)
    # Colombia tile bottom right + CTA bottom left
    y += 10
    sheet.image(A / "tile_colombia.png", 438, y - 100, 110, 110, fit="cover", id="Colombia tile")
    cta(sheet, LBL_X, y + 8, where="S3")
    y += 8 + 56 + 36
    sheet_bottom = y
    # resize the cream sheet now that the height is known
    sheet.children[sheet_rect_idx] = f'<rect x="{SX0}" y="{rows_top}" width="{SX1 - SX0}" height="{sheet_bottom - rows_top}" fill="{CREAM}"/>'
    import re as _re
    sheet.children[grain_idx] = _re.sub(r'height="[\d.]+"', f'height="{sheet_bottom - rows_top}"', sheet.children[grain_idx], count=1)
    # binder clip on the top edge
    clip = s3.g("Binder clip")
    clip.path(shapes.binder_clip(300, rows_top - 14, 72, 22), fill="#1A1A1A")
    clip.line(282, rows_top - 14, 268, rows_top - 38, stroke="#8A8A8A", stroke_width=2, cap="round")
    clip.line(318, rows_top - 14, 332, rows_top - 38, stroke="#8A8A8A", stroke_width=2, cap="round")
    clip.rect(268, rows_top - 42, 64, 6, fill="#8A8A8A", rx=3)
    # Diego as a paper-clipped instant print, tilted
    pr = sheet.g("Diego print", x=404, y=52, rotate=-3)
    pr.rect(-6, -6, 164, 264, fill="#000000", opacity=0.12)      # soft shadow
    pr.rect(0, 0, 158, 264, fill="#FDFBF7", stroke="#E4DCCB", stroke_width=1)
    pr.image(A / "diego_crop.jpg", 9, 9, 140, 154, fit="cover", id="Diego photo")
    pr.text_block(9, 185, "You may not know Diego yet, but he is the reason every Big Shoulders bag tastes just right.",
                  P, 14, 142, 400, BROWN, line_height=17, style="italic", max_lines=5)
    pr.path(shapes.paperclip(118, -14, 40, 16), fill="none", stroke="#8A8A8A", stroke_width=2.2, cap="round", join="round")
    # leader from the print to the ROASTED BY label
    S3H = sheet_bottom + 36
    e.section_h["03 Roast sheet"] = S3H
    e.y = e.section_y["03 Roast sheet"] + S3H
    s3.children[0] = f'<rect x="0" y="0" width="{W}" height="{S3H}" fill="{BLACK}"/>'

    # ------------------------------------------------------------------ S4 Reviews
    s4 = e.section("04 Reviews", 10, bg=BLACK)
    s4.image(A / "beans_dark.jpg", 0, 0, W, 700, fit="cover", opacity=0.85, id="Surface beans S4")
    left = s4.g("Counter column")
    left.text(MARGIN, 64, "LET CUSTOMERS SPEAK FOR US", MONO, 14, 600, ORANGE)
    counter = {0: "4.71", 1: "0.00", 2: "2.35", 3: "4.10"}[k3]
    m3 = left.g("M3 Counter band")
    m3.text(MARGIN, 176, counter, P, 96, 800, ORANGE, letter_spacing=-3)
    e.module("M3", "Counter", "04 Reviews", 84, 104, states=4, durations_ms=[2000, 250, 250, 250],
             what_moves="the 4.71 counts up from 0.00 through 2.35 and 4.10", frame1="4.71 (the real average)",
             assets=[], facts=["4.71 from 7 reviews, Judge.me"])
    left.text(MARGIN, 206, "Based on 7 reviews", P, 14, 500, WHITE)
    hist = left.g("Histogram")
    rows_h = [("5", 0.86, "86% (6)"), ("4", 0.0, "0% (0)"), ("3", 0.14, "14% (1)"), ("2", 0.0, "0% (0)"), ("1", 0.0, "0% (0)")]
    for i, (n, frac, lab) in enumerate(rows_h):
        yy = 232 + i * 22
        for j in range(5):
            hist.path(shapes.star(MARGIN + j * 11, yy, 9), fill=ORANGE if j < int(n) else "#2A2A2A")
        hist.rect(MARGIN + 62, yy + 2, 90, 5, fill="#2A2A2A")
        if frac:
            hist.rect(MARGIN + 62, yy + 2, 90 * frac, 5, fill=ORANGE)
        hist.text(MARGIN + 162, yy + 8, lab, MONO, 14, 500, WHITE)
    # right: cream strip with three stapled notes
    strip = s4.g("Review notes strip")
    NX0, NX1 = 262, 570
    strip_rect_idx = len(strip.children)
    strip.rect(NX0, 30, NX1 - NX0, 10, fill=CREAM)
    reviews = [
        ("BEST FLAVOR", [("“I have been buying this coffee for several years. We have it shipped to our home as we do not live in Chicago. It has a wonderful flavor and aroma and", False), ("no bitterness", True), ("”", False)], "LaCretia M."),
        ("BIG SHOULDERS COLUMBIA", [("“I enjoy all of the Big Shoulders coffees that I have tried, but the Columbia is always my go to. It just has a nice balance and flavor.”", False)], "Terry &.T.C."),
        ("BIG SHOULDERS COFFEE COLOMBIA", [("“I liked this coffee, it has a pleasant taste and aroma, there is", False), ("no bitterness,", True), ("for cappuccino and latte it is an ideal option for me.”", False)], "Nataliia A."),
    ]
    ny = 30
    for idx, (title, segs, name) in enumerate(reviews):
        note = strip.g(f"Note {idx + 1} {name}")
        ny += 24
        note.path(shapes.staple(NX0 + 20, ny - 4), fill="none", stroke="#7A7A7A", stroke_width=2)
        note.path(shapes.staple(NX1 - 34, ny - 4), fill="none", stroke="#7A7A7A", stroke_width=2)
        ny += 16
        note.stars(NX0 + 20, ny - 10, 5, size=12, gap=2, fill=ORANGE, empty="#D9C8A6", id=f"Stars note {idx + 1}")
        ny += 22
        note.text(NX0 + 20, ny, title, P, 14, 700, BROWN, letter_spacing=0.5)
        ny += 22
        hh = note.text_runs_block(NX0 + 20, ny, segs, P, 14, 268, BROWN, weight=400, bold_weight=700, line_height=19)
        ny += hh + 4
        note.text(NX0 + 20, ny, name, P, 14, 500, BROWN)
        ny += 18
        if idx < 2:
            note.line(NX0 + 20, ny + 2, NX1 - 20, ny + 2, stroke=BROWN, stroke_width=1, dash="4 5", opacity=0.5)
    ny += 26
    strip.children[strip_rect_idx] = f'<rect x="{NX0}" y="30" width="{NX1 - NX0}" height="{ny - 30}" fill="{CREAM}"/>'
    S4H = max(ny + 30, 372)
    e.section_h["04 Reviews"] = S4H
    e.y = e.section_y["04 Reviews"] + S4H
    s4.children[0] = f'<rect x="0" y="0" width="{W}" height="{S4H}" fill="{BLACK}"/>'

    # ------------------------------------------------------------------ S5 Next bag
    s5 = e.section("05 Next bag", 10, bg=CREAM)
    s5.image(A / "paper_grain.png", 0, 0, W, 420, fit="stretch", opacity=0.45, id="Paper grain S5")
    s5.rect(0, 0, W, 3, fill=BLACK)
    s5.text(MARGIN, 52, "OUR MOST-LOVED COFFEES, READY TO ENJOY.", P, 14, 700, BLACK, letter_spacing=1)
    tiles = [
        ("tile_nightshift.png", "NIGHT SHIFT", "$24.00", "Dark chocolate, peanut butter, caramel, toasted marshmallow finish.", "https://bigshoulderscoffee.com/products/night-shift"),
        ("tile_1848.png", "1848", "$26.00", "A touch of cacao nib, with warm tobacco, vanilla & a pop of pomegranate.", "https://bigshoulderscoffee.com/products/1848"),
        ("tile_ethiopia.png", "ETHIOPIA NATURAL", "$26.00", "Kossa Geshe, Jimma Zone, Oromia.", "https://bigshoulderscoffee.com/products/ethiopia-sidamo-guji"),
    ]
    tw = 170
    bottoms = []
    for i, (img, name, price, notes, url) in enumerate(tiles):
        tg = s5.g(f"Tile {name}")
        tx = MARGIN + i * (tw + 15)
        tg.image(A / img, tx, 74, tw, tw, fit="cover", id=f"{name} tile")
        tg.text(tx, 272, name, P, 14, 700, BLACK, letter_spacing=0.5, decoration="underline")
        tg.text(tx, 292, price, P, 14, 500, BLACK)
        hh = tg.text_block(tx, 316, notes, P, 14, tw, 400, BROWN, line_height=19)
        bottoms.append(316 + hh)
    S5H = max(bottoms) + 30
    e.section_h["05 Next bag"] = S5H
    e.y = e.section_y["05 Next bag"] + S5H
    s5.children[0] = f'<rect x="0" y="0" width="{W}" height="{S5H}" fill="{CREAM}"/>'

    # ------------------------------------------------------------------ S6 Close + footer
    S6H = 500
    s6 = e.section("06 Close", S6H, bg=BLACK)
    s6.image(A / "beans_dark.jpg", 0, 0, W, S6H, fit="cover", opacity=0.8, id="Surface beans S6")
    s6.line(MARGIN, 0, W - MARGIN, 0, stroke="#2A2A2A", stroke_width=1)
    s6.text(MARGIN, 72, "CRAFTED IN CHICAGO,", P, 30, 800, WHITE)
    s6.text(MARGIN, 108, "SAVORED EVERYWHERE.", P, 30, 800, WHITE)
    s6.text_block(MARGIN, 142, "First time subscribers get 20% off their first order. Free Shipping On All Orders.", P, 15, 540, 400, WHITE, line_height=22, opacity=0.8)
    cta(s6, MARGIN, 186, where="S6")
    ft = s6.g("Footer")
    ft.line(MARGIN, 272, W - MARGIN, 272, stroke="#2A2A2A", stroke_width=1)
    ft.text_block(MARGIN, 296, "Big Shoulders Coffee · 2415 W. 19th St Chicago, IL 60608 · 312-846-1439 · information@bigshoulderscoffee.com", P, 12, 540, 400, WHITE, line_height=17, opacity=0.7)
    ft.text(MARGIN, 338, "Facebook · Instagram · YouTube · TikTok", P, 12, 500, WHITE, opacity=0.7)
    ft.text_block(MARGIN, 358, "Can't see this email? View it in your browser. / No longer want to receive these emails? Unsubscribe.", P, 12, 540, 400, WHITE, line_height=17, opacity=0.7)
    big = s6.g("Giant logotype (cropped)", clip=(0, 392, W, S6H - 392))
    big.image(A / "logo_drip_white.png", -8, 400, 1040, 127, fit="contain", id="Logotype giant")
    return e


if __name__ == "__main__":
    em = build({})
    print(em.save(HERE / "final" / f"{NAME}.svg"), em.height)
