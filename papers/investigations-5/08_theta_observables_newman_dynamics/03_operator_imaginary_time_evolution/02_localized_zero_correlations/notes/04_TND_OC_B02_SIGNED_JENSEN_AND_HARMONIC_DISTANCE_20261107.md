# B02: signed Jensen gaps and a sharp harmonic-distance obstruction

7 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance. Exact backend model and reasoning
effort are unavailable in exposed session metadata; neither is inferred
from the recommended Astra configuration. One authoring agent, no delegation.

**Status: proved in-note; proof-author self-check only.** The decision is a
scoped failure of the two comparisons below, not a failure of localized
statistics or the complete theta source. No canonical signed smallness,
zero exclusion, numerical certificate, or literature novelty is claimed.
[Decision03](../brainstorm/notes/03_TND_OC_B02_SIGNED_COMPARISON_DECISION_20261107.md)
owns the bounded selection; the [sole register](../research-progress/01_TND_OC_RESEARCH_PROGRESS_20261107.md)
owns current status. [Self-check03](../reviews/03_TND_OC_B02_AUTHOR_SELF_CHECK_20261107.md)
is not an independent assessment.

The quantitative result is the sharp local inequality

\[
 \inf_{v\ {\rm harmonic}}\int_{D(a,\ell)}|\log|F|-v|\,dA
 \ \ge\ \frac{\pi\log2}{2}\,m\ell^2
 \tag{1}
\]

when F is holomorphic and has a zero of multiplicity m at a. In the
accepted E02 disk, a real zero at the window center consequently forces
the **full-disk absolute-log error allowance** of any harmonic baseline
to be at least \(m\log2/36\) for Q. The true transverse mass need not be
positive. The result exposes the cost of paying for real zeros that the
actual observable deliberately ignores.

## 1. Fixed source, tests and classification

Retain [Note02](02_TND_OC_LOCAL_LOG_TRANSFER_20261107.md) and its accepted
[E02 consumer](03_TND_OC_E02_VERIFIED_CONSUMER_20261107.md):

\[
 \lambda=0,\quad X\ge10,\quad0<h\le1,\quad
 s=\tfrac12-iz/2,\quad F(z)=\frac{s-1}{s}\zeta(s)=D(z)H_0(z),
 \quad c=X+4i,\quad r=25/6,\quad R=9/2.
 \tag{2}
\]

H is the complete canonical theta cosine integral, and D is exactly
Note02(11), nonvanishing on the enlarged disk. For either of the fixed
nonnegative compact C^(1,1) tests

\[
 a=w((x-X)/h)y_+^2\kappa(y),\qquad
 \varphi_Q=2a,\qquad\varphi_\eta=2\log(1+\eta a),\quad\eta>0,
 \tag{3}
\]

write

\[
 S_\varphi(F)=\frac1{2\pi}\int_{D(c,r)}\Delta\varphi\log|F|\,dA
 =\sum_{F(z)=0}m_z\varphi(z),\qquad
 K_\varphi=\frac{\|\Delta\varphi\|_\infty}{2\pi}.
 \tag{4}
\]

Thus S is Q or log Z, with every multiplicity retained. A plateau pair
\(x_0\pm id\) contributes \(2d^2\) or
\(2\log(1+\eta d^2)\). Real zeros contribute zero, including multiple
ones. The weak-Laplacian formula and support buffer are the accepted
E02 inputs, not a new import. The classical smoothed Jensen passage was
reopened; see [source-use03](../references/03_TND_OC_B02_SOURCE_USE_20261107.md).

Classification under [avoid01](../../../../../../avoid/01_restating_the_target.md):
the signed-gap identity below is a **representation**, not a new criterion
or arithmetic gain. The harmonic-distance bound is a **scoped quantitative
obstruction**, judged by \(\pi\log2/2\) and its ensuing certificate floor.
All-window exact vanishing remains the reformulation already classified
in Note01; no finite checks are offered as evidence for it.

Exactly two proposals are considered: A, separate quadratic/Jensen estimates
on the two signs of the test Laplacian; B, a finite Euler or other harmonic
log baseline with the E02 full-disk absolute-error payment. The one focused
clarification is whether real zeros obstruct B although the tests ignore
them. The auxiliary radial function in section 3 is a norm-duality witness,
not a replacement event observable or third proposal.

