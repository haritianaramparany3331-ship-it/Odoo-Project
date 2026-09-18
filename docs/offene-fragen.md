# Offene Fragen — blockiert durch Hari / Willy

Eine Liste, ein Ort. Jede Frage steht mit der Phase, ab der sie blockiert, und
mit einer Empfehlung, wo Claude eine hat. Erledigte Punkte wandern nach unten
in „Entschieden", mit Datum und Antwort.

Stand: 2026-09-18 (Phase 5 — Build läuft; Texte bei Willy zur Freigabe)

---

## A. Blockiert **jetzt** (vor Phase 1)

_(keine — alle Phase-0-Fragen sind entschieden)_

## B. Blockiert ab **Phase 2** (Informationsarchitektur)

| # | Frage | Empfehlung | Wer |
|---|---|---|---|
| B2 | Gibt es **echte Odoo/ERP-Referenzkunden**? Falls nein: wie soll die Referenzen-Seite zum Launch aussehen (Platzhalter-Struktur, oder Seite vorerst weglassen)? | Struktur bauen, Platzhalter zeigen — Entscheidung nach Phase 1 (dort sehen wir, wie Wettbewerber ohne viele Referenzen arbeiten). | Willy |
| B3 | Dürfen **KIBH-KI-Referenzen** hier erscheinen — und mit welcher Einordnung? (Es sind KI-Projekte, keine ERP-Projekte.) | Nur mit klarer Kennzeichnung als KI-Projekte, z. B. im Block „KI-Hebel". | Willy |
| B5 | **ROI-Rechner** — gewünscht oder nicht? | **Empfehlung: nicht bauen.** Er bräuchte Ersparniswerte, die niemand erfinden darf (§4). Der CTA „Potenzialgespräch" trägt den Zweck. | Willy |

## F. Aus Phase 2 entstanden — für Phase 3 (Copy) gebraucht

