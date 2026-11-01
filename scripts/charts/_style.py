"""Shared chart style. Okabe–Ito colorblind-safe palette (see meta/style-guide.md)."""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"

PALETTE = ["#0072B2", "#E69F00", "#009E73", "#CC79A7", "#D55E00", "#56B4E9", "#F0E442", "#999999"]
VENDOR_COLORS = {
    "Everpure": "#0072B2", "Pure Storage": "#0072B2", "VAST": "#E69F00", "VAST Data": "#E69F00",
    "WEKA": "#009E73", "DDN": "#CC79A7", "Dell": "#56B4E9", "NetApp": "#D55E00", "HPE": "#999999",
}
TEXT = "#222222"
GRID = "#DDDDDD"


def apply() -> None:
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 11,
        "axes.edgecolor": "#888888",
        "axes.labelcolor": TEXT,
        "axes.titleweight": "bold",
        "axes.titlesize": 13,
        "axes.grid": True,
        "grid.color": GRID,
        "grid.linewidth": 0.6,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.prop_cycle": matplotlib.cycler(color=PALETTE),
        "xtick.color": TEXT,
        "ytick.color": TEXT,
        "legend.frameon": False,
        "figure.dpi": 110,
        "svg.fonttype": "none",
        "savefig.bbox": "tight",
        "savefig.facecolor": "white",
    })


def source_note(fig, text: str) -> None:
    """Add a small source line at the bottom-left of the figure."""
    fig.text(0.01, -0.02, text, fontsize=8, color="#555555", ha="left", va="top", wrap=True)


def save(fig, out_dir: Path, name: str) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{name}.svg"
    fig.savefig(path, format="svg", metadata={"Date": None})
    plt.close(fig)
    return path
