#!/usr/bin/env node
/**
 * [MARKENNAME] — static site build.
 *
 * Zero dependencies. Reads src/pages/*.html, injects shared partials from
 * src/partials/, writes plain static HTML to dist/. The output is an ordinary
 * folder of files: no runtime, no host-specific feature, no absolute paths —
 * it can be uploaded to any static host unchanged.
 *
 * Adapted from the KIBH build (../KIBH/build.js). Differences:
 *   - every asset and internal link is RELATIVE via {{root}} (KIBH used
 *     root-absolute paths plus Vercel's cleanUrls; CLAUDE.md §7 forbids that)
 *   - any partial can be included anywhere with {{> name}} so a block that
 *     appears on several pages (a CTA band, a card list) exists exactly once
 *   - site.config.json carries the domain and the indexable switch; canonical,
 *     og:url, sitemap.xml and robots.txt derive from it and are omitted while
 *     the domain is unknown, so nothing invented ends up in the markup
 *
 * Page files declare their metadata in a leading JSON front-matter block:
 *
 *   <!--{ "title": "...", "description": "...", "url": "/leistungen/" }-->
 *
 * Optional keys: "nav" (slug of the nav entry to mark active, defaults to the
 * file name), "bodyClass", "noindex" (true keeps the page out of the sitemap).
 *
 * Placeholders available in pages and partials:
 *   {{title}} {{description}} {{url}} {{root}} {{siteName}} {{v}}
 *   {{content}} (base only)  {{head_urls}} {{robots_meta}}  {{> partial}}
 */

const fs = require("fs");
const path = require("path");
const crypto = require("crypto");

const ROOT = __dirname;
const SRC = path.join(ROOT, "src");
const DIST = path.join(ROOT, "dist");
const CONFIG = JSON.parse(fs.readFileSync(path.join(ROOT, "site.config.json"), "utf8"));

const read = (p) => fs.readFileSync(p, "utf8");

/** dist path for a page, driven by its declared url. 404 stays flat: every
 *  host looks for it by that name. */
function outputPath(slug, url) {
  if (slug === "404") return "404.html";
  const clean = String(url || "/").replace(/^\/+|\/+$/g, "");
  return clean ? path.join(clean, "index.html") : "index.html";
}

/** Relative prefix from a page's folder back to the dist root ("./" or "../").
 *  The 404 page is served at any depth, so it alone gets a root-absolute "/". */
function rootPrefix(slug, out) {
  if (slug === "404") return "/";
  const depth = out.split(path.sep).length - 1;
  return depth ? "../".repeat(depth) : "./";
}

function loadPartials() {
  const dir = path.join(SRC, "partials");
  return Object.fromEntries(
    fs.readdirSync(dir)
      .filter((f) => f.endsWith(".html"))
      .map((f) => [path.basename(f, ".html"), read(path.join(dir, f))])
  );
}

function parseFrontMatter(raw) {
  const m = raw.match(/^\s*<!--(\{[\s\S]*?\})-->\s*/);
  if (!m) return [{}, raw];
  return [JSON.parse(m[1]), raw.slice(m[0].length)];
}

/** Mark the current page's nav entry: aria-current + class on the matching
 *  <a data-nav="slug">. Merges into an existing class attribute — a second
 *  class attribute would be ignored by the browser. */
function markActiveNav(html, slug) {
  return html.replace(new RegExp(`<a\\b[^>]*data-nav="${slug}"[^>]*>`, "g"), (tag) => {
    let out = tag;
    if (/\bclass="/.test(out)) {
      out = out.replace(/\bclass="([^"]*)"/, (m, c) => `class="${c} is-active"`);
    } else {
      out = out.replace(/^<a\b/, '<a class="is-active"');
    }
    return out.replace(/^<a\b/, '<a aria-current="page"');
  });
}

