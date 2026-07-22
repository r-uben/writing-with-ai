# Connect notes — batch 1 (Phase 4)

**Date:** 2026-07-22. **Phase:** `connect-draft`. Independent of extractors and Phase-3 merger.  
**Outputs:** updated `edges.json`, `tensions.md`. No `diagnosis.md`. No research question locked. No skill-implication nodes.

---

## Counts

| bucket | n |
|---|---|
| within-paper edges kept | 246 |
| cross-paper candidates in | 48 |
| candidates → accepted (refined to node edges) | 27 |
| candidates rejected | 21 |
| accepted cross-paper edges (from candidates) | 40 |
| new edges from active hunt | 7 |
| edges appended to `edges` | 47 |
| **total edges out** | **293** |
| of appended, `cross_paper: true` | 46 |
| of appended, within-paper `same_as` (ST-07→ST-16) | 1 |

### Appended edge types

critiques 21 · extends 11 · same_as 7 · depends_on 5 · contradicts 2 · motivates 1

---

## Accept / reject policy used

- **Accept** only when both endpoints exist in `nodes.json` and the relation is a SPEC edge type with a ≤15-word note.
- **Reject** out-of-batch papers (HG, DP, MO, hallmark, hellstrom, yakura, arxiv-shifts, pubmed-vocab, detection-review, stylometry cluster), outside-OCR citations (Bai/Song, Arnold, Johnson, Olson), and handwavy thematic neighbors (JK opinion-shift ≟ KB lexical excess; DH-24 ≟ JK/hallmark credit; KS-29 “may be challenged”).
- **Inheritance hygiene:** `KB-30 → PH-*` and `PH-03 → JK-*` are `depends_on`, never treated as independent corroboration. `kobak-academic-2024` dual-link correctly refused.
- **JK↔WC:** adjudicated as `extends` / `same_as` / method `critiques` of gaps/levers — not finding-level `contradicts`.
- **PH↔DH:** collective homogenization = `extends`; individual quality framing = scope tension (`DH-22 critiques PH-13`), not hard empirical contradiction across mismatched tasks.
- **KS↔ST:** dense `critiques` map; only `ST-14/ST-15` promoted to `contradicts`.

---

## Hunt beyond candidates

From `merge_log` propose_merge clusters and active contradiction pass:

- Longitudinal gap `same_as`: PH-34 ↔ JK-31 ↔ WC-30  
- ST-07 ↔ ST-16 within-paper `same_as`  
- DH-22 → PH-13 critiques (professionalization vs tradeoff)  
- WC-22 → JK-32 critiques (failed brief safeguards vs monitoring lever)  
- ST-02 → KS-31 extends (commentary sharpens KS’s own sample gap)

DH-24 vs KS-21 left **unlinked** (ownership neighbors; different evaluandum).

---

## Next (not this agent)

Phase 5: `diagnosis.md` — clusters, hubs, thin spokes, gap inventory. Still no question lock until author decision (Phase 6).
