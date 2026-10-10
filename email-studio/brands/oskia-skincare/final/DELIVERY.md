# OSKIA · welcome-01 · DELIVERY

Spec welcome email for cold outreach, built from COPY.md and DESIGN_INTENT.md (10 Oct 2026): Midnight Elixir read as a skin nutrition facts label, with the £10 and the travel-size Super-R as the reason to start. UK spelling. 600 x 3497 px, 6 sections, 3 motion modules.

Files: `oskia-skincare_welcome-01.svg` (Figma-ready), `_600.png`, `_1200.png`, `gifs/M1_Night_to_morning.gif`, `gifs/M2_Results_bars.gif`, `gifs/M3_Histogram.gif`, `oskia-skincare_welcome-01_full.gif` (frame 1 = the static email, 1157 KB).

## Sections

| # | Section | y | height | pose |
|---|---|---|---|---|
| 1 | 01 Hero | 0 | 520 | the brand's own night scene (bottle in moss, moths, starry sky) with a legibility shade on the left; announcement bar; kicker; three-line Suranna headline; sub; drawn stars + proof lines; white CTA. M1 lifts the scene from night to morning |
| 2 | 02 Ten pounds off | 520 | 300 | white with slate hairlines; giant cobalt £10 in Suranna; kicker, serif headline, the footer line and the gift line; Super-R jar small; near-black CTA centred |
| 3 | 03 Nutrition facts | 820 | 1063 | slate field; white-ruled NUTRITIONAL FACTS label with thick title rule, serving line, five actives rows with bold lead phrases, RESULTS AFTER 8 WEEKS bars (M2), the trial footnote printed on the label; small bottle leaning on the label's corner; inverted CTA |
| 4 | 04 Georgie | 1883 | 400 | white with a slate side rail carrying the two facts; big cobalt open quote; Suranna quote; founder line in Montserrat caps |
| 5 | 05 Reviews | 2283 | 766 | cobalt with the brand's drip photo as a faint surface; 4.8 in Suranna, 196 Reviews, five-row histogram (M3), the 91% line; ruled list of four reviews with mono age tags, drawn stars, caps titles |
| 6 | 06 Close | 3049 | 448 | white close line in Suranna + offer line + CTA; near-black footer with the vector OSKIA logo, awards line, socials, unsubscribe |

## Motion spec (brief 12.1)

| ID | Section | What moves | Frame-1 state | Band | States & timing | Assets | Facts used | KB |
|---|---|---|---|---|---|---|---|---|
| M1 | 01 Hero | the sky lifts from night through navy and dawn grey to morning; bottle and type stay put, type turns near-black on the morning frame | night: the brand's starry sky, white type, white CTA | 600x520 at y=0 | 2500ms / 600ms / 600ms / 2000ms (4 states, loop 5700ms) | brand night scene photo (bottle in moss, moths) | Marie Claire line, 4.8 / 196 / 91% | 376 |
| M2 | 03 Nutrition facts | the eight result bars fill from zero to half to their printed values (first three on a 0 to 50 scale, the five felt rows on 0 to 100) | all bars at their printed values | 600x332 at y=1336 | 3300ms / 300ms / 300ms (3 states, loop 3900ms) | none | clinical block with footnote, five consumer lines | 19 |
| M3 | 05 Reviews | the five star-count bars fill from zero to half to 162 / 24 / 6 / 3 / 1 | bars at the Bazaarvoice counts | 600x116 at y=2489 | 2500ms / 300ms / 300ms (3 states, loop 3100ms) | none | snapshot 162/24/6/3/1 of 196 | 28 |

All three loop forever at 3 to 8 held states, none under 120 ms. M1 bakes the type into every frame (the intent's live-text option is not possible in a GIF); the morning frame switches the type and CTA to near-black for legibility. M2's F4 (same as F1) is folded into the frame-1 hold. M3 loops (holds the counts, then refills).

## STOLEN FROM (structure only, from DESIGN_INTENT.md; the refs library is not on disk yet)

- Last Crumb 202817: survey stats as horizontal bars with the numbers printed (S3 results, S5 histogram)
- Lemme fav-200717: big % results with the study footnote directly underneath (S3 footnote on the label)
- Peace Out fav-195802: small kicker over a giant promise (S1)
- David Protein 202046: mono data tags in ruled rows on dark (S5 age tags)
- OSKIA's own NUTRITIONAL FACTS panel: slate label, white rules (S3). Note: the panel URL in COPY.md section 9 now serves the brand's night-scene image, not the panel; the label is drawn from the brief's description and the scene photo is used for the hero.

## Concept (one line)

The skin nutrition facts label: Midnight Elixir's actives and its 8-week trial printed as the back-of-pack panel OSKIA already uses, footnote included, with 196 reviews as a ruled lab list.

## Copy changes

- None to the words. Layout: S1 headline on three lines at 44 px (two lines do not clear the bottle); the trial footnote is set at 14 px (the studio's minimum text size) rather than the intent's 10 px; S3 bars sit under their lines rather than beside them so the labels never run under a bar; S3 grew to about 1,000 px and S5 to about 700 px to hold the label and four quotes legibly.
- The hero uses the brand's own night photograph (which the brief's panel URL serves) instead of a drawn gradient; the scene already contains the bottle, so no separate cut-out sits in S1. The award text on that image is cropped out and not used.

## Fonts

- IBM Plex Mono: Google Font, available in Figma
- Montserrat: Google Font, available in Figma
- Suranna: Google Font, available in Figma
- Suranna and Montserrat are the site's own CSS fonts and both are on Google Fonts, so no substitute is needed. IBM Plex Mono only for the S5 age tags. The OSKIA logo is embedded as vector paths from the site's new_logo.svg.

## Verify before sending

- Midnight Elixir £165.00 (50ml) / £60.00 (15ml), both available (midnight-elixir.js, 10 Oct 10:10 WAT).
- Bazaarvoice on the product page: 4.8 / 196 Reviews; 162 / 24 / 6 / 3 / 1; 121 out of 133 (91%) recommend. Names and age bands as the widget shows them (Emma M, Monika, Roma25 Scotland, Adele London). Roma25's 'Only downside is price' is trimmed per COPY.md section 8; restore if David prefers.
- Clinical block and its footnote verbatim from the product page; the page's separate '32%' line is not used anywhere.
- ANNOUNCEMENT BAR: the copy's line 'Enjoy a complimentary travel-size Super-R with every order' was read on 10 Oct 10:12 WAT, but the studio's scrape later the same day shows the bar reading 'Choose 3 Samples With All Orders'. Re-check the live bar before sending; if the Super-R gift has ended, S1 bar, S2 second line, the preview and the S6 line all change.
- No code is lettered: OSKIA must supply the £10 code (then add the YOUR CODE box under the £10). No shipping threshold used (the site shows two).
- Marie Claire line and the 250 awards / B Corp lines as printed on the product and about pages.
- Images are the brand's own files: night scene, Midnight-Elixir-shadow cut out, super-r-shadow cut out, the drip photo as a surface, new_logo.svg.

## Not done (needs the missing inputs)

- No comparison against refs/13-stars or the v6 set, no REF_INDEX pick (library not in the repo).
- No Figma import inspection (Starter plan MCP quota spent).
