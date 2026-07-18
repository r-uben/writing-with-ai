# Morris–Shin taste probe — full AI option

**Date:** 2026-07-19  
**Status:** AI proposal for author comparison — **not Track B**  
**Concept:** morris-shin-1998 (unique equilibrium in currency attacks)  
**Paper:** Morris & Shin (1998, AER) — library `1998__morris_shin__unique_equilibrium_self_fulfilling_currency_attacks__AER`  
**Constraints applied:** taste P1/P2 + anti-slop levers; no detector-chase  
**Vendors:** gpt-sol, grok, ollama-deepseek

---

## Primary probe (recommended for tomorrow’s compare)

**Selected:** grok — strongest timing open (ERM ripe-before-attack), scarce pivots, mechanism line that compresses higher-order beliefs without restating MS verbatim, no Theorem-2 formula risk.

### Draft

Self-fulfilling models of currency attack show how beliefs can force a peg: when a continuum of speculators sells against e*, the government abandons the parity and the sale is vindicated; when they hold, the peg stands and holding is vindicated. What they leave open is timing and policy. The ERM looked ripe well before September 1992, and Mexico before its collapse; at any earlier date, coordinated selling would have forced the authorities off the parity. After the fact, every path looks rational. Timing is unexplained.

The repair is not denser fundamentals but thinner common knowledge. Give each speculator a private noisy signal of θ ∈ [0,1]. Then every participant can see that the economy is sound without knowing that every other participant sees the same thing — and without knowing that others know that others see it. Coordination turns on that hierarchy of beliefs, not on θ alone.

Under noisy private signals the game admits a unique cutoff θ*: attack below it, hold above it. The mass of hot money and the transaction cost t > 0 shift that threshold; sand in the wheels, as in Eichengreen et al. (1995), moves θ*.

Multiple equilibria left intervention silent. A unique cutoff makes onset and policy analysable, and monetary-policy transparency matters because it rewrites beliefs about beliefs, not merely the first-order forecast of fundamentals.

### Taste moves
- P1 pivots: “Timing is unexplained.” / “Multiple equilibria left intervention silent.”
- Mechanism: higher-order beliefs chain (see draft ¶2)
- ~222 words

### Verify before use
- [ ] Continuum / e* / t>0 / θ∈[0,1] — Morris & Shin (1998) model
- [ ] ERM ripe before Sept 1992; Mexico analogous — MS intro (cites Eichengreen & Wyplosz 1993)
- [ ] Unique θ*; hot money + transaction costs — MS
- [ ] Sand-in-the-wheels — Eichengreen et al. (1995) as framed in MS
- [ ] Transparency via higher-order beliefs — MS

---

## Vendor variants

### gpt-sol (~224 words)

Multiple-equilibrium models of currency attacks explain self-fulfillment, but they do not explain timing or policy: when attack and restraint are both equilibria, either outcome can be rationalized after the fact. The model accommodates the event without selecting it. This is policy silence.

Morris and Shin instead give a continuum of speculators noisy private signals of fundamentals θ∈[0,1] before they decide whether to attack the peg e*, at cost t>0. The remedy is poorer common knowledge, not richer fundamentals. Everyone can know the peg is sound without knowing that everyone knows it is sound; private noise breaks the higher-order chain that coordinates an attack.

The break selects a unique cutoff θ*: speculators attack below it and hold above it. As noise vanishes, θ* solves f(θ*)=e*−2t, pinning down the boundary left free under complete information. Its location depends on the mass of hot money and transaction costs, making capital mobility and “sand in the wheels” determinants of attack incentives (Eichengreen et al. 1995).

Multiplicity cannot explain why the ERM collapsed in September 1992 rather than when conditions appeared ripe earlier (Eichengreen and Wyplosz 1993); Mexico presents the same timing problem. A unique cutoff makes timing and intervention analysable because policy can move the boundary. Transparency also matters through higher-order beliefs: public information changes what speculators expect others to do, not merely what each believes about fundamentals.

**Note:** Uses Theorem 2 limit `f(θ*)=e*−2t` — verify against paper before any use outside this probe.

### ollama-deepseek (~218 words)

Multiple-equilibrium models of currency attacks capture self-fulfillment: a continuum of speculators, facing peg e* and attack cost t>0, can force abandonment when they sell and spare the parity when they hold, with fundamentals θ∈[0,1] common knowledge throughout. They cannot pin down timing or evaluate intervention. By the accounts in Eichengreen and Wyplosz (1993), the ERM was ripe well before September 1992, and Mexico sat in a similar window before its collapse; any date inside those intervals can be rationalized after the fact.

The fix is poorer common knowledge, not richer fundamentals. Hand each speculator a private noisy signal of θ. Sound fundamentals can be known to all without being known to be known — and without being known to be known to be known. Coordination then turns on beliefs about others' beliefs, not on θ alone.

That structure selects a unique cutoff θ*: attack below it, hold above it. The mass of hot money and the transaction cost t enter as comparative statics on θ*. Sand in the wheels, in the sense of Eichengreen et al. (1995), moves the threshold.

Multiple equilibria were policy silence. Unique θ* makes onset and intervention analysable: transparency of monetary policy matters because it rearranges higher-order beliefs, not merely the first-order forecast of θ.

---

## Paper-lookup notes (for your B write — outline refresh only)

From MS intro (OCR; Track C is the cleaner extract):

- Self-fulfilling beliefs leave timing unexplained: ERM/Mexico “ripe” for long windows before the actual attack.
- Multiplicity also blocks policy analysis (e.g. sand-in-the-wheels).
- Mechanism: imperfect private signals → failure of common knowledge → unique critical state θ*.
- Signature line (human original): “everyone may know that the fundamentals are sound, but it may not be that everyone knows that everyone knows this.”
- Transparency matters because of higher-order beliefs, not just first-order information volume.

**Do not open Track Q/P or this probe while writing Track B.** Use `fixtures/morris-shin-1998.md` outline only.

---

## Comparison worksheet (fill tomorrow)

| Dimension | Your B | Primary AI (grok) | Prefer |
|-----------|--------|-------------------|--------|
| Opening | | ERM ripe / timing unexplained | |
| Mechanism compression | | higher-order beliefs chain | |
| Pivot short-declaratives | | Timing is unexplained / Multiple equilibria left intervention silent | |
| Policy close | | transparency via beliefs about beliefs | |
| Overall register | | | |

Notes:
