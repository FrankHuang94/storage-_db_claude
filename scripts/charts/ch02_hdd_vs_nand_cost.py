"""Ch02 — HDD vs enterprise SSD $/TB over time, and the SSD/HDD price premium.

Reads data/ch02_hdd_vs_nand_cost.csv. Panel A: sparse sourced $/TB points (log scale).
Panel B: SSD/HDD $/TB premium readings; single-vendor indices and company projections are
marked with distinct hollow markers. Writes docs/assets/charts/ch02-hdd-vs-nand-cost.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch02_hdd_vs_nand_cost.csv"
NAME = "ch02-hdd-vs-nand-cost"
SERIES_STYLE = {
    "HDD (Backblaze purchase price)": dict(color="#0072B2", marker="s", linestyle="-"),
    "Nearline HDD (market)": dict(color="#0072B2", marker="o", linestyle="--"),
    "Enterprise SSD (market)": dict(color="#D55E00", marker="o", linestyle="--"),
}


def _load() -> list[dict]:
    with CSV.open(newline="") as fh:
        return list(csv.DictReader(fh))


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.5, 4.8))
    # Panel A
    for name, st in SERIES_STYLE.items():
        pts = sorted((float(r["date"]), float(r["value"])) for r in rows
                     if r["panel"] == "usd_per_tb" and r["series"] == name)
        a1.plot([p[0] for p in pts], [p[1] for p in pts], label=name, linewidth=1.6, markersize=7, **st)
        for x, v in pts:
            a1.annotate(f"${v:,.0f}" if v >= 20 else f"${v:.1f}", (x, v), xytext=(4, 6), textcoords="offset points",
                        fontsize=9, color=st["color"])
    a1.set_yscale("log")
    a1.set_ylim(8, 2000)
    a1.set_xlim(2008, 2027.5)
    a1.set_ylabel("US$ per TB (log scale)")
    a1.set_title("A. Price per TB, sparse sourced points", fontsize=12, loc="left")
    a1.legend(loc="upper left", fontsize=9)
    # Panel B
    marks = {"sourced": ("o", "#222222", "#222222"), "search-summary only": ("o", "#222222", "white"),
             "single-vendor index": ("D", "#D55E00", "white"), "company-stated projection": ("^", "#0072B2", "white")}
    seen = set()
    pts = sorted((float(r["date"]), float(r["value"]), r["status"], r["period"]) for r in rows if r["panel"] == "premium")
    a2.plot([p[0] for p in pts if p[2] != "company-stated projection"],
            [p[1] for p in pts if p[2] != "company-stated projection"], color="#BBBBBB", linewidth=1, zorder=1)
    legend_names = {"sourced": "Market data (TrendForce via analyst)", "search-summary only": "Analyst chart (search summary only)",
                    "single-vendor index": "Single-vendor price index (VDURA)", "company-stated projection": "HDD vendor projection (Seagate)"}
    for x, v, stt, per in pts:
        m, ec, fc = marks[stt]
        a2.plot([x], [v], marker=m, markersize=8, markeredgecolor=ec, markerfacecolor=fc, linestyle="none", zorder=3,
                label=None if stt in seen else legend_names[stt])
        seen.add(stt)
        a2.annotate(f"{v:g}×\n{per}", (x, v), xytext=(5, 4), textcoords="offset points", fontsize=8.5, color="#333333")
    a2.set_ylim(0, 27)
    a2.set_xlim(2016.5, 2027.8)
    a2.set_ylabel("Enterprise SSD $/TB ÷ nearline HDD $/TB")
    a2.set_title("B. The flash premium fell to ~6–10×, then spiked", fontsize=12, loc="left")
    a2.legend(loc="upper left", fontsize=8.5)
    fig.suptitle("HDD vs enterprise flash: $/TB over time (mixed bases; read as direction, not precision)",
                 fontsize=13, fontweight="bold", x=0.01, ha="left")
    _style.source_note(fig, "Sources: Backblaze (2022) purchase prices; TrendForce via Wells Fargo/Blocks & Files (2019, 2020); Seagate via "
                            "Blocks & Files (2024, company projection); VDURA index via Forbes/PCSP and Hardware Busters (2026). Bases differ "
                            "(purchase vs contract vs index; QLC vs TLC). Data: data/ch02_hdd_vs_nand_cost.csv")
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    return _style.save(fig, out_dir, NAME)