## 2. Proposal A: what a two-sided quadratic comparison leaves unpaid

Since the test is compact, \(\int\Delta\varphi=0\). It is nonzero and
nonnegative, so its Laplacian has positive and negative parts of equal,
strictly positive mass. Set

\[
 b_\varphi=\int(\Delta\varphi)_+\,dA
           =\int(\Delta\varphi)_-\,dA>0,\qquad
 d\mu_\pm=\frac{(\Delta\varphi)_\pm}{b_\varphi}\,dA.
 \tag{5}
\]

For any nonzero holomorphic f on the disk define

\[
 A_\pm=\int|f|^2d\mu_\pm>0,\qquad
 J_\pm=\log A_\pm-\int\log|f|^2d\mu_\pm\ge0.
 \tag{6}
\]

All integrals are finite: the densities are bounded and compactly
supported, holomorphic zeros have locally integrable logarithms, and
their area measure is zero. Concavity of log gives the last inequality,
by positive regularization and a limit if necessary. Direct subtraction
gives the exact identity

\[
 \boxed{S_\varphi(f)=\frac{b_\varphi}{4\pi}
       \left[\log\frac{A_+}{A_-}+J_--J_+\right].}
 \tag{7}
\]

The sign of the difference of Jensen gaps cannot be inferred from their
individual nonnegativity. Moreover integration by parts gives

\[
 A_+-A_-=
 \frac1{b_\varphi}\int\Delta\varphi\,|f|^2dA
 =\frac4{b_\varphi}\int\varphi|f'|^2dA\ge0.
 \tag{8}
\]

It is strictly positive for a nonconstant f: the test is positive on an
open set, and f' cannot vanish throughout that set. Scalar normalization
does not change (7)'s ratio or gaps. For \(f=F/M_X\), this strict case
applies. The canonical F is nonconstant: on the real s-axis its value tends to
one as s tends to positive infinity, whereas its value at s=2 is
zeta(2)/2<1. Analytic continuation then excludes local constancy.

Consequently the quadratic part of (7) has the positive sign. Even a
zero-free nonconstant field has \(S_\varphi(f)=0\), so its exact gaps
satisfy

\[
 J_--J_+=-\log(A_+/A_-)<0.
 \tag{9}
\]

For example \(f=e^{tz}\), real \(t\ne0\), has this property for every
nonzero test (3). This is an information control, not a theta source.
It shows that cancellation of quadratic variation is already needed
in a field without any zeros.

For completeness, a generic claim that discards the gap difference as
nonpositive is false. On the unit disk take the auxiliary test
\(\psi=(1-|z|^2)_+^2\) and the real polynomial \(f=z^2+1/4\).
Here \(b_\psi=2\pi\), and direct radial integration gives

\[
 A_+=\frac{17}{24}+\frac1{16}=\frac{37}{48},\quad
 A_-=\frac1{24}+\frac1{16}=\frac5{48},\quad
 S_\psi(f)=2(1-1/4)^2=\frac98>rac12\log\frac{37}{5}.
 \tag{10}
\]

The strict inequality follows, for example, from the positive cubic
Taylor lower bound for \(e^{9/4}>37/5\). Thus the gap difference can
also be positive. This example is a check on the **generic signed-Jensen
argument**, not a counterexample to an unproved statement restricted to
the canonical F and tests (3).

### Canonical information and complete acquisition costs

The quantities A are genuine complete-source quadratic integrals. Taking
\(f=F/M_X\), substitute \(F=D\int_0^\infty\Phi(u)\cos(zu)du\) in
(6). Fubini is justified by the complete super-exponential source tails
on the compact disk. This produces a double source integral with kernels

\[
 \mathcal K_\pm(u,v)=\int |D(z)|^2
          \cos(zu)\overline{\cos(zv)}\,d\mu_\pm(z),
 \quad
 A_\pm=M_X^{-2}\iint\Phi(u)\Phi(v)\mathcal K_\pm(u,v)\,du\,dv.
 \tag{11}
\]

The literal theta coefficients enter (11). Positivity of these two
quadratic kernels is not a comparison of their logarithmic gaps.

