# Green fields and localized zero correlations: shared discussion and routing

7 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Root model/effort unavailable; the bounded conceptual check was tool-selected **gpt-6-astra/ultra**, hierarchy discovery and Green documentation **gpt-6.1-sol/ultra**. These selections are dispatch provenance, not independent backend verification.

**Evidence level: author-directed setup and discussion synthesis, not a new signed estimate.** This is not a chat transcript. [Request18](18_TND_O_E22_BIFURCATION_SETUP_REQUEST_20261107.md), [inputs40](../../research-progress/handoffs/40_TND_O_E22_BIFURCATION_INPUTS_20261107.json) and [return40](../../research-progress/handoffs/40_TND_O_E22_BIFURCATION_RETURN_20261107.json) bind this setup.

## 1. The author's priorities and the two homes

The author first requested an accessible mathematical explanation of the manuscript, then favored §18's Green method, proposed localized Vandermonde/configuration statistics, and finally suggested a single Wirtinger integration of the zero-source equation. The author now requests two sub-investigations that can exchange results:

| Home | Primary question | One live status owner |
| --- | --- | --- |
| [01_green_potential_resolvent](../../01_green_potential_resolvent/README.md) | Can the first-order field or an arithmetic comparison provide the missing canonical Green upper margin? | Child TND-OG register |
| [02_localized_zero_correlations](../../02_localized_zero_correlations/README.md) | Can marked local pairs or a full configuration functional retain a single nonreal defect and admit a source-side estimate? | Child TND-OC register |

Green is the author's preferred direction. Correlations remain a distinct conceptual branch, not a compulsory prerequisite. Setup does not start either research cycle. The [parent register](../../research-progress/02_SMOOTH_LOCALIZATION_RESEARCH_PROGRESS_20261106.md) retains completed/shared TND-O tasks and Gaussian alternatives.

## 2. Exact common dictionary

Write \(\vartheta(v)=\sum_{n\in\mathbb Z}e^{-\pi n^2v}\). The half-line theta primitive
\[
p(u)=\tfrac12e^u[\vartheta(e^{4u})-1],\qquad
p''-p=8\Phi,\quad p'(0)=-\tfrac12
\]
generates
\[
H_\lambda(z)=\int_0^\infty e^{\lambda u^2}\Phi(u)\cos(zu)\,du,
\quad H_0(z)=\tfrac18\xi((1+iz)/2),\quad
\partial_\lambda H_\lambda=-\partial_z^2H_\lambda .
\]
Forward heat time is \(t=\lambda_0-\lambda\). Zeta coordinates satisfy \(z=2\gamma+i(1-2\beta)\). To avoid the manuscript's two J symbols, write
\[
\mathcal P_\lambda(z)=\int_0^\infty p(u)e^{\lambda u^2}\cos(zu)\,du,
\quad
8H_\lambda=\tfrac12+(2\lambda-1-z^2)\mathcal P_\lambda+
4\lambda z\mathcal P_\lambda'-4\lambda^2\mathcal P_\lambda''.
\]
These are manuscript §§1–2, 6; the primitive derivation is also [Note11 §3](../../notes/11_TND_O_B02_CRITICAL_COEFFICIENTS_THETA_AND_RODGERS_TAO_20261106.md). Neither positivity of p nor of the complete source controls logarithmic cancellations automatically. The source resolvent \(G_\lambda(u)=8(1-\partial_u^2)^{-1}F_\lambda(u)\) is distinct from the spatial-strip Green kernel; its raw transform has a narrower strip and is not directly substituted at height 8 without analytic continuation through H.

With \(U_\lambda=\log|H_\lambda|\) and the complete multiplicity measure \(\nu_\lambda=\sum_jm_j\delta_{z_j}\),
\[
\Delta U_\lambda=2\pi\nu_\lambda,\qquad
R_\lambda=2\partial_zU_\lambda=H_\lambda'/H_\lambda,\qquad
\partial_{\bar z}R_\lambda=\pi\nu_\lambda.
\]
The conventions are \(\partial_z=(\partial_x-i\partial_y)/2\), \(\partial_{\bar z}=(\partial_x+i\partial_y)/2\). Thus the author's intermediate object is a meromorphic Cauchy field. Inversion permits a holomorphic ambiguity; the canonical product and normalization fix it. Opposite zeros must be paired in infinite sums. A multiplicity-m zero contributes \(m/(z-z_j)\), not a bounded density.

For compactly supported smooth \(\varphi\), the shared weak interface is
\[
\int\varphi\,d\nu_\lambda
=\frac1{2\pi}\int U_\lambda\Delta\varphi\,dA
=-\frac1\pi\int R_\lambda\,\partial_{\bar z}\varphi\,dA.
\]
The last expression uses the distributional bilinear pairing without complex conjugation. These representation identities do not themselves acquire a favorable sign.

## 3. What the Green branch inherits

For \(0\le\lambda\le1/2\), all zeros satisfy \(|y_j|\le1\). With \(a=\pi/8\),
\[
K(u)=\frac1{16\cosh(au)},\qquad
G(d,y)=\operatorname{artanh}\frac{\sin(ay)}{\cosh(ad)},
\]
manuscript §18, equations (18.2)–(18.3), gives
\[
\mathcal J_\lambda(X)
=\int_{\mathbb R}K(x-X)[U_\lambda(x)+U_\lambda(x+8i)]\,dx
-U_\lambda(X+4i)
=\sum_{y_j>0}G(X-x_j,y_j).
\]
One zero with \(y_j\ge d>0\), \(|x_j-X|\le r\), forces
\(\mathcal J_\lambda(X)\ge m(d,r)=d\sin(\pi/8)/\cosh(\pi r/8)\).
The required new input is a strict **upper** comparison below this margin with complete errors. At time zero the exact prime baseline has **plus** pole correction:
\(\mathcal J_0=\mathcal L-P+G(X,1)\), manuscript (18.15).

