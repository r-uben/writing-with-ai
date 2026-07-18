# Independent review: Draft Mode (D1–D6)

**Date:** 2026-07-19
**Reviewer:** code-reviewer subagent (≠ implementer)
**Scope:** skill/SKILL.md Draft Mode only; taste A2 not yet wired
**Method:** static review against charter + anti-slop panel levers

---

## Summary

The Draft Mode scaffolding is coherent and the charter-level commitments (no invented facts, independent judge required) are present and clearly stated. The critical problems are operational, not philosophical: D6 never explains how to actually hand the in-memory draft to the Gemini path, D2 will silently deadlock any non-interactive invocation, and D5's post-hoc verify list relies on the same model that drafted to self-certify its own outputs—leaving hallucinated numbers intact in the prose body. Several minor findings involve underspecification (word-count handling, `--venue` semantics, solo-authorship assumption) and one structural risk: the anti-tell word list in D3, while correctly framed as a register guide, carries latent detector-chasing motivation that the charter explicitly forbids.

---

## Findings

### C1-F1 — D6 operational gap: draft never reaches Gemini
- **Severity:** major
- **Steps:** D6
- **Issue:** D6 instructs the agent to "reuse the Antigravity/Gemini path (Review Mode, Step 3) to score the draft." Review Mode Step 3 invokes `agy -p` with an `@FILE_PATH` reference and an `--add-dir` flag pointing to a directory on disk. The draft produced in D3/D4 exists only in the agent's response buffer—it is never written to a file. No step between D4 and D6 tells the agent to materialize the draft, and no alternative inline-paste invocation is given. The result: D6 is mechanically unreachable as written.
- **Evidence:** D6: "Hand the draft to an independent judge — reuse the Antigravity/Gemini path (Review Mode, Step 3) to score the draft against the 20 rules and return concrete fixes." Review Mode Step 3: `agy -p "$(cat <<'PROMPT' ... Review @FILE_PATH. PROMPT)"`. No intervening write-to-disk step.
- **Rewrite:** Replace the first two sentences of D6 with:

  > Write the draft (Step D3/D4 output) to a temporary file, e.g. `/tmp/writing_draft_<timestamp>.md`. Then pass it to the independent judge using the same Antigravity invocation as Review Mode Step 3, substituting that temp file for `FILE_PATH`. The prompt sent to Antigravity should scope the review to prose style (all 20 rules) and return concrete rewrites. Delete the temp file after the review completes or errors.

---

### C1-F2 — D2 deadlock on non-interactive invocation
- **Severity:** major
- **Steps:** D2
- **Issue:** D2 ends: "Do not draft until the outline is confirmed (or the human says 'just draft it')." This presupposes an interactive, synchronous session where the human can reply. When the skill is invoked as a background subagent, in a Cursor automation, or via a piped `claude -p` call, there is no channel for the human to respond. The agent will present the outline and then wait indefinitely—or, if it guesses and proceeds, it violates the stated constraint. Neither outcome is specified.
- **Evidence:** D2: "Present the outline to the human for a quick confirmation or reorder. This is where the human steers the argument. Do not draft until the outline is confirmed (or the human says 'just draft it')."
- **Rewrite:** Add a fallback clause at the end of D2:

  > If invoked non-interactively (e.g., the concept was provided entirely inline with no further input expected), treat the outline as auto-confirmed and note it in the output: `### Outline (auto-confirmed — no interactive round-trip)`. In interactive sessions, wait for explicit confirmation or the phrase "just draft it" before proceeding.

---

