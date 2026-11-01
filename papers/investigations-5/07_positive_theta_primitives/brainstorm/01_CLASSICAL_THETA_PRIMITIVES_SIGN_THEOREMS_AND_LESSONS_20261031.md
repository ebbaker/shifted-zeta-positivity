# Classical theta primitives and indirect sign arguments

31 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **xhigh**.

**Status: opening brainstorm and careful synthesis of classical results, inherited repository results, and their limitations.** The elementary normalization and integration-by-parts calculations are written out below. Imported theorems retain their source hypotheses and reading status. This is not a new RH, simplicity, global Laguerre-sign, or strip-contraction theorem, and has not received independent specialist review.

Investigation07 studies how the simpler positive theta primitive can supply additional information for sign and zero questions. It grows out of the author's three-dimensional integration-by-parts work in [Investigation05](../../05_radial_theta_collision_geometry/README.md), but the initial focus is the classical scalar Riemann representation and its uses. The geometric construction is the provenance of the question; no priority attribution for that construction is made here.

Three successful mechanisms organize the starting point: convexity converts one oscillatory transform to a positive integral; the exact modular boundary behavior forces Hardy's alternating moments; and log-concavity of a different integrated kernel yields quadratic coefficient inequalities. Each is more specific than positivity of the source. The objective at this stage is to understand these mechanisms before choosing a new deformation or estimate.

Read with the [result index](../../../../result-summaries/README.md), especially [theta identities](../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md), and the [avoid index](../../../../avoid/README.md), especially [restating the target](../../../../avoid/01_restating_the_target.md), [shape-only premises](../../../../avoid/02_shape_only_arguments_and_the_controls.md), [scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [separate absolute bounds](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

The [annotated bibliography](../references/01_ANNOTATED_BIBLIOGRAPHY_20261031.md) records the exact versions, passages checked, limitations, and prior PDF receipts. The originating [literature review](../../05_radial_theta_collision_geometry/reviews/CHAT0053_POSITIVE_THETA_PRIMITIVE_LITERATURE_REVIEW_20261031.md) remains the historical record; the present note develops the new investigation's starting exposition and lessons.

## 1. The precise classical objects

Write
\[
\vartheta(x)=\sum_{n\in\mathbb Z}e^{-\pi n^2x},\qquad
p(u)=e^u\frac{\vartheta(e^{4u})-1}{2},\quad u\ge0.
\]
Thus \(p=\psi_\theta\) in Investigation05. The real source coordinate is \(u\), the real spectral coordinate is \(a\), its complex continuation is \(z\), and physical heat time is \(t\). The complete source and transform are
\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},
\qquad H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du.
\]
For \(u\ge0\), each source summand is positive; modularity gives the even smooth extension to all real \(u\). The decay permits every fixed source derivative and compact-parameter differentiation used below. Set
\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
\qquad \Xi(\tau)=\xi(1/2+i\tau).
\]
Here \(s\) is the Mellin variable only; any auxiliary-flow time below is denoted \(\sigma\).

