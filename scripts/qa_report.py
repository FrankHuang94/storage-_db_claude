#!/usr/bin/env python3
"""Per-chapter QA: template compliance, words vs budget, visual density, VERIFY count,
footnote integrity. Writes meta/qa-report.md and prints a summary.

Usage: python3 scripts/qa_report.py [--chapter 16] [--quiet]
Exit code 1 if any existing chapter fails a hard check.
"""
from __future__ import annotations

import math
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from atlas_lib import (DEEP_DIVE_EXTRA, DEEP_DIVES, META, ROOT, TEMPLATE_HEADINGS, all_chapters,  # noqa: E402
                       count_verify, count_visuals, count_words, headings)


def check(ch: dict) -> dict:
    md = ch["path"].read_text()
    words = count_words(md)
    vis = count_visuals(md)
    h2 = headings(md, 2)
    required = list(TEMPLATE_HEADINGS) + (DEEP_DIVE_EXTRA if ch["num"] in DEEP_DIVES else [])
    missing = [h for h in required if h not in h2]
    issues = []
    if missing:
        issues.append("missing headings: " + ", ".join(missing))
    first = md.lstrip().splitlines()[0] if md.strip() else ""
    if not first.startswith("# "):
        issues.append("no H1 title")
    if "**Depth:**" not in md[:600] or "**Last verified:**" not in md[:600]:
        issues.append("header block (Depth/Reading time/Last verified) missing")
    need_vis = max(3, math.ceil(words / 700))
    if vis["total"] < need_vis:
        issues.append(f"visuals {vis['total']} < required {need_vis}")
    if vis["non_table"] < 2:
        issues.append(f"non-table visuals {vis['non_table']} < 2")
    # footnotes: every ref has a definition and vice versa
    refs = set(re.findall(r"\[\^([^\]]+)\](?!:)", md))
    defs = set(re.findall(r"^\[\^([^\]]+)\]:", md, flags=re.M))
    undefined = refs - defs
    unused = defs - refs
    if undefined:
        issues.append(f"undefined footnotes: {sorted(undefined)[:8]}")
    if unused:
        issues.append(f"unused footnote defs: {sorted(unused)[:8]}")
    if ch["budget"] and words < 0.9 * ch["budget"]:
        issues.append(f"words {words} < 90% of budget {ch['budget']}")
    # playbook sanity
    if "Conversation playbook" in h2 and not re.search(r"Don.t say", md):
        issues.append("playbook lacks 'Don't say this'")
    # images need alt text
    if re.search(r"!\[\s*\]\(", md):
        issues.append("image without alt text")
    return {"num": ch["num"], "title": ch["title"], "words": words, "budget": ch["budget"],
            "visuals": vis, "need_vis": need_vis, "verify": count_verify(md),
            "footnotes": len(defs), "issues": issues}


def main(argv: list[str]) -> int:
    only = None
    if "--chapter" in argv:
        only = argv[argv.index("--chapter") + 1]
    quiet = "--quiet" in argv
    rows = []
    for ch in all_chapters():
        if only and ch["num"] != only:
            continue
        if not ch["path"].exists():
            rows.append({"num": ch["num"], "title": ch["title"], "missing": True})
            continue
        rows.append(check(ch))
    lines = ["# QA report", "", "| Ch | Title | Words / budget | Visuals (M/I/T) / need | VERIFY | Fn | Status |",
             "|---|---|---|---|---|---|---|"]
    fails = 0
    tw = tv = tver = 0
    for r in rows:
        if r.get("missing"):
            lines.append(f"| {r['num']} | {r['title']} | — | — | — | — | not written |")
            continue
        v = r["visuals"]
        tw += r["words"]; tv += v["total"]; tver += r["verify"]
        status = "PASS" if not r["issues"] else "FAIL: " + "; ".join(r["issues"])
        if r["issues"]:
            fails += 1
        lines.append(f"| {r['num']} | {r['title']} | {r['words']:,} / {r['budget']:,} | "
                     f"{v['total']} ({v['mermaid']}/{v['images']}/{v['tables']}) / {r['need_vis']} | "
                     f"{r['verify']} | {r['footnotes']} | {status} |")
    lines += ["", f"**Totals (written chapters):** {tw:,} words · {tv} visuals · {tver} VERIFY markers · "
              f"{fails} failing chapter(s)"]
    if not only:
        (META / "qa-report.md").write_text("\n".join(lines) + "\n")
    if not quiet:
        print("\n".join(lines))
    else:
        print(lines[-1])
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
