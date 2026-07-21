"""Render the prose-moves graph (bipartite moves <-> papers) as a figure.

The graph is a research aid for taste calibration, not a generator. Its point is the
*degree* of each move-node across mined intros — and, just as loudly, the empty
negative-control slot: with only published (successful) papers, degree measures genre
compliance, not taste. The renderer draws the control band even when empty so the missing
counterfactual is visible rather than implied.

Run: `uv run prose-graph-viz` (reads/writes next to the notes file by default).
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.patches as mpatches  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
DEFAULT_DATA = REPO / "docs/notes/taste-probes/prose-moves-graph.json"
DEFAULT_OUT = REPO / "docs/notes/taste-probes/prose-moves-graph.png"

# degree -> (fill, label) ; degree here counts only published papers
DEGREE_STYLE = {
    3: ("#b03a2e", "spine (all 3 — genre law?)"),
    2: ("#d68910", "shared (2 — probably genre)"),
    1: ("#95a5a6", "candidate (1 — unverified)"),
}
BAND_Y = {"published": 0.72, "control": 0.20}


def _degree(move: dict, published_ids: set[str]) -> int:
    return sum(1 for p in move["papers"] if p in published_ids)


def render(data: dict, out: Path) -> Path:
    papers = data["papers"]
    moves = data["moves"]
    published = [p for p in papers if p["band"] == "published"]
    controls = [p for p in papers if p["band"] == "control"]
    pub_ids = {p["id"] for p in published}

    # positions
    px = 0.82
    paper_pos: dict[str, tuple[float, float]] = {}
    for band, band_papers in (("published", published), ("control", controls)):
        n = max(len(band_papers), 1)
        span = 0.16 * (n - 1)
        y0 = BAND_Y[band] + span / 2
        for i, p in enumerate(band_papers):
            paper_pos[p["id"]] = (px, y0 - i * 0.16)

    moves_sorted = sorted(moves, key=lambda m: (-_degree(m, pub_ids), m["id"]))
    mx = 0.30
    top, bot = 0.88, 0.18
    step = (top - bot) / max(len(moves_sorted) - 1, 1)
    move_pos = {m["id"]: (mx, top - i * step) for i, m in enumerate(moves_sorted)}

    fig, ax = plt.subplots(figsize=(13.5, 8.6))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    band_of = {p["id"]: p["band"] for p in papers}

    # edges
    for m in moves_sorted:
        deg = _degree(m, pub_ids)
        mxp, myp = move_pos[m["id"]]
        is_spine = deg == 3
        for pid in m["papers"]:
            if pid not in paper_pos:
                continue
            pxp, pyp = paper_pos[pid]
            if band_of.get(pid) == "control":  # AI/control edge — teal dashed, never counted
                ax.plot([mxp + 0.008, pxp - 0.05], [myp, pyp],
                        color="#138d75", lw=1.8, ls=(0, (4, 2)), zorder=2, alpha=0.95)
            else:
                ax.plot([mxp + 0.008, pxp - 0.05], [myp, pyp],
                        color="#b03a2e" if is_spine else "#c8ccd0",
                        lw=2.1 if is_spine else 1.0,
                        zorder=1, alpha=0.9 if is_spine else 0.7)

    # move nodes
    for m in moves_sorted:
        deg = _degree(m, pub_ids)
        fill, _ = DEGREE_STYLE[deg]
        x, y = move_pos[m["id"]]
        ax.scatter([x], [y], s=140 + deg * 190, color=fill, zorder=3,
                   edgecolors="white", linewidths=1.4)
        ax.text(x - 0.03, y, m["id"], ha="right", va="center", fontsize=10.5,
                color="#1c2833", fontfamily="DejaVu Sans")

    # paper nodes
    for p in papers:
        x, y = paper_pos[p["id"]]
        ptype = p.get("ptype")
        if ptype == "placeholder":
            box = mpatches.FancyBboxPatch(
                (x - 0.045, y - 0.05), 0.20, 0.10,
                boxstyle="round,pad=0.012", linewidth=1.6, linestyle="--",
                edgecolor="#c0392b", facecolor="none", zorder=2)
            ax.add_patch(box)
            ax.text(x + 0.055, y + 0.015, p["label"], ha="center", va="center",
                    fontsize=9.5, color="#c0392b", fontweight="bold")
            ax.text(x + 0.055, y - 0.022, f"({p['subfield']})", ha="center", va="center",
                    fontsize=8.5, color="#c0392b", style="italic")
        elif p["band"] == "control":  # AI draft
            box = mpatches.FancyBboxPatch(
                (x - 0.045, y - 0.05), 0.20, 0.10,
                boxstyle="round,pad=0.012", linewidth=1.6,
                edgecolor="#138d75", facecolor="#e8f6f3", zorder=2)
            ax.add_patch(box)
            ax.text(x + 0.055, y + 0.015, p["label"], ha="center", va="center",
                    fontsize=9.3, color="#0e6251", fontweight="bold")
            ax.text(x + 0.055, y - 0.022, p["subfield"], ha="center", va="center",
                    fontsize=8.3, color="#148f77", style="italic")
        else:
            box = mpatches.FancyBboxPatch(
                (x - 0.045, y - 0.05), 0.20, 0.10,
                boxstyle="round,pad=0.012", linewidth=1.4,
                edgecolor="#34495e", facecolor="#eaf0f6", zorder=2)
            ax.add_patch(box)
            ax.text(x + 0.055, y + 0.014, p["label"], ha="center", va="center",
                    fontsize=10, color="#1c2833", fontweight="bold")
            ax.text(x + 0.055, y - 0.022, p["subfield"], ha="center", va="center",
                    fontsize=8.5, color="#5d6d7e")

    # band labels
    ax.text(px + 0.055, 0.975, "PUBLISHED  (top-5, selection-on-success)",
            ha="center", fontsize=9.5, color="#34495e", fontweight="bold")
    ax.text(px + 0.055, 0.40, "NEGATIVE CONTROL  (human-vs-AI axis)", ha="center",
            fontsize=9.5, color="#0e6251", fontweight="bold")
    ax.text(0.30, 0.965, "MOVES  (node size = degree)", ha="center", fontsize=9.5,
            color="#34495e", fontweight="bold")

    # the point, spelled out
    ax.annotate(
        "AI draft (teal, dashed) reproduces the spine + both genre moves →\n"
        "high degree ≠ human taste. Only enumerated-gaps & the\n"
        "rhetorical-question pivot stay human-only (the real signal).",
        xy=(px - 0.05, 0.28), xytext=(0.40, 0.045),
        fontsize=9.3, color="#0e6251", ha="left", va="center",
        arrowprops=dict(arrowstyle="->", color="#138d75", lw=1.4))

    # legend
    handles = [mpatches.Patch(color=DEGREE_STYLE[d][0], label=DEGREE_STYLE[d][1])
               for d in (3, 2, 1)]
    handles.append(Line2D([], [], color="#138d75", ls="--", lw=1.8,
                          label="AI draft reproduces move"))
    ax.legend(handles=handles, loc="lower left", bbox_to_anchor=(-0.02, -0.04),
              fontsize=8.8, frameon=False, title="move degree", title_fontsize=9)

    fig.suptitle("Prose-moves graph — N=3 published econ intros",
                 fontsize=15, fontweight="bold", y=0.985)
    ax.text(0.30, 0.005, "≈ Swales CARS (1990): establish territory → niche → occupy. "
            "Use as audit/anti-move critic, not a drafting template.",
            ha="center", fontsize=8.6, color="#5d6d7e", style="italic")

    fig.savefig(out, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description="Render the prose-moves graph figure.")
    ap.add_argument("--data", type=Path, default=DEFAULT_DATA)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args()
    data = json.loads(args.data.read_text())
    out = render(data, args.out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
