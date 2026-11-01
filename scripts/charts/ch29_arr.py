"""Ch29 — Everpure subscription ARR (bars) and remaining performance obligations (line), fiscal
period-ends FY2023–Q2 FY2027.

Reads data/ch29_arr.csv (every row carries `source`, `as_of`, `verified`). ARR in US$B on the left axis;
RPO in US$B on the right axis. Writes docs/assets/charts/ch29-arr.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch29_arr.csv"
NAME = "ch29-arr"
BLUE = "#0072B2"
ACCENT = "#D55E00"


def _load() -> list[dict]:
    with CSV.open(newline="") as fh:
        return list(csv.DictReader(fh))


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    fig, ax = plt.subplots(figsize=(10, 5))
    xs = list(range(len(rows)))
    arr = [float(r["subscription_arr_musd"]) / 1000 for r in rows]
    ax.bar(xs, arr, color=BLUE, width=0.6, label="Subscription ARR (left axis)")
    for x, v in zip(xs, arr):
        lab = f"\\${v:.2f}B"
        ax.text(x, v - 0.06, lab, ha="center", va="top", fontsize=9, color="white", fontweight="bold")
    ax.set_ylabel("Subscription ARR (US$ billions)")
    ax.set_ylim(0, 3.0)
    ax.set_xticks(xs)
    ax.set_xticklabels([r["period"].replace(" end", "\nend") for r in rows], fontsize=9)
    ax.grid(axis="x", visible=False)
    ax2 = ax.twinx()
    pts = [(x, float(r["rpo_busd"])) for x, r in zip(xs, rows) if r["rpo_busd"]]
    ax2.plot([p[0] for p in pts], [p[1] for p in pts], color=ACCENT, marker="o", linewidth=2.2,
             label="Remaining performance obligations, RPO (right axis)")
    for x, v in pts:
        ax2.annotate(f"\\${v:.1f}B", (x, v), textcoords="offset points", xytext=(0, 9), ha="center",
                     fontsize=9, color=ACCENT)
    ax2.set_ylim(0, 5.0)
    ax2.set_yticks([0, 1, 2, 3, 4, 5])
    ax2.set_ylabel("RPO (US$ billions)", color=ACCENT)
    ax2.spines["right"].set_visible(True)
    ax2.grid(False)
    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=9)
    ax.set_title("Everpure subscription ARR and RPO at fiscal period-ends, FY2023–Q2 FY2027",
                 loc="left", fontsize=12.5)
    _style.source_note(fig, "Sources: Pure Storage / Everpure Form 10-K FY2024–FY2026, Q4 FY25 results (8-K Ex. 99.1), Q1 and Q2 FY27 "
                            "results releases. ARR = annualised value of active subscriptions + quarterly on-demand revenue x4 "
                            "(company definition). Period-ends are fiscal (FY2026 ended 2026-02-01; Q2 FY27 ended 2026-08-02). "
                            "Figures from search summaries of the filings; Q2 FY27 ARR rounded. FY2023 RPO not charted. "
                            "Data: data/ch29_arr.csv")
    fig.tight_layout()
    return _style.save(fig, out_dir, NAME)
