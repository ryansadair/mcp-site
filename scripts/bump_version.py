#!/usr/bin/env python3
"""
bump_version.py — stamps a fresh cache-busting token onto every css/js
reference so browsers fetch new versions immediately after a deploy.

Run whenever style.css or main.js changes:
    python scripts/bump_version.py
Then commit the HTML files it touched along with your CSS/JS changes.
"""
import re
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKEN = time.strftime("%Y%m%d%H%M")

FILES = ["index.html", "team.html", "philosophy.html", "insights.html",
         "scripts/build_insights.py"]

for name in FILES:
    p = ROOT / name
    s = p.read_text()
    s = re.sub(r'css/style\.css(\?v=[\w]*)?', f'css/style.css?v={TOKEN}', s)
    s = re.sub(r'js/main\.js(\?v=[\w]*)?', f'js/main.js?v={TOKEN}', s)
    p.write_text(s)
    print(f"stamped {name}")

print(f"cache-bust version: {TOKEN}")
