"""Ch27 — FlashBlade//EXA MLPerf Storage v3.0 checkpoint-write scaling with data-node count.

Reads data/ch27_mlperf_checkpoint_scaling.csv (vendor-submitted MLPerf Storage v3.0 results as
reported by Everpure/HPCwire and StorageReview; per-node values are atlas arithmetic).
Bars = total checkpoint write bandwidth; dashed line = perfectly linear extrapolation of the
10-node point; annotations = GiB/s per data node. Writes docs/assets/charts/ch27-mlperf-checkpoint-scaling.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch27_mlperf_checkpoint_scaling.csv"
NAME = "ch27-mlperf-checkpoint-scaling"


def _load():
    rows = []
    with CSV.open(newline="") as fh:
        for r in csv.DictReader(fh):
            rows.append((int(r["data_nodes"]), float(r["checkpoint_write_gib_s"]), float(r["per_node_gib_s"])))
    return sorted(rows)


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    nodes = [r[0] for r in rows]
    total = [r[1] for r in rows]
    per = [r[2] for r in rows]
    fig, ax = plt.subplots(figsize=(9.5, 5))
    ax.bar(nodes, total, width=3.2, color=_style.VENDOR_COLORS["Everpure"], label="Measured checkpoint write (GiB/s)")
    base = rows[0][1] / rows[0][0]
    xs = [8, 32]
    ax.plot(xs, [base * x for x in xs], color="#D55E00", linestyle="--", linewidth=1.6,
            label="Perfectly linear from the 10-node point")
    for n, t, p in rows:
        ax.text(n, t + 18, f"{t:,.0f}\n({p:.1f} per node)", ha="center", va="bottom", fontsize=9, color=_style.TEXT)
    ax.set_xticks(nodes)
    ax.set_xlabel("FlashBlade//EXA data nodes in the submitted configuration")
    ax.set_ylabel("Checkpoint write bandwidth (GiB/s)")
    ax.set_ylim(0, 1150)
    ax.set_xlim(5, 34)
    ax.legend(loc="upper left")
    ax.set_title("MLPerf Storage v3.0: FlashBlade//EXA checkpoint write vs data-node count (vendor submission)",
                 fontsize=12, loc="left")
    _style.source_note(fig, "Source: MLPerf Storage v3.0 results as reported by Everpure (HPCwire, 2026-09-02) and StorageReview (2026-09); "
                            "15- and 20-node points reported by StorageReview only. Per-node values are atlas arithmetic. "
                            "No VAST, WEKA or DDN submission in v3.0. Data: data/ch27_mlperf_checkpoint_scaling.csv")
    fig.tight_layout()
    return _style.save(fig, out_dir, NAME)
