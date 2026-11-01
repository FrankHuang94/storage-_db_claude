"""Ch26 — DirectFlash Module (DFM) capacity by year vs the largest standard data-centre SSD.

Reads data/ch26_dfm_capacity.csv. Shipped points (filled), Pure Storage's 2023-stated roadmap
(hollow), undated ambitions (hatched band at right) and a standard-SSD roadmap point are kept
visually distinct. Writes docs/assets/charts/ch26-dfm-capacity.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch26_dfm_capacity.csv"
NAME = "ch26-dfm-capacity"
UNDATED_X = 2028.6


def _load() -> list[dict]:
    with CSV.open(newline="") as fh:
        return list(csv.DictReader(fh))


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    fig, ax = plt.subplots(figsize=(10.5, 5.6))
    blue, orange, grey = "#0072B2", "#E69F00", "#999999"

    def pts(series):
        sel = [r for r in rows if r["series"] == series]
        return sel, [float(r["year"]) if r["year"] else UNDATED_X for r in sel], [float(r["capacity_tb"]) for r in sel]

    s, x, y = pts("DFM shipped")
    ax.plot(x, y, "-o", color=blue, markersize=8, linewidth=2, label="DirectFlash Module, shipped", zorder=4)
    for r, xi, yi in zip(s, x, y):
        right = xi < 2020 or abs(yi - 150) < 1
        ax.annotate(r["label"], (xi, yi), xytext=(9, -3) if right else (-8, 9), textcoords="offset points",
                    ha="left" if right else "right", va="top" if right else "baseline", fontsize=8.5, color=blue)

    s, x, y = pts("DFM roadmap (stated 2023)")
    ax.plot(x, y, "--o", color=blue, markerfacecolor="white", markersize=8, linewidth=1.2,
            label="DFM roadmap as stated in 2023", zorder=3)

    s, x, y = pts("Largest standard SSD")
    ax.plot(x, y, "-s", color=orange, markersize=7, linewidth=2, label="Largest standard SSD, shipping", zorder=4)
    for r, xi, yi in zip(s, x, y):
        ax.annotate(r["label"], (xi, yi), xytext=(6, -14), textcoords="offset points", fontsize=8.5, color="#8a5d00")

    s, x, y = pts("Standard SSD roadmap")
    ax.plot(x, y, "s", color=orange, markerfacecolor="white", markersize=8, label="Standard SSD vendor roadmap", zorder=4)
    for r, xi, yi in zip(s, x, y):
        ax.annotate(r["label"], (xi, yi), xytext=(-6, 8), textcoords="offset points", ha="right", fontsize=8.5, color="#8a5d00")

    s, x, y = pts("DFM ambition (undated)")
    ax.axvspan(UNDATED_X - 0.45, UNDATED_X + 0.45, color=grey, alpha=0.15, hatch="//", zorder=1)
    ax.plot(x, y, "D", color=blue, markerfacecolor="white", markersize=8, label="DFM stated ambition, no date", zorder=4)
    for r, xi, yi in zip(s, x, y):
        ax.annotate(r["label"], (xi, yi), xytext=(-10, 0), textcoords="offset points", ha="right", va="center",
                    fontsize=8.5, color=blue)

    ax.set_yscale("log", base=2)
    ax.set_yticks([16, 32, 64, 128, 256, 512, 1024])
    ax.set_yticklabels(["16", "32", "64", "128", "256", "512", "1,024"])
    ax.set_ylim(12, 1500)
    ax.set_xlim(2018.8, 2029.3)
    ticks = list(range(2019, 2028))
    ax.set_xticks(ticks + [UNDATED_X])
    ax.set_xticklabels([str(t) for t in ticks] + ["no date"])
    ax.set_ylabel("Capacity per module or drive, TB (log2 scale)")
    ax.set_xlabel("Year shipped or targeted")
    ax.legend(loc="upper left", fontsize=9)
    ax.set_title("DFM capacity doubled roughly every 1-1.5 years since 2023, each step landing above the largest standard SSD",
                 loc="left", fontsize=12)
    _style.source_note(fig, "Sources: Pure Storage/Everpure filings, blogs and webinars; Blocks & Files (2023-03-01, 2024-09-24, "
                            "2025-08-05, 2026-08-11); StorageReview; TechTarget; Micron (2026-05-05). 2019 and 2025 DFM points rest "
                            "partly on search summaries [VERIFY]. Roadmap and ambition points are company statements, not shipments. "
                            "Data: data/ch26_dfm_capacity.csv")
    fig.tight_layout()
    return _style.save(fig, out_dir, NAME)
