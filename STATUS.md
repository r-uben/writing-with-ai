# Status

**Last updated:** 2026-07-19 (overnight wave 3)

## Stage

Branch `setup/initial-structure`. Pangram audit **wave 0–3 complete** for agent-side work: Track C/Q/P fixtures, Layer-1 metrics (C/Q/P), blind Layer-2 panel on Q vs P, independent Draft Mode review logged. **Blocked on author:** taste picks (A1b), Morris–Shin Track B rewrite, Pangram quota for scoring. Skill fixes from C1 **not** applied yet; taste wiring (A2) waits on picks. Not pushed; not deployed.

## Where things live

| What | Where |
|---|---|
| **Volatile TODO / next action** | this file (`STATUS.md`) |
| **Plan ticket graph (stable spec)** | `docs/plans/2026-07-19_writing-skill-pangram-audit/TICKETS.md` |
| **Plan dispatch state** | `docs/plans/2026-07-19_writing-skill-pangram-audit/STATUS.md` |
| **Wave dispatch logs** | `docs/plans/.../logs/2026-07-19_wave*.md` |
| **Blind panel logs** | `docs/plans/.../logs/panel-{ns,ms,ff}.md` |
| **Draft Mode review** | `docs/plans/.../logs/review-draft-mode.md` |
| **Experiment fixtures** | `docs/notes/pangram-audit/fixtures/` |
| **Experiment runbook** | `docs/notes/pangram-audit/README.md` |

## Live artifacts

- `skill/SKILL.md` — Review + Draft modes; independently reviewed (C1 logged); fixes pending C2
- `docs/notes/pangram-audit/` — three-concept audit (C/Q/P done; B empty)
- `src/writing_audit/` — `writing-metrics`, `track-p` CLIs
- `docs/plans/2026-07-19_writing-skill-pangram-audit/` — dependency-gated plan

## Recent progress (2026-07-19)

- Wave 0–2: protocol, Track C/Q/P, metrics baseline (Q), taste pairs drafted
- Wave 3 overnight: committed Track P; blind Q/P panel (3 judges); Draft Mode review; metrics for C+P

## Outstanding TODOs

**Author (blocks Open Q#2 + taste wiring)**
- [ ] Pick taste Q3–Q5 in `docs/notes/taste-profile.md`
- [ ] Morris & Shin from-memory rewrite → `morris-shin-1998-track-b.md` (outline only)
- [ ] Skim C1 majors in `logs/review-draft-mode.md` (F1–F3)

**Pangram audit (quota-gated)**
- [ ] Score Track C extracts first when quota resets
- [ ] Score Q, P, B cells per protocol
- [ ] Blind quality panel on B when author rewrite exists
- [ ] Write audit synthesis + Open Q#2 verdict

**Skill ship path**
- [ ] Wire taste principles into skill (A2, after author picks)
- [ ] Apply C1 review fixes (C2) — after A2 or author go-ahead
- [ ] E2E draft on real user concept
- [ ] Deploy proposal (user approval required)

**Deferred**
- [ ] Layer-1 calibration panel + human corpus thresholds
- [ ] Optional: forward-guidance graded revision ladder (B2-FG)

## Empirical results

**Pangram v3.3.2:** Prior n=4 (forward-guidance) — AI quality drafts 100% AI; human same-topic 100% Human. New three-concept audit: **scoring not yet run.**

**Layer-2 blind panel (Q vs P, overnight):** Q cleaner on NS and FF (3/3); P cleaner on MS (3/3). See `logs/panel-*.md`.

## Next action

1. **You:** taste picks + Morris–Shin rewrite + skim C1-F1–F3
2. **Pangram:** score `*-track-c.md` when quota resets
3. **Agent after A1b:** wire taste (A2), then C2 skill fixes
