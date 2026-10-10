"""Pure Inventions · spec welcome email 01 · "The spa water station card".
Source: brands/pure-inventions/COPY.md + DESIGN_INTENT.md (10 Oct 2026). Copy verbatim. Popup P0 is in build_popup.py.
"""
from __future__ import annotations
import math, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "tools"))
from emailkit import Email, FontRegistry, shapes, MARGIN  # noqa: E402

BRAND = "pure-inventions"
NAME = "pure-inventions_welcome-01"
A = HERE / "assets"

fonts = FontRegistry()
fonts.google("Lora", weights=(400, 500, 600), italics=True)
fonts.google("Roboto", weights=(400, 500, 700))
fonts.google("Roboto Mono", weights=(400, 500))
L, R, MONO = "Lora", "Roboto", "Roboto Mono"

BLUE, SOFT, CREAM, GREY, WHITE, BLACK, GREEN = "#467C99", "#90B0C2", "#F9F8F4", "#F2F2F2", "#FFFFFF", "#000000", "#5AA600"
PALE = "#DCE7EE"
INK = "#1F2A33"
W = 600
TINTS = {"Coconut": "#DCEAF2", "Watermelon": "#F7C9D1", "Cranberry + Elderberry": "#D9A7B3", "Mango": "#F8D7B0"}
SWATCH = {"Coconut": "#FFFFFF", "Watermelon": "#F28B9B", "Cranberry + Elderberry": "#8E1B3A", "Mango": "#F4A33C"}


def cta(g, x, y, label="SHOP COCONUT WATER", w=360, where=""):
    """The one CTA shape: 52 px pill, full radius, #467C99, white caps 15 px, 1 px tracking."""
    return g.button(x, y, w, 52, label, R, 15, 700, fill=BLUE, text_fill=WHITE, rx=26, letter_spacing=1, id=f"CTA {label} {where}".strip())


def glass(g, x, y, w, h, level=0.78, tint="#DCEAF2", stroke=BLUE):
    """Tall drinking glass: slight taper, water fill to `level`."""
    taper = w * 0.08
    body = f"M{x} {y} L{x + w} {y} L{x + w - taper} {y + h} Q{x + w / 2} {y + h + 6} {x + taper} {y + h} Z"
    if level > 0:
        wy = y + h * (1 - level)
        tl = taper * (1 - level)
        water = f"M{x + tl} {wy} L{x + w - tl} {wy} L{x + w - taper} {y + h} Q{x + w / 2} {y + h + 6} {x + taper} {y + h} Z"
        g.path(water, fill=tint)
        g.ellipse(x + w / 2, wy, (w - 2 * tl) / 2, 4, fill="none", stroke=stroke, stroke_width=1, opacity=0.5)
    g.path(body, fill="none", stroke=stroke, stroke_width=2, join="round")
    g.ellipse(x + w / 2, y, w / 2, 5, fill="none", stroke=stroke, stroke_width=2)


def dropper(g, cx, y, h=56, stroke=BLUE):
    g.rrect(cx - 7, y, 14, 16, 6, fill=BLACK)           # bulb
    g.rect(cx - 3, y + 16, 6, h - 16, fill="none", stroke=stroke, stroke_width=1.5)   # tube
    g.path(f"M{cx - 3} {y + h} L{cx} {y + h + 6} L{cx + 3} {y + h} Z", fill=stroke)


