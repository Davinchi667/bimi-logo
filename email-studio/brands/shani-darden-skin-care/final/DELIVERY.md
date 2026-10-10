# Shani Darden Skin Care · welcome-01 · DELIVERY

Spec welcome email for cold outreach, built from COPY.md and DESIGN_INTENT.md (10 Oct 2026): the home-care card an esthetician hands over, with Shani's first four weeks of Retinol Reform night by night. 600 x 3785 px, 7 sections, 2 motion modules (the optional M3 bottle turn was not built: no clean angled cut-out exists in B5).

Files: `shani-darden-skin-care_welcome-01.svg` (Figma-ready), `_600.png`, `_1200.png`, `gifs/M1_Nights_fill_in.gif`, `gifs/M2_Count_up.gif`, `shani-darden-skin-care_welcome-01_full.gif` (frame 1 = the static email, 917 KB).

## Sections

| # | Section | y | height | pose |
|---|---|---|---|---|
| 1 | 01 Hero | 0 | 620 | off-white with grain; shipping bar; black logo; violet kicker; centred two-line Playfair headline; sub; the bottle on a thin black rule; drawn 4.8 stars; caps rating line; black CTA |
| 2 | 02 Note from Shani | 620 | 306 | white; square greyscale portrait left; italic serif quote right; small caps sign-off |
| 3 | 03 Home-care card | 926 | 838 | slate; cream aftercare card: HOME CARE header rule, Shani's directions in italic, the M T W T F S S night grid (M1), 'Example schedule', the Then line, HOW TO APPLY, the caution, Libby K.'s handwritten margin note with 4 drawn stars, START WITH THE TRAVEL SIZE CTA; a travel bottle paper-clipped to the card corner |
| 4 | 04 Study row | 1764 | 330 | white; CLINICAL RESULTS kicker; four Playfair numbers with captions (M2); rule; the full study footnote |
| 5 | 05 Clients | 2094 | 841 | off-white; FAVORITE FEATURES rail with three slate bars; four torn-edge index-card notes of different heights with a slate left rule, stars, caps titles, quotes, names |
| 6 | 06 Routine | 2935 | 442 | slate; bottle and cream jar on a white shelf line; routine line; two-segment size toggle; three ruled perks with drawn checks; inverted CTA; subscription small print |
| 7 | 07 Close | 3377 | 408 | white; serif homepage paragraph; black CTA; footer with the logo, social line, copyright and unsubscribe |

## Motion spec (brief 12.1)

| ID | Section | What moves | Frame-1 state | Band | States & timing | Assets | Facts used | KB |
|---|---|---|---|---|---|---|---|---|
| M1 | 03 Home-care card | the retinol nights fill in week by week: empty grid, week 1, weeks 1 and 2, weeks 1 to 3, then all four | all four weeks filled (2, 3, 4, 5 nights) | 600x196 at y=1112 | 2200ms / 500ms / 500ms / 500ms / 1100ms (5 states, loop 4800ms) | none | Shani's directions line | 29 |
| M2 | 04 Study row | the four numbers count 0, half, then the printed values | 100% · 100% · 100% · 94% | 600x130 at y=1834 | 2400ms / 300ms / 300ms (3 states, loop 3000ms) | none | 2-week study on 39 subjects, product page | 50 |

Both loop forever at 3 to 8 held states, none under 120 ms. M2's F4 (same as F1) is folded into the frame-1 hold. The study footnote sits outside the M2 band as live text, always visible.

## STOLEN FROM (structure only, from DESIGN_INTENT.md; the refs library is not on disk yet)

- Lemme fav-200717: results timeline in rows (S3 week rows)
- Crown Affair board-201437: calm editorial bands with small caps labels (S3 card type, S5 rail)
- Last Crumb 202817: big % numbers with captions and the footnote under them (S4)
- David Protein STEAL_THIS 'mono stat rail': a thin stat rail beside content (S5)
- Manukora board-201601: quiet premium product on a single ground (S1, S6)

## Concept (one line)

The home-care card: Shani's own directions drawn as the aftercare card, four weeks of retinol nights filling in, with the trial numbers and the sensitive-skin reviews beneath it.

## Copy changes

- None to the words. Layout: the night grid labels the days M T W T F S S; the week rows carry the copy's night counts on the right; 'Example schedule' is set at 14 px (studio minimum) instead of 10; the S4 footnote at 14 px instead of 11; S3 grew to about 1,000 px to hold the card at legible sizes; S5 reviews stack as four torn notes beside the rail.
- Night placement is illustrative (labelled), per the copy's design note.

## Fonts

- Caveat: Google Font, available in Figma
- Inter: Google Font, available in Figma (substitute for Maison Neue)
- Playfair Display: Google Font, available in Figma (substitute for Didot Display)
- The site sets Didot / Didot Display and Maison Neue (both proprietary, study/fonts.json). Playfair Display stands in for Didot and Inter for Maison Neue; Caveat is the one handwriting face for the margin note. The logo is the site's SVG rasterised to PNG (its path data does not survive extraction).

## Verify before sending

- Prices and availability (.js, 10 Oct 09:50 WAT): Retinol Reform Full Size (30 ML) $75.00, Travel Size (10 ML) $30.00; Hydration Peptide Cream $60.00.
- Rated 4.8 out of 5 stars · 118 Reviews (homepage card and Okendo aggregate). Favorite Features tallies (Easy To Use 74, Gentle 60, Non-Irritating 46) from the Okendo aggregate, labelled as the widget's own.
- Quotes verbatim from Okendo with the trims in COPY.md section 8; names as given (Natty, alyssa f., Kelly B., Kathy M., Libby K. at 4 stars).
- Clinical numbers only with the full footnote in the same section. Caution line kept with the directions.
- Perks as printed: shipping bar, cart drawer ('Pick 2 Free Samples with any order'), product page subscribe line with its minimum-orders note.
- No discount or code anywhere. No street address: add the Klaviyo sender address before a real send.
- Images are the brand's own files: the product shot cut out, the portrait cropped and converted to greyscale, the cream jar cut out, the logo SVG.

## Not done (needs the missing inputs)

- No comparison against refs/13-stars or the v6 set, no REF_INDEX pick (library not in the repo).
- No Figma import inspection (Starter plan MCP quota spent).
