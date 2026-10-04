# Centered dual energy with an independently positive reference

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited parent configuration; exact serving variant
and configured reasoning effort are not exposed here and are not inferred.
Same-model analytic audit, not independent specialist refereeing. The root
derivation and separate agent checks are internal research. No global bound
or arithmetic positivity certificate is claimed. This note continues the
[complement and parity analysis](02_complement_obstruction_and_parity_20261003.md).

The replacement target is a centered residual energy X(r) in a reference
metric whose gap is known to be at least one. A polynomial bound gives
an independently positive main with a polynomial adverse allowance,
without assuming a nonnegative arithmetic complement. An even more
explicit sufficient target is the squared norm of the complete projected
prime response. Both polynomial targets are equivalent to RH; the
equivalence is a scope check, not a proof of their required bounds.

**Continuation:** [Complete response and signed pairs](04_complete_response_and_signed_pairs_20261003.md)
now proves a causal local-energy reduction, polynomial diagonal cost,
prime-only reduction, and exact complete top-boundary Gram. Its full
pole-inclusive linear formula supplies the unprojected RH converse
left unasserted in Section 8 below. The signed off-diagonal upper
bound and the global dual-energy estimate remain open.

## 1. A reference positive before the arithmetic estimate

Use gamma(t)=Re psi(1/4+it/2)-log pi. The already established integral
identity is

    gamma(t)-gamma(0)
      =2 integral_0^infinity e^(-u/2)(1-cos(tu))/(1-e^(-2u))du >=0.

Thus gamma has its minimum at zero. Set c=1-gamma(0)>0. The global
archimedean form A_infinity=Gamma+cI has multiplier gamma(t)+c>=1.
On a fixed support interval I, restrict this form to the closed prepared
three-moment source Hilbert space H(I). Its closed form realization A is
selfadjoint and satisfies A>=I. It is a known positive reference and uses
no positivity of the arithmetic difference Q.

