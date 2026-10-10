#!/usr/bin/env python3
"""Brand scraper: everything a spec email needs, saved to brands/<brand>/study/.

  scrape_brand.py https://brand.com [--brand slug] [--extra URL ...] [--max-images 160] [--no-images]

Writes
  products.json       every product (Shopify /products.json, else JSON-LD crawl): title, handle,
                      url, price, compare_at, variants, tags, type, images (full size), description text
  fonts.json          computed font per role (h1 h2 h3 body button nav) + every @font-face with file URLs;
                      font files downloaded to fonts/
  colors.json         computed colours (body, header, footer, buttons, links, big sections) + screenshot palette
  logos/              header/footer logo files (svg/png), light/dark guesses by filename; favicon
  text/*.txt          homepage, about, faq, reviews, press, extra pages as visible text (URL on line 1)
  reviews.json        aggregate rating/count (JSON-LD, widgets) + review quotes with names AS PRINTED + source URL
  press.json          "as seen in / featured in" logos (alt + file)
  offers.json         announcement bar, popup text, free-shipping / % off / subscribe & save lines AS PRINTED
  images.json + images/ + contact_sheet_NN.png    every image found, numbered
  homepage_full.png (popup closed), homepage_popup.png (if a popup showed)
  STUDY.md            one-page summary with a VERIFY list
  scrape.log

Nothing here invents: every field is copied from the site or left empty.
"""
from __future__ import annotations

import argparse
import io
import json
import re
import sys
import time
import traceback
from collections import Counter
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
from image_prep import full_res_url  # noqa: E402

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
HDR = {"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"}
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
ROOT = Path(__file__).resolve().parent.parent

PAGE_GUESSES = {
    "about": ["/pages/about", "/pages/about-us", "/pages/our-story", "/pages/story", "/pages/mission", "/about", "/about-us", "/our-story"],
    "faq": ["/pages/faq", "/pages/faqs", "/pages/frequently-asked-questions", "/faq", "/faqs", "/pages/help"],
    "reviews": ["/pages/reviews", "/pages/testimonials", "/reviews", "/pages/customer-reviews"],
    "press": ["/pages/press", "/press", "/pages/in-the-press", "/pages/media"],
    "ingredients": ["/pages/ingredients", "/pages/science", "/pages/how-it-works"],
}
NAV_WORDS = {"about": r"about|story|mission|who we are|why", "faq": r"faq|help|questions", "reviews": r"review|testimonial|love",
             "press": r"press|media|featured", "ingredients": r"ingredient|science|how it works|benefit"}

REVIEW_WIDGETS = [  # (container, body, author, rating attr/selector)
    (".jdgm-rev", ".jdgm-rev__body", ".jdgm-rev__author", ".jdgm-rev__rating"),
    (".yotpo-review", ".content-review", ".yotpo-user-name", ".yotpo-review-stars"),
    (".oke-w-review", ".oke-reviewContent-body", ".oke-w-reviewer-name", ".oke-stars"),
    (".stamped-review", ".stamped-review-content-body", ".author", ".stamped-starratings"),
    (".loox-review", ".review-text", ".review-author", ".loox-rating"),
    (".R-ReviewsList__item", ".R-ReviewsList__item--body", ".R-ReviewsList__item--author", ".R-RatingStars"),  # reviews.io
    (".spr-review", ".spr-review-content-body", ".spr-review-header-byline", ".spr-starratings"),  # shopify product reviews
    ("[class*='testimonial']", "p, blockquote, [class*='text'], [class*='quote']", "[class*='name'], [class*='author'], cite, figcaption", "[class*='star']"),
    ("[class*='review-card'], [class*='review_card'], [class*='reviewCard']", "p, [class*='body'], [class*='text'], [class*='content']", "[class*='name'], [class*='author'], cite, figcaption, strong", "[class*='star']"),
]

log_lines: list[str] = []


def log(msg):
    print(msg)
    log_lines.append(f"{time.strftime('%H:%M:%S')} {msg}")