| # | Frage | Empfehlung | Wer |
|---|---|---|---|
| F1 | **Footer-Link zur KIBH-Seite** („KI-Beratung: kiberatunghessen.com") — ja/nein? | Ja: zeigt die gewachsene Firma hinter dem neuen Geschäftsfeld, SEO-Verknüpfung in beide Richtungen. | Willy |
| F2 | **Das Potenzialgespräch konkret:** Dauer, Format (Video/vor Ort), Teilnehmer, was der Kunde danach in der Hand hat (z. B. schriftliche Einschätzung?). | Bis dahin `[PLATZHALTER: Dauer/Format]` im CTA-Band und auf /kontakt/. Ohne diese Angaben bleibt der wichtigste CTA vage. | Willy |
| F3 | **Regionale Aussage** in Texten und SEO: „aus Hessen für den Mittelstand in Deutschland" (Vorschlag) — oder nur Hessen/Rhein-Main, oder DACH? | Vorschlag wie genannt; passt zu den Keywords des Briefings („… Deutschland", „… Hessen"). | Willy |

## C. Blockiert ab **Phase 3** (Content)

| # | Frage | Empfehlung | Wer |
|---|---|---|---|
| C1 | **Markenname** — bis dahin überall `[MARKENNAME]`. | Nicht blockierend: ein Find-and-Replace am Ende. | Willy |
| C2 | „**über 20.000 Entwickler weltweit**" — geprüft 18.09.2026 auf odoo.com: die Community-Seite sagt wörtlich „20,000+ **people contribute** to the success of Odoo" (Mitwirkende, nicht Entwickler); die Startseite sagt „100k+ developers", „40k+ community apps", „28 million users". Details in `marktanalyse.md` §3. | Willy wählt: (a) „über 20.000 Mitwirkende weltweit" (exakt belegt) oder (b) „laut Odoo über 100.000 Entwickler weltweit" (Odoos eigene Startseitenzahl). Claude nimmt bis zur Entscheidung (a). „Tausende Add-ons" ist belegt (40k+). | Willy |

## D. Blockiert ab **Phase 5** (Build) — jetzt nur Platzhalter

| # | Frage | Empfehlung | Wer |
|---|---|---|---|
| D1 | **Impressum / Datenschutz** — alle Firmendaten (Anschrift, HRB, USt-IdNr., Geschäftsführer, Kontakt). | Struktur wird gebaut, Inhalte bleiben `[PLATZHALTER]`, Willy prüft vor Go-live. | Willy |
| D2 | **Analyse-Tool** + Consent-Ansatz. | Empfehlung mit 2–3 Optionen folgt in Phase 5 (Plausible / Umami / Matomo self-hosted). Nichts wird ohne Freigabe eingebaut. | Willy |
| D3 | **Terminbuchung:** eigenes Calendly-Event oder das von KIBH? | Platzhalter; Frage vor Einbettung. | Willy |
| D4 | **Kontaktformular:** eigenes Formspree-Formular oder das von KIBH? | Platzhalter; Frage vor Einbettung. | Willy |
| D5 | **Avenir-Webfont-Lizenz** vorhanden? (Dann wäre Mulish → Avenir ein Ein-Zeilen-Wechsel, auf beiden Seiten.) | Aus KIBH übernommen, weiterhin offen. | Willy |

## E. Vor **Go-live**

| # | Frage | Empfehlung | Wer |
|---|---|---|---|
| E1 | **Domain** der neuen Seite (für Canonical-URLs, Sitemap, OG-Tags). | Bis dahin bleibt der Build ohne absolute URLs bzw. mit der Vercel-Preview-URL. | Willy |
| E2 | **Endhost** nach der Vercel-Review-Phase (IONOS, Hostinger, Vercel Pro …). | `dist/` ist ein reiner Ordner — Umzug ist ein Upload. Einzige Host-Abhängigkeit: die 404-Seite. Vercel nimmt `404.html` automatisch; ein Apache-Host (IONOS, Hostinger) braucht eine `.htaccess` mit `ErrorDocument 404 /404.html` — wird beim Umzug ergänzt. | Willy |
| E3 | Drittanbieter-Konten (Calendly, Formspree, Analytics, Hosting) auf **Firmen-Adresse** registrieren, nicht auf Haris private. | CLAUDE.md §16.12 | Hari / Willy |

---

## Platzhalter im Content

**Eine Liste, ein Ort:** alle Platzhalter stehen mit Nummer, Fundstelle und Bedarf in `platzhalter.md` (PH-01 … PH-20). Diese Datei hier hält nur die Entscheidungsfragen; die Fragen B2/B3/C2/D1–D5/E1/F1–F3 entsprechen dort PH-08/PH-18/PH-11–PH-16/PH-02/PH-19/PH-03/PH-17.

---

## Entschieden

| Datum | Frage | Entscheidung |
|---|---|---|
| 2026-09-18 | Design-Konzept (Phase 4) | **Freigegeben:** Kontoblatt-Zeilen statt Karten, helles CTA-Band, Hero-Konvergenz-Animation ja, Odoo-Screenshot (PH-13) als Platzhalter-Rahmen bis Hari ihn liefert. |
| 2026-09-18 | B1 Referenzen/Über uns | **Eine Seite „Über uns"** mit Referenzen-Anker (Phase 2 freigegeben). |
| 2026-09-18 | B4 Branchen | **Vier:** Bau & Handwerk · Produktion & Lebensmittelhandwerk · Handel & E-Commerce · Dienstleistung, Beratung & Agenturen (Phase 2 freigegeben). |
| 2026-09-18 | A1 Shared Components | **Build-Schritt** (`build.js` + `src/partials/`). CLAUDE.md §7 entsprechend angepasst. |
| 2026-09-18 | A3 `vercel.json` | **OK** — nur `buildCommand` + `outputDirectory`, sonst nichts. |
| 2026-09-18 | Vercel | Projekt verbunden, Deploy geprüft: `https://odoo-project-topaz.vercel.app/` (200, 404-Seite, noindex, Fonts). Review-URL, kein Endhost. |
| 2026-09-18 | A2 GitHub-Repo | `https://github.com/haritianaramparany3331-ship-it/Odoo-Project` (Haris Account, wie KIBH). Push nur nach Freigabe. |
