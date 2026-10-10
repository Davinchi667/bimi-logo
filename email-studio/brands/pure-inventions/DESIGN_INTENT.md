# Pure Inventions · DESIGN INTENT · 2026-10-10 WAT

Copy: COPY.md in this folder. Build it exactly. One popup frame (P0, 600 x 520) plus one welcome email, 600 px wide, 6 sections, 2,460 px tall, 3 motion moments (P0, S3, S5).

## Signature concept: the spa water station card

Spa guests are how this brand gets found: at least 10 Coconut Water and Cranberry + Elderberry reviewers say they first tasted it at a spa (Amy T. "at a high end spa", Maria L. "with some girlfriends", Marie "my massage therapist gave me a cup", Madison S. "brought the spa home with me"). The email is built from that spa moment: the folded tent card that stands beside an infused-water dispenser, listing "TODAY'S WATER". S2 is the card itself (four real flavours, servings and prices from .js, the "DEVELOPED BY NUTRITIONISTS · PERFECTED SINCE 2003" stamp). The hero glass wears a carafe tag. The reviews sit along a path from the spa to the reader's kitchen. Real proof inside the concept: the site's "thousands of renowned spas and resorts" line, the 205 Coconut Water reviews, and four verbatim spa-discovery reviews.

What we are moving away from: a white canvas, one bottle centred, "Welcome to Pure Inventions", a three-card review row.

## (a) Inspo refs (structure only, never their words)

| **\#** | **Brand**                             | **File**                                                                      | **Pose taken**                                                                   | **Lands in**                                                  |
|--------|---------------------------------------|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------|---------------------------------------------------------------|
| 1      | Last Crumb                            | /workspace/design-studio/inspo/mailboard/last-crumb/newest-202817-desktop.jpg | Survey stats as giant boxed numbers with a small caption under each              | S3 "96 OZ" counter with the struck "12 OZ"                    |
| 2      | Olipop                                | /workspace/design-studio/inspo/mailboard/olipop/newest-202238-desktop.jpg     | One product on a field coloured to its flavour, stacked sections changing ground | S1 bottle and glass on blue; S5 water tinting to each flavour |
| 3      | Poppi                                 | /workspace/design-studio/inspo/mailboard/poppi/newest-202335-desktop.jpg      | Flavour swatch row with a selector moving across it                              | S5 swatches + ring                                            |
| 4      | Grüns                                 | /workspace/design-studio/inspo/mailboard/gruns/newest-204911-desktop.jpg      | Callouts pinned to points with small markers                                     | S4 review tags pinned with drops along the route              |
| 5      | Fungies (STEAL_THIS: "in-email quiz") | /workspace/design-studio/inspo/mailboard/\_meta/STEAL_THIS.md                 | A question with tappable options leading to a product                            | P0 "I want to" chips                                          |

## (b) Section map

| **Section**          | **Pose / layout**                                                                                                                  | **Copy block** | **Image (COPY.md §9)** | **Motion**        | **Height**           |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------|----------------|------------------------|-------------------|----------------------|
| P0 Popup             | 480 px card on a scrim; tilted bottle with falling drop; question; four outline chips; email field; button; No thanks              | P0             | A2                     | Yes, chip tap     | 520 (separate frame) |
| S1 Hero              | Logo bar; pale blue wash; 52 px serif headline left; bottle before a tall glass right, cut by bottom; round carafe tag on a string | S1             | A1, A2                 | No                | 440                  |
| S2 Spa water card    | Cream tent card angled on blue; TODAY'S WATER menu with dotted leaders, 40 px bottles, round stamp                                 | S2             | A2, A3, A4, A5         | No                | 540                  |
| S3 Ounce counter     | Deep blue; outlined bottle filling left; 96 OZ display right, 12 OZ struck above; quote; mono value row                            | S3             | none                   | Yes, fill + count | 380                  |
| S4 Route             | Cream; hand-drawn dotted path; four tags of different widths pinned with blue drops; small bottle at the end                       | S4             | A2 (40 px) or A2b crop | No                | 420                  |
| S5 First drop        | White; glass centred, dropper above; four swatches; label left                                                                     | S5             | A2                     | Yes, drop + tint  | 380                  |
| S6 Founders + footer | Pale blue, left aligned; italic promise; button; white footer                                                                      | S6             | A1                     | No                | 300                  |
| Total                |                                                                                                                                    |                |                        | 3                 | 2,460 + popup        |

