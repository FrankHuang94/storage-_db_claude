"""Ch43 — WEKA funding by round (bars, primary vs secondary) with cumulative total (line), plus
latest private valuations of WEKA, DDN and VAST Data (right panel).

Reads data/ch43_funding.csv (every row carries `label`, `source`, `as_of`). Writes
docs/assets/charts/ch43-funding.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch43_funding.csv"
NAME = "ch43-funding"
WEKA = _style.VENDOR_COLORS["WEKA"]


def _load() -> list[dict]:
    with CSV.open(newline="") as fh:
        return list(csv.DictReader(fh))


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    rounds = [r for r in rows if r["series"] == "WEKA"]
    comps = [r for r in rows if r["series"] == "Comparator"]
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(11.5, 5.2), gridspec_kw={"width_ratios": [2.1, 1]})

    xs = list(range(len(rounds)))
    prim = [float(r["primary_usd_m"]) for r in rounds]
    sec = [float(r["secondary_usd_m"]) for r in rounds]
    ax.bar(xs, prim, color=WEKA, width=0.6, label="Primary capital (to the company)")
    sx = [(x, s_, p_) for x, s_, p_ in zip(xs, sec, prim) if s_ > 0]
    ax.bar([t[0] for t in sx], [t[1] for t in sx], bottom=[t[2] for t in sx], color="#F0E442",
           edgecolor="#222222", linewidth=0.6, width=0.6, hatch="//", label="Secondary (employee share sales)")
    cum, run = [], 0.0
    for r in rounds:
        run += float(r["amount_usd_m"])
        cum.append(run)
    ax.plot(xs, cum, color="#D55E00", marker="o", linewidth=2, label="Cumulative raised")
    for x, r, c in zip(xs, rounds, cum):
        amt = float(r["amount_usd_m"])
        tag = f"\\${amt:.0f}M"
        if r["post_money_usd_b"]:
            tag += f"\n@ \\${float(r['post_money_usd_b']):.2f}B".replace(".60B", ".6B").replace(".75B", ".75B")
        ax.text(x, amt + 6, tag, ha="center", va="bottom", fontsize=9)
        if x == 0:
            continue
        ax.annotate(f"\\${c:.0f}M", (x, c), textcoords="offset points", xytext=(14, -4), fontsize=8.5,
                    color="#D55E00")
    labels = []
    for r in rounds:
        lab = r["round"].replace(" (label disputed)", "*").replace("Pre-Series C rounds (seed, A, B), implied",
                                                                    "Pre-C rounds\n(implied)")
        labels.append(f"{lab}\n{r['date']}")
    ax.set_xticks(xs)
    ax.set_xticklabels(labels, fontsize=8.5)
    ax.set_ylabel("US$ millions")
    ax.set_ylim(0, 480)
    ax.grid(axis="x", visible=False)
    ax.legend(loc="upper left", fontsize=8.5)
    ax.set_title("WEKA capital raised by round (company-stated and press-reported)", loc="left", fontsize=12)

    names = [r["round"].replace(" latest priced round", "\n(May 2024)").replace(" (Blackstone minority investment)",
             "\n(Jan 2025)").replace(" Series F", "\n(Apr 2026)") for r in comps]
    vals = [float(r["post_money_usd_b"]) for r in comps]
    cols = [WEKA, _style.VENDOR_COLORS["DDN"], _style.VENDOR_COLORS["VAST"]]
    bx.bar(range(len(vals)), vals, color=cols, width=0.6)
    for i, v in enumerate(vals):
        bx.text(i, v + 0.5, f"\\${v:g}B", ha="center", fontsize=10, fontweight="bold")
    bx.set_xticks(range(len(vals)))
    bx.set_xticklabels(names, fontsize=8.5)
    bx.set_ylabel("Post-money valuation, US$ billions")
    bx.set_ylim(0, 34)
    bx.grid(axis="x", visible=False)
    bx.set_title("Latest private valuations", loc="left", fontsize=12)

    _style.source_note(fig, "Sources: WEKA Series E release (2024-05-15); StorageNewsletter (2019-05-15); Blocks & Files "
                            "(2022-01-04); SiliconANGLE and Calcalist (2022-11); Blackstone (2025-01-09); CNBC (2026-04-22). "
                            "Series D valuation reported by press, not disclosed by WEKA. *Jan 2022 round label disputed "
                            "(Series C extension vs D). Pre-C bar derived from the company-stated US$66.7M total after the "
                            "Series C. No later WEKA priced round found as of 2026-11-01. Data: data/ch43_funding.csv")
    fig.tight_layout()
    return _style.save(fig, out_dir, NAME)