The minimum can also be read directly from the
[digamma series](https://dlmf.nist.gov/5.7.E6): subtract its value at
1/4 and take real parts. Every resulting term is
(t/2)^2/[(n+1/4)((n+1/4)^2+(t/2)^2)] and is nonnegative. The exact
constant is c=1+EulerGamma+pi/2+3 log 2+log pi.

Let W_L be the complete bounded prime-shift operator compressed to that
prepared source space. Then

    Q=Gamma-W_L=A-V_L,   V_L=W_L+cI.

V_L is bounded selfadjoint at every fixed window, so D(Q)=D(A). The
support-adapted active prime powers, not only prime bases, must all be
included. This is the complete arithmetic Q, not a fixed incomplete Euler
product. A itself does not depend on the finite-place inverse metric.

## 2. Relative operator and the exact dual energy

Define the bounded selfadjoint operator

    T=I-A^(-1/2)V_L A^(-1/2).

For F in the logarithmic form domain put v=A^(1/2)F. Then

    Q[F]=<v,Tv>.

If F belongs to D(Q)=D(A), let f=QF and define

    X[F]=||Tv||^2=||A^(-1/2)f||^2=<f,A^(-1)f>.

The equality follows from A^(-1/2)AF=A^(1/2)F. For a general form-domain
source the first definition still makes sense, but the expression QF must
then be interpreted in the form dual rather than automatically in L2.

The actual translated polynomial source belongs to D(A): its Fourier
decay is order six, hence integral log(2+|t|)^2 |Fhat(t)|^2 dt is finite.
The global archimedean operator applied to its zero extension is L2;
restriction and prepared-moment projection represent the compressed form.
The bounded arithmetic perturbation preserves the operator domain.

Unconditionally the arithmetic vector f is the prepared-source projection
of the complete expression on I:

    gamma(D)F
      -sum_(log n<L) Lambda(n)/sqrt(n)
                         [F(x+log n)+F(x-log n)].

All functions F in that expression are zero-extended. The source projection
and support restriction are part of the operator and cannot be omitted.

## 3. Exact positive-square split and the coefficient correction

For any epsilon>0 define

    P_epsilon[F]=||(T+epsilon I)v||^2/(4epsilon) >=0,
    E_epsilon[F]=||(T-epsilon I)v||^2/(4epsilon) >=0.

Then exactly

    Q[F]=P_epsilon[F]-E_epsilon[F].

Writing a=A[F] and q_F=Q[F], the adverse term is the equality

    E_epsilon = X/(4epsilon)+epsilon a/4-q_F/2.

When X>0 the optimal parameter is epsilon=sqrt(X/a), not sqrt(X)/a.
It gives

    inf_(epsilon>0) E_epsilon = (sqrt(Xa)-q_F)/2.

If X=0, then q_F=0 and the infimum zero is approached as epsilon tends
to zero. Cauchy--Schwarz gives |q_F|<=sqrt(Xa), so in all cases

    inf E_epsilon <=sqrt(Xa),   Q[F]>=-sqrt(Xa).

If only a certified upper x>=X is available, choosing epsilon=sqrt(x/a)
when x>0 still gives E_epsilon<=sqrt(xa). This does not assume the sign
of Q: the same Cauchy inequality controls its negative contribution.
The positive-square construction is generic for a bounded selfadjoint T;
its useful new content would be a bound on the particular X[F_r].

The main is a closed positive form on V: its defining source operator is
(T+epsilon I)A^(1/2)=(1+epsilon)A^(1/2)-A^(-1/2)V_L, a bounded
perturbation of a nonzero multiple of the closed operator A^(1/2).
This construction does not require the loss to be finite rank. It is a
source form rather than a positive ambient-operator split, so the previous
ambient exponential-loss obstruction does not automatically apply.

## 4. Uniform reference energy of the moving source

For r>ell the normalized source F_r=(g+tau_r g)/sqrt2 has norm one and
multiplier |Fhat_r|^2=a_g(1+cos(rt)). Therefore

    1<=A[F_r]<=2A[g]=2(q+c),

since gamma+c is positive and q=Q[g]=Gamma[g] when ell<log 2. The
established separated-source identity also gives the sharper expression

    A[F_r]=q+c+epsilon_g(r),   |epsilon_g(r)|<=b(r).

Thus no moving-window inverse or uniform arithmetic-complement positivity
is needed to bound the reference energy a(r).

## 5. The polynomial target is equivalent to RH, without a hidden tail sign

If X(r)<=C(1+r)^m for all sufficiently large real r, then

    Q[F_r]>=-sqrt(2(q+c)C)(1+r)^(m/2).

Together with Q[F_r]=q-M_g(r)+epsilon_g(r), this gives an eventual upper
subexponential envelope for M_g. The established one-sided theorem implies
RH. The same implication follows from a subexponential pointwise bound on
X, or from weighted integrability integral exp(-epsilon r)X(r)dr<infinity
for every epsilon>0, by Cauchy--Schwarz for the square root.

Conversely assume RH solely for this converse. With distinct critical zeros
and multiplicities m_rho, put

    S_g=sum_rho m_rho |ghat(gamma_rho)| <infinity.

The sixth-power decay and the standard zero count make this sum absolutely
convergent. The decay is established in the
[probe zero-tail note](../GLOBAL_GROWTH_ZERO_TAIL_20261003.md).
The classical count N(T)=O(T log T), including multiplicities, is
supported by [Hasanalizade, Shen and Wong](https://arxiv.org/abs/2107.06506).
Only that order of growth is used here. The polarized complete explicit
formula gives

    u_F(x)=sum_rho m_rho Fhat(gamma_rho) exp(i gamma_rho x),
    QF=P_(H(I))(u_F restricted to I).

There is no extra factor two: the sum already includes both positive and
negative ordinates with multiplicities. For F_r,
|Fhat_r(gamma)|<=sqrt2 |ghat(gamma)|, so the sum converges uniformly and
|u_(F_r)(x)|<=sqrt2 S_g for every x and r. Source projection is an L2
contraction. Hence, with L=|I|=r+ell,

    ||QF_r||_2^2<=2 S_g^2 L,
    X(r)<=||QF_r||_2^2<=2 S_g^2(r+ell).

To justify the operator identity, first polarize against compact smooth
prepared sources, then use their L2 density and the bounded uniform zero
sum. Moment-preserving mollification of the existing polynomial g gives
the same identity by absolute convergence; the finite-regularity operator
domain established above removes any ambiguity in QF_r.

Thus a polynomial X bound is neither stronger than RH nor already proved:
RH implies even a linear bound, and any polynomial bound would imply RH.
The reference A is independently positive throughout this implication.
No full-tail positivity of the unknown arithmetic I-H is hidden among the
hypotheses.

## 6. Source inverse versus the global Fourier inverse

The compressed source A^(-1) is not simply multiplication by
1/(gamma+c). However restriction of the variational dual problem gives
a useful rigorous upper bound. For u in H(I), extended by zero,

    <u,A^(-1)u>
      =sup_(F in V(I)) [2 Re<u,F>-A[F]]
      <=sup_(F in global form domain) [2 Re<u,F>-A_infinity[F]]
      =integral_R |uhat(t)|^2/(gamma(t)+c) dt/(2pi)
      <=||u||_2^2.

The first inequality retains the difference between source and global
inverses. It can sharpen residual bounds without requiring a compressed
inverse computation or a small scalar gap.

The variational equality can be checked directly by completing the square:

    2 Re<u,F>-A[F]
      =||A^(-1/2)u||^2-||A^(1/2)F-A^(-1/2)u||^2.

The supremum is attained at F=A^(-1)u in the source domain. Enlarging the
admissible domain to the global form domain gives the Fourier-inverse upper
bound; it does not identify the two inverse operators.

## 7. Full residual upper certificate

Let f=QF be the actual source vector and choose y in D(A) within the same
prepared source space. Put R=f-Ay. Then exactly

    X = 2 Re<f,y>-<y,Ay>+<R,A^(-1)R>.

Since A>=I, a valid upper certificate is

    X <= 2 Re<f,y>-A[y]+||R||_2^2.

The global inverse multiplier bound from Section 6 can replace ||R||^2 by
integral |Rhat|^2/(gamma+c) when that integral is fully enclosed. The
unconditional lower bound 2 Re<f,y>-A[y]<=X alone is not an upper
certificate; the full residual term is essential.

The residual must include source complements, the support restriction,
all three moment projections, every active prime-power shift, and numerical
evaluation errors. A small Galerkin residual on selected coordinates is
insufficient. If y lies only in the form domain, R need not be an L2 vector;
the simple ||R||^2 bound then requires additional regularity or an explicit
form-dual certificate.

## 8. A purely arithmetic projected-response target

There is a stronger directly sufficient response norm that does not require
even the known reference inverse to be computed. Let

    w_r(x)=sum_(log n<L) Lambda(n)/sqrt(n)
                      [F_r(x+log n)+F_r(x-log n)],   x in I,
    W_H F_r=P_(H(I)) w_r,
    R_ar(r)=||W_H F_r||_2^2.

The signs and weights are exactly those in Q=Gamma-W. In the convention
U_aF(x)=F(x-a), the two shifts are U_(-log n) and U_(log n). If W_L already
denotes the prepared-source compressed operator, W_H=W_L and an additional
prepared projection is redundant. Every active prime power is retained.

The prepared projection is explicit: subtract the components in
span{1,e^(x/2),e^(-x/2)} using their 3x3 Gram matrix, or the established
orthonormal moment basis. It is an L2 contraction and contains no unknown
Sonin inverse metric. The definition includes restriction to I before that
projection.

Define the unconditional finite archimedean constant

    C_Gamma=sqrt2 ||gamma(D)g||_(L2(R)).

Its finiteness follows from sixth-power Fourier decay and logarithmic
gamma growth. The multiplier inequality |Fhat_r|<=sqrt2 |ghat| gives
||gamma(D)F_r||<=C_Gamma. Restriction and source projection only decrease
this norm. The exact compressed operator relation therefore gives

    ||QF_r|| <= C_Gamma+sqrt(R_ar(r)),
    sqrt(R_ar(r)) <= ||QF_r||+C_Gamma,
    X(r) <= (C_Gamma+sqrt(R_ar(r)))^2.

A polynomial bound on R_ar gives a polynomial bound on ||QF_r|| and hence
|Q[F_r]|, since ||F_r||=1. The special-probe criterion then implies RH.
Conversely, under the RH assumption used in Section 5,

    R_ar(r) <= (sqrt2 S_g sqrt(r+ell)+C_Gamma)^2 = O(r).

Consequently the existence of a polynomial projected-response bound is
also equivalent to RH, and RH implies a linear one. The same pointwise
subexponential or all-positive-weight integrability variants are sufficient.

This formulation exposes a finite arithmetic source vector and three
explicit moment subtractions. It does not prove cancellation in that
vector. An equivalence or linear bound for the unprojected norm ||w_r|| is
not asserted: the prepared-source operator identity alone does not control
components in the removed moment directions. A full pole-inclusive formula
would be needed to justify such an additional claim.

## 9. Scope

This is a valid replacement target avoiding the prescribed-local-head tail
obstruction. Its reference inverse has a known gap one. It remains a
reformulation of the central signed arithmetic problem: absolute prime-shift
estimates can still be exponentially large, and the current work does not
prove a polynomial, subexponential, or weighted-integral bound on X(r).
No positive zero-sampling argument is used until RH is explicitly assumed
for the converse in Section 5.

## 10. An explicit odd prime response for calculation

For a centered interval I=(-L/2,L/2), L=r+ell, write
F_r(x)=[g(x+r/2)+g(x-r/2)]/sqrt(2). It is odd. The complete shift
response is odd as well. Since ell=1/2<log 2, the two outward-shifted
packets are entirely outside I. Hence on I the response simplifies to

\[
w_r(x)=\sum_{\log n<L}\frac{\Lambda(n)}{\sqrt{2n}}
\left[g(x+r/2-\log n)+g(x-r/2+\log n)\right].
\tag{1}
\]

All active prime powers are included. The prepared-source moment
projection on odd functions removes only s(x)=sinh(x/2); the constant
and cosh moment directions are even. Therefore

\[
\boxed{R_{\rm ar}(r)=\int_I|w_r(x)|^2dx
-\frac{\left|\int_I\sinh(x/2)w_r(x)dx\right|^2}
       {\sinh(L/2)-L/2}.}
\tag{2}
\]

The denominator is the exact squared L2 norm of s on I and is positive.
Equation (2) gives a finite arithmetic target containing its full signed
cross terms and the exact removed moment component. It contains no Sonin
metric inverse. Subtracting the moment term may improve an estimate, but
no general size or cancellation bound for it is asserted.

The stable interior probe formula for numerical evaluation is

\[
g_0(x)=-64x(1-16x^2)^5(2689-215072x^2+256x^4),
\quad |x|<1/4,
\]

with its known exact rational squared norm. For each fixed rational r,
the finitely many shifted profiles are polynomial on the intervals cut
by their support endpoints. The squared response has degree at most 30
on each such interval. A 16-point Gauss rule would integrate that polynomial
exactly in ideal real arithmetic; logarithmic breakpoints, coefficients,
and computer arithmetic still require outward errors for a certificate.
The sinh-weighted moment integral is not polynomial and needs its own
enclosure. A floating calculation must not be described as an exact norm.

The [small response pilot](../../numerics/selective_loss_dual_response_20261003/README.md)
evaluates this target at five bounded separations. It is a diagnostic of
the proposed quantity and keeps the full moment projection. It does not
evaluate X or a Sonin Schur response and does not establish a global
growth law. Its interpretation and limitations are recorded there.

## 11. Complete continuum centering has fixed endpoint cost

Use the full logarithmic window 0<=u<=L. Replacing the prime-power
measure by its smooth density gives the reference response

\[
w_{0,r}(x)=\frac1{\sqrt2}\int_0^L e^{u/2}
 [g(x+r/2-u)+g(x-r/2+u)]\,du.
\tag{3}
\]

For x in I every contributing u is within [0,L], so the upper limit
can equivalently be infinity. Put y=x+r/2 and z=x-r/2. The first
integral is e^(y/2) int_(-infinity)^y e^(-v/2)g(v)dv, and the second
is e^(-z/2) int_z^infinity e^(v/2)g(v)dv. The prepared exponential
moments make them vanish outside their fixed endpoint caps.

With nu=||g0||^2 and the compact polynomial h, integration by parts
gives the exact cap profiles

\[
v(y)=\frac{-h''(y)-h'(y)/2}{\sqrt\nu},\qquad
q_0(z)=\frac{h''(z)-h'(z)/2}{\sqrt\nu},
\]
\[
w_{0,r}(x)=\frac{v(x+r/2)+q_0(x-r/2)}{\sqrt2}.
\tag{4}
\]

All profiles are zero-extended. Their supports have disjoint interiors
for r>ell, q0(z)=-v(-z), and int h''h'=0. Consequently

\[
\boxed{\|w_{0,r}\|_2^2=
\frac{\|h''\|_2^2+\|h'\|_2^2/4}{\nu}
=\frac{917180}{580421327}\approx0.00158019693.}
\tag{5}
\]

This bound is unconditional and independent of r. The exact rational
constant is reproduced in the numerical package. The large smooth-density
contribution cancels before a norm is taken; its residual consists of two
fixed cap profiles rather than an exponential volume term.

Define the complete weighted discrepancy measure and response by

\[
d\mu(u)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
                 \delta_{\log n}(du)-e^{u/2}du,
\]
\[
e_r(x)=w_r(x)-w_{0,r}(x)
=\frac1{\sqrt2}\int_0^L
 [g(x+r/2-u)+g(x-r/2+u)]\,d\mu(u).
\tag{6}
\]

The moment projection is retained. Therefore

\[
\sqrt{R_{\rm ar}(r)}\le
\sqrt{917180/580421327}+\|P_{\mathcal H}e_r\|_2,
\]
\[
\sqrt{X(r)}\le C_\Gamma+
\sqrt{917180/580421327}+\|P_{\mathcal H}e_r\|_2.
\tag{7}
\]

A polynomial bound on the last squared norm suffices. Conversely its
polynomial growth follows under RH from Section 8 and the bounded cap
term, so this discrepancy formulation has the same precise RH strength.
No such global bound is obtained here.

## 12. A sharp cutoff creates an exponential continuum edge

The complete window in (3) is essential. If the logarithmic prime-density
integral is stopped at u=r instead of r+ell, its omitted density response is

\[
t_r(x)=\frac1{\sqrt2}\int_r^{r+\ell}e^{u/2}
 [g(x+r/2-u)+g(x-r/2+u)]du
\]
\[
=\frac{e^{r/2}}{\sqrt2}
 [q_0(x+r/2)+v(x-r/2)].
\tag{8}
\]

Thus its squared norm is exactly e^r times the constant in (5).
Even the three-moment projection does not remove that exponential edge.
Let H_h(1/2)=int h(x)e^(x/2)dx and
lambda0=H_h(1/2)/(2 sqrt(2nu)). The actual scaled edge has sinh moment
lambda0 exp(r/4). Hence

\[
\boxed{\|P_{\mathcal H}t_r\|_2^2
=e^r\frac{917180}{580421327}
-\frac{\lambda_0^2e^{r/2}}
       {\sinh((r+\ell)/2)-(r+\ell)/2}
=e^r\frac{917180}{580421327}-O(1).}
\tag{9}
\]

This is an exact continuum calculation, not a claim about the size of
the actual prime discrepancy. It shows why separating the partial-density
edge and then bounding it absolutely is unsuitable: cancellation with
the rest of the complete response must occur before taking norms.
It agrees with the earlier
[weighted cutoff obstruction](../GLOBAL_GROWTH_WEIGHTED_ENERGY_CUTOFF_20261003.md)
in this concrete source-response metric.

## 13. A rigorous bound in terms of the weighted Chebyshev error

There is a simple unconditional comparison to a classical error norm.
Put psi(x)=sum_(n<=x) Lambda(n) and

\[
\widetilde E(u)=e^{-u/2}(\psi(e^u)-e^u),\qquad
J_\psi(L)=\int_0^L|\widetilde E(u)|^2du
=\int_1^{e^L}\frac{|\psi(x)-x|^2}{x^2}dx.
\tag{10}
\]

Stieltjes integration by parts in (6) has zero upper boundary because
the shifted probe vanishes at the contributing support endpoints.
At u=0, psi(1)-1=-1 gives the lower boundary F_r. With y=x+r/2,
z=x-r/2 it yields

\[
e_r(x)=F_r(x)+\frac1{\sqrt2}\int_0^L\widetilde E(u)
\big[g'(y-u)+g(y-u)/2-g'(z+u)+g(z+u)/2\big]du.
\tag{11}
\]

The two kernel L1 norms agree by reflection. Young's convolution
inequality and source restriction give

\[
\|P_{\mathcal H}e_r\|_2\le\|e_r\|_2
\le1+\sqrt2\|g'+g/2\|_1\sqrt{J_\psi(L)}
\le1+\sqrt{D_gJ_\psi(L)},
\tag{12}
\]

where Dg=||g'||^2+1/4. The last step uses the support length ell=1/2
and int g'g=0. Its exact rational value is recorded with the fixed-probe
constants. Thus a polynomial bound on Jpsi in L would suffice for the
desired polynomial loss without a Sonin inverse or arithmetic-tail sign.

This is a sufficient comparison, not an estimate proving polynomial
Jpsi. It takes an absolute error norm and can lose useful signed smoothing.
The existing unconditional prime-number-theorem envelopes still give an
exponential response rate through this bound; they do not close the gap.
A sharper proof should retain the kernels and complete-window cancellation
in (6) or (11) rather than discarding them prematurely.

## 14. Next proof obligation

The immediate target is a signed estimate for (2), or a sharper direct
estimate for X using the full positive-A residual certificate. Either
should retain the actual arithmetic response and the prepared moment
projection before taking norms. A separated prime-amplitude bound gives
an exponential envelope and is insufficient.

Proving R_ar(r)<=C(1+r)^m for every sufficiently large real r would finish
the program via the existing one-sided theorem. A smaller bound on X can
also suffice even when the response norm estimate is pessimistic. The
current derivation provides neither global estimate. It removes the
unjustified endpoint-complement sign and the small unknown Sonin gap from
this particular certification task.

See the [continuation review](../../reviews/SELECTIVE_LOSS_COMPLEMENT_AND_DUAL_REVIEW_20261003.md)
and [program overview](overview.md) for the current work sequence.
