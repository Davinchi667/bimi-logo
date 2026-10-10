"""Copper Cow Coffee · spec welcome email 01 · "The 90-second brew clock".
Source: brands/copper-cow-coffee/COPY.md + DESIGN_INTENT.md (10 Oct 2026). Copy verbatim.
"""
from __future__ import annotations
import math, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "tools"))
from emailkit import Email, FontRegistry, shapes, MARGIN  # noqa: E402

BRAND = "copper-cow-coffee"
NAME = "copper-cow-coffee_welcome-01"
A = HERE / "assets"

fonts = FontRegistry()
fonts.google("Poppins", weights=(400, 500, 600, 700, 800))
fonts.substitute("NaNJaune", "Fredoka", weights=(600, 700))   # the packs' chunky rounded face
P, F = "Poppins", "Fredoka"

GREEN, DEEP, CREAM, PINK, LIME, WHITE = "#004E42", "#13322B", "#F9F7E8", "#F2A7C3", "#C8E86B", "#FFFFFF"
PINK_DK = "#D97A9B"
W = 600
URL = "https://coppercowcoffee.com/products/classic-black-vietnamese-pour-over-coffee"
MARQUEE = ["CLIMATE RESILIENT", "ZERO FAKE", "REAL FLAVOR", "AAPI WOMAN OWNED", "VIETNAMESE COFFEE", "SUSTAINABLY SOURCED"]


def cta(g, x, y, invert=False, w=250, where=""):
    """The one CTA shape: 54 px pill, green fill, cream caps; inverted on the green band."""
    return g.button(x, y, w, 54, "SHOP CLASSIC BLACK", P, 15, 700, fill=CREAM if invert else GREEN,
                    text_fill=GREEN if invert else CREAM, rx=27, letter_spacing=1, id=f"CTA SHOP CLASSIC BLACK {where}".strip())


def blob(g, cx, cy, rx, ry, rot=0, fill=PINK, speckle=0, seed=1, id=None):
    """Cow-spot blob: a wobbly ellipse path plus optional darker speckle dots inside."""
    pts = []
    n = 9
    import random
    rnd = random.Random(seed)
    for i in range(n):
        a = 2 * math.pi * i / n
        r = 1 + rnd.uniform(-0.18, 0.18)
        pts.append((cx + rx * r * math.cos(a), cy + ry * r * math.sin(a)))
    d = f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"
    for i in range(n):
        p0, p1 = pts[i], pts[(i + 1) % n]
        pm = ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2)
        d += f" Q{p0[0]:.1f} {p0[1]:.1f} {pm[0]:.1f} {pm[1]:.1f}"
    d += " Z"
    gg = g.g(id or f"Blob {cx:.0f} {cy:.0f}", rotate=0)
    gg.path(d, fill=fill, transform=f"rotate({rot} {cx} {cy})" if rot else None)
    for _ in range(speckle):
        a = rnd.uniform(0, 2 * math.pi); r = rnd.uniform(0, 0.8)
        gg.circle(cx + rx * r * math.cos(a), cy + ry * r * math.sin(a), rnd.uniform(0.8, 1.8), fill=PINK_DK, opacity=0.8)
    return gg


def filter_tag(g, x, y, w, h, fill=CREAM, stroke=GREEN):
    """Pour-over filter outline: body with a hanger tab on top."""
    tab_w, tab_h = 56, 16
    d = (f"M{x + 10} {y + tab_h} H{x + w / 2 - tab_w / 2} V{y + 2} a4 4 0 0 1 4 -2 H{x + w / 2 + tab_w / 2 - 4} a4 4 0 0 1 4 2 V{y + tab_h} H{x + w - 10} "
         f"a10 10 0 0 1 10 10 V{y + h - 12} a12 12 0 0 1 -12 12 H{x + 12} a12 12 0 0 1 -12 -12 V{y + tab_h + 10} a10 10 0 0 1 10 -10 Z")
    g.path(d, fill=fill, stroke=stroke, stroke_width=2, join="round")
    g.rect(x + w / 2 - 14, y + 5, 28, 6, fill=stroke, rx=3)


