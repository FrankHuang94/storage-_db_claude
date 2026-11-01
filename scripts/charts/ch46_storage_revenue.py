"""Ch46 — Storage revenue in the fiscal quarter ending July/August 2026 vs. a year earlier,
for the four incumbents/peers that disclose a storage-relevant line (Dell, NetApp, HPE, Everpure).

Reads data/ch46_storage_revenue.csv (`source`, `as_of`, plus `prior_year_basis` noting where the
year-ago value is derived from reported growth). Definitions differ by company and are printed
under each bar group. IBM, Hitachi Vantara and Huawei do not disclose storage revenue and are omitted.
Writes docs/assets/charts/ch46-storage-revenue.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

import _style

CSV = _style.DATA / "ch46_storage_revenue.csv"
NAME = "ch46-storage-revenue"
SHORT_DEF = {
    "Dell": "ISG storage line\nQ2 FY27 (May–Jul 2026)",
    "NetApp": "Total company revenue\nQ1 FY27 (14 weeks)",
    "Everpure": "Total company revenue\nQ2 FY27 (to Aug 2, 2026)",
    "HPE": "Storage line, Cloud & AI\nQ3 FY26 (May–Jul 2026)",
}


def _load() -> list[dict]:
    with CSV.open(newline="") as fh:
        return list(csv.DictReader(fh))


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    fig, ax = plt.subplots(figsize=(10.5, 5.4))
    w = 0.36
    for i, r in enumerate(rows):
        v = r["vendor"]
        cur, prev = float(r["revenue_busd"]), float(r["prior_year_busd"])
        derived = r["prior_year_basis"].startswith("derived")
        color = _style.VENDOR_COLORS.get(v, "#999999")
        ax.bar(i - w / 2, prev, w, color="#DDDDDD", edgecolor="#888888", hatch="//" if derived else None)
        ax.bar(i + w / 2, cur, w, color=color, edgecolor="#555555" if v == "HPE" else color)
        ax.text(i - w / 2, prev + 0.06, f"{prev:.2f}", ha="center", va="bottom", fontsize=9, color="#555555")
        ax.text(i + w / 2, cur + 0.06, f"{cur:.2f}\n{(cur / prev - 1) * 100:+.0f}%", ha="center", va="bottom",
                fontsize=9.5, color="#222222", fontweight="bold")
    ax.set_xticks(range(len(rows)))
    ax.set_xticklabels([f"{r['vendor']}\n{SHORT_DEF[r['vendor']]}\nIDC 2Q26 share: {r['idc_2q26_share_pct']}%" for r in rows], fontsize=9)
    ax.set_ylabel("Revenue in the quarter (US$ billions)")
    ax.set_ylim(0, 5.8)
    ax.grid(axis="x", visible=False)
    ax.legend(handles=[Patch(facecolor="#DDDDDD", edgecolor="#888888", label="Same quarter a year earlier"),
                       Patch(facecolor="#DDDDDD", edgecolor="#888888", hatch="//",
                             label="Year-earlier value derived from reported growth rate"),
                       Patch(facecolor="#555555", label="Quarter ending Jul/Aug 2026 (bar in vendor colour)")],
              loc="upper right", fontsize=9)
    ax.set_title("Storage-relevant revenue, fiscal quarter ending July–August 2026 vs a year earlier\n"
                 "(definitions differ: not a like-for-like market-share comparison)", loc="left", fontsize=12)
    _style.source_note(fig, "Sources: Dell Q2 FY27 results (2026-08); NetApp Q1 FY27 results (2026-09-02); Everpure Q2 FY27 "
                            "results (2026-08-26); HPE Q3 FY26 8-K (2026-09-02). IDC shares: Worldwide Quarterly Enterprise "
                            "Storage Systems Tracker, 2Q26 (calendar Apr–Jun 2026), external storage only. IBM, Hitachi "
                            "Vantara and Huawei do not disclose storage revenue. Data: data/ch46_storage_revenue.csv")
    fig.tight_layout()
    return _style.save(fig, out_dir, NAME)