Ground sequence: white bar → blue wash → blue with cream card → deep blue → cream → white → pale blue → white footer.

## (c) Motion (frame 1 is a finished static design; Outlook shows frame 1)

**M1 · P0 popup chips** · 480 x 360 GIF, 4 frames, about 4 s, loop.

- F1 (static, 1,600 ms): Chip 1 filled \#467C99 with white text, email field and button visible. This is the finished state.

- F2 (600 ms): all four chips outline only, no email field.

- F3 (600 ms): cursor over Chip 1, chip fills.

- F4 (1,200 ms): email field slides up under the chips (same as F1). The email field and button are live HTML in a real build; in the spec PNG they are drawn.

**M2 · S3 ounce counter** · 560 x 300 GIF, 5 frames, about 4 s, loop.

- F1 (static, 1,600 ms): bottle full, "96 OZ" in white, "12 OZ" struck above.

- F2 (400 ms): bottle at one eighth, number reads 12 OZ, no strike.

- F3 (400 ms): bottle half, 48 OZ. F4 (400 ms): three quarters, 72 OZ. F5 (1,200 ms): same as F1. The quote, name and value row are static HTML below the GIF.

**M3 · S5 first drop** · 300 x 320 GIF, 4 frames, 900 ms each, loop.

- F1 (static): clear glass, Coconut Water bottle A2 beside it, white Coconut swatch ringed.

- F2: drop falls, water tints pink, Watermelon ringed. F3: deep red, Cranberry + Elderberry ringed. F4: soft orange, Mango ringed. Keep tints light; the water should still read as water. Budget for all GIFs: about 450 KB.

## (d) The one CTA shape

Pill, 52 px tall, full radius, \#467C99 fill, white caps 15 px, letter-spaced 1 px, 360 px wide centred (left aligned in S6). Main wording SHOP COCONUT WATER (S1, S4, S5, S6); SHOP ALL FLAVORS once in S2; SEND ME MY FLAVOR PICKS in the popup. Chips are outline pills with no fill until tapped; the stamp and carafe tag are round but never filled blue, so only the button looks clickable.

## (e) Palette and type (from the site)

- Dark blue \#467C99, soft blue \#90b0c2, cream \#F9F8F4, light grey \#f2f2f2, white, black text \#000000, accent green \#5aa600 (used only on the stamp ring). All from the homepage CSS.

- Flavour tints for S5 only: watermelon pink, cranberry red, mango orange, sampled from the bottle labels in A3 to A5.

- Type: the site body is Roboto. Use Roboto 16 px body, Roboto 500 caps for kickers and chips. Display: a soft serif (Lora or similar) at 44 to 56 px for headlines, to give the spa-card feel; the menu in S2 uses Roboto with dotted leaders; S3's value row in a mono (Roboto Mono).

## (f) What NOT to do

- No three white review cards. Reviews are tags along the S4 path.

- No colour-swap template: no centred bottle on white, no grey footer, no four-up product grid (the four flavours are a menu, not tiles).

- No discount, code box, percentage or "% OFF" anywhere. The site has no offer.

- No site-wide star average and no Black Cherry rating.

- No health claims beyond the site lines quoted; no "immunity", "urinary", "calm" benefit badges.

- No stock spa photos or people: no founder photo was pulled, no spa photo exists in the assets. The spa is suggested by the card, the carafe tag and the path.

- No em dash in any text layer. No emoji (stars are drawn).

## Asset gaps and fallbacks

| **Want**                  | **Have?**            | **Fallback**                           |
|---------------------------|----------------------|----------------------------------------|
| Founders' photo           | Not pulled           | Type only in S6                        |
| Spa interior              | No                   | Drawn tent card and path               |
| Mango flavour description | No line pulled       | "NEW" tag, as the menu shows           |
| Black logo variant        | Only colour PNG (A1) | Use on white bar and white footer only |