def mug_icon(g, x, y, w, h, fill_level=0.0, stroke=GREEN):
    g.rrect(x, y, w, h, 6, fill=WHITE, stroke=stroke, stroke_width=2)
    if fill_level > 0:
        fh = (h - 8) * fill_level
        g.rrect(x + 4, y + h - 4 - fh, w - 8, fh, 3, fill=PINK)
    g.path(f"M{x + w} {y + h * 0.3} h8 a8 8 0 0 1 0 {h * 0.4:.0f} h-8", fill="none", stroke=stroke, stroke_width=2, join="round")


def build(state: dict | None = None) -> Email:
    state = state or {}
    e = Email(fonts, name=NAME, bg=CREAM)
    k1, k2, k3 = state.get("M1", 0), state.get("M2", 0), state.get("M3", 0)

    # ------------------------------------------------------------------ S1 Hero 520
    H1 = 520
    s = e.section("01 Hero", H1, bg=CREAM)
    s.image(A / "paper_grain.png", 0, 0, W, H1, fit="stretch", opacity=0.35, id="Paper grain S1")
    spots = s.g("Cow spots", clip=(0, 0, W, H1))
    blob(spots, 585, 95, 120, 70, rot=-20, speckle=70, seed=2, id="Spot top right")
    blob(spots, 560, 330, 95, 130, rot=15, speckle=60, seed=5, id="Spot right")
    blob(spots, 120, 505, 110, 46, rot=-8, speckle=30, seed=9, id="Spot bottom left")
    s.image(A / "logo_green_dark.png", MARGIN, 34, 56, 62, fit="contain", id="Logo green")
    s.text(MARGIN, 134, "BOLD. SMOOTH. SERIOUSLY GOOD.", P, 14, 700, GREEN, letter_spacing=1.5)
    hl = s.g("Headline")
    hl.text(MARGIN, 186, "Vietnamese Coffee,", F, 44, 700, GREEN)
    hl.text(MARGIN, 236, "Ready in 90 Seconds.", F, 44, 700, GREEN)
    s.text_block(MARGIN, 272, "Brewed from premium Vietnamese robusta beans. Each single-serve filter is pre-filled to deliver a fresh, barista-quality cup…anytime, anywhere.",
                 P, 15, 290, 400, DEEP, line_height=22, max_lines=5)
    s.stars(MARGIN, 388, 5, size=13, gap=2, fill=GREEN, id="Stars hero")
    s.text(MARGIN + 80, 399, "Rated 5.0 out of 5 stars · 29 Reviews", P, 14, 500, DEEP)
    cta(s, MARGIN, 418, where="S1")
    # M1 marquee strip at the foot
    band = s.g("M1 Marquee band", clip=(0, H1 - 40, W, 40))
    band.rect(0, H1 - 40, W, 40, fill=GREEN)
    items = [(ph, band.measure(ph, P, 14, 700, 1.5)) for ph in MARQUEE]
    unit = sum(tw + 44 for _, tw in items)
    x = 20 - unit / 6 * k1
    while x < W + unit:
        for ph, tw in items:
            if -unit < x < W + 60:
                band.text(x, H1 - 15, ph, P, 14, 700, CREAM, letter_spacing=1.5)
                band.path(shapes.arrow_right(x + tw + 12, H1 - 29, 18), stroke=LIME, stroke_width=2.2, cap="round", join="round")
            x += tw + 44
    e.module("M1", "Marquee", "01 Hero", H1 - 40, 40, states=6, durations_ms=[400] * 6,
             what_moves="the brand's own value marquee slides left one sixth of its loop per frame, seamless",
             frame1="CLIMATE RESILIENT leads, readable from the left edge", facts=["six homepage marquee phrases"])
    # product cut-out, drawn in S2 so it paints over the band and the S2 wave

    # ------------------------------------------------------------------ S2 The 15 percent
    H2 = 310
    s2 = e.section("02 The 15 percent", H2, bg=GREEN)
    wave = s2.g("Lime wave edge")
    wave.path(f"M0 0 H{W} V22 C500 44 420 8 300 24 C180 40 100 6 0 26 Z", fill=LIME)
    s2.image(A / "hero_cut.png", 364, -226, 236, 225, fit="contain", id="Classic Black box pouch mug (bleeds from S1)")
    tk = s2.g("Coupon ticket")
    TX, TY, TW, TH = 70, 64, 460, 150
    tk.rrect(TX, TY, TW, TH, 10, fill=CREAM)
    for cy in (TY + 20, TY + TH / 2, TY + TH - 20):      # scalloped short edges
        tk.circle(TX, cy, 9, fill=GREEN); tk.circle(TX + TW, cy, 9, fill=GREEN)
    tk.line(TX + 150, TY + 16, TX + 150, TY + TH - 16, stroke=GREEN, stroke_width=1.5, dash="4 5")
    tk.text(TX + 75, TY + 84, "15%", F, 58, 700, GREEN, anchor="middle", letter_spacing=-1)
    tk.text(TX + 75, TY + 116, "off", F, 26, 600, GREEN, anchor="middle")
    tk.text_block(TX + 172, TY + 44, "Sign up for 15% off and exclusive deals.", P, 17, 270, 700, GREEN, line_height=23, max_lines=2)
    tk.text_block(TX + 172, TY + 100, "Free shipping is available after your discounted subtotal reaches at least $30.", P, 14, 270, 400, DEEP, line_height=19, max_lines=3)
    cta(s2, 175, 232, invert=True, where="S2")

    # ------------------------------------------------------------------ S3 Brew clock
    s3 = e.section("03 Brew clock", 10, bg=CREAM)
    s3.image(A / "paper_grain.png", 0, 0, W, 900, fit="stretch", opacity=0.35, id="Paper grain S3")
    s3.text(300, 56, "HOW TO BREW", P, 14, 700, GREEN, anchor="middle", letter_spacing=2)
    s3.text(300, 100, "Tear. Hang. Pour. Enjoy!", P, 34, 800, GREEN, anchor="middle")
    CX, CY, R = 300, 336, 148
    m2 = s3.g("M2 Brew clock band")
    secs = {0: 90, 1: 0, 2: 10, 3: 30, 4: 60}[k2]
    lit_upto = {0: 4, 1: 1, 2: 2, 3: 3, 4: 3}[k2]        # how many step photos are lit
    dial = m2.g("Dial")
    dial.circle(CX, CY, R + 14, fill=WHITE, opacity=0.6)
    dial.circle(CX, CY, R, fill="none", stroke=GREEN, stroke_width=3)
    for t in range(0, 100, 5):   # 100-second face, 0 at the top
        a = math.radians(t * 3.6 - 90)
        inner = R - (14 if t % 10 == 0 else 7)
        dial.line(CX + inner * math.cos(a), CY + inner * math.sin(a), CX + (R - 2) * math.cos(a), CY + (R - 2) * math.sin(a), stroke=GREEN, stroke_width=2 if t % 10 == 0 else 1)
    # crown + button like a stopwatch
    dial.rect(CX - 10, CY - R - 30, 20, 18, fill=GREEN, rx=3)
    dial.rect(CX - 16, CY - R - 36, 32, 8, fill=GREEN, rx=4)
    steps = [("tear", 0, "Tear"), ("hang", 10, "Hang"), ("pour", 30, "Pour"), ("enjoy", 90, "Enjoy!")]
    for i, (key, t, label) in enumerate(steps):
        a = math.radians(t * 3.6 - 90)
        px, py = CX + R * math.cos(a), CY + R * math.sin(a)
        on = i < lit_upto
        pg = dial.g(f"Step {label}")
        pg.circle(px, py, 43, fill=LIME if on else "#E6E2CF")
        pg.image(A / f"step_{key}.jpg", px - 37, py - 37, 74, 74, fit="cover", clip_d=shapes.circle(px, py, 37), opacity=1 if on else 0.4, id=f"{label} photo")
        lx = px + (58 if math.cos(a) > 0.2 else -58 if math.cos(a) < -0.2 else 0)
        ly = py + (-54 if math.sin(a) < -0.2 else 60 if math.sin(a) > 0.2 else 6)
        pg.text(lx, ly, label, F, 18, 700, GREEN if on else "#9A9A8A", anchor="middle" if abs(math.cos(a)) <= 0.2 else ("start" if math.cos(a) > 0 else "end"))
        pg.text(lx, ly + 16, f"{t} s", P, 14, 500, GREEN if on else "#9A9A8A", anchor="middle" if abs(math.cos(a)) <= 0.2 else ("start" if math.cos(a) > 0 else "end"))
    # hand
    a = math.radians(secs * 3.6 - 90)
    dial.line(CX, CY, CX + (R - 50) * math.cos(a), CY + (R - 50) * math.sin(a), stroke=GREEN, stroke_width=4, cap="round")
    dial.circle(CX, CY, 7, fill=GREEN)
    centre = {0: "90 SECONDS", 1: "0:00", 2: "0:10", 3: "0:30", 4: "1:00"}[k2]
    dial.text(CX, CY + 62, centre, F, 22 if k2 == 0 else 26, 700, GREEN, anchor="middle")
    if k2 == 0:
        dial.text(CX, CY + 82, "READY IN", P, 14, 700, GREEN, anchor="middle", letter_spacing=2)
    if k2 == 3:
        tag = dial.g("Wait tag")
        tag.rrect(CX - 50, CY + 72, 100, 24, 12, fill=PINK)
        tag.text(CX, CY + 89, "wait 30 sec", P, 14, 600, DEEP, anchor="middle")
    # callouts with leader lines (static, inside the band area)
    co = s3.g("Callouts")
    co.text_block(MARGIN, 300, "A higher boost in caffeine (compared to arabica beans)", P, 14, 112, 500, DEEP, line_height=18)
    co.line(MARGIN + 112, 312, CX - R - 6, 330, stroke=GREEN, stroke_width=1.5)
    co.circle(CX - R - 6, 330, 3, fill=GREEN)
    co.text_block(458, 300, "Lower acidity (compared to arabica beans)", P, 14, 112, 500, DEEP, line_height=18)
    co.line(458, 312, CX + R + 6, 330, stroke=GREEN, stroke_width=1.5)
    co.circle(CX + R + 6, 330, 3, fill=GREEN)
    # strength rail
    rail = m2.g("Strength rail")
    RY = 548
    rail.line(150, RY, 450, RY, stroke=GREEN, stroke_width=2)
    for i in range(10):
        rail.line(150 + i * 33.3, RY - 4, 150 + i * 33.3, RY + 4, stroke=GREEN, stroke_width=1.5)
    mug_icon(rail, 96, RY - 30, 34, 36, fill_level=(0.85 if k2 == 4 else 0.35))
    rail.rrect(466, RY - 44, 26, 50, 4, fill=WHITE, stroke=GREEN, stroke_width=2)
    rail.rrect(470, RY - 44 + 50 - 4 - 42 * (0.85 if k2 == 4 else 0.35), 18, 42 * (0.85 if k2 == 4 else 0.35), 2, fill=PINK)
    marker_x = 150 + 300 * (0.72 if k2 == 4 else 0.3)
    rail.path(shapes.drop(marker_x, RY - 10, 7), fill=PINK_DK)
    rail.text(130, RY + 30, "3 oz VIETNAMESE STYLE", P, 14, 700, GREEN, anchor="middle")
    rail.text(470, RY + 30, "12 oz AMERICANO", P, 14, 700, GREEN, anchor="middle")
    e.module("M2", "Brew clock", "03 Brew clock", 136, 450, states=5, durations_ms=[2600, 500, 500, 700, 700],
             what_moves="the hand sweeps 0, 10, 30, 60 then rests at 90; each step photo lights as the hand passes; a wait-30-sec tag at 30; the pink fill rises in the rail mug at 60",
             frame1="hand at 90, all four photos lit, centre reads 90 SECONDS", assets=["four HowTo photo crops"],
             facts=["brew steps verbatim", "Ready in 90 seconds", "two bracketed site lines"])
    # steps list
    st = s3.g("Steps")
    sy = 620
    for line in ["Step 1 · Hook filter over your mug.", "Step 2 · Pour 1 oz hot water, wait 30 sec.",
                 "Step 3 · Add 3–12 oz more hot water depending on desired strength (3 oz for Vietnamese style, up to 12 oz for an Americano).",
                 "Step 4 · Enjoy black or with creamer."]:
        num, rest = line.split(" · ", 1)
        st.text(MARGIN, sy, num.upper(), P, 14, 700, GREEN, letter_spacing=1)
        hh = st.text_block(MARGIN + 74, sy, rest, P, 15, 466, 400, DEEP, line_height=21)
        sy += hh + 8
    cta(s3, 175, sy + 12, where="S3")
    S3H = sy + 12 + 54 + 44
    e.section_h["03 Brew clock"] = S3H; e.y = e.section_y["03 Brew clock"] + S3H
    s3.children[0] = f'<rect x="0" y="0" width="{W}" height="{S3H}" fill="{CREAM}"/>'

    # ------------------------------------------------------------------ S4 Brewers
    s4 = e.section("04 Brewers", 10, bg=PINK)
    s4.image(A / "speckle.png", 0, 0, W, 700, fit="stretch", opacity=0.9, id="Speckle")
    slab = s4.g("Green slab")
    slab.rrect(MARGIN, 36, W - 2 * MARGIN, 160, 18, fill=GREEN)
    slab.text(MARGIN + 24, 68, "FEEDBACK FROM OUR BREWERS", P, 14, 700, LIME, letter_spacing=1.5)
    m3 = slab.g("M3 Counter band")
    n, pct = {0: ("29", "100%"), 1: ("0", "0%"), 2: ("9", "40%"), 3: ("21", "80%")}[k3]
    m3.text(MARGIN + 24, 132, n, F, 60, 700, CREAM)
    nw = m3.measure("29", F, 60, 700)
    m3.text(MARGIN + 24 + nw + 12, 132, "REVIEWS", P, 14, 700, CREAM, letter_spacing=1.5)
    m3.text(330, 132, pct, F, 60, 700, LIME)
    pw = m3.measure("100%", F, 60, 700)
    m3.text(330 + pw + 10, 118, "would", P, 14, 600, CREAM)
    m3.text(330 + pw + 10, 134, "recommend", P, 14, 600, CREAM)
    e.module("M3", "Counter", "04 Brewers", 84, 60, states=4, durations_ms=[2000, 250, 250, 250],
             what_moves="29 counts 0, 9, 21, 29 while 100% counts 0, 40, 80, 100", frame1="29 REVIEWS · 100% would recommend", facts=["Okendo: 29 reviews, 100% would recommend this product"])
    slab.stars(MARGIN + 24, 146, 5, size=11, gap=2, fill=LIME, id="Stars slab")
    slab.text(MARGIN + 94, 156, "5.0 · Rated 5.0 out of 5 stars · Based on 29 reviews", P, 14, 500, CREAM)
    slab.text(MARGIN + 24, 180, "100% would recommend this product", P, 14, 500, CREAM)
    reviews = [
        ("ABSOLUTE FAVORITE", [("“These pourovers are the absolute best.", False), ("1000% better than any coffee pod,", True), ("the flavor is consistent and delicious.”", False)], "Natalie D."),
        ("BOLD FLAVOR- SO EASY", [("“This coffee has a bold flavor without the bitterness. I was very pleased. And so easy.”", False)], "Cheryl P."),
        ("MY GO TO", [("“I've been a loyal customer for 5 years. Mu go to coffee every morning.”", False)], "dee B."),
        ("WE LOVE COPPER COW", [("“Always a winner in our home.”", False)], "Kara M."),
    ]
    hang = [0, 22, 14, 30]
    tags = s4.g("Hung review tags")
    TW2 = 258
    row_bottom = 0
    ry0 = 232
    for i, (title, segs, name) in enumerate(reviews):
        col, row = i % 2, i // 2
        tx = MARGIN + col * (TW2 + 24)
        ty = ry0 + row * 0 + hang[i]
        if row == 1:
            ty = row_bottom + 34 + hang[i]
        tg = tags.g(f"Tag {name}")
        # line the tag hangs from
        th = 130 + (38 if len(segs) > 1 or len(segs[0][0]) > 60 else 0)
        if row == 0 and i == 0:
            tags.line(MARGIN, ry0 - 12, W - MARGIN, ry0 - 12, stroke=GREEN, stroke_width=2)
        line_y = (ry0 - 12) if row == 0 else (ty - 12 - hang[i])
        tg.line(tx + TW2 / 2, line_y, tx + TW2 / 2, ty + 2, stroke=GREEN, stroke_width=2)
        filter_tag(tg, tx, ty, TW2, th)
        tg.stars(tx + 18, ty + 30, 5, size=11, gap=2, fill=GREEN, id=f"Stars {name}")
        tg.text(tx + 18, ty + 60, title, P, 14, 700, GREEN, letter_spacing=0.5)
        hh = tg.text_runs_block(tx + 18, ty + 80, segs, P, 14, TW2 - 36, DEEP, weight=400, bold_weight=700, line_height=18)
        tg.text(tx + 18, ty + 80 + hh + 6, name, P, 14, 600, GREEN, runs=[(name, {"weight": 600}), (" · VERIFIED BUYER", {"weight": 500, "fill": PINK_DK})])
        # bottom of this tag
        bottom = max(ty + th, ty + 80 + hh + 6 + 8)
        if ty + 80 + hh + 14 > ty + th:   # grow the tag to fit the quote
            tg.children = []
            th = (80 + hh + 24)
            tg.line(tx + TW2 / 2, line_y, tx + TW2 / 2, ty + 2, stroke=GREEN, stroke_width=2)
            filter_tag(tg, tx, ty, TW2, th)
            tg.stars(tx + 18, ty + 30, 5, size=11, gap=2, fill=GREEN, id=f"Stars {name}")
            tg.text(tx + 18, ty + 60, title, P, 14, 700, GREEN, letter_spacing=0.5)
            tg.text_runs_block(tx + 18, ty + 80, segs, P, 14, TW2 - 36, DEEP, weight=400, bold_weight=700, line_height=18)
            tg.text(tx + 18, ty + 80 + hh + 6, name, P, 14, 600, GREEN, runs=[(name, {"weight": 600}), (" · VERIFIED BUYER", {"weight": 500, "fill": PINK_DK})])
            bottom = ty + th
        if row == 0:
            row_bottom = max(row_bottom, bottom)
        if row == 1 and col == 0:
            tags.line(MARGIN, ty - 12 - hang[i], W - MARGIN, ty - 12 - hang[i], stroke=GREEN, stroke_width=2)
        last_bottom = bottom if row == 1 else 0
        if row == 1:
            row2_bottom = max(bottom, locals().get("row2_bottom", 0))
    S4H = row2_bottom + 40
    e.section_h["04 Brewers"] = S4H; e.y = e.section_y["04 Brewers"] + S4H
    s4.children[0] = f'<rect x="0" y="0" width="{W}" height="{S4H}" fill="{PINK}"/>'

    # ------------------------------------------------------------------ S5 Debbie
    s5 = e.section("05 Debbie and the farmers", 10, bg=GREEN)
    s5.rect(0, 0, W, 4, fill=LIME)
    s5.text(MARGIN, 58, "WOMEN AND AAPI OWNED", P, 14, 700, LIME, letter_spacing=1.5)
    hh = s5.text_block(MARGIN, 96, "Robusta's been overlooked for too long.", P, 28, 310, 800, CREAM, line_height=34, max_lines=3)
    y5 = 96 + hh + 10
    hh = s5.text_block(MARGIN, y5, "Founded and led by Debbie, a Vietnamese-Californian obsessed with traditional Vietnamese coffee. We source climate-resilient beans from Vietnam's first organic-certified farms.", P, 15, 310, 400, CREAM, line_height=22, opacity=0.9)
    y5 += hh + 10
    hh = s5.text_block(MARGIN, y5, "We pay our farmers 2X the market rate because they've earned it.", P, 15, 310, 600, CREAM, line_height=22)
    y5 += hh
    s5.image(A / "woman_owned.png", 362, 60, 216, 122, fit="contain", id="Woman owned badge")
    S5H = max(y5 + 44, 240)
    e.section_h["05 Debbie and the farmers"] = S5H; e.y = e.section_y["05 Debbie and the farmers"] + S5H
    s5.children[0] = f'<rect x="0" y="0" width="{W}" height="{S5H}" fill="{GREEN}"/>'

    # ------------------------------------------------------------------ S6 Next box + close + footer
    s6 = e.section("06 Next box and close", 10, bg=CREAM)
    s6.image(A / "paper_grain.png", 0, 0, W, 700, fit="stretch", opacity=0.35, id="Paper grain S6")
    s6.text(MARGIN, 54, "EXPLORE OUR GREATEST SIPS", P, 14, 700, GREEN, letter_spacing=2)
    prods = [
        ("snick_cut.png", GREEN, CREAM, "*NEW* SNICKERDOODLE POUR OVER COFFEE - 8CT", "$16.00", "Snickerdoodle Spice & Everything Nice!"),
        ("mystery_cut.png", LIME, DEEP, "MYSTERY LATTE BUNDLE - 10CT", "$15.00", "10 lattes inside (10 pour overs, 10 creamers)!"),
        ("vanilla_cut.png", PINK, DEEP, "VANILLA CREAMER - 24CT", "$22.00", ""),
    ]
    bw = 172
    bottoms = []
    for i, (img, bg, fg, name, price, note) in enumerate(prods):
        bx = MARGIN + i * (bw + 12)
        pg = s6.g(f"Block {name[:24]}")
        pg.rrect(bx, 76, bw, 150, 14, fill=bg)
        pg.image(A / img, bx + 12, 84, bw - 24, 134, fit="contain", id=f"{name[:20]} photo")
        hh = pg.text_block(bx, 252, name, P, 14, bw, 700, GREEN, line_height=18)
        pg.text(bx, 252 + hh + 2, price, P, 14, 600, DEEP)
        yy = 252 + hh + 24
        if note:
            hh2 = pg.text_block(bx, yy, note, P, 14, bw, 400, DEEP, line_height=18)
            yy += hh2
        pw_ = pg.measure(price, P, 14, 600)
        pg.path(shapes.arrow_right(bx + pw_ + 8, 252 + hh - 10, 16), stroke=GREEN, stroke_width=2, cap="round", join="round")
        bottoms.append(yy)
    cy6 = max(bottoms) + 24
    cta(s6, 175, cy6, where="S6")
    fy = cy6 + 54 + 40
    ft = s6.g("Footer")
    ft.rect(0, fy, W, 150, fill=GREEN)
    ft.image(A / "logo_cream.png", MARGIN, fy + 24, 50, 56, fit="contain", id="Logo cream")
    ft.text(MARGIN + 66, fy + 46, "Copper Cow Coffee · support@coppercowcoffee.com", P, 12, 500, CREAM)
    ft.text(MARGIN + 66, fy + 66, "Instagram · Facebook · YouTube · Pinterest · TikTok", P, 12, 500, CREAM, opacity=0.85)
    ft.text_block(MARGIN + 66, fy + 92, "Can't see this email? View it in your browser. / No longer want to receive these emails? Unsubscribe.", P, 12, 470, 400, CREAM, line_height=16, opacity=0.8)
    S6H = fy + 150
    e.section_h["06 Next box and close"] = S6H; e.y = e.section_y["06 Next box and close"] + S6H
    s6.children[0] = f'<rect x="0" y="0" width="{W}" height="{S6H}" fill="{CREAM}"/>'
    return e


if __name__ == "__main__":
    em = build({})
    print(em.save(HERE / "final" / f"{NAME}.svg"), em.height)