def slugify(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def get(url, **kw):
    try:
        return requests.get(url, headers=HDR, timeout=kw.pop("timeout", 40), **kw)
    except requests.RequestException as e:
        log(f"  GET failed {url}: {e}")
        return None


def strip_html(html: str) -> str:
    return re.sub(r"\s+\n", "\n", BeautifulSoup(html or "", "lxml").get_text("\n")).strip()


# --------------------------------------------------------------------------- products
def shopify_products(base: str) -> list[dict]:
    out = []
    for page in range(1, 20):
        r = get(f"{base}/products.json?limit=250&page={page}")
        if not r or r.status_code != 200 or not r.headers.get("content-type", "").startswith("application/json"):
            break
        try:
            items = r.json().get("products", [])
        except ValueError:
            break
        if not items:
            break
        for p in items:
            prices = [float(v["price"]) for v in p.get("variants", []) if v.get("price")]
            out.append({
                "title": p["title"], "handle": p["handle"], "url": f"{base}/products/{p['handle']}",
                "type": p.get("product_type"), "vendor": p.get("vendor"), "tags": p.get("tags"),
                "price_min": min(prices) if prices else None, "price_max": max(prices) if prices else None,
                "variants": [{"title": v["title"], "price": v["price"], "compare_at_price": v.get("compare_at_price"),
                              "available": v.get("available"), "sku": v.get("sku")} for v in p.get("variants", [])],
                "images": [full_res_url(im["src"]) for im in p.get("images", [])],
                "description": strip_html(p.get("body_html", ""))[:3000],
                "published_at": p.get("published_at"),
            })
        if len(items) < 250:
            break
    return out


def jsonld_products(base: str, page_html_fetch, limit=40) -> list[dict]:
    """Fallback for non-Shopify: product URLs from sitemap or /collections/all, JSON-LD Product on each."""
    urls = []
    for sm in ("/sitemap.xml", "/sitemap_products_1.xml", "/product-sitemap.xml"):
        r = get(base + sm)
        if r and r.status_code == 200 and "<loc>" in r.text:
            urls += [u for u in re.findall(r"<loc>(.*?)</loc>", r.text) if "/product" in u]
    urls = list(dict.fromkeys(urls))[:limit]
    out = []
    for u in urls:
        r = get(u)
        if not r or r.status_code != 200:
            continue
        soup = BeautifulSoup(r.text, "lxml")
        for s in soup.find_all("script", type="application/ld+json"):
            try:
                data = json.loads(s.string or "")
            except ValueError:
                continue
            for d in (data if isinstance(data, list) else [data]):
                if isinstance(d, dict) and d.get("@type") in ("Product", ["Product"]):
                    offers = d.get("offers") or {}
                    if isinstance(offers, list):
                        offers = offers[0] if offers else {}
                    imgs = d.get("image") or []
                    out.append({"title": d.get("name"), "handle": urlparse(u).path.rstrip("/").split("/")[-1], "url": u,
                                "price_min": offers.get("price") or offers.get("lowPrice"), "price_max": offers.get("highPrice") or offers.get("price"),
                                "variants": [], "images": [full_res_url(i) for i in (imgs if isinstance(imgs, list) else [imgs])],
                                "description": strip_html(d.get("description", ""))[:3000], "source": "jsonld"})
    return out


# --------------------------------------------------------------------------- browser helpers
JS_FONTS = r"""
() => {
  const roles = {h1:'h1', h2:'h2', h3:'h3', body:'p, li', button:"button, a.btn, a.button, [class*='btn'], [class*='button'], input[type=submit]", nav:"nav a, header a"};
  const vis = el => { const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); return r.width>0 && r.height>0 && cs.visibility!=='hidden' && cs.display!=='none' && (el.innerText||'').trim().length>0; };
  const out = {};
  for (const [role, sel] of Object.entries(roles)) {
    const els = [...document.querySelectorAll(sel)].filter(vis).slice(0, 40);
    out[role] = els.map(el => { const cs = getComputedStyle(el); return {
      family: cs.fontFamily, weight: cs.fontWeight, size: cs.fontSize, color: cs.color, bg: cs.backgroundColor,
      letterSpacing: cs.letterSpacing, transform: cs.textTransform, lineHeight: cs.lineHeight, radius: cs.borderRadius,
      border: cs.border, sample: (el.innerText||'').trim().slice(0, 80) }; });
  }
  return out;
}
"""

JS_COLORS = r"""
() => {
  const rgb = c => c;
  const pick = sel => { const el = document.querySelector(sel); if(!el) return null; const cs = getComputedStyle(el); return {bg: cs.backgroundColor, color: cs.color}; };
  const res = { body: pick('body'), header: pick('header, [class*="header"]'), footer: pick('footer, [class*="footer"]'), link: pick('a') };
  const secs = [...document.querySelectorAll('section, main > div, body > div > div')].map(el => { const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); return {area: r.width*r.height, bg: cs.backgroundColor, color: cs.color, tag: el.tagName, cls: (el.className||'').toString().slice(0,60)}; }).filter(s => s.area > 200000 && s.bg !== 'rgba(0, 0, 0, 0)').slice(0, 40);
  res.sections = secs;
  return res;
}
"""

JS_LOGOS = r"""
() => {
  const out = [];
  const scope = [...document.querySelectorAll('header, [class*="header"], nav, footer, [class*="logo"]')];
  const seen = new Set();
  for (const root of scope) {
    for (const el of root.querySelectorAll('img, svg, a[class*="logo"]')) {
      const hint = ((el.getAttribute('alt')||'') + ' ' + (el.className && el.className.baseVal !== undefined ? el.className.baseVal : el.className||'') + ' ' + (el.getAttribute('src')||'') + ' ' + ((el.closest('a')||{}).className||'')).toLowerCase();
      const isLogo = hint.includes('logo') || hint.includes('brand') || (el.closest('a') && (el.closest('a').getAttribute('href')||'') === '/');
      if (!isLogo) continue;
      const r = el.getBoundingClientRect();
      if (r.width > 0 && r.width < 48) continue;   // icons, not logos
      const cs = getComputedStyle(el);
      if (el.tagName.toLowerCase() === 'svg') {
        const s = el.outerHTML; if (seen.has(s)) continue; seen.add(s);
        out.push({kind: 'inline-svg', svg: s, w: r.width, h: r.height, hint, where: root.tagName.toLowerCase(), color: cs.color, fill: cs.fill});
      } else if (el.tagName.toLowerCase() === 'img') {
        const src = el.currentSrc || el.src || el.getAttribute('data-src'); if (!src || seen.has(src)) continue; seen.add(src);
        out.push({kind: 'img', src, alt: el.alt, w: r.width, h: r.height, hint, where: root.tagName.toLowerCase()});
      }
    }
  }
  const fav = [...document.querySelectorAll('link[rel*="icon"]')].map(l => l.href);
  return {logos: out, favicons: fav};
}
"""

JS_IMAGES = r"""
() => {
  const out = [];
  for (const img of document.querySelectorAll('img')) {
    let src = img.currentSrc || img.src || img.getAttribute('data-src') || '';
    const ss = img.getAttribute('srcset') || img.getAttribute('data-srcset') || '';
    if (ss) { const parts = ss.split(',').map(s => s.trim().split(/\s+/)); parts.sort((a,b) => (parseInt(b[1]||'0') - parseInt(a[1]||'0'))); if (parts[0] && parts[0][0]) src = parts[0][0]; }
    if (!src || src.startsWith('data:')) continue;
    const r = img.getBoundingClientRect();
    out.push({src, alt: img.alt || '', w: Math.round(r.width), h: Math.round(r.height), natural: [img.naturalWidth, img.naturalHeight]});
  }
  for (const el of document.querySelectorAll('*')) {
    const bg = getComputedStyle(el).backgroundImage;
    if (bg && bg.startsWith('url(')) { const m = bg.match(/url\(["']?(.*?)["']?\)/); if (m && !m[1].startsWith('data:')) { const r = el.getBoundingClientRect(); out.push({src: m[1], alt: '(background)', w: Math.round(r.width), h: Math.round(r.height)}); } }
  }
  return out;
}
"""

JS_POPUP = r"""
() => {
  const vis = el => { const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); return r.width>200 && r.height>100 && cs.visibility!=='hidden' && cs.display!=='none' && parseFloat(cs.opacity||'1')>0.1; };
  const sels = '[role="dialog"], [class*="popup"], [class*="modal"], [class*="klaviyo"], [class*="newsletter"], [id*="popup"], [class*="Popup"], [class*="lightbox"], .needsclick';
  const texts = [];
  for (const el of document.querySelectorAll(sels)) { if (!vis(el)) continue; const t = (el.innerText||'').trim(); if (/^cart\b|^your (cart|bag)/i.test(t)) continue; if (t.length > 20 && t.length < 2000) texts.push(t); }
  const bar = [...document.querySelectorAll('[class*="announcement"], [class*="Announcement"], [class*="promo-bar"], [class*="topbar"], [class*="top-bar"], [id*="announcement"]')].filter(vis).map(el => (el.innerText||'').trim()).filter(Boolean);
  return {popups: [...new Set(texts)], announcement: [...new Set(bar)]};
}
"""

JS_CLOSE = r"""
() => {
  let n = 0;
  const sels = '[aria-label*="close" i], [aria-label*="dismiss" i], .klaviyo-close-form, button[class*="close" i], [class*="close-button" i], [class*="closeButton"], [class*="modal__close"], [class*="popup__close"], [data-testid*="close" i]';
  for (const b of document.querySelectorAll(sels)) { const r = b.getBoundingClientRect(); if (r.width>0 && r.height>0) { try { b.click(); n++; } catch(e){} } }
  return n;
}
"""

JS_REVIEWS = r"""
(widgets) => {
  const out = [];
  for (const [cont, body, author, rating] of widgets) {
    for (const el of document.querySelectorAll(cont)) {
      const b = el.querySelector(body); const a = el.querySelector(author); const r = el.querySelector(rating);
      const text = b ? (b.innerText||'').trim() : '';
      if (text.length < 15) continue;
      let stars = null;
      if (r) { stars = r.getAttribute('data-score') || r.getAttribute('aria-label') || r.getAttribute('title') || (r.innerText||'').trim() || null; const svg = r.querySelectorAll('svg, i, span').length; if (!stars && svg) stars = svg + ' star elements'; }
      out.push({widget: cont, text: text.slice(0, 600), name: a ? (a.innerText||'').trim().slice(0, 80) : null, rating_raw: stars});
    }
    if (out.length) break;
  }
  return out;
}
"""

JS_PRESS = r"""
() => {
  const out = [];
  const heads = [...document.querySelectorAll('h1,h2,h3,h4,h5,p,span,div')].filter(el => /as seen in|featured in|as featured|in the press|press mentions|loved by|trusted by|as seen on/i.test((el.innerText||'').trim().slice(0,60)) && (el.innerText||'').trim().length < 60);
  for (const h of heads.slice(0, 6)) {
    const sec = h.closest('section') || h.parentElement && h.parentElement.parentElement || h.parentElement;
    if (!sec) continue;
    const imgs = [...sec.querySelectorAll('img, svg')].slice(0, 20).map(i => ({src: i.currentSrc || i.src || null, alt: i.getAttribute('alt') || i.getAttribute('aria-label') || null, svg: i.tagName.toLowerCase()==='svg' ? i.outerHTML.slice(0, 20000) : null}));
    if (imgs.length) out.push({heading: (h.innerText||'').trim(), items: imgs});
  }
  return out;
}
"""

JS_JSONLD = r"""
() => [...document.querySelectorAll('script[type="application/ld+json"]')].map(s => s.textContent)
"""

JS_LINKS = r"""
() => [...document.querySelectorAll('a[href]')].map(a => ({href: a.href, text: (a.innerText||'').trim().slice(0,60)}))
"""


def scroll_through(page, step=900, pause=250):
    h = page.evaluate("document.body.scrollHeight")
    y = 0
    while y < h and y < 30000:
        page.evaluate(f"window.scrollTo(0,{y})")
        page.wait_for_timeout(pause)
        y += step
        h = page.evaluate("document.body.scrollHeight")
    page.evaluate("window.scrollTo(0,0)")
    page.wait_for_timeout(400)


def rgb_to_hex(c: str) -> str | None:
    m = re.match(r"rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)", c or "")
    if not m:
        return None
    if m.group(4) is not None and float(m.group(4)) == 0:
        return None
    return "#{:02X}{:02X}{:02X}".format(int(m.group(1)), int(m.group(2)), int(m.group(3)))


def parse_font_faces(css: str, base_url: str) -> list[dict]:
    faces = []
    for block in re.findall(r"@font-face\s*{([^}]*)}", css, flags=re.I | re.S):
        fam = re.search(r"font-family\s*:\s*['\"]?([^;'\"]+)", block, re.I)
        w = re.search(r"font-weight\s*:\s*([^;]+)", block, re.I)
        st = re.search(r"font-style\s*:\s*([^;]+)", block, re.I)
        srcs = re.findall(r"url\(\s*['\"]?([^'\")]+)['\"]?\s*\)", block)
        if fam:
            faces.append({"family": fam.group(1).strip(), "weight": (w.group(1).strip() if w else "400"),
                          "style": (st.group(1).strip() if st else "normal"),
                          "files": [urljoin(base_url, s) for s in srcs if not s.strip().startswith("data:")]})
    return faces


def _lum(hexc: str) -> float:
    hexc = hexc.lstrip("#")
    if len(hexc) == 3:
        hexc = "".join(c * 2 for c in hexc)
    r, g, b = int(hexc[0:2], 16), int(hexc[2:4], 16), int(hexc[4:6], 16)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def logo_tone(kind: str, data, computed_color: str | None = None) -> str:
    """'dark' = dark marks (for light backgrounds), 'light' = light marks (for dark backgrounds).
    SVG: average luminance of fill/stroke colours (currentColor -> computed colour).
    Raster: mean luminance of opaque pixels."""
    try:
        if kind == "inline-svg" or (isinstance(data, bytes) and data[:200].lstrip().startswith((b"<svg", b"<?xml"))):
            txt = data if isinstance(data, str) else data.decode("utf-8", "ignore")
            cols = re.findall(r"(?:fill|stroke)\s*[:=]\s*[\"']?(#[0-9a-fA-F]{3,6}|rgb\([^)]*\)|currentColor)", txt)
            lums = []
            for c in cols:
                if c == "currentColor":
                    h = rgb_to_hex(computed_color or "")
                    if h:
                        lums.append(_lum(h))
                elif c.startswith("rgb"):
                    h = rgb_to_hex(c)
                    if h:
                        lums.append(_lum(h))
                else:
                    lums.append(_lum(c))
            if not lums:
                h = rgb_to_hex(computed_color or "")
                lums = [_lum(h)] if h else [0]
            return "light" if sum(lums) / len(lums) > 140 else "dark"
        im = Image.open(io.BytesIO(data)).convert("RGBA")
        import numpy as np
        a = np.asarray(im)
        mask = a[:, :, 3] > 128
        if not mask.any():
            return "dark"
        rgb = a[:, :, :3][mask].astype(float)
        lum = (0.2126 * rgb[:, 0] + 0.7152 * rgb[:, 1] + 0.0722 * rgb[:, 2]).mean()
        return "light" if lum > 140 else "dark"
    except Exception:
        return "unknown"


def palette_from_image(im: Image.Image, n=8):
    small = im.convert("RGB").resize((200, int(200 * im.height / im.width) or 1))
    q = small.quantize(colors=n, method=Image.Quantize.MEDIANCUT)
    pal = q.getpalette()[: n * 3]
    import numpy as np
    counts = Counter(np.asarray(q).ravel().tolist())
    total = sum(counts.values())
    rows = []
    for idx, c in counts.most_common(n):
        r, g, b = pal[idx * 3: idx * 3 + 3]
        rows.append({"hex": "#{:02X}{:02X}{:02X}".format(r, g, b), "share": round(c / total, 3)})
    return rows


def summarise_fonts(raw: dict) -> dict:
    out = {}
    for role, rows in raw.items():
        if not rows:
            out[role] = None
            continue
        fam = Counter(r["family"] for r in rows).most_common(1)[0][0]
        same = [r for r in rows if r["family"] == fam]
        out[role] = {
            "family_stack": fam, "family": fam.split(",")[0].strip("'\" "),
            "weight": Counter(r["weight"] for r in same).most_common(1)[0][0],
            "sizes": [s for s, _ in Counter(r["size"] for r in same).most_common(3)],
            "color": Counter(rgb_to_hex(r["color"]) for r in same).most_common(1)[0][0],
            "bg": Counter(rgb_to_hex(r["bg"]) for r in same).most_common(1)[0][0] if role == "button" else None,
            "letter_spacing": Counter(r["letterSpacing"] for r in same).most_common(1)[0][0],
            "transform": Counter(r["transform"] for r in same).most_common(1)[0][0],
            "radius": Counter(r["radius"] for r in same).most_common(1)[0][0] if role == "button" else None,
            "samples": [r["sample"] for r in same[:3]],
        }
    return out


def contact_sheets(img_dir: Path, records: list[dict], out_dir: Path, per_sheet=40, cols=5, cell=220):
    font = ImageFont.load_default()
    sheets = []
    for si in range(0, len(records), per_sheet):
        chunk = records[si: si + per_sheet]
        rows = -(-len(chunk) // cols)
        sheet = Image.new("RGB", (cols * cell, rows * (cell + 36)), "#F2F2F2")
        d = ImageDraw.Draw(sheet)
        for i, rec in enumerate(chunk):
            r, c = divmod(i, cols)
            x, y = c * cell, r * (cell + 36)
            try:
                im = Image.open(img_dir / rec["file"]).convert("RGBA")
                im.thumbnail((cell - 12, cell - 12))
                bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
                bg.alpha_composite(im)
                sheet.paste(bg.convert("RGB"), (x + 6 + (cell - 12 - im.width) // 2, y + 6 + (cell - 12 - im.height) // 2))
            except Exception:
                d.text((x + 10, y + 100), "load failed", fill="#900", font=font)
            d.rectangle([x, y + cell, x + cell, y + cell + 36], fill="#FFFFFF")
            d.text((x + 6, y + cell + 3), f"#{rec['index']:03d} {rec.get('size') or ''}", fill="#000", font=font)
            d.text((x + 6, y + cell + 18), (rec.get("alt") or rec.get("product") or rec.get("page") or "")[:34], fill="#555", font=font)
        p = out_dir / f"contact_sheet_{si // per_sheet + 1:02d}.png"
        sheet.save(p)
        sheets.append(p)
    return sheets


# --------------------------------------------------------------------------- main
def scrape(url: str, brand: str | None, extra: list[str], max_images: int, do_images: bool):
    from playwright.sync_api import sync_playwright

    u = urlparse(url if "://" in url else "https://" + url)
    base = f"{u.scheme}://{u.netloc}"
    brand = brand or slugify(u.netloc.replace("www.", "").split(".")[0])
    study = ROOT / "brands" / brand / "study"
    for sub in ("logos", "fonts", "text", "images"):
        (study / sub).mkdir(parents=True, exist_ok=True)
    for sub in ("logos", "text"):          # regenerated every run; images/ and fonts/ are kept
        for old in (study / sub).iterdir():
            if old.is_file():
                old.unlink()
    log(f"brand={brand} base={base} -> {study}")
    summary = {"brand": brand, "url": base}

    # products
    products = shopify_products(base)
    summary["platform"] = "shopify" if products else "unknown"
    if not products:
        log("no /products.json; trying sitemap + JSON-LD")
        products = jsonld_products(base, None)
    (study / "products.json").write_text(json.dumps(products, indent=2, ensure_ascii=False))
    log(f"products: {len(products)}")

    fonts_json = {"roles": {}, "font_faces": [], "downloaded": []}
    colors_json = {}
    reviews_json = {"aggregate": [], "quotes": []}
    offers_json = {"announcement": [], "popups": [], "lines": []}
    press_json = []
    images: list[dict] = []
    pages_text: dict[str, str] = {}
    page_urls: dict[str, str] = {}

    with sync_playwright() as pw:
        try:
            browser = pw.chromium.launch()
        except Exception:
            browser = pw.chromium.launch(executable_path=CHROME)
        ctx = browser.new_context(user_agent=UA, viewport={"width": 1440, "height": 900}, locale="en-US")
        page = ctx.new_page()

        def visit(target, wait=2500):
            page.goto(target, wait_until="domcontentloaded", timeout=60000)
            page.wait_for_timeout(wait)
            return page.url

        # ---- homepage
        try:
            visit(base, 4000)
            pop = page.evaluate(JS_POPUP)
            offers_json["popups"] = pop["popups"]
            offers_json["announcement"] = pop["announcement"]
            if pop["popups"]:
                page.screenshot(path=str(study / "homepage_popup.png"), full_page=False)
                page.keyboard.press("Escape")
                n = page.evaluate(JS_CLOSE)
                page.wait_for_timeout(800)
                log(f"popup captured, closed {n} control(s)")
            scroll_through(page)
            raw_fonts = page.evaluate(JS_FONTS)
            fonts_json["roles"] = summarise_fonts(raw_fonts)
            fonts_json["raw_samples"] = {k: v[:6] for k, v in raw_fonts.items()}
            colors_json = page.evaluate(JS_COLORS)
            for k in ("body", "header", "footer", "link"):
                if colors_json.get(k):
                    colors_json[k] = {kk: rgb_to_hex(vv) for kk, vv in colors_json[k].items()}
            colors_json["sections"] = [{"bg": rgb_to_hex(s["bg"]), "color": rgb_to_hex(s["color"]), "tag": s["tag"], "class": s["cls"]} for s in colors_json.get("sections", [])]
            colors_json["buttons"] = [{"bg": rgb_to_hex(r["bg"]), "color": rgb_to_hex(r["color"]), "radius": r["radius"], "border": r["border"], "sample": r["sample"]} for r in raw_fonts.get("button", [])[:8]]
            # font faces from all stylesheets
            sheets = page.evaluate("() => [...document.styleSheets].map(s => s.href).filter(Boolean)")
            inline_css = page.evaluate("() => [...document.querySelectorAll('style')].map(s => s.textContent).join('\\n')")
            faces = parse_font_faces(inline_css, base)
            for href in sheets[:40]:
                r = get(href)
                if r and r.status_code == 200:
                    faces += parse_font_faces(r.text, href)
            seen = set()
            for f in faces:
                key = (f["family"], f["weight"], f["style"])
                if key in seen or not f["files"]:
                    continue
                seen.add(key)
                fonts_json["font_faces"].append(f)
                for fu in f["files"][:1]:
                    ext = Path(urlparse(fu).path).suffix or ".bin"
                    name = f"{slugify(f['family'])}-{slugify(f['weight'])}{'-italic' if 'ital' in f['style'] else ''}{ext}"
                    rr = get(fu)
                    if rr and rr.status_code == 200 and len(rr.content) > 1000:
                        (study / "fonts" / name).write_bytes(rr.content)
                        fonts_json["downloaded"].append({"family": f["family"], "weight": f["weight"], "file": f"fonts/{name}", "url": fu})
            log(f"fonts: roles={ {k: (v or {}).get('family') for k, v in fonts_json['roles'].items()} } faces={len(fonts_json['font_faces'])} files={len(fonts_json['downloaded'])}")
            # logos + favicon
            lg = page.evaluate(JS_LOGOS)
            li = 0
            for l in lg["logos"]:
                li += 1
                if l["kind"] == "inline-svg":
                    tone = logo_tone("inline-svg", l["svg"], l.get("color"))
                    p = study / "logos" / f"logo_{li:02d}_{l['where']}_{tone}-marks.svg"
                    p.write_text(l["svg"])
                else:
                    r = get(l["src"])
                    if r and r.status_code == 200:
                        ext = ".svg" if "svg" in r.headers.get("content-type", "") or l["src"].lower().endswith(".svg") else Path(urlparse(l["src"]).path).suffix or ".png"
                        tone = logo_tone("raster", r.content)
                        p = study / "logos" / f"logo_{li:02d}_{l['where']}_{tone}-marks{ext}"
                        p.write_bytes(r.content)
                    else:
                        continue
                l["tone"] = tone
                l["file"] = f"logos/{p.name}"
            (study / "logos" / "logos.json").write_text(json.dumps(lg, indent=2))
            fav = lg["favicons"][0] if lg["favicons"] else base + "/favicon.ico"
            r = get(fav)
            if r and r.status_code == 200:
                ext = Path(urlparse(fav).path).suffix or ".ico"
                (study / f"favicon{ext}").write_bytes(r.content)
            log(f"logos: {len(lg['logos'])}, favicon: {fav}")
            # text, reviews, press, offers, jsonld
            pages_text["homepage"] = page.evaluate("() => document.body.innerText")
            page_urls["homepage"] = base
            reviews_json["quotes"] += [dict(q, source=base) for q in page.evaluate(JS_REVIEWS, REVIEW_WIDGETS)]
            press_json += [dict(p, source=base) for p in page.evaluate(JS_PRESS)]
            for s in page.evaluate(JS_JSONLD):
                try:
                    d = json.loads(s)
                except ValueError:
                    continue
                for node in (d if isinstance(d, list) else [d]):
                    if isinstance(node, dict):
                        ar = node.get("aggregateRating")
                        if ar:
                            reviews_json["aggregate"].append({"source": base, "name": node.get("name"), "rating": ar.get("ratingValue"), "count": ar.get("reviewCount") or ar.get("ratingCount")})
            links = page.evaluate(JS_LINKS)
            if do_images:
                images += [dict(i, page="homepage") for i in page.evaluate(JS_IMAGES)]
            page.screenshot(path=str(study / "homepage_full.png"), full_page=True)
            log("homepage captured")
        except Exception as e:
            log(f"homepage step failed: {e}\n{traceback.format_exc()}")
            links = []

        # ---- secondary pages (nav links first, then guesses)
        targets: dict[str, str] = {}
        for kind, pat in NAV_WORDS.items():
            for l in links:
                if re.search(pat, l["text"], re.I) and urlparse(l["href"]).netloc == u.netloc and kind not in targets:
                    targets[kind] = l["href"]
        for kind, paths in PAGE_GUESSES.items():
            if kind in targets:
                continue
            for pth in paths:
                r = get(base + pth, allow_redirects=True)
                if r and r.status_code == 200 and "/404" not in r.url:
                    targets[kind] = base + pth
                    break
        for i, ex in enumerate(extra):
            targets[f"extra_{i + 1}"] = ex
        for kind, target in targets.items():
            try:
                final = visit(target, 5000 if kind == "reviews" else 2500)
                page.keyboard.press("Escape")
                page.evaluate(JS_CLOSE)
                scroll_through(page, pause=150)
                pages_text[kind] = page.evaluate("() => document.body.innerText")
                page_urls[kind] = final
                reviews_json["quotes"] += [dict(q, source=final) for q in page.evaluate(JS_REVIEWS, REVIEW_WIDGETS)]
                press_json += [dict(p, source=final) for p in page.evaluate(JS_PRESS)]
                for s in page.evaluate(JS_JSONLD):
                    try:
                        d = json.loads(s)
                    except ValueError:
                        continue
                    for node in (d if isinstance(d, list) else [d]):
                        if isinstance(node, dict) and node.get("aggregateRating"):
                            ar = node["aggregateRating"]
                            reviews_json["aggregate"].append({"source": final, "name": node.get("name"), "rating": ar.get("ratingValue"), "count": ar.get("reviewCount") or ar.get("ratingCount")})
                if do_images and kind in ("about", "press", "ingredients") or kind.startswith("extra"):
                    images += [dict(i, page=kind) for i in page.evaluate(JS_IMAGES)]
                log(f"page {kind}: {final} ({len(pages_text[kind])} chars)")
            except Exception as e:
                log(f"page {kind} failed: {e}")

        # ---- product pages: JSON-LD aggregate ratings + widget quotes on the 3 best sellers
        for p in products[:3]:
            try:
                final = visit(p["url"], 2500)
                page.keyboard.press("Escape")
                page.evaluate(JS_CLOSE)
                scroll_through(page, pause=120)
                for s in page.evaluate(JS_JSONLD):
                    try:
                        d = json.loads(s)
                    except ValueError:
                        continue
                    for node in (d if isinstance(d, list) else [d]):
                        if isinstance(node, dict) and node.get("aggregateRating"):
                            ar = node["aggregateRating"]
                            reviews_json["aggregate"].append({"source": final, "name": node.get("name"), "rating": ar.get("ratingValue"), "count": ar.get("reviewCount") or ar.get("ratingCount")})
                qs = page.evaluate(JS_REVIEWS, REVIEW_WIDGETS)
                reviews_json["quotes"] += [dict(q, source=final, product=p["title"]) for q in qs]
                pages_text[f"product_{p['handle']}"] = page.evaluate("() => document.body.innerText")
                page_urls[f"product_{p['handle']}"] = final
                log(f"product {p['handle']}: {len(qs)} review quotes")
            except Exception as e:
                log(f"product page {p['url']} failed: {e}")
        browser.close()

    # ---- text files
    for k, t in pages_text.items():
        (study / "text" / f"{k}.txt").write_text(f"{page_urls.get(k, '')}\n\n{t}")

    # ---- offers as printed
    alltext = "\n".join(pages_text.values())
    pats = [r"[^\n]*free shipping[^\n]*", r"[^\n]*\b\d{1,2}% off[^\n]*", r"[^\n]*subscribe (?:&|and) save[^\n]*", r"[^\n]*\bcode\b[^\n]*",
            r"[^\n]*money[- ]back[^\n]*", r"[^\n]*guarantee[^\n]*", r"[^\n]*\b\d[\d,]*\+? (?:happy )?(?:customers|reviews|five[- ]star)[^\n]*"]
    lines = []
    for pt in pats:
        for m in re.findall(pt, alltext, flags=re.I):
            s = m.strip()
            if 6 < len(s) < 200 and s not in lines:
                lines.append(s)
    offers_json["lines"] = lines[:60]

    # ---- aggregate rating printed as text (Okendo / Judge.me / Yotpo summaries)
    for k, t in pages_text.items():
        for m in re.finditer(r"(\d\.\d)\s*(?:/\s*5)?\s*\n(?:[^\n]*\n){0,2}?\s*Based on ([\d,]+) reviews", t):
            reviews_json["aggregate"].append({"source": page_urls.get(k), "name": k, "rating": m.group(1), "count": m.group(2), "how": "printed text"})
        for m in re.finditer(r"([\d,]{3,}\+?)\s*(?:5-star|five-star|verified)?\s*reviews", t, re.I):
            reviews_json.setdefault("count_mentions", []).append({"source": page_urls.get(k), "text": m.group(0)})

    # ---- dedupe reviews
    seen = set()
    uniq = []
    for q in reviews_json["quotes"]:
        k = q["text"][:80]
        if k in seen:
            continue
        seen.add(k)
        uniq.append(q)
    reviews_json["quotes"] = uniq
    seen = set()
    agg = []
    for a in reviews_json["aggregate"]:
        k = (a.get("name"), str(a.get("rating")), str(a.get("count")))
        if k not in seen:
            seen.add(k)
            agg.append(a)
    reviews_json["aggregate"] = agg

    # ---- images: homepage/about + product images; download + contact sheets
    recs = []
    if not do_images and (study / "images.json").exists():
        recs = json.loads((study / "images.json").read_text())   # keep the previous run's index
    if do_images:
        for p in products:
            for im in p["images"]:
                images.append({"src": im, "alt": p["title"], "product": p["handle"], "page": "products.json"})
        seen = set()
        for im in images:
            src = im["src"]
            if src.startswith("//"):
                src = "https:" + src
            src = urljoin(base, src)
            fr = full_res_url(src)
            key = re.sub(r"\?.*$", "", fr)
            if key in seen or key.lower().endswith(".svg") and "logo" in key.lower():
                continue
            seen.add(key)
            im["full_src"] = fr
            recs.append(im)
        recs = recs[:max_images]
        kept = []
        for i, rec in enumerate(recs, 1):
            try:
                r = get(rec["full_src"])
                if not (r and r.status_code == 200 and r.headers.get("content-type", "").startswith("image")):
                    r = get(rec["src"])
                if not (r and r.status_code == 200 and r.headers.get("content-type", "").startswith("image")):
                    continue
                pil = Image.open(io.BytesIO(r.content))
                ext = {"JPEG": ".jpg", "PNG": ".png", "WEBP": ".webp", "GIF": ".gif"}.get(pil.format, ".img")
                stem = slugify(Path(urlparse(rec["full_src"]).path).stem)[:40] or "image"
                fn = f"{i:03d}_{stem}{ext}"
                (study / "images" / fn).write_bytes(r.content)
                rec.update(index=i, file=fn, size=f"{pil.width}x{pil.height}")
                kept.append(rec)
            except Exception as e:
                log(f"  image {rec.get('full_src')} skipped: {str(e)[:60]}")
        recs = kept
        (study / "images.json").write_text(json.dumps(recs, indent=2, ensure_ascii=False))
        sheets = contact_sheets(study / "images", recs, study)
        log(f"images: {len(recs)} downloaded, {len(sheets)} contact sheet(s)")

    # palette from homepage screenshot
    try:
        colors_json["screenshot_palette"] = palette_from_image(Image.open(study / "homepage_full.png"))
    except Exception:
        pass

    (study / "fonts.json").write_text(json.dumps(fonts_json, indent=2, ensure_ascii=False))
    (study / "colors.json").write_text(json.dumps(colors_json, indent=2, ensure_ascii=False))
    (study / "reviews.json").write_text(json.dumps(reviews_json, indent=2, ensure_ascii=False))
    (study / "offers.json").write_text(json.dumps(offers_json, indent=2, ensure_ascii=False))
    (study / "press.json").write_text(json.dumps(press_json, indent=2, ensure_ascii=False))

    # ---- STUDY.md
    roles = fonts_json["roles"]
    md = [f"# {brand} study", f"Source: {base}  ", f"Platform: {summary['platform']}  Products: {len(products)}", "",
          "## Fonts (computed on the live site)", "| role | family | weight | sizes | colour | transform |", "|---|---|---|---|---|---|"]
    for role, v in roles.items():
        if v:
            md.append(f"| {role} | {v['family']} | {v['weight']} | {', '.join(v['sizes'])} | {v['color']} | {v['transform']} |")
    md.append("")
    md.append("@font-face families: " + ", ".join(sorted({f['family'] for f in fonts_json['font_faces']})) or "(none found)")
    md.append(f"Font files downloaded: {len(fonts_json['downloaded'])} (study/fonts/)")
    md += ["", "## Colours", f"body {colors_json.get('body')}  header {colors_json.get('header')}  footer {colors_json.get('footer')}  link {colors_json.get('link')}",
           "buttons: " + "; ".join(f"{b['bg']} on {b['color']} r={b['radius']} ({b['sample'][:20]})" for b in colors_json.get("buttons", [])[:4]),
           "big sections: " + ", ".join(str(s["bg"]) for s in colors_json.get("sections", [])[:10]),
           "screenshot palette: " + ", ".join(f"{p['hex']} {p['share']:.0%}" for p in colors_json.get("screenshot_palette", [])), ""]
    md += ["## Products", "| title | price | variants | images |", "|---|---|---|---|"]
    for p in products[:40]:
        md.append(f"| {p['title']} | {p.get('price_min')}{'' if p.get('price_min') == p.get('price_max') else ' to ' + str(p.get('price_max'))} | {len(p['variants'])} | {len(p['images'])} |")
    md += ["", "## Reviews (as printed)"]
    for a in reviews_json["aggregate"][:8]:
        md.append(f"- aggregate: {a.get('rating')} from {a.get('count')} ({a.get('name')}) <{a['source']}>")
    for q in reviews_json["quotes"][:12]:
        md.append(f"- \"{q['text'][:160]}\" {('by ' + q['name']) if q.get('name') else '(no name printed)'} [{q.get('rating_raw')}] <{q['source']}>")
    if not reviews_json["aggregate"] and not reviews_json["quotes"]:
        md.append("- none found on the pages visited. Do NOT invent a rating or count.")
    md += ["", "## Offers (as printed)"]
    md += [f"- announcement: {a}" for a in offers_json["announcement"][:5]]
    md += [f"- popup: {p[:300]}" for p in offers_json["popups"][:3]]
    md += [f"- line: {l}" for l in offers_json["lines"][:25]]
    md += ["", "## Press"]
    for p in press_json[:4]:
        md.append(f"- '{p['heading']}': " + ", ".join(str(i.get('alt') or Path(urlparse(i.get('src') or '').path).name) for i in p['items'][:12]) + f" <{p['source']}>")
    if not press_json:
        md.append("- none found. Do NOT invent press.")
    md += ["", "## Pages captured (text/)", *[f"- {k}: {v}" for k, v in page_urls.items()], "",
           f"## Images: {len(recs)} in images/, numbered on contact_sheet_NN.png", "",
           "## VERIFY before sending", "- prices and variant availability (products.json published_at / available)",
           "- review rating and count only if listed above with a source URL", "- any code or threshold only from offers.json 'lines' or 'popups'",
           "- logo tone (dark-marks / light-marks) is measured from the file's colours; still open the files", ""]
    (study / "STUDY.md").write_text("\n".join(md))
    (study / "scrape.log").write_text("\n".join(log_lines))
    log(f"done -> {study}")
    return study


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--brand")
    ap.add_argument("--extra", nargs="*", default=[])
    ap.add_argument("--max-images", type=int, default=160)
    ap.add_argument("--no-images", action="store_true")
    a = ap.parse_args()
    scrape(a.url, a.brand, a.extra, a.max_images, not a.no_images)
