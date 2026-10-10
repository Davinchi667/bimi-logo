# tools/

Everything runs with the system `python3` (3.13) and the Playwright Chromium at /opt/pw-browsers. Dependencies: playwright 1.56, Pillow, numpy, scipy, fonttools, lxml, beautifulsoup4, requests, rembg (+ onnxruntime). `pip install -r tools/requirements.txt` on a fresh machine, then `playwright install chromium` if /opt/pw-browsers is missing (render.py falls back to the default Playwright browser).

## One entry point
```
python3 tools/studio.py scrape https://brand.com --brand slug [--extra URL ...] [--max-images 160] [--no-images]
python3 tools/studio.py qa    brands/<brand>/build.py     # build + validate + render + flat-area + layer list
python3 tools/studio.py gif   brands/<brand>/build.py     # every module GIF + full-email GIF
python3 tools/studio.py all   brands/<brand>/build.py
python3 tools/studio.py test                              # runs qa + gif on tools/examples/demo_build.py
```
Outputs land in brands/<brand>/final/ (`<NAME>.svg`, `<NAME>_600.png`, `<NAME>_1200.png`, `gifs/`, `<NAME>_full.gif`, `review/slice_NN.png`, `review/contact_sheet.png`, `review/flat_heatmap.png`, `review/layers.txt`). NAME defaults to `<brand>_welcome-01`; set `BRAND`, `NAME` and `OUT` (output folder under brands/<brand>/, default `final`) in build.py to override. A second frame such as a popup gets its own `OUT = "final/popup"` so review slices do not collide.

## a) scrape_brand.py (Playwright + requests)
Given a URL, writes brands/<brand>/study/:
- `products.json`: Shopify `/products.json?limit=250` paginated (else sitemap + JSON-LD Product crawl): title, handle, url, price range, variants (price, compare_at, available, sku), tags, type, full-size image URLs (Shopify size suffixes stripped), description text, published_at.
- `fonts.json`: computed font per role (h1, h2, h3, body, button, nav: family, weight, sizes, colour, letter-spacing, text-transform, button radius) plus every `@font-face` (family, weight, style, file URLs) from inline and linked stylesheets; the first file of each face is downloaded to `fonts/` (woff/woff2; load with `fonts.local()` only to study letterforms or when you have the licence).
- `colors.json`: body/header/footer/link computed colours, button bg/colour/radius/border, large section backgrounds, and an 8-colour palette of the homepage screenshot with shares.
- `logos/`: header/footer/nav logos (inline SVG saved as .svg, img downloaded), named `logo_NN_<where>_<dark|light>-marks.<ext>`; tone measured from the file's own colours (dark marks go on light backgrounds). Icons under 48 px wide are skipped. `logos.json` keeps the DOM hints. `favicon.*` next to it.
- `text/*.txt`: homepage, about, faq, reviews, press, ingredients (nav links first, then common /pages/ paths), every `--extra` URL, and the first three products' pages, as visible text with the URL on line 1.
- `reviews.json`: `aggregate` (JSON-LD aggregateRating, or a "4.9 / Based on 7,790 reviews" block printed on the page), `quotes` from Judge.me, Yotpo, Okendo, Stamped, Loox, Reviews.io, Shopify Reviews and generic testimonial cards (text, name as printed, rating_raw, source URL), `count_mentions` ("7,790 reviews" lines). Widgets that render inside an iframe are not read: pass the reviews page as `--extra` and check `text/`.
- `press.json`: images under "as seen in / featured in / in the press / loved by / trusted by" headings (alt + src/svg).
- `offers.json`: announcement bar, visible popups (cart drawers excluded), and lines matching free shipping / % off / subscribe & save / code / guarantee / N reviews, as printed.
- `images.json`, `images/NNN_name.ext` (full-resolution masters, up to --max-images), `contact_sheet_NN.png` (numbered, 40 per sheet).
- `homepage_full.png` (popup closed), `homepage_popup.png` (if one showed), `STUDY.md` (summary + VERIFY list), `scrape.log`.
Every failure is logged and skipped; the scrape never aborts on one page. Cloudflare "verify you are human" pages come back as near-empty text: check `homepage_full.png` first.

## b) image_prep.py (Pillow + numpy + scipy + rembg)
```
image_prep.py download URL out.png                 master file (Shopify size suffix stripped)
image_prep.py cutout in out.png [--mode auto|rembg|white]   transparent cutout: rembg (u2net, alpha matting) or
                                                   border-connected white matte; then defringe (1 px alpha erode +
                                                   edge colour decontamination) so there is no white halo
image_prep.py trim in out.png [--pad N]            crop to the alpha bbox
image_prep.py crop in out.png --box x y w h
image_prep.py fit in out.png --w 600 --h 400 [--mode cover|contain]
image_prep.py textures photo.jpg out_dir --size 300 --n 6     busiest non-overlapping crops of a brand photo, for surfaces
```
Leftover badges ("NEW", price stickers) are not detected automatically: crop them off with `crop` before `cutout`, and look at the result.

