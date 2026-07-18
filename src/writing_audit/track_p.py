from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from writing_audit.agents import run_agent
from writing_audit.metrics import compute_metrics
from writing_audit.prose import extract_draft

STAGE1_PROMPT = """You rewrite academic economics prose to reduce predictable LLM token patterns while preserving every factual claim and number exactly.

Rules:
- Keep all numbers, dates, and citations unchanged.
- Vary sentence openings aggressively; break periodic sentences.
- Inject one very short sentence at an argumentative pivot.
- Remove stock academic phrases; replace with plain verbs.
- Do NOT add hedging or filler.
- Output ONLY the rewritten prose — no preamble.

PROSE:
"""

STAGE2_PROMPT = """You are a structural scrambler. Reorder clauses within paragraphs, split long sentences, merge short ones, and swap active/passive where meaning is preserved.

Hard constraints:
- Do NOT change any number, proper noun, or factual claim.
- Do NOT soften the argument.
- Output ONLY the rewritten prose.

PROSE:
"""

STAGE3_PROMPT = """Final pass: make the prose read like a human economist wrote it in one sitting — slightly uneven rhythm, one colloquial grace note allowed, no thesaurus swaps.

Do NOT change facts or numbers. Output ONLY the prose.

PROSE:
"""

STAGE_PROMPTS = (STAGE1_PROMPT, STAGE2_PROMPT, STAGE3_PROMPT)


@dataclass
class TrackPResult:
    input_path: Path
    outdir: Path
    fixture_path: Path
    final_path: Path


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _log(outdir: Path, message: str) -> None:
    line = f"[track-p] {message}"
    print(line)
    with (outdir / "run.log").open("a") as handle:
        handle.write(line + "\n")


def run_track_p(
    input_path: Path,
    *,
    rounds: int = 2,
    reviser: str = "claude",
) -> TrackPResult:
    input_path = input_path.resolve()
    if not input_path.is_file():
        raise FileNotFoundError(input_path)

    root = _repo_root()
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    basename = input_path.stem
    outdir = root / "docs/notes/pangram-audit/runs" / f"{basename}-{stamp}"
    outdir.mkdir(parents=True, exist_ok=True)

    _log(outdir, f"Input: {input_path}")
    _log(outdir, f"Output dir: {outdir}")
    _log(outdir, f"Rounds: {rounds}")

    current = outdir / "00-input.md"
    current.write_text(input_path.read_text())

    prose = extract_draft(current.read_text()) or current.read_text()

    for round_idx in range(1, rounds + 1):
        for stage_idx, template in enumerate(STAGE_PROMPTS, start=1):
            stage_out = outdir / f"r{round_idx}-stage{stage_idx}.md"
            prompt = f"{template}{prose}"
            if run_agent(reviser, prompt, stage_out):
                prose = stage_out.read_text().strip()
                _log(outdir, f"Round {round_idx} stage {stage_idx} OK ({reviser})")
            else:
                stage_out.write_text(prose)
                _log(outdir, f"Round {round_idx} stage {stage_idx} SKIPPED (no agent)")

        current = outdir / f"r{round_idx}-final.md"
        current.write_text(prose)

    fixture_name = basename.replace("-track-q", "") + "-track-p.md"
    fixture_path = root / "docs/notes/pangram-audit/fixtures" / fixture_name
    fixture_path.write_text(
        "\n".join(
            [
                "## Draft: Track P output",
                "",
                f"**Source:** {input_path}",
                f"**Run:** {outdir}",
                f"**Rounds:** {rounds}",
                "",
                "### Draft",
                "",
                prose,
                "",
                "### Pangram (manual)",
                "- [ ] Score: ___% AI / ___% Human (version ___)",
                "",
                "### Notes",
                "- Record each Pangram check in run.log",
                "",
            ]
        )
    )

    metrics = compute_metrics(current, prose)
    metrics_text = metrics.format()
    (outdir / "metrics.txt").write_text(metrics_text + "\n")
    _log(outdir, f"Wrote {fixture_path}")
    _log(outdir, "Next: paste final prose into Pangram; record score in fixture + run.log")
    print(metrics_text)

    return TrackPResult(
        input_path=input_path,
        outdir=outdir,
        fixture_path=fixture_path,
        final_path=current,
    )
