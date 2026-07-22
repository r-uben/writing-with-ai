# Diagnosis — batch-1 idea graph

**Phase:** 5 (diagnosis). **Date:** 2026-07-22.  
**Inputs:** `nodes.json` (merge-draft, 218 nodes), `edges.json` (connect-draft, 293 edges), `orphans.md`, `tensions.md`, `merge-notes.md`, `connect-notes.md`, `scout.md`.

Independent of extractors, merger, and connect agent. **No research question locked.** No skill-implication nodes. No skill-edit recommendations.

---

## 1. Census

| object | n |
|---|---|
| nodes | **218** |
| edges | **293** |
| within-paper edges | **247** |
| cross-paper edges | **46** |
| papers in batch | **7** |

### By type

| type | n | type | n |
|---|---:|---|---:|
| finding | 83 | critique | 16 |
| gap | 27 | framing | 13 |
| metric | 21 | mechanism | 11 |
| interpretation | 19 | assumption | 6 |
| lever | 17 | definition | 5 |

Findings dominate (~38%). Gaps + metrics + levers together (~30%) already give a rich discovery surface beyond “what happened.”

### By theme_fit

| theme_fit | n | theme_fit | n |
|---|---:|---|---:|
| persuasion | 65 | orphan | 9 |
| cognitive/authorship | 47 | bias/equity | 7 |
| homogenization | 29 | stylometry | 3 |
| framing/co-writing | 27 | ownership-credit | 2 |
| lexical shift | 27 | graph-structure | 1 |
| | | collective-social-dilemma | 1 |

README themes cover most nodes, but persuasion + cognitive/authorship alone are **112/218 (~51%)**. Stylometry and graph-structure are almost empty in this batch (second-batch papers not yet extracted). Twelve nodes sit outside the README set (`orphan` + new labels; see §4).

### By status

| status | n |
|---|---:|
| measured | 113 |
| asserted | 47 |
| suggested | 39 |
| contested | 11 |
| inherited | 8 |

Roughly half the graph is measured; the other half is interpretive, definitional, or inherited. That split matters for hubs (§3).

### By paper

| paper | nodes | extraction flags |
|---|---:|---|
| kosmyna-2025 | 37 | **`partial_ocr`** |
| padmakumar-he-2024 | 35 | — |
| williams-ceci-2026 | 34 | preregistered; N=2582; safeguard inventory |
| doshi-hauser-2024 | 33 | rich design/scope/exploratory flags |
| jakesch-2023 | 32 | — |
| kobak-biomed-2025 | 30 | — |
| stankovic-2026 | 17 | — |

### Cross-paper edge-type mix (46 edges)

| type | n | role in batch |
|---|---:|---|
| critiques | 21 | almost entirely ST→KS (+ WC→JK safeguard stress; DH→PH framing) |
| extends | 11 | homogenization triad; JK→WC persuasion robustification |
| same_as | 6 | unawareness / mechanism family; longitudinal-gap cluster |
| depends_on | 5 | inheritance hygiene (KB→PH; PH→JK; WC→JK) |
| contradicts | 2 | only ST-15→KS-02 and ST-14→KS-30 |
| motivates | 1 | KS-31→ST-12 redesign |

Cross edges are **critique-heavy**, not corroboration-heavy. The densest corroboration family is persuasion (JK↔WC `extends`/`same_as`); the densest conflict family is cognitive debt (KS↔ST).

### Flags

- **`partial_ocr` on kosmyna-2025:** all 37 KS nodes retained; appendix dDTF / topic-stratified NLP incompletely extracted. Session-4 and topic-homogeneity claims (`KS-15`, `KS-24`/`KS-25`) are especially fragile—ST already attacks them.
- **DH design/scope flags:** idea-springboard (not multi-turn chat); YA microfiction; exploratory ownership/credit (`DH-24`/`DH-25`).
- **WC preregistration + failed safeguards** preserved as first-class lever outcomes.
- **No dual Kobak corroboration:** `kobak-academic-2024` correctly absent; `KB-30` is `inherited` and `depends_on` PH.

---

## 2. Clusters / hubs

### Idea clusters (7)

