# Pangram audit: three-concept parallel build

**Status:** fixtures + Track Q baselines ready; Track P harness in `src/writing_audit/`; Pangram scoring pending quota reset.

Broad economics coverage across three registers:

| ID | Paper | Register | Human control (Track C) |
|---|---|---|---|
| `nakamura-steinsson-2018` | Nakamura & Steinsson (2018, QJE) | Empirical macro / identification | Intro + HF window passage from OCR library |
| `morris-shin-1998` | Morris & Shin (1998, AER) | Theoretical macro / global games | Intro from OCR library |
| `fama-french-1997` | Fama & French (1997, JFE) | Empirical finance / asset pricing | Abstract + intro from OCR library |

## Tracks (per concept)

| Track | Location | Status |
|---|---|---|
| **Concept + outline** | `fixtures/<id>.md` | ready |
| **Q** — quality draft | `fixtures/<id>-track-q.md` | ready |
| **P** — Pangram harness | `uv run track-p fixtures/<id>-track-q.md` → `fixtures/<id>-track-p.md` | harness ready; outputs pending run |
| **B** — human rewrite | `fixtures/<id>-track-b.md` | **author only** — empty template |
| **C** — human control | noted in each fixture | extract from library when scoring |

## Commands

Layer-1 metrics (sentence-length SD, TTR, etc.):

```bash
uv run writing-metrics docs/notes/pangram-audit/fixtures/nakamura-steinsson-2018-track-q.md
```

Track P pipeline (research only — 3-stage multi-agent rewrite):

```bash
uv run track-p docs/notes/pangram-audit/fixtures/nakamura-steinsson-2018-track-q.md --rounds 2
uv run track-p docs/notes/pangram-audit/fixtures/morris-shin-1998-track-q.md --reviser agy
```

Run logs and intermediates land in `docs/notes/pangram-audit/runs/<fixture>-<timestamp>/`.

## Run order (when Pangram quota available)

1. Score **C** passages (human library extracts) — calibration anchors.
2. Score **Q** drafts (already written).
3. Run **P** via `uv run track-p` on each Q draft; score each iteration; cap checks per concept.
4. Author produces **B** from-memory rewrites (do not read Q while writing).
5. Blind quality panel on Q/P/B; record Pangram + Layer-1 metrics (`writing-metrics` on each cell).
6. Write results to `docs/notes/2026-07-19_dual-track-pangram-audit.md`.

**Quota budget suggestion:** 4 free checks/day → prioritize B (1) + Q (1) + best P iteration (1) per concept; defer extra P iterations.
