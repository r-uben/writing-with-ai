# Case 3 — FF primary probe → P7 / anti-slop revise

**Date:** 2026-07-22  
**Seed:** `2026-07-22_fama-french-taste-probe.md` (primary / grok-style)  
**Origin:** AI-generated (AI revise of AI)  
**Pass:** consolidated `/writing` anti-slop + P7 (levers from Case 1)  
**Pangram:** author to run after taste OK — secondary only

## Detect (before)

| Quote | Rule | Fix |
|---|---|---|
| “Switching models does not buy precision.” | P7 / cute | Drop *buy*; state the imprecision fact |
| “estimation as housekeeping” | P7 metaphor | Plain: estimation is treated as secondary |
| “left offstage” | P7 metaphor | “left out of the decision” |
| “bands stay fat” | borderline slang | “bands remain wide” |
| “gets this backwards” | tour-guide | State the ordering error flatly |
| Possible metronome in ¶2 shorts | slop / S2 | Merge into longer mechanism sentences |

## After (revise)

Textbooks in corporate finance stress that cash flows are uncertain. They say far less about the discount rate: once a pricing model is picked, the cost of equity is treated as a known input. It is not. Industry estimates under both the CAPM and the Fama–French three-factor model typically have standard errors above 3 percent per year. That figure is the applied stake of the paper, not a side remark.

Model choice does not restore a precise industry rate. The CAPM is the default and remains contested; the three-factor model improves in-sample fit but rests on empirical motivation rather than a settled theoretical claim. At the industry level, both leave wide uncertainty bands. The noise has two layers that compound: uncertainty in the factor risk premia themselves, and imprecision in industry loadings on those factors. Drop either and the bands shrink; keep both and they remain wide. Textbook practice that treats model choice as the hard step and estimation as a secondary detail reverses the constraint that binds for applied work.

That matters for practice. Industry costs of equity already carry more than 3 percent annual standard error. Firm and project rates inherit that noise and add their own. NPV calculations that treat the discount rate as known therefore overstate how sharp the answer can be, unless estimation risk enters the decision rather than being ignored after the rate is plugged in.

## Author checklist

- [ ] Taste OK / further kills: ___
- [ ] Pangram (optional): label= ___ ; vs origin: softer / match / harder
- [ ] Fold new kills into `2026-07-22_author-antislop-hits.md`?