**A. Homogenization / monoculture (PH–DH–KS, with KB inheritance)**  
Hubs: **PH-11** (InstructGPT corpus homogenization), **DH-20** (story similarity ↑), **KS-15** (edu-essay within-topic homogeneity). Framing spoke: **PH-01** / **DH-01** / **DH-31**. Inheritance spoke: **KB-30** `depends_on` PH (not a third independent measurement). Cross edges: `DH-20 extends PH-11`; `KS-15 extends PH-11` and `DH-20`. Papers: PH, DH, KS (+ KB framing only).

**B. Individual quality uplift vs collective cost (DH, tension with PH)**  
Hubs: **DH-10**/**DH-11** (novelty/usefulness ↑), **DH-22** (professionalization reading), **DH-01** (individual↑/collective↓ framing). Scope wall vs PH: **DH-22 critiques PH-13** (professionalization vs quality–diversity tradeoff). Papers: DH primary; PH as contrasting quality story (flat human ratings / tradeoff reading).

**C. Lexical excess / corpus LLM imprint (KB)**  
Hubs: **KB-14** (13.5% lower bound on 2024 PubMed LLM-processed abstracts), **KB-11** (Δ_G metric). Mechanism: **KB-24** (style-verb/adjective insertion). Largely within-paper; cross-link is framing hygiene to PH, not measurement corroboration. Papers: KB only (in batch).

**D. Latent persuasion / attitude shift (JK–WC)**  
Hubs: **JK-15** (attitude shift d≈0.2), **WC-08**/**WC-09** (larger multi-issue replication), **WC-03**/**JK-25** (behavior→attitude mechanism family), **JK-18**/**JK-19** ↔ **WC-12**/**WC-14** (unawareness `same_as`). Soft tension at mitigation: **WC-22 critiques JK-32**. Papers: JK, WC.

**E. Cognitive debt / EEG engagement / authorship (KS–ST)**  
Hubs: **KS-30** (summary interpretation—highest degree), **KS-10** (connectivity ↓ with support), **KS-05** (tool-condition lever), **KS-21** (ownership interview). Critique swarm from ST (`ST-02`…`ST-17`). Only hard contradicts: **ST-15→KS-02**, **ST-14→KS-30**. Papers: KS, ST.

**F. Ownership / credit norms (DH exploratory + KS interview neighbor)**  
Hubs: **DH-24** (≥25% evaluator ownership penalty), **DH-25** (ethics/disclosure), **KS-21**/**KS-22** (self-ownership → agency reading), **ST-08** (agency construct attack). Connect left DH-24 and KS-21 **unlinked** (neighbors, not `same_as`). Papers: DH, KS, ST.

**G. Longitudinal / repeated-exposure absence (cross-theme gap cluster)**  
Hubs: **PH-34** ↔ **JK-31** ↔ **WC-30** (`same_as` triangle). Shared “single-shot designs silently agree.” Theme tags differ (orphan / persuasion); structural role is one gap family. Papers: PH, JK, WC.

### Degree-ish hub list (undirected degree ≥7)

| id | deg | type/status | one-line |
|---|---:|---|---|
| **KS-30** | 11 | interpretation/suggested | LLM users fare worse across neural/linguistic/scoring levels |
| **PH-11** | 10 | finding/measured | InstructGPT co-writing raises corpus homogenization |
| **WC-03** | 10 | mechanism/suggested | Biased autocomplete → behavior-to-attitude shift |
| **JK-15** | 9 | finding/measured | Post-task attitudes shift toward model stance |
| **KS-10** | 9 | finding/measured | Connectivity falls as writing support rises |
| **KS-15** | 9 | finding/measured | LLM essays more homogeneous within topics |
| **KS-05** | 8 | lever/measured | ChatGPT / Search / Brain-only conditions |
| **DH-22** | 7 | interpretation/suggested | GenAI “professionalizes” stories |
| **DH-20** | 7 | finding/measured | GenAI raises within-condition story similarity |
| **JK-04** | 7 | lever/measured | Opinionated GPT-3 assistant arms |
| **WC-09** | 7 | finding/measured | Exp2 multi-issue attitude shift |
| **KS-21** | 7 | finding/measured | Lowest perceived ownership in LLM group |

