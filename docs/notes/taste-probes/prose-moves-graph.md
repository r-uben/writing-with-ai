# Prose-moves graph — real econ intros

**Purpose.** Calibrate the writing skill's *taste* against genuine human theory/empirical
prose, not against AI probes. Bipartite incidence graph:

- **Move-node** = a named rhetorical/structural move.
- **Paper-node** = a real mined intro.
- **Edge** = "paper exhibits move."

**How to read the graph.** A move's **degree** (how many papers wire to it) is the signal:

- **degree = N (all papers)** → a *general* prose law → safe to codify into taste.
- **degree ≥ 2** → shared across subfields → probably genre, not author.
- **degree = 1** → *candidate* idiosyncrasy — but with a small sample this may just mean
  "not enough papers mined yet." Degree-1 is a hypothesis, not a verdict.

**Sample so far (N=3).** Too small to trust degree-1 verdicts; trust the degree-3 laws.

| Paper | id | subfield |
|---|---|---|
| Morris & Shin 1998, *Unique Equilibrium…* (AER) | MS | theory macro (global games) |
| Fama & French 1997, *Industry Costs of Equity* (JFE) | FF | empirical asset pricing |
| Nakamura & Steinsson 2018, *High-Frequency Identification…* (QJE) | NS | empirical macro / identification |

## Incidence matrix

| Move | def (one line) | MS | FF | NS | degree |
|---|---|:--:|:--:|:--:|:--:|
| `incumbent→defect→our-fix` | set up the going approach, name what it can't do, position own contribution as the fix | ✓ | ✓ | ✓ | **3** |
| `thesis-in-first-sentence` | the actual finding lands in sentence 1 (abstract or intro), no runway | ✓ | ✓ | · | 2 |
| `enumerated-gaps` | objections/problems numbered — "First… Secondly…", "at least three problems" | ✓ | ✓ | · | 2 |
| `concrete-episode-as-evidence` | a real historical event grounds the abstract claim | ✓ | · | ✓ | 2 |
| `plain-mechanism-before-math` | the mechanism is stated in words before any formalism | ✓ | · | ✓ | 2 |
| `concede-then-claim` | abstract concedes the rival's premise, then asserts the result against it | ✓ | · | · | 1? |
| `big-question-opener` | intro opens on the field's big question, thesis withheld | · | · | ✓ | 1? |
| `named-models-as-landscape` | prior work enters as named models/citations, not episodes | · | ✓ | · | 1? |
| `concede-own-limitation-early` | the intro confesses the method's own weakness (e.g. low power) | · | · | ✓ | 1? |
| `rhetorical-question-pivot` | a direct question turns the intro | ✓ | · | · | 1? |

## Evidence locators (so claims are checkable)

- **`incumbent→defect→our-fix`** — MS ¶2–3 "merely pointing to the self-fulfilling nature of
  beliefs leaves open…"; FF ¶2 "CAPM is the common choice… Recent evidence suggests… As an
  alternative, Fama and French propose… But some argue…"; NS ¶2 "The most common approach…
  The worry with this approach… An alternative approach—the one we pursue…"
- **`thesis-in-first-sentence`** — MS abstract "Even though… we demonstrate the uniqueness";
  FF abstract "Estimates of the cost of equity for industries are imprecise." (NS withholds:
  opens on the big question instead.)
- **`enumerated-gaps`** — MS "First… Secondly…"; FF "There are at least three cost of capital
  problems. First…".
- **`concrete-episode-as-evidence`** — MS ERM + Mexican peso, "two years in Europe… a year in
  Mexico"; NS "September 2001… 9/11" as a VAR misread. (FF grounds in named models instead.)
