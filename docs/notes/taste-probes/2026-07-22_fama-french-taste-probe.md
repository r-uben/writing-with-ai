# Fama–French taste probe — full AI option

**Date:** 2026-07-22  
**Status:** AI proposal for author comparison — **not Track B**  
**Concept:** fama-french-1997 (industry costs of equity are imprecise)  
**Paper:** Fama & French (1997, JFE) — library `1997__Fama_French__Industry_Costs_of_Equity__JFE`  
**Constraints applied:** outline + supplied numbers only; no detector-chase; no Track C paste  
**Vendors:** gpt-style, grok-style, terse-alternative (single-agent voice variants; not external CLI calls)

---

## Primary probe (recommended for compare)

**Selected:** grok-style — clearest textbook-defect open, named CAPM/FF3 landscape without runway, quantitative anchor early, stakes close on NPV illusion; no First/Secondly enumeration and no rhetorical-question pivot.

### Draft

Textbooks in corporate finance stress that cash flows are uncertain. They say far less about the discount rate: once a pricing model is picked, the cost of equity is treated as a known input. It is not. Industry estimates under both the CAPM and the Fama–French three-factor model typically have standard errors above 3 percent per year. That figure is the applied stake of the paper, not a side remark.

Switching models does not buy precision. The CAPM is the default and remains contested; the three-factor model improves in-sample fit but rests on empirical motivation rather than a settled theoretical claim. At the industry level, both leave wide bands. The noise has two layers that compound: uncertainty in the factor risk premia themselves, and imprecision in industry loadings on those factors. Drop either and the bands shrink; keep both and they stay fat. Textbook practice that treats model choice as the hard step and estimation as housekeeping gets this backwards.

That matters for practice. Industry costs of equity already arrive with more than 3 percent annual standard error. Firm and project rates inherit that noise and add their own. NPV calculations that treat the discount rate as known therefore overstate how sharp the answer can be, unless estimation risk is written into the decision rather than left offstage.

### Taste moves (self-report)
- `incumbent→defect→our-fix` — yes (textbook known-rate → large estimation error → estimation risk must enter the decision)
- `thesis-in-first-sentence` — no (opens on textbook habit; thesis lands mid-¶1)
- `enumerated-gaps` — no (two error sources named, but not First/Secondly / “at least three”)
- `named-models-as-landscape` — yes (CAPM; Fama–French three-factor)
- `concrete-episode-as-evidence` — no
- `rhetorical-question-pivot` — no
- `quantitative-anchor` — yes (SEs > 3%/yr)
- `stakes/so-what` — yes (NPV precision partly illusory at firm/project level)
- ~218 words

### Verify before use
- [ ] Standard errors > 3.0% per year (typical) for industry cost of equity under CAPM and FF3 — fixture
- [ ] CAPM standard but contested; FF3 better in-sample fit, empirically motivated — outline
- [ ] Two stacked errors: factor-premium sampling error + industry loading imprecision — outline
- [ ] Firm/project estimates worse than industry; NPV precision partly illusory unless estimation risk enters the decision — outline
- [ ] Do **not** use paper dates (received March 1994 / final August 1996) in prose unless citing publication history

---

## Vendor variants

### gpt-style (~225 words)

Corporate finance textbooks dwell on cash-flow uncertainty and treat the discount rate as if it were known once a model is chosen. That understates the problem: the cost of equity itself is estimated with large error, and the error is typical rather than exceptional. Whether one uses the CAPM or the Fama–French three-factor model, industry-level cost-of-equity estimates routinely carry standard errors above 3 percent per year. The band is not a curiosity of one specification; it shows up under both.

Model choice does not resolve the imprecision. The CAPM remains the classroom standard and is contested on empirical grounds; the three-factor model fits better in sample but is itself empirically motivated. At the industry level both deliver fat uncertainty bands. Two sources of error stack. Sampling variation in estimated factor risk premia is one; imprecise industry betas and factor loadings are the other. Neither is negligible, and together they dominate the precision that applied work often assumes when it plugs a single industry rate into a valuation.

