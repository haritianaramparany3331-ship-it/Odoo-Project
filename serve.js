#!/usr/bin/env node
/**
 * Minimal local server for dist/. Zero dependencies. Serves folder index
 * files and the custom 404 the way an ordinary static host does, so QA runs
 * against the same behaviour the final host will show.
 *
 *   node serve.js [port]      (default 4180)
 */

const http = require("http");
const fs = require("fs");
const path = require("path");

const DIST = path.join(__dirname, "dist");
const PORT = Number(process.argv[2]) || 4180;

const TYPES = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".xml": "application/xml; charset=utf-8",
  ".txt": "text/plain; charset=utf-8",
  ".svg": "image/svg+xml",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".webp": "image/webp",
  ".ico": "image/x-icon",
  ".woff2": "font/woff2",
};

function resolve(urlPath) {
  const clean = decodeURIComponent(urlPath.split("?")[0]);
  const candidates = [
    path.join(DIST, clean),
    path.join(DIST, clean, "index.html"),
    path.join(DIST, clean + ".html"),
  ];
  for (const c of candidates) {
    if (c.startsWith(DIST) && fs.existsSync(c) && fs.statSync(c).isFile()) return c;
  }
  return null;
}

http
  .createServer((req, res) => {
    const file = resolve(req.url);
    if (!file) {
      const notFound = path.join(DIST, "404.html");
      res.writeHead(404, { "Content-Type": TYPES[".html"] });
      res.end(fs.existsSync(notFound) ? fs.readFileSync(notFound) : "404");
      return;
    }
    res.writeHead(200, { "Content-Type": TYPES[path.extname(file)] || "application/octet-stream" });
    res.end(fs.readFileSync(file));
  })
  .listen(PORT, () => {
    console.log(`dev server → http://localhost:${PORT}`);
  });
