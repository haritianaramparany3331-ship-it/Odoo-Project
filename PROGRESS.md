# PROGRESS

One block per session. A fresh session should be able to continue from
`CLAUDE.md` + this file alone. Newest at the bottom.

---

## Session 1 — 2026-09-17 — Phase 0 (Setup)

**Finished**
- Repo scanned (only `CLAUDE.md` existed). KIBH project found at `../KIBH`
  (sibling folder) and used as the design-token source.
- `docs/design-tokens.md`: every color, type, spacing, radius, shadow and
  motion value read from `../KIBH/assets/css/main.css` `:root` + breakpoint
  overrides, with source lines. Includes the explicit **font-weight table**
  (400 / 600 / 700 only) and the **spacing scale** with the three gaps that
  were re-fixed repeatedly on KIBH (section padding, CTA → next heading,
  block gap). Contrast ratios computed, not estimated.
- Mulish self-hosted (`assets/fonts/`, 3 variable woff2 subsets, OFL) instead
  of KIBH's Google-CDN load — flagged in the tokens doc.
- `docs/` stubs for all §13 deliverables; `docs/offene-fragen.md` triaged into
  "blocks now / Phase 2 / Phase 3 / Phase 5 / go-live".
- Build scaffold: `build.js` (adapted from KIBH: relative `{{root}}` paths,
  `{{> partial}}` includes, `site.config.json` with `siteUrl` + `indexable`
  switch → canonical/og:url/sitemap/robots derive from it), `serve.js`,
  `package.json` (zero deps), `vercel.json` (buildCommand + outputDirectory
  only — pending Hari's OK, see offene-fragen A3), `.gitignore`,
  `.claude/settings.json` (project-wide: ask before `git push`), `.gitattributes` (LF everywhere).
- `assets/css/main.css`: tokens on `:root`, German wrapping rules global from
  line 1, base reset, container/section/button utilities, minimal header/footer.
- Placeholder Startseite + 404 page built and checked in headless Chromium:
  200/404 statuses correct, Mulish loads from the self-hosted file, computed
  styles match the tokens, no console errors, no horizontal overflow at
  360/414/768/1024/1440, served HTML is valid UTF-8.
- Local git repo initialised, first commit.

**Next**
- STOP: Hari approves tokens + build-step approach, creates the GitHub repo
  and Vercel project (Root = repo root, Build = `node build.js`, Output =
  `dist`), approves the push → deploy pipeline verified with the placeholder.
- Then Phase 1 (Marktanalyse).

**Blocked**
- Deploy verification: needs the GitHub repo + Vercel connection (no `gh` /
  `vercel` CLI on this machine; push needs approval anyway — CLAUDE.md §12).
- `docs/offene-fragen.md` A1–A3.

---

## Session 2 — 2026-09-18 — Phase 0 close-out + Phase 1 (Marktanalyse)

**Finished**
- A1 (build step) and A3 (2-key vercel.json) approved; CLAUDE.md §7 reconciled
  and `[x]` ticked; decisions logged in `docs/offene-fragen.md`.
- GitHub remote added (`haritianaramparany3331-ship-it/Odoo-Project`), push
  approved by Hari, `main` pushed. **Vercel import + deployed-placeholder check
  still open** (needs Hari's Vercel project; then verify status/noindex/fonts).
- Phase 1 research done and written to `docs/marktanalyse.md`: partner
  population DE/AT/CH from odoo.com, 7 homepages captured in headless Chromium
  (screenshots + structured extraction), local Rhein-Main check (HAV Media
  Kassel/Silver, cloudition, regional landing pages of non-local firms),
  synthesis (patterns, keep/break, the gap), word counts measured.
- "über 20.000 Entwickler" traced on odoo.com → "20,000+ people contribute";
  decision for Willy in offene-fragen C2.
- `docs/ki-recherche.md` Punkt 1 bullets written.

**Later the same day**
- Phase 1 synthesis approved. Vercel project connected by Hari:
  `https://odoo-project-topaz.vercel.app/` — verified with curl: `/` 200,
  CSS + woff2 200, custom 404 with status 404 and root-absolute CSS, robots
  `Disallow: /` + `noindex` meta (review build), no sitemap by design. Doc
  commits pushed (approved).
- **Phase 2 written:** `docs/informationsarchitektur.md` — funnel (7 steps
  with "what must be true"), 5-page structure (B1 proposal: one "Über uns"
  page with Referenzen anchor), 4-industry shortlist (B4 proposal, grounded in
  Phase 1 + KIBH's real references), content blocks per page with pain point /
  Odoo strength / word budget, ASCII wireframes, CTA placement rule (header +
  one end band; Startseite also hero). New open items F1–F3.

**Phase 2 approved, Phase 3 written (same day)**
- `docs/platzhalter.md`: the single placeholder register (PH-01 … PH-20) Hari
  asked for; `build.js` now prints open placeholders per page after each build.
- `docs/seo-keywords.md`: clusters by intent → page, title/meta per page, no
  invented volumes (validation plan instead).
- `docs/content.md`: all copy for 5 pages + header/footer + legal structure +
  404, every claim with a source note, placeholders as PH-nn. Word counts via
  `tools/wordcount.py`: Startseite 436 · Leistungen 600 · Branchen 356 · Über
  uns 306 · Kontakt 197; heroes 23–39 words.
- Verified on odoo.com docs: DATEV export + ELSTER UStVA (Enterprise reporting
  modules); GoBD applies to the taxpayer, Odoo provides the means (GoBD export)
  — copy says exactly that, no "GoBD-konform" claim.

**Phase 4 written (same day)**
- `docs/design-konzept.md`: 6 color roles, type roles, the "Kontoblatt-Zeile"
  layout principle (ruled rows instead of cards, one left axis), where cards
  are allowed (2 places), light CTA band, one motion moment (hero convergence),
  5 principles, self-critique table vs. the generic B2B-IT default with the
  changes made. Open for Hari: rows-not-cards, light CTA band, animation
  yes/no, who makes the Odoo screenshot.
- `docs/bildbedarf.md`: every image with display + asset px sizes (PH-07/08/13/
  14/15) and the deliberate no-image places.
- `docs/ki-recherche.md` Punkt 4 bullets.

**Next**
- STOP: Hari approves the design concept → Phase 5 build (tokens+CSS → header/
  footer → Startseite → inner pages → legal → 404 → sitemap/robots), then
  Phase 6 QA, Phase 7 docs.

**Blocked**
- Text approval by Willy (content.md) can run in parallel with the build;
  PH-03 changes CTA wording later. Design approval (this STOP).
