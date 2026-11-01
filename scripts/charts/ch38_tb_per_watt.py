"""Ch38 — Capacity per watt (TB/W) for drives and for whole enclosures/systems.

Reads data/ch38_tb_per_watt.csv. Two panels with separate x-axes: single drives/modules (top)
and enclosures or systems (bottom), because system overheads (controllers, fans, NICs) cut
TB/W by 2-10x versus the bare drive. Bars are coloured by vendor group; HDD bars are hatched.
Writes docs/assets/charts/ch38-tb-per-watt.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch38_tb_per_watt.csv"
NAME = "ch38-tb-per-watt"
COLORS = {"Everpure": "#0072B2", "VAST": "#E69F00", "DDN": "#CC79A7",
          "commodity flash": "#56B4E9", "HDD": "#999999"}
LABELS = {"Everpure": "Everpure (company-stated)", "VAST": "VAST Data", "DDN": "DDN",
          "commodity flash": "Commodity QLC SSD", "HDD": "Hard disk (hatched)"}


def _load() -> list[dict]:
    with CSV.open(newline="") as fh:
        return list(csv.DictReader(fh))


def _panel(ax, rows, title, xmax):
    rows = sorted(rows, key=lambda r: float(r["tb_per_w"]))
    ys = range(len(rows))
    for y, r in zip(ys, rows):
        v = float(r["tb_per_w"])
        hdd = r["group"] == "HDD"
        ax.barh(y, v, color=COLORS[r["group"]], hatch="//" if hdd else None,
                edgecolor="white" if not hdd else "#555555", linewidth=0.6, height=0.62, zorder=3)
        ax.text(v + xmax * 0.012, y, f"{v:.2f}  ({float(r['watts']):,.0f} W, {r['watts_basis']})",
                va="center", fontsize=8.3, color="#333333")
    ax.set_yticks(list(ys))
    ax.set_yticklabels([r["item"] for r in rows], fontsize=9.2)
    ax.set_xlim(0, xmax)
    ax.set_title(title, loc="left", fontsize=11)
    ax.grid(axis="y", visible=False)


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(10.5, 7.4), gridspec_kw={"height_ratios": [5, 5]})
    _panel(a1, [r for r in rows if r["level"] == "drive"], "Single drive or module, TB per watt (raw)", 13.5)
    _panel(a2, [r for r in rows if r["level"] == "system"],
           "Enclosure or system, TB per watt (raw except DDN, usable)", 3.4)
    a2.set_xlabel("Terabytes per watt (higher is better)")
    handles = [plt.Rectangle((0, 0), 1, 1, color=COLORS[k], hatch="//" if k == "HDD" else None,
                             ec="#555555" if k == "HDD" else "white") for k in COLORS]
    a1.legend(handles, [LABELS[k] for k in COLORS], loc="lower right", fontsize=8.5)
    fig.suptitle("QLC beats disk about 2x per watt at the drive; at system level the gap depends on drive size and "
                 "what the box includes", x=0.01, ha="left", fontsize=12, fontweight="bold")
    _style.source_note(fig, "Sources: StorageReview (Micron 6600 ION, Solidigm D5-P5336, Seagate Exos M); Blocks & Files "
                            "(2023-03-01, Pure DFM and FlashBlade//E); VAST Ceres V2 datasheet; WD Data102 user guide; "
                            "Everpure NCP note; DDN (2025-08-04). Watts basis differs by row (max, typical, stated) and "
                            "several rows rest on search summaries [VERIFY]. Systems differ in what they include: the VAST "
                            "DBox excludes CNodes, the WD JBOD excludes its head server, FlashBlade includes compute. "
                            "Data: data/ch38_tb_per_watt.csv")
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    return _style.save(fig, out_dir, NAME)
