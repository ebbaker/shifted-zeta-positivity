# Global heat geometry: proposals and initial stress tests

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**. Exploratory proposals, analytic calculations,
and same-assistant assessment; no independent or specialist review.

**Purpose.** Assess the proposed global geometric investigations before
opening separate folders. The full function already has global geometric
realizations. Several of them have invariants that vanish at simple zeros
and detect higher multiplicities. The unresolved issue is an additional
constraint coming from the unchanged theta source that bounds these
invariants or prevents their concentration.

The screens below justify further *bounded exploration*, with different
levels of readiness. They do not establish a new simplicity mechanism.
This note stays in the existing brainstorm folder; no new investigation
folders, manuscript additions, or numerical theta campaign accompany it.

Read with the [result index][results], [collision controls][controls],
[local geometry summary][local-summary], [geometric realization summary][geom-summary],
and [avoid index][avoid], especially [target classification][avoid01],
[coordinate lifts][avoid03], and [scoped conclusions][avoid07].
The current [HMC register][progress] continues to govern the existing
program. [Notes 24][n24] and [25][n25] contain the previously derived
Gauss-area defect, relative Chern/Hopf observation, and global-scope
clarification. Their established formulas are inputs here.

## 1. Five ideas, with three possible eventual homes

| Direction | Object and question | Initial screen | Present assessment |
| --- | --- | --- | --- |
| A. Global physical jet geometry | The immersion built from the primitive of the complete \(H\); can curvature transport constrain the endpoint defect? | Multiple zeros give a real defect, but the quadratic heat model produces it in a smooth ambient space. The induced metric is generally not hyperkähler. | Useful geometric formulation; another curvature identity alone would duplicate existing work. |
| B. Relative Chern/Hopf charges | The global map \(G=(H,H_z)\) on complex heat spacetime; can complete boundary data force its local charges to vanish? | The invariant is multiplicity-selective and admits stable boundary certification. Trivial bundles and flat ambient geometry do not force zero charge. | A concrete boundary-estimation problem; arithmetic and cost advantages remain unproved. |
| C. Direct spectral covers and periods | The family \(w^2=H(t,z)\); can vanishing cycles, monodromy, or periods distinguish a multiple endpoint? | A simple zero is a smooth branch point; a multiple zero is a singular fiber point. An exact period calculation survives the collapsing-cycle test without contradiction. | A viable additional representation worth a bounded period calculation. Global finiteness and a source constraint are missing. |
| D. Arithmetic theta-source geometry | The marked elliptic family, theta line bundle, hyperkähler metric, and full transform to \(H\); what geometric relation survives the transform? | The source realization is exact. Direct pullback curvature vanishes, and a simple proposed modular descent fails an explicit transformation test. | The route that directly exposes the arithmetic source; its missing transform estimate is substantial. |
| E. Quantitative Jensen-surface degeneration | Compact curves made from complete theta moments; can their degeneration rates detect multiplicity in the limiting entire function? | Finite topology cannot prove simplicity. An explicit approximation bound and double/triple splitting calculation identify a scale-sensitive diagnostic. | Viable as an approximation/diagnostic project; lower priority until a useful quantitative advantage is specified. |

A and B were described in the preceding discussion. D is the separate
source-manifold construction in Investigation 22. E develops its compact
Jensen construction. C is an additional natural construction prompted by
the question about a manifold for the *entire* heat family; it is not
being attributed to an already completed repository result.

Three potential homes would be:

1. **Global heat geometry and collision charges:** A–C, initially as
   related subproblems. Curvature, relative charge, and singular fibers
   inspect the same heat family, so they should share controls and
   boundary accounting.
2. **Theta-source geometry and transform constraints:** D. This needs a
   different source-side calculation and should have its own progress
   criteria.
3. **Jensen-surface degeneration and resolution:** E, provisionally a
   reserve direction. Its task would concern effective resolution,
   rather than further checks of the known RH-equivalent topology.

These are suggested groupings, not folder creation instructions or a
claim that all three have passed a benefit test.

## 2. A: the global physical jet manifold and curvature transport

### Construction and the useful invariant

