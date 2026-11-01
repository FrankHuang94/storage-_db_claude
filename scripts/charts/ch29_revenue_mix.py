"""Ch29 — Everpure (formerly Pure Storage) revenue mix: product vs subscription services, FY2023–FY2026
plus the first half of FY2027.

Reads data/ch29_revenue_mix.csv (every row carries `source`, `as_of`, `verified`). Stacked bars in US$M,
with the subscription share of revenue labelled. The H1 FY2027 bar is half a year (Q1+Q2) and is
hatched so it is not read as a full year. Writes docs/assets/charts/ch29-revenue-mix.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

import _style

CSV = _style.DATA / "ch29_revenue_mix.csv"
NAME = "ch29-revenue-mix"
PRODUCT = "#0072B2"
SUBS = "#E69F00"


def _load() -> list[dict]:
    with CSV.open(newline="") as fh:
        return list(csv.DictReader(fh))


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    fig, ax = plt.subplots(figsize=(10, 5.2))
    for i, r in enumerate(rows):
        p, s = float(r["product_musd"]), float(r["subscription_musd"])
        half = r["period_type"].startswith("first half")
        hatch = "//" if half else None
        ax.bar(i, p, color=PRODUCT, hatch=hatch, edgecolor="white", linewidth=0.8)
        ax.bar(i, s, bottom=p, color=SUBS, hatch=hatch, edgecolor="white", linewidth=0.8)
        ax.text(i, p / 2, f"\\${p/1000:.2f}B", ha="center", va="center", color="white", fontsize=9, fontweight="bold")
        ax.text(i, p + s / 2, f"\\${s/1000:.2f}B", ha="center", va="center", color="#222222", fontsize=9)
        ax.text(i, p + s + 50, f"Subscription\n{s/(p+s)*100:.0f}% of revenue", ha="center", va="bottom",
                fontsize=8.5, color="#222222")
    ax.set_xticks(range(len(rows)))
    ax.set_xticklabels([r["period"] + ("\n(half year)" if r["period_type"].startswith("first half") else "")
                        for r in rows])
    ax.set_ylabel("Revenue (US$ millions)")
    ax.set_ylim(0, 5000)
    ax.grid(axis="x", visible=False)
    ax.text(1, 3350, "FY24: product falls 9% as\nEvergreen//One shifts sales\ninto ratable subscription",
            ha="center", fontsize=8.5, color="#555555")
    ax.text(4, 2900, "H1 FY27: product +54–55% YoY\n(price rises, large deals,\nhyperscale starts to ramp)",
            ha="center", fontsize=8.5, color="#555555")
    handles = [Patch(color=PRODUCT, label="Product (arrays, DFMs, hyperscale licence/royalty)"),
               Patch(color=SUBS, label="Subscription services (Evergreen, Evergreen//One, Pure1, Portworx, support)"),
               Patch(facecolor="white", edgecolor="#555555", hatch="//", label="Half year only: Q1+Q2 FY27, not comparable to full years")]
    ax.legend(handles=handles, loc="upper left", fontsize=8.5)
    ax.set_title("Everpure revenue mix by fiscal year: product vs subscription services, FY2023–H1 FY2027",
                 loc="left", fontsize=12.5)
    _style.source_note(fig, "Sources: Pure Storage / Everpure Form 10-K FY2024, FY2025, FY2026; Q1 and Q2 FY27 results releases "
                            "(2026-05-27, 2026-08-26). Fiscal years end near Feb 1 (FY2026 ended 2026-02-01). Figures taken from "
                            "search summaries of the filings; FY2025 subscription derived as total minus product; H1 FY27 rounded. "
                            "Data: data/ch29_revenue_mix.csv")
    fig.tight_layout()
    return _style.save(fig, out_dir, NAME)
