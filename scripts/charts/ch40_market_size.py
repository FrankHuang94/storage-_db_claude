"""Ch40 — IDC worldwide external (OEM) enterprise storage systems revenue.

Reads data/ch40_market_size.csv (every row carries `source`, `as_of` and `status`).
Left panel: second-quarter revenue across years (2Q18-2Q26, gaps where no public release was found).
Right panel: the eight most recent quarters (3Q24-2Q26). Derived values (computed from IDC's
published growth rates or vendor share tables) are hatched. Writes docs/assets/charts/ch40-market-size.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

import _style

CSV = _style.DATA / "ch40_market_size.csv"
NAME = "ch40-market-size"
BLUE = "#0072B2"
SKY = "#56B4E9"
ACCENT = "#D55E00"


def _load() -> list[dict]:
    with CSV.open(newline="") as fh:
        return list(csv.DictReader(fh))


def _bars(ax, rows, highlight):
    xs = list(range(len(rows)))
    for x, r in zip(xs, rows):
        v = float(r["revenue_busd"])
        derived = r["status"] == "derived"
        color = ACCENT if r["period"] == highlight else (SKY if derived else BLUE)
        ax.bar(x, v, width=0.65, color="white" if derived else color, edgecolor=color,
               hatch="//" if derived else None, linewidth=1.4)
        ax.text(x, v + 0.15, f"{v:.1f}", ha="center", va="bottom", fontsize=9.5, color="#222222")
        if r["yoy_pct"]:
            ax.text(x, v / 2, f"{float(r['yoy_pct']):+.1f}%", ha="center", va="center", fontsize=8.5,
                    color="#222222" if derived else "white", fontweight="bold")
    ax.set_xticks(xs)
    ax.set_xticklabels([r["period"] for r in rows], fontsize=9.5)
    ax.set_ylim(0, 11.8)
    ax.grid(axis="x", visible=False)


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    hist = sorted([r for r in rows if r["series"] == "q2_history"], key=lambda r: float(r["sort_key"]))
    recent = sorted([r for r in rows if r["series"] == "recent"], key=lambda r: float(r["sort_key"]))
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.8), gridspec_kw={"width_ratios": [5, 8]}, sharey=True)
    _bars(a1, hist, "2Q26")
    a1.set_title("Second quarters, 2018–2026", loc="left", fontsize=11)
    a1.set_ylabel("Vendor revenue, US$ billions")
    _bars(a2, recent, "2Q26")
    a2.set_title("Last eight quarters (Q4 is seasonally strongest)", loc="left", fontsize=11)
    handles = [Patch(color=BLUE, label="Reported by IDC"),
               Patch(facecolor="white", edgecolor=SKY, hatch="//", label="Derived from IDC growth or share tables"),
               Patch(color=ACCENT, label="Latest quarter, 2Q26")]
    a2.legend(handles=handles, loc="upper left", fontsize=9)
    fig.suptitle("External enterprise storage systems revenue (IDC): flat for years, then +34% in 2Q26",
                 x=0.01, ha="left", fontsize=12.5, fontweight="bold")
    _style.source_note(fig, "Sources: IDC Worldwide Quarterly Enterprise Storage Systems Tracker press releases (2018-09, 2019-09, 2021-09, "
                            "2025-12-11, 2026-03-12, 2026-06-15, 2026-09-10). Percentages inside bars are IDC-reported YoY growth. "
                            "1Q26 growth was later restated by IDC from 22.7% to 28.7%; 2Q20, 2Q22-2Q24 omitted (no public figure retrieved). "
                            "Data: data/ch40_market_size.csv")
    fig.tight_layout()
    return _style.save(fig, out_dir, NAME)
