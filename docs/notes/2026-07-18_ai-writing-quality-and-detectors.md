# AI-assisted scholarly prose: quality, tells, and ownership

**Date:** 2026-07-18
**Source:** `deep-research` harness — 6 search angles, 25 sources fetched, 116 claims extracted, 25 adversarially verified (23 confirmed, 2 refuted). Full task output: `tasks/wgk24oma2.output`.
**Framing:** writing quality and authorial ownership, with AI-text detectors as an imperfect *quality proxy* — not an evasion recipe. Two claims were killed in verification; recorded below so we don't build on them.

---

## Bottom line

Producing scholarly prose where the human supplies the idea and the AI drafts — yet the result reads as human-authored and carries real ownership — is a **writing-quality problem**, and the detector is a lagging proxy for it. The three legs:

1. **Detectors key on style fingerprints, not perplexity or topic.** Pangram is a supervised transformer, not a perplexity meter. You cannot reason about it as "predictable = flagged."
2. **The tells are register/style markers** — flowery verbs, low sentence-length variance, elevated formality — which are *exactly* the failure modes of good academic writing. Fixing them is a quality gain, not a trick.
3. **Minimal revision and felt ownership are in tension.** Ownership is partly effort-based; writers refuse to own a draft they didn't sweat over. "Human supplies idea, AI does the rest" secures *conceptual* ownership but not *effort-based* or *stylistic* ownership. This is the central design tension of the whole project.

---

## 1. What Pangram actually measures

- **Supervised transformer classifier**, trained on ~28M confirmed human documents (papers, books, student writing) plus LLM-generated **"synthetic mirrors"** — for each human text, an AI version matched on topic and length, so the model learns *"solely based on specific characteristics of LLM writing"* rather than topic. Hard-negative mining + active learning. [primary: arxiv 2402.14873v3]
- **Deliberately rejects perplexity methods** because they misfire on human texts that appear in LLM training corpora (e.g. the Declaration of Independence). So burstiness/perplexity intuitions describe *older* detectors, not Pangram.
- **Reported false-positive rate ~1 in 10,000** (0.004% academic essays, 0.000% medical papers, 0.23% recipes, 0.05% poetry). *Vendor self-reported*, only directionally corroborated by third parties (Chicago Booth testing ranked it first; Nature 2026 review keeps commercial tools <1%, Pangram lowest). [primary: pangram.com/blog]
- **False positives concentrate on** short (<~200 words), incomplete-sentence, formulaic, or underrepresented-domain text. Accuracy is strongest on long, complete-sentence, original text. Independent reviews: accuracy degrades under ~50 words, false positives cluster around 34 words.
- **Known bias (separate literature):** Liang et al. (Cell Patterns 2023) found GPT detectors misclassified 61.3% of non-native TOEFL essays as AI while near-flawlessly clearing native writers — detectors key on low lexical variety, which penalizes ESL writers. Relevant to the *fairness* critique of the whole enterprise.

## 2. The linguistic tells (all register/style, not content)

- **Excess vocabulary spike (2024 vs 2021–22 baseline):** `delves` r=25.2 (0.21 → 14.38 occurrences per million in abstracts, 2020–24), `showcasing` r=9.2, `underscores` r=9.1; also *intricate, meticulously, pivotal, realm, surpass*. [primary: Kobak et al. 2406.07016; focal-words 2412.11385]
- **These are style words, not topic words:** of 280 excess style words in 2024, **66% verbs, 18% adjectives**. Contrast genuine content shifts (Covid-era "coronavirus") which are nouns. Not explained by training-data frequency — focal words appear far less in ArXiv/Wikipedia/Leipzig than in ChatGPT output. **Implication:** neutralizing flowery verbs and register-flatness matters more than swapping nouns.
- **Low variance is the most robust structural tell:** human writing has scattered, high-variance sentence- and document-length distributions ("burstiness"); LLM output clusters tightly around the mean. News-text study: human sentence-length SD ~7 vs AI ~2.7; corroborating academic-prose figure: human SD ~8.2 vs GPT-4o ~4.1. [primary: 2308.09067; PMC12969083]
- **Elevated formality:** LLM prose shows a 54–72% reduction in informal language (LIWC) and over-prefers formal connectors — *furthermore, regarding, but also*. [medium confidence — single Portuguese-language news study, iScience]
- **More numbers, symbols, auxiliaries, pronouns** — an "objective-sounding" register (2-1 vote, weaker).

