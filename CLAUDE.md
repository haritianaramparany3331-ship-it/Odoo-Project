# CLAUDE.md — Neue Webseite: Digitalisierung / ERP-Systemhaus (Odoo)

> This file is loaded automatically at the start of every Claude Code session in
> this project. It is the standing context and the standing rules. Read it fully
> before doing anything.

---

## 1. Project identity

- **Company:** I Robot - You Profit GmbH
- The company has **two business fields**:
  1. **KI Beratung / KI Automation** — existing brand "KI Beratung Hessen" (KIBH),
     live at `kiberatunghessen.com`
  2. **Digitalisierung / ERP-Systemhaus (Odoo)** — **this project**: a brand-new
     website for business field 2
- **Brand / site name for this new site:** not decided yet. Hari will supply it.
  Until then, use the literal token `[MARKENNAME]` — exactly that string, every
  time, in nav, footer, page titles, meta tags, alt texts, copy, everywhere. One
  token, spelled identically, so a single find-and-replace finishes the job later.
  Do **not** invent a name, and do **not** use varying placeholders like "die
  Firma", "unser ERP-Systemhaus", "XYZ GmbH" — those can't be found and replaced,
  and they read as real text.
- **Site language:** German (all content, including legal pages)
- **Audience:** B2B, German Mittelstand — decision-makers (Geschäftsführung,
  IT-Leitung, Kaufmännische Leitung), not developers

This is **not** a migration or a rebuild of an existing site. It is a new site,
built from scratch. There is no "original" to copy from — but see §6 (design),
where KIBH's existing visual identity is a hard requirement.

---

## 2. What is being sold (Willy's words — factual basis, do not contradict)

> "Wir verkaufen die Implementierung samt Migration, Schulung und Pflege von einem
> ganzen ERP system oder einzelne Module (CRM, Zeiterfassung, Personal, Lagerhaus
> etc.). Alles von dem ERP anbieter Odoo."

So the offering is, concretely:
- Implementation of a full Odoo ERP system, **or** individual modules
- Migration (from existing systems into Odoo)
- Schulung (training)
- Pflege (ongoing maintenance/support)
- Named example modules: CRM, Zeiterfassung, Personal, Lagerhaus

**Odoo advantages as given by Willy.** These are the approved factual basis. Copy
may rephrase them for readability and tone, but must not inflate, extend, or
contradict them:

1. **Alles in einem System** – CRM, Verkauf, Einkauf, Lager, Buchhaltung und mehr
   zentral verbunden.
2. **Open Source & flexibel** – individuell anpassbar und maximale Kompatibilität
   mit KI-Automationen.
3. **Zentrale Datenbasis** – alle Unternehmensdaten an einem Ort und in Echtzeit
   verfügbar.
4. **Skalierbar** – jederzeit um neue Funktionen, Nutzer und Geschäftsbereiche
   erweiterbar.
5. **Keine Vendor-Lock-ins** – über 20.000 Entwickler weltweit; durch Open Source
   tausende Add-ons; geringe Kosten durch Selfhosting.

**One caveat on point 5:** the "über 20.000 Entwickler weltweit" figure is a
concrete, checkable number. Verify it against odoo.com or Odoo's official
communications before publishing it as a claim on a commercial site. If it can't
be verified, flag it to Hari rather than publishing an unverifiable number, and
rephrase without the figure in the meantime.

---

## 3. The assignment (Willy's brief, in full)

**Aufgabenstellung:** Mache eine neue Webseite für das Geschäftsfeld
Digitalisierung / ERP-Systemhaus (Odoo).

**Benutze möglichst viel KI bei der Recherche.** Dokumentiere, wie KI zu den
jeweiligen Punkten (1–4) benutzt wurde — aber: *nicht zu tief ins Detail, nur die
2–3 Top-Highlights ausführen, ansonsten stichpunktartig.*

### Fokus & Umfang (Scope)

