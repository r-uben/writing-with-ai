# Status

**Last updated:** 2026-07-24 (Renamed skill invoke from `/writing` → `/no-ai-slop`)

## Stage

Branch `cursor/rename-skill-no-ai-slop-860f`. Skill renamed in repo (`name: no-ai-slop`).
**Cloud env synced** to `~/.config/ai-skills/no-ai-slop/SKILL.md` (symlink
`~/.claude/skills/no-ai-slop`); byte-identical (sha256 `fc5b08e9…`). Your local Claude
machine still needs the same sync + removal of leftover `writing` install dirs.

**Ultimate goal:** AI draft/revise in economist/academic register for real paper work.

## Live thread — taste + skill (MAIN LINE)

- **P1–P5 confirmed** in `docs/notes/taste-profile.md`; encoded in `skill/SKILL.md`.
- **P6 (enumerated-gaps) REJECTED** — author cares about epistemic hedges, not longer First/Second lists.
- **P2 tightened (2026-07-22):** ban *to our knowledge* / *as far as we know* / *to the best of our
  knowledge* / soft *at least…*; keep numeric lower bounds (*at least 3%*). D3 + D4(h) in repo skill.
- **Anti-slop constraints added (2026-07-23):** Ban explicit novelty claims (S10), require substantive signposting (S14), strip non-quantitative adjectives for noun-driven prose, and enforce a strict contrast "Scope Fence" for limitations.
- **Rename (2026-07-24):** skill invoke `/writing` → `/no-ai-slop` (frontmatter `name`, docs, deploy paths).
- Taste graph / FF–NS probes remain useful as audit evidence; not a drafting recipe.

## Parked

- Q2 individual-vs-collective pilot; idea-graph is archive only.
- S8 / rhetorical-question-pivot change (still frozen).

## Next action

On the machine where Claude loads skills:
1. Sync `skill/SKILL.md` → `~/.config/ai-skills/no-ai-slop/SKILL.md`
2. Symlink `~/.claude/skills/no-ai-slop` → that dir; remove old `writing` install paths
3. Smoke-test `/no-ai-slop --draft` on `examples/ff-concept.md` or `examples/ns-concept.md`
   (hedges, novelty bans, scope fences)
