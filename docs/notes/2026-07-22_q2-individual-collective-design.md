# Q2 design — individual quality vs collective diversity

**Date:** 2026-07-22 · **Status:** PARKED (same-day revision).  
**Why parked:** Ultimate goal is AI writing in **economist/academic register**, not a general
individual-vs-collective creativity experiment. Q2 stays as inventory / possible later
guardrail. Live path: taste probes + skill + academic humanising
(`phase-6-decision.md` revised).

**Locks (historical morning):** Q2 spine; Q1 guardrail; Q3 constraint — superseded afternoon.  
**Graph:** batch-1 idea-graph (`diagnosis.md` §6–7). **Related:** humanising L×E note
(`2026-07-22_humanising-ai-writing-design.md`).

## The question (spine)

Under what **task** and **intervention** regimes does AI assistance raise **individual
quality** while reducing **collective diversity**—and when is that a true tradeoff vs
**mismatched metrics** across genres?

Anchors: `DH-01` (framing), `DH-10/11/20` (individual ↑ + within-condition similarity ↑),
`PH-11/30` (homogenization ↑ with quality flat), `DH-22 critiques PH-13` (scope/framing
tension), `DH-31` (social-dilemma reading).

## Why this is not “re-run Doshi + Padmakumar”

Those papers already show pieces of the pattern in **different regimes**:

| paper | assistance | task | individual | collective |
|---|---|---|---|---|
| Doshi–Hauser | optional GPT-4 *ideas* (≤5) | YA microfiction | novelty/usefulness ↑ | embedding similarity ↑ |
| Padmakumar–He | inline Solo / GPT-3 / InstructGPT | NYT-style essays | human quality ~flat | pairwise homogenization ↑ (InstructGPT) |

Q2 asks for a **joint map**: same metric definitions, crossed regimes, so we can tell
tradeoff from apples-to-oranges. The deliverable is a **regime × outcome matrix**, not a
single effect size.

## Constraints from the lock

### Q1 — instrument guardrail

Do **not** use as primary Q2 outcomes:

- EEG / dDTF “engagement” (`KS-07` family)
- quoting-without-looking (`KS-09`)
- interview ownership / self-ownership as a quality proxy (`KS-08`, also DH exploratory credit)

Those are contested constructs (`ST-15→KS-02`, `ST-14→KS-30` + critique swarm). Ownership/credit
may appear only as **exploratory covariates**, never as the individual-quality axis.

Prefer: evaluator quality/novelty/usefulness (DH-style) or relevance/depth ratings (PH-style),
plus deterministic diversity metrics (below).

### Q3 — persistence constraint

Default pilot label: **session-bound**. Any positive claim must say so explicitly.

Optional stretch (not blocking Pilot A): one **repeat-exposure** arm (same writers, second
session on a matched topic) to probe `PH-34` / `JK-31` / `WC-30`. If skipped, the write-up
must not generalize to “co-writing over time.”

## Axes

### Tasks (genre regimes)

Start with **two** genres that already disagree in the literature, not ten:

1. **Expository short essay** (PH-like: shared topic prompts; argument/explanation).
2. **Short fiction** (DH-like: constrained length; creative).

Reuse humanising Pilot 1’s lesson: narrative carries fidelity risk; keep claim-level fidelity
as a **validity check** on individual “quality” gains (not as a diversity metric).

Defer econ-intro / academic register until after the two-genre matrix is readable (taste
thread stays parallel).

### Interventions (assistance regimes)

Crossed, minimal:

| code | lever | maps to |
|---|---|---|
| **H** | Human-only (no model text) | DH Human-only / PH Solo |
| **I** | Idea springboard (fixed k model ideas; writer drafts) | DH-09 |
| **C** | Inline co-writing (chat or autocomplete; model in the draft loop) | PH-05 family |

Same base model family within a pilot wave (avoid PH’s InstructGPT-vs-GPT3 confound unless
model class is an explicit factor in a later wave).

### Evaluators (outcomes)

