# Dual-track experiment: quality harness vs Pangram harness (audit)

**Date:** 2026-07-19
**Status:** in progress — wave 0–3 complete (Q/P panel + Draft Mode review logged); Pangram scoring pending quota reset
**Depends on:** Pangram free quota reset; Variant B (human from-memory rewrite) still load-bearing
**Related:** `2026-07-18_ai-writing-quality-and-detectors.md` (decoupling result, n=4); `2026-07-18_anti-slop-harness-panel.md` (quality judges)

## Why

Prior results show register-quality optimization and Pangram origin detection are decoupled: anti-tell, restructure, and panel-winning TICL drafts all score 100% AI; same-topic human prose scores 100% Human. The open social worry is that readers treat Pangram as a truth oracle. Before building more harness machinery, measure whether a **quality objective** and a **Pangram objective** produce different prose — and what that implies about Pangram.

This is an **audit of Pangram as a proxy**, not a commitment to ship detector-evasion into the skill.

## Hard separation rule

| Artifact | May optimize for Pangram? |
|---|---|
| `skill/SKILL.md` (production Draft/Review) | **No** — quality, ownership, fidelity only |
| This experiment + fixtures under `docs/notes/` | **Yes** — Track P is research-only |

Track P never writes into the skill. Pangram remains a measured outcome on both tracks, never the skill's fitness function.

## Tracks

Same human-supplied **concept** and confirmed **claim outline** (D1–D2). Two AI producers, plus the existing human cells.

| Track | Objective function | Method (sketch) |
|---|---|---|
| **Q** — quality | Taste profile + contrast exemplars + independent prose judge (current Draft Mode D3–D6) | One draft via existing skill path; no Pangram in the loop |
| **P** — Pangram | Minimize Pangram AI score / maximize Human score | `uv run track-p` — iterative multi-agent rewrite pipeline; Pangram scored manually (budgeted checks). Research-only code in `src/writing_audit/` |
| **B** — human rewrite | Author from-memory rewrite of an AI draft (already planned) | Human only — if a model produces B, the cell is void |
| **C** — human control | Published human prose, same topic (Andrade et al. already run) | Baseline: 100% Human |

## Shared measures (every cell)

1. **Pangram** — version, % AI / Human, confidence, segment notes. Record quota use.
2. **Layer-2 quality** — blind independent judge(s), same rubric as the anti-slop panel (not the drafting model). Score register/slop; do not ask judges to guess origin.
3. **Layer-1 linguistics** — `uv run writing-metrics <fixture>`: sentence-length SD, TTR, and whatever replaces the dead tell-lexicon once calibrated. Thresholds from human corpus when available; until then, report raw metrics only.

Optional later: edit distance / semantic similarity of P vs Q vs B to see whether Pangram-chasing collapses meaning.

## Interpretation matrix

| Pattern | Reading |
|---|---|
| Q high quality, Pangram still ~100% AI; P clears Pangram, quality flat or worse | Pangram tracks **origin/fingerprint**, not quality — proxy fails; do not put P into the skill |
| Q and P both improve quality *and* Pangram moves together | Proxy still partially valid; investigate what P changed that Q missed |
| P clears Pangram only via semantic drift / argument softening | Evasion tax on fidelity — charter forbids shipping that |
| B clears Pangram; Q and P do not | Human revision is the lever; AI-side harnesses (both tracks) are exhausted for detection |

## Minimum fair test (one concept)

Expanded to **three concepts** across economics registers — see `docs/notes/pangram-audit/README.md`:

| ID | Register |
|---|---|
| `nakamura-steinsson-2018` | Empirical macro |
| `morris-shin-1998` | Theoretical macro |
| `fama-french-1997` | Empirical finance |

Per concept:

1. Fix concept + outline (fixtures in `docs/notes/pangram-audit/fixtures/`).
2. Produce **Q** with current Draft Mode (Track Q baselines written).
3. Produce **P** with `uv run track-p` (budgeted Pangram feedback loop).
4. Produce **B** (author only) from outline or from Q — record which before writing.
5. Extract **C** from paper library (human published prose).
6. Blind-judge Q, P, B for quality; run Pangram when quota allows.
7. Write results into this note + `STATUS.md`.

**N caveat:** three concepts × four tracks is still directional (not a formal study), but cross-register divergence is the point. If Q vs P diverge similarly in all three, the audit conclusion is much stronger than n=1.

## Explicit non-goals

- Do not deploy Track P into `~/.config/ai-skills/no-ai-slop/`.
- Do not treat a Pangram pass as proof the prose is good, or a fail as proof it is bad.
- Do not invent facts/citations to game either track (charter).
- Do not claim the audit "beats" Pangram — claim only what the contingency table shows.

