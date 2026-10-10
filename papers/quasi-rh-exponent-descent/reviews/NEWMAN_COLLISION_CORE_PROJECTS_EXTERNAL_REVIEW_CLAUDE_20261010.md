# External review of the core Newman-collision projects (09, 13, 17)

10 October 2026. Prepared for Edward Baker. Reviewer model: Claude Fable 5.1
(`claude-fable-5-1`), Anthropic, in Claude Cowork. Cross-model review of
material prepared with GPT-6 / GPT-6.1-sol (Codex). Source state: GitHub
`main` at `eddf25c` (the author's local `claude-investigation` branch does
not yet contain folder 17; the GitHub copy was used for it).

This is the companion to
`NEWMAN_COLLISION_PORTFOLIO_EXTERNAL_REVIEW_CLAUDE_20261010.md`, which
covered the thirteen lift projects. It covers the three folders that
received the program's main effort: 09 (prime phase torus, nine notes and a
27-page manuscript), 13 (microlocal phase space, six notes, a manuscript
and four interval certificates), and 17 (enlarged-state transport, a new
manuscript in active development).

Method. Four parallel Claude reviewers: one each for 09, 13 (analysis) and
17, plus one devoted solely to reproducing 13's interval certificates from
scratch. Same brief as before (hand-check every identity, rerun every
checker, independent replay in separate code, classify every theorem as
proved / imported / conditional / numerical), with the explicit instruction
not to presume the verdict of the lift projects. Two program-wide facts
from the first review were supplied as tools: (A) at an all-real double
zero the threshold expression equals `72 W(x)² Σ_{ρ≠±x}(x−ρ)⁻² > 0`, so
`L(f) < −Δ` is the collision exclusion itself; (B) the kernel
`q_{T,b} = e^{−Tu²}[φ(u)/2 + φ(u−2b)/4 + φ(u+2b)/4]`, `φ = e^{−cosh u}`,
has de Bruijn–Newman constant exactly `T`. I verified the Polymath-box
argument in section 2.2 myself.

## 1. Verdict

The mathematics is correct throughout, and 13's computational work is of
high quality: its four certificates were reproduced field-for-field by
rerunning the checkers (198–516 s each) and, separately, by an independent
45-digit implementation of the approximant written from the stable
manuscript's definitions, which matched the certified center values to
`10⁻³⁶`, found the same 13/12/12/13 zeros in the same bands with the same
derivative signs, and placed all 1245 grid points inside the stored leaf
enclosures with zero violations. The transfer bound from the approximant
to the genuine `H_t` was audited against Polymath Theorem 1.3 and holds
with 9% margin (literal `η_N = 0.00884` versus the `5e^{−b/t} = 0.00964`
used); certified margins exceed transfer errors by factors of 4 to 65. As
verified infrastructure, this is the best thing in the repository.

But none of the three projects contains a step toward collision exclusion,
and each has a specific reason.

Project 13's certified theorem — no joint zero of `(H_t, H_t')`, all zeros
simple, in windows at `x ≈ 6.1·10⁹`, `t ∈ [0.04999, 0.05]` — is a known
fact (section 2.2). Nothing from the Husimi/current/Schur machinery
enters the proofs; every leaf is decided by `|F| > η/2` or `|F'| > Lη/2`.

Project 09's 27-page manuscript is a sequence of correct, coefficient-blind
transformations of the threshold quadratic `K`; by fact (A) the open
inequality `K < −payment` is the exclusion itself, the generic sign is the
wrong one (`K > 0` at all 24,001 sampled points including every
near-candidate), and the payments exceed `|K|` at every height where
anything can be computed (`N ≲ 10⁶`, i.e. `t ≳ 1/28`).

Project 17's central theorem (the adjoint-transport certificate) is an
"if and only if": a certificate with multiplier norm `Y` exists on a cell
exactly when the first jet satisfies `‖(F/2, F'/2L)‖ ≥ (1−R)/Y` there. The
multipliers carry no information and the divisor-transport arithmetic is
decorative; the continuous, angular and reflection sections are
kernel-generic and are killed by (B).

| Folder | Verdict | Promise (toward exclusion) | Reusable |
| --- | --- | --- | --- |
| 09 prime_phase_torus | close with note | 1 | moment dictionary; Thm `tr:finite-product` as a lemma |
| 13 microlocal_phase_space | close with note | 1 (4 as infrastructure) | evaluator + interval toolchain, validated against ξ |
| 17 enlarged_state_transport | close with note | 1 | the "iff" (so no one builds multiplier constructions) |

