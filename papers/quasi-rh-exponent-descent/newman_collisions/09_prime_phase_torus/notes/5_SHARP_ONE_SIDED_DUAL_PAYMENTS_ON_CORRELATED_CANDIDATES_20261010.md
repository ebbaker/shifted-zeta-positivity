# Sharp one-sided dual payments on correlated candidates

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6.1-sol (Codex); configured reasoning effort: ultra, verified
from the parent chat's recorded configuration. Derivations, exact replays,
and agent cross-readings are internal checks, not independent mathematical
validation.

This continues [Note 4](4_PRESCRIBED_HEAT_WEIGHT_COVARIANCE_AND_SIGNED_HIERARCHY_20261010.md)
and uses [Heat Note 18](../../notes/18_CORRELATED_HOLOMORPHIC_PAYMENTS_AND_CANDIDATE_COVERAGE_20261010.md)'s
correlated lower-jet body. The new result solves the exact one-sided
candidate-null payment for every quadratic dual. Its two-dimensional
minimization reduces to two cubic critical-root problems and one interior
stationary point, including singular cases. Complete moment intervals
require only eight common corners. This improves the paid certificate
generally; its prescribed four-channel signed upper bound remains open.

## 1. Physical candidate coordinates and the one-sided payment

Retain the complete natural cutoff at an actual center in
`kappa in [1,3/2]`, `0<t<=1/20`, with `L=kappa/t`,
`x=4 pi exp(L)`. Freeze time, integer cutoff, and centering
`mu=Omega/c` for all raw spatial jets. Define the prescribed moments

\[
 M_j=\sum_{n\le N}w_ne^{i\phi_n}(\log n-\mu)^j=X_j+iY_j,
\quad e=(X_0,Z_1)^T,\quad Z_1=Y_1+(d/c)X_1,
\]
\[
 u=(X_2,Y_3,X_4)^T,\qquad A=-d\mu.
\tag{1}
\]

The physical first jet is exactly `F_N'/2=A X_0-c Z_1`, with
amplitude drift present. If `eta>0` is the full holomorphic approximation
bound, a genuine collision necessarily satisfies

\[
 (2X_0/\eta)^2+2|A X_0-cZ_1|/(L\eta)\le1.
\tag{2}
\]

Thus put

\[
 z=(s,v)^T\in\mathcal C:=\{s^2+|v|\le1\},\quad e=Dz,
 \qquad D=\begin{pmatrix}\eta/2&0\\A\eta/(2c)&-L\eta/(2c)\end{pmatrix}.
\tag{3}
\]

Here `s=F_N/eta`, `v=F_N'/(L eta)`, and `D` is invertible.
The body is sharp for locally bounded holomorphic error first jets by
Heat Note 18; actual prescribed arithmetic states form a smaller class.

Keep Note 3's dual with the same parameters in its estimate and payment:

\[
 \mathcal K=2Y_3^2+3X_2X_4-\Gamma X_2^2,\quad
 \Gamma=\gamma/c^2,\quad \mathcal K_{\Lambda,B}=\mathcal K+q(e,u),
\]
\[
 q(e,u)=e^T\Lambda e+2e^TBu.
\tag{4}
\]

If the actual complete pair estimate gives `K_dual<=U`, the discarded
term needs an upper bound for `-q`, rather than for its absolute value.
Define the sharp one-sided payment

\[
 \boxed{\Pi^-_{\Lambda,B}(u)
   =\max_{z\in\mathcal C}[-q(Dz,u)]
   =-\min_{z\in\mathcal C}q(Dz,u).}
\tag{5}
\]

It is nonnegative because zero is feasible. The sufficient criterion is

\[
 \boxed{U_{\Lambda,B}+\Pi^-_{\Lambda,B}(u)
                   +\widehat\Delta/(4c^6)<0.}
\tag{6}
\]

Retain the exact normalizer `gamma=18 partial_x^2 log A_t+9/x^2`,
the full physical Bell residuals `E_2,E_3,E_4`, spatial errors
`j! L^j eta`, and the measured quadratic payment `widehat Delta`
of Note 2. [Heat Note 19](../../notes/19_HIGHER_SCHUR_PAYMENTS_AND_MULTI_CUTOFF_SIGNED_CONTINUATION_20261010.md)
can additionally replace independent holomorphic higher-error-jet
payments by their Schur body. The Bell residuals are separate physical
jet errors; they cannot be placed in that holomorphic body without a
new disk bound.

The old absolute rectangle payment always dominates (5): the body (2)
is inside that rectangle and `-q<=|q|`. The improvement removes both
the sign loss and the square enlargement. If `Lambda` is positive
semidefinite and `B=0`, **the payment is exactly zero**, whereas an
absolute payment generally was positive. The positive null term already
makes the dual an upper bound for `K`.

