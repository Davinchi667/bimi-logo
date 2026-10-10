# evanhealy · welcome-01 · DELIVERY (built from a DRAFT copy brief)

Spec welcome email for cold outreach, built from COPY.md (marked DRAFT, not final-checked by the copy writer) and DESIGN_INTENT.md (10 Oct 2026): the oil & water protocol as a herbalist's lab sheet, the popup's own code on the two bottles it needs, and the Harvest Ritual priced against its parts. 600 x 4170 px, 6 sections, 3 motion modules.

Files: `evanhealy_welcome-01.svg` (Figma-ready), `_600.png`, `_1200.png`, `gifs/M1_Popup_replay.gif`, `gifs/M2_Press.gif`, `gifs/M3_Price_rail.gif`, `evanhealy_welcome-01_full.gif` (frame 1 = the static email, 1077 KB).

## Sections

| # | Section | y | height | pose |
|---|---|---|---|---|
| 1 | 01 Hero | 0 | 520 | warm paper with grain; shipping bar; black logo left; two-line Cormorant headline with a short sage rule; the site sentence; black CTA; the HydroSoul-and-copper-still photo right, cropped so the still runs off the edge |
| 2 | 02 Your code | 520 | 420 | sage; a white replay of the popup card (M1): the UNLOCK line dimmed, the code sentence, a dashed YOUR CODE box with SEEKER15 as live mono text; the exclusion line; centred CTA |
| 3 | 03 Lab sheet | 940 | 832 | paper with an 8 px grid; PROTOCOL NO. 1 · OIL & WATER header strip with a sheet number; three numbered steps on a copper tubing line; a line-drawn palm (M2) labelled mist · mix · press; the serum photo framed and the HydroSoul bottle cut out with handwritten labels, leader lines and mono prices; mono sum and math lines; CTA |
| 4 | 04 Notes in the margin | 1772 | 1138 | paper; serif headline; a sage stem with leaf sprigs; four pinned specimen labels staggered left and right, each with stars, a caps title, its product in sage caps, the quote and the verified name; mono ratings line |
| 5 | 05 Harvest Ritual | 2910 | 740 | deep green; kicker; italic line; the five-product set cut out left; a mono price rail with sizes, the struck $187.46 and $135 large in Cormorant (M3); drawn 4.8 stars and the 557 line; the exclusion small print; cream CTA |
| 6 | 06 Regenerative | 3650 | 520 | paper; a drawn ROC seal in sage type (two arcs, ROC, BEAUTY BRAND); the ROC paragraph; sage rule; The Garden line in serif; black CTA; white footer with the logo, phone, links, shipping and returns, copyright, unsubscribe |

## Motion spec (brief 12.1)

| ID | Section | What moves | Frame-1 state | Band | States & timing | Assets | Facts used | KB |
|---|---|---|---|---|---|---|---|---|
| M1 | 02 Your code | the brand's popup replays: the UNLOCK view with an email field, the GET MY 15% OFF CODE button pressed, then the code view; the code itself stays live text outside the band | the code view with the dashed YOUR CODE box | 600x232 at y=556 | 2800ms / 600ms / 600ms (3 states, loop 4000ms) | none | Klaviyo popup V37uH9 wording | 27 |
| M2 | 03 Lab sheet | an empty palm, mist droplets land, one amber serum drop lands beside them, they swirl together, then rest as a golden sheen | oil and mist merged into a soft golden sheen in the palm | 600x176 at y=1104 | 1400ms / 500ms / 500ms / 500ms / 700ms (5 states, loop 3600ms) | none | directions verbatim beside it | 23 |
| M3 | 05 Harvest Ritual | five lines only, then the $187.46 total appears, then the strike draws across it and $135 rises in | five lines, $187.46 struck, $135 large | 600x372 at y=3070 | 1600ms / 400ms / 400ms / 1100ms (4 states, loop 3500ms) | none | five .js prices, compare-at 18746 and price 13500 | 103 |

All three loop forever at 3 to 8 held states, none under 120 ms. The code SEEKER15 is live text under the M1 band, never baked into the GIF. M1's F4 and M3's final frame are folded into the frame-1 holds.

## STOLEN FROM (structure only, from DESIGN_INTENT.md; the refs library is not on disk yet)

- Alice Mushrooms fav-195808: labels floating around a product with fine lines (S3 bottle labels)
- Ghost 202933: callout diagram with leader lines (S3 steps on the tubing line)
- Lemme fav-200717: numbered step rows (S3)
- Crown Affair board-201437: quiet editorial serif on warm paper (S1, S6)
- David Protein STEAL_THIS 'monospace stat rail': mono rail beside the product (S5)

## Concept (one line)

The oil & water lab sheet: Protocol No. 1 (mist, mix, press) in the brand's own words on a herbalist's notebook page, with the two bottles labelled, the sum done, and the customers' notes pinned as specimens.

## Copy changes

- None to the words. Layout: the hero uses the brand's still photo in a frame rather than a cut-out (the cut-out carries a halo); the serum sits in a framed photo on the sheet and the HydroSoul as a cut-out; the ritual rail puts each size on its own line under the product name; the ROC seal text is split into two arcs with ROC and BEAUTY BRAND inside; S3 and S4 grew to about 700 px each to hold the steps, labels and four quotes legibly.
- 'mist · mix · press' under the palm is the copy's own step labels (which the copy marks as ours).

## Fonts

- Caveat: Google Font, available in Figma
- Cormorant Garamond: Google Font, available in Figma (substitute for Cochin)
- IBM Plex Mono: Google Font, available in Figma
- Montserrat: Google Font, available in Figma (substitute for proxima-nova)
- The site's Cochin and proxima-nova are proprietary; Cormorant Garamond and Montserrat stand in. IBM Plex Mono for the sum line, rail and header number; Caveat for the bottle labels and the palm caption. The logo is the site's SVG rasterised.

## Verify before sending

- DRAFT BRIEF: the copy writer stopped before final checks. Every fact below was taken from COPY.md as written; re-run the copy's own rule check before this goes out.
- Prices and availability (.js, 10 Oct 09:44 WAT): Pomegranate Vitality Serum 0.5 fl oz $48.99; Rose Geranium HydroSoul 4 fl oz $31.99 / 1 fl oz $10.99; Harvest Ritual $135.00, compare-at $187.46 (equals the five full sizes: $38.99 + $31.99 + $48.99 + $38.99 + $28.50).
- SEEKER15 is the popup's own public code (Klaviyo form V37uH9); whether it is still accepted at checkout was not tested. The ritual exclusion line is printed beside the code and under the ritual.
- 'With SEEKER15: $68.83' and '$80.98' are our arithmetic, labelled.
- Reviews verbatim from Okendo with the trims in COPY.md section 8; names as given (Gloria P., Pam F., Dana H., Maxine S.), each labelled with its product. Ratings 4.8 / 153 and 4.92 / 147 from the Okendo aggregates; 4.8 / 557 as the ritual page prints it (a group of five products).
- The footer form on the live site promises no 15% (COPY.md problem 2); only the popup does.
- No official ROC logo: the seal is drawn type. Images are the brand's own files.

## Not done (needs the missing inputs)

- No comparison against refs/13-stars or the v6 set, no REF_INDEX pick (library not in the repo).
- No Figma import inspection (Starter plan MCP quota spent).
