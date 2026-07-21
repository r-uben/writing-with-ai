# Status

**Last updated:** 2026-07-21 (prose-moves taste graph; AI control coded)

## Stage

Branch `setup/initial-structure`. Not pushed, not deployed. This session pivoted the taste work:
instead of writing Track B blind from the outline, we built a **prose-moves graph** from *real*
published econ intros to calibrate taste against attested human prose. Track B blind write is
**paused/superseded** for now (and, if resumed, was reclassified human+AI — see graph note). The
Pangram audit and skill-ship threads below are unchanged and still live.

## Live thread — prose-moves taste graph (2026-07-21)

Home: `docs/notes/taste-probes/prose-moves-graph.md` (+ `.json` data, `.png` figure via
`uv run prose-graph-viz`). What happened, in order:

1. Mined 3 real intros (Morris–Shin theory / Fama–French empirical-AP / Nakamura–Steinsson
   empirical-macro); named 10 moves; found one degree-3 spine (`incumbent→defect→our-fix`).
2. 3-vendor panel (gpt-sol / grok-4.5 / kimi-k3) hit one triangulated flaw: **selection-on-success
   — degree measures genre compliance, not taste, with no negative control.** ≈ Swales CARS (1990).
   Reframed the graph as an **audit / anti-move critic, not a drafting template**.
3. WP→published control design **empirically dead** in this library: NS, Bauer–Pflueger–Sunderam,
   Hansen–McMahon–Prat all have publication-grade intros already at WP stage (elite authors).
4. Filled the control on the **human-vs-AI axis**: all **3/3** AI Morris–Shin drafts reproduce the
   spine + genre moves but miss `enumerated-gaps` and `rhetorical-question-pivot`. → **high degree ≠
   taste; the candidate discriminators sit in the degree-1 tail.**

**Open tension (do not act until corroborated + reviewed by a non-generating model):** `SKILL.md`
bans the big-question / rhetorical-question opener — yet the rhetorical-question pivot is one of the
few human-only moves. The skill may be suppressing a taste signal.

**Next actions for this thread (pick):**
- Test the discriminator on FF/NS content (not just MS) before generalizing.
- Weak-human axis still empty (graph placeholder) — needs external SSRN / lower-tier pull.
- Reconcile the SKILL.md big-question ban against the finding (needs independent reviewer).
- Provisional un-graphed moves + pre-registered control rule are recorded in the graph note.

## Where things live

| What | Where |
|---|---|
| **Volatile TODO / next action** | this file (`STATUS.md`) |
| **Prose-moves taste graph** | `docs/notes/taste-probes/prose-moves-graph.{md,json,png}` |
| **Graph renderer** | `src/writing_audit/prose_graph_viz.py` (`uv run prose-graph-viz`) |
| **AI taste probe (NOT Track B)** | `docs/notes/taste-probes/` |
| **Plan ticket graph** | `docs/plans/2026-07-19_writing-skill-pangram-audit/TICKETS.md` |
| **Blind panel logs** | `docs/plans/.../logs/panel-{ns,ms,ff}.md` |
| **Experiment fixtures** | `docs/notes/pangram-audit/fixtures/` |

## Outstanding TODOs

**Taste (this session's thread)** — see "Live thread" above.

**Author (pre-existing; still open)**
- [ ] Taste picks Q3–Q5 (+ accept/revise draft P3–P5) — now informed by the graph, not just the AI probe
- [ ] Skim C1-F1–F3 (`docs/plans/.../logs/review-draft-mode.md`)

**Pangram audit (quota-gated; 2026-07-19: 4/4 spent on off-protocol MS probes — results in `docs/notes/2026-07-19_dual-track-pangram-audit.md` §Results)**
- [ ] Author: attest what the two AI-flagged "Multiple-equilibrium models" variants were, and origin of the "We argue that" paraphrase
- [ ] Score Track C first when quota resets (NS + FF; MS-C final ¶ already Human 0.0025 high-conf)
- [ ] Score Q, P, B cells
- [ ] Audit synthesis + Open Q#2 verdict

**Skill ship path**
- [ ] Wire taste (A2) after picks
- [ ] Apply C1 fixes (C2)
- [ ] E2E draft → deploy proposal (approval required)

## Next action

**Taste thread:** corroborate the human-vs-AI discriminator on FF/NS content, then decide whether to
reconcile the SKILL.md big-question ban. **Author:** taste picks Q3–Q5 remain the downstream blocker.
**Pangram:** score Track C when quota resets.
