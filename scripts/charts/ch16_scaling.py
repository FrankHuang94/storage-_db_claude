"""Ch16 — Illustrative worked example: cost of meeting a requirement, shared-nothing vs DASE.

Reads data/ch16_scaling.csv (generated from the chapter's stated assumptions; every row carries
`source` and `as_of`). Two panels: (A) capacity fixed, throughput requirement grows;
(B) throughput fixed, capacity requirement grows. Writes docs/assets/charts/ch16-scaling.svg.

Pattern for later chart modules: read CSV with csv.DictReader, call _style.apply(), draw with
matplotlib, label illustrative data as such in the title, add a source note, save via _style.save().
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch16_scaling.csv"
NAME = "ch16-scaling"
COLORS = {"Shared-nothing": "#009E73", "DASE": "#D55E00"}  # architecture colors, not vendor colors
MARKERS = {"Shared-nothing": "o", "DASE": "s"}


def _load() -> dict:
    series: dict = {}
    with CSV.open(newline="") as fh:
        for r in csv.DictReader(fh):
            key = (r["scenario"], r["architecture"])
            series.setdefault(key, []).append((float(r["x_value"]), float(r["cost_index"])))
    return series


def build(out_dir: Path) -> Path:
    _style.apply()
    s = _load()
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6), sharey=False)
    panels = [
        ("A_fixed_capacity_5PB", "A. Capacity fixed at 5 PB usable", "Throughput required (GB/s)", 180,
         "shared-nothing gets\n~180 GB/s 'free'\nwith 5 PB of nodes"),
        ("B_fixed_throughput_200GBps", "B. Throughput fixed at 200 GB/s", "Usable capacity required (PB)", 5.9,
         "shared-nothing gets\n~5.9 PB 'free'\nwith 200 GB/s of nodes"),
    ]
    for ax, (scen, title, xlabel, kink, note) in zip(axes, panels):
        for arch in ("Shared-nothing", "DASE"):
            pts = sorted(s[(scen, arch)])
            ax.plot([p[0] for p in pts], [p[1] for p in pts], color=COLORS[arch], marker=MARKERS[arch],
                    markersize=4, linewidth=2, label=arch)
        ax.axvline(kink, color="#888888", linestyle=":", linewidth=1.2)
        ymax = ax.get_ylim()[1]
        ax.text(kink, ymax * 0.97, " " + note.replace("\n", "\n "), fontsize=9, color="#555555", va="top")
        ax.set_title(title, fontsize=12)
        ax.set_xlabel(xlabel)
        ax.set_ylim(bottom=0)
    axes[0].set_ylabel("Hardware cost index (relative units)")
    axes[0].legend(loc="lower right")
    fig.suptitle("Illustrative worked example: decoupling pays off when your workload is off the node's built-in ratio",
                 fontsize=13, fontweight="bold", x=0.01, ha="left")
    _style.source_note(fig, "Illustrative model, not vendor data. Assumptions: 30.72 TB QLC drives; shared-nothing node = 24 drives, "
                            "8+2 EC, 20 GB/s; CNode = 20 GB/s; DBox = 22 drives, ~6% EC overhead, 50 GB/s; DASE adds a fixed "
                            "back-end fabric cost. Data reduction ignored. Data: data/ch16_scaling.csv")
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    return _style.save(fig, out_dir, NAME)
