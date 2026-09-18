"""QA pass over the built site (Phase 6, CLAUDE.md §15/§16).

Crawls every page at five viewports and reports, per page:
  - HTTP status, console errors, failed requests
  - horizontal overflow (scrollWidth > clientWidth), with the widest elements
  - German compounds broken mid-word (a word without hyphen/slash whose
    client rects span two lines) — measured with the Range API
  - touch targets under 44px on phone widths (buttons, nav, chips, summary,
    form controls, key links)
  - exactly one <h1>, no skipped heading levels, unique <title> and meta
    description, lang="de", images without alt
  - every internal link and #anchor resolves
  - the navigation drawer opens/closes at phone width, Escape closes it
  - the 404 route returns 404 with the branded page
  - visible word count per page (placeholders excluded) and reading time

    py tests/qa.py [base_url]        default http://localhost:4180

Screenshots land in tests/screenshots/ (git-ignored). Exit code 1 on problems.
"""
import re
import sys
import pathlib
from urllib.parse import urljoin, urlparse, urldefrag

from playwright.sync_api import sync_playwright

BASE = (sys.argv[1] if len(sys.argv) > 1 else "http://localhost:4180").rstrip("/")
SHOTS = pathlib.Path(__file__).parent / "screenshots"
SHOTS.mkdir(exist_ok=True)

PAGES = ["/", "/leistungen/", "/branchen/", "/ueber-uns/", "/kontakt/", "/impressum/", "/datenschutz/"]
LIMITS = {"/": 480, "/leistungen/": 600, "/branchen/": 520, "/ueber-uns/": 420, "/kontakt/": 240}
VIEWPORTS = {"360": (360, 780), "414": (414, 896), "768": (768, 1024), "1024": (1024, 800), "1100": (1100, 800), "1440": (1440, 900)}
PHONE = {"360", "414"}

problems = []
titles, descriptions = {}, {}
link_cache = {}

JS_OVERFLOW = """() => {
  const vw = document.documentElement.clientWidth;
  const wide = [...document.querySelectorAll('body *')]
    .filter(el => { const r = el.getBoundingClientRect(); return r.width > 0 && (r.right > vw + 1 || r.left < -1); })
    .map(el => el.tagName.toLowerCase() + (el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\\s+/).join('.') : ''));
  return { sw: document.documentElement.scrollWidth, vw, wide: [...new Set(wide)].slice(0, 6) };
}"""

JS_MIDWORD = """() => {
  const out = [];
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
    acceptNode: n => {
      const p = n.parentElement;
      if (!p || !n.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
      if (p.closest('script, style, noscript, .ph, .ph-img, .nav:not(.is-open) , [hidden]')) return NodeFilter.FILTER_REJECT;
      const cs = getComputedStyle(p);
      if (cs.display === 'none' || cs.visibility === 'hidden') return NodeFilter.FILTER_REJECT;
      return NodeFilter.FILTER_ACCEPT;
    }
  });
  let node;
  while ((node = walker.nextNode())) {
    const text = node.nodeValue;
    const re = /[^\\s]+/g; let m;
    while ((m = re.exec(text))) {
      const word = m[0];
      // words with a hyphen or a soft hyphen (U+00AD) may break at that joint
      if (word.length < 6 || /[-\\/–—\\u00AD]/.test(word)) continue;
      const r = document.createRange();
      r.setStart(node, m.index); r.setEnd(node, m.index + word.length);
      const rects = [...r.getClientRects()].filter(x => x.width > 0);
      if (rects.length > 1) {
        const tops = [...new Set(rects.map(x => Math.round(x.top)))];
        if (tops.length > 1) out.push(word + ' <' + (node.parentElement.tagName.toLowerCase()) + '>');
      }
    }
  }
  return [...new Set(out)].slice(0, 10);
}"""

JS_TOUCH = """() => {
  const sel = '.btn, .nav__link, .jump__link, summary, input:not([type=checkbox]), textarea, button, .text-link, a.ledger__key';
  return [...document.querySelectorAll(sel)]
    .filter(el => { const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden'; })
    .filter(el => el.getBoundingClientRect().height < 44)
    .map(el => el.tagName.toLowerCase() + '.' + (el.className || '').toString().trim().split(/\\s+/)[0] + ' ' + Math.round(el.getBoundingClientRect().height) + 'px: ' + el.textContent.trim().slice(0, 30))
    .slice(0, 8);
}"""

