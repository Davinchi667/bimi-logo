# Big Shoulders Coffee · DESIGN INTENT · 2026-10-10 WAT

For: Claude (claude.ai) building the email from COPY.md, and Design Studio for the three GIFs. Build the copy exactly. 600 px wide, 6 sections, 2,400 px tall, 3 motion moments.

## Signature concept: this week's roast sheet

A roastery runs on production sheets: coffee, origin, roast level, grind, who roasted it. The brand's own label tiles already carry a LIGHT ROAST / DARK ROAST slider with a coffee-drop marker. The email turns S3 into Diego's filled-in roast sheet for the Colombia: cream paper clipped onto a black field, mono labels, ruled rows, his photo paper-clipped in the corner, the tile's sliders redrawn full width with the drop marker sliding into place, and the six real grind options lighting one by one. Proof inside the sheet (all from the site): "between 1,500 and 2,070 meters above sea level", "roughly 65 dedicated growers", \$26.00 / \$105.00, the six grinds from the .js, and "crowned the 2025 US Coffee Roasting Champion" next to Diego's photo. S4 then reads like the sheet's tasting column: 4.71 counting up, the real histogram, three 5-star reviewer notes.

## Inspo refs (structure only, never their words)

| **\#** | **Brand / file**                                                                                 | **Pose taken**                                                          | **Lands in**                                                     |
|--------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|------------------------------------------------------------------|
| 1      | Liquid Death · /workspace/design-studio/inspo/mailboard/liquid-death/newest-202647-desktop.jpg   | All-black canvas, left-aligned deadpan headline between hairline rules  | S1, S6                                                           |
| 2      | David Protein · /workspace/design-studio/inspo/mailboard/david-protein/newest-202046-desktop.jpg | Monospace data rows on dark, one column inverted                        | S3 sheet rows                                                    |
| 3      | Last Crumb · /workspace/design-studio/inspo/mailboard/last-crumb/newest-202817-desktop.jpg       | Boxed giant numbers and thin bar charts as the story                    | S2 "20%", S4 histogram                                           |
| 4      | Ghost · /workspace/design-studio/inspo/mailboard/ghost/newest-202933-desktop.jpg                 | Heavy condensed caps, product bleeding off a section edge, leader lines | S1 bag crossing into S2; S3 leaders from photo to ROASTED BY row |
| 5      | Big Shoulders' own label tile · BSCWebTile-Colombia-Apr142026.png                                | The roast slider with the drop marker                                   | S3 GIF                                                           |

## Section map

| **Section**                                                                                                | **Pose**                                                                                                                           | **Image**                                 | **Motion**             | **Height** |
|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|------------------------|------------|
| S1 Hero                                                                                                    | Orange ticker strip; black field; white logo; 2-line heavy caps headline left; bag right, bleeding into S2                         | hero bag crop, white logo                 | Yes: M1 ticker         | 480        |
| S2 The 20%                                                                                                 | Orange band, giant black "20%" left, footer lines right, black button                                                              | none                                      | No                     | 240        |
| S3 Roast sheet                                                                                             | Cream sheet on black, binder clip at top, ruled mono rows, sliders, grind chips, Diego print top right, Colombia tile bottom right | Diego IMG_3881, Colombia tile             | Yes: M2 slider + grind | 640        |
| S4 Reviews                                                                                                 | Black; orange 4.71 counter + histogram left; three reviewer notes on a cream strip right                                           | none                                      | Yes: M3 counter        | 400        |
| S5 Next bag                                                                                                | Cream; three label tiles in a row, no borders, text links                                                                          | Night Shift, 1848, Ethiopia Natural tiles | No                     | 300        |
| S6 Close + footer                                                                                          | Black; headline, button, footer; giant white logotype cropped at the bottom                                                        | white logo                                | No                     | 340        |
| Total                                                                                                      |                                                                                                                                    |                                           | 3                      | 2,400      |
| Background sequence: orange strip, black, orange, black with cream sheet, black, cream, black. Hard edges. |                                                                                                                                    |                                           |                        |            |

## Motion moments (frame 1 is always a finished static state; Outlook shows frame 1)

**M1 · S1 ticker** · 600 x 36 GIF, 6 frames, 400 ms each, loop. F1: text starting flush left, fully readable (static). F2 to F6: text shifted left 100 px per frame, wrapping. Black Poppins 13 px bold caps on \#F68B1E. **M2 · S3 roast sheet** · 520 x 220 GIF covering the ROAST and GRIND rows, 7 frames, loop, about 5 s. F1 (1,500 ms, static): both drop markers at their tile positions (about 45% and 38%), "Whole Bean" chip lit orange. F2 (300 ms): markers at far left. F3 (300 ms): markers halfway. F4 (600 ms): markers settled (as F1). F5 to F7 (600 ms each): the lit chip moves to Espresso, Automatic Drip, Pour Over. All other sheet rows are live HTML text outside the GIF. **M3 · S4 counter** · 200 x 140 GIF, 5 frames, no loop (ends on final), about 2 s. F1 (static, also the final): "4.71" in \#F68B1E, 120 px. F2 to F4 (250 ms): 0.00, 2.35, 4.10. F5 (hold): 4.71. Histogram bars are static HTML. GIF budget about 350 KB total. Export each F1 as PNG for the static build.

## The one CTA shape

Rectangle, 56 px tall, 0 radius, \#F68B1E fill, black Poppins 700 caps 16 px, 1 px letter spacing. On the orange S2 band invert it: black fill, white text. One wording: SHOP COLOMBIA, to [<u>https://bigshoulderscoffee.com/products/colombia-popayan-reserve</u>](https://bigshoulderscoffee.com/products/colombia-popayan-reserve). Grind chips, histogram and tiles must never look like buttons (chips are outlined pills, tiles are text-linked).

## Palette and type (from the site)

\#000000 black, \#F68B1E orange (theme and Judge.me star colour), \#FFFFFF, tile cream (sample from the Colombia tile, about \#F6E6C8), tile brown (about \#4A1E12) for sheet values. Poppins for headings and body (site variables). A monospace (for example IBM Plex Mono) only for sheet labels and the ticker is not mono. Headline 54 px heavy caps; body 16 px; sheet labels 11 px caps.

## What NOT to do

- No three white review cards; reviews are notes on the cream strip beside the counter.

- No colour-swap template: no white canvas, centred bag, grey footer.

- No three-up "light / medium / dark" roast grid (the generic roaster welcome).

- No made-up code anywhere, no code box until the brand gives its real code.

- No 2024 badge from the hero composite and no trophy text as a claim.

- No "best seller" label on Colombia (the brand lists it third in its own block).

- No Manos de Mujer, subscription ladder or wholesale content.

- No em dash in any text layer. No emoji.

## Asset gaps and fallbacks

| **Wanted**                 | **Have it?**                              | **Fallback**                                                        |
|----------------------------|-------------------------------------------|---------------------------------------------------------------------|
| Clean Colombia bag cut-out | No (product image is a text tile)         | Crop the bag from Big_Shoulders_Coffee_Hero.png; use the tile in S3 |
| Bag photos for S5          | No (tiles only)                           | Use the tiles as specimens                                          |
| Roastery photo             | Diego photo shows the roastery behind him | Use it as the clipped print                                         |
