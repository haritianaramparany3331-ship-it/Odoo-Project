"""Count the visible words per page in docs/content.md.

Counts what a visitor would read: headings, running text, buttons, labels.
Excludes source notes (lines starting with ">"), production notes (lines in
parentheses), markup labels (H1:/H2:/Button:/Link: ...), anchors and the
placeholder tokens themselves (a placeholder counts as 1 placeholder, 0 words).

    py tools/wordcount.py            prints the table
    py tools/wordcount.py --write    also replaces section 10 of content.md
"""
import re
import sys
import pathlib

DOC = pathlib.Path(__file__).resolve().parent.parent / "docs" / "content.md"
PAGES = {
    "Startseite": ("## 2. Startseite", "## 3. Leistungen"),
    "Leistungen": ("## 3. Leistungen", "## 4. Branchen"),
    "Branchen": ("## 4. Branchen", "## 5. Über uns"),
    "Über uns": ("## 5. Über uns", "## 6. Kontakt"),
    "Kontakt": ("## 6. Kontakt", "## 7. Impressum"),
}
LIMITS = {"Startseite": 480, "Leistungen": 600, "Branchen": 520, "Über uns": 420, "Kontakt": 240}
WPM = 200

LABELS = re.compile(r"\*\*(H[1-6]:?|Unterzeile:|Buttons?:|Bild:|Passende Module:|Typischer Einstieg:)\*\*|^(Link|Links|Erfolg|Fehler|Fallback|Option[^:]*):", re.M)


def clean(text: str):
    lines = []
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith(">") or s.startswith("(") or s.startswith("_(") or s.startswith("#"):
            continue
        lines.append(line)
    text = "\n".join(lines)
    placeholders = len(re.findall(r"\[PLATZHALTER[^\]]*\]", text))
    text = re.sub(r"`?\[PLATZHALTER[^\]]*\]`?", " ", text)
    text = re.sub(r"`\[PH-\d+[^\]]*\]`|`#[\w-]+`", " ", text)
    text = re.sub(r"\[MARKENNAME\]", "Markenname", text)
    text = LABELS.sub(" ", text)
    text = re.sub(r"\*\*|`|^[-*\d.]+\s+|☐", " ", text, flags=re.M)
    words = re.findall(r"[\wÄÖÜäöüß][\wÄÖÜäöüß'’\-/&.]*", text)
    return len(words), placeholders


def hero(text: str):
    m = re.search(r"### \d\.1 Hero(.*?)(?=\n### )", text, re.S)
    return clean(m.group(1))[0] if m else 0


def main():
    src = DOC.read_text(encoding="utf-8")
    rows = []
    for page, (start, end) in PAGES.items():
        a, b = src.index(start), src.index(end)
        section = src[a:b]
        words, ph = clean(section)
        h = hero(section)
        rows.append((page, words, ph, h, LIMITS[page]))
    table = ["| Seite | Wörter | Platzhalter | Lesezeit (200 W/min) | Budget | Hero (≤ 50) |", "|---|---|---|---|---|---|"]
    for page, words, ph, h, limit in rows:
        ok = "✓" if words <= limit else "✗ über Budget"
        hok = "✓" if h <= 50 else "✗"
        table.append(f"| {page} | {words} | {ph} | {words / WPM:.1f} min | {limit} {ok} | {h} {hok} |")
    out = "\n".join(table)
    print(out)
    if "--write" in sys.argv:
        new = re.sub(r"(## 10\. Wortzählung je Seite\n\n)(.*)$", lambda m: m.group(1) + "Gezählt mit `tools/wordcount.py` (sichtbarer Text ohne Quellenvermerke; ein Platzhalter zählt 0 Wörter).\n\n" + out + "\n", src, flags=re.S)
        DOC.write_text(new, encoding="utf-8", newline="\n")
        print("\ncontent.md §10 aktualisiert")


if __name__ == "__main__":
    main()
