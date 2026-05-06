# Martin Capital Partners — Static Site

A static HTML replica of [martincp.com](https://www.martincp.com), built to be hosted from a GitHub repository (e.g. via GitHub Pages or any other static host).

## Structure

```
martincp-site/
├── index.html          # Home
├── team.html           # MCP Team
├── philosophy.html     # Investment Philosophy
├── insights.html       # Quarterly letter archive (2010–2026)
├── README.md
└── assets/
    ├── styles.css      # Brand styles (green #569542, blue #07415A, gold #C9A84C)
    └── logo.png        # ← drop the M Vector logo here
```

## Setup

1. **Add the logo.** Copy `M__Vector_.png` into `assets/` and rename it `logo.png` — that's the only missing asset. Every page references `assets/logo.png`.
2. **Push to GitHub.** Create a new repo and push these files at the root.
3. **Enable GitHub Pages.** In repo Settings → Pages → set Source to `main` branch, root folder. The site will serve from `https://<username>.github.io/<repo>/` within a minute or two.

## What's included vs. live site

**Faithful to live site:**
- Same four primary pages and navigation structure
- Identical homepage tagline ("Dividend Cultures | Mitigated Risk")
- Full team member list and bio openings
- All four philosophical tenets, verbatim
- Full Insights archive — every quarterly letter from October 2010 through April 2026, grouped by year
- Brand colors throughout (green section markers, blue header in footer, gold accents)
- Contact info, address, phone, email
- LinkedIn link in footer

**Intentionally left as dead links (`href="#"`) per your instructions:**
- All Insights PDF links — you'd need to either upload the PDFs to the repo or point them back to the Wix-hosted PDFs at `martincp.com/_files/...`
- Privacy Policy / Terms / Form ADV II / Form ADV III (CRS) — same as above
- Client Portal (Tamarac) and Charles Schwab links

**Differences from live:**
- Team photos rendered as initial placeholders (CKM, RCW, RSA, AP) since I don't have the headshots locally. Drop real JPGs into `assets/` and swap the `<div class="team-photo">XXX</div>` blocks for `<img>` tags.
- Removed Wix branding/scripts — pure HTML/CSS, ~30KB total payload, no JS dependencies (except a tiny mobile menu toggle).

## Quick local preview

Just open `index.html` in a browser, or run a local server:

```bash
cd martincp-site
python3 -m http.server 8000
# visit http://localhost:8000
```

## To wire up the dead links

If you want the Insights PDFs to keep working without re-hosting:

```html
<!-- Just point hrefs back to your existing Wix-hosted PDFs -->
<a href="https://www.martincp.com/_files/ugd/9adee3_00e5b176902943f2b41a0fac0062ab59.pdf">
  <span class="insight-title">Durability vs. Prediction</span>
  <span class="insight-date">April 2026</span>
</a>
```

Search/replace `href="#"` across `insights.html` and `index.html` to swap in real URLs. The PDF URLs are all in the Wix scrape and follow the pattern `https://www.martincp.com/_files/ugd/9adee3_<hash>.pdf`.
