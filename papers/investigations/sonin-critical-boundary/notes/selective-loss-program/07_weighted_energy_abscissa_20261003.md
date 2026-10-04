# Weighted energy, the convergence abscissa, and a Hardy-space obligation

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Same-model analytic research, not independent specialist refereeing.
No global quadratic estimate or proof of RH is claimed.

The exact normalized source and complete arithmetic response are fixed in
[04_complete_response_and_signed_pairs_20261003.md](04_complete_response_and_signed_pairs_20261003.md).
The finite continuum certificate is recorded separately in
[05_quadratic_target_and_finite_sign_20261003.md](05_quadratic_target_and_finite_sign_20261003.md).
This note addresses the remaining infinite-window obligation.

## 1. Physical weighted formulations of the quadratic target

Write a=1/4 and retain the same real prepared source g. Set

    p(y)=sum_(n>=2) Lambda(n)/sqrt(n) g(y-log n),
    J(Y)=int_0^Y p(y)^2dy,
    N(r)=J(r+a)-(p*p)(r).

The response p vanishes below b=log(2)-a>a. For epsilon>0 define the
possibly infinite physical energies

    J_epsilon=int_0^infinity e^(-2epsilon y)p(y)^2dy,
    I_epsilon=int_0^infinity e^(-2epsilon r)N(r)dr.

For J=D+Theta, the unconditional diagonal asymptotic D(Y)~Y^2/2 and
D>=0 give

    Theta_+(Y)=O((1+Y)^2)  <=>  J(Y)=O((1+Y)^2).       (1)

Monotone integration by parts gives

    J_epsilon=2epsilon int_0^infinity
                            e^(-2epsilon Y)J(Y)dY,   (2)

with equality also when both sides are infinite. Thus

    J(Y)=O((1+Y)^2)  <=>  J_epsilon=O(epsilon^(-2))
                            as epsilon decreases to zero.             (3)

The reverse implication follows from J(Y)<=e^2 J_(1/Y) for large Y.
This uses cumulative energy, not a pointwise bound on p.

Since |(p*p)(r)|<=J(r), the full-window energy satisfies

    [(e^(2epsilon a)-1)/(2epsilon)]J_epsilon
                                                <=I_epsilon.          (4)

This inequality is valid for extended nonnegative integrals. If I_epsilon
is finite, (4) first proves J_epsilon finite. Once J_epsilon is finite,
absolute integrability of the convolution gives the exact identity

    I_epsilon=e^(2epsilon a)J_epsilon/(2epsilon)
                                                -P(2epsilon)^2,       (5)
    P(s)=int_0^infinity p(y)e^(-sy)dy.

For this actual arithmetic response, (3) is also equivalent to

    I_epsilon=O(epsilon^(-3)) as epsilon decreases to zero.             (6)

Forward, discard the nonnegative square in (5). In reverse, establish
physical finiteness using (4), then identify its true Laplace transform
with the arithmetic expression on Re s>epsilon. Near real s=0 this
expression is O(s), because zeta(1/2)!=0 and G(s)=O(s). Therefore
P(2epsilon)=O(epsilon), and (5) gives

    J_epsilon=2epsilon e^(-2epsilon a)
                                  [I_epsilon+O(epsilon^2)].            (7)

Substituting a meromorphic scalar value in (5) before proving physical
convergence would be invalid. The order of these steps matters.

## 2. The unconditional endpoint epsilon=1/2

