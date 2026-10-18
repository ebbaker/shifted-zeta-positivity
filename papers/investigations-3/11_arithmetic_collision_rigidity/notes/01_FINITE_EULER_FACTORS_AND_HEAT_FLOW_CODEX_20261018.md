# Finite Euler factors under heat flow and their collision interpretation

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model: **gpt-6-astra (Codex)**; reasoning effort:
**max**, verified from this turn's metadata.

**Status:** discussion and elementary derivation of the finite heat algebra,
with an explanation of existing complete-packet identities. No new arithmetic
sign estimate, collision exclusion, numerical experiment, or independent
review is claimed. The proposal's opening estimate remains unresolved.

Edward's suggestion is to express finite Euler products explicitly at positive
heat time, then reorganize the resulting terms to obtain control or positivity.
This directly connects [project 09][p09], which seeks estimates for complete
arithmetic packets, with [project 11][p11], which asks what those estimates force
near a hypothetical collision. Heat flow preserves usable finite arithmetic
identities, but replaces scalar multiplication by operators involving complex
shifts. Mixed-prime terms and half-line boundary terms are essential.

The earlier comment is recorded in the [fixed-character discussion][prior].
Use the [result summaries][summaries], especially [arithmetic bookkeeping][s14]
and [collision laws][s13], together with the [patterns to avoid][avoid],
especially [criterion classification][a01], [control screening][a02],
[scoped exclusions][a07], and [paired cancellations][a12].

## Three different finite arithmetic objects

For a finite set of primes P, distinguish:

1. The usual finite Euler product
   \(Z_P(s)=\prod_{p\in P}(1-p^{-s})^{-1}\). Its Dirichlet expansion is
   infinite: every power of each retained prime occurs.
2. A finite Dirichlet polynomial obtained by bounding those powers, or the
   finite reciprocal product \(M_P(s)=\prod_{p\in P}(1-p^{-s})\).
   The latter is a finite sum over squarefree divisors.
3. A finite Euler-factor operation on the *complete* theta transform, whose
   source still contains the full arithmetic information and decay.

The elementary heat action is exact on object 2. Object 3 has a convergent
source-integral definition at positive time. For object 1, the straightforward
termwise positive-time Dirichlet expansion diverges, even with just one prime.
These are different statements; the last is not an exclusion of other
regularized constructions.

## The exact finite sum and the interaction between primes

Use the proposal's normalization
\[
H_t=-H_{zz},\qquad s(z)=\tfrac12+\tfrac{iz}{2}.
\]
Write \(U_t=e^{-t\partial_z^2}\) on finite exponential sums. Since
\(-\partial_z^2e^{-iaz}=a^2e^{-iaz}\),
\[
U_t[n^{-s(z)}]=b_n(t)n^{-s(z)},\qquad
b_n(t)=\exp\!\left(\frac t4\log^2n\right).                 \tag{1}
\]
For fixed finite bounds \(K_p\), this gives the explicit expression
\[
U_t\!\left[\prod_{p\in P}\sum_{k=0}^{K_p}p^{-ks(z)}\right]
=\sum_{0\le k_p\le K_p}
\exp\!\left(\frac t4\Bigl(\sum_{p\in P}k_p\log p\Bigr)^2\right)
\prod_{p\in P}p^{-k_ps(z)}.                               \tag{2}
\]
The square contains the individual-prime terms and all cross terms:
\[
b_{pq}=b_pb_q\exp\!\left(\frac t2\log p\log q\right).
                                                               \tag{3}
\]
Thus heat evolution of the whole product is generally different from the
product of separately evolved factors. Already for two reciprocal factors,
\[
U_t[(1-p^{-s})(1-q^{-s})]
=1-b_pp^{-s}-b_qq^{-s}+b_{pq}(pq)^{-s},                    \tag{4}
\]
whereas multiplication of the two individually evolved factors gives
\(b_pb_q\) in the last coefficient. Even within one prime,
\(b_{p^k}=b_p^{k^2}\), rather than \(b_p^k\).

For the ordinary reciprocal local factor, the proposed termwise evolution
would be
\[
\sum_{k\ge0}\exp\!\left(\frac t4k^2\log^2p\right)p^{-ks}.
                                                               \tag{5}
\]
For every fixed \(t>0\) and finite complex s, its terms have magnitude
\(\exp(tk^2\log^2p/4-k\operatorname{Re}(s)\log p)\), which tends to
infinity. Finitely many primes therefore do not justify an infinite-power
positive-time expansion. In particular, (1) is not an ordinary convergent
Dirichlet-series representation of \(H(t,z)\).