[Notes28](../../notes/28_TND_O_E20_PAID_QUADRATIC_GREEN_COMPARISON_20261107.md)–[29](../../notes/29_TND_O_E20_R2_UNIFORM_EULER_LENGTH_OBSTRUCTION_20261107.md), accepted within scope by [Review12](../../reviews/12_TND_O_E21_SIGNED_ACQUISITION_ASSESSMENT_20261107.md), pay \(\mathcal J_0\le\frac12\log(1+\epsilon_Q^2)\). They do not prove smallness. Their growing finite-Euler obstruction is a lower bound on an averaged quadratic residual for one product per dyadic interval with primorial length \(\le(T/2)^\theta\), fixed \(\theta<17/33\). It is not a lower bound on \(\mathcal J_0\), a pointwise obstruction at every center, or an exclusion of arbitrary coefficients/adaptive choices.

The first-order proposal is worth testing because contour extraction and pole subtraction may expose cancellation before the logarithmic integral. It still needs a zero-free contour, a denominator margin, source and zero tails, and an explicit transfer to the Green defect scale. Newman-time Burgers,
\(\partial_\lambda R=-R_{zz}-2RR_z\), is an off-pole identity; nonlinear products across poles need their own prescription.

## 4. What the correlation branch retains

A Vandermonde ensemble has \(p_N=Z_N^{-1}|\Delta|^2\prod w_0\); its two-point marginal integrates the **whole normalized density**, including the confining weight. Montgomery's original deterministic zero statistic does not supply this joint law for canonical zeros. Height independence is a feature of a translation-invariant unfolded limit, not a restriction on local correlation observables.

The author's weighting can be imposed before marginalization:
\[
\mathcal Z_{X,h}(\eta)=\mathbb E\prod_j[1+\eta w((x_j-X)/h)].
\]
The factors equal one outside the window. Coefficients are weighted factorial correlations of all orders. A Fredholm determinant requires a justified determinantal process and operator hypotheses.

For the actual deterministic zero multiset, retain transverse marks:
\[
S_{\lambda,X,h}[\Psi]=\sum_{j\ne k}w_jw_k
\Psi(x_j-x_k,y_j,y_k),\qquad
\mathcal Z_\lambda[f]=\prod_j(1+f(z_j))
\]
initially for compact support. The pair measure is
\(\nu_\lambda^{\otimes2}-\operatorname{diag}_*\nu_\lambda\), retaining distinct multiplicity copies. A factor \((y_j-y_k)^2\) kills real pairs and detects a conjugate pair. Height-only Vandermonde factors also vanish for equal ordinates of a nonreal reflected pair and for a multiple real zero; the full complex Vandermonde distinguishes their separations but supplies no canonical positive ensemble by itself.

The common Green specialization
\[
\prod_{y_j>0}e^{-sG(X-x_j,y_j)}
=e^{-s\mathcal J_\lambda(X)}
\]
is a convergent identity by inherited tails, not new information. A useful hierarchy must supply an independently controlled coefficient, connected response or comparison, beyond repackaging this identity. A center-averaged allowance can dilute one defect by order \(h/T\); growing order must pay coefficient growth and convergence. The [hierarchy locator](20_TND_O_PRIOR_HIERARCHY_LOCATOR_20261107.md) now identifies the author-specified heat-density fluctuation/recurrence hierarchy as primary background; source/fermion and theta-kernel constructions remain secondary comparators. None is assumed to be a zero process. [Source-use17](../../references/17_TND_O_GREEN_CORRELATION_SETUP_SOURCE_USE_20261107.md) records exact external claims and inspection limits.

## 5. Dated task crosswalk and exchange contract

- Completed TND-O results, issued requests, proofs and reviews remain at their current paths and evidence levels. Manuscript integration still ends at E17; Notes28–29 remain later assessed material.
- The unissued TND-O-B04 r6 default is superseded by the author-directed bifurcation. TND-OG-B01 prioritizes the first-order Green field; its optional second candidate is coefficient preconditioning. Continuation30 is historical routing, not an executed task.
- TND-OC-B01 owns selection between a marked pair consumer and a full configuration hierarchy. Earlier Gaussian-Laguerre and transverse-moment hierarchies remain available in the parent; neither is silently renamed a factorial-correlation hierarchy.
- Each B cycle compares at most two mechanisms and one clarification. A ready E successor requires an exact source/version freeze, concrete signed margin or paid comparison, explicit unbounded regime, and one shared-file owner. Absolute allowances, RH-equivalent criteria and finite numerical checks do not meet the signed-bound standard.
- A branch exporting an estimate states its observable, normalization, regime, constants, complete tails, evidence level and the precise input its consumer receives. The receiving branch evaluates whether these meet its actual defect margin; no automatic status or theorem transfer.

This setup is complete only with both branch continuations and local validation. No new notes in the research notes directories, numerical campaign, manuscript revision or new chat identity is produced here.