**Caveat — moving target:** the specific word list dates fast as models are steered away from flagged words. The *register-flatness principle* persists; the vocabulary is disposable. Corpora are biomedical abstracts + news; generality to long-form humanities/social-science prose is an extrapolation.

## 3. Generation / voice-transfer techniques

- **Frontier LLMs only partially imitate an author's implicit style** — better in structured genres (news, email) than informal (blogs, forums). [primary: "Catch Me If You Can? Not Yet", 2509.14543, 6 models, 400+ authors]
- **Piling on few-shot examples plateaus fast (~2–10).** Marginal effect of more examples is near-zero on style-alignment metrics — though few-shot still >> zero-shot. Volume is not the lever.
- **The lever is iterative contrast, not volume — TICL** (Trial-Error-Explain In-Context Learning): personalizes with **<10 of the author's own samples**, no fine-tuning, by adding **model-generated negative examples + stylistic explanations** to the prompt. Pairwise win rate up to 91.5% vs prior SOTA (upper bound; LLM-as-judge metric). [primary: 2502.08972] **Practical upshot: show the model what NOT to sound like, and why — a self-critique/contrast loop beats more exemplars.**
- **Personalization taxonomy:** prompting is one of four families (with RAG, representation learning, RLHF); "writing-style consistency with the user's prior text" is a named core criterion. [survey: 2411.00027]
- **Show-don't-tell:** few-shot exemplars of the author's own writing beat both generic style instructions and author-name prompting ("write like Hemingway"). [blogs: ninapanickssery, towardsai]

## 4. Where human input must land (ownership)

- **Ownership decomposes into stylistic, conceptual, and effort-based** subtypes. [primary: 2509.15440 creative co-writing; caveat: creative, not academic]
- **Academics want agency at planning/idea generation**, ceding more in translating/reviewing. Tools should calibrate intervention to where writers want control, not automate uniformly. [PRISMA review of 109 HCI papers + 15 interviews: 2504.12488]
- **Effort-based ownership is behaviorally real:** writers "would not take ownership over a draft until they had spent a great deal of time editing" (P14: *"I have to say that I did this, that I sweated it out"*). Fewer keystrokes / less time → lower felt ownership. [CHI 2026, n=18]
- **The tension, stated plainly:** the less the human revises, the weaker their ownership. Supplying the idea buys *conceptual* ownership; it does not buy the *effort-based* or *stylistic* ownership that scholarly accountability may require.

## Refuted in verification (do NOT build on these)

- ✗ "Human writing has greater lexical diversity than LLM output" (1-2). Contradicts the naive assumption; also the mechanism behind ESL false positives, so treat with care.
- ✗ "LLM text defaults to an average, generic tone that stays readily detectable" (1-2). Refuted — modern LLM output is *not* obviously robotic. Strengthens the case that this is a subtle-quality problem, not a "sounds like a robot" problem.

## Open questions (candidate first research bites)

1. Do the vocabulary + low-variance tells (from 2023–24 biomedical abstracts / news) transfer to long-form humanities/social-science prose, and how fast are they eroding?
2. **What minimum revision effort simultaneously secures felt ownership AND removes the statistical tells — can "minimal revision" and "real ownership" coexist, or are they fundamentally in tension?** (The load-bearing question for this project.)
3. How does Pangram respond to TICL-style, author-grounded idiolect drafts — does author-grounded style transfer lower detector confidence, and is that a quality gain or mimicry?
4. Does conceptual ownership (supplying the idea/argument) suffice for academic accountability, or do scholarly norms require effort-based and stylistic ownership too?

---

## Mapping to the existing `/writing` skill (skill/SKILL.md)

Several of the 20 style rules already target the documented AI-tells — on quality grounds, which is the convergence thesis made concrete:

| AI-tell (from research) | Covered by rule | Gap? |
|---|---|---|
| Low sentence-length variance (burstiness) | **S2** sentence rhythm | Covered in spirit; S2 has no *quantitative* target (SD/variance) |
| Flowery excess verbs (*delve, underscore, showcase*) | **S16** vivid specifics, **S17** jargon discipline | Partial — no explicit banned-register list |
| Hedging / apologetic register | **S11** no apologetic framing, **S10** confident not arrogant | Covered |
| Filler / formal connectors (*furthermore, it is worth noting*) | **S4** no filler | Partial — S4 lists filler, not formal connectors specifically |
| Register flatness / uniform paragraph shape | **S19** one idea per paragraph, **S2** | Weakly covered — no rule on inter-paragraph variety |
| Buried point / uniform structure | **S5** conclusion first, **S8** question-driven openings | Covered |

**Gaps worth a rule or a harness step:** (a) no quantitative burstiness check; (b) no explicit "excess-vocabulary" register flag; (c) the skill *reviews* prose — it has no *generation/drafting* or *voice-transfer* path, which is what the idea→draft→minimal-revision workflow actually needs.

## Implied harness shape (not yet built — for discussion)

Idea/concept (human) → **plan-then-write separation** (outline as a distinct step) → draft conditioned on **<10 author exemplars** → **TICL-style contrast loop** (generate, critique against negative examples + explanations, revise) → human **substantive revision** (the step that earns ownership) → optional detector check as a *quality proxy*, never the objective function.

The unresolved design decision is Open Question #2: how much revision is the minimum that both secures ownership and clears the tells.

---

## Design decisions (2026-07-18)

**Ownership reframed.** The "effort-based ownership" finding (writers won't own a draft until they've sweated over it) is rejected as a design constraint — it's a *psychological* claim, not a requirement. What is kept is **factual accountability**: the human owns the argument (conceptual) and vouches that every claim/number/citation is true. That is one verification pass, not heavy editing, and it is the charter's no-invention rule — not sentiment. "Minimal revision" is therefore compatible with the operating model, provided the verify pass happens.

**Draft mode added to `skill/SKILL.md`** (not a sibling skill — one skill, two modes). Pipeline: D1 parse concept → D2 claim outline (human steers here) → D3 draft with anti-tells as *generation-time* constraints (burstiness/S2, excess-vocab ban, no filler/hedging) → D4 TICL self-critique + one revision → D5 verify-before-use list (accountability) → D6 **independent evaluation, required** (drafting model ≠ sole reviewer, per charter; reuses the Antigravity/Gemini path).

**Evaluation architecture — two layers, decided:**
- *Layer 1, deterministic linguistic metrics* (no LLM, reproducible): sentence-length SD (burstiness), tell-word frequency scan, formality/TTR. Thresholds to be **derived from a human reference corpus**, not hardcoded (per global rule against magic numbers). Cheap pre-filter.
- *Layer 2, model judgment*: one independent judge in the production skill (existing Gemini slot). Hard rule: the drafting model is never on the panel.
- *Calibration panel (separate research step, not per-draft):* run 4–5 heterogeneous models (grok + kimi + gpt + fable + gemini) ONCE over (human paper / AI draft / AI-revised) samples to (a) see which tells each model catches, (b) validate that Layer-1 metrics track human judgment, (c) derive Layer-1 thresholds. This is what `/fanout` / `/claudex` are for. Deferred until draft mode is tested.

**Not yet done:** the calibration panel; deriving Layer-1 thresholds; testing draft mode on a real concept.

---

## Empirical result (2026-07-18): Pangram flags hand-tuned anti-tell prose at 100%

**Test:** the forward-guidance intro paragraph drafted via the new Draft Mode (D1–D5, anti-tells applied at generation: burstiness, no filler, no excess-vocab). 217 words. Independent Gemini judge (D6) reported *"no generic LLM tell-words found"* and praised sentence-length variance and conclusion-first structure.

**Pangram verdict (v3.3.2, live tool):** **100% AI-generated, Confidence High.** 1 AI segment (the whole text). Not a hedge — maxed out.

