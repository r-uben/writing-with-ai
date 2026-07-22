# Nakamura–Steinsson taste probe — full AI option

**Date:** 2026-07-22  
**Status:** AI proposal for author comparison — **not Track B**  
**Concept:** nakamura-steinsson-2018 (high-frequency monetary identification / information effect)  
**Paper:** Nakamura & Steinsson (2018, QJE) — library `2018__nakamura_steinsson__high_frequency_identification_of_monetary_non_neutrality_the_information_effect__QJE`  
**Constraints applied:** draft from confirmed outline + supplied numbers only; empirical macro / identification register; ~220 words; no detector-chase; no Track C paste  
**Voices:** gpt-style, grok-style, terse-alternative (all authored in-session as distinct registers)

---

## gpt-style (~227 words)

Do interest-rate movements identify the real effects of monetary policy? Most observed rate changes are endogenous responses to the same news that moves output and inflation, so residual variation after VAR controls still mixes policy with confounding macro information. The identification problem is confounding, not missing controls alone.

High-frequency measurement around scheduled FOMC announcements addresses that mix. Unexpected rate changes in a roughly 30-minute window are useful because everything public before the window is already priced; episodes such as September 2001 that a monthly VAR can misattribute as policy are outside the window and drop out. Identification is clean; power is not. The monetary shocks have a standard deviation of only about 5 basis points — too small to trace output quarters ahead. Inference therefore lives in contemporaneous financial objects: TIPS yields, forwards, and survey expectations.

Scaled this way, policy news moves short-horizon nominal and real rates — about 106 basis points on two-year real yields, with two-year nominal forwards peaking near 114 basis points — so markets treat monetary shocks as mattering for real rates even though longer-run real effects fade. Part of the short-run response is an information channel: markets read the rate move as a signal of the Fed's private assessment of the economy, not only as a pure shift in policy stance. Ten-year forwards can even turn negative when that inflation channel dominates.

### Move self-report
| Move | Present? |
|---|---|
| `incumbent→defect→our-fix` | yes — VAR endogeneity → residual confounding → HF window |
| `big-question-opener` | yes — opens on identifying real effects of policy |
| `concrete-episode-as-evidence` | yes — September 2001 / VAR misattribution |
| `plain-mechanism-before-math` | yes — pre-window public info already priced |
| `concede-own-limitation-early` | yes — clean ID, low power / ~5 bp |
| `enumerated-gaps` | no |
| `rhetorical-question-pivot` | no — opener question is `big-question-opener`, not a mid-intro pivot |
| `quantitative-anchor` | yes — 5 bp; 106 bp; 114 bp |
| `scope-fence` | yes — inference in contemporaneous financial objects, not delayed output |

---

## grok-style (~213 words)

Most interest-rate changes are endogenous. VARs absorb observables and still leave residual bias: the remaining variation confounds policy with macro news. Missing variables are not the whole problem; confounding is.

The high-frequency fix measures unexpected rate changes in about 30 minutes around scheduled FOMC releases. Public information at the start of the window is already in prices, so 9/11-type misattribution falls away. Identification improves; power does not. Shock standard deviation is only about 5 basis points — too small to follow output quarters ahead. Contemporaneous financial objects are where inference lives: TIPS, forwards, survey expectations. We cannot directly recover distant real effects from these tiny shocks; we can measure how markets reprice real and nominal claims when the announcement lands.

On that scale, policy news moves short-horizon nominal and real rates — roughly 106 basis points on two-year real yields, with two-year nominal forwards peaking near 114. Markets treat monetary shocks as real-rate relevant even as longer-run real effects fade. Part of the short-run move is information, not pure transmission: the rate change reveals the Fed's private assessment. Ten-year forwards can go negative when the inflation channel dominates. Clean short-horizon evidence of non-neutrality therefore coexists with low power and with an information effect that rewrites what the measured shock means for causal interpretation.

