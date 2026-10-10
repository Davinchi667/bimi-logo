"""Charles Chocolates · spec welcome email 01 · "The box key".
Source: brands/charles-chocolates/COPY.md + DESIGN_INTENT.md (10 Oct 2026). Copy verbatim.
"""
from __future__ import annotations
import math, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "tools"))
from emailkit import Email, FontRegistry, shapes, MARGIN  # noqa: E402

BRAND = "charles-chocolates"
NAME = "charles-chocolates_welcome-01"
A = HERE / "assets"

fonts = FontRegistry()
fonts.substitute("Georgia", "Lora", weights=(400, 500, 600), italics=True)
fonts.google("Poppins", weights=(400, 500, 600, 700))
S, P = "Lora", "Poppins"

TEAL, BROWN, GOLD, CREAM, INK, BLACK, WHITE = "#108474", "#533528", "#A68660", "#F6EFE6", "#303030", "#000000", "#FFFFFF"
W = 600
LOGO_W, LOGO_H = 378, 98


def logo(g, cx, y, h, cream=False, id="Logo"):
    w = h * LOGO_W / LOGO_H
    g.image(A / ("logo_cream.png" if cream else "logo.png"), cx - w / 2, y, w, h, fit="contain", id=id)


def cta(g, cx, y, label="SHOP THE CLASSIC COLLECTION", invert=False, where=""):
    """The one CTA shape: 340 x 54, 2 px radius, teal (cream on teal grounds), white caps, 1.5 px tracking, 1 px gold inner rule."""
    gg = g.button(cx - 170, y, 340, 54, label, P, 15, 600, fill=CREAM if invert else TEAL, text_fill=BROWN if invert else WHITE,
                  rx=2, letter_spacing=1.5, id=f"CTA {label} {where}".strip())
    gg.rect(cx - 170 + 4, y + 4, 332, 46, fill="none", stroke=GOLD, stroke_width=1, rx=1)
    return gg


def seal(g, cx, cy, r, lines, id):
    sg = g.g(id)
    sg.circle(cx, cy, r, fill="none", stroke=GOLD, stroke_width=1.5)
    sg.circle(cx, cy, r - 6, fill="none", stroke=GOLD, stroke_width=1)
    n = 36
    for i in range(n):
        a = 2 * math.pi * i / n
        sg.circle(cx + (r + 4) * math.cos(a), cy + (r + 4) * math.sin(a), 1.6, fill=GOLD)
    ty = cy - (len(lines) - 1) * 8
    for i, (txt, fam, size, wt) in enumerate(lines):
        sg.text(cx, ty + i * 16 + 5, txt, fam, size, wt, CREAM, anchor="middle", letter_spacing=0.5 if fam == P else 0)
    return sg


def gift_tag(g, x, y, w, h, rot, fill, id):
    tg = g.g(id, x=x, y=y, rotate=rot)
    tg.path(f"M14 0 H{w - 14} L{w} 14 V{h} H0 V14 Z", fill=fill, stroke="#D9CBB8", stroke_width=1, join="round")
    tg.circle(w / 2, 10, 3.5, fill="none", stroke=BROWN, stroke_width=1.2)
    return tg