## Sequencing vs other work

Primary path remains: taste database → independent skill review → real-concept Draft Mode test → Variant B when quota resets.

This dual-track run slots in **with** Variant B (same quota window, same concept if possible) so one human rewrite cell serves both Open Q#2 and the Pangram audit. Track P is optional if quota is tight: prioritize B over P.

---

## Protocol (frozen 2026-07-19)

**Pangram tool:** record version (currently v3.3.2), % AI / % Human, confidence, segment notes, checks used / quota remaining.

**Scoring schema:** one row per cell — concept × track (C/Q/P/B) × Pangram result × `writing-metrics` output.

**Track B rules (human rewrite):**
- **Default: outline-only.** Read the concept fixture (`*-concept.md` or `<id>.md`); do not open Track Q while writing.
- From-memory rewrite into `*-track-b.md`.
- Author attestation: no AI paste; confirm Q draft was not visible.
- Target length: 200–330 words.

**Track C rules (human control):** published pre-ChatGPT prose from paper library OCR; record source path + page refs + word count.

**Track Q / P:** already produced; do not edit before scoring except via Track P harness for P.

**Quality panel (Layer 2):** ≥3 cross-vendor judges; anti-slop rubric from `2026-07-18_anti-slop-harness-panel.md`; **do not ask judges to guess origin**; exclude Kimi until quota reset.

**Quota budget (~4 free checks/day):** day 1 — human controls (C) + Morris–Shin B; day 2 — Q cells; day 3 — P + remaining B; FG graded ladder when B2-FG tiers exist. Record every check.

**Passage length band:** 200–330 words for fair cross-cell comparison.

**Hard separation:** Track P never writes into `skill/SKILL.md`.

---

## Results — 2026-07-19 checks (Pangram 3.3.2, quota 4/4 used)

Checks run by author ~19:47–19:53 CEST, before the agent session; details recovered from Pangram history (no extra quota spent). `P(AI)` is the raw `prediction_prob` from the dashboard API.

| # | Time (CEST) | Text | Words | Verdict | Confidence | P(AI) |
|---|---|---|---|---|---|---|
| 1 | 19:47 | MS variant A — "Multiple-equilibrium models … **explain** self-fulfillment, but they do not explain timing or policy" | 233 | AI (100%) | High | 0.9931 |
| 2 | 19:47 | MS variant B — "Multiple-equilibrium models … **capture** self-fulfillment: a continuum of speculators" | 214 | AI (100%) | High | 0.9929 |
| 3 | 19:50 | Morris–Shin (1998) published paragraph, verbatim ("We argue here that the apparent multiplicity…") — final ¶ of `morris-shin-1998-track-c.md` | 156 | Human (100%) | High | 0.0025 |
| 4 | 19:53 | Close paraphrase of the same paragraph ("We argue that the apparent multiplicity…") | 133 | Human (100%) | Low | 0.0747 |

### Provenance caveats (author to confirm)

- Checks 1–2 do **not** match the frozen `morris-shin-1998-track-q.md` / `-track-p.md` fixtures verbatim. They read as revised Q-side variants (the "counsel of despair" flourish flagged by the panel is gone). Confirm what they were and whether either counts as a protocol cell; if not, they are off-protocol probes and the frozen Q/P cells are still unscored.
- Check 3 scored only the final paragraph (156 w) of the Track C extract, not the full ~265 w fixture.
- Check 4's origin is unattested (author paraphrase from the open paper? from memory?). If author-written with the source visible, it is neither Track B (must be from outline only) nor Track C. Log as an off-protocol probe unless attested otherwise.
- Checks 3–4 are below the 200–330 word band; Pangram confidence may degrade on short passages (cf. FF fixture note).

### Directional reading (n small, off-protocol cells included)

- Same concept, same claims, same register: AI-side drafts ~0.993, published human prose 0.0025. Consistent with the decoupling result — Pangram tracks origin/fingerprint, not quality.
- The paraphrase cell is the most informative: near-identical semantics to the published paragraph, still "Human" but confidence Low and P(AI) up 30× (0.0025 → 0.0747). Human-performed re-encoding of the same content moves the score toward AI without changing the claims — a fingerprint, not a content, signal.
- No protocol cell is fully scored yet: NS/FF Track C, all Track Q, all Track P, and Track B remain for the next quota windows (per the frozen budget: C first, then Q, then P + B).

### Quota log

- 2026-07-19: 4/4 used (author, pre-session). Next window: 4 checks after daily reset (~06:00 CEST 2026-07-20 based on prior-day usage at ~18:30–19:00 ET clearing overnight; verify at first check).
