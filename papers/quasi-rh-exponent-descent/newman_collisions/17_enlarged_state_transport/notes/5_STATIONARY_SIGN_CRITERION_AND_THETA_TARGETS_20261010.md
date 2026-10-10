# A stationary-sign criterion and complete theta targets

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); active reasoning effort unavailable to this session
and not inferred. This is internal LLM derivation and parallel review,
not independent mathematical validation.

## 1. A sufficient condition covering every multiplicity

Let \(H\) be a real analytic solution of \(H_t=-H_{xx}\) on an open
set \(\Omega\subset\{t>0\}\). Assume each zero of a spatial slice under
consideration has finite multiplicity. If throughout \(\Omega\)
\[
H H_{xx}\le0\quad\hbox{whenever }H_x=0,
\tag{S0}
\]
and
\[
H_xH_{xxx}\le0\quad\hbox{whenever }H_{xx}=0,
\tag{S1}
\]
then \(H=H_x=0\) has no solution in \(\Omega\).

The signs are non-strict. Their role is to prohibit a particular stationary
point immediately before a putative collision. For a closed target
domain, the signs must hold on a neighborhood containing those earlier
critical branches, including branches that cross a spatial or cutoff
boundary. A sign at the collision itself is insufficient: both products
there are zero for suitable multiplicities.

For the genuine theta flow, a global proof of these signs for all positive
times and heights would exclude finite positive-time multiple zeros.
The existing [parent threshold and no-escape reduction](../../newman_collision_reductions.tex)
would then supply the RH implication. A proof on a bounded open region
only excludes collisions in that region. No assertion about simplicity
of the zeros at \(t=0\) follows.

## 2. Proof by a rescaled implicit chart

Let \(F_t=-F_{xx}\) have exact even multiplicity \(m=2r\) at
\((T,a)\). Write \(F_j=\partial_x^jF(T,a)\), so \(F_m\ne0\) and
all lower spatial jets vanish. Let \(h=T-t>0\). The heat Taylor expansion
is
\[
F(T-h,a+z)=\sum_{p,q\ge0}\frac{F_{2p+q}}{p!q!}h^p z^q.
\tag{1}
\]
It converges in a sufficiently small neighborhood by joint real
analyticity and the heat relation. After setting \(z=hy\),
\[
K(h,y)=h^{-r}F_x(T-h,a+hy)
\]
extends analytically across \(h=0\). Indeed, every nonzero Taylor term
has \(2p+q+1\ge2r\), hence \(p+q\ge r\). The two terms of degree
exactly \(r\) give
\[
K(0,y)=\frac{F_m}{(r-1)!}y+\frac{F_{m+1}}{r!}.
\]
Its \(y\)-derivative is nonzero. The ordinary implicit function theorem
provides an analytic real curve
\[
\chi(h)=a+h y(h)
=a-\frac{F_{m+1}}{rF_m}h+O(h^2),\qquad
F_x(T-h,\chi(h))=0.
\tag{2}
\]
The same expansion gives
\[
F(T-h,\chi(h))=\frac{F_m}{r!}h^r+O(h^{r+1}),
\quad
F_{xx}(T-h,\chi(h))=\frac{F_m}{(r-1)!}h^{r-1}+O(h^r).
\tag{3}
\]
Consequently
\[
F F_{xx}=\frac{F_m^2}{r!(r-1)!}h^{2r-1}+O(h^{2r})>0
\tag{4}
\]
for sufficiently small \(h>0\). Such points remain in any open
neighborhood of \((T,a)\), and \(h<T\) keeps time positive.

If a multiple zero of \(H\) has even multiplicity, take \(F=H\);
(2)--(4) violate (S0). If it has odd multiplicity \(m\ge3\), take
\(F=H_x\). This is another analytic heat solution, with even
multiplicity \(m-1\). Its earlier critical point has
\(H_{xx}=0\) and \(H_xH_{xxx}>0\), violating (S1). This proves the
criterion, including multiplicities for which the ordinary-double
Jacobian of \((H,H_x)\) is singular.

For a quantified local contradiction, if the remainder in (4) is bounded
by \(M h^{2r}\), choose
\[
0<h<\min\left(T,h_0,
\frac{F_m^2}{2M r!(r-1)!}\right).
\]
Here \(h_0\) is a proved chart and domain radius; if \(M=0\), omit the
last restriction. No such uniform constants for genuine candidates are
claimed in this note. The analytic criterion itself needs no prescribed
minimum separation from the collision.

## 3. What this gains, and what it costs

The fold formulation of the ordinary threshold test in
[Note 4](4_COORDINATE_INVARIANCE_AND_IMPLICIT_HEAT_FOLDS_20261010.md) still
uses the fourth derivative and an all-real threshold hypothesis. The
stationary-sign criterion uses derivatives only through order three and
does not need all-realness. Its input is stronger in a different way: it
requires signs along two complete stationary sets on a predecessor
neighborhood, rather than a test at one hypothetical threshold point.
It supplies neither a first-jet estimate nor a cost improvement by itself.

The signs are stationary restrictions of the familiar quadratic
expressions \(H_x^2-HH_{xx}\) and \(H_{xx}^2-H_xH_{xxx}\). The proof
above needs only the stated restrictions. We make no novelty claim for
the general heat or implicit-function mechanism.

