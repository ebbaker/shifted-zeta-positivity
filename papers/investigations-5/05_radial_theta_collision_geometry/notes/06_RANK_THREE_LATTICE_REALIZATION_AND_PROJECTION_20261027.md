# Rank three lattice realizations of the radial theta profile

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Research conversation: **Review radial theta collision work**, Investigation05 chat0002, thread 01a17ee9-ed08-7271-9f66-04ac5ee516b8.

Edward Baker proposed finding a genuine lattice in Z^3 that recreates the spherically symmetric profile A(r), so that the higher-dimensional interpretation has a lattice origin. This note tests direct equality, constructs an exact geometric marginal, and gives a uniform approximation from a full-rank integer sublattice.

**Status: elementary analytical feasibility results with same-assistant checking.** An ordinary full-rank three-dimensional Gaussian lattice trace cannot equal the rank-one profile exactly. An exact transverse marginal of the cubic torus heat kernel recovers it. The full-rank lattice Z x 3Z x 3Z approximates A with relative error below 9 x 10^(-11) throughout r>=1. These statements concern the profile and its representation; no new collision exclusion or physical first-jet margin is obtained.

The [result index](../../../../result-summaries/README.md), especially [theta identities and lattice projections](../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [geometric realizations](../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md), and the [avoid index](../../../../avoid/README.md), especially [coordinate lifts](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [scoped conclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [target restatements](../../../../avoid/01_restating_the_target.md), fix the interpretation. The results below are representation identities, an approximation bound, and scoped obstructions; no new RH-equivalent criterion is proposed.

## The profile and the meaning of a lattice realization

The original profile is

\[
A(r)=\sum_{n\ge1}e^{-\pi n^2r^2},\qquad
\Theta_1(r)=1+2A(r).
\]

Writing A(|y|) makes a spherically symmetric function on R^3. In this existing construction the mode index is still n in Z. The use of the three-dimensional radial Laplacian in Note01 is exact, but does not itself give a rank-three lattice of modes.

For a full-rank lattice Lambda=B Z^3 in Euclidean R^3, the natural Gaussian trace is

\[
\Theta_\Lambda(r)=\sum_{v\in\Lambda}e^{-\pi r^2|v|^2},
\qquad
A_\Lambda(r)=\frac{\Theta_\Lambda(r)-1}{2}.
\tag{1}
\]

For an integer sublattice, B can be taken to be an invertible integer matrix. The impossibility argument below allows any invertible real B, so changing angles, lengths, or the lattice covolume does not evade it.

In (1), r is a Gaussian scale parameter. A spatial heat kernel on R^3/Lambda also has a three-component position variable. A trace, a transverse marginal, and a spherical average of that spatial kernel are different observations. A cubic lattice has discrete cubic symmetry; it is not invariant under every spatial rotation. The scalar trace in (1) should not be confused with an unaveraged spherically symmetric spatial lattice density.

## The cubic lattice has additional shells

Let q=exp(-pi r^2). Product factorization gives

\[
\Theta_{\mathbb Z^3}(r)=\Theta_1(r)^3.
\tag{2}
\]

The first terms are

\[
\Theta_1=1+2q+2q^4+2q^9+\cdots,
\]
\[
\Theta_{\mathbb Z^3}
=1+6q+12q^2+8q^3+6q^4+24q^5+\cdots.
\tag{3}
\]

For example, the vectors (+/-1,+/-1,0) and their permutations produce the twelve q^2 terms. Those squared lengths do not occur in the target series. Multiplying the nonconstant part by 1/3 matches the first shell but leaves these additional shells.

The finite [checker](../numerics/06_check_rank_three_lattice_lift_20261027.py) enumerates every shell through squared norm 16 and verifies (2) by exact convolution. The infinite obstruction does not depend on this finite enumeration.

## Direct full-rank equality is impossible

For every fixed full-rank lattice in R^3,

\[
\Theta_\Lambda(r)\sim\frac1{|\det B|\,r^3}
\qquad(r\downarrow0),
\tag{4}
\]

whereas

\[
\Theta_1(r)\sim r^{-1}.
\tag{5}
\]

A direct proof of (4) is the Gaussian Riemann sum

\[
r^3\sum_{m\in\mathbb Z^3}e^{-\pi|B(rm)|^2}
\longrightarrow
\int_{\mathbb R^3}e^{-\pi|Bx|^2}\,dx
=|\det B|^{-1}.
\]

Gaussian decay controls the tails of the Riemann sums; on compact sets ordinary Riemann convergence applies. The same argument in one dimension proves (5).

Thus no fixed multiplicative normalization, fixed length rescaling, or additive constant can turn the complete trace of a full-rank three-dimensional lattice into Theta_1, or its nonconstant half into A. Both functions are holomorphic in s=r^2 on Re(s)>0. Consequently exact equality only on r>=1, or on any nonempty open r-interval, would extend to all r>0 and contradict (4)-(5).

This excludes direct equality of these Gaussian traces. It does not exclude approximation on r>=1, marginals, nontrivial observation operators, or other kernels derived from a lattice.

There is a second obstruction that also covers fixed positive weights on every lattice point. Suppose

\[
\sum_{v\in\Lambda}w_v e^{-\pi r^2|v|^2}=\Theta_1(r),
\qquad w_v>0,
\tag{6}
\]

with absolute convergence for every r>0. Uniqueness of a discrete Laplace series forces the total weight on each squared-length shell to equal the target coefficient. One elementary proof successively isolates the smallest differing exponent by letting r tend to infinity; convergence at a smaller fixed positive r dominates the remaining tail. Therefore every lattice vector must have integer length, since nonsquare shells have zero target coefficient and positive weights cannot cancel.

No lattice containing two independent vectors can have integer lengths for all its vectors. Choose independent u,v and let |v|=k be an integer. If all lengths b_n=|u+nv| were integers, then b_(n+1)-b_n would be an integer tending to k. It would eventually equal k exactly. Hence b_n=kn+c for all sufficiently large n. Comparing its square with

\[
|u+nv|^2=k^2n^2+2(u\cdot v)n+|u|^2
\]

gives (u dot v)^2=|u|^2|v|^2, contradicting independence.

This strengthens the direct obstruction to fixed full-support positive spectral weights. It does not cover weights allowed to vanish on unwanted shells, signed cancellation, or weights depending on the observation scale. Choosing weights solely to reproduce the desired shell coefficients would encode the target; an independently specified geometric reason for those weights would still be needed.

## An exact parent on the three-dimensional torus

There is nevertheless a genuine three-dimensional heat system with an exact recovery map. On the unit flat torus T^3=R^3/Z^3 let

\[
K_3(s;\theta_1,\theta_2,\theta_3)
=\sum_{m\in\mathbb Z^3}
e^{-\pi s|m|^2}e^{2\pi i m\cdot\theta},
\qquad
\partial_sK_3=\frac1{4\pi}\Delta_{\mathbb T^3}K_3.
\tag{7}
\]

Define the transverse marginal with normalized Haar measure:

\[
(PF)(\theta_1)=
\int_0^1\int_0^1
F(\theta_1,\theta_2,\theta_3)\,d\theta_2d\theta_3.
\]

Fourier orthogonality gives exactly

\[
PK_3(s;\theta_1)=
\sum_{n\in\mathbb Z}e^{-\pi s n^2}e^{2\pi in\theta_1}
=K_1(s;\theta_1),
\]
\[
\boxed{A(r)=\frac{(PK_3)(r^2;0)-1}{2}.}
\tag{8}
\]

This uses a real rank-three lattice and a standard geometric integration map. It is not a direct equality between the two complete lattice traces. Transverse modes with (m2,m3) different from (0,0) are removed by P.

Periodicity also gives P Delta_T3=partial_theta1^2 P. Thus this is an exact dimensional reduction of the three-dimensional heat equation. For the present product heat kernel the observed and unobserved Fourier sectors evolve independently.

The complete theta source is recovered as well. Set x=log r, D=partial_x and w_t=exp(tx^2/4+x/2). Define

\[
\mathscr G_3(t,x,\theta)
=w_t(D^2+D)K_3(e^{2x};\theta).
\]

Uniform convergence on compact positive s-sets permits P to commute with the source derivatives, and

\[
(P\mathscr G_3)(t,x,0)
=4e^{tx^2/4}\Phi(x/2)=g_t(x).
\tag{9}
\]

The original physical heat transform can then be applied to this recovered complete source. No separate whole-line transform of unrecombined lattice sectors is assumed.

The limitation of this particular lift is explicit: the transverse modes disappear from the observation and do not feed the retained mode under the linear heat equation. Extra dimensions have a genuine parent geometry, but no additional physical sign constraint follows from their existence. A stronger coupled observation or estimate remains a separate problem.

The repository already contains a more elaborate [finite E8 character projection](../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/48_E8_CHARACTER_PROJECTION_AND_SIGNED_HEAT_SECTORS_20261015.md). It recovers a source product with a transverse normalization and retains the missing signed estimate. The present torus marginal is an elementary related construction, with no novelty claim.

## A full-rank integer lattice approximates A uniformly on the physical half-line

Take the concrete lattice

\[
\Lambda_L=\mathbb Z\times L\mathbb Z\times L\mathbb Z,
\qquad L\in\mathbb N,\quad L\ge2.
\]

Its complete unprojected trace is

\[
\Theta_{\Lambda_L}(r)=\Theta_1(r)\Theta_1(Lr)^2.
\tag{10}
\]

This is a full-rank lattice of covolume L^2. Write a=A(r), b=A(Lr) and q=exp(-pi r^2). Then

\[
A_{\Lambda_L}-A=2b(1+b)(1+2a).
\tag{11}
\]

For n>=1, n^2>=1+3(n-1). Hence, for r>=1,

\[
q\le a\le\frac q{1-q^3},
\qquad
b\le\frac{q^{L^2}}{1-q^{3L^2}}.
\]

The inherited bound pi>3 and the exact Taylor inequality
sum_(j=0)^8 3^j/j!>20 imply q<1/20. Put

\[
d_L=\frac{20^{-L^2}}{1-20^{-3L^2}}.
\]

Equations (10)-(11) give the complete uniform bounds

\[
0<
\frac{\Theta_{\Lambda_L}-\Theta_1}{\Theta_1}
\le4d_L+4d_L^2,
\]
\[
0<
\frac{A_{\Lambda_L}-A}{A}
\le
\frac{2\,20^{-(L^2-1)}}{1-20^{-3L^2}}
(1+d_L)(1+2d_1).
\tag{12}
\]

Exact rational evaluation for L=3 proves

\[
\boxed{
0<\frac{A_{\mathbb Z\times3\mathbb Z\times3\mathbb Z}(r)-A(r)}
{A(r)}
<\frac9{10^{11}}
\quad\text{for every }r\ge1.}
\tag{13}
\]

The complete-theta relative error is separately less than 8/10^12. The distinction matters because subtracting the constant term amplifies relative error. These are sufficient analytical bounds, not measured optimal errors.

For this L=3 lattice the first shell counts at squared norms 1,4,9,10 are 2,2,6,8. The first additional transverse modes occur at norm 3. Making L large suppresses them throughout r>=1, while the small-r behavior remains three-dimensional at every fixed finite L.

The approximation applies to A itself on the physical half-line r=e^(2u)>=1. It does not preserve the exact modular reflection law, and no derivative, heat-transform or relative first-jet error is claimed here. Applying the source differential operator requires its own error bound. Near a physical zero, a small relative source-profile error does not supply a relative error for H.

## Scope of the collision controls and the remaining geometric question

No collision criterion is established by these constructions. The [control register](../../../../result-summaries/12_collision_controls_and_screening.md) gives the relevant premise distinctions:

| Family | What the present construction does and does not distinguish |
| --- | --- |
| Weighted-square and finite-tail controls | Fourier heat evolution and transverse projection work with changed initial coefficients too. These controls fail the full canonical unit-coefficient source and reflection, so the canonical fundamental heat kernel is additional source data, not yet a collision estimate |
| Reflected smooth and positive-primitive controls | They share evenness and the elementary radial Kelvin representation but lack the unchanged square arithmetic |
| Gaussian-polynomial control of Note01 | It retains the generic forced boundary realization and its cancellation; it is not generated by the canonical lattice source in (9) |
| Euler-factor threshold controls | Their source and conductor differ; canonical lattice reconstruction cannot be silently assigned to them |

These are analytic premise screens. Existing event certificates are not rerun, and finite local controls are not promoted to global thresholds.

The proposed distinction is now concrete. Direct exact equality with the full Gaussian trace is excluded in the stated lattice classes. Exact recovery through a genuine geometric marginal is available, and an unprojected full-rank approximation is available on r>=1. A further attempt can specify a different natural observation, lattice-derived kernel or coupling, but must explain what surviving higher-dimensional information constrains the physical transform. The present marginal and approximation establish no such sign.

## References and internal checks

The multidimensional theta definition was checked at [DLMF 21.2.1](https://dlmf.nist.gov/21.2.E1), with Omega=i r^2 B^T B. [DLMF 21.5.4](https://dlmf.nist.gov/21.5.E4) supplies the general modular framework; the rank asymptotic used here is proved directly by the Gaussian Riemann sum, without importing an unchecked phase convention. These are selected-passage checks, not a chapter audit. No new third-party PDF was needed.

The [exact record](../numerics/06_RANK_THREE_LATTICE_CHECKS_20261027.json) verifies cubic shell coefficients, the finite transverse zero-mode selector, the stretched-lattice shell coefficients, the rational exponential bound, and the two distinct relative-error allowances. It does not certify the infinite analytical arguments by enumeration. All checking is same-assistant and no specialist review is claimed.

This return adds a source-realization feasibility result under RTC-03. It does not upgrade RTC-04, RTC-05, RTC-06, or RTC-07, and is not a manuscript milestone or investigation closeout.
