# Worked example — consolidated `/writing` anti-slop + P7

**Purpose:** show what the single skill does on a real flagged paragraph.  
**Source before:** `2026-07-22_mp-belief-synthesis-draft-antislop.md` ¶2–3  
**Not a Pangram exercise.**

## Detect (as D4(i) / Review would flag)

| Quote | Rule | Fix in a few words |
|---|---|---|
| “The measurement problem is upstream of any VAR.” | **P7** | Drop *upstream*; name the identifying problem |
| “not what the tape showed” | **P7** | Drop *tape*; state the co-movement fact |
| “the surprise looks like policy” | **P7** | Say: used to isolate a monetary policy shock |
| “something else is in the statement” | **P7** / soft | Name outlook / assessment news |
| “more like a standard model object” | **P7** | “closer to a textbook monetary shock” |
| “That mix is not only an econometric nuisance.” | **P7** + binary setup | Cut the rhetorical turn; start Caballero–Simsek |
| “from the theory side” / “from the other direction” | **P7** | Drop tour-guide bridge; state the CS setup |
| bare “market forwards” | **P7** | “policy path priced in futures” (or name the instrument) |
| Stack of short punch lines in ¶1–2 | **slop** / S2 / P1 | Vary clause length; keep at most one pivot short |

Skipped (not our craft): re-introducing “I think / maybe”; detector score.

## Before (excerpt)

> A pure easing that cheapens equities is not what the tape showed.
>
> The measurement problem is upstream of any VAR. … When rates and stocks fall together after a tightening (or rise together after an easing), the surprise looks like policy. When they rise together after a tightening, something else is in the statement: news about the central bank’s outlook. … Once the information piece is stripped out, the remaining policy shock contracts output and tightens financial conditions more like a standard model object, and the price level falls more cleanly.
>
> That mix is not only an econometric nuisance. Caballero and Simsek (2022) start from…

## After (same claims, skill rewrite)

On March 20, 2001, the FOMC cut the federal funds rate by a larger-than-expected 50 basis points, and within thirty minutes the S&P 500 declined. Jarociński and Karadi (2020) report that about one-third of FOMC announcements since 1990 exhibit the same positive co-movement between interest rates and stock prices. That pattern is hard to square with a pure instrument surprise.

High-frequency identification around FOMC releases uses the co-movement of three-month fed funds futures and the S&P 500 in a half-hour window. Under a broad class of models, a policy tightening that is not accompanied by other news raises rates and lowers equity values, because discount rates rise and expected dividends fall. Negative co-movement of rates and stocks in that window is therefore used to isolate a monetary policy shock; positive co-movement is used to isolate a central-bank information shock—news about the central bank’s assessment of the outlook rather than about the stance alone. Jarociński and Karadi impose those sign restrictions in a Bayesian SVAR. After the information component is removed, the remaining policy shock produces contractions in output and tighter financial conditions, and a clearer decline in the price level, closer to what standard monetary models predict. If the information component is left inside a single “policy surprise,” estimates of nonneutrality inherit both shocks.

Caballero and Simsek (2022) start from Fed–market disagreement about future activity. Greenbook assumptions and FOMC dots often diverge from the policy path priced in futures, in part for that reason. In their model, that disagreement leads the market to anticipate policy the Fed would regard as mistaken; current demand responds to that anticipation; and the Fed optimally accommodates the market’s view in part while implementing its own view only as beliefs update. An announcement that unexpectedly revises the Fed’s belief then moves markets much as a conventional policy shock would. When the market instead misreads the Fed’s belief and overreacts, the same announcement becomes a tantrum. Gradualism and communication limit exposure to those misreadings.

## What changed

- Removed P7 metaphors (*tape*, *upstream*, *looks like policy*, *standard model object*, *econometric nuisance*).
- Replaced vague “something else” with *assessment of the outlook*.
- Dropped tour-guide bridges (*theory side* / *other direction*); replaced bare *market forwards* with *policy path priced in futures*.
- Broke metronome; kept one short opener fact, then longer mechanism sentences.
- Dropped binary “not only a nuisance” bridge; entered Caballero–Simsek directly.

Pangram may still read ~100% AI on fully machine-generated cells — expected under the dual-track audit; this pass is taste/register, not detector evasion.

Full-file sibling of this after-state: `2026-07-22_mp-belief-synthesis-draft-v3.md`.
