"""Ch12 — PCIe generations: per-lane rate and x4 (SSD-width) bandwidth per direction, by spec release date.

Reads data/ch12_pcie_bandwidth.csv (spec dates sourced; x4 GB/s is worked arithmetic from the
line rate and encoding, stated in the CSV `source` column). Writes docs/assets/charts/ch12-pcie-bandwidth.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch12_pcie_bandwidth.csv"
NAME = "ch12-pcie-bandwidth"


def _load() -> list[dict]:
    with CSV.open(newline="") as fh:
        return list(csv.DictReader(fh))


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    fig, ax = plt.subplots(figsize=(10.5, 5.2))
    xs = [float(r["release_year"]) for r in rows]
    eff = [float(r["x4_gbps_effective_per_dir"]) for r in rows]
    raw = [float(r["x4_gbps_raw_per_dir"]) for r in rows]
    for r, x, e, w in zip(rows, xs, eff, raw):
        target = r["status"] == "target"
        color = "#999999" if target else ("#0072B2" if r["signaling"] == "NRZ" else "#D55E00")
        ax.bar(x, e, width=0.9, color=color, alpha=0.55 if target else 1.0,
               hatch="//" if target else None, edgecolor=color, zorder=3)
        ax.text(x, e * 1.12, f"{e:.1f} GB/s", ha="center", va="bottom", fontsize=9, fontweight="bold", color="#222222")
        if r["shipping_ssd_x4_read_gbps"]:
            s = float(r["shipping_ssd_x4_read_gbps"])
            ax.plot(x + 0.75, s, marker="D", color="#009E73", markersize=8, zorder=4)
            ax.annotate(f"{r['shipping_ssd_name']}\n{s:.0f} GB/s, in volume 2026",
                        xy=(x + 0.75, s), xytext=(x - 5.2, s * 1.6), fontsize=8, color="#009E73",
                        arrowprops={"arrowstyle": "-", "color": "#009E73"})
    ax.set_yscale("log", base=2)
    ax.set_ylim(0.5, 300)
    ax.set_yticks([1, 2, 4, 8, 16, 32, 64, 128])
    ax.set_yticklabels(["1", "2", "4", "8", "16", "32", "64", "128"])
    ax.set_xlim(2009.5, 2029.5)
    ax.set_xticks(xs)
    ax.set_xticklabels([f"{r['generation']}\n{r['gt_s_per_lane']} GT/s/lane\n{r['spec_release']}" for r in rows], fontsize=8.5)
    ax.grid(axis="x", visible=False)
    ax.set_xlabel("Generation, per-lane rate and specification release date (x-position = release date)")
    ax.set_ylabel("x4 link, GB/s per direction (log2 scale)")
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color="#0072B2", label="NRZ, 128b/130b encoding"),
                       Patch(color="#D55E00", label="PAM4, 256-byte FLIT"),
                       Patch(facecolor="#999999", alpha=0.55, hatch="//", label="Target, not yet released")],
              loc="upper left", bbox_to_anchor=(0.12, 1.0))
    ax.set_title("PCIe doubles per generation; a x4 SSD link went from ~4 GB/s (2010 spec) to ~59 GB/s (2025 spec)",
                 loc="left", fontsize=12)
    _style.source_note(fig, "Spec dates: PCI-SIG releases (2010-11-18, Oct 2017, 2019-05-29, 2022-01-11, 2025-06-11); PCIe 8.0 is a 2028 target. "
                            "GB/s = worked arithmetic: lanes x GT/s x encoding efficiency / 8 (128/130 for Gen3-5; 236/256 TLP bytes per FLIT for Gen6+, "
                            "an upper bound). Data: data/ch12_pcie_bandwidth.csv")
    fig.tight_layout()
    return _style.save(fig, out_dir, NAME)