For the complete theta flow, \(H\) is jointly entire in complex \(t,z\),
is even in \(z\), and satisfies \(H_t=-H_{zz}\). Put

\[
P(t,z)=\int_0^zH(t,\zeta)\,d\zeta,\qquad
X_t(z,w)=(P(t,z),H(t,z),w).
\tag{A1}
\]

The map is global. Its regular parameter domain is
\(\{E_t>0\}\times\mathbb C\), where
\(E_t=|H|^2+|H_z|^2\), with induced metric

\[
g_t=E_t|dz|^2+|dw|^2.
\tag{A2}
\]

Global injectivity and completeness do not follow. Because \(H_z(t,0)=0\),
\(P_t=-H_z\) and \(\partial_tX_t=-\partial_z^2X_t\).
This is a deformation of parametrized maps in a fixed spectral coordinate;
no intrinsic Ricci-flow identity has been established.

On the regular curve factor, write

\[
\mu_t=\frac{|HH_{zz}-H_z^2|^2}{E_t^2}\,dA,
\qquad K_t\,dA_{g_t}=-2\mu_t.
\tag{A3}
\]

For an \(m\)-fold zero at time zero, Note 24 proves the local weak limit
\(\mu_t\rightharpoonup\mu_{\rm reg}+\pi(m-1)\delta_a\).
The *defect* vanishes for \(m=1\), although smooth Gauss area need not.
The four-dimensional product construction carries this same defect
multiplied by the auxiliary area; it does not supply an independent sign.

### Stress test: a bounded boundary expression can still carry an atom

For \(H=z^2-2t\), Note 24 gives

\[
\lim_{t\to0,\ t\ne0}\mu_t(D_R)
 =\pi+\frac{\pi R^2}{R^2+4}.
\tag{A4}
\]

The fixed-circle flux is finite and smooth through the event. The first
term in A4 is lost if one cancels the common factor in the time-zero jet
before taking the limit. Thus rewriting the integral as a nonsingular
boundary expression does **not** by itself remove the concentration.

A new estimate would have to control something stronger, such as uniform
integrability of the relevant curvature densities, or a compensated
boundary budget smaller than the predicted defect. Generic heat germs
do not have this property. A bound assumed to hold near every proposed
multiple endpoint is an exclusion criterion, not an independently
available premise.

The induced metric also fails a basic hyperkähler test: its Ricci-flat
condition is \(HH_{zz}-H_z^2=0\), which on a connected regular domain
forces a nonzero slice to be exponential. The theta slice is even and
nonconstant. Adding \(z\) as another graph coordinate replaces \(E_t\)
by \(1+E_t\), giving a smooth graph through a physical jet zero; that
regularity leaves the original zero in place. These are the scoped
results of [Investigation 22, §5][g-manuscript].

**Next useful task.** Choose one finite domain and one source-dependent
curvature or boundary estimate. Retain its defect, lower and upper
boundaries, and any auxiliary-volume normalization. Compare the final
error with the existing direct complete-jet estimate using the same
input information. Re-deriving A3 or its product lift is not this task.

## 3. B: global relative charges and a boundary certificate

### What the charge measures

Complexify physical heat time and set \(G=(H,H_z):\mathbb C^2\to\mathbb C^2\).
On a bounded domain \(B\) with smooth boundary, assume \(G\ne0\) on the
boundary and finitely many isolated zeros inside. Give \(B\) complex
orientation. With

\[
\alpha=\frac{\operatorname{Im}
 (\overline H\,dH+\overline{H_z}\,dH_z)}{|H|^2+|H_z|^2},
\]

the global boundary account is

\[
Q_B=\frac1{4\pi^2}\int_{\partial B}\alpha\wedge d\alpha
 =\sum_{p\in B:\,G(p)=0}\dim_{\mathbb C}\mathcal O_p/(H,H_z).
\tag{B1}
\]

At a heat event of spatial order \(m\), the local summand is
\(\binom m2\), by [Investigation 22 Note 08][g08]. Note 25 identifies
it with a relative top Chern number and, for a small spherical link,
a Hopf invariant. A simple zero contributes zero.

The positive regularization is also available:

\[
\left(\frac{i}{2\pi}\partial\bar\partial
       \log(E+\epsilon^2)\right)^2
 =\frac{2\epsilon^2|H_zH_{zzz}-H_{zz}^{\,2}|^2}
        {\pi^2(E+\epsilon^2)^3}\,dV.
\tag{B2}
\]

Its mass converges to B1 under these boundary and isolation hypotheses.
It is a regularized intersection measure, not the ordinary second Chern
form of the trivial flat bundle. Higher jet common-factor defects
\((m-k)_+\) provide further multiplicity thresholds, but do not add
arithmetic information. The centered trace-free quadrupole fails on the
radially symmetric double-event profile, as already screened in Note 25.

### Two exact controls

For \(H=z^2-2t\),

\[
G=(z^2-2t,2z),\qquad \det_{\mathbb C}DG=-4,
\tag{B3}
\]

so a small ball has \(Q_B=1\), even though both the ambient space and the
jet bundle are trivial and the ambient metric can be flat hyperkähler.
Absolute \(c_2=0\) does not erase the relative boundary obstruction.

The cubic family supplies a separate global warning:

\[
H(t,z)=z^3+(a-6t)z+b,\qquad b\ne0.
\]

Its simultaneous equations reduce exactly to

\[
z^3=b/2,\qquad t=(a+3z^2)/6.
\tag{B4}
\]

There are three simple complex spacetime events, since the Jacobian at
each is \(-36z^2\ne0\). If \(a,b\) are real, exactly one has real \(z,t\);
the other two have nonreal time. A domain containing all three has
charge three, irrespective of their physical relevance. For example,

\[
H=z^3-(4+6t)z+2
\]

has its real collision at \(t=-1/6\) and three distinct real roots at
\(t=0\), remaining simple and real for \(t\ge0\). Its other two
complex-time events remain part of the global charge. Consequently a
global complex charge is not automatically a count of forbidden physical
events. These polynomial controls test the geometric inference; they
do not have the unchanged theta source.

### A concrete, stable boundary task

Let \(G_0\) be a reference boundary map with known degree. If

\[
\sup_{\partial B}\|G-G_0\|
 <\inf_{\partial B}\|G_0\|,
\tag{B5}
\]

the straight homotopy is nonzero on the entire boundary, so
\(\deg(G/\|G\|)=\deg(G_0/\|G_0\|)\). This follows immediately
from the triangle inequality along the homotopy. If the reference degree
is zero, positivity of local holomorphic intersection multiplicities
excludes every joint zero in \(B\).

B5 makes a finite experiment concrete: certify boundary degree with
complete theta errors, and compare the total acquisition cost and
coverage with direct interior jet exclusion. It could avoid evaluating
the entire interior. The three-dimensional boundary, complex-time
growth, and nonphysical events could also make it more expensive.
No efficiency or theta margin has been demonstrated here.

**Classification.** Vanishing of the charge around every physical
multiple-zero candidate restates simplicity. A paid certificate on a
specified bounded region is a finite quantitative milestone. A universal
charge bound requires a new theta estimate, even though the charge itself
is now exactly defined.

## 4. C: the direct spectral cover and its vanishing cycles

This is a literal global geometric object built from the whole function:

\[
\mathcal S=\{(t,z,w)\in\mathbb C^3:w^2=H(t,z)\},
\qquad \mathcal S_t=\{(z,w):w^2=H(t,z)\}.
\tag{C1}
\]

It is a complex analytic family, not necessarily a smooth manifold
everywhere. Its regular fibers are noncompact Riemann surfaces.
It also has a real structure when \(t\) is real. This construction does
not identify \(w\) with the elliptic-fiber coordinate of the source
manifold in Direction D.

### Simple and multiple zeros are geometrically different

If \(H(t_0,a)=0\) and \(H_z(t_0,a)\ne0\), the gradient of
\(w^2-H(t_0,z)\) is nonzero at \((a,0)\). This is a smooth branch
point of the projection to \(z\).

If instead \(H(t_0,z)=(z-a)^m g(z)\), \(g(a)\ne0\), choose a local
holomorphic square root of \(g\) and replace \(w\) by \(w/\sqrt{g(z)}\).
The fiber germ becomes