### C1-F3 — D5 hallucination check is post-hoc and leaves invented numbers in prose
- **Severity:** major
- **Steps:** D3, D5
- **Issue:** D5 generates a verify-before-use checklist from the same model that drafted in D3. If the agent hallucinated a specific figure during drafting (e.g., fabricated a percentage to satisfy S6), D5 will list it in the checklist—but the number remains verbatim in the draft body. The human must manually cross-reference prose and checklist; no instruction tells them to treat unconfirmed `NEEDS SOURCE` items as placeholders to be excised, not merely acknowledged. The anti-invention protection is aspirational rather than mechanical.
- **Evidence:** D3: "anchor claims to the human-supplied numbers…Never fabricate a figure to satisfy S6 — if a claim needs a number the human did not supply, mark it (Step D5), do not invent one." D5: "Flag explicitly any place the draft needed a fact the human did not supply. Nothing in this list may be an invented value." The draft body itself carries no placeholder; the instruction to "mark it (Step D5)" defers the mark to the checklist, not the prose.
- **Rewrite:** Add to D3 an explicit inline-marking convention, and add a paragraph to D5 with the human's required action:

  > **D3 addition (after S6/S7 bullet):** When a claim requires a number or citation the human did not supply, insert the placeholder `[VERIFY: description]` directly in the prose at that point. Do not choose a plausible value. The placeholder propagates into D5 automatically.

  > **D5 addition (new final sentence):** Any item marked `NEEDS SOURCE` in this list corresponds to a `[VERIFY: ...]` placeholder in the draft body. The human must either supply the value and replace the placeholder, or delete the claim before use. Do not treat confirmation of the list alone as permission to use the unverified prose.

---

### C1-F4 — D3 anti-tell word list inverts charter priority
- **Severity:** minor
- **Steps:** D3
- **Issue:** The charter (CLAUDE.md) states: "Optimize for clarity, argumentative ownership, semantic preservation, source fidelity, and transparent revision—not AI-detector outcomes." D3's "excess-vocabulary ban" is ostensibly framed as a register guide ("the durable rule is: flat, uniformly-flowery register is the tell — write plainly and variably instead"), but the named list (*delve, underscore, showcase, intricate, meticulous(ly), pivotal, realm, tapestry, testament, nuanced, crucial, comprehensive*) is organized around detector signal, not prose quality. Several words on the list (*nuanced*, *crucial*, *comprehensive*) are ordinary English adjectives whose vice is imprecision, not tell-status. The inversion surfaces as: an agent following the list could produce detector-clean prose that is still bad (precise word, wrong register reason), and could avoid a perfectly apt word because it appears on a list anchored to 2025-era model outputs. The skill acknowledges this ("the specific words date as models are steered off them") but buries the acknowledgment after the list.
- **Evidence:** D3: "Avoid: *delve, underscore, showcase, intricate, meticulous(ly), pivotal, realm, tapestry, testament, nuanced, crucial, comprehensive*; formal-connector overuse: *furthermore, moreover, additionally, notably, it is worth noting, importantly*. The durable rule is: flat, uniformly-flowery register is the tell — write plainly and variably instead."
- **Rewrite:** Invert the ordering so the durable principle leads and the examples follow:

  > **Excess-vocabulary discipline:** The register tell is uniformity and floweriness, not any specific word. Write plainly and variably; a short direct word where a longer flowery one would be instinctive is the discipline. As dated examples of the over-flowery register to avoid (not a fixed blocklist—the signal drifts as models are retrained): *delve, underscore, showcase, intricate, meticulous(ly), pivotal, realm, tapestry, testament*; formal connectors used as throat-clearing: *furthermore, moreover, additionally, notably, importantly*. The vice of *nuanced, crucial, comprehensive* is imprecision, not tell-status—flag them for vagueness, not for appearance on this list.

---

### C1-F5 — D3 bakes in solo-author voice, overriding S12
- **Severity:** minor
- **Steps:** D3
- **Issue:** D3 says "One owned first-person move ('I argue', per S12)." S12 says: "Determine from context (single author → 'I'; multiple → 'we')." D3 hardcodes `I argue` as the canonical owned move regardless of authorship context. If the concept implies co-authorship (e.g., the outline names multiple authors, or the field context makes plural authorship obvious), D3's instruction directly contradicts S12.
- **Evidence:** D3: "One owned first-person move ('I argue', per S12)." S12: "'I' for solo-authored papers, 'we' for co-authored. Never 'the authors', 'the present study', 'this paper argues'. Determine from context."
- **Rewrite:**

  > One owned first-person move per S12 — use "I argue" for solo-authored work, "we argue" for co-authored. Determine authorship from the concept or ask if ambiguous.

