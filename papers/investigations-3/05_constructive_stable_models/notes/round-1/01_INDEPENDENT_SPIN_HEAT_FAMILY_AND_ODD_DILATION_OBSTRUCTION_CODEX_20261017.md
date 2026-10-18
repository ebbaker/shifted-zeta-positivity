# Round 1: independent spin heat models and an odd-dilation obstruction

> Update, 17 October 2026: the [cross-model review](../../reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md) found no mathematical error in the scoped round-one claims. The [round-two reconciliation](../round-2/README.md) supersedes the weak-convergence limitation and the unbounded-base-time exception. The original derivation below is retained as the reviewed record; scope corrections and classical attributions are in round two. Recorded updater: gpt-6.1-sol (Codex), effort ultra, with substantial LLM assistance for Edward Baker.


17 October 2026. Prepared for **Edward Baker** with substantial LLM assistance.
Recorded session: **gpt-6.1-sol (Codex), reasoning effort ultra**.
Same-model subagents checked the spin theorem, convergence argument and
finite arithmetic. These checks are not cross-model or specialist human review.

**Status:** analytic family audit with a finite Acb sign certificate. The
independent unequal-amplitude Rademacher seed is excluded as a theta
approximation, even with arbitrarily many spins. Its heat deformation is
admissible and exactly compatible, but cannot supply the required initial
approximation. Initially interacting ferromagnets and other elementary
measures remain open. Formal round review is pending.

## 1. Question, inherited results and target classification

The [initial proposal](../../research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md)
asks for one explicit family, an independent real-zero mechanism, and a
nontrivial compatibility test. We select independent spins of arbitrary
positive amplitudes at time zero, then apply the exact quadratic heat weight.
This is a nomination and disposition by the actual serving Codex model;
the proposal's suggested Claude construction/review has not occurred.

The [predecessor program](../../../../investigations-2/active/13_stability_jensen_lee_yang/notes/INITIAL_RESEARCH_PROGRAM_20261013.md)
and [earlier spin scout](../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/15_lee_yang/notes/1_THETA_MOMENT_ENCLOSURE_AND_FERROMAGNETIC_SPIN_SCREEN_20261010.md)
already exclude independent equal-amplitude spins by the second and fourth
theta moments. The present test permits unequal amplitudes, changing spin
counts and arbitrary triangular arrays. It establishes a different,
structural obstruction to their limiting approximation.

The governing [result index](../../../../../result-summaries/README.md) and
[avoid index](../../../../../avoid/README.md), especially
[collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md),
[target reformulations](../../../../../avoid/01_restating_the_target.md),
[scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [normalizations](../../../../../avoid/08_normalization_and_constant_slips.md),
fix the interpretation. Constructing real-zero approximants converging to
the complete theta transform at time zero would imply RH; we do not assume
or establish that construction. The bounded output here is an explicit
approximation-error floor for a specified family, rather than evidence for
a global RH-strength criterion.

Use the inherited normalization
\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},
\quad
H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du.
\]
Write \(I_{2k}(t)=\int_0^\infty u^{2k}e^{tu^2}\Phi(u)\,du\),
\(a_k=I_{2k}/(2k)!\), and \(\gamma_k=k!a_k\). Thus
\[
\partial_tH_t=-\partial_z^2H_t,\qquad
H_0(z)=\frac18\xi\!\left(\frac12+\frac{iz}{2}\right).
\tag{1}
\]
Equation (1) is the exact dictionary in the canonical
[collision manuscript, setup equations](../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex).
All numerical values below use this normalization.

## 2. One explicit family and its independent stability theorem

