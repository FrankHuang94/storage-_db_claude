"""Ch42 — VAST Data funding rounds: amount raised (bars) and post-money valuation (log-scale markers).

Reads data/ch42_funding.csv (every row carries `label` = company-stated / reported, plus `source`, `as_of`).
Company-stated figures are solid; press-reported figures are hatched or hollow. Writes
docs/assets/charts/ch42-funding.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

import _style

CSV = _style.DATA / "ch42_funding.csv"
NAME = "ch42-funding"
VAST = _style.VENDOR_COLORS["VAST"]
ACCENT = "#D55E00"


def _load() -> list[dict]:
    with CSV.open(newline="") as fh:
        return list(csv.DictReader(fh))


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    xs = list(range(len(rows)))
    labels = [f"{r['round'].split(' (')[0]}\n{r['date']}" for r in rows]

    # Panel A: amount raised
    for x, r in zip(xs, rows):
        stated = r["label"] == "company-stated"
        if not r["amount_usd_m"]:
            ax1.text(x, 30, "amount\nn/a", ha="center", va="bottom", fontsize=8.5, color="#555555")
            continue
        v = float(r["amount_usd_m"])
        ax1.bar(x, v, color=VAST if stated else "white", edgecolor=VAST, hatch=None if stated else "//",
                linewidth=1.4, width=0.62)
        ax1.text(x, v + 18, f"\\${v:,.0f}M", ha="center", va="bottom", fontsize=9, color=_style.TEXT)
    ax1.set_xticks(xs)
    ax1.set_xticklabels(labels, fontsize=8.5)
    ax1.set_ylabel("Amount raised (US$ millions)")
    ax1.set_ylim(0, 1150)
    ax1.grid(axis="x", visible=False)
    ax1.set_title("A. Amount raised per round", loc="left", fontsize=12)
    ax1.text(5, 560, "~half secondary\n(reported)", ha="center", fontsize=8.5, color="#333333")

    # Panel B: valuation, log scale
    pts = [(x, float(r["valuation_usd_b"]), r["label"]) for x, r in zip(xs, rows) if r["valuation_usd_b"]]
    ax2.plot([p[0] for p in pts], [p[1] for p in pts], color="#999999", linewidth=1.2, zorder=1)
    for x, v, lab in pts:
        stated = lab == "company-stated"
        ax2.scatter(x, v, s=90, zorder=2, color=VAST if stated else "white", edgecolor=VAST, linewidth=1.8)
        ax2.annotate(f"\\${v:g}B", (x, v), textcoords="offset points", xytext=(0, 10), ha="center", fontsize=9.5)
    ax2.set_yscale("log")
    ax2.set_ylim(0.5, 80)
    ax2.set_yticks([1, 3, 10, 30])
    ax2.set_yticklabels(["\\$1B", "\\$3B", "\\$10B", "\\$30B"])
    ax2.set_xticks(xs)
    ax2.set_xticklabels(labels, fontsize=8.5)
    ax2.set_xlim(-0.5, len(rows) - 0.5)
    ax2.set_ylabel("Post-money valuation (US$, log scale)")
    ax2.grid(axis="x", visible=False)
    ax2.set_title("B. Valuation: ~25x in six years", loc="left", fontsize=12)
    ax2.text(0, 0.62, "valuation\nnot disclosed", ha="center", fontsize=8.5, color="#555555")

    handles = [Patch(color=VAST, label="Company-stated"),
               Patch(facecolor="white", edgecolor=VAST, hatch="//", label="Reported by press"),
               Line2D([0], [0], marker="o", color="white", markeredgecolor=VAST, markerfacecolor="white",
                      markersize=9, label="Reported valuation (talks, Feb 2026: US$25-27B midpoint)")]
    fig.legend(handles=handles, loc="upper center", ncol=3, fontsize=9, bbox_to_anchor=(0.5, 0.99))
    fig.suptitle("VAST Data funding rounds and valuations, 2019-2026", x=0.01, ha="left", y=1.06,
                 fontsize=13, fontweight="bold")
    _style.source_note(fig, "Sources: VAST Data press releases; StorageNewsletter 2021-05-05; Blocks & Files 2023-12-06 and "
                            "2026-02-05; Crunchbase News 2020-04; Bloomberg and CNBC 2026-04. Series A and early investor "
                            "attribution omitted (unconfirmed). Series F amount (~US$1B) includes a secondary tender, so it is "
                            "not all new capital. Data: data/ch42_funding.csv")
    fig.tight_layout()
    return _style.save(fig, out_dir, NAME)
