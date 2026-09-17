# Content — alle Texte der Website (Punkt 3)

> Alle Texte an einem Ort, damit Willy sie prüfen kann, ohne HTML zu lesen.
> Stand: 2026-09-18 (Phase 3, Entwurf zur Freigabe).
>
> **Lesehilfe**
> - `> Quelle:` unter einem Block nennt die Herkunft jeder Faktenaussage
>   (CLAUDE.md §2 = Willys Angaben; odoo.com = auf Odoos Seiten belegt).
>   Diese Zeilen sind keine Website-Texte.
> - `[PLATZHALTER PH-nn: …]` ist eine Lücke, die echte Angaben braucht.
>   Was genau, steht in `platzhalter.md` unter derselben Nummer.
> - `[MARKENNAME]` wird am Ende in einem Zug ersetzt.
> - Wortzählung je Seite: §10 am Ende (Skript, nicht geschätzt).
>
> **Was Willy prüfen sollte:** Stimmt die Aussage? Klingt es nach uns? Fehlt
> etwas Wichtiges? Zahlen, Referenzen, Namen und Preise stehen bewusst nicht im
> Text — dafür gibt es Platzhalter.

---

## 1. Global: Header, Footer, Meta

### Header
- Wortmarke: `[MARKENNAME]` (Link zur Startseite; Alt-Text „[MARKENNAME] – zur Startseite")
- Navigation: **Leistungen** · **Branchen** · **Über uns** · **Kontakt**
- Button: **Potenzialgespräch vereinbaren** (→ /kontakt/)
- Skip-Link: „Zum Inhalt springen" · Burger: „Menü öffnen" / „Menü schließen"

### Footer
- `[MARKENNAME]` — „Odoo-Einführung für den Mittelstand: komplett oder Modul für Modul. Implementierung, Migration, Schulung und Pflege."
- **Seiten:** Leistungen · Branchen · Über uns · Kontakt
- **Rechtliches:** Impressum · Datenschutz
- **Kontakt:** `[PLATZHALTER PH-04: Anschrift]` · `[PLATZHALTER PH-04: Telefon]` · `[PLATZHALTER PH-04: E-Mail]`
- Zeile: „Ein Geschäftsfeld der I Robot - You Profit GmbH." · „KI-Beratung: KI Beratung Hessen" `[PH-19: Link ja/nein]`
- „© 2026 I Robot - You Profit GmbH"

> Quelle: Firmenname und Geschäftsfelder — CLAUDE.md §1.

### Title / Meta-Description je Seite
Siehe `seo-keywords.md` §3 (dort gepflegt, hier nicht doppelt).

---

## 2. Startseite `/`

### 2.1 Hero
**H1:** Ein System statt fünf Programmen und zehn Excel-Listen.

**Unterzeile:** [MARKENNAME] führt Odoo ein, das Open-Source-ERP für den Mittelstand – komplett oder Modul für Modul: CRM, Lager, Buchhaltung, Zeiterfassung, Personal. Implementierung, Migration, Schulung und Pflege aus Hessen.

**Buttons:** Kostenloses ERP-Potenzialgespräch vereinbaren · Leistungen ansehen

**Bild:** `[PLATZHALTER PH-13: Odoo-Screenshot]`

> Quelle: Angebot und Module — CLAUDE.md §2 („Implementierung samt Migration, Schulung und Pflege … CRM, Zeiterfassung, Personal, Lagerhaus"). Odoo ist Open Source — odoo.com (Community-Edition, LGPLv3). „aus Hessen" — PH-17 (F3).

### 2.2 Kennen Sie das?
**H2:** Kennen Sie das?

- Vertrieb, Lager und Buchhaltung arbeiten in verschiedenen Programmen – und keines kennt die Daten des anderen.
- Dieselbe Bestellung wird dreimal erfasst: im Angebot, im Lieferschein, in der Rechnung.
- Wie läuft der Monat? Die Antwort braucht einen Tag – und stimmt am Ende doch nicht ganz.

Das ist kein Fleißproblem Ihrer Mitarbeiter. Es ist ein Systemproblem – und lösbar.

> Quelle: keine Faktenaussage; beschreibt die Ausgangslage der Zielgruppe (informationsarchitektur.md, Funnel Stufe 2).

### 2.3 Alles in einem System
**H2:** Alles in einem System

Odoo verbindet die Abläufe Ihres Unternehmens in einer Software. Sie starten mit dem Modul, das am meisten drückt.

- **CRM & Vertrieb** — Vom ersten Kontakt bis zum Auftrag: jeder Lead sichtbar, jeder Schritt nachvollziehbar.
- **Finanzen & Buchhaltung** — Rechnungen, Zahlungen, offene Posten: Buchhaltung, die aus den Belegen entsteht.
- **Lager & Einkauf** — Bestände in Echtzeit, Nachbestellung nach Regeln – ohne Zettel, ohne Zuruf.
- **Zeiterfassung & Projekte** — Stunden erfassen, Projekte planen, abrechnen – aus denselben Daten.
- **Personal** — Mitarbeiterdaten, Urlaub, Bewerbungen: an einem Ort statt in Ordnern.
- **Fertigung** — Aufträge, Stücklisten, Arbeitspläne: die Produktion sieht, was verkauft wurde.

Link: Alle Leistungen und Module

> Quelle: CLAUDE.md §2 Punkt 1 („Alles in einem System"); die sechs Module entsprechen Odoo-Apps (CRM, Sales, Invoicing/Accounting, Inventory, Purchase, Timesheets, Project, Employees, Time Off, Recruitment, Manufacturing) — odoo.com/page/all-apps.

### 2.4 Warum Odoo?
**H2:** Warum Odoo?

Fünf Gründe, die für den Mittelstand zählen:

(Im HTML als Liste mit fetten Lead-ins, ohne Nummern-Marker — CLAUDE.md §6.)

1. **Alles in einem System.** CRM, Verkauf, Einkauf, Lager, Buchhaltung und mehr – zentral verbunden.
2. **Open Source und flexibel.** Anpassbar an Ihre Abläufe, offen für KI-Automation.
3. **Eine Datenbasis.** Alle Unternehmensdaten an einem Ort und in Echtzeit verfügbar.
4. **Skalierbar.** Neue Funktionen, Nutzer und Geschäftsbereiche jederzeit ergänzbar – ohne Neustart.
5. **Kein Vendor-Lock-in.** Über 20.000 Mitwirkende weltweit, tausende Add-ons, Selfhosting möglich – Ihre Daten und Ihre Kosten bleiben bei Ihnen.

> Quelle: CLAUDE.md §2, Vorteile 1–5, umformuliert. „Über 20.000 Mitwirkende" — odoo.com/page/community („20,000+ people contribute"), Formulierung PH-18 (C2). „Tausende Add-ons" — odoo.com („40k+ community apps"). „Selfhosting möglich" — Odoo-Dokumentation, Administration (On-premise).

### 2.5 So gehen wir vor
**H2:** So gehen wir vor

1. **Potenzialgespräch.** Wir hören zu: Wo hakt es, was soll sich ändern? Kostenlos und unverbindlich.
2. **Analyse und Konzept.** Wir sehen uns Ihre Abläufe und Systeme an und empfehlen, womit Sie starten – auch wenn es nur ein Modul ist.
3. **Einführung.** Wir richten Odoo ein, übernehmen Ihre Daten aus Altsystemen und Excel und binden an, was bleibt.
4. **Schulung.** Ihr Team lernt Odoo an den eigenen Abläufen – nicht an Beispielen aus dem Handbuch.
5. **Pflege.** Updates, Support, neue Module: Odoo wächst mit, wir bleiben dran.

> Quelle: CLAUDE.md §2 (Implementierung, Migration, Schulung, Pflege; ganzes System oder einzelne Module). Die Fünf-Schritte-Folge ist ein Positionierungsvorschlag — Freigabe Willy (PH-20).

### 2.6 Der KI-Hebel
**H2:** Der KI-Hebel

Ein ERP mit sauberer Datenbasis ist die Voraussetzung für KI, die wirklich arbeitet: Eingangsrechnungen prüfen, Dokumente auslesen, Anfragen vorsortieren. Unser Schwestergeschäftsfeld KI Beratung Hessen entwickelt genau solche Automationen – und Odoo ist dafür ein offenes Fundament.

Link: Mehr zum KI-Hebel

**Bild:** `[PLATZHALTER PH-14: ruhiges Motiv]`

> Quelle: Automationsbeispiele — Leistungsangebot auf kiberatunghessen.com (Rechnungsprüfung, Dokumentenverarbeitung, Kommunikation); „offenes Fundament" — CLAUDE.md §2 Punkt 2 („maximale Kompatibilität mit KI-Automationen").

