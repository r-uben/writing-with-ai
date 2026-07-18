# TICKETS — writing skill + Pangram audit

Status keys: `TODO` · `WIP` · `DONE` · `BLOCKED`. `depends-on` gates dispatch.
Parallelizable = no shared files / no dep. Each ticket = one implementer agent,
then one reviewer pass before commit.

**Panel synthesis (2026-07-19):** advisory critique from three cross-vendor reviewers ([gpt-luna](52d8d1c1-4cb1-4d59-a395-cc906cf5e770), [grok-fast](dfa6a3f9-a15d-473e-9a81-cbc87380650b), [ollama-deepseek](2a1b8554-8b55-47b3-b770-bfda18ca3f58)). Second-pass patches (same day): B0m Layer-1 baseline, B4 split by quota tier (C→Q→B/P), B2-FG graded-revision ladder for Open Q#2, OQ2 verdict ticket, B2-MS non-blocking in wave 1, hardened Done-when clauses.

---

## Stream G — Repo baseline

### TICKET-G0 — Initial commit on feature branch · TODO · depends-on: none · wave 0 · agent: claude
**Problem:** Zero commits; no diff/review/rollback boundary for parallel dispatch.
**Do:** Stage named files only (no `git add -A`); commit current tree on `setup/initial-structure` (or successor branch). Verify not on `main`/`master`.
**Files:** all tracked project files (`skill/`, `docs/`, `src/`, `pyproject.toml`, `uv.lock`, root md)
**Done when:** `git log -1` exists; `git status` clean; branch is not main/master.

---

## Stream B0 — Audit protocol

### TICKET-B0 — Freeze Pangram audit protocol · TODO · depends-on: G0 · wave 0 · agent: claude
**Problem:** Protocol drift across three concepts will invalidate cross-comparison.
**Do:** Append a **Protocol** section to `docs/notes/2026-07-19_dual-track-pangram-audit.md`: Pangram version, scoring schema (AI%/Human%/confidence/quota used), Track B rules (**outline-only**, from-memory, no Q open while writing), passage length band (~200–330 words), judge rubric reference (anti-slop panel), quota budget (B before P, ~4 checks/day). Update all three `*-track-b.md` templates: circle "outline only"; remove ambiguous "after reading Q" as default path.
**Files:** `docs/notes/2026-07-19_dual-track-pangram-audit.md`, `docs/notes/pangram-audit/fixtures/*-track-b.md`
**Done when:** Protocol section committed; all B templates locked to outline-only default.

### TICKET-B0m — Layer-1 baseline on Track Q · TODO · depends-on: G0 · wave 1 · agent: claude
**Problem:** Audit requires metrics table before Pangram scoring; no ticket scheduled it ([grok-fast](dfa6a3f9-a15d-473e-9a81-cbc87380650b)).
**Do:** Run `uv run writing-metrics` on all three `*-track-q.md` fixtures; append results to `docs/notes/pangram-audit/metrics-baseline.md`.
**Files:** `docs/notes/pangram-audit/metrics-baseline.md`
**Done when:** Table lists NS/MS/FF with sentence count, mean length, SD, TTR; command + date recorded.

---

## Stream A — Taste database

### TICKET-A1a — Draft taste minimal pairs Q3–Q5 · TODO · depends-on: G0 · wave 1 · agent: claude
**Problem:** Next taste judgments need forced-choice passages before the author can pick.
**Do:** Add three minimal-pair rows to `taste-profile.md` Judgment log with **Options** filled for: (1) P2 carve-out — limit stated as hard declarative vs soft qualifier; (2) opening move — dated fact vs question vs mechanism-first; (3) citation weave — narrative vs parenthetical dump. Leave Pick/Reason blank.
**Files:** `docs/notes/taste-profile.md`
**Done when:** Three new judgment rows with competent A/B passages; one dimension each; non-strawman.

### TICKET-A1b — Author completes taste Q3–Q5 · TODO · depends-on: A1a · wave 2 · agent: human
**Problem:** Taste signal requires author picks + reasons; agents cannot substitute.
**Do:** Author fills Pick + Reason for Q3–Q5; confirm or revise distilled principles P3–P5 in the executable rules section.
**Files:** `docs/notes/taste-profile.md`
**Done when:** Three picks with reasons recorded; three new `P#` principles (or explicit revisions to P1/P2) in the executable rules block; **P2 carve-out resolved** (not "pending author ruling").

