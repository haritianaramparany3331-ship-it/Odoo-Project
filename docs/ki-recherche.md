# KI-Recherche — wie KI in diesem Projekt eingesetzt wurde (für Willy)

> Vorgabe aus der Aufgabenstellung: *nicht zu tief ins Detail, nur die 2–3
> Top-Highlights ausführen, ansonsten stichpunktartig.*
>
> Werkzeug: Claude Code (Anthropic) als Arbeitspartner in der Kommandozeile —
> mit Zugriff auf Websuche, einen gesteuerten Browser (Playwright/Chromium),
> das Dateisystem und Git. Hari führt, entscheidet und gibt frei; Claude
> recherchiert, entwirft, baut und prüft. Alle Zwischenstände liegen als
> Commits vor. Stand: 2026-09-19.

---

## Die drei Highlights

### 1. Die Wettbewerber wurden besucht, nicht gegoogelt

Für die Marktanalyse hat Claude zuerst Odoos offizielles Partnerverzeichnis
für Deutschland, Österreich und die Schweiz ausgelesen (101 / 40 / 61 Partner
nach Stufe) und daraus sieben Anbieter ausgewählt. Dann hat es die sieben
Startseiten in einem gesteuerten Browser geöffnet — Cookie-Banner weggeklickt,
den sichtbaren Bereich fotografiert, Überschriften, Unterzeilen, Buttons,
Abschnittsfolge, Navigation und Logos automatisch ausgelesen — und sich die
Screenshots anschließend selbst angesehen, um die Hero-Sections visuell zu
bewerten. Das Ergebnis war belastbarer als jede Suchergebnis-Zusammenfassung:
Alle sieben Headlines sagen, *wer der Anbieter ist*, keine sagt, was der Kunde
bekommt; nur einer von sieben zeigt die Software; niemand beziffert einen
Kundennutzen; KI ist überall Thema, nirgends Angebot. Aus genau diesen Lücken
ist die Positionierung dieser Website entstanden (`marktanalyse.md`).

### 2. Jede Zahl und jeder Fachbegriff wurde an der Quelle geprüft

Das Briefing nannte „über 20.000 Entwickler weltweit". Claude hat die Zahl auf
odoo.com gegengelesen: Die Community-Seite sagt wörtlich „20,000+ people
contribute" — Mitwirkende, nicht Entwickler; die Startseite sagt „100k+
developers". Beide Varianten liegen Willy zur Entscheidung vor, im Text steht
bis dahin die exakt belegte. Genauso bei DATEV und GoBD: Claude hat Odoos
deutsche Lokalisierungs-Dokumentation gelesen. DATEV-Export und
ELSTER-Übermittlung sind Enterprise-Module — der Text sagt „Odoo Enterprise".
Zur GoBD schreibt Odoo selbst, die Pflichten lägen beim Steuerpflichtigen,
nicht bei der Software — unsere FAQ sagt deshalb genau das, während ein
Wettbewerber „GoBD-konform" behauptet. Unter jedem Textblock in `content.md`
steht die Quelle; was keine Quelle hat, ist ein nummerierter Platzhalter.

### 3. Die Qualitätssicherung ist ein Skript, kein Augenmaß