- **`plain-mechanism-before-math`** — MS ¶1 belief loop in words; NS ¶3–4 identification logic
  in words ("all information public at the start of the 30-minute window is already
  incorporated").
- **`rhetorical-question-pivot`** — MS "Why did the attacks happen when they did?"
- **`concede-own-limitation-early`** — NS "this comes at the cost of reduced statistical
  power… shocks… standard deviation of only about 5 basis points."

## Emerging read (N=3, provisional)

- **The spine of an econ intro is `incumbent→defect→our-fix`** — degree 3, crosses all three
  subfields. This is the strongest candidate taste law.
- **`thesis-in-first-sentence` and `enumerated-gaps`** look like general habits (degree 2)
  that NS simply chose not to use — worth confirming against more papers.
- Everything at degree 1 is **unverified**. Need more nodes before calling any of them an
  author tic vs. a genre move.

## External review — 3-vendor brainstorm (2026-07-21, gpt-sol / grok-4.5 / kimi-k3)

**Triangulated fatal flaw (all three, independently): selection-on-success / no
counterfactual.** Every mined paper is a canonical top-5 artifact, so degree measures
*genre compliance* (what survives the editorial filter), NOT taste or quality. A botched
`incumbent→defect→our-fix` scores identically to Morris–Shin's. Degree is a base rate, not a
discriminating signal. **Fix before scaling N:** add negative/contrastive evidence.

**Second shared flaw: circular induction.** Moves were defined from the same N=3 that then
scores them — post-hoc labels fitted to the data. "Beautifully formalize a tautology" (kimi).

**Distinct high-value contributions:**
- **kimi-k3 — this is Swales' CARS model (1990).** `incumbent→defect→our-fix` ≈ CARS's
  establish-territory / establish-niche / occupy-niche. 35 yrs of genre analysis (Swales,
  Bhatia, Hyland) already built and validated this taxonomy *and* documented its failure
  modes (annotator drift, move cyclicity, discipline-dependence). Steal the codebook; spend
  effort where CARS is weak = **quality of execution**, which is where taste actually lives.
  Sharpest proxy for execution quality: **working-paper → published deltas** (referee-forced
  revision = taste under adversarial pressure).
- **grok-4.5 — don't make the graph the generative policy.** High-degree = the field's
  persuasion technology; codifying it industrializes legitimacy cues, colliding with the
  charter's "argumentative ownership." Use the graph as (A) a question-factory feeding
  forced-choice taste items and (B) a post-draft *critic*, never a drafting template. Prefer
  **anti-moves / constraints** over required moves ("don't open on a stock big question")
  — constraints generate variety, recipes collapse it. Author taste = the *residual* after
  projecting out degree-N genre.
- **gpt-sol — the real object is epistemic-structure → reader-belief-update, not prose.**
  Caught a live contradiction: `SKILL.md` categorically **bans big-question openers**, yet NS
  (a great paper) opens on one. Move = affordance with `use_when` / `avoid_when` /
  `reader_update` / `required_evidence` / `failure_mode`, never a sentence stem. Generate
  2–3 incompatible architectures per intro and pick by fit to the rhetorical state.

**Missing moves (union, deduped) worth adding as nodes:** `quantitative-result-preview`
(finding lands with a number), `stakes/so-what-with-units` (the "why care" obligation —
absent from all 10), `affiliative-lit-entry` (build-on vs defect-naming; our N=3 are all
insurgent field-redefiners → biased toward manufactured conflict), `objection-anticipation`
(reader-modeling; core of argumentative ownership), `identification-threat→design→residual`
(empirical spine ≠ theory incumbent→defect), `scope-fence`, `sentence-grain rhythm` +
`motif/ring-closure` (graph is paragraph-grain — blind to sentence-level taste and
whole-paper arcs).

**Revised next tests (consensus order):**
1. **Negative control first** — mine weak/desk-rejected/mid-venue intros; the signal is
   `degree(GOOD) − degree(CONTROL)`, not degree.
2. **WP→published pairs** of the same paper (NS has a public WP) — cheapest taste-under-
   pressure proxy.
3. **Codebook-first, freeze, hold out**; two coders from different model families (per the
   repo generation≠evaluation rule); per-move κ/AC1 gate. Expect `concede-then-claim` and
   `rhetorical-question-pivot` to fail.
4. Audit `SKILL.md` unconditional laws (big-question ban, mandatory pivot, roadmap) against
   the corpus **after** the control test — not before.

## Provisional move candidates (NOT coded into the graph — pending held-out validation)

Discovered by re-reading the existing N=3, so per kimi-k3 (2026-07-21) these are **codebook
definition, not degree evidence**: MS/FF/NS may not count toward these moves' degrees because
they generated them. Held for induction on a fuller dev set (≥6, incl. controls), then measure
only on held-out papers. Two of them are *execution-flavored* and cannot be coded without
contrast cases (you can't code "surprise" without non-surprise) — a second reason to wait.

- `quantitative-anchor` — a number that sizes the finding/problem. FF "std errors > 3.0%/yr";
  NS "std dev of only ~5 basis points."
- `stakes / so-what` — names what becomes *possible* / why care. MS "allows analysis of policy
  proposals"; NS information effects matter for the causal effect of policy.
- `objection-anticipation` — name and defuse the reader's objection. NS "this comes at the cost
  of reduced statistical power…"; MS concede-then-claim is a special case.
- `scope-fence` — affirmatively state what you can/can't identify. NS "precludes us from directly
  estimating… We can, however, measure…"
- `surprise-vs-standard-model` *(execution-flavored — needs contrast)* — NS forecasts move "the
  opposite of what standard models imply."

## Control-selection rule — PRE-REGISTER before looking (kimi-k3)

A "weak intro" picked by eye *after* reading will select controls that confirm the spine. Decide
the criterion first.

**LOCKED RULE (v1, 2026-07-21, author-approved incl. "target SSRN / working papers").** Control =
a **pre-referee version of the same paper**, not a paper judged weak by eye. Design, in priority:

1. **Within-paper WP→published pair** (strongest): a paper the library holds as BOTH a
   working-paper/NBER/Fed/SSRN version AND a published top-journal version. The WP intro is the
   control *by pre-referee status*; the delta is referee-forced revision, content held constant.
2. Selection is **status- and topic-based, blind to prose quality**: enumerate all such pairs by
   venue tag; keep those topic-matched to an anchor (MS theory / FF empirical-AP / NS
   empirical-macro); **verify the two intros actually differ** — if byte-identical (the NS
   failure), discard as *no-delta*, NOT as a control.
3. Fallback if too few pairs: WP-/SSRN-only papers topic-matched to an anchor, treated as
   non-top-5-polished controls, selected by topic proximity only.

**Candidate WP↔published pairs found (venue tags only):** hansen_mcmahon_prat FOMC transparency
(Fed'17 → QJE'18) · bauer_pflueger_sunderam perceptions of MP (WP → QJE'24) · caballero_simsek
opinionated markets (WP → AER/JF) · hansen_mcmahon shocking-language (WP'15 → JIE'16) · clayton et
al currency competition (SSRN ↔ WP; both preprint — weaker, but topic-matches MS). NS QJE↔WP is
**excluded** (byte-identical, no delta).

## FINDING — the WP→published delta proxy is empirically dead (this library) (2026-07-21)

Tested the LOCKED RULE's within-paper design on three topic-matched pairs. **All three intros are
publication-grade already at WP stage — no meaningful referee-forced revision:**

| Pair | WP vs published intro |
|---|---|
| Nakamura–Steinsson (WP ↔ QJE) | byte-identical |
| Bauer–Pflueger–Sunderam (WP ↔ QJE'24) | identical but for copy-edits ("In this paper"→"In this article", "time series"→"time-series") |
| Hansen–McMahon–Prat (Fed'17 ↔ QJE'18) | byte-identical opening sentence, verbatim |

**Interpretation.** The kimi/grok "referee-forced revision = taste under pressure" proxy assumes
pre-referee ⇒ weaker prose. For **elite authors at top-5**, that assumption is false: they write
publication-grade intros in the first public draft; refereeing changes results/robustness, not the
intro's rhetorical architecture. So this library's WP↔published pairs cannot supply a negative
control. Per the pre-registered rule (verify-differ-or-discard), all three are *no-delta discards*,
not controls. Three consecutive nulls = signal, not bad luck — stop mining pairs.

**Pivot options for the negative control (decide with author):**
- **(a) lower-tier human prose** — non-elite authors / lower venues. In-library candidates are
  mostly ESG/LLM-finance WPs (topic-mismatched to our theory/macro anchors); a clean match needs
  an *external* SSRN/job-market pull.
- **(b) the AI-probe drafts we already have** (`taste-probes/`) — tests the *human-vs-AI* axis, which
  is arguably the skill's real job and directly checks grok's claim that the degree-3 spine is
  "the modal econ ritual every competent AI performs." Free, local, and on-charter.

## Control filled — human-vs-AI axis (2026-07-21)

Coded grok's AI Morris–Shin probe (`taste-probes/2026-07-19_morris-shin-taste-probe.md`) against
the 10-move codebook, same content as human MS. **AI reproduces:** `incumbent→defect→our-fix`
(the degree-3 spine), `concrete-episode-as-evidence`, `plain-mechanism-before-math`,
`concede-then-claim` (borderline). **AI does NOT reproduce:** `enumerated-gaps` (compresses
"timing and policy" to a phrase, no First/Secondly), `rhetorical-question-pivot` (uses a flat
declarative "Timing is unexplained." instead of MS's "Why did the attacks happen when they did?"),
`thesis-in-first-sentence` (format artifact — probe rewrote the intro not the abstract).

**Result:** the degree-3 spine + degree-2 genre moves do **not** discriminate human from machine —
confirms grok-4.5's prediction empirically. The candidate discriminators are the two moves we were
tempted to dismiss as degree-1 noise (`enumerated-gaps`, `rhetorical-question-pivot`).

**Corroborated 3/3 (2026-07-21).** Coded all three AI variants (grok, gpt-sol, ollama-deepseek):
identical move set — all reproduce spine + concrete-episode + plain-mechanism + concede-then-claim,
all miss `enumerated-gaps` and `rhetorical-question-pivot`. The discriminator holds across three
model families. (Aside: gpt-sol put a formula `f(θ*)=e*−2t` in the intro; human MS kept the intro
verbal — a difference, but not a coded move.) Still one *concept* (Morris–Shin); test on FF/NS
content before generalizing.

**Direct skill implication (to confront):** gpt-sol flagged that `SKILL.md` *bans* the
big-question / rhetorical-question opener — yet the rhetorical-question pivot is one of the few
human-only moves in this probe. The skill may be banning a taste signal. Do not act until
corroborated + reconciled by a non-generating reviewer.

**Still open: the weak-human axis** (placeholder node in the graph). Needs an external SSRN /
lower-tier pull; deferred.

## Open moves (decide with author)

- Rename / split / merge move-nodes (esp. whether `concede-then-claim` and
  `thesis-in-first-sentence` should collapse).
- Which papers to mine next to break degree-1 ambiguity (add a 2nd theory paper to test
  `plain-mechanism-before-math` and `rhetorical-question-pivot`).
- Which degree-≥2 moves get promoted into the taste profile (Q3–Q5 / P3–P5).
