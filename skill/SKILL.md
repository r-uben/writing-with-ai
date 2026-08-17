---
name: writing
description: Draft or review prose destined for an academic paper, against a codified 20-rule style profile plus the CJ register tick. Review mode: Claude takes the argument lens, Antigravity/Gemini the register lens, output synthesizes concrete rewrites. Draft mode (--draft) turns a human-supplied idea or outline into near-final academic prose, self-critiques, and hands off to an independent judge. Use when the destination is a journal, working paper, or dissertation chapter — including a .md concept note being drafted toward one. For prose destined anywhere else (README, blog, Slack, docs, email), use no-ai-slop instead.
---

# Writing

Two modes over one academic style profile.

- **Review mode** (default): critique existing prose. Claude reviews on the argument lens; Antigravity/Gemini reviews on the register lens via `agy`; output synthesizes both into concrete rewrites.
- **Draft mode** (`--draft`): turn a human-supplied idea or outline into near-final academic prose. The human owns the argument and vouches for the facts; the skill drafts, self-critiques against the 20 rules, CJ, and P1–P5 taste, then hands the result to an independent judge (never the drafting model alone).

The rules serve both modes: in review they are the critique checklist; in draft they are generation-time constraints.

## Scope — which skill

**The test is destination, not file extension.** Where do these words get published, and who reads them there?

| Destination | Skill |
|---|---|
| Journal, working paper, dissertation chapter, referee report | **`writing`** (this one) |
| A `.md` or `.txt` concept note being drafted *toward* one of the above | **`writing`** |
| README, blog post, Slack, docs, email, changelog, landing copy | **`no-ai-slop`** |

Extension does not decide this. A `.md` concept note headed for Section 3 belongs here; a `.tex` file of lecture handouts for undergraduates probably does not.

Destination is **not subject matter**. A blog post about monetary policy is still general prose — a blog reader is not a referee.

**If the destination is genuinely unclear, ask once, in one line:** "Headed for a paper, or somewhere else?" Then proceed. Do not guess silently — the two skills give opposite verdicts on the same sentence (a scope fence like "Identification improves; power does not." is required here and cut there).

`--venue` or `--academic` skips the question. Never run both skills over the same passage.

## Style Profile

Apply these rules when reviewing. Each issue MUST reference its rule ID.