---

### C1-F6 — D3 `--words` flag parsed but never acted on
- **Severity:** minor
- **Steps:** D1, D3
- **Issue:** Input Parsing lists `--words <N>` as a draft option that "tunes draft-mode output." D1 says to extract constraints including `--words`. D3 never mentions the word target again: there is no instruction on how to apply it (aim for N ± some tolerance?), what to do if the natural draft length diverges substantially, or what counts against the target (prose only? including outline headings?). An agent reading only D3 has no guidance on `--words`.
- **Evidence:** Input Parsing rule 5: "`--section <name>`, `--words <N>`, `--venue <AER|generic|...>` tune draft-mode output." D3: no mention of `--words`.
- **Rewrite:** Add a bullet to D3's opening paragraph:

  > **`--words <N>`**: target the draft body (excluding outline, verify list, and review) to N ± 10%. If the argument requires substantially more to be coherent, note the shortfall in the output rather than silently truncating an incomplete argument.

---

### C1-F7 — D6 Gemini failure mode not specified for Draft Mode
- **Severity:** minor
- **Steps:** D6
- **Issue:** Review Mode's Error Handling section covers Antigravity failures: "If Antigravity takes longer than 120 seconds or fails, proceed Claude-only and note this in the output." D6 invokes the same Gemini path but does not say what to do if that call fails in draft context. An implementer reading D6 in isolation does not know whether to (a) fail the whole draft, (b) proceed and note the gap, or (c) retry. The output template's `### Independent review` slot says `"skipped (--no-gemini) — no independent check"` only for the explicit flag case.
- **Evidence:** D6: "Hand the draft to an independent judge — reuse the Antigravity/Gemini path (Review Mode, Step 3)." No fallback specified for draft mode. Error Handling section applies to Review Mode only by position in the document.
- **Rewrite:** Add to D6:

  > If Antigravity fails or times out (per the 120 s / `--print-timeout 10m` guidance in Review Mode Step 3), fill `### Independent review` with: `"Antigravity unavailable — independent check could not run. Do not treat this draft as independently reviewed."` Do not silently omit the section or treat the self-critique (D4) as a substitute.

---

### C1-F8 — D3 external file reference is brittle
- **Severity:** minor
- **Steps:** D3
- **Issue:** D3 references `docs/notes/2026-07-18_prose-exemplar-ratings.md` as the source for the exemplar levers: "full ratings in `docs/notes/2026-07-18_prose-exemplar-ratings.md`." This is a repository-local path. If the skill is invoked from a different project, if the notes directory hasn't been created yet, or if the file is renamed, the reference silently breaks. The exemplar levers are already inlined in D3 and the file reference adds no executable value—it is documentation provenance, not a required read.
- **Evidence:** D3: "**Exemplar levers (positive contrast, distilled from rated field prose — full ratings in `docs/notes/2026-07-18_prose-exemplar-ratings.md`).**"
- **Rewrite:** Drop the parenthetical or make it non-prescriptive:

  > **Exemplar levers (positive contrast).**

  If provenance is important, move it to a non-imperative footnote-style comment: "(Ratings sourced from docs/notes/2026-07-18_prose-exemplar-ratings.md, if present.)"

---

### C1-F9 — D4 "rewrite once" ambiguity
- **Severity:** minor
- **Steps:** D4
- **Issue:** The step heading says "Self-critique + **one revision** (TICL-style)" but the body says "For each weak passage, name what it drifts toward … then rewrite once." The heading implies a single revision pass over the entire draft; the body implies one rewrite per flagged passage. These are not equivalent: one pass over ten flagged passages is ten rewrites. The intended scope affects how heavily D4 should intervene.
- **Evidence:** D4 heading: "one revision." D4 body: "for each weak passage … then rewrite once."
- **Rewrite:** Clarify the heading:

  > ### Step D4: Self-critique + targeted revision (TICL-style)

  And add a scope clarifier in the body:

  > For each weak passage identified in the four passes below, provide one rewrite. Do not re-draft the entire document; confine changes to the flagged passages. The goal is precision, not a second generative draft.