For the exact finite source in Note02(27), let
\(\epsilon=\delta/M_X\), with the **complete** arithmetic/radial error
and enlarged-disk multiplier of Note02(29)--(34). Both normalized fields
have modulus at most one, hence

\[
 |A_\pm-\widehat A_\pm|\le2\epsilon.
 \tag{12}
\]

If \(\widehat A_\pm>2\epsilon\), an explicit logarithm error is
\(2\epsilon/(\widehat A_\pm-2\epsilon)\). Without that positive
denominator, no such logarithm estimate is licensed. Also, by E02,

\[
 \left|\int\log|f|^2d\mu_\pm-
             \int\log|\widehat f|^2d\mu_\pm\right|
 \le \frac{2\|\Delta\varphi\|_\infty}{b_\varphi}
          C_X\epsilon^{\alpha_X},\qquad
 \alpha_X=\frac2{n_X+2}.
 \tag{13}
\]

These are acquisition errors, not favorable values. Exact finite-source
integrals still require integration/rounding payment if evaluated. For S
itself the existing direct E02 bound \(K_\varphi C_X\epsilon^{\alpha_X}\)
is available without splitting (7) into separately estimated terms.

**Disposition A.** If one bounds \(J_-\le B_-\) separately and merely
drops \(-J_+\), the resulting allowance is

\[
 U_A=\frac{b_\varphi}{4\pi}
       [\log(A_+/A_-)+B_-]
 \ge\frac{b_\varphi}{4\pi}\log(A_+/A_-)>0.
 \tag{14}
\]

For each fixed nonconstant canonical F, window and response, this
recipe therefore cannot resolve **all** d tending to zero. There is no
uniform positive lower bound in X asserted here, and (14) does not rule
out individual positive defect budgets or new coupled estimates.
The first unpaid arithmetic input is a favorable bound on the *difference*
\(J_--J_+\), or equivalent correlated small-value information, beyond
separate moment positivity. Equation (7) does not supply it. No ready
execution task is issued to “make this difference small”.

## 3. Proposal B: harmonic baselines and the sharp local distance

For any real harmonic v on a neighborhood of the test support,

\[
 \int v\Delta\varphi\,dA=0,\qquad
 S_\varphi(F)=\frac1{2\pi}\int(\log|F|-v)\Delta\varphi\,dA.
 \tag{15}
\]

This includes \(v=\log|G|\) for holomorphic, nonvanishing G. For any
finite prime set P, the canonical-looking reference

\[
 G_P(z)=\frac{s(z)-1}{s(z)}
             \prod_{p\in P}(1-p^{-s(z)})^{-1}
 \tag{16}
\]

is nonvanishing and holomorphic on a neighborhood of \(\overline D(c,R)\).
Indeed Re(s)>=1/4, so |p^(-s)|<1; s=0 and s=1 are outside this disk
because X>=10. Finite prime-power logarithmic sums are harmonic there
as well. The infinite Euler product is only imported in its Re(s)>1
domain; no convergence to the canonical log on this disk is assumed.
Termwise integration of a finite harmonic prime sum against the test
Laplacian yields exactly zero. Any zero-sensitive contribution must reside
in the unestimated remainder.

### Sharp local lemma

Let F be holomorphic and not identically zero on an open neighborhood
of \(\overline D(a,\ell)\), with a zero of multiplicity m>=1 at a.
Let v be real harmonic there. Then (1) holds. No zero separation is
assumed: other zeros only strengthen the following lower bound.

For \(0<\rho<\ell\), write t=|z-a| and define

\[
 \Psi_\rho(t)=
 \begin{cases}
 (\rho^2\log2-t^2)/4,&0\le t\le\rho/\sqrt2,\\
 (t^2-\rho^2)/4-(\rho^2/2)\log(t/\rho),
                       &\rho/\sqrt2\le t\le\rho,\\
 0,&t\ge\rho.
 \end{cases}
 \tag{17}
\]

It is nonnegative and compact C^(1,1). At both joins its value and
first normal derivative match; at the outer circle both are zero.
Its weak Laplacian has no circle atom and equals -1 in the inner
half-area disk and +1 in the outer half-area annulus, with zero outside.
In particular

\[
 \|\Delta\Psi_\rho\|_\infty=1,\qquad
 \Psi_\rho(a)=\rho^2\log2/4.
 \tag{18}
\]

