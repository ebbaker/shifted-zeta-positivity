# Aggregated arithmetic kernel and a shorter signed divisor target

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel analytical work and same-model cross-review are internal checks,
not independent specialist refereeing. Based on repository commit
`62ac139771ae317f6e4b624765783c6856739d8f`. No new global prime-variance
exponent or mathematical priority is claimed.

## 1 Outcome

This continues the [one-sided arithmetic attempt](ONE_SIDED_ARITHMETIC_ATTEMPT_20261004.md)
at its proposed next calculation: aggregate the arithmetic kernel before
estimating its correlation with prime-counting error. Three deductions
sharpen that calculation.

1. The aggregated kernel has uniformly bounded weighted absolute integral.
   The earlier factor of log squared in the prime-error envelope is unnecessary.
2. A small-divisor portion of the complete signed correlation can be removed
   at a proved power cost. For the illustrative saving kappa=0.01, the
   remaining complementary divisors lie between X^(1397/2800) and
   X^(1399/2800).
3. The apparent product of two arithmetic errors does not supply a
   contraction. An exact mixed-discrepancy formula and its Mellin moments
   preserve a hypothetical forbidden zero's coefficient. The cutoff
   multiplier also takes value exactly one at each such zero.

The shortened correlation still requires a one-sided power estimate.
Neither that estimate nor a new zero-free strip is proved. The useful
advance is a more localized target and an exact explanation of why
factorization alone does not improve its exponent.

## 2 Exact aggregation including the singleton correction

Use the inherited fixed probe, with A=exp(-1/4), C=2exp(1/4), q=7/3,

\[
\ell(v)=\int_1^2 y w(v/y)\,dy,\qquad
A_U(m)=\sum_{d\mid m,\ d>U}\mu(d),\qquad
E(t)=\theta(t)-t.
\]

The [centering note](PRIME_DISCREPANCY_CENTERING_20261004.md) proves
that ell is C^5, supported on [A,C], with D^7 ell a finite signed measure
and integral ell=0. Throughout the estimates below assume

\[
U>C/A,\qquad U^2\le AX,\qquad T_* = CX/U.
\tag{1}
\]

All cutoffs are real. The arithmetic sums use their displayed strict
or weak inequalities; E(U) is right-continuous. Define

\[
P_U(t)=\sum_{m>U}A_U(m)\ell(mt/X),\qquad
\mathcal K(t)=P_U'(t)/X,
\]
\[
\mathcal I(X;U)=\int_U^{T_*}E(t)\mathcal K(t)\,dt.
\tag{2}
\]

For every positive integer m, including m<=U,

\[
A_U(m)=\mathbf1_{m=1}-\sum_{d\le U,\ d\mid m}\mu(d).
\tag{3}
\]

Thus, for all t>0, the locally finite identities are

