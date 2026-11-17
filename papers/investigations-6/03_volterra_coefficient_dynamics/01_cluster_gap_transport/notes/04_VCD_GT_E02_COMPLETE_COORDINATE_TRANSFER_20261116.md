# Contour transfer at physical and model cluster coordinates

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Helper dispatch selected
**gpt-6.1-sol / ultra**. Separate backend attestation of actual execution
settings and the lead's actual recorded settings are unavailable.

**Proved in-note under the stated two-zero geometry.** This is analytical
support for the signed transport consumer in VCD-GT-B01. The proof
supplies transfer constants and a signed cumulative cost allowance.
Canonical geometry and a useful signed model cost remain application
inputs. See the [frozen E02 r1 request](../research-progress/handoffs/VCD-GT-E02-r1.md),
[plan §3](../research-plan/01_VCD_GT_RESEARCH_PLAN_20261116.md), and
[overview](../research-overview/01_VCD_GT_RESEARCH_OVERVIEW_20261116.md).

## 1. Fixed geometry and collar budget

Let \(I=[u,v]\) and let \(\Gamma=\{|z-a|=\rho\}\) be fixed,
counterclockwise, with \(a\in\mathbb R\) and length \(L=2\pi\rho\).
For each time, let \(F=F_\lambda\) and \(G=G_{N,\lambda}\) be holomorphic
on a neighborhood of the closed disk, real under conjugation, and
nonvanishing on \(\Gamma\). Assume each has exactly two zeros in the
disk, counting multiplicity. Both pairs lie in one fixed inner convex
region \(U\) of the disk with \({\rm dist}(U,\Gamma)\ge b>0\).
The region may contain real roots, a conjugate pair, or a double root.
In particular \(|w-a|\le \rho-b\) for every \(w\in U\).
All time functions in the estimates below are assumed measurable,
with the displayed time budgets integrable. The canonical fields and
contour coordinates have their inherited time regularity.

