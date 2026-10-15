---
research_program: PR02-CORR
parent_program: PR02
secondary_programs: [ALG, PR02]
status: positive_auxiliary_transform_exact_source_identity_pointwise_sign_open
---

# A positive theta primitive and the remaining signed cancellation

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from current-session metadata.

A complete theta primitive has a strictly positive cosine transform throughout the investigation's heat interval. An exact differential identity recovers the physical theta field while retaining its lower-boundary constant. This gives a concrete positive auxiliary channel, but its algebraic spectral size differs from the physical energy scale. A separate theorem excludes exact finite rational-coefficient jet closure on an open spectral interval. These are analytic results within the source-certificate program of [Note 47](../04_octonionic_reductions/47_ORIENTED_CURRENT_AND_ACCRETIVE_SOURCE_CERTIFICATES_20261015.md), with the signed-form interpretation of [Note 50](../04_octonionic_reductions/50_QUATERNION_FORMS_HODGE_PAIRING_AND_SOURCE_TARGET_20261015.md). No literature novelty claim is made for the elementary transform and operator methods.

Use the complete source and normalization of Notes 12, 46 and 47:
\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},
\qquad H(t,x)=\int_0^\infty e^{tu^2}\Phi(u)\cos(xu)\,du.
\]
The complete source extends evenly to the real line. The following statements use all theta indices and no numerical experiment.

## 1. A complete auxiliary primitive with its boundary term retained

