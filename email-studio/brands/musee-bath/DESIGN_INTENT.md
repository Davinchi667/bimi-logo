# Musee Bath · DESIGN INTENT · 2026-10-10 WAT

Copy: COPY.md in this folder. Build it exactly. One welcome email, 600 px wide, 6 sections plus a 40 px ticker band, 2,460 px tall, 2 motion moments (S2 fizz, T ticker).

## Signature concept: the pastry chef's recipe card

Leisha Pickering was a pastry chef before she founded Musee in 2011, and the product page already gives a method: "Draw a warm bath. Place balm in water. Soak in Life." The email is her recipe box. S2 is the card: "RECIPE NO. 1 · THE DREAMWEAVER BATH", the real ingredient list, the method, the chef's note (the product's own description), and two 5-star reviews written in the margin like a cook's notes (Dr. W. "largest balm I've ever seen", Gypsy831 "super soft"). The bakery idea carries through: a cake stand in the hero, a glass pastry case of what is in stock today (S4), and the order spike of customer tickets (S5). Real proof inside the concept: the Stamped reviews (verbatim), the ingredient list, the price, and the site's own "is low in stock!" line.

Moving away from: a Halloween banner with a sold-out product grid; anything that shows the 16 sold-out best sellers.

## (a) Inspo refs

| **\#** | **Brand**       | **File**                                                                          | **Pose taken**                                                  | **Lands in**               |
|--------|-----------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------|----------------------------|
| 1      | Milk Bar        | /workspace/design-studio/inspo/mailboard/milk-bar/newest-202840-desktop.jpg       | Bakery products in a grid labelled by occasion on a pink ground | S4 pastry case, pink field |
| 2      | Last Crumb      | /workspace/design-studio/inspo/mailboard/last-crumb/newest-202820-desktop.jpg     | Each product given its own line of copy on torn paper           | S4 price tents, S5 tickets |
| 3      | Alice Mushrooms | /workspace/design-studio/inspo/mailboard/alice-mushrooms/board-201509-desktop.jpg | Review tied to that SKU with the key phrase bolded              | S2 margin notes            |
| 4      | Magic Spoon     | /workspace/design-studio/inspo/mailboard/magic-spoon/newest-201925-desktop.jpg    | Ticker marquee band between sections                            | T ticker                   |
| 5      | Olipop          | /workspace/design-studio/inspo/mailboard/olipop/newest-202238-desktop.jpg         | Scalloped edges between sections                                | S1 doily edge              |

## (b) Section map

| **Section**       | **Pose / layout**                                                                                                                              | **Copy** | **Image (COPY.md §9)** | **Motion**  | **Height** |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------------|-------------|------------|
| S1 Hero           | Light pink; black logo; 52 px thin serif headline; balm in a circle on a drawn cake stand; hanging price tag; scalloped white bottom edge      | S1       | C0, C1                 | No          | 460        |
| S2 Recipe card    | Cream; rotated ruled card with pink header; ingredients + method + chef's note left; fizzing tub GIF right; margin notes; low-stock corner tag | S2       | C1, C2                 | **Yes, M1** | 560        |
| S3 Story          | White; pink drop-cap M; story; italic pull line                                                                                                | S3       | none                   | No          | 300        |
| T Ticker          | Black strip, pink caps scrolling                                                                                                               | T        | none                   | **Yes, M2** | 40         |
| S4 Pastry case    | Hot pink; drawn glass case with two shelves; four cut-outs; white price tents; IN STOCK TODAY chalk sign                                       | S4       | C3, C4, C5, C6         | No          | 460        |
| S5 Order spike    | Cream; spike with 3 to 4 tilted tickets of different heights                                                                                   | S5       | none                   | No          | 340        |
| S6 Close + footer | Light pink; tagline; \$75 meter; button; white footer                                                                                          | S6       | C0                     | No          | 300        |
| Total             |                                                                                                                                                |          |                        | 2           | 2,460      |

Ground sequence: light pink → cream → white → black → hot pink → cream → light pink → white footer.

## (c) Motion (frame 1 is a finished static state)

**M1 · S2 the fizz** · 200 x 260 GIF, 4 frames, about 3.6 s, loop.

- F1 (static, 1,500 ms): water in the drawn tub tinted soft lavender with a swirl, the balm half dissolved, bubbles around it. Finished state.

- F2 (600 ms): clear water, whole balm (C1 cut-out) just touching the surface.

- F3 (600 ms): first ring of fizz, faint lavender.

- F4 (900 ms): more fizz, deeper lavender; loop to F1. The ingredients, method, notes and button are live HTML beside the GIF.

**M2 · T ticker** · 600 x 40 GIF, 6 frames at 250 ms, seamless loop. F1 shows "HANDCRAFTED AT OUR STUDIO IN MISSISSIPPI · FOUNDED IN 2011" fully readable from the left edge (a complete static line).

GIF budget about 300 KB total.

## (d) The one CTA shape

Pill, 52 px tall, full radius, black \#1a1a1a fill, white caps 14 px, letter-spaced 1.5 px, 300 px wide, centred. On the black ticker neighbour it never appears. Wording SHOP DREAMWEAVER (S1, S2 with "· \$12", S6); SHOP THE BATH once (S4). Tags, tents and tickets are paper shapes, never pills.

## (e) Palette and type (from the site)

- Hot pink \#ff7ba7, light pink \#ffc2d6, black \#1a1a1a / \#000000, text \#333333, cream \#f5f5f5, white \#ffffff. All from homepage CSS. Lavender for the fizz water only (from the balm photo C1).

- Display: Canela Thin (the site's "Canela-Thin-Web"), 28 to 52 px. Body: Poppins 15 to 16 px (the site's). Margin notes and tickets: a pen-style hand (e.g. Caveat), one face only.

## (f) What NOT to do

- No three white review cards: reviews are margin notes and spiked tickets.

- No colour-swap template, no grey footer, no generic 4-up grid (the case has shelves, tents and a sign).

- No sold-out products, no "back soon", no Ice Cream Truck, Eucalyptus & Mint Shower Steamers or Dreamweaver Bath Soak (all sold out).

- No discount, code box or "Best Deals" amount.

- No Oprah badge or press logos (not on the site).

- No people photos or stock women: the second-chance line stands in type.

- No sleep or skin promises beyond the quoted product lines.

- No em dash in any text layer. No emoji; stars are drawn.

## Asset gaps and fallbacks

| **Want**               | **Have?**                 | **Fallback**                                              |
|------------------------|---------------------------|-----------------------------------------------------------|
| Transparent cut-outs   | Photos are on backgrounds | Circle crops (S1) and soft rectangles on the shelves (S4) |
| Leisha or studio photo | Not pulled                | Type only                                                 |
| Fizz frames            | No video                  | Drawn tub; C1 cut-out composited in frames                |