Using the weak test formula already justified in E02, harmonic
annihilation and nonnegativity of the zero measure gives

\[
 \int_{D(a,\ell)}|\log|F|-v|\,dA
 \ge\int(\log|F|-v)\Delta\Psi_\rho\,dA
 =2\pi\sum_zm_z\Psi_\rho(z)
 \ge\frac{\pi\log2}{2}m\rho^2.
 \tag{19}
\]

Let rho increase to ell. The same conclusion holds if F and v are
only defined on the open disk, using these compact inner tests and
interpreting an infinite L1 integral as an automatic bound.

The constant is sharp for the asserted local class. For
\(F(z)=(z-a)^m\), choose the constant harmonic function
\(v=m\log(\ell/\sqrt2)\). Then

\[
 \int_{D(a,\ell)}|\log|F|-v|\,dA
 =\frac{\pi m\ell^2}{2}\int_0^1|\log(2q)|\,dq
 =\frac{\pi\log2}{2}m\ell^2.
 \tag{20}
\]

This proves sharpness without claiming that the canonical F attains
equality, or that the later E02 allowance constant is sharp.

### Exact consequence for the accepted disk and defect budgets

Suppose **F has a real zero at X**, of multiplicity m. This is a local
hypothesis; no claim is made that every center has a real zero. The
distance from a=X to the boundary of \(D(X+4i,25/6)\) is 1/6. Applying
(19) on every smaller ball centered at X gives, for every harmonic v
on this disk,

\[
 B_X(v):=\int_{D(c,r)}|\log|F|-v|\,dA
 \ge\frac{\pi m\log2}{72}.
 \tag{21}
\]

A certificate that replaces the exact signed integral (15) by
\(S_\varphi\le K_\varphi B\), where \(B\ge B_X(v)\), must therefore
pay at least \(K_\varphi\pi m\log2/72\). On the plateau and just
above y=0, \(\Delta\varphi_Q=4\), while
\(\Delta\varphi_\eta\to4\eta\). Consequently

\[
 \boxed{K_QB\ge\frac{m\log2}{36},\qquad
 K_\eta B\ge\frac{\eta m\log2}{36}.}
 \tag{22}
\]

In particular the same floor applies to E02's declared allowance
\(E_\varphi=K_\varphi C_X(\delta/M_X)^{\alpha_X}\) **if its field
approximant G is nonvanishing on the whole enlarged disk and satisfies
the actual E02 error/anchor hypotheses**. In that case its logarithm
is harmonic and (18) of Note02 supplies the required upper B. The
comparison statistic of G is zero. Equivalently such a field error must
satisfy

\[
 \delta\ge M_X\left(\frac{\pi m\log2}{72C_X}\right)^{(n_X+2)/2}
 \tag{23}
\]

whenever it lies in the allowed E02 range. If no error in that range is
possible, this particular certificate is unavailable rather than exempt
from the floor.

Since \(2\log(1+\eta d^2)\le2\eta d^2\), neither strict defect
consumer can pass through this harmonic-baseline/full-disk-absolute
recipe whenever

\[
 \boxed{d^2\le\frac{m\log2}{72}.}
 \tag{24}
\]

Increasing the finite prime set, changing the harmonic baseline, or
improving its actual full-disk L1 bound cannot remove (21). The obstruction
already comes from a **real** zero, whose contributions to Q and log Z
are exactly zero. These are lower bounds on an *allowance*, never on the
true transverse mass or the finite theta-source statistic.

**Disposition B.** Stop zero-free harmonic log approximation followed by
this complete-disk absolute payment as an arbitrary-small-defect strategy
at real-zero-centered windows. The result does not exclude direct signed
remainder estimates, weighted errors that exploit real-axis vanishing,
baselines containing independently controlled real zeros, all-real
approximants with zeros, windows satisfying different hypotheses, or
the original finite theta approximant. That approximant may have zeros
and is not in the zero-free class (16).

## 4. Controls, averaging and remaining errors

The analytical screen uses [cluster12](../../../../../../result-summaries/12_collision_controls_and_screening.md)
and [cluster04](../../../../../../result-summaries/04_positive_constructions_and_scoped_obstructions.md),
with [Note01 section 5](01_TND_OC_REFLECTION_AND_CONFIGURATION_REDUCTION_20261107.md)
as the branch's control ledger. No previously certified collision was
rerun and no new physical source control is claimed.

