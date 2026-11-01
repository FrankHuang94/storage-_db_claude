"""Ch37 — MLPerf Storage v3.0 checkpoint-write bandwidth for selected submissions.

Reads data/ch37_mlperf_v3_checkpoint.csv (vendor-reported MLPerf Storage v3.0 results as
reported by the submitters and StorageReview). Configurations, models and deployment types
differ, which is the point of the chart: the headline number is mostly a function of how
much hardware was submitted. Writes docs/assets/charts/ch37-mlperf-v3-checkpoint.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch37_mlperf_v3_checkpoint.csv"
NAME = "ch37-mlperf-v3-checkpoint"
COLORS = {"Everpure": "#0072B2", "Azure": "#56B4E9", "Alluxio": "#E69F00", "NVIDIA": "#009E73"}


def _load():
    with CSV.open(newline="") as fh:
        rows = list(csv.DictReader(fh))
    for r in rows:
        r["v"] = float(r["checkpoint_write_gib_s"])
    return sorted(rows, key=lambda r: r["v"])


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    fig, ax = plt.subplots(figsize=(10, 5.2))
    ys = range(len(rows))
    for y, r in zip(ys, rows):
        hatch = "//" if "405B" in r["model"] else None
        ax.barh(y, r["v"], color=COLORS.get(r["submitter"], "#999999"), hatch=hatch,
                edgecolor="white" if hatch is None else "#222222", height=0.62)
        ax.text(r["v"] + 12, y + 0.12, f"{r['v']:,.1f} GiB/s", va="center", fontsize=10,
                color=_style.TEXT, fontweight="bold")
        ax.text(r["v"] + 12, y - 0.22, f"{r['model']} · {r['deployment']} · {r['config_note']}",
                va="center", fontsize=8, color="#444444")
    ax.set_yticks(list(ys))
    ax.set_yticklabels([r["label"] for r in rows], fontsize=10)
    ax.set_xlim(0, 1900)
    ax.set_axisbelow(True)
    ax.set_xticks([0, 250, 500, 750, 1000])
    ax.set_xlabel("Checkpoint write bandwidth (GiB/s), mean of 10 checkpoints")
    ax.grid(axis="y", visible=False)
    ax.set_title("MLPerf Storage v3.0 checkpoint write, selected submissions (vendor-reported; "
                 "configurations not comparable)", fontsize=12, loc="left")
    _style.source_note(fig, "Sources: Everpure release via HPCwire (2026-09-02); Microsoft Learn Azure Managed Lustre v3.0 page; "
                            "NVIDIA AIStore blog (2026-09-01); Alluxio blog (2026-09, search summary only, hatched bar = 405B model, "
                            "not the 1T-class model); StorageReview (2026-09). VAST, WEKA and DDN did not submit to v3.0. "
                            "Data: data/ch37_mlperf_v3_checkpoint.csv")
    fig.tight_layout()
    return _style.save(fig, out_dir, NAME)
