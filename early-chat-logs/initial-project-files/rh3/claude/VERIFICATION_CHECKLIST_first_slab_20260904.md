# Verification checklist — *Archimedean first-slab positivity for shifted zeta canonical systems*

**For:** the author, and any collaborator asked to verify part of this manuscript
**Manuscript:** WORKING_DRAFT_first_slab_positivity, 3 September 2026
**Prepared:** 4 September 2026

---

## How to use this

The manuscript is a computer-assisted result prepared with substantial
language-model assistance. It has been through two adversarial review rounds and
one clean-room reimplementation, and no error survives in the main proof chain.
What it has **not** had is a human who has derived the central steps on paper and
will stand behind them. That is what this checklist is for.

Items are grouped by who can do them, not by where they appear in the paper. Each
says what to check, why it carries weight, what a failure would look like, and
roughly how long it takes. **Part 0 should be done before the manuscript is
archived anywhere**, because a deposit freezes what it contains.

### Already checked — please don't redo this

An independent third implementation (neither the primary Arb code nor the
clean-room audit) reproduced the following from the definitions printed in the
manuscript. Treat these as corroborated and spend your time elsewhere.

- All algebraic identities in §§2.2, 3.1, 3.3, 4.1, 6.1, 6.2, 10.2, 10.4.
- The explicit impulse of §3.2: its Laplace transform matches `K_ω(p)` to 1.5e−17
  at ω = 1/2 and 8.3e−11 at ω = 0.3.
- Proposition 4.1 as a *statement*: the multiplier identity holds to 30 digits at
  ω = 0.1 and 0.3. (The *proof* still needs a human — see A1.)
- The endpoint lemma of §4.2: the corrected formula agrees with `Q₀ + C_{1/2}` to
  ~1e−9 for two test functions, where the pre-correction formula was off by
  0.2402.
- §6.3: `t₀`, the closed form for `h`, the `N(q)` sign analysis, `t_m`, `h(t_m)`,
  `h(log2 − t₀)`, and `∫₀^{log2}|h| = 0.012293050401142319559`.
- §7.1's Schur loss: `(0.012294 + κ)²/1.5176929819194765` reproduces both reported
  values to 17 digits.
- §7.2's certified margins: an independent 16-mode Legendre reconstruction gives
  head minima and margins consistent with the reported values to within the
  expected interval-widening penalty (2.26e−5 even, 8.65e−6 odd — unchanged across
  both certificate revisions).
- The Taylor remainder `1.532967865231399e−12` from the Investigation 12 §6
  formula.
- Investigation 14's sample `T₁` entries, to 13 digits.
- All reference metadata, including that [5] is X. Zhu on v2, not the v1 author.

### Known non-issues — already chased, nothing there

- The `(−i)ⁿ` vs `iⁿ` phase in §5.2 affects no computed quantity (same-parity
  blocks only).
- The primary-vs-audit margin discrepancy (~1.6e−8) is explained and the
  arithmetic is self-consistent.
- The former factor-2 in the Schur bound was conservatism, not a `Q = B/2`
  normalization leak; doubling the perturbation would make the certificate fail,
  and it does not fail.

---

## Part 0 — Fix before archiving *(author, one hour)*

| # | Item | Where |
|---|---|---|
| 0.1 | Investigation 12 §4 still contains the **old** derivation of Prop 4.1 ("with the usual common local renormalization"). The rewritten, correct proof exists only in the manuscript. Replace it, or omit Investigation 12 from the deposit. | Inv 12 §4 |
| 0.2 | Investigation 12 §8.4 says the calculation "is not yet independently implemented… pending audit", contradicting its own §12 ledger and §13. | Inv 12 §8.4 |
| 0.3 | State that the certified Weyl–Schur margin is a valid (non-sharp) lower bound for the form on all of `D_log` — the tail block is ⪰ 1.5177 ≫ m, so the block-Schur construction gives `Q ⪰ m·I`. §8.6 consumes it that way; Inv 12 §1 and §8.4 currently read as denying it. | manuscript §8.6 / Inv 12 §1 |
| 0.4 | Pin the word "equivalent" in §1.1 to the exact statement in [1,2]. §1.1 elsewhere allows "permitted meromorphic poles", and this sentence now carries the paper's significance claim. | manuscript §1.1 |
| 0.5 | Investigation 14 §9's ledger row "Kernel norm bound — passed" overstates what was audited: §7 says the endpoint-row-maximum *argument* is inherited from Investigation 12 and only the scalar integral was recomputed. Say so. | Inv 14 §7, §9 |
| 0.6 | Insert the missing line in §6.3's case split: `a ≤ t₀` cannot occur, since `a ≥ L/2 = 0.3466 > t₀ = 0.2812`. | manuscript §6.3 |

---

## Part A — Self-checkable *(no specialist background; half a day each)*

