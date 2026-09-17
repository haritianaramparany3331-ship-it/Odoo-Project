# Design Tokens — extracted from the KIBH rebuild

**Rule (CLAUDE.md §6, Willy):** same colors, same typeface as the KIBH website.
Everything below is *read* from the KIBH rebuild's source files, not estimated.

**Sources**

| Source | Path | What was taken |
|---|---|---|
| KIBH rebuild stylesheet | `../KIBH/assets/css/main.css`, `:root` block (lines 9–113) and the `@media (max-width: 1024px)` / `(max-width: 767px)` overrides (lines 3549 ff., 3624 ff.) | every color, size, spacing, radius, shadow, transition value |
| KIBH design-system doc | `../KIBH/docs/design-system.md` | derivation of the palette and the type scale from the live site (`kiberatunghessen.com`, Elementor kit `.elementor-kit-10`) |
| KIBH base partial | `../KIBH/src/partials/base.html` | how fonts are loaded (see "Font loading" — flagged) |
| KIBH weight usage | `grep font-weight` over `main.css`, mapped selector → weight | the font-weight rule below |

Values are reproduced verbatim as CSS custom properties in `assets/css/main.css`
on `:root`. Nothing outside this file is a source for a visual value.

---

## 1. Colors

### Brand palette (the four Elementor globals of the live site)

| Token | Hex | Role on the KIBH site | Role on this site |
|---|---|---|---|
| `--c-primary` | `#31363F` | dark slate — headings, dark bands, header/footer surfaces | same |
| `--c-secondary` | `#EEEEEE` | light grey — text on dark bands, light section backgrounds | same |
| `--c-text` | `#222831` | body text (the real "black" — **not** `#111`/`#0B0B0B`) | same |
| `--c-accent` | `#76ABAE` | teal — buttons, links, highlights | same; the single accent |

### Extended palette (in use on KIBH)

| Token | Hex | Role |
|---|---|---|
| `--c-white` | `#FFFFFF` | page ground |
| `--c-surface` | `#F8FAF9` | off-white section surface |
| `--c-surface-alt` | `#EDF0EF` | light neutral section surface |
| `--c-lime` | `#D6D84F` | yellow-green secondary accent (KIBH uses it very sparingly; treat as optional) |
| `--c-teal-muted` | `#587274` | muted teal |
| `--c-teal-dark` | `#3C6264` | dark teal — link hover |
| `--c-teal-deep` | `#1C3738` | very dark teal |
| `--c-ink` | `#0D1D20` | near-black teal — darkest surface |

### Derived (defined by the KIBH rebuild, reused unchanged)

| Token | Value | Role |
|---|---|---|
| `--c-text-muted` | `#5B636E` | secondary text, captions |
| `--c-border` | `#E2E6E5` | hairlines, card borders |
| `--c-accent-dark` | `#5F9295` | link color, primary-button hover; the accent darkened for text contrast |
| `--c-accent-soft` | `rgba(118,171,174,0.12)` | soft teal wash (chips, icon backgrounds) |

**Contrast note.** White text on `#76ABAE` measures only 2.56:1 (computed, WCAG 2.x). KIBH accepts
this for buttons (brand decision, matches the live site). For *text* links KIBH
uses `--c-accent-dark #5F9295` (3.48:1 on white — passes AA only for large text; `--c-teal-dark #3C6264` is 6.72:1 and is the safe choice for small link text). So on this site body-size teal
text on white is always `--c-accent-dark`, never `--c-accent`. Nothing is
changed here — recorded so the choice is conscious rather than accidental.

---

## 2. Typography

### Families

| Token | Stack | Used for | Why |
|---|---|---|---|
| `--font-display` | `Mulish, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif` | all headings, nav, buttons, labels | The live site sets these in **Avenir** (licensed Linotype face, self-hosted there). The KIBH rebuild substitutes **Mulish**, chosen by measuring candidates against the real Avenir files (100.2 % heading width, letterforms stay in register across a line). See `../KIBH/docs/design-system.md`, "Open decisions" |
| `--font-sans` | `Verdana, Geneva, "DejaVu Sans", sans-serif` | running text, lists, forms, quotes | The live site's body face is Verdana; it ships with Windows and macOS, so no webfont and no licence question |

### Font loading — flagged (CLAUDE.md §10)

- **KIBH loads Mulish from the Google Fonts CDN** (`base.html` lines 18–23:
  `fonts.googleapis.com` + `fonts.gstatic.com`). German courts (LG München I,
  20 Jan 2022, 3 O 17493/20) have treated the IP transfer to Google as a GDPR
  issue. **This site self-hosts instead**: Mulish is SIL-OFL-licensed, the
  variable `woff2` files live in `assets/fonts/` (latin, latin-ext, latin
  italic; 27–32 KB each; the browser downloads only the subsets a page uses).
  → Recommendation for Hari: KIBH should switch to the same self-hosted files.
- KIBH's `base.html` also loads **Plus Jakarta Sans** — only for the
  `/e-rechnung/` and U2care pages that mirror the original 1:1. Not a brand
  face; not used here.
