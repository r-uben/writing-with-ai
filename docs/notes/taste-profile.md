# Taste profile — elicited writing preferences

**Started:** 2026-07-18  
**Overnight AI proposals (2026-07-19):** see `docs/notes/taste-probes/` — Q3–Q5 recommendations + draft P3–P5. **Not author judgments.** Confirm or reject here yourself after writing Track B blind.

**Purpose:** capture the author's *taste* (what they judge good vs. bad prose) as clean personalization signal for Draft Mode. Built one judgment at a time from concrete minimal-pair passages; each answer yields a distilled principle that feeds D3 (positive levers) and D4 (contrast + the author's own "why").

**Why this works when a voice corpus doesn't.** There is no clean sample of the author's *unaided* prose (the JMP is substantially AI-assisted, per author, 2026-07-18). But *taste* is elicitable directly and live, uncontaminated. Preferences are clean signal even though the prose isn't. And eliciting "which is better, and why" is exactly the TICL contrast structure the evidence favours over piling on positive exemplars.

**Honest scope — read this.** This captures *aspirational* taste (what you admire), not *native* voice (how you write unaided). People routinely admire prose they don't naturally produce. So a taste-conditioned drafter writes toward the register you *value*, which for a drafting tool is the right target — but it is "write toward what I admire," not "write like me." Do not let it drift into a claim about origin or authorship.

**Method.** Each question is a forced choice between two real, non-strawman passages that differ on ONE dimension, both competent, so the pick reveals taste and not quality. The *reason* is the load-bearing signal — capture it, not just the pick.

---

## Elicited principles (the executable rules — distilled from answers)

- **P1 (register): sustained flow as the baseline, a short hard declarative at each argumentative pivot.** Not uniformly punchy (A) nor uniformly periodic (B). The long, qualification-rich sentence carries setup and nuance; a very short declarative lands at the pivot where the mechanism turns or resolves (e.g. "It will tighten."). This is exactly the panel's rewarded *pivot short-declarative* move — high sentence-length variance is a byproduct of it, not a target. **Trigger = the argumentative pivot, not author discretion**, so it stays executable (otherwise "combine both" degrades to random). Reason: punch reserved for impact; flow for the reasoning. **Confirmed 2026-07-18:** trigger = the argumentative pivot; ~1–2 per section, scarcity gives force. Already encoded in D3 (S2/burstiness bullet).
- **P2 (certainty): assert flat by default; soft/apologetic hedging is slop, banned.** Author read the calibrated "show-the-seam" register as "pure AI slop." Lean S10 (confident) hard; zero tolerance for S4/S11 wool ("may suggest", "somewhat", "it is worth noting"). **Carve-out (pending author ruling):** a genuine limit — e.g. a point estimate that would otherwise read as a law — should still be *stated*, but as a hard short declarative in the A register ("The size is not."), never as a soft qualifier. This is "no wool," not "no limits": dropping all limits would violate S7 and risk referee-punished overclaiming. The fix is stating the limit in the punchy register, not hiding it.

## Judgment log (raw)

| # | Date | Dimension | Options | Pick | Reason | Principle extracted |
|---|------|-----------|---------|------|--------|---------------------|
| 1 | 2026-07-18 | Register / rhythm | A punchy short-declarative vs. B sustained periodic | **A, then refined** | Wants a combination: sustained baseline, punch deployed "when we should" — not uniform | P1 (revised) |
| 2 | 2026-07-18 | Certainty / hedging | A assert flat vs. B show-the-seam | **A** | "B is pure AI slop" — reads soft calibration as slop | P2 (+ carve-out pending) |
| 3 | 2026-07-19 | P2 carve-out / limits | **A:** "We cannot identify the long-run multiplier from this design. The size is not." vs. **B:** "While our estimates are informative, the long-run multiplier may be somewhat uncertain and should be interpreted with caution." | | | |
| 4 | 2026-07-19 | Opening move | **A:** "On January 29, 2018, the two-year Treasury yield moved 8 basis points in the 30 minutes after the FOMC statement." vs. **B:** "A central question in macroeconomics is how monetary policy affects the economy." | | | |
| 5 | 2026-07-19 | Citation weave | **A:** "\citet{nakamura2018} show that high-frequency windows around FOMC announcements isolate policy shocks; \citet{romer2004} reach a similar conclusion with narrative shocks." vs. **B:** "High-frequency identification is well established in the literature (Nakamura and Steinsson, 2018; Romer and Romer, 2004; Kuttner, 2001)." | | | |