def build(state: dict | None = None) -> Email:
    state = state or {}
    e = Email(fonts, name=NAME, bg=CREAM)
    k1, k2 = state.get("M1", 0), state.get("M2", 0)

    # ------------------------------------------------------------------ S1 Hero (brown)
    H1 = 660
    s = e.section("01 Hero", H1, bg=BROWN)
    s.image(A / "grain_light.jpg", 0, 0, W, H1, fit="stretch", opacity=0.12, id="Grain S1")
    bar = s.g("Announcement bar")
    bar.rect(0, 0, W, 54, fill=CREAM)
    bar.text_block(MARGIN, 22, "Get a Free Chocolate Bar! Join our newsletter and enjoy a free chocolate bar with your first $50+ purchase.", P, 14, 540, 500, BROWN, line_height=17, anchor="middle")
    logo(s, 300, 76, 52, cream=True, id="Logo cream")
    hl = s.g("Headline")
    hl.text(300, 192, "The chocolates that", S, 46, 400, CREAM, anchor="middle")
    hl.text(300, 242, "started it all.", S, 46, 400, CREAM, anchor="middle")
    s.text_block(MARGIN + 50, 280, "Our signature box of handmade confections. Small-batch, all-natural, made fresh in San Francisco.", P, 15, 440, 400, CREAM, line_height=22, anchor="middle", max_lines=3)
    bx = s.g("Small box angled", x=300, y=322, rotate=-6)
    bx.image(A / "box_small_cut.png", -130, 0, 260, 222, fit="contain", id="Classic Collection 10 piece")
    rib = s.g("Ribbon tag", x=70, y=526, rotate=-6)
    rib.line(236, -24, 214, 2, stroke=CREAM, stroke_width=1)
    rib.path("M0 0 H232 L244 14 L232 28 H0 Z", fill=CREAM, stroke=GOLD, stroke_width=1)
    rib.text(118, 19, "CLASSIC COLLECTION · FROM $31", P, 14, 600, BROWN, anchor="middle")
    cta(s, 300, 580, where="S1")

    # ------------------------------------------------------------------ S2 Box key (teal)
    s2 = e.section("02 Box key", 10, bg=TEAL)
    s2.image(A / "grain_light.jpg", 0, 0, W, 760, fit="stretch", opacity=0.12, id="Grain S2")
    BX, BY, BW = 36, 40, 262
    BH = BW * 1194 / 700
    m1 = s2.g("M1 Box key band")
    m1.image(A / "box_open_cut.png", BX, BY, BW, BH, fit="contain", id="Classic Collection 20 piece open")
    sc = BW / 700
    pieces = [(100, 700), (255, 700), (330, 850), (470, 850), (470, 1000), (600, 1130)]   # six pieces, image coords
    fillings = ["Fleur de sel caramel", "Raspberry", "Passion fruit", "Citrus pairings", "Espresso", "Mint"]
    card = m1.g("Key card")
    KX, KY, KW = 326, 60, 244
    card.rect(KX + 5, KY + 5, KW, 10, fill=BLACK, opacity=0.15)
    card_idx = len(card.children)
    card.rect(KX, KY, KW, 10, fill=CREAM)
    card.text(KX + 20, KY + 36, "WHAT'S INSIDE", P, 14, 700, BROWN, letter_spacing=3)
    card.line(KX + 20, KY + 48, KX + KW - 20, KY + 48, stroke=GOLD, stroke_width=1)
    ky = KY + 78
    lit = k1   # 0 = all lit, 1..6 = that line lit
    rows_y = []
    for i, f in enumerate(fillings):
        on = (lit == 0) or (lit == i + 1)
        col = GOLD if (lit == i + 1) else BROWN
        card.text(KX + 20, ky, f"{i + 1}", S, 18, 600, col, opacity=1 if on else 0.45)
        card.text(KX + 44, ky, f, S, 17, 400 if lit != i + 1 else 600, col, opacity=1 if on else 0.45)
        rows_y.append(ky - 6)
        ky += 30
    ky += 6
    card.line(KX + 20, ky, KX + KW - 20, ky, stroke=GOLD, stroke_width=1)
    hh = card.text_block(KX + 20, ky + 24, "Milk and dark chocolate confections, made with premium cacao and fresh cream. Enjoy these fresh cream truffles within one month of receipt for the best taste.", P, 14, KW - 40, 400, INK, line_height=18)
    ky += 24 + hh + 10
    card.line(KX + 20, ky, KX + KW - 20, ky, stroke=GOLD, stroke_width=1)
    card.text(KX + 20, ky + 26, "10 PIECE $31 · 20 PIECE $58", P, 14, 700, BROWN, letter_spacing=0.5)
    card_h = ky + 26 + 24 - KY
    card.children[card_idx] = f'<rect x="{KX}" y="{KY}" width="{KW}" height="{card_h}" fill="{CREAM}"/>'
    card.children[card_idx - 1] = f'<rect x="{KX + 5}" y="{KY + 5}" width="{KW}" height="{card_h}" fill="{BLACK}" opacity="0.15"/>'
    leaders = m1.g("Leader lines")
    for i, ((px, py), ry) in enumerate(zip(pieces, rows_y)):
        ax, ay = BX + px * sc, BY + py * sc
        hot = (lit == i + 1)
        dim = lit != 0 and not hot
        leaders.line(ax, ay, KX - 8, ry, stroke=GOLD, stroke_width=2.2 if hot else 1.2, opacity=0.4 if dim else 1)
        leaders.circle(ax, ay, 5, fill=GOLD if not dim else "none", stroke=GOLD, stroke_width=1.2, opacity=0.5 if dim else 1)
        leaders.circle(KX - 8, ry, 2.5, fill=GOLD, opacity=0.4 if dim else 1)
    band_h = int(max(BY + BH, KY + card_h) + 10)
    e.module("M1", "Box key", "02 Box key", 0, band_h, states=7, durations_ms=[1600] + [550] * 6,
             what_moves="each numbered card line turns gold in turn with its leader line thickened while the others dim", frame1="all six leaders gold, all six lines at full strength", assets=["open 20 piece box cut-out"], facts=["six fillings from the product description", "sizes and prices from .js"])
    cta(s2, 300, band_h + 24, where="S2")
    S2H = band_h + 24 + 54 + 40
    e.section_h["02 Box key"] = S2H; e.y = e.section_y["02 Box key"] + S2H
    s2.children[0] = f'<rect x="0" y="0" width="{W}" height="{S2H}" fill="{TEAL}"/>'

    # ------------------------------------------------------------------ S3 Free bar meter (cream)
    H3 = 440
    s3 = e.section("03 Free bar meter", H3, bg=CREAM)
    s3.image(A / "grain_light.jpg", 0, 0, W, H3, fit="stretch", opacity=0.35, id="Grain S3")
    s3.text(300, 52, "YOUR FREE CHOCOLATE BAR", P, 14, 700, BROWN, anchor="middle", letter_spacing=3)
    m2 = s3.g("M2 Meter band")
    MX0, MX1, MY = 40, 560, 170
    val = {0: 58, 1: 0, 2: 31, 3: 50}[k2]
    frac = lambda v: (MX1 - MX0) * v / 60
    m2.rect(MX0, MY, MX1 - MX0, 14, fill=BROWN, rx=7)
    if val:
        m2.rect(MX0, MY, frac(val), 14, fill=TEAL, rx=7)
    for v, lab, above in ((0, "$0", False), (31, "10 PIECE $31", False), (58, "20 PIECE $58", False)):
        x = MX0 + frac(v)
        m2.line(x, MY - 6, x, MY + 20, stroke=BROWN, stroke_width=1.5)
        m2.text(x if v else MX0, MY + 40, lab, P, 14, 600, BROWN, anchor="middle" if 0 < v < 58 else ("end" if v == 58 else "start"))
    fx = MX0 + frac(50)
    if val >= 58:
        m2.image(A / "bar_cut.png", fx - 66, MY - 98, 50, 84, fit="contain", transform=f"rotate(-18 {fx - 41} {MY - 56})", id="A wrapped bar slides out")
    flag = m2.g("Flag at 50")
    lit50 = val >= 50
    flag.line(fx, MY - 70, fx, MY + 20, stroke=GOLD, stroke_width=2)
    flag.path(f"M{fx} {MY - 70} H{fx + 96} L{fx + 84} {MY - 56} L{fx + 96} {MY - 42} H{fx} Z", fill=GOLD if lit50 else CREAM, stroke=GOLD, stroke_width=1.5)
    flag.text(fx + 42, MY - 51, "FREE BAR AT $50", P, 14, 700, BROWN if lit50 else GOLD, anchor="middle", letter_spacing=-0.4)
    e.module("M2", "Meter", "03 Free bar meter", 80, 160, states=4, durations_ms=[1600, 400, 400, 400],
             what_moves="the teal fill runs from $0 to the $31 marker to $50 (flag lights) and on to $58, where a wrapped bar slides out from under the flag", frame1="fill at $58, flag gold, bar out", assets=["a wrapped bar cut-out (not named as the free bar)"], facts=["$31 and $58 from .js", "$50 condition from the homepage"])
    s3.text_block(MARGIN, 252, "Join our newsletter and enjoy a free chocolate bar with your first $50+ purchase. Non-cumulative.", P, 15, 540, 500, INK, line_height=22, anchor="middle")
    s3.text_block(MARGIN, 306, "The 20 piece Classic Collection is $58, so it clears $50 on its own.", S, 18, 540, 400, BROWN, line_height=26, anchor="middle", style="italic")
    cta(s3, 300, 352, label="SHOP THE 20 PIECE BOX", where="S3")

    # ------------------------------------------------------------------ S4 Awards + press (brown)
    s4 = e.section("04 Awards and press", 10, bg=BROWN)
    s4.image(A / "grain_light.jpg", 0, 0, W, 520, fit="stretch", opacity=0.12, id="Grain S4")
    seal(s4, 190, 110, 66, [("BEST", P, 14, 700), ("CHOCOLATIER", P, 14, 700), ("IN THE BAY AREA", P, 14, 700), ("San Francisco Magazine", S, 14, 400)], "Seal San Francisco Magazine")
    seal(s4, 410, 110, 66, [("SUNSET", P, 14, 700), ("MAGAZINE'S", P, 14, 700), ("“BEST OF", P, 14, 700), ("THE WEST”", P, 14, 700)], "Seal Sunset Magazine")
    quotes = [("“The one that we found superior in every way was the Charles Chocolates Dubai Done Better Original Pistachio Bar.”", "TASTING TABLE"),
              ("“This is the kind of chocolate that disappears quickly and leaves a lasting impression.”", "PRIME REAL ESTATE"),
              ("“These artisan treats make show-stopping gifts for anyone who loves gourmet chocolate.”", "MSN")]
    cw = (W - 2 * MARGIN - 2 * 20) / 3
    qy = 236
    bottoms = []
    for i, (q, who) in enumerate(quotes):
        x = MARGIN + i * (cw + 20)
        col = s4.g(f"Press {who}")
        hh = col.text_block(x, qy, q, S, 14, cw, 400, CREAM, line_height=19, style="italic")
        col.text(x, qy + hh + 12, who, P, 14, 600, GOLD, letter_spacing=1)
        bottoms.append(qy + hh + 12)
        if i < 2:
            s4.line(x + cw + 10, qy - 14, x + cw + 10, qy + 150, stroke=GOLD, stroke_width=1, opacity=0.6)
    S4H = max(bottoms) + 50
    e.section_h["04 Awards and press"] = S4H; e.y = e.section_y["04 Awards and press"] + S4H
    s4.children[0] = f'<rect x="0" y="0" width="{W}" height="{S4H}" fill="{BROWN}"/>'

    # ------------------------------------------------------------------ S5 Gift tags (cream)
    s5 = e.section("05 Gift tags", 10, bg=CREAM)
    s5.image(A / "grain_light.jpg", 0, 0, W, 900, fit="stretch", opacity=0.35, id="Grain S5")
    s5.text(MARGIN, 64, "Mostly, people give it away.", S, 32, 400, BROWN)
    ribbon = s5.g("Black signature ribbon")
    ribbon.rect(0, 96, W, 14, fill=BLACK)
    tags = [("GREAT GIFT FOR JAPAN", "“We brought boxes of the Classic Collection to family in Tokyo, who don't like the other California chocolate brands. They loved the Charles chocolates and finished them fast.”", "Anonymous", 262, -3, "#E8D9C3"),
            ("SENT BOX TO MY BEST FRIEND FOR HER BIRTHDAY", "“She loved it and sent me a funny picture of her with her tongue sticking out with a piece of candy on it. She's only 73 so I guess it's socially acceptable!”", "Christine Duffy", 250, 2, WHITE),
            ("DELICIOUS", "“I'm more of a dark chocolate person, the darker the better. Charles chocolate has made me re-appreciate milk chocolate.”", "Pomponette", 240, -2, WHITE),
            ("UNFATHOMABLY DELICIOUS", "“I first discovered these way back in the 2000s when Charles' was located in Emeryville. I was walking back to work from lunch and wandered into the shop.”", "Darren Gibbs", 262, 3, "#E8D9C3")]
    tg_all = s5.g("Gift tags")
    xs = [MARGIN, 318, MARGIN + 10, 308]
    ys = [116, 126, 0, 0]
    row_bottom = 0
    for i, (title, quote, name, tw, rot, fill) in enumerate(tags):
        x = xs[i]
        y = ys[i] if i < 2 else row_bottom + 50
        probe = tg_all.g(f"probe {i}")
        tl = len(probe.wrap(title, P, 14, tw - 36, 700, 0.5)); ql = len(probe.wrap(quote, S, 14, tw - 36, 400))
        tg_all.children.pop()
        th = 40 + tl * 18 + 6 + ql * 19 + 10 + 20 + 14
        tg = gift_tag(tg_all, x, y, tw, th, rot, fill, f"Tag {name}")
        tg.line(tw / 2, 10, tw / 2, -(y - 110), stroke=BLACK, stroke_width=1.5)   # string up to the ribbon
        tg.stars(18, 26, 5, size=11, gap=2, fill=BROWN, id=f"Stars {name}")
        tg.text_block(18, 56, title, P, 14, tw - 36, 700, BROWN, line_height=18, letter_spacing=0.5)
        qy = 56 + tl * 18 + 6
        tg.text_block(18, qy, quote, S, 14, tw - 36, 400, INK, line_height=19)
        tg.text(18, qy + ql * 19 + 10, name, P, 14, 500, TEAL)
        if i < 2:
            row_bottom = max(row_bottom, y + th)
        else:
            row_bottom2 = max(locals().get("row_bottom2", 0), y + th)
    S5H = row_bottom2 + 60
    s5.text(300, S5H - 30, "Let customers speak for us · from 617 reviews", P, 14, 500, BROWN, anchor="middle")
    e.section_h["05 Gift tags"] = S5H; e.y = e.section_y["05 Gift tags"] + S5H
    s5.children[0] = f'<rect x="0" y="0" width="{W}" height="{S5H}" fill="{CREAM}"/>'

    # ------------------------------------------------------------------ S6 Split (black / cream)
    H6 = 440
    s6 = e.section("06 Also in the shop", H6, bg=CREAM)
    s6.rect(0, 0, 300, H6, fill=BLACK)
    s6.image(A / "grain_light.jpg", 300, 0, 300, H6, fit="stretch", opacity=0.35, id="Grain S6 right")
    L_ = s6.g("Left Skulls")
    L_.image(A / "skulls_cut.png", 40, 36, 220, 150, fit="contain", id="Filled Skulls Trio")
    L_.text_block(MARGIN, 212, "JOHN KELLY CHOCOLATES, OUR LA SISTER BRAND", P, 14, 240, 600, GOLD, line_height=17, letter_spacing=0.5)
    hh = L_.text_block(MARGIN, 262, "Filled Skulls Trio: Garnet, Dark and Milk Chocolate", S, 17, 240, 500, WHITE, line_height=22)
    y6 = 262 + hh + 4
    hh = L_.text_block(MARGIN, y6, "A wicked gift for yourself or a fun gift for a loved one.", P, 14, 240, 400, WHITE, line_height=18, opacity=0.85)
    y6 += hh + 4
    L_.text(MARGIN, y6, "$55", P, 16, 700, WHITE)
    L_.text(MARGIN, y6 + 30, "SHOP THE SKULLS", P, 14, 700, GOLD, letter_spacing=1.5, decoration="underline")
    R_ = s6.g("Right Almonds")
    R_.image(A / "almonds_cut.png", 340, 30, 220, 160, fit="contain", id="Triple Chocolate Almonds")
    hh = R_.text_block(330, 220, "Triple Chocolate Almonds", S, 17, 240, 500, BROWN, line_height=22)
    y6r = 220 + hh + 4
    hh = R_.text_block(330, y6r, "Our premium California almonds are roasted darker, then coated in our exceptional blend of bittersweet and milk chocolates and dusted with cocoa powder.", P, 14, 240, 400, INK, line_height=18)
    y6r += hh + 4
    R_.text(330, y6r, "$14", P, 16, 700, BROWN)
    R_.text(330, y6r + 30, "SHOP THE ALMONDS", P, 14, 700, TEAL, letter_spacing=1.5, decoration="underline")
    H6n = max(y6, y6r) + 30 + 40
    e.section_h["06 Also in the shop"] = H6n; e.y = e.section_y["06 Also in the shop"] + H6n
    s6.children[0] = f'<rect x="0" y="0" width="{W}" height="{H6n}" fill="{CREAM}"/>'
    s6.children[1] = f'<rect x="0" y="0" width="300" height="{H6n}" fill="{BLACK}"/>'

    # ------------------------------------------------------------------ S7 Close + footer (teal, white footer)
    s7 = e.section("07 Close", 10, bg=TEAL)
    s7.image(A / "grain_light.jpg", 0, 0, W, 320, fit="stretch", opacity=0.12, id="Grain S7")
    hh = s7.text_block(MARGIN + 20, 70, "Handcrafted with all-natural, premium ingredients for an exceptional, award-winning chocolate journey.", S, 22, 500, 400, CREAM, line_height=30, anchor="middle")
    y7 = 70 + hh + 14
    cta(s7, 300, y7, invert=True, where="S7")
    fy = y7 + 54 + 40
    ft = s7.g("Footer")
    ft.rect(0, fy, W, 140, fill=WHITE)
    logo(ft, 300, fy + 22, 40, id="Logo footer")
    ft.text(300, fy + 90, "Charles Chocolates · 2650 18th Street, San Francisco CA 94110", P, 12, 500, BROWN, anchor="middle")
    ft.text(300, fy + 110, "Nut Free Chocolates · Gluten Free Chocolates · Corporate Gifts · Unsubscribe", P, 12, 400, BROWN, anchor="middle")
    S7H = fy + 140
    e.section_h["07 Close"] = S7H; e.y = e.section_y["07 Close"] + S7H
    s7.children[0] = f'<rect x="0" y="0" width="{W}" height="{S7H}" fill="{TEAL}"/>'
    return e


if __name__ == "__main__":
    em = build({})
    print(em.save(HERE / "final" / f"{NAME}.svg"), em.height)
