# Track R — red-team boundary-mapping + responsible disclosure protocol

**Date:** 2026-07-19
**Status:** harness stubbed (`uv run track-r`), protocol pre-registration draft — NOT yet run
**Charter:** research-only. Track R never writes into `skill/SKILL.md` and is never deployed. Same hard separation as Track P.
**Relationship to Track P:** Track P was a *stacked laundering* pipeline (one final output). Track R is its disciplined successor: **single-lever ablation**, every variant independently scored, provenance logged, rate reported with a denominator.

## Why this exists (and why it is NOT a laundering pipeline)

Two independent reviews (session 2026-07-19, primary model + second-opinion model) converged on the same conclusion: building and keeping a working "make machine text read as Human" recipe is a weaponizable dual-use artifact with a poor risk/teach ratio, and the repo's own data predicts it either fails automatically or only "works" by smuggling in human tokens / drifting semantically.

The valuable, defensible, charter-aligned contribution is a **characterization of Pangram's decision boundary**, not an exploit:

> Which single perturbation moves P(AI), by how much, at what semantic cost — and does any *fully machine-generated* variant cross to "Human" without semantic drift or near-extractive copying?

That question yields the same disclosure value to Pangram (here is where you are brittle) while leaving behind a boundary map, not a turnkey evader.

## Pre-registered hypotheses (write down BEFORE scoring)

- **H1 (primary):** No fully-automated single lever (L1–L3) flips a machine draft to "Human" at high confidence without semantic drift. Expected: all machine cells stay AI, P(AI) high.
- **H2:** The human-encoding lever (L4) is the dominant mover; it is also the only lever that injects genuine human tokens. Any "success" is therefore a statement about human contribution, not automated evasion.
- **H3:** Cross-model paraphrase (L3) moves P(AI) more than de-tell (L1) or restructure (L2) but stays AI — moving between machine fingerprints, not off the machine manifold.
- **H4:** A close human paraphrase of *published* source stays "Human" but with rising P(AI) and falling confidence as content is regularized (replicates the 2026-07-19 paraphrase cell: 0.0025 → 0.0747, High → Low).

Record predictions with a timestamp before the first score. A confirmed H1 is a *publishable, honest* result on its own.

## Levers (single-lever ablation; no stacking)

| Lever | Type | Injects human tokens? |
|---|---|---|
| L0-identity | control, unchanged | no |
| L1-detell | remove LLM token patterns | no |
| L2-restructure | clause/sentence re-encode | no |
| L3-crossmodel | end-to-end paraphrase, different voice | no |
| L4-human | **manual** author re-encoding slot | **yes — flagged, reported separately** |

Levers are applied to the *same base prose* so effects compare independently. The harness never fabricates human tokens; L4 is a stub the author fills by hand.

## Measurement rules (what makes the disclosure credible)

1. **Denominator, always.** Score *every* cell — controls and failures included. The claim is a rate (false-Human / total machine cells) with an interval, never a highlight reel. Rows that scored AI are not deleted.
2. **Distribution, not verdict.** Record raw `prediction_prob` (P(AI)) and confidence per cell, not just AI/Human. A calibration curve is more useful to Pangram than a pass count.
3. **Provenance.** `manifest.json` logs the exact lever, reviser, and `human_injected` flag per cell. "Fully machine-generated" is only claimed for cells with `human_injected=false` produced end-to-end by the harness.
4. **Independent fidelity.** "No semantic drift" must be certified by an evaluator that is NOT the generating model (charter: generator ≠ reviewer). A cell that scores Human but drifted is fluent nonsense, not evasion.
5. **Anti-plagiarism guard.** Any machine cell that flips to Human is checked against the human source for near-extractive copying before it counts — otherwise it is a plagiarism artifact, not a detector result.
6. **Version pinning.** Record Pangram version (currently 3.3.2), date, and any params on every score. Detectors drift; results are a snapshot.
7. **Quota discipline.** ~4 free checks/day. Score in priority order: L0 baseline → L3 → L1 → L2 → L4. Log every check against quota.

## Run procedure

```bash
# 1. Emit cells (agentless run writes control copies; with a reviser CLI on PATH it perturbs)
uv run track-r docs/notes/pangram-audit/fixtures/<id>-track-q.md --reviser claude

# 2. Author fills the L4-human stub by hand (optional, flagged)

# 3. Score EVERY cell on Pangram; fill SCORING-WORKSHEET.md (P(AI), confidence, fidelity)

# 4. Independent fidelity pass on any Human-scoring machine cell (separate evaluator)

# 5. Update manifest.json with scores; write findings into this note
```

## Disclosure discipline (responsible disclosure, not publication)

- **Private + embargoed.** Contact Pangram directly first. Do not publish the recipe, the passing corpus, or the highest-yield lever settings.
- **Report is the deliverable, not the corpus.** Hand them: pre-registration, full denominator + P(AI) distribution, the ablation (which lever moved what), version/params, and a reproducible harness — not a pile of undetectable text.
- **Name the honest ask.** If a "successful" cell contains human tokens, "detect this as AI" may be an unreasonable request; say so. That candor makes the correspondence more credible, not less.
- **No turnkey evader leaves the repo.** If an automated cell genuinely flips without drift or copying, that is a real finding — disclose the *mechanism* privately; still do not ship or publish the runnable exploit.

## Explicit non-goals

- Do not build or retain a corpus of certified-undetectable machine essays.
- Do not deploy Track R into `~/.config/ai-skills/writing/` or `skill/`.
- Do not report a rate without its denominator, or a "no drift" claim without independent certification.
- Do not treat a single pass as the finding; the finding is the boundary and the ablation.
