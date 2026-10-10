# OSKIA Skincare · DESIGN INTENT · 2026-10-10 WAT

For: Claude (claude.ai) building from COPY.md, and Design Studio for the three GIFs. 600 px wide, 6 sections, 2,580 px tall, 3 motion moments. UK spelling in every text layer.

## Signature concept: the skin nutrition facts label

OSKIA sells "Intelligent Skin Nutrition", and its own Midnight Elixir gallery includes a slate-grey "NUTRITIONAL FACTS" panel listing vitamins, minerals, amino acids, peptides and EGFs, like the back of a food pack. S3 builds the email's centrepiece as that label at full height: the actives groups on top, then a "RESULTS AFTER 8 WEEKS" block where the trial numbers sit as bars that fill in, then the trial footnote printed on the label itself, the way a nutrition panel carries its small print. The bottle leans on the label's corner, breaking its frame. Proof inside the concept: "Contains 30 Actives" and the named actives from the .js; "36% increase in elasticity / 24% increase in firmness / 24% improvement in wrinkle depth" and the five "felt" percentages; the footnote "\*Independent clinical trials 2024. 20 subjects of mixed ethnicity and skin tone (20% Fitzpatrick 5 & 6), one application a day over 8 weeks." S5 continues the lab tone: 196 reviews as a ruled notebook list with each reviewer's age band as a mono tag.

## Inspo refs

| **\#** | **Brand / file**                                                                                 | **Pose taken**                                            | **Lands in**                  |
|--------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------|-------------------------------|
| 1      | Last Crumb · /workspace/design-studio/inspo/mailboard/last-crumb/newest-202817-desktop.jpg       | Survey stats as horizontal bars with boxed numbers        | S3 results bars, S5 histogram |
| 2      | Lemme · /workspace/design-studio/inspo/mailboard/lemme/fav-200717-desktop.jpg                    | Big % results with the study footnote directly underneath | S3 footnote placement         |
| 3      | Peace Out · /workspace/design-studio/inspo/mailboard/peace-out/fav-195802-desktop.jpg            | Small kicker over a giant promise                         | S1 kicker + headline          |
| 4      | David Protein · /workspace/design-studio/inspo/mailboard/david-protein/newest-202046-desktop.jpg | Mono data rows on a dark gradient                         | S5 age tags and rules         |
| 5      | OSKIA's own NUTRITIONAL FACTS panel (product image)                                              | Slate label, white rules, two columns of nutrients        | S3 label                      |

## Section map

| **Section**                                                                          | **Pose**                                                                                 | **Image**                  | **Motion**               | **Height** |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|----------------------------|--------------------------|------------|
| S1 Hero                                                                              | Night gradient, bottle right, serif headline left, kicker with the Marie Claire line     | bottle                     | Yes: M1 night to morning | 520        |
| S2 £10 + Super-R                                                                     | White, slate rules, "£10" serif 120 px cobalt left, lines right, small Super-R jar       | Super-R                    | No                       | 260        |
| S3 Nutrition facts                                                                   | Slate field, 480 px label with white rules, results bars, footnote, bottle on the corner | bottle, panel as reference | Yes: M2 bars             | 700        |
| S4 Georgie                                                                           | White, big cobalt quote mark, serif quote, slate side rail                               | none                       | No                       | 320        |
| S5 196 reviews                                                                       | Cobalt; 4.8 + histogram left; ruled list of four reviews with age tags right             | none                       | Yes: M3 histogram        | 480        |
| S6 Close + footer                                                                    | White close line + button; near-black footer with white logo                             | logo                       | No                       | 300        |
| Total                                                                                |                                                                                          |                            | 3                        | 2,580      |
| Background sequence: night gradient, white, slate, white, cobalt, white, near-black. |                                                                                          |                            |                          |            |

## Motion moments (frame 1 is a finished static state)

**M1 · S1 midnight to morning** · 600 x 520 GIF (background layer only, type live HTML over it where possible; otherwise type baked into every frame identically), 4 frames, loop, about 6 s. F1 (2,500 ms, static): deep cobalt-black night, small stars, bottle lit. F2 (600 ms): navy lifting at the bottom edge. F3 (600 ms): pale blue-grey dawn band. F4 (2,000 ms): soft morning grey; bottle the same. Text colour must stay legible on all frames (white with a subtle shadow, or switch the headline only in F4 to \#1C1B1F). **M2 · S3 results bars** · 440 x 300 GIF covering the RESULTS block, 4 frames, loop, about 4 s. F1 (1,800 ms, static): all eight bars at their printed values (36, 24, 24, 100, 100, 95, 90, 90; the first three on one scale, the five "felt" rows on a 0 to 100 scale, visibly separate). F2 (300 ms): bars at 0. F3 (300 ms): half. F4 (1,500 ms): full, as F1. Numbers stay printed in every frame. The footnote is live HTML under the GIF. **M3 · S5 histogram** · 200 x 120 GIF, 3 frames, no loop, ends on final. F1 (static and final): bars at 162 / 24 / 6 / 3 / 1 out of 196. F2: zero. F3: final. GIF budget about 450 KB (M1 is the heaviest; keep it 4 frames, 64 colours).

## The one CTA shape

Rectangle, 52 px tall, 0 radius, \#1C1B1F fill, white Montserrat 600 caps 13 px, 2 px letter spacing, 280 px wide, left-aligned in S1 and S3, centred in S2 and S6. On the cobalt and slate fields, invert (white fill, near-black text). One wording: DISCOVER MIDNIGHT ELIXIR → [<u>https://www.oskiaskincare.com/products/midnight-elixir</u>](https://www.oskiaskincare.com/products/midnight-elixir). Nothing else in the email may look like a button.

## Palette and type

Bottle cobalt (about \#23297A, sample from the bottle photo), slate (about \#5E6772, sample from the NUTRITIONAL FACTS panel), \#1C1B1F near-black (theme), \#FFFFFF, \#D9D9D9 rules. Suranna for display and the quote (site CSS), Montserrat for body, labels and buttons (site CSS). A monospace only for the S5 age tags. Body 15 to 16 px; footnotes no smaller than 10 px.

## What NOT to do

- No three white review cards: reviews are a ruled list on cobalt with age tags.

- No colour-swap template, no beige "spa" stock photos, no leaves or water splashes.

- No "32%" anywhere (it conflicts with the clinical block); no clinical number without its footnote in the same section.

- No skin or menopause claims beyond the copy; no "anti-ageing" promise as a headline.

- No code lettered; no code in subject or preview; no shipping threshold (the site shows two).

- No US spelling. No em dash in any layer. No emoji.

- Do not show the full Super-R jar as "free": the gift is the travel size.

## Asset gaps and fallbacks

| **Wanted**                | **Have it?**                           | **Fallback**                                                 |
|---------------------------|----------------------------------------|--------------------------------------------------------------|
| Georgie photo             | No URL found                           | Type-only quote block                                        |
| Super-R travel-size photo | Only the full jar (super-r-shadow.jpg) | Show the jar small, captioned by the copy line "travel-size" |
| Night/morning photography | None                                   | Drawn gradient                                               |