For measured complete moment intervals `u_j in [u_j^-,u_j^+]`,
the exact independent-body payment is

\[
 \boxed{\Pi^-(\mathcal U)
     =\max_{u\in\operatorname{corners}(\mathcal U)}
                              \Pi^-_{\Lambda,B}(u).}
\tag{7}
\]

There are at most eight corners. For fixed `e`, the objective is linear
in `u`, so its maximum is attained at a common corner. Interchanging
the two maxima proves (7). Different corners for different summands
would enlarge the payment. Sharpness is on the specified product class
`D C x U`; actual correlations between `e` and `u` may improve it.

## 2. Exact finite minimization theorem

Set

\[
 H=D^T\Lambda D=\begin{pmatrix}h&k\\k&r\end{pmatrix},
 \quad g=D^TBu=(l,m)^T,
 \quad q(s,v)=h s^2+2ksv+r v^2+2ls+2mv.
\tag{8}
\]

**Theorem.** The minimum of this quadratic on `C` is the minimum
of the following finite set of objective values:

1. the endpoint values `q(-1,0),q(1,0)`;
2. each boundary polynomial's values at every real derivative root in
   `(-1,1)`;
3. the value at the nonsingular stationary point below, if feasible.

For `tau=+1,-1`, the boundary and derivative are

\[
\begin{split}
 P_\tau(s)&=q(s,\tau(1-s^2))\\
 &=r s^4-2\tau k s^3+(h-2r-2\tau m)s^2
                    +(2\tau k+2l)s+r+2\tau m,\\
 P_\tau'(s)&=4r s^3-6\tau k s^2
            +2(h-2r-2\tau m)s+2\tau k+2l.
\end{split}
\tag{9}
\]

An identically zero derivative gives a constant edge, already covered
by endpoints. Count repeated roots once. For `delta=hr-k^2 !=0`,

\[
 s_*=(km-rl)/\delta,\quad v_*=(kl-hm)/\delta,
 \quad q(s_*,v_*)=(-r l^2+2klm-hm^2)/\delta.
\tag{10}
\]

Include it if `s_*^2+|v_*|<=1`. No definiteness assumption is needed.
Adding the feasible value `q(0,0)=0` is harmless and guarantees that
the recorded payment is nonnegative.

A continuous quadratic has a minimum on the compact body. Boundary
minima follow (9), including endpoints. An interior minimum satisfies
`Hz+g=0`; an invertible `H` gives (10). If `H` is singular and
a stationary point exists, choose a nonzero vector `n` in its
nullspace. The objective is constant along `z_*+a n`, because
`Hz_*+g=0` and `Hn=0`. That line reaches the boundary of the
bounded convex body with the same value. Thus singular stationary
ridges require no additional interior candidate. The identically zero
objective is also covered by endpoints. This proves every degeneracy.

For rational coefficients, square-free polynomial division followed by
exact sign-variation isolation encloses the cubic roots. Rational interval
Horner evaluation gives outward objective intervals. Their minimum gives
an outward payment interval whose upper endpoint is safe in (6). The
theorem itself is exact for arbitrary real parameters; no floating root
or uncertified numerical sign is part of the rational certificate.

For actual irrational input data, first outwardly enclose the five
coefficients `(h,k,r,l,m)` in rational intervals. The exact payment over
that coefficient box is the maximum of the same finite payment problem
at its at most **32 corners**: for fixed `(s,v)`, the objective is affine
in the five coefficients. This gives a fully rational outward application
without trying to enclose parameter-dependent cubic roots directly.
It is sharp on the coefficient box; dependencies lost in forming that
box may allow further improvement.

## 3. Closed-form gains and optimization geometry

If `q=-a s^2-b v^2` with `a,b>=0`, then

\[
 \Pi^-=\max(a,b),
\tag{11}
\]

where the absolute square pays `a+b`. Indeed `v^2<=(1-s^2)^2`;
the objective `a y+b(1-y)^2` in `y=s^2` is convex on `[0,1]`,
so its maximum occurs at an endpoint.

For a cross term alone,

\[
 \boxed{q=2\beta sv\quad\Longrightarrow\quad
                      \Pi^-=4|\beta|/(3\sqrt3).}
\tag{12}
\]

Maximize `|s|(1-s^2)` at `|s|=1/sqrt3` and select the adverse
sign of `v`. Compared with the normalized square payment `2|beta|`,
the factor is `2/(3sqrt3)`, about `0.3849`.

When `Lambda=0`, Heat Note 18's support formula gives

