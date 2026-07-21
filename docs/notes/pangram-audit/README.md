# Pangram audit: three-concept parallel build

**Status (2026-07-19 evening):** Wave 0–3 agent work complete. Blind Q/P panel done. First Pangram results in: 4/4 checks used 2026-07-19 (author, off-protocol MS probes — see results section of `2026-07-19_dual-track-pangram-audit.md`). Protocol cells (C/Q/P/B) still unscored; quota 0/4 until reset.

## What's done

| Artifact | Status |
|---|---|
| Experiment protocol | Frozen in `2026-07-19_dual-track-pangram-audit.md` |
| Human originals (Track C) | `*-track-c.md` — all 3 concepts |
| AI quality drafts (Track Q) | `*-track-q.md` — all 3 concepts |
| AI detector-chase drafts (Track P) | `*-track-p.md` — all 3 concepts |
| Layer-1 metrics | `metrics-baseline.md` — Q, C, P |
| Blind Layer-2 panel (Q vs P) | `docs/plans/.../logs/panel-{ns,ms,ff}.md` |
| Human rewrites (Track B) | Empty — **author** |
| Pangram scores | 4 off-protocol MS probes scored 2026-07-19 (2×AI ~0.993 high-conf; MS-C final ¶ Human 0.0025 high-conf; paraphrase Human 0.0747 low-conf). Protocol cells pending quota |

## Concepts

| ID | Paper | Register |
|---|---|---|
| `nakamura-steinsson-2018` | Nakamura & Steinsson (2018, QJE) | Empirical macro |
| `morris-shin-1998` | Morris & Shin (1998, AER) | Theoretical macro |
| `fama-french-1997` | Fama & French (1997, JFE) | Empirical finance |

## Fixture map

| Track | Meaning | Files |
|---|---|---|
| **C** | Human published prose | `*-track-c.md` |
| **Q** | AI quality draft | `*-track-q.md` |
| **P** | AI detector-chase draft | `*-track-p.md` |
| **B** | Your from-memory rewrite | `*-track-b.md` |

## Layer-2 panel (Q vs P, overnight)

| Concept | Cleaner track | Notes |
|---|---|---|
| NS | **Q** (3/3) | P added ornamental intensifiers |
| MS | **P** (3/3) | Q hit “counsel of despair” stock flourish |
| FF | **Q** (3/3) | P’s “And here's the thing” / “mirage” = moderate |

Track P never ships into `skill/SKILL.md`.

## Commands

```bash
uv run writing-metrics docs/notes/pangram-audit/fixtures/<fixture>.md
uv run track-p docs/notes/pangram-audit/fixtures/<id>-track-q.md --rounds 1
```

## Dispatch log

| Wave | Date | Log |
|---|---|---|
| 0–1 | 2026-07-19 | `docs/plans/.../logs/2026-07-19_wave0-1.md` |
| 2 | 2026-07-19 | `docs/plans/.../logs/2026-07-19_wave2.md` |
| 3 | 2026-07-19 | `docs/plans/.../logs/2026-07-19_wave3.md` |

Plan board: `docs/plans/2026-07-19_writing-skill-pangram-audit/STATUS.md`

## Next

1. Author: write Track B **blind** (`morris-shin-1998-track-b.md`), then compare AI probe in `docs/notes/taste-probes/`
2. Author: confirm taste Q3–Q5 (+ draft P3–P5 proposal in taste-probes)
3. Pangram: score Track C when quota resets
4. Agent: wire taste into skill after author picks; apply C1 skill fixes (C2)
