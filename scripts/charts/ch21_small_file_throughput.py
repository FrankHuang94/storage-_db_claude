"""Ch21 — Illustrative worked example: effective read throughput vs file size at fixed metadata IOPS.

Model (stated in the chart and the chapter): effective throughput = min(B, M x S / k), where
B = aggregate data bandwidth (500 GB/s), M = cluster metadata ops/s, S = file size, k = metadata
ops per file (4: lookup, open, getattr, close). Reads data/ch21_small_file_throughput.csv and writes
docs/assets/charts/ch21-small-file-throughput.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

import _style

CSV = _style.DATA / "ch21_small_file_throughput.csv"
NAME = "ch21-small-file-throughput"
COLORS = {100000: "#D55E00", 1000000: "#0072B2", 10000000: "#009E73"}
LABELS = {100000: "100k metadata ops/s", 1000000: "1M metadata ops/s", 10000000: "10M metadata ops/s"}


def _load() -> dict:
    series: dict = {}
    with CSV.open(newline="") as fh:
        for r in csv.DictReader(fh):
            m = int(r["metadata_ops_per_s"])
            series.setdefault(m, []).append((float(r["file_size_bytes"]), float(r["effective_GBps"])))
    return series


def _size_fmt(x, _pos) -> str:
    if x >= 1e9:
        return f"{x / 1e9:g} GB"
    if x >= 1e6:
        return f"{x / 1e6:g} MB"
    return f"{x / 1e3:g} KB"


def build(out_dir: Path) -> Path:
    _style.apply()
    s = _load()
    fig, ax = plt.subplots(figsize=(10, 5.4))
    for m in sorted(s):
        pts = sorted(s[m])
        ax.plot([p[0] for p in pts], [p[1] for p in pts], color=COLORS[m], linewidth=2.2, label=LABELS[m])
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.xaxis.set_major_formatter(FuncFormatter(_size_fmt))
    ax.axhline(500, color="#888888", linestyle="--", linewidth=1)
    ax.text(4.5e3, 560, "data-bandwidth ceiling B = 500 GB/s", fontsize=9, color="#555555")
    for x, label, ha, dx in ((113e3, "ImageNet-style JPEG\n~113 KB", "left", 1.12),
                             (256e6, "tar / TFRecord shard\n~256 MB", "right", 1 / 1.12)):
        ax.axvline(x, color="#999999", linestyle=":", linewidth=1.2)
        ax.text(x * dx, 0.15, label, fontsize=9, color="#444444", va="bottom", ha=ha)
    ax.annotate("28 GB/s: GPUs see ~6% of\nthe bandwidth they paid for", xy=(113e3, 28.25), xytext=(4e5, 2.5),
                fontsize=9, color="#0072B2", arrowprops=dict(arrowstyle="->", color="#0072B2"))
    ax.set_xlabel("File (sample) size, log scale")
    ax.set_ylabel("Effective read throughput (GB/s), log scale")
    ax.set_ylim(0.08, 1500)
    ax.legend(loc="center right")
    ax.set_title("Illustrative worked example: below the crossover size, metadata IOPS, not bandwidth, sets throughput",
                 fontsize=12, loc="left")
    _style.source_note(fig, "Illustrative model, not vendor data: effective throughput = min(B, M x S / k); B = 500 GB/s; "
                            "k = 4 metadata ops per file (lookup, open, getattr, close);\ncrossover S* = k x B / M "
                            "(20 MB, 2 MB, 200 KB). Data: data/ch21_small_file_throughput.csv")
    fig.tight_layout()
    return _style.save(fig, out_dir, NAME)
