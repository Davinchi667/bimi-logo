# Mojisola Oshinubi — brand study

Source: https://mojisola-oshinubi.vercel.app/ — every page crawled: `/` (home), `/case-dropx`, `/case-levvy-box`, `/resume`.
Raw files, computed styles and screenshots live in `brand-study/` (`computed-styles.json`, `screens/`, `assets/`, `mirror/`).

The "brand" is a personal brand: an operations manager's portfolio. It reads like a calm editorial magazine,
not a tech startup: warm paper, an elegant condensed serif, a deep plum band, dusty-rose italics, white pill chips.

---

## 1. Colour (from `:root` in `style.css`, confirmed with computed styles)

| Token | Hex | Where it's used |
|---|---|---|
| `--paper` | `#FCFBF8` | Page background (warm off-white), text on the dark solid button |
| `--ink` | `#141414` | All body/headline text, solid button fill, "go" arrow circles, toast |
| `--muted` | `#6E6C64` | Eyebrows, labels, sub-copy, chip text in the hero, numbers like "01" |
| `--hair` | `#E6E2D8` | 1px hairlines: section dividers, chip/pill borders, card borders |
| `--band` | `#3A2140` | Deep plum: the About band (26px radius card), footer marquee, "Open to opportunities" sticker note, the nudge arrow stroke |
| `--band-ink` | `#FFFFFF` | Text on plum |
| `--accent` | `#B4748F` | Dusty rose: every italic emphasis in h1/h2 (*operate more efficiently*, *something repeatable*), hit-stage borders |
| `--accent-ink` | `#8A4A66` | Darker rose: clock text, step numbers, case meta lines, button hover, "Incoming" badge text |
| (inline) | `#EAC3D6` | Pale pink: italic emphasis *on* the plum band |
| (inline) | `#2FBF6E` | Live green dot (+ pulsing ring) beside the clock = "Open to opportunities" |
| (inline) | `#FFFFFF` | Chips, cards, line buttons, book-a-call card |
| (inline) | `#B4553C` / `#3F7D57` | Rust "Before" / green "After" labels on the Levvy before/after cards |
| (inline) | `rgba(0,0,0,.07)` / `0 10px 30px -22px rgba(0,0,0,.45)` | The only shadows: tiny nav-pill shadow, soft hover shadow on case rows |

No gradients anywhere except the marquee's edge fade-mask. No purple-to-blue anything.

## 2. Type

| Role | Family | Details | Licence / source |
|---|---|---|---|
| Display / headlines / numbers / quotes | **Instrument Serif** 400, roman + *italic* | h1 70px max, line-height 1.02, letter-spacing −0.022em; h2 54px, −0.018em; stat numbers 46px, −0.025em, lh .92; the italic is always the coloured emphasis | Google Font, OFL → install `@fontsource/instrument-serif` |
| Body / UI | **Plus Jakarta Sans** (variable 200–800) | Global letter-spacing −0.03em (`--track`). Labels: 12–12.5px, 500–600, UPPERCASE, +0.02em. Body 14.5–17px, lh 1.6. Buttons 14.5px/500 | Google Font, OFL (self-hosted on the site) → `@fontsource-variable/plus-jakarta-sans` |
| Mono | none on the site | Clock uses `font-variant-numeric: tabular-nums` in Jakarta | — |

Pairing rule on the site: the serif carries the statement and the sans carries the facts. Italic rose words are the "punchline" in almost every headline.

## 3. Logo, icons, imagery

- **Logo:** none. The identity is a wordmark in text: `MOJISOLA OSHINUBI — OPERATIONS MANAGER` (12.5px Jakarta 600 uppercase, role in muted). No favicon (404).
- **Icons:** only three, all hand-drawn-feeling strokes: a curved arrow from the "Want to know more" sticker (2.4px round-cap stroke), a curved nudge arrow in the footer (draws on with stroke-dashoffset), a ↗ arrow in black circles (2px round stroke), and a ↑ back-to-top arrow. Marquee separator: ✦. → Icon set for the video: 2.4px round-cap/round-join strokes, open shapes, slightly loose curves.
- **Photos** (only on Levvy Box case, downloaded to `brand-study/assets/`):
  `levvy-rooftop-billboard.jpg` (car with rooftop billboard), `levvy-seatback-mainstack.jpg`, `levvy-seatback-fil.jpg` (seat-back ad panels). They show third-party campaigns (Mainstack, Fil), so I'd only use them small, as "proof of execution" polaroids, or not at all.
- **Product images:** none (she sells a service).

## 4. Layout language

