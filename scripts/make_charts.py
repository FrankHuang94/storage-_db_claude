#!/usr/bin/env python3
"""Regenerate every chart: imports each scripts/charts/ch*.py and calls build(out_dir).

Usage: python3 scripts/make_charts.py [name_substring ...]
Also validates that every data/*.csv has 'source' and 'as_of' columns.
"""
from __future__ import annotations

import csv
import importlib.util
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHARTS = ROOT / "scripts" / "charts"
OUT = ROOT / "docs" / "assets" / "charts"
sys.path.insert(0, str(CHARTS))


def check_csvs() -> int:
    bad = 0
    for p in sorted((ROOT / "data").glob("*.csv")):
        with p.open(newline="") as fh:
            header = next(csv.reader(fh), [])
        cols = {h.strip().lower() for h in header}
        if not {"source", "as_of"} <= cols:
            print(f"CSV missing source/as_of columns: {p.relative_to(ROOT)}")
            bad += 1
    return bad


def main(argv: list[str]) -> int:
    failures = check_csvs()
    mods = sorted(p for p in CHARTS.glob("ch*.py"))
    if argv:
        mods = [m for m in mods if any(a in m.name for a in argv)]
    for m in mods:
        spec = importlib.util.spec_from_file_location(m.stem, m)
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)
            out = mod.build(OUT)
            print(f"ok   {m.name} -> {out if out else OUT}")
        except Exception:  # noqa: BLE001
            failures += 1
            print(f"FAIL {m.name}")
            traceback.print_exc()
    print(f"{len(mods)} chart module(s), {failures} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
