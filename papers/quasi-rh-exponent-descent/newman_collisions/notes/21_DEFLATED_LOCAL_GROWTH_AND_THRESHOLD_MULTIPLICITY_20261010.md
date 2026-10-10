# Deflated local growth, density-strengthened thresholds, and multiplicity

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model family: GPT-6 (Codex); the exact serving variant and configured reasoning
effort are unknown and are not inferred. This is an internal analytical
derivation, not independent mathematical validation. No numerical experiments
or parameter sweeps were used.

This continues the complete-deflation argument of
[Heat Note 12](12_THRESHOLD_COLLISION_JETS_AND_PAID_LAGUERRE_TEST_20261009.md),
the correlated holomorphic payments of
[Heat Note 19](19_HIGHER_SCHUR_PAYMENTS_AND_MULTI_CUTOFF_SIGNED_CONTINUATION_20261010.md),
and the local-to-average question in
[Heat Note 13](13_RECENT_HEAT_RESULTS_AND_PATHS_FORWARD_20261009.md).
Its density-strengthened inequalities supply a stronger target for
[Heat Note 20](20_ANALYTIC_SCHUR_CONES_AND_DENSITY_STRENGTHENED_THRESHOLDS_20261010.md)
and the complete signed criterion in
[project 09 Note 6](../09_prime_phase_torus/notes/6_ANALYTIC_COMMON_FACTOR_SMOOTHING_AND_PRIMITIVE_SIGNED_FRONTIER_20261010.md).

