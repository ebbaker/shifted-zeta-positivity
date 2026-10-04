# Mixed Mertens and prime discrepancy feedback

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant
and configured reasoning effort are not exposed. Internal same-model
analysis and cross-review, not independent specialist refereeing. No new
global variance exponent, zero-free strip, or mathematical priority is
claimed.

This is a companion to the
[aggregated-kernel continuation](AGGREGATED_KERNEL_CONTINUATION_20261004.md)
and continues the exact correlation in the
[one-sided attempt](ONE_SIDED_ARITHMETIC_ATTEMPT_20261004.md).

## 1. Outcome and scope

The prime-discrepancy target admits an exact double integral involving
increments of both the Mertens function and the prime-counting error.
After summing the cofactor variable, its fixed kernel has third-order
decay at the origin. This preserves the signed joint cancellation and
gives a useful object for a future dispersion estimate.

It does not by itself create a contraction. Separate logarithmic
envelopes give logarithmic bounds. Even hypothetical equal power
envelopes for the two inputs reproduce the same global power, up to a
logarithm. More sharply, a deterministic power-mode calculation at a
simple zeta zero reproduces exactly the original scalar residue. This
last statement is a test of explicit input functions, not an expansion
of the actual arithmetic errors into zeros, and it assumes no actual
zero is simple.

## 2. Exact double-increment identity

Use the notation and fixed probe from the
[centering derivation](PRIME_DISCREPANCY_CENTERING_20261004.md):

\[
A=e^{-1/4},\quad C=2e^{1/4},\quad q=7/3,\quad
\ell(v)=\int_1^2 y w(v/y)\,dy,
\]
\[
A_U(m)=\sum_{d\mid m,\ d>U}\mu(d),\quad
M_1(U)=\sum_{d\le U}\frac{\mu(d)}d,
\]
\[
J_0(X;U)=c_wM_1(U)+\frac1{qX}
\sum_{m>U}\sum_{p>U}A_U(m)(\log p)\ell(mp/X).
\]

Assume real \(U\ge1\), \(U^2\le AX\). Write

\[
M(s)=\sum_{d\le s}\mu(d),\quad E(t)=\theta(t)-t,
\quad M_U(s)=M(s)-M(U),\quad E_U(t)=E(t)-E(U).
\]

The right-continuous values at \(U\) exclude its atom if \(U\) is an
integer or prime. The density calculation already proves exactly

\[
J_0=Q+R,\qquad
Q=\frac1{qX}\sum_{m>U}A_U(m)
\int_{(U,\infty)}\ell(mt/X)\,dE(t),
\tag{1}
\]

with \(R=O_w((U^2/X)^8)\). We retain that exact remainder; no new
estimate of it is needed here.

Since \(A_U=\mu_{>U}*1\), integration by parts first in the prime
variable gives

\[
Q=-\frac1{qX^2}\sum_{k\ge1}k
\int_U^\infty E_U(t)
\int_{(U,\infty)}s\ell'(kst/X)\,dM(s)\,dt.
\tag{2}
\]

Set

