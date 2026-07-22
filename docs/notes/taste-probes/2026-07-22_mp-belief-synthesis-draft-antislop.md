# Draft (anti-slop rewrite) — MP belief synthesis

**Mode:** same concept/outline as Kimi “before”; rewrite targets *AI tour-guide texture*, not Pangram.  
**Before:** `2026-07-22_mp-belief-synthesis-draft-kimi.md`  
**Concept:** `2026-07-22_mp-belief-synthesis-concept.md`

### What this pass tries to kill
- Parallel Paper-A / Paper-B tour
- Slogan pivots (“empirical foothold”, “policy-shock signature”, “Gradualism and communication follow”)
- “Empirically… Theoretically…” twin closing
- Even paragraph jobs

### Draft

On March 20, 2001 the FOMC cut the funds rate by more than markets expected—50 basis points—and the S&P 500 fell inside half an hour. Jarociński and Karadi (2020) put the share of FOMC announcements since 1990 with that same positive co-movement of rates and stocks at about one-third. A pure easing that cheapens equities is not what the tape showed.

The measurement problem is upstream of any VAR. In a narrow window around the announcement, three-month fed funds futures and the S&P 500 can move together or against each other. Textbook policy tightening raises rates and lowers stocks, because discount rates rise and expected dividends fall. When rates and stocks fall together after a tightening (or rise together after an easing), the surprise looks like policy. When they rise together after a tightening, something else is in the statement: news about the central bank’s outlook. Jarociński and Karadi turn that sign into an identifying restriction in a Bayesian SVAR. Once the information piece is stripped out, the remaining policy shock contracts output and tightens financial conditions more like a standard model object, and the price level falls more cleanly. Leave the information piece in the “policy” residual and nonneutrality estimates inherit the mix.

That mix is not only an econometric nuisance. Caballero and Simsek (2022) start from the fact that Greenbook paths and FOMC dots routinely disagree with market forwards, in part because the Fed and the market disagree about future activity. In their model the market anticipates Fed mistakes under that disagreement; current demand moves with that anticipation; the Fed finds it optimal to accommodate the market’s view in part and to push its own view only as beliefs update. An announcement that unexpectedly revises the Fed’s belief then looks, in markets, like a textbook policy shock. A tantrum is the same announcement misread: the market overreacts to what it thinks the Fed believes. Gradualism and communication are then not ornaments on a rule. They are how an optimizing Fed limits the damage from being misread, while disagreement itself tilts market expected inflation and leaves a cost-push-like trade-off on the table.

So the high-frequency surprise is not a clean instrument for “the” monetary policy shock. It is a rate move bundled with a belief revision—either the Fed’s private assessment of demand (Jarociński–Karadi) or the wedge between Fed and market demand views (Caballero–Simsek). Use the bundle as if it were pure policy and you mismeasure nonneutrality; ignore the wedge and you misread why an optimizing Fed still moves slowly and talks carefully.

The note stops at that joint reading. It does not re-estimate either paper or choose which belief channel dominates in a given sample.

*(~340 words — slightly long; cut candidate: the cost-push sentence if you want ≤320)*

### D5 — Verify before use
- [ ] March 20, 2001; >expected 50 bp cut; S&P fell within ~30 minutes — JK
- [ ] ~1/3 FOMC announcements since 1990 with positive rate–stock co-movement — JK
- [ ] Half-hour / narrow window; 3m FFF + S&P — JK
- [ ] Sign of co-movement separates policy vs information — JK
- [ ] Bayesian SVAR; purged policy looks more textbook; clearer price decline; info shock raises rates with activity/prices — JK
- [ ] Ignoring info content biases nonneutrality — JK
- [ ] Greenbook / dots vs forwards; activity disagreement — CS
- [ ] Anticipate mistakes → partial accommodation → gradual implementation — CS
- [ ] Fed-belief surprise ≈ MP shock; tantrum = misread/overreact — CS
- [ ] Gradualism/communication as response to tantrum risk; cost-push-like trade-off — CS
- [ ] No euro-area “almost half” claim
- [ ] P2: no *to our knowledge* / soft *at least*

### Author ask
Does this still read as slop? If yes, mark the worst 2–3 sentences. If better, say whether the remaining AI tell is rhythm, vocabulary, or the two-paper sandwich itself.