There is a useful finite integral version of (2). For a standard real Gaussian
G and a finite exponential polynomial f,
\[
U_tf(z)=\mathbb E[f(z+i\sqrt{2t}\,G)]\quad(t\ge0).          \tag{6}
\]
Every factor in a product is evaluated using the *same* G. Replacing that
common variable by independent variables discards exactly the interactions
in (3). The positive Gaussian measure does not imply a positive result for
complex factors, or positivity of a physical Laguerre expression.

This coefficient weight also occurs in the effective finite Dirichlet sums
of the Polymath work. Tao's [2 March 2018 discussion][tao] explains using
\(\prod_{p\le P}(1-b_pp^{-s})\) as a mollifier to reduce oscillation.
That is a useful precedent for the proposed strategy, but such a mollifier
is not the exact evolution (4) of the undeformed reciprocal product. The
[Polymath paper][polymath] supplies rigorous approximations with explicit
remainder estimates; its finite sums must not be replaced by (5).

## Finite Euler operations on the complete field

Let \(f_0(z)=\frac12\int_{\mathbb R}K(u)e^{izu}\,du\), with K decaying
fast enough that the integral and every fixed real translate remain
absolutely integrable with all relevant heat weights. The theta source has
this property. Define \(f_t\) by inserting \(e^{tu^2}\) in that integral.
A change of variable proves, for real a,
\[
U_t[e^{-iaz}f_0(z)]
=e^{ta^2-iaz}f_t(z+2ita).                               \tag{7}
\]
Here the left side means heat evolution of the translated source. It does
not require claiming convergence of a differential-operator power series
on an arbitrary entire function.

Set \(a_d=\frac12\log d\) and
\[
(\mathcal T_d^tf)(z)
=d^{-1/2}e^{ta_d^2-iza_d}f(z+2ita_d).
\]
If \(Q=\prod_{p\in P}p\), then the field whose initial value is
\(M_P(s(z))H(0,z)\) has the exact finite evolution
\[
\widetilde H_P(t,z)
=\sum_{d\mid Q}\mu(d)\mathcal T_d^tH(t,z).               \tag{8}
\]
This uses the complete H at shifted arguments. It is not a closed product
formula for H in terms of the primes of P alone. Direct composition gives
\[
\mathcal T_d^t\mathcal T_e^t=\mathcal T_{de}^t,
\qquad
\widetilde H_P=\prod_{p\in P}(I-\mathcal T_p^t)H.
                                                               \tag{9}
\]
Indeed the extra factor from shifting \(e^{-iza_e}\) is
\(e^{2ta_da_e}\), producing \(e^{t(a_d+a_e)^2}\). The Euler algebra
survives as an algebra of commuting shift operators.

Multiplication by the one-sided \(M_P(s(z))\) generally loses the even and
real structure of H. Its reflected counterpart must be retained when
constructing a real physical observation. Symmetrizing (8) is valid but
changes the object under study; it cannot silently be identified with H.

## The complete half-line formula used by the proposal

The proposal works with
\[
F(t,z)=\int_0^\infty e^{tu^2+izu}\Phi(u)\,du,
\qquad H(t,z)=\tfrac12[F(t,z)+F(t,-z)].
\]
The [existing packet note][packets] proves
\[
\mathcal P_d(t,z)
=d^{-1/2}e^{ta_d^2-iza_d}
\left[F(t,z+2ita_d)-L_d(t,z)\right],                    \tag{10}
\]
\[
L_d(t,z)=\int_0^{a_d}e^{tv^2+i(z+2ita_d)v}\Phi(v)\,dv.
\]
Its source is \(D_d\Phi(u)=d^{-1/2}\Phi(u+a_d)
=\sum_{d\mid n}\phi_n(u)\), the exact divisible-index source.
The lower integral in (10) follows from translating a half-line. It is
absent from the whole-line calculation (7) because the domains differ.
The entire physical even transform of this half-line packet is
\((\mathcal P_d(t,z)+\mathcal P_d(t,-z))/2\); it is not generally
\(\mathcal T_d^tH\).

For two primes, the complete inclusion-exclusion block is
\[
\mathcal B_{p,q}=F-\mathcal P_p-\mathcal P_q+\mathcal P_{pq}.
                                                               \tag{11}
\]
This is an explicit finite-time arithmetic identity with the mixed term,
all lower integrals, and their derivatives retained. The same note proves
that the separate positive-time infinite Möbius series for the shifted
F terms and lower intervals fail the term test; the paired packet series
converges. This is a scoped obstruction to that separation, not to joint
estimates of (10) or finite blocks such as (11).

