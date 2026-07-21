from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path

from writing_audit.agents import run_agent
from writing_audit.metrics import compute_metrics
from writing_audit.prose import extract_draft

# ---------------------------------------------------------------------------
# Track R — red-team BOUNDARY-MAPPING harness (research only; never ships).
#
# Purpose (per docs/notes/pangram-audit/track-r-redteam-protocol.md):
#   NOT to produce a corpus of undetectable machine text. The deliverable is a
#   CHARACTERIZATION: for a given input, run an ablation of single-lever
#   perturbations, emit each variant as an INDEPENDENTLY SCOREABLE cell, and
#   record provenance so the eventual disclosure to Pangram reports a *rate*
#   with a denominator and a per-stage P(AI) curve — not a highlight reel.
#
# Design invariants that keep this a characterization, not an exploit:
#   * Every variant is logged in manifest.json with the exact lever applied.
#   * Stages are emitted separately (not just the final laundered text) so the
#     ablation question "which lever moved P(AI), at what semantic cost?" is
#     answerable.
#   * The human-in-the-loop lever is a STUB slot the author fills by hand; the
#     harness never fabricates human tokens and flags any human-injected cell so
#     "fully machine-generated" claims stay honest.
#   * A fidelity slot per cell must be certified by an INDEPENDENT evaluator
#     (charter: generator != reviewer) before any "no drift" claim is made.
# ---------------------------------------------------------------------------

# Single-lever perturbations. Each is applied to the SAME base prose so their
# effects can be compared independently (ablation), rather than stacked blindly.
LEVERS: dict[str, str] = {
    "L0-identity": "",  # control: base prose unchanged, re-scored for baseline P(AI)
    "L1-detell": (
        "Rewrite this economics prose to remove predictable LLM token patterns "
        "(stock academic phrases, uniform sentence openings) while preserving "
        "every number, date, citation, and factual claim EXACTLY. Do not hedge, "
        "soften, or add filler. Output ONLY the prose.\n\nPROSE:\n"
    ),
    "L2-restructure": (
        "Structurally re-encode this prose: reorder clauses, split long "
        "sentences, merge short ones, swap active/passive where meaning is "
        "preserved. Change NO number, proper noun, or claim. Do not soften the "
        "argument. Output ONLY the prose.\n\nPROSE:\n"
    ),
    "L3-crossmodel": (
        "Paraphrase this prose end to end in a different register-neutral voice, "
        "as if a different author reconstructed it from notes. Preserve every "
        "fact and number. Output ONLY the prose.\n\nPROSE:\n"
    ),
    # L4 is deliberately NOT an agent lever. It is a manual human-encoding slot.
    "L4-human": "__HUMAN_STUB__",
}


@dataclass
class CellRecord:
    cell_id: str
    lever: str
    lever_desc: str
    source_input: str
    reviser: str | None
    human_injected: bool
    variant_path: str
    words: int
    # Filled in by hand after scoring:
    pangram_version: str = ""
    pangram_verdict: str = ""  # "AI" | "Human" | "Mixed" | ""
    pangram_confidence: str = ""  # "High" | "Low" | ""
    pangram_p_ai: str = ""  # raw prediction_prob, as string; blank until scored
    fidelity_verdict: str = ""  # independent evaluator: "faithful" | "drift" | ""
    fidelity_evaluator: str = ""  # who/what certified fidelity (NOT the generator)
    notes: str = ""


@dataclass
class TrackRRun:
    input_path: Path
    outdir: Path
    manifest_path: Path
    worksheet_path: Path
    cells: list[CellRecord]


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _log(outdir: Path, message: str) -> None:
    line = f"[track-r] {message}"
    print(line)
    with (outdir / "run.log").open("a") as handle:
        handle.write(line + "\n")


def _wordcount(text: str) -> int:
    return len(extract_draft(text).split())


