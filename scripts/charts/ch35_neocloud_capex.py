"""Ch35 — Neocloud capital expenditure versus the largest disclosed neocloud storage contract.

Reads data/ch35_neocloud_capex.csv (every row carries `source`, `as_of` and a `verified` flag).
Horizontal bars: actual capex (solid), guidance (hatched, with low–high range), and the
VAST–CoreWeave contract total for scale. Rows taken only from search summaries carry a dagger.
Writes docs/assets/charts/ch35-neocloud-capex.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

import _style

CSV = _style.DATA / "ch35_neocloud_capex.csv"
NAME = "ch35-neocloud-capex"
GREY = "#999999"
SKY = "#56B4E9"
VAST = _style.VENDOR_COLORS["VAST"]


def _load() -> list[dict]:
    with CSV.open(newline="") as fh:
        return list(csv.DictReader(fh))


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    fig, ax = plt.subplots(figsize=(10.5, 4.6))
    labels = []
    for i, r in enumerate(rows):
        lo, hi = float(r["low_busd"]), float(r["high_busd"])
        mid = (lo + hi) / 2
        kind = r["kind"]
        if kind == "guidance":
            ax.barh(i, mid, color="white", edgecolor=SKY, hatch="//", linewidth=1.5)
            ax.errorbar(mid, i, xerr=[[mid - lo], [hi - mid]], color="#0072B2", capsize=5, linewidth=1.5)
            txt = f"${lo:.0f}–{hi:.0f}B"
            x = hi
        elif kind == "contract":
            ax.barh(i, mid, color=VAST)
            txt = f"\\${mid:.2f}B total ≈ \\$0.23–0.39B a year"
            x = mid
        else:
            ax.barh(i, mid, color=GREY if r["company"] == "Oracle" else SKY)
            txt = f"${mid:.1f}B"
            x = mid
        ax.text(x + 0.8, i, txt, va="center", fontsize=9.5, color="#222222")
        lab = r["label"]
        if r["verified"].startswith("search-summary"):
            lab += " †"
        labels.append(lab)
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels(labels, fontsize=9.5)
    ax.invert_yaxis()
    ax.set_xlim(0, 68)
    ax.set_xlabel("US$ billions")
    ax.grid(axis="y", visible=False)
    handles = [Patch(color=SKY, label="Neocloud capex, actual"), Patch(color=GREY, label="Oracle (quasi-neocloud), actual"),
               Patch(facecolor="white", edgecolor=SKY, hatch="//", label="Guidance midpoint, range bar"),
               Patch(color=VAST, label="Largest disclosed storage contract")]
    ax.legend(handles=handles, loc="lower right", fontsize=9)
    ax.set_title("Neocloud capex versus the largest disclosed neocloud storage contract",
                 loc="left", fontsize=12.5)
    _style.source_note(fig, "Sources: CoreWeave and Nebius results coverage (Aug 2026); Oracle FY2026 results coverage; "
                            "StorageNewsletter 2025-11-07 (VAST, company-stated total; 3–5-year term is VAST's stated typical range, "
                            "annualised here). † = from search summaries, not checked against the filing. Oracle's fiscal year ends in May. "
                            "Data: data/ch35_neocloud_capex.csv")
    fig.tight_layout()
    return _style.save(fig, out_dir, NAME)
