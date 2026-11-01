"""Ch04 — Illustrative worked example: raw -> usable -> effective capacity waterfall.

Reads data/ch04_capacity_waterfall.csv (24 x 61.44 TB QLC shelf; assumptions in the `source`
column). Writes docs/assets/charts/ch04-capacity-waterfall.svg.
"""
from __future__ import annotations

import csv
import textwrap
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch04_capacity_waterfall.csv"
NAME = "ch04-capacity-waterfall"


def build(out_dir: Path) -> Path:
    _style.apply()
    with CSV.open(newline="") as fh:
        rows = sorted(csv.DictReader(fh), key=lambda r: int(r["order"]))
    fig, ax = plt.subplots(figsize=(10.5, 4.8))
    level = 0.0
    for i, r in enumerate(rows):
        v = float(r["value"])
        if r["kind"] == "total":
            bottom, height = 0.0, v
            level = v if not r["step"].startswith("Effective") else level
            color = "#0072B2" if r["step"].startswith(("Raw", "Usable")) else "#56B4E9"
            if "claim" in r["step"]:
                color = "#E69F00"
        else:
            bottom, height = level + v, -v
            level = level + v
            color = "#D55E00"
        ax.bar(i, height, bottom=bottom, color=color, edgecolor="white", width=0.7)
        label = f"{v:+,.0f}" if r["kind"] == "delta" else f"{v:,.0f}"
        top = bottom + height
        ax.text(i, top + 70, label, ha="center", fontsize=9.5, color="#222222")
    ax.set_xticks(range(len(rows)))
    ax.set_xticklabels([textwrap.fill(r["step"], 13) for r in rows], fontsize=9)
    ax.set_ylabel("Capacity (TB for raw; TiB thereafter)")
    ax.set_ylim(0, 4800)
    ax.grid(axis="x", visible=False)
    ax.set_title("Illustrative worked example: one 24-drive QLC shelf, from raw to 'effective'",
                 loc="left", fontsize=13)
    _style.source_note(fig, "Illustrative, not vendor data. 24 × 61.44 TB drives; 1 TB = 0.9095 TiB; one drive-equivalent spare; "
                            "20+2 erasure coding; 8% metadata/system reserve. Effective = usable × assumed data-reduction ratio. "
                            "Data: data/ch04_capacity_waterfall.csv")
    fig.tight_layout()
    return _style.save(fig, out_dir, NAME)
