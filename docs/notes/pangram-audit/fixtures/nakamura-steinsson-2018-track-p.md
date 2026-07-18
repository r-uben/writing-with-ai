## Draft: Track P output

**Source:** /Users/rubenffuertes/repos/skills/writing-with-ai/docs/notes/pangram-audit/fixtures/nakamura-steinsson-2018-track-q.md
**Run:** /Users/rubenffuertes/repos/skills/writing-with-ai/docs/notes/pangram-audit/runs/nakamura-steinsson-2018-track-q-20260719-005102
**Rounds:** 1

### Draft

Rate changes rarely come from nowhere. The Fed cuts when a financial shock unfolds, and tightens when inflation runs hot. Control for output and prices in a VAR and the endogeneity still survives: the policy move stays entangled with the disturbance. The problem is confounding, not a shortage of controls.

The high-frequency fix is narrow but sharp. Around each scheduled FOMC announcement, take a 30-minute window and measure the unexpected rate change inside it. Anything public beforehand already sits in prices; anything that moves during the window is news about policy. Monthly VARs miss this, which is how September 2001 can register as a monetary shock when it was in fact a terror shock. Identification comes clean. The catch is size. These shocks carry a standard deviation of about 5 basis points, so any power to trace output quarters ahead is gone. The inference is carried instead by contemporaneous objects — Treasury forwards, TIPS-implied real rates, survey expectations.

Those objects still move, and move hard. In the authors' scaling, a 100 bp policy-news shock raises the two-year real yield by roughly 106 basis points at impact; two-year nominal forwards crest near 114 basis points, then fade at longer horizons as break-even inflation adjusts. Markets price monetary shocks as if they bend real rates for years, not minutes. Some of that short-run response is an information effect: because the announcement also reveals how the Fed reads the economy, the rate move is signal as much as stance. Over long horizons the real effect goes to zero, as theory demands. In the short run, it just doesn't.

### Pangram (manual)
- [ ] Score: ___% AI / ___% Human (version ___)

### Notes
- Record each Pangram check in run.log
