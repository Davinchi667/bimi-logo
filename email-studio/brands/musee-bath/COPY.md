# Musee Bath · COPY (spec welcome email for cold outreach)

Brief date: 2026-10-10 10:30 WAT · Writer: Brand Copywriter bot · Research: RESEARCH.md in this folder (not edited) plus the live checks in the Research log. Designer: build straight from this file and DESIGN_INTENT.md. 600 px wide, 7 sections (one is a thin ticker band), 2,460 px tall. Copy is final: use it exactly.

## 1. Header

| **Field**                                 | **Value**                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Brand name                                | Musee Bath (the site writes "Musee", no accent)                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Website link                              | [<u>https://www.museebath.com/</u>](https://www.museebath.com/)                                                                                                                                                                                                                                                                                                                                                                                                       |
| Nature                                    | Flow (welcome), for the footer form "Want to Soak in the Best Deals? Sign up for Emails!"                                                                                                                                                                                                                                                                                                                                                                             |
| Angle                                     | Leisha Pickering was a pastry chef before she made bath balms, and the product pages already read like recipes ("Draw a warm bath. Place balm in water. Soak in Life."). The welcome is a recipe card for one bath, then a bakery case of what is in stock today. Every product shown is available in .js today; 16 of 30 best sellers are not.                                                                                                                       |
| Best seller (in stock)                    | Dreamweaver Therapy Bath Balm · [<u>https://www.museebath.com/products/dreamweaver-bath-balm</u>](https://www.museebath.com/products/dreamweaver-bath-balm) · \$12.00 · available, page says "is low in stock! Order now before we sell out." (dreamweaver-bath-balm.js and page, 10:15 WAT) · 7 reviews, all 5 stars (Stamped widget API, 10:17 WAT). How verified: the first in-stock product in /collections/best-sellers order (the three above it are sold out). |
| Products to feature (all available today) | Dreamweaver Therapy Bath Balm \$12 · Sweet Orange & Sunflower Shower Steamers \$28 · Eucalyptus & Mint Mini Bath Salt Soak \$10 · Forever Young Therapy Bath Soak \$24 · Ghost Boxed Bath Balm \$12 (Halloween, matches the homepage hero)                                                                                                                                                                                                                            |
| Subject line A                            | The Dreamweaver Bath Balm, \$12                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Subject line B                            | Free shipping at \$75 on handcrafted bath                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Preview                                   | leisha was a pastry chef before musee. here's her recipe for tonight.                                                                                                                                                                                                                                                                                                                                                                                                 |
| Announcement bar                          | Free Shipping at \$75!                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Offer                                     | No signup offer exists ("Best Deals" is promised with no amount). Only "Free Shipping at \$75!". No code box.                                                                                                                                                                                                                                                                                                                                                         |
| Length                                    | S1 460 + S2 560 + S3 300 + T 40 + S4 460 + S5 340 + S6 300 = 2,460 px                                                                                                                                                                                                                                                                                                                                                                                                 |

Voice rules: sweet, whimsical, warm ("spread joy", "Soak in Life", "boo-tiful") · "Musee" without accent, "Bath Balms" capitalised as the site does · they capitalise "Life" in "Soak in Life." · US spelling · no emoji · no skin or sleep claims beyond the site's own lines ("Lull yourself to sleep...", "hydrate and soften the skin") · second-chance employment told in their words only · CTAs in caps.

## Research log

| **Studied**                  | **Where / when**                                                                                                                                        | **Move taken**                                                                                                                                                                                                                                                                                                                                                                      |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Best Sellers collection JSON | [<u>https://www.museebath.com/collections/best-sellers/products.json</u>](https://www.museebath.com/collections/best-sellers/products.json) · 10:14 WAT | Still 16 of 30 sold out (same as RESEARCH.md). In stock picked: Dreamweaver Bath Balm, Sweet Orange & Sunflower Shower Steamers, Eucalyptus & Mint Mini Bath Salt Soak, Forever Young Therapy Bath Soak, Ghost Boxed Bath Balm.                                                                                                                                                     |
| products .js (5 handles)     | /products/.js · 10:15 WAT                                                                                                                               | Prices, availability, descriptions, image URLs.                                                                                                                                                                                                                                                                                                                                     |
| Stamped widget reviews       | stamped.io/api/widget/reviews?productId=\<id\>&storeUrl=musee-bath-development-test.myshopify.com · 10:17 WAT                                           | **Correction to RESEARCH.md:** reviews exist, they just are not in the server HTML. Dreamweaver Bath Balm 7, Sweet Orange & Sunflower Shower Steamers 13, Forever Young Bath Soak 3, Ghost Boxed Bath Balm 1, Mini Salt Soak 0. Store total 667. Customer words that repeat: scent ("smells divine", "Heavenly scent", "orange grove"), soft skin, gifts (teachers, granddaughter). |
| Dreamweaver page             | [<u>https://www.museebath.com/products/dreamweaver-bath-balm</u>](https://www.museebath.com/products/dreamweaver-bath-balm) · 10:15 WAT                 | The ingredient list and the three-step "Draw a warm bath..." line make the recipe card.                                                                                                                                                                                                                                                                                             |
| Homepage                     | [<u>https://www.museebath.com/</u>](https://www.museebath.com/) · 10:16 WAT                                                                             | "Halloween Magic, Made for the Bath" hero; story block for S3. The 404 nav link to /products/adventure-bar-soap is still there (2 hrefs, 404, 10:16 WAT). Oprah Bath O-Wards: 0 hits on home or product page; not used.                                                                                                                                                             |
| Really Good Emails welcome   | [<u>https://reallygoodemails.com/categories/welcome</u>](https://reallygoodemails.com/categories/welcome) · 09:31 WAT                                   | "You have good taste. 🍪" (a bakery-ish welcome) shows food language working in a welcome. Taken: the recipe frame; not its words or emoji.                                                                                                                                                                                                                                         |
| Mailboard inspo              | Milk Bar newest-202906, Last Crumb newest-202820, Magic Spoon (ticker), Alice (constellation)                                                           | Bakery-case product row, recipe ingredients floating, ticker band.                                                                                                                                                                                                                                                                                                                  |

## Diagnosis

Segment: a footer subscriber who likes the look of Musee and has not ordered; many buy as gifts. Awareness stage 2: knows bath balms, not sure why Musee's are worth \$12. Task: sharpen the image (handmade by a pastry chef, in Mississippi, by women rebuilding their lives). Sophistication 2 to 3 (labelled assumption: bath bombs are everywhere), so the maker and the recipe carry it. One performance: a bath made like a pastry. Belief built on: handmade things are better. Belief routed around: a bath balm is a bath bomb from the drugstore. Left alone: wellness or sleep promises beyond the site's lines. Route: peripheral (\$12, gift). Defensible claim: handcrafted at their studio in Mississippi since 2011, Dreamweaver \$12 with chamomile and lavender oil, 5-star reviews quoted verbatim, free shipping at \$75. Structure: story-led welcome. Levers, three: the maker (Leisha, pastry chef), social proof (reviews about scent and size), mission (second-chance employment). Left out: subscription boxes, quiz, corporate gifting, low-stock urgency beyond one tag.

## 2. Problems spotted (for David's first email)

| **\#** | **Problem**                                                                                                                                                          | **Where**                              | **Checked** | **Evidence**                   | **Confidence**                                              | **Use**                  |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|-------------|--------------------------------|-------------------------------------------------------------|--------------------------|
| 1      | The "Shop All Lifestyle" nav link still points to /products/adventure-bar-soap, which returns 404.                                                                   | homepage nav                           | 10:16 WAT   | curl 404, 2 hrefs in home.html | confirmed                                                   | FOR EMAIL                |
| 2      | 16 of 30 Best Sellers are sold out, including the top three.                                                                                                         | /collections/best-sellers              | 10:14 WAT   | products.json                  | confirmed                                                   | FOR EMAIL                |
| 3      | The footer form promises "the Best Deals" with no amount, and Klaviyo has 0 live forms (RESEARCH.md).                                                                | footer                                 | 10:16 WAT   | home.html                      | confirmed                                                   | FOR EMAIL                |
| 4      | NEW: the store has 667 reviews in Stamped, none in the page HTML, so they are invisible to anything that does not run the widget script.                             | product pages                          | 10:17 WAT   | widget API vs dw.html          | confirmed                                                   | call note                |
| 5      | NEW: quiz-builder admin text is in the homepage HTML ("Choose the ID of the Quiz you want to render...", "Fragrance Quiz Template (copy)"). May be hidden on screen. | homepage HTML                          | 10:16 WAT   | home.html                      | likely (render not checked)                                 | call note                |
| 6      | NEW: Ghost Boxed Bath Balm's product images are named "ChatGPTImageAug20_2026..." and the shop domain in scripts is "musee-bath-development-test.myshopify.com".     | ghost-boxed-bath-balm.js; page scripts | 10:15 WAT   | .js image URLs; dw.html        | confirmed (file names only; says nothing about the picture) | call note, handle gently |
| 7      | NEW: Eucalyptus & Mint Mini Bath Salt Soak, a best seller, has 0 reviews.                                                                                            | Stamped                                | 10:17 WAT   | API total 0                    | confirmed                                                   | call note                |

## 3. Verified proof and offers

| **Item**   | **Verbatim**                                                                                                                                                                        | **Source**       | **Checked** |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|-------------|
| Shipping   | Free Shipping at \$75!                                                                                                                                                              | site bar         | 10:16       |
| Founder    | Leisha Pickering, a former pastry chef, founded Musee Bath in 2011 with a vision to care for her community by creating handcrafted products that would provide jobs and spread joy. | homepage story   | 10:16       |
| Mission    | Musee proudly offers second-chance employment to women in recovery trying to rebuild their lives after incarceration and addiction.                                                 | same             | 10:16       |
| Made       | Our products are handcrafted at our studio in Mississippi with natural, relaxing and soothing ingredients.                                                                          | Dreamweaver page | 10:15       |
| Directions | Draw a warm bath. Place balm in water. Soak in Life.                                                                                                                                | Dreamweaver page | 10:15       |
| Low stock  | is low in stock! Order now before we sell out.                                                                                                                                      | Dreamweaver page | 10:15       |
| Reviews    | Stamped, counts above; all quoted reviews are 5 stars                                                                                                                               | widget API       | 10:17       |
| Not used   | Oprah Bath O-Wards (not on site), a store-wide average, any % off, sold-out products.                                                                                               |                  |             |

## 4. Email copy, section by section

### S1 · Hero · 460 px · static

Layout/pose: pink \#ffc2d6 field with a white scalloped edge at the bottom like a cake box doily. Logo (black SVG) top centre. Headline in Canela-style thin serif, 52 px, black, two lines, centred. Under it the Dreamweaver balm photo cut into a circle (300 px) as if sitting on a white cake stand drawn in 2 px black line. A small round pink tag hangs from the stand. Image: C1 (dreamweaverbalm.jpg).

Announcement bar: Free Shipping at \$75!

Headline: Bath recipes from a former pastry chef.

Subheadline: Musee invites you to slow down and enjoy the sweet things in life like a warm bath.

Tag: DREAMWEAVER · \$12

CTA: SHOP DREAMWEAVER

\[DESIGN NOTE\] Headline 6 words, ours, built from the story block's "a former pastry chef". The stand is a drawing; the balm is the real photo.

### S2 · Recipe No. 1 (signature: the recipe card) · 560 px · MOTION

Layout/pose: cream \#f5f5f5 field. A handwritten-style recipe card (520 px) with ruled lines and a pink header strip, slightly rotated (-2 degrees), like a card from a pastry chef's box. Left two thirds: title, "Makes", ingredients, method. Right third: the balm fizzing in a drawn tub (GIF). Two reviews written in the card's margin as "notes", in a pen-style face, each with drawn stars. Images: C1 (cut to a circle in the tub), C2 (ingredient image, optional texture behind the card).

Card title: RECIPE NO. 1 · THE DREAMWEAVER BATH

Makes: one warm bath

Ingredients: Lavender Oil, Grapeseed Oil, Shea Nut Oil, Vitamin E Oil, French Lavender Essential Oil, Chamomile Essential Oil.

Method: Draw a warm bath. Place balm in water. Soak in Life.

Chef's note: Lull yourself to sleep with the soothing waters of calming chamomile and lavender oil- a wonderful way to end the day.

Margin note 1: ★★★★★ "Everything one would want in a bath balm, as it smells divine, great quality, and good value too (largest balm I've ever seen)." Dr. W.

Margin note 2: ★★★★★ "Love the smell and the way it made my skin feel super soft!" Gypsy831

Tag on card corner: is low in stock! Order now before we sell out.

CTA: SHOP DREAMWEAVER · \$12

\[DESIGN NOTE\] The ingredients line is the site's list with Sodium Bicarbonate, Citric Acid, Fragrance Oil and Coloreze left out for space; keep the full list in a 10 px line at the card foot: "Full list: Sodium Bicarbonate, Citric Acid, Lavender Oil, Grapeseed Oil, Shea Nut Oil, Fragrance Oil, Vitamin E Oil, Coloreze, French Lavender Essential Oil, Chamomile Essential Oil." Their "oil- a" spacing stays. The method is presented as the recipe's method, not as three designed bullets: one line, one sentence run. Fizz GIF frames in DESIGN_INTENT.md.

### S3 · Leisha, and who makes it · 300 px · static

Layout/pose: white field. Left: a large pink drop-cap "M". Story text left-aligned in 15 px. A thin pink rule, then the second-chance line in 18 px italic serif, set apart.

Kicker: THE MUSEE STORY

Body: Leisha Pickering, a former pastry chef, founded Musee Bath in 2011 with a vision to care for her community by creating handcrafted products that would provide jobs and spread joy. Drawing from her expertise in working with high-quality ingredients, Leisha crafted a line of whimsical, luxurious bath products.

Pull line: Musee proudly offers second-chance employment to women in recovery trying to rebuild their lives after incarceration and addiction.

\[DESIGN NOTE\] No photo of Leisha or the team: none pulled. Do not use stock people.

### T · Ticker band · 40 px · MOTION

Layout/pose: black \#1a1a1a strip, pink caps 13 px, scrolling right to left.

HANDCRAFTED AT OUR STUDIO IN MISSISSIPPI · FOUNDED IN 2011 · FREE SHIPPING AT \$75 · HANDCRAFTED AT OUR STUDIO IN MISSISSIPPI ·

### S4 · Fresh from the studio (the bakery case) · 460 px · static

Layout/pose: pink \#ff7ba7 field. A drawn glass pastry case (white line, two shelves) runs across the section. Four products sit on the shelves as cut-out photos, each with a small folded white price tent in front (name, one line, price). Top right corner of the case: a chalk-style "IN STOCK TODAY" sign. Images: C3, C4, C5, C6.

Sign: IN STOCK TODAY

Top shelf:

Sweet Orange & Sunflower Shower Steamers · Relax in a refreshing shower, as sweet orange essential oil fills the air and invigorates your senses. · \$28

Eucalyptus & Mint Mini Bath Salt Soak · Pacific sea salt and Epsom salt, with eucalyptus and mint. · \$10

Bottom shelf:

Forever Young Therapy Bath Soak · Experience the renewal of a jasmine and rosehip bath as rose clay brings a youthful glow to tired skin. · \$24

Ghost Boxed Bath Balm · A little ghost, a lot of glow. Marshmallow & Whipped Cream, Surprise Inside. · \$12

CTA: SHOP THE BATH

\[DESIGN NOTE\] Only these four (plus Dreamweaver) are shown because they are available in .js today. Re-check availability on build day; if any flips to sold out, drop it rather than show a sold-out tag. The Mini Soak line is shortened from its description (§8).

### S5 · The order spike · 340 px · static

Layout/pose: cream field. A bakery order spike drawn in the centre; three paper order tickets stuck on it at different heights and angles, each with a ticket number in the corner, the reviewer's title as the "order", the quote, and the name. A fourth ticket half-hidden behind (no text).

Headline: What customers ordered more of

Ticket 1 · ★★★★★ SMELLS LIKE YOU ARE IN AN ORANGE GROVE

"Every scent this company makes is wonderful! There isn't one I don't love!" Pattyt, Seattle, Washington

Ticket 2 · ★★★★★ THE TEACHERS LOVED THEM!

"I bought these as teacher gifts! They absolutely loved them!! They smelled amazing!" Drea E., Madison, MS

Ticket 3 · ★★★★★ PLS MAKE MORE IN THIS SCENT

"i would do anything if they would make more products in this scent please im begging" Nora

Ticket 4 · ★★★★★ MY FAVORITE BATH SOAK!

"My favorite way to unwind after a long day! I love the scent! This bath soak left my skin so soft and smooth." Jessica, Hattiesburg, MS

\[DESIGN NOTE\] Tickets 1 to 3 are Sweet Orange & Sunflower Shower Steamers reviews; ticket 4 is Forever Young Bath Soak. If only three tickets fit, drop ticket 4 onto the hidden ticket's place at smaller size, do not cut a quote mid-sentence. Ticket numbers are decoration (e.g. No. 01 to 04), not claims.

### S6 · Close and footer · 300 px · static

Layout/pose: pink \#ffc2d6 field, centred. The tagline in thin serif 28 px, a free-shipping meter (thin bar with a marker at \$75) under it, then the button. Footer below on white: logo, link row, copyright.

Tagline: Wellness products that create joyful moments for the happiest you.

Meter label: Free Shipping at \$75!

CTA: SHOP DREAMWEAVER

Footer: Musee Bath · Handcrafted at our studio in Mississippi · Store Locator · Corporate Gifting · Returns + Exchanges · Follow us

Copyright © 2026 Musee Bath · Unsubscribe

\[DESIGN NOTE\] No street address found on the homepage; Klaviyo adds the sender address at build. The meter is a static drawing with only "\$75" marked; no cart total is implied.

## 5. Rule check

U+2014: none · the o-word: none · banned phrases: none · reviews: 6 verbatim, Stamped, names and places as given · offer: none, no code · sold-out products: none shown · CTAs caps (SHOP DREAMWEAVER main, SHOP THE BATH once) · subjects carry real numbers (\$12, \$75) · lint: PASS.

## 6. Claims I could NOT verify (left out)

1.  Oprah Bath O-Wards (leads CSV only; 0 hits on site).

2.  A store-wide rating (API returns 5.0 over 667, not seen rendered).

3.  A street address.

4.  Whether the "Best Deals" signup gets any offer.

5.  Whether any of the four in-stock picks are best sellers by revenue (collection order only).

## 7. Verified (exact source)

| **Line**                        | **Verbatim source**                                                                                                                                                         | **URL**                                                                                                                           |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Free Shipping at \$75!          | same                                                                                                                                                                        | homepage bar                                                                                                                      |
| former pastry chef / story body | Leisha Pickering, a former pastry chef, founded Musee Bath in 2011... luxurious bath products.                                                                              | [<u>https://www.museebath.com/</u>](https://www.museebath.com/)                                                                   |
| S1 subheadline                  | Musee invites you to slow down and enjoy the sweet things in life like a warm bath.                                                                                         | homepage                                                                                                                          |
| Dreamweaver \$12                | Default Title 12.00, available                                                                                                                                              | dreamweaver-bath-balm.js                                                                                                          |
| Ingredients                     | Sodium Bicarbonate, Citric Acid, Lavender Oil, Grapeseed Oil, Shea Nut Oil, Fragrance Oil, Vitamin E Oil, Coloreze, French Lavender Essential Oil, Chamomile Essential Oil. | /products/dreamweaver-bath-balm                                                                                                   |
| Method                          | Draw a warm bath. Place balm in water. Soak in Life.                                                                                                                        | same                                                                                                                              |
| Chef's note                     | Lull yourself to sleep with the soothing waters of calming chamomile and lavender oil- a wonderful way to end the day.                                                      | same (.js description)                                                                                                            |
| Low stock                       | is low in stock! Order now before we sell out.                                                                                                                              | same                                                                                                                              |
| Dr. W.                          | "Perfect", 5, 01/11/2021                                                                                                                                                    | Stamped, Dreamweaver Bath Balm                                                                                                    |
| Gypsy831                        | "Loved it!", 5, 01/29/2021                                                                                                                                                  | same                                                                                                                              |
| Pull line                       | Musee proudly offers second-chance employment...                                                                                                                            | homepage                                                                                                                          |
| Ticker                          | Our products are handcrafted at our studio in Mississippi... · founded ... in 2011 · Free Shipping at \$75!                                                                 | Dreamweaver page; homepage                                                                                                        |
| S4 lines + prices               | descriptions; \$28, \$10, \$24, \$12, all available                                                                                                                         | sweet-orange-sunflower-shower-steamer.js, eucalyptus-mint-mini-salt-soak.js, forever-young-bath-soak.js, ghost-boxed-bath-balm.js |
| Pattyt                          | "Smells like you are in an orange grove", 5, 04/02/2021, Seattle, Washington                                                                                                | Stamped, Sweet Orange & Sunflower                                                                                                 |
| Drea E.                         | "The Teachers LOVED them!", 5, 12/30/2020, Madison, MS                                                                                                                      | same                                                                                                                              |
| Nora                            | "PLS MAKE MORE IN THIS SCENT", 5, 07/28/2026                                                                                                                                | same                                                                                                                              |
| Jessica                         | "My favorite bath soak!", 5, 10/20/2020, Hattiesburg, MS                                                                                                                    | Stamped, Forever Young Bath Soak                                                                                                  |
| Tagline                         | Wellness products that create joyful moments for the happiest you.                                                                                                          | homepage                                                                                                                          |
| Footer links                    | Store Locator · Corporate Gifting · Returns + Exchanges · Follow us · Copyright © 2026 Musee Bath                                                                           | homepage footer                                                                                                                   |

## 8. Changes from the brand's own words

| **Section**        | **Site text**                                                                                                                                              | **Copy text**                                              | **Why**                              |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|--------------------------------------|
| S2                 | full ingredient list                                                                                                                                       | short list + full list at card foot                        | Space; full list kept.               |
| S4 Mini Soak       | Experience the renewal of this Pacific sea salt and Epsom salt bath. Rest in fragrant waters of eucalyptus and mint while shea nut oil hydrates your skin. | Pacific sea salt and Epsom salt, with eucalyptus and mint. | Fit on a price tent; no claim added. |
| S4 Ghost           | Marshmallow & Whipped Cream / Surprise Inside / A little ghost, a lot of glow.                                                                             | reordered into one line                                    | Fit.                                 |
| S5 Pattyt, Drea E. | "isn�t", "don�t" (broken apostrophes in the API), double spaces                                                                                            | "isn't", "don't", single spaces                            | Encoding repair only.                |
| S5 titles          | mixed case                                                                                                                                                 | caps                                                       | Review title format.                 |
| S3                 | story continues about Bath Balms' ingredients                                                                                                              | first two sentences + mission line                         | Length.                              |

## 9. Assets (real image URLs, Shopify CDN from .js)

| **ID** | **Use**                                                  | **URL**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|--------|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| C0     | Logo, SVG                                                | [<u>https://www.museebath.com/cdn/shop/files/MUSEE_LOGO-02.svg?v=1690480958</u>](https://www.museebath.com/cdn/shop/files/MUSEE_LOGO-02.svg?v=1690480958)                                                                                                                                                                                                                                                                                                                                                     |
| C1     | Dreamweaver Therapy Bath Balm (S1, S2)                   | [<u>https://cdn.shopify.com/s/files/1/0282/1295/3160/files/dreamweaverbalm.jpg?v=1762525734</u>](https://cdn.shopify.com/s/files/1/0282/1295/3160/files/dreamweaverbalm.jpg?v=1762525734)                                                                                                                                                                                                                                                                                                                     |
| C2     | Dreamweaver ingredient image (S2 texture, optional)      | [<u>https://cdn.shopify.com/s/files/1/0282/1295/3160/files/ingredientimage6.jpg?v=1737663128</u>](https://cdn.shopify.com/s/files/1/0282/1295/3160/files/ingredientimage6.jpg?v=1737663128)                                                                                                                                                                                                                                                                                                                   |
| C3     | Sweet Orange & Sunflower Shower Steamers (S4)            | [<u>https://cdn.shopify.com/s/files/1/0282/1295/3160/files/sweetorangeandsunflowersteamer.jpg?v=1762526128</u>](https://cdn.shopify.com/s/files/1/0282/1295/3160/files/sweetorangeandsunflowersteamer.jpg?v=1762526128)                                                                                                                                                                                                                                                                                       |
| C4     | Eucalyptus & Mint Mini Bath Salt Soak (S4)               | [<u>https://cdn.shopify.com/s/files/1/0282/1295/3160/files/Eucalyptussoak_1512x_6bd4e225-d1ba-4c82-a121-b623f5556756.png?v=1772829409</u>](https://cdn.shopify.com/s/files/1/0282/1295/3160/files/Eucalyptussoak_1512x_6bd4e225-d1ba-4c82-a121-b623f5556756.png?v=1772829409)                                                                                                                                                                                                                                 |
| C5     | Forever Young Therapy Bath Soak (S4)                     | [<u>https://cdn.shopify.com/s/files/1/0282/1295/3160/files/foreveryoung-salt.jpg?v=1762525754</u>](https://cdn.shopify.com/s/files/1/0282/1295/3160/files/foreveryoung-salt.jpg?v=1762525754)                                                                                                                                                                                                                                                                                                                 |
| C6     | Ghost Boxed Bath Balm (S4)                               | [<u>https://cdn.shopify.com/s/files/1/0282/1295/3160/files/ChatGPTImageAug20_2026at09_32_15AM_a97c9327-154c-488c-b1f4-4eb0d7071309.png?v=1787236464</u>](https://cdn.shopify.com/s/files/1/0282/1295/3160/files/ChatGPTImageAug20_2026at09_32_15AM_a97c9327-154c-488c-b1f4-4eb0d7071309.png?v=1787236464)                                                                                                                                                                                                     |
| C7     | Site icons (flower, heart, rainbow), optional decoration | [<u>https://www.museebath.com/cdn/shop/files/flower-icon_54x54.png?v=1686338378</u>](https://www.museebath.com/cdn/shop/files/flower-icon_54x54.png?v=1686338378) · [<u>https://www.museebath.com/cdn/shop/files/heart-icon_54x54.png?v=1686338392</u>](https://www.museebath.com/cdn/shop/files/heart-icon_54x54.png?v=1686338392) · [<u>https://www.museebath.com/cdn/shop/files/rainbow-icon_100x100.png?v=1686338404</u>](https://www.museebath.com/cdn/shop/files/rainbow-icon_100x100.png?v=1686338404) |

## Self-check (master-copywriter §7, 40 questions)

1 Brief: yes (Soph labelled). 2 One performance: a bath made like a pastry. 3 Censor-safe: site lines only. 4 Belief lines: yes. 5 Mechanism: the recipe (real ingredients), described not argued. 6 Structure: story-led welcome. 7 n/a. 8 Stage 2 task: sharpen the image. 9 Brand-specific: pastry chef, Mississippi, second chance, their recipe line. 10 One job: buy Dreamweaver. 11 First sentence under 12: 6. 12 Subject who/what: yes. 13 Opening: the maker. 14 Relevance up front: yes. 15 Accepted first: handmade things are better. 16 Proof after reason: margin notes after the recipe, tickets after the case. 17 Mechanism level: described. 18 Supportable: yes. 19 Three levers: maker, social proof, mission. 20 Scarcity: one true site line ("low in stock"), shown once. 21 Social proof from gift buyers like the reader: yes; no average shown. 22 Discount reason: none. 23 Flaw: none admitted. 24 Compliments: none. 25 Sentence length: short in ours. 26 One-syllable: mostly. 27 "you": S1 subheadline. 28 No could/may/might: yes. 29 Densest: S4 tents. 30 Read aloud: yes. 31 Momentum: light. 32 Offer before ask: free shipping in bar, ticker, meter. 33 Ask as a step: start with Dreamweaver. 34 Guarantee: not found; not invented. 35 Urgency: one true line. 36 P.S.: none. 37 Free to say no: yes. 38 Checkable: §7. 39 Glad after: yes. 40 Ready: yes.
