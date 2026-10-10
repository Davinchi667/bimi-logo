# Musee Bath · welcome-01 · DELIVERY

Spec welcome email for cold outreach, built from COPY.md and DESIGN_INTENT.md (10 Oct 2026): the pastry chef's recipe card for one Dreamweaver bath, then the bakery case of what is in stock today. 600 x 4018 px, 6 sections plus the ticker band, 2 motion modules.

Files: `musee-bath_welcome-01.svg` (Figma-ready), `_600.png`, `_1200.png`, `gifs/M1_Fizz.gif`, `gifs/M2_Ticker.gif`, `musee-bath_welcome-01_full.gif` (frame 1 = the static email, 1087 KB).

## Sections

| # | Section | y | height | pose |
|---|---|---|---|---|
| 1 | 01 Hero | 0 | 640 | light pink with grain; shipping bar; black logo; two-line Cormorant headline; sub; the Dreamweaver balm cut out on a drawn white cake stand; hot-pink luggage-style price tag on a string; black pill CTA; white doily scallop into S2 |
| 2 | 02 Recipe card | 640 | 786 | cream with the brand's lavender ingredient photo as a faint texture; a rotated ruled recipe card with a pink header: Makes, Ingredients, Method and the chef's note (handwriting face for the recipe lines), the drawn tub with the fizzing balm (M1), two 5-star margin notes, the low-stock corner tag, the full ingredient list at the foot; SHOP DREAMWEAVER · $12 pill |
| 3 | 03 Story | 1426 | 374 | white; THE MUSEE STORY kicker; hot-pink drop-cap M; story text; pink rule; the second-chance line in italic serif |
| 4 | T Ticker | 1800 | 40 | black strip, hot-pink caps scrolling (M2) |
| 5 | 04 Pastry case | 1840 | 818 | hot pink; FRESH FROM THE STUDIO; tilted chalk sign IN STOCK TODAY; a drawn glass case with a curved top and two shelves; four product photos as soft rectangles with folded price tents, names and lines |
| 6 | 05 Order spike | 2658 | 912 | cream; serif headline; a drawn order spike with four tilted paper tickets (zigzag torn bottoms, ticket numbers, drawn stars, caps titles, handwritten quotes, pink names) |
| 7 | 06 Close | 3570 | 448 | light pink; serif tagline; a free-shipping meter with the $75 marker; black pill; white footer with the logo, studio line, links, copyright and unsubscribe |

## Motion spec (brief 12.1)

| ID | Section | What moves | Frame-1 state | Band | States & timing | Assets | Facts used | KB |
|---|---|---|---|---|---|---|---|---|
| M1 | 02 Recipe card | clear water with the whole balm, first fizz ring and faint lavender, more fizz and deeper lavender, then the half-dissolved balm in lavender water with a swirl | balm half dissolved, water lavender, bubbles | 600x150 at y=750 | 1500ms / 600ms / 600ms / 900ms (4 states, loop 3600ms) | Dreamweaver balm circle crop | product photo only | 32 |
| M2 | T Ticker | the three lines slide left one sixth of the loop per frame, seamless | HANDCRAFTED AT OUR STUDIO IN MISSISSIPPI · FOUNDED IN 2011 readable from the left | 600x40 at y=1800 | 250ms / 250ms / 250ms / 250ms / 250ms / 250ms (6 states, loop 1500ms) | none | Dreamweaver page line, homepage 2011, shipping bar | 24 |

Both loop forever at 3 to 8 held states, none under 120 ms. The recipe text, notes and button sit outside the M1 band as the intent asks.

## STOLEN FROM (structure only, from DESIGN_INTENT.md; the refs library is not on disk yet)

- Milk Bar 202840: bakery products on a pink ground, labelled (S4)
- Last Crumb 202820: each product its own line of copy on torn paper (S4 tents, S5 tickets)
- Alice Mushrooms board-201509: review tied to the SKU beside it (S2 margin notes)
- Magic Spoon 201925: ticker band between sections (T)
- Olipop 202238: scalloped edge between sections (S1 doily)

## Concept (one line)

The pastry chef's recipe card: Dreamweaver's own ingredients and method written up as Recipe No. 1, with the bakery case and the order spike carrying the in-stock products and the reviews.

## Copy changes

- None to the words. Layout: the full ingredient list sits at 14 px (studio minimum) instead of 10; 'Chef's note' is set in Poppins where the recipe lines are handwritten, so the product line reads as the product's own words; the hero tag reads 'DREAMWEAVER · $12' on one luggage-style tag; S4 adds 'FRESH FROM THE STUDIO' as the section's kicker (the copy's own section title) alongside the IN STOCK TODAY sign; the ticker shows three phrases and repeats (the copy repeats the first). Dreamweaver's photo is also cut out of its cream background for the hero (the intent's circle-crop fallback was not needed).

## Fonts

- Caveat: Google Font, available in Figma
- Cormorant Garamond: Google Font, available in Figma (substitute for Canela-Thin-Web)
- Poppins: Google Font, available in Figma
- The site's Canela Thin is proprietary; Cormorant Garamond (light) stands in. Poppins is in the site's CSS and on Google Fonts. Caveat is the one pen face for the recipe lines, margin notes, chalk sign and tickets. The logo is the site's SVG rasterised.

## Verify before sending

- Availability and prices (.js, 10 Oct 10:15 WAT): Dreamweaver Therapy Bath Balm $12 (page says low in stock); Sweet Orange & Sunflower Shower Steamers $28; Eucalyptus & Mint Mini Bath Salt Soak $10; Forever Young Therapy Bath Soak $24; Ghost Boxed Bath Balm $12. Re-check on send day; drop anything sold out rather than tag it.
- Reviews verbatim from the Stamped widget API with the trims and encoding repairs in COPY.md section 8; names and places as given (Dr. W., Gypsy831, Pattyt Seattle Washington, Drea E. Madison MS, Nora, Jessica Hattiesburg MS).
- No offer, code or store-wide rating used. 'Free Shipping at $75!' as the bar prints it.
- The Ghost Boxed Bath Balm product image file is named as an AI-generated image on the brand's CDN (COPY.md problem 6); it is the brand's own listing image, used as listed.
- Images are the brand's own files; the ingredient photo is used as a faint texture behind the recipe card.

## Not done (needs the missing inputs)

- No comparison against refs/13-stars or the v6 set, no REF_INDEX pick (library not in the repo).
- No Figma import inspection (Starter plan MCP quota spent).
