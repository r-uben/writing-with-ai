# Scout — literature OCR for idea-graph

**Date:** 2026-07-22. **Phase:** 0 complete.

## Corpus

- **Tracked index:** `docs/notes/literature/{README.md,refs.bib}`
- **OCR root:** `docs/notes/literature/ocr/` (gitignored locally)
- **Prefix map in SPEC:** 23 extractable keys (Kobak collapsed to published version)

## Completeness (`ocr/metadata.json`)

| status | keys |
|---|---|
| **completed** | arxiv-shifts-2025, dependencyai-2026, detection-review-2026, diverse-personas-2026, doshi-hauser-2024, fluency-semantic-net-2024, gender-bias-2023, hallmark-2024, hellstrom-2024, jakesch-2023, kobak-biomed-2025, mdpi-prisma-2026, munoz-ortiz-2024, padmakumar-he-2024, pubmed-medical-vocab, stankovic-2026, story-networks-2025, stroke-stylometry, williams-ceci-2026, yakura-podcasts-2024 |
| **partial** | homogenizing-growthrate (10pp), kobak-academic-2024 (16pp), kosmyna-2025 (216pp), threads-subtlety-2024 (26pp) |

Every SPEC prefix has a `<key>/<key>.md`. Word counts range ~2.5k (stankovic) → ~67k (kosmyna).

## Duplicate / collapse

- `kobak-academic-2024` (partial) and `kobak-biomed-2025` (completed) are the **same study**. Extract from **`kobak-biomed-2025` only**; preprint OCR kept for optional delta check later, not as independent corroboration.

## Batch-1 readiness (SPEC suggested first batch)

| key | OCR | words (approx) | note |
|---|---|---|---|
| padmakumar-he-2024 | completed | ~14k | go |
| doshi-hauser-2024 | completed | ~9k | go |
| kobak-biomed-2025 | completed | ~7.5k | go (not academic) |
| jakesch-2023 | completed | ~12k | go |
| williams-ceci-2026 | completed | ~12k | go |
| kosmyna-2025 | **partial** | ~67k | extract what OCR covers; flag `extractionFlags: partial_ocr` |
| stankovic-2026 | completed | ~2.5k | go |

## Not in OCR (SPEC skip list unchanged)

Juzek & Ward; Lee et al. co-writing design space; Draxler ghostwriter; nbc-coalition primary study.

## Decision

Proceed to **Phase 2 batch 1** per SPEC. No question locked. No skill edits.