### TICKET-A2 — Wire taste principles into skill D3/D4 · TODO · depends-on: A1b · wave 3 · agent: claude
**Problem:** Taste database is inert until encoded as generation/revision constraints.
**Do:** Patch `skill/SKILL.md` D3/D4 with confirmed P3–P5 (and any P1/P2 revisions) as concrete moves + contrast examples. If P2 carve-out still pending, wire only confirmed principles and leave explicit TODO in taste-profile — do not invent the carve-out. No other skill sections changed.
**Files:** `skill/SKILL.md`, `docs/notes/taste-profile.md`
**Done when:** Each confirmed `P#` appears as a D3 bullet and/or D4 pass; no orphan principles without a skill mapping; diff limited to D3/D4.

---

## Stream C — Skill review & deploy gate

### TICKET-C1 — Independent review of Draft Mode · TODO · depends-on: A2 · wave 4 · agent: code-reviewer (subagent)
**Problem:** Charter forbids shipping unaudited Draft Mode; review must cover taste-integrated skill.
**Do:** Review `skill/SKILL.md` Draft Mode (D1–D6) only. Reviewer must not be the drafter of A2. Output findings by rule ID with concrete rewrites → `logs/review-draft-mode.md`.
**Files:** `skill/SKILL.md` (read), `logs/review-draft-mode.md` (write)
**Done when:** Review artifact lists ≥5 findings (or explicit "no major issues") with severity; D3/D4/D6 each addressed.

### TICKET-C2 — Apply review fixes to skill · TODO · depends-on: C1 · wave 5 · agent: claude
**Problem:** Review findings must land before E2E test or deploy proposal.
**Do:** Apply major findings from C1; document any rejected findings with one-line rationale in review log.
**Files:** `skill/SKILL.md`, `logs/review-draft-mode.md`
**Done when:** Every C1 `major` finding is patched or explicitly rejected in log; no open major items.

### TICKET-C3 — E2E draft on real user concept · TODO · depends-on: C2 · wave 6 · agent: claude
**Problem:** Skill untested on a fresh concept outside audit fixtures.
**Do:** Run Draft Mode D1–D6 on a user-supplied concept (not one of the three audit fixtures). Save output to `docs/notes/e2e-draft-<slug>.md` with outline, draft, verify list, independent review.
**Files:** new e2e note under `docs/notes/`
**Done when:** Note contains confirmed outline, draft prose, verify-before-use checklist, and D6 judge output (or documented `--no-gemini` skip with warning).

### TICKET-C4 — Deploy readiness proposal · TODO · depends-on: C3 · wave 7 · agent: claude
**Problem:** Deployment requires symlink verification and explicit user approval.
**Do:** Verify `~/.config/ai-skills/writing` and `~/.claude/skills/writing` symlink resolution; byte-compare repo vs installed skill; write deploy proposal (do NOT overwrite installed skill).
**Files:** `logs/deploy-readiness.md`, `STATUS.md` (repo root)
**Done when:** Log records symlink paths, diff result, and "awaiting user approval" — no install performed.

---

## Stream B — Pangram audit (per concept)

Concepts: **NS** = nakamura-steinsson-2018 · **MS** = morris-shin-1998 · **FF** = fama-french-1997

### TICKET-B1-NS — Extract Track C (Nakamura–Steinsson) · TODO · depends-on: B0 · wave 1 · agent: claude
**Do:** Extract ~200–330 word human intro/HF-identification passage from paper library OCR; save with source path + page refs.
**Files:** `docs/notes/pangram-audit/fixtures/nakamura-steinsson-2018-track-c.md`
**Done when:** File contains prose, library path, word count, pre-ChatGPT confirmation.

### TICKET-B1-MS — Extract Track C (Morris–Shin) · TODO · depends-on: B0 · wave 1 · agent: claude
**Files:** `docs/notes/pangram-audit/fixtures/morris-shin-1998-track-c.md`
**Done when:** Same as B1-NS.

### TICKET-B1-FF — Extract Track C (Fama–French) · TODO · depends-on: B0 · wave 1 · agent: claude
**Files:** `docs/notes/pangram-audit/fixtures/fama-french-1997-track-c.md`
**Done when:** Same as B1-NS.

