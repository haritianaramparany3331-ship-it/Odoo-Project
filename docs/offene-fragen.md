# Offene Fragen — blockiert durch Hari / Willy

Eine Liste, ein Ort. Jede Frage steht mit der Phase, ab der sie blockiert, und
mit einer Empfehlung, wo Claude eine hat. Erledigte Punkte wandern nach unten
in „Entschieden", mit Datum und Antwort.

Stand: 2026-09-17 (Phase 0)

---

## A. Blockiert **jetzt** (vor Phase 1)

| # | Frage | Empfehlung von Claude | Wer |
|---|---|---|---|
| A1 | **Shared Components:** minimaler Build-Schritt (`build.js` + `src/partials/`, wie bei KIBH) oder reine HTML-Duplikation mit dokumentierter Liste? | **Build-Schritt.** Null Abhängigkeiten, ein Node-Skript, bewährt auf KIBH. Header/Footer/CTA-Band existieren genau einmal. Ausgabe ist ein reiner Ordner statischer Dateien (`dist/`), der auf jeden Host passt. | Hari |
| A2 | **GitHub-Repo anlegen** und mit Vercel verbinden (Root Directory = Repo-Root, Build Command `node build.js`, Output Directory `dist`). Auf welchem Account — Haris (wie KIBH) oder ein Firmen-Account (CLAUDE.md §16.12)? | Firmen-Account, falls vorhanden; sonst Haris wie bei KIBH, mit Umzug vor Go-live. | Hari |
| A3 | Darf eine **2-Zeilen-`vercel.json`** (nur `buildCommand` + `outputDirectory`, keine Rewrites/Header/Functions) ins Repo, damit der Deploy reproduzierbar ist statt in Dashboard-Klicks zu leben? | Ja — es ist Konfiguration, kein Vercel-Feature; der Endhost ignoriert die Datei. Alternative: dieselben zwei Werte im Vercel-Dashboard setzen. | Hari |

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

_(noch nichts)_
