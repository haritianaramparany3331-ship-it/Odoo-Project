# Offene Fragen — blockiert durch Hari / Willy

Eine Liste, ein Ort. Jede Frage steht mit der Phase, ab der sie blockiert, und
mit einer Empfehlung, wo Claude eine hat. Erledigte Punkte wandern nach unten
in „Entschieden", mit Datum und Antwort.

Stand: 2026-09-18 (Phase 0 → 1)

---

## A. Blockiert **jetzt** (vor Phase 1)

_(keine — alle Phase-0-Fragen sind entschieden)_

## B. Blockiert ab **Phase 2** (Informationsarchitektur)

| # | Frage | Empfehlung | Wer |
|---|---|---|---|
| B1 | **„Referenzen / Über uns & KI-Hebel"** — eine Seite oder zwei? | Vorschlag folgt in Phase 2 nach der Wettbewerbsanalyse. | Hari |
| B2 | Gibt es **echte Odoo/ERP-Referenzkunden**? Falls nein: wie soll die Referenzen-Seite zum Launch aussehen (Platzhalter-Struktur, oder Seite vorerst weglassen)? | Struktur bauen, Platzhalter zeigen — Entscheidung nach Phase 1 (dort sehen wir, wie Wettbewerber ohne viele Referenzen arbeiten). | Willy |
| B3 | Dürfen **KIBH-KI-Referenzen** hier erscheinen — und mit welcher Einordnung? (Es sind KI-Projekte, keine ERP-Projekte.) | Nur mit klarer Kennzeichnung als KI-Projekte, z. B. im Block „KI-Hebel". | Willy |
| B4 | **Branchenfokus:** welche Branchen? | Shortlist folgt in Phase 2 (aus Wettbewerbsrecherche + KIBH-Branchen). | Willy |
| B5 | **ROI-Rechner** — gewünscht oder nicht? Er bräuchte echte Zahlen (Stundensätze, Zeitersparnis pro Modul), die niemand erfinden darf. | Nicht bauen, bis reale Eingabewerte vorliegen. Alternative: „Potenzialgespräch" als CTA trägt denselben Zweck ohne Zahlen. | Willy |

## C. Blockiert ab **Phase 3** (Content)

| # | Frage | Empfehlung | Wer |
|---|---|---|---|
| C1 | **Markenname** — bis dahin überall `[MARKENNAME]`. | Nicht blockierend: ein Find-and-Replace am Ende. | Willy |
| C2 | Ist „**über 20.000 Entwickler weltweit**" belegbar? | Claude prüft in Phase 1/3 auf odoo.com; falls nicht belegbar, Formulierung ohne Zahl. | Claude → Willy |

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

## Platzhalter im Content (werden ab Phase 3 hier gesammelt)

_(noch keine)_

---

## Entschieden

| Datum | Frage | Entscheidung |
|---|---|---|
| 2026-09-18 | A1 Shared Components | **Build-Schritt** (`build.js` + `src/partials/`). CLAUDE.md §7 entsprechend angepasst. |
| 2026-09-18 | A3 `vercel.json` | **OK** — nur `buildCommand` + `outputDirectory`, sonst nichts. |
| 2026-09-18 | A2 GitHub-Repo | `https://github.com/haritianaramparany3331-ship-it/Odoo-Project` (Haris Account, wie KIBH). Push nur nach Freigabe. |