### TICKET-B2-MS — Human Track B (Morris–Shin, load-bearing) · TODO · depends-on: B0 · wave 1 · agent: human · non-blocking
**Problem:** Open Q#2 directional answer hinges on genuine human from-memory rewrite; MS is first pick.
**Do:** Author reads `morris-shin-1998.md` outline only; writes from memory into `morris-shin-1998-track-b.md`; records "outline only" in template. Does not block B1/B3/B0m.
**Files:** `docs/notes/pangram-audit/fixtures/morris-shin-1998-track-b.md`
**Done when:** ≥200 words; template records outline-only provenance; author attestation (no AI paste; Q draft not open during writing).

### TICKET-B2-FG — Graded human revisions (forward-guidance, Open Q#2) · TODO · depends-on: B0 · wave 2 · agent: human
**Problem:** B2-MS alone cannot answer Open Q#2's graded-minimum question ([ollama-deepseek](2a1b8554-8b55-47b3-b770-bfda18ca3f58)) — original experiment used forward-guidance paragraph with light→deep edit ladder.
**Do:** Using the forward-guidance AI draft from `2026-07-18_anti-slop-harness-panel.md` (ticl co-winner) or equivalent fixture: author produces **three** human revision tiers — (1) light copy-edit, (2) moderate rephrase, (3) from-memory rewrite — each saved to `docs/notes/pangram-audit/fixtures/forward-guidance-track-b-{light,moderate,memory}.md` with tier labeled.
**Files:** three new fixtures under `pangram-audit/fixtures/`
**Done when:** Three tiers exist with word counts; author confirms human authorship per tier; protocol defines what each tier means (recorded in B0 Protocol section or fixture header).

### TICKET-B2-NS — Human Track B (Nakamura–Steinsson) · TODO · depends-on: B2-MS · wave 3 · agent: human
**Files:** `docs/notes/pangram-audit/fixtures/nakamura-steinsson-2018-track-b.md`
**Done when:** Same provenance rules as B2-MS.

### TICKET-B2-FF — Human Track B (Fama–French) · TODO · depends-on: B2-MS · wave 3 · agent: human
**Files:** `docs/notes/pangram-audit/fixtures/fama-french-1997-track-b.md`
**Done when:** Same provenance rules as B2-MS.

### TICKET-B3-NS — Run Track P (Nakamura–Steinsson) · TODO · depends-on: B0 · wave 2 · agent: claude
**Do:** `uv run track-p docs/notes/pangram-audit/fixtures/nakamura-steinsson-2018-track-q.md --rounds 2`; verify `*-track-p.md` + run log exist.
**Files:** `fixtures/nakamura-steinsson-2018-track-p.md`, `docs/notes/pangram-audit/runs/`
**Done when:** Track P fixture written; Layer-1 metrics in run dir.

### TICKET-B3-MS — Run Track P (Morris–Shin) · TODO · depends-on: B0 · wave 2 · agent: claude
**Files:** `fixtures/morris-shin-1998-track-p.md`, runs/
**Done when:** Same as B3-NS.

### TICKET-B3-FF — Run Track P (Fama–French) · TODO · depends-on: B0 · wave 2 · agent: claude
**Files:** `fixtures/fama-french-1997-track-p.md`, runs/
**Done when:** Same as B3-NS.

### TICKET-B4-MS-C — Pangram Track C (Morris–Shin) · TODO · depends-on: B1-MS · wave 3 · agent: claude + human paste · blocked-external: pangram-quota
**Do:** Score Track C in Pangram; record version/confidence/quota; run `writing-metrics` on cell; append row to dual-track note scoring table.
**Done when:** C cell scored or quota-blocked with date; metrics row recorded.

### TICKET-B4-MS-Q — Pangram Track Q (Morris–Shin) · TODO · depends-on: B3-MS · wave 4 · agent: claude + human · blocked-external: pangram-quota
**Done when:** Q cell scored or blocked; metrics row recorded.

### TICKET-B4-MS-BP — Pangram Track B + P (Morris–Shin) · TODO · depends-on: B2-MS, B3-MS · wave 4 · agent: claude + human · blocked-external: pangram-quota
**Do:** Score B first, then best P iteration; prioritize B per quota budget.
**Done when:** B and P scored or blocked; metrics on both.

### TICKET-B4-FG — Pangram graded B tiers (forward-guidance) · TODO · depends-on: B2-FG · wave 3 · agent: claude + human · blocked-external: pangram-quota
**Do:** Score light/moderate/memory tiers in Pangram (up to 3 checks); record ladder results in dual-track note.
**Done when:** All three tiers scored or quota-blocked with explicit partial table.

