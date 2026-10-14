"""
ShareForge health tests.
Built by Mourad.Soltani
"""

import pytest
from shareforge.generator import generate_meta_tags, validate_inputs

def test_basic_generation():
    html = generate_meta_tags(
        title="ShareForge Demo",
        description="Perfect social previews in seconds.",
        image_url="https://example.com/og.png",
        site_name="ShareForge",
        url="https://example.com",
    )
    assert 'property="og:title"' in html
    assert "ShareForge Demo" in html
    assert 'name="twitter:card"' in html
    assert "summary_large_image" in html
    assert "og:image" in html

def test_escaping():
    html = generate_meta_tags(
        title='Title with "quotes" & <tags>',
        description="Desc",
    )
    assert "&quot;" in html
    assert "&amp;" in html
    assert "&lt;" in html

def test_warnings():
    warns = validate_inputs("A" * 70, "B" * 200)
    assert "title" in warns
    assert "description" in warns

def test_empty_optional():
    html = generate_meta_tags(title="T", description="D")
    assert "og:image" not in html
    assert "twitter:image" not in html
