"""Ch31 — Worked example: checkpoint size vs model size (weights-only vs on-disk checkpoint vs full training state).

All values are atlas arithmetic, not measurements:
  size_bytes = parameters x bytes_per_parameter
  weights-only (bf16)                 = 2 B/param
  typical on-disk checkpoint          = 14 B/param (bf16 weights 2 + fp32 master 4 + Adam m 4 + Adam v 4; gradients not saved)
  full in-GPU training state          = 16 B/param (the above + bf16 gradients 2)
Reads data/ch31_checkpoint_size.csv (params_billion and bytes-per-param columns); recomputes every size
from those inputs and checks the stored TB columns. Run this file with --write-csv to regenerate the CSV.
Writes docs/assets/charts/ch31-checkpoint-size.svg.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch31_checkpoint_size.csv"
NAME = "ch31-checkpoint-size"
MODELS = [("70B", 70), ("405B", 405), ("1T", 1000), ("2T", 2000)]
LAYERS = [  # (column, label, bytes per parameter, colour)
    ("weights_bf16_tb", "Weights only, bf16 (2 B/param)", 2, "#56B4E9"),
    ("checkpoint_on_disk_tb", "Typical saved checkpoint (14 B/param)", 14, "#0072B2"),
    ("full_training_state_tb", "Full in-GPU training state (16 B/param)", 16, "#D55E00"),
]
WINDOW_S = 60
SOURCE = ("Atlas worked example: size = parameters x bytes/param (bf16 weights 2, fp32 master 4, Adam m 4, Adam v 4, "
          "bf16 grads 2); write rate = full state / 60 s. Not a measurement.")


def compute() -> list[dict]:
    rows = []
    for name, pb in MODELS:
        r = {"model": name, "params_billion": pb}
        for col, _, b, _ in LAYERS:
            r[col] = round(pb * 1e9 * b / 1e12, 3)
        r["write_gbps_full_state_60s"] = round(r["full_training_state_tb"] * 1000 / WINDOW_S, 1)
        r["source"] = SOURCE
        r["as_of"] = "2026-11-01"
        rows.append(r)
    return rows


def write_csv() -> None:
    rows = compute()
    with CSV.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def _load() -> list[dict]:
    with CSV.open(newline="") as fh:
        rows = list(csv.DictReader(fh))
    for r in rows:
        pb = float(r["params_billion"])
        for col, _, b, _ in LAYERS:
            calc = pb * 1e9 * b / 1e12
            assert abs(calc - float(r[col])) < 1e-3, f"{r['model']} {col}: CSV {r[col]} != computed {calc}"
            r[col] = calc
    return rows


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    fig, ax = plt.subplots(figsize=(9.8, 5.4))
    n = len(LAYERS)
    width = 0.26
    xs = range(len(rows))
    for i, (col, label, _, colour) in enumerate(LAYERS):
        pos = [x + (i - (n - 1) / 2) * width for x in xs]
        vals = [r[col] for r in rows]
        ax.bar(pos, vals, width=width, color=colour, label=label)
        for p, v in zip(pos, vals):
            ax.text(p, v * 1.12, f"{v:,.2f}" if v < 10 else f"{v:,.0f}", ha="center", va="bottom", fontsize=9,
                    color=_style.TEXT)
    ax.set_yscale("log")
    ax.set_ylim(0.08, 120)
    ax.set_yticks([0.1, 1, 10, 100])
    ax.set_yticklabels(["0.1 TB", "1 TB", "10 TB", "100 TB"])
    ax.set_xticks(list(xs))
    ax.set_xticklabels([f"{r['model']} parameters\nfull state in 60 s\n= {float(r['write_gbps_full_state_60s']):,.0f} GB/s"
                        for r in rows], fontsize=10)
    ax.set_ylabel("Size (decimal TB, log scale)")
    ax.legend(loc="upper left", fontsize=10)
    ax.set_title("Worked example: checkpoint size by model size, mixed-precision Adam", loc="left", fontsize=12.5)
    _style.source_note(fig, "Atlas arithmetic, not measured. Size = parameters x bytes/parameter. 14 B/param = bf16 weights 2 + fp32 master "
                            "weights 4 + Adam first moment 4 + Adam second moment 4; 16 B/param adds bf16 gradients 2 (held in GPU memory, "
                            "usually not saved). Dense or MoE: size follows total, not active, parameters. Data: data/ch31_checkpoint_size.csv")
    fig.tight_layout()
    return _style.save(fig, out_dir, NAME)


if __name__ == "__main__":
    if "--write-csv" in sys.argv:
        write_csv()
        print(f"wrote {CSV}")
