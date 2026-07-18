# Status

**Last updated:** 2026-07-19

## Stage

Research documented; draft mode built and refined from the blind anti-slop panel (D3/D4 updated same day). Skill not yet independently reviewed, not yet run on a real user concept.

## Live drafts

- `skill/SKILL.md` — two modes: Review (existing) + Draft (`--draft`); D3/D4 refined per panel findings.
- `docs/notes/2026-07-18_ai-writing-quality-and-detectors.md` — research findings + design decisions.
- `docs/notes/2026-07-18_anti-slop-harness-panel.md` — blind cross-vendor harness experiment (7 drafts, 4 judges) + the seven draft fixtures.
- `docs/notes/2026-07-18_prose-exemplar-ratings.md` — 12 field writers rated on the rubric (3 parallel readers); top-4 levers wired into D3/D4 as TICL contrast.
- `docs/notes/taste-profile.md` — elicited taste database (one judgment at a time); aspirational taste, not native voice.
- `docs/notes/2026-07-19_dual-track-pangram-audit.md` — planned Q vs P harness comparison (quality vs Pangram objective) to audit the detector; Track P research-only.
- `docs/notes/pangram-audit/` — three-concept parallel build (macro empirics, macro theory, finance); Track Q drafts + fixtures ready; Track P via `uv run track-p`.
- `src/writing_audit/` + `pyproject.toml` — Python research harnesses (`writing-metrics`, `track-p`).
- `docs/plans/2026-07-19_writing-skill-pangram-audit/` — dependency-gated plan (TICKETS.md + STATUS.md).

## Recent decisions

- Voice-cloning the author is currently blocked: the JMP (only single-authored paper in the library) is substantially AI-assisted per the author, so it is not a clean voice corpus, and no pre-2022 clean writing exists in the library. Pivoted to (a) good-authority *contrast* exemplars and (b) an elicited *taste* database — both clean signal. This captures aspirational taste, not native voice; kept honest as "write toward what I admire," not "write like me."
- Exemplar rating (2026-07-18): 12 genre-matched field writers rated on the rubric. Top-4 positive levers (Cochrane, Morris & Shin, Nakamura & Steinsson, Gürkaynak–Sack–Swanson) wired into D3; a fourth D4 pass added (declarative-then-justify). Key finding: even 9/10 human writers emit the "AI tells" (stock openers, connector scaffolding) — re-confirms tells = register, not origin, from the good-writer side.
- Objective: AI drafts prose from a human-supplied idea/concept; human owns the argument and vouches for the facts. Detectors (Pangram) are a quality proxy, not a target — not evasion.
- "Effort-based ownership" rejected as a design constraint (psychological, not required). Kept: factual accountability = one verify pass, per the no-invention charter rule.
- Detectors key on style fingerprints, not perplexity. Tells are register/style (flowery verbs, low sentence-length variance, high formality), not content — so fixing them is a quality gain.
- The real style-transfer lever is TICL-style contrast (show the anti-pattern + why), not more few-shot examples.
- Evaluation architecture: Layer 1 deterministic linguistic metrics (thresholds from a human corpus, not hardcoded) → Layer 2 one independent judge. Drafting model never judges its own draft (charter).
- Big 4–5 model calibration panel is a one-time research step (`/fanout`/`/claudex`), not a per-draft tax.
- Anti-slop panel (2026-07-18, blind, 4 cross-vendor judges): generation-time constraints beat the unconstrained baseline decisively; ticl and anti-tell tied at the top; the static tell-word lexicon has zero discriminating power (0 hits everywhere while judges found slop) — the real markers are stock academic phrases off any list. Sentence-length SD is a byproduct of the pivot short-declarative move, not a target. No same-vendor judge favoritism. D3/D4 updated accordingly.
- Dual-track Pangram audit (2026-07-19): run quality-optimized (Q) and Pangram-optimized (P) drafts on the same concept/outline, plus Variant B, and compare quality judges vs Pangram. Track P never ships into `skill/SKILL.md` — research audit only. Expanded to three library-sourced concepts (Nakamura–Steinsson, Morris–Shin, Fama–French). Full plan in the note + `docs/notes/pangram-audit/`.
- Tooling (2026-07-19): consolidated research harnesses to Python + uv. Entry points: `writing-metrics` (Layer-1 linguistics), `track-p` (Track P pipeline). Removed shell scripts.
- Plan (2026-07-19): `/plan create` → `docs/plans/2026-07-19_writing-skill-pangram-audit/`; three-reviewer advisory panel; second-pass patches applied (B2-FG, OQ2, B4 quota split, B0m). Next: `/plan next` → G0.

## Outstanding TODOs

- Independently review the Draft Mode section of `skill/SKILL.md` (including the 2026-07-18 D3/D4 refinements) before deploying.
- Test draft mode end-to-end on a real concept (generic academic voice).
- Run the calibration panel; derive Layer-1 metric thresholds from a human reference corpus — and find a better deterministic operationalization than the dead tell-lexicon.
- Decide when personal voice corpus gets wired in (currently generic academic only).
- Settle Open Q#2: can "minimal revision" and clearing the tells coexist?
- Run dual-track Pangram audit (Q vs P vs B vs C) on three concepts per `docs/notes/pangram-audit/` once quota resets; prioritize B over P if checks are scarce.
- Optional: unconfounded re-test of constraint-list transferability (same drafter, different lists) — grok/gpt underperformance is confounded with drafter identity.
- Operational: Kimi quota exhausted for this billing cycle (both kimi seats died in the panel run); exclude kimi agents until reset.

## Empirical results (2026-07-18, Pangram v3.3.2 live)

| Variant | Producer | Pangram |
|---|---|---|
| Original | AI, anti-tell draft (Gemini judge: "no tells") | 100% AI, high conf |
| A | AI, heavy restructure of same argument | 100% AI |
| D | AI, panel-winning ticl draft (slop-free per 4 blind judges) | 100% AI |
| C | Human (Andrade et al. AEJ 2019, same topic, ESL authors) | 100% Human |
| B | Human from-memory rewrite of AI draft | **untested** |

Perfect separation on origin, not register: surface anti-tell prompting does nothing; re-generation does nothing; even the panel-optimal slop-free draft reads 100% AI; human prose on the identical topic clears at 100%. AI-side optimization is exhausted — register quality and origin detection are fully decoupled (n=4). Full interpretation + caveats in the note. Pangram free quota: 0/4, resets daily.

## Next action

**Your turn:**
1. Commit staged files (`git commit -m "Initial scaffold"`) — agent commit blocked by hook
2. Pick taste Q3–Q5 in `docs/notes/taste-profile.md` (three minimal pairs waiting)
3. Morris & Shin from-memory rewrite in `morris-shin-1998-track-b.md` (read outline only)

**Agent next (Wave 2):** run detector-chase pipeline on three quality drafts once commit lands.
