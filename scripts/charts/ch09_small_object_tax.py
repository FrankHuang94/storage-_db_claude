"""Ch09 — Illustrative worked example: the small-object tax on S3-style object storage.

Reads data/ch09_small_object_tax.csv (derived from public S3 Standard GET pricing and the baseline
per-prefix request rate; every row carries `source` and `as_of`). Two log-scale bar panels:
(A) GET request cost to read 1 PB once, by object size; (B) partitioned prefixes needed to read
1 PB in one hour at 5,500 GET/s per prefix. Writes docs/assets/charts/ch09-small-object-tax.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch09_small_object_tax.csv"
NAME = "ch09-small-object-tax"


def _load() -> list[dict]:
    with CSV.open(newline="") as fh:
        return list(csv.DictReader(fh))


def _fmt(v: float, money: bool) -> str:
    if money:
        return f"${v:,.0f}" if v >= 10 else f"${v:,.2f}"
    return f"{v:,.0f}" if v >= 10 else f"{v:.1f}"


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    labels = [r["object_size"] for r in rows]
    cost = [float(r["get_cost_usd_to_read_1pb"]) for r in rows]
    pref = [float(r["prefixes_to_read_1pb_in_1h"]) for r in rows]

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))
    panels = [
        (axes[0], cost, "A. GET request cost to read 1 PB once", "US$ (log scale)", "#D55E00", True),
        (axes[1], pref, "B. Prefixes needed to read 1 PB in 1 hour", "Partitioned prefixes (log scale)", "#0072B2", False),
    ]
    for ax, vals, title, ylabel, color, money in panels:
        bars = ax.bar(labels, vals, color=color, width=0.6)
        ax.set_yscale("log")
        ax.set_title(title, fontsize=12)
        ax.set_xlabel("Object size")
        ax.set_ylabel(ylabel)
        ax.grid(axis="x", visible=False)
        for b, v in zip(bars, vals):
            ax.text(b.get_x() + b.get_width() / 2, v * 1.25, _fmt(v, money), ha="center", va="bottom", fontsize=9)
        ax.set_ylim(top=max(vals) * 8)
    fig.suptitle("Illustrative worked example: per-request pricing and per-prefix limits punish small objects",
                 fontsize=13, fontweight="bold", x=0.01, ha="left")
    _style.source_note(fig, "Illustrative arithmetic, not a measurement. 1 PB = 1e15 bytes, one GET per object; S3 Standard GET "
                            "$0.0004 per 1,000 requests; baseline 5,500 GET/s per partitioned prefix (1 PB/hour = ~278 GB/s). "
                            "Data: data/ch09_small_object_tax.csv")
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    return _style.save(fig, out_dir, NAME)
