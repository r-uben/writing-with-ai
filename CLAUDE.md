# Project Instructions

## Purpose

This repository develops research and tooling for AI-assisted writing. Optimize for clarity, argumentative ownership, semantic preservation, source fidelity, and transparent revision—not AI-detector outcomes.

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