\[
 \Pi^-=h_{\mathcal C}(2l,2m)=
 \begin{cases}
 2|m|+l^2/(2|m|),&m\ne0,\ |l|\le2|m|,\\
 2|l|,&|l|\ge2|m|\text{ or }m=0.
 \end{cases}
\tag{13}
\]

For general duals, (5) is convex in `Lambda,B`, positively homogeneous
for nonnegative scalars, and subadditive: it is a maximum of linear
functions of those parameters. The properties hold with the moment box
as well. An attaining pair `(e_*,u_*)` gives the supporting subgradient

\[
 (\delta\Lambda,\delta B)\ \longmapsto
       -e_*^T\delta\Lambda e_*-2e_*^T\delta B u_*.
\tag{14}
\]

Consequently a pair-bound mechanism with affine or convex dual dependence
can use this exact payment for optimization. Active boundary/interior
witnesses certify the payment. No convexity of the still unknown
arithmetic upper bound is assumed.

For the actual candidate point and the same `u`, an exact protection
against a free dual sign is

\[
 \mathcal K_{\Lambda,B}(e,u)+\Pi^-_{\Lambda,B}(u)
                                           \ge\mathcal K(e,u).
\tag{15}
\]

A dual choice can reduce a bounding method's conservative payment or
improve its signed cancellation; it cannot change the actual threshold
value. At `e=0`, the original indefinite `Q` and its two positive
directions survive as in Note 3. Prescribed coefficients still have to
enter the signed upper bound more strongly than arbitrary moment vectors.

Uniformly bounded dual parameters retain the previous vanishing rate:
`|u|=O(exp(a/t))`, `||D||=O(L eta)`, and

\[
 \Pi^-=O\big(L e^{-\kappa^2/(8t)}+L^2e^{-2\mathfrak b/t}\big),
 \quad\mathfrak b=\kappa(\kappa+4)/16.
\tag{16}
\]

Thus the new payment improves constants and sign structure without
changing that exponential scale. Note 4's Gaussian covariance still
needs its signed estimate: the actual mean candidate body does not
condition each auxiliary tilted state or the shifted moment hierarchy.

## 4. Four channels and verification scope

Keep exactly `mathbb Q=[[Lambda,B],[B^T,Q]]`, with the physical
`epsilon=d/c` and `Gamma=gamma/c^2`. For
`r(rho)=(1,epsilon rho,rho^2,0,rho^4)` and
`s(rho)=(0,rho,0,rho^3,0)`, put
`R=r_n^T mathbb Q r_m`, `S=s_n^T mathbb Q s_m`,
`C_nm=r_n^T mathbb Q s_m`. The kernels remain

\[
 D_c=(R+S)/2,\quad D_s=(C_{mn}-C_{nm})/2,
 \quad P_c=(R-S)/2,\quad P_s=(C_{nm}+C_{mn})/2.
\tag{17}
\]

They multiply `cos(T log(n/m))`, `sin(T log(n/m))`,
`cos(2theta_t+T log(nm))`, `sin(2theta_t+T log(nm))`, respectively.
The prescribed heat pair weight, common height/carrier, ratio/product
regrouping, diagonals, product squares and complete mixed block/core
terms remain unchanged. The new payment removes no pair channel and
introduces no independent prime phase.

The [checker](../numerics/check_curved_one_sided_dual_payment.py) passes
**10,081 exact assertions**. Known sharp classes include irrational
cross-term extrema, singular stationary ridges, constant edges and interior
minima. Square-free cubic isolation and rational interval evaluation
give the retained controls payment widths below `1e-17`. Twelve
drift-containing controls verify both physical transformed candidate
coordinates; their certified upper payment ratios compared with the old
absolute rectangle range from below `0.345` to below `0.989`. These are
formal payment controls, not numerical signs at prescribed candidates.
Eight common moment corners, 32 common coefficient corners, and the
complete four-channel identity are checked independently with rational
one-frequency phase controls.

The [small record](../numerics/curved_one_sided_dual_payment_record_20261010.json)
binds the final source and exact payment enclosures. The
[internal review](../reviews/5_CURVED_ONE_SIDED_DUAL_PAYMENT_INTERNAL_REVIEW_20261010.md)
records the sharpness class and replay scope. The remaining sector-wide
task is a prescribed-coefficient signed bound for the same complete four
pair channels beating (6), or Note 4's signed hierarchy criterion with
this reduced payment. No such bound is established. Uniform collision
exclusion, higher multiplicity, the small-time endpoint, RH and global
Newman conclusions remain open. Earlier sources and the manuscript are
preserved; files follow [LARGE_FILES.md](../../../../../LARGE_FILES.md).