Claude hat ein Prüfskript geschrieben (`tests/qa.py`), das alle sieben Seiten
bei fünf Bildschirmbreiten (360 bis 1440 px) im Browser lädt und misst: Fehler
in der Konsole, horizontales Überlaufen, **mitten im Wort umgebrochene
Komposita** (jedes Wort einzeln vermessen), zu kleine Touch-Ziele, tote Links
und Anker, Überschriftenfolge, doppelte Titel, Wortzahl je Seite gegen das
Budget. Der erste Lauf fand sieben konkrete Fehler — darunter drei Wörter, die
auf Handy-Breite zerbrachen („Datenschutzerklärung"), und Links, die zu klein
zum Tippen waren. Alle wurden behoben, bevor jemand die Seite gesehen hat.
Dazu zählt der Build nach jedem Lauf die offenen Platzhalter je Seite: Bei
null ist die Seite Go-live-fähig.

---

## Punkt 1 — Marktanalyse & Konkurrenz-Benchmark

- Grundgesamtheit aus Odoos Partnerverzeichnis statt aus dem Bauchgefühl;
  Auswahl nach Referenzzahl und regionaler Relevanz (Hessen/Rhein-Main
  gesondert geprüft).
- Echte Besuche im gesteuerten Browser, Screenshots von Claude bewertet.
- Grenzen erkannt und ausgeglichen: eine Seite blockte den einfachen Abruf
  (403), animierte Zähler wurden als „0+" erfasst und aus der Meta-Description
  ergänzt; ein Anbieter mit „Odoo Hessen"-Seite sitzt in Bayern.
- Wortzahlen der Wettbewerber-Startseiten gemessen (fünf von sieben über dem
  2–3-Minuten-Limit unserer Aufgabenstellung).

## Punkt 2 — Informationsarchitektur & Wireframing

- Funnel aus dem abgeleitet, was die Wettbewerber an derselben Stelle tun — und
  auslassen.
- Branchen-Shortlist als Schnittmenge aus Wettbewerbernennungen und KIBHs
  echten Branchen (Claude hat die KIBH-Referenzseiten ausgelesen).
- Wortbudgets je Block vorab gerechnet (200 Wörter/min), nicht hinterher
  gekürzt.
- Jeder Block trägt Pain Point und Odoo-Stärke aus dem Briefing (O1–O5).

## Punkt 3 — Content-Strategie

- Keyword-Cluster aus Briefing, Wettbewerber-Titles und Odoo-Modulnamen, nach
  Suchintention auf die fünf Seiten verteilt; Suchvolumen bewusst nicht
  geraten (Validierung per Search Console nach Go-live).
- Alle Texte mit Quellenvermerk; nummerierte Platzhalter (PH-01 … PH-20) im
  Register `platzhalter.md`.
- Wortzahlen per Skript (`tools/wordcount.py`): Hero ≤ 50 Wörter, Seite
  ≤ Budget — Kürzen statt Limits anheben.

## Punkt 4 — Design & Conversion-Optimierung

- Farben, Schriften, Abstände, Radien und Schatten aus dem CSS des
  KIBH-Projekts gelesen (mit Zeilenangabe), Kontraste berechnet.
- Entwurf gegen den generischen „B2B-IT-Agentur"-Standard geprüft und an fünf
  Stellen geändert (Karten → Kontoblatt-Zeilen, dunkles → helles CTA-Band,
  Laptop-Mockup → Screenshot als Dokument, Scroll-Reveal gestrichen, Icons
  gestrichen).
- Gestaltungsidee aus dem Gegenstand: die Seite als Kontoblatt.
- Bildgrößen vorab in px entschieden (`bildbedarf.md`).
- Schriften selbst gehostet statt vom Google-CDN (KIBH lädt sie noch von dort —
  Empfehlung zum Nachziehen).
- Analyse-Tool: drei cookielose Optionen mit Empfehlung, nichts eingebaut
  (`analytics-tracking.md`).

## Was überraschend, kaputt oder zeitaufwendig war

- Die sieben Wettbewerber laufen alle auf Odoos eigenem Website-Builder — sie
  sehen sich entsprechend ähnlich.
- „Odoo Hessen"-Suchergebnisse sind Landingpages auswärtiger Anbieter; vor Ort
  gibt es einen Silver-Partner in Kassel und einen kleinen Anbieter bei
  Darmstadt.
- Ein Screenshot-Werkzeug ließ bei ganzseitigen Aufnahmen die Navigation im
  klebenden Header verschwinden — ein Fehlalarm, der eine halbe Stunde kostete,
  bis die Messung im Browser das Gegenteil zeigte.
- Die Vercel-Review-Umgebung ist bewusst auf `noindex` gestellt; die Domain
  fehlt noch (PH-02) — Canonical-URLs, Sitemap und `og:url` entstehen erst
  damit.
