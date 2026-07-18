# Prose-exemplar ratings: which field writers to condition D3 on

**Date:** 2026-07-18
**Method:** 3 parallel `general-purpose` readers, 12 genre-matched monetary/macro/finance papers from the local Papers library. Each read clean PDF-text-layer prose (Intro + one prose section; OCR markdown avoided — it hallucinates boilerplate) and scored a fixed 10-criterion rubric (the 20-rule levers: precision opening, rhythm, conclusion-first, argument-carried transitions, mechanism-compressing lines, low stock-register, quantitative anchoring, jargon discipline, first-person ownership, distinctive voice) with quoted evidence.
**Purpose:** pick positive exemplars + build the TICL *contrast* set for Draft Mode D3/D4. NOT imitation targets — the `exemplar` strategy (naive imitate-this-passage) already ranked 4th of 7 on slop (see `2026-07-18_anti-slop-harness-panel.md`). Doubles as the human calibration corpus `STATUS.md` wants for Layer-1 thresholds.

## Ranked ratings

| Rank | Author (year) — venue | Overall | Signature lever | Weakest habit (the anti-example) |
|---|---|---|---|---|
| 1= | Cochrane (2004) — NBER discussion | 9/10 | Mechanism as bare declarative, then justify with a concrete number/example | Slide-note fragments (format, not prose) |
| 1= | Nakamura & Steinsson (2018) — QJE | 9/10 | Plain-English mechanism intuition paired to every empirical claim; relentless numeric anchoring | Stock opener: "A central question in macroeconomics is…" |
| 1= | Gürkaynak, Sack & Swanson (2005) — IJCB | 9/10 | Open on a dated, fully-quantified anomaly; structure around one memorable antithesis | Mild "Thus…" scaffolding at policy turns |
| 1= | Morris & Shin (1998) — AER | 9/10 | Force the abstract mechanism into plain aphoristic compression | Two-paragraph motivational throat-clear before "We argue…" |
| 5 | Caballero & Simsek (2022) — AER | 8/10 | "Concretely, suppose…" — run one scenario through the mechanism before generalizing | therefore/however/moreover mortar; "First…Second…Third…Finally" |
| 6 | Jarociński & Karadi (2020) — AEJ:Macro | 8/10 | "Consider a revealing example" then numbered plain-language mechanism | Stock opener: "a classic question in macroeconomics" |
| 7 | Sims (1992) — EER | 7.5/10 | Open by naming the genuine limit of knowledge, then adjudicate ("the range of our ignorance") | Sprawling subordinated sentences |
| 8 | Angeletos & Lian (2022) — REStud | 7/10 | Bold run-in claim-labels putting each subsection's conclusion in the first 3 words | AD/AS/GE/TFP acronym clotting |
| 9 | Woodford (2003) — monograph | 7/10 | Confident first-person, project-owning stance | Monograph pacing: grand-sweep openers, buried thesis, decorative lines |
| 10 | Shiller (2017) — AER address | 6.5/10 | Sustain one outside-discipline metaphor as connective tissue | "My goal in this paper is to describe…" signposting; loose accreting sentences |
| 11 | Ramey (2016) — Handbook | 6/10 | Never state a result without its specific number + source in the same sentence | Roadmap signposting; generic survey register |
| 12 | Bauer & Swanson (2023) — WP | 5/10 | (organizational only: explicit two-part roadmap) | "Over the past two decades…" open; stacked Thus/Moreover/In addition |

## The payoff: convergent levers and convergent tells

**Levers that recur at the top (the positive contrast set):**
- Mechanism-as-plain-declarative, then justify — Cochrane ("The Fed never rolls dice; every move is a response to something"), N&S, Morris & Shin ("everyone may know that the fundamentals are sound, but it may not be that everyone knows that everyone knows this").
- Open on a specific dated quantified anomaly — GSS (Jan 28 2004, 20–25bp), J&K (March 20 2001), Caballero & Simsek (Dec 2007 FOMC + live WSJ quote).
- Concrete-instantiation before generalizing — "Concretely, suppose…" / "Consider a revealing example".
- Numbers welded into the claim sentence — Ramey, N&S, GSS.
- Name the limit honestly — Sims.

**Tells that recur even among 9/10 writers (the negative contrast set — and the key finding):** stock big-question openers, connector scaffolding (therefore/however/moreover/thus), roadmap signposting, acronym clotting. Nakamura & Steinsson and Jarociński & Karadi both open on a throat-clearing "classic question" sentence and still earn 8–9/10 on everything after.

**Implication (re-confirms the project thesis from the good-writer side):** the "AI tells" are register markers, not origin markers — the best *human* writers in the field emit them too. This is the same conclusion the Variant C human control gave, now from admired prose rather than a single pre-2022 passage. It also means the contrast set can be built almost entirely from real field writing: good move (their best line) vs. slop move (their own weakest habit), both quoted.

## Recommendation

- **Positive exemplars (top 4):** Cochrane, Morris & Shin, Nakamura & Steinsson, Gürkaynak–Sack–Swanson. Distinct, complementary levers; all 9/10.
- **Single-lever pickups:** Caballero & Simsek ("Concretely, suppose…"), Sims (name-the-limit opening), J&K (flag-and-mine a concrete example).
- **Counter-example bank:** Bauer & Swanson (openers + connector reliance) and Ramey (roadmap signposting) as the negative side — clear, competent prose that is nonetheless mostly template, exactly what to train against.
- **Use as TICL contrast in D3/D4, not imitation.** Extract the lever + a quoted good line and pair it with the quoted anti-example; do not instruct "write like Cochrane."

## Open / next
- Build the contrast set into D3/D4 from the quoted pairs above (pending user greenlight on the authority set — corpus should reflect the author's taste, not the rater's).
- These 12 (clean PDF text) are the seed of the Layer-1 calibration corpus; deterministic metrics (sentence-length SD, stock-phrase detection) can be derived against them.
- Caveat: n=1 paper per author; scores are one reader's judgment against the rubric, evidence-quoted but not inter-rater-validated.
