# MC09-B01: Hermitian source kernel and a matched-Gram obstruction

3 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance; actual recorded **gpt-6-astra (Codex), reasoning
effort max**, chat `01a1a43c-e3ab-7f73-9373-d130d40c1068`, turn
`01a1a447-c6e4-7d40-9b2c-8b5eb421cd46`.

**Disposition: MC09-B01 is complete as a bounded conceptual assessment.**
The conjugate-kernel candidate admits an exact positive Hermitian kernel
that retains the original states' Hilbert metrics. Nevertheless, kernel
positivity and those separate Gram matrices do not bound the neighboring
overlap ratio: an explicit finite-dimensional preparation control keeps the
complete theta source, every moment orbital, the ground-state orbital and
the entire three-orbital derivative Gram matrix, while attaining any
prescribed positive ratio. It changes the derivative preparations, which
is precisely the omitted premise. This is a scoped information obstruction,
not a counterexample to the original theta inequality.

The alternative common-contour index shift reproduces the parent's known
signed two-copy residual. Neither bounded candidate supplies a new signed
estimate. The results below are **proved in-note with proof-author checking
only**; separate MC09-E01 assessment is ready and unstarted. No numerical
theta acquisition, new comparison domain or RH result is claimed.

| Next task | Type and recommendation | Readiness | Deliverable |
| --- | --- | --- | --- |
| MC09-E01 | E — Sol; the formulas and proof obligations are fixed | Ready under the [frozen request r1](../research-progress/handoffs/01_MC09_E01_REVIEW_AND_MODEL_CONTINUATION_20261103.md) | Check the compact kernel, matched-Gram construction, limit qualification and control scope; accept, correct or identify a precise gap. |

Read with the [plan](../research-overview/01_SOURCE_OVERLAP_KERNELS_RESEARCH_OVERVIEW_20261103.md),
[live register](../research-progress/01_SOURCE_OVERLAP_KERNELS_RESEARCH_PROGRESS_20261103.md),
[result index][results], especially [theta identities][theta] and
[collision controls][controls], and [avoid index][avoid], especially
[reformulations][reformulation], [re-realizations][rerealization],
[joint estimates][joint] and [scoped exclusions][scope].

## 1. Fixed source, candidates and claim classification