\[
w^2=(z-a)^m.
\tag{C2}
\]

It is singular precisely for \(m\ge2\). The dimension of its Jacobian
algebra is

\[
\dim_{\mathbb C}\mathbb C\{z-a,w\}/((z-a)^{m-1},w)=m-1.
\tag{C3}
\]

This is the usual Milnor number for this plane-curve germ. It differs
from the primitive-curve Milnor number \(m(m-1)\) in Note 25: the
embeddings are different. The double case is the ordinary nodal
degeneration of local Picard–Lefschetz theory; see [Seidel, §2][seidel]
for the Morse-fibration and vanishing-cycle framework. No global
finite-dimensional period system for C1 is being imported from that
local framework.

At a double event, \(H_{zz}\ne0\), so \(H_t=-H_{zz}\ne0\).
The total surface \(\mathcal S\) is then smooth, although its
projection to \(t\) has a nondegenerate critical point. At an event of
order \(m\ge3\), all three first derivatives of \(w^2-H\) vanish.
The total family itself is singular there. Thus a proposal requiring
a smooth Lefschetz fibration for every multiplicity would miss the
higher-order cases unless it included an appropriate resolution.

### Exact period stress test

Take the local double model \(H=z^2-2t\), \(t>0\), and set
\(a=\sqrt{2t}\). Let \(\delta_t\) traverse the cut \([-a,a]\)
on the sheet \(w=+i\sqrt{a^2-z^2}\), returning on the other sheet.
Then direct integration gives

\[
\oint_{\delta_t}\frac{dz}{w}=-2\pi i,
\qquad
\oint_{\delta_t}w\,dz=2\pi i\,t.
\tag{C4}
\]

Reversing orientation changes both signs. The substitution \(z=a\xi\)
already explains the scaling: \(dz/w\) has no power of \(a\), whereas
\(w\,dz\) has a factor \(a^2=2t\).

The cycle shrinks to the node while the first period remains finite
and nonzero. There is no contradiction. On the limiting branches
\(w=\pm z\), its differential becomes \(\pm dz/z\), with a pole
at the node. It was not a uniformly regular one-form across the
limiting total-space point. The ambient regular form \(w\,dz\)
has the vanishing period expected of a collapsing cycle.

This directly answers the analogous shrinking-cap concern in a manifold
setting. Periods can detect degeneration, but a proposed impossibility
argument must independently control the differential through that
degeneration. The derivative relation
\(\partial_t(w\,dz)=-dz/w\) is also consistent with C4.

### Global topology has an unbounded budget

Under RH, each \(t>0\) slice has infinitely many simple real zeros.
Choose a disk centered at zero containing exactly \(2N\) zeros, with
none on its boundary. Its inverse image in C1 is a connected double
cover with two boundary components. Riemann–Hurwitz gives

\[
\chi=2-2N,\qquad g=N-1.
\tag{C5}
\]

Indeed a branched double cover subtracts one from Euler characteristic
per simple branch point; the even number gives trivial boundary
monodromy and two boundary components. Exhausting the zeros therefore
exhibits arbitrarily large genus. The full spectral curve is not a
compact finite-genus surface with an automatically finite Euler budget.

**Next useful task.** Work on one finite spectral domain with a fixed
boundary and transported cycles. Derive a source-dependent estimate for
a specified period or its variation, including moving-branch and outer
boundary terms. Subtract the exact C4 contribution before interpreting
the first correction as an arithmetic obstruction. A finite
Picard–Fuchs system cannot be assumed for an arbitrary entire \(H\).
If the result only recovers C2–C4 for generic heat germs, retain it as
a diagnostic and stop that particular exclusion attempt.

## 5. D: the theta-source manifold and a transform-compatible constraint

### The existing arithmetic realization

Use distinct notation for the source geometry:

\[
\tau=p+iq\in\mathbb H,\qquad
\zeta=r+\tau s,\qquad (r,s)\in\mathbb T^2.
\]

[Investigation 22, §8][g-manuscript] supplies the global marked-family
metric and holomorphic symplectic form