Cross-paper degree leaders: **KS-30** (xdeg 4), **JK-15** / **PH-11** / **KS-15** (xdeg 3). The graph’s most connected *proposition* is an interpretation under fire, not a clean measured finding.

---

## 3. Thin support / load-bearing weak nodes

### Load-bearing interpretations (many edges hang on suggested/asserted status)

| node | deg | problem |
|---|---:|---|
| **KS-30** | 11 | Suggested summary reading; attacked by ST-01/09/14/17 and KS’s own gaps (KS-31/32). Highest hub is also thinnest epistemic glue. |
| **WC-03** | 10 | Suggested mechanism; `same_as` JK-25. Attitude findings (WC-08/09) are measured; the pathway is not identified (WC-29 gap). |
| **DH-22** | 7 | Suggested professionalization reading; within-paper `DH-15 contradicts DH-22` (comedy null). |
| **KS-12** | 5 | Suggested “lower connectivity = lower engagement”; ST-07/ST-16 critique the bridge. |
| **KS-02** | 4 | Asserted definition of cognitive debt; ST-15 contradicts the monotonic debt gradient. |
| **JK-22** | 6 | Suggested “latent persuasion” reading of JK-15/09/10 — load-bearing label for the persuasion cluster. |
| **DH-01** | 5 | Asserted individual↑/collective↓ framing; measured legs (DH-10/11/20) support pieces, not the full dilemma claim. |
| **KB-30** | — | Inherited monoculture framing; `depends_on` PH — must not be counted as independent diversity evidence. |

### Measured findings with status/support mismatches

- **KS-10**, **KS-15**, **KS-18/19**, **KS-21**, **KS-24/25**: status `measured`, but ST critiques target *operationalization → debt/agency* bridges more than raw group differences. Pattern findings can stand while construct readings collapse.
- **KS-15** as third homogenization spoke is thinned by **ST-03** (sparse topic cells) + **partial_ocr**.
- **PH-03** (`inherited`): PH’s citation of Jakesch is correctly `depends_on` JK — not a corroboration spoke for persuasion.
- **DH-24** ownership penalty is measured but **exploratory (S5)** per paper flags — thinner than preregistered novelty/usefulness.

### Status mismatch pattern (batch signature)

The graph repeatedly pairs **measured surface findings** with **suggested interpretive hubs**. Cross-paper conflict concentrates on the interpretive layer (debt, agency, engagement, professionalization), not on denying that groups differ.

---

## 4. Orphans & framing holes

From `orphans.md` + graph read:

| hole | evidence nodes | what README framing misses |
|---|---|---|
| **Temporal / feedback dynamics** | PH-24, **PH-34** (+ JK-31, WC-30) | Single-session diversity optimism vs unstudied repeated user–model loops |
| **Ownership-credit as distinct axis** | **DH-24**, DH-25 | Evaluator credit penalty ≠ writer cognitive agency (KS-21/22); new theme kept |
| **Collective social dilemma** | **DH-31** (↔ DH-01) | Strategic aggregate uniqueness loss ≠ pairwise homogenization metric |
| **Energy / material cost** | KS-37 | Non-cognitive externality of LLM writing assistance |
| **Method / task external validity** | KS-32–34, DH-30, DH-15 | EEG pipeline bounds; unsegmented writing stages; comedy null; pro writers understudied |
| **Almost-empty README themes** | stylometry (3), graph-structure (1) | Batch-1 cannot speak to structure/stylometry cluster yet |

Papers with **zero** orphans/new themes: KB, JK, WC, ST — their claims fit README buckets; discovery pressure from orphans is concentrated in **PH, DH, KS**.

---

## 5. Tensions that survive connect

Compressed from `tensions.md`; kinds separated.

### True contradictions (2 cross-paper + notable within)

1. **ST-15 ―contradicts→ KS-02** — null Search vs Brain-only quoting undercuts monotonic “more delegation → more cognitive debt.”
2. **ST-14 ―contradicts→ KS-30** — attention-oriented differences ≠ impaired-learning / across-the-board worse summary.
3. Within-paper (not literature fight): **DH-15 ―contradicts→ DH-22** (funny-null vs professionalization); **WC-22/23/24 ―contradicts→ WC-20/21** (safeguard failure modeled as finding-vs-lever conflict).

### Method / construct critiques (dominant KS↔ST mass)

