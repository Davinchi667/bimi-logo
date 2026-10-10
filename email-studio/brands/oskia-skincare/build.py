"""OSKIA · spec welcome email 01 · "The skin nutrition facts label".
Source: brands/oskia-skincare/COPY.md + DESIGN_INTENT.md (10 Oct 2026). Copy verbatim, UK spelling.
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "tools"))
from emailkit import Email, FontRegistry, shapes, MARGIN  # noqa: E402

BRAND = "oskia-skincare"
NAME = "oskia-skincare_welcome-01"
A = HERE / "assets"

fonts = FontRegistry()
fonts.google("Suranna", weights=(400,))
fonts.google("Montserrat", weights=(400, 500, 600, 700))
fonts.google("IBM Plex Mono", weights=(500,))
S, M, MONO = "Suranna", "Montserrat", "IBM Plex Mono"

COBALT, SLATE, INK, WHITE, RULE = "#23297A", "#5E6772", "#1C1B1F", "#FFFFFF", "#D9D9D9"
NIGHT_TOP, NIGHT_BOTTOM = "#05070C", "#0E1230"
W = 600
URL = "https://www.oskiaskincare.com/products/midnight-elixir"

_vb, *LOGO_PATHS = (A / "logo_paths.txt").read_text().splitlines()
LOGO_W, LOGO_H = 326.09, 103.5


def logo(g, x, y, h, fill):
    s = h / LOGO_H
    gg = g.g(f"Logo OSKIA {fill}")
    for d in LOGO_PATHS:
        gg.path(d, fill=fill, transform=f"translate({x} {y}) scale({s:.4f})")
    return LOGO_W * s


def cta(g, x, y, invert=False, where=""):
    """The one CTA shape: 280 x 52 rectangle, 0 radius, near-black / white inverted on dark fields."""
    return g.button(x, y, 280, 52, "DISCOVER MIDNIGHT ELIXIR", M, 13 if False else 14, 600,
                    fill=WHITE if invert else INK, text_fill=INK if invert else WHITE, rx=0, letter_spacing=2,
                    id=f"CTA DISCOVER MIDNIGHT ELIXIR {where}".strip())


def build(state: dict | None = None) -> Email:
    state = state or {}
    e = Email(fonts, name=NAME, bg=WHITE)
    k1, k2, k3 = state.get("M1", 0), state.get("M2", 0), state.get("M3", 0)

    # ------------------------------------------------------------------ S1 Hero 520 (M1: night to morning)
    H1 = 520
    s = e.section("01 Hero", H1, bg=NIGHT_TOP)
    m1 = s.g("M1 Night to morning band", clip=(0, 0, W, H1))
    grad = e.gradient("night", [(0, NIGHT_TOP), (1, NIGHT_BOTTOM)])
    m1.rect(0, 0, W, H1, fill=grad)
    m1.image(A / "night_scene.jpg", 0, 0, W, H1, fit="cover", id="Night scene (brand photo)")
    m1.rect(0, 0, 380, H1, fill=e.gradient("legibility", [(0, "#05070C"), (0.55, "#05070C"), (1, "#05070C")], x1=0, y1=0, x2=1, y2=0), opacity=0.0)
    m1.rect(0, 36, 400, H1 - 36, fill=e.gradient("shade", [(0, "#04060B"), (0.6, "#04060B"), (1, "#04060B")], x1=0, y1=0, x2=1, y2=0), opacity=0.0)
    m1.raw(f'<rect x="0" y="36" width="420" height="{H1 - 36}" fill="url(#shadeL)"/>')
    e._defs.append('<linearGradient id="shadeL" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#04060B" stop-opacity="0.92"/><stop offset="0.6" stop-color="#04060B" stop-opacity="0.75"/><stop offset="1" stop-color="#04060B" stop-opacity="0"/></linearGradient>')
    # dawn overlays per state
    if k1 == 1:
        m1.rect(0, 0, W, H1, fill=e.gradient("dawn1", [(0, "#05070C"), (0.55, "#1A2558"), (1, "#3A4A8C")]), opacity=0.75)
    elif k1 == 2:
        m1.rect(0, 0, W, H1, fill=e.gradient("dawn2", [(0, "#2B3560"), (0.5, "#7E8FB3"), (1, "#B9C4D6")]), opacity=0.85)
    elif k1 == 3:
        m1.rect(0, 0, W, H1, fill=e.gradient("morning", [(0, "#B9BFCB"), (1, "#E3E6EA")]), opacity=0.96)
    ink = INK if k1 == 3 else WHITE
    sub_ink = INK if k1 == 3 else WHITE
    # bar
    bar = m1.g("Announcement bar")
    bar.rect(0, 0, W, 36, fill=INK if k1 == 3 else "#000000", opacity=0.85)
    bar.text(300, 24, "ENJOY A COMPLIMENTARY TRAVEL-SIZE SUPER-R WITH EVERY ORDER", M, 14, 600, WHITE, anchor="middle", letter_spacing=0.6)
    # bottle, right, with a soft reflection
    m1.text(MARGIN, 96, "MARIE CLAIRE - BEST NEW NIGHT SERUM", M, 14, 600, sub_ink, letter_spacing=2, opacity=0.85)
    hl = m1.g("Headline")
    hl.text(MARGIN, 150, "A firmer, brighter", S, 44, 400, ink)
    hl.text(MARGIN, 198, "complexion", S, 44, 400, ink)
    hl.text(MARGIN, 246, "by morning.", S, 44, 400, ink)
    m1.text_block(MARGIN, 282, "Formulated to work with our circadian systems to repair and regenerate skin overnight.", M, 15, 320, 400, sub_ink, line_height=22, opacity=0.9, max_lines=3)
    m1.stars(MARGIN, 352, 4.8, size=13, gap=2, fill=ink, empty="#6B6F8A", id="Stars hero")
    m1.text(MARGIN + 82, 363, "4.8 · 196 Reviews", M, 14, 600, sub_ink)
    m1.text(MARGIN, 386, "91% of reviewers recommend", M, 14, 500, sub_ink, opacity=0.9)
    cta(m1, MARGIN, 414, invert=(k1 != 3), where="S1")
    e.module("M1", "Night to morning", "01 Hero", 0, H1, states=4, durations_ms=[2500, 600, 600, 2000],
             what_moves="the sky lifts from night through navy and dawn grey to morning; bottle and type stay put, type turns near-black on the morning frame",
             frame1="night: the brand's starry sky, white type, white CTA", assets=["brand night scene photo (bottle in moss, moths)"], facts=["Marie Claire line", "4.8 / 196 / 91%"])

    # ------------------------------------------------------------------ S2 £10 + Super-R 300
    H2 = 300
    s2 = e.section("02 Ten pounds off", H2, bg=WHITE)
    s2.image(A / "paper_grain.png", 0, 0, W, H2, fit="stretch", opacity=0.16, id="Grain S2")
    s2.rect(0, 0, W, 1, fill=SLATE); s2.rect(0, H2 - 1, W, 1, fill=SLATE)
    s2.text(MARGIN, 158, "£10", S, 120, 400, COBALT, id="Giant ten pounds")
    col = s2.g("Offer column")
    cx = 238
    col.text(cx, 66, "WELCOME TO OSKIA", M, 14, 600, SLATE, letter_spacing=2)
    col.text(cx, 100, "£10 off your first order", S, 26, 400, INK)
    col.text_block(cx, 130, "Sign up to our newsletters and receive £10 off your first order.", M, 14, 230, 400, INK, line_height=20, max_lines=3)
    col.text_block(cx, 178, "Enjoy a complimentary travel-size Super-R with every order.", M, 14, 230, 400, INK, line_height=20, max_lines=3)
    s2.image(A / "super_r_cut.png", 476, 92, 96, 71, fit="contain", id="Super-R jar")
    cta(s2, 160, 228, where="S2")

    # ------------------------------------------------------------------ S3 Nutrition facts (slate)
    s3 = e.section("03 Nutrition facts", 10, bg=SLATE)
    s3.text(300, 52, "INTELLIGENT SKIN NUTRITION", M, 14, 600, WHITE, anchor="middle", letter_spacing=3)
    LX0, LX1 = 60, 540
    label = s3.g("Nutrition label")
    frame_idx = len(label.children)
    label.rect(LX0, 80, LX1 - LX0, 10, fill="none", stroke=WHITE, stroke_width=2)   # resized at the end
    IX = LX0 + 22
    IW = LX1 - LX0 - 44
    y = 80 + 48
    label.text(IX, y, "NUTRITIONAL FACTS", M, 28, 700, WHITE, letter_spacing=1)
    y += 24
    label.text(IX, y, "MIDNIGHT ELIXIR", M, 14, 500, WHITE, letter_spacing=3)
    y += 16
    label.rect(IX, y, IW, 7, fill=WHITE)
    y += 28
    label.text(IX, y, "Contains 30 Actives · 50ml £165.00 · 15ml £60.00", M, 14, 600, WHITE)
    y += 12
    label.line(IX, y, IX + IW, y, stroke=WHITE, stroke_width=1)
    rows = [
        [("Peptides & EGFs:", True), ("Five Bio-tech Growth Factors (EGF, IGF-1, Acidic FGF, Basic FGF, VEGF) firm, regenerate and repair.", False)],
        [("Shiitake & Trametes Versicolor Complex", True), ("(with double Vitamin C) brightens and illuminates.", False)],
        [("Melatonin Liposomes & Sea Fennel", True), ("boost regeneration.", False)],
        [("Snap 8™ Peptide (Acetyl Octapeptide-3)", True), ("relaxes muscles to smooth.", False)],
        [("Plus our OSKIA MSM Regen Complex and Vitamins A, C, E, B3, B9 & Pro-Vitamin D3.", False)],
    ]
    for segs in rows:
        y += 24
        hh = label.text_runs_block(IX, y, segs, M, 14, IW, WHITE, weight=400, bold_weight=700, line_height=19)
        y += hh - 19 + 12
        label.line(IX, y, IX + IW, y, stroke=WHITE, stroke_width=1, opacity=0.7)
    y += 2
    label.rect(IX, y, IW, 7, fill=WHITE)
    y += 36
    label.text(IX, y, "RESULTS AFTER 8 WEEKS*", M, 16, 700, WHITE, letter_spacing=1)
    y += 14
    # --- M2 results bars
    band_top = y
    m2 = label.g("M2 Results bars band")
    fill_frac = {0: 1.0, 1: 0.0, 2: 0.5}[k2]
    results = [("36%", "increase in elasticity", 36, 50), ("24%", "increase in firmness", 24, 50), ("24%", "improvement in wrinkle depth", 24, 50)]
    felt = [("100%", "felt their skin was more hydrated", 100, 100), ("100%", "felt their skin looked calmer", 100, 100), ("95%", "felt their skin was firmer", 95, 100),
            ("90%", "felt their skin looked more rested", 90, 100), ("90%", "felt their skin looked more energised", 90, 100)]
    def bar_rows(items, yy):
        for num, lab, val, scale in items:
            yy += 24
            m2.text(IX, yy, num, M, 15, 700, WHITE)
            m2.text(IX + 50, yy, lab, M, 14, 400, WHITE)
            yy += 8
            m2.rect(IX, yy, IW, 6, fill=WHITE, opacity=0.22)
            w = IW * (val / scale) * fill_frac
            if w > 0:
                m2.rect(IX, yy, w, 6, fill=WHITE)
            yy += 6
        return yy
    y = bar_rows(results, y)
    y += 12
    m2.line(IX, y, IX + IW, y, stroke=WHITE, stroke_width=1, opacity=0.7)
    y += 2
    y = bar_rows(felt, y)
    y += 14
    band_h = y - band_top
    e.module("M2", "Results bars", "03 Nutrition facts", band_top, band_h, states=3, durations_ms=[3300, 300, 300],
             what_moves="the eight result bars fill from zero to half to their printed values (first three on a 0 to 50 scale, the five felt rows on 0 to 100)",
             frame1="all bars at their printed values", facts=["clinical block with footnote", "five consumer lines"])
    label.rect(IX, y, IW, 7, fill=WHITE)
    y += 24
    hh = label.text_block(IX, y, "*Independent clinical trials 2024. 20 subjects of mixed ethnicity and skin tone (20% Fitzpatrick 5 & 6), one application a day over 8 weeks.", M, 14, IW, 400, WHITE, line_height=19, opacity=0.75)
    y += hh + 10
    label_bottom = y
    label.children[frame_idx] = f'<rect x="{LX0}" y="80" width="{LX1 - LX0}" height="{label_bottom - 80}" fill="none" stroke="{WHITE}" stroke-width="2"/>'
    # bottle leaning on the label's top-right corner
    bt = s3.g("Bottle on the corner", x=478, y=28, rotate=12)
    bt.image(A / "bottle_cut.png", 0, 0, 58, 160, fit="contain", id="Bottle small")
    cta(s3, LX0, label_bottom + 28, invert=True, where="S3")
    S3H = label_bottom + 28 + 52 + 44
    e.section_h["03 Nutrition facts"] = S3H; e.y = e.section_y["03 Nutrition facts"] + S3H
    s3.children[0] = f'<rect x="0" y="0" width="{W}" height="{S3H}" fill="{SLATE}"/>'

    # ------------------------------------------------------------------ S4 Georgie (white, slate rail)
    s4 = e.section("04 Georgie", 10, bg=WHITE)
    s4.image(A / "paper_grain.png", 0, 0, W, 520, fit="stretch", opacity=0.16, id="Grain S4")
    rail = s4.g("Slate rail")
    rail.rect(0, 0, 124, 10, fill=SLATE)   # resized below
    rail_idx = len(rail.children) - 1
    q = s4.g("Quote")
    q.text(128, 118, "“", S, 110, 400, COBALT, id="Open quote mark")
    hh = q.text_block(152, 150, "A true labour of love and a culmination of over 15 years of skin study and formulation, our Midnight Elixir promises to transform your skin. Rather selfishly formulated with myself very much in mind as I face my 49th year, it's a product that I am deeply proud of.",
                      S, 22, 418, 400, INK, line_height=31)
    y4 = 150 + hh + 14
    q.text(152, y4, "GEORGIE CLEEVE, FOUNDER", M, 14, 600, INK, letter_spacing=2)
    S4H = y4 + 50
    rail.children[rail_idx] = f'<rect x="0" y="0" width="124" height="{S4H}" fill="{SLATE}"/>'
    facts = rail.g("Rail facts")
    h1_ = facts.text_block(MARGIN, 60, "Born from veterinary science in 2009", M, 14, 78, 600, WHITE, line_height=18)
    facts.line(MARGIN, 60 + h1_ + 6, MARGIN + 64, 60 + h1_ + 6, stroke=WHITE, stroke_width=1, opacity=0.6)
    facts.text_block(MARGIN, 60 + h1_ + 36, "Produced in our own factory in Wales", M, 14, 78, 600, WHITE, line_height=18)
    e.section_h["04 Georgie"] = S4H; e.y = e.section_y["04 Georgie"] + S4H
    s4.children[0] = f'<rect x="0" y="0" width="{W}" height="{S4H}" fill="{WHITE}"/>'

    # ------------------------------------------------------------------ S5 196 reviews (cobalt)
    s5 = e.section("05 Reviews", 10, bg=COBALT)
    s5.image(A / "drip_dark.jpg", 0, 0, W, 760, fit="cover", opacity=0.2, id="Drip surface")
    s5.text(MARGIN, 56, "WHAT OUR CUSTOMERS SAY", M, 14, 600, WHITE, letter_spacing=2)
    left = s5.g("Rating column")
    left.text(MARGIN, 156, "4.8", S, 96, 400, WHITE)
    left.text(MARGIN, 184, "196 Reviews", M, 14, 600, WHITE)
    m3 = left.g("M3 Histogram band")
    frac3 = {0: 1.0, 1: 0.0, 2: 0.5}[k3]
    counts = [("5", 162), ("4", 24), ("3", 6), ("2", 3), ("1", 1)]
    for i, (n, c) in enumerate(counts):
        yy = 212 + i * 22
        m3.text(MARGIN, yy + 8, n, MONO, 14, 500, WHITE)
        m3.path(shapes.star(MARGIN + 14, yy - 1, 11), fill=WHITE)
        m3.rect(MARGIN + 34, yy + 1, 110, 6, fill=WHITE, opacity=0.22)
        w = 110 * c / 196 * frac3
        if w > 0:
            m3.rect(MARGIN + 34, yy + 1, max(w, 1.5), 6, fill=WHITE)
        m3.text(MARGIN + 154, yy + 8, str(c), MONO, 14, 500, WHITE)
    e.module("M3", "Histogram", "05 Reviews", 206, 116, states=3, durations_ms=[2500, 300, 300],
             what_moves="the five star-count bars fill from zero to half to 162 / 24 / 6 / 3 / 1", frame1="bars at the Bazaarvoice counts", facts=["snapshot 162/24/6/3/1 of 196"])
    left.text_block(MARGIN, 346, "121 out of 133 (91%) reviewers recommend this product", M, 14, 196, 500, WHITE, line_height=19, opacity=0.9)
    reviews = [
        ("AGE 55 TO 64", "DOES WHAT IT SAYS", "“Really loving this product I put it underneath the night cream and I wake up and my skin looks well rested and nourished”", "Emma M"),
        ("AGE 45 TO 54", "MY FAVOURITE SERUM", "“This is my third bottle and so far this is the best serum I've ever used. My skin looks radiant and plump.”", "Monika"),
        ("AGE 65 OR OVER", "OUTSTANDING RESULTS", "“This is my second purchase of the Midnight Elixir and I find it made my 70 year old skin more luminous and hydrated I also noticed a difference in fine lines since using the product”", "Roma25, Scotland"),
        ("AGE 35 TO 44", "LOVE THE MIDNIGHT SERUM", "“My skin loves the midnight serum. I've used 3 full bottles.”", "Adele, London"),
    ]
    RX = 256
    RW = W - MARGIN - RX
    ry = 76
    lst = s5.g("Review list")
    for i, (age, title, quote, name) in enumerate(reviews):
        row = lst.g(f"Review {name}")
        row.line(RX, ry, W - MARGIN, ry, stroke=WHITE, stroke_width=1, opacity=0.5)
        ry += 24
        tw = row.measure(age, MONO, 14, 500) + 16
        row.rect(RX, ry - 14, tw, 20, fill="none", stroke=WHITE, stroke_width=1)
        row.text(RX + 8, ry, age, MONO, 14, 500, WHITE)
        row.stars(RX + tw + 12, ry - 12, 5, size=11, gap=2, fill=WHITE, id=f"Stars {name}")
        ry += 26
        row.text(RX, ry, title, M, 14, 700, WHITE, letter_spacing=0.5)
        ry += 22
        hh = row.text_block(RX, ry, quote, M, 14, RW, 400, WHITE, line_height=19, opacity=0.92)
        ry += hh + 2
        row.text(RX, ry, name, M, 14, 500, WHITE, opacity=0.8)
        ry += 22
    lst.line(RX, ry, W - MARGIN, ry, stroke=WHITE, stroke_width=1, opacity=0.5)
    S5H = max(ry + 40, 420)
    e.section_h["05 Reviews"] = S5H; e.y = e.section_y["05 Reviews"] + S5H
    s5.children[0] = f'<rect x="0" y="0" width="{W}" height="{COBALT and S5H}" fill="{COBALT}"/>'

    # ------------------------------------------------------------------ S6 Close + footer
    s6 = e.section("06 Close", 10, bg=WHITE)
    s6.image(A / "paper_grain.png", 0, 0, W, 420, fit="stretch", opacity=0.16, id="Grain S6")
    hh = s6.text_block(MARGIN, 76, "Nutritional Support For Optimal Skin Health, Resilience & Longevity", S, 26, 540, 400, INK, line_height=34, anchor="middle")
    y6 = 76 + hh + 6
    hh2 = s6.text_block(MARGIN, y6, "£10 off your first order, and a complimentary travel-size Super-R with every order.", M, 14, 540, 400, INK, line_height=20, anchor="middle")
    y6 += hh2 + 12
    cta(s6, 160, y6, where="S6")
    fy = y6 + 52 + 44
    ft = s6.g("Footer")
    ft.rect(0, fy, W, 150, fill=INK)
    logo(ft, MARGIN, fy + 30, 26, WHITE)
    ft.text_block(MARGIN + 100, fy + 40, "OSKIA · Intelligent Skin Nutrition · 250 International Beauty Awards · B Corp Certified", M, 12, 440, 500, WHITE, line_height=16, opacity=0.9)
    ft.text(MARGIN + 100, fy + 80, "Instagram · Facebook · TikTok · Pinterest", M, 12, 500, WHITE, opacity=0.8)
    ft.text_block(MARGIN + 100, fy + 104, "Can't see this email? View it in your browser. / No longer want to receive these emails? Unsubscribe.", M, 12, 440, 400, WHITE, line_height=16, opacity=0.7)
    S6H = fy + 150
    e.section_h["06 Close"] = S6H; e.y = e.section_y["06 Close"] + S6H
    s6.children[0] = f'<rect x="0" y="0" width="{W}" height="{S6H}" fill="{WHITE}"/>'
    return e


if __name__ == "__main__":
    em = build({})
    print(em.save(HERE / "final" / f"{NAME}.svg"), em.height)
