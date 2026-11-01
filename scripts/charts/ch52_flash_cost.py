"""Ch52 — NAND flash price per GB over time (log scale), sparse sourced points.

Reads data/ch52_flash_cost.csv. Series use different bases (retrospective claims, retail card,
analyst market price, TrendForce 512Gb TLC wafer spot), so points are not joined across series.
Shaded bands mark the downturns and the 2025-26 surge discussed in Chapter 52.
Writes docs/assets/charts/ch52-flash-cost.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch52_flash_cost.csv"
NAME = "ch52-flash-cost"
SERIES = {
    "Company/press retrospective": dict(color="#999999", marker="D", linestyle="none"),
    "Retail flash card": dict(color="#CC79A7", marker="s", linestyle="none"),
    "NAND market price (analyst)": dict(color="#0072B2", marker="o", linestyle="-"),
    "512Gb TLC wafer spot (TrendForce)": dict(color="#D55E00", marker="o", linestyle="-"),
}
BANDS = [(2008.3, 2009.2, "2008\nbust"), (2012.0, 2012.9, "2012\nbust"), (2018.2, 2019.7, "2018-19\nbust"),
         (2022.4, 2023.7, "2022-23\nbust")]


def _load() -> list[dict]:
    with CSV.open(newline="") as fh:
        return list(csv.DictReader(fh))


def _fmt(v: float) -> str:
    if v >= 10:
        return f"\\${v:,.0f}"
    if v >= 1:
        return f"\\${v:.2f}"
    return f"{v * 100:.1f}¢"


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    fig, ax = plt.subplots(figsize=(11, 5.6))
    for x0, x1, label in BANDS:
        ax.axvspan(x0, x1, color="#DDDDDD", alpha=0.6, zorder=0)
        ax.text((x0 + x1) / 2, 30000, label, ha="center", va="top", fontsize=8.5, color="#555555")
    ax.axvspan(2025.5, 2027.0, color="#F0E442", alpha=0.35, zorder=0)
    ax.text(2026.25, 30000, "2025-26\nsurge", ha="center", va="top", fontsize=8.5, color="#555555")
    for name, st in SERIES.items():
        pts = sorted((float(r["date"]), float(r["usd_per_gb"]), r["status"], r["period"]) for r in rows
                     if r["series"] == name)
        xs, ys = [p[0] for p in pts], [p[1] for p in pts]
        ax.plot(xs, ys, label=name, linewidth=1.4, markersize=7, zorder=3, **st)
        for x, v, status, per in pts:
            if status != "sourced":  # hollow overlay for unverified / company-stated points
                ax.plot([x], [v], marker=st["marker"], markersize=4, color="white", linestyle="none", zorder=4)
            dy = 7 if name != "512Gb TLC wafer spot (TrendForce)" else -14
            if per in ("Mar 2026", "Aug 2026"):
                continue
            ax.annotate(f"{_fmt(v)}\n{per}", (x, v), xytext=(4, dy), textcoords="offset points", fontsize=7.5,
                        color=st["color"])
    ax.set_yscale("log")
    ax.set_ylim(0.01, 40000)
    ax.set_xlim(1993, 2027.5)
    ax.set_ylabel("US\\$ per GB (log scale, nominal)")
    ax.set_xlabel("Year")
    ax.legend(loc="lower left", fontsize=9)
    ax.text(2009.5, 400, "~35%/yr average decline, 2005 to mid-2023\n(\\$45/GB to ~2.2¢/GB; worked, mixed bases)",
            fontsize=8.5, color="#333333")
    ax.set_title("NAND flash \\$/GB: ~5 orders of magnitude down, then a ~15x spike in 2023-26 (sparse sourced points)",
                 loc="left", fontsize=12.5)
    _style.source_note(fig, "Sources: Kioxia (2022, company-stated); Design News (2022); McCallum log via PhotographyTalk; "
                            "Semico/iSuppli via MacDailyNews (2005); iSuppli via MacTech (2010); Objective Analysis via EE Times "
                            "Japan (2015) and TechTarget (2019, 2021); TrendForce 512Gb TLC wafer spot (2023-26, per 512Gb unit / 64). "
                            "Small white centre = search-summary only or company-stated. Bases differ; read the slope, not decimals. "
                            "Data: data/ch52_flash_cost.csv")
    fig.tight_layout()
    return _style.save(fig, out_dir, NAME)