The implication is sharper once the unit of analysis shrinks. If industry costs of equity are measured with standard errors above 3 percent per year, firm- and project-level estimates are worse still. Apparent precision in NPV analysis is then partly illusory unless estimation risk enters the decision rule rather than being ignored after the rate is plugged in.

**Taste moves (self-report)**
- `incumbent→defect→our-fix` — yes
- `thesis-in-first-sentence` — no
- `enumerated-gaps` — no (parallel “one… the other…”, not First/Secondly)
- `named-models-as-landscape` — yes (CAPM; FF3)
- `concrete-episode-as-evidence` — no
- `rhetorical-question-pivot` — no
- `quantitative-anchor` — yes (SEs > 3%/yr)
- `stakes/so-what` — yes (NPV illusion / estimation risk in the rule)

### terse-alternative (~200 words)

Cash-flow risk dominates corporate-finance teaching; estimation risk in the discount rate does not. Industry costs of equity under the CAPM and under the Fama–French three-factor model typically have standard errors above 3 percent per year. That is the central fact for applied work that treats an industry rate as a tight number. The same order of imprecision appears under both models, so switching the classroom workhorse does not restore a sharp input.

Neither model choice nor better in-sample fit removes the band. The CAPM is standard and contested; the three-factor model fits better in sample and is empirically motivated. Both leave industry estimates imprecise. Two errors stack: sampling error in factor risk premia, and imprecision in industry betas and loadings. Each is material; together they explain why textbook confidence in a plugged-in rate is misplaced. The discount rate is not known once the model is named.

If industry standard errors already exceed 3 percent per year, firm- and project-level costs of equity are noisier still. Precision in NPV analysis is then partly an artifact of ignoring estimation risk. Decision rules that take the rate as known understate how wide the plausible range really is, and project acceptance inherits that overconfidence.

**Taste moves (self-report)**
- `incumbent→defect→our-fix` — yes (compressed)
- `thesis-in-first-sentence` — partial (¶1 sentence 2–3 carry the finding; sentence 1 is contrast setup)
- `enumerated-gaps` — no
- `named-models-as-landscape` — yes
- `concrete-episode-as-evidence` — no
- `rhetorical-question-pivot` — no
- `quantitative-anchor` — yes
- `stakes/so-what` — yes

---

## Paper-lookup notes (for your B write — outline refresh only)

From fixture `fixtures/fama-french-1997.md` (outline only; Track C not opened for drafting):

- Textbooks stress cash-flow uncertainty; they understate discount-rate estimation error.
- CAPM contested; FF3 fits better in sample but empirically motivated; both give fat industry bands.
- Two stacked errors: (i) factor-premium sampling error; (ii) industry loading imprecision.
- Punchline: industry SEs > 3%/yr ⇒ firm/project worse; NPV precision partly illusory unless estimation risk enters the decision.
- Supplied number: SEs > 3.0% per year (typical) under CAPM and FF3.

**Do not open Track C or this probe while writing Track B.** Use `fixtures/fama-french-1997.md` outline only.

---

## Comparison worksheet (fill later)

| Dimension | Your B | Primary AI (grok-style) | Prefer |
|-----------|--------|-------------------------|--------|
| Opening | | textbook cash-flow focus / known discount rate | |
| Model landscape | | CAPM contested; FF3 in-sample / empirical | |
| Error stack | | premia sampling + loading imprecision (not First/Secondly) | |
| Quantitative anchor | | SEs > 3%/yr | |
| Stakes close | | NPV precision illusory / estimation risk in decision | |
| Overall register | | | |

Notes:

- Self-reports above are author-side only; a later coder should re-check against the move codebook.
- This file is a **taste probe**, not a Pangram Track B cell and not detector-optimized text.
