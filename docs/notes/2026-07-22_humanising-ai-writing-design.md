# Humanising AI writing — research design

**Date:** 2026-07-22 · **Status:** design note (pre-pilot). Exploratory, repository-bound.

## The question

Not "can we make AI text pass as human?" (an arms race that expires on every model
release) but: **is "human-likeness" a single axis, or does it decompose into axes that
dissociate under intervention?**

If humanising along one axis (say, structural variability) does *not* move the others
(quality, detectability, collective diversity), then "humanise AI writing" is not one
problem but several, and the interesting result is the **dissociation structure** — which
levers buy which axes, and at what cost to the rest.

## Why this repo can answer it (prior findings this builds on)

- **Quality ⊥ origin-detection** already observed in `docs/notes/2026-07-19_dual-track-pangram-audit.md`
  (~99% AI on all quality-optimised drafts; published human prose ~100% Human). This
  *predicts* dissociation: humanising-for-quality and humanising-for-detector are likely
  different interventions.
- **A discriminator already exists.** `docs/notes/taste-probes/prose-moves-graph.md`: 3/3 AI
  drafts reproduce the genre spine but miss the human-only tail moves
  `rhetorical-question-pivot` and `enumerated-gaps` (holds across three model families). That
  is a ready-made humanising **lever** targeting an *observed* gap, not a guessed one.
- **A non-detector evaluator already exists** (the taste probes / move-graph), so "human-like"
  can be scored without "fools a detector" being the target.
- **Collective-diversity lever** from the corpus: `diverse-personas-2026` (Wan & Kalman) —
  persona diversity recovers cross-output diversity.

## Design: levers × evaluators

**Levers (the humanising interventions):**
- **L1 — tail-move induction.** Prompt/generate to include the missing human-only moves
  (`rhetorical-question-pivot`, `enumerated-gaps`). Cleanest lever: targets a measured gap.
- **L2 — variance injection.** Increase burstiness / structural variability at generation.
- **L3 — persona-diversified decoding.** For the collective axis (Wan-Kalman style).
- **L4 — post-hoc paraphrase/edit.** The Track-R lever. **Research-only** (see guardrails).

**Evaluators (axes of "human-like"):**
| Axis | Evaluator | Role |
|---|---|---|
| E1 structural | distributional match: burstiness, dependency depth, move-diversity (graph) | optimise |
| E2 quality + fidelity | non-generating LLM/human raters on quality; semantic-drift certification | optimise |
| E3 detectability | Pangram score | **measure only** |
| E4 indistinguishability | blind human/rater panel | measure |
| E5 collective | diversity across N outputs | optimise (L3) |

**The deliverable is the L×E matrix** — for each lever, whether it moves each axis, and the
tradeoffs. Not a single optimised number.

## Central hypothesis + falsification

**H1 (dissociation):** humanising levers move E1/E2/E5 largely independently of E3; a lever
that improves E1 (structural match) need not improve E2 (quality) — "difference ≠
improvement" (the exact fallacy the cross-vendor review flagged when downgrading S2 in
`docs/reference/skill-evidence-map.md`).

**Falsified if:** the axes move together — one lever monotonically improves structural match,
quality, indistinguishability, *and* lowers detectability, with no semantic drift. That would
mean "human-like" is one axis after all (and, awkwardly for the charter, that quality and
detector-evasion are the same thing — contradicting the dual-track finding).

## Pilot (L1 only, minimal)

1. Take a fixed set of concepts/outlines (reuse Morris-Shin + add Fama-French, Nakamura-Steinsson
   to escape the N=1 problem the review flagged).
2. Generate baseline AI drafts (several model families).
3. Apply **L1**: regenerate with tail-move induction.
4. Score baseline vs L1 on **all five axes**, using **cross-vendor, non-generating judges**
   (generation ≠ evaluation) — the same harness pattern as the evidence-map audit.
5. Report the per-axis delta. Key read: does L1 improve E2 (quality) or only E1 (structure)?

## Guardrails (charter)

- **Detector axis is a thermometer, not a target.** E3 is measured, never optimised. No lever
  is tuned to lower Pangram score.
- **No shipped evader.** Deliverable = dissociation map + intervention characterisation +
  (if warranted) a private vendor disclosure. Never a runnable laundering tool or a corpus of
  "undetectable" text. L4 stays inside the Track-R fence.
- **Semantic drift certified by a non-generating evaluator**; "humanised" never means
  "meaning changed."
- **Generation ≠ evaluation** throughout: the model applying a lever never scores its own output.

## Next actions

- [ ] Confirm the L1 pilot scope (which concepts, which model families).
- [ ] Build the pilot workflow (generate → L1 → cross-vendor score on 5 axes).
- [ ] Corroborate the tail-move discriminator on FF/NS *before* over-claiming it as human-only
      (also unblocks the deferred S8 question in the evidence map).
