"""Ch40 — External enterprise storage vendor revenue share, 2Q25 vs 2Q26 (IDC).

Reads data/ch40_vendor_share.csv (`source`, `as_of`, `status_2q25`). 2Q26 shares and growth are
IDC-reported (via its 2026-09-10 release and trade-press tables); 2Q25 shares other than Dell's are
derived from 2Q26 revenue / (1 + growth) / 2Q25 market total. Writes docs/assets/charts/ch40-vendor-share.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

import _style

CSV = _style.DATA / "ch40_vendor_share.csv"
NAME = "ch40-vendor-share"
OTHER = "#BBBBBB"


def _load() -> list[dict]:
    with CSV.open(newline="") as fh:
        return list(csv.DictReader(fh))


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    fig, ax = plt.subplots(figsize=(10.5, 4.9))
    n = len(rows)
    h = 0.38
    for i, r in enumerate(rows):
        col = _style.VENDOR_COLORS.get(r["vendor"], "#E69F00" if r["vendor"] == "Huawei" else OTHER)
        s25, s26 = float(r["share_2q25_pct"]), float(r["share_2q26_pct"])
        ax.barh(i - h / 2, s25, height=h, color="white", edgecolor=col, hatch="//", linewidth=1.3)
        ax.barh(i + h / 2, s26, height=h, color=col)
        ax.text(s25 + 0.4, i - h / 2, f"{s25:.1f}%", va="center", fontsize=9, color="#555555")
        ax.text(s26 + 0.4, i + h / 2, f"{s26:.1f}%   (revenue {float(r['yoy_2q26_pct']):+.1f}% YoY)",
                va="center", fontsize=9.5, color="#222222")
    ax.set_yticks(range(n))
    ax.set_yticklabels([r["vendor"] for r in rows], fontsize=10.5)
    ax.invert_yaxis()
    ax.set_xlim(0, 62)
    ax.set_xlabel("Share of worldwide external enterprise storage vendor revenue (%)")
    ax.grid(axis="y", visible=False)
    ax.legend(handles=[Patch(facecolor="white", edgecolor="#555555", hatch="//", label="2Q25 (Dell reported; others derived)"),
                       Patch(color="#555555", label="2Q26 (IDC-reported)")], loc="upper right", fontsize=9)
    ax.set_title("Vendor share, 2Q25 vs 2Q26: Everpure gains most; 'Others' still 40% of the market",
                 loc="left", fontsize=12.5)
    _style.source_note(fig, "Sources: IDC 2Q2026 ESS Tracker release (2026-09-10) and StorageReview / itreseller.ch tables (2026-09). "
                            "2Q25 shares for Huawei, NetApp, Everpure, HPE and Others are derived as 2Q26 revenue / (1+YoY) / $7.74B "
                            "and may differ from IDC's restated figures. Huawei colour is ad hoc (not a style-guide vendor colour). "
                            "Data: data/ch40_vendor_share.csv")
    fig.tight_layout()
    return _style.save(fig, out_dir, NAME)
