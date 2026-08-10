#!/usr/bin/env python3
"""
build_insights.py — regenerates insights.html from data/letters.json.

Quarterly workflow:
  1. Add the new letter to data/letters.json (title, year, month, pdf URL).
  2. Run:  python scripts/build_insights.py
  3. Commit and push. Done.

The newest letter automatically becomes the featured letter; the archive
groups by year, newest first. Years with no letters simply don't appear.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "data" / "letters.json").read_text())
letters = sorted(data["letters"], key=lambda x: (x["year"], x["month"]), reverse=True)

featured, archive = letters[0], letters[1:]

def box(l):
    return (f'    <a class="insight-box reveal" href="{l["pdf"]}" target="_blank" rel="noopener">'
            f'<span>{l["title"]}</span><span class="when">{l["monthName"]} {l["year"]}</span></a>')

years_html = []
current_year = None
for l in archive:
    if l["year"] != current_year:
        if current_year is not None:
            years_html.append("  </div>")
        years_html.append(f'  <div class="year-block">\n    <div class="year reveal">{l["year"]}</div>')
        current_year = l["year"]
    years_html.append(box(l))
years_html.append("  </div>")
archive_html = "\n".join(years_html)

page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Insights | Martin Capital Partners</title>
<meta name="description" content="Martin Capital Partners' quarterly Point of View letters — {len(letters)} letters on dividends, durability, and risk, written continuously since 2010.">
<link rel="icon" type="image/png" href="assets/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Wix+Madefor+Display:wght@400;700&family=Wix+Madefor+Text:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<div class="page">

<header class="site">
  <a class="logo" href="index.html"><img src="assets/logo.png" alt="Martin Capital Partners logo"></a>
  <button class="menu-btn" aria-label="Toggle menu" aria-expanded="false" onclick="toggleMenu()"><span></span><span></span></button>
</header>

<nav class="menu-overlay" id="menuOverlay" aria-label="Site menu">
  <a href="index.html">Home</a>
  <a href="team.html">MCP Team</a>
  <a href="philosophy.html">Investment Philosophy</a>
  <a href="insights.html" onclick="closeMenu()">Insights</a>
  <a href="index.html#resources">Client Resources</a>
  <a href="index.html#contact">Contact</a>
</nav>

<h1 class="page-title">Insights</h1>

<div class="wrap-wide">
  <div class="featured-letter reveal">
    <div class="kicker">Latest &middot; Point of View</div>
    <h2>{featured["title"]}</h2>
    <div class="date">{featured["monthName"]} {featured["year"]}</div>
    <a class="btn" href="{featured["pdf"]}" target="_blank" rel="noopener">Read the Letter <span class="arrow"></span></a>
  </div>

{archive_html}
</div>

<footer class="site" id="contact" style="margin-top:60px">
  <div class="rule"></div>
  <div class="footer-inner">
    <h3>Contact Us</h3>
    <div class="addr">
      <p class="firm">Martin Capital Partners, LLC</p>
      <p>940 Willamette Street, Suite 350</p>
      <p>Eugene, Oregon 97401</p>
      <p><a href="mailto:info@martincp.com">info@martincp.com</a> &nbsp;|&nbsp; 541.636.4170</p>
    </div>
    <div class="legal">
      <a href="assets/docs/privacy-policy.pdf" target="_blank" rel="noopener">Privacy Policy</a>
      <a href="assets/docs/terms-and-conditions.pdf" target="_blank" rel="noopener">Terms &amp; Conditions</a>
      <a href="assets/docs/form-adv-ii.pdf" target="_blank" rel="noopener">Form ADV II</a>
      <a href="assets/docs/form-adv-iii-crs.pdf" target="_blank" rel="noopener">Form ADV III (CRS)</a>
    </div>
    <p class="copyright">&copy; 2026 Martin Capital Partners</p>
    <a class="linkedin" href="https://www.linkedin.com/company/martin-capital-partners-llc/about/" target="_blank" rel="noopener" aria-label="Martin Capital Partners on LinkedIn">
      <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.03-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.72v20.55C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.72C24 .77 23.2 0 22.22 0z"/></svg>
    </a>
  </div>
</footer>

</div>
<script src="js/main.js"></script>
</body>
</html>
"""

(ROOT / "insights.html").write_text(page)
print(f"insights.html generated: {len(letters)} letters, featured = {featured['title']} ({featured['monthName']} {featured['year']})")
