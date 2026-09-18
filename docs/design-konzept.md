# Design-Konzept (Punkt 4, Teil 1)

Stand: 2026-09-18 (Phase 4, Vorschlag zur Freigabe). Baut auf
`design-tokens.md` (fixe Farben und Schriften von KIBH), `marktanalyse.md`
(was der Markt tut) und `informationsarchitektur.md` (was auf welcher Seite
steht). Kein Code — der folgt in Phase 5 nach Freigabe.

---

## 0. Ausgangspunkt: was fest ist, was frei ist

**Fest (CLAUDE.md §6, Willy):** KIBHs Farben und Schriften. Slate `#31363F`,
Text `#222831`, Hellgrau `#EEEEEE`, Teal `#76ABAE`; Mulish für Überschriften,
Verdana für Lauftext. Spacing-Scale, Radien und Schatten aus `design-tokens.md`.

**Frei:** Layout, Komposition, Hierarchie, Bildbehandlung, Bewegung,
Strukturmittel.

**Worum es geht:** Ein ERP ist das geordnete Hauptbuch eines Unternehmens —
Tabellen, Zeilen, Spalten, Datensätze, Bestände, Salden. Der Kern unserer
Botschaft (Startseite-H1) ist *Ordnung statt Streuung*: „Ein System statt fünf
Programmen und zehn Excel-Listen." Aus dieser Welt — dem Kontoblatt, der
Warenwirtschaft, dem Lieferschein — kommt die Gestaltung. Nicht aus der Welt
„moderne IT-Agentur".

---

## 1. Farbe — sechs Token, sechs Rollen

| Token | Hex | Rolle auf dieser Seite |
|---|---|---|
| `--c-white` | `#FFFFFF` | Seitengrund. Die Regel, nicht die Ausnahme. |
| `--c-text` | `#222831` | Lauftext. Das echte KIBH-Schwarz. |
| `--c-primary` | `#31363F` | Überschriften — und **genau zwei dunkle Bänder je Seite maximal** („Warum Odoo" auf der Startseite, „KI-Hebel" auf Über uns). Header und Footer. |
| `--c-secondary` | `#EEEEEE` | Text auf dunklen Bändern. |
| `--c-accent` `#76ABAE` / `--c-accent-dark` `#5F9295` | Teal | **Knapp gehalten:** Primär-Button, Textlinks (dark, 3,5:1), und eine einzige Linie je Abschnitt — die 2-px-Regel unter dem Abschnittstitel. Sonst nichts Teal. Kein Teal-Verlauf, keine Teal-Flächen. |
| `--c-surface` `#F8FAF9` / `--c-surface-alt` `#EDF0EF` | Off-White / Neutral | Ruhige Wechselflächen für Abschnitte und das CTA-Band (hell, nicht dunkel — siehe Kritik). |

Hairlines: `--c-border #E2E6E5`. Schatten nur, wo etwas wirklich *liegt*: der
Hero-Rahmen und die zwei Kartentypen (§3). Sonst keine.

## 2. Schrift — zwei Familien, klare Arbeitsteilung

| Rolle | Schrift | Größe / Gewicht | Bemerkung |
|---|---|---|---|
| Hero-H1 (nur Startseite) | Mulish 600 | `--fs-hero` 52–64, Zeilenhöhe 1.1, `text-wrap: balance` | Neun Wörter, zwei Zeilen. Das längste Wort „Excel-Listen" bricht am Bindestrich; auf 360 px misst die Clamp-Formel den Schnitt. |
| Seiten-H1 (innen) | Mulish 600 | `--fs-h1` 48 / 44 / 38 | |
| Abschnittstitel H2 | Mulish 600 | `--fs-h2` 38 / 32 | linksbündig auf der Containerkante, darunter die 2-px-Teal-Regel |
| „Zeilenschlüssel" (Modulname, Leistungsname, Schrittnummer, Branche) | Mulish 600 | `--fs-h4` 24 | die linke Spalte der Kontoblatt-Zeile (§3) |
| Lauftext | Verdana 400 | 16 / 1.6, Zeilenmaß **46 rem** | Verdana läuft breit — 46 rem sind ≈ 65–70 Zeichen. Die Breite ist ein Geschenk der Vorgabe: Verdana sieht nach nichts aus, was gerade überall steht. |
| Intro unter H2, Hero-Unterzeile | Verdana 400 | `--fs-body-lg` 18, `--c-text-muted` | |
| Buttons, Nav | Mulish 600 / 700 | 15 | wie KIBH |