- Verdana needs no webfont. Where it is absent (Android, Linux) the stack
  falls back to DejaVu Sans / the system sans, exactly as on KIBH.
- **Open for Willy (carried over from KIBH):** if the company holds an Avenir
  webfont licence, swapping Mulish for Avenir is a one-token change on both sites.

### Type scale

All values from KIBH `:root` and its two breakpoint overrides. `rem` = 16 px.

| Token | Desktop (≥1025) | Tablet (≤1024) | Mobile (≤767) | Role |
|---|---|---|---|---|
| `--fs-hero` | `clamp(3.25rem, 5.4vw, 4rem)` = 52–64 | `3.25rem` = 52 | `clamp(2rem, calc((100vw - 2rem) / 9.1), 2.5rem)` = 32–40 | Startseite hero h1 only |
| `--fs-display` | `3.25rem` = 52 | 52 | `2.375rem` = 38 | oversized display line (used once, if at all) |
| `--fs-h1` | `3rem` = 48 | `2.75rem` = 44 | `2.375rem` = 38 | page h1 on inner pages |
| `--fs-h2` | `2.375rem` = 38 | 38 | `2rem` = 32 | section headline |
| `--fs-h2-sm` | `2rem` = 32 | 32 | 32 | smaller section headline / big card heading |
| `--fs-h3` | `1.75rem` = 28 | 28 | `1.5rem` = 24 | block heading |
| `--fs-h4` | `1.5rem` = 24 | 24 | 24 | card / small heading |
| `--fs-lead` | `1.25rem` = 20 | 20 | 20 | lead-in / label |
| `--fs-body-lg` | `1.125rem` = 18 | 18 | 18 | large body, section intro |
| `--fs-body` | `1rem` = 16 | 16 | **16** (KIBH keeps 16 on phones: iOS zooms form fields below 16 px) | body |
| `--fs-small` | `0.9375rem` = 15 | 15 | 15 | buttons, small body |
| `--fs-caption` | `0.875rem` = 14 | 14 | 14 | captions, footer meta |
| `--fs-eyebrow` | `0.75rem` = 12 | 12 | 12 | label (restricted use — see CLAUDE.md §6) |
| `--fs-numeral` | `10.625rem` = 170 | `8.75rem` = 140 | 140 | oversized numeral — **not used here** (we have no numbers we may publish) |

Line-heights (KIBH): body `1.6`; headings `1.2`; hero `1.1`; buttons `1.3`;
eyebrow `1.4` with `letter-spacing: 0.08em`.

### Font-weight rule — the explicit table (CLAUDE.md §16.4)

Three weights only. Nothing else, nothing improvised per section.
Verdana ships as 400 and 700 only; Mulish is served as a variable 400–700 file.

| Element | Face | Weight | Source in KIBH |
|---|---|---|---|
| Body text, list items, table cells, form fields, footer text | Verdana | **400** | `body { font-weight: 400 }` |
| `<strong>` / `<b>` inside body text | Verdana | **700** | browser default; Verdana's only bold |
| Lead paragraph (`.lead`), section intro | Verdana | **400** | `.lead` (no weight set → 400) |
| Quotes / testimonials (placeholders only for now) | Verdana | **400 italic** | KIBH's 500-italic quote resolves to 400 in Verdana anyway |
| **All headings h1–h6**, incl. card titles, hero h1, FAQ questions, legal-page headings | Mulish | **600** | `h1, h2, h3, h4, h5, h6 { font-weight: 600 }` |
| Buttons (`.btn`, all variants) | Mulish | **600** | `.btn { font-weight: 600 }` |
| Nav links (header + drawer) | Mulish | **700** | `.nav__link { font-weight: 700 }` |
| Footer column headings | Mulish | **700** | `.site-footer h2 { font-weight: 700 }` |
| Eyebrow / small label (only where a label is real information) | Mulish | **600**, uppercase, 12 px | `.eyebrow` |
| Emphasised word inside a Mulish context | Mulish | **600** | `.dre-pillar strong` |

**Not used:** 500 (KIBH uses it in three page-specific places), 800+, and any
per-page 700 heading override (KIBH has several, e.g. `.case-card h3`; they are
page-local exceptions, not the system). If a heading ever *looks* like it needs
700, the answer is size or spacing, not weight.

### Wrapping rules for German (set globally, first stylesheet — CLAUDE.md §16.8)

Carried over from KIBH, where each was earned the hard way:

- Headings: `overflow-wrap: break-word; hyphens: manual; text-wrap: balance;`
  (`hyphens: auto` was rejected on KIBH: it broke "maß-geschneiderte",
  "Erstge-spräch").
- `p, li, dd, blockquote`: `overflow-wrap: break-word`.
- Every grid/flex child: `min-width: 0` (otherwise the longest compound widens
  the track past the viewport).
- Card titles in narrow columns (~250 px): `hyphens: auto` **only there**, with
  `lang="de"` on `<html>` so the browser uses German hyphenation.
- Hero h1 on phones is sized so the longest word fits the column (the
  `calc((100vw - 2rem) / 9.1)` clamp above); the longest word in *our* hero copy
  must be measured against it in Phase 5.