| ID | Rule | Directive |
|----|------|-----------|
| S1 | Precision opening | Open with precision — no throat-clearing. First sentence of every paragraph should carry weight. Cut "It is well known that...", "In recent years...", "There is a growing body of literature...". See **Opening moves** below — not every question is the same move. |
| S2 | Sentence rhythm | Vary sentence length with purpose. Short sentences for impact, long for nuance. Flag monotonous runs of same-length sentences. |
| S3 | Voice balance | Active voice ~80%, passive only for depersonalization ("the model is estimated" not "we estimated the model" when the agent is irrelevant). Flag gratuitous passive. |
| S4 | No filler | No filler phrases. Cut "it is important to note that", "it should be mentioned that", "in order to", "the fact that", "it is worth noting". |
| S5 | Conclusion first | Lead with the conclusion, not the buildup. No buried ledes. The reader should know the point before the evidence. |
| S6 | Quantitative anchoring | Anchor claims to numbers. "Large effect" → "a 12pp increase". Flag vague quantifiers without numerical backup. |
| S7 | Explicit uncertainty | Label gaps and limitations directly. "We cannot identify X because Y" not "future research might explore X". Own the limitation. |
| S8 | Question-driven openings | Section and subsection openings should pose the question the section answers. Frame the reader's expectation. See **Opening moves** — this is the *encouraged* move, distinct from stock big-Q. |
| S9 | Parallel construction | Lists, enumerations, and comparisons must use parallel grammatical structure. Flag broken parallelism. |
| S10 | Confident, not arrogant | State findings directly. "The results show X" not "we believe the results might suggest X". Never explicitly claim novelty using self-evaluating words like *novel*, *unprecedented*, or *sheds new light*. Let the defect and the fix speak for themselves. |
| S11 | No apologetic framing | No "we merely", "this is only a first step", "we do not claim to". State scope and move on. |
| S12 | Author voice | "I" for solo-authored papers, "we" for co-authored. Never "the authors", "the present study", "this paper argues". Determine from context (single author → "I"; multiple → "we"). |
| S13 | Dialectical structure | Hypothesis → counter → synthesis. Present the tension, then resolve it. Flag sections that argue only one side. Requires a *real* rival claim — see **CJ** for the empty imitation. |
| S14 | Substantive signposting only | Weld every transition to a substantive claim. Never use empty predictive scaffolding ("The remainder of this section..."). "If X holds, Y should fall. Section 3 tests this by..." is good. |
| S15 | AER prose flow | No bullet points, no numbered lists in prose. AER style: flowing paragraphs with logical connectives. If information is enumerated, weave it into sentences ("First, ... Second, ... Finally, ..."). Tables are acceptable for data, never for arguments. |
| S16 | Memorable writing | Vivid specifics over abstractions ("the 2008 Lehman collapse" not "a financial crisis"). At least one striking, quotable formulation per section — and it must compress the argument's *mechanism*, not decorate it. Open and close sections with your strongest sentences. |
| S17 | Jargon discipline | Use the plainest word that carries the same precision. "Reverse causality" over "endogeneity" when both work. Technical terms earn their place only when no plain alternative exists. |
| S18 | Citation integration | Prefer narrative citations (`\citet`, `\textcite`) that weave into prose: "\citet{autor2003} shows..." over parenthetical dumps. Flag runs of 3+ stacked `\citep`/`\parencite` — break them up or integrate the most important ones narratively. |
| S19 | One idea per paragraph | Each paragraph makes one clear point. Flag paragraphs that drift across multiple topics. The first sentence should signal what the paragraph is about. |
| S20 | Reference consistency | Use `\eqref` for equations (never bare `\ref`). Use consistent naming for formal results: always "Proposition~\ref{prop:X}" not sometimes "Prop." sometimes "Proposition" sometimes a bare number. Same for Lemma, Theorem, Corollary. |

## Register tick: CJ — corrective juxtaposition

Empty contrast scaffolds that sound dialectical but add no substance. **Not** the same as S13.