### Move self-report
| Move | Present? |
|---|---|
| `incumbent→defect→our-fix` | yes — endogenous rates / VAR residual → HF fix |
| `big-question-opener` | no — opens on the identification defect |
| `concrete-episode-as-evidence` | yes — 9/11-type misattribution |
| `plain-mechanism-before-math` | yes — window pricing logic in words |
| `concede-own-limitation-early` | yes — “Identification improves; power does not” + 5 bp |
| `enumerated-gaps` | no |
| `rhetorical-question-pivot` | no |
| `quantitative-anchor` | yes — 5 bp; 106 bp; 114 bp |
| `scope-fence` | yes — cannot recover distant real effects; can measure announcement repricing |

---

## terse-alternative (~206 words)

Interest-rate changes mostly respond to the same news that drives the real economy; VAR residuals still confound policy with macro information. The defect is residual confounding, not merely an incomplete control set.

High-frequency identification measures unexpected rate moves in a roughly 30-minute window around scheduled FOMC announcements. Pre-window public news is already priced, so September-2001-style misreads drop out. Identification is clean; statistical power is not. Shock standard deviation is about 5 basis points — too small to trace output quarters ahead — so inference sits in contemporaneous TIPS yields, forwards, and survey expectations rather than in delayed real aggregates.

Scaled responses show large short-horizon rate effects: roughly 106 basis points on two-year real yields and a two-year nominal-forward peak near 114, while ten-year forwards can turn negative on the inflation channel. Markets therefore price monetary news as real-rate relevant at short horizons even as longer-run real effects fade. Part of that short-run response is an information effect — markets infer the Fed's private assessment of the economy — not only mechanical transmission from policy stance. The design separates announcement-window surprises from ambient macro news; it does not deliver a pure policy shock stripped of information content, and that distinction matters for what the measured non-neutrality means.

### Move self-report
| Move | Present? |
|---|---|
| `incumbent→defect→our-fix` | yes — VAR confounding named, then HF design |
| `big-question-opener` | no |
| `concrete-episode-as-evidence` | yes — September-2001-style misreads |
| `plain-mechanism-before-math` | yes — pre-window news already priced |
| `concede-own-limitation-early` | yes — clean ID / low power / 5 bp |
| `enumerated-gaps` | no |
| `rhetorical-question-pivot` | no |
| `quantitative-anchor` | yes — 5 bp; 106 bp; 114 bp |
| `scope-fence` | yes — separates window surprises; does not yield pure stance shocks |

---

## Verify before use

- [ ] ~30-minute window around scheduled FOMC announcements — NS outline / paper
- [ ] Monetary shock SD ≈ 5 basis points — supplied number (verify scaling in paper)
- [ ] 2-year real yield response ≈ 106 bp (their scaling) — supplied number
- [ ] 2-year nominal forward peak ≈ 114 bp; 10-year forward can go negative on inflation channel — supplied numbers
- [ ] September 2001 / 9/11 as VAR misattribution example — outline concrete episode (not a new claim)
- [ ] Information effect = markets reading Fed private assessment, not only pure policy stance — central claim / outline punchline
- [ ] No invented quantities, citations, or results beyond the fixture outline

---

## Paper-lookup notes (for your B write — outline refresh only)

From `fixtures/nakamura-steinsson-2018.md` (do not open Track C while writing Track B):

- Endogenous rates + VAR residual confounding is the incumbent defect; HF FOMC window is the fix.
- Power trade-off is first-class: ~5 bp shocks → contemporaneous financial objects, not quarterly output paths.
- Punchline couples short-horizon real-rate non-neutrality (~106 bp on 2y real, scaled) with an information channel.
- Human NS-specific moves to watch: `big-question-opener`, `concede-own-limitation-early` (plus shared spine / episode / mechanism / scope-fence).
- MS discriminators to re-test: `enumerated-gaps`, `rhetorical-question-pivot`.

**Do not open Track Q/P, Track C, or this probe while writing Track B.** Use `fixtures/nakamura-steinsson-2018.md` outline only.

---

## Comparison worksheet (fill on compare)

| Dimension | Your B / Track C | gpt-style | grok-style | terse | Prefer |
|-----------|------------------|-----------|------------|-------|--------|
| Opening | | big-question | defect-first | defect-first | |
| Early power/limitation concede | | yes | yes | yes | |
| Enumerated gaps | | no | no | no | |
| Rhetorical-question pivot | | no | no | no | |
| Mechanism compression | | window pricing | window + scope fence | window + purity fence | |
| Overall register | | | | | |

Notes:
