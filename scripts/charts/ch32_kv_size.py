"""Ch32 — Worked example: KV-cache size per session and across a fleet of retained sessions.

Reads data/ch32_kv_size.csv (computed from published model configs; every row carries `source`
and `as_of`). Panel A: KV-cache GB per session vs context length for four model configs, with
DGX B200 HBM reference lines. Panel B: total KV for N retained 128K-token Llama 3 70B sessions vs
the HBM, DRAM and local-NVMe capacity of one DGX B200-class node. Writes docs/assets/charts/ch32-kv-size.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

import _style

CSV = _style.DATA / "ch32_kv_size.csv"
NAME = "ch32-kv-size"
MODEL_STYLE = {
    "DeepSeek-V3 671B (MLA)": ("#009E73", "D"),
    "Llama 3.1 8B (GQA)": ("#56B4E9", "^"),
    "Llama 3 70B (GQA)": ("#0072B2", "o"),
    "Llama 3.1 405B (GQA)": ("#D55E00", "s"),
}


def _load():
    a: dict = {}
    b: list = []
    refs: dict = {}
    with CSV.open(newline="") as fh:
        for r in csv.DictReader(fh):
            if r["panel"] == "A_per_session":
                a.setdefault(r["model"], []).append((int(r["context_tokens"]), float(r["kv_gb"]),
                                                     int(r["kv_bytes_per_token"])))
            elif r["panel"].startswith("B_"):
                b.append((int(r["sessions"]), float(r["kv_gb"])))
            else:
                refs[r["model"]] = float(r["kv_gb"])
    return a, sorted(b), refs


def _ctx_label(x, _pos=None):
    return f"{int(x / 1024)}K" if x < 1024 * 1024 else f"{int(x / (1024 * 1024))}M"


def _gb_label(y, _pos=None):
    if y >= 1e6:
        return f"{y / 1e6:g} PB"
    if y >= 1e3:
        return f"{y / 1e3:g} TB"
    return f"{y:g} GB"


def build(out_dir: Path) -> Path:
    _style.apply()
    a, b, refs = _load()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.0))

    # Panel A
    for model, (color, marker) in MODEL_STYLE.items():
        pts = sorted(a[model])
        kib = pts[0][2] / 1024
        ax1.plot([p[0] for p in pts], [p[1] for p in pts], color=color, marker=marker, markersize=5,
                 linewidth=2, label=f"{model}: {kib:,.1f} KiB/token")
    for key, label in (("ref_one_B200_HBM", "one B200 GPU HBM (180 GB)"),
                       ("ref_DGX_B200_HBM", "8-GPU DGX B200 HBM (1,440 GB)")):
        ax1.axhline(refs[key], color="#888888", linestyle=":", linewidth=1.3)
        ax1.text(8192, refs[key] * 1.12, label, fontsize=9, color="#555555")
    ax1.set_xscale("log", base=2)
    ax1.set_yscale("log")
    ax1.set_xticks([8192, 32768, 131072, 262144, 524288, 1048576])
    ax1.xaxis.set_major_formatter(FuncFormatter(_ctx_label))
    ax1.yaxis.set_major_formatter(FuncFormatter(_gb_label))
    ax1.set_ylim(0.4, 4000)
    ax1.set_xlabel("Context length per session (tokens)")
    ax1.set_ylabel("KV cache per session (fp16/bf16)")
    ax1.set_title("A. One session: KV grows linearly with context", fontsize=12)
    ax1.legend(loc="lower right", fontsize=8.5)

    # Panel B
    xs = [p[0] for p in b]
    ys = [p[1] for p in b]
    ax2.bar(range(len(xs)), ys, color="#0072B2", width=0.6)
    for i, y in enumerate(ys):
        ax2.text(i, y * 1.25, _gb_label(float(f"{y:.3g}")), ha="center", fontsize=9, color="#222222")
    for key, label, color in (("ref_DGX_B200_HBM", "one node: HBM 1.44 TB", "#D55E00"),
                              ("ref_DGX_B200_DRAM", "DRAM 2 TB", "#E69F00"),
                              ("ref_DGX_B200_NVMe", "local NVMe 30.7 TB", "#009E73")):
        ax2.axhline(refs[key], color=color, linestyle="--", linewidth=1.3)
        ax2.text(-0.45, refs[key] * (0.6 if key == "ref_DGX_B200_HBM" else 1.12), label, fontsize=9, color=color)
    ax2.set_yscale("log")
    ax2.set_xticks(range(len(xs)))
    ax2.set_xticklabels([f"{x:,}" for x in xs])
    ax2.yaxis.set_major_formatter(FuncFormatter(_gb_label))
    ax2.set_ylim(10, 2e7)
    ax2.set_xlabel("Retained sessions (Llama 3 70B, 128K tokens each)")
    ax2.set_ylabel("Total KV cache to keep warm")
    ax2.set_title("B. A fleet: retained context outgrows a node fast", fontsize=12)
    ax2.grid(axis="x", visible=False)

    fig.suptitle("Worked example: KV-cache bytes = 2 (K,V) × layers × KV heads × head_dim × bytes per value",
                 fontsize=13, fontweight="bold", x=0.01, ha="left")
    _style.source_note(fig, "Worked example from published model configs (meta-llama/llama-models; deepseek-ai/DeepSeek-V3). "
                            "fp16/bf16 KV; fp8 KV halves every value. Llama 3.x configs natively support 128K; longer contexts "
                            "are hypothetical. Node references: NVIDIA DGX B200 spec. Activations and weights ignored. "
                            "Data: data/ch32_kv_size.csv")
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    return _style.save(fig, out_dir, NAME)
