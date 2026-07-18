---
name: writing
description: Draft or review academic LaTeX prose against a codified style profile. Review mode: Claude critiques, Antigravity/Gemini gives a parallel second opinion, output synthesizes concrete rewrites. Draft mode (--draft): turns a human-supplied idea/outline into near-final prose in a strong academic register, self-critiques against the 20 rules and measured AI-tells, and hands off to an independent judge. Use when the user wants to draft or tighten academic writing from a concept, review a LaTeX paper, or types /writing.
---

# Writing

Two modes over one 20-rule academic style profile.

- **Review mode** (default): critique existing LaTeX prose. Claude reviews; Antigravity/Gemini gives a parallel second opinion via `agy`; output synthesizes both into concrete rewrites.
- **Draft mode** (`--draft`): turn a human-supplied idea/outline into near-final academic prose. The human owns the argument and vouches for the facts; the skill drafts, self-critiques against the 20 rules and the measured AI-tells, and hands the result to an independent judge (never the drafting model alone).

The 20 rules serve both modes: in review they are the critique checklist; in draft they are generation-time constraints. Several rules (S2, S4, S11, S16, S17) double as anti-tell controls — the register markers detectors key on are the same failure modes these rules forbid.

## Style Profile

Apply these rules when reviewing. Each issue MUST reference its rule ID.

| ID | Rule | Directive |
|----|------|-----------|
| S1 | Precision opening | Open with precision — no throat-clearing. First sentence of every paragraph should carry weight. Cut "It is well known that...", "In recent years...", "There is a growing body of literature..." |
| S2 | Sentence rhythm | Vary sentence length with purpose. Short sentences for impact, long for nuance. Flag monotonous runs of same-length sentences. |
| S3 | Voice balance | Active voice ~80%, passive only for depersonalization ("the model is estimated" not "we estimated the model" when the agent is irrelevant). Flag gratuitous passive. |
| S4 | No filler | No filler phrases. Cut "it is important to note that", "it should be mentioned that", "in order to", "the fact that", "it is worth noting". |
| S5 | Conclusion first | Lead with the conclusion, not the buildup. No buried ledes. The reader should know the point before the evidence. |
| S6 | Quantitative anchoring | Anchor claims to numbers. "Large effect" → "a 12pp increase". Flag vague quantifiers without numerical backup. |
| S7 | Explicit uncertainty | Label gaps and limitations directly. "We cannot identify X because Y" not "future research might explore X". Own the limitation. |
| S8 | Question-driven openings | Section and subsection openings should pose the question the section answers. Frame the reader's expectation. |
| S9 | Parallel construction | Lists, enumerations, and comparisons must use parallel grammatical structure. Flag broken parallelism. |
| S10 | Confident, not arrogant | State findings directly. "The results show X" not "we believe the results might suggest X". But never overclaim — match confidence to evidence. |
| S11 | No apologetic framing | No "we merely", "this is only a first step", "we do not claim to". State scope and move on. |
| S12 | Author voice | "I" for solo-authored papers, "we" for co-authored. Never "the authors", "the present study", "this paper argues". Determine from context (single author → "I"; multiple → "we"). |
| S13 | Dialectical structure | Hypothesis → counter → synthesis. Present the tension, then resolve it. Flag sections that argue only one side. |
| S14 | Meta-commentary signposts | Use explicit transition signposts at section/paragraph boundaries. "Section 3 tests this prediction by...", "Having established X, I now turn to Y." |
| S15 | AER prose flow | No bullet points, no numbered lists in prose. AER style: flowing paragraphs with logical connectives. If information is enumerated, weave it into sentences ("First, ... Second, ... Finally, ..."). Tables are acceptable for data, never for arguments. |
| S16 | Memorable writing | Vivid specifics over abstractions ("the 2008 Lehman collapse" not "a financial crisis"). At least one striking, quotable formulation per section. Open and close sections with your strongest sentences. The reader should remember something. |
| S17 | Jargon discipline | Use the plainest word that carries the same precision. "Reverse causality" over "endogeneity" when both work. Technical terms earn their place only when no plain alternative exists. |
| S18 | Citation integration | Prefer narrative citations (`\citet`, `\textcite`) that weave into prose: "\citet{autor2003} shows..." over parenthetical dumps. Flag runs of 3+ stacked `\citep`/`\parencite` — break them up or integrate the most important ones narratively. |
| S19 | One idea per paragraph | Each paragraph makes one clear point. Flag paragraphs that drift across multiple topics. The first sentence should signal what the paragraph is about. |
| S20 | Reference consistency | Use `\eqref` for equations (never bare `\ref`). Use consistent naming for formal results: always "Proposition~\ref{prop:X}" not sometimes "Prop." sometimes "Proposition" sometimes a bare number. Same for Lemma, Theorem, Corollary. |

