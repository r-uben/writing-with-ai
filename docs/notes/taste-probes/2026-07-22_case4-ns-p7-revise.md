# Case 4 — NS grok probe → P7 / anti-slop revise

**Date:** 2026-07-22  
**Seed:** `2026-07-22_nakamura-steinsson-taste-probe.md` (grok-style)  
**Origin:** AI-generated (AI revise of AI)  
**Pass:** consolidated `/writing` anti-slop + P7 (levers from Case 1)  
**Pangram:** author to run after taste OK — secondary only

## Detect (before)

| Quote | Rule | Fix |
|---|---|---|
| “Missing variables are not the whole problem; confounding is.” | binary contrast | State confounding directly |
| “falls away” | soft metaphor | “are outside the window” |
| “Identification improves; power does not.” + stacked shorts | metronome / P1 | Keep one short pivot; weld neighbors |
| “rewrites what the measured shock means” | puffery | “changes what the measured shock identifies” |
| “9/11-type” | register | Keep September 2001 episode in plain terms (seed had it) |

## After (revise)

Most interest-rate changes are endogenous. Even after a VAR absorbs observables, the residual variation still mixes policy with macro news: the remaining bias is confounding, not only an incomplete control set.

High-frequency identification measures unexpected rate changes in about 30 minutes around scheduled FOMC releases. Public information at the start of the window is already in prices, so episodes such as September 2001 that a monthly VAR can misattribute as policy lie outside the window. Identification is cleaner than in monthly VARs; statistical power is not. Shock standard deviation is only about 5 basis points — too small to follow output quarters ahead — so inference lives in contemporaneous financial objects: TIPS yields, forwards, and survey expectations. Distant real effects cannot be recovered directly from these shocks; what can be measured is how markets reprice real and nominal claims when the announcement lands.

On that scale, policy news moves short-horizon nominal and real rates — roughly 106 basis points on two-year real yields, with two-year nominal forwards peaking near 114. Markets treat monetary shocks as real-rate relevant even as longer-run real effects fade. Part of the short-run move is information, not only transmission: the rate change reveals the Fed’s private assessment. Ten-year forwards can go negative when the inflation channel dominates. Clean short-horizon evidence of non-neutrality therefore coexists with low power and with an information effect that changes what the measured shock identifies for causal work.

## Author checklist

- [ ] Taste OK / further kills: ___
- [ ] Pangram (optional): label= ___ ; vs origin: softer / match / harder
- [ ] Fold new kills into `2026-07-22_author-antislop-hits.md`?
