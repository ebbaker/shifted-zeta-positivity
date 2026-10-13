# Deep dive: the one-sided, elastic form of the shifted screw criterion

**2026-08-27.** Standalone expansion of "direction 2" (§10.5.2 / Corollary 10.7 of
`PAPER_psi_omega_margin.tex`). *Update, same day:* the L¹ strengthening of §2 below has since
been folded into the paper as Theorem `thm:L1` (with the mass-balance/Fejér–Siegel remark);
the rest of this note remains supplementary material. Everything below either carries a proof
sketch at the level of the paper's arguments or is explicitly flagged as heuristic. The main
outcomes of the dive:

1. a **complete exponent dictionary**: the one-sided decay exponents of a single `Ψ_ω` compute
   `Θ` exactly, in both directions, and the transport is *lossless* — feeding the classical bound
   in returns exactly the classical conclusion;
2. a genuine **strengthening of Corollary 10.7 from pointwise to L¹**: only the *time-averaged
   negative part* of `Ψ_ω` matters. In particular **RH ⟺ the negative part of Ψ is integrable on
   (0,∞)** — a form we have not seen stated anywhere;
3. a proof that the criterion is **rigid under positive smoothing** (nothing gained, nothing
   lost — so one may as well work with the smoothest member);
4. an **anatomy of how a violation manifests**: two-sided, mass-balanced, with excursion
   densities computed; the extremal "one-sided-looking" configurations are Fejér-kernel zero
   patterns, which for Dirichlet `L` are *realized* by Siegel shielding (Prop. 9.5(iii) of the
   paper) and for `ζ` are impossible at frequency zero — which is exactly why the L¹ form is the
   right topology;
5. an **inventory of sign-sensitive technology** and where each tool stalls, ending with the
   cleanest new analytic target ("Weil positivity with exponential defect") and a graded list of
   open problems.

Notation as in the paper: `ϑ = Θ − ½`, `Ψ_ω = ωA(ω)t + B(ω) + R_ω(t)`,
`|R_ω(t)| ≤ A*(ω)e^{(ϑ−ω)t}` unconditionally, and the Laplace transform
`∫₀^∞ Ψ_ω(t)e^{izt}dt = −z⁻²(ξ′/ξ)(½+ω−iz)`. Throughout, the *only* arithmetic fact the Landau
arguments use is: `ζ` has no real zeros in `(½, 1]`.

---

## 1. The exponent dictionary, and losslessness

For `0 ≤ ω < ½` define the one-sided exponents

> `e₋(ω) := inf{ ε ≥ 0 : ∃C, Ψ_ω(t) ≥ −Ce^{εt} for all large t }`,
> `e₊(ω) := inf{ ε ≥ 0 : ∃C, Ψ_ω(t) ≤ +Ce^{εt} for all large t }`.

**Theorem 1.** `e₋(ω) = e₊(ω) = max(ϑ − ω, 0)` for every `ω ∈ [0, ½)`. Consequently a single
evaluation determines `Θ`: if `e₋(ω) > 0` then `Θ = ½ + ω + e₋(ω)` exactly; if `e₋(ω) = 0` then
`Θ ≤ ½ + ω`.

*Proof.* Upper bounds: `Ψ_ω ≥ ωA t + B − A*e^{(ϑ−ω)t}` and `Ψ_ω ≤ ωA t + B + A*e^{(ϑ−ω)t}`
unconditionally (paper, proof of Thm 6.1), so `e_± ≤ (ϑ−ω)⁺` (when `ϑ ≤ ω` the bound is linear,
so every `ε > 0` works). Lower bounds: Theorem 6.1(ii) of the paper says that for `ω < ϑ` and
every `ε < ϑ−ω` both `liminf e^{−εt}Ψ_ω = −∞` and `limsup = +∞`; its proof works verbatim at
`ω = 0`. ∎

Three readings.

