# RGD-B02 r1: a complete-source contour margin with explicit order dependence

4 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance; actual **gpt-6-astra (Codex), effort ultra**,
chat0004, thread 01a1a7c1-13a2-7371-8010-b0ace507476e,
turn 01a1a7c1-f46e-7771-80f4-f28b810aa0bc.

**Disposition: one bounded repair decision complete.** The author allowed
work beyond B03. After [Note07][b03]'s two fixed-reference obstructions,
B02 was classified in the [sole register][progress] before this repair.
The result is a **proved conditional determinant lemma**, with
proof-author and read-only same-model checks. Its scalar canonical
hypotheses remain unacquired. No new theta positivity range, all-index
induction, numerical experiment or certificate is claimed.

**Baseline qualification:** the parent catalog already records a stronger
reported cubic tail theorem; Section 7 explains why this simpler eighth-power
route is retained for method comparison and is not the default execution.

The selected mechanism uses the complete generating function. Its
positive reference margin is a Gaussian Vandermonde integral, proved
explicitly below. A single estimate pays all exterior and mixed regions.
The sufficient variance threshold grows as \(n^8\). If the stated scalar
theta estimates are proved, it gives an explicit domain
\(k\ge K(n)\) with \(K(n)=O(n^8)\). It leaves fixed small indices and
the growing complementary region unresolved.

Read the [result index][results], [theta cluster][theta], [controls][controls]
and [avoid index][avoid], especially [reformulations][a01],
[joint signed estimates][a12], [known-baseline tests][a11] and
[scoped claims][a07]. The assessment and optional fixed analytical route are in
[Packet12][packet]; [Packet11][continuation] gives model-change guidance.

## 1. Complete source and a separately justified reference

Write
\[
C(z)=\sum_{j\ge0}c_jz^j
=\int_0^\infty\Phi(u)\cosh(u\sqrt z)\,du
=\frac18\xi\!\left(\frac{1+\sqrt z}{2}\right).
\tag{1}
\]
The even transform defines an entire function; the functional equation
removes the apparent square-root ambiguity. The normalization follows
from the inherited coefficient identity \(b_j=8\,4^jc_j\).
In particular \(C(1)=1/16=b\). Equivalently the complete primitive gives
\[
C(z)=b+\frac{z-1}{8}\int_0^\infty p(u)\cosh(u\sqrt z)\,du.
\]
No mode, spatial exterior or inner-boundary contribution is removed.

For \(x>0\) define
\[
\mu(x)=xC'(x)/C(x),\qquad
v(x)=\frac{d\mu}{d\log x}.
\]
The positive probabilities \(c_jx^j/C(x)\) have mean \(\mu\) and variance
\(v>0\). Thus \(\mu\) is strictly increasing, tends to zero at zero and
to infinity at infinity. The last assertion follows because the positive
nonpolynomial series eventually places vanishing mass below any fixed
degree. Every integer \(k\ge1\) therefore has a unique saddle \(x=x(k)\)
with \(\mu(x)=k\).

Put
\[
\phi(\theta)=e^{-ik\theta}C(xe^{i\theta})/C(x),\qquad -\pi\le\theta\le\pi.
\]
Coefficient extraction and determinant multilinearity give
\[
D_{n,k}=
\frac{C(x)^n x^{-nk}}{n!(2\pi)^n}
\int_{[-\pi,\pi]^n}\prod_{i=1}^n\phi(\theta_i)
\prod_{i<j}4\sin^2\frac{\theta_i-\theta_j}{2}\,d\boldsymbol\theta.
\tag{2}
\]
One can verify (2) by applying the determinant integration formula to
the two exponential Vandermonde determinants. Their product is the
nonnegative squared circular Vandermonde. Coefficient extraction also
gives zero at every negative integer index, as required.

This is Katkova's Lemma 1, equation (12), in the present normalization;
it is an existing mechanism, not a novelty claim. The new work here is
the explicit sufficient joint-order budget below. The integral in (2)
is real by conjugation, but is not pointwise nonnegative.

## 2. Scalar hypotheses and the noncircular quantitative package

Fix constants \(0<c\le1\), \(B>0\), and \(0<\delta_0\le1\), independent of
\(n,k\). At the saddle suppose:

\[
\log\phi(\theta)=-v\theta^2/2+R(\theta),\qquad
|R(\theta)|\le Bv|\theta|^3,\quad |\theta|\le\delta_0,
\tag{H1}
\]
where the continuous local logarithm is zero at the origin, and
\[
|\phi(\theta)|\le\exp(-cv\theta^2/2),\qquad |\theta|\le\pi.
\tag{H2}
\]
Neither hypothesis mentions a determinant or assumes its sign. Local
nonvanishing is part of H1; no global zero-free hypothesis is made.
Define
\[
A=8+2\log(2/c),
\]
\[
G(n)=\max\left\{
\frac{An^2}{c\delta_0^2},\
\frac{4An^4}{3c},\
16B^2(A/c)^3n^8
\right\}.
\tag{3}
\]
Our quantitative package \(\mathcal H_n(k)\) is H1, H2,
\(\mu(x)=k\), and \(v(x)\ge G(n)\).

**Conditional theorem.** If \(\mathcal H_n(k)\) holds, then
\[
\boxed{
D_{n,k}>
\frac14\,\frac{C(x)^n x^{-nk}}{n!(2\pi)^n}
Z_n(v)>0,\qquad
Z_n(v)=(2\pi)^{n/2}v^{-n^2/2}\prod_{j=1}^n j!.
}
\tag{4}
\]
The scalar hypotheses apply at every order using the same \(x(k)\).
Since \(G\) increases, the package at order \(n\) supplies all orders
at most \(n\). Extension to \(n+1\) requires precisely the stronger
variance threshold \(G(n+1)\), not an unproved determinant sign.
This is a moving-domain mechanism; it is not an induction at fixed \(k\).

## 3. Proof: the margin and every error are normalized together

The Gaussian Vandermonde normalization is
\[
Z_n(v)=\int_{\mathbb R^n}e^{-v\sum\theta_i^2/2}
\prod_{i<j}(\theta_i-\theta_j)^2\,d\boldsymbol\theta.
\tag{5}
\]
For completeness, determinant integration makes this \(n!\) times the
Gaussian moment determinant. The monic Hermite polynomials obtained by
differentiating \(e^{-vx^2/2}\) have squared norms
\(\sqrt{2\pi}\,j!v^{-j-1/2}\), by integration by parts.
Multiplying the norms and \(n!\) proves (4)'s formula.
The product is \(\prod_{j=1}^n j!\), not \(\prod_{j=0}^{n-1}j!\)
without the additional \(n!\).

Choose
\[
\delta^2=\frac{An^2}{cv},\qquad
\tau=nBv\delta^3.
\tag{6}
\]
Condition (3) ensures \(\delta\le\delta_0\), \(\delta<1\),
\(\tau\le1/4\), and \(n(n-1)\delta^2/3\le1/4\).

On the cube \(|\theta_i|\le\delta\), H1 gives
\[
\Re\prod_i\phi(\theta_i)
\ge e^{-\tau}\cos(\tau)e^{-v\sum_i\theta_i^2/2}.
\]
For \(|y|\le1\), \(\sin y/y\ge e^{-y^2/3}\); this follows from
\(\sin y/y\ge1-y^2/6\) and
\(\log(1-z)\ge-z/(1-z)\). Consequently
\[
\prod_{i<j}4\sin^2\frac{\theta_i-\theta_j}{2}
\ge S\prod_{i<j}(\theta_i-\theta_j)^2,\qquad
S=(\sin\delta/\delta)^{n(n-1)}\ge e^{-1/4}.
\tag{7}
\]
At coincident variables the statement follows by continuity.

The Gaussian mass removed by restricting (5) to this cube is at most
\[
T Z_n(v),\qquad
T=2^{n^2/2}e^{-v\delta^2/4}.
\tag{8}
\]
Indeed, on the complement \(\sum\theta_i^2\ge\delta^2\). Split the
Gaussian exponent in half, pull out \(e^{-v\delta^2/4}\), and integrate
the remaining Gaussian at variance parameter \(v/2\) over all of
\(\mathbb R^n\). Its normalization ratio is \(2^{n^2/2}\).

For the **entire complementary region** of the contour cube, H2 and
\(4\sin^2[(a-b)/2]\le(a-b)^2\) give an absolute contribution at most
\[
E Z_n(v),\qquad
E=(2/c)^{n^2/2}e^{-cv\delta^2/4}.
\tag{9}
\]
The same split uses \(Z_n(cv/2)\). This includes every region with just
one variable outside, all other mixed configurations, and the fully
exterior region. There is no uncounted boundary or combinatorial
multiplicity. Enlarging to \(\mathbb R^n\) only increases this upper bound.

