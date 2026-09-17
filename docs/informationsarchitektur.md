# Informationsarchitektur & Seitenstruktur (Punkt 2)

Stand: 2026-09-18 (Phase 2, Vorschlag zur Freigabe). Baut auf
`marktanalyse.md` (Phase 1) und CLAUDE.md §2–§5 auf. Nichts hier ist Text für
die Seite — Wortbudgets und Blockinhalte beschreiben, *was* ein Block leistet;
die Formulierung ist Phase 3.

---

## 0. Entscheidungen, die diese Struktur voraussetzt

| # | Entscheidung | Vorschlag | Begründung |
|---|---|---|---|
| **B1** | „Referenzen / Über uns (& KI-Hebel)" — eine Seite oder zwei? | **Eine Seite: „Über uns"**, mit dem Referenzen-Block als Abschnitt (Anker `#referenzen`). Gebaut so, dass der Block zu einer eigenen Seite werden kann, sobald ≥ 3 echte ERP-Referenzen vorliegen (Nav-Platz reserviert). | Das Geschäftsfeld ist neu; ein Menüpunkt „Referenzen", der auf Platzhalter führt, schadet dem Vertrauen mehr als kein Menüpunkt (Phase 1: Vertrauen ist im Markt *die* Währung — und genau die dürfen wir nicht fälschen). Auf „Über uns" steht der Block neben dem, was wir wirklich haben: die Firma, das Vorgehen, den KI-Hebel. Ergibt **5 Kernseiten**. |
| **B4** | Welche Branchen? | **Vier:** 1 Bau & Handwerk · 2 Produktion & Lebensmittelhandwerk · 3 Handel & E-Commerce · 4 Dienstleistung, Beratung & Agenturen. Optional 5: Pflege & Sozialwirtschaft — **nicht empfohlen** (siehe unten). | Kreuzung aus Phase 1 (Wettbewerber nennen am häufigsten Produktion/Industrie, Handel/E-Commerce, Dienstleistung, Bau) und KIBHs echten Branchen (Bauwesen: Entropia; Lebensmittelhandwerk: Hinnerbäcker; Dienstleistung/Immobilien: JJ Real Estate; Pflege: U2care). Willys Module (CRM, Zeiterfassung, Personal, Lager) passen auf alle vier. Pflege ist ein regulierter Nischenmarkt mit eigener Abrechnungslogik — Odoo als „Pflege-Software" zu positionieren wäre ein Claim, den wir nicht belegen können. |
| — | Leistungen: eine Seite oder je Modul eine Unterseite? | **Eine Seite** `/leistungen/` mit Modul-Ankern. Modul-Unterseiten sind eine spätere SEO-Ausbaustufe (in `seo-keywords.md` vermerkt). | Vorgabe max. 5–6 Kernseiten und 2–3 Minuten Lesezeit. |
| — | Header-CTA-Beschriftung | Button im Header: **„Potenzialgespräch vereinbaren"**; in Hero und CTA-Bändern der volle Satz **„Kostenloses ERP-Potenzialgespräch vereinbaren"**. | Der volle Text ist für einen Header-Button zu lang (KIBH nutzt dort „Kostenloses Erstgespräch"). |
| — | Footer-Link zur KIBH-Seite? | **Ja, ein Link** („Unser Geschäftsfeld KI: KI Beratung Hessen") — beidseitig sinnvoll (Vertrauen, SEO). | Offen für Willy, siehe `offene-fragen.md` F1. |
| **B5** | ROI-Rechner | **Nicht bauen.** Alternative ohne Zahlen: keine. Der CTA „Potenzialgespräch" trägt den Zweck. | Ein Rechner setzt Ersparniswerte voraus, die niemand erfinden darf (§4). |

---

## 1. Conversion-Funnel

Zielgruppe: Geschäftsführung / kaufmännische Leitung / IT-Leitung im deutschen
Mittelstand. Ziel-Aktion: **Kostenloses ERP-Potenzialgespräch vereinbaren**
(Terminbuchung), Ersatzweg: Kontaktformular.

| Stufe | Seite | Frage im Kopf des Besuchers | Was wahr sein muss, damit er weitergeht | Nächster Schritt |
|---|---|---|---|---|
| 0 Einstieg | Suche („Odoo Partner Hessen", „ERP Mittelstand", „Odoo Einführung"), Empfehlung, KIBH-Link, LinkedIn | — | Title/Meta versprechen genau das, was die Seite zeigt (Phase 3) | Startseite oder direkt Leistungen/Branchen |
| 1 Orientierung (5–10 s) | **Startseite, Hero** | „Bin ich hier richtig? Für Firmen wie meine? Was machen die?" | Headline nennt Ergebnis + Zielgruppe (nicht „wir sind Partner"); Unterzeile nennt Odoo, Mittelstand, Region; die Software ist sichtbar; CTA sichtbar; das Design wirkt wie ein seriöses Beratungshaus (KIBH-Identität) | scrollen oder Leistungen |
| 2 Problem erkannt (20 s) | Startseite, „Ausgangslage" | „Die beschreiben meinen Alltag." | Drei konkrete Alltagsprobleme (Insellösungen, Doppelerfassung, keine Zahlen in Echtzeit), ohne Fachjargon | weiter |
| 3 Lösung verstanden (60 s) | Startseite, Module + Warum Odoo + Vorgehen | „Was ist Odoo, warum das und nicht SAP/Sage, wie läuft so ein Projekt?" | Ein System statt fünf; Willys fünf Odoo-Argumente knapp; ein transparentes Vorgehen in fünf Schritten ersetzt die Zähler, die wir nicht haben | Leistungen / Branchen / CTA |
| 4 Passung geprüft (60–90 s) | **Leistungen** | „Passt das Angebot zu meiner Situation — ganzes ERP oder erst ein Modul? Migration? Schulung? Und was passiert danach?" | Leistungen als Reise (Beratung → Einführung → Migration → Schulung → Pflege); Module als konkrete Einstiege; „ein Modul zuerst" ist ausdrücklich erlaubt; FAQ nimmt Einwände (Community/Enterprise, Cloud/Selfhosting, Daten) | Branchen oder CTA |
| 5 Relevanz geprüft (30–60 s) | **Branchen** | „Verstehen die meine Branche?" | Die Seite spricht die Prozesssprache der Branche und ordnet Module zu — Diagnosequalität statt Referenzzahlen | CTA |
| 6 Vertrauen (60 s) | **Über uns & KI-Hebel** | „Wer sind die — und warum die statt des Gold-Partners mit 500 Projekten?" | Firma real (I Robot - You Profit GmbH, zwei Geschäftsfelder), Haltung transparent (Standard first, modular, keine Lock-ins), der KI-Hebel ist konkret, der Referenzen-Block ehrlich | CTA |
| 7 Handlung | **Kontakt** | „Was passiert, wenn ich klicke? Bin ich zu etwas verpflichtet?" | Buchung in Sekunden, Formular als Alternative, „So geht es weiter" in drei Schritten, keine Preisfalle, Datenschutz-Hinweis | **Termin gebucht** |

Sekundärschleifen: Von jeder Seite führt genau ein CTA-Band zurück zu Stufe 7;
FAQ-Blöcke auf Leistungen und Kontakt fangen Einwände ab — nur mit Antworten,
die auf odoo.com belegbar sind oder das eigene Vorgehen beschreiben (§4: keine
Zahlen, keine Dauern, keine Preise).

---

## 2. Seitenstruktur & Navigation

```
/                      Startseite
/leistungen/           Odoo-Leistungen & Module        (Anker: #beratung #einfuehrung #migration #schulung #pflege #module #faq)
/branchen/             Branchenfokus                   (Anker: #bau #produktion #handel #dienstleistung)
/ueber-uns/            Über uns & KI-Hebel             (Anker: #vorgehen #ki-hebel #team #referenzen)
/kontakt/              Kontakt / Potenzialgespräch
/impressum/            Impressum        (Struktur, Inhalte Platzhalter — Willy)
/datenschutz/          Datenschutzerklärung (Struktur, Inhalte Platzhalter — Willy)
404.html               Seite nicht gefunden
robots.txt · sitemap.xml (aus build.js, sobald siteUrl gesetzt)
```

**Header (auf allen Seiten):**
`[MARKENNAME]` (Wortmarke → /) · Leistungen · Branchen · Über uns · Kontakt ·
**[Potenzialgespräch vereinbaren]** (Button → /kontakt/). ≤ 1024 px: Burger,
Drawer mit denselben fünf Einträgen, Button unten im Drawer. Aktive Seite
markiert (`aria-current`).

**Footer:** Wortmarke + ein Satz (was wir tun, für wen) · Spalte „Seiten" (die
fünf) · Spalte „Rechtliches" (Impressum, Datenschutz) · Spalte „Kontakt"
(`[PLATZHALTER: Adresse, Telefon, E-Mail]`) · Zeile „Ein Geschäftsfeld der
I Robot - You Profit GmbH — KI-Beratung: kiberatunghessen.com" (Link offen, F1).

---

## 3. Content-Blöcke pro Seite

Lesegeschwindigkeit für B2B-Deutsch: ≈ 200 Wörter/min. Budgets: Startseite ≤ 480
(2,4 min), Leistungen ≤ 600 (3 min), Branchen ≤ 520, Über uns ≤ 420, Kontakt
≤ 240. Hero überall ≤ 50 Wörter (Ziel 35–45). Zählweise: sichtbarer Fließtext
inkl. Überschriften und Buttons, ohne Navigation/Footer.

Kürzel für Odoo-Stärken (CLAUDE.md §2): **O1** Alles in einem System · **O2**
Open Source & flexibel, KI-kompatibel · **O3** Zentrale Datenbasis, Echtzeit ·
**O4** Skalierbar · **O5** Keine Vendor-Lock-ins (Community, Add-ons, Selfhosting).

### 3.1 Startseite `/` — Budget 480

| # | Block | Pain Point der Zielgruppe | Odoo-Stärke / Antwort | Wörter | CTA |
|---|---|---|---|---|---|
| 1 | **Hero**: H1 (Ergebnis + Zielgruppe), Unterzeile (Odoo · Mittelstand · Hessen/Deutschland · Implementierung, Migration, Schulung, Pflege), Primär-CTA, Sekundär-Link „Leistungen ansehen", **Software-Bild** (Odoo-Screenshot-Platzhalter) | „Ich weiß nicht, ob das für uns ist" | O1 als Versprechen; die Software sichtbar (Phase 1: im Markt die Ausnahme) | **45** | primär |
| 2 | **Ausgangslage** („Kennen Sie das?"): drei Alltagsprobleme — Insellösungen & Excel-Listen, Doppelerfassung zwischen Vertrieb/Lager/Buchhaltung, keine Zahlen in Echtzeit | genau diese drei | O1, O3 | **60** | — |
| 3 | **Alles in einem System**: sechs Module als Kacheln — CRM & Vertrieb · Finanzen & Buchhaltung · Lager & Einkauf · Zeiterfassung & Projekte · Personal · Fertigung — je ein Satz „was es für den Betrieb tut" | „Wir bräuchten fünf Programme" | O1, O3 | **80** | Link → /leistungen/#module |
| 4 | **Warum Odoo** — Willys fünf Punkte, je ein knapper Satz (Zahl „20.000" gemäß C2-Entscheidung) | „Warum nicht SAP/Sage/Business Central?" (Phase 1: diese Vergleiche werden gesucht) | O1–O5 | **80** | — |
| 5 | **So gehen wir vor** — fünf Schritte: Potenzialgespräch → Analyse & Konzept → Einführung (ganz oder ein Modul) → Schulung → Pflege & Weiterentwicklung | „Was kommt da auf uns zu? Wie lange bindet uns das?" — ohne Dauer-Zahlen | Transparenz ersetzt Zähler (Phase 1, Lücke 1 & 5) | **75** | — |
| 6 | **Der KI-Hebel** (Teaser): ERP + KI-Automation aus einer Hand — was das konkret heißt (Dokumente, Rechnungen, Kommunikation), Link → /ueber-uns/#ki-hebel | „Wir wollen KI nutzen, aber unsere Daten liegen überall verstreut" | O2 (KI-Kompatibilität), O3 | **50** | Link |
| 7 | **Branchen** — vier Einstiege als Links | „Kennen die meine Branche?" | — | **25** | Links → /branchen/#… |
| 8 | **Vertrauen** — `[PLATZHALTER: Referenz/Logos/Zitat]` — Struktur reserviert; **wird ohne echte Inhalte nicht gebaut**, die Seite funktioniert ohne den Block | — | — | (15) | — |
| 9 | **CTA-Band** — voller CTA + ein Satz, was das Gespräch ist (`[PLATZHALTER: Dauer/Format]`) + Sekundär „oder schreiben Sie uns" | „Was passiert, wenn ich klicke?" | — | **30** | primär |
| | **Summe** | | | **445 (+15)** | |

### 3.2 Leistungen `/leistungen/` — Budget 600

| # | Block | Pain Point | Odoo-Stärke / Antwort | Wörter | CTA |
|---|---|---|---|---|---|
| 1 | **Hero**: H1 (Implementierung, Migration, Schulung, Pflege — ganzes ERP oder einzelne Module), Unterzeile, CTA | „Was genau bieten die?" | Willys Angebot 1:1 | **40** | primär |
| 2 | **Leistungspfad** — fünf Leistungen in Reihenfolge der Kundenreise: **Beratung & Potenzialanalyse** · **Implementierung** (ganzes System oder Module) · **Migration** (aus Altsystemen, Excel, Insellösungen) · **Schulung** · **Pflege & Support** — je: was, für wen, Ergebnis (ohne Zahlen) | je Stufe: „Wer macht was, was bleibt bei uns hängen?" | O1 (Implementierung), O3 (Migration = eine Datenbasis), O4 (Pflege = Erweiterung) | **5 × 40 = 200** | — |
| 3 | **Module** (#module) — sechs Kacheln wie Startseite, je 25 Wörter: Aufgabe im Betrieb, typische Funktionen (nur odoo.com-belegbar) | „Welches Modul löst welches Problem?" | O1 | **165** | — |
| 4 | **Zwei Wege** — „Ganzes ERP" vs. „Ein Modul zuerst": wann welcher Weg passt; beide führen ins Potenzialgespräch | „Wir können nicht alles auf einmal umstellen" | O4 (Phase 1, Lücke 5) | **70** | Link → /kontakt/ |
| 5 | **FAQ** (#faq) — 4 Fragen, nur belegbare Antworten: Community oder Enterprise? · Cloud oder eigener Server? · Was passiert mit unseren bestehenden Daten? · Können wir mit einem Modul starten? | Einwände | O2, O5 | **100** | — |
| 6 | **CTA-Band** | | | **25** | primär |
| | **Summe** | | | **600** | |

### 3.3 Branchen `/branchen/` — Budget 520

Jeder Branchenblock ist **Positionierung, kein Kundenclaim** (§4): „Was Odoo in
dieser Branche leistet", nie „was wir dort schon gemacht haben" (außer nach
Freigabe B3).

| # | Block | Pain Point | Odoo-Stärke / Antwort | Wörter | CTA |
|---|---|---|---|---|---|
| 1 | **Hero**: H1 (Branchen, in denen Odoo den Mittelstand entlastet), Unterzeile: die vier Branchen, CTA | „Für Firmen wie meine?" | — | **40** | primär |
| 2 | **Bau & Handwerk** (#bau) — Ausgangslage: Angebote/Nachträge, Projektzeiten, Nachunternehmer-Rechnungen; Module: Projekte, Zeiterfassung, Einkauf, Buchhaltung; typischer Einstieg: Zeiterfassung & Projekte | Zettelwirtschaft zwischen Baustelle und Büro | O1, O3 | **105** | — |
| 3 | **Produktion & Lebensmittelhandwerk** (#produktion) — Ausgangslage: Bestände, Chargen, Einkauf auf Zuruf; Module: Lager, Einkauf, Fertigung, Qualität; Einstieg: Lager & Einkauf | Materialengpässe, Rückverfolgbarkeit | O1, O3, O4 | **105** | — |
| 4 | **Handel & E-Commerce** (#handel) — Ausgangslage: Shop, Lager und Buchhaltung getrennt; Module: Verkauf, Lager, Website/Shop, Buchhaltung; Einstieg: Lager & Verkauf | Bestände stimmen nirgends | O1, O3 | **105** | — |
| 5 | **Dienstleistung, Beratung & Agenturen** (#dienstleistung) — Ausgangslage: Leads in Mails, Stunden in Excel, Rechnungen per Hand; Module: CRM, Projekte, Zeiterfassung, Abrechnung, Personal; Einstieg: CRM oder Zeiterfassung | Unabgerechnete Stunden, kein Vertriebsüberblick | O1, O3 | **105** | — |
| 6 | **„Ihre Branche fehlt?"** — Odoo ist modular; Potenzialgespräch klärt die Passung | Nischenbetriebe | O4 | **30** | Link |
| 7 | **CTA-Band** | | | **25** | primär |
| | **Summe** | | | **515** | |

### 3.4 Über uns & KI-Hebel `/ueber-uns/` — Budget 420

| # | Block | Pain Point | Antwort | Wörter | CTA |
|---|---|---|---|---|---|
| 1 | **Hero**: H1 (wer wir sind: I Robot - You Profit GmbH, Geschäftsfeld ERP), Unterzeile (Region, Fokus) | „Wer steckt dahinter?" | Firma real, Region real | **40** | — |
| 2 | **Zwei Geschäftsfelder, ein Ziel** — KI Beratung Hessen (seit `[PLATZHALTER: Jahr]`) + Odoo-ERP: warum beides zusammengehört | „Sind die neu? Können die das?" | ehrlich: neues Geschäftsfeld, gewachsene Firma; Zahlen nur nach Freigabe | **60** | Link KIBH (F1) |
| 3 | **Unsere Haltung** (#vorgehen) — drei Prinzipien: Standard vor Sonderbau · ein Modul darf der Anfang sein · keine Abhängigkeit (Open Source, Selfhosting möglich, Daten gehören Ihnen) | „Werden wir abhängig — vom Partner, vom Hersteller?" | O2, O4, O5 | **75** | — |
| 4 | **Der KI-Hebel** (#ki-hebel) — was ein ERP mit sauberer Datenbasis für KI-Automation möglich macht: Dokumenten- und Rechnungsverarbeitung, Kommunikation, Auswertungen — beschrieben als Fähigkeit von KIBH (belegt durch die KIBH-Website), **nicht** als ERP-Referenz | „KI ist überall Thema, aber wo fängt man an?" | O2, O3 (Phase 1, Lücke 2) | **90** | — |
| 5 | **Team** (#team) — `[PLATZHALTER: Personen, Rollen, Fotos]`; Struktur: 2–4 Karten | „Mit wem spreche ich?" | — | **(25)** | — |
| 6 | **Referenzen** (#referenzen) — Struktur: 3 Karten je Branche · Ausgangslage · Lösung · Ergebnis · Zitat · Logo — **alle Inhalte `[PLATZHALTER]`**; Regel (B2/B3): ERP-Referenzen sobald vorhanden; KIBH-KI-Referenzen nur mit sichtbarer Kennzeichnung „KI-Projekt" und nur nach Freigabe | „Haben die das schon mal gemacht?" | — | **(40)** | — |
| 7 | **CTA-Band** | | | **25** | primär |
| | **Summe** | | | **290 (+65 Platzhalter)** | |

### 3.5 Kontakt `/kontakt/` — Budget 240

| # | Block | Pain Point | Antwort | Wörter | CTA |
|---|---|---|---|---|---|
| 1 | **Hero**: H1 „Kostenloses ERP-Potenzialgespräch", ein Satz, was es ist und was nicht (kein Verkaufsgespräch, keine Verpflichtung) | „Werde ich in etwas hineingezogen?" | — | **35** | — |
| 2 | **Termin buchen** — `[PLATZHALTER: Calendly-Einbettung, D3]` mit Fallback-Link | „Ich will das jetzt erledigen" | — | **25** | = die Aktion |
| 3 | **Nachricht schreiben** — Formular `[PLATZHALTER: Formspree, D4]`: Name, Firma, E-Mail, Telefon (optional), Anliegen, Datenschutz-Checkbox | „Ich schreibe lieber" | — | **40** | = die Aktion |
| 4 | **So geht es weiter** — drei Schritte nach der Buchung (Gespräch → schriftliche Einschätzung → Entscheidung liegt bei Ihnen) | „Was passiert danach?" | — | **60** | — |
| 5 | **Kontaktdaten** — `[PLATZHALTER: Adresse, Telefon, E-Mail]` | | | **(20)** | — |
| 6 | **FAQ** — 2 Fragen: Was bringe ich mit? · Für wen ist das Gespräch gedacht? | | | **50** | — |
| | **Summe** | | | **210 (+20)** | |

### 3.6 Impressum, Datenschutz, 404

- **Impressum:** Überschriftenstruktur nach § 5 DDG (Anbieter, Vertretung,
  Kontakt, Registereintrag, USt-IdNr., Verantwortlich i. S. d. § 18 MStV,
  Streitschlichtung) — jeder Wert `[PLATZHALTER]`, Hinweisbanner „Entwurf —
  vor Go-live durch Willy zu prüfen" (nur im Review-Build sichtbar).
- **Datenschutz:** Überschriftenstruktur (Verantwortlicher, Hosting, Server-Logs,
  Kontaktformular, Terminbuchung, Webfonts (self-hosted — kein Drittanbieter),
  Analyse-Tool (nur falls D2 = ja), Rechte der Betroffenen) — Inhalte
  `[PLATZHALTER]`; Abschnitte für Calendly/Formspree/Analytics werden erst
  aktiviert, wenn das Werkzeug tatsächlich eingebettet ist.
- **404:** H1, ein Satz, drei Wege zurück (Startseite, Leistungen, Kontakt).

---

## 4. ASCII-Wireframes (Desktop ≥ 1025 px; Mobile-Hinweis je Seite)

Legende: `[ ]` Button · `( )` Platzhalter-Bild · `====` Abschnittsgrenze ·
`▸` Link. Maße folgen dem Spacing-Scale aus `design-tokens.md`.

### 4.1 Header + Footer (alle Seiten)

```
┌──────────────────────────────────────────────────────────────────────────┐
│ [MARKENNAME]        Leistungen   Branchen   Über uns   Kontakt   [Potenzialgespräch vereinbaren] │
└──────────────────────────────────────────────────────────────────────────┘
   ≤1024: [MARKENNAME] ............................................. [≡]
          Drawer: Leistungen / Branchen / Über uns / Kontakt / [CTA]

┌──────────────────────────────────────────────────────────────────────────┐
│ [MARKENNAME]                Seiten            Rechtliches      Kontakt    │
│ Ein Satz: was, für wen.     ▸ Leistungen      ▸ Impressum      [PLATZHALTER │
│                             ▸ Branchen        ▸ Datenschutz     Adresse]   │
│                             ▸ Über uns                          [Telefon]  │
│                             ▸ Kontakt                           [E-Mail]   │
│ ─────────────────────────────────────────────────────────────────────────  │
│ Ein Geschäftsfeld der I Robot - You Profit GmbH · KI-Beratung: ▸ KIBH (F1) │
└──────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Startseite

```
==== 1 HERO (2 Spalten, Text 1.1fr / Bild 1fr) =============================
  H1  Ergebnis für die Geschäftsführung,             ┌────────────────────┐
      nicht „wir sind Partner"                       │ (Odoo-Screenshot   │
  Unterzeile: Odoo · Mittelstand · Hessen/DE ·       │  z. B. Dashboard/  │
  Implementierung, Migration, Schulung, Pflege       │  CRM, 16:9, im     │
  [Kostenloses ERP-Potenzialgespräch vereinbaren]    │  Rahmen, radius-lg)│
  ▸ Leistungen ansehen                               └────────────────────┘
==== 2 AUSGANGSLAGE ("Kennen Sie das?") ====================================
  H2
  ┌ Insellösungen ┐ ┌ Doppelerfassung ┐ ┌ Keine Zahlen in Echtzeit ┐   (3 Spalten)
==== 3 ALLES IN EINEM SYSTEM (Module) ======================================
  H2 + ein Satz
  ┌CRM & Vertrieb┐ ┌Finanzen┐ ┌Lager & Einkauf┐                       (3 × 2 Kacheln)
  ┌Zeiterfassung ┐ ┌Personal┐ ┌Fertigung     ┐   ▸ Alle Leistungen
==== 4 WARUM ODOO (dunkles Band, --c-primary) ==============================
  H2
  1 Alles in einem System   2 Open Source & flexibel   3 Zentrale Daten
  4 Skalierbar              5 Keine Lock-ins            (Liste, kein Kartenraster)
==== 5 SO GEHEN WIR VOR =====================================================
  H2
  Potenzialgespräch → Analyse & Konzept → Einführung → Schulung → Pflege
  (5 Schritte als echte Sequenz — hier sind Nummern erlaubt, weil es eine ist)
==== 6 KI-HEBEL (2 Spalten: Text / stilles Bild-Placeholder) ==============
  H2 + 50 Wörter + ▸ Mehr zum KI-Hebel
==== 7 BRANCHEN ============================================================
  ▸ Bau & Handwerk  ▸ Produktion & Lebensmittelhandwerk  ▸ Handel & E-Commerce  ▸ Dienstleistung
==== 8 [VERTRAUEN — nur mit echten Inhalten] ===============================
==== 9 CTA-BAND (surface-alt) ==============================================
  H2 + Satz [PLATZHALTER Dauer/Format]   [Kostenloses ERP-Potenzialgespräch vereinbaren]
  ▸ oder schreiben Sie uns
```
Mobile (≤ 767): Hero einspaltig, Bild **unter** dem CTA (der CTA bleibt im
ersten Viewport); Kacheln 1-spaltig; Vorgehen als vertikale Liste; Warum-Odoo
als Liste (ohnehin).

### 4.3 Leistungen

```
==== HERO (einspaltig, linksbündig, max 46rem) ==============================
  H1 · Unterzeile · [CTA]
==== LEISTUNGSPFAD (vertikale Sequenz, jede Stufe: Titel links, Text rechts) ==
  Beratung & Potenzialanalyse ───── Text (40 W)
  Implementierung ────────────────── Text
  Migration ──────────────────────── Text
  Schulung ───────────────────────── Text
  Pflege & Support ───────────────── Text
==== MODULE #module (3 × 2 Kacheln, wie Startseite, 25 W je Kachel) =========
==== ZWEI WEGE (2 Spalten) ==================================================
  ┌ Ganzes ERP ┐          ┌ Ein Modul zuerst ┐        ▸ Im Gespräch klären
==== FAQ #faq (Akkordeon, 4 Fragen; erste offen) ============================
==== CTA-BAND ===============================================================
```
Mobile: Leistungspfad Titel über Text; Zwei Wege untereinander; Akkordeon
bleibt (Touch-Ziel ≥ 44 px).

### 4.4 Branchen

```
==== HERO ===================================================================
==== SPRUNGLEISTE (4 Anker, sticky unter dem Header ab 1025 px) =============
==== BRANCHE 1 #bau (2 Spalten: Ausgangslage-Bullets | Module + Einstieg) ===
  H2 Bau & Handwerk
  Ausgangslage: • • •            Passende Module: CRM · Projekte · Zeiterfassung …
                                 Typischer Einstieg: Zeiterfassung & Projekte
==== BRANCHE 2 #produktion ========= (gleiches Raster, Hintergrund wechselt) ==
==== BRANCHE 3 #handel ======================================================
==== BRANCHE 4 #dienstleistung ==============================================
==== „IHRE BRANCHE FEHLT?" (kurz, zentriert) + CTA-BAND =====================
```
Mobile: Sprungleiste wird zu 4 Chips oben; Branchenblöcke einspaltig.

### 4.5 Über uns & KI-Hebel

```
==== HERO ===================================================================
==== ZWEI GESCHÄFTSFELDER (2 Spalten: KI Beratung Hessen | Odoo-ERP) ========
==== HALTUNG #vorgehen (3 Prinzipien nebeneinander, Text, keine Karten) =====
==== KI-HEBEL #ki-hebel (dunkles Band, 2 Spalten: Text | stilles Bild) ======
==== TEAM #team ([PLATZHALTER] 2–4 Karten, Foto 1:1, Name, Rolle) ===========
==== REFERENZEN #referenzen ([PLATZHALTER] 3 Karten: Branche · Ausgangslage · =
     Lösung · Ergebnis · Zitat · Logo — Kennzeichnung „KI-Projekt" falls B3) =
==== CTA-BAND ===============================================================
```

### 4.6 Kontakt

```
==== HERO (einspaltig) ======================================================
==== 2 SPALTEN ==============================================================
  ┌ Termin buchen ────────────────┐   ┌ Nachricht schreiben ───────────┐
  │ [PLATZHALTER Calendly, D3]    │   │ Name · Firma · E-Mail · Telefon │
  │ ▸ Fallback-Link               │   │ Anliegen · ☐ Datenschutz        │
  └───────────────────────────────┘   │ [Nachricht senden]  (D4)        │
                                      └─────────────────────────────────┘
==== SO GEHT ES WEITER (3 Schritte, Sequenz) ================================
==== KONTAKTDATEN [PLATZHALTER] · FAQ (2) ===================================
```
Mobile: Termin zuerst, Formular darunter.

---

## 5. Platzierung des primären CTA

Regel: **Header (immer) + genau ein CTA-Band am Seitenende**; die Startseite
zusätzlich im Hero. Kein CTA nach jedem Block — Phase 1 zeigt, wie „Demo
buchen" nach jedem zweiten Abschnitt wirkt.

| Seite | Positionen | Warum dort |
|---|---|---|
| Startseite | Hero · Band am Ende | Hero: der entschlossene Besucher (Empfehlung, Wiederkehrer) soll nicht scrollen müssen. Ende: nach Vorgehen + KI-Hebel ist die Frage „warum die?" beantwortet |
| Leistungen | Band am Ende; „Zwei Wege" verlinkt textlich | Nach Leistungspfad, Modulen und FAQ sind die Einwände abgeräumt — davor wäre der CTA eine Unterbrechung |
| Branchen | Band am Ende (+ „Ihre Branche fehlt?" als weicher Einstieg) | Wer seinen Block gelesen hat, ist qualifiziert |
| Über uns | Band am Ende | Vertrauen ist der letzte Schritt vor der Handlung |
| Kontakt | Die Seite selbst (Buchung + Formular) | — |
| Impressum/Datenschutz/404 | nur Header; 404 zusätzlich „▸ Kontakt" | rechtliche Seiten bleiben ruhig |

Sekundär-CTA (nur Startseite-Hero): „Leistungen ansehen" — für den Besucher,
der erst verstehen will. Kein `→` an Links und Buttons (CLAUDE.md §6).

---

## 6. Wortbudget-Übersicht

| Seite | Budget | Lesezeit (200 W/min) | Limit | Hero |
|---|---|---|---|---|
| Startseite | 445 (+15 Platzhalter) | 2,2 min | 2–3 min ✓ | 45 ✓ |
| Leistungen | 600 | 3,0 min | ✓ (Obergrenze) | 40 ✓ |
| Branchen | 515 | 2,6 min | ✓ | 40 ✓ |
| Über uns | 290 (+65) | 1,5–1,8 min | ✓ | 40 ✓ |
| Kontakt | 210 (+20) | 1,1 min | ✓ | 35 ✓ |

Phase 3 zählt die tatsächlichen Wörter je Seite und meldet sie in
`content.md`; Blöcke, die ihr Budget überschreiten, werden gekürzt, nicht die
Limits erhöht.

---

## 7. Was diese Struktur aus Phase 1 umsetzt

| Lücke / Regel (marktanalyse.md) | Umsetzung |
|---|---|
| Ergebnis statt Selbstbeschreibung | Hero-H1 + Block „Ausgangslage" auf der Startseite |
| Software zeigen | Hero-Bild der Startseite ist ein Odoo-Screenshot (Platzhalter, `bildbedarf.md` in Phase 4) |
| ERP + KI aus einer Hand | KI-Hebel-Teaser (Startseite) + Abschnitt (Über uns) |
| Rhein-Main / Hessen | Region in Unterzeilen, Kontaktdaten, SEO (Phase 3) — ohne Landingpage-Spam |
| Keine Lock-ins, Selfhosting | Warum Odoo (5) + Haltung (Über uns) + FAQ „Cloud oder eigener Server?" |
| Modularer Einstieg | „Zwei Wege" (Leistungen), „typischer Einstieg" je Branche, Vorgehen Schritt 3 |
| Keine Monsterseite | Budgets oben; ein CTA-Band je Seite |
| Keine gefälschten Trust-Signale | Vertrauen-Block nur mit echten Inhalten; Referenzen als Platzhalter-Struktur |