## Input Parsing

The user invokes `/writing` with arguments in any order:

```
/writing path/to/file.tex              # Review a file (all rules)
/writing path/to/file.tex S1 S5 S6     # Review with rule subset only
/writing path/to/file.tex --no-gemini  # Claude-only review
/writing --no-gemini S3 S12 file.tex   # Flags and rules in any order
/writing --draft concept.md            # Draft mode: idea/outline → prose
/writing --draft --section intro --words 400 "core claim + evidence"
```

**Parse rules:**
1. **`--draft`**: switch to Draft Mode (below). Everything after is the concept — a file path (idea/outline) or inline text stating the argument.
2. **File path**: any argument containing `/` or ending in `.tex`/`.md` → treat as a file path
3. **Rule subset**: arguments matching `S\d+` (e.g., `S1`, `S12`) → filter to those rules only
4. **`--no-gemini`**: skip the independent second opinion (Claude-only). Discouraged in draft mode — see the charter note in Draft Mode.
5. **Draft options**: `--section <name>`, `--words <N>`, `--venue <AER|generic|...>` tune draft-mode output.
6. **Pasted text**: with no `--draft` and no file path, treat remaining text as inline LaTeX to review.

If no arguments are given, ask whether the user wants to draft (and for what concept) or review (and for which file).

## Draft Mode

Triggered by `--draft`. Turns a human-supplied idea into near-final academic prose. The human supplies and owns the argument; the skill never invents the thesis, and never invents facts, numbers, or citations (see Step D5).

### Step D1: Parse the concept

Read the concept (file or inline). Extract: the central claim/argument, any sub-claims, supplied evidence or citations, and constraints (`--section`, `--words`, `--venue`). If the concept is only a topic with no argument, STOP and ask the human for the actual claim — drafting without an argument produces exactly the hollow, ownerless prose this skill exists to avoid.

### Step D2: Plan (claim outline)

Expand the concept into a one-line-per-paragraph outline where each line states *the point that paragraph makes* (not its topic). Present the outline to the human for a quick confirmation or reorder. This is where the human steers the argument — by shaping the outline, not by editing finished prose. Do not draft until the outline is confirmed (or the human says "just draft it").

### Step D3: Draft with anti-tells as generation constraints

Draft prose from the confirmed outline in a strong academic register (`--venue` default: generic strong-academic; `AER` → flowing-prose economics style). Apply these rules **at generation time**, not as an afterthought:

- **S2 / burstiness**: deliberately vary sentence length. No runs of same-length sentences; place at least one very short declarative sentence at an argumentative pivot ("It tightens.") — variance follows from that move; don't chase a numeric target.
- **Excess-vocabulary ban**: avoid the measured tell-register. Treat this as *examples of a register to avoid*, not a fixed blocklist (the specific words date as models are steered off them). Avoid: *delve, underscore, showcase, intricate, meticulous(ly), pivotal, realm, tapestry, testament, nuanced, crucial, comprehensive*; formal-connector overuse: *furthermore, moreover, additionally, notably, it is worth noting, importantly*. The durable rule is: flat, uniformly-flowery register is the tell — write plainly and variably instead.
- **Stock-register test**: stock academic phrases are slop even when off any tell list ("do the heavy lifting", "in the classic sense", "the standard prescription"). If a phrase could appear unchanged in a hundred other papers, replace it.
- **Argument-carried transitions**: the logic of adjacent sentences carries the turn; do not scaffold with *therefore/thus/yet/hence* where the content already turns.
- **S4/S5/S10/S11/S16**: no filler, conclusion-first, confident not arrogant, no apologetic hedging. The memorable formulation must compress the argument's mechanism itself ("the bank that must keep the promise is not the bank that made it") — decorative symmetry that could caption any argument gets cut. One owned first-person move ("I argue", per S12) and an occasional colloquial grace note are allowed.
- **S6/S7**: anchor claims to the human-supplied numbers; label uncertainty the human flagged. Never fabricate a figure to satisfy S6 — if a claim needs a number the human did not supply, mark it (Step D5), do not invent one.

