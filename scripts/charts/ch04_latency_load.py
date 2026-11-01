"""Ch04 — Illustrative model: latency versus load (the hockey stick) and the IOPS/latency knee.

Reads data/ch04_latency_load.csv (generated from the chapter's stated model; every row carries
`source` and `as_of`). Panel A: M/M/1 mean, p99 and p99.9 response time versus utilization.
Panel B: an SSD modelled as 32 NAND dies (80 us reads) swept over queue depth; latency vs IOPS,
with the ideal Little's-law bound. Writes docs/assets/charts/ch04-latency-load.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch04_latency_load.csv"
NAME = "ch04-latency-load"
COLORS = {"mean": "#0072B2", "p99": "#E69F00", "p99.9": "#D55E00",
          "random dies": "#0072B2", "ideal bound": "#999999"}


def _load() -> dict:
    out: dict = {}
    with CSV.open(newline="") as fh:
        for r in csv.DictReader(fh):
            out.setdefault((r["panel"], r["series"]), []).append(r)
    return out


def build(out_dir: Path) -> Path:
    _style.apply()
    d = _load()
    fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.8))

    for s in ("mean", "p99", "p99.9"):
        rows = d[("A_utilization", s)]
        a.plot([float(r["x"]) * 100 for r in rows], [float(r["latency_us"]) for r in rows],
               color=COLORS[s], linewidth=2, marker="o", markersize=3, label=s)
    a.set_ylim(0, 4000)
    a.set_xlim(0, 100)
    a.axvspan(70, 100, color="#F0E442", alpha=0.25, linewidth=0)
    a.text(71.5, 40, "beyond ~70% busy,\nthe tail explodes", fontsize=9, color="#555555", va="bottom")
    a.set_title("A. Response time vs utilization (M/M/1, 100 µs service)", fontsize=11)
    a.set_xlabel("Utilization of the bottleneck resource (%)")
    a.set_ylabel("Response time (µs)")
    a.legend(loc="upper left")

    for s, style in (("ideal bound", "--"), ("random dies", "-")):
        rows = d[("B_queue_depth", s)]
        b.plot([float(r["iops_k"]) for r in rows], [float(r["latency_us"]) for r in rows],
               color=COLORS[s], linestyle=style, linewidth=2, marker="o" if s == "random dies" else None,
               markersize=4, label="32 dies, random placement" if s == "random dies" else "ideal: perfect parallelism")
    for r in d[("B_queue_depth", "random dies")]:
        if r["queue_depth"] in {"1", "8", "32", "64", "128", "256"}:
            off = (4, 8) if r["queue_depth"] in {"1", "8"} else (-38, 4)
            b.annotate(f"QD{r['queue_depth']}", (float(r["iops_k"]), float(r["latency_us"])),
                       textcoords="offset points", xytext=off, fontsize=8.5, color="#222222")
    b.set_title("B. Latency vs IOPS as queue depth rises (32-die SSD)", fontsize=11)
    b.set_xlabel("Achieved random-read IOPS (thousands)")
    b.set_ylabel("Mean latency (µs)")
    b.set_ylim(0, 700)
    b.legend(loc="upper left")

    fig.suptitle("Illustrative model: latency is flat until a resource saturates, then only the queue grows",
                 fontsize=13, fontweight="bold", x=0.01, ha="left")
    _style.source_note(fig, "Illustrative queueing models, not vendor data. A: M/M/1, mean = S/(1-ρ), percentile q = S·ln(1/(1-q))/(1-ρ). "
                            "B: requests land on random dies; IOPS = busy dies ÷ 80 µs; latency = QD ÷ IOPS (Little's law). "
                            "Data: data/ch04_latency_load.csv")
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    return _style.save(fig, out_dir, NAME)
