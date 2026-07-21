# Pangram robustness findings — disclosure draft (SKELETON, do not send as-is)

**To:** Pangram Labs (security/research contact — find private channel first)
**From:** Ruben Fernández Fuertes
**Re:** Adversarial robustness of Pangram v3.3.2 origin detection on academic economics prose
**Disposition:** private, embargoed. Not for publication. No runnable evader or passing corpus attached — methodology + harness only.

---

## 1. Summary (fill after scoring)

We ran a controlled ablation against Pangram v3.3.2 on short academic economics passages (Morris–Shin 1998, Fama–French 1997, Nakamura–Steinsson 2018 registers). We report ___ machine-generated cells across ___ single-lever perturbations. False-"Human" rate on fully machine-generated text: ___% (___/___). [If ~0: "origin detection held across all automated perturbations" — a robustness *confirmation*, still useful.]

## 2. What we tested

- One base draft per concept; single-lever perturbations (de-tell, restructure, cross-model paraphrase), each scored independently. No stacking.
- A separate, clearly-flagged human-encoding condition (NOT machine-generated) for contrast.
- Every cell scored, including controls and AI-scoring failures. Denominator reported.

## 3. Results (fill)

| lever | machine? | n | verdict dist | mean P(AI) | conf | fidelity-certified |
|---|---|---|---|---|---|---|
| L0 control | yes | | | | | |
| L1 de-tell | yes | | | | | |
| L2 restructure | yes | | | | | |
| L3 cross-model | yes | | | | | |
| L4 human (contrast) | **no** | | | | | |

Calibration: [attach P(AI) distribution / curve, not just verdicts.]

## 4. The finding (fill — expected shape)

- Automated levers moved P(AI) by [Δ], but [did / did not] cross to Human without drift.
- Dominant mover: [likely L4-human, i.e. genuine human tokens] — which is a statement about human contribution, not automated evasion.
- Any machine cell that flipped was checked for (a) semantic drift via an independent evaluator and (b) near-extractive copying of source. [Report outcome.]

## 5. Honest framing of the ask

If the passages that evade detection contain genuine human-authored token sequences, "flag these as AI" may not be a well-posed request. Where we [did / did not] find *fully machine-generated* evasion, we state it plainly. We are flagging [the specific brittle region], not claiming a general break.

## 6. Reproducibility

- Harness: `track-r` (single-lever ablation), available on request under embargo.
- Pangram version: 3.3.2. Dates/params: [fill].
- We have withheld the highest-yield lever settings and the passing corpus from this document by design.

## 7. Suggested next step

Happy to share the harness and full per-cell data privately so your team can reproduce. We are not publishing this.

---

*Skeleton generated as part of Track R protocol. Author to complete after scoring; do not send until sections 1–6 are filled and a private contact is confirmed.*
