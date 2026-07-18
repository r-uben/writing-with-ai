from __future__ import annotations


def extract_draft(text: str) -> str:
    """Pull prose from a fixture's ### Draft section, or return full text."""
    if "### Draft" not in text:
        return text.strip()
    body = text.split("### Draft", 1)[1]
    if "###" in body:
        body = body.split("###", 1)[0]
    return body.strip()
