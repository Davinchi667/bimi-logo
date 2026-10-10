# Figma import test

Goal: prove the SVG lands in Figma with every image present, no empty text, sections at the right y, and know which fonts Figma used.

Scratch file (created 2026-10-10, David's team): https://www.figma.com/design/cjajeKw9lAXIrfn6SxXmF1

## Procedure (Figma MCP)
1. `mcp__Figma__upload_assets` with `fileKey=cjajeKw9lAXIrfn6SxXmF1`, `count=1`. It returns a single-use `submitUrl`.
2. POST the SVG as multipart (the filename becomes the layer name):
   ```
   curl -sS -X POST "<submitUrl>" -F "file=@brands/<brand>/final/<brand>_welcome-01.svg;type=image/svg+xml;filename=<brand>_welcome-01.svg"
   ```
   The response gives `placedOnNodeId` (e.g. `1:2`).
3. `mcp__Figma__get_metadata` on that node: compare the layer tree with `python3 tools/svg_layers.py <svg>` (group names, y positions, text and image counts).
4. `mcp__Figma__get_screenshot` on the node at `maxDimension` = email height: compare with `final/<name>_600.png`. Any glyph that turned into a box, any empty text, any missing image = fix the SVG and re-import.
5. Fonts: Figma keeps the family name from `font-family`; anything not installed/available in Figma shows as Inter with a "missing font" badge. Google Fonts are available. Record what was used in DELIVERY.md.

## Quota
The Starter plan allows only a handful of MCP calls per period. On 2026-10-10 the demo upload succeeded (node 1:2) but `get_metadata` and `get_screenshot` hit the limit. When that happens, open the file in Figma and check by eye: Layers panel for names and empty text, Text > Missing fonts for substitutions.

## What breaks at import (and how the builder avoids it)
| Problem | Cause | Builder rule |
|---|---|---|
| Whole text block disappears | nested `<tspan>` | validator fails on it; builder never emits it |
| Curved text gone | `<textPath>` | one `<text>` per letter with rotate() |
| Stars become tofu boxes | glyph characters | `shapes.star` paths |
| Layer names "Group 12" | `<g>` without id | every `Group` needs an id |
| Images missing | external href | base64 data URIs only |
| Font swapped to Inter | font not in Figma | Google Fonts or a named substitute |