---

### C1-F10 — Input Parsing rule 1 vs rule 5 conflict swallows draft flags
- **Severity:** minor
- **Steps:** Input Parsing (affects D1 and D3)
- **Issue:** Input Parsing rule 1: "Everything after [--draft] is the concept." Rule 5: "`--section <name>`, `--words <N>`, `--venue <AER|generic|...>` tune draft-mode output." If a user writes `/writing --draft --section intro --words 400 "core claim"`, rule 1 would consume `--section intro --words 400 "core claim"` as the concept, never reaching rule 5. The examples in Input Parsing show these flags co-present (`/writing --draft --section intro --words 400 "core claim + evidence"`) but give no parsing priority.
- **Evidence:** Input Parsing rule 1: "Everything after is the concept — a file path (idea/outline) or inline text stating the argument." Example: `/writing --draft --section intro --words 400 "core claim + evidence"`.
- **Rewrite:** Amend rule 1:

  > **`--draft`**: switch to Draft Mode. Strip any subsequent `--section`, `--words`, and `--venue` flags (and their values) first; treat the remaining tokens as the concept (file path or inline text).

---

## Per-step checklist

| Step | Verdict | Notes |
|------|---------|-------|
| D1 | gap | No failure mode for missing or empty concept file; `--words`/`--section`/`--venue` extraction mentioned but how to handle absent flags is not specified |
| D2 | conflict | "Do not draft until confirmed" deadlocks non-interactive invocations; no async fallback |
| D3 | gap / minor conflict | Anti-tell word list risks detector-chasing framing (charter violation direction); solo-authorship assumed; `--words` target never actioned; external file reference brittle; D3 is otherwise the strongest step |
| D4 | gap | "One revision" vs "rewrite once per passage" ambiguous; TICL acronym unexplained; four passes overlap heavily with D3 constraints without explaining the distinction (generate vs verify) |
| D5 | gap | Post-hoc checklist generated by drafting model; hallucinated numbers persist in prose body; no inline placeholder convention specified; human action on `NEEDS SOURCE` items underspecified |
| D6 | gap | No instruction to materialize draft as file before Gemini invocation; Gemini failure mode not specified for draft context; "optional" metrics trigger undefined |

---

## What to defer until after A2 (taste wiring)

- Any demand that D3 or D4 reference taste principles, personal voice, or field-specific register targets — these hooks are absent by design and their absence is not a defect.
- Evaluation of whether the exemplar levers in D3 align with the author's own rated prose (requires A2 profile to exist).
- Whether the memorable-line criterion in D3 should be taste-parameterized (mechanism-aphorism may be right for macro/finance but wrong for other subfields).
- The `--venue AER` shorthand — its concrete prose constraints should be defined when taste wiring lands, since taste and venue interact.

---

## Recommendation

**Ship blockers (must fix before use):**
1. **C1-F1** (D6 materialization gap): Draft Mode cannot invoke its mandatory independent check as written. Any use of `--draft` without `--no-gemini` will fail or silently skip D6.
2. **C1-F2** (D2 interactive deadlock): Non-interactive invocations stall. Cursor automations and subagent calls will hit this immediately.
3. **C1-F3** (D5 post-hoc hallucination check): The anti-invention protection is aspirational; hallucinated figures persist in prose and no inline marking convention enforces removal. This is a charter-level risk.

**Polish (should fix, not blocking):**
- C1-F4: Reorder anti-tell guidance to lead with durable principle, not word list.
- C1-F5: Remove solo-authorship assumption from D3's "I argue" example.
- C1-F6: Define `--words` handling in D3.
- C1-F7: Add Gemini failure fallback for Draft Mode.
- C1-F8: Decouple exemplar lever text from repository-local file path.
- C1-F9: Clarify "one revision" scope in D4 heading.
- C1-F10: Fix Input Parsing rule 1 to strip draft flags before consuming remainder as concept.

Do NOT apply these fixes in this review. (Overnight wave 3: findings logged only; C2 waits on author / A2 sequencing.)
