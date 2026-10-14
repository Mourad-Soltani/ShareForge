# Buyer Notes — ShareForge

## What you get
- Complete source code for ShareForge v1.0
- Browser-based social meta tag designer with live X/LinkedIn-style previews
- Python core library for generating tags programmatically
- Passing health tests (pytest)
- MIT License
- README with quick-start instructions

## How to run
1. Web UI: simply open `web/index.html` in Chrome, Firefox, or Safari. No install needed.
2. Python tests / library:
   ```bash
   pip install pytest
   python -m pytest tests/ -q
   ```
   Then import from `shareforge.generator`.

## Requirements
- Modern web browser (for the UI)
- Python 3.8+ and pytest (only if you want to run the library/tests)
- No external services, API keys, or accounts required
- All processing is local / client-side

## Support
Built by Mourad.Soltani. For commercial use, redistribution, or custom features, contact the author.
