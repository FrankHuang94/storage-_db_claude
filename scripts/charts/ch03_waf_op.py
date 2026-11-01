"""Ch03 — Illustrative model: write amplification factor (WAF) vs over-provisioning (OP).

build(out_dir) reads data/ch03_waf_op.csv and writes docs/assets/charts/ch03-waf-op.svg.

Two kinds of rows in the CSV, both illustrative (not vendor data):
  * Analytic model: uniform random single-page writes on a full drive, oldest-first (FIFO) cleaning,
    large erase blocks. A block survives one full pass of the log; during that pass the host writes
    N_phys * (1 - u) pages, each hitting a given LBA with probability 1 / N_user, so the fraction of
    a victim block still valid is u = exp(-(1 - u) * (1 + OP)) and WAF = 1 / (1 - u).
  * Simulation: a toy page-mapped FTL with greedy GC (victim = block with fewest valid pages),
    2,048 blocks x 128 pages. Re-create with:
        python3 scripts/charts/ch03_waf_op.py --resimulate   (about a minute on 4 cores)
"""
from __future__ import annotations

import csv
import math
import random
import sys
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch03_waf_op.csv"
NAME = "ch03-waf-op"
ANALYTIC = "Analytic model (FIFO fixed point)"
SERIES = {
    ANALYTIC: ("#0072B2", None, "-"),
    "Simulation: greedy GC, uniform random": ("#222222", "o", "none"),
    "Simulation: greedy GC, 80/20 skew, hot and cold mixed": ("#D55E00", "s", "--"),
}


def fifo_waf(op: float) -> float:
    """Solve u = exp(-(1-u)(1+OP)) by fixed-point iteration; return WAF = 1/(1-u)."""
    u = 0.5
    for _ in range(5000):
        u = math.exp(-(1 - u) * (1 + op))
    return 1 / (1 - u)


def _load() -> dict:
    out: dict = {}
    with CSV.open(newline="") as fh:
        for r in csv.DictReader(fh):
            out.setdefault(r["series"], []).append((float(r["op_pct"]), float(r["waf"])))
    return out


def build(out_dir: Path) -> Path:
    _style.apply()
    s = _load()
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    for name, (color, marker, ls) in SERIES.items():
        pts = sorted(s[name])
        label = name if name != ANALYTIC else "Analytic: WAF = 1/(1-u), u = exp(-(1-u)(1+OP))"
        ax.plot([p[0] for p in pts], [p[1] for p in pts], color=color, marker=marker, linestyle=ls,
                markersize=6, linewidth=2.2 if marker is None else 1.6, label=label)
    ax.axhline(1.0, color="#888888", linestyle=":", linewidth=1.2)
    ax.text(101, 0.88, "WAF = 1: host writes whole blocks sequentially (log-structured host, ZNS, FDP done well)",
            fontsize=9, color="#555555", ha="right", va="top")
    for x, label in ((7, "client\n~7%"), (14.5, "read-intensive\nenterprise ~14.5%"), (37, "mixed-use\nenterprise ~37%")):
        ax.axvline(x, color="#BBBBBB", linestyle="--", linewidth=1)
        ax.text(x + 1, 10.4, label, fontsize=9, color="#555555", va="top")
    ax.set_xlabel("Over-provisioning, % of user capacity  [(physical - user) / user]")
    ax.set_ylabel("Write amplification factor (NAND writes / host writes)")
    ax.set_xlim(0, 103)
    ax.set_ylim(0, 11)
    ax.legend(loc="upper right", bbox_to_anchor=(1.0, 0.72))
    ax.set_title("Illustrative model: under random writes, write amplification falls steeply with over-provisioning",
                 loc="left", fontsize=12.5)
    _style.source_note(fig, "Illustrative model, not vendor data. Uniform random single-page writes on a full drive; analytic curve "
                            "assumes oldest-first cleaning, simulation uses greedy GC (2,048 blocks x 128 pages). Skew = 80% of writes to "
                            "20% of LBAs. Excludes wear levelling, refresh, bad blocks, parity and TRIM. Data: data/ch03_waf_op.csv")
    fig.tight_layout()
    return _style.save(fig, out_dir, NAME)


