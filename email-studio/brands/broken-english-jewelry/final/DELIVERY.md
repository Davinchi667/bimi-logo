# Broken English Jewelry · welcome-01 · DELIVERY

Spec welcome email for cold outreach, built from COPY.md and DESIGN_INTENT.md (10 Oct 2026): the 10% and its $250 condition pointed at The Ear Edit, drawn as an ear map with five real singles and a running total. 600 x 3456 px, 7 sections, 3 motion modules.

Files: `broken-english-jewelry_welcome-01.svg` (Figma-ready), `_600.png`, `_1200.png`, `gifs/M1_Designer_ticker.gif`, `gifs/M2_Ear_map_build.gif`, `gifs/M3_Chat.gif`, `broken-english-jewelry_welcome-01_full.gif` (frame 1 = the static email, 1234 KB).

## Sections

| # | Section | y | height | pose |
|---|---|---|---|---|
| 1 | 01 Hero | 0 | 490 | warm white with paper grain; gold-tan announcement bar with sand rule; black logotype centred; sand designer ticker strip (M1); kicker, two-line Halant headline, sub, gold offer line with the $250 condition, black CTA; the huggie cut-out large, cropped by the right edge |
| 2 | 02 The ten percent | 490 | 270 | sand band; giant Halant 10%; the popup's lines, the asterisk terms in grey, the shipping line |
| 3 | 03 Ear map | 760 | 1196 | off-white with grain; line-drawn ear; five numbered pins on gold leaders to cut-outs with designer, name, metals, price; receipt-style running total with the $250 tick (M2); small print; CTA |
| 4 | 04 Laura | 1956 | 369 | white between hairline sand rules; both Laura quotes in Halant, gold-tan attribution; thin right rail with the two facts |
| 5 | 05 Client Care | 2325 | 330 | sand; EXPERT ADVICE kicker; chat thread: grey question bubble, typing dots, white reply bubble (M3); underlined mailto link |
| 6 | 06 Lauras Picks | 2655 | 395 | white; three cut-outs with no borders, designer small caps, Halant names, prices |
| 7 | 07 Close | 3050 | 406 | white serif close line, gold offer line with the condition, centred CTA; sand footer with the black logotype, contact and social line, unsubscribe |

## Motion spec (brief 12.1)

| ID | Section | What moves | Frame-1 state | Band | States & timing | Assets | Facts used | KB |
|---|---|---|---|---|---|---|---|---|
| M1 | 01 Hero | the designer names slide left one sixth of the loop per frame, seamless | TROUVER · FIAMETTA · LIZZIE MANDLER lead, readable from the left | 600x32 at y=104 | 450ms / 450ms / 450ms / 450ms / 450ms / 450ms (6 states, loop 2700ms) | none | designer names from the Designers menu and product vendors | 21 |
| M2 | 03 Ear map | the ear outline stays; pins, leaders and cut-outs land one by one while the receipt adds each price and ticks the $250 line with the first piece | all five pins on, total $2,540.00, $250 ticked | 600x847 at y=910 | 3000ms / 600ms / 700ms / 700ms / 700ms / 700ms (6 states, loop 6400ms) | five product cut-outs | five .js prices, Sold as a single, $250 offer condition | 314 |
| M3 | 05 Client Care | the question shows alone, typing dots appear, then the Client Care reply bubble lands | both bubbles visible | 600x184 at y=2391 | 3600ms / 600ms / 800ms (3 states, loop 5000ms) | none | about page Client Care line | 45 |

All three loop forever at 3 to 8 held states, none under 120 ms. M2's F7 (same as F1) is folded into the frame-1 hold; the labels stay printed in every frame as the intent asks, only pins, leaders, cut-outs and the receipt change.

## STOLEN FROM (structure only, from DESIGN_INTENT.md; the refs library is not on disk yet)

- Alice Mushrooms board-201509: labels floating around one central object (S3 pins around the ear)
- Ghost 202933: leader lines from the object to the callouts; product cropped by the edge (S3 leaders, S1 huggie)
- Fungies board-201234: a module that looks like an in-email tool (S3 running total)
- Alani Nu 202754: message bubbles as content (S5)
- Liquid Death 202647: hairline rules framing short left-aligned lines (S4, S7)

## Concept (one line)

The ear map: one line-drawn ear, five real singles pinned to it with their live prices, and a receipt that passes the $250 condition with the first piece.

## Copy changes

- None to the words. Layout: the asterisk terms in S2 are set at 14 px (studio minimum) instead of 12; the running total sits under the ear rather than top right so the five label rows have room; the pin-row order runs top to bottom from upper helix to lobe so no leader crosses another; receipt rows read 'PIN n · PLACE' with the piece price and the cumulative total below, which carries the copy's running-total figures.
- Pin placements are styling positions, not product claims; the ear is a drawn sketch, no model photography.

## Fonts

- Halant: Google Font, available in Figma (substitute for Frutiger Serif)
- Open Sans: Google Font, available in Figma
- The brief names Frutiger Serif (proprietary) from the site CSS; the live site actually renders its headings in Halant (study/fonts.json), which is on Google Fonts and is used here for display and quotes. Open Sans is the site's body font and is on Google Fonts.

## Verify before sending

- Prices and availability (.js, 10 Oct 10:50 WAT): Half Paved Huggie 9.5mm $590.00; Emerald Cut Mini Stud $550.00; Emerald Knife Edge Bar Stud $400.00; Diamond White Pierrot $430.00; Bow Ear Cuff $570.00; Twister Maxi $440.00; Gummy Pendant $240.00 (under the $250 minimum on its own; kept away from the offer line).
- The running total ($2,540.00) is our sum of listed prices, labelled by the small print.
- OFFER WORDING: the copy quotes the popup as 'GET 10% OFF* / Sign up for our newsletter to receive a discount code for first time customers. / Offer valid for orders $250 or more. / Some exclusions may apply...'. The studio's scrape today captured a popup reading 'JOIN US / Enjoy 10% OFF / Subscribe to get special offers, free giveaways, and once-in-a-lifetime deals. Save 10% OFF your next order over $250. Exclusions apply.' Re-check which popup is live before sending; the $250 condition is the same in both.
- No reviews exist on the site and none are used. No code is lettered (brand to supply; then add the gold-bordered YOUR CODE box in S2).
- Shipping line only as the announcement bar words it. Designer names as the Designers menu / product vendors.
- Images are the brand's own product photos cut out from white, and the black logotype file.

## Not done (needs the missing inputs)

- No comparison against refs/13-stars or the v6 set, no REF_INDEX pick (library not in the repo).
- No Figma import inspection (Starter plan MCP quota spent).