Let E(t)=psi(t)-t. For y>a the prepared continuum main vanishes, and
Stieltjes integration by parts yields

    p(y)=int_(e^(y-a))^(e^(y+a)) E(t)t^(-3/2)
                         [g'(y-log t)+g(y-log t)/2]dt.                 (8)

The classical effective PNT estimate
|E(t)|<=C t exp[-c sqrt(log t)] implies, for large y,

    |p(y)|<=C_g exp[y/2-c_g sqrt(y)]

with c_g>0. On every initial compact interval p is a finite sum of
continuous translated profiles, so its local squared norm is finite.
Consequently

    J_(1/2)<infinity,
    J_epsilon<infinity for all epsilon>=1/2.          (9)

This known prime-number estimate permits weighted Plancherel at the
endpoint after physical convergence has been established. It does not
approach the small-epsilon rate in (3).

## 3. Exact dependence of the energy abscissa on zero locations

Let

    alpha_*=sup_(nontrivial rho) (Re rho-1/2),
                           0<=alpha_*<=1/2.

For the fixed probe, the source transform is

    G(s)=s(1/4-s^2)H_h(s)/sqrt(nu).

Its only zero in Re s>0 is the pole-preparation zero s=1/2. Indeed the
normalized transform of h=(1-16x^2)^8 is a modified Bessel function of
order 17/2 whose nonzero zeros are purely imaginary. The exact source
note supplies this noncancellation fact.

The pole-inclusive smoothed linear formula, valid for y>a, is

    p(y)=-sum_rho m_rho G(rho-1/2)e^((rho-1/2)y)
         -sum_(k>=1) G(-2k-1/2)e^(-(2k+1/2)y).      (10)

The nontrivial coefficients are absolutely summable: G has sixth-power
decay uniformly across the critical strip and N(T)=O(T log T).
The trivial-zero sum is uniformly bounded for y>=a+eta for each fixed
eta>0, in particular for y>=1. For example the L1 majorant is

    sqrt(1/2) exp[-(5/2)(y-a)]/[1-exp(-2(y-a))].      (11)

This particular majorant is not finite at y=a; it must not be used to
claim uniform control there. The initial compact interval is handled
locally from the original finite arithmetic response. These facts give

    p(y)=O_g(e^(alpha_* y)),
    J_epsilon<infinity for epsilon>alpha_*.          (12)

Conversely, physical finiteness of J_epsilon makes P analytic in
Re s>epsilon by Cauchy--Schwarz. On its initial convergence half-plane,

    P(s)=-G(s) zeta'(1/2+s)/zeta(1/2+s),            (13)

and uniqueness continues this identity wherever the true transform is
analytic. A zero with Re rho-1/2>epsilon leaves the nonzero residue
-m_rho G(rho-1/2), contradicting analyticity. For epsilon>0, a zero on
the boundary Re rho-1/2=epsilon is also excluded: physical finiteness
would imply, for delta>0,

    |P(epsilon+delta+i Im rho)|
                       <=sqrt(J_epsilon)/sqrt(2delta),                (14)

whereas the uncanceled simple pole grows as a nonzero constant/delta.

Therefore the convergence abscissa among positive exponential weights is

    inf{epsilon>0 : J_epsilon<infinity}=alpha_*.     (15)

An attained offcritical supremum forces divergence at epsilon=alpha_*.
When the supremum is not attained, (15) alone does not decide endpoint
convergence. In particular (9) is consistent with alpha_*=1/2 because
no nontrivial zero lies on Re rho=1. The endpoints in (12), (14), and
(15) must be distinguished.

A new convergence bound at even one fixed epsilon<1/2 proves a fixed
zero-free right half-plane. Finiteness for every epsilon>0 forces RH.
Under RH the absolutely summable nontrivial series in (10) is bounded,
so J(Y)=O(1+Y); hence RH also gives the quadratic targets (1)--(6).

## 4. The analytic certificate required for a Hardy approach

A legitimate equivalent analytic formulation of the small-weight target
is to prove, for every sufficiently small epsilon>0, that the same
Euler-product continuation P is analytic throughout Re s>epsilon and

    sup_(sigma>epsilon) (1/(2pi)) int_R |P(sigma+it)|^2dt
                                           <=C epsilon^(-2),          (16)

with a single constant C. The half-plane Laplace/Hardy theorem and
uniqueness from the initial arithmetic convergence half-plane then
identify its L2 causal inverse with e^(-epsilon y)p(y). Thus (16) gives
the physical bound (3). Conversely physical finiteness gives the exact
identity

    sup_(sigma>epsilon) (1/(2pi)) int_R |P(sigma+it)|^2dt
                                                   =J_epsilon.        (17)

The analyticity requirement is substantive. The zero G(1/2)=0 cancels
the pole of zeta, but it cancels no offcritical zero pole.

A finite line norm of a meromorphic continuation is insufficient. For
alpha>0 and real gamma, consider

    P0(s)=1/(s-alpha-i gamma),
    p0(y)=e^((alpha+i gamma)y), y>=0.

For epsilon!=alpha its meromorphic line norm is

    (1/(2pi))int_R |P0(epsilon+it)|^2dt
                                         =1/[2|epsilon-alpha|],       (18)

but its physical weighted energy diverges for epsilon<=alpha. The line
norm can stay bounded as epsilon decreases to zero while every
sufficiently small physical energy is infinite.

Moving an inverse Laplace contour across a nontrivial-zero pole introduces
the residue -m_rho G(rho-1/2)e^((rho-1/2)y). It must remain in p before
squaring. Finite-height contour identities also retain horizontal pieces
until their vanishing is proved. Meromorphic continuation, a shifted
line integral, or a finite-window certificate supplies neither the
half-plane analyticity nor the small-weight Hardy bound in (16).

The finite result in the sibling certificate is useful local evidence.
The global quadratic estimate and the equivalent analytic obligation
remain open.
