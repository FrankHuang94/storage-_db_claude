#!/usr/bin/env python3
"""Check internal Markdown links (files + heading anchors) across the repo.

Usage: python3 scripts/check_links.py [--allow-planned] [file.md ...]
--allow-planned: links to chapters listed in meta/chapters.yml but not yet written are not errors.
Exit code 1 if any broken link is found.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

sys.path.insert(0, str(Path(__file__).parent))
from atlas_lib import ROOT, slugify, split_fences  # noqa: E402

LINK_RE = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")
SRC_RE = re.compile(r"<img[^>]+src=\"([^\"]+)\"")

_anchor_cache: dict[Path, set[str]] = {}


def anchors_for(path: Path) -> set[str]:
    if path in _anchor_cache:
        return _anchor_cache[path]
    text = path.read_text(errors="ignore")
    noncode = "\n".join(b for c, _l, b in split_fences(text) if not c)
    found: set[str] = set()
    counts: dict[str, int] = {}
    for h in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", noncode, flags=re.M):
        s = slugify(re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", h))
        n = counts.get(s, 0)
        found.add(s if n == 0 else f"{s}-{n}")
        found.add(s.strip("-"))
        counts[s] = n + 1
    found |= set(re.findall(r'id="([^"]+)"', text))
    found |= set(re.findall(r"\{#([\w\-]+)\}", text))
    _anchor_cache[path] = found
    return found


PLANNED: set[Path] = set()


def check_file(md: Path) -> list[str]:
    errors = []
    text = md.read_text(errors="ignore")
    noncode = "\n".join(b for c, _l, b in split_fences(text) if not c)
    # strip inline code spans
    noncode = re.sub(r"`[^`\n]*`", "", noncode)
    targets = [(m, False) for m in LINK_RE.findall(noncode)]
    targets += [(m, True) for m in IMG_RE.findall(noncode)]
    targets += [(m, True) for m in SRC_RE.findall(noncode)]
    for target, is_img in targets:
        if re.match(r"^[a-z]+:", target) or target.startswith("//"):
            continue  # external / mailto
        path_part, _, anchor = target.partition("#")
        path_part = unquote(path_part)
        dest = md if not path_part else (md.parent / path_part).resolve()
        if not dest.exists():
            if dest in PLANNED:
                continue  # chapter planned in meta/chapters.yml but not yet written
            errors.append(f"{md.relative_to(ROOT)}: missing target '{target}'")
            continue
        if anchor and dest.suffix == ".md" and anchor not in anchors_for(dest):
            errors.append(f"{md.relative_to(ROOT)}: missing anchor '#{anchor}' in {dest.relative_to(ROOT)}")
    return errors


def main(argv: list[str]) -> int:
    if "--allow-planned" in argv:
        from atlas_lib import all_chapters
        PLANNED.update(c["path"].resolve() for c in all_chapters())
        zh = ROOT / "Chinese translation"
        PLANNED.update((zh / c["path"].relative_to(ROOT)).resolve() for c in all_chapters())
        PLANNED.add((zh / "docs" / "glossary.md").resolve())
        argv = [a for a in argv if a != "--allow-planned"]
    files = [Path(a).resolve() for a in argv] if argv else sorted(
        [p for p in ROOT.rglob("*.md") if "node_modules" not in p.parts and "site" not in p.parts
         and ".git" not in p.parts])
    errs: list[str] = []
    for f in files:
        errs += check_file(f)
    for e in errs:
        print("BROKEN", e)
    print(f"Checked {len(files)} files — {len(errs)} broken link(s)")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