### TICKET-B4-NS / B4-FF — Pangram scoring (NS, FF) · TODO · depends-on: respective B1/B2/B3 · wave 5 · agent: claude + human
**Do:** Same C→Q→B/P staging as MS per concept; one concept per quota day if checks scarce.
**Done when:** Per concept: C/Q/B/P table complete or partial with quota note.

### TICKET-B5-MS — Blind quality panel (Morris–Shin) · TODO · depends-on: B3-MS · wave 4 · agent: claude (multi-vendor dispatch)
**Problem:** Quality judgment is origin-blind and must not wait on Pangram quota.
**Do:** Blind panel (≥3 cross-vendor judges, no Kimi) ranks Q/P/B slop; judges must not be drafting models. Save raw rankings → `logs/panel-ms.md`.
**Files:** `logs/panel-ms.md`
**Done when:** ≥3 judges; slop levels + ranks recorded; judges not asked to guess origin.

### TICKET-B5-NS / B5-FF — Blind quality panels · TODO · depends-on: B3-NS / B3-FF · wave 5
**Files:** `logs/panel-ns.md`, `logs/panel-ff.md`
**Done when:** Same as B5-MS.

### TICKET-OQ2 — Open Q#2 verdict · TODO · depends-on: B4-MS-BP, B4-FG · wave 5 · agent: claude
**Problem:** Open Q#2 ("can minimal revision and clearing Pangram coexist?") needs an explicit ruling ticket ([grok-fast](dfa6a3f9-a15d-473e-9a81-cbc87380650b)), not only narrative in B6.
**Do:** Write verdict section in dual-track note: does human B move Pangram off 100%? At which graded tier (FG ladder)? Compatible with charter "minimal revision" language? State yes/no/partial/incompatible with evidence links.
**Files:** `docs/notes/2026-07-19_dual-track-pangram-audit.md`
**Done when:** Verdict paragraph exists even if null ("no movement at any tier"); cites MS B + FG ladder scores.

### TICKET-B6 — Audit synthesis (cross-register) · TODO · depends-on: B4-NS, B4-FF, B5-MS, B5-NS, B5-FF, OQ2 · wave 6 · agent: claude
**Problem:** Interpretation matrix for three-concept audit requires all cells (partial OK if documented).
**Do:** Fill interpretation matrix; cross-register divergence analysis; update repo `STATUS.md` empirical table. Reference OQ2 verdict — do not re-decide it.
**Files:** `docs/notes/2026-07-19_dual-track-pangram-audit.md`, repo `STATUS.md`
**Done when:** Contingency table for NS/MS/FF; explicit caveat if B2-NS/FF or quota cells missing; cross-register conclusion stated.

### TICKET-B7 — Audit integrity check · TODO · depends-on: B6 · wave 6 · agent: claude
**Do:** Verify no Track P code/text in `skill/SKILL.md`; B cells human-authored; no invented facts in Q/P; every Pangram entry has version + quota note.
**Files:** `logs/audit-integrity.md`
**Done when:** Checklist pass/fail recorded with evidence links.

---

## Stream D — Calibration (deferred, non-blocking)

### TICKET-D1 — Layer-1 thresholds from human corpus · TODO · depends-on: B1-NS, B1-MS, B1-FF · wave deferred · agent: claude
**Do:** Run `writing-metrics` on all Track C extracts; derive draft SD/TTR bands; document in note (not hardcoded magic numbers in code yet).
**Files:** `docs/notes/` calibration note, optionally `src/writing_audit/metrics.py`
**Done when:** Human corpus metrics table + proposed threshold ranges documented.

### TICKET-D2 — One-time calibration panel · TODO · depends-on: D1 · wave deferred · agent: fanout/claudex
**Do:** Cross-vendor panel validates Layer-1 vs human judgment (per STATUS outstanding TODO).
**Done when:** Panel note committed; decision on tell-lexicon replacement.

---

## Critical paths

**Skill ship path:** G0 → A1a → A1b → A2 → C1 → C2 → C3 → C4

**Audit path:** G0 → B0 → B0m → (B1*, B2-MS human, B3* parallel) → B4 staged (C→Q→B/P) + B2-FG → OQ2 → B5* → B6 → B7

**Open Q#2 path:** B2-MS + B2-FG → B4-MS-BP + B4-FG → OQ2 (independent of full three-concept audit completion)

**Parallel after G0:** Wave 1: A1a ∥ B0m ∥ B1-* ∥ B2-MS (human, non-blocking). B5 runs on B3 output without waiting on B4.