Use the complete theta source at heat time zero and the established states
\[
c_j=\frac1{(2j)!}\int_0^\infty u^{2j}\Phi(u)\,du,
\quad f_i=\frac{\Phi^{(2i)}}{\sqrt\Phi},
\quad g_j=\frac{u^{2j}\sqrt\Phi}{(2j)!},\qquad c_j=0\ (j<0).
\tag{1}
\]
Their finite-index Hilbert membership, complete-source endpoint payments
and pairing \(\langle f_i,g_j\rangle=c_{j-i}\) retain the
[MC02 review's][mc02review] internal-review scope. Inner products are
conjugate-linear in the first slot; the source orbitals used here are real.
The original consumer is
\[
\eta_k=\frac{D_{3,k-1}D_{3,k+1}}{D_{3,k}^{\,2}}
\le\frac{k}{k+3},\qquad
D_{3,\ell}=\det[c_{\ell+b-a}]_{a,b=0}^2,\quad k\ge1.
\tag{2}
\]
The positive order-three denominator is inherited, not inferred from a
kernel. The all-minor destination remains the existing RH reformulation;
the order-three comparison is a stronger quantitative method pilot with
an unproved bound.

Exactly two candidates were compared:

| Candidate | Assessment |
| --- | --- |
| Conjugate-contour comparison preserving the original state norms | **Selected for full assessment.** Sections 2–4 construct the metric-preserving kernel and prove what its positivity plus separate Gram information cannot supply. |
| Joint neighboring-index comparison on common contours | Section 5 derives the exact joint residual. With no additional source differential estimate, it is the existing parent two-copy obligation; no second mechanism is developed. |

The first result is an exact representation. The matched-Gram theorem is
a scoped exclusion of a specified information class. The kernel-limit
result excludes only a pointwise halfline limit of the specified bare
kernel. None is a new sign criterion or a claim that all kernel methods
fail. The [MC03 saddle return][mc03] and [MC05 source-heat return][mc05]
were consulted to avoid duplicating their different open obligations.

## 2. A positive kernel that preserves both actual metrics

The unweighted bilinear kernel of [Note09][note09] reconstructs
\(a_i=\Phi^{(2i)}\) and \(b_j=z^{2j}/(2j)!\). Its unweighted Hermitian
version would compute the norms of a_i and b_j, not the norms of f_i and
g_j. To retain the latter, put
\[
d_j(z)=\Phi(z)b_j(z),\qquad
\mathcal Q_R(z,w)=\int_0^R
\frac{du}{\Phi(u)(\bar z-u)(w-u)}.
\tag{3}
\]
Only the real positive source occurs in the denominator. Both a_i and d_j
are holomorphic in the established strip \(|\operatorname{Im}z|<\pi/8\).
No complex square-root branch or global zero-free claim is needed.

Let \(\gamma:[0,1]\to\mathbb C\) parameterize a positively oriented,
piecewise C1 simple contour enclosing [0,R], with its filled closure in
that strip and distance d>0 from the segment. For boundary data A define
\[
(T_RA)(u)=\frac1{\sqrt{\Phi(u)}}\int_0^1
\frac{\gamma'(s)A(s)}{2\pi i(\gamma(s)-u)}\,ds.
\tag{4}
\]
For fixed R this is a bounded map from parameter-space L2 into L2(0,R):
\(\min_{[0,R]}\Phi>0\), the contour is separated, and its piecewise
derivative is bounded. Cauchy's formula, [DLMF 1.9.30][cauchy], gives
\[
T_R(a_i\circ\gamma)=f_i|_{[0,R]},\qquad
T_R(d_j\circ\gamma)=g_j|_{[0,R]}.
\tag{5}
\]
The exact parameter-space Gram kernel is
\[
\mathcal K_R(t,s)=
\frac{\overline{\gamma'(t)}\gamma'(s)}{4\pi^2}
\mathcal Q_R(\gamma(t),\gamma(s)).
\tag{6}
\]
Indeed, expanding (4) gives
\[
\langle T_RA,T_RB\rangle
=\int_0^1\!\int_0^1\overline{A(t)}\mathcal K_R(t,s)B(s)\,dt\,ds.
\tag{7}
\]
The conjugation of 1/i supplies the positive factor 1/(4 pi squared).
Both integrations remain independent. For any finite points z_j off the
segment and complex coefficients v_j,
\[
\sum_{j,l}\bar v_j\mathcal Q_R(z_j,z_l)v_l
=\int_0^R\frac1{\Phi(u)}
\left|\sum_l\frac{v_l}{z_l-u}\right|^2du\ge0.
\tag{8}
\]
The same calculation proves positivity of the integral operator (6).
All interchanges are compact: for example
\(|\mathcal Q_R(z,w)|\le R/(m_Rd_zd_w)\), with
\(m_R=\min_{[0,R]}\Phi\).

Equations (5)–(7) give the original truncated f-Gram matrix, g-Gram matrix
and mixed overlaps simultaneously. Their exterior powers therefore retain
the original wedge normalization. In particular the normalized mixed
overlap is still its determinant divided by the square root of the two
Gram determinants, when nonzero. Positive semidefiniteness in (8) signs
quadratic forms of one boundary vector; it does not sign a mixed matrix
element of two different vectors.

This is a source-dependent kernel, but its positivity uses only
\(\Phi(u)>0\), not the canonical derivative-preparation relation. The next
section tests whether retaining the *actual* separate Gram data repairs
that loss.

## 3. Matched-Gram theorem on the unchanged theta source

**Theorem (fixed k, separate-Gram information only).** For every integer
k>=1 and every prescribed L>0 there exist three real orbitals
\(h_0,h_1,h_2\) such that:

1. \(h_0=f_0=g_0\) and
   \(\langle h_i,h_j\rangle=\langle f_i,f_j\rangle\) for 0<=i,j<=2;
2. every g_j, the complete theta source and the kernel (3) are unchanged;
3. each h_i is \(\sqrt\Phi\) times a polynomial in u squared, so its
   numerator \(\sqrt\Phi h_i\) has the same strip analyticity required
   in (4)–(5);
4. the three consecutive mixed wedge overlaps
   \(\widetilde D_{\ell}=\det[\langle h_i,g_{\ell+b}\rangle]_{i,b=0}^2\),
   for ell=k-1,k,k+1, are strictly positive and satisfy
\[
\frac{\widetilde D_{k-1}\widetilde D_{k+1}}
{\widetilde D_k^{\,2}}=L.
\tag{9}
\]
The orbitals can all be chosen in
\[
\operatorname{span}\{g_0,g_{k-1},g_k,\ldots,g_{k+5}\},
\tag{10}
\]
a space of dimension at most eight. The state is one decomposable Slater
wedge, not a mixture of many-particle states.

### 3.1 Prescribe three minors without altering the first orbital

Write \(j_s=k-1+s\), \(\alpha_s=c_{j_s}>0\), s=0,...,4. These are the
unchanged first-row overlaps \(\langle g_0,g_{j_s}\rangle\). Set
\[
\varepsilon=\sqrt{\alpha_0/L}>0,\qquad
\beta=\frac{\alpha_3-\varepsilon}{\alpha_1},\qquad
\chi=\frac{1+\alpha_4\beta}{\alpha_3}.
\tag{11}
\]
For a positive scale lambda to be selected, prescribe the cross matrix
\[
\mathsf B_\lambda=
\begin{pmatrix}
\alpha_0&\alpha_1&\alpha_2&\alpha_3&\alpha_4\\
0&\lambda&0&\lambda\beta&\lambda\chi\\
0&0&\lambda&0&0
\end{pmatrix}.
\tag{12}
\]
Direct determinant expansion gives its three consecutive 3x3 minors:
\[
\lambda^2\alpha_0,\qquad
\lambda^2(\alpha_3-\alpha_1\beta)=\lambda^2\varepsilon,
\qquad
\lambda^2(\alpha_3\chi-\alpha_4\beta)=\lambda^2.
\tag{13}
\]
Their quotient is \(\alpha_0/\varepsilon^2=L\). No coefficient of the
actual theta source has been sampled or changed.

### 3.2 Realize the cross matrix with the exact derivative Gram matrix

Let
\(W=\operatorname{span}\{g_0,g_{j_0},\ldots,g_{j_4}\}\), discarding a
duplicate g_0 when k=1. Distinct moment orbitals are linearly independent:
a linear relation divided by the positive sqrt(Phi) is a polynomial
vanishing on an interval. Thus their finite Gram matrix is positive
definite. Its inverse constructs p_1,p_2 in W with
\[
\langle p_i,g_0\rangle=0,
\quad
(\langle p_1,g_{j_s}\rangle)_{s=0}^4=(0,1,0,\beta,\chi),
\quad
(\langle p_2,g_{j_s}\rangle)_{s=0}^4=(0,0,1,0,0).
\tag{14}
\]
For k=1 the first zero entry is exactly the duplicated g_0 constraint,
so there is no incompatibility. For k>1 it is an extra allowed zero.

Put \(\mathsf P=(\langle p_i,p_j\rangle)_{i,j=1}^2\) and
\(\mathsf S=(\langle f_i,f_j\rangle)_{i,j=1}^2\). The latter is
positive definite: pairing a hypothetical linear relation between f_1
and f_2 first with g_1, then with g_2, gives successive coefficients zero
because the relevant entries are c_0,0,c_0. Also
\(\langle f_0,f_i\rangle=\langle f_i,g_0\rangle=0\) for i=1,2.

Choose, for example,
\[
\lambda^2=\frac{\lambda_{\min}(\mathsf S)}
{2(1+\|\mathsf P\|_{\mathrm{op}})},\qquad
\mathsf C=\mathsf S-\lambda^2\mathsf P>0.
\tag{15}
\]
This is legitimate finite positive-matrix information, independent of the
unknown sign in (2). The inequality follows from
\(\lambda^2\mathsf P\preceq\lambda_{\min}(\mathsf S)I/2\).

Project g_{k+4}, g_{k+5} off W and orthonormalize their residuals. They
are independent modulo W by the same polynomial argument. This gives
real e_1,e_2 in W-perp, still finite linear combinations of moment
orbitals. Define
\[
h_0=g_0,\qquad
h_i=\lambda p_i+\sum_{l=1}^2(\mathsf C^{1/2})_{il}e_l,
\quad i=1,2.
\tag{16}
\]
The cross matrix with the five prescribed moment orbitals is (12).
Orthogonality gives
\(\operatorname{Gram}(h_1,h_2)=\lambda^2\mathsf P+\mathsf C=\mathsf S\),
and h_0 is orthogonal to h_1,h_2 just as f_0 is to f_1,f_2. Consequently
the entire 3x3 derivative Gram matrix and the wedge norm are matched
exactly. This proves (9)–(10).

### 3.3 Scope of the obstruction and the unpaid information

Choose L>k/(k+3). All three mixed amplitudes are positive and every
separate normalization factor is exactly that of the original states,
yet the desired ratio bound fails for these preparations. Even fixing
the complete source inside a positive kernel and fixing its separate
state Gram matrices is therefore insufficient for that bound.

**The failed canonical premise is the derivative preparation**, not the
theta source. Writing h_i=sqrt(Phi) P_i, the P_i here are polynomials in
u squared. The actual derivative ratio satisfies
\[
\frac{\Phi''(u)}{\Phi(u)}\sim16\pi^2e^{8u}\qquad(u\to\infty),
\tag{17}
\]
so h_1 cannot be f_1. To see (17), differentiate the first source term
twice: its leading multiplier is \(16(\pi e^{4u})^2\); the lower powers
are smaller and the remaining n>=2 source terms and their fixed
derivatives are exponentially smaller in \(\pi e^{4u}\). No spatial
cutoff replaces the full source in the theorem.

The controls do **not** preserve the entire Toeplitz cross-pairing, the
k=0 triangular determinant anchor, the differential ladder
\[
(\Phi P_i)''=\Phi P_{i+1},\quad P_0=1,
\tag{18}
\]
or all finite-R derivative Gram matrices. They do preserve the actual
full-halfline 3x3 derivative Gram matrix. Thus the theorem does not
exclude an argument that uses (18), the missing cross data, an additional
anchor restriction or the detailed R-dependent source information.
It is not a negative original-theta determinant or a collision control.

A useful way to locate the lost information is to project the original
f_i onto W. If \(\mathsf G\) is the moment Gram matrix of a basis of W
and \(\mathsf B\) its cross matrix with f_i, then
\[
\operatorname{Gram}(P_Wf_i)=\mathsf B\mathsf G^{-1}\mathsf B^T,
\qquad
\operatorname{Gram}(f_i)-\mathsf B\mathsf G^{-1}\mathsf B^T\succeq0.
\tag{19}
\]
The constructed controls satisfy precisely this metric constraint. The
original cross entries are fixed instead by (18) and its endpoint
payments. Substituting the already known entries c_{j-i} into (19)
does not create a bound for their minor ratio. The selected kernel has
supplied no additional quantitative restriction on that differential
subclass. This is where the selected attempt stops.

## 4. The bare inverse-source kernel has no finite halfline limit

For this specific metric-preserving choice, a second limit warning can be
proved explicitly. Define the finite constant
\[
C_\Phi=2\pi^2\sum_{n\ge1}n^4e^{-\pi(n^2-1)}.
\]
The complete source on u>=0 satisfies
\[
0<\Phi(u)\le C_\Phi e^{9u}e^{-\pi e^{4u}},
\tag{20}
\]
by omitting its negative summand and factoring the n=1 exponential from
the positive sum. For any fixed z off the nonnegative real axis and R>=1,
the contribution of u in [R-1,R] gives
\[
\mathcal Q_R(z,z)\ge
\frac{\exp\{\pi e^{4(R-1)}-9R\}}
{C_\Phi(R+|z|)^2}\longrightarrow+\infty.
\tag{21}
\]
Thus this bare kernel has no finite pointwise halfline limit. This excludes
neither another weighted reconstruction nor finite-R estimates retaining
the complete source factors. In fact the original mixed overlaps and
both original Gram matrices converge as R tends to infinity by the
inherited finite-index Hilbert membership and Cauchy–Schwarz. Their
convergence occurs *after* reconstruction; it does not permit exchanging
the limit with the separated positive kernel. No uniformity in k or
particle number is claimed.

## 5. Alternative candidate: the exact common-contour residual

Keep the original bilinear kernel H_R from Note09, with two independent
contours. For r=3 define the finite complex measure
\[
d\mu_R=\frac1{(3!)^2}\mathcal A_{(0,1,2)}(\mathbf z)
\det[\mathcal H_R(z_c,w_d)]V(\mathbf w^2)
\prod_c\frac{dz_c}{2\pi i}\prod_d\frac{dw_d}{2\pi i},
\quad q(\mathbf w)=\prod_{d=1}^3w_d^2.
\tag{22}
\]
All factors are on compact contours, so product integration and finite
algebra are legitimate. For integer ell>=0,
\[
U_\ell^R:=\int q^\ell\,d\mu_R
=F_{3,\ell}\det[M^R_{i,\ell+j}]_{i,j=0}^2,
\quad F_{3,\ell}=(2\ell)!(2\ell+2)!(2\ell+4)!.
\tag{23}
\]
This follows by factoring \(q^\ell/F_{3,\ell}\) from the moment
determinant; its remaining determinant is V(w squared), with the
original row/column convention. Symmetrizing the product of two copies
gives, without any division,
\[
U_{k-1}^RU_{k+1}^R-(U_k^R)^2
=\frac12\iint(qq')^{k-1}(q-q')^2\,d\mu_R\,d\mu_R',\quad k\ge1.
\tag{24}
\]
This is an exact signed residual, not a positive-variance formula. Both
the measure and q are complex on these contours. Reconstructing onto the
real variables recovers the parent's already known signed two-copy
formula; the negative source insertion is still present there.

At fixed indices, use equality with the original real integrals and keep
the finite-R endpoint terms before taking the limit. Then
\(U_\ell^R\to F_{3,\ell}D_{3,\ell}\). The exact factorial budget is
\[
B_{3,k}=\frac{F_{3,k-1}F_{3,k+1}}{F_{3,k}^2}
=\frac{(2k+6)(2k+5)}{2k(2k-1)}.
\]
Consequently (2) asks for
\[
\frac{U_{k-1}U_{k+1}}{U_k^2}\le
\frac{2k+5}{2k-1},
\tag{25}
\]
exactly the [parent Gaussian comparison][parent], not a new estimate.
Common contours and the index shift alone supply no additional
source-sensitive premise. This limited alternative is not selected for
further work; the calculation does not exclude a new differential
estimate of (24).

## 6. Claim-specific control screen

This is an analytical premise screen, not a rerun of collision numerics.
The four source families below are as defined and qualified in the
[control summary][controls]. Their time-zero order-three ratios are not
evaluated here, and a positive-time collision is not used as a witness
against (2).

| Control | Kernel premises and actual missing information |
| --- | --- |
| Matched-Gram preparations, Section 3 | Same complete theta source, moment family, ground state and full three-orbital Gram matrix; same analytic reconstruction and positive kernel. Fails canonical derivative preparation (18), full cross-pairing and generally the triangular anchor. This directly refutes a ratio bound from the retained information alone. |
| Euler-factor sources | Positive even real translates retain a common analytic strip, so the compact construction and positive kernel apply with that source's own weight and states. Canonical arithmetic/source identity fails. Kernel positivity excludes none of them; no quantitative ratio sign is inferred. |
| Weighted-square endpoint controls | Positive finite square sums are holomorphic and positive on [0,R], so compact reconstruction/positivity applies. Full canonical weights and full reflection fail. Any unmatched odd endpoint survives in an attempted halfline Toeplitz pairing; the first or first two matched endpoints do not pay every needed order. |
| Reflected super-Gaussian control | The cited source is positive and entire, so the compact kernel construction applies. Its source is not canonical theta. Evenness and Gram positivity provide no derivative-to-moment ratio estimate; none is tested here. |
| Smooth shape / positive-primitive controls | Positivity gives the real weighted Gram form. A holomorphic neighborhood for the specified smooth construction is not established by the cited shape/primitive properties, so its contour application is left unestablished. Literal canonical reconstruction fails; no ratio sign is assigned. |
| Gaussian source | Checks generic reconstruction and the already known equality in the Gaussian ratio comparison. It does not distinguish theta. The matched-Gram construction also shows why this equality cannot be deduced for arbitrary alternative preparations on that source. |

The important distinction is between putting theta into a kernel and
using its derivative-preparation identity quantitatively. The new
preparation control keeps theta itself; failure of a control to have
theta's arithmetic is therefore not the explanation for this obstruction.

## 7. Verification, boundaries and disposition

The proof-author checks are direct Cauchy reconstruction with conjugations,
the three universal minors in (13), the Gram completion (14)–(16), the
k=1 duplicate constraint, the positive lower bound (21), and the
factorials and two-copy algebra (23)–(25). The small
[exact algebra program](../numerics/mc09_b01_exact_algebra.py) and
[record](../numerics/MC09_B01_EXACT_ALGEBRA_20261103.json) check polynomial
identities only. They compute no theta coefficient, Gram eigenvalue,
contour quadrature, collision or comparison range. The universal theorem
rests on the written proof, not on a finite sample or assertion count.

All constructed orbitals are in L2 by complete-source decay and polynomial
growth. All original f_i have the inherited finite-index L2 justification.
The compact formula uses no endpoint integration by parts. Original
halfline Toeplitz claims retain all upper endpoint terms until the fixed-
index limit and use complete evenness at zero. The relaxed h_i do not
inherit those derivative identities. Singular source tails are never
discarded from a contour limit.

The only refreshed external passage is [Cauchy's formula][cauchy] with
its simple-contour/analyticity hypotheses, inspected on 3 November 2026;
the existing [source record05][source05] owns the reference provenance.
No new source theorem or claim about the unpublished quaternion draft is
imported. Input hashes and the return hash are recorded in the E01 packet;
they identify bytes and do not certify the mathematics.

**Decision:** park the selected *positive-kernel plus separate-Gram*
comparison after its separate assessment. The broader source-kernel
investigation remains open. MC09-B02 is not ready merely because the
kernel is positive: a continuation must supply an explicit estimate using
(18) or another specified source-preparation relation that is absent from
the control. The common-contour residual alone does not meet that gate.
No numerical E02 task is indicated by this return.

**Next: [E] MC09-E01 — Sol**, under the fixed review and model-continuation
packet. If accepted, MC09-E03 can integrate this scoped stop. Any new
mechanism needs a visible B revision; this return neither selects a third
candidate nor starts an unbounded search.

[results]: ../../../../../../../result-summaries/README.md
[theta]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[reformulation]: ../../../../../../../avoid/01_restating_the_target.md
[rerealization]: ../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[joint]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[scope]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[mc02review]: ../../02_fermionic_correlators/reviews/01_MC02_E01_SEPARATE_REVIEW_20261101.md
[note09]: ../../08_open_quantum_dynamics/brainstorm/notes/09_SEPARATED_CONTOUR_KERNEL_FOR_SOURCE_OVERLAPS_20261103.md
[parent]: ../../notes/01_INITIAL_BRANCH_EVALUATION_20261101.md
[mc03]: ../../03_connected_mellin_response/notes/01_COMPLETE_MELLIN_RESPONSE_RETURN_20261101.md
[mc05]: ../../05_schur_toda_structure/notes/01_THETA_SCHUR_CONSTRAINT_RETURN_20261101.md
[cauchy]: https://dlmf.nist.gov/1.9.E30
[source05]: ../../08_open_quantum_dynamics/references/05_SOURCE_KERNEL_DRAFT_AND_CAUCHY_20261103.md