**Exemplar levers (positive contrast, distilled from rated field prose — full ratings in `docs/notes/2026-07-18_prose-exemplar-ratings.md`).** Condition on the *move*, never imitate a passage (naive imitation ranked 4th of 7 on slop):

- **Mechanism as a plain declarative, then justify.** State the causal claim bare, then earn it with a number or a concrete instance. Good: "The Fed never rolls dice; every move is a response to something" (Cochrane). Not: "Markets understand the incentive structure and price the announcement accordingly" — abstract summary that states nothing.
- **Compress the hard idea to an aphorism that *is* the mechanism.** Good: "everyone may know that the fundamentals are sound, but it may not be that everyone knows that everyone knows this" (Morris & Shin). Not a decorative chiasmus that could caption any argument.
- **Open on a specific, dated, quantified fact — never a big-question throat-clear.** Good: a named FOMC date and the basis-point move (Gürkaynak–Sack–Swanson). Not: "A central question in macroeconomics is…" — a stock opener even 9/10 writers fall into, and still slop.
- **Weld the number into the claim sentence.** Good: "the multiplier is 1.4 at 8 quarters and 1.1 at 16" (Ramey). Not: "the effect is large and persistent."
- **Instantiate before generalizing.** Run one concrete scenario through the mechanism ("Concretely, suppose…", Caballero & Simsek) before stating the general result.

### Step D4: Self-critique + one revision (TICL-style)

Critique the draft against the 20 rules and the anti-tell register. For each weak passage, name *what* it drifts toward (which tell / which rule) and *why*, then rewrite once. Run four targeted passes: (a) **stock-register hunt** — flag any phrase that could appear unchanged in a hundred other papers; (b) **connector strip** — remove *therefore/thus/yet/hence* where the adjacent content already carries the turn; (c) **memorable-line test** — does the quotable line state the mechanism, or decorate it? Cut decoration; (d) **declarative-then-justify** — does each core mechanism claim land as a plain declarative before its justification, or is it buried mid-sentence in a subordinated periodic clause? Surface it. This contrast step (show what NOT to sound like, and the reason) is the lever that outperforms piling on more examples — but it is **not** a substitute for independent review (Step D6).

### Step D5: Verify-before-use list

Extract every factual claim, quantity, date, and citation in the draft into a checklist for the human to confirm. This is the accountability pass — one review, not heavy editing. Flag explicitly any place the draft needed a fact the human did not supply. Nothing in this list may be an invented value.

### Step D6: Independent evaluation (required)

The drafting model must not be the sole reviewer of its own draft (project charter). Hand the draft to an independent judge — reuse the Antigravity/Gemini path (Review Mode, Step 3) to score the draft against the 20 rules and return concrete fixes. Optionally run the deterministic linguistic metrics (sentence-length SD, tell-word frequency) as a cheap pre-filter before the judge. `--no-gemini` disables this; warn the human that draft mode then has no independent check.

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

### Step 1: Read LaTeX

Read the target file. If it contains `\input{}` or `\include{}` directives for prose sections, follow those chains and read the included files too. Concatenate into a single prose body.

**Focus on prose only.** Skip:
- Preamble (`\documentclass` through `\begin{document}`)
- Math environments (`equation`, `align`, `gather`, etc.)
- Tables (`tabular`, `table`)
- Figure environments (`figure`)
- Bibliography entries
- Comments (`%`)
- Pure formatting commands (`\label`, `\ref`, `\cite` — keep surrounding prose)