## 2. Project 13

### 2.1 What was verified

The approximant: with `s = (1−iz)/2`, `m_0`, `α`, `m_t = m_0 + (t/4)α²`,
`P_{t,N}(s) = Σ_{n≤N} exp(t log²n/4 − (s + tα/2) log n)`,
`G = M_t(s)P(s) + M_t(1−s)P(1−s)`, `F = G/A_t`, which the certificate
reviewer checked equals `B_t·f_t` of Polymath Theorem 1.3 exactly (the
`−s̄*` exponent reduces to `−(1−s) − (t/2)α(1−s)`, so `G` is holomorphic at
fixed `N`). The real-axis closed forms for `α_r, α_i, U, V, θ_t` agree with
direct complex evaluation to `10⁻⁴⁵`; the derivative `S' = Σ q_n γ_n` is
the `x`-derivative of the same fixed-cutoff function (matches a central
difference to 20 digits), so the "different cutoffs" hazard does not arise.

The interval arithmetic: closed Decimal intervals at 60 digits with
directed rounding on every operation; `ln`/`exp` via libmpdec's
correctly-rounded contract plus one ulp outward; `π` by Machin with an
alternating-series bound; trig by argument reduction and 30-term Taylor
with Lagrange remainder `4⁶⁰/60!`; the dangerous phase `T log n` with
`T ≈ 3·10⁹` is never formed — the sum is factored relative to `n = M` and
the integer multiple `πM²` is removed analytically. Integer powers use
repeated directed multiplication (the authors caught that `Context.power`
is only "almost always" correctly rounded; the earlier block-current record
still rests on it but is re-certified downstream). Height is handled by a
degree-63 Taylor expansion of a frozen-frequency comparison sum with
remainder `4⁶⁴B₆₄/64! < 1.5·10⁻⁶` and adaptive dyadic bisection; time by a
single padding `Δt·B_t ≈ 0.02` over the whole interval, which is the
dominant error (twice `η`). Zero count and simplicity by sign change plus
strict monotonicity on merged candidate bands, not the argument principle.
No error found.

Ground truth: the same evaluator at `t = 0` reproduces
`H_0(x) = ξ(1/2 + ix/2)/8` (via mpmath's independent Riemann–Siegel code,
`|H_0| ≈ 10^{−10⁹}`) to 0.1–1%, the expected size of the dropped
Riemann–Siegel `C` term; mpmath's `siegelz` finds exactly 13 zeros of
`ζ(1/2 + iT)` in the corresponding `t = 0` window, within `10⁻³` of the
`t = 0` approximant's zeros. The normalizer, carrier, weights and cutoff
are all right.

### 2.2 Why the certified statement is already known

Polymath 15 (arXiv 1904.12438) proves `Λ ≤ 0.22` by showing that for
`0 ≤ t ≤ 0.2` no zero of `H_t` crosses the barrier near
`X = 6·10¹⁰ + 83952 − 1/2`, that all zeros lie in the strip `|Im z| ≤ 1`,
and that at `t = 0` all zeros with `|Re z| ≤ X` are real and simple
(Platt). The zero count in the box `{|Re z| ≤ X, |Im z| ≤ 1}` is therefore
conserved on `[0, 0.2]`. Let `t₁` be the infimum of times at which a
non-real zero exists in the box. At `t₁` all zeros are real; non-real zeros
can appear only through a real collision at `t₁`; but a real zero of
multiplicity `m ≥ 2` at time `t*` is preceded by non-real zeros
(`H_{t*−δ} ≈ a(z−x)^{m−2}[(z−x)² + m(m−1)δ]`, Polymath Prop. 3.1), which
contradicts minimality. So every zero of `H_t` with `|x| ≤ 6·10¹⁰` is real
and simple for all `0 ≤ t ≤ 0.2`, and `(H_t, H_t') ≠ (0, 0)` there.

Project 13's windows are at `x ∈ [6.1187·10⁹, 6.1265·10⁹ + 8]`,
`t ≤ 0.05`: inside the box by a factor of ten in height and four in time.
The certificates re-derive, by a different method, a fact that follows
from published results; the only new content is the counts 13/12/12/13 and
the band positions, which the `t = 0` zeta zeros plus the computed drift
(`≤ 0.2` per zero between `t = 0` and `t = 0.05`) already imply. Nothing in
the folder mentions this. More to the point for the program: a Newman
collision at time `Λ` requires a pre-existing complex pair, and the
certified region has none by the same argument, so the windows could not
have carried information about `Λ > 0` whatever they found.

