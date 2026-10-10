# Pure Inventions · welcome-01 + popup P0 · DELIVERY

Spec welcome email for cold outreach plus the signup popup the site lacks, built from COPY.md and DESIGN_INTENT.md (10 Oct 2026): the spa water station card for the guest who first tasted the drops at a spa. Email 600 x 4088 px, 6 sections, 2 motion modules; popup 600 x 580 px, 1 motion module.

Files: `pure-inventions_welcome-01.svg` (Figma-ready), `_600.png`, `_1200.png`, `gifs/M2_Ounce_counter.gif`, `gifs/M3_First_drop.gif`, `pure-inventions_welcome-01_full.gif` (frame 1 = the static email, 1082 KB); popup in `final/popup/`: `pure-inventions_popup-P0.svg`, `_600.png`, `_1200.png`, `gifs/M1_Popup_chips.gif`, `pure-inventions_popup-P0_full.gif`.

## Sections

| # | Section | y | height | pose |
|---|---|---|---|---|
| 1 | 01 Hero | 0 | 470 | white logo bar; cream-to-blue wash with grain; two-line Lora headline; the spa line; pill CTA; a drawn glass of water with the Coconut bottle in front, cut by the edge; a round carafe tag on a string with the product page's spa phrase |
| 2 | 02 Spa water card | 470 | 764 | soft blue field; cream folded tent card: TODAY'S WATER, four flavours as a menu with dotted leaders, small bottle cut-outs, servings and prices, the NEW tag for Mango, the italic card foot, a green two-arc stamp; SHOP ALL FLAVORS pill |
| 3 | 03 Ounce counter | 1234 | 470 | deep blue; outlined bottle filling (M2) beside the 96 OZ counter with 12 OZ struck; ALINE N.'s line; mono value row and the math line |
| 4 | 04 Route | 1704 | 1360 | cream; headline; a dotted route with blue drop pins, four review tags of different widths staggered left and right; the Coconut bottle at the route end; pill CTA |
| 5 | 05 First drop | 3064 | 520 | white; small caps label; dropper over a drawn glass (M3 tints the water), Coconut bottle beside it; four flavour swatches with the selected one ringed; the site line; pill CTA |
| 6 | 06 Founders | 3584 | 504 | pale blue; promise kicker, the founders' sentence, the italic promise, Lynne and Lori; left-aligned pill; white footer with the colour logo, address, phone, email, socials, shipping line, unsubscribe |
| P0 | Popup (separate frame) | 0 | 580 | 40% black scrim over the blurred homepage; 480 px white card; tilted Coconut bottle with a dropper and one drop; kicker, Lora question, 'I want to...', four outline chips (chip 1 filled), email field, pill button, 'Free Shipping Over $50. No thanks' |

## Motion spec (brief 12.1)

| ID | Section | What moves | Frame-1 state | Band | States & timing | Assets | Facts used | KB |
|---|---|---|---|---|---|---|---|---|
| M2 | 03 Ounce counter | the outlined bottle fills from an eighth to half to three quarters to full while the number reads 12, 48, 72 then 96 OZ with 12 OZ struck through | bottle full, 96 OZ, 12 OZ struck above | 600x280 at y=1284 | 2800ms / 400ms / 400ms / 400ms (4 states, loop 4000ms) | none | ALINE N. review line | 136 |
| M3 | 05 First drop | a drop falls and the water tints to each flavour in turn while the matching swatch is ringed | clear water, Coconut swatch ringed, bottle beside the glass | 600x360 at y=3084 | 900ms / 900ms / 900ms / 900ms (4 states, loop 3600ms) | Coconut bottle cut-out | four flavours on sale | 102 |
| M1 | P0 Popup | all four chips go to outline with no email field, a cursor taps chip 1 which fills blue, then the email field and button return | chip 1 filled, email field and button visible | 600x510 at y=60 (popup frame) | 2800ms / 600ms / 600ms (3 states, loop 4000ms) | Coconut bottle cut-out | four homepage picker lines | 61 |

All loop forever at 3 to 8 held states, none under 120 ms. M2's F5 (same as F1) is folded into the frame-1 hold; the popup's F4 likewise. The quote, name and value row sit outside the M2 band as the intent asks.

## STOLEN FROM (structure only, from DESIGN_INTENT.md; the refs library is not on disk yet)

- Last Crumb 202817: giant boxed number with a small caption (S3 96 OZ with the struck 12 OZ)
- Olipop 202238: one product on a field coloured to its flavour, grounds changing section by section (S1, S5 tints)
- Poppi 202335: flavour swatch row with a selector moving across it (S5)
- Grüns 204911: callouts pinned to points with small markers (S4 drops along the route)
- Fungies STEAL_THIS 'in-email quiz': a question with tappable options (P0 chips)

## Concept (one line)

The spa water station card: TODAY'S WATER as the tent card beside a spa dispenser, with the four real flavours, their prices, the nutritionists' stamp, and the reviews laid along the path from the spa to the reader's kitchen.

## Copy changes

- None to the words. Layout: S2 menu puts servings and price on the description line when a flavour name is too long for one row (Electrolytes + Vitamin C Watermelon); the stamp text is split across a top and bottom arc; the review tags' titles wrap where needed; S4 grew to about 1,100 px and the email to about 4,090 px to hold four full quotes and the route legibly.
- Flavour tints in S5 are sampled from the bottle labels; the Coconut glass stays clear as the copy says.

## Fonts

- Lora: Google Font, available in Figma
- Roboto: Google Font, available in Figma
- Roboto Mono: Google Font, available in Figma
- The site body is Roboto (site CSS) and the intent asks for a soft serif display; Lora and Roboto Mono are both on Google Fonts. The live site's headings compute to Noto Sans (study/fonts.json); the brief's serif choice is kept for the spa-card feel.

## Verify before sending

- Prices and availability (.js, 10 Oct 09:25 WAT): Coconut Water 30 servings $24.99; Electrolytes + Vitamin C Watermelon 30 servings $24.99; Cranberry + Elderberry 60 servings $35.99; Mango Coconut Water 30 servings $24.99.
- Review counts and quotes from the Stamped widget API (Coconut Water 205); quotes verbatim with the trims listed in COPY.md section 8; names as given (Amy T., Maria L., Marie, Madison S., ALINE N.).
- OFFER LINES ON THE LIVE SITE: the copy states the site has no offer, but the studio's scrape today shows an announcement 'Fall in Love with Fall - Buy 2 or More Bottles, Get 20% Off / Use Code: FALL' on the homepage and 'Enjoy 15% off your first order!' in the cart drawer / newsletter block on inner pages. Neither is used in the email or popup per the brief; re-check before sending and decide whether the popup should carry the 15%.
- 'About 83 cents a glass' is our math ($24.99 / 30), labelled as such.
- Images are the brand's own product PNGs (already transparent), the colour logo, and a blurred crop of the live homepage behind the popup.

## Not done (needs the missing inputs)

- No comparison against refs/13-stars or the v6 set, no REF_INDEX pick (library not in the repo).
- No Figma import inspection (Starter plan MCP quota spent).