- **Seitenumfang:** maximal 5–6 Kernseiten festlegen (Startseite,
  Odoo-Leistungen/Module, Branchenfokus, Referenzen / Über uns (& KI-Hebel),
  Kontakt)
- **Seiten-Lesedauer:** maximal 2–3 Minuten pro Seite, um kompakte,
  leserfreundliche B2B-Texte sicherzustellen
- **Vermeidung von Monsterseiten:** klare Wort-Obergrenzen pro Sektion
  (z. B. Hero max. 50 Wörter; Leistungsblöcke kurz und prägnant mit Bullet Points
  statt Fließtext-Romanen)

### 1) Marktanalyse & Konkurrenz-Benchmark

- **Wettbewerber recherchieren:** mindestens 4–5 DACH-Raum-Agenturen
  identifizieren, die sich auf Odoo-ERP-Implementierungen spezialisiert haben
- **Hero-Section-Analyse:** dokumentieren, wie die Startseiten aufgebaut sind
  (Value Proposition, Haupt-Call-to-Action, visuelle Darstellung der Software)
- **Nutzenkommunikation:** analysieren, welche Vorteile (z. B. Kosten,
  Zeitersparnis, modulare Skalierbarkeit) an welchen Stellen der Customer Journey
  platziert werden
- **Referenzen & Trust-Signale:** prüfen, wie Kundenprojekte präsentiert werden
  (Branchenfokus, messbare Ergebnisse, Logos, Testimonials)

### 2) Informationsarchitektur & Seitenstruktur (Wireframing)

- **Conversion-Funnel definieren:** den logischen Pfad vom Erstbesuch über die
  Leistungsübersicht bis hin zur Lead-Generierung (z. B. Erstgespräch buchen)
  festlegen
- **Kernseiten festlegen:** Struktur für Startseite, Leistungs-/Modulübersichten
  (Finanzen, CRM, Lager), Branchenlösungen, Referenzen, Über uns und Kontakt
  skizzieren
- **Content-Blöcke pro Seite:** pro definierter Unterseite festlegen, welche Pain
  Points der Zielgruppe angesprochen und welche Odoo-Stärken als Lösung
  präsentiert werden

### 3) Content-Strategie