def run_track_r(
    input_path: Path,
    *,
    reviser: str = "claude",
    levers: list[str] | None = None,
) -> TrackRRun:
    """Emit one independently-scoreable cell per single-lever perturbation.

    No stacking, no 'final' laundered artifact. The output is a scoring
    worksheet + provenance manifest for the boundary-map ablation.
    """
    input_path = input_path.resolve()
    if not input_path.is_file():
        raise FileNotFoundError(input_path)

    selected = levers or list(LEVERS.keys())
    root = _repo_root()
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    basename = input_path.stem
    outdir = root / "docs/notes/pangram-audit/track-r-runs" / f"{basename}-{stamp}"
    outdir.mkdir(parents=True, exist_ok=True)

    _log(outdir, f"Input: {input_path}")
    _log(outdir, f"Levers: {', '.join(selected)}")
    _log(outdir, f"Reviser: {reviser}")
    _log(outdir, "Ablation mode: one lever per cell, no stacking.")

    base_raw = input_path.read_text()
    base_prose = extract_draft(base_raw) or base_raw
    (outdir / "00-base.md").write_text(base_prose)

    cells: list[CellRecord] = []
    for lever in selected:
        if lever not in LEVERS:
            _log(outdir, f"Unknown lever '{lever}' — skipped.")
            continue
        template = LEVERS[lever]
        cell_id = f"{basename}::{lever}"
        variant_path = outdir / f"cell-{lever}.md"

        if lever == "L0-identity":
            variant_path.write_text(base_prose)
            cells.append(
                CellRecord(
                    cell_id=cell_id, lever=lever, lever_desc="control (unchanged)",
                    source_input=str(input_path), reviser=None, human_injected=False,
                    variant_path=str(variant_path), words=_wordcount(base_prose),
                    notes="Baseline P(AI) for this input; anchors the ablation.",
                )
            )
            _log(outdir, f"{lever}: wrote control cell.")
            continue

        if template == "__HUMAN_STUB__":
            variant_path.write_text(
                "<!-- L4-human: AUTHOR fills this by hand with a genuine human "
                "re-encoding of 00-base.md. Leave empty to skip. This cell is "
                "flagged human_injected=true and MUST NOT be reported as "
                "'fully machine-generated'. -->\n"
            )
            cells.append(
                CellRecord(
                    cell_id=cell_id, lever=lever,
                    lever_desc="manual human-encoding slot (author-filled)",
                    source_input=str(input_path), reviser=None, human_injected=True,
                    variant_path=str(variant_path), words=0,
                    notes="STUB. Not machine-generated. The likely dominant lever "
                          "per prior data — run last, report separately.",
                )
            )
            _log(outdir, f"{lever}: wrote human stub (author to fill).")
            continue

        prompt = f"{template}{base_prose}"
        if run_agent(reviser, prompt, variant_path):
            variant_prose = variant_path.read_text().strip()
            variant_path.write_text(variant_prose)
            _log(outdir, f"{lever}: OK via {reviser}.")
        else:
            variant_path.write_text(base_prose)
            _log(outdir, f"{lever}: agent unavailable — control copy written.")
        cells.append(
            CellRecord(
                cell_id=cell_id, lever=lever,
                lever_desc=template.split(".")[0][:80],
                source_input=str(input_path), reviser=reviser, human_injected=False,
                variant_path=str(variant_path), words=_wordcount(variant_path.read_text()),
            )
        )
        m = compute_metrics(variant_path)
        (outdir / f"metrics-{lever}.txt").write_text(m.format() + "\n")

    manifest_path = outdir / "manifest.json"
    manifest_path.write_text(
        json.dumps(
            {
                "input": str(input_path),
                "created_utc": datetime.utcnow().isoformat() + "Z",
                "reviser": reviser,
                "ablation": True,
                "cells": [asdict(c) for c in cells],
            },
            indent=2,
        )
    )

    worksheet_path = outdir / "SCORING-WORKSHEET.md"
    _write_worksheet(worksheet_path, input_path, cells)

    _log(outdir, f"Wrote manifest: {manifest_path}")
    _log(outdir, f"Wrote worksheet: {worksheet_path}")
    _log(outdir, "Next: score EVERY cell on Pangram (record the denominator), "
                 "fill P(AI)+fidelity in the worksheet, then update manifest.")
    return TrackRRun(
        input_path=input_path, outdir=outdir, manifest_path=manifest_path,
        worksheet_path=worksheet_path, cells=cells,
    )


def _write_worksheet(path: Path, input_path: Path, cells: list[CellRecord]) -> None:
    lines = [
        f"# Track R scoring worksheet — {input_path.stem}",
        "",
        "**Rule: score EVERY cell below, including controls and failures.** "
        "The disclosure claim is a *rate* (false-Human / total machine cells), "
        "not a highlight reel. Do not delete rows that scored AI.",
        "",
        "**Provenance:** cells with `human_injected=true` are NOT machine-generated "
        "and must be reported separately. Fidelity must be certified by an "
        "evaluator that is NOT the generating model.",
        "",
        "| cell | lever | machine? | words | Pangram ver | verdict | conf | P(AI) | fidelity | evaluator |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for c in cells:
        machine = "no" if c.human_injected else "yes"
        lines.append(
            f"| {c.lever} | {c.lever_desc[:40]} | {machine} | {c.words} | "
            f"{c.pangram_version or '___'} | {c.pangram_verdict or '___'} | "
            f"{c.pangram_confidence or '___'} | {c.pangram_p_ai or '___'} | "
            f"{c.fidelity_verdict or '___'} | {c.fidelity_evaluator or '___'} |"
        )
    lines += [
        "",
        "## Denominator (fill after scoring)",
        "- Machine cells scored: ___",
        "- Machine cells returning **Human**: ___",
        "- False-Human rate: ___% (with 95% interval if n allows)",
        "- Of the Human-scoring cells, how many passed independent fidelity: ___",
        "",
        "## Which lever moved P(AI)? (the actual finding)",
        "- Baseline (L0) P(AI): ___",
        "- Largest single-lever delta: lever ___, ΔP(AI) ___",
        "- Any fully-machine cell that flipped to Human without drift? ___ "
        "(if yes: verify it is not near-extractive copying of the human source)",
        "",
    ]
    path.write_text("\n".join(lines))
