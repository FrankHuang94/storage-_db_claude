"""Ch30 — Illustrative data-volume funnel: from a web crawl to a trained model, and back out again.

Reads data/ch30_data_funnel.csv (every row carries `source` and `as_of`; `kind` marks reported figures,
Atlas byte estimates and worked examples). Horizontal log-scale bars in funnel order.
Writes docs/assets/charts/ch30-data-funnel.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Patch

import _style

CSV = _style.DATA / "ch30_data_funnel.csv"
NAME = "ch30-data-funnel"
COLORS = {"reported": "#0072B2", "estimate": "#56B4E9", "worked": "#D55E00"}


def _load() -> list[dict]:
    with CSV.open(newline="") as fh:
        return sorted(csv.DictReader(fh), key=lambda r: int(r["order"]))


def _fmt(tb: float) -> str:
    if tb >= 1000:
        return f"~{tb / 1000:,.0f} PB"
    if tb >= 1:
        return f"~{tb:,.0f} TB" if tb >= 10 else f"~{tb:,.1f} TB"
    return f"~{tb * 1000:,.0f} GB"


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    labels = [f"{r['stage']}\n{r['label']}" for r in rows]
    vals = [float(r["size_tb"]) for r in rows]
    cols = [COLORS[r["kind"]] for r in rows]

    fig, ax = plt.subplots(figsize=(11, 5.6))
    y = list(range(len(rows)))[::-1]
    bars = ax.barh(y, vals, color=cols, height=0.62)
    ax.set_xscale("log")
    ax.set_xlim(0.3, 60000)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=9.5)
    ax.set_xlabel("Bytes stored, terabytes (log scale)")
    ax.grid(axis="y", visible=False)
    for b, v, r in zip(bars, vals, rows):
        tok = f"  ({r['tokens_trillion']}T tokens)" if r["tokens_trillion"] else ""
        ax.text(v * 1.15, b.get_y() + b.get_height() / 2, (r.get("display") or _fmt(v)) + tok, va="center", fontsize=9.5)
    # divider between the funnel and the re-expansion
    ax.axhline(0.5, color="#888888", linewidth=0.8, linestyle="--")
    ax.legend(handles=[Patch(color=COLORS["reported"], label="Reported size"),
                       Patch(color=COLORS["estimate"], label="Reported tokens, bytes estimated at ~4 B/token"),
                       Patch(color=COLORS["worked"], label="Worked example")],
              loc="lower right", fontsize=9)
    fig.suptitle("Illustrative data-volume funnel: ~10 PB of crawl becomes <1 TB of weights, then checkpoints re-expand it",
                 fontsize=12.5, fontweight="bold", x=0.01, ha="left")
    _style.source_note(fig, "Illustrative chain across different public corpora, not one lab's pipeline. Sources: Common Crawl; DataComp-LM "
                            "(NeurIPS 2024); FineWeb (NeurIPS 2024) and dataset card; Llama 3 Herd of Models (2024). "
                            "Data: data/ch30_data_funnel.csv")
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    return _style.save(fig, out_dir, NAME)