def build(state: dict | None = None) -> Email:
    state = state or {}
    e = Email(fonts, name=NAME, bg=WHITE)
    k2, k3 = state.get("M2", 0), state.get("M3", 0)

    # ------------------------------------------------------------------ S1 Hero
    H1 = 470
    s = e.section("01 Hero", H1, bg=WHITE)
    s.text(300, 24, "Free Shipping Over $50", R, 14, 500, BLUE, anchor="middle", letter_spacing=1)
    s.line(0, 36, W, 36, stroke=GREY, stroke_width=1)
    s.image(A / "logo_color.png", 236, 46, 128, 60, fit="contain", id="Logo colour")
    wash = e.gradient("wash", [(0, CREAM), (1, SOFT)])
    s.rect(0, 116, W, H1 - 116, fill=wash)
    s.image(A / "grain_light.jpg", 0, 116, W, H1 - 116, fit="stretch", opacity=0.55, id="Grain S1")
    hl = s.g("Headline")
    hl.text(MARGIN, 196, "The water you", L, 46, 500, BLUE)
    hl.text(MARGIN, 248, "tasted at the spa.", L, 46, 500, BLUE)
    s.text_block(MARGIN, 286, "Pure Inventions is proud to be served in thousands of renowned spas and resorts. Now it can be in your water bottle, too.", R, 15, 300, 400, INK, line_height=22, max_lines=5)
    cta(s, MARGIN, 392, w=300, where="S1")
    sc = s.g("Glass and bottle")
    glass(sc, 424, 176, 76, 200, level=0.8)
    sc.line(500, 180, 516, 234, stroke=INK, stroke_width=1)   # tag string
    sc.image(A / "coconut_cut.png", 352, 214, 100, 300, fit="contain", id="Coconut Water bottle (cut by the edge)")
    tag = s.g("Carafe tag")
    tag.circle(518, 302, 70, fill=WHITE, stroke=INK, stroke_width=1)
    tag.circle(518, 236, 3, fill="none", stroke=INK, stroke_width=1)
    tag.curved_text(518, 302, 57, "SERVED IN LUXURY SPAS", R, 14, 500, INK, start_deg=-90, letter_spacing=0.4, id="Tag rim top")
    tag.curved_text(518, 302, 57, "AND WELLNESS CENTERS", R, 14, 500, INK, start_deg=90, letter_spacing=0.4, id="Tag rim bottom", inside=True)
    tag.text(518, 298, "COCONUT", R, 14, 700, BLUE, anchor="middle", letter_spacing=1)
    tag.text(518, 316, "WATER", R, 14, 700, BLUE, anchor="middle", letter_spacing=1)

    # ------------------------------------------------------------------ S2 Spa water card
    s2 = e.section("02 Spa water card", 10, bg=SOFT)
    s2.image(A / "grain_light.jpg", 0, 0, W, 700, fit="stretch", opacity=0.5, id="Grain S2")
    card = s2.g("Tent card")
    CX0, CX1, CY = 60, 540, 64
    card.path(f"M{CX0 + 14} {CY - 26} L{CX1 - 14} {CY - 26} L{CX1} {CY} L{CX0} {CY} Z", fill="#ECE8DD")   # folded top
    face_idx = len(card.children)
    card.rect(CX0 + 8, CY + 8, CX1 - CX0, 10, fill=BLACK, opacity=0.12)  # shadow, resized
    card.rect(CX0, CY, CX1 - CX0, 10, fill=CREAM)                        # face, resized
    y = CY + 46
    card.text(300, y, "TODAY'S WATER", R, 14, 500, INK, anchor="middle", letter_spacing=4)
    y += 14
    card.line(CX0 + 28, y, CX1 - 28, y, stroke=INK, stroke_width=1)
    menu = [("coconut_cut.png", "Coconut Water", "Fresh sweet coconut flavor from coconut juice extract", "30 servings · $24.99"),
            ("watermelon_cut.png", "Electrolytes + Vitamin C Watermelon", "Delicious, refreshing watermelon flavor", "30 servings · $24.99"),
            ("cranberry_cut.png", "Cranberry + Elderberry", "Light, delicious cranberry and elderberry flavor", "60 servings · $35.99"),
            ("mango_cut.png", "Mango Coconut Water", "NEW", "30 servings · $24.99")]
    for img, name, desc, right in menu:
        y += 26
        row = card.g(f"Menu {name}")
        row.image(A / img, CX0 + 28, y - 10, 34, 50, fit="contain", id=f"{name} bottle small")
        nw = row.measure(name, L, 18, 500)
        rw = row.measure(right, R, 14, 700)
        avail = (CX1 - 28) - (CX0 + 74)
        if nw + rw + 24 <= avail:
            row.text(CX0 + 74, y + 8, name, L, 18, 500, INK)
            row.text(CX1 - 28, y + 8, right, R, 14, 700, INK, anchor="end")
            row.line(CX0 + 74 + nw + 8, y + 6, CX1 - 28 - rw - 8, y + 6, stroke=INK, stroke_width=1.5, dash="0 4", cap="round", opacity=0.6)
        else:
            row.text(CX0 + 74, y + 8, name, L, 18, 500, INK)
            row.line(CX0 + 74 + nw + 8, y + 6, CX1 - 28, y + 6, stroke=INK, stroke_width=1.5, dash="0 4", cap="round", opacity=0.6)
            row.text(CX1 - 28, y + 30, right, R, 14, 700, INK, anchor="end")
        if desc == "NEW":
            row.rrect(CX0 + 74, y + 18, 42, 18, 9, fill=GREEN)
            row.text(CX0 + 95, y + 31, "NEW", R, 14, 700, WHITE, anchor="middle", letter_spacing=1)
            y += 40
        else:
            hh = row.text_block(CX0 + 74, y + 30, desc, R, 14, 300, 400, "#5E5854", line_height=18)
            y += 22 + hh
        y += 6
        card.line(CX0 + 28, y, CX1 - 28, y, stroke=INK, stroke_width=1, opacity=0.15)
    y += 30
    hh = card.text_block(CX0 + 28, y, "A few drops in still or sparkling water. Free of sugar, artificial sweeteners, caffeine, and gluten.", L, 15, 236, 400, INK, line_height=21, style="italic")
    foot_y = y + hh
    stamp = card.g("Stamp", x=CX1 - 118, y=y + 62, rotate=-8)
    stamp.circle(0, 0, 90, fill="none", stroke=GREEN, stroke_width=2)
    stamp.circle(0, 0, 83, fill="none", stroke=GREEN, stroke_width=1)
    stamp.curved_text(0, 0, 70, "DEVELOPED BY NUTRITIONISTS", R, 14, 500, GREEN, start_deg=-90, letter_spacing=0.4, id="Stamp rim top")
    stamp.curved_text(0, 0, 70, "PERFECTED SINCE 2003", R, 14, 500, GREEN, start_deg=90, letter_spacing=0.4, id="Stamp rim bottom", inside=True)
    stamp.text(0, 12, "2003", L, 34, 600, GREEN, anchor="middle")
    card_bottom = max(foot_y, y + 62 + 90) + 30
    card.children[face_idx] = f'<rect x="{CX0 + 8}" y="{CY + 8}" width="{CX1 - CX0}" height="{card_bottom - CY}" fill="{BLACK}" opacity="0.12"/>'
    card.children[face_idx + 1] = f'<rect x="{CX0}" y="{CY}" width="{CX1 - CX0}" height="{card_bottom - CY}" fill="{CREAM}"/>'
    cta(s2, 120, card_bottom + 30, label="SHOP ALL FLAVORS", where="S2")
    S2H = card_bottom + 30 + 52 + 40
    e.section_h["02 Spa water card"] = S2H; e.y = e.section_y["02 Spa water card"] + S2H
    s2.children[0] = f'<rect x="0" y="0" width="{W}" height="{S2H}" fill="{SOFT}"/>'

    # ------------------------------------------------------------------ S3 Ounce counter (deep blue)
    H3 = 470
    s3 = e.section("03 Ounce counter", H3, bg=BLUE)
    s3.image(A / "grain_light.jpg", 0, 0, W, H3, fit="stretch", opacity=0.42, id="Grain S3")
    m2 = s3.g("M2 Ounce counter band")
    level = {0: 1.0, 1: 0.125, 2: 0.5, 3: 0.75}[k2]
    num = {0: "96 OZ", 1: "12 OZ", 2: "48 OZ", 3: "72 OZ"}[k2]
    bot = m2.g("Outlined bottle")
    BX, BY, BW, BH = 70, 60, 96, 250
    bot.rrect(BX + 30, BY, 36, 22, 4, fill="none", stroke=WHITE, stroke_width=2)             # cap
    bot.path(f"M{BX + 26} {BY + 22} L{BX + 70} {BY + 22} L{BX + BW} {BY + 58} L{BX + BW} {BY + BH - 16} a16 16 0 0 1 -16 16 L{BX + 16} {BY + BH} a16 16 0 0 1 -16 -16 L{BX} {BY + 58} Z", fill="none", stroke=WHITE, stroke_width=2, join="round")
    fh = (BH - 62) * level
    bot.rrect(BX + 6, BY + BH - 6 - fh, BW - 12, fh, 8, fill="#A9CBE0", opacity=0.9)
    for i in range(1, 8):
        yy = BY + BH - 6 - (BH - 62) * i / 8
        bot.line(BX + BW - 14, yy, BX + BW - 4, yy, stroke=WHITE, stroke_width=1, opacity=0.6)
    cnt = m2.g("Counter")
    if k2 == 0:
        cnt.text(236, 118, "12 OZ", L, 28, 400, WHITE, opacity=0.7)
        cnt.line(236, 109, 236 + cnt.measure("12 OZ", L, 28, 400), 109, stroke=WHITE, stroke_width=2, opacity=0.8)
    cnt.text(232, 214, num, L, 96, 600, WHITE)
    e.module("M2", "Ounce counter", "03 Ounce counter", 50, 280, states=4, durations_ms=[2800, 400, 400, 400],
             what_moves="the outlined bottle fills from an eighth to half to three quarters to full while the number reads 12, 48, 72 then 96 OZ with 12 OZ struck through",
             frame1="bottle full, 96 OZ, 12 OZ struck above", facts=["ALINE N. review line"])
    s3.text_block(236, 256, "“The product has helped me go from drinking 12oz of water a day to 96oz.”", R, 15, 334, 400, WHITE, line_height=22)
    s3.text(236, 330, "ALINE N.", R, 14, 700, WHITE, letter_spacing=1.5)
    s3.line(MARGIN, 356, W - MARGIN, 356, stroke=WHITE, stroke_width=1, opacity=0.4)
    s3.text_block(MARGIN, 384, "Coconut Water: $24.99, makes up to 30 delicious beverages. About 83 cents a glass.", MONO, 14, 540, 500, WHITE, line_height=19)
    s3.text(MARGIN, 440, "Our math: $24.99 divided by 30 servings, before shipping.", MONO, 14, 400, WHITE, opacity=0.75)

    # ------------------------------------------------------------------ S4 Route (cream)
    s4 = e.section("04 Route", 10, bg=CREAM)
    s4.image(A / "grain_light.jpg", 0, 0, W, 1000, fit="stretch", opacity=0.55, id="Grain S4")
    s4.text_block(MARGIN, 66, "Most of them found us the same way.", L, 30, 540, 500, BLUE, line_height=36)
    reviews = [
        ("LOVE THIS STUFF!!", "“I first tasted this water at a high end spa. It was the BEST coconut water I have ever tried! When I came home, I immediately ordered some and now I cannot drink water without it.”", "Amy T.", 330, 0),
        ("FOREVER A FAN!!", "“I discovered it at a spa I went to a while ago with some girlfriends. I literally thought it was the best water I had ever had in my life. I bought a bottle right then and there and have been hooked ever since!”", "Maria L.", 350, 1),
        ("THE BEST", "“I hate drinking water, I said it lol. One day at the spa I go to , my massage therapist gave me a cup of water that was flavored with the coconut drops. I couldn't believe how delicious it was!”", "Marie", 320, 0),
        ("BRING THE SPA HOME, SAVE THE ENVIRONMENT", "“First tasted this at a spa, then brought the spa home with me. I love the sustainability component of adding to my own container vs. buying individually packaged coconut water.”", "Madison S.", 360, 1),
    ]
    route_pts = []
    ty = 110
    tags = s4.g("Review tags")
    pins = []
    for i, (title, quote, name, tw, side) in enumerate(reviews):
        tx = MARGIN if side == 0 else W - MARGIN - tw
        tg = tags.g(f"Tag {name}")
        inner = tw - 36
        # measure height first
        tmp_lines = tg.wrap(quote, R, 14, inner)
        th_lines = len(tmp_lines)
        th = 50 + len(tg.wrap(title, R, 14, inner, 700, 0.5)) * 18 + 6 + th_lines * 19 + 12 + 20 + 14
        tg.rrect(tx + 4, ty + 4, tw, th, 10, fill=BLACK, opacity=0.08)
        tg.rrect(tx, ty, tw, th, 10, fill=WHITE)
        tg.stars(tx + 18, ty + 18, 5, size=12, gap=2, fill=BLUE, id=f"Stars {name}")
        tl = tg.text_block(tx + 18, ty + 50, title, R, 14, inner, 700, INK, line_height=18, letter_spacing=0.5)
        qy = ty + 50 + tl + 6
        hh = tg.text_block(tx + 18, qy, quote, R, 14, inner, 400, "#3F4A52", line_height=19, lines=tmp_lines)
        tg.text(tx + 18, qy + hh + 12, name, R, 14, 500, BLUE)
        pin = (tx + (tw if side == 0 else 0), ty + 24)
        pins.append(pin)
        ty += th + 36
    # the route: a loose dotted path through the pins, drawn under the tags
    pts = [(300, 104)] + pins + [(300, ty + 30)]
    d = f"M{pts[0][0]} {pts[0][1]}"
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        cx = (x0 + x1) / 2 + (40 if y1 > y0 else -40)
        d += f" Q{cx} {(y0 + y1) / 2} {x1} {y1}"
    route = s4.g("Route path")
    route.path(d, fill="none", stroke=BLUE, stroke_width=2, dash="1 7", cap="round")
    s4.children.insert(2, s4.children.pop())   # route under the tags
    drops = s4.g("Route drops")
    for (px, py) in pins:
        drops.path(shapes.drop(px, py, 7), fill=BLUE)
    s4.image(A / "coconut_cut.png", 240, ty + 24, 120, 120, fit="contain", id="Coconut bottle at the route end")
    cta(s4, 120, ty + 170, where="S4")
    S4H = ty + 170 + 52 + 44
    e.section_h["04 Route"] = S4H; e.y = e.section_y["04 Route"] + S4H
    s4.children[0] = f'<rect x="0" y="0" width="{W}" height="{S4H}" fill="{CREAM}"/>'

    # ------------------------------------------------------------------ S5 First drop (white)
    H5 = 520
    s5 = e.section("05 First drop", H5, bg=WHITE)
    s5.image(A / "grain_light.jpg", 0, 0, W, H5, fit="stretch", opacity=0.5, id="Grain S5")
    s5.text_block(MARGIN, 120, "START WITH COCONUT. THE SPA GUESTS DO.", R, 14, 150, 500, BLUE, line_height=20, letter_spacing=1)
    m3 = s5.g("M3 First drop band")
    names = ["Coconut", "Watermelon", "Cranberry + Elderberry", "Mango"]
    sel = names[k3]
    gl = m3.g("Glass")
    glass(gl, 250, 96, 100, 150, level=0.72, tint=TINTS[sel])
    dropper(gl, 300, 30)
    if k3 > 0:
        gl.path(shapes.drop(300, 112, 5), fill=SWATCH[sel] if sel != "Coconut" else BLUE)
    m3.image(A / "coconut_cut.png", 356, 140, 112, 112, fit="contain", id="Coconut bottle beside the glass")
    sw = m3.g("Flavour swatches")
    for i, nm in enumerate(names):
        cx = 120 + i * 120
        if nm == sel:
            sw.circle(cx, 300, 27, fill="none", stroke=BLUE, stroke_width=2)
        sw.circle(cx, 300, 20, fill=SWATCH[nm], stroke="#C8D1D8" if nm == "Coconut" else "none", stroke_width=1)
        sw.text_block(cx - 56, 340, nm, R, 14, 112, 500 if nm == sel else 400, INK, line_height=17, anchor="middle")
    e.module("M3", "First drop", "05 First drop", 20, 360, states=4, durations_ms=[900, 900, 900, 900],
             what_moves="a drop falls and the water tints to each flavour in turn while the matching swatch is ringed", frame1="clear water, Coconut swatch ringed, bottle beside the glass", assets=["Coconut bottle cut-out"], facts=["four flavours on sale"])
    s5.text_block(MARGIN, 404, "Our drops make ordinary water better by transforming plain water into wellness beverages that are delicious and support a healthy lifestyle.", R, 15, 540, 400, INK, line_height=22, anchor="middle")
    cta(s5, 120, 448, where="S5")

    # ------------------------------------------------------------------ S6 Founders + footer
    s6 = e.section("06 Founders", 10, bg=PALE)
    s6.image(A / "grain_light.jpg", 0, 0, W, 460, fit="stretch", opacity=0.5, id="Grain S6")
    y6 = 56
    y6 += s6.text_block(MARGIN, y6, "OUR PROMISE: BE PURE IN OUR INVENTIONS AND IN OUR INTENTIONS.", R, 14, 540, 500, BLUE, line_height=20, letter_spacing=1) + 14
    y6 += s6.text_block(MARGIN, y6, "Pure Inventions was founded in 2003 by us - Lynne and Lori. We're two lifelong friends who both became Certified Clinical Nutritionists and product developers.", R, 15, 500, 400, INK, line_height=22) + 14
    y6 += s6.text_block(MARGIN, y6, "This has been our intention from day one. We promise it will never change.", L, 20, 500, 400, INK, line_height=28, style="italic") + 8
    s6.text(MARGIN, y6, "Lynne and Lori", L, 18, 500, BLUE)
    y6 += 28
    cta(s6, MARGIN, y6, where="S6")
    fy = y6 + 52 + 40
    ft = s6.g("Footer")
    ft.rect(0, fy, W, 150, fill=WHITE)
    ft.image(A / "logo_color.png", MARGIN, fy + 28, 100, 48, fit="contain", id="Logo footer")
    ft.text_block(MARGIN + 116, fy + 40, "Pure Inventions · 64B Grant Place, Little Silver, NJ 07739 · 732-842-5777 · info@pureinventions.com", R, 12, 424, 400, INK, line_height=16)
    ft.text(MARGIN + 116, fy + 82, "Instagram · Facebook · YouTube", R, 12, 500, BLUE)
    ft.text(MARGIN + 116, fy + 102, "Free Shipping Over $50 · Unsubscribe", R, 12, 400, INK, opacity=0.8)
    S6H = fy + 150
    e.section_h["06 Founders"] = S6H; e.y = e.section_y["06 Founders"] + S6H
    s6.children[0] = f'<rect x="0" y="0" width="{W}" height="{S6H}" fill="{PALE}"/>'
    return e


if __name__ == "__main__":
    em = build({})
    print(em.save(HERE / "final" / f"{NAME}.svg"), em.height)
