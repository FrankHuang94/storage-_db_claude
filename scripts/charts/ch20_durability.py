"""Ch20 — Illustrative model: durability "nines" vs drive AFR (panel A) and vs rebuild time (panel B).

Reads scheme parameters and reference AFRs from data/ch20_durability.csv (every row carries `source`
and `as_of`) and computes the curves here, so the formulas are in one checkable place:

    lambda        = AFR / 8766 h                     (per-drive failure rate, exponential)
    mu            = 1 / MTTR                          (rebuild rate)
    MTTDL_group   = mu^m / (n (n-1) ... (n-m) * lambda^(m+1))      n = k + m drives per group
                    (standard Markov approximation, valid when mu >> lambda)
    P_loss_year   = 1 - exp(-G * 8766 / MTTDL_group)  G = groups for 10 PB usable on 30 TB drives
    nines         = -log10(P_loss_year)
    correlated    = MTTDL_group / c^m, c = 10         (each further failure in a rebuild window 10x likelier)

Ignores unrecoverable read errors, latent sector errors, software bugs and operator error; treats groups as
independent (optimistic for random placement; see Cidon et al. 2013). Writes docs/assets/charts/ch20-durability.svg.
"""
from __future__ import annotations

import csv
import math
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter, MultipleLocator

import _style

CSV = _style.DATA / "ch20_durability.csv"
NAME = "ch20-durability"
HOURS_PER_YEAR = 8766.0
USABLE_TB = 10_000.0  # 10 PB usable
DRIVE_TB = 30.0
CORR = 10.0
COLORS = {
    "RAID 6 (8+2) classic rebuild": "#D55E00",
    "EC 8+2 declustered": "#E69F00",
    "EC 16+4 declustered": "#0072B2",
    "3-way replication": "#009E73",
    "EC 16+4 with 10x correlated failures during rebuild": "#0072B2",
}


def _load() -> tuple[list[dict], list[dict]]:
    schemes, refs = [], []
    with CSV.open(newline="") as fh:
        for r in csv.DictReader(fh):
            (refs if r["row_type"] == "afr_ref" else schemes).append(r)
    return schemes, refs


def nines(k: int, m: int, mttr_h: float, afr: float, corr: float = 1.0) -> float:
    n = k + m
    lam = afr / HOURS_PER_YEAR
    mu = 1.0 / mttr_h
    prod = 1.0
    for i in range(m + 1):
        prod *= (n - i)
    mttdl = mu ** m / (prod * lam ** (m + 1)) / corr ** m
    groups = USABLE_TB / (k * DRIVE_TB)
    rate = groups * HOURS_PER_YEAR / mttdl
    p = -math.expm1(-rate)
    return -math.log10(p)


def build(out_dir: Path) -> Path:
    _style.apply()
    schemes, refs = _load()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 5.4))
    afrs = [10 ** (x / 50) for x in range(-50, 36)]  # 0.1% .. ~5%
    for s in schemes:
        k, m, mttr = int(s["k"]), int(s["m"]), float(s["mttr_hours"])
        corr = CORR if s["row_type"] == "scheme_corr" else 1.0
        ys = [nines(k, m, mttr, a / 100, corr) for a in afrs]
        ls = "--" if corr > 1 else "-"
        lab = s["label"] + ("" if corr > 1 else f" ({mttr:.0f} h rebuild)")
        ax1.plot(afrs, ys, ls, color=COLORS[s["label"]], linewidth=2, label=lab)
    for r in refs:
        x = float(r["value_pct"])
        ax1.axvline(x, color="#999999", linestyle=":", linewidth=1)
        ax1.text(x * 1.05, 23.3, r["label"], rotation=90, va="top", fontsize=8, color="#555555")
    ax1.axhline(11, color="#222222", linewidth=0.8)
    ax1.text(3.0, 11.3, "11 nines", fontsize=9)
    ax1.set_xscale("log")
    ax1.set_xlim(0.1, 5)
    ax1.set_ylim(2, 24)
    ax1.set_xticks([0.1, 0.2, 0.5, 1, 2, 5])
    ax1.set_xticklabels(["0.1%", "0.2%", "0.5%", "1%", "2%", "5%"])
    ax1.set_xlabel("Drive annual failure rate (log scale)")
    ax1.set_ylabel("Modelled annual durability (nines) for 10 PB usable")
    ax1.set_title("A. Nines vs drive AFR", loc="left", fontsize=11)
    handles, labels = ax1.get_legend_handles_labels()

    mttrs = [10 ** (x / 40) for x in range(0, 90)]  # 1 h .. ~178 h
    afr = 0.0136
    for s in schemes:
        if s["row_type"] != "scheme" or s["label"].startswith("RAID"):
            continue
        k, m = int(s["k"]), int(s["m"])
        lab = s["label"].replace(" declustered", "") + (" (= RAID 6)" if (k, m) == (8, 2) else "")
        ax2.plot(mttrs, [nines(k, m, t, afr) for t in mttrs], color=COLORS[s["label"]], linewidth=2, label=lab)
    ax2.axhline(11, color="#222222", linewidth=0.8)
    ax2.set_xscale("log")
    ax2.set_xlim(1, 170)
    ax2.set_ylim(2, 24)
    ax2.set_xticks([1, 4, 12, 24, 72, 168])
    ax2.set_xticklabels(["1 h", "4 h", "12 h", "1 d", "3 d", "1 wk"])
    ax2.set_xlabel("Time to restore redundancy (log scale), AFR fixed at 1.36%")
    ax2.set_title("B. Nines vs rebuild time", loc="left", fontsize=11)
    ax2.legend(loc="upper right", fontsize=8.5)
    for ax in (ax1, ax2):
        ax.xaxis.set_minor_formatter(NullFormatter())
        ax.yaxis.set_major_locator(MultipleLocator(2))
    fig.legend(handles, labels, loc="lower left", bbox_to_anchor=(0.06, 0.0), ncol=2, fontsize=9)

    fig.suptitle("Illustrative model: durability nines are a formula output; parity count dominates, and correlation can erase the gain",
                 x=0.01, ha="left", fontsize=12, fontweight="bold")
    _style.source_note(fig, "Illustrative model, not vendor data. MTTDL = mu^m / (n(n-1)...(n-m) lambda^(m+1)); lambda = AFR/8766 h; mu = 1/MTTR; "
                            "P(loss/yr) = 1 - exp(-G x 8766/MTTDL), G = groups in 10 PB usable on 30 TB drives. Independent failures; ignores UREs, "
                            "bugs, operator error. Reference AFRs: Backblaze 2025 HDD 1.36%; Backblaze SSD lifetime 0.9% (to mid-2023); Everpure DFM 0.15% "
                            "(company-stated). Data: data/ch20_durability.csv")
    fig.tight_layout(rect=(0, 0.11, 1, 1))
    return _style.save(fig, out_dir, NAME)
