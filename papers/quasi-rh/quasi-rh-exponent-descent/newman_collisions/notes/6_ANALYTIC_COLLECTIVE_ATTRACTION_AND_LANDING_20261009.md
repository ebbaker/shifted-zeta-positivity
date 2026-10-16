# Analytic collective attraction and improved landing times

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Same-model cross-review is an internal check, not independent validation.

The heat-flow investigation now targets quantitative collective attraction
at positive time. Expansion of the compact numerical rectangles in
[Notes 4](4_CERTIFIED_COMPACT_CUTOFF_CROSSING_20261009.md) and
[5](5_CERTIFIED_ZERO_BEARING_DERIVATIVE_CELL_20261009.md) is deferred.

Two analytic results give intermediate progress. A sharp comparison of the
exact attraction field with an off-zero logarithmic derivative permits
every probe height above the maximal zero height. Separately, uniform
counts of **all** zeros give a global attraction floor and a strictly
improved landing formula without locating neighbors. The counting constant
remains implicit; no new numerical Newman bound or literature novelty is
claimed. Applied to the original unit strip, the count argument recovers
the already known qualitative conclusion \(\Lambda<1/2\).

## 1. Exact attraction and projected attraction

Use the standard normalization \(H_0(z)=\xi(1/2+iz/2)/8\) and
\(\partial_tH_t=-H_t''\). At a simple nonreal zero \(z=x+iy\), \(y>0\),
whose imaginary height is maximal among all zeros, put \(w=y^2\) and

\[
 E_t(z)=\frac1y\sum_{\rho\ne z,\bar z}
 \frac{y-\Im\rho}{(x-\Re\rho)^2+(y-\Im\rho)^2},\qquad
 G_t(z)=\sum_{\rho\ne z,\bar z}
 \frac1{(x-\Re\rho)^2+4w}.
 \tag{1}
\]

Zeros are counted with multiplicity; canonical-product sums are grouped
under the real symmetries. The simple-zero motion formula gives

\[
 w'=-2-4wE_t(z),\qquad E_t(z)\ge G_t(z)\ge0.
 \tag{2}
\]

The minus two is exactly the own conjugate's contribution. A real external
zero at horizontal distance \(d\) contributes \(1/(d^2+w)\) to \(E\).
An external conjugate pair \(a\pm iv\), \(0<v\le y\), contributes

\[
 \frac1y\left[
 \frac{y-v}{d^2+(y-v)^2}+\frac{y+v}{d^2+(y+v)^2}\right],
 \qquad d=x-a.
\]