### 2.7 Odoo in Ihrer Branche
**H2:** Odoo in Ihrer Branche

- Bau & Handwerk
- Produktion & Lebensmittelhandwerk
- Handel & E-Commerce
- Dienstleistung, Beratung & Agenturen

(Vier Links auf /branchen/#…; im HTML als Liste, nicht als Punkt-getrennte Zeile.)

### 2.8 Vertrauen — nur mit echten Inhalten
`[PLATZHALTER PH-09: Kundenlogos oder ein Zitat — sonst wird dieser Block nicht gebaut]`

### 2.9 CTA-Band
**H2:** Wo steht Ihr Unternehmen – und wo könnte es mit einem System stehen?

Im kostenlosen ERP-Potenzialgespräch klären wir, ob und wie Odoo zu Ihnen passt. `[PLATZHALTER PH-03: Dauer und Format, z. B. „30 Minuten per Video"]` Kein Verkaufsgespräch, keine Verpflichtung.

**Button:** Kostenloses ERP-Potenzialgespräch vereinbaren · Link: oder schreiben Sie uns

---

## 3. Leistungen `/leistungen/`

### 3.1 Hero
**H1:** Odoo einführen – komplett oder Modul für Modul

**Unterzeile:** Implementierung, Migration, Schulung und Pflege: [MARKENNAME] begleitet Ihr Unternehmen vom ersten Gespräch bis zum laufenden Betrieb – ob ganzes ERP oder einzelne Module wie CRM, Lager, Zeiterfassung und Personal.

**Button:** Kostenloses ERP-Potenzialgespräch vereinbaren

> Quelle: CLAUDE.md §2.

### 3.2 Von der Analyse bis zum laufenden Betrieb
**H2:** Von der Analyse bis zum laufenden Betrieb

**H3 Beratung & Potenzialanalyse** `#beratung`
Bevor wir etwas einrichten, verstehen wir Ihren Betrieb: Welche Programme laufen, wo Daten doppelt erfasst werden, welche Zahlen fehlen. Daraus entsteht eine Empfehlung, womit Sie starten sollten – und womit nicht.

**H3 Implementierung** `#einfuehrung`
Wir konfigurieren Odoo für Ihre Abläufe – so nah am Standard wie möglich, damit Updates einfach bleiben. Wo Ihr Betrieb anders arbeitet, passen wir an. Schnittstellen zu Werkzeugen, die bleiben, gehören dazu.

**H3 Migration** `#migration`
Kunden, Artikel, Lieferanten, offene Posten, Belege: Wir übernehmen Ihre Daten aus Altsystemen, Excel-Listen und Insellösungen nach Odoo – bereinigt, geprüft, nachvollziehbar. Der Wechsel wird so geplant, dass der Betrieb weiterläuft.

**H3 Schulung** `#schulung`
Ihr Team lernt Odoo an den eigenen Aufgaben: der Vertrieb an seinen Angeboten, das Lager an seinen Buchungen. Rollenbezogen, in kleinen Gruppen, mit Unterlagen für den Alltag.

**H3 Pflege & Support** `#pflege`
Nach dem Start bleiben wir Ansprechpartner: für Fragen aus dem Alltag, Anpassungen, Updates – und neue Module, wenn Ihr Unternehmen wächst.

> Quelle: CLAUDE.md §2 (Implementierung, Migration, Schulung, Pflege). „So nah am Standard wie möglich" ist Haltung, kein Fakt — PH-20. Keine Reaktionszeiten, Laufzeiten oder SLAs genannt (§4).

### 3.3 Die Module `#module`
**H2:** Die Module

Jedes Modul arbeitet für sich – und mit den anderen zusammen.

**H3 CRM & Vertrieb**
Leads, Angebote und Aufträge in einer Pipeline. Der Vertrieb sieht, wer wann mit wem gesprochen hat und was ansteht. Ein Angebot wird per Klick zum Auftrag und zur Rechnung.

**H3 Finanzen & Buchhaltung**
Rechnungen entstehen aus Aufträgen, Zahlungen werden abgeglichen, offene Posten sind sichtbar. DATEV-Export und die ELSTER-Übermittlung der Umsatzsteuer-Voranmeldung sind in der deutschen Lokalisierung von Odoo Enterprise enthalten.

**H3 Lager & Einkauf**
Bestände in Echtzeit über alle Lagerorte, Nachbestellung nach Regeln, Wareneingang per Scanner. Der Einkauf sieht, was der Vertrieb verkauft hat – bevor etwas fehlt.

**H3 Zeiterfassung & Projekte**
Stunden auf Projekte und Aufgaben buchen, Planung und Abrechnung aus denselben Daten. Wer wie lange woran gearbeitet hat, steht fest – ohne Nachfragen am Monatsende.

**H3 Personal**
Mitarbeiterdaten, Urlaub und Abwesenheiten, Bewerbungen und Onboarding in einem Modul – verbunden mit Zeiterfassung und Projekten.

**H3 Fertigung**
Fertigungsaufträge, Stücklisten und Arbeitspläne, verbunden mit Lager und Verkauf: Die Produktion plant mit echten Beständen und echten Aufträgen.

> Quelle: Odoo-Apps und -Funktionen — odoo.com/page/all-apps (CRM, Sales: Angebot → Auftrag → Rechnung; Inventory: mehrere Lagerorte, Nachbestellregeln, Barcode; Purchase; Timesheets; Project; Employees; Time Off; Recruitment; Manufacturing: Fertigungsaufträge, Stücklisten, Arbeitspläne). DATEV-Export (`l10n_de_reports`) und ELSTER-UStVA (`l10n_de_reports_elster`) — Odoo-Dokumentation 19.0, Fiscal Localizations → Germany; beide setzen die Enterprise-Buchhaltungsberichte voraus, daher „Odoo Enterprise". „Wareneingang per Scanner" — Odoo Barcode (Enterprise-App).

### 3.4 Zwei Wege zum Start
**H2:** Zwei Wege zum Start

**H3 Das ganze ERP**
Wenn mehrere Bereiche gleichzeitig an ihre Grenzen stoßen und Sie den Wechsel in einem Zug wollen.

**H3 Ein Modul zuerst**
Wenn ein Bereich am meisten drückt – meist Vertrieb, Lager oder Zeiterfassung – und der Rest später folgen soll.

Welcher Weg passt, klären wir im Potenzialgespräch.

Link: Potenzialgespräch vereinbaren

> Quelle: CLAUDE.md §2 („ganzes ERP-System oder einzelne Module"; Vorteil 4 „Skalierbar").

### 3.5 Häufige Fragen `#faq`
**H2:** Häufige Fragen

**Community oder Enterprise?**
Odoo gibt es als kostenlose Open-Source-Version (Community) und als Enterprise-Version mit zusätzlichen Modulen und Herstellersupport, lizenziert pro Nutzer. Welche passt, hängt von den Modulen ab, die Sie brauchen.

**Cloud oder eigener Server?**
Beides. Odoo läuft in der Odoo-Cloud oder auf einem Server Ihrer Wahl – im Rechenzentrum oder bei Ihnen im Haus. Selfhosting ist möglich; mit der Community-Version sogar ohne Lizenzkosten.

**Was ist mit DATEV und GoBD?**
Der DATEV-Export ist in der deutschen Lokalisierung von Odoo Enterprise enthalten, ebenso die ELSTER-Übermittlung der Umsatzsteuer-Voranmeldung. Die GoBD gelten für Sie als Unternehmen, nicht für die Software – Odoo stellt dafür Mittel bereit, etwa den GoBD-Export für die Betriebsprüfung, und wir richten das System entsprechend ein.

**Können wir mit einem Modul starten?**
Ja. Odoo ist modular: CRM, Zeiterfassung oder Lager laufen für sich und werden später um weitere Module ergänzt – ohne Neuanfang.

**Was kostet Odoo?**
Die Lizenzpreise legt Odoo fest und veröffentlicht sie auf odoo.com; die Community-Version ist kostenlos. Was die Einführung kostet, hängt vom Umfang ab – dafür bekommen Sie ein konkretes Angebot.

> Quelle: Editionen — odoo.com/page/editions (Community kostenlos/Open Source; Enterprise lizenziert pro Nutzer). Hosting — Odoo-Dokumentation, Administration (Odoo Online, Odoo.sh, On-premise). DATEV/ELSTER — Odoo-Dokumentation, Germany. GoBD — Odoo-Dokumentation, Germany, Abschnitt „GoBD compliance": „GoBD applies only to the taxpayer, the software editor can by no means be held responsible …"; „GoBD export" (Z1–Z3). Preise: bewusst keine Zahl (§4), Verweis auf odoo.com.

### 3.6 CTA-Band
**H2:** Welcher Weg passt zu Ihnen?

Das klären wir im kostenlosen ERP-Potenzialgespräch – ohne Verpflichtung.

**Button:** Kostenloses ERP-Potenzialgespräch vereinbaren

---

## 4. Branchen `/branchen/`

> Regel (CLAUDE.md §4, Branchenfokus): jeder Block beschreibt, was Odoo in der Branche leistet — nie, was wir dort schon gemacht haben.

### 4.1 Hero
**H1:** Odoo für Bau, Produktion, Handel und Dienstleistung

**Unterzeile:** Vier Branchen, in denen Insellösungen am teuersten sind – und was Odoo dort verbindet. Ihre Branche fehlt? Odoo ist modular; die Passung klären wir im Potenzialgespräch.

**Button:** Kostenloses ERP-Potenzialgespräch vereinbaren

### 4.2 Bau & Handwerk `#bau`
**H2:** Bau & Handwerk

**Ausgangslage**
- Angebote und Nachträge entstehen in Word, die Stunden auf der Baustelle auf Zetteln, die Rechnungen der Nachunternehmer im Postfach.
- Am Monatsende weiß niemand genau, welches Projekt Geld verdient hat.
- Material wird bestellt, wenn es fehlt – nicht, wenn es geplant war.

**Passende Module:** Projekte, Zeiterfassung, Einkauf, Buchhaltung – und CRM für Anfragen und Angebote.

**Typischer Einstieg:** Zeiterfassung & Projekte. Stunden werden dort erfasst, wo sie entstehen, und landen direkt auf dem Projekt.

### 4.3 Produktion & Lebensmittelhandwerk `#produktion`
**H2:** Produktion & Lebensmittelhandwerk

**Ausgangslage**
- Bestände stehen in einer Liste, die beim Ausdrucken schon veraltet ist.
- Chargen und Haltbarkeiten müssen rückverfolgbar sein – von Hand ist das Fleißarbeit mit Fehlerrisiko.
- Der Einkauf erfährt vom Großauftrag, wenn das Material knapp wird.

**Passende Module:** Lager, Einkauf, Fertigung, Qualität, Verkauf – mit Chargen- und Seriennummern und Ablaufdaten im Standard.

**Typischer Einstieg:** Lager & Einkauf. Bestände in Echtzeit, Nachbestellung nach Regeln – und die Produktion plant mit echten Zahlen.

> Quelle: Chargen-/Seriennummern und Ablaufdaten — Odoo Inventory (Lots & Serial Numbers, Expiration Dates), odoo.com; Qualitätsmodul — Odoo Quality.

### 4.4 Handel & E-Commerce `#handel`
**H2:** Handel & E-Commerce

**Ausgangslage**
- Der Shop kennt andere Bestände als das Lager – und die Buchhaltung andere als beide.
- Bestellungen aus Shop, Telefon und Außendienst werden in drei Systemen erfasst.
- Retouren und Gutschriften laufen über E-Mails und Erinnerungen.

**Passende Module:** Verkauf, Lager, Website & Shop, Buchhaltung, Kasse – ein Artikelstamm, ein Bestand, ein Kundenkonto.

**Typischer Einstieg:** Lager & Verkauf. Ein Bestand für alle Kanäle, Aufträge aus jedem Kanal an einem Ort.

> Quelle: Odoo eCommerce, Point of Sale — odoo.com/page/all-apps.

### 4.5 Dienstleistung, Beratung & Agenturen `#dienstleistung`
**H2:** Dienstleistung, Beratung & Agenturen

**Ausgangslage**
- Leads liegen in Postfächern, Angebote in Ordnern – und der Stand eines Kunden im Kopf eines Kollegen.
- Stunden werden am Monatsende aus dem Gedächtnis nachgetragen – und zu wenig abgerechnet.
- Neue Mitarbeiter, Urlaub, Bewerbungen: alles per E-Mail und Tabelle.

**Passende Module:** CRM, Projekte, Zeiterfassung, Abrechnung, Personal – vom Lead bis zur Rechnung in einem Datensatz.

**Typischer Einstieg:** CRM oder Zeiterfassung – das Modul, das im Alltag am meisten drückt. Beide wachsen zusammen.

### 4.6 Ihre Branche fehlt?
**H2:** Ihre Branche fehlt?

Odoo ist modular und in vielen weiteren Branchen im Einsatz. Ob es zu Ihren Abläufen passt, klären wir in einem Gespräch – ehrlich, auch wenn die Antwort Nein lautet.

> Quelle: Branchenbreite — odoo.com/industries.

### 4.7 CTA-Band
**H2:** Sprechen wir über Ihre Abläufe

Im kostenlosen ERP-Potenzialgespräch sehen wir uns an, wo bei Ihnen die Daten heute liegen – und wo sie liegen könnten.

**Button:** Kostenloses ERP-Potenzialgespräch vereinbaren

---

## 5. Über uns & KI-Hebel `/ueber-uns/`

### 5.1 Hero
**H1:** Wer hinter [MARKENNAME] steht

**Unterzeile:** [MARKENNAME] ist das Geschäftsfeld Digitalisierung und ERP der I Robot - You Profit GmbH aus Hessen – die Schwester von KI Beratung Hessen. Wir führen Odoo im Mittelstand ein: mit der Haltung eines Beratungshauses, nicht eines Softwareverkäufers.

> Quelle: CLAUDE.md §1 (Firma, zwei Geschäftsfelder). „aus Hessen" — PH-17. Der letzte Satz ist Positionierung — PH-20.

### 5.2 Zwei Geschäftsfelder, ein Zusammenhang
**H2:** Zwei Geschäftsfelder, ein Zusammenhang

KI Beratung Hessen entwickelt seit `[PLATZHALTER PH-10: Jahr]` KI-Automationen für den Mittelstand – von der Dokumentenverarbeitung bis zur internen Kommunikation. Der Zusammenhang ist einfach: KI arbeitet nur so gut, wie die Daten darunter geordnet sind. Deshalb gibt es [MARKENNAME] – für das System, das die Daten ordnet. Beides denken wir zusammen.

Link: Zur KI Beratung Hessen `[PH-19]`

> Quelle: Leistungen von KIBH — kiberatunghessen.com (Dokumentenverarbeitung, Prozessautomatisierung, interne Kommunikation). Keine Zahlen, keine Projektanzahl (§4).

### 5.3 Unsere Haltung `#vorgehen`
**H2:** Unsere Haltung

**H3 Standard vor Sonderbau**
Wir richten Odoo so nah am Standard ein wie möglich. Das hält Updates einfach und Kosten überschaubar. Sonderbau gibt es dort, wo Ihr Betrieb wirklich anders arbeitet.

**H3 Ein Modul darf der Anfang sein**
Niemand muss sein Unternehmen an einem Wochenende umstellen. Wer mit Zeiterfassung oder CRM beginnt, hat schon gewonnen – der Rest kommt, wenn er passt.

**H3 Keine Abhängigkeit**
Odoo ist Open Source, Selfhosting ist möglich, Ihre Daten gehören Ihnen. Sie könnten jederzeit mit einem anderen Partner weiterarbeiten – wir arbeiten dafür, dass Sie es nicht wollen.

> Quelle: Open Source, Selfhosting — CLAUDE.md §2 Punkt 2 und 5; Odoo-Dokumentation (On-premise). Die drei Prinzipien sind ein Positionierungsvorschlag — PH-20.

### 5.4 Der KI-Hebel `#ki-hebel`
**H2:** Der KI-Hebel: erst das System, dann die Automation

Ein ERP sammelt, was im Unternehmen passiert: Aufträge, Belege, Stunden, Bestände. Liegt das an einem Ort, kann KI darauf arbeiten – Eingangsrechnungen prüfen, Dokumente auslesen und zuordnen, Anfragen vorsortieren, Auswertungen in Sprache erklären. Genau solche Automationen entwickelt KI Beratung Hessen.

Odoo ist dafür ein offenes Fundament: Open Source, mit Schnittstellen, an die sich KI-Werkzeuge direkt anbinden lassen. Für Sie heißt das: ein Partner für das System, das die Daten ordnet – und für die Automation, die damit arbeitet.

**Bild:** `[PLATZHALTER PH-14: ruhiges Motiv]`

> Quelle: Automationsbeispiele — kiberatunghessen.com (Rechnungsprüfung, Dokumentenverarbeitung, Chatbots/Kommunikation). Schnittstellen — Odoo External API (XML-RPC/JSON-RPC), Odoo-Dokumentation; CLAUDE.md §2 Punkt 2.

### 5.5 Ihre Ansprechpartner `#team`
**H2:** Ihre Ansprechpartner

`[PLATZHALTER PH-07: 2–4 Personen — Name, Rolle, Foto, ein Satz]`

### 5.6 Referenzen `#referenzen`
**H2:** Referenzen

`[PLATZHALTER PH-08: 3 Karten — Branche · Ausgangslage · Lösung · Ergebnis · Zitat mit Name und Funktion · Logo. Nur echte ERP/Odoo-Projekte; KIBH-KI-Projekte nur mit Kennzeichnung „KI-Projekt" und nach Freigabe B3.]`

Option, falls zum Launch keine Referenz vorliegt (Freigabe Willy): „[MARKENNAME] ist ein junges Geschäftsfeld einer gewachsenen Firma. Erste Odoo-Projekte dokumentieren wir hier, sobald unsere Kunden zustimmen."

### 5.7 CTA-Band
**H2:** Lernen wir uns kennen

Ein kostenloses ERP-Potenzialgespräch ist der einfachste Anfang – ohne Verpflichtung.

**Button:** Kostenloses ERP-Potenzialgespräch vereinbaren

---

## 6. Kontakt `/kontakt/`

### 6.1 Hero
**H1:** Kostenloses ERP-Potenzialgespräch

**Unterzeile:** Ein Gespräch über Ihre Abläufe, Ihre Systeme und die Frage, ob und wie Odoo zu Ihnen passt. Kein Verkaufsgespräch, keine Verpflichtung. `[PLATZHALTER PH-03: Dauer und Format, z. B. „30 Minuten per Video oder Telefon"]`

### 6.2 Termin wählen
**H2:** Termin wählen

Sie sehen freie Zeiten und wählen, was passt. Die Bestätigung kommt per E-Mail.

`[PLATZHALTER PH-05: Calendly-Einbettung]`

Fallback: Falls die Terminauswahl nicht lädt: Schreiben Sie uns kurz – wir melden uns mit Terminvorschlägen.

### 6.3 Oder schreiben Sie uns
**H2:** Oder schreiben Sie uns

Formular `[PLATZHALTER PH-06: Formspree]`:
- Name *
- Firma
- E-Mail *
- Telefon (optional)
- Ihr Anliegen *
- ☐ Ich habe die Datenschutzerklärung gelesen und bin damit einverstanden, dass meine Angaben zur Bearbeitung der Anfrage verarbeitet werden. *
- **Button:** Nachricht senden

Erfolg: Danke – Ihre Nachricht ist angekommen. Wir melden uns `[PLATZHALTER PH-03: Zeitraum, z. B. „innerhalb von zwei Werktagen"]`.
Fehler: Das hat nicht geklappt. Bitte versuchen Sie es noch einmal oder schreiben Sie an `[PLATZHALTER PH-04: E-Mail]`.

> Quelle: Einwilligungstext ist Standard-Formulierung, rechtliche Prüfung mit PH-12. Reaktionszeit bewusst Platzhalter (§4: keine Reaktionszeiten erfinden).

### 6.4 So geht es weiter
**H2:** So geht es weiter

1. **Gespräch.** Sie schildern, wo es hakt; wir fragen nach und ordnen ein.
2. **Einschätzung.** Sie erhalten `[PLATZHALTER PH-03: was der Kunde bekommt, z. B. „eine kurze schriftliche Einschätzung"]` – womit ein Start Sinn ergibt, und womit nicht.
3. **Entscheidung.** Ob und wie es weitergeht, entscheiden Sie. Ohne Nachfassen im Wochentakt.

### 6.5 Kontakt
**H2:** Kontakt

`[PLATZHALTER PH-04: Anschrift · Telefon · E-Mail]`

### 6.6 Kurz gefragt
**H2:** Kurz gefragt

**Was sollte ich mitbringen?**
Nichts Aufwendiges. Ein Bild Ihrer heutigen Abläufe und Programme reicht – eine Liste der Werkzeuge, die im Einsatz sind, hilft.

**Für wen ist das Gespräch gedacht?**
Für Geschäftsführung, kaufmännische Leitung und IT-Leitung mittelständischer Unternehmen, die mehrere Systeme durch eines ersetzen wollen – ganz oder Schritt für Schritt.

---

## 7. Impressum `/impressum/` — Struktur, Inhalte Platzhalter

> Rechtsseite: Überschriften und Reihenfolge sind ein Strukturvorschlag; **jeder Inhalt ist PH-11 und wird von Willy (ggf. mit Rechtsberatung) geprüft**. Nichts hier ist Rechtsberatung. Hinweis: Der frühere Standardsatz zur EU-Streitschlichtungsplattform (OS-Plattform) entfällt — die Plattform wurde 2025 eingestellt.

**H1:** Impressum

- **Angaben gemäß § 5 DDG** — `[PLATZHALTER PH-11: Firmierung, Rechtsform, Anschrift]`
- **Vertreten durch** — `[PLATZHALTER PH-11: Geschäftsführer]`
- **Kontakt** — `[PLATZHALTER PH-11: Telefon, E-Mail]`
- **Registereintrag** — `[PLATZHALTER PH-11: Registergericht, Handelsregisternummer]`
- **Umsatzsteuer-Identifikationsnummer** — `[PLATZHALTER PH-11: USt-IdNr. gemäß § 27a UStG]`
- **Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV** — `[PLATZHALTER PH-11: Name, Anschrift]`
- **Verbraucherstreitbeilegung** — `[PLATZHALTER PH-11: Aussage zur Teilnahme nach § 36 VSBG — prüfen]`
- **Haftung für Inhalte und Links, Urheberrecht** — `[PLATZHALTER PH-11: Standardtexte, rechtlich geprüft]`

## 8. Datenschutzerklärung `/datenschutz/` — Struktur, Inhalte Platzhalter

> **Jeder Inhalt ist PH-12** und wird vor Go-live geprüft. Abschnitte zu Drittanbietern werden nur aktiviert, wenn das Werkzeug tatsächlich eingebettet ist (PH-05, PH-06, PH-16).

**H1:** Datenschutzerklärung

1. **Verantwortlicher** — `[PLATZHALTER PH-12]`
2. **Hosting** — `[PLATZHALTER PH-12: Review-Phase Vercel Inc. (USA) → Endhost]`
3. **Server-Logfiles** — `[PLATZHALTER PH-12]`
4. **Kontaktformular** — `[PLATZHALTER PH-12: Anbieter aus PH-06, Zweck, Rechtsgrundlage, Speicherdauer]`
5. **Terminbuchung** — `[PLATZHALTER PH-12: Anbieter aus PH-05]`
6. **Schriftarten** — Die Schriften dieser Website werden vom eigenen Server geladen; es wird keine Verbindung zu Google Fonts oder anderen Anbietern aufgebaut. `[PH-12: prüfen]`
7. **Webanalyse** — `[PLATZHALTER PH-16/PH-12: nur falls ein Tool freigegeben ist]`
8. **Ihre Rechte** — `[PLATZHALTER PH-12: Auskunft, Berichtigung, Löschung, Einschränkung, Datenübertragbarkeit, Widerspruch, Beschwerderecht]`
9. **Stand** — `[PLATZHALTER PH-12: Datum]`

> Quelle Punkt 6: technische Tatsache dieses Builds (self-hosted Mulish, design-tokens.md §2).

## 9. 404-Seite

**H1:** Diese Seite gibt es nicht.

Vielleicht hat sich die Adresse geändert – oder ein Tippfehler eingeschlichen.

Links: Zur Startseite · Leistungen · Kontakt

---

## 10. Wortzählung je Seite

Gezählt mit `tools/wordcount.py` (sichtbarer Text ohne Quellenvermerke; ein Platzhalter zählt 0 Wörter).

| Seite | Wörter | Platzhalter | Lesezeit (200 W/min) | Budget | Hero (≤ 50) |
|---|---|---|---|---|---|
| Startseite | 436 | 4 | 2.2 min | 480 ✓ | 39 ✓ |
| Leistungen | 600 | 0 | 3.0 min | 600 ✓ | 38 ✓ |
| Branchen | 356 | 0 | 1.8 min | 520 ✓ | 35 ✓ |
| Über uns | 306 | 4 | 1.5 min | 420 ✓ | 39 ✓ |
| Kontakt | 197 | 7 | 1.0 min | 240 ✓ | 23 ✓ |
