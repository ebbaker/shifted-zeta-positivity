# Circle comparison and the cost of positive completion

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **ultra**, verified from this turn’s metadata.

**Status: proved in-note, with separate same-model agent review.** This is
the first bounded I4-W01 round. It gives an exact complete-form circle
comparison and an explicit exponential error, then rejects specified
positive completions and repairs. It proves no Weil positivity or RH.
No novelty priority or independent specialist validation is claimed.

Read the [result index][results] and [avoid index][avoid], especially
[finite-horizon evidence][finite], [CCM scope][ccm-summary],
[target classification][a01], [geometric re-realizations][a03],
[coupled estimates][a12] and [full-target identification][a13].
The [program][program] asks for independent positivity **and** a one-sided
comparison tending to zero on each fixed test; these are distinct gates.
The [review][review] and [small check record][record] specify verification.

## 1. Exact candidate, domains and conventions

Use the [finite-horizon manuscript, label eq:weil][weil]
for the authoritative convention. For a complex f in C_c^infinity((-L/2,L/2)), write
\[
 a(\tau)=\Re\psi(1/4+i\tau/2)-\log\pi,\qquad
 a_0=-\gamma-\pi/2-3\log2-\log\pi<0,
\]
\[
 A_{\mathbb R}[f]=\frac1{2\pi}\int a(\tau)|\widehat f(\tau)|^2d\tau,
 \quad C_\lambda(f)=\int f(x)\cosh(\lambda x)dx,
 \quad S_\lambda(f)=\int f(x)\sinh(\lambda x)dx.
\]
The transform is integral f(x)exp(-i tau x)dx. With c_n=Lambda(n)/sqrt(n)
and the zero-extended delay T_b f(x)=f(x-b), the complete target is
\[
 Q_0[f]=A_{\mathbb R}[f]+2|C_{1/2}(f)|^2-2|S_{1/2}(f)|^2
       -2\sum_{\log n<L}c_n\Re\langle f,T_{\log n}f\rangle.       \tag{1}
\]
The inner product is antilinear in its first argument. Every prime power
with nonzero correlation is retained; non-prime powers have c_n=0.

Take the circle T_P=R/PZ with its centered cell (-P/2,P/2), and the
isometric input I_P f given by zero extension in that cell. Let
U_b g(x)=g(x-b mod P), tau_k=2 pi k/P, and g_k be coefficients in the
orthonormal basis P^(-1/2)exp(i tau_k x). Define
\[
 A_P[g]=\sum_{k\in\mathbb Z}a(\tau_k)|g_k|^2,
\]
\[
 Q^\circ_{P,X}[g]=A_P[g]-2\sum_{2\le n\le X}c_n\Re\langle g,U_{\log n}g\rangle
                  +2|C_{1/2,P}(g)|^2-2|S_{1/2,P}(g)|^2.         \tag{2}
\]
Moments with a P subscript are integrated over the centered cell. They
are bounded functionals for each P; their representative weights are not
claimed to be smooth periodic sections. In particular sinh jumps at the
cut. The full logarithmic Fourier form domain is
sum_k log(2+|tau_k|)|g_k|²<infinity; prime and moment terms are bounded
perturbations there. No finite Fourier truncation is built into (2).

For the fixed-test comparison impose
\[
 P>2L,\qquad \max(2,e^L)\le X\le e^{P-L}.                     \tag{3}
\]
Such choices exist for all sufficiently large P. X may be fixed or vary
subject to (3). These are separate parameters: L is fixed test-support
length, P is circumference, X is the prime-power cutoff, and there is no
heat time or zeta shift in this central-form calculation.

## 2. Archimedean images with a paid error

Subtracting the two [digamma integrals, DLMF 5.9.16][digamma] gives
\[
 a(\tau)-a_0=2\int_0^\infty k(s)(1-\cos(\tau s))ds,
 \quad k(s)=\frac{e^{-s/2}}{1-e^{-2s}}
          =\sum_{r\ge0}e^{-\lambda_rs},\quad\lambda_r=2r+1/2.   \tag{4}
\]
The special value a_0 follows from [DLMF 5.4.19][special]. In particular
\[
 A_{\mathbb R}[f]=a_0\|f\|_2^2+
       \int_0^\infty k(s)\|f-T_sf\|_2^2ds,                   \tag{5}
\]
with the analogous circle formula using U_s. Both integrals converge:
near zero the squared difference is O(s²) for these tests, while k(s)
is O(1/s); at infinity k is exponentially decreasing. The identity also
holds for compact H^1 tests by the same argument.