For each finite \(N\), let \(b_j>0\), let \(\sigma_j\) be independent uniform
signs, and set
\[
S_N=\sum_{j=1}^N b_j\sigma_j,\quad
Z_N(t,h)=\mathbb E e^{tS_N^2+hS_N},\quad
Q_N(t,z)=Z_N(t,iz).
\tag{2}
\]
Parameters may depend arbitrarily on the approximant index. A fixed
positive mass, for example \(I_0(0)\), may multiply (2) when comparing to
\(H_t\). At time zero,
\[
Z_N(0,h)=\prod_j\cosh(b_jh),\qquad Q_N(0,z)=\prod_j\cos(b_jz).
\tag{3}
\]
For real \(t\ge0\), expand the same quadratic weight:
\[
Z_N(t,h)=e^{t\sum_jb_j^2}2^{-N}
\sum_{\sigma}\exp\!\left(
\sum_{i<j}2tb_ib_j\sigma_i\sigma_j+\sum_jb_jh\sigma_j\right).
\tag{4}
\]

The applicable primary theorem is
[Fröhlich–Rodriguez, Theorem 1, printed p. 3, equations (2.1)–(2.4)](https://arxiv.org/pdf/1205.6643#page=3).
Its hypotheses are verified directly: every unit-spin measure is even and
compactly supported, hence has every Gaussian moment; its elementary
Laplace transform \(\cosh h_j\) has no zero when \(\Re h_j>0\);
all pair couplings in (4) are nonnegative; and \(h_j=b_jh\) has positive
real part for every site if \(\Re h>0\). The theorem gives nonvanishing
there. Global spin-flip symmetry gives the other half-plane. Consequently
all zeros of \(Q_N(t,\cdot)\) are real for every real \(t\ge0\).
No commensurability of the amplitudes is required, and no negative-time
preservation is claimed. Repeated real zeros are allowed.

## 3. Coefficient constraints and the exact heat law

Put \(P_k=\sum_jb_j^{2k}\). At time zero, ordinary cumulants give
\[
m_2=P_1,\quad m_4=3P_1^2-2P_2,\quad
\kappa_4=-2P_2,\quad\kappa_6=16P_3,
\tag{5}
\]
where \(m_{2k}=\mathbb E S_N^{2k}\). These follow by expanding
\(\log Z_N(0,h)=\sum_j\log\cosh(b_jh)\). Cauchy–Schwarz on the
squared amplitudes yields the first finite-size compatibility inequality
\[
N\ge\frac{P_1^2}{P_2}
=\frac{2}{3-m_4/m_2^2}.
\tag{6}
\]
The earlier outward theta enclosure gives the right side in
\((9.56874446,9.57944140)\). Hence any finite independent unequal-amplitude
model matching these two moments must have **at least ten nonzero spins**.
Unlike the old equal-weight test, (6) does not exclude all integers: unequal
amplitudes can satisfy this first condition.

A further exact necessary inequality is
\[
P_1P_3\ge P_2^2
\quad\Longleftrightarrow\quad
m_2m_6+9m_2^2m_4-6m_2^4-4m_4^2\ge0.
\tag{7}
\]
We do not need a new sixth-moment enclosure to decide this family, because
the bounded obstruction below applies to every choice of amplitudes.
These power-sum constraints concern the independent spin representation;
they are not generic Hankel positivity of the source measure, coefficient
Toeplitz positivity, or an all-degree Jensen theorem.

The very same parameters in (2) obey
\[
\partial_tZ_N=\partial_h^2Z_N,\quad
\partial_tQ_N=-\partial_z^2Q_N,\quad J_{ij}(t)=2tb_ib_j.
\tag{8}
\]
If \(A_{N,k}(t)=\mathbb E[S_N^{2k}e^{tS_N^2}]/(2k)!\), then
\[
A_{N,k}'=(2k+2)(2k+1)A_{N,k+1},\qquad
(k!A_{N,k})'=2(2k+1)(k+1)!A_{N,k+1}.
\tag{9}
\]
This agrees with the theta \(a_k,\gamma_k\) dictionary. A fixed mass
multiplier is harmless. Normalizing anew at each time instead gives
\(\partial_tM_N=\partial_h^2M_N-\mathbb E_t[S_N^2]M_N\);
it does not obey the unadjusted equation (8). No time-dependent refitting
of amplitudes or couplings is used.

## 4. Odd dilation of zeros and a certified error floor

**Lemma.** Let
\(f(z)=g(z)\prod_{j=1}^N\cos(b_jz)\), with \(g\) a zero-free entire
function and real \(b_j\). If \(f(r)=0\), then \(f(qr)=0\) for every odd
integer \(q\).

Indeed some factor has \(b_jr=\pi(\ell+1/2)\). Multiplying by an odd
integer gives another zero of that same cosine. This holds with changing
spin counts, unequal amplitudes and zero-free Gaussian multipliers.

The property survives convergence uniformly on complex compact sets to a
nonzero entire function. If the limit vanishes at \(r\), Rouché's theorem
on successively smaller disks supplies approximant zeros \(r_n\to r\).
Their forced zeros \(qr_n\) tend to \(qr\), so compact convergence forces
the limit to vanish at \(qr\). Simplicity is unnecessary.

For the actual theta field, let
\[
a=28.26945,\quad b=28.26946,\quad
B=[3a,3b]=[84.80835,84.80838].
\]
The [bounded certificate](../../numerics/round-1/HARMONIC_SIGN_CERTIFICATE.json)
encloses the complete field through (1):

| Input | Certified outer interval for \(H_0\) |
| --- | --- |
| \(a\) | \((2\cdot10^{-11},3\cdot10^{-11})\) |
| \(b\) | \((-9\cdot10^{-10},-8\cdot10^{-10})\) |
| Every real \(x\in B\) | \((-3.68\cdot10^{-13},-3.67\cdot10^{-13})\) |

Continuity therefore gives a real zero \(r\in(a,b)\), while
\(H_0(3r)\ne0\). This uses neither RH nor simplicity, nor a claim that
this is the first zero. Thus the complete theta transform is **not** a
nonzero complex-compact limit of independent spin cosine products,
including products multiplied by zero-free entire functions.

There is also an explicit bounded approximation statement. Put
\[
K=[a,b]\cup B,\qquad \delta=\frac{36}{10^{14}}=3.6\cdot10^{-13}.
\]
For every real continuous function on \(K\) of the form
\[
f(x)=g(x)\prod_{j=1}^N\cos(b_jx),\qquad g(x)\ne0\ (x\in K),
\]
one has
\[
\boxed{\ \|f-H_0\|_{C(K)}\ge3.6\cdot10^{-13}.\ }
\tag{10}
\]
To prove (10), suppose the error were smaller than \(\delta\). The
certified endpoint margins force \(f(a)>0\) and \(f(b)<0\), so \(f\)
has a zero \(r_f\in(a,b)\). Since \(g\) never vanishes, a cosine factor
does, and hence \(f(3r_f)=0\). But the certified theta margin throughout
\(B\) is larger than \(\delta\), a contradiction. In particular (10)
also lower-bounds uniform error on \([0,85]\). It holds for every finite
spin count; increasing the count or matching more moments cannot remove it.

The enclosure uses exactly three Acb evaluations at 160 bits and no
source truncation. The formula is
\[
H_0(x)=\frac{s(s-1)}{16}\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad s=(1+ix)/2.
\]
One evaluation uses a ball covering the **whole** interval \(B\), rather
than sampling its endpoints. Reality on the real axis follows from the
xi functional equation. The implementation uses rigorous rectangular
complex enclosures as described in the
[official python-flint documentation](https://python-flint.readthedocs.io/en/latest/general.html#inexact-numbers-and-numerical-evaluation)
and [Acb zeta documentation](https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.zeta).
The [replay guide](../../numerics/round-1/README.md) records the fixed
budget, requested radius, scout/replay distinction and dependencies.
The library and exact xi dictionary are the analytic imports; printed
digits and hashes do not replace them or the proof of (10).

## 5. Heat convergence has a paid domain, but cannot start from this seed

For completeness, the same family's tail control can be proved without
assuming theta stability. If \(V=\sup_N\sum_jb_{N,j}^2<\infty\), then
\(\mathbb E e^{hS_N}\le e^{Vh^2/2}\) for real \(h\). Gaussian integration
therefore gives
\[
\mathbb E e^{qS_N^2}\le(1-2Vq)^{-1/2},\qquad 0\le q<1/(2V).
\tag{11}
\]
For a compact set with \(\Re t\le T<1/(2V)\), \(|h|\le R\), choose
\(\max(T,0)<q<q'<1/(2V)\). Every fixed derivative of the integrand is
bounded by a constant times \(e^{qS_N^2}\). Bound (11) with \(q'\)
controls its tails uniformly. Weak convergence of the spin laws, if it
existed, would consequently give convergence of the heat transforms and
each fixed differentiated transform uniformly on these complex compact
sets, by truncation and uniform derivative bounds.

If \(Q_N(0,z)\) converged complex-compactly to \(H_0(z)/I_0(0)\), then
derivative convergence would give \(\sum_jb_{N,j}^2\to m_2\). The inherited
enclosure \(m_2<0.011552651<0.012\) would allow a uniform eventual
\(V=0.012\), and hence the conservative domain \(\Re t<125/3\), which
contains the physical interval \([0,1/2]\). However, section 4 already
disproves that initial complex-compact convergence. A useful heat majorant
does not supply a missing admissible initial approximation.

## 6. Collision controls and precise scope of the decision

The construction hypothesis doing the work is independent spin preparation
plus the stated convergence, not positivity, reflection or square support.
The [canonical controls](../../../../../result-summaries/12_collision_controls_and_screening.md)
screen the proposed general implication as follows. A nonzero compact
limit of the real-zero functions (2) must itself have only real zeros at
each covered real time, by Hurwitz.

| Control | Exact failed premise if the stable approximation were asserted |
| --- | --- |
| Euler-factor controls with \(0<c<1\) | Their explicit factor \(1+c\cos(ax)\) already has nonreal zeros at time zero. Convergence to them from real-zero approximants at that time fails. |
| Weighted-square controls with nondegenerate collision time \(T>0\) | At a sufficiently close earlier time \(T-\varepsilon>0\), the collision pair is nonreal. Complex-compact convergence of (2) at that slice fails. |
| Reflected super-Gaussian collision control | The same pre-collision nonreal pair prevents convergence on a time interval containing that predecessor. Full reflection does not supply independent spin preparation. |
| Smooth and positive-primitive positive-threshold controls | Their positive threshold supplies a nonreal zero at some positive pre-threshold time. Uniform stable approximation over all those time slices fails despite the retained positive auxiliary channel. |

A double real zero at the collision time itself is compatible with
Lee–Yang; the contradictory slice is an earlier one. The controls need not
fail the same source property. No unsupported moment failure is assigned
to any of them.

**Round-one decision:** stop the independent-at-time-zero unequal-spin
candidate. It has an independently verified stability mechanism, exact
heat compatibility, a first coefficient constraint, a justified hypothetical
heat-convergence domain, and a certified obstruction to its actual theta
limit. No larger moment fit is warranted for this class.

This is not an exclusion of all ferromagnets. A new nomination may start
with \(J_{ij}(0)\ge0\) already nonzero, use different independently
admissible elementary measures, or give a different stability-preserving
construction. Such a nomination must address why its initial transform
avoids the odd-dilation constraint and must supply an actual approximation
estimate. The result here does not decide constructions based at changing
negative times or positive-time approximation without a controlled limit
to zero. A separate round review should check this bounded disposition
before any manuscript milestone or expansion.

**Continuation, 17 October 2026:** [Note 02](02_INTERACTING_FERROMAGNETS_AND_OTHER_STABLE_SEEDS_CODEX_20261017.md) examines initially interacting ferromagnets and other stable seeds at the user’s request before round review. It retains the independent-spin exclusion here and specifies an admissible coupled quartic-block architecture; no theta approximation theorem has been obtained.
