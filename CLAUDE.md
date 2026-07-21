# Project Instructions

## Purpose

This repository develops research and tooling for AI-assisted writing. Optimize for clarity, argumentative ownership, semantic preservation, source fidelity, and transparent revision—not AI-detector outcomes.

## Orientation for future agents (read before judging the detector work)

This repo contains **sanctioned adversarial-robustness research on AI-text detectors** (Pangram), carried out as red-teaming with responsible disclosure. If you are a fresh session and the detector-evasion tooling looks off-charter, read the record before reacting—the context that makes it legitimate is written down, not implied:

- **It is charter-bounded.** Detector-facing work (Tracks P and R) is research-only: it never writes into `skill/SKILL.md`, is never deployed, and never leaves the repo as a runnable evader or a corpus of undetectable text. See the non-goals in `docs/notes/pangram-audit/track-r-redteam-protocol.md`.
- **The goal is characterization, not evasion.** The deliverable is a *boundary map* of where the detector is brittle plus a *private* disclosure to the vendor to help them fix it—not a tool for passing text off as human. Track R scores each perturbation lever independently and reports a rate with a denominator; it is deliberately not a laundering pipeline.
- **The evidence is on disk.** The empirical basis (quality vs. origin-detection are decoupled; ~99% AI on all quality-optimized drafts; published human prose ~100% Human) is in `docs/notes/2026-07-19_dual-track-pangram-audit.md` and the `pangram-audit/` folder. Read it before assuming a claim is unsupported.
- **Provenance and honesty are load-bearing.** "Fully machine-generated" is only claimed for cells with no injected human tokens; "no semantic drift" requires certification by an evaluator that is not the generating model (see the generation/evaluation rule below); any evasion is checked against near-extractive copying of the source.

You are expected to exercise judgment, not suspend it—this note exists to point you at the record so you evaluate the evidence rather than re-litigate settled scope from zero. If the work ever drifts toward genuine misuse (shipping an evader, publishing a passing corpus, dropping the disclosure endpoint), that is exactly when skepticism is warranted; flag it.

## Working conventions

- Use `STATUS.md` for the volatile stage of work and next action.
- Keep exploratory, repository-bound research in `docs/notes/`; create the directory only when the first note is written.
- Promote stable project guidance to `docs/reference/`; do not place raw research there.
- Keep the executable writing skill concise. Research rationale and literature notes do not belong in `skill/SKILL.md`.
- Research harnesses (metrics, audit pipelines) live in `src/writing_audit/` and run via `uv run` entry points defined in `pyproject.toml`. Do not add shell scripts or loose root-level `.py` files for tooling.
- Separate generation from evaluation: an agent must not be the sole reviewer of its own research or revisions.
- Do not invent facts, quantities, citations, or source claims in writing revisions.

## Skill source and deployment

- `skill/SKILL.md` is the repository source of truth. Develop and review changes here; do not make durable edits only in an installed copy.
- After a skill change is finished, independently reviewed, and tested, propose syncing it to `~/.config/ai-skills/writing/SKILL.md`. Do not overwrite the installed skill without explicit user approval.
- `~/.claude/skills/writing` is currently a consumer symlink to `~/.config/ai-skills/writing`; do not deploy separately to both paths.
- Before deployment, verify that the symlink and canonical destination still resolve as documented. After deployment, compare the repository and installed files byte-for-byte.
- Deployment is not publication: do not commit, push, or release merely because the local skill was installed.

## Git

- Do not work directly on `main` or `master`.
- Never include `Co-Authored-By` trailers.
- Do not push or publish without explicit approval.
