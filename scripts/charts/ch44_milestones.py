"""Ch44 — DDN revenue as reported, 2003–2026, with corporate milestones.

DDN is private: every point is company-stated, a trade-press estimate or a press report,
and the 2023–2025 figures conflict between sources. Reads data/ch44_milestones.csv
(every row carries `basis`, `source` and `as_of`). Writes docs/assets/charts/ch44-milestones.svg.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt

import _style

CSV = _style.DATA / "ch44_milestones.csv"
NAME = "ch44-milestones"
DDN = "#CC79A7"
STYLES = {
    "company-stated (historic)": dict(marker="o", color=DDN, label="Company-stated (historic interviews / statements)"),
    "trade-press estimate (Blocks & Files)": dict(marker="s", color="#E69F00", label="Trade-press figure or estimate (Blocks & Files, Jan 2025)"),
    "reported by press (Forbes 2026)": dict(marker="D", color="#0072B2", label="Reported by press (Forbes, Aug 2026)"),
    "company target reported by press (Forbes 2026)": dict(marker="*", color="#D55E00", label="2026 target reported by Forbes (not an actual)"),
}
MILESTONES = [
    (2002, "2002: founders buy\nout venture investors"),
    (2018.5, "2018: Intel Lustre team\n(Whamcloud), Tintri"),
    (2025.03, "Jan 2025: Blackstone\n\\$300M at \\$5B"),
]


def _load() -> list[dict]:
    with CSV.open(newline="") as fh:
        return list(csv.DictReader(fh))


def build(out_dir: Path) -> Path:
    _style.apply()
    rows = _load()
    fig, ax = plt.subplots(figsize=(11, 5.4))
    seen = set()
    for r in rows:
        st = STYLES[r["basis"]]
        x, y = float(r["year"]), float(r["value_musd"])
        kw = dict(marker=st["marker"], color=st["color"], s=170 if st["marker"] == "*" else 70, zorder=3)
        if r["basis"] not in seen:
            kw["label"] = st["label"]
            seen.add(r["basis"])
        ax.scatter([x], [y], **kw)
        dx = -0.35 if r["label"] == "$400M" and x == 2024 else 0.25
        ha = "right" if dx < 0 else "left"
        ax.text(x + dx, y + 18, r["label"], fontsize=9, ha=ha, va="bottom", color="#222222")
    # connect the Forbes-reported series and target
    fx = [float(r["year"]) for r in rows if "Forbes" in r["basis"]]
    fy = [float(r["value_musd"]) for r in rows if "Forbes" in r["basis"]]
    ax.plot(fx, fy, color="#0072B2", linewidth=1, linestyle="--", zorder=2)
    for x, txt in MILESTONES:
        ax.axvline(x, color="#999999", linewidth=0.8, linestyle=":", zorder=1)
        ax.text(x - 0.2, 1080, txt, fontsize=8.5, color="#555555", ha="right", va="top")
    ax.set_xlim(2001, 2027.2)
    ax.set_ylim(0, 1120)
    ax.set_xticks([2003, 2005, 2010, 2015, 2020, 2023, 2026])
    ax.set_ylabel("Annual revenue (US$ millions)")
    ax.set_title("DDN revenue as reported, 2003–2026: a private company with conflicting public figures",
                 loc="left", fontsize=12.5)
    ax.legend(loc="center left", fontsize=8.5, bbox_to_anchor=(0.0, 0.55))
    ax.grid(axis="x", visible=False)
    _style.source_note(fig, "Sources: The Register 2014-06-30 (2003, 2005, 2010); Blocks & Files 2025-01-09 (2020 company "
                            "statement; 2023 figure and 2024 estimate); Forbes 2026-08-06 via syndicated copies (2024, 2025, "
                            "2026 target). None are audited. 2023–2025 sources disagree. Data: data/ch44_milestones.csv")
    fig.tight_layout()
    return _style.save(fig, out_dir, NAME)