## What the formula would have to prove near a collision

At an exact double collision \((T,x_*)\), \(T>0\), let
\(c=H_{xx}(T,x_*)/2\ne0\), and write \(\varepsilon=T-t\).
On the nearby stationary branch \(H_x=0\), the established local laws give
\[
H=2c\varepsilon+O(\varepsilon^2),\quad
H_{xx}=2c+O(\varepsilon),\quad
\mathcal L_0=-4c^2\varepsilon+O(\varepsilon^2),
\]
\[
E=H^2+H_x^2=4c^2\varepsilon^2+O(\varepsilon^3),\qquad
\mathcal L_0/E=-1/\varepsilon+O(1),                     \tag{12}
\]
where \(\mathcal L_0=H_x^2-HH_{xx}\). Thus an independently proved
arithmetic estimate \(\mathcal L_0\ge-C E\), with C finite through the
event, would exclude that event. Such an estimate for this double-event
class is a restricted goal; extending the relevant criteria to all events
and multiplicities reaches the RH-equivalent target recorded in [s13][s13].
Writing the inequality is preparation, not an estimate.

The nonlocal part of (10) is unavoidable: at \(t\to T>0\), its displacement
\(2ita_d=it\log d\) tends to a fixed nonzero imaginary displacement.
After division by \(\sqrt\varepsilon\), it escapes every bounded local
collision coordinate domain. A finite local Taylor expansion cannot
evaluate that shifted observation with a controlled remainder by itself.
Also \(H=H_x=0\) does not imply \(F=F_z=0\).

Positive source coefficients, a positive Gaussian measure, or positive
operator norms do not by themselves give the required signed inequality.
An error \(O(|H|)\) is \(O(\varepsilon)\) here, whereas E is
\(O(\varepsilon^2)\). A fixed small absolute error does not become small
relative to E on approaching the event. The paired terms must be controlled
at the scale of the selected physical observable.

## Control comparison and the next bounded test

The algebra (1), (6), and (7) is generic and fails none of the colliding
controls merely by being true. It supplies no exclusion on its own.
The arithmetic identification in (10) uses additional premises:

- The weighted-square controls fail the complete constant-coefficient
  relations and full reflection. For a weighted source, prime excision
  leaves coefficient defects \(a_n-a_{n/p}\) on multiples of p.
- The reflected smooth and positive-primitive controls fail the complete
  normalized theta square expansion. Reflection and primitive positivity
  alone therefore cannot provide the proposed estimate.
- Euler-factor controls change coefficient, level, or lattice data. A
  finite tested prime list cannot simply be assumed to detect a change at
  another prime. The argument must identify the actual failed premise or
  quantitative estimate on the control's event domain.
- Generic heat germs and translated-field examples lack full theta
  arithmetic. They prevent assuming an arbitrary shifted value vanishes
  whenever the physical energy E vanishes.

These are the premise comparisons in [summary 12][s12], not newly performed
numerical tests. No proposed positive estimate has yet passed this screen.

Use the proposal's d=2 packet as the baseline. The smallest test of an
interaction between distinct primes is then the complete \(\{2,3\}\)
block (11), with divisors 1, 2, 3, 6 and the correctly reflected expression.
Keep the mixed contribution and lower intervals together before estimating.
The research question is whether this joint expression gives a new bound
on the specific exterior combination that enters \(\mathcal L_0\), with
an error controlled after the normalization (12). A factorization as a
nonnegative form would be one possible mechanism; a useful lower bound or
an independent compatibility restriction would also count.

This is a concrete route connecting 09 and 11. Existing finite identities
make it possible to begin without assuming an ordinary positive-time Euler
product. The remaining advance is a signed arithmetic consequence of their
coupling.

[p09]: ../../09_coupled_arithmetic_dilations/research-overview/01_EXPLORATORY_RESEARCH_PROPOSAL_20261018.md
[p11]: ../research-overview/01_EXPLORATORY_RESEARCH_PROPOSAL_20261018.md
[prior]: ../../brainstorm/notes/02_FIXED_CHARACTER_GOALS_AND_ARITHMETIC_COLLISION_RESEARCH_CODEX_20261018.md
[packets]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/11_MULTIPLICATIVE_DILATION_AND_COMPLETE_HEAT_PACKETS_20261015.md
[summaries]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[s12]: ../../../../result-summaries/12_collision_controls_and_screening.md
[s13]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[s14]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[tao]: https://terrytao.wordpress.com/2018/03/02/polymath15-fifth-thread-finishing-off-the-test-problem/
[polymath]: https://arxiv.org/abs/1904.12438
