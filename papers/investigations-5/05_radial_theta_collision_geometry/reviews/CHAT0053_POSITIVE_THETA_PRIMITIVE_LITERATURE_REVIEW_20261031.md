# Positive theta primitives and their use in sign and zero theorems

31 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, effort **xhigh**, Investigation05 chat0053.

**Status: selected-primary-source literature review with normalization checks.** This reviews uses of Riemann's undifferentiated theta representation and positive or integrated kernels. It does not attribute this investigation's three-dimensional construction to earlier authors, claim a new theta sign theorem, or supply independent assessments of the recent preprints. The scope follows the author's clarification in this chat: the classical primitive is the focus.

The strongest direct precedents are Hardy's use of the undifferentiated theta expression to force infinitely many real zeros, and Csordas–Norfolk–Varga's use of a different integrated theta kernel to prove Turán inequalities. They support the usefulness of indirect kernel arguments. The decisive extra inputs are complex boundary behavior and log-concavity, respectively.

Read with the [result index](../../../../result-summaries/README.md), especially [cluster14](../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [control cluster12](../../../../result-summaries/12_collision_controls_and_screening.md), and the [avoid index](../../../../avoid/README.md), especially [reformulations](../../../../avoid/01_restating_the_target.md) and [unchecked imports](../../../../avoid/16_unchecked_imports_and_novelty_claims.md). Bibliographic versions, inspected passages, and external PDF receipts are in [reference21](../references/21_POSITIVE_THETA_PRIMITIVE_LITERATURE_SOURCES_20261031.md). Riemann's 1859 paper and the DLMF formula retain [reference13](../references/13_RIEMANN_THETA_MELLIN_ATTRIBUTION_20261028.md).

## 1. The precise classical objects

Write
\[
\vartheta(x)=\sum_{n\in\mathbb Z}e^{-\pi n^2x},\qquad
p(u)=e^u\frac{\vartheta(e^{4u})-1}{2},\quad u\ge0.
\]
Thus \(p=\psi_\theta\) in the manuscript. With its complete source \(\Phi\),
\[
p''-p=8\Phi,\qquad p'(0)=-\frac12.
\]
The decaying half-line primitive and its cosine transform are
\[
J(a)=\int_0^\infty p(u)\cos(au)\,du,\qquad
H(0,a)=\frac1{16}-\frac{1+a^2}{8}J(a).
\tag{1}
\]
The boundary constant is essential. In particular, a zero of \(H(0,a)\) is a crossing of \(J(a)\) with \(1/[2(1+a^2)]\), not a zero of \(J\). This is an exact reformulation, not a proposed new criterion.

A second version is the smooth even completed primitive
\[
G(u)=\cosh u-\frac12e^u\vartheta(e^{4u})
=\frac12e^{-|u|}-p(|u|).
\tag{2}
\]
It satisfies
\[
(1-\partial_u^2)G=8\Phi,\qquad
16H(0,a)=(1+a^2)\int_{\mathbb R}G(u)e^{iau}\,du.
\tag{3}
\]
The integral in(3) initially defines a holomorphic function in \(|\operatorname{Im}a|<1\). The identity for real \(a\) suffices here. The expressions in(1)–(3) are the manuscript/book normalization of the classical scalar theta representation.

Both \(p\) and \(G\) are positive, but they are different kernels: \(p\) decays double exponentially and its even extension has a cusp; \(G\) is smooth and has exponential tails. Positivity at every point does not mean a fixed positive lower bound at infinity.

## 2. Convexity gives a rigorous positive transform

The convex-kernel criterion of Pólya says that a continuous even function, normalized at zero, convex on the positive half-line and tending to zero, is positive definite; see Csordas, Theorem3.4. Here the criterion applies to \(p(|u|)/p(0)\), not to the smooth even physical kernel.

The specialization is elementary and already proved in [Investigation21 Note52](../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/52_POSITIVE_THETA_PRIMITIVE_AND_DIFFERENTIAL_CLOSURE_20261015.md):
\[
p''=p+8\Phi>0,\qquad
J(a)=\frac1{a^2}\int_0^\infty p''(u)(1-\cos au)\,du>0
\quad(a\ne0).
\tag{4}
\]
The value at zero is positive by its defining integral. Note52 also pays the convexity of \(e^{tu^2}p(u)\) for \(0\le t\le1/2\).

Equation(4) turns an oscillatory integral into a nonnegative one. Equation(1), however, still compares that positive transform with a particular rational profile. This explains exactly what the convexity theorem supplies and what it does not.

## 3. Hardy uses the same undifferentiated expression to force zeros

A direct modern source is Dixit–Kumar–Maji–Zaharescu, arXiv:1712.08435v1, Introduction(1.1)–(1.6), which recalls Hardy's 1914 method before extending it to other functions. With \(\Xi(\tau)=\xi(1/2+i\tau)\), its identity(1.3) is
\[
\frac2\pi\int_0^\infty
 \frac{\Xi(\tau)}{\tau^2+1/4}\cosh(\alpha\tau)\,d\tau
=e^{-i\alpha/2}-2e^{i\alpha/2}
 \sum_{n\ge1}e^{-\pi n^2e^{2i\alpha}},
\quad |\alpha|<\pi/4.
\tag{5}
\]
The right side is \(2G(i\alpha/2)\). This is the same completed primitive(2), without invoking a spatial realization. Hardy's use of it yields infinitely many critical-line zeros; it does not give reality of all zeros or simplicity.

**Normalization and mechanism, worked out here.** Define \(I(\alpha)\) as the integral in(5), and put
\[
B(\alpha)=e^{i\alpha/2}\vartheta(e^{2i\alpha}).
\]
Then
\[
I(\alpha)=\pi\cos(\alpha/2)-\frac{\pi}{2}B(\alpha).
\]
Along the circular approach \(\alpha\uparrow\pi/4\), \(B\) and each fixed derivative tend to zero. To see the source of this decay, set \(\delta=e^{2i\alpha}-i\). The theta factor is
\[
\vartheta(i+\delta)=\sum_{n\in\mathbb Z}(-1)^n e^{-\pi n^2\delta}
=\delta^{-1/2}\sum_{k\in\mathbb Z}
 e^{-\pi(k+1/2)^2/\delta}.
\tag{6}
\]
On this particular path, \(\operatorname{Re}(1/\delta)\to+\infty\) proportionally to \(1/(\pi/4-\alpha)\). The half-integer shift in(6) leaves no zero mode, and exponential decay dominates each fixed derivative's algebraic factors. This checks the needed boundary limit on the path actually used; no claim about arbitrary tangential approaches is needed.

Differentiating(5) \(2n\) times inside the open interval therefore gives the classical limiting signs
\[
\lim_{\alpha\uparrow\pi/4}
\int_0^\infty
\frac{\Xi(\tau)}{\tau^2+1/4}\tau^{2n}\cosh(\alpha\tau)\,d\tau
=\pi(-1)^n2^{-2n}\cos(\pi/8).
\tag{7}
\]
In our manuscript's variables \(a=2\tau\), \(H(0,a)=\Xi(a/2)/8\), this becomes
\[
\lim_{\beta\uparrow\pi/8}
\int_0^\infty
\frac{H(0,a)}{1+a^2}a^{2n}\cosh(\beta a)\,da
=\frac{\pi}{16}(-1)^n\cos(\pi/8).
\tag{8}
\]

Why can this force sign changes without locating individual zeros? If \(\Xi\) had one fixed sign beyond some height, the finite limits in(7) would imply integrability of each corresponding critical-boundary tail by monotone convergence. Contributions from a bounded interval grow at most like \(A^{2n}\); a nonzero interval beyond any larger \(B>A\), with the eventual sign, contributes at least a positive constant times \(B^{2n}\). The moments would eventually have that same sign. Their alternating signs in(7) contradict this. Thus the modular behavior at a complex boundary supplies information unavailable from positivity on the real source axis alone.

This is the most direct precedent for the author's proposed point of view.

## 4. An integrated kernel proves actual quadratic coefficient inequalities

Csordas–Norfolk–Varga, *The Riemann Hypothesis and the Turán Inequalities* (1986), Proposition2.1, prove strict log-concavity of
\[
K(x)=\int_x^\infty \Phi(\sqrt v)\,dv.
\tag{9}
\]
Their Theorem1.1 establishes the Turán inequalities for the normalized xi moments. This is a different primitive from \(p\); it is important not to identify them.

Here is the normalization connecting the result to our source. Set
\[
b_m=\int_0^\infty u^{2m}\Phi(u)\,du,\qquad
\gamma_m=\frac{m!}{(2m)!}b_m.
\]
For \(m\ge1\), elementary integration by parts gives
\[
b_m=\frac{2m-1}{4}\int_0^\infty x^{m-3/2}K(x)\,dx,
\qquad
\gamma_m=\frac{\sqrt\pi}{2\,4^m\Gamma(m-1/2)}
\int_0^\infty x^{m-3/2}K(x)\,dx.
\tag{10}
\]
Their concavity argument controls these normalized moments and yields
\[
\gamma_m^2-\gamma_{m-1}\gamma_{m+1}\ge0,\qquad m\ge1.
\tag{11}
\]
The first index is handled separately in the paper. This is substantive sign information, although it is about coefficients, not the expression \(H_a(a)^2-H(a)H_{aa}(a)\) at every frequency. The key gain is the stronger shape theorem for the integrated kernel.

As a later development in the coefficient approach, Griffin–Ono–Rolen–Zagier (2019), Theorems1–3, prove that for each fixed degree \(d\), the xi Jensen polynomials are real-rooted for all sufficiently large shifts \(n\), using a Hermite limit. The threshold depends on \(d\). This is an established partial result beyond a reformulation, but it does not cover all degrees and shifts simultaneously. It uses xi coefficient information rather than directly estimating the particular primitive in(1).

## 5. Which kernel positivity would control pointwise Laguerre signs?

Csordas (2014 preprint), Theorem3.7, studies the associated kernels
\[
\mathcal K_n(v)=\int_{\mathbb R}
\Phi(u+v)\Phi(u-v)u^{2n}\,du.
\tag{12}
\]
They are pointwise positive. The stronger property needed is positive definiteness:
\[
\sum_{j,k}c_j\overline{c_k}\,
\mathcal K_n(x_j-x_k)\ge0
\]
for every finite choice of points and coefficients.

For clarity, applying his full-line formula to \(F=2H(0,\cdot)\) gives, in our normalization,
\[
H_a(0,a)^2-H(0,a)H_{aa}(0,a)
=\int_{\mathbb R}\mathcal K_1(v)\cos(2av)\,dv.
\tag{13}
\]
Thus positive definiteness would sign this expression. The full hierarchy is an all-real-zero characterization, not an independent proof. His Open Problem4.7 explicitly asks for the first xi Laguerre inequality. The selected literature here supplies no global primitive-derived solution to that question.

This distinction is useful for an indirect approach: an autocorrelation or Gram representation of the required associated kernel would constitute extra information. Merely renaming pointwise positivity as positive definiteness would not.

## 6. Other uses worth keeping distinct

**Probability.** Biane–Pitman–Yor (published2001; 1999 preprint), Section2 and Proposition1, turn Riemann's integration-by-parts density into a positive random variable \(Y\) satisfying
\[
\mathbb E Y^s=2\xi(s),\quad
\mathbb E g(1/Y)=\mathbb E[Yg(Y)],\quad
\mathbb E e^{-\lambda Y^2}
=\left(\frac{\sqrt{\pi\lambda}}{\sinh\sqrt{\pi\lambda}}\right)^2.
\tag{14}
\]
This makes inversion a size-bias identity and supplies probabilistic constructions. Infinite divisibility of the displayed square-variable law does not imply infinite divisibility of \(\log Y\), whose tilted characteristic function is relevant to xi zeros. The paper does not prove the sought global signs. It is an adjacent use of the classical theta representation, not a new three-dimensional argument attributed to this project.

**Orthogonal polynomial bases.** Romik, arXiv:1902.06330v3, Section3, obtains a Meixner–Pollaczek expansion
\[
\Xi(\tau)=\sum_{n\ge0}(-1)^n c_{2n}
P_{2n}^{(3/4)}(\tau/2;\pi/2),
\qquad c_{2n}>0,
\tag{15}
\]
with compact convergence and quantitative coefficient estimates from theta integrals. It reorganizes the transform into a basis with understood zeros. Positive coefficients and real-rooted basis elements do not ensure real-rooted partial sums. The reviewed result is an adjacent representation, not a sign theorem for our primitive. The section numbers refer specifically to the preprint version.

**Current finite-order results.** Two author-hosted Sra preprints were located: *Sharp order-four sign regularity of a Jacobi theta kernel*, v1,10October2026, reports reverse regularity through order four and failure at order five for \(\Phi(\sqrt{x+y})\); *On some positivity properties of the Riemann Xi function*, v2,29October2026, reports finite-order total positivity for reciprocal-transform densities and generalized Laguerre inequalities on a range supported by verified zeros. These concern other kernels. Their selected theorem statements were checked, but the proofs and certificates were not independently audited. They are not evidence that the positive primitive has acquired a global sign theorem.

## 7. Consequences for this investigation

The literature supports a more precise judgment than either “the primitive is positive, so it should solve the sign problem” or “the representation is classical, so it cannot help.”

There are demonstrated ways that the simpler object becomes useful:

- Its convexity turns one oscillatory transform into a positive integral, as in(4).
- Its exact complex boundary behavior forces alternating spectral moments, as in Hardy's argument.
- A suitable integrated kernel has a stronger log-concavity theorem, which transfers to quadratic inequalities for coefficients.

The next conceptual question is which additional property of the complete theta primitive is tractable and has an independently proved sign consequence. The Hardy/modular-boundary and integrated-kernel concavity methods are the most directly relevant reading targets. The literature review does not select a new numerical campaign, assert a new RH-equivalent criterion as progress, or justify another auxiliary flow by itself.

Control screening remains material. The [positive-primitive collision control in Note56](../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/56_POSITIVE_PRIMITIVE_COLLISION_CONTROL_20261015.md) preserves positivity of the primitive transform, the reconstruction constant and every algebraic endpoint asymptotic, yet has a positive-time collision. It defeats using those premises alone. It does not establish the complete theta identity(6), nor has it been shown here to satisfy the integrated-kernel concavity premise(9). The weighted-square and Euler-factor controls likewise must not be treated as satisfying all complex modular boundary identities merely because they share selected real-source properties. No new separating premise has been verified for all controls in this review.

**Reading order:** the manuscript primitive identity alongside Dixit et al. Introduction(1.1)–(1.6); Csordas–Norfolk–Varga Sections1–3; Csordas Sections3–4; then Biane–Pitman–Yor Section2 or Romik Section3 according to the mechanism of interest. Sato's exposition of Pólya's criterion is recorded as a reading lead because full primary retrieval failed.

The review changes the emphasis of the preceding discussion: the absence of an auxiliary-flow advantage does not argue against indirect work through the primitive. The literature identifies specific extra structures that have already converted such viewpoints into nontrivial theorems.