JS_STRUCTURE = """() => {
  const hs = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].map(h => Number(h.tagName[1]));
  let skipped = [];
  for (let i = 1; i < hs.length; i++) if (hs[i] > hs[i-1] + 1) skipped.push(hs[i-1] + '->' + hs[i]);
  return {
    h1: document.querySelectorAll('h1').length,
    skipped,
    lang: document.documentElement.lang,
    title: document.title,
    description: (document.querySelector('meta[name=description]') || {}).content || '',
    robots: (document.querySelector('meta[name=robots]') || {}).content || '',
    imgsNoAlt: [...document.querySelectorAll('img')].filter(i => !i.hasAttribute('alt')).length,
    links: [...document.querySelectorAll('a[href]')].map(a => a.getAttribute('href')),
    words: (() => {
      const main = document.querySelector('main').cloneNode(true);
      main.querySelectorAll('.ph, .ph-img, .draft-notice').forEach(e => e.remove());
      return (main.innerText.match(/[\\wÄÖÜäöüß][\\wÄÖÜäöüß'’\\-\\/&.]*/g) || []).length;
    })()
  };
}"""


def check_link(page, url):
    if url in link_cache:
        return link_cache[url]
    try:
        status = page.request.get(url).status
    except Exception:
        status = 0
    link_cache[url] = status
    return status


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    for path in PAGES:
        for name, (w, h) in VIEWPORTS.items():
            ctx = browser.new_context(viewport={"width": w, "height": h}, reduced_motion="reduce")
            page = ctx.new_page()
            errors, failed = [], []
            page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
            page.on("pageerror", lambda e: errors.append(str(e)))
            page.on("requestfailed", lambda r: failed.append(r.url))
            resp = page.goto(BASE + path)
            page.wait_for_load_state("networkidle")
            tag = f"{path} @{name}"
            if resp.status != 200:
                problems.append(f"{tag}: status {resp.status}")
            if errors:
                problems.append(f"{tag}: console errors {errors[:3]}")
            if failed:
                problems.append(f"{tag}: failed requests {failed[:3]}")

            ov = page.evaluate(JS_OVERFLOW)
            if ov["sw"] > ov["vw"]:
                problems.append(f"{tag}: horizontal overflow {ov['sw']}>{ov['vw']} {ov['wide']}")
            mid = page.evaluate(JS_MIDWORD)
            if mid:
                problems.append(f"{tag}: mid-word breaks {mid}")
            if name in PHONE:
                small = page.evaluate(JS_TOUCH)
                if small:
                    problems.append(f"{tag}: touch targets < 44px {small}")

            if name == "1440":
                st = page.evaluate(JS_STRUCTURE)
                if st["h1"] != 1:
                    problems.append(f"{path}: {st['h1']} h1 elements")
                if st["skipped"]:
                    problems.append(f"{path}: skipped heading levels {st['skipped']}")
                if st["lang"] != "de":
                    problems.append(f"{path}: lang={st['lang']}")
                if not st["description"]:
                    problems.append(f"{path}: no meta description")
                if st["imgsNoAlt"]:
                    problems.append(f"{path}: {st['imgsNoAlt']} images without alt")
                if st["title"] in titles.values():
                    problems.append(f"{path}: duplicate title '{st['title']}'")
                if st["description"] in descriptions.values():
                    problems.append(f"{path}: duplicate description")
                titles[path], descriptions[path] = st["title"], st["description"]
                if path in ("/impressum/", "/datenschutz/") and "noindex" not in st["robots"]:
                    problems.append(f"{path}: legal page without noindex")
                if path in LIMITS:
                    minutes = st["words"] / 200
                    flag = "" if st["words"] <= LIMITS[path] else "  <-- over budget"
                    print(f"words {path:14s} {st['words']:4d}  ({minutes:.1f} min, budget {LIMITS[path]}){flag}")
                    if st["words"] > LIMITS[path]:
                        problems.append(f"{path}: {st['words']} words > budget {LIMITS[path]}")

                # links + anchors
                for href in st["links"]:
                    if href.startswith(("mailto:", "tel:", "http://", "https://")):
                        continue
                    target = urljoin(BASE + path, href)
                    url, frag = urldefrag(target)
                    if urlparse(url).netloc != urlparse(BASE).netloc:
                        continue
                    status = check_link(page, url)
                    if status != 200:
                        problems.append(f"{path}: link {href} -> {status}")
                    elif frag:
                        # anchor must exist on the target document
                        key = (url, frag)
                        if key not in link_cache:
                            html = page.request.get(url).text()
                            link_cache[key] = f'id="{frag}"' in html
                        if not link_cache[key]:
                            problems.append(f"{path}: anchor {href} not found")

            if name == "1440":
                # document hygiene: duplicate ids, dangling aria-labelledby,
                # header CTA present, the current page marked in the nav
                hyg = page.evaluate("""(path) => {
                  const ids = [...document.querySelectorAll('[id]')].map(e => e.id);
                  const dup = ids.filter((id, i) => ids.indexOf(id) !== i);
                  const dangling = [...document.querySelectorAll('[aria-labelledby]')]
                    .map(e => e.getAttribute('aria-labelledby')).filter(id => !document.getElementById(id));
                  const cta = !!document.querySelector('.site-header .btn--primary');
                  const active = document.querySelector('.nav__link.is-active[aria-current=page]');
                  const activeHref = active ? active.getAttribute('href') : null;
                  return { dup: [...new Set(dup)], dangling, cta, activeHref };
                }""", path)
                if hyg["dup"]:
                    problems.append(f"{path}: duplicate ids {hyg['dup']}")
                if hyg["dangling"]:
                    problems.append(f"{path}: aria-labelledby without target {hyg['dangling']}")
                if not hyg["cta"]:
                    problems.append(f"{path}: header CTA missing")
                if path not in ("/", "/impressum/", "/datenschutz/") and (not hyg["activeHref"] or path.strip("/") not in hyg["activeHref"]):
                    problems.append(f"{path}: current page not marked in nav (got {hyg['activeHref']})")

                # keyboard: skip link first, then a visible focus ring
                page.keyboard.press("Tab")
                first = page.evaluate("document.activeElement.className + '|' + (document.activeElement.getBoundingClientRect().left >= 0)")
                if not first.startswith("skip-link|true"):
                    problems.append(f"{path}: first Tab does not reach a visible skip link ({first})")
                page.keyboard.press("Tab")
                ring = page.evaluate("(() => { const cs = getComputedStyle(document.activeElement); return cs.outlineStyle + ' ' + cs.outlineWidth + ' ' + cs.outlineColor; })()")
                if "solid" not in ring or "3px" not in ring:
                    problems.append(f"{path}: no visible focus ring on second Tab stop ({ring})")

                # FAQ accordion opens and closes
                if page.locator(".faq details").count():
                    second = page.locator(".faq details").nth(1)
                    second.locator("summary").click()
                    if not second.evaluate("d => d.open"):
                        problems.append(f"{path}: FAQ item does not open")
                    second.locator("summary").click()
                    if second.evaluate("d => d.open"):
                        problems.append(f"{path}: FAQ item does not close")

                # contact form: submit shows the placeholder notice, nothing navigates
                if page.locator("form[data-placeholder]").count():
                    page.locator("form[data-placeholder] button[type=submit]").click()
                    page.wait_for_timeout(200)
                    shown = page.evaluate("(() => { const s = document.querySelector('.form__status'); return s && !s.hidden && s.textContent.includes('PH-06'); })()")
                    if not shown or page.url.rstrip('/') != (BASE + path).rstrip('/'):
                        problems.append(f"{path}: form submit did not show the placeholder notice in place")

            if name in ("360", "768", "1024", "1440"):
                page.screenshot(path=str(SHOTS / f"{(path.strip('/').replace('/', '-') or 'home')}-{name}.png"), full_page=True)

            # drawer behaviour on phones
            if name == "360" and path == "/":
                page.click(".nav-toggle")
                page.wait_for_timeout(300)
                opened = page.evaluate("document.querySelector('.nav').classList.contains('is-open') && document.querySelector('.nav-toggle').getAttribute('aria-expanded') === 'true'")
                if not opened:
                    problems.append("drawer does not open at 360")
                else:
                    small = page.evaluate(JS_TOUCH)
                    if small:
                        problems.append(f"drawer touch targets < 44px {small}")
                    page.screenshot(path=str(SHOTS / "home-360-drawer.png"))
                page.keyboard.press("Escape")
                page.wait_for_timeout(300)
                if page.evaluate("document.querySelector('.nav').classList.contains('is-open')"):
                    problems.append("drawer does not close on Escape")
            ctx.close()

    # 404 route
    ctx = browser.new_context(viewport={"width": 1440, "height": 900})
    page = ctx.new_page()
    resp = page.goto(BASE + "/diese-seite-gibt-es-nicht/")
    if resp.status != 404:
        problems.append(f"404 route returned {resp.status}")
    if page.locator("h1").count() != 1:
        problems.append("404 page has no single h1")
    ctx.close()
    browser.close()

print()
if problems:
    print(f"PROBLEMS ({len(problems)}):")
    for pr in problems:
        print("  -", pr)
    sys.exit(1)
print(f"OK — {len(PAGES)} pages × {len(VIEWPORTS)} viewports, {len([k for k in link_cache if isinstance(k, str)])} links, no problems.")
