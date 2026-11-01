"""Ch02 — 3D NAND layer count by year (leading announced/production parts).

Reads data/ch02_nand_layers.csv. Rows with status 'sourced' are drawn as filled markers;
rows with status 'background' (not verified this session) are drawn hollow and grey and are
labelled as background-only in the legend. Writes docs/assets/charts/ch02-nand-layers.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch02_nand_layers.csv"
NAME = "ch02-nand-layers"
# label offsets (dx years, dy layers) to avoid collisions
OFFSETS = {
    "Samsung 24L (first V-NAND)": (-0.8, 70), "48L": (-0.1, 22), "64L": (-0.2, 22), "96L": (-0.3, 22),
    "Micron 176L": (-1.5, 22), "Micron 232L": (-2.6, 10), "SK hynix 238L": (-2.2, 38),
    "Samsung V9 (~286L)": (-3.3, 20), "SK hynix 321L (mass production Nov 2024)": (-5.6, 62),
    "Micron G9 276L": (0.15, -38), "Kioxia/Sandisk BiCS10 332L": (-4.4, 24), "Samsung V10 (400+L)": (-3.2, 22),
}


def _load() -> list[dict]:
    with CSV.open(newline="") as fh:
        return list(csv.DictReader(fh))


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    fig, ax = plt.subplots(figsize=(10, 5.2))
    # envelope: running maximum of layers across all rows
    best: dict[int, int] = {}
    for r in rows:
        y, n = int(r["year"]), int(r["layers"])
        best[y] = max(best.get(y, 0), n)
    ys = sorted(best)
    run, env = 0, []
    for y in ys:
        run = max(run, best[y])
        env.append(run)
    ax.step(ys, env, where="post", color="#BBBBBB", linewidth=1.2, zorder=1)
    plotted = set()
    for r in rows:
        x, n, lab = int(r["year"]), int(r["layers"]), r["label"]
        if r["status"] == "sourced":
            kw = dict(color="#0072B2", markerfacecolor="#0072B2", label="Sourced (2024–26 press/vendor)")
        else:
            kw = dict(color="#888888", markerfacecolor="white", label="Background only (not verified this session)")
        lbl = kw.pop("label")
        ax.plot([x], [n], marker="o", markersize=8, linestyle="none", zorder=3,
                label=None if lbl in plotted else lbl, **kw)
        plotted.add(lbl)
        dx, dy = OFFSETS.get(lab, (0.2, 15))
        ax.annotate(lab, (x, n), xytext=(x + dx, n + dy), fontsize=9,
                    color="#222222" if r["status"] == "sourced" else "#777777",
                    arrowprops=dict(arrowstyle="-", color="#BBBBBB", lw=0.6))
    ax.set_xlim(2012, 2027.3)
    ax.set_ylim(0, 470)
    ax.set_xlabel("Year of announcement or volume production")
    ax.set_ylabel("Word-line layers")
    ax.legend(loc="upper left")
    ax.set_title("3D NAND layer count, 2013–2026: roughly 17× in 13 years", loc="left")
    _style.source_note(fig, "Sources: Blocks & Files (SK hynix 321L, 2024-11-21); Tom's Hardware (Micron G9, Kioxia/Sandisk BiCS10, "
                            "Samsung V10, 2026). Hollow grey points are background-only and unverified. Layer count is not bit density: "
                            "BiCS10 (332L) reportedly out-densities 400L+ parts. Data: data/ch02_nand_layers.csv")
    fig.tight_layout()
    return _style.save(fig, out_dir, NAME)