Grouping the pair gives at least \(2/(d^2+4w)\). Thus the projected field
can be bounded using horizontal counts without assuming external zeros
are real. The zero-motion and local Hermite-splitting theorems are imported
from [Polymath, Proposition 3.1](https://arxiv.org/html/1904.12438#S3.Thmproposition1).
The projected-field method is developed in
[Planat, Section 2](https://arxiv.org/html/2609.37164v2#S2); that preprint's
numerical certificates and endpoints are not inputs here.

## 2. A sharp logarithmic derivative comparison

For \(\eta>y\), define

\[
 L_\eta(t,x)=-\Im\frac{H_t'}{H_t}(x+i\eta),\qquad
 K(c)=\min\left\{1,\frac{c^2-1}{4}\right\},\quad c=\eta/y.
\]

The probe is above every zero, so it is zero-free. The canonical product
gives the positive external contribution

\[
 Q_\eta=\frac{L_\eta}{\eta}-\frac2{\eta^2-w}\ge0.
\]

**Exact-field comparison.** Every \(\eta>y\) satisfies

\[
 E_t(z)\ge K(\eta/y)Q_\eta.
 \tag{3}
\]

This statement concerns \(E\). It does not assert the corresponding
inequality for \(G\) when \(\eta<\sqrt5\,y\). At larger probe heights it
recovers a consequence of the existing projected-field bridge; the
additional range below \(\sqrt5\,y\) has a smaller explicit factor.

**Proof.** For an external pair, write
\(s=d^2/y^2\), \(u=1-v^2/y^2\), and \(q=\eta^2/y^2-1\).
Then \(s\ge0\), \(0\le u\le1\), \(q>0\). Apart from the common scale
\(2/y^2\), its exact and probe kernels are

\[
 e=\frac{s+u}{D_E},\quad p=\frac{s+q+u}{D_Q},\qquad
 D_E=s^2+2(2-u)s+u^2,\quad
 D_Q=s^2+2(q+2-u)s+(q+u)^2.
\]

The denominators are positive except at the excluded configuration
\(s=u=0\), which would coincide with the target pair.
For \(0<q\le4\), the cleared numerator of \(4e-qp\) is

\[
\begin{aligned}
&4(s+u)D_Q-q(s+q+u)D_E\\
&=(4-q)s^3
 +[12+4(1-u)+q(4-q)+uq]s^2\\
&\quad+u[12+4(1-u)+12q+2q^2+qu]s
 +u(u+q)[(4-q)u+4q].
\end{aligned}
 \tag{4}
\]

Every displayed factor is nonnegative. For \(q\ge4\), the numerator of
\(e-p\) factors as

\[
 (s+u)D_Q-(s+q+u)D_E
 =q[s^2+(q-4+6u)s+u(q+u)]\ge0.
 \tag{5}
\]

A real external root has exact/probe ratio
\((s+q+1)/(s+1)\ge1\). Summing proves (3).
For a pair with \(u=0\), the ratio tends to \(q/4\) as
\(s\downarrow0\), while at \(s\to\infty\) it tends to one. Thus the
factor is sharp for the allowed pairwise geometry; this does not assert
that extremal configurations occur for zeta. \(\square\)

In the nearer-probe range \(y<\eta\le\sqrt5\,y\), substitution into (2)
cancels the own-pair terms exactly:

\[
 w'\le-(\eta^2-w)\frac{L_\eta}{\eta}.
 \tag{6}
\]

The classical bound \(w'\le-2\) remains available, so (6) gives an
additional gain whenever \((\eta^2-w)L_\eta/\eta>2\).
An adaptive probe \(\eta=\eta(w)\) is evaluated instantaneously in (6);
no derivative of the probe occurs in the zero-motion identity.

For a fixed \(\eta>\sqrt{w_0}\) and a uniform lower bound
\(L_\eta\ge L_0\), a sufficient constant field floor is

\[
 E_t(z)\ge K(\eta/\sqrt{w_0})
 \max\left\{0,\frac{L_0}{\eta}-\frac2{\eta^2-w_0}\right\}
 \quad(0<w\le w_0).
 \tag{7}
\]

The true-function derivative can be bounded using the normalized
approximation and paid Cauchy errors in
[Note 3](3_NORMALIZED_HEAT_COLLISION_CRITERION_20261008.md).
The bound must cover the maximizing zeros throughout the relevant time
and spatial domains. A probe bound in one high-height sector alone is
insufficient for a global endpoint.

## 3. A global field from uniform counts of all zeros

Let \(N_t(R)\) count every zero with \(0<\Re\rho\le R\), including
multiplicity, and retain the time-dependent main term

\[
 p_t(R)=\frac{R}{4\pi}\log\frac{R}{4\pi}
 -\frac{R}{4\pi}+\frac{11}{8}
 +\frac{t}{16}\log\frac{R}{4\pi}.
\]

The imported count theorem supplies an absolute \(A\ge0\) such that

\[
 |N_t(R)-p_t(R)|\le A\log(2+R),
 \qquad 0<t\le1/2,\quad R\ge4\pi.
 \tag{8}
\]

[Polymath, Theorem 1.5(iv)](https://arxiv.org/html/1904.12438#S1.Thmtheorem5)
explicitly makes its error constants independent of \(t\). The numerical
value of \(A\) is not supplied here. Endpoint conventions can be absorbed
into \(A\) using the same theorem's local count bound.

Set

\[
 D=8\pi(4A+1),\quad X_* =\max\{(4\pi)^2,2D,3\},\quad
 n=\log X_*,\quad B=X_*+2D.
 \tag{9}
\]

**Global counting floor.** For every simple maximal-height nonreal zero
and every \(0<t\le1/2\),

\[
 E_t(z)\ge G_t(z)\ge\frac{n}{B^2+4w}.
 \tag{10}
\]

**Proof.** Evenness allows \(x\ge0\). If \(x\ge X_*\), use only roots
with real parts in \((x+D,x+2D]\). Neither member of the own pair is
there. On this interval,

\[
 p_t'(R)=\frac1{4\pi}\log\frac R{4\pi}+\frac{t}{16R}
 \ge\frac{\log x}{8\pi}.
\]

Because \(x\ge2D,3\), both endpoint-error logarithms are at most
\(2\log x\): indeed \(2+x+2D\le2+2x\le x^2\).
The number of roots in the block is at least

\[
 \left(\frac D{8\pi}-4A\right)\log x=\log x.
\]

Their horizontal distances are at most \(2D\), giving
\(G_t\ge\log x/(4D^2+4w)\).
If \(0\le x\le X_*\), use the fixed block
\((X_*+D,X_*+2D]\). The preceding count at \(x=X_*\) gives at least
\(n\) roots, all at horizontal distance at most \(B\). For the large
\(x\) case, use \(\log x\ge n\) and \(B\ge2D\). These observations
give the common floor (10). \(\square\)

This floor requires no horizontal confinement assumption. It counts
external nonreal roots as well as real roots and remains uniform as
positive times approach zero. That uniformity is a property of the
count theorem, not of the eventual-real-zero cutoff \(\exp(C/t)\).

The reflected own pair also gives
\(G_t(z)\ge1/[2(x^2+w)]\), since there are no purely imaginary zeros.
It can improve a bound in a bounded spatial sector. The density floor,
reflected-pair floor, and full probe floor overlap in their zero
contributions and must ordinarily be combined by a **maximum**, not a sum.
Adding bounds requires disjoint zero blocks or a separate joint inequality.

## 4. The improved landing formula

Suppose a valid initial strip estimate at time \(t_0\ge0\) gives squared
height at most \(w_0>0\), with \(t_0+w_0/2\le1/2\). Define

\[
 F_{n,B}(w)=\frac{w}{n+2}
 +\frac{B^2n}{4(n+2)^2}
 \log\left(1+\frac{2(n+2)w}{B^2}\right).
 \tag{11}
\]

Then

\[
 \Lambda\le t_0+F_{n,B}(w_0)<t_0+\frac{w_0}{2}.
 \tag{12}
\]

More generally, any continuous global floor \(E_t(z)\ge g(w)\ge0\)
gives the landing duration
\(\int_0^{w_0}[2+4u g(u)]^{-1}\,du\).
For (10), direct differentiation yields

\[
 F_{n,B}'(w)=\frac{B^2+4w}{2B^2+4(n+2)w}
 =\frac1{2+4wn/(B^2+4w)}.
 \tag{13}
\]

**Maximum switches and multiple roots.** On a compact positive-time
interval, eventual reality confines the nonreal zeros to a common
compact rectangle. There are uniformly finitely many zeros there.
The local Hermite expansion splits each multiple root into distinct
branches at nearby times, so multiple-root events in this compact
region are isolated and finite. Root branches are analytic away from
these events and analytic in the local square-root time parameter
near them. Their derivatives have integrable singularities.

The maximal squared height \(W(t)\), with zero included, is consequently
continuous and absolutely continuous on such intervals. At almost
every time with \(W>0\), a maximizing simple branch gives

\[
 W'\le-2-\frac{4nW}{B^2+4W},\qquad
 \frac{d}{dt}F_{n,B}(W(t))\le-1.
\]

All maximizers have the same field floor, so switching does not affect
the inequality. Integration across the finite collision events gives
(12). No field value at a multiple root itself is needed.

For \(t_0=0\), start instead at \(\varepsilon>0\). Classical strip
contraction gives \(W(\varepsilon)\le\max(w_0-2\varepsilon,0)\).
Apply the positive-time argument and let \(\varepsilon\downarrow0\).
This uses no attained maximum over nonreal zeros at time zero.
Once all roots are real, the usual threshold theorem preserves reality.

The gain has a useful explicit lower bound:

\[
 \frac w2-F_{n,B}(w)
 =\int_0^w\frac{nu}{B^2+2(n+2)u}\,du
 \ge\frac{nw^2}{2[B^2+2(n+2)w]}>0.
 \tag{14}
\]

For fixed \(n,B\), the gain begins at \(nw^2/(2B^2)\) as
\(w\downarrow0\). It is a strict quantitative improvement in terms
of the count parameters, but can be very small for coarse parameters.

## 5. Scope and the next analytic checkpoint

Equations (3), (10), and (11) are intermediate results at positive time.
The exact-field bridge and global counting argument are derived here
and cross-checked against the imported inputs; their originality in
the literature has not been established. The count theorem itself,
the zero dynamics, and the threshold property remain imported.

The counting constant can be made effective in principle, but the
source's proof passes through an approximation extended to imaginary
height three, unprinted growth constants in Jensen estimates, a
large-height cutoff, and a bounded initial segment. Making those
constants explicit is a separate analytic task. Merely assigning a
number to the source's \(O\)-notation would not prove a bound.

The next bounded task is to derive an effective logarithmic-derivative
lower bound in one chosen positive-time range, using (3) and retaining
all approximation and derivative errors. A useful output is a closed
analytic inequality in the initial strip width and the spatial
threshold, with explicit costs and an exact landing comparison.
The global count floor supplies a fallback outside any stronger
probe sector; the minimum across sectors is the valid global floor.
A stronger global conclusion needs control of every sector in which
a maximizing root may lie. Numerical rectangle expansion is deferred.

An improved value of \(\Lambda\) alone cannot be fed back as an earlier
strip estimate: strip contraction runs forward in time. Near an
ordinary hypothetical collision at \(T>0\),
\(w(t)=2(T-t)+O((T-t)^2)\), consistent with a finite positive field.
No iteration to zero follows from these results.

## 6. Verification and review

[The exact checker](../../numerics/check_collective_attraction_algebra.py)
verifies the universal polynomial identities (4), (5), the own-pair
cancellation, and the landing derivative and gain algebra by exact
coefficient equality. Supplementary rational substitutions check
the boundaries and denominator signs. It performs no heat-function
evaluation, zero search, or spatial/time grid.

The [small replay record](../../numerics/collective_attraction_algebra_record_20261009.json)
binds the checker hash. The [scoped review](../../reviews/COLLECTIVE_ATTRACTION_ANALYTIC_REVIEW_20261009.md)
records the separate kernel, counting, and envelope audits and the
remaining effective-constant obligation.
