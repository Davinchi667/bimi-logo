# Charles Chocolates · DESIGN INTENT · 2026-10-10 WAT

Copy: COPY.md in this folder. Build it exactly. One welcome email, 600 px wide, 7 sections, 2,580 px tall, 2 motion moments (S2 key, S3 meter).

## Signature concept: the box key

Every box of chocolates comes with a key card that tells you what is inside. The Classic Collection is "the chocolates that started it all", and its own photo is a top-down open turquoise box with a note printed in the lid. The email opens that box: the real 20 piece photo on the left, gold leader lines running to a cream "WHAT'S INSIDE" card listing the six fillings from the product description (fleur de sel caramel, raspberry, passion fruit, citrus pairings, espresso, mint), with the sizes and prices at its foot. The free bar is handled the same way, as a measured thing: a meter that shows the 20 piece box at \$58 clearing the \$50 line. Real proof inside the concept: the fillings and prices from .js, "Best Chocolatier in the Bay Area" (San Francisco Magazine) and Sunset's "Best of the West" as drawn seals, three press quotes, four Judge.me gift reviews on tags hung from their black signature ribbon, "from 617 reviews".

Moving away from: a Halloween hero with a bar-banner offer worded one of four ways, and three review cards.

## (a) Inspo refs

| **\#** | **Brand**  | **File**                                                                      | **Pose taken**                                                       | **Lands in**                |
|--------|------------|-------------------------------------------------------------------------------|----------------------------------------------------------------------|-----------------------------|
| 1      | Ghost      | /workspace/design-studio/inspo/mailboard/ghost/newest-202933-desktop.jpg      | Callout diagram with leader lines from a product to labels           | S2 box key                  |
| 2      | ARMRA      | /workspace/design-studio/inspo/mailboard/armra/board-201241-desktop.jpg       | Visual equation and thin-rule frames on a strong field               | S3 \$58 vs \$50 meter       |
| 3      | Olipop     | /workspace/design-studio/inspo/mailboard/olipop/newest-202238-desktop.jpg     | Ground colour changing section by section with a product per section | S1 brown, S2 teal, S3 cream |
| 4      | Milk Bar   | /workspace/design-studio/inspo/mailboard/milk-bar/newest-202904-desktop.jpg   | Checkerboard of photo and quote                                      | S6 split black/cream        |
| 5      | Last Crumb | /workspace/design-studio/inspo/mailboard/last-crumb/newest-202820-desktop.jpg | Each item given a paper label with a line of its own                 | S5 gift tags on the ribbon  |

## (b) Section map

| **Section**       | **Pose / layout**                                                         | **Copy** | **Image (COPY.md §9)** | **Motion**  | **Height** |
|-------------------|---------------------------------------------------------------------------|----------|------------------------|-------------|------------|
| S1 Hero           | Brown; logo; 50 px cream serif; closed small box angled; ribbon price tag | S1       | C0, D1                 | No          | 440        |
| S2 Box key        | Teal; open 20 piece box left; gold leader lines; cream key card right     | S2       | D2                     | **Yes, M1** | 560        |
| S3 Free bar meter | Cream; 520 px meter; markers \$31 / \$50 flag / \$58; bar slides out      | S3       | D5 (small)             | **Yes, M2** | 340        |
| S4 Awards + press | Brown; two gold line seals; three narrow quote columns with gold rules    | S4       | none                   | No          | 280        |
| S5 Gift tags      | Cream; black ribbon across; four tags, different sizes and tilts          | S5       | none                   | No          | 400        |
| S6 Split          | Left black with Skulls, right cream with Almonds; text links              | S6       | D3, D4                 | No          | 320        |
| S7 Close + footer | Teal, cream line, button; white footer                                    | S7       | C0                     | No          | 240        |
| Total             |                                                                           |          |                        | 2           | 2,580      |

Ground sequence: brown → teal → cream → brown → cream → black/cream split → teal → white footer.

## (c) Motion (frame 1 is a finished static state)

**M1 · S2 the key lights up** · 560 x 420 GIF, 7 frames, about 5 s, loop.

- F1 (static, 1,600 ms): all six leader lines drawn in gold, all six card lines at full cream, sizes visible. Finished state.

- F2 to F7 (550 ms each): one card line at a time turns gold with its leader line thickened; the others dim to 50%. Card copy is also set as live HTML under the GIF for accessibility (or the GIF carries alt text with the six fillings).

**M2 · S3 the meter fills** · 520 x 160 GIF, 5 frames, about 4 s, loop.

- F1 (static, 1,600 ms): fill to \$58, the \$50 flag reads FREE BAR, the bar image sits out from under the flag. Finished state.

- F2 (400 ms): fill at \$0. F3 (400 ms): fill at the \$31 marker. F4 (400 ms): fill at \$50, flag lights. F5 (1,200 ms): fill at \$58, bar slides out (same as F1). The offer line, the term and the math line are static HTML.

GIF budget about 400 KB.

## (d) The one CTA shape

Rectangle, 54 px tall, 2 px radius, teal \#108474 fill (cream \#f6efe6 fill with brown text on the teal S7 ground), white caps 15 px, letter-spaced 1.5 px, 340 px wide, with a 1 px gold \#A68660 inner rule like a box edge. Wording SHOP THE CLASSIC COLLECTION (S1, S2, S7); SHOP THE 20 PIECE BOX once (S3). S6 uses caps text links. Seals, tags and the meter flag never look like buttons.

## (e) Palette and type (from the site and the box)

- Teal \#108474 (site), chocolate brown \#533528 (site), gold \#A68660 (site), dark text \#303030, black \#000000, white. Cream \#f6efe6 as the paper colour (from the box note and key card idea; not a site hex, a neutral). Purple \#9e58bb appears on the site; not used.

- Type: Georgia serif (the site's) for headlines, quotes and the key card, 40 to 50 px display; Poppins (the site's body font) 15 to 16 px body and caps labels.

## (f) What NOT to do

- No three white review cards: reviews are gift tags on a ribbon.

- No colour-swap template, no grey footer, no product grid.

- No code, no code box, no "%" and no second wording of the offer. Only the homepage sentence with "Non-cumulative."

- Do not show which piece is which flavour beyond the numbered card; no labels printed on individual pieces.

- No publication logos (seals are drawn type); no Good Housekeeping quote (long dash).

- No Dubai bar as hero, no 4.83 average.

- No em dash in any text layer. No emoji (the site's press-label emoji are dropped).

## Asset gaps and fallbacks

| **Want**                    | **Have?**         | **Fallback**                                         |
|-----------------------------|-------------------|------------------------------------------------------|
| The actual free bar         | Not named on site | D5 wrapped bar as "a bar", or a drawn bar silhouette |
| White logo for dark grounds | Only logo.png     | Put it on a cream bar above S1, or invert if clean   |
| Award logos                 | Not used          | Drawn seals                                          |
