# SPEC — AI-writing literature as an idea network

**Date:** 2026-07-22. **Status:** discovery extraction contract (v0).

## Purpose

Build a **cross-paper idea graph** from the OCR'd corpus in
`docs/notes/literature/ocr/`. The goal of this phase is **idea-finding**, not skill
editing and not answering a pre-chosen research question.

We do not yet know the question. The graph exists so that clusters, contradictions,
orphans, and thin spokes can **force** candidate questions. Skill implications are
out of scope until after a separate diagnosis pass.

This is **not** a `/paper-graph` run. That skill restructures one paper's argument.
Here the unit is the **literature's idea space**; papers are provenance, not the
object being rewritten.

## Non-goals (this phase)

- No `skill-implication` nodes.
- No predetermined "question the graph must answer."
- No edits to `skill/SKILL.md` or `docs/reference/skill-evidence-map.md`.
- No detector-evasion framing; detector papers enter only as claims about structure /
  stylometry / measurement, with charter boundaries respected.
- Do not treat README theme headings as a closed taxonomy (see Orientation below).

## Inputs every extraction agent must read (in order)

1. This SPEC — the contract.
2. Assigned paper: `docs/notes/literature/ocr/<key>/<key>.md` (full OCR).
3. That paper's one-paragraph annotation in `docs/notes/literature/README.md` —
   **orientation only**; do not copy its framing as nodes.
4. `docs/notes/literature/refs.bib` entry for bibliographic fields.
5. **Do not read** `docs/reference/skill-evidence-map.md` during extraction — it is an
   applied filter and would smuggle predetermined questions into the graph.

## Orientation (not a closed set)

README themes exist (framing/co-writing, homogenization, lexical shift, persuasion,
cognitive/authorship, stylometry, graph-structure, bias/equity). Use them only to
avoid getting lost.

**Exhaustiveness rule:** if the paper asserts a proposition that fits no theme, still
emit the node. Tag `theme_fit: "orphan"` (or a new theme label if clearly stable).
Orphans are a primary discovery signal — they mark what our current framing misses.

Duplicate paper note: `kobak-academic-2024` and `kobak-biomed-2025` are the **same
study** (preprint + Science Advances). Extract **once** from the published OCR
(`kobak-biomed-2025`) unless a claim appears only in the preprint; never create two
independent corroboration chains from both keys.

## Node = one assertable proposition (or defined object / method / metric)

One proposition that could be true or false — not a paragraph, not a topic label.
If a sentence asserts two things → two nodes. If three sentences elaborate one thing →
one node. Prefer the paper's own claim grain over our wish to tidy.

### Node schema (JSON)

```json
{
  "id": "PH-03",
  "type": "finding",
  "statement": "Self-contained canonical restatement, <=35 words, present tense, no dangling referents.",
  "quote": "exact OCR snippet, <=60 words, ellipses allowed",
  "anchor": {"paper": "padmakumar-he-2024", "file": "padmakumar-he-2024.md", "approx_page": 4},
  "status": "measured",
  "scope": "InstructGPT co-writing; content diversity metric X",
  "theme_fit": "homogenization",
  "numbers": ["effect size or N if present"],
  "notes": null
}
```

- **id** — `<PREFIX>-<NN>` from the paper prefix map below; two-digit; document order;
  permanent; never reuse.
- **type** — discovery vocabulary (closed for v0; extend only at merge if needed):
  - `finding` — empirical result the paper claims to have shown
  - `mechanism` — proposed why / causal story
  - `lever` — intervention or mitigation tested or proposed
  - `metric` — operationalization (how something is measured)
  - `definition` — stipulated concept
  - `assumption` — taken as given
  - `critique` — attack on another claim/method/paper
  - `gap` — explicit limitation or “not studied”
  - `framing` — how the paper sets the terms of the problem (not a result)
  - `interpretation` — reading of a finding, distinct from the finding
- **status** — epistemic grain of *this paper's* support for the statement:
  - `measured` — with data/test in this paper
  - `replicated` — explicitly framed as replication/corroboration of prior work
  - `suggested` — argued or exploratory, weak/indirect evidence
  - `asserted` — claimed without evidence here
  - `inherited` — cited from elsewhere; this paper does not re-establish it
  - `contested` — this paper disputes a prior claim
- **scope** — population / domain / model / genre limits in ≤20 words; required.
- **theme_fit** — one of the README themes, or `"orphan"`, or a short new label.
- **numbers** — list of quantitative anchors if any; else `[]`.
- **quote + anchor** — mandatory for `finding`, `critique`, `gap`, `lever`; preferred
  for all. OCR page approx is enough; do not invent line numbers.

### Forbidden as nodes (metadata or later phases only)

- Skill rules, draft-mode controls, or “we should change SKILL.md.”
- Detector-pass / evasion tactics as goals.
- Topic headings (“homogenization”) with no assertable proposition.
- Connective rhetoric (“This paper proceeds as follows”).

### Granularity calibration

Dense results paragraph → typically 3–6 nodes (finding + metric + scope caveat +
interpretation if distinct). Related-work name-drops → `inherited` nodes only when the
paper relies on them; otherwise skip. One mechanism discussed at length → one
`mechanism` node plus separate `finding` nodes for evidence offered for it.

## Edges

Emit **within-paper** edges at extraction. **Cross-paper** edges are a later merge/
connect pass — extractors may leave `cross_paper_candidates` notes, not final edges.