| Control family | Applicable comparison and exact missing premise |
| --- | --- |
| Euler-factor controls, every admissible prime/coefficient | Generic (7), (8), (15), (19) hold on holomorphic windows. Literal theta coefficients/conductor are absent. No favorable gap difference is supplied; an actual nonreal pair retains its positive response. A zero-free *reference* must not be identified with this zero-bearing target. |
| Weighted squares and finite coefficient/tail changes | Conjugation and finite algebra survive. Complete canonical reflection and unchanged source coefficients are absent. Separate quadratic positivity does not pay the missing gap difference. |
| Reflected super-Gaussian and smooth/positive-primitive controls | Their shape, reflection or positive primitive does not identify F in (2). Harmonic annihilation and the local obstruction remain generic whenever their analytic hypotheses hold. |
| Finite-prime orbit controls | Selected prime identities do not supply full unchanged canonical arithmetic and reflection. A finite harmonic prime sum still annihilates the test; its missing remainder is not known small. |
| Atomic fixed-event and finite-profile controls, including continuous extensions | Finite profile data and positivity do not supply the full theta profile or eventual-simple-tail input. Any real multiple zero is invisible to (3) but still pays (19); this is consistent with the control. |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet-series arithmetic is absent. Added real double zeros give zero true response while obstructing the stated harmonic/absolute certificate. No simplicity conclusion is drawn. |
| Counter-kernels q and q_(T,a), smooth-density/two-channel constructions | Use the identities only where holomorphy and local finiteness hold. Their retained heat/realization properties do not supply the canonical field or the favorable Jensen-gap estimate. |
| Variable observation-kernel controls | Fixed amplitude alone lacks the full cosine readout/Newman equation. Formula (11) explicitly uses that readout. No claim transfers a theta estimate to the modified kernels. |

The generic identities do not reject controls and are not presented as
exclusion premises. The claimed obstruction rejects a **certificate
recipe** on its stated windows, equally for canonical and control fields.
Naming the controls' absent exact theta identity does not prove theta's
required sign. A positive-time collision is not silently reassigned to
lambda=0; generic local identities can be screened at that time without
importing the time-zero Euler normalization.

Every displayed canonical statement is local at the stated X. If centers
are averaged over an interval of length T, a complete simple-pair profile
contributes exactly

\[
 \frac{2d^2h}{T}\int w,\qquad
 \frac{2h}{T}\int\log(1+\eta d^2w(v))\,dv,
 \tag{25}
\]

as in Note01. No average is used to infer a bound at each center.
There is no new global zero truncation, or omission of approximate zeros
in 1<y<2. E02's decreasing exponent, enlarged-disk multiplier,
arithmetic/radial tails, h/eta derivative costs, and future
integration/rounding errors all remain. Nothing extends the HDA
negative-time theorem through zero or assigns a determinantal law to
canonical zeros.

## 5. Return and next boundary

B02 completes at its permitted **scoped-failure** outcome. The sharp
local norm obstruction and its explicit error floors are usable new
claims awaiting separate assessment. The signed-Jensen identity records
precisely why the proposed quadratic shortcut does not provide the
missing sign; it is not counted as an exclusion gain. No signed bound
below the one-pair threshold has been acquired.

**Next: [E] TND-OC-E03 — Sol.** Assess this written proof, weak-test
regularity, constants, hypothesis scopes and the resulting disposition
using the frozen [E03 request](../research-progress/handoffs/07_TND_OC_E03_ASSESSMENT_REQUEST_20261107.md).
This is a fixed proof audit, not a task to solve an unbounded signed estimate.
A later B03 decision may compare real-zero-aware transfer or coupled
logarithmic information, but remains conditional on this assessment and
has no selected proof route or numerical campaign.

Read the [result index](../../../../../../result-summaries/README.md),
[avoid index](../../../../../../avoid/README.md), especially
[scoped exclusions](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[separate bounds](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [shared-premise review](../../../../../../avoid/05_same_model_reviews_and_shared_premises.md).
Parent and Green results are unchanged: their residual lower bounds use
different objects and do not prove or disprove the local claims here.
