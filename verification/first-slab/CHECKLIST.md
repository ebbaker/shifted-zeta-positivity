# Verification checklist — *Archimedean first-slab positivity for shifted zeta canonical systems*

**For:** anyone willing to verify part of the manuscript
**Manuscript:** `papers/first-slab-positivity/first_slab_positivity.pdf`, preprint v1.0 (5 Sept 2026)
**Current status:** `papers/first-slab-positivity/VERIFICATION_STATUS.md`
**Prepared:** 4 Sept 2026 for the working draft; renumbered to the preprint 5 Sept 2026

---

## How to use this

The manuscript is a computer-assisted result prepared with substantial
language-model assistance. It has been through two adversarial review rounds
and one clean-room reimplementation, and no error survives in the main proof
chain. What it has **not** had is a human who has derived the central steps on
paper and will stand behind them. That is what this checklist is for.

Items are grouped by who can do them. Each says what to check, why it carries
weight, what a failure would look like, and roughly how long it takes.

### Already checked — please don't redo this

Two recomputations independent of the primary Arb code and of the clean-room
audit reproduced the following from the definitions printed in the manuscript.
Treat these as corroborated.

- All algebraic identities in §§2.2, 3.1, 3.3, 4.1, 6.1, 6.2, 10.2, 10.4.
- The explicit impulse of §3.2, eq. (3.6): its Laplace transform matches `K_ω(p)` (3.3) to 1.5e−17 at ω = 1/2 and ~1e−10 at ω = 0.3 (quadrature-limited).
- Proposition 4.2 as a statement (multiplier identity to 30 digits at ω = 0.1, 0.3, 1/2) and every step of its proof (see A1).
- Lemma 4.1 (endpoint): corrected formula agrees with `Q₀ + C_{1/2}` to ~1e−8 for test functions; the uncorrected pointwise-limit formula is off by 0.2402.
- §6.3: `t₀`, the closed form for `h`, the `N(q)` sign analysis, `t_m`, `h(t_m)`, `h(log2 − t₀)`, `∫₀^{log2}|h| = 0.012293050401142319559`, and `L/2 > t₀`.
- §7.1: `β* = 1.5299869819194765…`, `d_tail = 1.5176929819194764…`, both Schur losses `κ²/d_tail` to 17 digits.
- §7.2: head minima and margins by an independent 16-mode Legendre reconstruction, consistent to the interval-widening penalty (2.26e−5 even, 8.65e−6 odd).
- The Taylor remainder `1.532967865231399e−12`.
- Lemma 7.1 constants (Remark 7.2): `c_even = 6.11594…e−4`, `c_odd = 5.26131…e−2`.
- Investigation 14 sample `T₁` entries to 13 digits; all row counts (724, 783, 1360).
- All reference metadata, including that [5] is X. Zhu on v2.
- Against automated readings of Suzuki [1]: `γ(s) = Γ_∞(s)`; the Mellin formula for `g_ω` (Sect. 3.1 of [1]) is (3.3) at `s = p + ½`; the layer formula (2.5) is [1, eq. (2.3)]; Prop. 2.1 of [1] is consistent with the Dirichlet series of `c_ω`. **Human confirmation against the PDF is still wanted — see C1.**

### Known non-issues — already chased, nothing there

- The `(−i)ⁿ` phase in §5.2 affects no computed quantity (same-parity blocks only).
- The primary-vs-audit margin discrepancy (~1.6e−8) is explained (§7.6) and the arithmetic is self-consistent.
- The former factor 2 in the kernel bound was conservatism, not a `Q = B/2` normalization leak; doubling the perturbation would make the certificate fail, and it does not.
- The checklist's original wording of item 0.3 ("the block-Schur construction gives `Q ⪰ m·I`") was slightly wrong: the exact condition is `(λ_head − c)(d_tail − c) ≥ κ²`, so the coercivity constant is `c = m − κ²m/(d(d−m))`, ~4e−8 below `m`. The preprint states `c_* = 6.1159e−4` and proves it in Lemma 7.1.

---

## Part 0 — Fix before archiving *(done in v1.0)*

| # | Item | Resolution |
|---|---|---|
| 0.1 | Investigation 12 §4 contains the old derivation of Prop 4.2. | Not in the deposit (preprint only). Fix before any code/write-up release. |
| 0.2 | Investigation 12 §8.4 stale "not yet independently implemented" sentence. | Same. |
| 0.3 | State that the certified margin gives a lower bound for the form on all of `D_log`. | Done, with the correction above: Lemma 7.1, Remark 7.2, §8.6. |
| 0.4 | Pin "equivalent" in §1.1 to the exact statement in [1]. | Done: [1, Prop. 1.2], [1, Thm. 2.2], [1, Lemma 4.1] quoted; single-shift "equivalence" removed. §9.3 rewritten around [1, Lemma 4.4]. |
| 0.5 | Investigation 14 §9 ledger overstates the kernel-norm audit. | Not in the deposit. The preprint says so explicitly (end of §7.6). |
| 0.6 | Insert the missing line in the §6.3 case split (`a ≤ t₀` cannot occur). | Done (Lemma 6.1). |

