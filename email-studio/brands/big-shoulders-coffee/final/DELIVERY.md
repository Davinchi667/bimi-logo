# Big Shoulders Coffee · welcome-01 · DELIVERY

Spec welcome email for cold outreach, built from COPY.md and DESIGN_INTENT.md (10 Oct 2026): the brand's own roast sheet for the Colombia, delivering the footer's 20% promise with Diego, the real reviews and three next bags. 600 x 3256 px, 6 sections, 3 motion modules.

Files: `big-shoulders-coffee_welcome-01.svg` (Figma-ready), `_600.png`, `_1200.png`, `gifs/M1_Ticker.gif`, `gifs/M2_Roast_sheet.gif`, `gifs/M3_Counter.gif`, `big-shoulders-coffee_welcome-01_full.gif` (frame 1 = the static email, 2118 KB).

## Sections

| # | Section | y | height | pose |
|---|---|---|---|---|
| 1 | 01 Hero | 0 | 480 | orange ticker strip (M1), bean-sack surface on black, white logo, drawn-star 4.77 line, 3-line heavy caps headline, sub, orange CTA, bag cut-out right bleeding 76 px into S2 |
| 2 | 02 The 20 percent | 480 | 280 | orange band, giant black 20%, footer lines + black CTA on the right |
| 3 | 03 Roast sheet | 760 | 923 | cream production sheet on black with binder clip, mono labels / Poppins values, ruled rows, Diego as a paper-clipped tilted print with caption, sliders + grind chips (M2), Colombia tile, CTA |
| 4 | 04 Reviews | 1683 | 651 | beans surface on black; 4.71 counter (M3) + five-row histogram left; cream strip with three stapled reviewer notes right |
| 5 | 05 Next bag | 2334 | 422 | paper-grain cream; black rule; three label tiles, underlined name links, price, notes |
| 6 | 06 Close | 2756 | 500 | beans surface on black; two-line caps headline, offer line, CTA; footer; giant white one-line logotype cropped at the bottom edge |

## Motion spec (brief 12.1)

| ID | Section | What moves | Frame-1 state | Band | States & timing | Assets | Facts used | KB |
|---|---|---|---|---|---|---|---|---|
| M1 | 01 Hero | strip slides left one sixth of the phrase loop per frame, seamless | phrases flush left, fully readable | 600x36 at y=0 | 400ms / 400ms / 400ms / 400ms / 400ms / 400ms (6 states, loop 2400ms) | none | three site lines | 26 |
| M2 | 03 Roast sheet | both drop markers slide in from the left and settle; the lit grind chip steps Whole Bean, Espresso, Automatic Drip, Pour Over | markers at the tile positions, Whole Bean lit | 600x176 at y=1205 | 1500ms / 300ms / 300ms / 600ms / 600ms / 600ms / 600ms (7 states, loop 4500ms) | Colombia tile slider positions | six grinds from the .js, slider positions measured on the tile | 70 |
| M3 | 04 Reviews | the 4.71 counts up from 0.00 through 2.35 and 4.10 | 4.71 (the real average) | 600x104 at y=1767 | 2000ms / 250ms / 250ms / 250ms (4 states, loop 2750ms) | none | 4.71 from 7 reviews, Judge.me | 45 |

All three loop forever (brief rule) at 3 to 8 held states, none under 120 ms. M3 is specified in the intent as non-looping; the loop version holds 4.71 for 2 s then re-counts, so frame 1 and the resting state are both the real 4.71. Ticker shift is one sixth of the phrase loop per frame (not a flat 100 px) so the loop is seamless.

## STOLEN FROM (structure only, from DESIGN_INTENT.md; the refs library is not on disk yet, so these were not re-opened)

- Liquid Death 202647: all-black canvas, left-aligned deadpan caps headline (S1, S6)
- David Protein 202046: monospace data rows, labels left / values right (S3 rows)
- Last Crumb 202817: giant boxed number as the story, thin bar chart (S2 20%, S4 histogram)
- Ghost 202933: product bleeding across a section edge (S1 bag into S2)
- Big Shoulders' own Colombia tile: the LIGHT ROAST / DARK ROAST and TRADITIONAL / INNOVATIVE sliders with the drop marker (S3, M2)
- ARMRA / Last Crumb footer: giant cropped wordmark (S6)

## Concept (one line)

This week's roast sheet: Diego's filled-in production log for the Colombia, with the proof (altitude, growers, grinds, the champion line, 4.71 from 7) written on the sheet itself.

## Copy changes

- None to the words. Layout-only departures from the spec: S1 headline set on three lines at 40 px (two lines at 54 px do not fit beside the bag at 600 px); S2 kicker broken as 'SIGN UP FOR SALES / & SPECIAL OFFERS'; sheet labels set at 14 px (brief minimum) instead of the intent's 11 px; S3 and S4 grew to hold the copy at legible sizes; S5 price moved under the name line.
- Slider markers sit at 34 % and 24 % of the line, measured on the brand's Colombia tile (the intent estimated 'about 45 % and 38 %').
- Separators in the ticker are drawn drops, not the middle-dot character.

## Fonts

- IBM Plex Mono: Google Font, available in Figma
- Poppins: Google Font, available in Figma
- The site's own heading face (Fatura_display, proprietary, seen in study/fonts.json) is not used: the copy brief specifies Poppins, which is the site's body and nav font and is on Google Fonts. IBM Plex Mono is the monospace for sheet labels and kickers (the intent suggested it).

## Verify before sending

- Prices: Colombia $26.00 (12oz) / $105.00 (5lb); Night Shift $24.00; 1848 $26.00; Ethiopia Natural $26.00 (products .js, 10 Oct 09:20 WAT).
- 4.77 (From 125+ reviews) on the homepage hero; the same page also prints 'Based on 262 reviews'. Only the hero line is used.
- 4.71 / 7 reviews and the histogram 86% (6) · 0 · 14% (1) · 0 · 0 on the Colombia page (Judge.me).
- Reviewer names as printed: LaCretia M., Terry &.T.C., Nataliia A.
- 'Diego Guartan' spelt as the site spells it. No trophy text used.
- No code is lettered anywhere: the brand must supply its real 20% code (then add the dashed YOUR CODE box under the 20%).
- Six grind variants and their order from the .js.
- All images are the brand's own files (hero composite bag panel cut out, Diego IMG_3881, the four label tiles, the Night Shift product photo as the dark surface, the hero's bean sacks as the S1 surface).

## Not done (needs the missing inputs)

- No comparison against refs/13-stars or the v6 set: the reference library is not in the repo. No REF_INDEX pick: the STOLEN FROM list comes from the design intent.
- No Figma import inspection: the Figma MCP quota on the Starter plan is spent; upload per tools/figma_import.md when it resets.
