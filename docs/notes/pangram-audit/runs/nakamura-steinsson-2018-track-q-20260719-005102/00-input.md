## Draft: Nakamura & Steinsson (2018) — HF identification + information effect

### Outline (confirmed)
1. Most interest-rate changes are endogenous; VAR controls leave residual bias.
2. HF window around FOMC fixes confounding; 9/11-type misattribution drops out.
3. Clean ID, weak power: 5 bp shocks → contemporaneous finance, not output IRFs.
4. Real rates move at short horizons; part of that is Fed information revelation.

### Draft

Most changes in interest rates happen for a reason. The Fed cuts because a financial shock is unfolding; it tightens because inflation is running hot. VARs that "control for" output and prices still inherit endogeneity — the policy move and the disturbance are entangled. The identification problem is confounding, not a shortage of controls.

The high-frequency fix is narrow but sharp. Measure unexpected rate changes in a 30-minute window around scheduled FOMC announcements. Everything public before the window is already in prices; what moves inside it is news about policy. That is why monthly VARs can misread September 2001 as a monetary shock when it was a terror shock. Clean identification. Small shocks — standard deviation about 5 basis points — so power against output quarters ahead is gone. Contemporaneous objects carry the inference: Treasury forwards, TIPS-implied real rates, survey expectations.

Those objects still move a lot. In the authors' scaling, a 100 bp policy-news shock raises the two-year real yield by roughly 106 basis points at impact; two-year nominal forwards peak near 114 basis points and fade at longer horizons as break-even inflation adjusts. Markets act as if monetary shocks move real rates for years, not minutes. Part of that short-run response is an information effect: the announcement also reveals the Fed's read of the economy, so the rate move is signal as well as stance. Long-run real effects go to zero, as theory demands. Short-run effects do not.

### Verify before use
- [ ] 30-minute FOMC window — Nakamura & Steinsson (2018)
- [ ] Shock SD ≈ 5 bp — same
- [ ] 2y real yield +106 bp, 2y nominal forward ~114 bp — same, Table I scaling
- [ ] 9/11 VAR misattribution — Cochrane & Piazzesi (2002), cited in NS
- [ ] Information-effect interpretation — NS model section

### Independent review
Pending (run via `agy` when scoring Track Q in full audit).
