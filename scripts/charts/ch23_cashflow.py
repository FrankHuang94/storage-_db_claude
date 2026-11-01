"""Ch23 — Illustrative worked example: five-year customer cash outflows under capex purchase,
operating lease and storage-as-a-service (STaaS).

Reads data/ch23_cashflow.csv (generated from the chapter's stated assumptions; every row carries
`source` and `as_of`). Panel A: annual cash outflow by model (grouped bars). Panel B: cumulative
outflow (lines). Writes docs/assets/charts/ch23-cashflow.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch23_cashflow.csv"
NAME = "ch23-cashflow"
MODELS = ["Capex purchase", "Operating lease", "STaaS subscription"]
COLORS = {"Capex purchase": "#E69F00", "Operating lease": "#009E73", "STaaS subscription": "#0072B2"}
LABEL_DY = {"Capex purchase": -14, "Operating lease": 0, "STaaS subscription": 8}
MARKERS = {"Capex purchase": "o", "Operating lease": "s", "STaaS subscription": "^"}


def _load() -> dict:
    data: dict = {m: [] for m in MODELS}
    with CSV.open(newline="") as fh:
        for r in csv.DictReader(fh):
            data[r["model"]].append((int(r["year"]), float(r["total_outflow_k"])))
    return {m: sorted(v) for m, v in data.items()}


def build(out_dir: Path) -> Path:
    _style.apply()
    d = _load()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.6))
    width = 0.27
    for i, m in enumerate(MODELS):
        years = [y for y, _ in d[m]]
        vals = [v for _, v in d[m]]
        ax1.bar([y + (i - 1) * width for y in years], vals, width=width, color=COLORS[m], label=m)
        cum, run = [], 0.0
        for v in vals:
            run += v
            cum.append(run)
        ax2.plot(years, cum, color=COLORS[m], marker=MARKERS[m], linewidth=2, markersize=5, label=m)
        ax2.annotate(f"\\${cum[-1]:,.0f}K", (years[-1], cum[-1]), textcoords="offset points", xytext=(6, LABEL_DY[m]),
                     fontsize=9, color=COLORS[m])
    ax1.set_title("A. Annual cash outflow", fontsize=12)
    ax1.set_xlabel("Year")
    ax1.set_ylabel("US$ thousands")
    ax1.set_xticks(range(1, 6))
    ax1.legend(loc="upper right")
    ax2.set_title("B. Cumulative cash outflow", fontsize=12)
    ax2.set_xlabel("Year")
    ax2.set_xticks(range(1, 6))
    ax2.set_xlim(0.8, 5.8)
    ax2.set_ylim(bottom=0)
    fig.suptitle("Illustrative worked example: same storage, three cash-flow shapes (1 PB growing 20%/yr)",
                 fontsize=13, fontweight="bold", x=0.01, ha="left")
    _style.source_note(fig, "Illustrative model, not vendor pricing. Capex: 1.5 PB at \\$400K/PB in yr 1, 0.6 PB expansion in yr 4 "
                            "(prices -15%/yr), support 12%/yr. Lease: same hardware financed at 7%, plus support. STaaS: "
                            "\\$144K per PB-year on actual usage, refresh included. Power, tax and residual value ignored. "
                            "Data: data/ch23_cashflow.csv")
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    return _style.save(fig, out_dir, NAME)
