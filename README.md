# Martin Capital Partners — Static Site

Faithful static rebuild of martincp.com. No build system, no dependencies —
plain HTML/CSS/JS that any host (GitHub Pages, Cloudflare Pages, S3) can serve.

## Structure

```
index.html          Home (hero, team/philosophy previews, insights, resources, contact)
team.html           MCP Team + bio popups (all four full bios included)
philosophy.html     Investment Philosophy
insights.html       GENERATED — do not edit by hand (see below)
css/style.css       Single shared stylesheet (theme extracted from the live Wix site)
js/main.js          Menu overlay + bio modals
assets/             All images (originals pulled from the live site, web-optimized)
data/letters.json   Source of truth for the Insights archive (56 letters)
scripts/build_insights.py   Regenerates insights.html from letters.json
```

## Quarterly letter workflow

1. Add the new letter to `data/letters.json`:
   ```json
   { "title": "New Letter Title", "year": 2026, "month": 10,
     "monthName": "October", "pdf": "https://.../letter.pdf" }
   ```
2. Run `python scripts/build_insights.py`
3. Commit and push. The newest letter automatically becomes the featured
   letter; the archive regroups by year.

All 56 letter PDFs live in `assets/letters/` with clean, stable filenames
(`2026-jul-the-comfort-of-crowds.pdf`). The four legal documents live in
`assets/docs/`. The site has zero dependency on Wix.

## Deploying to GitHub Pages

1. Create a **private** repo won't work for Pages on the free tier — use a
   public repo or GitHub Pro/Team (MCP has M365, but Pages needs GitHub).
2. Push this folder to the repo root.
3. Settings → Pages → Deploy from branch → `main` / root.
4. Custom domain: add `www.martincp.com`, create the CNAME record at the DNS
   host, enable Enforce HTTPS.

## Design tokens (extracted from live site)

- Fonts: **Wix Madefor Display** (headings), **Wix Madefor Text** (body) — via Google Fonts
- Colors: `#000000` base, `#0A415A` deep blue, `#FFFFFF` text
- Page background: black fading to deep blue toward footer
- Buttons: pill outline, 1px white border, long-arrow icon
- Body paragraphs: justified

## Update workflow (post-deploy)

Tweaks arrive as single files from Claude. Then:
```
git add <file>
git commit -m "message"
git push
```
Pages redeploys automatically (~60s).

## Pre-cutover checklist

- [ ] robots.txt currently blocks ALL crawlers (intentional — the Wix site is
      still canonical). At cutover, replace with an allow-all + sitemap.
- [ ] Legal PDFs: when SCS issues updated versions, replace files in
      assets/docs/ (filenames stay stable).
- [ ] Compliance: full site review by Reid (CCO) before DNS cutover.
- [ ] Redirect strategy for old Wix _files/ugd/... PDF URLs (decision pending).
- [ ] Add sitemap.xml at cutover.