- **SEO-Keyword-Strategie:** relevante Suchbegriffe definieren (z. B. "Odoo ERP
  Partner Deutschland", "ERP Implementierung Mittelstand", "ERP Beratung Hessen")
- **Inhalts-Erstellung:** Entwurf von zielgruppengerechten Texten (Copywriting),
  die IT-Komplexität verständlich in unternehmerischen Nutzen übersetzen

### 4) Design & Conversion-Optimierung (CRO)

- **UI/UX-Konzept:** Erstellung eines modernen, vertrauenerweckenden Designs, das
  zu einer professionellen IT-Beratung passt. **Dieselben Farben und Font wie auf
  der KIBH-Webseite verwenden.**
- **Lead-Magnete & CTAs:** Integration klarer Handlungsaufforderungen (z. B.
  "Kostenloses ERP-Potenzialgespräch vereinbaren", ROI-Rechner)
- **Tracking & Analytics:** Einbindung von datenschutzkonformen Analyse-Tools zur
  Messung von Conversions und Nutzerverhalten

---

## 4. Content rules — what Claude may and may not write

**This project is different from the KIBH migration project.** There, Claude was
forbidden to write any website text at all. Here, **copywriting is explicitly part
of the assignment** (Punkt 3, "Inhalts-Erstellung"). So Claude writes the copy.

But that permission covers *wording*, not *facts*.

### ✅ Claude writes

- Headlines, subheadlines, hero copy, section intros
- Benefit and feature descriptions (grounded in §2 and verified Odoo facts)
- CTA labels, button text, form labels, microcopy
- FAQ entries (only where the answer is factually verifiable)
- Meta titles, meta descriptions, alt texts
- Navigation labels, footer text, 404 page copy
- Error/empty/success states

### ❌ Claude never invents — placeholder + flag instead

Never write any of the following unless Hari or Willy supplied it explicitly:

- **Customer names, client logos, testimonials, quotes, case studies, reference
  projects** — including "anonymized" ones ("ein mittelständischer Hersteller…")
- **Numbers and metrics** — Zeitersparnis in %, ROI figures, cost savings, number
  of projects, number of customers, number of employees, years in business,
  implementation duration, uptime, response times
- **Certifications and partner status** — e.g. "Odoo Gold Partner", "Odoo Ready
  Partner", ISO certifications, awards, memberships
- **Team members** — names, roles, bios, photos, quotes, LinkedIn links
- **Prices, packages, SLAs, Support-Zeiten, Vertragslaufzeiten**
- **Company legal data** — address, Handelsregister, USt-IdNr.,
  Geschäftsführer, contact details, phone numbers, email addresses
- **Claims about Odoo's capabilities** that can't be verified on odoo.com
- **Anything about the company's own experience, history, or track record in ERP**

When a section structurally needs one of these, write a clearly marked placeholder:

```
[PLATZHALTER: Kundenreferenz — Branche, messbares Ergebnis, Zitat, Logo]
```

…and add an entry to `docs/offene-fragen.md`. **Never fill the gap with something
plausible-sounding.** A plausible invented number on a real commercial B2B site is
worse than a visible gap.

**The general rule, beyond the list above:** whenever you are not sure whether
something is a fact you're allowed to state — use a placeholder and ask. Hari will
check with Willy. Uncertainty is never a reason to write the plausible version; it
is the signal to stop and flag. This applies even when the invented detail would be
small, obvious-seeming, or "just filler".

### Special case: the Referenzen page

The assignment lists "Referenzen" as a core page, and Punkt 1 asks for research
into how competitors present reference projects. But **this business field is new**
— real Odoo/ERP reference customers may not exist yet.

Do **not** build out a Referenzen page with invented case studies. Instead:
research how it *should* work (that's the assignment), design the page structure
and card layout, fill it with clearly marked placeholders, and ask Hari whether
there are real references to use, or whether KIBH's existing AI-consulting
references may be shown here (and if so, with what framing — they are AI projects,
not ERP projects, and must not be presented as ERP projects).

### Special case: Branchenfokus

The assignment asks for a Branchenfokus / Branchenlösungen page but doesn't name
the industries. Propose a shortlist based on (a) competitor research from Punkt 1
and (b) which industries KIBH already works in. **But:** presenting an industry as
a focus area is a positioning claim, not a customer claim — keep the copy about
what Odoo can do for that industry, never about work already done there unless
Hari confirms it.

---

## 5. Scope and page inventory

### Core pages (max 5–6, per the brief)

1. **Startseite**
2. **Odoo-Leistungen / Module** (Finanzen, CRM, Lager, Zeiterfassung, Personal, …)
3. **Branchenfokus / Branchenlösungen**
4. **Referenzen**
5. **Über uns (& KI-Hebel)**
6. **Kontakt**

> Note: the brief's bullet reads "Referenzen/Über uns & KI Hebel" (confirmed by
> Hari). Still open: whether that is **one** combined page or **two** separate
> pages. If separate, that's 6 core pages, still within scope. Propose your reading
> in the plan and let Hari confirm before building.

### Required beyond the core pages (not counted in the 5–6)

- **Header / Navigation** — consistent across all pages, mobile burger menu,
  persistent primary CTA
- **Footer** — nav links, legal links, brand, contact
- **Impressum** — legally required in Germany (§5 DDG/TMG). Structure and layout
  only; **all actual data is a placeholder for Willy to supply**
- **Datenschutzerklärung** — DSGVO. Same rule: structure yes, content placeholders.
  Must cover whatever third-party tools actually end up embedded (analytics,
  booking, forms, fonts)
- **404-Seite** — branded, with a way back into the site
- **`sitemap.xml`** and **`robots.txt`**
- **Favicon / Open Graph images** — placeholder

> ⚠️ Legal pages: draft the *structure and headings*, never invent legal content,
> company data, or data-processing descriptions. German Impressum/Datenschutz
> errors carry real Abmahnung risk. Flag clearly that Willy must review and
> complete these before go-live.

### Length discipline (hard rules from the brief)

- Reading time per page: **max 2–3 minutes**
- **Hero: max 50 words**
- Service/feature blocks: bullet points, short, no prose walls
- Before finishing each page, count the words and check it against these limits.
  Report the per-page word count and estimated reading time in your summary.

---

## 6. Design

### Hard requirement from Willy

> "Nehme die selben Farben und Font wie aus KIBH Webseite."

Same colors, same typeface as the KIBH website. This is not a suggestion — it's the
one visual constraint that is fixed.

**Source of truth for the design tokens:** the existing KIBH rebuild project
(Hari's other repo). Read the actual CSS custom properties / variables from there —
exact hex values, font families, weights, type scale, spacing scale, border radii,
shadows.

- Local path to the KIBH project: `[AUSFÜLLEN]`
- Fallbacks if that isn't available: `https://kibh-webseite.vercel.app` (the
  rebuild) and `https://kiberatunghessen.com` (the original) — inspect computed
  styles, don't eyeball colors from a screenshot.

Write the extracted tokens into `docs/design-tokens.md` and implement them as CSS
custom properties on `:root`, so this site and KIBH stay visually consistent and
the tokens are documented for the case study.

### What's free, and what to do with that freedom

Colors and typeface are fixed. Layout, composition, hierarchy, imagery treatment,
motion and structural devices are open. **Use the `frontend-design` skill** for
this — it's installed.

### Explicitly forbidden: generic AI design tells

Hari's instruction: no generic AI implementations. Concretely, avoid:

- **Inter** (or Geist/Manrope/Plus Jakarta as the "safe default" substitute) —
  irrelevant here anyway, since the typeface is dictated by KIBH
- Purple/violet gradients; any decorative gradient wash used as filler
- The SaaS-card kit: everything chopped into identical rounded cards, one
  border-radius on every element regardless of hierarchy, the same soft grey
  `rgba(0,0,0,.1)` shadow under each
- Tracked-out ALL-CAPS eyebrow labels above every heading
- Meta strings joined with middle dots (`A · B · C`)
- `WORD — fragment` labels with a spaced em dash
- A `→` appended to every link and button label
- Monospace faces used for small data labels as decoration
- Accenting a single word in a headline in a different color/italic
- Numbered markers `01 / 02 / 03` where the content is not actually a sequence
- Fade-and-slide-up entrance animations on *every* section and hover transitions on
  *every* card — the generic default. One orchestrated moment beats scattered
  effects.
- Tinted near-black (`#0B0B0B`, `#111`) standing in for black — use the real KIBH
  text color

### Motion

Motion that answers a user action (opening, expanding, confirming, hovering an
actual target) is welcome. Non-user-triggered motion: sparing and deliberate.
Respect `prefers-reduced-motion` everywhere.

### The 8 pillars of an expensive-feeling website

Every page is checked against these before it's considered done:

1. **Point of view, not a template** — a considered design decision, not a default
2. **Typography that does work** — type scale, weight and spacing actively guiding
   the eye, not just "readable"
3. **A restrained color system** — intentional and consistent, not scattered
4. **Hierarchy that breathes** — spacing that lets important things stand out
5. **Imagery with intent** — images placed and treated deliberately, not dropped in
6. **Motion that whispers** — subtle and premium, never flashy
7. **Mobile that's designed, not shrunk** — purpose-built mobile layouts
8. **The invisible expensive stuff** — fast loads, no layout shift, smooth
   scrolling, no console errors, favicon, hover/focus states, consistent details

---

## 7. Tech stack

- **Static HTML / CSS / JS. No framework.** (Same as the KIBH project — proven,
  and the point of the case study is that this stack is enough.)
- **No framework build** — no bundler, no transpiler, no npm dependencies. The
  only build is `node build.js`, a zero-dependency script that assembles
  `src/pages/` + `src/partials/` into `dist/`, a plain folder of static files
  (decided 2026-09-18, see "Shared components" below).
- Deployment: **Vercel temporarily**, so Willy can review the site via a link.
  Once the site is finished it moves to a paid host (same plan as the KIBH site) —
  Vercel's free Hobby tier prohibits commercial use, so it is a review environment
  here, not the final home.
  **Build so that the move is trivial:** relative paths only, no Vercel-specific
  features (no serverless functions, no `vercel.json` rewrites, no Vercel image
  optimisation, no Vercel analytics). A plain folder of static files should be
  uploadable to any host without changes. If you ever think a Vercel-specific
  feature is needed, ask first.
  Vercel config: root directory = repo root; build command = `node build.js`;
  output directory = `dist`. Both values also live in the 2-key `vercel.json`
  (approved 2026-09-18 — buildCommand + outputDirectory only, nothing else may
  be added to it). (The KIBH project's first deploy failed on a wrong root
  directory — don't repeat it.)
- GitHub repo: `[AUSFÜLLEN]`

### Shared components — one source, not copy-paste

On the KIBH project the same card markup was duplicated across two pages, so every
change had to be made twice and the two copies drifted apart. Decide up front how
header, footer, nav and repeated card/section blocks are kept in sync:

**Decided 2026-09-18: the minimal build step** (`build.js`, adapted from KIBH).
Header, footer and every block that appears on more than one page live exactly
once in `src/partials/` and are pulled in with `{{> name}}`. Rule: a block used
on two pages is never pasted twice — it becomes a partial. Changing a shared
block therefore changes every instance by construction.
- Keep CSS organized with custom properties on `:root`; watch selector specificity,
  especially section padding/margins cancelling each other out.

---

## 8. Images and assets

**Hari uploads real images later.** Until then, every image is a placeholder.

For every placeholder, add a row to `docs/bildbedarf.md` with:

| Seite | Position | Bildtyp | Format / Seitenverhältnis | Zweck | Suchbegriffe / Quelle |
|-------|----------|---------|---------------------------|-------|-----------------------|

Be specific and useful — "Bild" is not a recommendation. Say what kind of image
actually belongs there and why (e.g. "Screenshot des Odoo-CRM-Dashboards, 16:9,
zeigt die Software konkret statt abstrakter Symbolik — Wettbewerber tun das
durchgängig, siehe Punkt-1-Recherche"), plus a concrete size in px and where such
an image could come from (Odoo press kit, own screenshot, Stock, eigene Fotos).

Same for logos, favicon, Open Graph image, team photos, client logos.

Placeholders themselves should be visually neutral and clearly *not* final —
never ship a stock photo or an AI-generated image as if it were the real thing.

---

## 9. SEO

- Keyword strategy per Punkt 3 → document in `docs/seo-keywords.md`
- Per page: unique `<title>`, unique meta description, one `<h1>`, semantic
  heading order, descriptive alt texts
- German-language `lang="de"`
- `sitemap.xml`, `robots.txt`, canonical URLs
- Open Graph + Twitter card tags
- Structured data (`Organization` / `LocalBusiness` / `Service`) — **only with real
  data**, so leave it as a documented placeholder until Willy supplies the details.
  Never publish structured data containing invented company info.

---

## 10. Analytics, tracking, and third-party tools

The brief asks for "datenschutzkonforme Analyse-Tools". Because this is a German
commercial site, this is a legal question, not just a technical one.

- **Recommend, then ask.** Propose 2–3 DSGVO-friendly, ideally cookieless options
  (e.g. Plausible, Matomo self-hosted, Umami) with pros/cons and cost, and let
  Hari/Willy decide. **Do not implement any tracking without explicit approval.**
- **Never add Google Analytics** without explicit written approval — it carries
  known DSGVO complications in Germany.
- Any tool that's actually embedded must be reflected in the Datenschutzerklärung,
  and may require a consent banner. Flag this; don't silently skip it.
- **Self-host fonts** rather than loading Google Fonts from Google's CDN (German
  courts have ruled on this). If the KIBH font comes from a CDN, flag it.

## 11. Lead capture

- Primary CTA, per the brief: **"Kostenloses ERP-Potenzialgespräch vereinbaren"**
- **Booking:** KIBH uses Calendly. Whether this site gets its own Calendly event or
  reuses KIBH's is `[OFFEN]` — build a placeholder, ask before embedding.
- **Contact form:** KIBH is using Formspree. Same question here — placeholder, ask.
- **ROI-Rechner:** the brief lists it as an example ("z. B."), so treat it as
  **optional and un-approved**. It's also risky: an ROI calculator implies concrete
  savings figures, which fall under §4's "never invent numbers" rule. Propose it as
  an option with a note on what real inputs it would need; don't build it
  speculatively.

---

## 12. Git

- Commit locally after each meaningful step — good for the case-study trail.
- **Never run `git push` or open a PR without asking first. Every time. No
  exceptions.** Pushing triggers a Vercel deploy, so a push is effectively a
  publish.

---

## 13. Documentation deliverables

These are part of the assignment, not optional extras. Keep them updated as you go,
not at the end.

| File | Purpose |
|------|---------|
| `docs/ki-recherche.md` | **Required by the brief.** How AI was used for Punkte 1–4. 2–3 top highlights described properly; everything else in bullet points. Do **not** go deep — the brief explicitly says not to. |
| `docs/marktanalyse.md` | Punkt 1: the 4–5 DACH competitors, hero analysis, Nutzenkommunikation, Trust-Signale |
| `docs/informationsarchitektur.md` | Punkt 2: conversion funnel, page structure, content blocks per page, ASCII wireframes |
| `docs/seo-keywords.md` | Punkt 3: keyword strategy |
| `docs/content.md` | Punkt 3: all site copy in one place, so Willy can review it without reading HTML |
| `docs/design-tokens.md` | KIBH colors/fonts/spacing extracted, with source |
| `docs/bildbedarf.md` | Image placeholder table (§8) |
| `docs/offene-fragen.md` | Everything blocked on Hari or Willy |

---

## 14. Skills

Installed and expected to be used:
- **`webapp-testing`** — check your own work in a real browser before reporting done
- **`frontend-design`** — design direction, anti-generic guidance

If you judge that another skill would genuinely help, **say so and name it** —
Hari will install it. Don't silently work around a missing capability.

> Note: on this machine, `python` and `python3` are not on PATH. The `py` launcher
> works and resolves to Python 3.14.5. Use `py` for anything Python-based,
> including webapp-testing scripts.

---

## 15. Working rules

- **Ask rather than guess.** If a requirement is ambiguous, if content is missing,
  or if you're about to make a decision that's really Hari's or Willy's to make —
  stop and ask. This is explicitly wanted.
- **Plan before building.** Use plan mode for anything structural.
- **Check your own work.** Run `webapp-testing` before declaring a page finished,
  and fix what it surfaces yourself rather than reporting it back.
- **One task per session** where practical; `/compact` at natural breakpoints.
- Note anything surprising, broken, or time-consuming — it feeds the case study.

---

## 16. Lessons from the KIBH project — do not repeat these

Hari built the KIBH website with Claude Code before this project. These are the
things that actually went wrong there. Each one cost real time. Read them as rules,
not anecdotes.

### Content

1. **Text was invented where none was supplied.** The homepage ended up with
   sentences that existed nowhere in the source, and had to be found and replaced
   page by page. The failure mode is quiet: a gap gets filled with something that
   reads fine. See §4 — placeholder and ask, always.
2. **Contradictory rules caused drift.** The KIBH `CLAUDE.md` said content could be
   revised "where it feels too generic" in one section while forbidding invention
   in another. Claude followed the looser rule. If a new instruction conflicts with
   an existing one in this file, **reconcile both and say so** — never stack a new
   rule on top of a contradicting old one.

### Design

3. **Colors were guessed instead of sampled.** "Black" was implemented as dark
   grey. Read the real computed value from the source; never eyeball a hex.
4. **Font weight was inconsistent** — some headings bold that shouldn't be, some
   not bold that should be. Define in `docs/design-tokens.md` up front: exactly
   which elements are bold, and at which weight. Then apply that, don't improvise
   per section.
5. **Vertical gaps were repeatedly too large** and had to be fixed in several
   separate rounds. Define a spacing scale up front (section padding, gap between
   a CTA and the next heading, gap between blocks) and use only values from it.
6. **Images were sized ad hoc** — team photos far too large, one hero background
   missing entirely, logo sizes changed twice in opposite directions. Every image
   gets an explicit size decision in `docs/bildbedarf.md` before it's placed.
7. **An open-ended "improve the design" pass produced unusable output** and ~1.5 h
   had to be rolled back. Improvements must be **named and specific**. The 8-pillar
   check in Phase 6 produces a list of concrete, individually-described issues —
   it is never a mandate to redesign.

### Layout and language

8. **German compound words broke mid-word** at some widths ("Ge-schäftsführer").
   Set wrapping rules globally from the start so words wrap whole, and check at
   360 / 414 / 768 / 1024 px.
9. **Mobile was a late separate pass**, and the legal pages were forgotten in the
   first sweep. Build responsive from the first page, and treat Impressum,
   Datenschutz and 404 as real pages in every check.

### Process

10. **The first full review came only after the whole site was built**, producing
    one large batch of rework. That's why this project has STOP gates: structure
    approved before copy, copy approved before build.
11. **Verify the deploy pipeline early.** KIBH's first Vercel deploy failed because
    Root Directory pointed at a subfolder, so the output was looked for in the
    wrong place. Deploy something trivial and confirm it works *before* the site
    exists, not after.
12. **Third-party accounts belong to the company.** Calendly, Formspree, analytics,
    hosting — register them on a company address, not Hari's personal one.
13. **Sessions grew far too long** (one hit 258k tokens). Keep to roughly one
    session per phase, and at the end of each session append a short status line to
    `PROGRESS.md`: what was finished, what's next, what's blocked. A fresh session
    should be able to pick up from `CLAUDE.md` + `PROGRESS.md` alone.

---

## 17. Open questions (blocked on Hari / Willy)

- [ ] **Brand/site name** for the ERP business field — until then `[MARKENNAME]`
- [ ] **Domain** for the new site
- [ ] **GitHub repo** URL
- [ ] **Final host** after the Vercel review phase (IONOS, Hostinger, Vercel Pro …)
      — not blocking now, but decide before go-live
- [x] **Shared components**: minimal build step (decided 2026-09-18, §7)
- [ ] Is **"Referenzen / Über uns & KI-Hebel"** one page or two?
- [ ] Are there **real ERP/Odoo reference customers** yet? If not, how should the
      Referenzen page be handled at launch?
- [ ] May **KIBH's existing AI references** appear here, and with what framing?
- [ ] Which **industries** for Branchenfokus?
- [ ] **Impressum / Datenschutz** data — Willy
- [ ] **Analytics tool** choice + consent approach
- [ ] **Booking**: own Calendly event or KIBH's?
- [ ] **Contact form**: own Formspree form or KIBH's?
- [ ] **ROI-Rechner**: wanted or not?
- [ ] Is the "über 20.000 Entwickler" figure verifiable?
- [ ] Local path to the KIBH project (for design token extraction)