### 2.3 The lift and the current

The Husimi/Wigner smoothing of Note 1 reduces to `R_t^a = e^{−az²}H_t`:
every "drift", "contact term" and "negative momentum diffusion" statement
is the conjugation of `−∂_x²` by `e^{ax²}`. Note 1 concedes the smoothing
introduces no exclusion; Note 14's failure criterion for this program was
met at Note 1, and Notes 2–6 are a different project under the same name.

The coherent current `𝒥 = −Im(S' S̄) = u'v − uv'` satisfies
`|𝒥| ≤ |u'||v| + |u||v'|`, so the current test (5.4) is implied pointwise
by the two component screens `|u| ≤ η/2`, `|u'| ≤ Lη/2`. It can never
exclude a point that the component screens do not; Note 23's target "a
cell where the separate tests are inconclusive but the paid current test
excludes" can occur only as a bisection artefact. The "negative block
current `−181.17 w_M²`" is the statement that the argument of an
11,033-term exponential sum is increasing at one point: it is a measurement
of noise that Heat Note 16 lists as a new result. Heat Note 17 §3 already
exhibits (in substance) kernel (B), for which `𝒥 = 0` at the all-real
double zero, so "nonzero current ⇒ no collision" is false for a positive
kernel.

The threshold route (§8): the pilot's fourth-jet Cauchy payment
`24L⁴η ≈ 37,050` at `M = 22066` exceeds the signal by factors 5–72; by the
scaling `payment/𝒦 ~ L⁶ e^{−κ/(2t)}` the test cannot be certified before
`L ≈ 40`, i.e. `x ≈ 3·10¹⁸`, `N ≈ 5·10⁸` terms.

### 2.4 What to keep

The evaluator and interval toolchain, which have now been validated
externally against `ξ` and against an independent implementation. If a
window is ever to carry information for `t > 0`, it must lie above
Polymath's barrier (`x > 6·10¹⁰`), and it will still be a finite statement.
Further atlases at `x ≈ 6·10⁹`, and further current/Schur bookkeeping,
should stop.

Hygiene: SHA-chained sources, byte-identical replays across Python
3.10 → 3.13 (Decimal, unlike the floating checkers of 10 and 11),
`--output` to protect records. Weak points: the scripts cannot run under
`python3 -I` (sibling imports); `check_enlarged_state_identities.py` and
Review 8 belong to project 17, not 13, and the former rewrites its record
in place by default; the imported `η` ledger is cited as "Heat Notes 8
and 13" rather than the stable manuscript's proposition where it is proved;
`DRAFT_HISTOR.md` is misnamed (here, in 09 and in 17).

## 3. Project 09

### 3.1 What was verified

Every theorem in `prime_phase_torus_signed_reductions.tex` was
hand-checked and classified: the disk and count inputs are imported
(Polymath Thm 1.3 and 1.5(iv); hypotheses satisfied; the count constant
`C_count` is never made numerical, so `Γ_count` is not computable); Prop.
`fo:threshold-sign` is conditional (all-real time, ordinary double zero)
and correctly proved; the four-channel expansion, dual kernels, cubic
payment, Gram relaxation, covariance envelope, near-pair theorem,
Euler–Maclaurin remainder, finite Poisson/Fresnel (`tr:finite-product`),
Möbius sublattice formula, and stationary reflection are all proved here
and all correct. Eighteen symbolic checks (sympy, symbolic weights and
phases) and a numerical replay of the closed forms, the Poisson transform
(error at or below the claimed order), the sublattice bound, and the
reflection identities all pass. All five checkers pass and all five records
regenerate byte-for-byte. The manuscript compiles. No error anywhere.

### 3.2 Why it is not load-bearing

With `g_j ≈ 2(ic)^j M_j`, the target quadratic is
`K ≈ (2F₃² − 3F₂F₄ − γF₂²)/(4c⁶)`. By fact (A) this is `72W²Σ(x−ρ)⁻²` at
any all-real double zero. More elementarily, `2F₃² − 3F₂F₄` is a local
real-rootedness detector: for `F = cos ωx` it is `ω⁶(2 sin² + 3 cos²) > 0`
everywhere, for `F = cosh ωx` it is negative near zero. So "`K < −payment`
at every paid candidate" is exactly "no double zero of the trigonometric
kind in the sector" — the exclusion in moment coordinates. Nine notes and
the manuscript transform `K` exactly (with proved vanishing remainders);
none changes its sign, and none can.