Let R_f(s)=integral conjugate(f(x))f(x-s)dx. Its support is in [-L,L].
The circle autocorrelation of I_Pf is sum_j R_f(s+jP). The extra terms
vanish near s=0, so the difference of (5) is absolutely integrable, without
using a distributional Poisson formula. It yields
\[
 A_{\mathbb R}[f]-A_P[I_Pf]
 =\iint\overline{f(x)}f(y)\mathcal I_P(x-y)dxdy,\qquad
 \mathcal I_P(v)=\sum_{j\ne0}k(|v+jP|).                     \tag{6}
\]
For |v|<=L<P, summing positive exponential series gives exactly
\[
 \mathcal I_P(v)=2\sum_{r\ge0}
             \frac{\cosh(\lambda_r v)}{e^{\lambda_rP}-1}.     \tag{7}
\]
Define Image_P[f] to be the right side of (6). The hyperbolic difference
formula, with complex f allowed, gives
\[
 \boxed{\operatorname{Image}_P[f]=2\sum_{r\ge0}
       \frac{|C_{\lambda_r}(f)|^2-|S_{\lambda_r}(f)|^2}
            {e^{\lambda_rP}-1}.}                            \tag{8}
\]
All interchanges are dominated by the following uniform bound:
\[
 |\operatorname{Image}_P[f]|\le B_{P,L}\|f\|_1^2
       \le L B_{P,L}\|f\|_2^2,\quad
 B_{P,L}=\frac{2e^{-(P-L)/2}}
 {(1-e^{-P/2})(1-e^{-2(P-L)})}.                              \tag{9}
\]
Indeed 2 cosh(lambda v)<=2 exp(lambda L), each reciprocal
1/(1-exp(-lambda P))<=1/(1-exp(-P/2)), and the remaining geometric
series has ratio exp(-2(P-L)).

A pointwise positive image kernel is not a positive quadratic form.
For nonzero nonnegative even tests (8) is positive; for odd tests with
xf(x)>=0 it is negative. Parity is not being imposed on the target.

## 3. Complete arithmetic comparison and finite corrections

For 0<=b<=log X, a nonzero wrapped correlation would require
|b-jP|<L for some nonzero integer j. Condition (3) excludes this.
Consequently all prime correlations in (2) equal their zero-extended
counterparts; those with log n>=L vanish exactly. The pole moments also
agree exactly on I_Pf. Hence
\[
 \boxed{Q_0[f]-Q^\circ_{P,X}[I_Pf]=\operatorname{Image}_P[f],}
 \quad Q_0[f]\ge Q^\circ_{P,X}[I_Pf]-B_{P,L}\|f\|_1^2.        \tag{10}
\]
This is an actual one-sided estimate for the **complete signed model**.
It does not assert that the model is nonnegative. There is no omitted
source tail, no spectral projection error and no pole approximation in
(10). Outside (3), prime alias terms must be restored; making P large
while taking X past exp(P-L) is not covered.

For an integer M>=0 define a finite moment correction
\[
 Q^{\circ,M}_{P,X}[g]=Q^\circ_{P,X}[g]+2\sum_{r=0}^{M-1}
 \frac{|C_{\lambda_r,P}(g)|^2-|S_{\lambda_r,P}(g)|^2}
 {e^{\lambda_rP}-1}.                                       \tag{11}
\]
The remaining error in (10) is at most
\[
 B^{(M)}_{P,L}\|f\|_1^2,\quad
 B^{(M)}_{P,L}=\frac{2e^{-\lambda_M(P-L)}}
 {(1-e^{-\lambda_MP})(1-e^{-2(P-L)})}.                       \tag{12}
\]
This improves approximation, with an explicit price of M positive and M
negative moment ranks. It is not a positivity mechanism.