**Interpretation:**
- The naive convergence hypothesis — "remove surface tells + add burstiness ⇒ reads as human to a detector" — is **falsified** for Pangram. Exactly as the research predicted: Pangram rejects perplexity/burstiness heuristics *because they are gameable* and trains on synthetic mirrors to key on a deeper LLM-generation signature that survives cosmetic humanization.
- **Gemini-as-judge is not a proxy for Pangram.** Gemini said clean; Pangram said 100%. A general LLM cannot report what a supervised classifier keys on. Design consequence: Layer-2 model judgment measures *prose quality*, not detector risk — the two are now empirically decoupled here.
- **Vindicates the effort-based finding we discarded (partly).** Pangram is detecting a true fact — an LLM produced these tokens. The plausibly-only lever that moves it off 100% is substantial human rewriting, i.e. the revision effort the "minimal revision" goal wants to skip. So "AI drafts + minimal revision + passes Pangram" may be **mutually incompatible**, not a prompt-engineering gap.
- **Charter alignment:** a 100% score does not mean the prose is bad — it is decent. It means Pangram correctly detects AI *origin*. Since the charter optimizes for quality, not detector outcomes, the honest project stance is: use draft mode for quality; do not promise a Pangram pass; treat Pangram as a measure of *origin*, not *quality*.

**Caveat:** n=1, single short paragraph, one model's draft. Directionally strong (high confidence, prediction-matching) but not a study.

**Decisive next experiment (Open Q#2, now testable):** does real human revision move Pangram off 100%, and how much is needed? Take this paragraph → genuine human rewrite (or graded levels of edit distance) → re-test. If heavy revision still reads 100%, the premise collapses entirely; if a modest rewrite clears it, we've found the actual minimum.

**Variant A control (same day): heavy AI restructure also 100%.** A second AI rendering of the same argument — different structure, different phrasing, different rhythm ("Zero is not where forward guidance comes into its own...") — was also flagged 100% AI. Two maximally different AI surface realizations both max the detector. Confirms the signature is intrinsic to LLM generation, not surface form: re-generation is not a lever at all. The only untested lever is genuine human rewriting (Variant B, pending — must be produced by the human, not the model, or the experiment is void).

**Variant C control (same day): human prose, same topic → 100% Human Written.** Passage from Andrade, Gaballo, Mengus & Mojon (AEJ:Macro 2019), pp. 2–3 model-mechanism paragraphs — pre-ChatGPT, guaranteed human, topic-identical (forward guidance, ZLB, commitment), 329 words. Pangram v3.3.2: **100% human, full green**. Three readings:
1. **Pangram discriminates origin, not register.** Same genre, same topic, same technical vocabulary as the two AI variants — only the producer differs, and the verdict flips completely. The detector is not flagging "academic style"; it survives the strongest confound we could throw at it. As a domain-calibration check on econ prose, it passed (n=3, perfect separation).
2. **The ESL claim held.** Four non-native authors, visibly non-native phrasings ("contingent to any possible realization", "as signal of a longer trap") — cleared at 100% human. The Liang et al. ESL false-positive result (61% on TOEFL essays) does not reproduce on Pangram with fluent published ESL prose.
3. **Caveat:** published AEJ text may sit in Pangram's ~28M-doc human training corpus, so the "human" verdict may be partially memorization; and OCR'd text was checked clean before testing.

**Variant D (same day): the anti-slop panel winner also 100% AI.** The `ticl` co-winner from the blind cross-vendor harness experiment (see `2026-07-18_anti-slop-harness-panel.md`) — the draft all four judges rated slop-free, 216 words — was tested against the live tool. Predicted 100% AI before pasting; **Pangram v3.3.2: 100% AI, "fully AI-generated."** This closes the decoupling loop with the *best* register-quality draft available: panel-judged prose quality has zero measurable effect on origin detection. The AI-side optimization space (surface tells → full restructure → panel-optimized register) is now exhausted at n=3, all 100%.

**State of the contingency table:**
| Variant | Producer | Pangram |
|---|---|---|
| Original | AI, anti-tell draft | 100% AI, high conf |
| A | AI, heavy restructure | 100% AI |
| D | AI, panel-winning ticl draft (slop-free per 4 blind judges) | 100% AI |
| C | Humans, 2019, same topic, ESL | 100% Human |
| B | Human rewrite of AI draft | **untested — the load-bearing cell** |

The boundary between C and the three AI rows is precisely where the project lives. Everything now rides on B and its graded versions (light edit → deep rewrite): where between 0% and 100% human-edited does Pangram's needle actually move? Quota note: 0/4 free checks remaining as of the Variant D test — B waits for the daily reset.