| axis | role | operationalization (v0) | graph metric anchors |
|---|---|---|---|
| **E_ind** | individual quality | Blind non-generating raters on a short rubric (novelty + usefulness for fiction; clarity + relevance/depth for essays). Numeric + forced choice. | DH-06/07 → DH-10/11; PH human ratings → PH-30 |
| **E_col** | collective diversity | Within-condition embedding similarity (DH-19) **and** pairwise homogenization / unique-unit diversity (PH-10/14). Report both; disagreement is a finding. | DH-19/20; PH-10/11/14 |
| **E_fid** | fidelity gate | Deterministic claim/number diff vs outline or vs human-only draft (humanising Pilot 2 method). Disqualify “quality” wins that fail fidelity. | humanising design, not KS |
| **E_det** | thermometer only | Pangram (or similar) if quota allows — **measure, never optimize** | charter |

Generation ≠ evaluation: drafting model never scores its own cells.

**Explicitly out of primary outcomes:** ownership, EEG, quoting, detector score as target.

## Hypotheses (falsifiable)

- **H-tradeoff:** In at least one genre×lever cell, E_ind rises and E_col falls vs H (true
  tradeoff under matched metrics).
- **H-mismatch:** The PH-flat / DH-up pattern reappears as a **metric×genre** interaction
  (essay quality flat under C; fiction quality up under I) rather than a universal law.
- **H-lever:** Idea springboard (I) and inline co-writing (C) do not move E_col the same way
  at matched E_ind — mechanism/regime matter (`PH-23` vs `DH-05` left open; we measure, not
  adjudicate mechanism in Pilot A).
- **H-session:** (only if repeat arm runs) E_col harm accumulates or attenuates at session 2;
  otherwise no longitudinal claim.

**Falsified if:** across both genres and both AI levers, E_ind and E_col always move together
(both up or both down) under both diversity metrics — then “tradeoff” is the wrong object and
Q2 collapses to metric calibration (diagnosis rank 6) or vanishes.

## Pilot A (minimal)

**Goal:** get a 2×3 cell sketch (genre × {H,I,C}) with matched metrics — enough to see whether
H-tradeoff or H-mismatch dominates.

1. **Prompts:** 3 shared topics per genre (escape N=1/genre from humanising Pilot 1).
2. **Writers:** model-as-writer is allowed for a *cheap* first pass **only if** labeled as
   AI-author simulation; preferred path is human writers (even N small) because DH/PH effects
   are about *assisted humans*. If budget forces AI-only drafts, treat results as
   **regime-simulation**, not a replication of DH/PH.
3. **N per cell:** aim ≥6 outputs per genre×lever for E_col (diversity is a distributional
   statistic; N=1 is meaningless). Prefer more on C and I than on H if constrained.
4. **Score:** E_ind (2+ blind vendors or 1 vendor + 1 human), E_col (both metric families),
   E_fid on every AI-touched draft.
5. **Report:** cell means + the tradeoff indicator `sign(ΔE_ind) ≠ sign(ΔE_col)` per metric;
   highlight metric disagreement.

**Out of Pilot A:** EEG, ownership interviews, multi-week longitudinal, skill edits, detector
tuning, batch-2 stylometry extract (unless E_col metrics prove uninterpretable).

## Link to humanising work

| humanising | Q2 use |
|---|---|
| Pilot 1 texture win | Candidate **lever inside C/I** later (L1 tail-move), not the first factor |
| Pilot 2 claim-level fidelity + structural metrics | Supplies **E_fid** and optional structural covariates; do not use “structural_winner” as E_col |
| E5 collective diversity | Becomes first-class here (was under-measured in Pilot 1) |
| E3 detectability | Remains thermometer |

Do not fold Q2 into “humanise harder.” Humanising may raise E_ind and still hurt E_col — that
is a Q2 result, not a failure of humanising.

## Non-goals

- No `SKILL.md` change from Pilot A alone.
- No detector-evasion objective.
- No claim that session-bound results describe long-term co-writing (unless repeat arm runs).
- No treating DH novelty and PH “quality flat” as already the same construct.

## Next actions

- [ ] Author: approve Pilot A scope (2 genres × {H,I,C}; session-bound; dual E_col metrics).
- [ ] Fix writer mode: human-assisted vs AI-author simulation (label honestly).
- [ ] Spec E_ind rubrics per genre (≤5 items) + E_col scripts (reuse PH/DH definitions; implement
      under `src/writing_audit/` via `uv run` entry points — no loose scripts).
- [ ] Run Pilot A; write results into this note (or a dated sibling).
- [ ] Only then: decide whether skill / humanising levers need a collective-diversity check.