- **Losslessness.** The trivial input is `e₋ ≤ ½ − ω` (from `ϑ ≤ ½`, i.e. `Θ ≤ 1`, which is
  classical); the corollary's output at `ε = ½−ω` is `Θ ≤ 1` — the transport returns exactly what
  was fed in, with zero leakage. More generally, feeding in `Θ ≤ 1−δ′` gives the two-sided bound
  at rate `ϑ−ω ≤ ½−δ′−ω`, which fed back returns `Θ ≤ 1−δ′`. The reformulation is an *exact
  isomorphism of information at the level of exponents.* This is a feature and a proof of
  a limitation: no purely formal manipulation of the family (shifting, integrating, smoothing —
  see §4) can gain an exponent. Any gain must inject new arithmetic.
- **Rigidity of two-sidedness (for ζ).** `e₋ = e₊` is a theorem, not an accident: the primes
  cannot overshoot at one exponential rate without undershooting at the same rate. The mechanism
  is that a one-sided excursion pattern would force, via Landau, a singularity of
  `−z⁻²(ξ′/ξ)(½+ω−iz)` on the positive imaginary axis, i.e. a *real* zero in `(½,1]`, and there
  are none. For Dirichlet `L`-functions this symmetry breaks exactly at real zeros — a Siegel
  zero produces a genuinely one-sided (upward) exponential push (paper, Prop. 9.5). So
  `e₋ = e₊` is precisely the ζ-shadow of "no Siegel zeros for ζ".
- **Internal consistency check.** `ω ↦ e₋(ω)` must be `(ϑ−ω)⁺`, piecewise linear of slope `−1`.
  Any *measured* deviation from slope `−1` across two values of `ω` would be a contradiction —
  a redundancy that a numerical exploration of a hypothetical violation could exploit.

Numerical confirmation (synthetic quartet `ρ₀ = ½ + 0.3 ± 50i`, `ω = 0.1`, exact series terms,
`t ∈ [40, 60]`): fitted one-sided growth rates `+0.20054` and `−0.19946` against `ϑ−ω = 0.2`.

---

## 2. The L¹ strengthening: only the average negative part matters

This is the sharpest formulation the dive produced, and it strictly implies Corollary 10.7. Write
`Ψ_ω⁻(t) := max(−Ψ_ω(t), 0)`.

**Theorem 2.** Let `0 ≤ ω < ½` and `0 ≤ ε`. Then

> `∫₀^T Ψ_ω⁻(t) dt ≤ C e^{εT}` for all `T`  ⟹  `Θ ≤ ½ + ω + ε`,

and conversely `ϑ ≤ ω + ε` implies the integral bound. In particular, taking `ω = ε = 0`:

> **RH ⟺ Ψ⁻ ∈ L¹(0, ∞)** ⟺ `∫₀^T Ψ⁻ = O(1)` ⟺ (for that matter) `∫₀^T Ψ⁻ = O(T^K)` for some `K`.

*Proof.* Set `g := Ψ_ω⁺ = Ψ_ω + Ψ_ω⁻ ≥ 0`, continuous, with finite Laplace abscissa
(`Ψ_ω = O(e^{(½−ω)t})` unconditionally). The hypothesis makes
`h(z) := ∫₀^∞ Ψ_ω⁻(t)e^{izt}dt` convergent and analytic on `Im z > ε` (integrate by parts
against `∫₀^T Ψ_ω⁻ ≤ Ce^{εT}`). On `Im z > ½−ω`,
`ĝ(z) = −z⁻²(ξ′/ξ)(½+ω−iz) + h(z)`. Since `g ≥ 0`, Landau's theorem makes `iσ_c` (`σ_c` the
abscissa of `ĝ`) a singularity of `ĝ`. If `σ_c > ε`, then near `iσ_c` the function `h` is
analytic and `−z⁻²(ξ′/ξ)` is analytic unless `½+ω+σ_c` is a *real* zero of `ξ` in `(½,1]` —
there are none. Hence `σ_c ≤ ε`, `ĝ` is analytic on `Im z > ε`, so
`−z⁻²(ξ′/ξ)(½+ω−iz) = ĝ − h` is analytic there, i.e. no zero has `Re ρ > ½+ω+ε`. The converse
is the pointwise bound `Ψ_ω⁻ ≤ A*e^{(ϑ−ω)t} + O(1)` integrated. ∎

