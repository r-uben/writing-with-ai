# Humanising Pilot 2 — academic register (Fama–French)

**Date:** 2026-07-22 · **Status:** pilot results (single-concept).  
**Goal alignment:** AI econ/academic register — induce the human-vs-AI texture miss
`enumerated-gaps`, check **fidelity** to the outline (not detector score).

**Baseline:** grok-style draft in `2026-07-22_fama-french-taste-probe.md` (no enumerated gaps).  
**Lever (L1 academic):** rewrite once to use explicit First / Second enumeration of the
outline’s two error sources — without adding facts, numbers, or a third invented gap.  
**Outline source of truth:** `docs/notes/pangram-audit/fixtures/fama-french-1997.md`.

**Note:** Human FF enumerates “at least three” cost-of-capital problems. Our fixture outline
only supplies **two** stacked errors. Pilot induces enumeration of those two — not a fake
third problem.

---

## Baseline (AI, pre-humanise)

Textbooks in corporate finance stress that cash flows are uncertain. They say far less about the discount rate: once a pricing model is picked, the cost of equity is treated as a known input. It is not. Industry estimates under both the CAPM and the Fama–French three-factor model typically have standard errors above 3 percent per year. That figure is the applied stake of the paper, not a side remark.

Switching models does not buy precision. The CAPM is the default and remains contested; the three-factor model improves in-sample fit but rests on empirical motivation rather than a settled theoretical claim. At the industry level, both leave wide bands. The noise has two layers that compound: uncertainty in the factor risk premia themselves, and imprecision in industry loadings on those factors. Drop either and the bands shrink; keep both and they stay fat. Textbook practice that treats model choice as the hard step and estimation as housekeeping gets this backwards.

That matters for practice. Industry costs of equity already arrive with more than 3 percent annual standard error. Firm and project rates inherit that noise and add their own. NPV calculations that treat the discount rate as known therefore overstate how sharp the answer can be, unless estimation risk is written into the decision rather than left offstage.

**Moves:** spine ✓ · named-models ✓ · quantitative-anchor ✓ · stakes ✓ · `enumerated-gaps` ·

---

## Humanised (L1: enumerated-gaps)

Textbooks in corporate finance stress that cash flows are uncertain. They say far less about the discount rate: once a pricing model is picked, the cost of equity is treated as a known input. It is not. Industry estimates under both the CAPM and the Fama–French three-factor model typically have standard errors above 3 percent per year. That figure is the applied stake of the paper, not a side remark.

Switching models does not buy precision. The CAPM is the default and remains contested; the three-factor model improves in-sample fit but rests on empirical motivation rather than a settled theoretical claim. At the industry level, both leave wide bands. The imprecision has two sources, and neither is negligible. First, estimated factor risk premia carry sampling error. Second, industry betas and factor loadings are themselves imprecise. Drop either layer and the bands shrink; keep both and they stay fat. Textbook practice that treats model choice as the hard step and estimation as housekeeping gets this backwards.

That matters for practice. Industry costs of equity already arrive with more than 3 percent annual standard error. Firm and project rates inherit that noise and add their own. NPV calculations that treat the discount rate as known therefore overstate how sharp the answer can be, unless estimation risk is written into the decision rather than left offstage.

**Moves:** same as baseline + `enumerated-gaps` ✓ (First / Second on the two outline errors)

---

## Claim-level fidelity check (deterministic)

Coder ≠ humaniser. Claims checked against fixture outline only.

| # | Claim in humanised draft | In outline / supplied numbers? | Status |
|---|---|---|---|
| 1 | Textbooks stress cash-flow uncertainty; understate discount-rate error | Outline §1 | OK |
| 2 | Cost of equity treated as known once model picked; it is not | Outline §1 | OK |
| 3 | Industry SEs typically > 3%/yr under CAPM and FF3 | Supplied number | OK |
| 4 | CAPM default and contested; FF3 better in-sample, empirically motivated | Outline §2 | OK |
| 5 | Both leave wide industry bands | Outline §2 | OK |
| 6 | First: sampling error in factor risk premia | Outline §3 (i) | OK |
| 7 | Second: imprecise industry betas/loadings | Outline §3 (ii) | OK |
| 8 | Neither negligible; compound | Outline §3 | OK |
| 9 | Firm/project estimates worse than industry | Outline §4 | OK |
| 10 | NPV precision partly illusory unless estimation risk enters the decision | Outline §4 | OK |
| 11 | Any third enumerated “problem,” new date, new %, new citation | — | **Absent** (good) |

**Fidelity verdict:** PASS — humanised draft does not add facts; enumeration only reshapes outline §3.

**Texture verdict:** `enumerated-gaps` successfully induced (First / Second). Word count still ~220.

---

## Read for the skill / taste path

1. For **econ intros**, a cheap humanising lever that matches attested human texture is:
   **enumerate the real gaps already in the outline** (First / Second / …) — do not invent
   extra gaps to look human.
2. This is safer than chasing `rhetorical-question-pivot` (MS-only; skill tension with S8).
3. **Candidate taste principle P6** (needs author confirm): when the outline lists ≥2 distinct
   defects/limits, draft them as an explicit enumeration in prose (S15 already allows
   “First… Second…” in flowing paragraphs).

## Next

- [x] Author: **rejected P6**; redirected to P2 epistemic-hedge ban (2026-07-22).
- [ ] Optional: repeat fidelity-only checks on MS/NS if useful; enumeration induction is not a skill target.
- [ ] Independent review of the P2 hedge-stem tighten in `skill/SKILL.md` before deploy sync.
