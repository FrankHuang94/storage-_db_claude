#!/usr/bin/env python3
"""Fix bold/italic emphasis that CommonMark (GitHub) refuses to render next to CJK punctuation.

CommonMark only treats `**` as a closing delimiter if it is "right-flanking": when the
character before it is punctuation, the character after it must be whitespace or punctuation.
Chinese text often has `**术语：**正文`, which therefore renders literally. This script moves
leading/trailing punctuation outside the emphasis when the neighbouring character is a letter
(e.g., a CJK character):  `**术语：**正文` -> `**术语**：正文`,  `中**“X”**文` -> `中“**X**”文`.

Usage: python3 scripts/zh_fix_bold.py [files...]   (default: every .md under "Chinese translation/")
Skips fenced code/Mermaid blocks and inline code.
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOLD = re.compile(r"(?<![*\\])\*\*(?!\s)(.+?)(?<!\s)\*\*(?!\*)")


def is_punct(ch: str) -> bool:
    return bool(ch) and unicodedata.category(ch)[0] in "PS"


def is_space_or_punct(ch: str) -> bool:
    return ch == "" or ch.isspace() or is_punct(ch)


def fix_line(line: str) -> tuple[str, int]:
    # protect inline code
    parts = re.split(r"(`[^`]*`)", line)
    changes = 0
    for i, part in enumerate(parts):
        if part.startswith("`"):
            continue
        out = []
        pos = 0
        for m in BOLD.finditer(part):
            start, end = m.span()
            inner = m.group(1)
            before = part[start - 1] if start > 0 else ""
            after = part[end] if end < len(part) else ""
            lead = trail = ""
            # trailing punctuation inside closing ** followed by a non-space, non-punct char
            while inner and is_punct(inner[-1]) and not is_space_or_punct(after):
                trail = inner[-1] + trail
                inner = inner[:-1]
            # leading punctuation inside opening ** preceded by a non-space, non-punct char
            while inner and is_punct(inner[0]) and not is_space_or_punct(before):
                lead += inner[0]
                inner = inner[1:]
            if (lead or trail) and inner.strip():
                out.append(part[pos:start] + lead + "**" + inner + "**" + trail)
                changes += 1
            else:
                out.append(part[pos:end])
            pos = end
        out.append(part[pos:])
        parts[i] = "".join(out)
    return "".join(parts), changes


def fix_file(path: Path) -> int:
    lines = path.read_text().split("\n")
    in_code = False
    total = 0
    for i, line in enumerate(lines):
        if line.lstrip().startswith(("```", "~~~")):
            in_code = not in_code
            continue
        if in_code or "**" not in line:
            continue
        new, n = fix_line(line)
        if n:
            lines[i] = new
            total += n
    if total:
        path.write_text("\n".join(lines))
    return total


def main(argv: list[str]) -> int:
    files = [Path(a) for a in argv] or sorted((ROOT / "Chinese translation").rglob("*.md"))
    grand = 0
    for f in files:
        n = fix_file(f)
        if n:
            print(f"{n:4d}  {f.relative_to(ROOT) if f.is_absolute() else f}")
        grand += n
    print(f"fixed {grand} emphasis span(s) in {len(files)} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
