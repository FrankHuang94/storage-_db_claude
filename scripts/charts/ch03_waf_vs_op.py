"""Ch03 — Illustrative simulation: write amplification factor (WAF) vs over-provisioning (OP).

build(out_dir) reads data/ch03_waf_vs_op.csv and writes docs/assets/charts/ch03-waf-vs-op.svg.
The CSV was produced by simulate() below (a toy page-mapped FTL with greedy garbage collection);
re-create it with:  python3 scripts/charts/ch03_waf_vs_op.py --resimulate   (takes ~1 min on 4 cores).
All assumptions are stated in the CSV `source` column and in the chart footnote. Not vendor data.
"""
from __future__ import annotations

import csv
import random
import sys
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch03_waf_vs_op.csv"
NAME = "ch03-waf-vs-op"
SERIES = {
    "Uniform random writes": ("#0072B2", "o", "-"),
    "Skewed 80/20, hot and cold mixed": ("#D55E00", "s", "-"),
    "Skewed 80/20, hot and cold separated": ("#009E73", "^", "--"),
}


def _load() -> dict:
    out: dict = {}
    with CSV.open(newline="") as fh:
        for r in csv.DictReader(fh):
            out.setdefault(r["workload"], []).append((float(r["op_pct"]), float(r["waf"])))
    return out


def build(out_dir: Path) -> Path:
    _style.apply()
    s = _load()
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    for name, (color, marker, ls) in SERIES.items():
        pts = sorted(s[name])
        ax.plot([p[0] for p in pts], [p[1] for p in pts], color=color, marker=marker, linestyle=ls,
                markersize=5, linewidth=2, label=name)
    ax.axhline(1.0, color="#888888", linestyle=":", linewidth=1.2)
    ax.text(101, 1.05, "WAF = 1: whole-block sequential writes\n(the target of ZNS, FDP and log-structured hosts)",
            fontsize=9, color="#555555", ha="right", va="bottom")
    for x, label in ((7, "client / read-\nintensive ~7%"), (28, "mixed-use\n~28%")):
        ax.axvline(x, color="#BBBBBB", linestyle="--", linewidth=1)
        ax.text(x + 1, 7.6, label, fontsize=9, color="#555555", va="top")
    ax.set_xlabel("Over-provisioning, % of user capacity  [(physical - user) / user]")
    ax.set_ylabel("Write amplification factor (NAND writes / host writes)")
    ax.set_xlim(0, 103)
    ax.set_ylim(0, 8.2)
    ax.legend(loc="upper right", bbox_to_anchor=(1.0, 0.82))
    ax.set_title("Illustrative simulation: write amplification falls steeply as over-provisioning rises",
                 loc="left", fontsize=13)
    _style.source_note(fig, "Illustrative model, not vendor data. Toy page-mapped FTL, greedy GC, 2,048 blocks x 128 pages, "
                            "single-page random host writes on a full drive; skewed = 80% of writes to 20% of LBAs. Excludes "
                            "wear leveling, refresh, bad blocks and parity. Data: data/ch03_waf_vs_op.csv")
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


def resimulate() -> None:
    from multiprocessing import Pool
    ops = [0.07, 0.10, 0.15, 0.20, 0.28, 0.40, 0.50, 0.70, 1.00]
    cfg = [("Uniform random writes", None, False), ("Skewed 80/20, hot and cold mixed", (0.8, 0.2), False),
           ("Skewed 80/20, hot and cold separated", (0.8, 0.2), True)]
    jobs = [(o, h, sp) for _, h, sp in cfg for o in ops]
    with Pool() as p:
        res = p.map(_job, jobs)
    with CSV.open(newline="") as fh:
        src = next(csv.DictReader(fh))["source"]
    with CSV.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["op_pct", "workload", "waf", "source", "as_of"])
        for i, o in enumerate(ops):
            for j, (name, _, _) in enumerate(cfg):
                w.writerow([round(o * 100), name, round(res[j * len(ops) + i], 2), src, "2026-11-01"])


if __name__ == "__main__" and "--resimulate" in sys.argv:
    resimulate()