Nothing arithmetic is used. Every theorem is proved for arbitrary smooth
weights `w(u)` with bounded log-derivative and degree-≤6 polynomial
kernels; the manuscript says so (§tr: "uses only the degree-six polynomial
envelope"). The prime torus is Bohr's observation and is never used after
Note 1; the orbit dynamics were abandoned when `F_{t,N}` turned out not to
be heat-invariant. Note 3's own control `(1 + r)²` already shows that
positivity, common frequency and both candidate equations cannot give the
sign; the manuscript proves nothing that distinguishes ζ's coefficients
from that control.

Two quantitative facts the manuscript never states. The size of `K` is
`≍ (Nw_N)² poly(L) ≍ N^{1−κ/4} poly(L)`, so the "`Δ̂ = o(1)`" of
`(fo:Delta-scale)` is misleading: the relevant ratio `Δ̂/|K| ≍ L⁴/N` is 31
at `N = 22066`, 11 at `10⁵`, 1.3 at `10⁶`, and drops below 1 only near
`N ≈ 10⁷` (`t ≈ 1/32`, `x ≈ 10¹⁵`). The criterion is untestable in the
computable part of the sector. And the "density-strengthened" `Γ_count`
has constant `≤ 0.028` even at `C_count = 0`; numerically `Γ_count X₂²` is
`10⁻³`–`10⁻⁵` of `K`, while the true inverse-square sum at an all-real
double zero is `≍ L²/48`, so the strengthening is about `L/300` of the
truth.

A scan of 24,001 points in `x ∈ [x₀ − 30, x₀ + 30]` at `N = 22066` (95
zeros of `F`, mean gap `0.626` versus `4π/L = 0.628`): `K > 0` at every
point, including the twelve best near-candidates (`|F/2|` down to
`1.9·10⁻⁴ < η/2`, but `|F'/2| ≈ 1.8 ≫ Lη/2 = 0.096`, so no sampled point
meets both tolerances) and the midpoints of the five closest zero pairs.
This agrees with Note 24's pilot in project 13 — a diagnostic 09 never ran
on itself — and is what section 2.2 predicts: at these heights all zeros
are real and simple, so `K` is approximately the sum of squares.

After the transformations, the "retained main expression" is longer than
`K`: `tr:global-primitive` keeps `≈ 8N²` oscillatory integrals per
sublattice; `em:remainder` with `J* = N^{2/5}` transforms a fraction
`N^{−2/5}` of pairs; the B-process maps a length-`N` sum to a dual of
comparable length. The text does not say so.

### 3.3 What to keep

The moment dictionary `(fo:candidate-coordinates)`–`(fo:Delta)` and
`tr:finite-product` as a clean, endpoint-uniform statement of the
van der Corput B-process. Everything else should stop. If anything
continues, it should begin by naming a property of `Σ n^{−s}` that is false
for generic smooth-weight sums — before any further rewriting of `K`.

## 4. Project 17

### 4.1 What was verified

All 49 displayed identities (anchored response, tangents, twist defect,
commutators, Gaussian realization, 3×3 example, gauge relation, support
function, Schwarz–Pick body, chord/gradient equations and hierarchy,
Gaussian control and its discriminant, angular shift identity, affine
Ward identity, reflection operator, exponent arithmetic of Cor. 3.4) check
by sympy or mpmath; `check_enlarged_state_identities.py` passes its 15,446
assertions with matching SHA; the manuscript compiles. An independent
evaluation of the actual state at the 13 calibration cell gives
`min ‖(F/2, F'/2L)‖ = 0.108` on `[x₀, x₀ + 8]` versus `η/2 = 0.0048`
(margin 22×) and 13 sign changes of `F`, agreeing with 13's atlas.

### 4.2 The certificate theorem is an equivalence

Since the divisor graph on `{1, …, N}` is connected,
`ker B_R = span{q_R, (iq)_R}`, so `range(B_Rᵀ)` is the entire orthogonal
complement of those two vectors. The certificate equation
`(eq:certificate)` then imposes exactly two scalar conditions on
`(y, z₀, r)`: pairing with `q_R` gives `1 = y·Cq_R + r·q_R`, pairing with
`(iq)_R` fixes `z₀`. Conversely, for any `y` set `ρ = 1 − y·Cq_R`,
`r = ρ b`, `z₀ = −y·C(iq)_R`; the residual is orthogonal to the kernel,
hence equals `B_Rᵀλ` for some `λ`, and `R = |ρ|` exactly. So a certificate
with `(R, Y)` exists on a cell if and only if `‖Cq_R‖ ≥ (1−R)/Y` there;
the optimal certificate has `r = 0`, `y = Cq_R/‖Cq_R‖²`, `‖y‖ = 1/‖Cq_R‖`.
The `≈ N Σ_p 1/p` multipliers `λ` carry no information; the arithmetic
enters only through `ker B = Cq`, i.e. through the definition of `q`. The
"regular construction" requirement (no division by `F, F'`) is not a
restriction: any bound `‖y‖ ≤ Y` proves `‖Cq_R‖ ≥ (1−R)/Y`, so every
construction must contain that proof; telescoping `λ` along divisor paths
reproduces the same equation in one line. Verified numerically on an
`N = 6` graph.

Cor. 3.4 therefore reads: if the first jet of `F_{t,N}` is never smaller
than `N^{−α}`, `α < 5/8`, then `H_t` has no double zero. True and trivial;
"multiplier growth exponent" renames `−log min‖(F/2, F'/2L)‖ / log N`. At
the 13 cell the best possible `Y = 9.29 = N^{0.223}`, far below `N^{5/8}`;
the finite milestone "resolve a cell where separate enclosures are
inconclusive" is one line in 13's existing checkers (enclose the joint
norm), and the uniform milestone is the collision problem for the
approximant.

