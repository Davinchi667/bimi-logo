# Copper Cow Coffee · DESIGN INTENT · 2026-10-10 WAT

For: Claude (claude.ai) building from COPY.md, and Design Studio for the three GIFs. 600 px wide, 6 sections, 2,500 px tall, 3 motion moments.

## Signature concept: the 90-second brew clock

The product's whole argument is its own brew card: "Hook filter over your mug. Pour 1 oz hot water, wait 30 sec. Add 3–12 oz more hot water ... Ready in 90 seconds!" S3 draws that as a stopwatch. The brand's four HowTo photos (Tear, Hang, Pour, Enjoy!) sit on the dial like hour marks; a green hand sweeps from 0 to 90 and each photo lights as the hand passes it. Under the dial a strength rail runs from a small mug "3 oz VIETNAMESE STYLE" to a tall glass "12 oz AMERICANO". Leader-line callouts carry the two function claims with the site's own brackets. Proof inside the concept: the brand's brew steps verbatim, "Ready in 90 seconds", and the two "(compared to arabica beans)" lines. S4 continues the pour-over idea: reviews hang on a line like filters hooked over a mug rim, under a 29-review counter and "100% would recommend this product".

## Inspo refs

| **\#** | **Brand / file**                                                                             | **Pose taken**                                                             | **Lands in**                                    |
|--------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|-------------------------------------------------|
| 1      | Ghost · /workspace/design-studio/inspo/mailboard/ghost/newest-202933-desktop.jpg             | Callouts on leader lines around one product; product bleeding off the edge | S1 product crop, S3 callouts                    |
| 2      | Magic Spoon · /workspace/design-studio/inspo/mailboard/magic-spoon/newest-201757-desktop.jpg | Wavy section edges and pastel fields                                       | S2 lime wave edge (matches their own wave PNGs) |
| 3      | Olipop · /workspace/design-studio/inspo/mailboard/olipop/newest-202237-desktop.jpg           | Each product on its own colour block                                       | S6 next-box row                                 |
| 4      | ARMRA · /workspace/design-studio/inspo/mailboard/armra/board-201241-desktop.jpg              | Dashed coupon chip; thin-rule frame                                        | S2 ticket                                       |
| 5      | Copper Cow's own HowTo graphic                                                               | Four circular step photos with hand-lettered labels                        | S3 dial                                         |

## Section map

| **Section**                                                                              | **Pose**                                                                                                                                                      | **Image**                                           | **Motion**      | **Height** |
|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|-----------------|------------|
| S1 Hero                                                                                  | Cream field, pink cow spots from the right, green 2-line headline left, box+pouch+mug cut-out right breaking the bottom edge; green marquee strip at the foot | ClassicHero_1, logo                                 | Yes: M1 marquee | 500        |
| S2 The 15%                                                                               | Green band, lime wave top edge, cream scalloped ticket with "15%", shipping line, button                                                                      | none                                                | No              | 260        |
| S3 Brew clock                                                                            | Cream; 400 px stopwatch in green line, four step photos on the dial, two leader callouts, strength rail, steps listed beside                                  | HowTo crops                                         | Yes: M2 clock   | 640        |
| S4 Brewers                                                                               | Pink spotted field; green slab with 5.0 / 29 / 100%; four reviews as filter-shaped tags hung from a line                                                      | none                                                | Yes: M3 counter | 440        |
| S5 Debbie                                                                                | Green field, cream type left, woman-owned badge right                                                                                                         | womanOwned                                          | No              | 300        |
| S6 Next box + footer                                                                     | Cream; three products on green / lime / pink blocks; button; green footer                                                                                     | Snickerdoodle, Mystery Latte, Vanilla Creamer, logo | No              | 360        |
| Total                                                                                    |                                                                                                                                                               |                                                     | 3               | 2,500      |
| Background sequence: cream, green strip, green, cream, pink, green, cream, green footer. |                                                                                                                                                               |                                                     |                 |            |

## Motion moments (frame 1 is a finished static state)

**M1 · S1 marquee** · 600 x 40 GIF, 6 frames, 400 ms, loop. F1: "CLIMATE RESILIENT → ZERO FAKE → REAL FLAVOR →" readable from the left (static). F2 to F6: shift left 100 px per frame. Cream Poppins 13 px bold caps on \#004E42. **M2 · S3 brew clock** · 420 x 420 GIF, 6 frames, loop, about 5 s. F1 (1,600 ms, static): hand at 90, all four photos lit, centre reads "90 SECONDS". F2 (500 ms): hand at 0, only "Tear" lit, centre "0:00". F3 (500 ms): hand at 10 s, "Hang" lit, "0:10". F4 (700 ms): hand at 30 s, "Pour" lit, "0:30" with a small "wait 30 sec" tag. F5 (700 ms): hand at 60 s, pink fill rising in the rail mug. F6 (1,000 ms): same as F1. Step text and callouts are live HTML outside the GIF. **M3 · S4 counter** · 260 x 120 GIF, 5 frames, no loop, ends on final. F1 (static and final): "29 REVIEWS · 100%". F2 to F4 (250 ms): 0 / 9 / 21 and 0% / 40% / 80%. F5: final. GIF budget about 400 KB. Export each F1 as PNG.

## The one CTA shape

Pill, 54 px tall, fully rounded, \#004E42 fill, cream Poppins 700 caps 15 px; on the green S2 band invert it (cream fill, green text). One wording: SHOP CLASSIC BLACK → [<u>https://coppercowcoffee.com/products/classic-black-vietnamese-pour-over-coffee</u>](https://coppercowcoffee.com/products/classic-black-vietnamese-pour-over-coffee). Product names in S6 are text links, not buttons. The ticket is not a button.

## Palette and type

\#004E42 green (theme), \#00594F, \#13322B deep green, \#F9F7E8 cream (theme), pink sampled from the packs (about \#F2A7C3), lime sampled from the product graphics (about \#C8E86B), white. Poppins (site CSS) for everything; headline 52 px 800, body 16 px. The packs use a chunky rounded display face; if Claude can match it, use it only for the S1 headline and "15%".

## What NOT to do

- No three white review cards: reviews are filter-shaped tags on a line.

- No colour-swap template: no white canvas, centred box, grey footer.

- No three-up roast grid; no generic "coffee beans" stock photos.

- No code lettered anywhere until the brand supplies it; no code in subject or preview.

- No press logo row and no Shark Tank line (quotes are unattributed on the page).

- No health language beyond the two bracketed site lines.

- No emoji (the ⏱️ becomes the drawn clock). No em dash in any layer.

- No mention of the age gate, shipping times or the 4-star review in the email.

## Asset gaps and fallbacks

| **Wanted**             | **Have it?**                   | **Fallback**                                |
|------------------------|--------------------------------|---------------------------------------------|
| Debbie photo           | No URL found on the pages read | Badge + type only                           |
| Isolated pouch cut-out | Composite images only          | Cut from ClassicHero_1 (green background)   |
| Pink spot pattern      | In pack art only               | Redraw the blobs in \#F2A7C3 with a speckle |