## 4. Literal positivity fails, including every finite image correction

The normalized odd circle function v_P(x)=sqrt(2/P)sin(beta x),
beta=2 pi/P, has C_{lambda,P}(v_P)=0 for every positive lambda. Direct
integration gives
\[
 Q^\circ_{P,X}[v_P]=a(\beta)-2\sum_{n\le X}c_n\cos(\beta\log n)
 -\frac{16\beta^2}{P}\frac{\sinh^2(P/4)}{(1/4+\beta^2)^2}.   \tag{13}
\]
For every real tau, (4) and 1-cos z<=z²/2 imply
\[
 a(\tau)\le a_0+B_\gamma\tau^2,\quad
 B_\gamma=\int_0^\infty s^2k(s)ds
         =16\sum_{r\ge0}(4r+1)^{-3}\le18.                  \tag{14}
\]
For the last inequality, sum_{r>=1}(r+1/4)^(-3)<=
integral_0^infinity(x+1/4)^(-3)dx=8 and B_gamma is one quarter of
the full sum including 64. The special value gives a_0+9/2<0.
Thus
\[
 P\ge\max(4\pi,4\log X)\quad\Longrightarrow\quad
                         Q^\circ_{P,X}[v_P]<0,             \tag{15}
\]
since beta<=1/2 and all prime cosines are nonnegative. Every correction
in (11) is nonpositive on this odd function. The same witness disproves
nonnegativity of Q^{circ,M} for **every finite M**, not only fixed M.

These are delocalized circle tests. They are not tests in the fixed
input image I_P C_c^infinity((-L/2,L/2)). There is no contradiction with
finite-horizon Weil positivity and no conclusion that Q_0[f] is negative.

A quantitative index version is also useful. Put
\[
 W_X=\sum_{n\le X}c_n,\quad D_X=2W_X-a_0>0,\quad
 B_X=B_\gamma+\sum_{n\le X}c_n(\log n)^2,\quad
 \eta_X=\sqrt{D_X/(2B_X)}.
\]
The diagonal symbol b_X(tau)=a(tau)-2 sum c_n cos(tau log n)
is at most -D_X/2 on |tau|<=eta_X. In the
N=2 floor(P eta_X/(2 pi))+1 dimensional Fourier block, imposing C=0
leaves at least N-1 strictly negative directions. After M moment corrections,
a self-adjoint addition whose positive spectral subspace has dimension
at most r, and a restriction of codimension q, the negative index is at least
\[
                 \max(0,N-1-M-r-q).                        \tag{16}
\]
Assume the added form is defined on this finite Fourier block and use the
common form domain for the restriction. Intersect the block with the kernels
of the positive functionals, the orthogonal complement of the positive
spectral subspace, and the restriction: dimension drops
by at most their listed ranks; every remaining added term is nonpositive.
For fixed X this defeats every fixed-rank repair as P grows. No uniform
eta_X is claimed for arbitrary growing-cutoff schedules.

## 5. A genuinely nonnegative candidate, and its exact failed comparison

Use the jump structure to define the explicit positive energy
\[
 E_{P,X}[g]=(A_P[g]-a_0\|g\|_2^2)
       +\sum_{n\le X}c_n\|g-U_{\log n}g\|_2^2
       +2|C_{1/2,P}(g)|^2\ge0.                             \tag{17}
\]
Positivity follows from (5) and c_n>=0; it assumes no Weil sign. Unitarity
of each U gives the **complete discrepancy**
\[
 E_{P,X}[g]-Q^\circ_{P,X}[g]=D_X\|g\|_2^2+2|S_{1/2,P}(g)|^2.
\]
Combining with (10),
\[
 \boxed{Q_0[f]-E_{P,X}[I_Pf]
 =\operatorname{Image}_P[f]-D_X\|f\|_2^2-2|S_{1/2}(f)|^2.}   \tag{18}
\]
Thus any allowance in Q_0[f]>=E_{P,X}[I_Pf]-epsilon_P[f] obeys
\[
 \varepsilon_P[f]\ge D_X\|f\|_2^2+2|S_{1/2}(f)|^2
                      -B_{P,L}\|f\|_1^2.                  \tag{19}
\]
For fixed X and every nonzero fixed f its lower limit is strictly positive.
For any varying X satisfying (3), D_X>=-a_0 already prevents a zero limit.
So (17) fails the program’s vanishing-error comparison for this input map.