### 4.3 The rest

Sections 4–6 (chord lift, angular theta field, logarithmic reflection)
hold for every positive even Schwartz kernel; the manuscript's own control
(Prop. 4.3, Gaussian tails) makes this point but leaves open whether
super-exponential decay matters, and kernel (B) closes that door. The
score-to-jet dictionary of Heat Note 25 (20)–(21) is consistent with fact
(A): at an exact double zero it reproduces the threshold quantity, which
is automatically of the collision's own sign. The affine Ward identity is
shared with the Green-kernel controls of 06.

Minor: the 3-node example `(eq:rational-source)` is a chain `1→2→3`, not
the prime-divisor graph on `{1, 2, 3}` (whose `A_bulk` is
`[[41,−2,−6],[−2,1,0],[−6,0,1]]`); Lemma 1.4, `h(D, B)` and
`eq:current-support` are reprints from 09/13/Note 24, correctly cited.

The abstract, §7 and README are scrupulous: "no useful uniform multiplier
construction, theta-specific overlap sign, new collision exclusion, or
proof of RH is established." The closure note should add the equivalence
of 4.2 so that no further effort goes into multiplier constructions.

## 5. Two remarks on the sector

The shrinking sector `κ ∈ [1, 3/2]`, `t ≤ 1/20` is genuinely outside
Polymath's trivial regime: `n = 1` dominance of the approximant
(`Σ_{n≥2} w_n < 1`) needs `κ ≳ 5–6` (`Σ_{n≥2} w_n ≈ 93, 199, 48, 5.7, 1.9,
1.03, 0.67` at `κ = 1, 1.5, 2, 3, 4, 5, 6`, `t = 0.05`), so the sector is
not already covered by Polymath 1.5. But a shrinking-sector theorem
addresses only `Λ ≤ 1/20` of the range `(0, 0.22]`, and only heights
`4πe^{1/t} ≤ x ≤ 4πe^{3/(2t)}` at each time; the manuscripts acknowledge
the coverage obligations. And in the computable part of the sector
(`t ≳ 1/28`) all zeros are real and simple by section 2.2, so every
numerical probe of the "opposite sign" there will return the sum-of-squares
sign, as both 09's scan and 13's pilot did.

## 6. Summary across all seventeen folders

With this review every project folder under `newman_collisions/` has been
externally reviewed. All are mathematically correct. None contains a step
toward excluding a positive-time collision: the thirteen lifts are
classical identities plus automatic obstructions; 13 is excellent
verification infrastructure certifying a known fact; 09 is a long exact
rewriting of the exclusion statement in coefficient-blind form; 17 is a
tautological certificate plus kernel-generic sections. The missing input is
the one Heat Note 13 named before the portfolio began: a property of the
arithmetic coefficients, not of the kernel's shape, incompatible with an
all-real double zero. Nothing in folders 01–17 constrains what that
property might be, and the generic numerical sign is against the proposed
route at every height where it can be tested.

Three assets are worth carrying into the stable heat manuscript: the
sum-of-squares identity (A) with its consequence for the threshold route;
the control kernel (B) with its exact Newman constant; and 13's validated
evaluator as the reference implementation of `F_{t,N}`.

No collision exclusion, threshold result, or RH conclusion is claimed or
refuted in this review.
