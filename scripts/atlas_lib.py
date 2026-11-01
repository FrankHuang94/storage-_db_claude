"""Shared helpers for atlas QA scripts."""
from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
META = ROOT / "meta"

TEMPLATE_HEADINGS = [
    "TL;DR",
    "Why this matters for Everpure strategy",
    "Core concepts",
    "How Everpure approaches it vs. competitors",
    "History and trajectory",
    "Numbers that matter",
    "Conversation playbook",
    "Key terms",
    "Sources",
]
DEEP_DIVE_EXTRA = [
    "Business model & financials",
    "Customers & go-to-market",
    "Why it gained traction",
    "Risks & open questions",
    "Strategic relevance to Everpure",
]
DEEP_DIVES = {"42", "43", "44"}


def load_registry() -> list[dict]:
    """Return list of parts, each with chapters (dicts with num,file,title,budget,path)."""
    data = yaml.safe_load((META / "chapters.yml").read_text())
    parts = data["parts"]
    for part in parts:
        for ch in part["chapters"]:
            ch["path"] = DOCS / part["dir"] / ch["file"]
            ch["part"] = part["id"]
    return parts


def all_chapters() -> list[dict]:
    return [ch for p in load_registry() for ch in p["chapters"]]


FENCE_RE = re.compile(r"^(```|~~~)")


def split_fences(text: str):
    """Yield (is_code, lang, block_text) segments."""
    lines = text.splitlines()
    buf: list[str] = []
    in_code = False
    lang = ""
    fence = ""
    for line in lines:
        stripped = line.lstrip()
        if not in_code and FENCE_RE.match(stripped):
            if buf:
                yield (False, "", "\n".join(buf))
                buf = []
            in_code = True
            fence = stripped[:3]
            lang = stripped[3:].strip().split()[0] if stripped[3:].strip() else ""
            continue
        if in_code and stripped.startswith(fence) and stripped.strip() == fence:
            yield (True, lang, "\n".join(buf))
            buf = []
            in_code = False
            lang = ""
            continue
        buf.append(line)
    if buf:
        yield (in_code, lang, "\n".join(buf))


def prose_text(md: str) -> str:
    """Strip everything that is not prose, for word counting."""
    # drop Sources section onwards (Sources is the last template section)
    m = re.search(r"^##\s+Sources\s*$", md, flags=re.M)
    if m:
        md = md[: m.start()]
    out = []
    for is_code, _lang, block in split_fences(md):
        if is_code:
            continue
        for line in block.splitlines():
            s = line.strip()
            if s.startswith("|"):
                continue  # table rows
            if s.startswith("[^") and "]:" in s[:12]:
                continue  # footnote definitions
            if re.match(r"^!\[.*\]\(.*\)\s*$", s):
                continue  # image lines
            if s.startswith("<") and not s.startswith("<details") and not s.startswith("<summary"):
                # html blocks (svg inline etc.) – drop the tags but keep text below
                s = re.sub(r"<[^>]+>", " ", s)
            s = re.sub(r"<[^>]+>", " ", s)
            s = re.sub(r"\[\^[^\]]+\]", " ", s)  # footnote refs
            s = re.sub(r"\]\([^)]*\)", "]", s)  # link targets
            s = re.sub(r"https?://\S+", " ", s)
            out.append(s)
    return "\n".join(out)


WORD_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9'’.\-/%$,]*")


def count_words(md: str) -> int:
    return len(WORD_RE.findall(prose_text(md)))


def count_visuals(md: str) -> dict:
    mermaid = 0
    for is_code, lang, _ in split_fences(md):
        if is_code and lang == "mermaid":
            mermaid += 1
    # images outside code
    noncode = "\n".join(b for c, _l, b in split_fences(md) if not c)
    images = len(re.findall(r"!\[[^\]]*\]\([^)]+\)", noncode)) + len(re.findall(r"<img\s", noncode))
    inline_svg = len(re.findall(r"<svg[\s>]", noncode))
    # tables: count table blocks with >=3 data rows and >=3 columns, excluding the "Numbers that matter" requirement? (counted)
    tables = 0
    lines = noncode.splitlines()
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith("|"):
            j = i
            while j < len(lines) and lines[j].strip().startswith("|"):
                j += 1
            block = lines[i:j]
            cols = block[0].strip().strip("|").count("|") + 1
            data_rows = max(0, len(block) - 2)
            if cols >= 3 and data_rows >= 3:
                tables += 1
            i = j
        else:
            i += 1
    return {
        "mermaid": mermaid,
        "images": images + inline_svg,
        "tables": tables,
        "total": mermaid + images + inline_svg + tables,
        "non_table": mermaid + images + inline_svg,
    }


def headings(md: str, level: int = 2) -> list[str]:
    noncode = "\n".join(b for c, _l, b in split_fences(md) if not c)
    return [h.strip() for h in re.findall(rf"^{'#' * level}\s+(.+?)\s*$", noncode, flags=re.M)]


def count_verify(md: str) -> int:
    return len(re.findall(r"\[VERIFY", md))


def slugify(text: str) -> str:
    """GitHub-compatible heading slug (close to MkDocs toc default)."""
    text = text.strip().lower()
    text = re.sub(r"[`*_~]", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[^\w\- ]", "", text)
    text = text.replace(" ", "-")
    return text