Riemann's split theta integral, in modern notation, reads
\[
\xi(s)=\frac12+\frac{s(s-1)}4
\int_1^\infty(\vartheta(x)-1)
\bigl(x^{s/2}+x^{(1-s)/2}\bigr)\frac{dx}{x}.
\tag{R}
\]
The integral on the right is entire in \(s\); this is the continuation obtained after splitting the initial Mellin integral, not a claim that the original unsplit Mellin integral converges everywhere. The substitution \(x=e^{4u}\) gives
\[
\xi(s)=\frac12+4s(s-1)\int_0^\infty p(u)\cosh((2s-1)u)\,du.
\]
At \(s=1/2+ia/2\), it becomes \(\Xi(a/2)=1/2-(1+a^2)J(a)=8H(0,a)\). Riemann and the DLMF normalization are annotated in [the bibliography](../references/01_ANNOTATED_BIBLIOGRAPHY_20261031.md#riemann1859).

For a direct differential check, \(P(u)=e^u\vartheta(e^{4u})=e^u+2p(u)\) is even by theta inversion. Consequently \(P'(0)=0\). Differentiating the complete series gives
\[
p''-p=8\Phi,\qquad p'(0)=-\frac12.
\]
The decaying half-line primitive and its cosine transform are
\[
J(a)=\int_0^\infty p(u)\cos(au)\,du,\qquad
H(0,a)=\frac1{16}-\frac{1+a^2}{8}J(a).
\tag{1}
\]
Indeed, \(\int_0^\infty p''(u)\cos(au)\,du=-p'(0)-a^2J(a)\); the terms at infinity vanish by double-exponential decay. The boundary constant is essential. In particular, a zero of \(H(0,a)\) is a crossing of \(J(a)\) with \(1/[2(1+a^2)]\), not a zero of \(J\). This is an exact reformulation, not a proposed new criterion.

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
The integral in (3) initially defines a holomorphic function in \(|\operatorname{Im}a|<1\). The identity for real \(a\) suffices here. The expressions in (1)–(3) are the manuscript/book normalization of the classical scalar theta representation.

The positivity of \(G\) can also be checked without a termwise comparison: the decaying Green function of \(1-D^2\) is \(e^{-|u|}/2\), so
\[
G(u)=4\int_{\mathbb R}e^{-|u-v|}\Phi(v)\,dv>0.
\]
This follows from the displayed differential equation and decay at both infinities; the difference of two such solutions of \((1-D^2)G=8\Phi\) is zero. It concerns real \(u\). The theta formula continues \(G\) analytically to \(|\operatorname{Im}u|<\pi/8\); the absolute-value formula is only its real-axis representation.

Both \(p\) and \(G\) are positive, but they are different kernels: \(p\) decays double exponentially and its even extension has a cusp; \(G\) is smooth and has exponential tails. Positivity at every point does not mean a fixed positive lower bound at infinity.

## 2. Convexity gives a rigorous positive transform

The convex-kernel criterion of Pólya says that a continuous even function, normalized at zero, convex on the positive half-line and tending to zero, is positive definite; see Csordas, Theorem 3.4. Here the criterion applies to \(p(|u|)/p(0)\), not to the smooth even physical kernel.

The specialization is elementary and already proved in [Investigation21 Note52](../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/52_POSITIVE_THETA_PRIMITIVE_AND_DIFFERENTIAL_CLOSURE_20261015.md):
\[
p''=p+8\Phi>0,\qquad
J(a)=\frac1{a^2}\int_0^\infty p''(u)(1-\cos au)\,du>0
\quad(a\ne0).
\tag{4}
\]
The value at zero is positive by its defining integral. The argument also extends to the physical heat interval \(0\le t\le1/2\). Let \(f_t=e^{tu^2}p\), and in one summand put \(q_n=\pi n^2e^{4u}\). For \(u\ge0\), \(0\le t\le1/2\),
\[
\frac{(e^{tu^2+u-q_n})''}{e^{tu^2+u-q_n}}
=(2tu+1-4q_n)^2+2t-16q_n
\ge9q_n^2-16q_n>0,
\]
because \(2tu+1\le u+1\le q_n\). Thus the same proof gives
\[
J(t,a)=\int_0^\infty e^{tu^2}p(u)\cos(au)\,du>0
\quad(0\le t\le1/2,\ a\in\mathbb R).
\]
The exact recovery identity, already in Note52, is
\[
8H(t,a)=\frac12+(2t-a^2-1)J(t,a)
+4taJ_a(t,a)-4t^2J_{aa}(t,a).
\tag{H}
\]
It follows by transferring both derivatives in \(p''-p\) to \(e^{tu^2}\cos(au)\), retaining the lower boundary. This identity holds for every finite real \(t\); the positivity assertion just proved is restricted to \(0\le t\le1/2\). The terms of (H) have different signs, so positivity of \(J\) does not determine the sign or nonvanishing of the reconstructed physical jet.

Equation (4) turns an oscillatory integral into a nonnegative one. Equation (1), however, still compares that positive transform with a particular rational profile. This explains exactly what the convexity theorem supplies and what it does not.

## 3. Hardy uses the same undifferentiated expression to force zeros

A direct modern source is Dixit–Kumar–Maji–Zaharescu, arXiv:1712.08435v1, Introduction (1.1)–(1.6), which recalls Hardy's 1914 method before extending it to other functions. With \(\Xi(\tau)=\xi(1/2+i\tau)\), its identity (1.3) is
\[
\frac2\pi\int_0^\infty
 \frac{\Xi(\tau)}{\tau^2+1/4}\cosh(\alpha\tau)\,d\tau
=e^{-i\alpha/2}-2e^{i\alpha/2}
 \sum_{n\ge1}e^{-\pi n^2e^{2i\alpha}},
\quad |\alpha|<\pi/4.
\tag{5}
\]
The right side is \(2G(i\alpha/2)\). This is the same completed primitive (2), without invoking a spatial realization. Hardy's use of it yields infinitely many critical-line zeros; it does not give reality of all zeros or simplicity.

**Normalization and mechanism, worked out here.** Define \(I(\alpha)\) as the integral in (5), and put
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
On this particular path, \(\operatorname{Re}(1/\delta)\to+\infty\) proportionally to \(1/(\pi/4-\alpha)\). The half-integer shift in (6) leaves no zero mode, and exponential decay dominates each fixed derivative's algebraic factors. This checks the needed boundary limit on the path actually used; no claim about arbitrary tangential approaches is needed.

Differentiating (5) \(2n\) times inside the open interval therefore gives the classical limiting signs
\[
\lim_{\alpha\uparrow\pi/4}
\int_0^\infty
\frac{\Xi(\tau)}{\tau^2+1/4}\tau^{2n}\cosh(\alpha\tau)\,d\tau
=\pi(-1)^n2^{-2n}\cos(\pi/8).
\tag{7}
\]
In the inherited normalization \(a=2\tau\), \(H(0,a)=\Xi(a/2)/8\), this becomes
\[
\lim_{\beta\uparrow\pi/8}
\int_0^\infty
\frac{H(0,a)}{1+a^2}a^{2n}\cosh(\beta a)\,da
=\frac{\pi}{16}(-1)^n\cos(\pi/8).
\tag{8}
\]

Why can this force sign changes without locating individual zeros? If \(\Xi\) had one fixed sign beyond some height, the finite limits in (7) would imply integrability of each corresponding critical-boundary tail by monotone convergence. Contributions from a bounded interval grow at most like \(A^{2n}\); a nonzero interval beyond any larger \(B>A\), with the eventual sign, contributes at least a positive constant times \(B^{2n}\). The moments would eventually have that same sign. Their alternating signs in (7) contradict this. Thus the modular behavior at a complex boundary supplies information unavailable from positivity on the real source axis alone.

This is the most direct precedent for the author's proposed point of view.

## 4. An integrated kernel proves actual quadratic coefficient inequalities

Csordas–Norfolk–Varga, *The Riemann Hypothesis and the Turán Inequalities* (1986), Proposition 2.1, prove strict log-concavity of
\[
K(x)=\int_x^\infty \Phi(\sqrt v)\,dv,\qquad x\ge0.
\tag{9}
\]
Their Theorem 1.1 establishes the Turán inequalities for the normalized xi moments. This is a different primitive from \(p\); it is important not to identify them.

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
The paper treats the indices at least two analytically and handles the first separately. Strict log-concavity of K and the full Turán conclusion are imported results of that paper; the integration-by-parts normalization (10) is the calculation reproduced here. Selected theorem and setup pages were checked, not the entire proof. This is substantive sign information, although it is about coefficients, not the expression \(H_a(a)^2-H(a)H_{aa}(a)\) at every frequency. The key gain is the stronger shape theorem for the integrated kernel.

As a later development in the coefficient approach, Griffin–Ono–Rolen–Zagier (2019), Theorems 1–3, prove that for each fixed degree \(d\), the xi Jensen polynomials are real-rooted for all sufficiently large shifts \(n\), using a Hermite limit. The threshold depends on \(d\). This is an established partial result beyond a reformulation, but it does not cover all degrees and shifts simultaneously. It uses xi coefficient information rather than directly estimating the particular primitive in (1).

## 5. Which kernel positivity would control pointwise Laguerre signs?

Csordas (2014 preprint), Theorem 3.7, studies the associated kernels
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
For example, the constant in (13) follows directly by writing \(F(a)=\int_{\mathbb R}\Phi(x)e^{iax}\,dx=2H(0,a)\). Symmetrization gives
\[
F'(a)^2-F(a)F''(a)
=\frac12\iint (x-y)^2\Phi(x)\Phi(y)e^{ia(x+y)}\,dx\,dy.
\]
Set \(x=v+u\), \(y=v-u\), whose Jacobian is 2, and use evenness of \(\Phi\); the result is four times the right side of (13). This also avoids a half-line/full-line factor ambiguity in importing the source formula.

For this continuous integrable kernel, positive definiteness makes its Fourier transform nonnegative and would therefore sign (13). The full hierarchy is an all-real-zero characterization, not an independent proof. His Open Problem 4.7 explicitly asks for the first xi Laguerre inequality. The selected literature here supplies no global primitive-derived solution to that question.

This distinction is useful for an indirect approach: an autocorrelation or Gram representation of the required associated kernel would constitute extra information. Merely renaming pointwise positivity as positive definiteness would not.

## 6. Other uses worth keeping distinct

**Probability.** Biane–Pitman–Yor (published 2001; 1999 preprint), Section 2 and Proposition 1, turn Riemann's integration-by-parts density into a positive random variable \(Y\) satisfying
\[
\mathbb E Y^s=2\xi(s),\quad
\mathbb E g(1/Y)=\mathbb E[Yg(Y)],\quad
\mathbb E e^{-\lambda Y^2}
=\left(\frac{\sqrt{\pi\lambda}}{\sinh\sqrt{\pi\lambda}}\right)^2.
\tag{14}
\]
This makes inversion a size-bias identity and supplies probabilistic constructions. Infinite divisibility of the displayed square-variable law does not imply infinite divisibility of \(\log Y\), whose tilted characteristic function is relevant to xi zeros. The paper does not prove the sought global signs. It is an adjacent use of the classical theta representation, not a new three-dimensional argument attributed to this project.

**Orthogonal polynomial bases.** Romik, arXiv:1902.06330v3, Section 3, obtains a Meixner–Pollaczek expansion
\[
\Xi(\tau)=\sum_{n\ge0}(-1)^n c_{2n}
P_{2n}^{(3/4)}(\tau/2;\pi/2),
\qquad c_{2n}>0,
\tag{15}
\]
with compact convergence and quantitative coefficient estimates from theta integrals. It reorganizes the transform into a basis with understood zeros. Positive coefficients and real-rooted basis elements do not ensure real-rooted partial sums. The reviewed result is an adjacent representation, not a sign theorem for our primitive. The section numbers refer specifically to the preprint version.

**Current finite-order results.** Two author-hosted Sra preprints were located: *Sharp order-four sign regularity of a Jacobi theta kernel*, v1, 10 October 2026, reports reverse regularity through order four and failure at order five for \(\Phi(\sqrt{x+y})\); *On some positivity properties of the Riemann Xi function*, v2, 29 October 2026, reports finite-order total positivity for reciprocal-transform densities and generalized Laguerre inequalities on a range supported by verified zeros. These concern other kernels. Their selected theorem statements were checked, but the proofs and certificates were not independently audited. They are not evidence that the positive primitive has acquired a global sign theorem.

## 7. Lessons carried from radial theta geometry and the auxiliary flow

### A simpler positive object can be useful without solving the target

The primitive approach has an actual gain already: (4) proves a positive transform, and (H) preserves the exact reconstruction boundary. Hardy's argument and the integrated-kernel theorem show that such a viewpoint can lead to substantive conclusions. Being classical does not make the representation exhausted. Conversely, the new spatial interpretation does not by itself strengthen the classical scalar sign conclusions. The useful question is what extra tractable property the representation exposes.

The three positive objects must remain separate: the half-line primitive p, the smooth completion G, and the square-root-variable integral K. Their decay, regularity, and transform domains differ. In particular, the modular-even \(P=e^u+2p\) grows like \(e^u\) and cannot replace p in a positive-time cosine integral. Positivity on the real source axis is not positivity of an oscillatory transform, positive definiteness of a correlation kernel, or a lower bound for a physical jet.

### Conservation is an identity until an independent estimate is added

The [zero-time auxiliary-flow discussion](../../05_radial_theta_collision_geometry/notes/CHAT0053_ZERO_TIME_AUXILIARY_EVOLUTION_AND_REAL_ZEROS_20261031.md) distinguishes
\[
\int P_\sigma(\rho_0k_z)=\int\rho_0k_z,
\qquad
\int(P_\sigma\rho_0)k_z=\int\rho_0P_\sigma^*k_z.
\]
The first transports the complete spectral density and preserves the original function, hence every zero and multiplicity. The second transports the source and gives a genuinely different spectral family. Removing the energy normalization does not remove the first conservation identity. A common propagator is needed to interpret the complex spectral family; frequency-by-frequency feedback choices do not automatically define a holomorphic evolution.

An energy lower bound obtained from an already positive physical vector mass cannot prove that initial mass margin. The finite rectangle near \(t=1/4\) and \(64\le a\le66\) demonstrates a useful calculation through a simple zero: H changes sign while \(H_a\) remains negative. Its common-flow energy floor is valid for every auxiliary time but only on that finite physical region, and it inherits the independently established first-jet margin. This is the status recorded in [Bottleneck Note32](../../05_radial_theta_collision_geometry/notes/fixed_coefficient_parameter_geometry/32_HIGH_HEIGHT_CANCELLATION_BOTTLENECKS_AND_TROUBLESHOOTING_20261030.md), not an obstruction to every possible auxiliary method.

### A deformation can lose a decisive endpoint cancellation

For the specific raw exterior source, drift \(v(X)=X+X/(1+|X|^2)\), and fixed logarithmic cosine observation, the source-only family is
\[
F_\sigma(z)=\int_0^\infty\Phi(u)\cos(z\chi_\sigma(u))\,du,
\qquad
\chi_\sigma(0)=\frac14\log\bigl(\sqrt{1+3e^{-4\sigma}}-1\bigr).
\]
Here \(\partial_\sigma\chi_\sigma=-[3/4-\tanh(2\chi_\sigma)/4]\) and \(\chi_0(u)=u\). The raw source is \(\rho_0(X)=\mathbf1_{|X|\ge1}\Phi(\log|X|/2)/(8\pi|X|^3)\), evolved by \(\partial_\sigma\rho=\operatorname{div}(v\rho)\), with characteristic velocity \(-v\). For nonzero finite \(\sigma\) the endpoint moves. Its leading boundary contribution is proportional to \(\sin(z\chi_\sigma(0))/z\), and the comparison of bounded-strip zero counts with entire growth yields zeros outside every bounded horizontal strip. This is **proved in-note with a same-assistant self-assessment**, not independently reviewed: [source-transport obstruction](../../05_radial_theta_collision_geometry/notes/CHAT0053_SOURCE_TRANSPORT_UNBOUNDED_STRIP_OBSTRUCTION_20261031.md), [assessment](../../05_radial_theta_collision_geometry/reviews/CHAT0053_SOURCE_TRANSPORT_OBSTRUCTION_SELF_ASSESSMENT_20261031.md). It excludes an eventual all-real theorem for that specified family at finite nonzero time. It does not exclude every source transport, an odd endpoint-preserving drift, or a different observation. Removing an endpoint defect would remove this particular obstruction, not prove a new zero theorem.

### Absolute control can erase the only useful interaction

For a real vector quantity \(V=M+R\),
\[
\|V\|^2=\|M\|^2+2\langle M,R\rangle+\|R\|^2.
\]
A large remainder need not be destructive. Bounding its mixed contribution by \(-2\|M\|\|R\|\) can discard a constructive interaction. The earlier absolute primitive and absolute Poisson-mode payments were failures of specified estimates; they do not reject every use of the primitive or Poisson summation. More arithmetic precision cannot repair an analytically oversized allowance. The same [bottleneck note](../../05_radial_theta_collision_geometry/notes/fixed_coefficient_parameter_geometry/32_HIGH_HEIGHT_CANCELLATION_BOTTLENECKS_AND_TROUBLESHOOTING_20261030.md) records the exact tested classes and the scope of the fixed-Gaussian-model obstruction; its separate-assessment status is not upgraded here.

The primitive has an especially transparent scale mismatch. Note52 gives
\[
J(t,a)=\frac1{2a^2}-\frac{1+6t}{2a^4}+O_T(a^{-6})
\quad(0\le t\le T),
\]
while the physical transform and fixed jets have exponential spectral decay. The differential combination (H) therefore cancels large algebraic terms. Its separately positive pieces are not naturally small relative to the final signal. Hardy's use of exact boundary limits is a precedent for extracting information before those cancellations are replaced by absolute bounds.

### The controls limit premises, not all indirect arguments

The [positive-primitive control in Note56](../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/56_POSITIVE_PRIMITIVE_COLLISION_CONTROL_20261015.md) preserves positivity of the primitive transform, the reconstruction constant, a smooth even completion, and all algebraic spectral endpoint asymptotics, yet has a positive-time collision. Those premises alone cannot imply the desired global noncollision conclusion. It does not establish the complete theta boundary identity (6); whether it satisfies the particular integrated-kernel log-concavity premise (9) has not been checked here.

The other families in [control cluster12](../../../../result-summaries/12_collision_controls_and_screening.md) impose different tests. Euler-factor controls change the complete theta coefficients; weighted-square controls retain square support and finitely many endpoints but fail full reflection; reflected smooth controls fail the full integer-square theta structure. These distinctions identify information that a future argument might use, not a completed control screen for a new theorem. No additional separating inequality is claimed in this opening note. A future proposal must name the premise or estimate that fails for each relevant control on a domain containing its collision.

### The conclusions have different quantifiers

Hardy's infinitely many real zeros do not exclude other zeros. Coefficient Turán inequalities do not establish every pointwise Laguerre inequality. Fixed-degree eventual Jensen hyperbolicity is not uniform in degree. A finite rectangle at positive time is not a cover of all heights together with \(t\) approaching zero. A scalar quotient by H becomes singular at its simple zeros; any later comparison intended to cross them must use a regular object, such as an independently controlled first jet, or justify a change of reference. The present note supplies no such global comparison.

## 8. Starting questions and reading order

The initial task is explanatory rather than a new numerical campaign. Read the Hardy identity and its boundary mechanism alongside p and G; then read the full Csordas–Norfolk–Varga concavity proof, keeping its K distinct from both. The first bounded mathematical question is what in those arguments is genuinely theta-specific and what survives for the registered controls.

For Hardy's method, investigate which joint transform identities are available before taking absolute values, and what sign conclusion each one actually has. For K, understand the normalized-moment inequality and the source of its log-concavity before asking whether an integrated correlation object has comparable structure. Positive definiteness of the entire associated-kernel hierarchy is already an all-real-zero characterization and should be stated once, not counted as progress through repeated finite checks. Any candidate beyond the classical results must be classified as a reformulation, an independently proved partial bound, or a hypothesis awaiting proof.

The probability and orthogonal-polynomial papers are secondary tools if their particular transforms become useful. No auxiliary-flow extension, global positivity claim, new numerical task, or manuscript is selected by this opening note. Its contribution is a precise starting account of what the primitive has already accomplished and which additional structures made those accomplishments possible.