---

## Part A — Self-checkable *(no specialist background; half a day each)*

Do them in this order; A1 is the one that matters most.

### A1. Proposition 4.2 — the bounded-kernel decomposition *(§4.3)*

**Claim.** `Q_{ω,L} = Q_{0,L} + C_{ω,L}` with kernel `c_ω(x,y) = (cosh(ω|x−y|) − 1)·R(|x−y|)`, `R(t) = e^{t/2} − e^{−5t/2}/(1−e^{−2t})`.

**Why it carries weight.** Everything downstream — the certificate, the endpoint safety, the common form domain, the entire-in-ω² expansion — rests on it. It is also the step whose first written proof was wrong in method (not in conclusion).

**Check, in four steps.**
1. `½ψ((p+c)/2) = −γ/2 + ∫₀^∞ (e^{−2t} − e^{−(p+c)t})/(1−e^{−2t}) dt`, from `ψ(z) = −γ + ∫₀^∞ (e^{−u} − e^{−zu})/(1−e^{−u}) du` with `u = 2t`.
2. **The crux.** Form `c = α, β` minus twice `c = ½` *before* splitting the integral. Both the `−γ/2` constants and the `e^{−2t}` terms cancel; each `e^{−2t}` piece alone diverges logarithmically at `t = 0` (there is no `L¹` kernel for `Q₀`, only a multiplier). Confirm the surviving integrand is `−2e^{−pt}e^{−t/2}(cosh ωt − 1)/(1−e^{−2t})`, integrable at zero.
3. The four rational terms: `cosh αt + cosh βt = 2cosh(t/2)cosh ωt`, giving `4cosh(t/2)(cosh ωt − 1)`.
4. `2cosh(t/2) − e^{−t/2}/(1−e^{−2t}) = e^{t/2} − e^{−5t/2}/(1−e^{−2t}) = R(t)`, then the `½` from `Q = (A + A*)/2` turns the factor 2 into 1.

**Failure would look like:** a surviving constant (a multiple of the identity) or a factor of 2 in the kernel. Either would change every entry of every `T_k`.

**Also check** the endpoint extension (last sentence of the proof): uniform convergence of `c_ω` on `I_L²` as `ω ↑ ½`, since Theorem B's range is closed at ½.

### A2. Lemma 4.1 — the endpoint lemma *(§4.2)*

**Claim.** At ω = ½, with the pointwise-limit multiplier, the coefficient of `|C₀(f)|² = |∫f|²` is `½`, not `1`.

**Check.** `½Re ψ((α+iτ)/2) ≈ −α/(α²+τ²)` as `α ↓ 0`, `∫α/(α²+τ²)dτ = π`, so the limit carries `−πδ₀`; then `(1/2π)(−π)|f̂(0)|² = −½|∫f|²` and `f̂(0) = C₀(f)`; the residue terms `|C_α|² − |S_α|²` tend to `|C₀|²`, total coefficient `½`.

**Why it carries weight.** The uncorrected display overstated the form by `½|∫f|² ≈ 0.24` for `f = 1` at `L = log 2`, against a certified margin of 6.1e−4. The certificate never used it, but the paper states it as a lemma. **Effort:** an hour.

### A3. Lemma 6.1 — the row-maximum argument *(§6.3)*

**Claim.** `‖C_{ω,L}‖ ≤ ∫₀^{log2}|h(t)|dt < 0.012294`, via the absolute row integral being maximal at an endpoint row.

**Check.** `h(t) = (q−1)(q⁶−q²−1)/(2q²(q+1)(q²+1))`, `q = e^{t/2}`; `sign(dh/dt) = sign(N(q))`; the stated grouping gives `N'(q) > 0` for `q ≥ 1`; `N(1) = −2 < 0`, `N(√ρ) = 3ρ² − 1 > 0`; the case split on `b ≥ t₀` vs `b ≤ t₀`, including the line `a ≥ L/2 = 0.3466 > t₀ = 0.2812`; uniformity in ω and L (last sentence).

**Why it carries weight.** This argument replaced a factor-2-conservative bound and roughly doubled the certified margin. It is single-sourced: the clean-room audit inherited the argument and recomputed only the scalar integral. **Effort:** half a day, elementary calculus.

### A4. The Volterra reduction *(§2.2, eq. (2.10))* — good warm-up

Four identities: `H = VR = RV*`, `RVR = V*`, `H² = VV*`, `‖H‖ = ‖V‖`. Each is a change of variables. They ground the translation between the centered interval `I_L` and the causal coordinates `(0,L)`, which is where a convention slip would hide. **Effort:** an hour or two.

### A5. Lemma 7.1 — block-Schur coercivity *(§7.3)* — new in v1.0

Check the 2×2 positivity condition and the sufficient choice `δ = κ²m/(d(d−m))` in the proof; confirm the numerical constants of Remark 7.2 from the data of §7.2 (`κ = 0.012294 + κ_central`, `d_tail`, `m`). **Effort:** an hour.

