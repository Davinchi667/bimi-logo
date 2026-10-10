# evanhealy · DESIGN INTENT · 2026-10-10 WAT

Copy: COPY.md in this folder. Build it exactly. One welcome email, 600 px wide, 6 sections, 2,480 px tall, 3 motion moments (S2 code, S3 press, S5 price rail).

## Signature concept: the oil & water lab sheet

evanhealy distills its HydroSouls "in alembic copper at low temperatures", calls its team "rag-tag alchemists", and its homepage's first instruction is "Start with oil & water." The email is a page from the herbalist's lab notebook: "PROTOCOL NO. 1 · OIL & WATER", a faint grid, three steps (mist, mix, press, in their exact words) linked by a line drawn like copper still tubing, the two bottles labelled with leader lines and prices, a mono sum line, and customer notes pinned as pressed-specimen labels down a dried rose-geranium sprig. Real proof inside the concept: the protocol verbatim from the ritual page, four Okendo reviews that describe pressing it in (each tagged with its product), the 4.8 / 153 and 4.92 / 147 ratings, the popup's own code, and the Harvest Ritual's own \$187.46 compare-at.

Moving away from: a centred jar on white with "Welcome, Truth Seeker" and a 15% banner over a ritual the code can't be used on.

## (a) Inspo refs

| **\#** | **Brand**                                        | **File**                                                                        | **Pose taken**                                                             | **Lands in**                             |
|--------|--------------------------------------------------|---------------------------------------------------------------------------------|----------------------------------------------------------------------------|------------------------------------------|
| 1      | Alice Mushrooms                                  | /workspace/design-studio/inspo/mailboard/alice-mushrooms/fav-195808-desktop.jpg | Ingredient constellation: labels floating around a product with fine lines | S3 bottle labels with leader lines       |
| 2      | Ghost                                            | /workspace/design-studio/inspo/mailboard/ghost/newest-202933-desktop.jpg        | Callout diagram with leader lines                                          | S3 step drawings tied to the tubing line |
| 3      | Lemme                                            | /workspace/design-studio/inspo/mailboard/lemme/fav-200717-desktop.jpg           | Numbered step/time rows                                                    | S3 three steps                           |
| 4      | Crown Affair                                     | /workspace/design-studio/inspo/mailboard/crown-affair/board-201437-desktop.jpg  | Quiet editorial serif on warm paper                                        | S1, S6                                   |
| 5      | David Protein (STEAL_THIS "monospace stat rail") | /workspace/design-studio/inspo/mailboard/\_meta/STEAL_THIS.md                   | Mono stat rail beside product                                              | S5 price rail                            |

## (b) Section map

| **Section**        | **Pose / layout**                                                                                                            | **Copy** | **Image (COPY.md §9)** | **Motion**  | **Height** |
|--------------------|------------------------------------------------------------------------------------------------------------------------------|----------|------------------------|-------------|------------|
| S1 Hero            | Paper; black logo; 56 px Cochin left; HydroSoul + copper still right, coil off the edge; sage rule                           | S1       | E0, E2                 | No          | 440        |
| S2 Your code       | Sage; white popup card replay; dashed YOUR CODE box; exclusion line                                                          | S2       | none                   | **Yes, M1** | 360        |
| S3 Lab sheet       | Paper with 8 px grid; header strip; 3 steps on a copper-tube line with line drawings; two bottle cut-outs labelled; mono sum | S3       | E1, E2                 | **Yes, M2** | 560        |
| S4 Specimen labels | Paper; dried sprig stem centre; four pinned cream tags staggered                                                             | S4       | none                   | No          | 400        |
| S5 Harvest Ritual  | Deep green; product set photo left; mono price rail right, total struck, \$135 in Cochin                                     | S5       | E3                     | **Yes, M3** | 400        |
| S6 ROC + footer    | Paper; drawn seal; ROC paragraph; Garden line; button; footer                                                                | S6       | E0                     | No          | 320        |
| Total              |                                                                                                                              |          |                        | 3           | 2,480      |

Ground sequence: paper → sage → paper with grid → paper → deep green → paper (footer on white).

## (c) Motion (frame 1 is a finished static state)

**M1 · S2 popup replay** · 460 x 240 GIF, 4 frames, about 4 s, loop.

- F1 (static, 1,600 ms): the code view: "Use Code SEEKER15 for 15% off your first purchase" with the empty dashed box below (live code text sits over it in HTML).

- F2 (600 ms): "UNLOCK 15% off your first purchase" with an email field. F3 (600 ms): "GET MY 15% OFF CODE" button pressed. F4 (1,200 ms): the code view (same as F1). The code itself is live HTML text, not baked into the GIF.

**M2 · S3 the press** · 220 x 220 GIF (palm drawing), 5 frames, about 3.6 s, loop.

- F1 (static, 1,400 ms): one amber-orange drop (serum colour, from E1) and clear mist droplets already merged in the palm into a soft golden sheen. Finished state.

- F2 (500 ms): empty palm. F3 (500 ms): mist droplets land. F4 (500 ms): one amber drop lands beside them. F5 (700 ms): they swirl together; loop to F1. Their own how-to GIF (E2b) is a reference for pacing only, not a frame source.

**M3 · S5 price rail** · 260 x 300 GIF, 4 frames, about 3.5 s, loop.

- F1 (static, 1,600 ms): five lines, \$187.46 struck, \$135 shown large. Finished state.

- F2 (400 ms): five lines only. F3 (400 ms): total \$187.46 appears. F4 (1,100 ms): strike draws across it and \$135 rises in; loop to F1.

GIF budget about 400 KB.

## (d) The one CTA shape

Rectangle, 52 px tall, 0 radius, black \#000000 fill, white caps proxima-nova 14 px, letter-spaced 2 px, 320 px wide, left-aligned with the copy (centred in S2). On the deep green S5, cream \#f5f2ed fill with black text. Wording SHOP THE OIL & WATER START (S1, S2, S3, S6); SHOP THE HARVEST RITUAL (S5). The code box is dashed and never filled; specimen tags are paper, not buttons.

## (e) Palette and type (from the site)

- Sage \#5B7B5C, deep green \#5A6F4F, warm paper \#f5f2ed, black \#000000, white. Copper for the tubing line and seal accents sampled from the still in E2. All other hexes from homepage CSS.

- Type: Cochin (the site's heading face) 40 to 56 px; proxima-nova (the site's body) 15 to 16 px; a mono (IBM Plex Mono) only for the sum line and the S5 rail; one light handwriting face for bottle labels.

## (f) What NOT to do

- No three white review cards: reviews are pinned specimen tags, each naming its product.

- No colour-swap template, no grey footer, no product grid.

- Never show SEEKER15 next to the Harvest Ritual as if it applies; the exclusion line stays beside the code and under the ritual.

- No official ROC or certification logos unless the brand supplies them; drawn type seal only.

- No medical words (acne, rosacea, eczema, healing) in any layer.

- No gift-with-purchase tiers (unconfirmed for rituals).

- No em dash in any text layer. No emoji; stars are drawn.

## Asset gaps and fallbacks

| **Want**                    | **Have?**             | **Fallback**                                                          |
|-----------------------------|-----------------------|-----------------------------------------------------------------------|
| Transparent bottle cut-outs | Photos on backgrounds | Mask from E1 and E2, or set the photos in rounded frames on the sheet |
| Evan's photo / signature    | Not pulled            | No founder block; the brand voice carries                             |
| ROC logo                    | Not used              | Drawn seal                                                            |
