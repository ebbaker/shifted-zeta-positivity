# Zero-Sphere Program — CLOSED

**Date closed:** 2026-08-23. **Decision:** the author's, on effort grounds after a
structural review. Nothing here is in progress. **A future session should not resume
this without an explicit instruction from the author** — several documents in this
project still read as though a publication pipeline is live. It is not.

---

## What was decided

The geometric program aimed at RH is closed. The author's own summary: *the idea
wasn't bad, it just doesn't work in the end* — good enough to have produced a
theorem, not good enough to continue, and outside his expertise to referee. Time
is going to quantum computing / quantum chemistry work instead.

## Why (findings from the 2026-08-23 review; see `memo4`–`memo8`)

Five results are closed in the strict sense — I would bet against anyone reviving them:

1. **Slice regularity contributes nothing.** Proved three independent ways: Theorem D
   (no linear functional separates), Theorem E (degree weights spheres by 2), and the
   project's own `appendix_extension_uniqueness.tex`, whose multiplicative-rigidity
   theorem shows the fiberwise triviality of the extension is *forced* by Frobenius —
   ℍ has no commutative subalgebra beyond a slice, so ℂ→ℍ cannot carry new information
   the way ℝ→ℂ does.
2. **The twistor lift's degeneracy is forced, not a modelling choice.** The zero divisor
   has isotropic class `mA` in `NS(Q)`, so Castelnuovo–Severi `D² ≤ 2d₁d₂` holds with
   *equality* — the divisor is the degenerate case Weil discards. And the appendix's
   incidence-rigidity theorem shows slice regular ⟺ `G = id` ⟺ product lift, so no
   choice of lift fixes it.
3. **The conjecture family is structurally contentless.** Conj 10.1 is RH-trivial
   (`S ≡ 0` verifies it); Conj 10.2 is RH-orthogonal. Root cause: RH is a *vanishing*
   statement, so statements about the defect being *computable* cannot have directional
   content.
4. **The Lorentzian / Hodge–Riemann bridge reduces exactly to the first Turán
   inequality** — already a theorem for Ξ (Csordas–Norfolk–Varga) and provably strictly
   weaker than hyperbolicity. Counterexample: `X⁴+10X³+26X²+22X+3`, Newton ratios
   `2.327, 1.366, 1.442`, one conjugate pair. (`lab_lorentzian_test.py`)
5. **The trace-form route is vacuous over ℝ and circular in the commutative case.**
   Signature is a complete invariant of a real quadratic form, so "realize it
   geometrically" asks for nothing; and for a commutative algebra with trivial
   involution, "trace form definite" *is* "totally real" — the conclusion. Weil's
   argument needs a non-commutative algebra and an element not fixed by the involution.
   (`lab_tower_check.py`, `memo6` §4)

   **Strengthened later the same day: the circularity survives the best noncommutative
   replacement.** ADHM data *is* genuinely noncommutative — 120/120 exact solutions of
   the ADHM equations with nonvanishing commutators at `k = 2, 3, 4`, plus an exact
   rational witness — so the objection in item 5 is not automatic, and ADHM was the one
   candidate in this program's orbit with the right algebraic shape (noncommutative,
   positive involution, positivity supplied structurally by `C = ΣT_a² + Re(λ†λ) ⪰ 0`).
   But requiring the bundle's **real jumping locus** to be the zero set of a slice
   extension forces `λ = 0` and `T₁ = T₂ = T₃ = 0` — the commutative real locus — after
   which hyperbolicity is just the spectral theorem for one real symmetric matrix.
   Proved (and the proof does not even use the nonlinear ADHM equations: the collapse is
   forced by the linear part of the reality condition), machine-certified at `k = 2` for
   symbolic monic `p`, and confirmed on 12 cases including a correct NO for item 4's
   counterexample. See `memo7_adhm_test.md`, `lab_adhm_check.py`.

   General lesson worth carrying: **matching-style dictionaries — those that identify an
   analytic object with a geometric one by equality of zero loci — have now failed for
   the same structural reason from three independent directions** (items 1, 2, and this).
   A surviving route would have to be a *transform* rather than a *matching*, in the
   sense in which the Fueter map is a transform rather than an extension.

   **And the obvious relaxation was tested too, with a sharper answer** (`memo8`,
   `lab_adhm_relax.py`). Weakening the four-dimensional matching to agreement on a single
   slice — "the object restricts to Ξ on a slice" — is *worse*, not better: it forces
   `λ = 0`, `T_a = e_a S`, `[T_0,S] = 0` (so the data is commutative and ℂ_e-valued) and
   is satisfiable for **every** real monic `p`, hyperbolic or not. Inside that family
   there is an exact deficit formula: with `t = ⟨Im q, e⟩` and `r = |Im q|`,
   `det M = Π_j (B_j − 2tσ_j)` against `P_p = Π_j (B_j − 2rσ_j)`, so `det M − P_p > 0`
   strictly off the slice whenever `S ≠ 0`, and **one slice plus one off-slice point
   already forces hyperbolicity**. Two consequences worth carrying:

   * *A cheap test for future proposals.* The entire discriminant is `r² − t²`, weighted
     by the imaginary parts of the roots. It is supported exactly on the 2-sphere
     directions transverse to any single slice, and a slice is precisely the equality
     locus of `t² ≤ r²`. So **if a proposed condition can be stated slice by slice, it
     carries no information about reality of zeros.** This is the fourth independent
     appearance of "the information lives in the transverse sphere directions" — the
     appendix's `−2B/r` trace term, the twistor note's σ-type of divisor components,
     `memo7` §6, and now this. Treat it as structural, not as four coincidences.
   * *No intermediate regime, and no uniformity.* Constraint and collapse are driven by
     the same quantity, so they switch on together; and the forcing degrades as `O(θ²)`
     in the angle between slices, so any approximate two-slice condition with tolerance
     `ε` admits non-hyperbolic `p` once `ε ≳ θ²`. Also recorded there: within the relaxed
     family "p hyperbolic" is exactly "`T₀ + iS` self-adjoint", i.e. the relaxation lands
     on the Hilbert–Pólya statement with no new input from the geometry.

Underlying all of it: **the missing ingredient is rationality, not finiteness.** Finite
rank is available for ζ; a ℚ-lattice is not, and the entries are moments of Riemann's
kernel. Geometry contributes nothing until an arithmetic object is *constructed*, which
is the central open problem of the Connes–Consani programme. Nothing in `memo7`–`memo8`
touches this: even had the ADHM test come out the other way, any ADHM data built from Ξ
has entries that are moments of Φ.

## What is NOT closed

**The operator / Hilbert–Pólya route via Connes–Consani–Moscovici.** It passes the
content test — their operators are built from *finite Euler products*, so arithmetic in,
zeros out — and it has a sharply posed open problem: the regularized determinants
appear numerically to converge to Ξ, nobody has proved it, and a proof would give RH.
See `Zeta Spectral Triples` (arXiv:2511.22755), `D_log operators` (arXiv:2601.12133),
Connes–Moscovici (PNAS 2022). Not pursued because it is crowded and expensive, not
because it is dead. Note the ℚ-structure obstruction above does *not* apply to it —
self-adjointness is a different mechanism with different inputs.

Caution if ever revisited: this is the most crank-saturated corner of RH (a 2026 search
returns mostly self-deposits and non-venues), and even the visible successes are
contested — Bender–Brody–Müller's PRL drew a published Comment from Bellissard.

## What is real, and where it is

Four artifacts, none depending on RH. **None has had human review; the author declined
to publish on the correct grounds that he cannot vouch for proofs he did not verify.**

| artifact | where | status |
|---|---|---|
| uniform oscillation lemma | `second_involution_resolution.tex` §, `zero_sphere_condensed.tex` §9 | **NOT NOVEL — see §"Novelty check" below.** Correct, but it is Landau (1912) with a smooth weight plus a folklore almost-periodicity argument. Do not circulate as a result. |
| quantifier-loophole diagnosis (existential quantifiers over continuum-valued parameters ranging after the instance are satisfiable by encoding) | same, Thm 9.1 | the most transferable output; a rediscovery of the uniform/non-uniform distinction |
| Lorentzian = first Turán reduction, with counterexamples | `memo5`, `lab_lorentzian_test.py` | **the one item the author could verify himself in an afternoon** |
| extension-uniqueness theorems (multiplicative rigidity, Vekua mismatch, incidence rigidity) | `appendix_extension_uniqueness.tex` | machine-verified identities; real audience in the slice-regular community |

The ADHM rigidity theorem of `memo7` §4 is a fifth self-contained statement with no
reference to RH, but it is **not** a candidate artifact until novelty-checked: it is a
rigidity result about determinantal representations of real polynomials by symmetric
pencils, and that circle (Lax conjecture, Helton–Vinnikov, ADHM regularity, Barth's
jumping lines) is heavily worked. Per the updated prior below, assume it is known.

A Zenodo deposit of the whole project — memos, lab code, drafts, historical manuscripts
— remains available as a *terminal* output with no read-through obligation, if the
author ever wants a citable, explicitly-unreviewed record. Recommended framing: a
per-artifact status line (claim / verified / not verified / provenance).

## Novelty check on the oscillation lemma (2026-08-23) — VERDICT: NOT NOVEL

Three independent literature sweeps, all agreeing. The lemma decomposes into two halves,
and both are known.

**Half 1 — frequency tuning to `log p` is Landau's theorem (1912).**
E. Landau, *Über die Nullstellen der Zetafunktion*, Math. Ann. **71** (1912), 548–564:
for fixed `X > 1`, `Σ_{0<γ≤T} X^ρ = −(T/2π)Λ(X) + O(log T)`. Landau himself wrote the
inverted prime-detection form, `Λ(t) = −(2π/T)√t Σ_{0<γ≤T} cos(γ log t) + O(log T/T)`.
**The `B₂ cos(c log 2)` term is the Landau resonance at `X = 2`**, with the sharp cutoff
replaced by a Gaussian. Uniform version: Gonek, *An explicit formula of Landau and its
applications*, Contemp. Math. **143** (1993), 395–413. Refinements: Fujii (1989, 1990);
Kaczorowski–Languasco–Perelli; Hughes–Pearce-Crump (2022); Durkan–Hughes–Pearce-Crump,
arXiv:2601.18025 (2026). Equidistribution form with an explicit density that vanishes
unless the frequency is `(a log p)/2πq`, plus a discrepancy lower bound: Ford–Zaharescu,
J. reine angew. Math. **579** (2005); Ford–Soundararajan–Zaharescu, Math. Ann. **343**
(2009).

**Closest single paper — and it is very close.** Balanzario, Cárdenas Romero, Chacón
Serna, *A smooth version of Landau's explicit formula*, arXiv:2311.04347 (2023): a smooth
(asymptotically Gaussian) window tuned to `log p`, single-prime recovery, *and* a
Heisenberg-uncertainty lower bound on the required window width. This is the smoothed,
localized Landau formula with the time-frequency analysis already done.

**Half 2 — the oscillation argument is folklore.** Not a named result and apparently not
written down as a lemma anywhere (Bohr I–III, Besicovitch, Jessen–Tornehave,
Levitan–Zhikov, Corduneanu all checked), but three lines from century-old machinery:
Bochner compactness of the hull + analyticity of hull elements + the identity theorem +
continuity of `osc` for the sup norm. Two simplifications a specialist would impose:
minimality of the hull makes the `B₂`-coefficient step **redundant**, and the statement
should be made for a general nonconstant a.p. holomorphic function on a strip, with no
Dirichlet series and no arithmetic. Modern one-sentence route: Bohr lift to `T^∞` plus
Kronecker (`{log p}` is ℚ-independent) plus "continuous positive function on a compact
group attains its minimum."