\[
G(v)=(v\ell'(v))'=\ell'(v)+v\ell''(v).
\tag{3}
\]

A second integration by parts gives

\[
\int_{(U,\infty)}s\ell'(kst/X)\,dM(s)
=-\int_U^\infty M_U(s)G(kst/X)\,ds.
\]

All endpoint terms vanish because increments vanish at their lower
endpoints and the test functions vanish at their upper support
endpoints. Thus

\[
\boxed{\quad
J_0(X;U)-R=
\frac1{qX^2}\sum_{k\ge1}k
\int_U^\infty\int_U^\infty
M_U(s)E_U(t)G(kst/X)\,ds\,dt.
\quad}
\tag{4}
\]

The cofactor sum is finite: only \(k<CX/U^2\) can contribute.
For every retained \(k\), the exact terminal domain is
\(s,t>U\), \(kst<CX\), together with the support of \(G\).
Neither the terminal intervals nor either increment may be discarded.

For comparison with the previous uncentered correlation, let

\[
\mathcal K(t)=\frac1{X^2}\sum_{m>U}mA_U(m)\ell'(mt/X),\qquad
\mathcal I_c=\int_U^\infty E_U(t)\mathcal K(t)\,dt.
\]

Then \(J_0=-\mathcal I_c/q+R\) exactly. If
\(\mathcal I=\int_U^\infty E(t)\mathcal K(t)dt\), then

\[
\mathcal I_c=\mathcal I+
\frac{E(U)}X\sum_{m>U}A_U(m)\ell(mU/X).
\tag{5}
\]

This explicitly recovers the previously retained lower-cutoff boundary.

## 3. The aggregated kernel and its origin decay

Define the fixed kernel, independent of \(X,U\), by

\[
\mathscr F(v)=\sum_{k\ge1}kG(kv),\qquad v>0.
\tag{6}
\]

For each positive \(v\) the sum is finite; it vanishes for \(v\ge C\).
Equation (4) becomes

\[
\boxed{\quad
J_0(X;U)-R=
\frac1{qX^2}\int_U^\infty\int_U^\infty
M_U(s)E_U(t)\mathscr F(st/X)\,ds\,dt.
\quad}
\tag{7}
\]

The finite smoothness already proved for the probe is enough to control
the origin. Put \(h(v)=vG(v)=v\ell'(v)+v^2\ell''(v)\), extended by zero.
Since \(D^7\ell\) is a finite signed measure, so is \(D^5h\).
Integration by parts twice gives

\[
\int h(v)\,dv
=\int v\ell'(v)\,dv+\int v^2\ell''(v)\,dv
=\int\ell(v)\,dv=0.
\]

The fifth-order Poisson estimate therefore gives

\[
\sum_{k\ge1}h(kv)=O_w(v^4),\qquad
\boxed{\mathscr F(v)=O_w(v^3)\quad(v\downarrow0).}
\tag{8}
\]

For example the first bound follows with constant
\(2\zeta(5)(2\pi)^{-5}\|D^5h\|_{\rm TV}\). No infinite
smoothness or unproved decay of a differentiated lattice remainder is
being assumed.

## 4. What absolute envelopes actually yield

Write \(H=X/U^2\). For any nonnegative measurable \(f\), changing
variables \(v=st/X\) gives

\[
\int_U^\infty\int_U^\infty
(st)^\beta f(st/X)\,ds\,dt
=X^{\beta+1}\int_{1/H}^C
v^\beta f(v)\log(Hv)\,dv
\tag{9}
\]

when \(f\) is supported below \(C\).

Suppose only that
\(|M_U(s)|\le a(s)s\), \(|E_U(t)|\le b(t)t\), and let
\(a_*,b_*\) bound these envelopes on the actual factor range
\([U,CX/U]\). Then

\[
|J_0-R|\le\frac{a_*b_*}{q}
\int_{1/H}^C v|\mathscr F(v)|\log(Hv)\,dv
\ll_w a_*b_*\log(CH).
\tag{10}
\]

The integral is finite by (8). For \(U=X^a\), with fixed
\(0<a<1/2\), the available logarithmic prime-error envelope and even
the trivial bound for \(M_U\) yield every fixed logarithmic saving,
after increasing the input logarithmic order. If logarithmic bounds
for both inputs are used, their orders add, with one logarithmic order
lost to the factor \(\log(CH)\) in (10). This still gives no fixed power.

For a conditional power-envelope diagnostic, assume

\[
|M_U(s)|\le C_M s^\beta,\qquad
|E_U(t)|\le C_E t^\beta\quad(s,t\ge U),\qquad 0<\beta<1.
\]

Then (8)–(9) give

\[
|J_0-R|\ll_{w,\beta} C_MC_E X^{\beta-1}\log(CH).
\tag{11}
\]

Both inputs are sampled near the square-root scale; multiplying their
normalized power errors reproduces the original full-scale power.
Equation (11) is not an available unconditional input and supplies no
bootstrap to a better \(\beta\). The two arithmetic functions are
deterministic and coupled by convolution identities. Nothing here
permits an independence assumption or deletion of their mixed terms.

## 5. Exact Mellin moments of the aggregate

Let

\[
L(z)=\int_A^C\ell(v)v^{z-1}\,dv,\qquad
\mathscr A(z)=\int_0^C v^z\mathscr F(v)\,dv.
\tag{12}
\]

The second integral is holomorphic on \(\Re z>-4\), by (8).
For \(\Re z>1\), absolute summation and integration by parts give

\[
\mathscr A(z)=\sum_{k\ge1}k^{-z}
\int_A^C u^zG(u)\,du
=z^2\zeta(z)L(z).
\]

Since \(L(1)=\int\ell=0\), the pole of \(\zeta\) at one is
removable in this product. Analytic continuation proves

\[
\boxed{\mathscr A(z)=z^2\zeta(z)L(z),\qquad \Re z>-4.}
\tag{13}
\]

In particular,

\[
\mathscr A(0)=\mathscr A'(0)=0,\qquad
\mathscr A(1)=L'(1)=q c_w\ne0.
\tag{14}
\]

Thus the aggregate does not have a vanishing first weighted moment.
One cannot calculate that moment by integrating each cofactor term and
then summing zero: the corresponding absolute series is harmonic and
does not converge. Formula (13) retains that endpoint effect exactly.

Moreover, \(\mathscr F\) is real, continuous, integrable, and has zero
ordinary integral but a nonzero first weighted moment. It therefore
assumes both positive and negative values. Cofactor aggregation has not
turned (7) into a positive-kernel comparison. This rejects that direct
shortcut, not every method involving positivity.

## 6. Deterministic power increments, including the boundary remainder

Fix complex \(z\) with \(\beta=\Re z>0\), and take positive real
arguments for all complex powers. Define the deterministic test

\[
\mathcal B_z(X,U)=\frac1{X^2}
\int_U^\infty\int_U^\infty
(s^z-U^z)(t^z-U^z)\mathscr F(st/X)\,ds\,dt.
\tag{15}
\]

Assume \(H=X/U^2\to\infty\). On setting \(v=st/X\), direct
integration in \(s\) gives the exact formula

\[
\mathcal B_z=X^{z-1}\int_{1/H}^C\mathscr F(v)
\left\{v^z\left(\log(Hv)-\frac2z\right)
+H^{-z}\left(\log(Hv)+\frac2z\right)\right\}\,dv.
\tag{16}
\]

For clarity, the inner integral behind this calculation is

\[
\int_U^{Xv/U}(s^z-U^z)((Xv/s)^z-U^z)\frac{ds}s
=((Xv)^z+U^{2z})\log(Hv)
-\frac2z((Xv)^z-U^{2z}).
\]

Extend the integral in (16) down to zero. Its term multiplied by
\(H^{-z}\) vanishes by \(\mathscr A(0)=\mathscr A'(0)=0\).
The other term becomes
\(\mathscr A'(z)+(\log H-2/z)\mathscr A(z)\).
The omitted interval \(0<v<1/H\) is bounded using (8). Set
\(u=Hv\); its absolute value, including the exterior factor, is at
most a fixed multiple of

\[
X^{\beta-1}H^{-\beta-4}
\int_0^1u^3
\left\{u^\beta\left(|\log u|+\frac2{|z|}\right)
+|\log u|+\frac2{|z|}\right\}\,du.
\]

This integral is finite. Consequently

\[
\boxed{\quad
\mathcal B_z(X,U)=X^{z-1}
\left\{\mathscr A'(z)+
\left(\log H-\frac2z\right)\mathscr A(z)\right\}
+O_{z,w}(X^{\beta-1}H^{-\beta-4}).
\quad}
\tag{17}
\]

The error includes the full lower product boundary; it is not obtained
by silently extending an arithmetic terminal interval.

There is also a deterministic saturation test requiring no hypothetical
zero. Since \(\mathscr A(1)=q c_w\ne0\), continuity implies
\(\mathscr A(\beta)\ne0\) for all real \(\beta<1\) sufficiently
close to one. Take the explicit input functions \(M(s)=s^\beta\) and
\(E(t)=t^\beta\), and \(U=X^a\) with fixed \(0<a<1/2\).
Their cutoff increments obey the separate power envelopes in (11), but
(17) gives

\[
\mathcal B_\beta(X,U)\sim
\mathscr A(\beta)(1-2a)X^{\beta-1}\log X.
\]

Thus even the logarithmic loss in (11) is attained in this broad input
class. A better power cannot follow from the two envelope sizes alone.
These test functions are not the arithmetic Mertens and prime errors;
an argument exploiting additional arithmetic structure is not excluded.

## 7. Simple-zero mode test: exact transmission, no contraction

Suppose, solely for this deterministic diagnostic, that \(\rho\) is a
simple zero of \(\zeta\), with \(\beta=\Re\rho>0\). Formula (13)
gives

\[
\mathscr A(\rho)=0,\qquad
\mathscr A'(\rho)=\rho^2\zeta'(\rho)L(\rho).
\tag{18}
\]

To identify the natural coefficients, use the von Mangoldt version of
(7), obtained by replacing \(\theta\) with \(\psi\) and primes
with \(\Lambda\) throughout. Its density term and derivation are
identical. The simple-pole residues of the Perron transforms
\(1/(z\zeta(z))\) and \(-\zeta'(z)/(z\zeta(z))\) at \(\rho\)
are respectively

\[
a_\rho=\frac1{\rho\zeta'(\rho)},\qquad b_\rho=-\frac1\rho.
\]

The prime-only version has the same pole coefficient when
\(\Re\rho>1/2\): on that half-plane the higher-prime-power series
\(\sum_p\sum_{j\ge2}(\log p)p^{-jz}\) is holomorphic by absolute
local uniform convergence, and subtracting it from
\(-\zeta'/\zeta\) does not change a zero pole. This is a statement
about local Dirichlet-series continuation, not an asserted asymptotic
expansion of \(\theta(t)-t\).

Insert the explicit test increments
\(a_\rho(s^\rho-U^\rho)\) and
\(b_\rho(t^\rho-U^\rho)\) into the mixed integral. Equations
(17)–(18) give

\[
\boxed{\quad
\frac{a_\rho b_\rho}{q}\mathcal B_\rho(X,U)
=-\frac{L(\rho)}qX^{\rho-1}
+O_{\rho,w}(X^{\beta-1}H^{-\beta-4}).
\quad}
\tag{19}
\]

The leading coefficient is exactly the zero-residue coefficient of the
original smoothed prime response
\((qX)^{-1}\sum_n\Lambda(n)\ell(n/X)\).
The putative logarithmic amplification in (17) cancels because
\(\zeta(\rho)=0\); its remaining coefficient transmits the complete
mode. If \(L(\rho)=0\), both displayed scalar coefficients vanish;
the fixed detector's separate nonvanishing theorem addresses the
relevant forbidden zeros.

This verifies a deterministic response of the kernel. It does not
expand the actual \(M\) or \(\psi-t\), interchange zero sums,
identify a dominant zero, or assert simplicity of any zero. Multiple
zeros would require logarithmic power inputs and are not needed for
this diagnostic. In particular (19) neither proves an obstruction to
every signed inequality nor proves such an inequality; it refutes a
purported automatic power improvement based only on the appearance of
two small errors.

The calculation can also retain the cross terms of a finite real
conjugate pair. For distinct fixed \(z,\xi\), with positive real parts,
define

\[
\mathcal B_{z,\xi}=X^{-2}\iint_{s,t>U}
(s^z-U^z)(t^\xi-U^\xi)\mathscr F(st/X)\,ds\,dt.
\]

The exact inner product integral at \(v=st/X\) is

\[
\begin{aligned}
&\int_U^{Xv/U}(s^z-U^z)((Xv/s)^\xi-U^\xi)\frac{ds}s\\
&=\frac{\xi}{z(z-\xi)}(Xv)^zU^{\xi-z}
-\frac{z}{\xi(z-\xi)}(Xv)^\xi U^{z-\xi}\\
&\qquad+U^{z+\xi}\left(\log(Hv)+\frac1z+\frac1\xi\right).
\end{aligned}
\]

Extending its product integral to zero, using (14), and treating the
omitted interval as in (17), gives

\[
\begin{aligned}
\mathcal B_{z,\xi}
&=\frac{(\xi/z)X^{z-1}U^{\xi-z}\mathscr A(z)
-(z/\xi)X^{\xi-1}U^{z-\xi}\mathscr A(\xi)}{z-\xi}\\
&\quad+O_{z,\xi,\ell}\left(
U^{\Re z+\Re\xi}X^{-1}H^{-4}\right).
\end{aligned}
\tag{20}
\]

For two distinct zeros, both main moments vanish. In particular, take
the two real deterministic input functions

\[
a_\rho(s^\rho-U^\rho)+\overline{a_\rho}(s^{\bar\rho}-U^{\bar\rho}),
\qquad
b_\rho(t^\rho-U^\rho)+\overline{b_\rho}(t^{\bar\rho}-U^{\bar\rho}).
\]

Equations (19)–(20) evaluate their full mixed integral, with its
normalization \(1/(qX^2)\), as

\[
-2\Re\left\{\frac{L(\rho)}qX^{\rho-1}\right\}
+O_{\rho,\ell}(X^{\beta-1}H^{-\beta-4}).
\tag{21}
\]

Thus the finite real test includes both conjugate cross terms. No
bound on an infinite collection of actual arithmetic zero modes, or
on a residual part of an actual explicit formula, follows from it.

## 8. Exact coefficient closure

The same feedback is already visible at the finite coefficient level.
Let

\[
P(n)=\begin{cases}\log n,&n\text{ prime},\\0,&\text{otherwise},\end{cases}
\quad R_{\rm rad}(n)=\log\operatorname{rad}(n)=(1*P)(n),
\]

and let \(\mu_L, P_L\) denote restrictions to \(n\le U\).
Since \(\mu*1=\delta_1\), one has identically

\[
\boxed{\quad
\mu_{>U}*1*P_{>U}
=P-P_L-\mu_L*R_{\rm rad}+\mu_L*1*P_L.
\quad}
\tag{22}
\]

Its left side is exactly the coefficient of the prime-inner term in
\(J_0\); \(A_U(m)=0\) for \(m\le U\) handles that cutoff
automatically. For the von Mangoldt version,

\[
\mu_{>U}*1*\Lambda_{>U}
=\Lambda-\Lambda_L-\mu_L*\log+\mu_L*1*\Lambda_L.
\tag{23}
\]

Equations (22)–(23) retain coefficient one on the original prime
response. The low prime-response term vanishes after applying the
prepared scalar if \(U<AX\), while the other pieces are precisely the
Type I and mixed terms already present in the reduction. Reinserting
these exact identities therefore restores that response; it does not
produce a numerical contraction coefficient.

The useful next target remains a signed estimate for the actual joint
integral (7), or its localized equivalent in the companion note. A
successful argument must supply cancellation beyond these algebraic
identities and the separate classical error envelopes.