Keine Eyebrows, keine Versalien-Labels, keine Monospace-Ziffern, kein
hervorgehobenes Einzelwort in Überschriften (CLAUDE.md §6).

## 3. Layout — die Kontoblatt-Zeile als Strukturprinzip

**Konzept in einem Satz:** Die Seite verhält sich wie ein gut geführtes
Kontoblatt — eine linke Achse, gelinierte Zeilen, Schlüssel links, Eintrag
rechts — und zeigt damit in ihrer eigenen Form, was das Produkt verspricht:
Ordnung.

**Ausrichtung:** alles linksbündig an einer Achse (Containerkante, 1140 px).
Nichts zentriert — außer dem 404-Text. Deutsche Komposita in zentrierten,
flatternden Zeilen sehen zerrissen aus; eine Achse führt das Auge.

### 3.1 Die Zeile

Jeder Inhaltsblock, der eine Liste von *Datensätzen* ist (Module, Leistungen,
Branchen-Module, die fünf Odoo-Gründe, die Vorgehensschritte), wird als
**gelinierte Zeilen** gesetzt — nicht als Karten:

```
──────────────────────────────────────────────────────────────────────  (hairline)
CRM & Vertrieb            Vom ersten Kontakt bis zum Auftrag: jeder Lead
(Mulish 600, 24)          sichtbar, jeder Schritt nachvollziehbar.   (Verdana 16)
──────────────────────────────────────────────────────────────────────
Finanzen & Buchhaltung    Rechnungen, Zahlungen, offene Posten: …
──────────────────────────────────────────────────────────────────────
```

Spalten: Schlüssel `minmax(14rem, 1fr)` | Eintrag `3fr`; Zeilenabstand
`--sp-5` innen, `--sp-7` zwischen Blöcken. Die Hairline ist Information (hier
endet ein Datensatz), keine Dekoration. Auf Phones stapelt die Zeile:
Schlüssel über Eintrag, Hairline bleibt.

### 3.2 Der Abschnittskopf

```
Warum Odoo?                                     ← H2, Mulish 600, 38
━━━━                                            ← 2 px Teal, 4 rem breit — die einzige Farbe im Kopf
Fünf Gründe, die für den Mittelstand zählen:    ← Verdana 18, muted, max 46 rem
```

Abstand Kopf → Inhalt `--sp-7` (48) wie in `design-tokens.md` §3.

### 3.3 Sequenzen (Vorgehen, „So geht es weiter")

Hier — und nur hier — gibt es Nummern, weil es Reihenfolgen sind: die Nummer
ist der Zeilenschlüssel (Mulish 600, 24, `--c-accent-dark`), rechts der Text.
Vertikale Linie links entlang der Nummern (`--c-border`), damit die Sequenz als
ein Weg lesbar ist.

### 3.4 Wo es Karten gibt — und nur dort

Karten (Radius 12, `--shadow-sm`, 1 px Rand) tragen eine **Wahl** oder ein
**Objekt**: die zwei Wege auf Leistungen (ganzes ERP | ein Modul zuerst) und
die drei Referenz-Platzhalter. Sonst nirgends. Buttons Radius 6, der Hero-Rahmen
Radius 20 — die Radienhierarchie bedeutet etwas.

### 3.5 Bänder

Je Seite höchstens zwei dunkle Bänder (`--c-primary`): Startseite „Warum Odoo";
Über uns „KI-Hebel". Wechselflächen `--c-surface` für jeden zweiten Abschnitt.
Das CTA-Band ist **hell** (`--c-surface-alt`) mit der Teal-Regel oben — der
Button ist dort das einzige Teal und deshalb unübersehbar.

