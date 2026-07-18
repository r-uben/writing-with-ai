# Status

**Last updated:** 2026-07-19

## Stage

Initial commit (`a815f2b`) on `setup/initial-structure`. Pangram audit **wave 0–2 complete**: protocol frozen, human extracts (Track C), quality drafts (Track Q), detector-chase drafts (Track P), metrics baseline, taste Q3–Q5 pairs drafted. **Blocked on:** author taste picks + Morris–Shin rewrite; Pangram quota for scoring. Skill not yet independently reviewed.

## Where things live

| What | Where |
|---|---|
| **Volatile TODO / next action** | this file (`STATUS.md`) |
| **Plan ticket graph (stable spec)** | `docs/plans/2026-07-19_writing-skill-pangram-audit/TICKETS.md` |
| **Plan dispatch state** | `docs/plans/2026-07-19_writing-skill-pangram-audit/STATUS.md` |
| **Wave dispatch logs** | `docs/plans/.../logs/2026-07-19_wave*.md` |
| **Experiment fixtures** | `docs/notes/pangram-audit/fixtures/` |
| **Experiment runbook** | `docs/notes/pangram-audit/README.md` |

There is no `TODO.md` — per `CLAUDE.md`, volatile work tracking lives here.

## Live artifacts

- `skill/SKILL.md` — Review + Draft modes; D3/D4 panel-refined; not independently reviewed
- `docs/notes/pangram-audit/` — three-concept audit (C/Q/P done; B empty)
- `src/writing_audit/` — `writing-metrics`, `track-p` CLIs
- `docs/plans/2026-07-19_writing-skill-pangram-audit/` — dependency-gated plan

## Recent progress (2026-07-19)

- Plan created with three-reviewer advisory panel; tickets in `TICKETS.md`
- Wave 0–1: protocol, Track C extracts, taste pairs, metrics baseline
- Commit `a815f2b` (initial scaffold)
- Wave 2: Track P outputs for all 3 concepts + run logs in `pangram-audit/runs/`

## Outstanding TODOs

**Author (blocks Open Q#2 + taste wiring)**
- [ ] Pick taste Q3–Q5 in `docs/notes/taste-profile.md`
- [ ] Morris & Shin from-memory rewrite → `morris-shin-1998-track-b.md` (outline only)

**Pangram audit (quota-gated)**
- [ ] Score Track C extracts first when quota resets
- [ ] Score Q, P, B cells per protocol
- [ ] Blind quality panel on Q/P/B
- [ ] Write audit synthesis + Open Q#2 verdict

**Skill ship path**
- [ ] Wire taste principles into skill (after author picks)
- [ ] Independent review of Draft Mode
- [ ] E2E draft on real user concept
- [ ] Deploy proposal (user approval required)

**Deferred**
- [ ] Layer-1 calibration panel + human corpus thresholds
- [ ] Optional: forward-guidance graded revision ladder (B2-FG)

## Empirical results (Pangram v3.3.2)

Prior n=4 (forward-guidance): AI quality drafts 100% AI; human same-topic 100% Human; Variant B untested.

New three-concept audit: **scoring not yet run.** Fixtures ready in `pangram-audit/fixtures/`.

## Next action

1. **You:** taste picks + Morris–Shin rewrite
2. **Pangram:** score `*-track-c.md` when quota resets
3. **Uncommitted:** Track P outputs + STATUS updates — commit when ready
