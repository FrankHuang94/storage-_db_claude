"""Ch45 — Radar-style comparison of FlashBlade//EXA, VAST, WEKA and DDN on eight axes.

Scores (1-5) are the Everpure Tech Atlas's own judgment, not measured data; the CSV `source`
column carries a one-line rationale per score. Reads data/ch45_radar.csv and writes
docs/assets/charts/ch45-radar.svg.
"""
from __future__ import annotations

import csv
import math
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch45_radar.csv"
NAME = "ch45-radar"
VENDORS = ["Everpure FlashBlade//EXA", "VAST", "WEKA", "DDN"]
COLORS = {"Everpure FlashBlade//EXA": _style.VENDOR_COLORS["Everpure"], "VAST": _style.VENDOR_COLORS["VAST"],
          "WEKA": _style.VENDOR_COLORS["WEKA"], "DDN": _style.VENDOR_COLORS["DDN"]}
STYLES = {"Everpure FlashBlade//EXA": "-", "VAST": "--", "WEKA": "-.", "DDN": ":"}


def _load() -> tuple[list[str], dict]:
    axes: list[str] = []
    scores: dict = {}
    with CSV.open(newline="") as fh:
        for r in csv.DictReader(fh):
            if r["axis"] not in axes:
                axes.append(r["axis"])
            scores[(r["vendor"], r["axis"])] = float(r["score"])
    return axes, scores


def build(out_dir: Path) -> Path:
    _style.apply()
    axes, scores = _load()
    n = len(axes)
    angles = [2 * math.pi * i / n for i in range(n)]
    fig, panels = plt.subplots(1, 4, figsize=(16, 5.4), subplot_kw={"projection": "polar"})
    for ax, vendor in zip(panels, VENDORS):
        # faint outlines of the other three vendors for comparison
        for other in VENDORS:
            vals = [scores[(other, a)] for a in axes]
            if other == vendor:
                continue
            ax.plot(angles + angles[:1], vals + vals[:1], color="#BBBBBB", linewidth=0.9,
                    linestyle=STYLES[other])
        vals = [scores[(vendor, a)] for a in axes]
        ax.plot(angles + angles[:1], vals + vals[:1], color=COLORS[vendor], linewidth=2.4,
                linestyle=STYLES[vendor])
        ax.fill(angles + angles[:1], vals + vals[:1], color=COLORS[vendor], alpha=0.22)
        ax.set_theta_offset(math.pi / 2)
        ax.set_theta_direction(-1)
        ax.set_ylim(0, 5)
        ax.set_rlabel_position(200)
        ax.set_yticks([1, 2, 3, 4, 5])
        ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=8, color="#777777")
        ax.set_xticks(angles)
        ax.set_xticklabels([a.replace(" and ", " &\n").replace("ecosystem ", "ecosystem\n")
                            .replace("benchmark ", "benchmark\n").replace("Capacity ", "Capacity\n")
                            .replace("Deployment ", "Deployment\n").replace("Platform ", "Platform\n")
                            .replace("Proven ", "Proven\n") for a in axes], fontsize=8.5)
        ax.tick_params(axis="x", pad=10)
        ax.set_title(vendor, fontsize=12, fontweight="bold", color=COLORS[vendor], pad=22)
        ax.grid(color=_style.GRID)
    fig.suptitle("Atlas judgment, not measured data: four AI-storage platforms scored 1-5 on eight axes (Nov 2026)",
                 fontsize=13, fontweight="bold", x=0.01, ha="left")
    _style.source_note(fig, "Scores are the Everpure Tech Atlas's qualitative assessment from public sources "
                            "(Chapters 27, 34, 37, 42-44). Grey outlines show the other three vendors. "
                            "Axes are unweighted; do not sum them. One-line rationale per score in "
                            "data/ch45_radar.csv (source column).")
    fig.tight_layout(rect=(0, 0.02, 1, 0.92))
    return _style.save(fig, out_dir, NAME)
