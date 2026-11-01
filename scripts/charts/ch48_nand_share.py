"""Ch48 — NAND supplier share, 2Q26: revenue share (TrendForce) vs bit-shipment share (Counterpoint).

Reads data/ch48_nand_share.csv (every row carries `source`, `as_of`, `verified`). Two horizontal-bar
panels: left = share of NAND brand revenue (TrendForce, top five plus a derived "all others"),
right = share of NAND bits shipped (Counterpoint). The contrast shows YMTC is a top-three bit
shipper but sits outside the top five by revenue. Writes docs/assets/charts/ch48-nand-share.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch48_nand_share.csv"
NAME = "ch48-nand-share"
COLORS = {
    "Samsung": "#0072B2", "SK hynix": "#E69F00", "Micron": "#009E73", "Kioxia": "#CC79A7",
    "Sandisk": "#D55E00", "YMTC": "#56B4E9", "All others": "#999999",
}


def _color(name: str) -> str:
    for k, v in COLORS.items():
        if name.startswith(k):
            return v
    return "#999999"


def _load() -> list[dict]:
    with CSV.open(newline="") as fh:
        return list(csv.DictReader(fh))


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.0), sharex=True)
    panels = [("revenue", "Share of NAND revenue, 2Q26 (TrendForce)"),
              ("bits", "Share of NAND bits shipped, 2Q26 (Counterpoint)")]
    for ax, (panel, title) in zip(axes, panels):
        sub = [r for r in rows if r["panel"] == panel]
        names = [r["supplier"] for r in sub]
        vals = [float(r["share_pct"]) for r in sub]
        y = list(range(len(sub)))[::-1]
        derived = [r["verified"] == "derived" for r in sub]
        ax.barh(y, vals, color=[_color(n) for n in names],
                hatch=["//" if d else None for d in derived], edgecolor="white")
        for yi, v, r in zip(y, vals, sub):
            label = f"{v:.1f}%" if panel == "revenue" else f"{v:.0f}%"
            if r["revenue_usd_b"]:
                label += f"  (\\${float(r['revenue_usd_b']):.2f}B, +{float(r['qoq_pct']):.0f}% QoQ)"
            ax.text(v + 0.6, yi, label, va="center", fontsize=8.5, color="#222222")
        ax.set_yticks(y)
        ax.set_yticklabels(names, fontsize=9.5)
        ax.set_xlim(0, 48)
        ax.set_xlabel("Share (%)")
        ax.grid(axis="y", visible=False)
        ax.set_title(title, loc="left", fontsize=11.5)
    fig.suptitle("NAND supplier share, 2Q26: Samsung leads both ways; YMTC is #3 by bits but outside the top five by revenue",
                 x=0.01, ha="left", fontsize=12, fontweight="bold")
    _style.source_note(fig, "Sources: TrendForce, 'Combined Revenue of Top Five NAND Flash Brands Rises 77% QoQ in 2Q26', 2026-08-18 "
                            "(top-five revenue \\$68.87B; 'All others' is derived as 100% minus top five, hatched). Counterpoint Research, "
                            "'Server-led eSSDs hit 48% of NAND shipments', 2026, via search summaries and Herald Corp coverage "
                            "(residual 1% derived). Figures read from search summaries, not the full releases. Data: data/ch48_nand_share.csv")
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    return _style.save(fig, out_dir, NAME)
