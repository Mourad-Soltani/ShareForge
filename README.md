# ShareForge
# Built by Mourad.Soltani

A lightweight, privacy-first micro-tool for designing and exporting perfect Open Graph, Twitter/X Card, and SEO meta tags with live social platform previews.

## Features
- Live preview cards for X (Twitter), LinkedIn, Facebook, and Slack-style
- Generate complete HTML meta tags (og:*, twitter:*, standard SEO)
- Custom title, description, image URL, site name, type
- Character counters and best-practice hints
- Copy-to-clipboard or download snippet
- Runs 100% client-side (web UI) + optional Python CLI for automation
- Zero dependencies for the web version

## Quick Start (Web)
Open `web/index.html` in any modern browser. No server required.

## Python CLI (optional)
```bash
python -m shareforge.cli --title "My Product" --description "..." --image "https://..."
```

## Health Tests
```bash
python -m pytest tests/ -q
```

Built by Mourad.Soltani