**One genuine point of content, worth recording.** The naive elementary proof — "almost
periods move any window into `[0, L]`, and `osc` is continuous and positive there" — is
**circular**: `L = L(ε)` grows as `ε → 0`, so the minimum over `[0, L(ε)]` degrades to
exactly the infimum being bounded. Compactness of the *hull* is doing real work. Also:
the statement is FALSE without analyticity (a continuous periodic function can be
constant on an interval without being constant).

**Two errors found in our own work.**
1. **The slogan "the Gaussian in frequency selects `n = 2`" is false at σ = 1**, and so is
   the phrase "the prime-2 term is never drowned," which appears in memos 4–6 and is *my*
   formulation, not the paper's. Recomputing: `B₃ ≈ 0.5677 > B₂ = 0.5407`, and
   `Σ_{n≠2} B_n ≈ 2`, roughly 4× `B₂`. At σ = 1 the frequency window width `1/σ = 1`
   exceeds `log 3 − log 2 = 0.4055`, so it selects nothing. The *proof* survives (it needs
   only `B₂ > 0` and frequency separation, which is what the `C₁` bound supplies), but the
   narrative around it is wrong, and frequency separation forces `a₀ ≳ 2π/0.4055 ≈ 15.5`
   — so `a₀ = 43.98` is lossy by a factor of ~2.8.
2. **σ = 1 is the worst possible choice for the mechanism.** At σ ≥ 5–6 the selection
   becomes real (`e^{−σ²(log 3 − log 2)²/2} ≈ 0.05` at σ = 6), `B₂` grows `∝ σ`, and the
   archimedean drift nearly vanishes (`≈ 0.63 log(c/2π)` at σ = 1 versus `~10⁻³ log c` at
   σ = 6), which would remove the need for the threshold `C₃` entirely.

**And the objection a referee would raise first: the observable is RH-blind.** `F` is
unconditionally computable from primes and the identity `F = A + E + P` holds whether or
not RH is true. An off-line zero `β + iγ'` enters with weight multiplied by
`e^{(β−1/2)²/2σ²} ≤ e^{1/8σ²}` — an `O(1)` perturbation that violates no oscillation
lower bound. So no contradiction is extractable and the lemma is inert for RH,
independently of novelty.

**Consequence.** There is no paper here. The correct output would be a two-line note:
*this is Landau's 1912 formula with a smooth weight, plus the standard fact that a
nonconstant almost periodic holomorphic function is not locally constant.* Nothing to
circulate.

**Updated prior on the other three artifacts.** One of four was checked and came back
known; that should lower confidence in the rest. In particular the appendix's
multiplicative-rigidity theorem (§Thm A) is plausibly also standard in the slice-regular
literature — it is Frobenius plus a character argument — and has **not** been novelty
checked. Do not treat any of these as new without a sweep of the same kind. The same
applies to the `memo7` §4 ADHM rigidity theorem and to everything in `memo8` (elementary
statements about commuting real symmetric pairs and Cauchy–Schwarz; the deficit formula
is the kind of thing that falls out of standard axial-monogenic/Vekua computations).

## Correction recorded for the record

`zero_sphere_condensed.tex` §8 and `second_involution_intro.tex` state
`ι_R : ρ ↦ ρ̄ (γ ↦ γ̄)`. In the rotated variable this should be **`γ ↦ −γ̄`**. As
printed, "the two involutions agree" reads `−γ = γ̄`, i.e. γ purely imaginary — the
opposite of RH. Harmless downstream (the group generated is the same), but it is in the
central slogan of both documents. Left unfixed since neither will be circulated.