| | |
|--|--|
| **CJ (flag)** | "Not X, but rather Y" / "Rather than merely A, we B" where X was never a live rival claim — pure throat-clear contrast. |
| **S13 (keep)** | A real counterargument or identification threat is stated, then resolved with evidence or a scope limit. |
| **Bad (CJ)** | "Rather than simply estimating average effects, we examine heterogeneity." (nobody offered "simply averages" as the paper's foil) |
| **Good (S13)** | "A natural concern is reverse causality from prices to policy. We address this with high-frequency surprises around FOMC announcements, which…" |

Cite **CJ** in the Rule column when flagging the empty scaffold; cite **S13** when the dialectic is missing or one-sided for a *real* tension.

The test is whether the X-side is a live rival: an attributed claim, a stated hypothesis, a plausible identification threat, or an evidenced alternative. If nothing in the literature or the data ever proposed X, the contrast is scaffolding. S13 never requires the literal "not X but Y" wording.

## Decorrelated review lenses (default)

By default the two reviewers do **not** share the same checklist (correlated hits waste a second model). Escape: `--full-profile` restores S1–S20 (+ CJ) for both.

| Reviewer | Lens | Primary IDs |
|----------|------|-------------|
| **Claude** | **Argument** — claims, structure, openings, dialectic, evidence altitude | S1 (openings / stock big-Q), S5, S6, S7, S8, S10, S11, S13, S14, S18, S19 + opening-moves split |
| **Gemini** | **Register** — voice, rhythm, filler, jargon, AER surface, CJ tick | S2, S3, S4, S9, S12, S15, S16, S17, S20, **CJ** |

User-specified `S\d+` subsets still override: both reviewers get only those IDs (plus CJ if register-relevant and not excluded). `--full-profile` ignores the lens split.

## Opening moves (three laws — do not conflate)

There is **no** unconditional ban on opening with a question. Distinguish three moves:

### 1. Stock big-question throat-clear — flag / ban

| | |
|--|--|
| **use_when** | Almost never in published AER-style prose as the paper's first move. |
| **avoid_when** | Always, when the question is a generic field template with no immediate turn into *this* paper's object. |
| **Bad** | "A central question in macroeconomics is how monetary policy affects asset prices." |
| **Good** | Open on a dated, quantified fact, then the claim (Gürkaynak–Sack–Swanson-style): "On [date], the FOMC surprised markets by X bp; we show…" |

### 2. Rhetorical-question pivot — provisional taste (not auto-ban)

| | |
|--|--|
| **use_when** | The question is the setup for an immediate, owned answer that *is* the mechanism (human probe signal on Morris–Shin). Mark as provisional taste until corroborating probes (W2). |
| **avoid_when** | The question hangs without a turn; or it is interchangeable with stock big-Q above. |
| **Good** | A tight interrogative that the next sentence resolves into the paper's distinctive claim. |
| **Bad** | "Why does this matter?" followed by vague importance claims. |

### 3. S8 section-frame question — encourage

| | |
|--|--|
| **use_when** | Section / subsection openings that pose the question *this section* answers. |
| **avoid_when** | Using a stock field big-Q as if it were S8; burying the section's job. |
| **Good** | "Does the credit channel survive when banks can securitize? This section estimates…" |
| **Bad** | Section opens with throat-clear or with the answer buried after a page of setup. |

When citing issues, use **S8** for section-frame failures; for stock big-Q or failed pivots, cite **S1** (precision opening) and name the move (stock big-Q / pivot) in the Issue column.

## Input Parsing

The user invokes `/writing` with arguments in any order:

```
/writing path/to/file.tex                 # Review a file (default: decorrelated lenses)
/writing path/to/file.tex S1 S5 S6        # Review with rule subset only (both reviewers)
/writing path/to/file.tex --no-gemini     # Claude-only review
/writing path/to/file.tex --full-profile  # Both reviewers get full S1–S20 + CJ
/writing path/to/file.tex --force         # Skip soft structure gate
/writing path/to/file.tex --apply-agreed  # After review, offer to apply Agreed majors only
/writing --no-gemini S3 S12 file.tex      # Flags and rules in any order
/writing --draft concept.md               # Draft mode: idea/outline → prose
/writing --draft --section intro --words 400 "core claim + evidence"
```

**Parse rules:**
1. **`--draft`**: switch to Draft Mode (below). Everything after is the concept — a file path (idea/outline) or inline text stating the argument.
2. **File path**: any argument containing `/` or ending in `.tex`/`.md`/`.txt` → treat as a file path. Extension does **not** decide scope — see **Scope**.
3. **Rule subset**: arguments matching `S\d+` (e.g., `S1`, `S12`) → filter to those rules only (both reviewers).
4. **`--no-gemini`**: skip the independent second opinion (Claude-only). Discouraged in draft mode — see the charter note in Draft Mode.
5. **`--full-profile`**: both reviewers use the full style profile + CJ (no argument/register split).
6. **`--force`**: skip the soft structure gate (Step 1b).
7. **`--apply-agreed`**: after the review tables, enter the optional apply flow (Step 5) — still never auto-edits without a yes.
8. **Draft options**: `--section <name>`, `--words <N>`, `--venue <AER|generic|...>` tune draft-mode output. `--venue` or `--academic` also confirms scope without asking.
9. **Pasted text**: with no `--draft` and no file path, treat remaining text as inline prose to review.

If no arguments are given, ask whether the user wants to draft (and for what concept) or review (and for which file).

## Draft Mode

Triggered by `--draft`. Turns a human-supplied idea into near-final academic prose. The human supplies and owns the argument; the skill never invents the thesis, and never invents facts, numbers, or citations (see Step D5).

### Step D1: Parse the concept

Read the concept (file or inline). Extract: the central claim/argument, any sub-claims, supplied evidence or citations, and constraints (`--section`, `--words`, `--venue`). If the concept is only a topic with no argument, STOP and ask the human for the actual claim — drafting without an argument produces exactly the hollow, ownerless prose this skill exists to avoid.

### Step D2: Plan (claim outline)

Expand the concept into a one-line-per-paragraph outline where each line states *the point that paragraph makes* (not its topic). Present the outline to the human for a quick confirmation or reorder. This is where the human steers the argument — by shaping the outline, not by editing finished prose.

**Non-interactive / automation:** if the user already said "just draft it", passed `--yes`, or the invocation is headless with no human in the loop, treat the outline as auto-confirmed after showing it once in the output (do not deadlock waiting for a reply). Otherwise do not draft until the outline is confirmed.

### Step D3: Draft with the register as a generation constraint

Draft prose from the confirmed outline in a strong academic register (`--venue` default: generic strong-academic; `AER` → flowing-prose economics style). Apply these at **generation time**, not as an afterthought:

- **S2 / burstiness**: deliberately vary sentence length. No runs of same-length sentences; place at least one very short declarative sentence at an argumentative pivot ("It tightens."). Variance follows from that move; don't chase a numeric target.
- **Register, not a blocklist**: the durable tell is a flat, uniformly-flowery register — write plainly and variably instead. Do **not** maintain a static banned-word list: the 2026-07-18 panel measured hit-counts of zero on real drafts, and such lists date as models are steered off them. Judge the phrase in its sentence. Inflated register (*delve*, *tapestry*, *pivotal*, *underscore*) is cut when a plainer precise word exists — because it is imprecise, not because it is on a list.
- **Stock-register test**: stock academic phrases are slop even when off any list ("do the heavy lifting", "in the classic sense", "the standard prescription"). If a phrase could appear unchanged in a hundred other papers, replace it.
- **Argument-carried transitions**: the logic of adjacent sentences carries the turn; do not scaffold with *therefore/thus/yet/hence* where the content already turns. Formal-connector overuse (*furthermore, moreover, additionally, notably, importantly*) is the same failure.
- **CJ at generation time**: do not manufacture a foil. If you write "not X but Y", X must be a live rival claim.
- **Noun-driven over adjective-driven**: strip non-quantitative adjectives and adverbs. If an effect is "large", state the mechanism or the exact number. Strong academic writing relies on precise nouns and active verbs.
- **S4/S5/S10/S11/S16**: no filler, conclusion-first, confident not arrogant. Ban apologetic wool on ordinary claims (**P2**), including *to our knowledge*, *as far as we know*, *to the best of our knowledge*, *as far as we are aware*, and soft *at least* ("we can at least say…"). Rewrite as a flat claim or a named P3 limit. Do **not** ban quantitative lower bounds ("standard errors of at least 3%"). **P3 exception:** when stating a *genuine* identification or scope limit the human flagged, prefer explicit caution that names what cannot be delivered — not punchy telegraphic denial ("The size is not.") as the default. Do not use limit-caution as cover for soft claims elsewhere. The memorable formulation must compress the argument's mechanism itself — decorative symmetry that could caption any argument gets cut. First-person: follow S12 from authorship context (solo → "I"; coauthored → "we"), not a baked-in solo assumption.
- **The Scope Fence (Limitations)**: when conceding a limitation or lack of power, define the exact border of what is still valid using a strict contrast ("Cannot X; Can Y"). Never spiral into an apologetic hedge. "Identification improves; power does not."
- **S6/S7**: anchor claims to the human-supplied numbers; label uncertainty the human flagged (P3 voice for real limits). Never fabricate a figure to satisfy S6 — if a claim needs a number the human did not supply, insert `[VERIFY: description]` **inline in the prose** at that point (do not invent a plausible value). Placeholders flow into D5 automatically.
- **Author taste P4 (openings):** if a dated/named/quantified fact is in the concept, prefer opening on it; a real setup / section-frame question is OK when it states this draft's job. Never stock "A central question in [field] is…". See **Opening moves** for the three-way split.
- **Author taste P5 (citations):** narrative `\citet` when the source does sentence-level work; parenthetical clusters OK for ancillary or well-established stacks — pick by context, don't force one mode.

**Exemplar levers (positive contrast, distilled from rated field prose — full ratings in `docs/notes/2026-07-18_prose-exemplar-ratings.md`).** Condition on the *move*, never imitate a passage (naive imitation ranked 4th of 7 on slop):

- **Mechanism as a plain declarative, then justify.** State the causal claim bare, then earn it with a number or a concrete instance. Good: "The Fed never rolls dice; every move is a response to something" (Cochrane). Not: "Markets understand the incentive structure and price the announcement accordingly" — abstract summary that states nothing.
- **Compress the hard idea to an aphorism that *is* the mechanism.** Good: "everyone may know that the fundamentals are sound, but it may not be that everyone knows that everyone knows this" (Morris & Shin). Not a decorative chiasmus that could caption any argument.
- **Openings (P4):** prefer a supplied concrete fact when available; allow a real setup question that frames this section's job; never stock big-Q throat-clear. Rhetorical-question pivot remains provisional taste (W2).
- **Weld the number into the claim sentence.** Good: "the multiplier is 1.4 at 8 quarters and 1.1 at 16" (Ramey). Not: "the effect is large and persistent."
- **Instantiate before generalizing.** Run one concrete scenario through the mechanism ("Concretely, suppose…", Caballero & Simsek) before stating the general result.

### Step D4: Self-critique + one revision (TICL-style)

Critique the draft against the 20 rules, CJ, and author taste **P1–P5** (`docs/notes/taste-profile.md`). For each weak passage, name *what* it drifts toward and *why*, then rewrite once. Targeted passes:

(a) **stock-register hunt**; (b) **connector strip**; (c) **memorable-line test** — does it compress the mechanism, or could it caption any argument?; (d) **declarative-then-justify**; (e) **limit voice (P3)** — genuine limits stated with clear caution naming the missing object, not punchy denial-by-default and not wool on non-limits; (f) **opening (P4)** — cut stock big-Q; keep concrete fact or real setup as context demands; (g) **citation work (P5)** — for each cluster, either each source earns a clause or the stack is honestly ancillary; (h) **epistemic-hedge hunt (P2)** — cut *to our knowledge* / *as far as we know* / *to the best of our knowledge* / *as far as we are aware* / soft *at least*; keep quantitative lower bounds; (i) **novelty-claim strip** — cut *novel*, *unprecedented*, etc.; (j) **scope fence check** — ensure conceded limits end in a strict "Cannot X; Can Y" contrast; (k) **CJ pass** — every "not X but Y" has a live rival on the X-side, or it goes.

Not a substitute for independent review (Step D6).

### Step D5: Verify-before-use list

Extract every factual claim, quantity, date, and citation in the draft into a checklist for the human to confirm. This is the accountability pass — one review, not heavy editing. Flag explicitly any place the draft needed a fact the human did not supply. Nothing in this list may be an invented value. Any `NEEDS SOURCE` item must correspond to a `[VERIFY: …]` placeholder still in the draft body — confirmation of the list alone is not permission to use unverified prose; the human must supply the value or delete the claim.

### Step D6: Independent evaluation (required, and final)

The drafting model must not be the sole reviewer of its own draft (project charter).

1. **Materialize the draft** to a temp `.tex` or `.md` file under the project (or `/tmp`) so `agy` can use `@FILE_PATH` — D3/D4 output in the chat buffer alone is not enough.
2. Hand that file to an independent judge — reuse the Antigravity/Gemini path (Review Mode, Step 3) against the style profile. Optionally run deterministic linguistic metrics first.
3. `--no-gemini` disables this; warn that draft mode then has no independent check. If `agy` fails, say so and do not pretend D6 passed.

**D6 is the last step. There is no D7.** Do not hand academic prose to `no-ai-slop` afterwards — its general-register rules cut the scope fence, the pivot fragment, and the S16 mechanism line, all of which are required here. The two skills are exclusive by destination.

### Draft Mode output

```
## Draft: [section / concept]

### Outline (confirmed)
1. [paragraph point] ...

### Draft
[near-final prose]

### Verify before use
- [ ] [claim / number / citation to confirm] — [source or "NEEDS SOURCE"]

### Independent review
[judge's issues + rewrites, or "skipped (--no-gemini) — no independent check"]
```

## Review Mode Execution

### Step 1: Read the source

Read the target file. If it contains `\input{}` or `\include{}` directives for prose sections, follow those chains and read the included files too. Concatenate into a single prose body.

**Focus on prose only.** Skip:
- Preamble (`\documentclass` through `\begin{document}`)
- Math environments (`equation`, `align`, `gather`, etc.)
- Tables (`tabular`, `table`)
- Figure environments (`figure`)
- Bibliography entries
- Comments (`%`)
- Pure formatting commands (`\label`, `\ref`, `\cite` — keep surrounding prose)

### Step 1b: Soft structure gate (ask once)

Deep prose review on unfixed argument structure wastes budget. **Unless `--force`:** after the read, do a one-pass structural skim (section order vs claims, missing ID of the paper's job, obvious buried lede at document scale). If structure looks broken enough that sentence-level polish would be premature:

1. Say so in 2–4 bullets.
2. Ask once: continue with style review anyway, or stop and fix structure first?
3. Wait for the answer; do not start Step 2 until they choose.

`--force` skips this gate. This is a **soft ask**, not a paper-graph dependency — do not require `paper-graph` outputs or refuse to review without a graph.

### Step 2: Claude Review

**Default lens = argument** (see Decorrelated review lenses). Apply only the argument-lens IDs, unless the user passed a rule subset or `--full-profile`.

**Abstract check**: If the file contains an abstract (`\begin{abstract}` ... `\end{abstract}`), count its words. If it exceeds 100 words, flag it separately at the top of the output with the current word count and a concrete cut-down rewrite.

**Constraints:**
- Identify the 10-15 most impactful issues. Not exhaustive — prioritize what matters most.
- Every issue MUST include a concrete rewrite. Never say "consider rephrasing" or "this could be improved." Write the actual replacement text.
- Rewrites MUST preserve meaning and produce valid LaTeX.
- Style only — no grammar, spelling, or punctuation corrections.
- Assign severity: `major` (undermines clarity/argument) or `minor` (polish).
- Reference location by line content or paragraph, not line numbers (LaTeX line numbers shift).
- Also note 2-3 specific strengths — passages that exemplify good style.

Record Claude's issues internally for synthesis in Step 4.

### Step 3: Antigravity/Gemini Review (parallel)

**Skip this step if `--no-gemini` was specified.**

Fire an Antigravity query in parallel using the Bash tool. Use `agy -p` for non-interactive review and `@` file references so Antigravity reads the file directly. Do not call the legacy `gemini` CLI from this skill.

**Default: send the register-lens IDs only** (S2, S3, S4, S9, S12, S15, S16, S17, S20, CJ). With `--full-profile`, send S1–S20 + CJ. With a user rule subset, send that subset.

```bash
agy -p "$(cat <<'PROMPT'
You are reviewing academic prose for style. Apply ONLY these rules:

S2: Vary sentence length with purpose
S3: Active voice ~80%, passive only for depersonalization
S4: No filler phrases ("it is important to note", "in order to", etc.)
S9: Parallel construction in lists and comparisons
S12: "I" for solo-authored, "we" for co-authored. Never "the authors" or "this paper argues"
S15: No bullet points or numbered lists. AER flowing prose style
S16: Memorable writing — a striking formulation that compresses the MECHANISM, not decoration
S17: Jargon discipline — plainest word that carries the same precision
S20: Reference consistency — \eqref for equations, consistent naming for Proposition/Lemma/Theorem
CJ: Corrective juxtaposition — flag "not X, but rather Y" / "rather than merely A, we B" where X
    was never a live rival claim (no attributed claim, stated hypothesis, identification threat,
    or evidenced alternative). Do NOT flag a real counterargument that the text then resolves.

INSTRUCTIONS:
- Identify the 10-15 most impactful STYLE issues (not grammar/spelling).
- For each issue, provide: the original passage, the rule ID, severity (major/minor), and a CONCRETE REWRITE (not "consider rephrasing" — write the actual replacement).
- Also note 2-3 specific strengths.
- Respond in this exact format:

STRENGTHS:
1. [passage quote] — [why it works]

ISSUES:
1. PASSAGE: [original text]
   RULE: [S# or CJ]
   SEVERITY: [major/minor]
   REWRITE: [concrete replacement]

STRUCTURAL NOTES:
[Any observations about paragraph ordering, argument flow, signposting]

Review @FILE_PATH.
PROMPT
)" --add-dir "$(dirname FILE_PATH)"
```

Replace `FILE_PATH` with the actual file path, and replace `$(dirname FILE_PATH)` with the containing directory. If the current working directory already contains the file, `--add-dir` can be omitted.

**Timeout**: If Antigravity takes longer than 120 seconds or fails, proceed Claude-only and note this in the output. For long reviews, pass `--print-timeout 10m` or run the command in the background.

### Step 4: Synthesize

Match issues from Claude and Antigravity by location overlap (same passage or adjacent sentences about the same problem).

Classify each issue:
- **Agreed**: Both Claude and Antigravity flagged the same passage/problem (highest confidence)
- **Claude Only**: Only Claude flagged it
- **Antigravity Only**: Only Antigravity flagged it

Under the default decorrelated lenses, "Agreed" is rarer by construction — the reviewers are looking at different things. That is the point, not a failure. Do not widen the lenses to manufacture agreement; use `--full-profile` if the user actually wants both checklists.

For agreed issues, prefer Claude's rewrite unless Antigravity's is clearly better.

For strengths, note which reviewer(s) highlighted each one.

### Output Format

Present the final review in this structure:

```
## Writing Review: [filename]

### Abstract
> [word count] words (limit: 100). [PASS / OVER BY N WORDS]
> If over, provide a concrete ≤100-word rewrite here.

(Omit this section if the file contains no abstract.)

### Strengths
[passage reference] — [why it works] (Claude / Antigravity / Both)

### Issues

#### Agreed (both flagged)
| # | Location | Rule | Issue | Severity | Rewrite |
|---|----------|------|-------|----------|---------|
| 1 | "original passage..." | S4 | Filler phrase adds no content | major | "rewritten passage..." |
| 2 | "Rather than simply…" | CJ | Empty corrective juxtaposition | minor | "We examine heterogeneity across…" |

#### Claude Only
| # | Location | Rule | Issue | Severity | Rewrite |
|---|----------|------|-------|----------|---------|

#### Antigravity Only
| # | Location | Rule | Issue | Severity | Rewrite |
|---|----------|------|-------|----------|---------|

### Structural Notes
[Paragraph ordering, argument flow, signpost observations from both reviewers]

### Summary
Issues: N major, N minor. Lenses: Claude (argument) + Antigravity/Gemini (register) — or full-profile / Claude only if flags say so. Top priority: [single most impactful change to make first].
```

If running Claude-only (either by `--no-gemini` or Antigravity failure), collapse the three issue tables into a single table and note the mode:

```
### Issues
> Antigravity review skipped ([reason]).

| # | Location | Rule | Issue | Severity | Rewrite |
|---|----------|------|-------|----------|---------|
```

### Step 5: Optional apply-agreed (never auto-edit)

**Default:** stop after the tables. Rewrites are for the human to paste.

**When `--apply-agreed` is set, or the user asks after reading the tables:** offer to apply **Agreed + major** rows only (Claude-only / Antigravity-only and all minors stay out unless the user explicitly expands the set).

Flow:

1. List the candidate rows (number + one-line location).
2. Ask for explicit yes (or a subset of row numbers). No silent file write.
3. On yes: apply those rewrites to the file with a normal edit tool; show a short diff summary.
4. Never overwrite the file without that yes. Never invent edits beyond the agreed rewrites.

If Claude-only mode produced a single table, treat **major** rows in that table as the candidate set (same yes gate).

## Error Handling

- **File not found**: Tell the user and ask for the correct path.
- **No prose detected**: If the file is mostly math/tables/preamble, warn and review whatever prose exists.
- **Wrong destination**: If the text is plainly headed somewhere other than a paper, say so in one line and point at `no-ai-slop` rather than reviewing it under academic rules.
- **Antigravity fails**: Proceed Claude-only. Add a note: "Antigravity/Gemini was unavailable — Claude-only review."
- **Antigravity returns garbage**: If the response doesn't follow the requested format, discard it and proceed Claude-only with a note.
