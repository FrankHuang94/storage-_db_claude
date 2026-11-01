"""Ch41 — AI-native storage vendors: reported valuations over time and headline valuation multiples.

Reads data/ch41_valuations.csv (`series` = valuation | multiple; `label` = company-stated / reported / worked;
plus `source`, `as_of`). Panel A plots post-money valuations on a log scale (solid = company-stated,
hollow = reported by press). Panel B shows worked valuation / revenue-signal multiples. Writes
docs/assets/charts/ch41-valuations.svg.
"""
from __future__ import annotations

import csv
from datetime import date
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

import _style

CSV = _style.DATA / "ch41_valuations.csv"
NAME = "ch41-valuations"
COLORS = {"VAST": _style.VENDOR_COLORS["VAST"], "WEKA": _style.VENDOR_COLORS["WEKA"], "DDN": _style.VENDOR_COLORS["DDN"]}


def _load() -> list[dict]:
    with CSV.open(newline="") as fh:
        return list(csv.DictReader(fh))


def _to_year(s: str) -> float:
    y, m = s.split("-")[:2]
    return int(y) + (int(m) - 0.5) / 12


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    vals = [r for r in rows if r["series"] == "valuation"]
    mults = [r for r in rows if r["series"] == "multiple"]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), gridspec_kw={"width_ratios": [1.25, 1]})

    # Panel A: valuations over time
    for co, color in COLORS.items():
        pts = sorted(((_to_year(r["date"]), float(r["valuation_usd_b"]), r["label"]) for r in vals if r["company"] == co))
        ax1.plot([p[0] for p in pts], [p[1] for p in pts], color=color, linewidth=1.4, zorder=1)
        for x, v, lab in pts:
            stated = lab == "company-stated"
            ax1.scatter(x, v, s=80, zorder=2, color=color if stated else "white", edgecolor=color, linewidth=1.8)
            ax1.annotate(f"\\${v:g}B", (x, v), textcoords="offset points", xytext=(0, 9) if stated else (-16, -16), ha="center", fontsize=9)
        ax1.text(pts[-1][0] + 0.15, pts[-1][1], co, color=color, fontsize=11, fontweight="bold", va="center")
    ax1.set_yscale("log")
    ax1.set_ylim(0.4, 80)
    ax1.set_yticks([0.5, 1, 3, 10, 30])
    ax1.set_yticklabels(["\\$0.5B", "\\$1B", "\\$3B", "\\$10B", "\\$30B"])
    ax1.set_xlim(2019.8, 2027.2)
    ax1.set_xticks(range(2020, 2027))
    ax1.set_ylabel("Post-money valuation (US$, log scale)")
    ax1.set_title("A. Last priced valuations, 2020-2026", loc="left", fontsize=12)

    # Panel B: headline multiples
    labels = [f"{r['company']} {r['date'][:4]}\n{r['event'].split(' / ')[1]}" for r in mults]
    ys = list(range(len(mults)))[::-1]
    for y, r in zip(ys, mults):
        m = float(r["multiple_x"])
        ax2.barh(y, m, color=COLORS[r["company"]], height=0.6)
        ax2.text(m + 1, y, f"{m:g}x", va="center", fontsize=10)
    ax2.set_yticks(ys)
    ax2.set_yticklabels(labels, fontsize=9)
    ax2.set_xlim(0, 72)
    ax2.set_xlabel("Valuation / revenue signal (x)")
    ax2.grid(axis="y", visible=False)
    ax2.set_title("B. Worked headline multiples", loc="left", fontsize=12)

    handles = [Line2D([0], [0], marker="o", color="white", markerfacecolor="#555555", markeredgecolor="#555555",
                      markersize=9, label="Company-stated valuation"),
               Line2D([0], [0], marker="o", color="white", markerfacecolor="white", markeredgecolor="#555555",
                      markersize=9, label="Reported by press")]
    fig.legend(handles=handles, loc="upper center", ncol=2, fontsize=9, bbox_to_anchor=(0.5, 0.99))
    fig.suptitle("AI-native storage vendors: valuations and what they imply, 2020-2026", x=0.01, ha="left",
                 y=1.06, fontsize=13, fontweight="bold")
    _style.source_note(fig, "Sources: VAST, WEKA and Blackstone releases; StorageNewsletter 2021-05-05; Blocks & Files "
                            "2023-12-06 and 2026-02-05 (Feb 2026 = midpoint of reported US$25-27B); Calcalist 2022-11; CNBC "
                            "2026-04-22. Panel B is worked arithmetic: denominators mix committed ARR (VAST), ARR (WEKA) "
                            "and reported revenue (DDN, Forbes 2026, unverified), so the multiples are indicative, not "
                            "comparable. Data: data/ch41_valuations.csv")
    fig.tight_layout()
    return _style.save(fig, out_dir, NAME)


if __name__ == "__main__":
    print(build(_style.ROOT / "docs" / "assets" / "charts"))