The imported genuine-function inputs are the all-real order-one canonical
product and uniform zero-count theorem already used in the manuscript; their
primary source is [Polymath, Section 3 and Theorem 1.5(iv)](https://arxiv.org/html/1904.12438v2#S1).
The deductions below are proved explicitly. They establish neither the
missing prescribed-coefficient signed inequality nor an RH conclusion.
Polynomial examples identify the scope of general mechanisms and do not
represent the zeta heat function.

## 1. Exact deflated local growth

Fix a time \(T\) when all zeros of \(H_T\) are real, and an exact multiplicity
\(m\ge2\) at \(x_*=a>0\). Evenness permits this choice of sign. On a real
interval around \(a\), write

\[
H_T=A_TQ_T,\qquad b=(\log A_T)',\qquad
q_j=Q_T^{(j)}(a),\qquad c=\frac{q_m}{m!}\ne0.
\]

The normalizer is analytic, nonvanishing, and positive on the real interval.
All derivatives in this section are spatial derivatives at the fixed time
\(T\). Remove all \(m\) copies of the root \(a\), and let
\(\mathcal Z_T^{(a)}\) be the multiset of all remaining roots. Define

\[
d=\inf_{\rho\in\mathcal Z_T^{(a)}}|\rho-a|>0,
\qquad S_0=\sum_{\rho\in\mathcal Z_T^{(a)}}\frac1{(\rho-a)^2},
\qquad \alpha=\frac{q_{m+1}}{(m+1)q_m}.
\tag{1}
\]

The sum converges absolutely by the imported canonical-product theorem.
The mirror root \(-a\) has multiplicity \(m\), so
\(d\le2a\) and \(S_0\ge m/(4a^2)\).

Choose \(0<h<d\), set \(r=h/d\), and put

\[
B=\sup_{0\le y\le h}|b_x(T,a+y)|,
\qquad K_- =\frac{S_0}{1+r}-B,
\qquad K_+=\frac{S_0}{1-r}+B.
\tag{2}
\]

There is a positive real function \(R\) on \([0,h]\) such that

\[
Q_T(a+y)=c y^mR(y),\qquad R(0)=1.
\]

The following bounds retain the full deflated root data:

\[
e^{\alpha y-K_+y^2/2}\le R(y)
\le e^{\alpha y-K_-y^2/2},\qquad 0\le y\le h.
\tag{3}
\]

With

\[
D_\pm(y)=m+\alpha y-K_\pm y^2,
\]

one also has

\[
|Q_T'(a+y)|^2
\le c^2y^{2m-2}e^{2\alpha y-K_-y^2}
\max\{D_+(y)^2,D_-(y)^2\}.
\tag{4}
\]

### Proof

Let \(g(z)=H_T(z)/(z-a)^m\). It has order at most one, is real entire,
and has precisely the remaining real roots. On the root-free interval,
the canonical product gives

\[
(\log|g|)''(a+y)=-S(y),\qquad
S(y)=\sum_{\rho\in\mathcal Z_T^{(a)}}
\frac1{(\rho-a-y)^2}.
\]

Since \(g(a+y)=A_T(a+y)cR(y)\),

\[
(\log R)''(y)=-S(y)-b_x(T,a+y).
\tag{5}
\]

The argument uses the product for the genuine \(H_T\); it does not assume a
global real-root product for \(Q_T\).

Put \(\delta_\rho=\rho-a\). Twice integrating (5), using the value
and slope of \(R\) at zero, gives

\[
\begin{split}
\log R(y)={}&\alpha y+
\sum_{\rho\in\mathcal Z_T^{(a)}}
\left\{\log\left(1-\frac y{\delta_\rho}\right)
+\frac y{\delta_\rho}\right\}\\
&-\int_0^y(y-u)b_x(T,a+u)\,du.
\end{split}
\tag{6}
\]

The series converges absolutely and locally uniformly because each summand
is \(O(y^2/\delta_\rho^2)\). Every logarithm is real because
\(|y/\delta_\rho|<1\). The linear coefficient \(\alpha\) already absorbs
the canonical exponential and the normalizer's first logarithmic derivative.

For \(|v|\le r<1\), the identity

\[
\log(1-v)+v=-v^2\int_0^1\frac{u}{1-uv}\,du
\]

implies

\[
-\frac{v^2}{2(1-r)}\le\log(1-v)+v
\le-\frac{v^2}{2(1+r)}.
\]

The normalizer integral in (6) has absolute value at most \(By^2/2\).
Summing these inequalities proves (3). The denominators \(1\pm r\)
retain more information than applying a constant bound on the second
derivative, which would give squared denominators.

Differentiating (6) gives

\[
(\log R)'(y)=\alpha-y
\sum_{\rho\in\mathcal Z_T^{(a)}}
\frac1{\delta_\rho(\delta_\rho-y)}
-\int_0^y b_x(T,a+u)\,du.
\]

Each summand in the middle sum is positive, and

\[
\frac{S_0}{1+r}\le
\sum_{\rho\in\mathcal Z_T^{(a)}}
\frac1{\delta_\rho(\delta_\rho-y)}
\le\frac{S_0}{1-r}.
\]

Thus \(m+y(\log R)'(y)\) lies between \(D_+(y)\) and \(D_-(y)\).
Using

\[
Q_T'(a+y)=c y^{m-1}R(y)\{m+y(\log R)'(y)\}
\]

and (3) proves (4). The value at \(y=0\) follows by continuity. The same
proof applies on the left after replacing \(y\) by \(-y\), \(\alpha\) by
\(-\alpha\), and \(B\) by the bound on the left interval.

## 2. A conditional analytical local-to-average criterion

Suppose a complete, paid physical derivative average satisfies

\[
\frac1h\int_0^h\left(\frac{2Q_T'(a+y)}L\right)^2dy\ge\frac18
\]

on an interval covered by Section 1. Then a sufficient exclusion condition
for the candidate is

\[
\boxed{
\frac{4c^2}{L^2h}\int_0^h
y^{2m-2}e^{2\alpha y-K_-y^2}
\max\{D_+(y)^2,D_-(y)^2\}\,dy<\frac18.}
\tag{7}
\]

This implication does not freeze the arithmetic phases or require a heat
approximation on a single complex disk of radius \(h\). It does require the
same physical function and interval in both estimates.

An elementary closed-form sufficient replacement is

\[
\boxed{\frac{4c^2E_h}{L^2}\Psi_m(h)<\frac18,}
\tag{8}
\]

where

\[
E_h=\exp\!\left(\max_{0\le y\le h}
\{2\alpha y-K_-y^2\}\right),
\]

\[
\begin{aligned}
\Psi_m(h)={}&\frac{m^2h^{2m-2}}{2m-1}
+\frac{2m|\alpha|h^{2m-1}}{2m}
+\frac{(\alpha^2+2mK_+)h^{2m}}{2m+1}\\
&+\frac{2|\alpha|K_+h^{2m+1}}{2m+2}
+\frac{K_+^2h^{2m+2}}{2m+3}.
\end{aligned}
\tag{9}
\]

Indeed \(K_+\ge|K_-|\): both \(K_+-K_-\ge0\) and
\(K_++K_->0\) follow directly from (2). Therefore each bracket magnitude
in (4) is bounded by \(m+|\alpha|y+K_+y^2\). Expanding its square and
integrating proves (8)–(9). The maximum defining \(E_h\) occurs at an endpoint
or, when \(K_->0\) and \(0<\alpha/K_-<h\), at \(y=\alpha/K_-\).
Thus (8) uses only elementary operations and no numerical optimizer or
quadrature. It is weaker than (7).

The substantive input still needed is control of \(c,\alpha,S_0,d\), and
the normalizer on a paid probe interval. A center mirror inequality alone
does not supply those controls.

## 3. Genuine zero density strengthens the threshold sign

At the center, (5) is exactly

\[
S_0=\alpha^2-
\frac{2q_{m+2}}{(m+1)(m+2)q_m}-b_x(T,a).
\tag{10}
\]

The complete-deflation expression in Heat Note 12 is therefore

\[
\begin{split}
\mathscr D_m={}&
\frac{q_{m+1}^2}{(m+1)^2}
-\frac{2q_mq_{m+2}}{(m+1)(m+2)}
-\left(b_x(T,a)+\frac m{4a^2}\right)q_m^2\\
={}&q_m^2\left(S_0-\frac m{4a^2}\right).
\end{split}
\tag{11}
\]

The mirror alone gives \(\mathscr D_m\ge0\). The genuine zero density
gives a strict additional floor at high height, with a symbolic constant.

### Uniform counting input and explicit symbolic constants

For \(0<T\le1/2\), let \(N_T(R)\) count every zero with
\(0<\operatorname{Re}\rho\le R\), including multiplicity. Take an absolute
constant \(C_{\rm count}\ge0\) large enough that the imported theorem,
with this endpoint convention, reads

\[
|N_T(R)-p_T(R)|\le C_{\rm count}\log(2+R),
\qquad R\ge4\pi,
\tag{12}
\]

where

\[
p_T(R)=\frac R{4\pi}\log\frac R{4\pi}-\frac R{4\pi}
+\frac{11}{8}+\frac T{16}\log\frac R{4\pi}.
\tag{13}
\]

An endpoint convention can be absorbed into the constant using the same
theorem's local count bound, as in the manuscript. No numerical value of
\(C_{\rm count}\) is asserted. Set

\[
D_0=8\pi(4C_{\rm count}+1),\qquad
X_0=\max\{(4\pi)^2,2D_0,3\}.
\tag{14}
\]

For \(a\ge X_0\), the main-term derivative obeys

\[
p_T'(R)=\frac1{4\pi}\log\frac R{4\pi}+\frac T{16R}
\ge\frac{\log a}{8\pi},
\qquad a+D_0\le R\le a+2D_0.
\]

Here \(a\ge(4\pi)^2\) supplies the logarithmic inequality. Since
\(a\ge2D_0,3\),

\[
2+a+2D_0\le2+2a\le a^2,
\]

so each endpoint error in (12) is at most
\(2C_{\rm count}\log a\). Hence

\[
\begin{split}
N_T(a+2D_0)-N_T(a+D_0)
&\ge\left(\frac{D_0}{8\pi}-4C_{\rm count}\right)\log a\\
&=\log a.
\end{split}
\tag{15}
\]

At the all-real time every root counted by (15) is real. It lies strictly
to the right of \(a\), at distance at most \(2D_0\), and is disjoint from
both the deflated cluster at \(a\) and the forced mirror cluster at \(-a\).
Consequently the two contributions add:

\[
d\le2D_0,\qquad
S_0\ge\frac m{4a^2}+\frac{\log a}{4D_0^2}.
\tag{16}
\]

Combining (11) and (16) proves the strengthened genuine threshold condition

\[
\boxed{\mathscr D_m\ge\frac{\log a}{4D_0^2}q_m^2,}
\qquad a\ge X_0.
\tag{17}
\]

This uses the exact leading nonzero derivative \(q_m\). It is nonvacuous
at every exact multiplicity \(m\ge2\).

For an ordinary double root, Heat Note 12's expression

\[
\mathscr L=2q_3^2-3q_2q_4-\gamma(T,a)q_2^2,
\qquad \gamma(T,a)=18b_x(T,a)+9/a^2,
\]

is \(18\mathscr D_2\). Thus

\[
\boxed{\mathscr L\ge\frac{9\log a}{2D_0^2}q_2^2.}
\tag{18}
\]

Subtracting this floor before taking a paid Schur upper bound produces a
stronger exclusion criterion. Heat Note 20 gives its normalized cone
form, including the general-\(m\) version. The counting constant is still
symbolic, and no opposite inequality has been proved for the prescribed
finite arithmetic jets. The density floor is a stronger necessary target,
not an arithmetic exclusion theorem.

## 4. What density says about the probe length and multiplicity hierarchy

The existing complete derivative average uses

\[
H_d=D_{\rm av}T^2e^{2\mathfrak a/T},\qquad
\mathfrak a=\frac{\kappa(4-\kappa)}{16},
\qquad a=4\pi e^{\kappa/T},\quad L=\kappa/T.
\tag{19}
\]

On the shrinking sector \(1\le\kappa\le2\), \(H_d\to\infty\)
uniformly as \(T\downarrow0\). Once \(a\ge X_0\), (16) gives
\(d\le2D_0\). Therefore the hypothesis \(H_d<d\) required to apply
the single root-free chart in Sections 1–2 is impossible for sufficiently
small \(T\). A root-product transfer across this entire probe would need
multiple charts retaining the intervening zeros and derivative information
at their transitions. The counting lower bound on \(S_0\) does not itself
bound the deflated leading coefficient \(c\) or slope \(\alpha\).

The same counting input bounds exact multiplicity pointwise. For \(a>4\pi\),
take the left limit at \(a\) in (12). The continuity of \(p_T\), and the
jump of the cumulative count, give

\[
m=N_T(a)-\lim_{R\uparrow a}N_T(R)
\le2C_{\rm count}\log(2+a).
\tag{20}
\]

Thus in the stated shrinking sector,

\[
m\le2C_{\rm count}
\left(\frac\kappa T+\log(4\pi+2)\right)=O(T^{-1}).
\tag{21}
\]

More generally, (21) is uniform on a bounded positive \(\kappa\)-interval.
It provides a finite derivative hierarchy on each time range
\(T\ge T_{\min}>0\) **within that sector**. It does not give a single
finite hierarchy as \(T\downarrow0\), and the count estimate alone does
not give a globally uniform multiplicity bound at arbitrary heights when
only a lower bound on \(T\) is imposed. Its upper bound grows with height.
Any global conclusion using a separate high-height simplicity or collision
localization theorem must import that additional input explicitly.

## 5. Arbitrary multiplicity at an exact positive polynomial heat threshold

For each integer \(m\ge2\), threshold \(T>0\), root position \(a>0\),
and amplitude \(C_{\rm pol}>0\), define the even polynomial flow

\[
P_\tau(z)=(-1)^m C_{\rm pol}
e^{-(\tau-T)\partial_z^2}(z^2-a^2)^m.
\tag{22}
\]

The exponential is a finite differential sum. This flow has the following
properties:

* \(\partial_\tau P_\tau=-P_\tau''\).
* Its all-real time set is exactly \([T,\infty)\).
* At time \(T\), both \(a\) and \(-a\) have exact multiplicity \(m\), and
  \(P_T(0)\ne0\).
* If \(a^2\ge4m(2m-1)T\), then \(P_\tau(iy)>0\) for every
  \(\tau\ge0\) and every real \(y\).
* At time \(T\), its complete-deflation mirror inequalities are equalities.

These models show that evenness, reality, backward heat, imaginary-axis
positivity, an exact positive all-real threshold, and the mirror signs do
not by themselves bound multiplicity. They do not satisfy the genuine
zero-counting law and therefore do not contradict Sections 3–4.

### Proof of the exact all-real time set

If \(p\) is a real polynomial with all roots real, then \(p+u p'\) has
all roots real for every real \(u\). For simple roots this follows from the
strictly decreasing logarithmic derivative on every interval between roots
and the appropriate exterior interval. Repeated-root cases follow by
approximating by real simple-root polynomials. Hence, for \(s\ge0\),

\[
1-s\partial_z^2
=(1-\sqrt s\,\partial_z)(1+\sqrt s\,\partial_z)
\]

preserves real-rootedness. The coefficientwise limit

\[
e^{-s\partial_z^2}p
=\lim_{n\to\infty}(1-s\partial_z^2/n)^n p
\]

also preserves it, because fixed-degree polynomials with a fixed nonzero
leading coefficient and all real roots form a closed set. Thus \(P_\tau\)
is all-real whenever \(\tau\ge T\). The same argument proves forward
preservation from any other all-real time.

For times just before \(T\), put \(s=T-\tau>0\) and
\(z=a+\sqrt s\,u\). Expanding the initial polynomial and applying the
finite differential exponential yields, uniformly on compact \(u\)-sets,

\[
\frac{P_{T-s}(a+\sqrt s\,u)}
{(-1)^m C_{\rm pol}(2a)^m s^{m/2}}
\longrightarrow e^{\partial_u^2}u^m.
\tag{23}
\]

Indeed \((z^2-a^2)^m=(2a\sqrt s\,u+s u^2)^m\), and every term beyond
the leading monomial has a factor \(\sqrt s\) after normalization.

Let \(h_m(u)=e^{-\partial_u^2}u^m\). Its Rodrigues formula is

\[
h_m(u)=(-2)^m e^{u^2/4}
\frac{d^m}{du^m}e^{-u^2/4}.
\]

Integration by parts shows orthogonality to every lower-degree polynomial
under \(e^{-u^2/4}\,du\). If \(h_m\) had fewer than \(m\) real sign
changes, multiplying it by the product of its real sign-change factors
would give a nonzero constant-sign integrand of lower-degree test type,
contradicting that orthogonality. Thus \(h_m\) has \(m\) distinct real roots.

Now \(e^{\partial_u^2}u^m=i^{-m}h_m(iu)\), so its roots are simple
and imaginary. Because \(m\ge2\), at least two are nonzero and nonreal.
Rouché's theorem on small circles separated from the real axis, applied
to (23), gives nonreal roots of \(P_{T-s}\) for every sufficiently small
\(s>0\). If any earlier time \(\tau_0<T\) were all-real, forward preservation
would contradict this fact. The threshold is therefore exactly \(T\).

### Proof of imaginary-axis positivity

Set \(W_\tau(y)=P_\tau(iy)/C_{\rm pol}\). Since
\(\partial_z^2=-\partial_y^2\) under this substitution,

\[
W_\tau(y)=e^{(\tau-T)\partial_y^2}(y^2+a^2)^m.
\]

For \(\tau\ge T\), all coefficients are nonnegative and the constant
coefficient is positive. For \(0\le\tau<T\), put \(s=T-\tau\le T\).
The coefficient of \(y^{2j}\), divided by its positive initial coefficient
\(\binom mj a^{2(m-j)}\), is

\[
1+\sum_{k=1}^{m-j}\frac{(-s/a^2)^k}{k!}
\frac{(m-j)!}{(m-j-k)!}
\frac{j!}{(j+k)!}\frac{(2j+2k)!}{(2j)!}.
\]

The last two factorial ratios have product

\[
\prod_{r=1}^k2(2j+2r-1)\le\{2(2m-1)\}^k,
\]

and \((m-j)!/(m-j-k)!\le m^k\). Hence the absolute value of the
entire perturbing tail is at most

\[
e^{2m(2m-1)T/a^2}-1\le e^{1/2}-1<1.
\]

Every coefficient remains strictly positive. This proves the asserted
positivity on the whole imaginary axis at every nonnegative time.

### Equality in every exact-multiplicity mirror test

At time \(T\), deflating the root \(a\) leaves

\[
g(z)=(-1)^m C_{\rm pol}(z+a)^m,
\qquad S_0=\frac m{4a^2}.
\]

With \(A_T=1\), the leading jets satisfy

\[
q_m=(-1)^m C_{\rm pol}m!(2a)^m,
\quad \frac{q_{m+1}}{(m+1)q_m}=\frac m{2a},
\quad \frac{2q_{m+2}}{(m+1)(m+2)q_m}
=\frac{m(m-1)}{4a^2}.
\]

Substitution in (10)–(11) gives \(\mathscr D_m=0\). Dividing the flow
by the same prescribed positive, zero-free local analytic normalizer
transports it into the normalized heat equation and preserves equality in
the corresponding \(b_x\)-corrected mirror test. This operation supplies
neither the zeta arithmetic coefficients nor their holomorphic approximation
theorem, genuine density, or positive theta-kernel representation.

## 6. Sharpness of the absolute curvature-to-average bound

Fix \(M_2>0\), \(h>0\), \(L>0\), and \(T>0\). In the preceding
construction take \(m=2\) and amplitude

\[
C_a=\frac{M_2}{8a^2+24ah+12h^2}.
\]

At threshold, on \(0\le y\le h\),

\[
P_T'(a+y)=4C_a(a+y)y(2a+y),
\qquad
0<P_T''(a+y)=C_a\{8a^2+24ay+12y^2\}\le M_2.
\]

As \(a\to\infty\), \(P_T'(a+y)\to M_2y\) uniformly for this fixed
interval. Therefore

\[
\boxed{
\lim_{a\to\infty}\frac1h\int_0^h
\left(\frac{2P_T'(a+y)}L\right)^2dy
=\frac{4M_2^2h^2}{3L^2}.}
\tag{24}
\]

The remaining roots lie at \(-a\), so \(d=2a>h\) for sufficiently large
\(a\), and the imaginary-axis positivity condition also holds. This
asymptotically attains the existing absolute Taylor upper bound while
retaining an ordinary double collision at an exact positive threshold.

If \(h>\sqrt{3/32}\,L/M_2\), sufficiently large \(a\) makes the average
strictly larger than \(1/8\), despite the collision and curvature bound.
Thus the old transfer deficit cannot be removed by only generic heat,
real-root geometry, imaginary-axis positivity, and root-free coverage.
This example uses \(A_T=1\); it does not obstruct a transfer using genuine
density, the prescribed arithmetic coefficients, or their fixed normalizer.

## 7. Analytical consequences for the continuing program

The density floor (17) is a genuine strengthening of the necessary signed
threshold inequality. Its proof retains disjoint zero blocks, not an
absolute arithmetic coefficient bound. The paid Schur cones in Heat Note 20
can use that stronger target without a numerical search.

The local-growth lemma gives another explicit target: prove
candidate-conditioned control of the leading deflated coefficient, slope,
root distances, and complete inverse-square sum sufficient for (7) or (8)
on an interval with a paid lower derivative average. The existing long
probe cannot be covered by a single root-free chart. A shorter genuinely
signed arithmetic average, or a controlled transfer through the intervening
roots, would be additional theorems.

The genuine count gives a pointwise multiplicity bound, but not a fixed
finite hierarchy through the small-time endpoint. The arbitrary-multiplicity
polynomial models explain why mirror inequalities and heat dynamics alone
cannot provide the missing uniform restriction. A signed arithmetic proof
covering only ordinary doubles must retain higher multiplicity as an
explicit obligation. A uniform general-\(m\) argument must pay its derivatives
and lower-jet constraints uniformly; the structural constants of a
factorial-normalized Schur cone do not establish that arithmetic uniformity.