Combining the local real margin and the full exterior error gives
\[
\frac{\Re\int_{[-\pi,\pi]^n}\prod_i\phi(\theta_i)\Delta_{\rm circ}^2
\,d\boldsymbol\theta}{Z_n(v)}
\ge e^{-\tau}\cos\tau\,S(1-T)-E.
\tag{10}
\]
This retains the product of all local exponential errors before bounding
it; no linearization or separate determinant cancellation is used.

By (6) and the definition of \(A\),
\[
E=e^{-2n^2},\qquad T\le e^{-2n^2}.
\]
Thus the right side of (10) is at least
\[
e^{-1/2}\cos(1/4)(1-e^{-2})-e^{-2}
>\frac{61}{224}>\frac14.
\tag{11}
\]
For an elementary strict check use \(e^{-1/2}>1/2\),
\(\cos(1/4)\ge31/32\), and \(e^{-2}<1/7\).
Equations (2) and (10) prove (4).

## 4. Explicit order/index consumer and the unclosed region

If canonical analysis supplies H1–H2 for all \(x\ge x_0\) and
\[
\mu(x)/4\le v(x)\le\mu(x),
\tag{12}
\]
let \(k_0\) be an explicit integer at least \(\mu(x_0)\). Then
\[
\boxed{k\ge K(n):=\left\lceil\max\{k_0,\,4G(n)\}\right\rceil}
\tag{13}
\]
implies (4), for every finite \(n\). All constants in \(K\) must come
from the scalar proof; no favorable samples may substitute for them.

This displays why the conservative power is eight. The exterior payment
is \(e^{-2n^2}\). Our elementary Gaussian tail bound chooses
\(\delta\asymp n/\sqrt v\); the total cubic log error is then
\(O(n^4/\sqrt v)\). Requiring fixed slack produces \(v\gtrsim n^8\).
This is a sufficient analytical exponent, not an optimal law or a
measured growth rate.

For the original combined target, set
\[
M_{n,k}=\frac{C(x)^n x^{-nk}Z_n(v)}{4n!(2\pi)^n}.
\]
At \(k\ge K(r+1)\), both factors have independently proved positive
margins, so
\[
Q_{r,k}=D_{r+1,k}D_{r-1,k}>M_{r+1,k}M_{r-1,k}>0.
\tag{14}
\]
No next-order sign was inserted into the premises.

There is still **no joining argument** for \(1\le k<K(n)\) as \(n\)
grows. This includes fixed small \(k\), the boundary transition \(k\sim n\),
and a large intermediate region. A growing finite table cannot close it.
The all-order/all-index implication to PF-infinity and the parent
real-zero conclusion therefore remains unavailable. The entire purpose
of the next execution task is the scalar input to this explicit tail
mechanism, not a claim to have solved that complement.

## 5. Fixed route for scalar canonical acquisition

[Packet12][packet] specifies this as an **optional, inactive RGD-E02 r3
route — execution, Sol**. The baseline check in Section 7 makes acquisition
nondefault; a distinct method-comparison benefit must be selected before
activation. The analytical route, if selected, is fixed:

1. Use (1), \(s=(1+\sqrt x\,e^{i\theta/2})/2\), and the gamma/zeta
   product for xi. Prove explicit bounds for \(\mu,v\), including (12).
2. In a fixed small angular sector, \(\Re s>1\) for large \(x\).
   Absolute convergence gives a legitimate local analytic
   \(\log\zeta\); uniform differentiated Stirling estimates give H1
   with explicit \(B,x_0,\delta_0\).
3. Shrink \(\delta_0\) so \(B\delta_0\le1/4\).
   H1 then gives the local part of H2. This step avoids trying to use
   an additive asymptotic error at arbitrarily small angles.
4. On \(\delta_0\le|\theta|\le\pi\), use uniform Stirling bounds and a
   polynomial upper bound on \((s-1)\zeta(s)\) for \(\Re s\ge1/2\).
   An Euler-summation integral is one direct route to that bound.
   No global logarithm or zero exclusion for zeta is needed.
5. Give explicit \(c,B,\delta_0,x_0,k_0\), insert them into (13), and
   return either the complete theorem or the exact failed estimate.