\[
g_{\rm sf}=q|d\tau|^2+q^{-1}|dr+\tau ds|^2,
\qquad \Omega=d\tau\wedge d\zeta.
\tag{D1}
\]

The theta line bundle and its covariant vertical derivative
\(\mathcal D=\partial_\zeta+2\pi i s\) recover the complete source:

\[
\Phi(u)=\frac{y^{1/4}}{16\pi^2}
 \bigl(y^2\mathcal D^4\vartheta-3\pi^2\vartheta\bigr)(0,iy),
\qquad y=e^{4u}.
\tag{D2}
\]

The full function is then

\[
H(t,z)=\frac1{64\pi^2}\int_1^\infty
 e^{t(\log y)^2/16}y^{1/4}
 \bigl(y^2\mathcal D^4\vartheta-3\pi^2\vartheta\bigr)(0,iy)
 \cos\!\left(\frac z4\log y\right)\frac{dy}{y}.
\tag{D3}
\]

Both the covariant correction and all theta indices matter. Physical
heat time \(t\) is not the elliptic modulus \(\tau\).
The pairing in D3 is oscillatory; positive fiber degree or an ambient
curvature norm does not turn it into a positive Hermitian norm.

### Stress test 1: the curvature must reach the observable

The [adapted ASD connection][g-asd] has curvature

\[
F=2\pi i(q\,dp\wedge dq-dr\wedge ds).
\]

Along the physical path \(\gamma(u)=(ie^{4u},0)\), its pullback is
zero. The natural external product on two such paths also has zero
curvature. In the adapted arithmetic frame the pulled-back connection
itself vanishes. Ambient transverse commutators must be taken before
restriction; they can survive, and the existing notes give their exact
lower-jet terms. Pure tangential pullback creates no new curvature term.

This leaves a legitimate question about a *coupled or nonlocal*
source-dependent estimate. It also places that question after the
existing [S06 finite-jet reductions][s06] and [S07 trace comparisons][s07],
not before them. The stopped S06 comparison used the same independent
jet balls and lost to direct exclusion. The stopped S07 comparison used
one specified whole-profile norm and incurred excessive trace payments.
Those scopes do not exclude different coupled information or a different
canonical observation norm.

### Stress test 2: a simple scalar modular repair cannot work

For a holomorphic nonvanishing \(h(\tau)\), the marked-family ansatz

\[
g_h=q|h(\tau)|^2|d\tau|^2+q^{-1}|dr+\tau ds|^2,
\qquad \Omega_h=h(\tau)d\tau\wedge d\zeta
\tag{D4}
\]

is locally hyperkähler. Its Kähler form is
\(q|h|^2dp\wedge dq+dr\wedge ds\), which is closed, and its
Hermitian determinant is \(|h|^2\), with vanishing Ricci form.
The displayed holomorphic volume form has constant norm and is parallel.