### Step 2: Claude Review

Apply the style profile (all 20 rules, or the user-specified subset) to the prose.

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

```bash
agy -p "$(cat <<'PROMPT'
You are reviewing academic LaTeX prose for style. Apply ONLY these rules:

S1: Open with precision — no throat-clearing
S2: Vary sentence length with purpose
S3: Active voice ~80%, passive only for depersonalization
S4: No filler phrases ("it is important to note", "in order to", etc.)
S5: Conclusion first, no buried ledes
S6: Quantitative anchoring — numbers on claims
S7: Explicit uncertainty — label gaps directly
S8: Question-driven section openings
S9: Parallel construction in lists and comparisons
S10: Confident, not arrogant
S11: No apologetic framing
S12: "I" for solo-authored, "we" for co-authored. Never "the authors" or "this paper argues"
S13: Hypothesis → counter → synthesis structure
S14: Meta-commentary signposts at transitions
S15: No bullet points or numbered lists. AER flowing prose style
S16: Memorable writing — vivid specifics, striking formulations, quotable sentences
S17: Jargon discipline — plainest word that carries the same precision
S18: Citation integration — narrative \citet/\textcite over parenthetical dumps of 3+ \citep
S19: One idea per paragraph
S20: Reference consistency — \eqref for equations, consistent naming for Proposition/Lemma/Theorem

INSTRUCTIONS:
- Identify the 10-15 most impactful STYLE issues (not grammar/spelling).
- For each issue, provide: the original passage, the rule ID, severity (major/minor), and a CONCRETE REWRITE (not "consider rephrasing" — write the actual replacement).
- Also note 2-3 specific strengths.
- Respond in this exact format:

STRENGTHS:
1. [passage quote] — [why it works]

ISSUES:
1. PASSAGE: [original text]
   RULE: [S#]
   SEVERITY: [major/minor]
   REWRITE: [concrete replacement]

STRUCTURAL NOTES:
[Any observations about paragraph ordering, argument flow, signposting]

Review @FILE_PATH.
PROMPT
)" --add-dir "$(dirname FILE_PATH)"
```

Replace `FILE_PATH` with the actual file path, and replace `$(dirname FILE_PATH)` with the containing directory. If the current working directory already contains the file, `--add-dir` can be omitted. If a rule subset was specified, include only those rules in the Antigravity prompt.

**Timeout**: If Antigravity takes longer than 120 seconds or fails, proceed Claude-only and note this in the output. For long reviews, pass `--print-timeout 10m` or run the command in the background.

### Step 4: Synthesize

Match issues from Claude and Antigravity by location overlap (same passage or adjacent sentences about the same problem).

Classify each issue:
- **Agreed**: Both Claude and Antigravity flagged the same passage/problem (highest confidence)
- **Claude Only**: Only Claude flagged it
- **Antigravity Only**: Only Antigravity flagged it

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

#### Claude Only
| # | Location | Rule | Issue | Severity | Rewrite |
|---|----------|------|-------|----------|---------|

#### Antigravity Only
| # | Location | Rule | Issue | Severity | Rewrite |
|---|----------|------|-------|----------|---------|

### Structural Notes
[Paragraph ordering, argument flow, signpost observations from both reviewers]

### Summary
Issues: N major, N minor. Reviewers: Claude + Antigravity/Gemini (or Claude only if --no-gemini / Antigravity failed). Top priority: [single most impactful change to make first].
```

If running Claude-only (either by `--no-gemini` or Antigravity failure), collapse the three issue tables into a single table and note the mode:

```
### Issues
> Antigravity review skipped ([reason]).

| # | Location | Rule | Issue | Severity | Rewrite |
|---|----------|------|-------|----------|---------|
```

## Error Handling

- **File not found**: Tell the user and ask for the correct path.
- **No prose detected**: If the file is mostly math/tables/preamble, warn and review whatever prose exists.
- **Antigravity fails**: Proceed Claude-only. Add a note: "Antigravity/Gemini was unavailable — Claude-only review."
- **Antigravity returns garbage**: If the response doesn't follow the requested format, discard it and proceed Claude-only with a note.
