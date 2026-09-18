# Platzhalter-Register — alles, was noch echt werden muss

**Das ist die eine Liste.** Jeder Platzhalter auf der Website hat hier eine
Zeile mit einer festen Nummer (`PH-nn`). Dieselbe Nummer steht im Text und
später im HTML, z. B. `[PLATZHALTER PH-04: Adresse]`. Wer eine Nummer im Text
sieht, findet hier, was eingetragen werden muss und von wem.

**So findet man jedes Vorkommen:**
- Im Code: `grep -rn "PH-04" src/ docs/content.md`
- Nach jedem Build zählt `node build.js` alle offenen Platzhalter je Seite und
  gibt sie am Ende aus — bei **0** ist die Seite Go-live-fähig.
- `[MARKENNAME]` ist der einzige Platzhalter ohne Nummer (CLAUDE.md §1): ein
  Find-and-Replace über das ganze Repo, sobald der Name feststeht.

Status: ⬜ offen · 🟨 Antwort da, noch nicht eingebaut · ✅ eingebaut

Stand: 2026-09-19 (Phase 6 — alle Platzhalter stehen als Tokens im HTML; `node build.js` zählt 76 Platzhalter und 62× `[MARKENNAME]`)

---

## A. Platzhalter im Text und Code (müssen gefüllt werden)

| ID | Wo | Was eingetragen werden muss | Wer | Status |
|---|---|---|---|---|
| **PH-01** | überall (`[MARKENNAME]`) | Der Markenname des ERP-Geschäftsfelds. Ein Find-and-Replace. Zusätzlich prüfen: Titel-Längen (SEO), Wortmarke im Header, Footer, OG-Tags. | Willy | ⬜ |
| **PH-02** | `site.config.json` → `siteUrl`, `indexable` | Die Domain (`https://…`). Damit entstehen Canonical-URLs, `og:url`, `sitemap.xml`; `indexable: true` erst zum Go-live. | Willy | ⬜ |
| **PH-03** | Startseite CTA-Band · Kontakt Hero · Kontakt „So geht es weiter" (Schritt 2) | **Das Potenzialgespräch konkret:** Dauer (z. B. 30 oder 45 Minuten), Format (Video / Telefon / vor Ort), wer teilnimmt, was der Kunde danach bekommt (z. B. eine schriftliche Kurzeinschätzung — ja/nein?). Ohne das bleibt der wichtigste CTA vage. (= offene-fragen F2) | Willy | ⬜ |
| **PH-04** | Footer (alle Seiten) · Kontakt „Kontaktdaten" · Impressum | Firmenanschrift, Telefonnummer, E-Mail-Adresse **für dieses Geschäftsfeld** (eigene Adresse/Nummer oder die von KIBH?). | Willy | ⬜ |
| **PH-05** | Kontakt „Termin buchen" | Calendly-Einbettung: eigenes Event für ERP-Potenzialgespräche oder das von KIBH? Event-URL. Konto auf Firmen-Adresse. (= D3) | Willy | ⬜ |
| **PH-06** | Kontakt „Nachricht schreiben" | Formular-Backend: eigenes Formspree-Formular oder das von KIBH? Formular-ID, Empfänger-Adresse. Konto auf Firmen-Adresse. (= D4) | Willy | ⬜ |
| **PH-07** | Über uns „Team" | 2–4 Personen: Name, Rolle, Foto (1:1, siehe `bildbedarf.md`), optional ein Satz. Wer ist Ansprechpartner für ERP? | Willy | ⬜ |
| **PH-08** | Über uns „Referenzen" (3 Karten) | Je Referenz: Branche · Ausgangslage · Lösung · Ergebnis · Zitat mit Name und Funktion · Logo (Freigabe des Kunden!). **Nur echte ERP/Odoo-Referenzen** — gibt es welche? Falls KIBH-KI-Referenzen genutzt werden sollen: nur mit Kennzeichnung „KI-Projekt" und nur nach Freigabe. (= B2, B3) | Willy | ⬜ |
| **PH-09** | Startseite „Vertrauen" (Block 8) | Kundenlogos oder ein Zitat — **nur wenn echt vorhanden**. Sonst wird der Block gar nicht gebaut; die Seite funktioniert ohne ihn. | Willy | ⬜ |
| **PH-10** | Über uns „Zwei Geschäftsfelder" | Gründungs- bzw. Startjahr von KI Beratung Hessen („seit …"). | Willy | ⬜ |
| **PH-11** | Impressum (alle Felder) | Firmierung, Rechtsform, Anschrift, Vertretungsberechtigte (Geschäftsführer), Kontakt (Telefon, E-Mail), Registergericht + HRB-Nummer, USt-IdNr., inhaltlich Verantwortlicher (§ 18 Abs. 2 MStV), ggf. Berufsrecht. **Rechtliche Prüfung durch Willy vor Go-live.** | Willy | ⬜ |
| **PH-12** | Datenschutzerklärung (alle Abschnitte) | Verantwortlicher, Hosting-Anbieter (Vercel in der Review-Phase → Endhost), Server-Logs, Kontaktformular (Anbieter PH-06), Terminbuchung (Anbieter PH-05), Analyse-Tool (nur falls PH-16), Rechte der Betroffenen, ggf. Datenschutzbeauftragter. **Rechtliche Prüfung vor Go-live.** | Willy | ⬜ |
| **PH-13** | Startseite Hero (Bild) | Odoo-Screenshot (z. B. CRM-Pipeline oder Dashboard), Maße in `bildbedarf.md`. Quelle: eigener Screenshot einer Odoo-Demo oder Odoo-Pressematerial (Nutzungsrechte prüfen). Entschieden 2026-09-18: Claude hat den neutralen Rahmen gebaut, Hari tauscht das Bild später ein (`src/pages/index.html`, `.hero__frame`). | Hari | ⬜ |
| **PH-14** | Startseite „KI-Hebel" · Über uns „KI-Hebel" (Bild) | Ruhiges Motiv, keine Stock-Roboter. Maße in `bildbedarf.md`. | Hari | ⬜ |
| **PH-15** | Header, Footer, Favicon, `og:image` | Wortmarke/Logo (SVG + PNG), Favicon-Set, Open-Graph-Bild 1200×630. Maße in `bildbedarf.md`. | Willy / Designer | ⬜ |
| **PH-16** | `base.html` (Head) · Datenschutz | Analyse-Tool — **nur nach Freigabe**. Empfehlung liegt vor in `analytics-tracking.md` (Plausible, Umami Cloud oder self-hosted Matomo). Bis dahin: nichts eingebaut. (= D2) | Willy | ⬜ |

