# External review of the Newman-collision lift portfolio (projects 01–08, 10–12, 14–16)

10 October 2026. Prepared for Edward Baker. Reviewer model: Claude Fable 5.1
(`claude-fable-5-1`), Anthropic, in Claude Cowork. Cross-model review of
material prepared with GPT-6 / GPT-6.1-sol (Codex) on 10 October 2026.
Source state: branch `claude-investigation` at `92aa635`, identical to
GitHub `main` at `eddf25c` for the folders reviewed.

Scope. Thirteen of the seventeen project folders under
`papers/quasi-rh-exponent-descent/newman_collisions/`. Projects 09, 13 and
17 are excluded at the author's request (17 is in active development and
builds on 09 and 13). Project 12 was reviewed separately in
`12_radial_bessel/reviews/3_RADIAL_BESSEL_EXTERNAL_REVIEW_CLAUDE_20261010.md`
and its verdict is carried into the table below.

Method. Five parallel Claude reviewers each took two or three folders with
one common brief: read every file; verify every displayed identity by hand;
rerun every checker with `python3 -I`; write an independent replay of each
central numerical claim in separate code (mpmath/sympy, not the folder's
Decimal certificates); then ask, for each "result", whether it is trivial
or classical, whether it is insensitive to the Newman scale, and whether
the proposed next task carries any leverage the one-dimensional problem did
not already have. I verified the two program-wide findings in section 2
myself (sympy identity check; direct reading of the 08 checker source).
Reviewer scripts are in the session scratch space and were not committed.

Standard applied. Heat Note 14's own sentence: "An exact lift alone is a
representation result; collision exclusion requires an additional theorem
that survives reduction."

## 1. Verdict

Across roughly 150 displayed equations in thirteen folders, no reviewer
found a mathematical error. Every checker passes; every rational record
reproduces exactly; every independently replayed number agrees (typically
to 25–30 digits). The work is clean.

It is also, with two partial exceptions, not load-bearing. Each folder
follows the same arc: an exact "lift" that is a classical identity in new
notation (Pólya's Gaussian average, the Segal–Bargmann isometry, Riemann's
1859 integral formula, the definition of ξ via the Eisenstein constant
term, Mori–Zwanzig, Hubbard–Stratonovich, the Hall–Ho pencil); then an
"obstruction" that was either automatic from the existence of a single
real zero of ξ, or already printed in Heat Note 14 as the project's
stopping criterion; then a "next bounded task" which, on inspection, is
the Note 13 strict-sign target `L(f) < −Δ` or the joint collision
estimate of program 09, rewritten in the folder's coordinates. Nothing in
any folder depends on `t ≤ 1/20`, on `Λ ≤ 0.2`, or on the shrinking
sector; every certified sign or positivity holds for all real `t`.

My recommendation is to close all thirteen. Six deserve a short closure
note because they contain a reusable fact (section 4); the other seven
can be closed with a line in the program README.

| Folder | What it is, in one line | Verdict | Promise |
| --- | --- | --- | --- |
| 01 analytic_gaussian | Pólya Gaussian average; Hermite dictionary; heavy tail constants | close with note | 1 |
| 02 bargmann_fock | Same Hilbert space as 01 at width 2t, uncentered (worse) | close | 0 |
| 03 susy_dirac_hodge | Witten Laplacian / Stein identities for ρ_t | close with note | 1 |
| 04 cohomological_localization | Contractible superspace; only constants protected | close | 0 |
| 05 interacting_susy_gauge | Gaussian imaginary shift on the Dirichlet polynomial | close | 0 |
| 06 theta_lattice | Riemann's formula heat-conjugated; explicit positive control | close with note | 1 |
| 07 automorphic_scattering | ξ by definition at t=0; wrong spectral slice at t>0 | close | 0 |
| 08 adelic_local_models | Hubbard–Stratonovich at N=6; class number one of Q | close with note | 1 |
| 10 kinetic_stochastic | Mori–Zwanzig of ∂_t h_j = −h_{j+2}; state-independent memory | close with note | 0.5 |
| 11 boundary_extensions | Sturm–Liouville facts; rank-one tensor extension | close | 0 |
| 12 radial_bessel | H_t(abs z) positive-definite on R^d, d ≤ 9 | close with note | 0 |
| 14 integrable_lax | Hall–Ho pencil; Note 12's quartic time-translated | close | 1 |
| 15 lee_yang | Classical zeta-zero moments; target is RH by Newman's theorem | close | 0 |
| 16 nonlinear_collective_fields | Moment hierarchy; one useful identity (section 2.1) | close with note | 1 |

## 2. Three findings that bear on the whole program

