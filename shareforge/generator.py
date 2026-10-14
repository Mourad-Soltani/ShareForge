"""
ShareForge core meta tag generator.
Built by Mourad.Soltani
"""

from typing import Dict, Optional


def generate_meta_tags(
    title: str,
    description: str,
    image_url: Optional[str] = None,
    site_name: Optional[str] = None,
    url: Optional[str] = None,
    card_type: str = "summary_large_image",
    og_type: str = "website",
) -> str:
    """Generate complete HTML meta tags for Open Graph, Twitter, and SEO."""
    tags = []

    # Standard SEO
    tags.append(f'<meta name="description" content="{_escape(description)}">')
    if site_name:
        tags.append(f'<meta name="author" content="{_escape(site_name)}">')

    # Open Graph
    tags.append(f'<meta property="og:title" content="{_escape(title)}">')
    tags.append(f'<meta property="og:description" content="{_escape(description)}">')
    tags.append(f'<meta property="og:type" content="{_escape(og_type)}">')
    if url:
        tags.append(f'<meta property="og:url" content="{_escape(url)}">')
    if image_url:
        tags.append(f'<meta property="og:image" content="{_escape(image_url)}">')
    if site_name:
        tags.append(f'<meta property="og:site_name" content="{_escape(site_name)}">')

    # Twitter / X Cards
    tags.append(f'<meta name="twitter:card" content="{_escape(card_type)}">')
    tags.append(f'<meta name="twitter:title" content="{_escape(title)}">')
    tags.append(f'<meta name="twitter:description" content="{_escape(description)}">')
    if image_url:
        tags.append(f'<meta name="twitter:image" content="{_escape(image_url)}">')
    if site_name:
        tags.append(f'<meta name="twitter:site" content="@{_escape(site_name)}">')

    return "\n".join(tags)


def _escape(text: str) -> str:
    """Basic HTML attribute escaping."""
    return (
        text.replace("&", "&amp;")
        .replace('"', "&quot;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def validate_inputs(title: str, description: str) -> Dict[str, str]:
    """Return warnings for common best-practice violations."""
    warnings = {}
    if len(title) > 60:
        warnings["title"] = "Title longer than 60 chars may be truncated."
    if len(description) > 160:
        warnings["description"] = "Description longer than 160 chars may be truncated."
    if len(title) < 10:
        warnings["title_short"] = "Title is very short."
    return warnings
