"""Ch10 — Link-speed roadmap: IEEE Ethernet standards and NVIDIA flagship networking products, 2010-2026.

Reads data/ch10_link_speeds.csv (each row has `source` and `as_of`). Plots port speed (log2 axis)
against date, marker by category, and annotates the per-lane SerDes rate that made each speed possible.
Writes docs/assets/charts/ch10-link-speeds.svg.
"""
from __future__ import annotations

import csv
from datetime import date
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch10_link_speeds.csv"
NAME = "ch10-link-speeds"
STYLE = {
    "IEEE Ethernet standard": ("#0072B2", "o"),
    "NVIDIA InfiniBand product": ("#E69F00", "s"),
    "NVIDIA Ethernet/DPU product": ("#009E73", "D"),
}
SHORT = {
    "IEEE 802.3ba 100GbE": "802.3ba 100GbE",
    "IEEE 802.3bs 200/400GbE": "802.3bs 400GbE",
    "IEEE 802.3ck 100G-per-lane electrical": "802.3ck 100G lanes",
    "IEEE 802.3df 400/800GbE": "802.3df 800GbE",
    "IEEE 802.3dj 1.6TbE (draft in ballot)": "802.3dj 1.6TbE\n(still in ballot)",
    "NVIDIA Quantum-2 NDR InfiniBand": "Quantum-2 NDR",
    "NVIDIA Quantum-X800 XDR InfiniBand": "Quantum-X800 XDR",
    "NVIDIA BlueField-4 DPU": "BlueField-4",
    "NVIDIA Spectrum-6 switch ASIC (1.6TbE-capable)": "Spectrum-6 ASIC",
}
OFFSETS = {
    "802.3ba 100GbE": (8, -4), "802.3bs 400GbE": (-40, 10), "802.3ck 100G lanes": (6, -16),
    "802.3df 800GbE": (-100, -26), "802.3dj 1.6TbE\n(still in ballot)": (8, -30),
    "Quantum-2 NDR": (-34, 10), "Quantum-X800 XDR": (-70, 12),
    "BlueField-4": (8, -26), "Spectrum-6 ASIC": (-96, 6),
}


def _load() -> list[dict]:
    with CSV.open(newline="") as fh:
        rows = list(csv.DictReader(fh))
    for r in rows:
        y, m, d = (int(x) for x in r["date"].split("-"))
        r["dt"] = date(y, m, d)
        r["port"] = float(r["port_gbps"])
        r["lane"] = int(float(r["lane_gbps"]))
    return rows


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    fig, ax = plt.subplots(figsize=(10.5, 5.4))
    for cat, (color, marker) in STYLE.items():
        pts = [r for r in rows if r["category"] == cat]
        ax.scatter([r["dt"] for r in pts], [r["port"] for r in pts], color=color, marker=marker, s=70,
                   label=cat, zorder=3,
                   facecolors=["white" if "ballot" in r["status"] else color for r in pts],
                   edgecolors=color, linewidths=1.8)
        for r in pts:
            label = SHORT[r["milestone"]]
            dx, dy = OFFSETS.get(label, (6, 6))
            ax.annotate(f"{label}\n{r['lane']}G/lane", (r["dt"], r["port"]), textcoords="offset points",
                        xytext=(dx, dy), fontsize=8.5, color="#222222")
    ax.set_yscale("log", base=2)
    ax.set_yticks([100, 200, 400, 800, 1600])
    ax.set_yticklabels(["100G", "200G", "400G", "800G", "1.6T"])
    ax.set_ylim(70, 2600)
    ax.set_xlim(date(2009, 1, 1), date(2027, 6, 1))
    ax.set_ylabel("Port speed (log scale)")
    ax.set_xlabel("Standard approval or product announcement date")
    ax.legend(loc="upper left")
    ax.set_title("Port speed follows SerDes lane rate: sourced Ethernet and InfiniBand milestones, 2010-2026",
                 loc="left")
    _style.source_note(fig, "Sources: IEEE 802.3 task-force pages and ballot records; Ethernet Alliance; NVIDIA newsroom; "
                            "ServeTheHome; SDxCentral. Hollow marker = draft still in ballot, plotted at the as-of date "
                            "(2026-11-01 data). Lane = electrical lane rate (e.g., 200G PAM4 on '224G' SerDes). "
                            "Data: data/ch10_link_speeds.csv")
    fig.tight_layout()
    return _style.save(fig, out_dir, NAME)