### 3.6 Seitenskizzen (Desktop)

```
STARTSEITE
┌─ Header 92 ───────────────────────────────────────────────────────────────┐
│ [MARKENNAME]      Leistungen  Branchen  Über uns  Kontakt   [Potenzialgespräch vereinbaren] │
├────────────────────────────────────────────────────────────────────────────┤
│  Ein System statt fünf               ┌──────────────────────────────┐      │
│  Programmen und zehn                 │  ▒▒ ▒▒  (Odoo-Screenshot,     │      │
│  Excel-Listen.                       │  ▒▒▒▒▒   Rahmen r20, shadow) │      │
│  Unterzeile (Verdana 18, muted)      │  ▒▒ ▒▒▒▒                     │      │
│  [Kostenloses ERP-Potenzialgespräch  └──────────────────────────────┘      │
│   vereinbaren]   Leistungen ansehen        ⌐ Ghost-Tiles (CSS), die beim   │
│                                               Laden in den Rahmen ziehen  │
├─ surface ──────────────────────────────────────────────────────────────────┤
│  Kennen Sie das?                                                           │
│  ━━━━                                                                      │
│  ───────────────────────────────────────────────────────────────────────   │
│  Vertrieb, Lager und Buchhaltung arbeiten in verschiedenen Programmen …    │
│  ───────────────────────────────────────────────────────────────────────   │
│  Dieselbe Bestellung wird dreimal erfasst …                                │
│  ───────────────────────────────────────────────────────────────────────   │
│  Wie läuft der Monat? …                                                    │
│  Das ist kein Fleißproblem … Es ist ein Systemproblem – und lösbar.        │
├─ white ────────────────────────────────────────────────────────────────────┤
│  Alles in einem System                 (6 gelinierte Zeilen, Schlüssel|Eintrag) │
├─ primary (dunkel) ─────────────────────────────────────────────────────────┤
│  Warum Odoo?                           (5 gelinierte Zeilen, Hairline in   │
│                                         rgba(238,238,238,.18))            │
├─ white ────────────────────────────────────────────────────────────────────┤
│  So gehen wir vor                      1 │ Potenzialgespräch …            │
│                                        2 │ Analyse und Konzept …           │
│                                        … (vertikale Linie links)          │
├─ surface ──────────────────────────────────────────────────────────────────┤
│  Der KI-Hebel        Text (46 rem)     │ Bild PH-14 (4:3, r12)            │
├─ white ────────────────────────────────────────────────────────────────────┤
│  Odoo in Ihrer Branche   Bau & Handwerk / Produktion … (4 Textlinks als Zeilen) │
├─ surface-alt, Teal-Regel oben ─────────────────────────────────────────────┤
│  Wo steht Ihr Unternehmen – …         [Kostenloses ERP-Potenzialgespräch …]│
│  Text (PH-03)                          oder schreiben Sie uns              │
├─ Footer primary ───────────────────────────────────────────────────────────┤
```

Innenseiten: gleicher Aufbau ohne die Hero-Komposition — H1 + Unterzeile
linksbündig, max 46 rem, darunter direkt der erste Abschnitt. Der Hero einer
Innenseite ist Typografie, kein Bild.

### 3.7 Mobil (≤ 767) — gestaltet, nicht geschrumpft

