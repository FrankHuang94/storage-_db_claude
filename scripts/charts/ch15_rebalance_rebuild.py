"""Ch15 — Illustrative worked example: data movement on node add, and rebuild time on node loss.

Reads data/ch15_rebalance_rebuild.csv (generated from the chapter's stated assumptions; every row
carries `source` and `as_of`). Two panels: (A) % of data moved when one node is added, naive
hash-mod-N vs consistent hashing / CRUSH; (B) hours to rebuild one lost node vs cluster size for
two drive capacities. Writes docs/assets/charts/ch15-rebalance-rebuild.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch15_rebalance_rebuild.csv"
NAME = "ch15-rebalance-rebuild"
COLORS = {
    "Naive hash mod N": "#D55E00",
    "Consistent hashing or CRUSH": "#0072B2",
    "24 x 30.72 TB drives per node": "#009E73",
    "24 x 122.88 TB drives per node": "#CC79A7",
}


def _load() -> dict:
    series: dict = {}
    with CSV.open(newline="") as fh:
        for r in csv.DictReader(fh):
            key = (r["panel"], r["series"])
            series.setdefault(key, []).append((float(r["cluster_nodes"]), float(r["value"])))
    return series


def build(out_dir: Path) -> Path:
    _style.apply()
    s = _load()
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))

    ax = axes[0]
    for name in ("Naive hash mod N", "Consistent hashing or CRUSH"):
        pts = sorted(s[("A_data_moved", name)])
        ax.plot([p[0] for p in pts], [p[1] for p in pts], color=COLORS[name], marker="o",
                markersize=4, linewidth=2, label=name)
    ax.set_title("A. Data moved when one node is added", fontsize=12)
    ax.set_xlabel("Nodes before the add (N)")
    ax.set_ylabel("% of stored data that must move")
    ax.set_ylim(0, 100)
    ax.legend(loc="center right")

    ax = axes[1]
    for name in ("24 x 30.72 TB drives per node", "24 x 122.88 TB drives per node"):
        pts = sorted(s[("B_rebuild_hours", name)])
        ax.plot([p[0] for p in pts], [p[1] for p in pts], color=COLORS[name], marker="s",
                markersize=4, linewidth=2, label=name)
    ax.set_yscale("log")
    ax.axhline(24, color="#888888", linestyle=":", linewidth=1.2)
    ax.text(250, 26, "1 day", fontsize=9, color="#555555", ha="right", va="bottom")
    ax.set_title("B. Hours to rebuild one lost node (8+2 EC)", fontsize=12)
    ax.set_xlabel("Nodes in cluster")
    ax.set_ylabel("Hours (log scale)")
    ax.legend(loc="upper right")

    fig.suptitle("Illustrative worked example: placement math decides how much moves; cluster size decides how fast",
                 fontsize=13, fontweight="bold", x=0.01, ha="left")
    _style.source_note(fig, "Illustrative model, not vendor data. Panel B: node = 24 drives, 80% full; 8+2 erasure coding, so "
                            "each rebuilt strip reads 8 strips and writes 1 over the back-end; each surviving node donates "
                            "2 GB/s to rebuild. Data: data/ch15_rebalance_rebuild.csv")
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    return _style.save(fig, out_dir, NAME)