Under \(\tau'=(a\tau+b)/(c\tau+d)\),
\(\zeta'=\zeta/(c\tau+d)\), invariance of this volume form requires

\[
h(\tau')=(c\tau+d)^3h(\tau).
\tag{D5}
\]

For the central element \(-I\in SL_2(\mathbb Z)\), \(\tau'=\tau\)
and \(\zeta'=-\zeta\), so D5 says \(h=-h\). Thus this particular
base-only scalar ansatz cannot supply a nonzero invariant holomorphic
two-form on the full quotient. A level cover, a character or bundle
twist, or different period data changes the problem and must be stated.
Metric invariance alone is weaker than invariance of the full
hyperkähler triple; D5 is specifically the latter test.

The original marked metric is also incomplete as \(q\downarrow0\),
since \(\int_0^{q_0}\sqrt q\,dq<\infty\).
[Gross–Wilson][gross-wilson] construct Ricci-flat K3 metrics using
specified elliptic fibrations and corrections around singular fibers.
Their existence theorem does not identify D3 with a K3 invariant.
These facts screen the proposed *automatic* completion/descent; they
are not an exclusion of all compact or twisted realizations.

### What would make this a research proposal with a measurable gain?

Specify a source-side section, cycle or current and an exact observation
map to one of the physical quantities in A–C. Then derive a joint
estimate using theta's actual coefficient or automorphy relations, with
its physical restriction, zero mode, lower endpoint and full tail paid.
Before a numerical acquisition, choose a finite comparison domain and
the same-information direct reference. The gain must be an explicit
improvement in error, exclusion margin, coverage, or acquisition cost.

At present this is a **bridge-search proposal**, not a proved inequality
or a fully specified quantitative pilot. It is worth preserving because
it contains the actual arithmetic structure absent from the polynomial
controls. The initial screens remove two tempting shortcuts and leave
the harder coupled estimate as the genuine task.

## 6. E: compact Jensen surfaces and multiplicity-sensitive resolution

### Why finite topology alone fails the simplicity test

Use [Investigation 22 Note 05][g-jensen]'s entire function

\[
f(s)=\xi(1/2+\sqrt s)=\sum_{k\ge0}c_ks^k,
\qquad c_k=\gamma_k/k!>0,
\]

where the square-root expression denotes the single-valued even power
series. The physical normalization is \(H(0,z)=f(-z^2/4)/8\);
at nonzero zeros this substitution preserves multiplicity. Define

\[
J_d(X)=\sum_{k=0}^d\binom dk\gamma_kX^k,
\qquad F_d(s)=J_d(s/d).
\tag{E1}
\]

Under RH, every \(J_d\) has distinct negative real roots, even if \(f\)
has multiple zeros. The existing proof uses infinitely many positive
first-order factors and explicitly permits repetition. Thus every
associated odd-degree compact surface can have the expected genus and
maximal real-component count while a multiple zero remains possible in
the limiting \(f\).

An explicit control for these Jensen premises is

\[
f_*(s)=(1+s)\frac{\sinh(\pi\sqrt s)}{\pi\sqrt s}
 =(1+s)\prod_{n\ge1}(1+s/n^2).
\tag{E2}
\]

It is entire of order \(1/2\), has positive Taylor coefficients and
infinitely many negative real zeros, and has a double zero at \(-1\).
The same strict Jensen argument applies to every finite degree. E2 is
not asserted to be a positive-source theta heat control; it fails the
unchanged theta moment sequence. It tests precisely the inference from
these Jensen and growth premises to simplicity.

### An explicit full-series approximation bound

There is a useful calculation beyond this topological screen. For
\(d\ge1\), set

\[
b_{d,k}=\begin{cases}
\displaystyle\prod_{j=0}^{k-1}(1-j/d),&k\le d,\\
0,&k>d,
\end{cases}
\qquad q_{d,k}=\frac{k(k-1)}{2d}.
\]

For \(k\le d\), the elementary product bounds give

\[
0\le1-b_{d,k}\le q_{d,k},\qquad
0\le b_{d,k}-1+q_{d,k}\le\frac{q_{d,k}^2}{2}.
\tag{E3}
\]

For clarity, the second upper bound follows by retaining the first two
terms in the inclusion–exclusion upper bound for the product: its
second elementary symmetric sum is at most half the square of the
first. For \(k>d\), \(q_{d,k}\ge1\), and E3 follows from
\(q-1\le q^2/2\). Thus E3 also pays the entire omitted coefficient
tail, rather than only expanding a fixed finite polynomial.

Since \(F_d=\sum_{k\ge0}c_kb_{d,k}s^k\), positivity of the complete
coefficients gives, on \(|s|\le R\),

\[
|F_d(s)-f(s)|\le\frac{R^2f''(R)}{2d},
\tag{E4}
\]

and the sharper expansion with explicit remainder

\[
F_d(s)=f(s)-\frac{s^2}{2d}f''(s)+\mathcal R_d(s),
\qquad |\mathcal R_d(s)|\le\frac{C_R}{d^2},
\tag{E5}
\]

\[
C_R=\frac{R^4f^{(4)}(R)+4R^3f^{(3)}(R)+2R^2f''(R)}8.
\tag{E6}
\]

Indeed \(k^2(k-1)^2=(k)_4+4(k)_3+2(k)_2\), so E6 is exactly the
sum of the coefficient bound in E3. These constants use full positive
moments and are finite. They may be expensive at large \(R\); no useful
height-dependent cost bound is being claimed.

### What a double or triple zero does to the finite surfaces

Suppose \(a\ne0\) and \(f(s)=(s-a)^m g(s)\), \(g(a)\ne0\).
For \(m=2\) or \(m=3\), substitute
\(s=a+a u/\sqrt d\) into E5. Uniformly on each bounded complex
\(u\)-set, direct Taylor expansion gives

\[
\frac{d^{m/2}F_d(a+a u/\sqrt d)}{g(a)a^m}
 =\begin{cases}
u^2-1+O(d^{-1/2}),&m=2,\\
u^3-3u+O(d^{-1/2}),&m=3.
\end{cases}
\tag{E7}
\]

The limiting polynomials have simple roots. Local zero stability then
gives the corresponding root locations with \(O(d^{-1})\) error in
the original \(s\) coordinate. In particular a double zero has two
nearby approximant roots separated by

\[
\frac{2|a|}{\sqrt d}+O(d^{-1}).
\tag{E8}
\]

For a triple, the leading normalized roots are \(-\sqrt3,0,\sqrt3\).
At a simple zero, E5 instead gives one nearby root at

\[
a+\frac{a^2f''(a)}{2d f'(a)}+O(d^{-2}).
\tag{E9}
\]

For the particularly simple control \(f(s)=(1+s)^2\), the calculation
is exact:

\[
F_d(s)=1+2s+(1-1/d)s^2,\qquad
s_\pm=-\frac1{1\pm d^{-1/2}},\qquad
|s_+-s_-|=\frac{2\sqrt d}{d-1}\quad(d>1).
\tag{E10}
\]

Higher multiplicities require additional terms beyond E5; no
all-multiplicity remainder claim follows from the first-order expansion.
The Hermite shapes in E7 are local smoothing profiles. This degree
limit for the *unshifted* \(J_d(s/d)\) is different from the fixed-degree,
large coefficient-shift regime in [Griffin–Ono–Rolen–Zagier][gorz].
The classical Jensen framework and coefficient asymptotics are also
discussed by [O'Sullivan][osullivan]. No novelty claim is made for
these approximation mechanisms.

**Assessment.** The finite surfaces retain multiplicity information
through a quantified degenerating scale, even though their topology is
unchanged. That passes the diagnostic test. Generic multiple-zero
functions have exactly this behavior, so observing it or ruling it out
at a few known zeros supplies no evidence for the global simplicity
criterion. A useful next milestone is an effective resolution bound at
a specified height, with complete moment/degree/error costs compared
against direct \(H,H_z\) evaluation. An independent arithmetic gap or
period bound would still be needed for an exclusion argument.

## 7. Control screen and limits of the conclusions

The controls must be matched to the premises actually used. In
particular, finite-source controls do not have an all-real heat slice,
so they cannot be inserted into the all-real root-motion argument.

| Control or test class | What it tests here | Premise it does not supply |
| --- | --- | --- |
| Quadratic and cubic polynomial heat families | A–C: rank loss, curvature concentration, nonzero relative charges, nonphysical complex events, collapsing periods | The unchanged theta source, its full growth and arithmetic data |
| Atomic and finite-profile threshold families | Generic positive-source and finite-observation claims near multiple endpoints | Complete theta coefficients/profile growth and eventual simplicity at the threshold |
| RH-conditional close-source endpoint controls in [BW10 Note 05][n05] | A–C even with positive sources close to theta, preserved leading tail/completion normalization, and simple all-real zeros for positive time | Ordinary Dirichlet-series arithmetic; their added double endpoints escape to high ordinate |
| Euler-factor controls | Exclusions based only on broad completion or symmetry properties | The original Euler factor/coefficient data; use the particular control's parameter regime |
| Weighted-square and finite-prime controls | Claims using square support, finitely many endpoint conditions or finitely many prime identities | Full normalized reflection and unchanged coefficients; also no all-real heat slice for the finite-source cases |
| Reflected super-Gaussian and positive-primitive controls | Reflection, source positivity, or positive auxiliary channels by themselves | The canonical normalized integer-square expansion; use each family's actual preservation list |
| E2 and E10 | Jensen hyperbolicity/topology and finite-degree resolution claims | The unchanged theta moments; no positive theta-source realization is asserted |

The cited [control summary][controls] routes to the constructions and
their exact hypotheses. This note does not merge distinct controls'
property lists into one hypothetical example.

Direction D retains arithmetic data missing from these controls, but
retaining it in a representation is not yet exploiting it in a bound.
Any proposed estimate must state which missing premise it uses and why
its numerical margin or analytic bound depends on that premise.

## 8. What this first round accomplished, and what should happen next

The new work in this brainstorm is the explicit cubic event screen B4,
the direct spectral-cover tests C2–C5, the scalar modular-descent test
D4–D5, and the paid Jensen approximation and local resolution formulas
E3–E10. The underlying heat-jet charges and source geometry are inherited
from the linked notes. These are analytic stress tests and proposal
clarifications, not evidence that the global simplicity target is true.

E3 was additionally checked with exact rational arithmetic for
\(1\le d\le40\), \(0\le k\le3d+10\), including the omitted-tail case.
E10's discriminant and squared root gap were checked for \(2\le d\le40\).
The written
inequalities and exact formulas carry the argument; the finite check is
only a transcription check. No new numerical theta claim is made.

Before separate folders are opened, the most useful choices are:

1. **For A–C, select the observable.** Boundary charge certification is
   already precisely defined. A spectral period is a different candidate
   with a concrete universal contribution to subtract. Pick one bounded
   comparison rather than developing several equivalent dictionaries.
2. **For D, specify the new bridge.** A coupled source identity or estimate
   must survive the physical transform and lie outside the already
   screened finite-jet/independent-ball/selected-profile classes. A
   compactification without such an observation map is a separate
   geometric problem with no established HMC payoff.
3. **For E, decide whether resolution is the objective.** The formulas
   support a finite approximation study. Another proof or verification
   of maximal real-component topology would not address simplicity.

The strongest practical reason to retain these directions is now
specific: we have multiplicity-selective geometric observations, explicit
controls, and identified places where a source-dependent inequality
would enter. The initial tests do not provide that inequality.
**HMC-05 remains open and HMC-06 remains gated.** A different global
route could discharge the exclusion requirement without finding a later
collision, but it would need its own complete arithmetic estimate and
height/multiplicity coverage.

[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[local-summary]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[geom-summary]: ../../../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[avoid]: ../../../../../../../avoid/README.md
[avoid01]: ../../../../../../../avoid/01_restating_the_target.md
[avoid03]: ../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[avoid07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[progress]: ../research-progress/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRESS_20261021.md
[n05]: ../notes/05_CLOSE_POSITIVE_SOURCES_AND_NORMALIZED_DOUBLE_ZEROS_20261020.md
[n24]: ../notes/24_GAUSS_AREA_CONCENTRATION_AND_CURVATURE_FLUX_20261021.md
[n25]: ../notes/25_MULTIPLICITY_SELECTIVE_CHERN_AND_HOPF_OBSERVATIONS_20261021.md
[g-manuscript]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex
[g08]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/08_REAL_AND_COMPLEX_COLLISION_MULTIPLICITIES_20261015.md
[g-jensen]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/05_JENSEN_HYPERELLIPTIC_TOPOLOGY_20261015.md
[g-asd]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/02_ASD_METRIC_FREEDOM_AND_PHYSICAL_RESTRICTION_20261015.md
[s06]: ../../../../../11_arithmetic_collision_rigidity/symmetries/06_hodge_and_transverse_geometry/notes/05_BOUNDED_COMPLETED_CURRENT_AND_DIRECT_COMPARISON_20261019.md
[s07]: ../../../../../11_arithmetic_collision_rigidity/symmetries/07_geometric_duality_and_quaternionic_symmetry/notes/04_PAID_PROFILE_TRACE_AND_DIRECT_TAIL_COMPARISON_20261019.md
[seidel]: https://arxiv.org/pdf/math/0007115
[gross-wilson]: https://arxiv.org/pdf/math/0008018
[gorz]: https://arxiv.org/html/1902.07321
[osullivan]: https://arxiv.org/html/2007.13582
