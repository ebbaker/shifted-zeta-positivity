# MC07-B03: bounded boundary Ward-identity feasibility return

2 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual author **gpt-6-astra / xhigh**, verified from this turn's recorded configuration. Analytical assessment and self-check by one assistant; no separate or specialist review.

**Disposition: stop this bounded route without a new Mellin estimate.** Two candidate identities were screened and one worked through the complete order-three response. The boundary Ward identity and its required coupling derivatives give an explicit signed flux determinant. Its two-copy Mellin integral remains uncontrolled in sign relative to the Gaussian budget. No interval, including the first required interval [0,2], has been gained. This is a failure to acquire an estimate from the selected identities, not an impossibility theorem for gauge theory.

The author explicitly requested this follow-up. The [scope record](../numerics/MC07_B03_SCOPE_RECORD_20261102.json) retains the two-identity/one-route limit. The theory, magnetic sector, source and comparison are exactly those of [Return02, Sections 3–7](02_POINT_INSERTIONS_AND_VAFA_WITTEN_ANOMALY_RETURN_20261101.md). No numerical implementation or further candidate was launched. Classification under [avoid/01](../../../../../../../avoid/01_restating_the_target.md): a bounded information-sufficiency assessment; the formulas below identify the surviving target, not a new criterion or estimate. Use the [result index](../../../../../../../result-summaries/README.md), [theta cluster](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [avoid index](../../../../../../../avoid/README.md) and [scoped-exclusion rule](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## 1. Two candidates and the selection

| Candidate | Potential use | Decision |
| --- | --- | --- |
| Boundary supercurrent Ward identity, DPW PDF (4.32) / HTML (77), evaluated in PDF (4.37)–(4.38) / HTML (82)–(83) | Transfer the complete source derivatives to a boundary expression, retaining a possible sign-bearing insertion | Selected and worked below. |
| Stress-tensor / graded-trace response, DPW PDF (4.21) and the first equality of (4.32) / HTML (66),(77) | Seek a positive energy-covariance interpretation of coupling derivatives | Screened: the published trace includes fermion parity; its supercurrent insertion is not a positive density. The physical identity therefore does not authorize ordinary thermal-variance positivity. |

These are two aspects of the same source framework, not independent evidence. No additional heat equation, theory or altered observable was introduced. The second screen does not assert that every supertrace expectation is negative; it identifies the absent positivity premise for the proposed argument. Even the positive extracted flux measure, used below, leaves a signed determinant.

Primary source: [Dabholkar–Putrov–Witten, arXiv:2004.14387v3](https://arxiv.org/html/2004.14387v3), Sections 4.3–4.4, selected passages only. Its normalization and orientation limitations remain those of Return02. The explicit mathematical completion fixes our conventions. A further inspection receipt is in the [existing source record](../../../../references/10_VAFA_WITTEN_RH_LITERATURE_SOURCES_20261102.md).

## 2. Keep the whole boundary normalization

Write y=Im(tau), take tau=i beta/2 only after the antiholomorphic derivative, and set

\[
 U(\beta)=\left.\langle\bar G\rangle_{\mathcal Y}\right|_{\tau=i\beta/2},
 \qquad
 C(\tau)=-\frac{e^{\pi i/4}}{\sqrt{8y}\eta(\tau)},
 \qquad
 N(\beta)=\frac{16\pi i}{3}y^{3/2}\eta(\tau)^3.
\]

DPW's identity is \(\partial_{\bar\tau}Z=C\langle\bar G\rangle_{\mathcal Y}\). Thus, putting \(K=NC\), the selected response is

\[
 \mathcal A(\beta)=K(\beta)U(\beta)=\Theta(\beta).
 \tag{1}
\]

The checked boundary evaluation is

\[
 U(\beta)=\frac{-3i e^{3\pi i/4}}{4\pi\sqrt2\,y\eta(\tau)^2}
 \sum_{n\in\mathbb Z}e^{-\pi\beta n^2}.
 \tag{2}
\]

Multiplication by K cancels the phases and factors exactly. This also retains the zero flux. The boundary calculation concerns a noncompact target, so setting the Q-exact insertion to zero would discard the contribution being computed. The Wess–Zumino three-form integral, DPW PDF (4.36) / HTML (81), is the fixed factor 12 pi² already absorbed here; it is distinct from our signed insertion h3.

Let \(D=\beta\partial_\beta\), \(\beta=e^{4x}\), and \(F_i(x)=\Phi^{(2i)}(x)\) for i=0,1,2. Applying the *entire* source operator of Return02 gives

\[
 F_i(x)=16^i\beta^{1/4}
 (D+\tfrac14)^{2i}(D^2+\tfrac12D)[K(\beta)U(\beta)].
 \tag{3}
\]

Indeed \(\partial_x=4D\), \(\beta^2\partial_\beta^2+\tfrac32\beta\partial_\beta=D^2+\tfrac12D\), and \(D\beta^{1/4}=\beta^{1/4}(D+1/4)\) as an operator identity. Equation (3) reaches six coupling derivatives for i=2. Differentiating U alone would miss derivatives of K. Working with the completed function (1) includes all these terms without assuming an unevaluated multi-insertion path integral has no contact terms. We differentiate the explicit completed function; we do not prove interchange of derivatives with the unevaluated large-radius path-integral limit. No new local Ward identity for h3 is claimed.

## 3. The complete differentiated flux insertion

For \(t=\pi\beta n^2\), define polynomials by

\[
 P_0(t)=2t^2-3t,\qquad
 \mathcal L=t\partial_t+\tfrac14-t,\qquad
 P_{i+1}=\mathcal L^2P_i.
 \tag{4}
\]

Equation (3) becomes the exact convergent expression

\[
 F_i(x)=16^i\beta^{1/4}
 \sum_{n\ge1}P_i(\pi\beta n^2)e^{-\pi\beta n^2}.
 \tag{5}
\]

Both nonzero flux signs are included in P0's factor of two. The source operator kills the zero mode before this rewriting. For checking the recurrence,

\[
 \mathcal L^2t^k=t^{k+2}-(2k+\tfrac32)t^{k+1}
 +(k+\tfrac14)^2t^k,
\]
\[
 P_1(t)=2t^4-14t^3+\tfrac{165}{8}t^2-\tfrac{75}{16}t.
 \tag{6}
\]

An elementary exact check is \(P_0(4)=20>0\), while \(P_1(4)=-291/4<0\). This occurs for n=1 at the allowed coupling beta=4/pi>1. It disproves a termwise nonnegativity premise for these derivative insertions; it does **not** claim that one negative term decides the determinant or its integral. P2 is specified exactly by (4), with no fitted coefficients or truncation.

Write \(\Delta(\mathbf x)=\det[F_i(x_j)]_{i=0,1,2;\,j=1,2,3}\), \(\beta_j=e^{4x_j}\), and \(t_j=\pi\beta_jn_j^2\). Multilinearity gives

\[
 \Delta(\mathbf x)=16^3(\beta_1\beta_2\beta_3)^{1/4}
 \sum_{n_1,n_2,n_3\ge1}e^{-t_1-t_2-t_3}
 \det[P_i(t_j)]_{i=0,1,2;\,j=1,2,3}.
 \tag{7}
\]

All triples occur, including repeated flux integers. The three couplings are different external parameters; one cannot impose a flux ordering or replace this determinant by a determinant square. Positive Gaussian weights alone do not make (7) a positive Gram formula. At the inherited source level, \(\Delta=\prod_j\Phi(x_j)V(R(\mathbf x))h_3\), so the established negative region of h3 is retained exactly.

These manipulations are analytic. For beta>=1, each differentiated series is dominated by a polynomial in beta and n times exp(-pi beta n²). It converges uniformly on compact beta intervals. In x the upper tail is double-exponentially decaying. Near x=0 the source and its even derivatives are smooth and bounded. Consequently the determinant expansion, integrations and up to two sigma derivatives below are absolutely justified for sigma>=0, locally uniformly in sigma, with the logarithmic factors integrable at the lower endpoints.

## 4. Work the Ward response through the Mellin curvature

On \(\Omega=\{0<x_1<x_2<x_3\}\), define the full signed density

\[
 W_\sigma(\mathbf x)=\prod_jx_j^{2\sigma}
 V(\mathbf x^2)\Delta(\mathbf x),\qquad
 T(\mathbf x)=2\sum_j\log x_j,
 \qquad M(\sigma)=\int_\Omega W_\sigma.
 \tag{8}
\]

This is the unchanged M3, with the real-tilt positivity inherited from the [initial Mellin return](../../notes/01_INITIAL_BRANCH_EVALUATION_20261101.md) at its existing internal-review scope. Define \(I_k=\int_\Omega T^kW_\sigma\), k=0,1,2. Then M=I0, M'=I1, M''=I2, and (7) gives each Ik explicitly in terms of the full boundary flux response.

The surviving quantity is

\[
 \boxed{\begin{aligned}
 \mathscr R(\sigma)
 &=I_0I_2-I_1^2-\kappa_3(\sigma)I_0^2\\
 &=\int_{\Omega^2}W_\sigma(\mathbf x)W_\sigma(\mathbf y)
 \left[\tfrac12(T(\mathbf x)-T(\mathbf y))^2
       -\kappa_3(\sigma)\right]d\mathbf x\,d\mathbf y,
 \end{aligned}}\tag{9}
\]

where \(\kappa_3(\sigma)=\sum_{j=0}^2\sum_{\nu\ge0}(\sigma+j+1/2+\nu)^{-2}\). The desired bound is precisely \(\mathscr R(\sigma)\le0\). Equation (9) is an explicit surviving term, **not a newly acquired sufficient criterion**. Substitution of (7) retains every flux, determinant sign and coupling weight; no unspecified physical correlator has been substituted for the problem.

The carrier form identifies the same unpaid contribution. With the inherited positive probability measure mu_sigma, m=E T and A=E h3>0,

\[
 \frac{\mathscr R}{M^2}
 =\operatorname{Var}T-\kappa_3
 +\frac{E[(h_3-A)(T-m)^2]}{A}
 -\frac{E[h_3(T-m)]^2}{A^2}.
 \tag{10}
\]

The last term is nonpositive but was already present in Return02. The centered-square term has no sign supplied by the chosen Ward identity, and that identity also supplies no Gaussian upper bound on the carrier variance. No claim is made that the centered-square term must be positive or that the desired inequality fails.

Why the boundary identity stops here is precise. Q acts on the physical fields; sigma and the external coupling kernels are parameters. Multiplication by the Mellin weights and differentiation in sigma therefore do not create a new Q identity controlling their logarithms. Applying the selected identity in each factor only replaces the bulk response by the same boundary response in (3)–(7). The boundary term remains. The inspected identity and its finite coupling derivatives have supplied no inequality beyond the already known theta expression. Interpreting h3 itself as a new protected local insertion would require an additional dictionary and identity, neither present in the selected source nor derived here.

## 5. Control screen and disposition

This applies the [collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md) and [premise rule](../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md). It is an analytical premise check, not a numerical replay or a claim to exclude collisions.

| Control | Premise check |
| --- | --- |
| Weighted/finite square sources | Their differentiated Gaussian sums still satisfy the algebraic recurrence (4). They fail the unchanged infinite unit-weight anomaly (1)–(2). The recurrence or positivity of flux moments alone does not distinguish them. |
| Euler-factor controls | They change the full extracted source. No realization satisfying the unchanged anomaly is supplied; generic positivity/reflection would not suffice to reject them. |
| Reflected, smooth-shape and positive-primitive controls | They may retain selected shape, reflection or endpoint properties but fail the exact unit-weight square expansion. No physical exclusion beyond that premise is asserted. |
| Gaussian comparator | It does not satisfy the same CP2 anomaly. No Ward identity comparing its Mellin curvature with this theory's curvature has been obtained. |

The exact source premise distinguishes theta; the argument still provides no quantitative margin for theta. The source match is retained as useful background, with the literature attribution in [Review03](../reviews/03_VAFA_WITTEN_RH_LITERATURE_REVIEW_20261102.md).

**MC07-B03 completes with a surviving uncontrolled term, not a new bound. Park this specific boundary-Ward/trace-positivity route.** Reopening it would require a concrete additional identity or inequality applying to (9) or the full combination (10), with its domain and boundary/contact terms controlled. No E numerical contract is issued because this return supplies no usable numerical mechanism to implement. Other theories, new insertions or deformations require a new conceptual decision; none is launched by this conclusion. The broader Jensen and Mellin-curvature investigations remain open.

The [same-assistant self-check](../reviews/04_MC07_B03_BOUNDARY_WARD_SELF_CHECK_20261102.md) records the algebra, convergence, limitations and source scope. This note does not inherit the separate-review status of Return02.