- No `overflow-x: hidden` on `body` — it hides overflow from QA instead of
  fixing it.

---

## 3. Spacing scale (CLAUDE.md §16.5)

Only these values are used for margins, paddings and gaps. Any value not on the
scale is a bug.

| Token | Desktop | Mobile (≤767) | px |
|---|---|---|---|
| `--sp-1` | `0.25rem` | — | 4 |
| `--sp-2` | `0.5rem` | — | 8 |
| `--sp-3` | `0.75rem` | — | 12 |
| `--sp-4` | `1rem` | — | 16 |
| `--sp-5` | `1.5rem` | — | 24 |
| `--sp-6` | `2rem` | — | 32 |
| `--sp-7` | `3rem` | — | 48 |
| `--sp-8` | `4rem` | — | 64 |
| `--sp-9` | `5rem` | `3.5rem` | 80 / 56 |
| `--sp-10` | `7rem` | `4rem` | 112 / 64 |

### The three gaps that were re-fixed repeatedly on KIBH, now fixed up front

| Situation | Value | Rationale |
|---|---|---|
| **Section padding** (top and bottom) | `--sp-9` (80 / 56) | KIBH `.section` |
| Section padding, tight variant (`.section--tight`, e.g. a short band) | `--sp-8` (64) desktop / `--sp-7` (48) mobile | KIBH; the mobile step keeps "tight" tighter than normal after `--sp-9` shrinks |
| **Section head → its content** (`.section-head` margin-bottom) | `--sp-7` (48) | KIBH `.section-head` |
| Eyebrow → h2 | `--sp-3` (12) | KIBH |
| h2 → intro paragraph | `--sp-4` (16) | KIBH `.section-head p` |
| **Gap between blocks / cards in a grid** | `--sp-5` (24) | KIBH grid gutter |
| Content → CTA row (`.btn-row` margin-top) | `--sp-6` (32) | KIBH `.btn-row` |
| **CTA row → next section's heading** | section bottom padding drops to `--sp-5` (24) when the section *ends* on a CTA row, so the visible gap is 24 + 80 = **104 px**, not 32 + 80 + 80 = 192 | KIBH `.section:has(> .container > .btn-row:last-child)` — Willy flagged the 156–172 px holes on KIBH |
| Paragraph → paragraph in prose | `--sp-4` (16) | |
| Container side gutter | `--sp-5` (24) desktop / `--sp-4` (16) mobile | KIBH `.container` |
| Header height | 92 px desktop / 76 px ≤767 / 56 px phone-landscape | KIBH `--header-h` (settled after Willy: 76 → 104 → 92) |

---

## 4. Layout

| Token | Value | Source |
|---|---|---|
| `--container` | `1140px` | Elementor default content width on the live site |
| `--container-wide` | `1240px` | header/footer width on KIBH |
| Breakpoints | `≤767` mobile · `≤1024` tablet · `≥1025` desktop | Elementor's three-tier set (29× / 26× occurrences in the live CSS) |
| Burger menu | `≤1024` | KIBH `.nav-toggle { display: flex }` inside the 1024 query |
| Test widths (CLAUDE.md §16.8) | 360 · 414 · 768 · 1024 · 1440 | 768 and 1024 sit one pixel *above* a breakpoint — desktop type in a narrow column, the worst case for compounds |

## 5. Radii, shadows, motion

Radius follows hierarchy — one radius per *level*, not one radius everywhere
(CLAUDE.md §6):

| Token | Value | Applied to |
|---|---|---|
| — | `3px` | focus ring corner |
| — | `6px` | buttons, inputs, chips |
| `--radius` | `12px` | cards |
| `--radius-lg` | `20px` | large panels, media frames, the hero visual |

| Token | Value |
|---|---|
| `--shadow-sm` | `0 1px 3px rgba(34,40,49,.06), 0 4px 12px rgba(34,40,49,.05)` — tinted with `--c-text`, not neutral black |
| `--shadow-md` | `0 4px 16px rgba(34,40,49,.08), 0 12px 32px rgba(34,40,49,.07)` |
| `--transition` | `180ms cubic-bezier(0.4, 0, 0.2, 1)` |
| Focus ring | `outline: 3px solid var(--c-accent); outline-offset: 3px` |
| Reduced motion | `@media (prefers-reduced-motion: reduce)` zeroes all animation/transition durations and disables smooth scroll |

Button geometry (KIBH): Mulish 600, 15 px, padding `0.8125rem 1.625rem`,
`border: 2px solid`, radius 6 px, `translateY(-1px)` on hover (pointer devices
only). Primary = teal fill, white text; outline = `--c-primary` border.

---

## 6. What is deliberately *not* carried over from KIBH

- The cursor glow (`--glow-a`) — a KIBH-specific device; this site gets its own
  "one bold thing" in Phase 4.
- Plus Jakarta Sans, the 170 px numeral, the ghost button's `›` suffix (a
  `→`/`›` on every link is on the §6 forbidden list).
- Scroll-in animations on every section (`.js-anim`) — §6 forbids the
  fade-and-slide-up default. Motion is decided per element in Phase 4.