Use \(Q(z)=(z-c)^2-D,\ Q_N(z)=(z-c_N)^2-D_N\) for the two
monic pair polynomials, and set \(h=(F/Q)'/(F/Q)\) and
\(h_N=(G/Q_N)'/(G/Q_N)\), with primes here denoting \(z\)-derivatives.
These logarithmic derivatives are holomorphic through the cluster
zeros. The real centers and discriminants are the contour moments of
[parent Note 27](../../notes/27_VCD_CLUSTER_RESOLUTION_AND_HEAT_COLLISIONS_20261116.md)
and [manuscript §10.4](../../manuscript/sections/cluster_resolution.tex).
Let \(e_N\ge |c_N-c|\), \(d_N\ge |D_N-D|\), and
\(M_N\ge\sup_\Gamma |G'/G|\) be nonnegative allowances, possibly
time-dependent.

Assume a single-valued holomorphic logarithm \(H=\log(F/G)\) on a
collar of \(\Gamma\), with \(\sup_\Gamma|H|\le\ell_N\). For example,
if \(\sup_\Gamma|F-G|\le\delta_N\) and
\(\inf_\Gamma|G|\ge m_N>\delta_N\), the logarithm series gives
\(\ell_N=-\log(1-\delta_N/m_N)\) and extends to some collar by
compactness and strictness. The same construction applies with a floor
for \(F\) by reversing the ratio and the sign of its logarithm. A verified
floor for \(G\) and upper bound \(\sup_\Gamma|G'|\le j_N\) also give
\(M_N=j_N/m_N\). When one field has verified count two, the stated
strict boundary inequality transfers the count by Rouché. The inner
buffer is a separate payment, for example via a verified count on a
smaller concentric circle for both fields. A contour zero-exclusion
condition on its own supplies no value for \(\ell_N\).

For an explicit coordinate payment, put
\(p_k=(2\pi i)^{-1}\oint_\Gamma (z-a)^k F'/F\,dz\) and define
\(p_{k,N}\) using \(G\). Since \(H'=F'/F-G'/G\), integration by parts
around the closed contour gives

\[
 |p_k-p_{k,N}|\le\frac{kL\rho^{k-1}}{2\pi}\ell_N.
\]

Each moment sums the \(k\)-th powers of the two zero offsets from \(a\).
Using \(c-a=p_1/2,\ D=p_2/2-(c-a)^2\) and the same formulas for the
model, one may take

\[
 e_N=\frac{L}{4\pi}\ell_N=\frac{\rho}{2}\ell_N,\qquad
 d_N=\frac{L\rho}{2\pi}\ell_N+2(\rho-b)e_N
       =\rho(2\rho-b)\ell_N.                                      \tag{1}
\]

The manuscript's \(d_N=2\rho^2\ell_N\) also suffices. Any independently
paid tighter enclosures of the coordinate differences can be used.

## 2. Both contour comparisons

For \(Q_*=(z-c_*)^2-D_*\) with both zeros inside the disk, write

\[
 \mathcal T[B;c_*,D_*]=\frac1{2\pi i}\oint_\Gamma \frac{B(z)}{Q_*(z)}\,dz .
\]

Applied to a holomorphic \(B\), the integral equals its divided
difference at the zeros of \(Q_*\), or \(B'(c_*)\) when \(D_*=0\).
For the physical and model pairs we can use the whole logarithmic
derivatives \(F'/F\) and \(G'/G\) on the boundary. Indeed
\((Q'/Q)/Q_*\) is rational, all of its poles lie inside \(\Gamma\),
and it is \(O(z^{-3})\) at infinity. Its integral vanishes, by
enlarging the contour and taking its radius to infinity. The same
holds for \((Q_N'/Q_N)/Q_*\), even if the two pair polynomials have a
common root or either one has a double root. Thus the following three
quantities are the indicated unit divided differences:

\[
\begin{aligned}
 K &=\mathcal T[F'/F;c,D],\\
 K_N(c,D)&=\mathcal T[G'/G;c,D],\\
 K_N &=\mathcal T[G'/G;c_N,D_N].
\end{aligned}                                                     \tag{2}
\]

Their values are real by conjugation symmetry, including when the
arguments form a conjugate pair. This agrees with the projection
in [parent discussion28 §2](../../notes/28_VCD_COLLISION_CONTROL_ROUTE_DISCUSSION_20261116.md).

For the common physical arguments, use the collar logarithm before
taking an absolute bound:

\[
 K-K_N(c,D)
 =\frac1{2\pi i}\oint_\Gamma\frac{H'(z)}{Q(z)}\,dz
 =-\frac1{2\pi i}\oint_\Gamma H(z)(1/Q(z))'\,dz.
\]

Since \(1/Q=\prod_{j=1}^2(z-r_j)^{-1}\) and each
\(|z-r_j|\ge b\) on \(\Gamma\), \(|(1/Q)'|\le 2/b^3\), including for
repeated \(r_j\). Therefore

\[
 |K-K_N(c,D)|\le \frac{L\ell_N}{\pi b^3}.                            \tag{3}
\]

This applies the same scalar-log integration by parts as
[Rodgers–Tao branch Note 02 §4](../../../../investigations-5/02_heat_flow_rh_applications/rodgers_tao/notes/02_CORRECTED_PROPAGATION_AND_CONTOUR_FORCE_TRANSFER_20261026.md),
here to the regular pair divided difference. The collar avoids choosing
a ratio logarithm through either interior zero set.

For the coordinate change, subtract the rational kernels:

\[
 \frac1Q-\frac1{Q_N}=\frac{Q_N-Q}{QQ_N},\qquad
 Q_N-Q=(c-c_N)(2z-c-c_N)+(D-D_N).
\]

Both \(|Q|\) and \(|Q_N|\) are at least \(b^2\) on \(\Gamma\).
The center of each pair is in \(U\) by convexity, so
\(|2z-c-c_N|\le 4\rho-2b\) there. Taking the model boundary derivative
bound gives

\[
 |K_N(c,D)-K_N|
 \le\frac{LM_N}{2\pi b^4}\big((4\rho-2b)e_N+d_N\big).               \tag{4}
\]

In particular, define the complete pointwise remainder

\[
 \kappa_N(\lambda)=\frac{L\ell_N}{\pi b^3}
  + \frac{LM_N}{2\pi b^4}\big((4\rho-2b)e_N+d_N\big).
 \quad\text{Then}\quad |K-K_N|\le \kappa_N.                          \tag{5}
\]

There is no root matching in (1)–(5). The denominators reflect the
contour buffer alone. If the physical or model discriminant vanishes,
its own term in (2) is the unit derivative at its center, with the
same estimates. A small outer buffer or large \(M_N\) can still make
the bound expensive.

## 3. Signed time cost and evaluation allowances

Use the inherited physical equation \(D'=2+4KD\), valid through
\(D=0\). At a simple pair this follows from
\(r_\pm'=\pm 1/\sqrt D+2h(r_\pm)\). At a double event the contour
expressions for \(D\) and \(K\) are regular and the model-free
calculation in Proposition 10.6 gives \(D'=2\). These are physical
derivatives. \(G\) enters only through its independent snapshots
in (2)–(5).

Define the signed cumulative quantities and the remainder by

\[
 S(t,v)=4\int_t^v K(s)\,ds,\qquad
 S_N(t,v)=4\int_t^v K_N(s)\,ds,\qquad
 \mathfrak E_N(t,v)=4\int_t^v \kappa_N(s)\,ds .
\]

Then \(|S-S_N|\le \mathfrak E_N\), so for the complete cost
\(\mathcal C(u,v)=2\int_u^v e^{S(t,v)}\,dt\) one has

\[
 2\int_u^v e^{S_N(t,v)-\mathfrak E_N(t,v)}\,dt
 \ \le\ \mathcal C(u,v)\
 \le\ 2\int_u^v e^{S_N(t,v)+\mathfrak E_N(t,v)}\,dt .                \tag{6}
\]

All contributions of \(K_N\) retain their signs in \(S_N\).
For example, suppose \(\widetilde K_N\) is a real model evaluator
with \(|K_N(s)-\widetilde K_N(s)|\le\eta_K(s)\), and the reported
\(\widehat S_N(t,v)\) differs from \(4\int_t^v\widetilde K_N\) by at
most \(\eta_S(t)\) for every \(t\in I\). Here \(\eta_K\) can include
model coordinate enclosures and contour evaluation errors for (2),
and \(\eta_S\) includes interpolation or time quadrature errors in
the primitive. With \(\widehat{\mathfrak E}_N(t)\ge\mathfrak E_N(t,v)\),
a paid upper
integrand is

\[
 W^+(t)=\exp\!\left(\widehat S_N(t,v)+\widehat{\mathfrak E}_N(t)
                         +4\int_t^v \eta_K(s)\,ds+\eta_S(t)\right).  \tag{7}
\]

Any approximation to the nonnegative error integrals in (7) needs an
upper enclosure. If the reported \(\widehat{\mathcal C}\) satisfies
\(2\int_u^v W^+(t)\,dt\le\widehat{\mathcal C}+\eta_{\mathcal C}\),
including outer time quadrature and exponent evaluation in
\(\eta_{\mathcal C}\), then \(B=\widehat{\mathcal C}+\eta_{\mathcal C}\)
is an upper cost. Pointwise samples alone supply neither of these
time-interval bounds. Equation (6) also applies directly if the
signed primitive and its cost are handled analytically.

The integrating-factor identity gives

\[
 e^{S(x,v)}D(x)=D(v)-2\int_x^v e^{S(t,v)}\,dt
 \qquad(x\in I).
\]

Thus a paid incoming lower bound \(L_v\le D(v)\) with \(L_v>B\)
yields positive \(D\) on \(I\). The inequality \(L_v\ge B\) yields
nonnegative \(D(u)\) and, for \(u<v\), strictly positive \(D(x)\)
at \(u<x\le v\), since the integrand is positive. A lower coordinate
enclosure \(D_N(v)-d_N(v)\) is one possible acquisition of \(L_v\).
The transfer alone supplies neither a canonical incoming value nor
a signed model primitive that wins this comparison. The pointwise
same-information baseline remains \(D_N-d_N\), with separated root
jets available wherever their additional slope floors are paid.
No improvement against those baselines is asserted here.

## 4. Endpoint and control checks

For the exact quadratic heat field
\(F_\lambda=(z-a)^2-2(\lambda-T)\), one has \(c=a\),
\(D=2(\lambda-T)\), \(h=0\), and \(K=0\). Take the shifted model
\(G_\lambda=F_\lambda-\varepsilon\) with \(\varepsilon>0\), so
\(D_N=D+\varepsilon\) and \(K_N=K_N(c,D)=0\). Choose a fixed circle
with \(\rho^2>\sup_I |D+\varepsilon|+\varepsilon\). Both pairs then
fit in an inner disk with positive buffer, \(m_N\ge
\rho^2-\sup_I|D+\varepsilon|>\varepsilon\), and the logarithm
budget is finite through both double times. The actual transfer error
vanishes even where the discriminants have different signs. When
\(\varepsilon=0\), (5) gives zero using the exact zero error allowances.
The exact cost is \(2(v-u)\). With incoming gap \(2(v-T)\), the
comparison is strict for \(u>T\), is saturated at \(u=T\), and fails
for \(u<T\). This example checks the orientation, the factor of two,
and the distinction between a nonnegative and a strictly positive
left endpoint. For a constant signed \(K=k\ne 0\), direct evaluation
gives \((e^{4k(v-u)}-1)/(2k)\), including \(k<0\), tending to
\(2(v-u)\) at \(k=0\).

The analytical premise screen uses the [result index](../../../../../result-summaries/README.md),
[collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md),
[avoid index](../../../../../avoid/README.md), and patterns
[01](../../../../../avoid/01_restating_the_target.md),
[02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
and [07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).
The generic bound (5) applies wherever its geometric and approximation
premises hold. For a counted tube spanning a double event at \(u=T\)
and extending to \(v>T\), the exact incoming gap equals the exact
cost, so the strict success premise \(L_v>B\) fails. For a short tube
starting before that event with \(D(u)<0\), even \(L_v\ge B\) fails.
These statements concern tubes with the indicated isolated double
event and sign orientation. The controls were screened analytically
using their established scopes and [discussion28 §5](../../notes/28_VCD_COLLISION_CONTROL_ROUTE_DISCUSSION_20261116.md).

| Control | Premise verdict |
| --- | --- |
| Polynomial/Hermite example | Has local heat evolution, an isolated pair and a buffered collar. The explicit quadratic exhausts the strict gap budget at its event. It lacks a positive theta source. |
| Euler-factor sources | Fail unchanged ordinary theta/Dirichlet coefficients. The positive-threshold witnesses rule out a global inference from a late real slice alone. A threshold witness by itself does not specify a counted local tube. |
| Weighted-square and finite-tail controls | Fail full canonical reflection/completion in the weighted-square examples or unchanged coefficients for a nonzero finite-tail change. The recorded finite-source class also fails a finite all-real global anchor. An isolated double event can still obey the local transfer and exhaust the strict budget. |
| Reflected super-Gaussian and smooth shape/positive-primitive controls | Fail unchanged integer-square theta arithmetic, even with the stated reflection or primitive properties. Regular local unit and contour bounds remain compatible with their events. |
| Atomic BW-01/finite-profile and continuous finite-profile controls | Fail unchanged full theta profile and threshold eventual simplicity, as recorded. The atomic chains also lack an infinite nondegenerate Jacobi continuation. Finite profiles do not supply the required strict gap margin at a counted event. |
| Finite-prime, finite-head, and finite-score controls | Fail full canonical identities even when selected finite measurements match. Their recorded constructions do not claim fixed-region events or a finite global threshold. Small local approximation error would still have to be compared with the incoming gap and signed cost. |
| RH-conditional normalized endpoint control | The perturbed sources fail ordinary Dirichlet arithmetic and the construction retains its RH premise. Its endpoint double illustrates the distinction between the two cost comparisons when the local premises hold. |
| Changed polynomial observation kernels and actual-theta finite-profile relaxations | The former fail the physical Fourier/heat equation. The latter fail the premise of a specified actual analytic field with a counted pair. Neither is an event of the canonical physical field. |

This support proof uses the prescribed fixed pair, buffer and kernel.
No source-specific cost inequality was tested, and no numerical
certificate was rerun. A paid canonical tube still requires count,
modulus, collar size sufficient for a logarithm, inner localization,
data for (1) or tighter coordinate enclosures, \(M_N\), and the signed
time and evaluation budgets relative to \(L_v\). The comparison here
does not supply these values, changing-contour composition, or coverage
at unbounded height. Those missing canonical inputs remain with the
named B decisions in the research plan.