Comments.

- The pointwise Corollary 10.7 is the special case; but Theorem 2 is *strictly* weaker as a
  hypothesis: `Ψ_ω` may dip arbitrarily deep, arbitrarily often, as long as the *time-average*
  of the dips is exponentially small. "Allowed to fail on a sparse set" is now a theorem rather
  than a heuristic: pointwise control off an exceptional set `E` suffices whenever
  `∫_{E∩[0,T]} Ψ_ω⁻ ≤ Ce^{εT}`.
- The same argument with `g := (Ce^{εt} + Dt − Ψ_ω)⁺` gives the mirrored (upper-bound) L¹ form.
- `RH ⟺ Ψ⁻ ∈ L¹` deserves to be singled out: the screw function of ζ is the twice-integrated
  PNT error, and RH is *equivalent to the integrability of its negative part*. The positive part
  is then automatically bounded (`Ψ ≤ 2B(0)` under RH), so the criterion asks for an asymmetry:
  finite total negative mass against infinite total positive mass. Almost certainly this is
  folklore-adjacent (Landau's oscillation theory has one-signed and averaged variants), but we
  have not found this form in the literature, and in the screw normalisation it is exact and
  constant-free.
- Caution about a tempting further weakening: one cannot replace `Ψ_ω⁻` by
  `(Ψ_ω − ωA(ω)t − B(ω))⁻` and hope for more — that recentred function has mean zero at every
  rate and its negative mass genuinely grows like `e^{(ϑ−ω)T}` when `ϑ > ω` (see §5), which is
  consistent; the theorem is already calibrated at the right object.

---

## 3. Arithmetic translation: what a prover would actually need to show

With `x = e^t`, define the twice-integrated weighted Chebyshev sum and its smooth prediction:

> `W_ω(x) := Σ_{n ≤ x} Λ(n) n^{−½−ω} log(x/n)`,
> `G_ω(t) :=` the smooth blocks of the paper's eq. (2.4) `= 4e^{(½−ω)t}/(1−2ω)² + (linear and bounded terms, explicit)`.

Then `Ψ_ω(t) = G_ω(t) − W_ω(e^t)` and Theorem 1/2 read:

- **(Overshoot form.)** If for a single `ω` and some `ε < ½−ω`:
  `W_ω(x) ≤ G_ω(log x) + C x^ε` for all large `x` — *primes never exceed their prediction by
  `x^ε`, one-sidedly* — then `Θ ≤ ½+ω+ε`.
- **(Undershoot form.)** The same conclusion from `W_ω(x) ≥ G_ω(log x) − C x^ε`.
- **(L¹ form.)** The same conclusion if merely
  `∫_{1}^{X} max(W_ω(x) − G_ω(log x), 0) dx/x ≤ C X^ε`.

Note `W_ω(x) = ∫₁^x ψ_ω(u) du/u` with `ψ_ω(u) = Σ_{n≤u} Λ(n)n^{−½−ω}`: this is the
logarithmically-averaged weighted Chebyshev function. At `ω = 0` and `ε = ½ − δ` the overshoot
form is, in substance, the classical Landau/E. Schmidt oscillation theorem ("a one-sided estimate
`ψ(x) − x = O(x^{1−δ})` already forces `Θ ≤ 1−δ`", Ingham Ch. V). **What the screw packaging
adds is not the phenomenon but its optimal form**: (i) the two integrations make the target a
*continuous* function with an exact, constant-free identity rather than a distribution-adjacent
sum; (ii) the `ω`-family gives the exchange rate `Θ ≤ ½+ω+ε` with equality (Theorem 1), so
nothing is lost anywhere in the range; (iii) the L¹ weakening appears to be new at this level of
cleanness; (iv) the margin (`Ψ_ω`'s linear main term) means the inequality being targeted is not
saturated — the truth, if `Θ ≤ ½+ω`, sits a full linear term above the boundary being defended.

The most striking special case remains: **an upper bound alone on a weighted prime sum implies
zero-free half-planes.** Upper bounds on primes are traditionally the "easy" direction
(Chebyshev, Brun–Titchmarsh) — but only at constant-factor precision, and the exchange rate is
merciless about that distinction (§6).

---

## 4. Rigidity under smoothing

**Proposition 3.** Let `ν` be a finite positive Borel measure on `[0,∞)`, either compactly
supported or with `∫ e^{au} dν(u) < ∞` for some `a > 0`, and suppose its transform
`ν̂(z) = ∫ e^{izu} dν(u)` has no zeros in `{Im z > ε}`. If the truncated convolution
`K(t) := ∫_{[0,t]} Ψ_ω(t−u) dν(u)` satisfies `K(t) ≥ −Ce^{εt}` for all large `t` (or the
L¹ analogue of §2), then `Θ ≤ ½+ω+ε`.

*Proof sketch.* `K̂ = Ψ̂_ω · ν̂` (Laplace convolution). Run the §2 argument on `K⁺`: the
candidate Landau singularities on the ray `{iy : y > ε}` are poles of `Ψ̂_ω` there (none — real
zeros again) since `ν̂` is analytic; and analyticity of `K̂` on `Im z > ε` forces every pole of
`Ψ̂_ω` there to be a zero of `ν̂` — excluded by hypothesis. ∎

Examples of admissible `ν`: point masses, `e^{−au}du`, truncated Gaussians. Two consequences:

- **Nothing is lost**: one may pre-smooth `Ψ_ω` with essentially any positive kernel and prove
  the one-sided bound for the smoothed object instead. Since the arithmetic side's roughness
  (corners at `t = log p^m`) is a nuisance for any hard-analysis attack, this licence is worth
  having. The natural choice is the smoothest: convolving to make the target real-analytic
  changes nothing.
- **Nothing is gained**: the nonvanishing hypothesis on `ν̂` is exactly what prevents the kernel
  from accidentally (or deliberately) cancelling the pole of a violating zero. One *could* kill a
  known pole with a kernel zero — but the poles are unknown, and a kernel with zeros filling the
  whole strip is not the transform of a positive measure (positive measures have zero-free
  transforms on the imaginary axis, Bochner). Positivity of the smoothing is precisely the
  obstruction to cheating. This is losslessness (§1) seen from the other side.

---

## 5. Anatomy of a violation: excursion geometry, Fejér extremals, Siegel shielding

Suppose `ϑ > ω` and look at the dominant oscillation. For a single dominant quartet at
`ρ₀ = ½+δ±iτ₀` (paper, Prop. 1.5) the signal is `−(2/(τ₀²+(δ−ω)²)) e^{(δ−ω)t} cos(τ₀t+α)` plus
lower-order terms. Measured on the exact series (δ=0.3, ω=0.1, τ₀=50, t∈[40,60], 8001 points):

| quantity | measured | predicted |
|---|---|---|
| density of `{Ψ^{(q)} < 0}` | 0.4994 | ½ |
| density of `{Ψ^{(q)} < −½·envelope}` | 0.3325 | ⅓ (`cos ≤ −½` on a third of a period) |
| one-sided growth rate, + side | +0.20054 | `ϑ−ω = 0.2` |
| one-sided growth rate, − side | −0.19946 | `ϑ−ω = 0.2` |
| envelope saturation at `t=60` | 0.987 | → 1 |
| `∫Ψ⁺ / ∫Ψ⁻` over `[40,60]` | 0.9985 | 1 (mean-zero mass balance) |

So in the single-quartet regime a violation is as visible as it could be: sign changes of density
½, deep excursions of density ⅓, and *exactly balanced* L¹ masses of the two signs.

**How one-sided can a violation look?** The general oscillatory part is an almost periodic sum
`Σ c_γ e^{iτ_γ t}` at each exponential rate. Configurations that are extreme in the pointwise
sense exist: Fejér-kernel patterns (`|Σ e^{iτ_j t}|²`-shaped coefficient arrangements) are
non-negative with rare, shallow dips — a zero multiset arranged like the frequencies of a square
would make negative excursions pointwise-shallow while the positive spikes are huge. Two
structural facts control this:

1. **A square needs a frequency-zero component, and for ζ there is none.** Any configuration of
   the form `|Σ_j a_j e^{iτ_j t}|²` contains the constant `Σ|a_j|²` at the top exponential rate.
   In the zero-side series, a frequency-zero term at a positive exponential rate is *exactly* a
   real zero pair `β = ½+δ` (locked phase, positive sign — the paper's Prop. 9.5(i)). For ζ,
   real zeros in `(½,1]` do not exist, so the top-rate oscillation has **mean zero at every
   exponential rate**: no fully Fejér (i.e. one-signed) configuration is possible. For Dirichlet
   `L`-functions, the Fejér extremal is *arithmetically realizable* — it is Siegel shielding,
   Prop. 9.5(iii) of the paper, where the real zero supplies the positive constant that lifts
   the whole oscillation above the axis. The excursion analysis and the Siegel-blindness
   proposition are the same fact seen twice.
2. **Mean zero forces mass balance, which is what Theorem 2 is calibrated to.** A mean-zero
   almost periodic function can have very asymmetric *amplitudes* (Fejér-minus-mean has min `−1`
   against max `n−1`) but always has *equal L¹ masses* of its two signs. So a hypothetical
   near-Fejér zero configuration for ζ could make deep negative excursions rare and shallow —
   defeating naive density arguments — but it cannot reduce the negative *mass* below the
   balance, and the L¹ criterion of §2 sees the mass. This is the precise sense in which the L¹
   topology is the right one for this problem: pointwise one-sidedness is (barely) fakeable by
   conspiracy; averaged one-sidedness is not.

(Heuristic caveat: the mean-zero/mass-balance argument at the top rate is rigorous for finitely
many dominant zeros and is only heuristic when the supremum `Θ` is approached but not attained
by infinitely many zeros; Theorem 2 itself needs no such hypothesis — the caveat applies only to
the *interpretation* that mass balance is the mechanism.)

---

## 6. Inventory: where could a one-sided bound come from?

The corollary reduces zero-free half-planes to a *sign-sensitive* estimate at a sub-trivial
exponential scale. Essentially all of analytic number theory's workhorses are quadratic
(mean values, moments, large sieve inequalities) and therefore sign-blind. The known
sign-sensitive tools, and where each stalls:

1. **Sieves** (Chebyshev, Brun–Titchmarsh, Selberg) produce one-sided prime bounds with
   non-negative weights — but at *constant-factor* precision: `ψ(x) ≤ (1+c)x` gives
   `W_ω(x) ≤ (1+c)·(main term)`, i.e. error `≍ x^{½−ω}` — exactly the trivial exponent with a
   worse constant. The exchange rate pays only for exponent improvements; constants are worth
   nothing (Theorem 1's losslessness again). Going below the density scale one-sidedly is
   blocked by the parity problem. The corollary is, in this light, a quantitative statement of
   what breaking the parity barrier at *any* exponential scale would buy: the first zero-free
   half-plane.
2. **Explicit-formula positivity** (Weil-side squares: Bombieri's variational method,
   Connes–Consani's reproducing-kernel positivity). These prove `W(f) ≥ 0` unconditionally for
   test functions of *restricted support/scale*. The needed object is the shifted triangle
   family: in test-function terms, `Ψ_ω(t)` is the Weil functional against
   `e^{−ω|x|}·Δ_t(x)` (up to explicit archimedean bookkeeping), whose support `[−t,t]` grows.
   One might hope the damping `e^{−ω|x|}` gives an effective small support — it does not: the
   *arithmetic mass* of the test function sits at the edge `|x| ≈ t` (the summand mass at scale
   `v` is `≍ e^{(½−ω)v}`, increasing), exactly where small-support positivity has no grip. But
   Theorem 2 resets the target: such methods need not prove positivity of the family — they need
   only bound the *defect*:

   > **Problem (Weil positivity with exponential defect).** Exhibit any `ω ∈ [0,½)`,
   > `ε < ½−ω`, `C`, and an unconditional proof that `W(e^{−ω|x|}Δ_t) ≥ −Ce^{εt}` for all `t` —
   > or even only in the averaged sense of §2.

   This is formally weaker than anything the positivity programme currently aims at, and any
   solution is a zero-free half-plane. To our knowledge the defect version has never been posed.
3. **Turán's power-sum method** points the other way: it makes *oscillation* effective, not
   positivity. Its natural role here is an effective converse — given a violating zero at
   `½+δ+iτ₀`, produce an explicit `t ≤ T(δ, τ₀, ω)` with a certified dip
   `Ψ_ω(t) < −e^{εt}`, handling the interference of all other zeros (the paper's Prop. 1.5 does
   the single-quartet envelope; the masking problem is exactly power-sum territory, cf. the
   Knapowski–Turán comparative-prime-number-theory programme). A clean effective statement here
   is a self-contained, publishable sub-project and would upgrade Theorem 1 to an effective
   dictionary.
4. **Bias phenomena** (Chebyshev bias, Rubinstein–Sarnak) live at scale `x^{½}/log x`, inside
   the trivial envelope, and are conditional besides: no help, no obstruction.

Summary: sieve methods are scale-blocked, positivity methods are support-blocked (but now have a
strictly weaker target), power sums aim at the converse, and quadratic technology is sign-blind.
The corollary does not make any of these succeed; it prices exactly what a success would earn,
and (via §5) explains *why* one-sidedness is the natural hardness: sign-sensitivity below the
density scale is the parity barrier's analytic shadow.

---

## 7. Graded open problems

In decreasing order of strength (all unconditional statements to be proved for a single fixed
`ω ∈ [0,½)`):

- **P1 (half-plane).** `Ψ_ω(t) ≥ −Ce^{(½−ω−δ)t}` for some `δ > 0` — or its §2 averaged form.
  Prize: `Θ ≤ 1−δ`, the first zero-free half-plane. Equivalent to `Θ < 1` (Theorem 1), so
  exactly as hard — but stated as a one-sided growth bound on one explicit continuous function.
- **P2 (defect positivity).** The Weil-side version above, for the specific family
  `e^{−ω|x|}Δ_t` — the form in which reproducing-kernel technology would engage it.
- **P3 (effective converse).** Power-sum localisation of the first certified dip below
  `−e^{εt}` given a violating zero, uniform in the unknown remaining zeros.
- **P4 (family average).** The `q`-averaged analogue for Dirichlet characters (paper §10.5.3),
  where orthogonality thins the prime side; the L¹ form of §2 is the right target there too, and
  the Fejér/Siegel analysis of §5 says precisely what the exceptional-character configuration
  would look like in the average.

## 8. Honest limits

Theorem 1's losslessness cuts both ways: since the transport of exponents is exact, *every*
formal operation available inside the family (shift `ω`, integrate, smooth by Prop. 3, average
in `ω` — whose transform analysis gives nothing beyond the smallest `ω` in the support) provably
cannot improve the exponent. The only degrees of freedom this note adds are: the relaxation from
pointwise to averaged negative mass (Theorem 2), the licence to smooth (Prop. 3), and the sharper
description of what a proof must overcome (§5–6). RH itself sits at the closed end `ε → 0`,
`ω → 0` of the price list and inherits all of its hardness; the open half-planes `Θ ≤ 1−δ` sit
at the open end, where any sub-trivial one-sided input at all is enough. That is where this
reformulation is most exposed to an actual idea.

## Reproduction

All numerics: `mpmath` at 15 digits. §1/§5 table: exact four-term series of eq. (2.3) of the
paper for `γ ∈ {±50 ± 0.3i}`, `ω = 0.1`, 8001-point grid on `[40,60]`; rates fitted on windowed
maxima of each sign; L¹ masses by trapezoid rule (ratio 0.9985). The `κ = Σ|γ|⁻³ = 0.0014591`
and `Σγ⁻²` cross-checks reuse the paper's zero data (first 100 ordinates + Riemann–von Mangoldt
tail). The `Ψ^{[1]}` identity behind §2's ω=0 special case was verified against the arithmetic
side (closed-form thrice-integrated prime sum vs. zero sum, agreement `~10⁻⁷` = 200-zero
truncation tail) during the paper revision of 2026-08-27.
