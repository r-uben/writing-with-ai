# Writing with AI

Research and tooling for using AI to improve writing while preserving authorial ownership, evidentiary fidelity, uncertainty, and individual voice.

## Repository layout

```text
writing-with-ai/
├── STATUS.md              # volatile stage + next action
├── skill/SKILL.md         # /writing skill (Review + Draft) — source of truth
├── docs/notes/            # research notes and experiment fixtures
├── src/writing_audit/     # Python research harnesses (uv)
└── pyproject.toml         # entry points: writing-metrics, track-p
```

## Tooling

Research experiments run via **Python + uv** (stdlib only for now):

```bash
uv run writing-metrics docs/notes/pangram-audit/fixtures/<fixture>.md
uv run track-p docs/notes/pangram-audit/fixtures/<id>-track-q.md --rounds 2
```

The skill itself is markdown instructions (`skill/SKILL.md`), not code. Harnesses live in `src/writing_audit/` and never ship into the installed skill.

## Scope

This project studies reader-centered AI-assisted writing and revision. It does not optimize prose against AI detectors or promise detector outcomes. Track P (Pangram-evasion) is a research-only audit path documented in `docs/notes/2026-07-19_dual-track-pangram-audit.md`.