The pole term is not the sole reason. If nonzero phi is smooth and compactly
supported, then f=(d²/dx²-1/4)phi is nonzero and integration by parts gives
C_{1/2}(f)=S_{1/2}(f)=0. The fixed defect remains D_X||f||². Nor do inactive
primes disappear in (17): a delay beyond the support contributes
2c_n||f||² to its jump square, although its exact correlation in (1) is zero.
Its diagonal subtraction in (18) is essential. This is an explicit
candidate-specific cost, not an assertion that every positive energy fails.
The general scalar-offset trap was already recorded in [CCM’s founding
note][ccm-offset]; the new content here is the paid circle comparison and
its exact cost for (17).

## 6. A stronger screen: nonnegative Fourier-diagonal repairs

Let R_{P,X} be any nonnegative Fourier multiplier with coefficients r_k,
finite on the tested modes, such that Q^circ_{P,X}+R_{P,X}>=0 on its form
domain, including trigonometric polynomials and the fixed embedded test.
This covers any successful nonnegative Fourier-diagonal repair. Clipping
the diagonal symbol alone need not make the full pole-perturbed form
positive: on the odd witness it can leave the negative sinh moment. The
theorem does not cover the spectral positive part of the complete rank-two
perturbed operator, which need not be Fourier diagonal.

Set
\[
 K=\left\lfloor\min\{P/(6\log X),P/(8\pi)\}\right\rfloor.
\]
For |k|<=K, |tau_k|<=1/4 and |tau_k log n|<=pi/3, so (14) implies
b_X(tau_k)<=-W_X. At most one coefficient b_X(tau_k)+r_k can remain
negative: two such Fourier modes would have a nonzero combination in
ker C_P, where the other pole term is nonpositive. Therefore
\[
 r_k\ge W_X\quad\hbox{on all but at most one of these }2K+1\hbox{ modes}.
                                                                    \tag{20}
\]
Choose a fixed smooth compact f with m_f=integral f nonzero. If X tends
to infinity and log X=o(P), then for all sufficiently large parameters
|fhat(tau_k)|>=|m_f|/2 throughout this band, and K>=P/(12 log X).
Using (I_Pf)_k=P^(-1/2)fhat(tau_k) yields
\[
 R_{P,X}[I_Pf]\ge\frac{K W_X|m_f|^2}{2P}
             \ge\frac{W_X|m_f|^2}{24\log X}.                \tag{21}
\]
This diverges without a prime-number theorem. For integer n, the valuation
of binom(2n,n) at each prime is a sum of zeros and ones over powers up to
2n, so binom(2n,n) divides lcm(1,...,2n). Also
binom(2n,n)>=2^(2n)/(2n+1). Taking 2n=2 floor(X/2) gives
\[
 \psi(X)=\sum_{j\le X}\Lambda(j)
 \ge (X-2)\log2-\log(X+1),\qquad W_X\ge\psi(X)/\sqrt X.      \tag{22}
\]
Here psi(X) in (22) is Chebyshev’s function, **not** the digamma psi in
(4). Thus W_X/log X tends to infinity. Conditions (3) hold eventually
for each fixed f under the displayed schedule. By (10),
(Q^circ+R)[I_Pf]-Q_0[f]=R[I_Pf]-Image_P[f] diverges, so this class of
repairs cannot supply a vanishing fixed-test comparison either.

This excludes diagonal corrections for the specified schedule, not
non-diagonal arithmetic couplings, different input maps, or every joint
cutoff schedule. Equation (16) separately excludes bounded-rank repairs
at fixed X. Growing-rank non-diagonal arithmetic repair remains outside
these theorems and would owe its own complete comparison.

## 7. Controls, comparison and decision