# ---------------------------------------------------------------------------------------------
# Simulator used to generate the CSV (kept here so the numbers are reproducible).
BIG = 10 ** 9


def simulate(op: float, hot: tuple | None = None, sep: bool = False, P: int = 128, NB: int = 2048,
             mult: int = 10, warm: int = 4, seed: int = 7) -> float:
    import numpy as np
    rnd = random.Random(seed)
    U = int(NB * P / (1 + op))
    key = np.full(NB, BIG, dtype=np.int64)  # valid-page count for closed blocks, BIG otherwise
    valid = [0] * NB
    owner = [[-1] * P for _ in range(NB)]
    loc_b, loc_k = [-1] * U, [-1] * U
    free = list(range(NB))
    S = 2 if sep else 1
    openb: list = [free.pop() for _ in range(S)]
    fill = [0] * S
    state = {"count": False, "gcw": 0}
    hl = int(U * hot[1]) if hot else 0

    def stream(l: int) -> int:
        return (0 if l < hl else 1) if sep else 0

    def write(l: int, s: int, gcmode: bool) -> None:
        while openb[s] is None or fill[s] == P:
            if openb[s] is not None:
                key[openb[s]] = valid[openb[s]]
                openb[s] = None
            if not gcmode:
                while len(free) < S + 1:
                    gc()
            if openb[s] is None:
                openb[s] = free.pop()
                fill[s] = 0
        b, k = openb[s], fill[s]
        fill[s] += 1
        ob = loc_b[l]
        if ob >= 0:
            owner[ob][loc_k[l]] = -1
            valid[ob] -= 1
            if key[ob] != BIG:
                key[ob] -= 1
        owner[b][k] = l
        valid[b] += 1
        loc_b[l], loc_k[l] = b, k

    def gc() -> None:
        v = int(np.argmin(key))
        key[v] = BIG
        for l in [x for x in owner[v] if x >= 0]:
            write(l, stream(l), True)
            if state["count"]:
                state["gcw"] += 1
        owner[v] = [-1] * P
        free.append(v)

    for l in range(U):
        write(l, stream(l), False)
    host = 0
    for i in range(U * mult):
        if i == U * warm:
            state["count"] = True
        if hot:
            l = rnd.randrange(hl) if rnd.random() < hot[0] else hl + rnd.randrange(U - hl)
        else:
            l = rnd.randrange(U)
        write(l, stream(l), False)
        if state["count"]:
            host += 1
    return (host + state["gcw"]) / host


def _job(args):
    return simulate(*args)


def _job(args):
    return simulate(*args)


SIM_CFG = [("Simulation: greedy GC, uniform random", None, False),
           ("Simulation: greedy GC, 80/20 skew, hot and cold mixed", (0.8, 0.2), False),
           ("Simulation: greedy GC, 80/20 skew, hot and cold separated", (0.8, 0.2), True)]


def resimulate() -> None:
    """Re-run the greedy-GC simulation and rewrite its rows; analytic rows are recomputed too."""
    from multiprocessing import Pool
    ops = [0.07, 0.10, 0.15, 0.20, 0.28, 0.40, 0.50, 0.70, 1.00]
    jobs = [(o, h, sp) for _, h, sp in SIM_CFG for o in ops]
    with Pool() as p:
        res = p.map(_job, jobs)
    with CSV.open(newline="") as fh:
        rows = list(csv.DictReader(fh))
    ana_src = next(r["source"] for r in rows if r["series"] == ANALYTIC)
    sim_src = next(r["source"] for r in rows if r["series"] != ANALYTIC)
    ana_ops = sorted({float(r["op_pct"]) for r in rows if r["series"] == ANALYTIC})
    with CSV.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["op_pct", "series", "waf", "source", "as_of"])
        for o in ana_ops:
            w.writerow([f"{o:g}", ANALYTIC, round(fifo_waf(o / 100), 2), ana_src, "2026-11-01"])
        for i, o in enumerate(ops):
            for j, (name, _, _) in enumerate(SIM_CFG):
                w.writerow([round(o * 100), name, round(res[j * len(ops) + i], 2), sim_src, "2026-11-01"])


if __name__ == "__main__" and "--resimulate" in sys.argv:
    resimulate()