## B. Formulierungen, die eine Entscheidung brauchen (kein Token im Text, aber Text ändert sich)

| ID | Wo | Frage | Vorschlag im Text | Wer | Status |
|---|---|---|---|---|---|
| **PH-17** | Startseite Hero-Unterzeile, Über uns Hero, Meta-Descriptions | Regionale Aussage (= F3): Hessen? Rhein-Main? Deutschland? DACH? | „aus Hessen für den Mittelstand in Deutschland" | Willy | ⬜ |
| **PH-18** | Startseite „Warum Odoo", Punkt 5 | Die „20.000"-Zahl (= C2) | „über 20.000 Mitwirkende weltweit" (belegt: odoo.com/page/community) | Willy | ⬜ |
| **PH-19** | Footer | Link zur KIBH-Website (= F1) | Link setzen: „KI-Beratung: kiberatunghessen.com" | Willy | ⬜ |
| **PH-20** | Über uns „Unsere Haltung" | Die drei Prinzipien (Standard vor Sonderbau · ein Modul darf der Anfang sein · keine Abhängigkeit) sind ein Positionierungsvorschlag von Claude — trägt Willy das so? | wie in `content.md` | Willy | ⬜ |

## C. Gelöst

| ID | Datum | Lösung |
|---|---|---|
| _(noch nichts)_ | | |

---

## Regeln

1. Jeder neue Platzhalter bekommt hier **sofort** eine Zeile — nicht am Ende
   einer Phase.
2. Im Text immer dieselbe Form: `[PLATZHALTER PH-nn: Kurzbeschreibung]`.
3. Wird ein Platzhalter gefüllt: Status ✅, Zeile nach C verschieben, Datum.
4. Go-live-Check: `node build.js` meldet 0 Platzhalter **und** 0 `[MARKENNAME]`.
