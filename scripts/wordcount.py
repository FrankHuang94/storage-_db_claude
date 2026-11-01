#!/usr/bin/env python3
"""Prose word count per chapter / part / total.

Excludes fenced code & Mermaid, tables, HTML tags, image lines, footnote
definitions and the '## Sources' section.

Usage: python3 scripts/wordcount.py [--json] [file.md ...]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from atlas_lib import ROOT, count_words, load_registry  # noqa: E402


def main(argv: list[str]) -> int:
    as_json = "--json" in argv
    files = [a for a in argv if not a.startswith("--")]
    if files:
        for f in files:
            p = Path(f)
            print(f"{count_words(p.read_text()):>7}  {p}")
        return 0
    parts = load_registry()
    report = {"parts": [], "total": 0, "budget": 0}
    for part in parts:
        prow = {"id": part["id"], "title": part["title"], "words": 0, "budget": 0, "chapters": []}
        for ch in part["chapters"]:
            w = count_words(ch["path"].read_text()) if ch["path"].exists() else 0
            prow["chapters"].append({"num": ch["num"], "title": ch["title"], "words": w, "budget": ch["budget"],
                                      "exists": ch["path"].exists()})
            prow["words"] += w
            prow["budget"] += ch["budget"]
        report["parts"].append(prow)
        report["total"] += prow["words"]
        report["budget"] += prow["budget"]
    if as_json:
        print(json.dumps(report, indent=2))
        return 0
    for prow in report["parts"]:
        print(f"\n{prow['title']}  —  {prow['words']:,} / {prow['budget']:,}")
        for c in prow["chapters"]:
            flag = "" if c["exists"] else "  (missing)"
            pct = (100 * c["words"] / c["budget"]) if c["budget"] else 0
            print(f"  Ch {c['num']:>4}  {c['words']:>6,} / {c['budget']:>5,}  {pct:5.0f}%  {c['title']}{flag}")
    print(f"\nTOTAL: {report['total']:,} prose words (budget {report['budget']:,})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
