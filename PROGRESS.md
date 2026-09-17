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
  `.claude/settings.local.json` (ask before `git push`).
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
