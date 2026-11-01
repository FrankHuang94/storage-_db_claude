"""Ch6 — Illustrative typical RPO and RTO ranges by protection technique (log time axis).

Reads data/ch06_rpo_rto.csv (every row carries `source` and `as_of`); writes docs/assets/charts/ch06-rpo-rto.svg.
Zero values are drawn at a 1-second floor and annotated "0".
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch06_rpo_rto.csv"
NAME = "ch06-rpo-rto"
FLOOR = 1.0
TICKS = [1, 60, 3600, 86400, 2419200]
TICKLABELS = ["1 s", "1 min", "1 h", "1 day", "4 wk"]


def _load() -> list[dict]:
    with CSV.open(newline="") as fh:
        return list(csv.DictReader(fh))


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8), sharey=True)
    y = list(range(len(rows)))
    for ax, key, title, color in ((axes[0], "rpo", "RPO: how much data you lose", "#D55E00"),
                                  (axes[1], "rto", "RTO: how long you are down", "#0072B2")):
        for i, r in enumerate(rows):
            lo, hi = float(r[f"{key}_min_s"]), float(r[f"{key}_max_s"])
            lo_p, hi_p = max(lo, FLOOR), max(hi, FLOOR)
            if hi_p <= lo_p * 1.15:
                ax.plot([lo_p], [i], marker="o", markersize=9, color=color)
            else:
                ax.plot([lo_p, hi_p], [i, i], linewidth=9, solid_capstyle="round", color=color)
            if hi == 0:
                ax.text(FLOOR * 1.6, i, "0", va="center", fontsize=10, fontweight="bold", color="#222222")
        ax.set_xscale("log")
        ax.set_xlim(0.6, 5e6)
        ax.set_xticks(TICKS)
        ax.set_xticklabels(TICKLABELS)
        ax.set_title(title, loc="left", fontsize=12)
        ax.grid(axis="y", visible=False)
    axes[0].set_yticks(y)
    axes[0].set_yticklabels([r["technique"] for r in rows])
    axes[0].invert_yaxis()
    fig.suptitle("Illustrative: typical RPO and RTO ranges by protection technique", fontsize=13,
                 fontweight="bold", x=0.01, ha="left")
    _style.source_note(fig, "Illustrative typical ranges, not vendor guarantees; actual values depend on configuration, distance, change rate and "
                            "runbooks. Zero is drawn at 1 s. Ransomware RTO reflects Sophos 2025 survey data (about half fully recover within a week). "
                            "Data: data/ch06_rpo_rto.csv")
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    return _style.save(fig, out_dir, NAME)
