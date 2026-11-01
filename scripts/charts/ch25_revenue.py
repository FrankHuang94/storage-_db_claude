"""Ch25 — Everpure (formerly Pure Storage) fiscal-year revenue, FY2016–FY2026, plus FY2027 guidance.

Reads data/ch25_revenue.csv (every row carries `source`, `as_of` and a `verified` flag).
Actual years are solid bars; FY2017–FY2018 (pre-ASC 606, as originally reported) are lighter;
FY2027 guidance is a hatched bar with its low–high range. Rows not checked against the filing
this session are marked with a dagger. Writes docs/assets/charts/ch25-revenue.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

import _style

CSV = _style.DATA / "ch25_revenue.csv"
NAME = "ch25-revenue"
BLUE = "#0072B2"
SKY = "#56B4E9"
ACCENT = "#D55E00"


def _load() -> list[dict]:
    with CSV.open(newline="") as fh:
        return list(csv.DictReader(fh))


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    fig, ax = plt.subplots(figsize=(11, 5.2))
    prev = None
    for i, r in enumerate(rows):
        val = float(r["revenue_musd"])
        guidance = r["kind"] == "guidance"
        pre606 = "ASC 605" in r["basis"]
        if guidance:
            ax.bar(i, val, color="white", edgecolor=ACCENT, hatch="//", linewidth=1.5)
            lo, hi = float(r["revenue_low_musd"]), float(r["revenue_high_musd"])
            ax.errorbar(i, val, yerr=[[val - lo], [hi - val]], color=ACCENT, capsize=5, linewidth=1.5)
        else:
            ax.bar(i, val, color=SKY if pre606 else BLUE)
        label = f"{val/1000:.2f}B"
        if prev:
            label += f"\n{(val/prev - 1)*100:+.0f}%"
        ax.text(i, val + 60, label, ha="center", va="bottom", fontsize=8.5, color="#222222")
        prev = val
    ticks = []
    for r in rows:
        t = r["fiscal_year"]
        if not r["verified"].startswith(("checked", "guidance")):
            t += "†"
        ticks.append(t)
    ax.set_xticks(range(len(rows)))
    ax.set_xticklabels(ticks, rotation=0, fontsize=9)
    ax.set_ylabel("Total revenue (US$ millions)")
    ax.set_ylim(0, 6000)
    notes = [(4.5, 2250, "FY21 +2%: COVID year;\nPortworx closes"), (7.6, 3400, "FY24 +3%: second\nnear-flat year"),
             (9.3, 4700, "FY27 guide raised twice:\n4.3–4.4B (Feb 2026) to\n5.03–5.07B (Aug 2026)")]
    for x, y, txt in notes:
        ax.text(x, y, txt, fontsize=8.5, color="#555555", ha="center", va="bottom")
    handles = [Patch(color=SKY, label="Actual, pre-ASC 606 as reported"), Patch(color=BLUE, label="Actual (ASC 606)"),
               Patch(facecolor="white", edgecolor=ACCENT, hatch="//", label="FY2027 guidance midpoint, range bar (not actual)")]
    ax.legend(handles=handles, loc="upper left", fontsize=9)
    ax.set_title("Everpure (formerly Pure Storage) revenue by fiscal year, FY2016–FY2026, with FY2027 guidance",
                 loc="left", fontsize=12.5)
    ax.grid(axis="x", visible=False)
    _style.source_note(fig, "Sources: Pure Storage / Everpure Form 10-K filings FY2016–FY2026; FY2027 guidance from the "
                            "Q2 FY27 results release, 2026-08-26. Fiscal years end near Feb 1. FY2022 had 53 weeks. "
                            "† = taken from search summaries of the 10-K, not re-checked against the filing this session. "
                            "Data: data/ch25_revenue.csv")
    fig.tight_layout()
    return _style.save(fig, out_dir, NAME)