The matched comparator throughout is the original complete form (1) on
the **same** fixed f. Pole terms, prime delays and every Fourier mode are
retained analytically. The only error in (10) is the explicitly signed
archimedean image; (18) retains its nonvanishing diagonal/pole cost.
There is no hidden change of norm or claim of superiority based on a
less informed comparator.

The [checker][checker] independently compares real-line autocorrelation
integration with truncated Fourier sums and with the moment-image series.
It checks even and odd signs, exact cyclic jump identities, exact rational
autocorrelations, the elementary binomial divisibility and the odd global
circle witness. The [receipt][record] records 144 exact integer/rational
checks and floating diagnostics. At P=8, L=2, X=8, the even/odd compact
H^1 controls have image discrepancies about +0.038899 and -0.000267900;
the 4096-mode Fourier residuals are below 1.3e-10. At P=16 the odd circle
witness has form about -711.987. These numbers are **not interval certificates**,
new theta-zero data or the proof of the analytic theorems. Finite truncation
is confined to these diagnostics. The two fixed test values do not establish
a new finite-horizon positivity certificate.

The existing [paired-collar seam control][n19] remains valid: endpoint
trace zero is not zero collar interaction. The pointwise-positive image
kernel versus odd negative quadratic value is an additional sign control.
A pole-null smooth test shows why merely removing the negative pole does
not repair the completion.

The [arithmetic collision families][controls] screen any attempted upgrade
from positive auxiliary energy to theta exclusion. Euler-factor controls
change canonical arithmetic; weighted-square/finite-prime sources lack
full normalized reflection; reflected/primitive sources lack canonical
square coefficients. These distinct families have not been merged or
assigned new event data. No physical heat-field estimate is proposed here,
so no fresh theta collision replay is claimed: the analytic screen is that
(17) is positive using only nonnegative weights and no distinguishing
full-source relation. These results supply no premise that excludes a
catalogue collision. This respects [avoid 02][a02] and the
[scope rule][a07].

**Decision.** Complete I4-W01 for this bounded candidate class, with a
failed positivity/comparison gate. Retain (10)–(12) as explicit approximation
tools. Stop literal sampled-circle positivity and finite image corrections
as a positivity fix in the cutoff regime (15), fixed-rank repairs in (16),
the unrenormalized energy (17) under (3), and diagonal repairs when
X tends to infinity with log X=o(P) as in Section 6. Other schedules are
not excluded by these statements. I4-W02 remains gated.
This candidate is not the Connes–Consani–Moscovici construction: periodic
Fourier coordinates for the original interval operator preserve its
non-diagonal matrix and seam data. The current [CCM gates][ccm] are unchanged.

The program’s next priority is I4-S01: a coupled unchanged-theta source
restriction with a signed consequence. A later compact candidate must
identify genuinely different arithmetic coupling and a paid fixed-test map,
not merely increase spectral resolution or remove a fixed set of modes.

[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[finite]: ../../../../result-summaries/02_finite_horizon_certificates.md
[ccm-summary]: ../../../../result-summaries/08_character_channels_ccm_and_detector.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a13]: ../../../../avoid/13_a_factor_is_not_the_target.md
[program]: ../../research-overview/01_COMPACT_GEOMETRY_HEAT_TRANSPORT_AND_WEIL_POSITIVITY_PROGRAM_20261021.md
[weil]: ../../../weil-positivity/shifted-zeta/weil-depth/manuscript/finite_horizon_weil.tex
[n19]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/19_COMPACT_SURFACE_SEQUENCES_AND_WEIL_POSITIVITY_20261021.md
[ccm]: ../../../investigations/ccm-operator-realizations/README.md
[ccm-offset]: ../../../investigations/ccm-operator-realizations/notes/CCM_SPECTRAL_OPERATORS_AND_CHIRAL_REALIZATION_20260926.md
[digamma]: https://dlmf.nist.gov/5.9.E16
[special]: https://dlmf.nist.gov/5.4.E19
[checker]: ../numerics/check_circle_comparison.py
[record]: ../numerics/CIRCLE_COMPARISON_CHECK_20261021.json
[review]: ../reviews/01_CIRCLE_COMPARISON_REVIEW_20261021.md