### Edge schema (JSON)

```json
{
  "from": "PH-03",
  "to": "PH-01",
  "type": "supports",
  "note": "<=15 words"
}
```

### Edge types (v0)

| type | meaning |
|---|---|
| `supports` | evidence or argument strengthens a claim |
| `depends_on` | claim requires another node’s truth |
| `motivates` | problem/gap leads to question, lever, or study design |
| `measures` | metric node operationalizes a finding/mechanism object |
| `tests` | lever or design tests a mechanism/finding |
| `interprets` | interpretation node reads a finding |
| `critiques` | critique attacks a claim/method |
| `contradicts` | direct logical or empirical conflict |
| `extends` | same claim family, wider scope or new domain |
| `same_as` | duplicate proposition (merge signal) |

**Altitude:** a finding does not `supports` the question it answers; use `motivates` from
gap/framing → design, and keep answers as findings linked by `tests` / `measures`.

## Paper prefix map (OCR complete)

Extract in this order unless a batch plan says otherwise. Same study collapsed:

| prefix | key | notes |
|---|---|---|
| HB | `hellstrom-2024` | framing |
| HM | `hallmark-2024` | provenance / transparency |
| PH | `padmakumar-he-2024` | content diversity |
| DH | `doshi-hauser-2024` | individual vs collective |
| HG | `homogenizing-growthrate` | diversity growth-rate metric |
| DP | `diverse-personas-2026` | mitigation lever |
| KB | `kobak-biomed-2025` | excess vocabulary; skip re-extract of `kobak-academic-2024` except preprint-only deltas |
| AS | `arxiv-shifts-2025` | preprint lexical shift |
| YK | `yakura-podcasts-2024` | speech lexical drift |
| PM | `pubmed-medical-vocab` | domain corroboration |
| JK | `jakesch-2023` | opinion shift |
| WC | `williams-ceci-2026` | attitude shift / safeguards |
| KS | `kosmyna-2025` | cognitive debt |
| ST | `stankovic-2026` | critique of Kosmyna |
| MD | `mdpi-prisma-2026` | stylometry survey |
| SS | `stroke-stylometry` | clinical domain stylometry |
| SN | `story-networks-2025` | story social graphs |
| TS | `threads-subtlety-2024` | discourse motifs |
| DA | `dependencyai-2026` | dependency-label detection |
| MO | `munoz-ortiz-2024` | dependency/constituent structure |
| FS | `fluency-semantic-net-2024` | semantic association nets |
| DR | `detection-review-2026` | active/passive detection review |
| GB | `gender-bias-2023` | downstream gender bias |

Not in OCR yet (no extraction until present): Juzek & Ward; Lee et al. co-writing design
space; Draxler ghostwriter effect; press-only `nbc-coalition-2026` without primary study.

## Phased workflow (discovery)

| Phase | What | Output | Question locked? |
|---|---|---|---|
| 0 | Scout corpus completeness / duplicate keys | short scout note | no |
| 1 | This SPEC | `SPEC.md` | no |
| 2 | Per-paper extract (batched) | `fragments/<key>.json` | no |
| 3 | Merge duplicates; normalize types; list orphans | `nodes.json` draft + `orphans.md` | no |
| 4 | Connect cross-paper edges; contradiction hunt | `edges.json` + `tensions.md` | no |
| 5 | Diagnose graph structure (clusters, hubs, thin support, gaps) | `diagnosis.md` | **candidates emerge** |
| 6 | Author picks the question(s) worth pursuing | STATUS update | yes, by decision |

**Stop after phase 5** until the author chooses a question. No skill-implication layer
before that choice.

## Suggested first batch (not a priority ranking of truth)

To get a readable graph early without claiming the rest are irrelevant:  
`padmakumar-he-2024`, `doshi-hauser-2024`, `kobak-biomed-2025`, `jakesch-2023`,
`williams-ceci-2026`, `kosmyna-2025`, `stankovic-2026`.

Second batch: structure/stylometry cluster + levers/metrics (`threads-subtlety-2024`,
`munoz-ortiz-2024`, `story-networks-2025`, `diverse-personas-2026`,
`homogenizing-growthrate`, …).

Full corpus still in scope; batching is logistical.

## Independent evaluation rule

The model (or vendor) that extracts a paper must not be the sole merger or the sole
contradiction auditor for that paper’s nodes. Generation ≠ evaluation applies to the
graph itself.

## What else the graph is allowed to reveal

Besides “ideas for writing with AI,” diagnosis should explicitly inventory:

- **orphans** — claims outside current themes (framing exhaustiveness test)
- **metrics** — how the field operationalizes diversity, ownership, structure, bias
- **levers** — interventions actually tested (with outcomes), distinct from findings
- **contradictions / critiques** — e.g. Kosmyna ↔ Stanković
- **scope walls** — which findings cannot travel across domain/genre/model class
- **stated gaps** — including gaps that suggest questions this repo could own

These are first-class discovery products. They are not secondary to a single through-line.

## Done means

- `fragments/` for every OCR’d key in the prefix map (or an explicit skip log)
- merged `nodes.json` / `edges.json`
- `orphans.md`, `tensions.md`, `diagnosis.md`
- no skill edits; no single “the question” asserted by the extractors

The author’s next decision after diagnosis: which candidate question becomes the live
research thread.
