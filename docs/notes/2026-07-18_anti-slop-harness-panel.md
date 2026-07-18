# Anti-slop harness panel: which drafting harness produces the least sloppy academic prose?

**Date:** 2026-07-18
**Method:** `anti-slop-paragraph-lab` workflow (run `wf_ad14cea3-000`), 15 agents, ~634k tokens, ~4.5 min.
**Question:** Holding the argument fixed, which generation-time harness yields prose a blind cross-vendor panel judges least sloppy? This measures **register quality only** — it says nothing about Pangram/AI-origin detection (established separately: origin and register quality are decoupled; see `2026-07-18_ai-writing-quality-and-detectors.md`).

## Design

- **Fixture:** the same forward-guidance/time-inconsistency claim + 3-beat outline used in the Pangram tests, ~200–220 words per draft, theory prose only.
- **8 strategies** (7 survived — `kimi-anti-tell` died on an exhausted Kimi billing-cycle quota):
  baseline (no constraints, slop control) · anti-tell (generation-time constraints from skill D3) · ticl (anti-tell + negative slop exemplar + why it fails) · persona (specific-scholar habits) · exemplar (voice-conditioned on the Andrade et al. human passage) — all Claude — plus the anti-tell harness on GPT-5.6-sol and Grok-4.5.
- **Blind panel:** drafts labeled P1–P7 in fixed shuffled order, provenance hidden. Judges: Claude, GPT-5.6-terra, Grok-4-fast, DeepSeek-v4 (kimi-k3 judge also lost to quota). Each judge: per-passage slop markers (exact quotes), slop level, and a full ranking.
- **Deterministic metrics** (separate agent, bash only): sentence count, mean/SD sentence length, tell-word hits.

## Results

Mean rank across 4 judges (lower = better):

| Strategy (drafter) | Mean rank | Slop levels (4 judges) |
|---|---|---|
| **ticl** (claude) | **1.50** | none ×4 |
| **anti-tell** (claude) | **1.50** | none ×3, light ×1 |
| persona (claude) | 3.00 | none ×2, light ×2 |
| exemplar (claude) | 4.50 | light ×4 |
| gpt-anti-tell (gpt) | 4.75 | light ×4 |
| baseline (claude) | 6.00 | light ×3, moderate ×1 |
| grok-anti-tell (grok) | 6.75 | light ×2, moderate ×2 |

Headline findings:

1. **Generation-time constraints matter.** The unconstrained baseline finished worst of the five Claude-drafted passages (drafter held fixed), flagged by every judge for stock register ("do the heavy lifting", "in the classic sense", "supposed to take over"). Quality cannot be deferred entirely to a revision pass.
2. **ticl ≈ anti-tell: statistical tie at the top** (identical mean rank, 2 first-place votes each). The tiebreak toward ticl rests only on cleaner slop-level ratings. The negative exemplar cost nothing but is not proven to add anything at n=1.
3. **The static tell-word lexicon has zero discriminating power.** Every draft scored 0 hits — yet judges found abundant slop in the low-ranked drafts. What they actually penalized was *stock academic register* off any list: "do the heavy lifting" (3 drafts), "in the classic sense", "the standard prescription", connector scaffolding (yet/therefore/thus), throat-clearing openers. The lexicon is either fully avoided by all modern harnesses or too narrow to matter; either way it is dead as a metric.
4. **Sentence-length SD tracked quality loosely and non-monotonically.** The two winners had the highest SDs (15.6, 12.2), the smooth losers the lowest (~9.1–9.5), but the middle breaks the ordering. Best read: SD is a *byproduct* of the specific rewarded move — a very short declarative sentence at the argumentative pivot ("It will tighten. Nothing binds it, and everyone knows nothing binds it") — not an independent target.
5. **No same-family favoritism.** Grok-fast ranked its own family's draft last; GPT-terra put its own 5th; the DeepSeek judge (no draft in the set) matched the consensus. All four judges agreed on the same top-3 and bottom-2 sets.
6. **Vendor transplants underperformed** (grok-anti-tell last, gpt-anti-tell mid-pack) — but strategy is confounded with drafter identity, so this cannot separate "anti-tell lists don't transfer across vendors" from "those drafters wrote worse prose here."

## Transferable levers (what separated winners from losers)

- **The memorable line must compress the mechanism, not decorate it.** Winners: "The bank that must keep the promise is not the bank that made it"; "credible because it is redundant"; "a check the bank's present self writes on an account its future self controls" — each *is* the time-inconsistency argument. Loser: a contentless chiasmus flagged as "gesturing at profundity rather than earning it."
- **The argument, not connectors, carries transitions.** P2 was penalized precisely for yet/therefore/thus scaffolding.
- **Concrete agents and verbs over abstract summary.** "The future committee inherits the inflation, not the recession" vs. the flagged "Markets understand the incentive structure and price the announcement accordingly" — same claim, one owned, one filler.
- **Rhythm breaks at pivots** (the short-declarative move above).
- **Stock academic phrases are slop even off any tell list.** Test: could the phrase appear unchanged in a hundred other papers?
- **Owned first-person stance and colloquial grace notes help at the margin** ("I argue", "for a spell" — unanimous third place).