---

## Part B — Needs a functional analyst *(§8; several days)*

Section 8 converts generator positivity into strict contractivity. It is the least computationally checkable part of the paper and the part with the most asserted estimates. In order of concern:

**B1. §8.1 — `s ↦ V_{s,L}` is `C¹` in operator norm.** The multiplier bounds are stated in `O(·)` with no constants and no proof. This is the weakest-supported claim in the manuscript. Needed: explicit uniform Stirling estimates on `Re p = η`, then that the difference quotients converge in the multiplier norm.

**B2. §8.1 — the weighted-to-unweighted transfer.** `V' = −AV` is adjoint-free so it transfers between `L²(ℝ₊, e^{−2ηt}dt)` and unweighted `L²(0,L)`; confirm that norm-differentiability transfers too, and that every adjoint from §8.4 on is unweighted.

**B3. §8.3 — `V_sL² ⊂ D_log`, and the closure step (8.7).** One clause doing real work: `A_{s,L}` is unbounded, and the identity is between a closed form and an operator pairing.

**B4. §8.5 — the improper strong-operator integral.** That the monotone strong limit exists and equals `D_{ω,L}`, given `D_{ε,L} → 0` strongly.

**B5. §8.6 — strictness.** Measurability argument; uniform coercivity constant `c_* = 6.1159e−4` on all of `D_log` via Lemma 7.1.

**What failure would look like:** B1–B4 failing would not make the theorem false, but would leave Theorem C unproved, which would leave Theorem A resting only on the older Mosco/direct-transfer route described in §11.

---

## Part C — Needs an analytic number theorist *(highest risk)*

**C1. The Suzuki normalization chain.** Verify `k_ω(t) = Σ_n c_ω(n)n^{−1/2}κ_ω(t − log n)` (2.5), the transfer `K_ω(p) = Γ_∞(½+p−ω)/Γ_∞(½+p+ω)` (3.3), the identification `H_{ω,a} = P_aH_ωP_a ↔ L = 2 log a` (§2.2), and the hypotheses of [1, Lemma 4.4] as cited in §9.3 — directly against the PDF of Suzuki [1], not against this project's restatements. The comparisons made so far used automated readings of the paper (two independent extractions agreed). A factor or a shift here moves the log 2 threshold and with it the entire identification of the first slab. **This is the single highest-risk unverified item.** Suzuki himself is the natural person to ask.

**C2. Novelty boundary.** For `L ≤ log 2` no prime term enters the explicit formula, so `Q_{0,L}` is the full Weil functional on that window — the ω = 0 case of Theorem B reproduces a classical result, as §5.3 says. What remains is an originality search for (a) the off-center kernel identity of Prop. 4.2 and (b) the shift-radial energy identity, against [4], [5], [12], [13] and anything newer. Three closely related papers appeared in this niche within two months; the neighborhood is active.

**C3. §1.1's equivalence statement** as rewritten, and the §9.3 claim that [1, Lemma 4.4] covers strict contractivity for `ω > ½` at every `a > 1`.

---

## Part D — Needs the repository, not a pencil

**D1. The inherited Investigation 7 central certificate.** Both the primary and the clean-room audit take as given: the Binet bound `w₀(τ) ≥ β*` for `|τ| ≥ 30`, and the spherical-Bessel Legendre-tail majorants (couplings `1.4084884e−9` / `2.2191643e−10`, deviations `9.78e−24` / `2.43e−25`). This is the least-audited load-bearing component in the stack, and the one place a shared upstream assumption could propagate into both implementations undetected. `β*` itself is arithmetically safe by a wide margin; the tail majorants are the part to re-derive.

**D2. The interval `LDLᵀ` and box construction.** Neither reviewer read this code.

**D3. Full primary-vs-audit row diff.** Only summary minima have been compared. The two runs differ in the 8th digit for reasons that took a paragraph to explain — the complete diff either closes that or exposes something.

**D4. Version-pinned rerun of both implementations** in clean environments, with archived logs and manifests.

**D5. Fix items 0.1, 0.2, 0.5** in the Investigation write-ups before releasing them.

---

## Optional strengthening, not verification

- **Certify the positivity horizon.** The crossings `L*_odd ≈ 0.7429`, `L*_even ≈ 0.8199`, `ω*_even ≈ 0.8611` are floating Galerkin diagnostics; §12.2's research plan rests on them. Promoting them to interval certificates is cheap with the existing machinery.
- **Extend the box sweep to ω ≈ 0.85.** Since `dD/ds = 2V*Q_sV`, certifying `Q_s ⪰ 0` on `[½, ω]` gives `D_ω ⪰ D_{1/2} ≻ 0`: an independent, Paley–Wiener-free proof of strict contractivity on the first slab in that range. Available up to ω ≈ 0.861 and no further.
- **Double the box count** to 512. The box radius (2.42e−5) is the second-largest erosion of the even margin after the Schur loss (9.96e−5).
