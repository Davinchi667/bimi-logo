# Shani Darden Skin Care · DESIGN INTENT · 2026-10-10 WAT

Copy: COPY.md in this folder. Build it exactly. One welcome email, 600 px wide, 7 sections, 2,580 px tall, 2 motion moments (S3, S4) plus one optional (S1 bottle turn, see M3).

## Signature concept: the home-care card

At the end of a facial, an esthetician hands the client a card that says what to do at home. Shani's own directions for Retinol Reform are exactly that kind of card: "Start with 1-2 times per week and add a night each week to build tolerance." The email builds the card: a cream aftercare card on a slate field, a four-week calendar with retinol nights filled in, her apply-steps and caution line, a Travel Size bottle paper-clipped to the corner, and one reviewer's margin note ("you still have to ease into using", Libby K., 4 stars). Real proof inside the concept: Shani's directions verbatim, the 2-week clinical numbers with their 39-subject footnote right below the card, and the review widget's own "Favorite Features" tallies (Easy To Use 74, Gentle 60, Non-Irritating 46).

Moving away from: a white page with a bottle, "Welcome", three review cards, a 15% banner that the site does not actually send.

## (a) Inspo refs

| **\#** | **Brand**                                    | **File**                                                                       | **Pose taken**                                           | **Lands in**                |
|--------|----------------------------------------------|--------------------------------------------------------------------------------|----------------------------------------------------------|-----------------------------|
| 1      | Lemme                                        | /workspace/design-studio/inspo/mailboard/lemme/fav-200717-desktop.jpg          | Results timeline in rows (day one / later)               | S3 week rows                |
| 2      | Crown Affair                                 | /workspace/design-studio/inspo/mailboard/crown-affair/board-201437-desktop.jpg | Calm, editorial diagnostic bands with small caps labels  | S3 card typography, S5 rail |
| 3      | Last Crumb                                   | /workspace/design-studio/inspo/mailboard/last-crumb/newest-202817-desktop.jpg  | Big % numbers with captions, footnote under them         | S4 study row                |
| 4      | David Protein (STEAL_THIS: "mono stat rail") | /workspace/design-studio/inspo/mailboard/\_meta/STEAL_THIS.md                  | A thin stat rail beside content                          | S5 Favorite Features rail   |
| 5      | Manukora                                     | /workspace/design-studio/inspo/mailboard/manukora/board-201601-desktop.jpg     | Quiet premium product on a single ground with a pill CTA | S1, S6                      |

## (b) Section map

| **Section**       | **Pose / layout**                                                                                        | **Copy** | **Image (COPY.md §9)** | **Motion**      | **Height** |
|-------------------|----------------------------------------------------------------------------------------------------------|----------|------------------------|-----------------|------------|
| S1 Hero           | Off-white; black logo; 54 px Didot headline centred; bottle on a black rule; drawn star rating           | S1       | B0, B2                 | Optional M3     | 440        |
| S2 Shani's note   | White; square greyscale portrait left, italic quote right, small caps sign                               | S2       | B1                     | No              | 260        |
| S3 Home-care card | Slate; cream card; 4 x 7 night grid; directions; caution; clipped Travel bottle; handwritten margin note | S3       | B3                     | **Yes, M1**     | 540        |
| S4 Study row      | White; four Didot numbers; captions; rule; footnote                                                      | S4       | none                   | **Yes, M2**     | 320        |
| S5 Clients        | Off-white; left stat rail; right four torn-edge note cards, uneven heights, slate left rule              | S5       | none                   | No              | 420        |
| S6 Routine        | Slate; bottle + cream jar on a shelf line; size toggle; three ruled perks; button                        | S6       | B2, B4                 | No              | 360        |
| S7 Close + footer | White; serif paragraph; button; footer                                                                   | S7       | B0                     | No              | 240        |
| Total             |                                                                                                          |          |                        | 2 (+1 optional) | 2,580      |

Ground sequence: off-white → white → slate → white → off-white → slate → white.

## (c) Motion (frame 1 is a finished static state; Outlook shows frame 1)

**M1 · S3 the nights fill in** · 500 x 300 GIF (the grid only), 5 frames, about 4.2 s, loop.

- F1 (static, 1,600 ms): all four weeks filled (2, 3, 4, 5 nights). This is the printed state.

- F2 (500 ms): grid empty, row labels on.

- F3 (500 ms): Week 1 filled. F4 (500 ms): Weeks 1 and 2. F5 (1,100 ms): Weeks 1 to 3, then loop to F1. Directions, caution, margin note and button are static HTML around the GIF.

**M2 · S4 count-up** · 560 x 120 GIF, 4 frames, about 3 s, loop.

- F1 (static, 1,600 ms): 100% 100% 100% 94%.

- F2 (300 ms): 0% each. F3 (300 ms): 50% 50% 50% 47%. F4 (800 ms): final (same as F1). The footnote is HTML under the GIF, always visible.

**M3 (optional) · S1 bottle turn** · 220 x 300 GIF, 3 frames: front (B2), angled (B5 crop), front. Use only if a clean angled cut-out can be made from B5; otherwise keep S1 static.

## (d) The one CTA shape

Rectangle, 52 px tall, 0 radius, black \#000000 fill (white \#FFFFFF fill with black text on slate grounds), white caps 14 px, letter-spaced 2 px, 320 px wide. Wording SHOP RETINOL REFORM (S1, S6, S7); the card's START WITH THE TRAVEL SIZE, \$30 uses the same shape once. Night circles, size toggle and stat rail are outlines, never filled rectangles.

## (e) Palette and type (from the site)

- Black \#000000, white \#FFFFFF, slate \#272d45, muted violet-grey \#676986, warm grey text \#4A474A, off-white \#f4f4f6, rule grey \#e5e5e5. All in the homepage CSS. Card cream: \#f4f4f6 warmed slightly is acceptable; no new hues.

- Display: "Didot Display" (the site's own, Georgia fallback) for headlines and numbers. Body: the theme's inherited sans; build in a clean sans (Helvetica Neue / Arial) 15 to 16 px. Margin note in a light handwriting face, one use only.

## (f) What NOT to do

- No three white review cards in a row: reviews are torn notes of different heights beside a stat rail, and one sits on the card.

- No colour-swap template, no grey footer bar, no four-product grid.

- No discount, code box or "mystery discount" (never rendered on site).

- No before/after photo: its claims sit in the image and are not checked line by line.

- No % without the study footnote beside it. No "acne", "prescription", "clinically proven" badges.

- No invented night schedule beyond COPY.md; label it "Example schedule".

- No em dash in any text layer (the long dash before the site's "Shani" sign-off is dropped). No emoji; stars are drawn.

## Asset gaps and fallbacks

| **Want**                          | **Have?**                  | **Fallback**                                        |
|-----------------------------------|----------------------------|-----------------------------------------------------|
| Transparent cut-out of the bottle | B2 is on white             | Place on white or off-white only, or mask the white |
| Travel Size photo                 | Not separate in .js images | Scale B3 down and label "TRAVEL SIZE (10 ML)"       |
| Address for footer                | No                         | Klaviyo sender address at build time                |
