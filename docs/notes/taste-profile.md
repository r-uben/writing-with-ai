# Taste profile — elicited writing preferences

**Started:** 2026-07-18  
**Q3–Q5 confirmed:** 2026-07-22 (author). Overnight AI proposals in `docs/notes/taste-probes/` were recommendations only.

**Purpose:** capture the author's *taste* (what they judge good vs. bad prose) as clean personalization signal for Draft Mode. Built one judgment at a time from concrete minimal-pair passages; each answer yields a distilled principle that feeds D3 (positive levers) and D4 (contrast + the author's own "why").

**Why this works when a voice corpus doesn't.** There is no clean sample of the author's *unaided* prose (the JMP is substantially AI-assisted, per author, 2026-07-18). But *taste* is elicitable directly and live, uncontaminated. Preferences are clean signal even though the prose isn't. And eliciting "which is better, and why" is exactly the TICL contrast structure the evidence favours over piling on more examples.

**Honest scope — read this.** This captures *aspirational* taste (what you admire), not *native* voice (how you write unaided). People routinely admire prose they don't naturally produce. So a taste-conditioned drafter writes toward the register you *value*, which for a drafting tool is the right target — but it is "write toward what I admire," not "write like me." Do not let it drift into a claim about origin or authorship.

**Method.** Each question is a forced choice between two real, non-strawman passages that differ on ONE dimension, both competent, so the pick reveals taste and not quality. The *reason* is the load-bearing signal — capture it, not just the pick. “Both / depends on context” is a valid answer when the dimension is conditional.

---

## Elicited principles (the executable rules — distilled from answers)

- **P1 (register): sustained flow as the baseline, a short hard declarative at each argumentative pivot.** Not uniformly punchy (A) nor uniformly periodic (B). The long, qualification-rich sentence carries setup and nuance; a very short declarative lands at the pivot where the mechanism turns or resolves (e.g. "It will tighten."). **Trigger = the argumentative pivot**; ~1–2 per section. **Confirmed 2026-07-18.** Encoded in D3 (S2/burstiness).

- **P2 (certainty): assert flat by default; soft/apologetic hedging is slop, banned.** Author read the calibrated "show-the-seam" register as "pure AI slop." Lean S10; ban S4/S11 wool ("may suggest", "somewhat", "it is worth noting") when the sentence is *not* stating a genuine limit.

- **P3 (limits / P2 carve-out): for genuine identification or scope limits, prefer explicit caution (Q3 = B), not punchy telegraphic denial.** Name what the design cannot deliver; allow “uncertain / interpret with caution” when the object of the limit is clear. **Do not** use that register for ordinary claims (P2 still bans wool there). **Do not** prefer A’s “The size is not.” as the default limit voice. **Confirmed 2026-07-22.**

- **P4 (openings): context chooses — concrete fact *or* a real setup question; never stock big-Q throat-clear.** When a dated/named/quantified fact is supplied, prefer opening on it. A field or section-frame question is fine when it states *this paper’s* job (aligns with S8 / W1). Still ban empty “A central question in macroeconomics is…” templates. **Confirmed 2026-07-22: both, depends on context.**

- **P5 (citations): context chooses — narrative when the source does sentence-level work; parenthetical clusters OK when ancillary.** Prefer `\citet` / narrative weave when each paper earns a clause. Parenthetical stacks are fine for established methods or secondary support where naming each role would be pedantic. **Confirmed 2026-07-22: both, depends on context.**

---

## Judgment log (raw)

| # | Date | Dimension | Options | Pick | Reason | Principle extracted |
|---|------|-----------|---------|------|--------|---------------------|
| 1 | 2026-07-18 | Register / rhythm | A punchy short-declarative vs. B sustained periodic | **A, then refined** | Combination: sustained baseline, punch at pivots | P1 |
| 2 | 2026-07-18 | Certainty / hedging | A assert flat vs. B show-the-seam | **A** | "B is pure AI slop" | P2 |
| 3 | 2026-07-22 | P2 carve-out / limits | A hard denial vs. B cautious limit | **B** | Prefers B for limits | P3 |
| 4 | 2026-07-22 | Opening move | A concrete fact vs. B stock field Q | **Both** | Depends on context | P4 |
| 5 | 2026-07-22 | Citation weave | A narrative vs. B parenthetical cluster | **Both** | Depends on context | P5 |
