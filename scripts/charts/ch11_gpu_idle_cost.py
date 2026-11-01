"""Ch11 — Worked example: annual cost of GPU idle time caused by storage stalls on a 1,024-GPU H100 cluster.

Reads data/ch11_gpu_idle_cost.csv (every row carries `source` and `as_of`). Grouped horizontal bars:
four stall scenarios x three rental-price tiers. Writes docs/assets/charts/ch11-gpu-idle-cost.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch11_gpu_idle_cost.csv"
NAME = "ch11-gpu-idle-cost"
TIER_COLORS = ["#56B4E9", "#0072B2", "#D55E00"]


def _load():
    scenarios: list[str] = []
    tiers: list[str] = []
    vals: dict = {}
    fracs: dict = {}
    with CSV.open(newline="") as fh:
        for r in csv.DictReader(fh):
            s, t = r["scenario"], r["price_tier"]
            if s not in scenarios:
                scenarios.append(s)
            if t not in tiers:
                tiers.append(t)
            vals[(s, t)] = float(r["annual_idle_cost_usd"])
            fracs[s] = float(r["stall_fraction"])
    return scenarios, tiers, vals, fracs


def build(out_dir: Path) -> Path:
    _style.apply()
    scenarios, tiers, vals, fracs = _load()
    fig, ax = plt.subplots(figsize=(11, 5.4))
    h = 0.26
    order = list(reversed(scenarios))
    for i, t in enumerate(tiers):
        ys = [k + (1 - i) * h for k in range(len(order))]
        xs = [vals[(s, t)] / 1e6 for s in order]
        ax.barh(ys, xs, height=h, color=TIER_COLORS[i], label=t)
        for y, x in zip(ys, xs):
            ax.text(x + 0.03, y, f"${x:.2f}M", va="center", fontsize=9, color="#222222")
    ax.set_yticks(range(len(order)))
    ax.set_yticklabels([f"{s}\n({fracs[s] * 100:.2f}% of wall-clock idle)" for s in order], fontsize=10)
    ax.set_xlabel("Annual cost of idle GPU time (US$ millions)")
    ax.grid(axis="y", visible=False)
    ax.set_xlim(0, max(vals.values()) / 1e6 * 1.22)
    ax.legend(title="Rental price per GPU-hour", loc="upper right", bbox_to_anchor=(1.0, 0.70), fontsize=9, title_fontsize=9,
              frameon=True, facecolor="white", edgecolor="#DDDDDD", framealpha=1.0)
    fig.suptitle("Worked example: what storage stalls cost a 1,024-GPU H100 cluster per year",
                 fontsize=13, fontweight="bold", x=0.01, ha="left")
    _style.source_note(fig, "Worked example, not measured data. Idle cost = stall fraction x 1,024 GPUs x 8,760 h x price. "
                            "Checkpoint = 70B parameters x 16 bytes (bf16 weights + fp32 master + Adam state) = 1.12 TB. "
                            "Prices: CoreWeave and Lambda on-demand as reported by price trackers, 2026; $2.00 is an illustrative "
                            "low tier. Data: data/ch11_gpu_idle_cost.csv")
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    return _style.save(fig, out_dir, NAME)
