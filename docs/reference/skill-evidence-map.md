# Skill evidence map: what grounds the writing skill

**Status:** REVIEWED DRAFT. Written by Claude; independently audited 2026-07-22 by a
cross-vendor workflow (GPT + Kimi + Grok — see §4a), with over-claims downgraded per that
review. Per the charter (generation ≠ evaluation), no "candidate change" (§3) has been
applied to `skill/SKILL.md`, and the S8 change is explicitly deferred pending replication +
a non-generating reviewer. Nothing here has been written into the skill.

**Purpose.** Make the writing skill's design *defensible*: connect each rule / draft-mode
control to the empirical literature that justifies it, rate how strong that grounding is,
and — where the literature pushes back on a rule rather than endorsing it — say so. The
skill stays lean; the rationale lives here (`docs/reference/`), not in `SKILL.md`.

Citation keys refer to `docs/notes/literature/refs.bib`. Full annotations in
`docs/notes/literature/README.md`; OCR'd full text in `docs/notes/literature/ocr/`.

---

## 1. The through-line: human prose is *variable*, AI prose is *concentrated*

One finding recurs across every strand of the corpus, measured on different objects:

- **Content diversity** collapses under co-writing (`padmakumar-he-2024`).
- **Collective diversity** falls even as individual output improves (`doshi-hauser-2024`;
  `homogenizing-growthrate`, which supplies a *diversity growth-rate* metric).
- **Vocabulary** converges on a shared LLM register at population scale
  (`kobak-academic-2024`, `arxiv-shifts-2025`, `pubmed-medical-vocab`) and even in
  *speech* (`yakura-podcasts-2024`).
- **Structure** is more regular: character-network topology (`story-networks-2025`),
  discourse motifs (`threads-subtlety-2024`), dependency/constituent patterns
  (`munoz-ortiz-2024`), and semantic-association networks (`fluency-semantic-net-2024`)
  all show human text with *wider spread* and AI text *more concentrated*.

This is the skill's foundational premise, and it is well supported. A style profile that
rewards distinctiveness, burstiness, and specificity is not aesthetic preference — it is
pushing generated prose back toward the human distribution the corpus shows AI collapses.

**Direct consequences for the skill:** grounds **S2** (sentence-rhythm/burstiness),
**S16** (memorable/distinctive), the **excess-vocabulary ban** and **stock-register test**
in Draft Mode D3, and the whole rationale for having a taste profile at all.

---

## 2. Rule / control → evidence

Strength: **direct** (paper measures exactly this) · **supportive** (same mechanism,
adjacent object) · **suggestive** (consistent with, not tested).

| Skill element | What it asks | Grounding | Strength |
|---|---|---|---|
| **S2** sentence rhythm; **D3** burstiness | vary sentence length; variance at pivots | Human structural variability > AI across `munoz-ortiz-2024`, `threads-subtlety-2024`, `story-networks-2025` | ~~direct~~ → **unsupported** (§4a) |
| **S16** memorable / vivid specifics | distinctive, quotable, concrete | Homogenization = loss of distinctiveness (`padmakumar-he-2024`, `doshi-hauser-2024`) | supportive · scope-limited (§4a) |
| **D3 excess-vocabulary ban** | avoid *delve/underscore/…* register | `kobak-academic-2024` measures exactly this excess set; corroborated `arxiv-shifts-2025`, `pubmed-medical-vocab` | direct (measured words only) |
| **D3** "treat as register, not a fixed blocklist" | words date as models are steered off them | Population vocab *shifts over time* (`kobak-academic-2024`, `arxiv-shifts-2025`) — durable signal is register uniformity, not a word list | ~~direct~~ → **supportive** (§4a) |
| **S17** jargon discipline; **D3** stock-register test | plainest precise word; cut stock phrases | Register uniformity as the tell (`kobak-academic-2024`; review `mdpi-prisma-2026`) | ~~supportive~~ → **suggestive** (§4a) |
| **D1/D2** human supplies & owns the argument; **S12** author voice | skill never invents the thesis; human steers via outline | Opinionated assistants shift the *writer's own* views, often unnoticed (`jakesch-2023`, direct); *safeguards don't prevent it* (`williams-ceci-2026`, **unverified** — §4a) | direct (on Jakesch) |
| **D6** independent judge; **D5** verify-before-use; **D4** self-critique | drafting model never sole reviewer; accountability pass | Cognitive debt / reduced ownership under AI assistance (`kosmyna-2025`; read with critique `stankovic-2026`) | ~~supportive~~ → **suggestive** (§4a) |
| **S6/S7** quantitative anchoring; explicit uncertainty | numbers on claims; own the limits | Anti-homogenization (specific > generic) + ownership (`padmakumar-he-2024`, `kosmyna-2025`) | suggestive |
| **S13/S8** dialectical structure; question-driven openings | pose tension; frame the question | See **§4 tension** — partly *counter*-indicated by homogenization | mixed |

---

## 3. Candidate refinements mined from the literature

Proposals for `SKILL.md`, **not applied** — each needs the independent-reviewer gate.

1. **Name the persuasion risk as a first-class draft-mode control.** The skill enforces
   human argument-ownership operationally (D1/D2) but never states *why*. `williams-ceci-2026`
   shows disclosure/awareness does **not** neutralize the effect — which is the actual
   argument for structural separation (human owns the thesis) over a mere "AI-assisted"
   disclaimer. Candidate: one line in Draft Mode citing the mechanism, and a check that the
   *stance* in the draft traces to the human's outline, not the model's completion.