| target bridge | ST attack | KS nodes |
|---|---|---|
| connectivity → engagement | ST-07, ST-16 | KS-12 (KS-10 pattern less denied) |
| quoting → memory/debt | ST-10, ST-04 | KS-09, KS-18, KS-19 |
| ownership interview → agency | ST-08 | KS-21, KS-22 |
| Session-4 lasting cost | ST-11, ST-13 | KS-24, KS-25, KS-36 |
| pipeline / power / reporting | ST-02, ST-05, ST-06 | KS-07, KS-10 |
| narrative altitude | ST-01, ST-09, ST-17 | KS-13, KS-30 |

**Verdict:** method-vs-construct fights dominate densest cluster; raw differences are less often denied than the debt/agency story built on them.

### Scope / framing conflicts (not empirical flip-flops)

- **DH vs PH quality story:** DH-22 critiques PH-13 — professionalization vs quality–diversity tradeoff; different genres (YA stories vs argumentative essays), interventions (idea springboards vs inline co-writing), quality metrics. Collective homogenization **agrees** (extends); individual-benefit claim is DH-scoped.
- **JK→WC:** extension/robustification, not finding conflict. Soft tension: WC failed Warning/Debrief **critiques** JK-32 monitoring lever as insufficient.
- **Homogenization triad + KB:** extension family; KB-30 must not dual-count; ST-03 thins KS-15 as third spoke.
- **Longitudinal gaps (PH-34 / JK-31 / WC-30):** shared absence, not a fight.

---

## 6. Inventory of other discovery products

### Metrics catalogue (21)

| id | statement (abbrev.) | measures → |
|---|---|---|
| DH-06 | Novelty index (novel/original/rare) | DH-10 |
| DH-07 | Usefulness index (appropriate/feasible/publishable) | DH-11 |
| DH-08 | DAT divergent-association creativity | DH-17, DH-18 |
| DH-19 | Within-condition story embedding similarity | DH-20 |
| JK-07 | Written-opinion sentence crowd labels | JK-09, JK-10, JK-13 |
| JK-08 | Post-task attitude Likert | JK-15 |
| KB-04 | Counterfactual expected frequency q | — |
| KB-05 | Excess gap δ and ratio r | — |
| KB-06 | Excess-word threshold rule | KB-07–09 |
| KB-11 | Marker-set frequency gap Δ_G (LLM-usage lower bound) | KB-12,13,16–18 |
| KS-07 | EEG engagement via dDTF connectivity | KS-10,11,14,24 |
| KS-08 | Interview ownership (full/partial/absent) | KS-21 |
| KS-09 | Quoting-without-looking memory | KS-18,19,25 |
| PH-06 | Model contribution % (keystroke) | PH-07 |
| PH-08 | Key-point authorship (Rouge-L + characters) | PH-09 |
| PH-10 | Essay/corpus homogenization (pairwise sim) | PH-11,12 |
| PH-14 | Corpus diversity (unique info units) | PH-16 |
| PH-15 | Key-point uniqueness clustering | PH-17 |
| PH-27 | Compression-ratio diversity | PH-28 |
| WC-06 | Posttask attitude Likert (AI-alignment scored) | WC-08–10 |
| WC-07 | Bias / influence awareness items | WC-12,14 |

Field operationalizes “diversity” at least five ways (pairwise sim, unique units, clustering, compression, embedding similarity) and “ownership/engagement” via interview + quoting + EEG — a measurement pluralism that itself pressures construct-validity questions.

### Levers catalogue (17) + tested outcomes

