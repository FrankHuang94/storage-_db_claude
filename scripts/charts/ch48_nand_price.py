"""Ch48 — NAND contract-price cycle, 1Q23–4Q26: TrendForce quarterly QoQ forecasts.

Reads data/ch48_nand_price.csv (one row per quarter x segment x forecast vintage; each row has its own
`source`, `as_of`, `verified`). Bars show the midpoint of the latest TrendForce range for blended NAND
and for enterprise SSD, with whiskers for the published range. Where TrendForce revised a quarter
(4Q25, 1Q26) the superseded original forecast is drawn as a hollow diamond. A line on the right axis
compounds the blended midpoints into an index (end-4Q22 = 100; 2Q25, with no blended figure, is held flat). These are forecasts,
not realised prices. Writes docs/assets/charts/ch48-nand-price.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

import _style

CSV = _style.DATA / "ch48_nand_price.csv"
NAME = "ch48-nand-price"
QUARTERS = ["1Q23", "2Q23", "3Q23", "4Q23", "1Q24", "2Q24", "3Q24", "4Q24",
            "1Q25", "2Q25", "3Q25", "4Q25", "1Q26", "2Q26", "3Q26", "4Q26"]
BLEND = "#0072B2"
ENT = "#E69F00"


def _load() -> list[dict]:
    with CSV.open(newline="") as fh:
        return list(csv.DictReader(fh))


def _pick(rows, q, seg):
    """Latest vintage for a quarter/segment, plus the superseded original if revised."""
    cand = [r for r in rows if r["quarter"] == q and r["segment"] == seg]
    if not cand:
        return None, None
    rev = [r for r in cand if "revised" in r["kind"]]
    orig = [r for r in cand if "original" in r["kind"]]
    latest = rev[0] if rev else cand[-1]
    return latest, (orig[0] if rev and orig else None)


def _mid(r):
    return (float(r["low_pct"]) + float(r["high_pct"])) / 2


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    fig, ax = plt.subplots(figsize=(11.5, 5.6))
    w = 0.38
    index, level = [], 100.0
    for i, q in enumerate(QUARTERS):
        for seg, off, col in (("blended NAND", -w / 2, BLEND), ("enterprise SSD", w / 2, ENT)):
            latest, orig = _pick(rows, q, seg)
            if latest is None:
                continue
            m = _mid(latest)
            lo, hi = float(latest["low_pct"]), float(latest["high_pct"])
            hatch = "//" if "VERIFY" in latest["verified"] else None
            ax.bar(i + off, m, width=w, color=col, edgecolor="white", hatch=hatch)
            if hi > lo:
                ax.errorbar(i + off, m, yerr=[[m - lo], [hi - m]], fmt="none", ecolor="#444444",
                            capsize=2.5, linewidth=0.9)
            if orig is not None:
                ax.plot(i + off, _mid(orig), marker="D", mfc="white", mec="#222222", ms=6, zorder=5)
            if seg == "blended NAND" and abs(m) >= 10:
                ax.text(i + off, m + (3 if m > 0 else -3), f"{(int(m + 0.5) if m > 0 else -int(-m + 0.5)):+d}%", ha="center",
                        va="bottom" if m > 0 else "top", fontsize=7.5, color="#222222")
            if seg == "blended NAND":
                level *= 1 + m / 100
        index.append(level)
    ax.axhline(0, color="#888888", linewidth=0.8)
    ax.set_xticks(range(len(QUARTERS)))
    ax.set_xticklabels(QUARTERS, fontsize=9)
    ax.set_ylabel("QoQ contract-price change, forecast midpoint (%)")
    ax.set_ylim(-25, 85)
    ax.grid(axis="x", visible=False)
    ax2 = ax.twinx()
    ax2.plot(range(len(QUARTERS)), index, color="#D55E00", linewidth=2, marker="o", ms=3.5)
    ax2.set_ylabel("Compounded blended index (end-4Q22 = 100)", color="#D55E00")
    ax2.tick_params(axis="y", colors="#D55E00")
    ax2.set_ylim(0, 560)
    ax2.grid(False)
    ax2.spines["right"].set_visible(True)
    ax2.text(len(QUARTERS) - 1, index[-1] + 12, f"{index[-1]:.0f}", color="#D55E00", ha="center", fontsize=9,
             fontweight="bold")
    ax.text(1.2, 28, "2023: tail of the\nworst downturn;\nsuppliers cut output", fontsize=8.5, color="#555555", ha="center")
    ax.text(8.6, 45, "4Q24–1Q25: inventory\ncorrection, then AI\nand HDD shortage", fontsize=8.5, color="#555555", ha="center")
    handles = [Patch(color=BLEND, label="Blended NAND contract price (TrendForce)"),
               Patch(color=ENT, label="Enterprise SSD contract price (where published)"),
               Patch(facecolor="white", edgecolor="#555555", hatch="//", label="Seen only via secondary coverage [VERIFY]"),
               Line2D([], [], marker="D", mfc="white", mec="#222222", ls="none", label="Original forecast, later revised up"),
               Line2D([], [], color="#D55E00", lw=2, label="Index compounding blended midpoints (right axis)")]
    ax.legend(handles=handles, loc="upper left", fontsize=8.3)
    ax.set_title("NAND contract-price cycle, 1Q23–4Q26: TrendForce quarterly forecasts (midpoint of range; whiskers = range)",
                 loc="left", fontsize=12)
    _style.source_note(fig, "Sources: TrendForce press releases and syndicated copies, 2023-01-05 to 2026-09-30; one source per row in "
                            "data/ch48_nand_price.csv. Forecasts, not realised prices (realised moves were usually larger in "
                            "upturns, e.g. 1Q23 ASP fell ~15%). 2Q25 has no blended figure (enterprise SSD flat); 3Q24 enterprise "
                            "bar is the realised ~15% ASP rise; 4Q25 enterprise bar is a 'more than 25%' lower bound. Index is "
                            "illustrative arithmetic (2Q25 held flat). Data: data/ch48_nand_price.csv")
    fig.tight_layout()
    return _style.save(fig, out_dir, NAME)