These are elementary. Do them in this order; A1 is the one that matters most.

### A1. Proposition 4.1 — the bounded-kernel decomposition *(§4.3)*

**Claim.** `Q_{ω,L} = Q_{0,L} + C_{ω,L}` with kernel
`c_ω(x,y) = (cosh(ω|x−y|) − 1)·R(|x−y|)`.

**Why it carries weight.** This is the paper's central structural identity.
Everything downstream — the certificate, the endpoint safety, the common form
domain, the entire-in-ω² expansion — rests on it. It is also the step whose first
written proof was wrong in method (not in conclusion).

**Check, in four steps.**

1. The digamma representation
   `½ψ((p+c)/2) = −γ/2 + ∫₀^∞ (e^{−2t} − e^{−(p+c)t})/(1−e^{−2t}) dt`,
   obtained from `ψ(z) = −γ + ∫₀^∞ (e^{−u} − e^{−zu})/(1−e^{−u}) du` by `u = 2t`.
2. **The crux.** Form the combination `c = α, β` minus twice `c = 1/2` *before*
   splitting the integral. Both the `−γ/2` constants and the `e^{−2t}` terms
   cancel. This matters because each `e^{−2t}` piece diverges logarithmically at
   `t = 0` on its own — there is no `L¹` kernel for `Q₀`, only a multiplier, and
   the old proof separated them anyway. Confirm the surviving integrand is
   `−2e^{−pt}·e^{−t/2}(cosh ωt − 1)/(1−e^{−2t})` and is integrable at zero.
3. The four rational terms independently: `cosh αt + cosh βt = 2cosh(t/2)cosh ωt`,
   giving `4cosh(t/2)(cosh ωt − 1)`.
4. The bridge identity
   `2cosh(t/2) − e^{−t/2}/(1−e^{−2t}) = e^{t/2} − e^{−5t/2}/(1−e^{−2t}) = R(t)`,
   then the `½` from `Q = (A + A*)/2` turning the factor 2 into 1 in the kernel.

**Failure would look like:** a surviving constant (a multiple of the identity),
or a factor of 2 in the kernel. Either would change every entry of every `T_k`.

**Also check** the endpoint extension in the last sentence of the proof — uniform
convergence of `c_ω` on the compact square `I_L²` as `ω ↑ 1/2` — since Theorem B's
range is closed at 1/2.

### A2. The endpoint lemma *(§4.2)*

**Claim.** At ω = 1/2, with the pointwise-limit multiplier, the coefficient of
`|C₀(f)|² = |∫f|²` is `1/2`, not `1`.

**Check.** `½Re ψ((α+iτ)/2) ≈ −α/(α²+τ²)` as `α ↓ 0`, and `∫α/(α²+τ²)dτ = π`, so
the limit carries `−πδ₀`. Then confirm the bookkeeping: `(1/2π)·(−π)|f̂(0)|² =
−½|∫f|²`, and `f̂(0) = C₀(f)`.

**Why it carries weight.** The uncorrected version of this display overstated the
form by ½|∫f|² ≈ 0.24 for `f = 1` at `L = log2`, against a certified margin of
6.1e−4. The certificate never used it, but the paper states it as a theorem.

**Effort:** an hour.

### A3. The row-maximum argument *(§6.3)*

**Claim.** `‖C_{ω,L}‖ ≤ ∫₀^{log2}|h(t)|dt < 0.012294`, via the absolute row
integral being maximal at an endpoint row.

**Check.** The closed form `h(t) = (q−1)(q⁶−q²−1)/(2q²(q+1)(q²+1))` with
`q = e^{t/2}`; that `sign(dh/dt) = sign(N(q))`; that the stated grouping gives
`N'(q) > 0` for `q ≥ 1`; that `N(1) < 0` and `N(√ρ) = 3ρ² − 1 > 0`; then the case
split on `b ≥ t₀` vs `b ≤ t₀` — **and insert item 0.6**, which the draft omits.

**Why it carries weight.** This argument is what replaced a factor-2-conservative
bound and roughly doubled the certified margin. It is also single-sourced: the
clean-room audit inherited it rather than re-deriving it.

**Effort:** half a day, elementary calculus throughout.

### A4. The Volterra reduction *(§2.2)* — good warm-up

Four identities: `H = VR = RV*`, `RVR = V*`, `H² = VV*`, `‖H‖ = ‖V‖`. Each is a
change of variables. Confirming these grounds the translation between the centered
interval `I_L` and the causal coordinates `(0,L)`, which is where a convention slip
would hide. **Effort:** an hour or two.

---

## Part B — Needs a functional analyst *(§8; several days)*

Section 8 converts generator positivity into strict contractivity. It is the least
computationally checkable part of the paper and the part with the most asserted
estimates. In order of concern:

**B1. §8.1 — that `s ↦ V_{s,L}` is C¹ in operator norm.** The multiplier bounds
are stated in `O(·)` with no constants and no proof. This is the weakest-supported
claim in the manuscript. What is needed: explicit uniform Stirling estimates on
`Re p = η`, then that the difference quotients converge in the multiplier norm.

**B2. §8.1 — the weighted-to-unweighted transfer.** `V' = −AV` is adjoint-free so
it transfers between `L²(ℝ₊, e^{−2ηt}dt)` and unweighted `L²(0,L)`; confirm that
norm-differentiability transfers too (equivalent norms on a finite interval), and
that every adjoint from §8.4 on is unweighted. The draft now asserts this; it
should be argued.

**B3. §8.3 — `V_sL² ⊂ D_log`, and the closure step.** "By closure from the smooth
core, `Q_{s,L}[V_{s,L}f] = Re⟨A_{s,L}V_{s,L}f, V_{s,L}f⟩`" is one clause doing
real work: `A_{s,L}` is unbounded, and the identity is between a closed form and an
operator pairing.

**B4. §8.5 — the improper strong-operator integral.** That the monotone strong
limit exists and equals `D_{ω,L}`, given `D_{ε,L} → 0` strongly.

**B5. §8.6 — strictness.** Now clean (measurability, not continuity). Confirm the
uniform coercivity constant is legitimately `c_* = 6.116350109501e−4` on all of
`D_log` — see item 0.3.

**What failure would look like:** B1–B4 failing would not make the theorem false,
but would leave Theorem C unproved, which would leave Theorem A resting only on
the older Mosco/direct-transfer route described in §11.

---

## Part C — Needs an analytic number theorist *(highest risk)*

**C1. The Suzuki normalization chain.** *Nobody has done this.* Verify
`k_ω(t) = Σ_n c_ω(n)n^{−1/2}κ_ω(t − log n)`, the transfer
`K_ω(p) = Γ_∞(½+p−ω)/Γ_∞(½+p+ω)`, and the translated first-slab convention
directly against Suzuki [1,2], not against the project's restatements of them. A
factor or a shift here moves the log-2 threshold and with it the entire
identification of the first slab. **This is the single highest-risk unverified item
in the paper.** Suzuki himself is the natural person to ask.

**C2. Novelty boundary.** For `L ≤ log 2` no prime term enters the explicit
formula, so `Q_{0,L}` is the full Weil functional on that window — i.e. the ω = 0
case of Theorem B reproduces a classical result. The manuscript now says this
(§5.3). What remains is a genuine originality search for (a) the off-center kernel
identity of Prop 4.1 and (b) the shift-radial energy identity, against [4], [5],
[12], [13] and anything newer. Three closely related papers appeared in this niche
within two months; the neighborhood is active.

**C3. §1.1's equivalence claim** — see item 0.4.

---

## Part D — Needs the repository, not a pencil

**D1. The inherited Investigation 7 central certificate.** Both the primary and the
clean-room audit take as given: the Binet bound `w₀(τ) ≥ β*` for `|τ| ≥ 30`, and
the spherical-Bessel Legendre-tail majorants (couplings `1.4084884e−9` /
`2.2191643e−10`, deviations `9.78e−24` / `2.43e−25`). This is the least-audited
load-bearing component in the stack, and the one place a shared upstream assumption
could propagate into both implementations undetected. `β*` itself is arithmetically
safe by a wide margin (the asymptotic error is `O(1/τ²)` against a `1/30`
allowance); the tail majorants are the part to re-derive.

**D2. The interval LDL and box construction.** Neither reviewer read this code.

**D3. Full primary-vs-audit row diff.** §12.1 item 5 asks for it; only summary
minima have been compared. The two runs differ in the 8th digit for reasons that
took a paragraph to explain — the complete diff either closes that or exposes
something.

**D4. Version-pinned rerun of both implementations** in clean environments, with
archived logs and manifests.

---

## Optional strengthening, not verification

- **Certify the positivity horizon.** The crossings `L*_odd ≈ 0.7429`,
  `L*_even ≈ 0.8199`, `ω*_even ≈ 0.8611` are floating Galerkin diagnostics. §12.3's
  entire revised research plan now rests on them. Promoting them to interval
  certificates is cheap with the existing machinery and would convert the paper's
  most interesting structural fact from a caveat into a result.
- **Extend the box sweep to ω ≈ 0.85.** Since `dD/ds = 2V*Q_sV`, certifying
  `Q_s ⪰ 0` on `[1/2, ω]` gives `D_ω ⪰ D_{1/2} ≻ 0` and hence strict contractivity
  with no Paley–Wiener argument — which is exactly the step §9.3 declines to take.
  Available up to ω ≈ 0.861 and no further.
- **Double the box count** to 512. The box radius (2.42e−5) is now the
  second-largest erosion of the even margin after the Schur loss (9.96e−5).