| id | lever | tested outcome (if edged) |
|---|---|---|
| **PH-05** | Solo / GPT3 / InstructGPT co-writing | tests PH-07 (model contribution); drives PH-11 family |
| **PH-26** | Diverse multi-user feedback / personalization (proposed) | untested |
| **DH-09** | Optional GPT-4 story ideas (≤5) | tests DH-04/05 mechanisms; outcomes DH-10/11/20 |
| **DH-33** | Future open-ended/genre/novelty levers (proposed) | untested |
| **JK-04** | Opinionated GPT-3 assistant arms | tests JK-09/10/15 (written + attitude shift) |
| **JK-05** | Invisible prefix/infix opinionation | depends_on JK-04 |
| **JK-06** | Autocomplete UI (pause + tab accept) | depends_on JK-04; JK-29 critiques |
| **JK-32** | Monitor/engineer built-in opinions (proposed) | **WC-22 critiques** (brief warnings fail) |
| **WC-15** | Static Text (info-only biased bullets) | tests WC-16 |
| **WC-18** | Write-in-Favor overt instruction | tests WC-19 |
| **WC-20** | Warning (prebunk) | tests WC-22 → **fails** (contradicts lever) |
| **WC-21** | Debrief (debunk) | tests WC-23 → **fails** |
| **KS-05** | ChatGPT / Search / Brain-only | tests KS-10/11/15/18/21 |
| **KS-06** | Session-4 crossover | tests KS-24/25/26 |
| **KS-29** | Delay AI until self-driven effort (proposed) | untested |
| **ST-12** | Within-subjects + teacher/AI scoring redesign | suggested; extends KS-05 |
| **KB-29** | Excess-word monitoring for policy adherence | proposed |

**Tested-and-failed** levers are concentrated in persuasion safeguards (WC-20/21). **Tested-and-positive** levers are mostly the experimental manipulations themselves (opinionated autocomplete; idea springboards; InstructGPT co-writing), not mitigations of homogenization/persuasion/debt.

### Scope walls (cannot travel freely)

| wall | nodes / flags |
|---|---|
| Genre: YA microfiction vs NYT-style essays vs SAT essays vs PubMed abstracts | DH vs PH vs KS vs KB |
| Intervention class: idea springboard vs inline co-writing vs biased autocomplete vs tool-condition EEG lab | DH-09 vs PH-05 vs JK/WC vs KS-05 |
| Model class / vintage | PH-33 (only two OpenAI models); KS-32 (ChatGPT-specific); DH GPT-4; JK GPT-3; WC GPT-3.5/4 |
| Population | DH-30 (pros understudied); KS-31 (small/narrow); WC-31 (Prolific skew); PH-32 (students/L2) |
| Single-shot vs longitudinal | PH-34 / JK-31 / WC-30 |
| Exploratory vs preregistered | DH ownership/credit S5 vs WC main effects |

### Stated gaps worth pursuing (selected from 27 gap nodes)

| gap | why graph-pressure is high |
|---|---|
| **PH-34 / JK-31 / WC-30** | Cross-theme `same_as` — repeated exposure untested in both diversity and persuasion |
| **WC-29** | Mechanism identification gap under a high-degree mechanism hub (WC-03) |
| **WC-32** | Theory-informed awareness interventions beyond thin Warning/Debrief |
| **PH-31** | Mitigation of feedback-tuned diversity loss untested |
| **KS-31–34** (+ ST-11/13) | Sample, model, stage-segmentation, EEG, practice/time confounds — debt construct rests on fragile design |
| **KB-25** | Cannot ID individual LLM abstracts — measurement ceiling for lexical-imprint claims |
| **DH-30** | Professional / high-creativity populations missing from individual↑ story |

---

## 7. Candidate questions the graph forces

**NONE is chosen.** Ranked by how hard the current edge structure *pressures* the question (hub degree × cross-paper conflict/extension × thin interpretive bridges × shared gaps). Labels are typology tags, not a preferred research program.