For orientation only, writing \(t=\sqrt x/2\), Stirling's leading
angular loss is
\[
-\frac t2(1-\cos(\theta/2))\log(t/(2\pi))
-\frac t2(\theta/2)\sin(\theta/2)
+\frac t2(1-\cos(\theta/2)).
\tag{15}
\]
The remaining terms must be bounded explicitly in execution.
The leading scales \(\mu\sim(t/4)\log t,\ v\sim\mu/2\) explain the route,
but are not replacements for the uniform constants in H1–H2.
Polynomial zeta bounds alone introduce additive errors and cannot
establish H2 uniformly as \(\theta\to0\); the split above is mandatory.

This would be a fixed analytical derivation, so it belongs to E02/Sol.
It is not activated by this return. No numerical packet is issued. A need to change source, contour, scalar
hypotheses or determinant target returns to B02 before redesign.

## 6. Controls, baseline and review level

The conditional theorem applies to any positive entire coefficient
sequence satisfying H1–H2. Those hypotheses are local concentration and
global modulus estimates; they need not exclude the repository's
collision controls and do not imply all-index positivity. No control is
claimed to fail them without calculation.

The proposed *canonical acquisition route* uses the literal xi
normalization and its gamma/zeta representation. Weighted-square controls,
Euler-factor changes, reflected sources and smooth primitive controls do
not retain this exact identity; their additional terms would require
their own estimates. That distinction identifies a premise, not a
computed failure of H1 or H2.

The source mechanism and fixed-order eventual positivity already appear
in Katkova. The [reference record][refs] identifies the inspected
passages. This note is an explicit quantitative adaptation, with no
claim of novelty or improvement over the literature's best constants.
Even after successful acquisition, its gain would be a reproducible
joint-order threshold and margin, not an RH proof.

Two read-only same-model contributors checked the normalization,
\(n!\), \(v^{-n^2/2}\), sine loss, phase loss and all exterior regions.
This is internal analytical checking, not independent specialist review.
The [self-assessment][review] records the exact boundaries.
**Next: [E] RGD-E04 r4 — Sol**, then **B02 r2 — Astra** for the
complementary-region mechanism. E02 r3 remains an optional method comparison.

## 7. Stronger reported baseline and the next conceptual decision

The existing [parent catalog][baseline] records Michałowski's
[version 1](https://arxiv.org/html/2607.16795v1), reporting
\(D_{r,k}>0\) for \(k\ge10^{18}r^3\). Theorem 1.1 and selected
Sections 3–6 were rechecked; the full proof and certificates remain
unaudited. Its all-degree analytic bound, matrix response algebra and
inertia argument address the finite-regularity closure problem in the
tail. Therefore the eighth-power route above is not a claimed improvement.

A useful scoped deduction follows from its displayed majorant. Its main
term is
\[
\frac{128\,80^3\sqrt{r^3\tau}}
 {1-320\sqrt{r\tau}},\qquad \tau>1/(2k).
\]
At \(k=Cr\), even if the denominator is positive, this bound is at least
\(128\,80^3r/\sqrt{2C}\), so cannot remain small. This is an obstruction
to that sufficient majorant, not to the true perturbation or determinant.

**Decision:** assess the present return and source dependency first.
Then B02 r2 must choose a boundary-aware, nonperturbative comparison for
bounded \(k/r\), or a precise scoped stop. Improving constants or completing
the weaker tail route alone does not address that decision. No complete
proof audit, certificate replay, or new numerical task is authorized here.

[baseline]: ../../../../references/04_RH_FORMULATION_SOURCES_20261101.md#Michalowski260716795v1

[b03]: 07_RGD_B03_R2_EXACT_PAYMENT_OBSTRUCTION_AND_TRUE_TAIL_20261104.md
[progress]: ../research-progress/01_RADIAL_GREEN_DETERMINANTS_RESEARCH_PROGRESS_20261104.md
[packet]: ../research-progress/handoffs/12_RGD_E04_R4_AND_E02_R3_COMPLETE_SOURCE_CONTOUR_20261104.md
[continuation]: ../research-progress/handoffs/11_RGD_B03_B02_RETURN_AND_MODEL_CONTINUATION_20261104.md
[review]: ../reviews/05_RGD_B03_B02_AUTHOR_AND_SAME_MODEL_CHECKS_20261104.md
[refs]: ../references/README.md
[results]: ../../../../../../../result-summaries/README.md
[theta]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a11]: ../../../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
