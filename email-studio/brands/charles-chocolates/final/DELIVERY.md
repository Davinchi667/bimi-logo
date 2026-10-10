# Charles Chocolates · welcome-01 · DELIVERY

Spec welcome email for cold outreach, built from COPY.md and DESIGN_INTENT.md (10 Oct 2026): the Classic Collection opened with its key card, and the free bar handled as a measured thing on a $50 meter. 600 x 3643 px, 7 sections, 2 motion modules.

Files: `charles-chocolates_welcome-01.svg` (Figma-ready), `_600.png`, `_1200.png`, `gifs/M1_Box_key.gif`, `gifs/M2_Meter.gif`, `charles-chocolates_welcome-01_full.gif` (frame 1 = the static email, 1056 KB).

## Sections

| # | Section | y | height | pose |
|---|---|---|---|---|
| 1 | 01 Hero | 0 | 660 | chocolate brown; cream announcement bar with the offer sentence; cream logo; two-line Lora headline; sub; the open 10 piece box angled; a cream ribbon tag reading CLASSIC COLLECTION · FROM $31; teal CTA with the gold inner rule |
| 2 | 02 Box key | 660 | 662 | teal; the open 20 piece box cut out on the left; six gold leader lines from six pieces to a cream WHAT'S INSIDE key card (numbered fillings, the note, the sizes) (M1); teal CTA |
| 3 | 03 Free bar meter | 1322 | 440 | cream with grain; YOUR FREE CHOCOLATE BAR kicker; a 520 px meter with $0, 10 PIECE $31 and 20 PIECE $58 markers, a gold FREE BAR AT $50 flag and a wrapped bar sliding out (M2); the offer sentence with its term; the italic math line; SHOP THE 20 PIECE BOX |
| 4 | 04 Awards and press | 1762 | 393 | brown; two drawn gold rosette seals with the award names in type; three press quotes in italic serif columns with gold rules and outlet names |
| 5 | 05 Gift tags | 2155 | 660 | cream; serif headline; a black signature ribbon across; four kraft-and-cream gift tags hung on strings, two rows, different tilts; stars, caps titles, quotes, names; 'from 617 reviews' line |
| 6 | 06 Also in the shop | 2815 | 420 | split: black left with the Filled Skulls Trio and the John Kelly kicker; cream right with the Triple Chocolate Almonds; names, lines, prices, underlined caps text links |
| 7 | 07 Close | 3235 | 408 | teal; serif homepage line; inverted cream CTA; white footer with the logo, address and links |

## Motion spec (brief 12.1)

| ID | Section | What moves | Frame-1 state | Band | States & timing | Assets | Facts used | KB |
|---|---|---|---|---|---|---|---|---|
| M1 | 02 Box key | each numbered card line turns gold in turn with its leader line thickened while the others dim | all six leaders gold, all six lines at full strength | 600x544 at y=660 | 1600ms / 550ms / 550ms / 550ms / 550ms / 550ms / 550ms (7 states, loop 4900ms) | open 20 piece box cut-out | six fillings from the product description, sizes and prices from .js | 233 |
| M2 | 03 Free bar meter | the teal fill runs from $0 to the $31 marker to $50 (flag lights) and on to $58, where a wrapped bar slides out from under the flag | fill at $58, flag gold, bar out | 600x160 at y=1402 | 1600ms / 400ms / 400ms / 400ms (4 states, loop 2800ms) | a wrapped bar cut-out (not named as the free bar) | $31 and $58 from .js, $50 condition from the homepage | 57 |

Both loop forever at 3 to 8 held states, none under 120 ms. The M1 band carries the card text (so the lines can turn gold); the same six fillings also appear as live text in the SVG for Figma. M2's F5 is folded into the frame-1 hold.

## STOLEN FROM (structure only, from DESIGN_INTENT.md; the refs library is not on disk yet)

- Ghost 202933: callout diagram with leader lines from a product to labels (S2)
- ARMRA board-201241: a visual equation on a strong field with thin-rule frames (S3 meter, CTA inner rule)
- Olipop 202238: ground colour changing section by section with one product per section (S1 brown, S2 teal, S3 cream)
- Milk Bar 202904: checkerboard of photo and copy (S6 split)
- Last Crumb 202820: each item on its own paper label (S5 gift tags)

## Concept (one line)

The box key: the Classic Collection opened, six fillings keyed to six pieces with gold leaders, and the free bar shown as the $58 box clearing the $50 line.

## Copy changes

- None to the words. Layout: the brand's 10 piece photo is an open box (no closed-box photo exists), shown angled as the intent asks; the ribbon tag sits under the box's left side; leader lines point to six different pieces as a key style, numbers appear on the card only; S4 seals set 'San Francisco Magazine' on two lines; the press quotes keep the Tasting Table line whole.
- 'A wrapped bar' on the meter is the Dubai Done Better wrapped bar photo, used as a bar and never named as the free bar.

## Fonts

- Lora: Google Font, available in Figma (substitute for Georgia)
- Poppins: Google Font, available in Figma
- The intent asks for a Georgia-style serif; Lora stands in (Georgia is a system font Figma may not carry). Poppins is the site's body font and is on Google Fonts. The logo is the site's PNG with a cream knockout for dark grounds.

## Verify before sending

- Prices and availability (.js, 10 Oct 10:40 WAT): Classic Collection 10 piece $31.00, 20 piece $58.00; Filled Skulls Trio $55.00; Triple Chocolate Almonds $14.00.
- The offer wording is the homepage section's sentence with 'Non-cumulative.'; the site words the offer at least four ways (COPY.md problem 3). The brand must confirm how the bar is applied (code, automatic, packed) before a real send; that line goes under the meter.
- Awards and press quotes verbatim from the homepage; seals are drawn type, not publication logos.
- Reviews verbatim from Judge.me with the trims in COPY.md section 8; names as given (Anonymous, Christine Duffy, Pomponette, Darren Gibbs). 'from 617 reviews' as the homepage prints it; the 4.83 average is not used.
- Address from the brand's own cart email, not a site page: confirm.
- Images are the brand's own files cut out from white; the box key leaders are a styling device (the site does not say which piece holds which filling).

## Not done (needs the missing inputs)

- No comparison against refs/13-stars or the v6 set, no REF_INDEX pick (library not in the repo).
- No Figma import inspection (Starter plan MCP quota spent).