### 2.1 The threshold-jet test is a sum of squares

The all-real-threshold necessary condition of Heat Note 12,

    L(q) = 2 q_3^2 − 3 q_2 q_4 − (18 ∂_x^2 log A_t + 9/x^2) q_2^2 ≥ 0,

has, at an exact double zero `H_t(x) = H_t'(x) = 0`, the normalizer-free
form `A_t^2 L(q) = 2H_3^2 − 3H_2H_4 − 9H_2^2/x^2` (found independently by
the 03, 06, 12 and 16 reviewers; the `18 b_x` term cancels exactly). Write
`H_t(z) = (z^2 − x^2)^2 G(z)` with `G` even, and `W(z) = (z + x)^2 G(z)`.
Then, at `z = x`,

    2H_3^2 − 3H_2H_4 − 9H_2^2/x^2 = −72 W(x)^2 (log G)''(x)
                                 = 72 (2x)^4 (G'^2 − G G'')(x).

If `G` is real-rooted of genus ≤ 1 (the all-real-threshold hypothesis),
`−(log G)''(x) = Σ_ρ (x − ρ)^{−2}` over the remaining zeros, so

    A_t^2 L(q) = 72 W(x)^2 Σ_{ρ ≠ ±x} (x − ρ)^{−2} > 0.

I verified this symbolically. Consequences: (i) the inequality `L ≥ 0` is
Laguerre's inequality for the deflated function and is strict whenever any
other zero exists; it is saturated only by the bare quartic `(z^2 − 1)^2`,
which is why that control "saturates" in Notes 12 and 14. (ii) A proof of
`L(f) < −Δ` at a candidate would be a proof that no all-real double zero
exists there, i.e. the collision exclusion itself. The threshold-jet route
is therefore a restatement of the target, not a reduction of it; pursuing
it in Hermite (01), score (03), Green (06), sine (12), pencil (14) or
moment (16) coordinates changes nothing. (iii) At an exact collision the
normalizer `A_t` drops out entirely; it must still be carried for
approximate candidates, as Note 12 says.

### 2.2 A standard counterexample kernel exists and has Newman constant exactly T

Three folders (01, 06, 12) each construct a positive, even, smooth,
super-exponentially decaying kernel whose flow has an all-real double zero
at a chosen positive time. The cleanest form (06 Note 2 §4; 01 eq. 29):

    q_{T,b}(u) = e^{−T u^2} [ φ(u)/2 + φ(u − 2b)/4 + φ(u + 2b)/4 ],   φ = e^{−cosh u},

whose time-`T` readout is `B(z) cos^2(bz)` with `B(z) = 2K_{iz}(1)`. By
Pólya (1926) `B` has only real zeros, so the readout is in the
Laguerre–Pólya class; backward heat preserves that for `t > T` (de Bruijn),
while for `t < T` the double zero at `π/(2b)` splits into the pair
`π/(2b) ± i√(2(T − t)) + …`. So this kernel's de Bruijn–Newman constant is
exactly `T`, and it satisfies every property any folder in the portfolio
has used: positivity, evenness, decay, alternating Taylor signs, positive
Hankel matrices, 3-dimensional radial positivity, the Green/endpoint
hierarchy of 06, the memory positivity of 10, the Ward identities of 03.
The 06 reviewer confirmed numerically that zeros are complex just before
`T` and real just after. This single object closes every mechanism in the
portfolio that does not use something arithmetic about Φ, and should be
recorded once in the heat manuscript as the standing control.

### 2.3 Two hygiene issues

Assertion counts are inflated. The 08 checker reports "440 exact
assertions"; 405 of them are `check(arch + local == 0)` where the script
defines `local = −arch`, 11 check a quantity against its own definition,
and 6 check commutativity of rational multiplication; 18 carry content, all
at the level of `log 6 = log 2 + log 3`. The 06 scout checker tests
`4·a·(−b/4) = −a·b` with placeholder rationals in place of `Φ(0)` and
`ϑ(1)` under the family name "odd-endpoint mismatch"; the 07 checker
inflates with ten Leibniz-coefficient tautologies. Across the portfolio,
no checker evaluates a theta or zeta quantity except 03, 12 and 15.

Floating-point records are not byte-reproducible across Python versions
(10 and 11 differ in the last digits between 3.10 and 3.13), contrary to
Note 15's "reproduced byte for byte". Rational and Decimal-interval records
do reproduce exactly. Folder 01 has no checker at all despite a review
citing numerical diagnostics. Several checkers rewrite their record into the
source tree on every run.

## 3. Folder-by-folder

**01 analytic_gaussian.** The Pólya/Polymath representation
`H_t(x) = ∫ p_t(y) H_0(x + iy) dy`, the Hermite dictionary
`H_t^{(j)} = (−i)^j (2t)^{−j} P_t(h_j f)`, the Parseval identity (10), and
an exhaustive tail payment (the printed `e^{−84}` at `R = 9` is actually
`e^{−110}`; the envelope constants are loose by `e^{150}`). All verified by
hand, sympy and mpmath to 30 digits. The "scoped obstruction" is that a
rank-two projection is not coercive on an infinite-dimensional space, which
Note 14 printed in advance (`(z − x)^2 + 2t` is in the kernel). The
normalizer-cancellation "result" (11) is the definition of γ. Next task is
the original problem in Hermite coordinates. Close with note recording the
isometry (10) and the control of section 2.2.

**02 bargmann_fock.** The same Hilbert space as 01: with `a = 2t` and
translation to `x`, 02's norm (4) is 01's (10) and 02's projection identity
(8) is 01's (9). Neither folder notices. The uncentered width-`a` geometry
is strictly worse: the observation subspace at height `x` carries weight
`e^{−x^2/a}` of the state (`10^{−42}` at `x = 10`, `10^{−10^{19}}` in the
sector). The coefficient restriction tested in §4 (even, alternating,
Hankel-positive) is by Hamburger just "Fourier transform of a positive even
measure", the whole class. Close; merge any residue into 01.

**03 susy_dirac_hodge.** Witten Laplacian `K_t = B_t^† B_t` with ground
state `√ρ_t`; Ward identities; gap bound; score residual hierarchy; certified
`β_t ∈ (86.390, 86.563)`, a sign change of the residual `R_t`, and a Fisher
defect `D_0 > 0.00012`. All correct and replayed (true `D_0 ≈ 0.853`;
`J_t μ_2 = 1.0099`, so θ saturates Cramér–Rao to 1%; Poincaré constant
`≈ 86.2`). But: the Ward identities are Stein's identity; the gap bound is
the Poincaré inequality, and is dominated by the two-term Taylor bound
`Re C ≥ 1 − μ_2 x^2/2` (zero-free to 13.2 versus 9.3, first zero at 28.27);
`D_0 > 0` is Cramér–Rao; and the "certified sign change" is logically
equivalent to `ρ_t` not being Gaussian, since `R_t` is odd and
`E[uR_t] = 0` exactly. All of it holds for every `t` (replayed at
`t = 1, 5, 37`). The residual map `(C_2..C_6) ↔ (r_1..r_5)` has determinant
`β^5`, so Note 16's priority-4 task "bound `r_1 r_3`" is the original
threshold problem. Close with note recording the Laguerre form of the
threshold test and the actual sizes of `D_0` and `J μ_2`.

**04 cohomological_localization.** Zero-dimensional superspace with
`Qu = ψ, Qψ̄ = ib`; Berezin reduction gives the pushforward of `N(0, 1/λ)`
under the quantile map (Nicolai map / Parisi–Sourlas). Algebra correct
(sympy). The note never states the decisive fact: `(u, ψ)` and `(ψ̄, b)`
are contractible pairs, so the Q-cohomology is the constants, "no
Q-closed completion of `cos(xu)`" is a special case, and the localization
limit `λ → ∞` sends the readout to the constant 1, erasing every zero. The
mechanism was dead by design; no checker, nothing numeric claimed. Close.

**05 interacting_susy_gauge.** `e^{tu^2} = E[e^{2λu}]` with `λ ~ N(0, t/2)`
applied termwise to the Dirichlet polynomial: the classical Gaussian
imaginary-shift representation (de Bruijn; Polymath). The "interaction"
`q_{a+1,b+1} q_{a,b} / (q_{a+1,b} q_{a,b+1}) = e^{(t/2) log 2 log 3}` is the
cross term of `(a log 2 + b log 3)^2`. The Haar-averaging and
Laurent-identity obstructions are character orthogonality and linear
independence of exponentials. The checker validates Faà di Bruno with
rational stand-ins for `log 2, log 3`. The note's own stopping criterion
("stop if the model re-encodes the input coefficients") is met. Close.

**06 theta_lattice.** The "affine theta Ward identity"
`16H_t = 1 + (2t − 1 − x^2) J_t + 4tx J_t' − 4t^2 J_t''` is, at `t = 0`,
Riemann's 1859 formula `ξ(s) = 1/2 + (s(s−1)/2) ∫_1^∞ ψ(y)(…) dy` with
`y = e^{4u}` (the "Ward constant" is Riemann's `ξ(0) = 1/2`), and at
`t > 0` it is the conjugation `e^{−t∂^2} x^2 e^{t∂^2} = x^2 − 4tx∂ − 2t + 4t^2∂^2`.
Verified to 30 digits at several `(t, x)`. Conditional on a collision the
map `(J_4, J_5, J_6) ↔ (H_2, H_3, H_4)` is triangular with determinant
`−64t^6`, so Note 16's "integer-lattice constraint on `J_4, J_5, J_6`" is
the paid fourth-jet test. The two-rotor completion multiplies the kernel by
`ϑ(e^{4u})`, which is not even; the mismatch is immediate. The explicit
control of §4 is the one reusable artifact (section 2.2); the Laguerre
argument for its threshold positivity is redundant given the manuscript's
deflated-mirror proposition. README has a placeholder path. Close with note.

**07 automorphic_scattering.** The extraction operator
`E_s = (s/2) y^{−s/2}(D_y − 1 + s/2)` applied to the completed Eisenstein
constant term returns `ξ(s)` — by the definition of `ξ`. Replayed at three
points to 25 digits. At `t > 0` the "lift" `V_t = y^{s/2} Ξ_t(s)` is the
heat-flowed `ξ` times a power of `y`; it is the constant term of nothing,
so there is no automorphic content at positive time. The slice obstruction
(8) — the heat slice `s = 1/2 + ix/2` is `Re σ = 1/4`, not the unitary
`Re σ = 1/2` — is the textbook reason Selberg's unitarity gives
`ζ(1 + it) ≠ 0` and nothing on the critical line (Iwaniec, Spectral
Methods), and Note 14 anticipated it. Close.

**08 adelic_local_models.** Shared-Gaussian representation of the heat
weights (Hubbard–Stratonovich at coefficient level), exact through four
jets for `N = 6` (replayed to 30 digits). Every diagonal twist commutes with
everything (all operators are diagonal in `e_n`). The "global adelic
compatibility" (6) says the everywhere-unramified Hecke characters of `Q`
are `|·|^{iT}` — class number one — and this is imposed by fiat; the
manuscript's twist obstruction uses arbitrary completely multiplicative
`χ`, so restricting to Hecke characters is the "unexplained restriction"
Note 14 warned about, stated in advance. The surviving family `n^{iT}` is
exactly program 09's frozen-coefficient `x`-shift orbit, as the note says.
Assertion count: see 2.3. Close with note.

**10 kinetic_stochastic.** Exact Mori–Zwanzig memory equation for the five
jet observables on `|u| ≤ U`, with positive memory kernel and a tail bound
`E_j(U)` that is tight to a factor 0.61 (replayed). The decisive point: the
memory kernel `K(τ) = B e^{τD} B^*` is independent of the state — it is a
property of the five-dimensional subspace and `U` alone — so it cannot
distinguish θ from any kernel, and the note's own control confirms this.
Because `L r_j = −r_{j+2}`, the whole apparatus is `ḣ_3 = −h_5`,
`ḣ_4 = −h_6` in a Gram-orthogonalized basis. New quantitative fact from
the replay (`x_* = 30, t = 0.05`): the resolved and hidden parts of rows 3
and 4 are each 40–160 times the true derivative and cancel to 2–3%, so
neither the sign nor the size of the memory term is informative. "No
finite closure" is the absence of point spectrum for a multiplication
operator. Close with note.

**11 boundary_extensions.** Transfer matrix, Dirichlet-to-Neumann map,
Green identity, simplicity of 1-D Dirichlet eigenvalues: standard
Sturm–Liouville, all verified symbolically. The pole obstruction to
`r(x^2) = H_t(x)` for a passive Stieltjes response is a roundabout proof of
"a positive function is not an oscillating one" (first real zero of `H_0`
at `x = 28.2694…`, replayed). The "extension" `U_t = m_t ⊗ w` is a tensor
product with a fixed profile; its flux readout is the original integral
times `α/α`. The assigned first task (compare normalized jets with the
finite approximant on a rectangle; test visibility of candidate modes) was
not carried out — with a rank-one extension there are no modes to be
visible. Next task is a Hilbert–Pólya-type inverse realization of `ξ`.
Close.

**12 radial_bessel.** See the separate review. Radial positivity in `R^3`
holds to `t_* ≈ 37.45`; it is Bochner positive-definiteness of
`H_t(|z|)` on `R^d`, true through `d = 9` (exploratory) and false at
`d = 11`; the Gaussian-mixture and high-dimension obstructions follow from
Hardy's theorem and Schoenberg's theorem. Close with note.

**14 integrable_lax.** Hall–Ho pencil identity (1) verified symbolically
for `d = 3..6` with rational and complex roots; the time conversion from
arXiv 2202.09660 is right. The rank-one relation `[D, C] + I = 11^T` is
definitional and universal (the note admits it). The quartic control (4)–(5)
is Note 12's quartic translated in time: any polynomial with a double real
root gives "an explicit matrix collision at arbitrary positive threshold"
by time-translation invariance, and Pólya's theorem explains persistence of
real-rootedness after. The Taylor-model remainder (8)–(9) is correct and
loose by 10–60×, and is paid on `|z| ≤ 1`, where `H_t` has no zero at any
`t` (`min |H_t| ≈ 0.062`); reaching the first zero needs `M ≈ 28` terms with
14 digits of cancellation, and reaching the sector is impossible in
principle (`e^{αRu}` with `log_10 ≈ 5·10^9`). Close.

**15 lee_yang.** Outward enclosure of the theta moments (correct interval
arithmetic; delivers ~5 digits, not the 42 the precision setting suggests)
and two one-line exclusions: iid equal Rademacher sums (kurtosis `3 − 2/N`
never equals 2.7911) and the two-spin ferromagnet (kurtosis ≤ 2). The
moments are classical: `I_0 = ξ(1/2)/8`, `I_2 = ξ''(1/2)/32`,
`m_2 = (1/2) Σ_γ γ^{−2}`, `m_4 − 3m_2^2 = −(3/4) Σ_γ γ^{−4}` (replayed to 25
digits). Both excluded families are lattice measures, excluded by far more
than two moments. The structural point the folder itself states empties
the direction: a ferromagnetic Lee–Yang realization at `t = 0` is RH by
Newman's theorem, and at `t > 0` it is `Λ ≤ t`. The ten-spin Curie–Weiss fit
(replayed to 12 digits) is a curiosity; no `N` closes the sixth moment.
Close.

**16 nonlinear_collective_fields.** Moment/jet hierarchy
`ṁ_j = m_{j+2} − m_2 m_j`, log-convexity of `Z_t`, no universal finite
moment closure (truncated moment problem; Legendre-`P_6` witness), Fourier
injectivity. Textbook, correct. Its identity (7) — the normalizer drops out
of the threshold test at an exact collision — is the one item of value and
is the seed of section 2.1. Close with note recording 2.1.

## 4. What to carry forward

Five things from these thirteen folders are worth keeping in the heat
manuscript or its appendix; everything else can be left in the notes.

The sum-of-squares/Laguerre form of the threshold test (2.1), with its
consequence that `L(f) < −Δ` is the exclusion itself and not an auxiliary
constraint. The standard control kernel `q_{T,b}` with Newman constant
exactly `T` (2.2), as the single counterexample against every mechanism
that uses only positivity, evenness, decay, moment signs, radial
positivity, Green/endpoint data, or memory positivity. The isometry
`‖H_0(x + i·)‖^2_{L^2(μ_t)} = Σ_j (2t)^j |H_t^{(j)}(x)|^2 / j!` (01 = 02).
The dictionary `I_0 = ξ(1/2)/8`, `I_2 = ξ''(1/2)/32`, `m_2 = (1/2) Σ γ^{−2}`,
`m_4 − 3m_2^2 = −(3/4) Σ γ^{−4}`, `J_t μ_2 = 1.0099`, Poincaré constant
`≈ 86.2`, radial positivity threshold `t_* ≈ 37.45`. And the tight tail
bound of 10 eq. (6), in case a spectral cutoff is ever needed at
`|Im z| ≤ 1`.

## 5. On the portfolio as a method

The sixteen-project fan-out was explicitly a brainstorm, and as a
brainstorm it has done its job: thirteen mechanisms are now known not to
work, with the reasons written down. The cost is that each folder reads as
if it had found something, and the aggregate (Heat Notes 15 and 16,
README) compounds that impression — "the strongest concrete geometric
result in the portfolio" (12) is Bochner positive-definiteness, and
"certified sign change" (03) is non-Gaussianity. Two habits would have
caught this on day one: asking, before writing a note, whether the
obstruction follows from the existence of one zero of ξ or from the
standard control kernel; and checking whether a certified sign still holds
at `t = 37` before calling it a result for `t ≤ 1/20`.

The missing input is the one every folder names and none supplies: a
property of the arithmetic coefficients, not of the kernel's shape, that
is incompatible with a double real zero at an all-real time. Projects 09,
13 and 17 are where the genuine (finite, certified) content lives, and
where the author's effort already is. Nothing in the thirteen folders
reviewed here should pull effort away from them.

No collision exclusion, threshold result, or RH conclusion is claimed or
refuted in this review.