Let \(\vartheta(r)=\sum_{n\in\mathbb Z}e^{-\pi n^2r}\), and define on \(u\ge0\)
\[
P(u)=e^u\vartheta(e^{4u}),\qquad
\psi(u)=e^u\sum_{n\ge1}e^{-\pi n^2e^{4u}},\qquad P=e^u+2\psi.
\]
Theta modularity makes \(P\) even. Direct differentiation gives
\[
\Phi=\frac{P''-P}{16}=\frac{\psi''-\psi}{8},
\qquad \psi'(0)=-\tfrac12.
\tag{1}
\]
The last equality follows from \(P'(0)=0\). Define the convergent complete-index channel
\[
J(t,x)=\int_0^\infty e^{tu^2}\psi(u)\cos(xu)\,du.
\]
It is entire in \(x\) and exists for every finite real \(t\). Two integrations by parts, with \(F(u)=e^{tu^2}\cos(xu)\), yield
\[
8H=-\psi'(0)F(0)+\psi(0)F'(0)+\int_0^\infty\psi(F''-F)\,du.
\]
Here \(F'(0)=0\), and all upper boundary terms vanish. Consequently
\[
\boxed{8H=\tfrac12+(2t-x^2-1)J+4txJ_x-4t^2J_{xx}.}
\tag{2}
\]
The constant \(1/2\) is essential. Using the modular-even \(P\) directly in a positive-time cosine integral would be invalid: \(P(u)\sim e^u\), so \(e^{tu^2}P(u)\) is not integrable. Equation (2) uses the decaying half-line primitive \(\psi\), preserving the missing modular boundary contribution explicitly. It supplies an additional channel, not a finite closure in the original jets.

Equivalently, for \(D_t=2t\partial_x-x\),
\[
8H=\tfrac12-(D_t^2+1)J.
\tag{3}
\]
For \(t>0\), \(D_t\) is skew-adjoint on its natural domain in \(L^2(e^{-x^2/(2t)}dx)\). Gaussian conjugation sends it to \(2t\partial_x\), so \(-D_t^2-1\) becomes the shifted free Laplacian \(-4t^2\partial_x^2-1\). Its quadratic form takes both signs and its lower spectral edge is \(-1\); factorization does not establish the required nonnegative sign.

## 2. Strict positivity and the scale of the auxiliary channel

There is a genuine positivity statement for this channel. For \(0\le t\le1/2\), set
\[
f_n(u)=e^{tu^2+u-q_n(u)},\qquad q_n(u)=\pi n^2e^{4u}.
\]
Since \(2tu+1\le u+1\le q_n\),
\[
\frac{f_n''}{f_n}
=(2tu+1-4q_n)^2+2t-16q_n
\ge9q_n^2-16q_n>0.
\]
Thus \(f=e^{tu^2}\psi=\sum f_n\) is strictly convex. Its derivative satisfies \(f'(0)=-1/2\), \(f'(\infty)=0\). For \(x\ne0\), two further integrations by parts give
\[
\boxed{J(t,x)=\frac1{x^2}\int_0^\infty f''(u)\{1-\cos(xu)\}\,du>0.}
\tag{4}
\]
At \(x=0\), strict positivity follows from the defining integral. All differentiated sums and integrals converge by the same complete-source decay.

Evenness of \(P\) also gives \(\psi^{(2k+1)}(0)=-1/2\). Thus \(f'''(0)=-(1+6t)/2\), and repeated integration by parts gives, uniformly for \(0\le t\le T<\infty\),
\[
J(t,x)=\frac1{2x^2}-\frac{1+6t}{2x^4}+O_T(x^{-6}).
\tag{5}
\]
The remainder follows from the uniformly bounded endpoint value \(f^{(5)}(0)\) and uniformly integrable sixth source derivative. The physical theta jets instead have exponential spectral decay from the complete-source strip shift. Hence separate \(J\)-norms cannot be paid by \(E\) with a uniform or polynomial-in-height budget. This high-height statement does not exclude coefficients that are merely locally bounded at every finite point.

This positive auxiliary channel does not inherit the vanishing of \(E\). At any hypothetical real collision in this time range, \(J\) would still be strictly positive, so a locally bounded estimate \(J^2\le C E\) would fail there. Also (2) contains derivatives of \(J\) with signs; positivity of \(J\) does not establish the desired Laguerre inequality. Any continuation through this channel must retain the complete differentiated operator in (2) and its signed products with the full physical jets. Paying separate auxiliary norms would discard the required cancellation. No energy-relative signed inequality for those products has been proved here.

## 3. No exact rational finite-jet closure

**Proposition.** Fix any real heat time \(t\). There are no rational functions \(r_0(x),\ldots,r_m(x)\), not all zero, such that
\[
\sum_{k=0}^m r_k(x)h_k(t,x)=0
\tag{6}
\]
on a nonempty open real interval free of their poles.

**Proof.** Write \(w_t(u)=e^{tu^2}\Phi(u)\). The first source index dominates as \(u\to+\infty\):
\[
\Phi(u)=2\pi^2e^{9u-\pi e^{4u}}\{1+O(e^{-4u})\}.
\]
For every fixed nonnegative integer \(k\), direct differentiation of the source series gives
\[
\frac{w_t^{(k)}(u)}{w_t(u)}
=(-4\pi)^k e^{4ku}\{1+o(1)\}.
\tag{7}
\]
Indeed the leading contribution differentiates the factor \(e^{-\pi e^{4u}}\) once at each step. Derivatives of \(e^{tu^2+9u}\), and subsequent derivatives of the resulting factors, are lower order. For each fixed differentiation order the \(n\ge2\) terms remain exponentially smaller in \(e^{4u}\), even after their polynomial factors are included.

Suppose a nonzero polynomial-coefficient differential operator annihilated \(w_t\). Choose its largest derivative order \(M\), with coefficient \(p_M\ne0\), and divide its equation by \(p_M(u)w_t(u)e^{4Mu}\). By (7) its highest term tends to \((-4\pi)^M\), whereas every lower term tends to zero: a rational function of \(u\) cannot compensate for \(e^{-4(M-k)u}\). This is impossible.

Now clear denominators in (6). Since the theta jets are entire, the resulting polynomial-coefficient identity extends from the interval to all real \(x\). The complete even density satisfies
\[
H(t,x)=\tfrac12\int_{\mathbb R}w_t(u)e^{ixu}\,du.
\]
It and all its derivatives are rapidly decreasing. Fourier conjugation sends \(x\) to \(i\partial_u\) and \(\partial_x\) to \(iu\), with the order of composed factors respected. This is an invertible map on polynomial differential operators. Fourier injectivity therefore converts the nonzero operator annihilating \(H\) into a nonzero polynomial differential operator annihilating \(w_t\), contradicting the preceding paragraph. This proves the proposition.

Unlike Note 22's compact-filter obstruction, this applies to the untruncated complete theta field itself. In particular, Note 47's exact identities \(-h_2=a_0h_0+b_0h_1\) and \(-h_3=a_1h_0+b_1h_1+c_1h_2\) cannot hold on an open spectral interval if their coefficients are rational in \(x\). This statement does **not** exclude identities imposed only on the stationary locus, nonzero signed residuals, transcendental coefficients, or infinite/nonlocal theta relations. It also does not exclude inequalities. The result prevents a particular exact closure; it is not an obstruction to the original signed estimate.


## 4. The next signed quantity

At time zero, (2) becomes exactly
\[
J(0,x)=\frac{1}{2(1+x^2)}-\frac{8H(0,x)}{1+x^2}.
\]
The physical field is encoded in the small difference between the positive auxiliary transform and an explicit rational profile. Strict positivity of that transform cannot determine the difference or its differentiated signed products. At positive time, the full operator in (2) performs the corresponding cancellation.

The positivity proof is a direct instance of the convex-kernel principle discussed in [Csordas, Theorem 3.4](https://arxiv.org/pdf/1309.0055). The even extension of the primitive source has a cusp at zero, with one-sided slope \(f'(0+)=-1/2\). It is different from the smooth even source \(\Phi\); positivity of its cosine transform should not be transferred to that of \(\Phi\). All formulas above were derived directly with this investigation's normalization.

A useful continuation must bound the signed products obtained by applying the complete operator (2) and its physical derivatives before estimation, or give a source-prescribed residual certificate beyond the rational exact class excluded in Section 3. Neither positivity of \(J\) nor its separate derivative norms supply the missing energy payment. [Note 53](53_SOURCE_CONCAVITY_AND_POSITIVE_TIME_COLLISION_CONTROL_20261015.md) also rules out a replacement argument using only positivity, concavity, and fast decay of a general source.

No numerical calculation, new pointwise sign domain, manuscript revision, snapshot, commit, or tag is part of this note.