\[
P_U(t)=\ell(t/X)-\sum_{d\le U}\mu(d)L(X/(dt)),
\quad L(y)=\sum_{k\ge1}\ell(k/y),
\tag{4}
\]
\[
\mathcal K(t)=\frac{\ell'(t/X)}{X^2}
-\frac1{Xt}\sum_{d\le U}\mu(d)S(X/(dt)),
\quad S(y)=\sum_{k\ge1}g(k/y),\quad g(v)=v\ell'(v).
\tag{5}
\]

The singleton terms in (4)-(5) vanish on the entire retained interval
[U,T_*], since t/X<=C/U<A. This is why no missing lower-m correction
occurs when complementing the divisor sum. Outside that interval one
must keep the singleton unless its support is separately excluded.

## 3 A uniform kernel bound with no logarithmic divisor loss

Integration by parts gives integral g=0. Its sixth distributional
derivative is

\[
D^6g=vD^7\ell+6D^6\ell,
\]

a finite signed measure. Poisson summation, with Fourier convention
hat g(xi)=integral g(v) exp(-2 pi i xi v) dv, yields

\[
S(y)=y\sum_{h\ne0}\widehat g(hy),\qquad
|S(y)|\le c_g y^{-5},\quad
c_g=\frac{2\zeta(6)}{(2\pi)^6}\|D^6g\|_{\rm TV}.
\tag{6}
\]

The series converges absolutely. There is no zero Fourier mode. From
(5), sum_(d<=U) d^5<=U^6, and (1),

\[
|\mathcal K(t)|\le c_g\frac{U^6t^4}{X^6},\qquad
\int_U^{T_*}t|\mathcal K(t)|\,dt\le c_g C^6/6.
\tag{7}
\]

Consequently

\[
|\mathcal I(X;U)|\le (c_g C^6/6)
\sup_{U\le t\le T_*}|E(t)/t|.
\tag{8}
\]

This removes the earlier log-squared loss without estimating any Mertens
sum. It does not turn a subpower prime-error envelope into a fixed power.
For example the classical PNT from
[Tao's Notes 2, Corollary 39](https://terrytao.wordpress.com/2014/12/09/254a-notes-2-complex-analytic-multiplicative-number-theory/)
transfers directly through (8); passing from psi to theta only subtracts
higher prime powers. At U=X^a with fixed a>0 this remains a subpower
bound. A better unconditional exponent is not inferred.

More locally, for U<=T<=T_*, (7) gives

\[
\left|\int_U^T E(t)\mathcal K(t)dt\right|
\le \frac{c_g}{6}(UT/X)^6
\sup_{U\le t\le T}|E(t)/t|.
\tag{9}
\]

## 4 A seventh-order deletion using the primitive

The primitive gains one further power without differentiating E.
Seventh-order Poisson summation applied to ell gives

\[
|L(y)|\le c_\ell y^{-6},\qquad
c_\ell=\frac{2\zeta(7)}{(2\pi)^7}\|D^7\ell\|_{\rm TV}.
\tag{10}
\]

For 1<=D<=U, retain the signs and define on [U,T_*]

\[
P_{\le D}(t)=-\sum_{d\le D}\mu(d)L(X/(dt)),
\qquad \mathcal K_{\le D}=P_{\le D}'/X.
\]

Then

\[
|P_{\le D}(t)|\le c_\ell D^7t^6/X^6.
\tag{11}
\]

Stieltjes integration by parts is exact for any U<=T<=T_*:

\[
\int_U^T E(t)\mathcal K_{\le D}(t)dt
=\frac{E(T)P_{\le D}(T)-E(U)P_{\le D}(U)}X
-\frac1X\int_{(U,T]}P_{\le D}(t)\,dE(t).
\tag{12}
\]

Both endpoint terms are essential; an atom at T is included, one at U
is excluded. Since |E(t)|<=c t and
|dE|<=dtheta+dt, Chebyshev's bound gives total variation O(T) on
(U,T]. Applying (11) to every term of (12) proves

\[
\left|\int_U^T E(t)\mathcal K_{\le D}(t)dt\right|
\ll_w(DT/X)^7.
\tag{13}
\]

For D=U and UT/X<=1 this improves the power in (9) when only a bounded
prime-error envelope is used. More usefully, at T=T_* it gives

\[
\boxed{\quad
\mathcal I(X;U)=\mathcal I_{(D,U]}(X;U)+O_w((D/U)^7),\quad}
\tag{14}
\]
\[
\mathcal I_{(D,U]}=
-\frac1X\int_U^{T_*}\frac{E(t)}t
\sum_{D<d\le U}\mu(d)S(X/(dt))\,dt.
\tag{15}
\]

Equivalently (15) is the integral of E(t) times K(t)-K_(<=D)(t).
The interval [U,T_*] must be retained. A truncated complementary-divisor kernel need not vanish
outside the original product range.

For 0<kappa<14/29 set

\[
U=X^{1/2-\kappa/28},\qquad
D=U X^{-\kappa/14}=X^{1/2-3\kappa/28}.
\tag{16}
\]

The deleted portion in (14) is O(X^(-kappa/2)). Combining it with the
previous scalar and inner-prime-power comparisons gives

\[
\mathcal I_{(D,U]}(X;U)+q\lambda_V(X)
=O_{w,\kappa}(X^{-\kappa/2}).
\tag{17}
\]

Thus either eventual one-sided bound

\[
\mathcal I_{(D,U]}\ge-KX^{-\kappa/2}
\quad\hbox{or}\quad
\mathcal I_{(D,U]}\le KX^{-\kappa/2}
\tag{18}
\]

is separately equivalent to the original first-saving target, using the
inherited scalar detector. For kappa=1/100 the new divisor band is
X^(1397/2800)<d<=X^(1399/2800), and
U<=t<=C X^(1401/2800). The target remains X^(-1/200), including an
allowed constant-sized multiple of that scale in all comparison errors.

There is no additional useful removal of the initial t interval from
(13) at this maximally balanced cutoff: requiring (UT/X)^7<=X^(-kappa/2)
forces T<=U. A fixed-ratio split is possible but has no power gain by
itself. This saturation is part of the budget, not a proved obstruction
to every other localization method.

## 5 What survives in the terminal interval

On CX/(2U)<=t<=CX/U, every active outer factor satisfies U<m<=2U.
Its only divisor exceeding U is m itself, so A_U(m)=mu(m), with
m=2U correctly included if integral. Therefore the terminal correlation
is exactly

\[
\int_{C/2}^C\varepsilon((X/U)s)\,s
\left[\frac1U\sum_{U<m\le2U}\mu(m)\frac mU
\ell'(s m/U)\right]ds,
\qquad \varepsilon(t)=E(t)/t.
\tag{19}
\]

Here t=(X/U)s; assumption (1) ensures this terminal interval lies above
U. There is no prefactor that is a positive power of U^2/X. Equation
(19) exposes an actual Möbius-shell/prime-error correlation at
complementary scales. It supplies neither its sign nor a lower bound on
its size, and it cannot replace the entire correlation outside this
terminal interval.

A second exact form uses increments of both M(t)=sum_(n<=t) mu(n)
and E(t). The [mixed discrepancy companion](MIXED_DISCREPANCY_FEEDBACK_20261004.md)
derives this form, sums its cofactor kernel before bounding, and tests
its Mellin moments. Two separate arithmetic errors in that formula are
not independent random quantities. Their product does not justify a
squared decay rate.

## 6 The cutoff does not attenuate a forbidden Mellin pole

This calculation holds with U fixed, without (1). Use the equivalent
definition integral_(U,infinity) E(t) K(t) dt for every X>0. Put

\[
\mathscr M_U(z)=\sum_{d\le U}\mu(d)d^{-z},\qquad
F_U(z)=1-\zeta(z)\mathscr M_U(z),\qquad
D_\ell(z)=\frac1q\int\ell(v)v^{z-1}dv,
\]
\[
B_U(z)=\sum_{p>U}(\log p)p^{-z}
-\frac{U^{1-z}}{z-1}+E(U)U^{-z}.
\]

Initially on Re z>1, absolute convergence and (2) give

\[
\int_0^\infty \mathcal I(X;U)X^{-z}\,dX
=-qD_\ell(z)F_U(z)B_U(z).
\tag{20}
\]

For clarity, (20) is the Mellin transform of X I, not of I under the
measure X^(-z-1)dX. Indeed
sum_(m>U) A_U(m)m^(-z)=F_U(z),
integral ell'(v)v^z dv=-zqD_ell(z), and
z integral_U^infinity E(t)t^(-z-1)dt=B_U(z).
The right-continuous term E(U)U^(-z) is required.

The prime-power correction
sum_p sum_(j>=2) (log p)p^(-jz) is holomorphic on Re z>1/2, while
the full prime-power series is -zeta'/zeta. Hence at any zeta zero
rho with Re rho>1/2 and multiplicity r,

\[
F_U(\rho)=1,\qquad
\operatorname{Res}_{z=\rho}B_U(z)=-r,
\]
\[
\operatorname{Res}_{z=\rho}\mathcal M[X\mathcal I](z)
=qrD_\ell(\rho)\ne0.
\tag{21}
\]

Nonvanishing is the inherited fixed-probe theorem. No rightmost zero
or simple-zero hypothesis is used. Finite normalized averages over fixed
cutoffs retain the same residue; weights with total zero cancel the
residue and this detector together.

Equation (21) is meromorphic continuation, not evaluation of a convergent
Dirichlet series at rho. Substituting a moving U(X) into (20) would be
invalid. For the actual moving cutoff, (17) instead shows that the
Mellin transform of X I_(D,U] differs from
qD_ell(z) zeta'(z)/zeta(z) by a holomorphic function on
Re z>1-kappa/2, together with entire initial-cap terms. It therefore
retains every forbidden pole in that open half-plane. This explains why
summation and factorization alone provide no contraction.

## 7 Verification and the next calculation

The accompanying [exact checker](../../../numerics/01_signed_arithmetic_covariance/check_aggregated_kernel.py)
checks the aggregate/divisor identities, signed split, truncated
Stieltjes formula, centered error, and terminal Möbius shell using exact
fractions. Its compact polynomial kernel and prime atoms weighted by p
are synthetic algebra tests. Deliberately omitting endpoint terms,
using the terminal identity globally, or deleting the singleton outside
its valid support is detected. The retained
[record](../../../numerics/01_signed_arithmetic_covariance/aggregated_kernel_record_20261004.json)
and [internal review](../../../reviews/01_signed_arithmetic_covariance/AGGREGATED_KERNEL_REVIEW_20261004.md)
state the verification scope. These checks do not certify the fixed-probe
variation constants or an asymptotic estimate.

The next admissible analytic target is (18), preserving the whole
remaining divisor interval, the t interval, and their signed interaction.
The mixed-discrepancy representation gives another exact way to study
that interaction. Any proposed dispersion estimate should be tested
against its explicit Mellin moment identity before a numerical sweep:
the diagonal hypothetical zero mode is transmitted with the original
coefficient, so an assumed saving from independence would be circular.
No manuscript, outward certificate, compilation record, commit, or draft
snapshot is changed by this continuation.
