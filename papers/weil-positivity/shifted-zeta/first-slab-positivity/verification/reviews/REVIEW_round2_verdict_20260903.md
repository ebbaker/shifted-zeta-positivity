# Second-round referee note — response of 3 September 2026

**Verdict: all ten items resolved.** Every correction was re-verified by independent
recomputation, not accepted on assertion. Four small items remain, none affecting
Theorems A–C.

## Verified corrections

| Item (round 1) | Status | Independent check |
|---|---|---|
| §4.2 false at ω = 1/2 | **fixed, correct** | The new endpoint lemma (coefficient ½ on \|C₀(f)\|², i.e. −πδ₀ in the multiplier) now agrees with `Q₀ + C_{1/2}` to ~1e−9 (my quadrature floor) for `f = 1` and `f = 1+3x²`. The old formula was off by 0.240226507. Correctly propagated to §7.3, §12.1(2), Appendix C, and Inv 12 §3. |
| Schur factor of 2 | **fixed, and better than asked** | They proved the endpoint-row maximum rather than substituting a number. I verified the whole chain: `h(t) = (q−1)(q⁶−q²−1)/(2q²(q+1)(q²+1))` exact; `sign(dh/dt) = sign(N(q))` at five points; `N'(q)` grouping valid for q ≥ 1; `N(1) = −2`; `N(√ρ) = 4.264632999 = 3ρ²−1` exactly; `t_m = 0.14164548119438862`, `h(t_m) = −0.0044442714714076919`, `h(log2−t₀) = 0.012614663855624526`, sum `= 0.00817039238` > 0.00817039; `∫₀^{log2}\|h\| = 0.012293050401142319559`. The case `a ≤ t₀` cannot occur (`a ≥ L/2 = 0.3466 > t₀ = 0.2812`), so the argument is complete. |
| New Schur loss / margins | **reproduced to 17 digits** | `(0.012294 + κ)²/1.5176929819194765` gives `9.9586986585890301e−5` (even) and `9.9586967362349123e−5` (odd) — both draft values exactly. New margins: my floating prediction `7.33830e−4 − 9.9587e−5 = 6.3424e−4` vs certified `6.11635e−4`; the `2.26e−5` gap is *identical* to the gap in the previous run, i.e. pure box widening, unchanged. Inv 14 §8 confirms: radius row norm `2.42495e−5`, and `midpoint − radius − Schur loss − Taylor remainder = 6.116514637e−4` exactly. |
| Taylor remainder provenance | **fixed** | The Inv 12 §6 formula reproduces `1.532967865231399e−12` exactly in my recomputation. Text now correctly calls it a conservative absolute-profile Cauchy bound. |
| Positivity horizon / §12.3 | **accepted, correctly rewritten** | Crossings recorded as floating Galerkin diagnostics, not theorems; second-slab logic inverted as required. Declining the ω ∈ [1/2, 0.85] extension is a defensible judgment call, stated. |
| Prop 4.1 proof | **fixed** | Difference now formed before splitting. Every step checks: the `−2e^{−pt}e^{−t/2}(cosh ωt − 1)/(1−e^{−2t})` integrand, the `4cosh(t/2)(cosh ωt − 1)` rational kernel, and `2cosh(t/2) − e^{−t/2}/(1−e^{−2t}) = R(t)`. Endpoint by uniform convergence on the compact square. |
| §8 gaps (4) | **all fixed** | Adjoint-free identity + unweighted adjoints stated; continuity claim replaced by the measurability argument; uniform `c_*` stated; compression expanded to a full paragraph. |
| δ_central | **fixed** | `9.7777e−24` / `2.4269e−25` now stated; `β_* − 0.012294 = 1.5176929819194765585` matches the displayed tail bound. |
| Primary vs audit margins | **explained, arithmetic verified** | Δmidpoint `−1.57e−9`, Δradius `−1.80e−8` ⇒ `+1.645e−8`, which is the actual margin difference. Odd sector likewise. The wider central radius (≤ 8e−9 over a row) is swamped by the row radius (2.42e−5), so the explanation is quantitatively coherent. |
| Row counts | **fixed** | 724 = 6+1+1+202+2+512; 783 = 2+1+1+24+5+36+202+512; 1360 = 10 × 136. All add up. |
| Fourier phase | **fixed** to `(−i)ⁿ`. |
| Framing / [5] conflict | **resolved correctly** | `L = 2L_Z`; primes enter when `log n < 2L_Z`; [5] at `L_Z = 0.8` is prime-active. Matches my own analysis. Metadata update to X. Zhu with the revised title is correct (v2 verified). |
| References | **fixed** | All 13 now cited in the body. [9] Osterwalder–Schrader, [10] Graham–Zworski, [11] DLMF now used; Mikkola and Belishev–Vakulenko removed with the triangular-factor section. [12] (T. Kim et al.) and [13] (A. Groskin) metadata verified correct against arXiv. |
| Minors | plastic number, tautology, §1.4, ledger — all done. |

Spot checks of the audit: `T₁^even(0,0) = 0.010270060106310` and
`T₁^odd(0,0) = −0.027105108731948` reproduce Inv 14 §5 to 13 digits. The Inv 14
formulas in §5 and §6 are algebraically equivalent to my own reduction.

## Four items left

1. **Inv 12 §8.4 carries a stale sentence.** "The calculation is reproducible but is
   not yet independently implemented… project-internal computer-assisted theorem
   pending audit." This contradicts its own §12 ledger ("Arb-certified and
   independently audited") and §13 ("Investigation 14 has independently
   reconstructed…"). Delete or rewrite.

2. **Say that the certified margin is a valid lower bound for the whole form.**
   Inv 12 §1 and §8.4 say the margins "are margins in the block-Schur proof, not
   asserted sharp spectral gaps of the full operator", while the manuscript's §8.6
   now consumes `c_* = 6.116350109501e−4` as a coercivity constant on all of
   `D_log`. Both are right — the block-Schur construction does give `Q ⪰ m·I`
   because the tail block is `⪰ 1.5177 ≫ m` — but the two wordings read as a
   contradiction, and Theorem C's strictness now leans on the stronger reading.
   One sentence fixes it.
   *(v1.0 note: the exact block-Schur condition gives `c = m − κ²m/(d(d−m))`, i.e.
   ~4e−8 below `m`; the preprint states `c_* = 6.1159e−4` — Lemma 7.1.)*

3. **Pin the "equivalent" in §1.1.** "For 0 < ω < 1/2, meromorphic innerness is
   equivalent to the open quasi-RH assertion that ξ has no zero in Re s > 1/2+ω."
   The pole-side implication is immediate, but §1.1 two paragraphs earlier allows
   "permitted meromorphic poles", so the equivalence should be tied to the exact
   statement in [1,2] rather than asserted. This sentence is now load-bearing for
   the paper's significance claim.

4. **Optional.** With the Schur loss at `9.96e−5`, the box radius `2.42e−5` is now
   the second-largest erosion of the even margin. Doubling to 512 boxes would
   roughly halve it. Not needed for anything.

## Effect of the revision

Even-sector certified margin: `3.0965e−4 → 6.1164e−4` (essentially the doubling
predicted). Odd: `5.2315e−2 → 5.2617e−2`. Of the `7.35e−4` head eigenvalue at the
weakest box, erosion is now `9.96e−5` (Schur) + `2.42e−5` (box) = 17%, against 55%
for the Schur loss alone before. The certificate is materially more robust than it
was, and every headline constant in it has now been reproduced from the definitions
by a second, unrelated implementation.