The double Gaussian control violates (S0) just before its collision:
with \(A=H_{xx}(T,a)\ne0\), (3) gives
\(H H_{xx}=A^2h+O(h^2)>0\) on its earlier critical branch. The positive
quadruple Gaussian control gives the same obstruction with order
\(h^3\). The odd cubic heat polynomial
\(F(s,z)=z^3-6sz\) has no real critical points for \(s<0\), so (S0)
alone does not detect its triple zero at \(s=z=0\). Its derivative
has \(F_{xx}=0\) at \(z=0\) and
\(F_xF_{xxx}=-36s>0\) there for \(s<0\). This is an explicit reason
to retain (S1).

## 4. The chord and score quantities to estimate

Use the same complete prepared theta state as the manuscript:
\[
\mathfrak m=e^{tu^2}\Phi_e,\quad W=-\log\mathfrak m,\quad
A(x)=\mathcal A_t(x,0)=2H_t(x),\quad
C(x)=\partial_\ell^2\mathcal A_t(x,0).
\]
Fix \(\beta>0\) when taking spatial derivatives. Define
\[
E(x)=\widehat{\mathfrak m(W'-\beta u)^2}(x),\qquad
D(x)=4C(x)+E(x).
\]
The [Heat Note 25 dictionary](../../notes/25_ENLARGED_STATE_TRANSPORT_CHORD_DYNAMICS_AND_THETA_GLUING_20261010.md)
gives the exact identity
\[
D=-\beta^2A''-2\beta x A'-(x^2+2\beta)A.
\tag{5}
\]
Thus the two sufficient complete-source targets are
\[
A\,[D+(x^2+2\beta)A]\ge0\quad\hbox{on }A'=0,
\tag{T0}
\]
and
\[
A'\,[D'+(x^2+4\beta)A'+2xA]\ge0\quad\hbox{on }A''=0.
\tag{T1}
\]
The left sides equal \(-\beta^2AA''\) and
\(-\beta^2A'A'''\), respectively, on the stated stationary sets.
Since \(A=2H\), (T0)--(T1) are precisely (S0)--(S1).
Only \(D,D'\) are needed in this formulation, although they still encode
the scalar derivatives in (5). If \(\beta\) varies with \(x\), its
derivative terms must be restored; freezing it is part of the identity.

These are signed correlations of the complete theta score and transverse
curvature. Positivity of the density defining \(E\), a positive lifted
norm, or the chord PDE alone does not establish either target. The
Gaussian controls satisfy those generic properties and fail (T0).
The actual theta coefficients, gluing or another genuine preparation
property must supply the new sign. Estimates of independent absolute
overlaps do not automatically give a sign for their correlated products.

## 5. A fully paid approximation interface

Suppose \(a_j\) approximate the genuine physical derivatives
\(H_j\), with \(|H_j-a_j|\le\epsilon_j\), \(0\le j\le3\),
throughout a specified neighborhood. Put
\[
B_{ij}=|a_i|\epsilon_j+|a_j|\epsilon_i+\epsilon_i\epsilon_j.
\]
Then \(|H_iH_j-a_ia_j|\le B_{ij}\). It suffices to prove
\[
a_0a_2+B_{02}\le0\quad\hbox{where }|a_1|\le\epsilon_1,
\tag{P0}
\]
and
\[
a_1a_3+B_{13}\le0\quad\hbox{where }|a_2|\le\epsilon_2.
\tag{P1}
\]
Every genuine stationary point belongs to its corresponding candidate
band. Interval versions must use outward enclosures for products,
candidate bands and all physical derivative errors. These sufficient
tests can be conservative. Close to a collision the forced adverse
product tends to zero, so a fixed absolute error allowance cannot be
assumed harmless. Relative estimates, exact identities or compatible
local error orders would be needed there.

If the available approximation is a normalization \(G=bH\) with
\(b>0\), set \(\lambda=b_x/b\). The physical jets are
\[
H_0=G/b,\quad H_1=(G'-\lambda G)/b,
\]
\[
H_2=[G''-2\lambda G'+(\lambda^2-\lambda')G]/b,
\]
\[
H_3=[G'''-3\lambda G''+3(\lambda^2-\lambda')G'
 +(-\lambda^3+3\lambda\lambda'-\lambda'')G]/b.
\tag{6}
\]
Bounds for the normalization and all coefficients in (6) are part of the
payment. In particular, \(G'=0\) is not the same stationary set as
\(H'=0\). The normalized scalar need not obey the original heat equation.
The complete disk interface can supply Cauchy errors through order three,
but their costs must be calculated; the previous first-jet calibration
does not already certify (P0)--(P1).

## 6. Next research checkpoint

The concrete analytic target is (T0)--(T1) for the actual theta source on
a stated predecessor neighborhood. A bounded experiment should first
enclose its complete stationary candidate sets, then compare the signed
correlation with the full payment in (P0)--(P1) or an equivalent direct
\(A,D,D'\) interface. It must retain normalizer terms, natural-cutoff
changes, cross contributions and endpoint sources. Any claimed uniform
sign must distinguish the Gaussian controls.

This continuation establishes the conditional all-multiplicity criterion
and an exact source dictionary. It establishes neither theta sign,
bounded genuine stationary-set coverage nor a new RH conclusion. The
[checker and record](../numerics/HEAT_TRANSVERSALITY_RECORD_20261010.json)
validate finite polynomial algebra and negative controls; the analytic
IFT argument is proved above and internally audited separately.

Primary heat-flow context:
[Polymath, Proposition 3.1](https://arxiv.org/html/1904.12438v2#S3).
The local proof is explicit rather than inferred from a numerical plot.