## c) emailkit (tools/emailkit/) + validate_svg.py
`Email(fonts, name, bg)` → `section(id, height, bg)` → `Group` methods: `rect rrect circle ellipse line path image text text_block curved_text button stars icon divider g measure wrap`. Local coordinates per section; `Group.g(..., clip=(x,y,w,h))` for tickers and bleeds. `Email.gradient()`, `Email.pattern_dots()` for defs. `Email.module(...)` registers a motion band. `Email.motion_spec_rows()` returns the DELIVERY.md table rows.
Fonts: `fonts = FontRegistry(); fonts.google("Fraunces", weights=(400,700,900))`; `fonts.substitute("GT Alpina Typewriter", "Courier Prime", weights=(400,700))` records the substitution for the delivery note (`fonts.figma_report()`); `fonts.local("Family", "path.woff2", weight)` for files on disk. Text widths come from the TTF (advance widths + kern table), so `text_block(..., max_lines=N)` raises when copy does not fit instead of overflowing.
`validate_svg.py email.svg --fonts-from build.py` fails on: nested tspan, textPath, `<g>` without a readable id, glyph icons (★ ✓ → ...), non-embedded images, non-numeric font-weight, text under 14 px outside a `footer` group, text outside the 30 px margins (unless inside a clipped group), file over 6 MB. Warns on duplicate ids, dashes, double spaces, empty text.

## d) render.py (Playwright)
`render.py email.svg --out dir --fonts-from build.py --name NAME` → `NAME_600.png` (1x), `NAME_1200.png` (2x), `review/slice_NN.png` (600 px tall, 1x) and `review/contact_sheet.png`. The SVG is wrapped in an HTML page with `@font-face` data URIs for every registered font so Chromium uses the exact files the widths were measured with.

## e) build_gif.py (Pillow)
`build_gif.py build.py --out dir --name NAME`. For each registered module it calls `build({"M1": k})` for k in 0..states-1, renders the full SVG, crops the band (600 x h at y), and asserts state 0 equals the static PNG band pixel for pixel. Frames get ONE shared median-cut palette (no flicker), Floyd-Steinberg dither, `disposal=1`, `loop=0`; the palette shrinks 256 → 32 colours until the file is about 1 MB (hard max 2.5 MB, else it raises with what to shrink). `tween_frames=N` adds N 40 ms crossfade frames between held states. The full-email GIF composites every module band onto the static email on a common timeline (LCM of loop lengths, capped at ~12 s), frame 1 = the complete static email, 2.5 MB max. gifski is not installed; add it to PATH and swap `save_gif` if sizes get tight.

## f) flat_area.py
`flat_area.py NAME_600.png --heatmap out.png`: 10 px blocks, flat when every channel's range ≤ 6; prints the overall share (must be < 60 %) and the share per 600 px band, and tints flat blocks magenta in the heatmap.

## g) Figma import test
See `figma_import.md`. The Figma MCP is connected (David's team, Starter plan); the quota is small. `svg_layers.py email.svg` prints the expected layer tree (ids, y, text/word/image counts) to compare with `get_metadata`.

## Helpers added during the first batch
- `svg_to_png.py logo.svg out.png --width 1200`: rasterise a brand logo SVG with Chromium (transparent PNG) when its path data does not survive extraction (nested transforms, fill rules). Use the PNG via `Group.image`.
- `svg_layers.py` + `batch_overview.py brands/BATCH_<date>_overview.jpg --scale 0.22`: the layer tree for Figma checks, and all final PNGs side by side at one scale.
- `FontRegistry.substitute(..., italics=True)` loads italic cuts for a substitute family. `Group.text_runs_block` wraps mixed-weight text (bolded phrases inside a quote). `Group.g(..., rotate=deg)` for tilted cards, tags and prints. `shapes.drop / paperclip / binder_clip / staple` for the small props.
- Build-script conventions that kept QA green: dynamic section heights (`e.section_h[...]`, `e.y`, and replace `children[0]` for the background rect); measure before placing (`wrap`, `measure`) so tags and cards grow with their copy; a light grain JPEG on every flat field (flat-area check); clipped groups for tickers; `OUT = "final/popup"` for a second frame.

## Known limits
- Instagram and other logged-in sources are not scraped; pass product and review URLs as `--extra`.
- Review widgets in iframes are invisible to the DOM pass.
- GPOS kerning (most modern fonts) is not applied in width measurement; the kern table is. Widths err a few px wide, never narrow, for most fonts: keep 10 px of slack on the right of any measured line.
- Figma does not import `pattern` fills or `filter`s reliably; use solid, gradient or image fills.
