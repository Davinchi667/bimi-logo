# OSKIA Skincare · COPY (spec welcome email for cold outreach)

Brief date: 2026-10-10 10:40 WAT (10:40 UK) · Writer: Brand Copywriter bot · Research: briefs/2026-10-10/oskia-skincare/RESEARCH.md (not edited) · Design: DESIGN_INTENT.md in this folder Who builds it: Claude (claude.ai), from this file pasted in by David. Design Studio makes the GIFs only. 600 px wide, 6 sections, 2,580 px tall. UK spelling throughout, as the site writes it.

## 1. Header

| **Field**           | **Value**                                                                                                                                                                                                                                                                                                                          |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Brand name          | OSKIA (the site writes OSKIA in caps; "OSKIA London" on the bottle)                                                                                                                                                                                                                                                                |
| Website link        | [<u>https://www.oskiaskincare.com/</u>](https://www.oskiaskincare.com/) (oskiaskincare.com redirects here)                                                                                                                                                                                                                         |
| Nature              | Flow (welcome), the email behind the footer line "Sign up to our newsletters and receive £10 off your first order"                                                                                                                                                                                                                 |
| Angle               | The brand calls itself "Intelligent Skin Nutrition", and its own product graphic is a NUTRITIONAL FACTS panel. The welcome reads Midnight Elixir like a nutrition label: what is in it, what the 8-week trial measured, what 196 reviewers say, with the £10 and the complimentary Super-R travel size as the reason to start now. |
| Best seller         | Midnight Elixir · [<u>https://www.oskiaskincare.com/products/midnight-elixir</u>](https://www.oskiaskincare.com/products/midnight-elixir) · £165.00 (50ml), £60.00 (15ml), both available (products/midnight-elixir.js, 2026-10-10 10:10 WAT) · Bazaarvoice "4.8                                                                   |
| Products to feature | Midnight Elixir only. Super-R travel size named as the complimentary gift.                                                                                                                                                                                                                                                         |
| Style family        | Midnight cobalt (the bottle), slate grey of their NUTRITIONAL FACTS panel, white, near-black \#1C1B1F (theme); Suranna serif + Montserrat (site CSS). Motion: midnight-to-morning hero (S1), the label's results bars (S3), the 196-review histogram (S5)                                                                          |
| Subject line A      | £10 off your first OSKIA order                                                                                                                                                                                                                                                                                                     |
| Subject line B      | Midnight Elixir: 4.8 stars from 196 reviews                                                                                                                                                                                                                                                                                        |
| Preview             | plus a complimentary travel-size super-r with every order, from our factory in wales.                                                                                                                                                                                                                                              |
| Announcement bar    | ENJOY A COMPLIMENTARY TRAVEL-SIZE SUPER-R WITH EVERY ORDER                                                                                                                                                                                                                                                                         |
| Length              | 6 sections, 2,580 px (520 + 260 + 700 + 320 + 480 + 300)                                                                                                                                                                                                                                                                           |

Voice rules for this brand: calm, scientific, luxurious; UK spelling ("Anti-Ageing", "favourite", "energised", "labour"); "we/our" for OSKIA, Georgie in first person in her quote. No emoji. Skin claims only as the site states them, each clinical number with the site's own trial footnote. The site writes "Midnight Elixir" with capitals and "Super-R" with a hyphen. No code is known; none lettered.

## Research log

| **Studied**                                                                                                                                                                                   | **Where / when**           | **Move taken**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| midnight-elixir.js, live price re-check                                                                                                                                                       | 10 Oct 10:10 WAT           | £165.00 / £60.00, available. Price flag from research resolved: the £61 vs £54 question is the Autumn Trio, which is **£54.00 live** (autumn-trio.js 10:10 WAT); the £61.00 in the 9 Oct cart email no longer matches. Autumn Trio not used.                                                                                                                                                                                                                                                                                       |
| Bazaarvoice review widget, rendered in headless Chrome and read inside its shadow DOM                                                                                                         | product page, 10:15 WAT    | Real reviews exist (research said none captured). Snapshot: 5 stars 162, 4 stars 24, 3 stars 6, 2 stars 3, 1 star 1; 4.8 / 196; 91% recommend; Quality 4.9, Value 4.5. Four reviews taken with the names and ages shown.                                                                                                                                                                                                                                                                                                           |
| Product page body                                                                                                                                                                             | 10:15 WAT                  | "Clinical Results 36% increase in elasticity 24% increase in firmness 24% improvement in wrinkle depth 100% felt their skin was more hydrated ... \*Independent clinical trials 2024. 20 subjects of mixed ethnicity and skin tone (20% Fitzpatrick 5 & 6), one application a day over 8 weeks." These go into the label with the footnote. **New:** the same page also says "Experience a 32% improvement in elasticity in only 8 weeks"; the email uses only the clinical block (36%) with its footnote, and flags the mismatch. |
| Product images                                                                                                                                                                                | .js images                 | Bottle "Midnight-Elixir-shadow.jpg"; their "NUTRITIONAL FACTS" panel (Copy_of_Untitled_1750...png); "30 Actives, including:" annotated swatch; "clinical-trials.jpg" (+24 / +36 / -24). The NUTRITIONAL FACTS panel is the concept.                                                                                                                                                                                                                                                                                                |
| About page                                                                                                                                                                                    | /pages/about-us, 10:20 WAT | "Born from veterinary science in 2009", "up to 40 actives", "produced in their own factory in Wales", "250 International Beauty Awards".                                                                                                                                                                                                                                                                                                                                                                                           |
| Homepage / cart drawer                                                                                                                                                                        | 10:12 WAT                  | Bar: "Enjoy a complimentary travel-size Super-R with every order". Footer £10 line. **New:** the cart drawer says both "Free shipping on orders £25+" and "Free UK delivery On All Orders £40+"; no shipping line is used.                                                                                                                                                                                                                                                                                                         |
| Mailboard: Last Crumb 202817, Lemme fav-200717, Peace Out fav-195802, David Protein 202046                                                                                                    | inspo/mailboard            | Survey-style stats (Last Crumb), results timeline and big % stats with a study footnote (Lemme, Peace Out), mono data rows on dark (David Protein).                                                                                                                                                                                                                                                                                                                                                                                |
| Luxury skincare welcomes: Aesop "An introduction to Aesop" (via trykopi.ai), BIOSSANCE "\[Activate\] 20% off welcome offer" (reallygoodemails.com), Vintner's Daughter serum email (migma.ai) | search 10 Oct 10:30 WAT    | Aesop states the offer as one line under ingredient-and-laboratory storytelling; BIOSSANCE puts the offer in the subject. Taken: offer plainly in subject A and S2, the science carries the body. Not taken: Aesop's split offer (image plus a bottom block).                                                                                                                                                                                                                                                                      |

## Diagnosis

Segment: a UK visitor who signs up in the footer for "£10 off your first order", likely 40+ (the site's "Ages - 40+"; the reviewers' age bands are 35 to 65+). Awareness stage 2: they know OSKIA and serums; the doubt is £165 for a night serum. Stage 2 task: new proof (an independent 8-week trial and 196 reviews). Sophistication 4 (labelled assumption: "growth factors", "peptides" and "retinol alternative" are common across luxury night serums), so the mechanism is featured as a full label: 30 actives listed by group, the trial numbers with the footnote. One performance: a firmer, brighter complexion by morning. Belief built on: skin needs nutrients to repair. Belief routed around: "expensive serum is just marketing". Belief left alone: menopause specifics (one site line only). Route: central (£165, considered). Defensible claim: Midnight Elixir, 30 actives, independent clinical trials 2024 with 20 subjects over 8 weeks showing 36% increase in elasticity, 4.8 from 196 reviews, 91% recommend, £10 off the first order, complimentary travel-size Super-R with every order. Structure: proof-led product email (reason-why), offer stated after the hero. Levers, three: the discount (reason: signing up), social proof (196 reviews, ages, 91%), authority (the trial and Georgie's 15 years). Left out: the 250 awards as a lever (one line in the footer only), subscriptions, Autumn Trio, loyalty.

## 2. Problems spotted (for David, not for the design)

| **\#**                                                                                                                                                                                                | **Problem**                                                                                                                                                    | **Where**                  | **Checked**                                              | **Evidence**           | **Confidence**    | **Use**   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|----------------------------------------------------------|------------------------|-------------------|-----------|
| 1                                                                                                                                                                                                     | A £10 "First order discount" flyout is built in Klaviyo but never shows; the only visible capture is the footer line.                                          | homepage; Klaviyo UYXrF3   | RESEARCH.md 08:57 to 08:59 WAT; footer re-read 10:12 WAT | kf_oskia.json, renders | confirmed         | FOR EMAIL |
| 2                                                                                                                                                                                                     | The footer £10 form is a Shopify customer form while Klaviyo and Mailchimp both load.                                                                          | homepage HTML              | 08:56 WAT                                                | home.html              | confirmed (setup) | FOR EMAIL |
| 3                                                                                                                                                                                                     | New: the Midnight Elixir page gives two elasticity figures: "32% improvement in elasticity in only 8 weeks" and "36% increase in elasticity" (clinical block). | product page               | 10:15 WAT                                                | pdp                    | confirmed         | call note |
| 4                                                                                                                                                                                                     | New: the cart drawer shows two shipping thresholds: "Free shipping on orders £25+" and "Free UK delivery On All Orders £40+".                                  | cart drawer, homepage HTML | 10:12 WAT                                                | home.html              | confirmed in HTML | call note |
| 5                                                                                                                                                                                                     | Resolved: Autumn Trio is £54.00 live; the 9 Oct cart email showed £61.00.                                                                                      | autumn-trio.js             | 10:10 WAT                                                | .js                    | confirmed         | call note |
| 6                                                                                                                                                                                                     | Product description on the .js says "Contains 30 Actives"; the about page says "up to 40 actives" (range, not a conflict).                                     |                            | 10:20 WAT                                                |                        | n/a               | none      |
| How the design answers \#1: the email carries the £10 and the Super-R gift to anyone who signs up, flyout or footer.                                                                                  |                                                                                                                                                                |                            |                                                          |                        |                   |           |
| Needs sign-up test (David): sign up in the footer with [<u>davidoshinubi+oskia@gmail.com</u>](mailto:davidoshinubi+oskia@gmail.com); wait 24 h; note which tool sends and whether a £10 code arrives. |                                                                                                                                                                |                            |                                                          |                        |                   |           |

## 3. Verified proof and offers

| **Item**                                                                                                                                                                            | **Verbatim text**                                                                                                                                                                                                                                                                                                                                                                                                            | **Source URL**                                                                                      | **Checked**                                                                                                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Rating                                                                                                                                                                              | 4.8                                                                                                                                                                                                                                                                                                                                                                                                                          | 196 Reviews · 121 out of 133 (91%) reviewers recommend this product                                 | [<u>https://www.oskiaskincare.com/products/midnight-elixir</u>](https://www.oskiaskincare.com/products/midnight-elixir) |
| Snapshot                                                                                                                                                                            | 162 reviews with 5 stars · 24 with 4 stars · 6 with 3 stars · 3 with 2 stars · 1 review with 1 star                                                                                                                                                                                                                                                                                                                          | same (Bazaarvoice)                                                                                  | 10:15                                                                                                                   |
| Award                                                                                                                                                                               | Marie Claire - Best New Night Serum · Marie Claire Skin Awards 2025 - Best New Night Product                                                                                                                                                                                                                                                                                                                                 | same                                                                                                | 10:15                                                                                                                   |
| Clinical                                                                                                                                                                            | 36% increase in elasticity 24% increase in firmness 24% improvement in wrinkle depth 100% felt their skin was more hydrated 100% felt their skin looked calmer 95% felt their skin was firmer 90% felt their skin looked more rested 90% felt their skin looked more energised \*Independent clinical trials 2024. 20 subjects of mixed ethnicity and skin tone (20% Fitzpatrick 5 & 6), one application a day over 8 weeks. | same                                                                                                | 10:15                                                                                                                   |
| Signup offer                                                                                                                                                                        | Sign up to our newsletters and receive £10 off your first order                                                                                                                                                                                                                                                                                                                                                              | footer, all pages                                                                                   | 10:12                                                                                                                   |
| Gift                                                                                                                                                                                | Enjoy a complimentary travel-size Super-R with every order                                                                                                                                                                                                                                                                                                                                                                   | announcement bar                                                                                    | 10:12                                                                                                                   |
| Origin                                                                                                                                                                              | Born from veterinary science in 2009 · produced in their own factory in Wales · 250 International Beauty Awards                                                                                                                                                                                                                                                                                                              | [<u>https://www.oskiaskincare.com/pages/about-us</u>](https://www.oskiaskincare.com/pages/about-us) | 10:20                                                                                                                   |
| Not on site (do not use): a £10 code; a minimum spend for the £10 (none stated in the footer line; the hidden flyout's terms were not visible); a site-wide rating; customer count. |                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                     |                                                                                                                         |

## 4. Email copy, section by section

### S1 · Hero · 520 px · MOTION (midnight to morning)

Pose: full-bleed deep cobalt-to-black gradient (night). The Midnight Elixir bottle centred-right, large (about 360 px tall), a soft reflection under it. Headline in Suranna serif, white, 46 px, left, two lines. Small Montserrat caps kicker above with the award. The GIF changes only the background: midnight navy to a pale dawn grey over 4 frames; bottle and type stay put. Ref: Manukora (headline set in the sky of a full-bleed scene), Liquid Death 202647 (left-aligned line on dark). Image: [<u>https://cdn.shopify.com/s/files/1/0801/4151/7122/files/Midnight-Elixir-shadow.jpg?v=1757280688</u>](https://cdn.shopify.com/s/files/1/0801/4151/7122/files/Midnight-Elixir-shadow.jpg?v=1757280688) (cut the bottle from its white ground)

Bar: ENJOY A COMPLIMENTARY TRAVEL-SIZE SUPER-R WITH EVERY ORDER

Kicker: MARIE CLAIRE - BEST NEW NIGHT SERUM

Headline: A firmer, brighter complexion by morning.

Subheadline: Formulated to work with our circadian systems to repair and regenerate skin overnight.

Proof line: 4.8 · 196 Reviews · 91% of reviewers recommend

CTA: DISCOVER MIDNIGHT ELIXIR → https://www.oskiaskincare.com/products/midnight-elixir

\[DESIGN NOTE\] The hyphen in "MARIE CLAIRE - BEST NEW NIGHT SERUM" is the site's. Frame 1 is the night state, complete and readable; Outlook shows it.

### S2 · £10 off and the Super-R · 260 px · static

Pose: white field, thin slate rule top and bottom. Left: "£10" in Suranna, 120 px, cobalt. Right: the two offer lines and the button. Far right, small: the Super-R travel-size jar. Image: [<u>https://cdn.shopify.com/s/files/1/0801/4151/7122/files/super-r-shadow.jpg?v=1757280698</u>](https://cdn.shopify.com/s/files/1/0801/4151/7122/files/super-r-shadow.jpg?v=1757280698)

Kicker: WELCOME TO OSKIA

Headline: £10 off your first order

Sign up to our newsletters and receive £10 off your first order.

Enjoy a complimentary travel-size Super-R with every order.

CTA: DISCOVER MIDNIGHT ELIXIR → https://www.oskiaskincare.com/products/midnight-elixir

\[DESIGN NOTE\] No code box: no code is public and the flyout that would issue one is not showing. When OSKIA supplies the code, add a box reading "YOUR CODE:" in Montserrat bold under the £10. Never in the subject or preview. The Super-R image shows the full-size jar; label it "travel size" only in the copy line, do not imply the full jar is free.

### S3 · Skin nutrition facts · 700 px · MOTION (signature)

Pose: slate grey \#5E6772 field. Centre: a tall white-ruled "NUTRITIONAL FACTS" label in their style (white text on slate, thick rule under the title, thin rules between rows), 480 px wide, like the back of a food pack. Top block: serving line and the actives groups. Middle block: "RESULTS AFTER 8 WEEKS" with three horizontal bars (36, 24, 24) that fill in the GIF, then five "felt" rows as percentage bars. Bottom: the footnote in 10 px. The bottle sits small, tilted, at the label's top right corner, breaking the frame. Ref: the brand's own NUTRITIONAL FACTS graphic, Last Crumb 202817 (stat bars), Lemme fav-200717 (study footnote under big %). Images: NUTRITIONAL FACTS panel for reference [<u>https://cdn.shopify.com/s/files/1/0801/4151/7122/files/Copy_of_Untitled_1750_x_1750_px_6_27ce9862-7788-46b6-b9ea-6eb0d42e1131.png?v=1767957582</u>](https://cdn.shopify.com/s/files/1/0801/4151/7122/files/Copy_of_Untitled_1750_x_1750_px_6_27ce9862-7788-46b6-b9ea-6eb0d42e1131.png?v=1767957582) · bottle as S1

Kicker: INTELLIGENT SKIN NUTRITION

Title: NUTRITIONAL FACTS · MIDNIGHT ELIXIR

Serving: Contains 30 Actives · 50ml £165.00 · 15ml £60.00

Peptides & EGFs: Five Bio-tech Growth Factors (EGF, IGF-1, Acidic FGF, Basic FGF, VEGF) firm, regenerate and repair.

Shiitake & Trametes Versicolor Complex (with double Vitamin C) brightens and illuminates.

Melatonin Liposomes & Sea Fennel boost regeneration.

Snap 8™ Peptide (Acetyl Octapeptide-3) relaxes muscles to smooth.

Plus our OSKIA MSM Regen Complex and Vitamins A, C, E, B3, B9 & Pro-Vitamin D3.

RESULTS AFTER 8 WEEKS\*

36% increase in elasticity

24% increase in firmness

24% improvement in wrinkle depth

100% felt their skin was more hydrated

100% felt their skin looked calmer

95% felt their skin was firmer

90% felt their skin looked more rested

90% felt their skin looked more energised

\*Independent clinical trials 2024. 20 subjects of mixed ethnicity and skin tone (20% Fitzpatrick 5 & 6), one application a day over 8 weeks.

CTA: DISCOVER MIDNIGHT ELIXIR → https://www.oskiaskincare.com/products/midnight-elixir

\[DESIGN NOTE\] Keep the footnote on the label, same block as the numbers, at least 10 px and 70% white. Do not use the page's separate "32%" line anywhere. "™" stays on Snap 8. The "RESULTS AFTER 8 WEEKS" heading is drawn from "one application a day over 8 weeks" and the image "AFTER 8 WEEKS, UP TO:".

### S4 · Georgie · 320 px · static

Pose: white field. A large Suranna open-quote mark in cobalt, the quote in Suranna 22 px, left, max 3 short paragraphs; signature line in Montserrat caps. A slim slate side rail on the left with two facts. Image: none (no founder photo URL found on the pages read).

"A true labour of love and a culmination of over 15 years of skin study and formulation, our Midnight Elixir promises to transform your skin. Rather selfishly formulated with myself very much in mind as I face my 49th year, it's a product that I am deeply proud of."

GEORGIE CLEEVE, FOUNDER

Rail: Born from veterinary science in 2009 · Produced in our own factory in Wales

\[DESIGN NOTE\] The about page writes "produced in their own factory in Wales"; in OSKIA's own voice here it reads "our own factory" (§8). Quote trimmed at a sentence end (§8).

### S5 · 196 reviews · 480 px · MOTION (histogram)

Pose: deep cobalt field. Left column (200 px): "4.8" in Suranna 96 px white, "196 Reviews", the five-row histogram as thin white bars with counts (GIF fills them), then "121 out of 133 (91%) reviewers recommend this product". Right column: four reviews stacked as a lab-notebook list, each row with the reviewer's age band as a small mono tag on the left (the widget shows it), stars, bold caps title, quote, name and place. Thin white rules between rows. Ref: Last Crumb 202817 (bars), David Protein 202046 (mono tags in rows). Image: none.

Kicker: WHAT OUR CUSTOMERS SAY

4.8 · 196 Reviews

5 ★ 162 · 4 ★ 24 · 3 ★ 6 · 2 ★ 3 · 1 ★ 1

121 out of 133 (91%) reviewers recommend this product

AGE 55 TO 64 · ★★★★★ DOES WHAT IT SAYS

"Really loving this product I put it underneath the night cream and I wake up and my skin looks well rested and nourished"

Emma M

AGE 45 TO 54 · ★★★★★ MY FAVOURITE SERUM

"This is my third bottle and so far this is the best serum I've ever used. My skin looks radiant and plump."

Monika

AGE 65 OR OVER · ★★★★★ OUTSTANDING RESULTS

"This is my second purchase of the Midnight Elixir and I find it made my 70 year old skin more luminous and hydrated I also noticed a difference in fine lines since using the product"

Roma25, Scotland

AGE 35 TO 44 · ★★★★★ LOVE THE MIDNIGHT SERUM

"My skin loves the midnight serum. I've used 3 full bottles."

Adele, London

\[DESIGN NOTE\] Quotes are verbatim, missing punctuation kept (Emma M, Roma25). Roma25's review ends "Only downside is price"; it is trimmed before that line (§8), which is a real flaw: if David prefers to show it, restore it. Adele's is trimmed at a sentence end. Names exactly as the widget shows them.

### S6 · Close + footer · 300 px · static

Pose: white field, centred: one Suranna line, the button, then a near-black \#1C1B1F footer with the white logo, links and the awards line. Image: logo [<u>https://www.oskiaskincare.com/cdn/shop/files/new_logo.svg</u>](https://www.oskiaskincare.com/cdn/shop/files/new_logo.svg) (invert to white on the footer)

Headline: Nutritional Support For Optimal Skin Health, Resilience & Longevity

£10 off your first order, and a complimentary travel-size Super-R with every order.

CTA: DISCOVER MIDNIGHT ELIXIR → https://www.oskiaskincare.com/products/midnight-elixir

Footer: OSKIA · Intelligent Skin Nutrition · 250 International Beauty Awards · B Corp Certified

Instagram · Facebook · TikTok · Pinterest

Can't see this email? View it in your browser. / No longer want to receive these emails? Unsubscribe.

\[DESIGN NOTE\] No postal address on the pages read; Klaviyo adds the legal address.

## 5. Rule check and 40-point self-check

Long dashes: none (the site's "Marie Claire - Best New Night Serum" uses a hyphen) · the banned o-word: none · banned phrases: none · reviews: 4 verbatim from the rendered Bazaarvoice widget, all 5-star, names and ages as shown · code: none known, none lettered · skin claims: only the site's, clinical numbers with the site's footnote in the same block · UK spelling: yes · CTA: one shape, one wording (DISCOVER MIDNIGHT ELIXIR, the site's "Discover" verb), 4 uses · lint: PASS (final report). 40-point: 1 yes (stage 2, soph 4 labelled). 2 yes (firmer, brighter by morning). 3 yes. 4 yes. 5 yes, the label features the mechanism. 6 proof-led reason-why. 7 n/a. 8 new proof. 9 yes (their label, their trial, their founder). 10 yes. 11 yes (6 words). 12 yes. 13 opening: the promise in the site's words. 14 yes. 15 yes (skin repairs overnight). 16 yes. 17 featured. 18 yes, as stated. 19 three. 20 none. 21 yes, 4.8 not 5, 1-star row shown. 22 yes. 23 price flaw available (Roma25), noted. 24 none. 25 roughly yes. 26 no (ingredients). 27 no. 28 yes. 29 yes (footnote line). 30 yes. 31 none forced. 32 yes (S2 and S6). 33 yes. 34 no guarantee on site, none written. 35 none. 36 none. 37 yes. 38 yes. 39 yes. 40 yes as a spec.

## 6. Claims I could NOT verify (left out)

1.  The £10 code and any minimum spend · footer, flyout config (RESEARCH.md) · closest: "Sign up to our newsletters and receive £10 off your first order".

2.  Which free-shipping threshold is current (£25+ or £40+) · cart drawer · no shipping line used.

3.  "32% improvement in elasticity" vs "36% increase in elasticity" · product page · only the clinical block used.

4.  A founder photo · none found on the pages read.

## 7. Verified (exact source) for every line in §4

| **Line**              | **Verbatim source**                                                                                                                                   | **URL**                                                             |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Bar / gift            | Enjoy a complimentary travel-size Super-R with every order                                                                                            | homepage bar                                                        |
| Kicker                | Marie Claire - Best New Night Serum                                                                                                                   | product page                                                        |
| Headline              | ...revealing a firmer , brighter complexion by morning.                                                                                               | product page                                                        |
| Subheadline           | Formulated to work with our circadian systems to repair and regenerate skin overnight                                                                 | product page                                                        |
| Proof line            | 4.8                                                                                                                                                   | 196 Reviews · 121 out of 133 (91%) reviewers recommend this product |
| S2                    | Sign up to our newsletters and receive £10 off your first order                                                                                       | footer                                                              |
| S3 label              | Contains 30 Actives , including: Five Bio-tech Growth Factors ... Plus our OSKIA MSM Regen Complex and Vitamins A, C, E, B3, B9 & Pro-Vitamin D3.     | midnight-elixir.js                                                  |
| S3 results + footnote | Clinical Results 36% ... \*Independent clinical trials 2024 ... over 8 weeks.                                                                         | product page                                                        |
| S3 prices             | 50ml £165.00 · 15ml £60.00                                                                                                                            | .js                                                                 |
| S3 title              | NUTRITIONAL FACTS                                                                                                                                     | product image                                                       |
| S4                    | "A true labour of love ... deeply proud of and contains..." - Georgie Cleeve, Founder                                                                 | product page                                                        |
| S4 rail               | Born from veterinary science in 2009 · produced in their own factory in Wales                                                                         | /pages/about-us                                                     |
| S5                    | snapshot, ratings, four reviews, names, ages                                                                                                          | product page (Bazaarvoice, rendered)                                |
| S6                    | Nutritional Support For Optimal Skin Health, Resilience & Longevity · 250 International Beauty Awards · B Corp Certified · INTELLIGENT SKIN NUTRITION | about page, footer                                                  |

## 8. Changes from the brand's own words

| **Section**       | **Site text**                                                                                                    | **Copy text**                             | **Why**                                   |
|-------------------|------------------------------------------------------------------------------------------------------------------|-------------------------------------------|-------------------------------------------|
| S1 headline       | revealing a firmer , brighter complexion by morning.                                                             | A firmer, brighter complexion by morning. | Fragment as headline; stray space removed |
| S1 proof          | 121 out of 133 (91%) reviewers recommend this product                                                            | 91% of reviewers recommend                | Length (full line in S5)                  |
| S3                | Shiitake & Trametes Versicolor Complex Complex (with double Vitamin C )                                          | ...Complex (with double Vitamin C)        | Site's doubled word and stray space       |
| S4                | it's a product that I am deeply proud of and contains some of the most exciting new ingredients in our industry. | ends at "deeply proud of."                | Length                                    |
| S4 rail           | produced in their own factory in Wales                                                                           | Produced in our own factory in Wales      | Brand voice is first person in the email  |
| S5 Roma25         | ...since using the product Only downside is price                                                                | ends at "using the product"               | Length; flaw noted for David              |
| S5 Monika / Adele | longer reviews                                                                                                   | trimmed at sentence ends                  | Length                                    |

## 9. Assets (every image URL)

| **Use**                                                                                                                                                                                                                | **URL**                                                                                                                                                                                                                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Logo (SVG)                                                                                                                                                                                                             | [<u>https://www.oskiaskincare.com/cdn/shop/files/new_logo.svg</u>](https://www.oskiaskincare.com/cdn/shop/files/new_logo.svg)                                                                                                                                                                           |
| Midnight Elixir bottle (hero)                                                                                                                                                                                          | [<u>https://cdn.shopify.com/s/files/1/0801/4151/7122/files/Midnight-Elixir-shadow.jpg?v=1757280688</u>](https://cdn.shopify.com/s/files/1/0801/4151/7122/files/Midnight-Elixir-shadow.jpg?v=1757280688)                                                                                                 |
| Midnight Elixir 15ml                                                                                                                                                                                                   | [<u>https://cdn.shopify.com/s/files/1/0801/4151/7122/files/midnight-elixir-15ml-1403x2100-b71f08a8-72a7-4996-8c8c-09cf9d28b68f.jpg?v=1763041802</u>](https://cdn.shopify.com/s/files/1/0801/4151/7122/files/midnight-elixir-15ml-1403x2100-b71f08a8-72a7-4996-8c8c-09cf9d28b68f.jpg?v=1763041802)       |
| NUTRITIONAL FACTS panel                                                                                                                                                                                                | [<u>https://cdn.shopify.com/s/files/1/0801/4151/7122/files/Copy_of_Untitled_1750_x_1750_px_6_27ce9862-7788-46b6-b9ea-6eb0d42e1131.png?v=1767957582</u>](https://cdn.shopify.com/s/files/1/0801/4151/7122/files/Copy_of_Untitled_1750_x_1750_px_6_27ce9862-7788-46b6-b9ea-6eb0d42e1131.png?v=1767957582) |
| 30 Actives annotated swatch                                                                                                                                                                                            | [<u>https://cdn.shopify.com/s/files/1/0801/4151/7122/files/Midnight_Elixir_Annotated_Swatch.jpg?v=1763041802</u>](https://cdn.shopify.com/s/files/1/0801/4151/7122/files/Midnight_Elixir_Annotated_Swatch.jpg?v=1763041802)                                                                             |
| Clinical trials graphic                                                                                                                                                                                                | [<u>https://cdn.shopify.com/s/files/1/0801/4151/7122/files/clinical-trials.jpg?v=1763041802</u>](https://cdn.shopify.com/s/files/1/0801/4151/7122/files/clinical-trials.jpg?v=1763041802)                                                                                                               |
| Consumer trial graphic                                                                                                                                                                                                 | [<u>https://cdn.shopify.com/s/files/1/0801/4151/7122/files/ME-Consumer-trial.jpg?v=1763041802</u>](https://cdn.shopify.com/s/files/1/0801/4151/7122/files/ME-Consumer-trial.jpg?v=1763041802)                                                                                                           |
| Drip texture                                                                                                                                                                                                           | [<u>https://cdn.shopify.com/s/files/1/0801/4151/7122/files/midnight-elixir-pixeleyes-drip_1.jpg?v=1763041802</u>](https://cdn.shopify.com/s/files/1/0801/4151/7122/files/midnight-elixir-pixeleyes-drip_1.jpg?v=1763041802)                                                                             |
| Super-R                                                                                                                                                                                                                | [<u>https://cdn.shopify.com/s/files/1/0801/4151/7122/files/super-r-shadow.jpg?v=1757280698</u>](https://cdn.shopify.com/s/files/1/0801/4151/7122/files/super-r-shadow.jpg?v=1757280698)                                                                                                                 |
| Colours: bottle cobalt (sample, about \#23297A), slate panel (sample, about \#5E6772), \#1C1B1F near-black (theme), \#FFFFFF, \#D9D9D9 rules. Fonts: Suranna (serif display) and Montserrat (body), from the site CSS. |                                                                                                                                                                                                                                                                                                         |
