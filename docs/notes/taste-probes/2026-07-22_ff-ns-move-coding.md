# Independent move coding — FF / NS AI probes (2026-07-22)

**Coder:** parent session (did not draft the probes).  
**Drafts:** `2026-07-22_fama-french-taste-probe.md`, `2026-07-22_nakamura-steinsson-taste-probe.md`.  
**Codebook:** `prose-moves-graph.md` move defs. Generation ≠ evaluation.

## Fama–French (3/3 AI)

| Move | Human FF | AI gpt | AI grok | AI terse | Verdict |
|---|---|---|---|---|---|
| `incumbent→defect→our-fix` | ✓ | ✓ | ✓ | ✓ | AI reproduces |
| `named-models-as-landscape` | ✓ | ✓ | ✓ | ✓ | AI reproduces |
| `thesis-in-first-sentence` | ✓ | · | · | ~ | AI mostly misses (opens on textbook habit) |
| `enumerated-gaps` | ✓ (“at least three… First…”) | · | · | · | **AI misses** — names “two” error sources in prose, never First/Secondly / “at least three” |
| `rhetorical-question-pivot` | · | · | · | · | N/A (human FF lacks it); AI does not invent it |
| `quantitative-anchor` | ✓ | ✓ | ✓ | ✓ | AI reproduces (SEs > 3%/yr) |
| `stakes/so-what` | provisional | ✓ | ✓ | ✓ | AI reproduces |

**FF discriminator read:** Where human FF has `enumerated-gaps`, all three AI drafts miss the enumerated form. Matches the MS pattern for that move.

## Nakamura–Steinsson (3/3 AI)

| Move | Human NS | AI gpt | AI grok | AI terse | Verdict |
|---|---|---|---|---|---|
| `incumbent→defect→our-fix` | ✓ | ✓ | ✓ | ✓ | AI reproduces |
| `concrete-episode-as-evidence` | ✓ | ✓ | ✓ | ✓ | AI reproduces (9/11 / Sept 2001) |
| `plain-mechanism-before-math` | ✓ | ✓ | ✓ | ✓ | AI reproduces |
| `big-question-opener` | ✓ | ✓ | · | · | AI **sometimes** reproduces (1/3) |
| `concede-own-limitation-early` | ✓ | ✓ | ✓ | ✓ | AI reproduces (power / ~5 bp) — **not** a discriminator |
| `enumerated-gaps` | · | · | · | · | N/A (human NS lacks it) |
| `rhetorical-question-pivot` | · | · | · | · | N/A (human NS lacks it); gpt opener Q is `big-question-opener`, not a mid-intro pivot |
| `quantitative-anchor` | ✓ | ✓ | ✓ | ✓ | AI reproduces |
| `scope-fence` | provisional | ✓ | ✓ | ✓ | AI reproduces |

**NS discriminator read:** MS-coded `enumerated-gaps` / `rhetorical-question-pivot` cannot be tested as “AI miss of a human move” here — human NS lacks both. AI freely reproduces NS spine + limitation concede; big-question opener is unstable across voices.

## Cross-concept summary

| Candidate discriminator (from MS AI miss) | FF (human has move?) | NS (human has move?) | Still looks like AI miss? |
|---|---|---|---|
| `enumerated-gaps` | yes → AI 0/3 | no | **Yes on FF** (replicates) |
| `rhetorical-question-pivot` | no | no | Untestable on FF/NS content; still only MS-positive |

**Implication for skill / econ register:** `enumerated-gaps` is the stronger cross-paper human-vs-AI signal so far (MS + FF). `rhetorical-question-pivot` remains MS-only; do not promote to a skill mandate. S8 / pivot tension stays deferred pending more theory papers or weak-human controls — not unlocked by FF/NS.

**Caveat:** FF/NS probes were three voice-variants from one drafting agent session, not three vendor CLIs like MS (grok / gpt-sol / ollama). Treat as corroboration of *content* generalization, weaker than MS on *model-family* generalization.
