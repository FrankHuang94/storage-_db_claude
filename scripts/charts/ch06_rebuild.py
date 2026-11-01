"""Ch6 — Illustrative worked example: rebuild time vs device capacity, single-spare RAID vs declustered EC.

Reads data/ch06_rebuild.csv (every row carries `source` and `as_of`); writes docs/assets/charts/ch06-rebuild.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch06_rebuild.csv"
NAME = "ch06-rebuild"
COLORS = {"single spare": "#D55E00", "declustered": "#0072B2"}


def _load() -> tuple[list[str], dict]:
    devices: list[str] = []
    hours: dict = {}
    with CSV.open(newline="") as fh:
        for r in csv.DictReader(fh):
            if r["device"] not in devices:
                devices.append(r["device"])
            hours[(r["device"], r["mode"])] = float(r["rebuild_hours"])
    return devices, hours


def build(out_dir: Path) -> Path:
    _style.apply()
    devices, hours = _load()
    fig, ax = plt.subplots(figsize=(10, 5.2))
    y = list(range(len(devices)))
    h = 0.38
    for off, mode, label in ((-h / 2, "single spare", "Rebuild onto one replacement drive (classic RAID)"),
                             (h / 2, "declustered", "Declustered rebuild across 100 surviving drives")):
        vals = [hours[(d, mode)] for d in devices]
        bars = ax.barh([v + off for v in y], vals, height=h, color=COLORS[mode], label=label)
        for b, v in zip(bars, vals):
            txt = f"{v:.0f} h" if v >= 10 else (f"{v:.1f} h" if v >= 1 else f"{v * 60:.0f} min")
            ax.text(b.get_width() * 1.08, b.get_y() + b.get_height() / 2, txt, va="center", fontsize=9, color="#222222")
    ax.set_xscale("log")
    ax.set_xlim(0.1, 400)
    ax.set_yticks(y)
    ax.set_yticklabels(devices)
    ax.invert_yaxis()
    ax.axvline(24, color="#888888", linestyle=":", linewidth=1.2)
    ax.set_xticks([0.1, 1, 10, 24, 100])
    ax.set_xticklabels(["6 min", "1 h", "10 h", "24 h", "100 h"])
    ax.set_xlabel("Time to restore full redundancy (hours, log scale)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.45, -0.14), ncol=2, fontsize=9)
    ax.set_title("Illustrative worked example: a 245 TB SSD rebuilt the classic way\ntakes longer than a 30 TB HDD did",
                 loc="left", fontsize=12)
    _style.source_note(fig, "Illustrative model, not vendor data. Rebuild time = capacity / effective rebuild write rate. Single spare: HDD 200 MB/s, "
                            "SSD 1 GB/s (throttled under production load). Declustered: 100 drives x 50 MB/s (HDD) or x 0.5 GB/s (SSD). "
                            "Ignores read amplification (k strips read per strip rebuilt). Data: data/ch06_rebuild.csv")
    fig.tight_layout()
    return _style.save(fig, out_dir, NAME)