- Max width 1240px, 36px gutters, generous 104–110px section padding. Centered hero, then left-aligned editorial sections.
- **Corners:** 999px pills (chips, buttons, nav), 26px plum band, 24px book card, 18px case cards, 14–16px small cards.
- **Borders:** 1px `--hair` hairlines everywhere. Lists are rows separated by hairlines, numbered `01–08` in small muted sans.
- **Shadows:** almost none. Flat paper with hairlines; depth only on hover.
- **Signature elements:**
  1. **Sticker note:** white (or plum) box with serif text, rotated −2°, plus a hand-drawn curved arrow.
  2. **Live status:** green dot with pulse ring + live clock "14:44 GMT+2".
  3. **Skills marquee:** plum strip, serif skills, ✦ separators, edge fade.
  4. **Pill chips:** white, hairline border, small sans text.
  5. **Black circle "go" button** with ↗ arrow, rotates −45° on hover.
  6. **Stage chips** (DropX): 7 cards in a row, Vendor → Customer; "hit" stages get a rose border.
  7. **Stat strip:** big serif number + small muted caption, between hairlines.
- **Motion on the site:** soft reveals (`cubic-bezier(.2,.9,.2,1)`), arrows that draw on, words rising 0.34em, the pulse ring, the marquee. Calm, eased, nothing bouncy.

## 5. Voice

- First person, plain, confident, no hype. "I build and improve…", "Five things I own, week to week."
- Headline pattern: a plain statement ending in an *italic rose punchline*:
  "Operations, brought down to *something repeatable*." · "Four teams, four operations, *one approach*." · "People, processes, systems, *execution*." · "Let's build *better operations*." · "Smarter dispatch, better tracking, *fewer errors*." · "Every campaign runs the *same route*."
- Lists of three/four nouns with commas. Short sentences. Verbs: build, improve, coordinate, align, turn plans into action.
- Words she repeats: **operations, systems, processes, workflows, repeatable, structure, execution, efficiency, coordinate, people.**
- Tone: organised, warm, quietly senior.

## 6. Facts (only these will appear in the video)

**Who:** Mojisola Oshinubi, Operations Manager & Business Operations Professional. 5 years across e-commerce, logistics, customer, campaign and business operations. Pursuing an MBA (Operations Management a core course). BSc Biochemistry, Landmark University. Remote, GMT+2 clock, "Available to work full U.S. EST/PST hours". **Open to opportunities** in Operations Management, Business Operations, Process Improvement, Project & Operations Coordination.

**Headline numbers (home):** 40% reduction in manual work · 10+ hours saved weekly · 20% increase in customer retention · 6,000+ users supported · 90%+ SLA resolution.

**What she does (8):** Operations Management, Process Improvement, Workflow & Systems, Project Coordination, SOP & Documentation, Customer & Support Operations, Vendor & Partner Operations, Research & Analysis.

**Approach:** People (align the people responsible for execution) · Processes (clear, repeatable ways of working) · Systems (right tools and documentation) · Execution (turn plans into measurable action).

**Case work:**
- **DropX** (startup, multi-service delivery, Lagos), Operations Manager, June 2026–present: 3 core manuals, 9 policy & legal docs, 7-stage delivery flow field-tested end to end (Vendor · Order · Dispatch · Rider · Pickup · Delivery · Customer), 8 field issues surfaced & routed to product (OTP failures, login problems, logout behaviour, ETA discrepancies, rider live-location not visible, incorrect order status, active order hard to locate, delivery-code handling), 3 review gates cleared, 9 workstreams, 30–35 min delivery expectation.
- **Levvy Box**, Operations Manager/Lead, Feb 2026–present: 100+ drivers, 100 vehicles, up to 32 placements per campaign, 5 field team members, 8+ docs/workflows/systems, ~10 incidents handled. Flow: Allocate → Install → Verify → Document → Report. Before/after: panels batched for drivers on similar routes, centralised Excel tracking, Notion campaign profiles.
- **Try Bundler** (US), Operations Lead, Dec 2022–Jan 2026: SaaS platform, 6,000+ users, 90%+ SLA, delivery accelerated 30%, automated workflows across Stripe, Notion, Asana (−40% manual work, 10+ hrs/week saved), +20% retention, 1000+ new subscriptions in six months.
- **Wholeeats Africa**, Aug 2021–Apr 2022: CRM & support, +20% engagement.

**Offer / CTA:** "Book a 30-minute call ↗" (Calendly), "Thirty minutes to talk through your operations." Email mojisolaoshinubi@yahoo.com, LinkedIn.

**Tools (text only, no third-party logos):** Asana, Trello, ClickUp, Notion, Slack, Zoho, Zendesk, Monday.com, Shopify, Stripe, Google Workspace, Excel, Google Sheets…

**No testimonials, prices or reviews exist on the site**, so the video has none.

**Inconsistency to flag:** the Levvy case page says "5+ campaigns executed"; the résumé says "15 mobile advertising campaigns". I won't use a campaign count unless you tell me which is right.