| rank | pressure | type | question | evidence anchors |
|---|---|---|---|---|
| 1 | **highest** | construct-validity | When LLM-assisted writing changes EEG connectivity, quoting, and ownership self-reports, which of those are valid indicators of “cognitive debt” / agency vs attention, UI, or practice confounds? | KS-10/12/18/21/30; ST-07/08/10/14/15/16; contradicts ST-15→KS-02, ST-14→KS-30 |
| 2 | high | collective-vs-individual | Under what task and intervention regimes does AI assistance raise individual quality while reducing collective diversity—and when is that a true tradeoff vs mismatched metrics across genres? | DH-01/10/11/20/22; PH-11/13/30; DH-22 critiques PH-13; DH-20 extends PH-11 |
| 3 | high | longitudinal | Do single-session homogenization and attitude-shift effects persist, accumulate, or attenuate under repeated user–model interaction? | PH-34 ↔ JK-31 ↔ WC-30 `same_as`; PH-24 optimism vs PH-34 gap |
| 4 | high | intervention | Why do brief Warning/Debrief safeguards fail against biased autocomplete attitude shift, and what (if anything) would constitute an adequate awareness intervention? | WC-20–24 contradicts; WC-22 critiques JK-32; WC-32 gap; JK-15 / WC-08/09 |
| 5 | medium-high | mechanism | Is reduced diversity under co-writing primarily model-text injection (PH-23) or user anchoring on AI ideas (DH-05)—and do those mechanisms unify across springboard vs inline designs? | PH-19/23; DH-04/05; PH-05 vs DH-09 scope wall |
| 6 | medium-high | measurement | Can the field’s multiple diversity operationalizations (pairwise sim, unique units, clustering, compression, embeddings, excess vocabulary) be calibrated against each other, or do they name different objects? | PH-10/14/15/27; DH-19; KB-11; KS-15 |
| 7 | medium | credit-norms | How should “ownership” be decomposed into writer self-ownership, evaluator credit penalties, and cognitive agency—three constructs the graph currently leaves unlinked? | DH-24/25; KS-21/22; ST-08; connect explicitly left DH↔KS ownership unlinked |
| 8 | medium | mechanism | Which behavior-to-attitude pathway (biased scanning, dissonance, self-perception) actually carries latent persuasion under autocomplete? | WC-03 / JK-25; WC-29 gap; JK-23/24 alternatives |
| 9 | medium-low | other (corpus measurement) | How far can excess-vocabulary lower bounds (KB-14) travel as a monitoring lever (KB-29) without individual-abstract identification (KB-25)? | KB-11/14/25/29; KB-30 depends_on PH only |
| 10 | lower (batch-limited) | other (structure) | Do dependency/stylometric structure shifts (almost absent here) mediate homogenization and detectability claims once the structure/stylometry batch is connected? | PH-29 lone stylometry finding; theme census stylometry=3, graph-structure=1 |

Again: **none of these is selected** as the live research thread. Phase 6 is an author decision.

---

## 8. Batch-1 limits

1. **Missing second-batch papers** — structure/stylometry and lever/metric cluster not extracted: `threads-subtlety-2024`, `munoz-ortiz-2024`, `story-networks-2025`, `diverse-personas-2026`, `homogenizing-growthrate`, plus detection/dependency papers. Stylometry/graph-structure themes are nearly empty by logistics, not by literature absence.
2. **Partial OCR on kosmyna-2025** — densest conflict cluster rests partly on incomplete extraction; Session-4 and topic-NLP claims especially provisional.
3. **Selection bias of first batch** — SPEC’s “readable early graph” set over-weights persuasion (JK+WC) and cognition critique (KS+ST) relative to lexical-shift corroborators (arxiv-shifts, yakura, pubmed-vocab) and mitigation levers (diverse-personas, growth-rate metric). Homogenization looks well-supported partly because three batch-1 papers were chosen for that family.
4. **Inheritance hygiene already applied** — KB→PH and PH→JK `depends_on` edges correctly block dual-counting; diagnosis must not reintroduce it.
5. **Outside-OCR skips** — Juzek & Ward; Lee co-writing design space; Draxler ghostwriter; nbc-coalition primary study remain absent (scout/SPEC).
6. **No skill layer** — by contract; absence of skill-implication nodes is intentional, not a graph hole.

---

## Closing snapshot (for author Phase 6)

- **Top hubs:** KS-30 (suggested debt summary under fire), PH-11 (measured homogenization), WC-03 / JK-15 (persuasion mechanism + attitude shift).
- **Sharpest tension:** cognitive-debt construct vs ST null/attention reading (`ST-15→KS-02`, `ST-14→KS-30`), with a surrounding critique swarm on engagement/quoting/agency bridges.
- **Highest-pressure candidates (still unlocked):** (1) construct validity of cognitive-debt indicators; (2) individual quality vs collective diversity tradeoff across task regimes; (3) longitudinal persistence of homogenization and attitude shift.

- **Phase 6 lock (2026-07-22):** see `phase-6-decision.md` — **Q2 spine**, Q1 instrument guardrail, Q3 longitudinal design constraint. Ranks 4–10 remain non-live.
