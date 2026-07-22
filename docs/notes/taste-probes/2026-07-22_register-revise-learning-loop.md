# Learning loop — register revise + secondary Pangram note (2026-07-22)

## Correction (load-bearing)

The revised CS opener is **AI-generated text** (machine rewrite of machine prose; no human
tokens in the scored paragraph). Pangram called it *moderately AI assisted*.

That means we **moved Pangram’s class** while origin stayed machine-written — a detector
soft-label / boundary fact. It is **not** “provenance matched the score,” and it is **not**
a reason to tune `/writing` for Pangram.

| Cell type | Tokens in the window | Honest origin | Pangram (this run) |
|---|---|---|---|
| Full AI draft | model | AI-generated | 100% AI (earlier) |
| AI revise of AI (this case) | model | AI-generated | said “assisted” ← softer than origin |
| Human seed → AI revise | mix | AI-assisted (honest) | TBD — fair craft test |

## What to improve for next time

1. **Tag origin separately from Pangram.** Origin = who wrote the tokens. Pangram = what
   the detector said. Never equate them after a rewrite pass.
2. **Primary success = author taste** (P1–P5, P7). Log kills; fold into P7 if they recur.
3. **Pangram is secondary characterization only.** If a taste pass moves the label on still-
   machine text, log it as boundary evidence — do **not** change the skill to reproduce it.
4. **Prefer human seed next** so “AI assisted” can be *true* of the cell, not a detector
   under-call on pure AI text.
5. **Multi-case, same protocol** so one CS paragraph does not overfit P7 or the detector.

## Skill deltas already taken (taste only)

Author kills → **P7** / D3–D4(i): *upstream*, *tape*, “looks like policy,” *econometric
nuisance*, *standard model object*, tour-guide bridges, bare *market forwards*.

Next kills → `2026-07-22_author-antislop-hits.md`, then P7 if they recur. **No Pangram
levers in the skill.**

## Multi-case plan

| # | Case | Seed | Pass | Taste (author) | Origin | Pangram (optional) |
|---|---|---|---|---|---|---|
| 1 | MP / CS opener (done) | AI draft | P7 revise | better; residue remains | AI-generated | said “assisted” (under-call) |
| 2 | **Human seed** (priority) | author paste | `/writing` | TBD | hybrid | TBD |
| 3 | FF ¶ | human or AI | `/writing` | TBD | tag | TBD |
| 4 | NS ¶ | human or AI | `/writing` | TBD | tag | TBD |
| 5 | Other two-paper synthesis | outline or human | `/writing` | TBD | tag | TBD |

### Log template

```
## Case: [name] — [date]
- Origin (tokens): AI-generated | hybrid human+AI | human-only
- Pangram (optional): label= ; vs origin: match | softer | harder
- Seed / pass:
- Author taste kills:
- Skill update (taste only)?: Y/N
- Next:
```

## Non-goals

- Do not treat “not AI generated” / “assisted” as a shipping criterion when tokens are AI.
- Do not reopen detector-evasion as skill work; Track R stays research-only if revisited.
