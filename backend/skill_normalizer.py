import re

# Map common variants and typos to canonical skill tokens.
VARIANT_TO_CANONICAL = {
    "machine learning": "ml",
    "deep learning": "ml",
    "ml": "ml",
    "py": "python",
    "pyhton": "python",
    "phtyon": "python",
    "python": "python",
    "java script": "javascript",
    "javascript": "javascript",
    "javscript": "javascript",
    "javasript": "javascript",
    "js": "javascript",
    "reactjs": "react",
    "react": "react",
    "statitics": "statistics",
    "statistic": "statistics",
    "statistics": "statistics",
    "c sharp": "c#",
    "c#": "c#",
}


def _normalize_token(token):
    cleaned = re.sub(r"\s+", " ", token.strip().lower())
    if not cleaned:
        return ""
    return VARIANT_TO_CANONICAL.get(cleaned, cleaned)


def normalize_skills_text(skills_text):
    if not skills_text:
        return ""

    tokens = re.split(r"[;,]", skills_text)
    normalized = []
    seen = set()

    for token in tokens:
        cleaned = _normalize_token(token)
        if not cleaned:
            continue
        if cleaned not in seen:
            normalized.append(cleaned)
            seen.add(cleaned)

    return ", ".join(normalized)
