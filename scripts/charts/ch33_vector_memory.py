"""Ch33 — Worked example: where 1 billion 1024-dim vectors live under four index designs.

Reads data/ch33_vector_memory.csv (worked-example arithmetic; every row carries `source` and `as_of`).
Left panel: gigabytes in DRAM vs SSD per design. Right panel: media cost per index replica at 2026
prices. Writes docs/assets/charts/ch33-vector-memory.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch33_vector_memory.csv"
NAME = "ch33-vector-memory"
TIER_COLORS = {"DRAM": "#D55E00", "SSD": "#0072B2"}


def _load():
    designs: list[str] = []
    data: dict = {}
    with CSV.open(newline="") as fh:
        for r in csv.DictReader(fh):
            if r["design"] not in designs:
                designs.append(r["design"])
            data[(r["design"], r["tier"])] = (float(r["gigabytes"]), float(r["usd"]))
    return designs, data


def build(out_dir: Path) -> Path:
    _style.apply()
    designs, data = _load()
    labels = [d.replace(" + ", "\n+ ").replace(": ", ":\n") for d in designs]
    y = list(range(len(designs)))[::-1]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.8), sharey=True)
    h = 0.38
    for i, tier in enumerate(("DRAM", "SSD")):
        gb = [data[(d, tier)][0] for d in designs]
        ax1.barh([v + (h / 2 if tier == "DRAM" else -h / 2) for v in y], gb, height=h,
                 color=TIER_COLORS[tier], label=tier)
        for yy, g in zip(y, gb):
            ax1.text(g * 1.08, yy + (h / 2 if tier == "DRAM" else -h / 2), f"{g:,.0f} GB",
                     va="center", fontsize=9, color="#222222")
    ax1.set_xscale("log")
    ax1.set_xlim(30, 30000)
    ax1.set_yticks(y)
    ax1.set_yticklabels(labels, fontsize=10)
    ax1.set_xlabel("Gigabytes per index replica (log scale)")
    ax1.set_title("Bytes by tier", fontsize=12)

    left = [0.0] * len(designs)
    for tier in ("DRAM", "SSD"):
        usd = [data[(d, tier)][1] / 1000 for d in designs]
        ax2.barh(y, usd, left=left, height=0.55, color=TIER_COLORS[tier], label=tier)
        left = [a + b for a, b in zip(left, usd)]
    for yy, tot in zip(y, left):
        ax2.text(tot + 1, yy, f"${tot:,.1f}k", va="center", fontsize=10, color="#222222")
    ax2.set_xlim(0, 80)
    ax2.set_xlabel("Media cost per replica, US$ thousands (2026 prices)")
    ax2.set_title("Media cost", fontsize=12)
    ax2.legend(loc="lower right")
    fig.suptitle("Worked example: 1 billion 1024-dim vectors (4.1 TB raw fp32), placed four ways",
                 fontsize=13, fontweight="bold", x=0.01, ha="left")
    _style.source_note(fig, "Worked example, not vendor data. HNSW M=32 (264 B/vector graph); PQ 64 B/vector; DiskANN node = "
                            "4,096 B vector + 64 x 4 B neighbours. DRAM ~$14.5/GB (Counterpoint, 1Q26); enterprise SSD ~$0.75/GB "
                            "(Hardware Busters index, Q3 2026). Excludes CPUs, replicas, networking. Data: data/ch33_vector_memory.csv")
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    return _style.save(fig, out_dir, NAME)