- Hero: H1 → Unterzeile → Button (volle Breite) → Sekundärlink → **dann** der
  Rahmen mit dem Screenshot (Ghost-Tiles statisch, bereits „eingezogen"). Der
  Button bleibt im ersten Viewport.
- Kontoblatt-Zeile stapelt: Schlüssel (24 → 20 px) über Eintrag; Hairline
  bleibt; Zeileninnenabstand `--sp-4`.
- Sequenzen: Nummer und Text in einer Zeile (Nummer 2 rem breit), Linie links.
- Branchen: Sprungleiste wird zu vier Chips (Radius 6, `--c-accent-soft`),
  horizontal scrollbar; Blöcke einspaltig.
- Header 76 px, Drawer von rechts, Einträge 56 px hoch (Touch), Button unten.
- Zwei-Wege-Karten und Referenzkarten untereinander.

## 4. Bilder — drei, mit Absicht

| Bild | Behandlung | Warum |
|---|---|---|
| PH-13 Hero: Odoo-Screenshot | **Als Dokument, nicht als Gerät:** kein Laptop-Mockup (manaTec), kein Browser-Chrome. Rahmen Radius 20, 1 px `--c-border`, `--shadow-md`, Seitenverhältnis 16:10, deutsche Odoo-Oberfläche mit Demo-Daten (kein Kundenbezug). | Zeigt die Software (Phase 1: die Ausnahme im Markt) und behandelt sie wie das, was sie ist — das Arbeitsdokument des Kunden. |
| PH-14 KI-Hebel (Startseite, Über uns) | 4:3, Radius 12, ohne Schatten. Bevorzugt ein zweiter Odoo-Screenshot (Eingangsrechnung mit angehängtem Beleg), sonst ein eigenes Foto: Papierbeleg neben Bildschirm. **Keine Stock-Roboter, keine leuchtenden Gehirne.** | Bleibt bei „zeigen statt behaupten". |
| PH-07 Team | 1:1, Radius 12, 160 px Desktop / 96 px mobil, eigene Fotos, gleicher Hintergrund. | Menschen dort, wo sie hingehören: auf Über uns, klein, echt. |

Keine Icon-Sets. Die Modulnamen brauchen kein Piktogramm.

## 5. Bewegung — ein Moment

1. **Der Moment (nur Startseite, einmal beim Laden, ≤ 900 ms):** vier
   Ghost-Tiles — abstrakte Mini-Fenster in `--c-surface-alt` mit 1-px-Rand und
   angedeuteten Zeilen (keine lesbaren Daten) — stehen verstreut um den
   Hero-Rahmen und ziehen mit einem Ease-out in ihn hinein, während der
   Screenshot sich setzt. Danach: Stille. `prefers-reduced-motion`: die
   Endposition sofort. Das ist die H1 als Bild — Streuung wird ein System.
2. Nutzeraktionen: Akkordeon (FAQ) öffnet mit Höhe-Transition; Drawer gleitet
   ein; Buttons heben 1 px (nur bei `hover: hover`, wie KIBH).
3. Sonst nichts. Kein Scroll-Reveal, kein Zähler, kein Parallax.

## 6. Prinzipien — was diese Seite zu dieser Seite macht

1. **Ordnung als Bild.** Die Seite ist selbst das Kontoblatt: eine Achse,
   gelinierte Zeilen, Schlüssel und Eintrag. Das Produktversprechen ist die Form.
2. **Zeigen statt behaupten.** Die Software im Hero; keine Zähler, keine
   Badges, keine Stock-Menschen, keine Logo-Wand ohne Logos.
3. **Eine Achse.** Alles linksbündig. Das Auge sucht nie.
4. **Text trägt.** Mulish und Verdana leisten die Arbeit; kein Icon-Set, keine
   Illustration außer der Hero-Komposition.
5. **Ein Moment.** Eine Bewegung, die etwas bedeutet — dann Ruhe.

## 7. Das eine mutige Element

**Der Hero der Startseite: die Konvergenz.** Die Ghost-Tiles, die in den
Odoo-Rahmen ziehen. Alles andere — Zeilen, Bänder, Sequenzen, Karten, Footer —
bleibt bewusst still, damit dieser eine Moment trägt. Auf Innenseiten gibt es
ihn nicht; dort ist die Typografie das Ereignis.

---

## 8. Selbstkritik: was der generische Entwurf getan hätte

Zur Kontrolle habe ich den Entwurf gebaut, den ein Briefing „moderne Website
für eine B2B-IT-Beratung" ohne weitere Angaben bekommen hätte, und Punkt für
Punkt verglichen (CLAUDE.md §6, Skill-Checkliste).

| Generischer Entwurf | Mein erster Plan | Nach der Kritik |
|---|---|---|
| Hero: Headline links, Laptop-/Dashboard-Mockup rechts, zwei Buttons, Logo-Leiste darunter | Zweispaltig, **Laptop-Mockup** erwogen | Zweispaltig bleibt — Text und Bild müssen zusammen gesehen werden („ein System" + das System), und die Zeit ist (Phase 1) die Konvention, die der Besucher versteht. **Geändert:** kein Gerät, sondern der Screenshot als Dokument im Rahmen; die Konvergenz-Komposition statt statischem Mockup; keine Logo-Leiste (wir haben keine, und leere Slots sind schlimmer als keine). |
| Abschnitte: zentrierte H2 + Subline + drei Karten mit Icons | **Sechs Modul-Karten mit Icons** war der erste Reflex | **Geändert:** gelinierte Zeilen ohne Icons; linksbündig; Hairlines als Information. |
| „Warum wir"-Band mit vier Zählern | keine Zähler (verboten, §4) | Die fünf-Schritte-Sequenz ersetzt die Zahlen durch Transparenz. |
| Testimonial-Karussell | Platzhalter-Block | Block wird ohne echte Inhalte **nicht gebaut**. |
| Dunkles CTA-Band mit Verlauf | **dunkles CTA-Band** (KIBH-Muster) | **Geändert:** helles Band (`--c-surface-alt`) mit Teal-Regel oben; die dunklen Bänder gehören dem Inhalt („Warum Odoo", „KI-Hebel"), nicht dem Verkaufen. Der Button ist im hellen Band das einzige Teal. |
| Scroll-Reveal auf jedem Abschnitt | **Scroll-Reveal für die Zeilen** erwogen | **Gestrichen.** Ein Moment im Hero, sonst nichts. |
| Eyebrow-Labels, Middle-Dots, `→` an Links, Nummern 01/02/03 überall | nicht geplant | Nummern nur bei echten Sequenzen; Branchen-Links als Liste, nicht als Punktkette. |
| Einheitsradius 12 auf allem, grauer Schatten unter allem | Radien aus den Tokens | Hierarchie: 6 Buttons · 12 Karten · 20 Hero-Rahmen; Schatten nur unter Rahmen und Karten, getönt mit `--c-text`. |
| Icon-Set (Lucide o. ä.) für Module und Leistungen | Icons erwogen | **Gestrichen.** Namen genügen; Icons hätten die Zeilen zu Karten gemacht. |
| Broadsheet-Look (Hairlines überall, Radius 0, dichte Spalten) — ein anderer generischer Default, dem die Kontoblatt-Idee nahekommt | — | Bewusst abgegrenzt: Hairlines nur zwischen Datensätzen, nicht als Rahmen um alles; großzügige Zeilen (`--sp-5`), nicht Zeitungsdichte; KIBH-Radien bleiben. Das Kontoblatt ist luftig, die Zeitung ist eng. |

**Was gleich blieb — und warum:** der zweispaltige Hero (Konvention mit
Zweck), der vierspaltige Footer (Inhalt bestimmt die Spalten), das
FAQ-Akkordeon (Nutzeraktion, spart Lesezeit).

**Chanel-Test** (ein Accessoire ablegen): Die Ghost-Tiles hatten in der ersten
Fassung angedeutete Icons (Mail, Tabelle, Notiz). Weg damit — abstrakte
Rechtecke mit Zeilen reichen, und sie bleiben in der Palette.

---

## 9. Offen für Hari vor Phase 5

1. Freigabe des Konzepts — insbesondere **Kontoblatt-Zeilen statt Karten** und
   das **helle CTA-Band**.
2. Die **Konvergenz-Animation** als das eine mutige Element: ja, oder lieber
   die statische Komposition (Tiles bereits eingezogen)?
3. PH-13: ein eigener Odoo-Screenshot (Demo-Daten) — Hari macht ihn, oder
   Claude baut in Phase 5 einen neutralen Platzhalter-Rahmen und Hari ersetzt
   ihn? (Odoos Marken-Richtlinien für Screenshots vor Go-live prüfen:
   odoo.com/page/brand-assets.)
