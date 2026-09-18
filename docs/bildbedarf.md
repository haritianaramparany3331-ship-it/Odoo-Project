# Bildbedarf — jeder Platzhalter, jede Größe (CLAUDE.md §8)

> Hari lädt echte Bilder später hoch. Bis dahin ist jedes Bild ein neutraler,
> klar als Platzhalter erkennbarer Rahmen (gestrichelter Rand, Bezeichnung
> „PH-nn" im Bild). Jede Zeile enthält die Größenentscheidung in px, **bevor**
> das Bild platziert wird (CLAUDE.md §16.6). Nummern = `platzhalter.md`.
>
> Regeln für alle Bilder: WebP (Fallback JPG/PNG nur, wo nötig), `width`/`height`
> im HTML gesetzt (kein Layout-Shift), 2× für Retina, Alt-Text beschreibend.
> Stand: 2026-09-18 (Phase 4).

## Bilder auf den Seiten

| PH | Seite | Position | Bildtyp | Format / Seitenverhältnis (px) | Zweck | Suchbegriffe / Quelle |
|---|---|---|---|---|---|---|
| **PH-13** | Startseite | Hero, rechte Spalte | **Screenshot der Odoo-Oberfläche** — CRM-Pipeline oder Verkaufs-Dashboard, deutsche Sprache, Odoo-Demodaten (kein Kundenbezug), heller Modus, Browser-Chrome abgeschnitten | **16:10**, Anzeige max. 540 × 338 CSS-px (Spalte bei 1140) → Asset **1600 × 1000**, WebP ≤ 200 KB | Zeigt die Software konkret statt abstrakter Symbolik — im DACH-Markt macht das nur einer von sieben Wettbewerbern (marktanalyse.md §2.1). Wird als „Dokument" im Rahmen gezeigt, nicht als Laptop | Eigener Screenshot aus einer Odoo-Testinstanz (odoo.com → kostenlos testen, Sprache Deutsch, Demodaten aktiv). Alternativ Odoo-Pressematerial. **Vor Go-live:** Odoos Marken-Richtlinien prüfen (odoo.com/page/brand-assets) |
| **PH-14** | Startseite; Über uns | Block „KI-Hebel", rechte Spalte | Bevorzugt: **zweiter Odoo-Screenshot** — Eingangsrechnung mit angehängtem PDF-Beleg (Buchhaltung/Dokumente). Alternativ eigenes Foto: Papierbeleg neben Bildschirm, ruhiges Licht. **Keine Stock-Roboter, keine Gehirne, keine Leiterbahnen** | **4:3**, Anzeige max. 540 × 405 → Asset **1600 × 1200**, WebP ≤ 200 KB | Bleibt bei „zeigen statt behaupten"; verbindet Beleg (Papier) und System (Odoo) — das ist der KI-Hebel in einem Bild | Eigener Screenshot (wie PH-13) oder eigenes Foto |
| **PH-07** | Über uns | Block „Ihre Ansprechpartner", 2–4 Karten | **Porträtfotos** — gleicher Hintergrund, gleiches Licht, Blick zur Kamera, Business-leger | **1:1**, Anzeige 160 × 160 Desktop / 96 × 96 mobil → Asset **480 × 480**, WebP ≤ 60 KB | Menschen dort, wo sie hingehören — klein, echt, konsistent (KIBH: Teamfotos waren zu groß, §16.6) | Eigene Fotos; ggf. dieselben wie auf kiberatunghessen.com, wenn dieselben Personen |
| **PH-08** | Über uns | Referenzkarten (nur mit echten Referenzen) | **Kundenlogos** — Vektor, einfarbig in `--c-primary` oder Original | Box **160 × 60** CSS-px, Logo eingepasst → SVG oder PNG **320 × 120** | Trust-Signal, nur echt (§4) | Vom Kunden, mit schriftlicher Freigabe |

## Logo, Favicon, Open Graph

| PH | Asset | Format (px) | Zweck | Quelle |
|---|---|---|---|---|
| **PH-15** | Wortmarke / Logo `[MARKENNAME]` | **SVG** (skalierbar); Anzeige Header max. Höhe 40 px Desktop / 32 px mobil, Footer 46 px (KIBH-Maß). Zusätzlich PNG 600 × 210 (2× von 300 × 105, dem KIBH-Logo-Maß) | Header, Footer | Willy / Designer, sobald der Name feststeht (PH-01). Bis dahin: Wortmarke als Text in Mulish 700 |
| **PH-15** | Favicon-Set | SVG (beliebig) + PNG **32 × 32**, **192 × 192**, Apple-Touch **180 × 180** | Tab, Android, iOS — dieselben drei Größen wie KIBH | aus der Wortmarke ableiten; bis dahin der neutrale Teal-Platzhalter `assets/img/favicon.svg` |
| **PH-15** | Open-Graph-Bild | **1200 × 630**, JPG/PNG ≤ 300 KB | Link-Vorschau in LinkedIn, Teams, WhatsApp, Google-Snippets | Eigenes Motiv: Wortmarke + Hero-Satz auf `--c-primary`; kein Foto nötig |

## Bewusst ohne Bild

| Stelle | Warum kein Bild |
|---|---|
| Hero der Innenseiten (Leistungen, Branchen, Über uns, Kontakt) | Typografie ist dort das Ereignis; ein Bild pro Innenseite wäre Dekoration (design-konzept.md §3.6) |
| Module, Leistungen, Branchen (Zeilen) | Keine Icon-Sets — Namen genügen; Icons hätten die Zeilen zu Karten gemacht (design-konzept.md §8) |
| Hero-Ghost-Tiles | Reines CSS, kein Asset |
| Referenz-Block auf der Startseite (PH-09) | Wird ohne echte Logos/Zitate nicht gebaut |