2. **Reframe the anti-tell controls as quality, backed by measurement.** `SKILL.md` says
   the anti-tells "are the same failure modes these rules forbid." The stylometry/graph
   corpus (`mdpi-prisma-2026`, `threads-subtlety-2024`, `munoz-ortiz-2024`) supports the
   stronger claim: the markers are *genuine structural differences*, not detector artifacts.
   This matters for the charter — it legitimizes optimizing against them as a *quality*
   goal, not detector-gaming. Candidate: a sentence to that effect (rationale here, not in
   the skill).

3. **Bias/equity is an unhandled gap.** `gender-bias-2023` shows AI writing assistance
   propagates downstream gender bias in an educational setting. The skill has no equity
   check. Candidate: either a new review-mode flag, or an explicit *non-goal* stating bias
   auditing is out of scope (so the omission is a decision, not an oversight).

---

## 4. Where the literature *challenges* a rule (the useful part)

**S8 "question-driven openings" vs the homogenization result.** The tension is real but
*narrower* than first stated (correction from the §4a review — the earlier draft mis-stated
the rule):

- **Correction:** `SKILL.md` does **not** categorically ban rhetorical questions. Draft-Mode
  P4/D4(f) ban only the *stock stem* — "Never stock 'A central question in [field] is…'" —
  and explicitly **allow** "a real setup / section-frame question." The "bans the
  rhetorical-question opener" framing was inherited from `STATUS.md` and is inaccurate to the
  rule text. The stock-stem ban is *not* in tension with homogenization — it forbids one
  lexical cliché (Swales Move-1 territory-claiming), which the anti-homogenization goal
  supports.
- **The real tension is S8's *mandate*.** S8 tells every section opening to "pose the
  question the section answers." That mandates the single most genre-central frame — pushing
  prose toward the homogenized centre the corpus shows AI already occupies
  (`story-networks-2025`: AI reproduces the spine, misses the tail; project taste-graph: 3/3
  AI drafts hit the spine, miss `rhetorical-question-pivot` and `enumerated-gaps`). A
  question-*raised niche* (Swales Move-2, e.g. Morris-Shin's "Why did the attacks happen when
  they did?") is a legitimate human-distinctive move a rigid "pose the question" rule can
  flatten.
- **Direction (deferred — not a unilateral edit):** rewrite S8 from a mandate into a
  variety-preserving rule — require openings to establish the section's controlling
  problem/claim by *whatever* move fits (concrete fact per P4, direct conclusion, tension per
  S13, or a genuine setup question), and flag sections that open on the same move repeatedly.
  Keep the stock-stem ban. Do **not** add a categorical rhetorical-question ban.

**The anti-tell / anti-detector boundary.** Grounding S2/S16/excess-vocab in *quality*
literature (not detector evasion) is what keeps the skill on the right side of the charter.
If future edits start justifying these rules by "passes detector X," that is the drift the
charter warns about — this map should be the counter-reference.

---

## 4a. Independent cross-vendor review (2026-07-22)

This map was audited by a cross-vendor workflow (GPT-5.6 terra/sol, Kimi K3, Grok) — no
Claude agent judged Claude's map (run `wf_e8c92463-502`). Each grounding claim was checked
against the OCR source by a non-Claude model instructed to *refute*. Corrections applied
above:

- **S2-burstiness → unsupported.** Cited sources weren't yet OCR'd, and a structural
  human/AI *difference* does not establish that varying sentence length *improves* prose
  (difference ≠ intervention efficacy). The rule may still be good practice; it is not
  grounded by this corpus.
- **D3-register-not-blocklist → supportive.** Kobak holds the marker set *fixed* across
  subcorpora; the year-to-year turnover shown is Covid content-words vs 2024 style-words, not
  proof the LLM-marker set itself expires. "Register not blocklist" is a defensible inference,
  not a measured result.
- **S17-stock-register → suggestive.** Kobak is corpus-level ("cannot identify individual
  abstracts"); it can't validate an individual-level stock-register test. `mdpi-prisma-2026`
  was unread.
- **independent-judge → suggestive.** Kosmyna is an adjacent cognitive-debt mechanism; it
  does not test drafting/review separation or verify-before-use, and `stankovic-2026` cautions
  the performance-harm evidence is weak.
- **S16-memorable (held, scope-limited).** Doshi-Hauser's diversity loss is *collective* —
  individual novelty rose +8.1%; Padmakumar's homogenization is InstructGPT/RLHF-specific and
  absent for base GPT-3. Grounds "distinctiveness matters across writers," not "AI makes any
  single text less vivid."
- **ownership-persuasion (Jakesch direct; safeguards clause unverified).** Jakesch directly
  measures unnoticed opinion shift (N=1506, d≈0.19–0.22). The "safeguards don't prevent it"
  claim rests on `williams-ceci-2026`, which was unread — do not lean on it until verified.

**S8 verdict:** partial/real tension (2 of 3 lenses), one skeptic dissent that it's an N=1
pilot not worth acting on. Consensus: fix the map (done); **defer any `SKILL.md` change**
until the rhetorical-question-pivot is replicated on Fama-French / Nakamura-Steinsson content
and a non-generating reviewer signs off (matches the `STATUS.md` freeze-first protocol).

---

## 5. What this map does *not* claim

- It does not establish that following the rules *causes* better writing — the corpus shows
  AI/human *differences* and diversity *costs*, not that this specific rule set closes them.
  The rules are a defensible response to the evidence, not a validated treatment.
- Five grounding papers (`homogenizing-growthrate`, `williams-ceci-2026`,
  `threads-subtlety-2024`, `munoz-ortiz-2024`, `story-networks-2025`) were still being OCR'd
  when this was written; claims about them are at the finding level (verified abstracts/first
  pages), and any verbatim quote pulled into `SKILL.md` should be checked against the OCR.
- `kobak-academic-2024` and `kobak-biomed-2025` are the **same paper** (preprint + published);
  do not cite both as independent corroboration.
