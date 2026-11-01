"""Ch51 — Long-run US$ per GB for hard disks and flash, 1956-2026 (log scale).

Reads data/ch51_cost_per_gb.csv: sparse, individually sourced price points (nominal US$).
Filled markers = fetched or corroborated sources; hollow = search-summary only;
diamonds = single-vendor price index. Thin connecting lines are visual guides only,
because the bases differ (list price, purchase price, retail, contract, index).
Writes docs/assets/charts/ch51-cost-per-gb.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch51_cost_per_gb.csv"
NAME = "ch51-cost-per-gb"
COLORS = {"HDD": "#0072B2", "Flash": "#D55E00"}
LABEL_OFFSETS = {
    "IBM 350 RAMAC": (8, -4),
    "IBM 3380 mainframe DASD": (-30, 10),
    "Small-system disk drives (approx.)": (8, 4),
    "IBM 3380 (RAID paper Table I)": (-118, 6),
    "Conners CP3100 PC disk (RAID paper Table I)": (8, -14),
    "Lowest retail price (PriceWatch)": (-40, -16),
    "SunDisk 20 MB flash drive for IBM": (8, 4),
    "Intel X25-M 80 GB SSD": (-120, 4),
    "MLC NAND contract price (component)": (-150, -16),
    "Median consumer SSD": (8, 6),
    "Enterprise SSD (market)": (-120, 6),
    "30 TB TLC enterprise SSD (VDURA index)": (-150, 10),
    "30 TB nearline HDD (VDURA index)": (-150, 8),
}
SHORT = {
    "IBM 350 RAMAC": "RAMAC 1956",
    "IBM 3380 mainframe DASD": "IBM 3380 list, 1980",
    "Small-system disk drives (approx.)": "small drives ~1981",
    "IBM 3380 (RAID paper Table I)": "3380 in RAID paper, 1988",
    "Conners CP3100 PC disk (RAID paper Table I)": "PC disk in RAID paper, 1988",
    "Lowest retail price (PriceWatch)": "\\$1/GB retail, 2003",
    "Backblaze purchase price": None,
    "SunDisk 20 MB flash drive for IBM": "SunDisk 20 MB, 1991",
    "Intel X25-M 80 GB SSD": "Intel X25-M, 2008",
    "MLC NAND contract price (component)": "NAND chips, Q4 2008",
    "Median consumer SSD": "consumer SSD median, 2012",
    "Enterprise SSD (market)": "enterprise SSD, 2020",
    "30 TB TLC enterprise SSD (VDURA index)": "enterprise SSD index, Q3 2026",
    "30 TB nearline HDD (VDURA index)": "nearline HDD index, Q3 2026",
}


def _fmt(v: float) -> str:
    if v >= 1000:
        return f"\\${v:,.0f}"
    if v >= 1:
        return f"\\${v:.2f}".rstrip("0").rstrip(".")
    return f"\\${v:.3g}"


def build(out_dir: Path) -> Path:
    _style.apply()
    with CSV.open(newline="") as fh:
        rows = list(csv.DictReader(fh))
    fig, ax = plt.subplots(figsize=(11.5, 6.4))
    for series, color in COLORS.items():
        pts = sorted((float(r["year"]), float(r["usd_per_gb"]), r["status"], r["product"])
                     for r in rows if r["series"] == series)
        ax.plot([p[0] for p in pts], [p[1] for p in pts], color=color, linewidth=0.9, linestyle=":", alpha=0.7)
        first = True
        for x, v, status, product in pts:
            marker = "D" if status == "single-vendor index" else "o"
            face = color if status == "sourced" else "white"
            ax.plot([x], [v], marker=marker, markersize=8, markeredgecolor=color, markerfacecolor=face,
                    markeredgewidth=1.6, linestyle="none", zorder=3,
                    label=("Hard disk" if series == "HDD" else "Flash / SSD") if first else None)
            first = False
            short = SHORT.get(product, product)
            text = f"{short}: {_fmt(v)}" if short else _fmt(v)
            ax.annotate(text, (x, v), xytext=LABEL_OFFSETS.get(product, (6, 5)), textcoords="offset points",
                        fontsize=8.5, color=color)
    ax.set_yscale("log")
    ax.set_ylim(0.005, 5e7)
    ax.set_xlim(1953, 2029)
    ax.set_ylabel("US\\$ per GB, nominal (log scale)")
    ax.set_xlabel("Year")
    # marker legend
    ax.plot([], [], marker="o", color="#555555", markerfacecolor="#555555", linestyle="none", label="Sourced (fetched or corroborated)")
    ax.plot([], [], marker="o", color="#555555", markerfacecolor="white", linestyle="none", label="Search-summary only")
    ax.plot([], [], marker="D", color="#555555", markerfacecolor="white", linestyle="none", label="Single-vendor price index")
    ax.legend(loc="upper right", fontsize=9)
    ax.text(1954, 0.009, "Dotted lines are visual guides only: bases differ (list, purchase, retail, contract, index).\n"
                         "HDD fell ~8.8 orders of magnitude 1956-2022 (about 26% a year); 2026 shows a reversal.",
            fontsize=8.5, color="#555555")
    fig.suptitle("Seventy years of storage cost: US\\$ per GB, hard disk and flash (sparse sourced points)",
                 fontsize=13, fontweight="bold", x=0.01, ha="left")
    _style.source_note(fig, "Sources: History of Information (RAMAC); MSDN/StorageNewsletter (IBM 3380); Backblaze (1981 approx., "
                            "2009-2022); Patterson-Gibson-Katz SIGMOD 1988 Table I; Slashdot/PriceWatch (2003); ETHW/Computer Hope "
                            "(SunDisk); TechCrunch (X25-M); MacTech (NAND 2008); TechSpot (2012); TrendForce via Blocks & Files (2020); "
                            "VDURA index via Hardware Busters (2026). Nominal dollars, not inflation-adjusted. Data: data/ch51_cost_per_gb.csv")
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    return _style.save(fig, out_dir, NAME)
