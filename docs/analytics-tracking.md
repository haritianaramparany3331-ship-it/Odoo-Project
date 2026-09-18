# Analyse-Tool — Empfehlung zur Entscheidung (CLAUDE.md §10, Punkt 4 „Tracking & Analytics")

Stand: 2026-09-18. **Es ist nichts eingebaut.** Die Website lädt außer ihren
eigenen vier Dateien (HTML, CSS, JS, Schriften) keinen einzigen fremden
Request. Das bleibt so, bis Willy eines der Werkzeuge unten freigibt (PH-16).

## Warum die Frage nicht nur technisch ist

Jedes Werkzeug, das Besucher misst, muss in der Datenschutzerklärung stehen
(PH-12). Setzt es Cookies oder bildet es Profile, braucht die Seite außerdem
einen Einwilligungs-Banner — der auf einer Fünf-Seiten-B2B-Website mehr
Besucher kostet, als er Erkenntnis bringt. Deshalb die Vorauswahl:
**cookielos, DSGVO-tauglich, ohne Banner** (Aggregatdaten, keine
personenbezogenen Profile). Google Analytics steht aus genau diesem Grund nicht
auf der Liste (CLAUDE.md §10).

## Drei Optionen

| | **Plausible** (Cloud, EU) | **Umami** (self-hosted oder Cloud) | **Matomo** (self-hosted) |
|---|---|---|---|
| Was es ist | Gehostete, cookielose Web-Analyse aus der EU | Open-Source-Analyse, cookielos, sehr schlank | Der Open-Source-Klassiker; kann sehr viel, kann aber auch zu viel |
| Cookies / Banner | keine Cookies; nach Anbieter-Angabe ohne Banner nutzbar — **rechtliche Einschätzung durch Willy/Berater nötig** | keine Cookies; gleiche Einschätzung nötig | konfigurierbar cookielos (dann ohne Banner) — Standardkonfiguration setzt Cookies |
| Hosting / Daten | Anbieter-Server in der EU; Auftragsverarbeitungsvertrag verfügbar | eigener Server (Node + Datenbank) **oder** Umami Cloud | eigener Server (PHP + MySQL) |
| Kosten | Abo, nach Seitenaufrufen gestaffelt (aktueller Preis: plausible.io/#pricing — hier bewusst keine Zahl) | Self-hosted: nur Server; Cloud: Abo (umami.is/pricing) | Self-hosted: nur Server; Matomo Cloud: Abo |
| Aufwand für uns | ein `<script>`-Tag, fertig | Server aufsetzen und pflegen (oder Cloud wie Plausible) | Server aufsetzen und pflegen; Konfiguration anspruchsvoller |
| Was wir sehen | Besucher, Seiten, Quellen, Geräte, Zielerreichung (z. B. Klick auf „Potenzialgespräch") | dasselbe, etwas roher | alles — inklusive Dingen, die wir nicht brauchen |
| Passt zu | **einem kleinen Team ohne Server-Betrieb** | einem Team, das ohnehin Server betreibt (KIBH?) | Bedarf an Tiefe, Bereitschaft zur Pflege |

## Empfehlung

**Plausible** — oder Umami Cloud, falls die Kosten den Ausschlag geben. Beide
messen das, was diese Seite wissen muss (Woher kommen Besucher? Welche Seite
führt zum Kontakt? Wie viele klicken den CTA?), ohne Cookies, ohne Banner und
ohne Server, den jemand pflegen muss. Das Konto gehört auf eine Firmen-Adresse
(CLAUDE.md §16.12).

Self-hosted Matomo nur, wenn die Firma ohnehin einen gepflegten Server hat und
Daten grundsätzlich nicht bei Dritten liegen sollen — dann cookielos
konfigurieren.

## Was nach der Entscheidung passiert

1. Willy wählt (PH-16) und legt das Konto an.
2. Claude baut das Script in `src/partials/base.html` ein — ein Tag, nur im
   `indexable`-Build, nicht in der Review-Umgebung.
3. Abschnitt „7. Webanalyse" der Datenschutzerklärung wird mit dem gewählten
   Anbieter gefüllt (PH-12) und rechtlich geprüft.
4. Ein Ziel („Potenzialgespräch"-Klick, Formular abgeschickt) wird angelegt,
   damit die Frage der Aufgabenstellung — Conversions messen — beantwortet ist.

## Was wir *nicht* messen

Keine Session-Recordings, keine Heatmaps, kein Fingerprinting, keine
Verknüpfung mit Calendly-/Formular-Daten. Für eine Seite dieser Größe ist das
Rauschen, kein Signal — und rechtlich ein anderes Kapitel.
