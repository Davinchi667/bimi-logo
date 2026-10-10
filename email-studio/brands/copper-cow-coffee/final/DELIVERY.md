# Copper Cow Coffee · welcome-01 · DELIVERY

Spec welcome email for cold outreach, built from COPY.md and DESIGN_INTENT.md (10 Oct 2026): the brand's own brew card drawn as a 90-second stopwatch, delivering the footer's 15% on the Classic Black with the Okendo proof and Debbie's lines. 600 x 3425 px, 6 sections, 3 motion modules.

Files: `copper-cow-coffee_welcome-01.svg` (Figma-ready), `_600.png`, `_1200.png`, `gifs/M1_Marquee.gif`, `gifs/M2_Brew_clock.gif`, `gifs/M3_Counter.gif`, `copper-cow-coffee_welcome-01_full.gif` (frame 1 = the static email, 2534 KB).

## Sections

| # | Section | y | height | pose |
|---|---|---|---|---|
| 1 | 01 Hero | 0 | 520 | paper-grain cream, pink cow spots with speckle bleeding from the right, green logo, kicker, two-line Fredoka headline, sub, drawn-star 5.0 line, green pill CTA, box + pouch + mug cut-out breaking the bottom edge; green marquee strip at the foot (M1) |
| 2 | 02 The 15 percent | 520 | 310 | green band with lime wave top edge, cream scalloped coupon ticket (15% off stub, footer line, FAQ shipping line), inverted cream pill |
| 3 | 03 Brew clock | 830 | 867 | cream; 100-second stopwatch face with crown, four HowTo photo circles at 0, 10, 30 and 90 s, sweeping hand (M2), leader-line callouts with the bracketed site lines, strength rail from a 3 oz mug to a 12 oz glass, the four brew steps, CTA |
| 4 | 04 Brewers | 1697 | 678 | pink speckled field; green slab with the 29 / 100% counter (M3) and the Okendo lines; four reviews as pour-over filter tags hung by threads from two green lines at different heights |
| 5 | 05 Debbie and the farmers | 2375 | 416 | green; lime rule; kicker, headline, two site paragraphs; the woman-owned badge (with Debbie's photo) right |
| 6 | 06 Next box and close | 2791 | 634 | cream; three products cut out on green / lime / pink blocks with name, price and arrow links; CTA; green footer with cream logo |

## Motion spec (brief 12.1)

| ID | Section | What moves | Frame-1 state | Band | States & timing | Assets | Facts used | KB |
|---|---|---|---|---|---|---|---|---|
| M1 | 01 Hero | the brand's own value marquee slides left one sixth of its loop per frame, seamless | CLIMATE RESILIENT leads, readable from the left edge | 600x40 at y=480 | 400ms / 400ms / 400ms / 400ms / 400ms / 400ms (6 states, loop 2400ms) | none | six homepage marquee phrases | 38 |
| M2 | 03 Brew clock | the hand sweeps 0, 10, 30, 60 then rests at 90; each step photo lights as the hand passes; a wait-30-sec tag at 30; the pink fill rises in the rail mug at 60 | hand at 90, all four photos lit, centre reads 90 SECONDS | 600x450 at y=966 | 2600ms / 500ms / 500ms / 700ms / 700ms (5 states, loop 5000ms) | four HowTo photo crops | brew steps verbatim, Ready in 90 seconds, two bracketed site lines | 193 |
| M3 | 04 Brewers | 29 counts 0, 9, 21, 29 while 100% counts 0, 40, 80, 100 | 29 REVIEWS · 100% would recommend | 600x60 at y=1781 | 2000ms / 250ms / 250ms / 250ms (4 states, loop 2750ms) | none | Okendo: 29 reviews, 100% would recommend this product | 14 |

All three loop forever at 3 to 8 held states, none under 120 ms. The intent's M2 F6 (same as F1) is folded into the frame-1 hold; M3 is a loop (holds 29 / 100% for 2 s, then re-counts). The dial is a 100-second face so 0 s and 90 s do not share a mark; only 'wait 30 sec' and 'Ready in 90 seconds' are claims, the 10 s and 90 s marks are photo placements as the intent says.

## STOLEN FROM (structure only, from DESIGN_INTENT.md; the refs library is not on disk yet)

- Ghost 202933: product breaking the section edge; leader-line callouts around one object (S1, S3)
- Magic Spoon 201757: wavy pastel section edge (S2 lime wave)
- Olipop 202237: each product on its own colour block (S6)
- ARMRA board-201241: dashed coupon chip (S2 ticket)
- Copper Cow's own HowTo graphic: four circular step photos with hand-lettered labels (S3 dial)

## Concept (one line)

The 90-second brew clock: the brand's brew card drawn as a stopwatch, with the four HowTo photos on the dial, the strength rail under it and the reviews hung like filters on a mug rim.

## Copy changes

- None to the words. 'Tear / Hang / Pour / Enjoy!' and the second counts on the dial are the brand's HowTo labels and placements. The ellipsis in 'cup…anytime' and the en dash in '3–12' are kept as the site writes them. 'Mu go to' and 'dee B.' kept as written. Cheryl's double spaces collapsed (per COPY.md section 8).
- Layout departures from the spec: S1 headline at 44 px on two lines; S3 grew to about 820 px and S4 to about 650 px so the dial, rail, steps and four quotes stay legible; '15% off' set as a stub ('15%' over 'off') on the ticket.

## Fonts

- Fredoka: Google Font, available in Figma (substitute for NaNJaune)
- Poppins: Google Font, available in Figma
- The live site sets headings in NaNJaune (proprietary, chunky rounded) and body in Rebond-Grotesque (study/fonts.json). The copy brief names Poppins, which is in the site's CSS and on Google Fonts, so Poppins carries everything except the S1 headline and the '15%' stub, where Fredoka stands in for NaNJaune as the intent allows.

## Verify before sending

- Classic Black 8ct $16.00 available; Snickerdoodle 8ct $16.00; Mystery Latte Bundle 10ct $15.00; Vanilla Creamer 24ct $22.00 (.js / products.json, 10 Oct 09:50 WAT).
- Okendo on the Classic Black page: Rated 5.0 out of 5 stars, 29 Reviews, 100% would recommend this product. Note a 4-star review about shipping exists (Jennifer R.) and is not in the email.
- Reviewer names as printed: Natalie D., Cheryl P., dee B., Kara M.; all four marked VERIFIED BUYER by the widget.
- Free-shipping line only from /pages/promotions; the $30 threshold is after discount.
- No code is lettered: the brand must supply its 15% code (then add the dashed YOUR CODE box on the ticket).
- Marquee phrases from the homepage; 'Women and AAPI owned', Debbie line and 2X line from the homepage.
- Images are the brand's own files: ClassicHero_1 cut out, the HowTo grid cropped, womanOwned badge, the three product graphics cut out, newlogo files.

## Not done (needs the missing inputs)

- No comparison against refs/13-stars or the v6 set, no REF_INDEX pick (library not in the repo).
- No Figma import inspection (Starter plan MCP quota spent).