## Actions taken (same day)

Applied to `skill/SKILL.md` (D3/D4), as small evidence-backed refinements — **not yet independently reviewed**:
- D3: burstiness operationalized as the pivot short-declarative move rather than a variance vibe; stock-register test added ("a hundred other papers"); memorable-formulation constraint upgraded to "must compress the mechanism; decorative symmetry gets cut"; argument-carries-transitions constraint added; one first-person move + occasional colloquial grace note allowed.
- D4: self-critique now includes a stock-register hunt, a connector strip, and the memorable-line test.

Deferred (recorded, not applied):
- Widening D6 to a cross-vendor panel (feasible per this run — no favoritism, strong consensus — but a per-draft cost increase the current single-judge design doesn't need yet).
- Unconfounded re-test of list transferability (same drafter, different constraint lists).
- Replacing the deterministic tell-lexicon metric: needs a better operationalization (stock-phrase detection is judgment, not grep) — fold into the calibration-panel work.

## Caveats

- n = 1 draft per strategy, one highly canonical topic; sub-point rank gaps are noise. Nothing here generalizes automatically to less rehearsed arguments.
- All judges are LLMs and may share training-data aesthetics; cross-vendor agreement is reassuring, not human validation. `reads_human=true` for all 7 drafts — that field hit a ceiling and discriminates nothing.
- The synthesis agent flagged near-identical Claude/DeepSeek judge notes on P1 as possible contamination. On inspection the likelier cause is prompt echo: the judge prompt itself supplied the phrase "the argument carries the transitions," and both judges reused it; their *rankings* differ (P6-first vs P1-first), which cuts against contamination. Logged, not alarming.
- **This experiment does not touch the Pangram question.** All seven drafts are AI-origin — and this was confirmed empirically the same day: the ticl co-winner was pasted into the live Pangram tool and scored **100% AI** (Variant D in `2026-07-18_ai-writing-quality-and-detectors.md`). Panel-judged register quality has zero effect on origin detection. The decisive experiment there remains Variant B (human from-memory rewrite).

## Appendix: the seven drafts

### ticl (claude) — co-winner
Forward guidance fails where it is needed most. At the effective lower bound, with the policy rate pinned at zero, announcements about the future path of rates are the central bank's remaining instrument, and it is precisely there that their force drains away. This paper argues the weakness is not incidental but structural, built into the logic of the promise itself.

The mechanism is familiar. Guidance stimulates today only if it commits the bank to stay loose tomorrow: to hold rates down after the recovery has arrived, to let inflation run above the two-percent target, to be looser than it will then want to be. That last clause is the problem. Once the economy recovers, the overshoot serves no purpose the future bank recognizes; reneging costs nothing it then values, and an inflation-targeting institution built to fight overshoots will fight this one too. The bank that must keep the promise is not the bank that made it.

Markets price the promise, not the announcement. Rational investors weight the commitment by the probability it survives the recovery, so expected future rates fall by less than the bank intends and long yields barely respond. The stimulus arrives pre-shrunk, discounted at the source by the very credibility the bank spent decades building for the opposite purpose.

### anti-tell (claude) — co-winner
Forward guidance fails where it matters most. Away from the effective lower bound, a promise of low future rates merely restates the central bank's reaction function; it is credible because it is redundant. At the bound, where the policy rate is spent and announcements must do the work of stimulus, guidance can add power only by departing from that reaction function: the bank must pledge to hold rates down after the recovery arrives, accepting inflation above its two-percent target for longer than it would ever choose in the moment. Guidance is thus strongest where it is superfluous and weakest where it is essential.

The weakness is structural, not rhetorical. The promised overshoot is the whole mechanism, since only expected future accommodation can lower long rates today; yet once recovery comes, honoring the promise is pure cost to a bank that targets two percent. The future committee inherits the inflation, not the recession. It will tighten. Nothing binds it, and everyone knows nothing binds it.

Markets price accordingly. They discount the pledge by the odds it will be honored, so the stimulus arrives pre-shrunk: the deeper the slump, the larger the required overshoot, and the steeper the discount. This paper makes that erosion precise.

### persona (claude) — unanimous third
Forward guidance is supposed to matter most when the policy rate can fall no further. At the effective lower bound the conventional instrument is gone, and whatever leverage the central bank retains runs through expectations: it must move the long end of the curve by describing what it will do tomorrow. Yet this is precisely where guidance underperforms. The tool asked to carry the whole burden is weakest where the burden sits.

I argue this is not an anomaly but a consequence of what the tool is. Guidance works by promising future accommodation: the bank commits to holding rates low after the recovery arrives, tolerating inflation above its two-percent target for a spell, so that expected looseness tomorrow raises demand today. That promise is time-inconsistent in the classic sense. Once the recovery comes and inflation runs past target, the future committee inherits every incentive (mandate, reputation, hard-won credibility) to renege. The commitment is a check the bank's present self writes on an account its future self controls.

Markets know this. They price the promise at the probability it survives, which is to say at a discount, and the stimulus arrives pre-shrunk. The credibility that anchors ordinary policy, the settled belief that the bank will not let inflation run, is the very thing that disarms guidance when nothing else is left.

### exemplar (claude)
When the policy rate reaches its effective lower bound, the central bank loses its usual instrument and is left, mostly, with words. Forward guidance is the standard prescription: the bank promises to hold rates low beyond the point at which it would ordinarily tighten, and the expectation of future accommodation substitutes for accommodation it cannot deliver today. This paper argues that the prescription fails on its own terms. Forward guidance is weakest where it is supposed to do the heavy lifting.

The difficulty is one of incentives, not of communication. The stimulus in a lower-for-longer promise comes from what it implies about the recovery: the bank must let inflation run above its two-percent target after the constraint stops binding, at a moment when nothing compels it to. A bank that cares about the target while rates are at zero will care about it just as much once they are not. The promise to overshoot is therefore time-inconsistent, and the future bank's preferences are common knowledge.

Markets know this. The announcement trades at a discount to face value, and the discount is largest when the trap is deepest, since that is when the promised overshoot, and the temptation to renege, are largest. The bank announces a large stimulus and delivers a small one; the shortfall is built in from the start.

### gpt-anti-tell (gpt-5.6-sol)
Forward guidance is weakest at the effective lower bound, precisely where conventional policy has run out of room and expectations must do the work. The instrument asks words to substitute for rate cuts just when the promise behind those words is hardest to believe.

Its force comes from committing today to keep policy loose after the economy recovers and inflation begins to rise. That commitment must include some tolerance for inflation above the bank's target, perhaps above two percent, because an immediate return to the usual rule would leave future short rates too high to lift current demand. Yet once recovery arrives, the future central bank inherits the inflation but not the recession that justified the promise. It then has every reason to tighten. The guidance is therefore time-inconsistent: the policy that is optimal to announce in the slump is no longer optimal to carry out in the recovery.

Markets understand the bank's future incentives. They discount the promised overshoot before it can lower expected real rates, so the intended stimulus reaches the present already diminished. Forward guidance thus carries its own credibility haircut: the more its success requires tomorrow's bank to tolerate inflation it would rather suppress, the less relief today's economy receives. At the lower bound, the promise does not fail after policy changes course. It arrives pre-shrunk.

### baseline (claude) — slop control
When conventional policy runs out of room, forward guidance is supposed to take over. A central bank that can no longer cut its policy rate can still, in principle, shape the expected path of future rates and thereby stimulate demand today. This paper argues the instrument is weakest precisely where it is invoked: at the effective lower bound, the one place it is asked to do the heavy lifting.

The weakness is built into the promise itself. Guidance has bite only if it commits the bank to actions it will later regret: holding rates low deep into the recovery and tolerating the inflation overshoot that results, above the two-percent target it exists to defend. When that future arrives, the bank confronts a closed output gap and above-target inflation; its optimal policy is to tighten, and nothing binds it to the earlier pledge. The promise is time-inconsistent in the classic sense: optimal to announce ex ante, suboptimal to execute ex post.

Markets price this. Anticipating that the future bank will renege, they weight the promised path by the probability it survives the recovery, and discount the rest. Long rates fall by less than the announcement implies; the stimulus arrives pre-shrunk. The failure is not one of communication but of incentive, and no refinement of language can talk it away.

### grok-anti-tell (grok-4.5) — consensus loser
Forward guidance is weakest precisely where policy most needs it: at the effective lower bound. When the policy rate can fall no further, the central bank's remaining instrument is a promise about the future path of rates — a commitment to keep policy loose after the recovery has begun, and to tolerate inflation above the two-percent target for a time. That promise is what gives guidance its bite. It is also what undoes it.

The future bank has every reason to renege. Once demand has recovered and inflation is already pressing the target from below, the case for deliberate overshoot evaporates; a bank that cares about its mandate will tighten, not linger. The commitment is therefore time-inconsistent: it asks the institution to act, later, against the preferences it will then hold. Markets understand the incentive structure and price the announcement accordingly. They treat the promised path as a statement of present intention, not a binding rule.

The result is a stimulus that arrives already discounted. Forward guidance works by shifting expected short rates and, through them, longer yields and demand today; when agents assign low weight to the overshoot, those expectations barely move. The tool fails not because the message is unclear, but because the credibility it requires is hardest to manufacture exactly when the lower bound binds. What remains is verbal accommodation without the commitment that would make accommodation real.