/** {{> name}} includes, resolved recursively so a partial may include another. */
function includePartials(html, partials, depth = 0) {
  if (depth > 10) throw new Error("partial include loop");
  return html.replace(/\{\{>\s*([\w-]+)\s*\}\}/g, (full, name) => {
    if (!(name in partials)) throw new Error(`unknown partial: ${name}`);
    return includePartials(partials[name], partials, depth + 1);
  });
}

function render(template, vars) {
  return template.replace(/\{\{(\w+)\}\}/g, (full, key) => (key in vars ? vars[key] : full));
}

function build() {
  const partials = loadPartials();
  const pagesDir = path.join(SRC, "pages");
  const pages = fs.readdirSync(pagesDir).filter((f) => f.endsWith(".html"));
  const siteUrl = String(CONFIG.siteUrl || "").replace(/\/+$/, "");
  const indexable = Boolean(CONFIG.indexable) && Boolean(siteUrl);

  fs.rmSync(DIST, { recursive: true, force: true });
  fs.mkdirSync(DIST, { recursive: true });
  fs.cpSync(path.join(ROOT, "assets"), path.join(DIST, "assets"), { recursive: true });

  // Cache-busting as a query string, not a renamed file: works on every host
  // without cache-header configuration, and the file names stay predictable.
  const v = crypto
    .createHash("sha1")
    .update(read(path.join(ROOT, "assets", "css", "main.css")))
    .update(read(path.join(ROOT, "assets", "js", "main.js")))
    .digest("hex")
    .slice(0, 8);

  const built = [];
  const sitemap = [];

  for (const file of pages) {
    const slug = path.basename(file, ".html");
    const [meta, body] = parseFrontMatter(read(path.join(pagesDir, file)));
    const url = meta.url || "/";
    const out = outputPath(slug, url);
    const root = rootPrefix(slug, out);

    // Absolute URLs only once the domain exists. Until then the tags are left
    // out entirely rather than pointing at a placeholder domain.
    const headUrls = siteUrl
      ? [
          `<link rel="canonical" href="${siteUrl}${url}">`,
          `<meta property="og:url" content="${siteUrl}${url}">`,
        ].join("\n")
      : "<!-- canonical + og:url: set siteUrl in site.config.json -->";
    const robotsMeta = indexable && !meta.noindex
      ? ""
      : '<meta name="robots" content="noindex, nofollow">';

    const vars = {
      title: meta.title || CONFIG.siteName,
      description: meta.description || "",
      url,
      root,
      siteName: CONFIG.siteName,
      bodyClass: meta.bodyClass || "",
      v,
      head_urls: headUrls,
      robots_meta: robotsMeta,
    };

    let html = includePartials(partials.base, partials);
    html = html.replace("{{content}}", () => includePartials(body, partials));
    html = markActiveNav(html, meta.nav || slug);
    html = render(html, vars);

    const dest = path.join(DIST, out);
    fs.mkdirSync(path.dirname(dest), { recursive: true });
    fs.writeFileSync(dest, html);
    built.push(out.replace(/\\/g, "/"));
    if (slug !== "404" && !meta.noindex) sitemap.push(url);
  }

  // robots.txt + sitemap.xml: disallow everything while the site is a review
  // build; the sitemap needs absolute URLs and therefore the real domain.
  const robots = indexable
    ? `User-agent: *\nAllow: /\n\nSitemap: ${siteUrl}/sitemap.xml\n`
    : "User-agent: *\nDisallow: /\n";
  fs.writeFileSync(path.join(DIST, "robots.txt"), robots);

  if (indexable) {
    const xml =
      '<?xml version="1.0" encoding="UTF-8"?>\n' +
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
      sitemap.sort().map((u) => `  <url><loc>${siteUrl}${u}</loc></url>`).join("\n") +
      "\n</urlset>\n";
    fs.writeFileSync(path.join(DIST, "sitemap.xml"), xml);
  }

  console.log(`Built ${built.length} pages (${indexable ? "indexable" : "noindex — review build"}):`);
  for (const b of built.sort()) console.log(`  dist/${b}`);
}

build();
