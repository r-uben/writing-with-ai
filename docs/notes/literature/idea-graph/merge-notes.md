# Merge notes — batch 1 (Phase 3)

**Date:** 2026-07-22. **Phase:** `merge-draft`. Independent of extractors.  
**Outputs:** `nodes.json` (218 nodes), `edges.json` (246 within-paper edges + 48 cross-paper candidates), `orphans.md`.

No skill implications. No research question locked. No `diagnosis.md`.

---

## Counts by paper

| paper | prefix | nodes | within edges | cross candidates | flags |
|---|---|---|---|---|---|
| padmakumar-he-2024 | PH | 35 | 37 | 6 | — |
| doshi-hauser-2024 | DH | 33 | 38 | 5 | rich design/scope flags |
| kobak-biomed-2025 | KB | 30 | 31 | 6 | — |
| jakesch-2023 | JK | 32 | 34 | 6 | — |
| williams-ceci-2026 | WC | 34 | 38 | 2 | preregistered; N=2582 |
| kosmyna-2025 | KS | 37 | 50 | 6 | **`partial_ocr`** |
| stankovic-2026 | ST | 17 | 18 | 17 | — |
| **total** | | **218** | **246** | **48** | |

## Counts by type (after normalization)

| type | n |
|---|---|
| finding | 83 |
| gap | 27 |
| metric | 21 |
| interpretation | 19 |
| lever | 17 |
| critique | 16 |
| framing | 13 |
| mechanism | 11 |
| assumption | 6 |
| definition | 5 |
| **total** | **218** |

(Pre-normalization: KS-04 had invalid type `inherited` → counted above as `finding`.)

## Theme_fit distribution (high level)

| theme_fit | n |
|---|---|
| persuasion | 65 |
| cognitive/authorship | 47 |
| homogenization | 29 |
| framing/co-writing | 27 |
| lexical shift | 27 |
| orphan | 9 |
| bias/equity | 7 |
| stylometry | 3 |
| ownership-credit | 2 |
| collective-social-dilemma | 1 |
| graph-structure | 1 |

Outside README set: 9 + 2 + 1 = **12** (see `orphans.md`).

## Normalization changes

| id | change | note |
|---|---|---|
| **KS-04** | `type: inherited` → `type: finding` | `inherited` is a SPEC **status**, not type. Status already `inherited`; kept. Only type drift in batch 1. |

All other types already in SPEC v0 closed set. No status remaps. New theme labels (`ownership-credit`, `collective-social-dilemma`) **kept**, not forced into README themes.

## Duplicate / near-duplicate clusters (propose_merge; nodes kept)

**Within-paper**
- PH-24 ↔ PH-34 — feedback-loop optimism vs repeated-interaction gap.
- DH-01 ↔ DH-31 — social-dilemma framing vs interpretation (roles differ).
- ST-07 ↔ ST-16 — near-duplicate connectivity≠engagement critiques.
- WC-34 — meta N=2582; candidate demotion into WC-08/WC-09 notes.

**Cross-paper (do not dual-count)**
- PH-03 → JK-09/10/15 — inherited citation of Jakesch; not independent corroboration.
- JK-15 ↔ WC-08/09 — attitude-shift family; WC extends/robustifies JK lineage.
- JK-18 ↔ WC-12; JK-19 ↔ WC-14 — unawareness near-duplicates.
- JK-25 ↔ WC-03/05 — behavior→attitude mechanism family.
- PH-11 ↔ DH-20 ↔ KS-15 — homogenization family across essay/fiction/edu essays.
- PH-01/02 ↔ DH-01/31 ↔ KB-30 — monoculture framing; KB-30 inherits PH.
- PH-34 ↔ JK-31 ↔ WC-30 — longitudinal/persistence gap cluster.
- KS ↔ ST critique map — debt, connectivity, agency, quoting, time pressure (Phase 4 tension set).
- DH-24 vs KS-21 — ownership **neighbors**, not same proposition (credit penalty ≠ self-ownership).

Full `merge_log` is in `nodes.json`.

## Flags carried forward

- **kosmyna-2025:** `extractionFlags: ["partial_ocr"]` on paper meta; all 37 nodes retained. Extractor skipped exhaustive appendix dDTF/topic mining — Session-4 and topic-stratified claims especially fragile (also flagged by ST).
- **doshi-hauser-2024:** design/ITT/scope/exploratory flags preserved on paper meta.
- **williams-ceci-2026:** preregistration + safeguard inventory preserved.

## Suspicious / watch items in extracts (not silently fixed)

1. **KS-04 type drift** — fixed in merge; check other fragments in later batches for status-as-type.
2. **JK-10 control %** — extractor notes Fig.3 vs body 36% vs 38% for control “bad” sentences; numbers field may be slightly inconsistent.
3. **ST-04 reporting inconsistencies** — quotes Kosmyna quoting-direction flip and phantom group labels; Phase 4 should verify against OCR before treating as settled error.
4. **ST cross_paper_candidates volume** (17) — dense critique map to KS; not yet adjudicated edges.
5. **KB-30** — inherited homogenization framing citing Padmakumar & He; must not become a second independent spoke for diversity loss.
6. **DH-15 `contradicts` DH-22** within-paper — funny-null vs professionalization reading; intentional tension, keep.
7. **WC-22/23 `contradicts` levers** — failure of safeguards modeled as contradicts; slightly unconventional edge polarity (finding vs lever) but coherent; leave for Phase 4.
8. **No kobak-academic-2024 fragment** — correctly collapsed per SPEC/scout; do not invent dual corroboration.

## Edge type inventory (within-paper only)

supports 115 · measures 37 · motivates 31 · tests 21 · critiques 12 · extends 10 · depends_on 9 · interprets 6 · contradicts 5.  
No within-paper `same_as` edges yet — duplicate signals live in `merge_log` for Phase 4 connect.

## Next (not this agent)

Phase 4: adjudicate `cross_paper_candidates` + `merge_log` propose_merge clusters into real cross-paper edges; write `tensions.md` (esp. KS↔ST, JK↔WC, PH↔DH homogenization). Still no diagnosis / no question lock.
