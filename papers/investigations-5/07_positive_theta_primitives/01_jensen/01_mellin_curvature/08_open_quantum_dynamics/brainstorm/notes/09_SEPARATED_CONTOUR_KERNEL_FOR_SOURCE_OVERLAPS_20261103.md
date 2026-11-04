# Source overlap separation by a contour kernel

3 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance; actual **gpt-6.1-sol (Codex), reasoning effort ultra**, chat `01a19fdd-4e1e-7061-9ec4-141ca78368ce`, turn `01a1a422-aeb8-7d90-97c9-86e060c522a3`, unique brainstorm history **0002**. Two read-only inherited same-model support agents checked the finite Cauchy/Andréief algebra and the draft/v scope. This is same-execution checking with shared premises, not specialist or separate independent assessment.

**Type B discussion, MC08-B03 continuation:** the author proposes a source-state kernel interpretation inspired by equation 2.3 of his unpublished quaternion-forms draft and asks whether v-dynamics remains useful. This bounded response inspects the cited pages and constructs one compact-interval Cauchy analogue, retaining all constants and endpoints. The compact identities below are proved in-note with same-execution checks; no new signed estimate, preferred kernel inequality, global contour theorem or energy architecture is selected. The next consequential conceptual selection remains recommended Astra. This does not execute E07 or the former B04 Hamiltonian-choice task.

## 1. The author's unpublished draft and the analogy

Edward B. Baker III, *Integral formulas for quaternion valued forms, and their applications to Yang-Mills theory*, draft dated 14 February 2014, 14 pages. The author explicitly states that it was never published. [Source PDF](../../../../../../../investigations-2/active/21_quaternion_theta_geometry/source-documents/QuaternionForms-Final.pdf), SHA256 `5125461583b33e843f5e507b63577c7e6e0d801b8d1c64b34b7799bdcdc75920`, 283483 bytes. Pages 2–3 were extracted and visually inspected, including the complete page carrying equation 2.3.

Equation 2.3 has the structure
\[
I_n(\omega,\nu)=\int_\Omega\omega\wedge\nu
=C_n\int_{\partial\Omega}\int_{\partial\Omega}
\omega(z)\wedge K_n(z,w)\wedge\nu(w).
\tag{1}
\]
It separates the two form factors onto independent boundary variables, coupled by a kernel. The relevant mechanism is: reconstruct each factor from its own boundary values, then integrate their common original variable into a kernel. The variables are separate, not probabilistically independent, and the answer need not factor into a product of two integrals.

The printed formula concerns holomorphic/antiholomorphic top forms over a bounded complex domain; our overlap uses a real halfline. Accordingly neither the printed radial kernel nor its normalization is imported unchanged. The prior [Investigation21 comparison](../../../../../../../investigations-2/active/21_quaternion_theta_geometry/reviews/30_QUATERNION_FORMS_DRAFT_COMPARISON_AND_RELEVANCE_20261015.md) already records the unpublished status and questions about constants/domain terms elsewhere in Section 2. Here the construction is derived afresh for the actual real integration measure. No claim about the full draft or its quaternion/Yang–Mills arguments is assessed.

## 2. Cancel the square roots before analytic reconstruction

The original real source orbitals are
\[
f_i(u)=\Phi^{(2i)}(u)/\sqrt{\Phi(u)},\qquad
 g_j(u)=u^{2j}\sqrt{\Phi(u)}/(2j)!.
\]
For fixed finite i,j their real pairing is
\[
\langle f_i,g_j\rangle=\int_0^\infty
\Phi^{(2i)}(u)\frac{u^{2j}}{(2j)!}\,du=c_{j-i}.
\tag{2}
\]
The source is real on the real axis, so this product equals the usual Hermitian pairing there. Set
\[
a_i(z)=\Phi^{(2i)}(z),\qquad b_j(z)=z^{2j}/(2j)!.
\]
The canonical theta sum and its finite derivatives converge normally on compact subsets of
\[
|\operatorname{Im}z|<\pi/8.
\tag{3}
\]
Indeed Re(e^{4z})>0 there and the Gaussian n² decay dominates every finite derivative factor on each compact set. Thus a_i is holomorphic in this strip, while b_j is entire. No complex branch or global zero-free claim for sqrt(Phi) is required: it canceled before continuation. This is important because directly continuing the individually normalized f_i,g_j would create avoidable zero/branch issues.

## 3. Exact compact double-boundary formula

Fix R>0 and define the truncated mixed overlap
\[
M_{ij}^R=\int_0^R a_i(u)b_j(u)\,du.
\tag{4}
\]
Choose positively oriented simple closed contours Gamma_z,Gamma_w enclosing [0,R], with their filled closures in the strip (3) and positive distance from the segment. Rectangles with horizontal sides at +/-eta, 0<eta<pi/8, and real endpoints -delta,R+delta suffice.

Cauchy's formula reconstructs each factor separately:
\[
a_i(u)=\oint_{\Gamma_z}\frac{a_i(z)}{z-u}\frac{dz}{2\pi i},\qquad
b_j(u)=\oint_{\Gamma_w}\frac{b_j(w)}{w-u}\frac{dw}{2\pi i}.
\]
Substitute both into (4) and apply Fubini on compact contours:
\[
\boxed{M_{ij}^R=
\oint_{\Gamma_z}\oint_{\Gamma_w}
a_i(z)\,\mathcal H_R(z,w)\,b_j(w)
\frac{dw}{2\pi i}\frac{dz}{2\pi i}.}
\tag{5}
\]
The source-independent kernel is explicit:
\[
\boxed{\mathcal H_R(z,w)=\int_0^R\frac{du}{(z-u)(w-u)}
=\frac{\ell_R(z)-\ell_R(w)}{w-z},\qquad
\ell_R(z)=\int_0^R\frac{du}{z-u}=\log\frac{z}{z-R}.}
\tag{6}
\]
The logarithm is the branch defined by the integral, tending to zero as z tends to infinity. Partial fractions give the sign in (6). At z=w the apparent singularity is removable:
\[
\mathcal H_R(z,z)=-\ell_R'(z)=\frac{R}{z(z-R)}.
\tag{7}
\]
Thus the two contours may coincide; no diagonal singularity is introduced away from the original segment. If d_z,d_w are their distances from [0,R], then |H_R|<=R/(d_z d_w), which, together with bounded a_i,b_j and finite contour lengths, pays the interchange. There is no hidden conjugation or missing minus sign: (5) reconstructs the real bilinear product in (2) through two positively oriented holomorphic contour integrals.

The only imported complex-analysis formula here is [NIST DLMF 1.9.30](https://dlmf.nist.gov/1.9.E30), rechecked with its simple-contour/analyticity hypotheses. Equations (5)–(7) are the present elementary calculation. [Source record05](../../references/05_SOURCE_KERNEL_DRAFT_AND_CAUCHY_20261103.md) preserves the author-draft and DLMF provenance.

## 4. Exterior products separate with the determinant kernel

For increasing lists I,J of length r, define
\[
\mathcal A_I(\mathbf z)=\det[a_{i_a}(z_c)]_{a,c=1}^r,
\qquad \mathcal B_J(\mathbf w)=\det[b_{j_b}(w_d)]_{d,b=1}^r.
\]
Multilinearity and two finite Andréief expansions yield
\[
\boxed{
\det[M^R_{i_a j_b}]
=\frac1{(r!)^2}
\oint_{\Gamma_z^r}\oint_{\Gamma_w^r}
\mathcal A_I(\mathbf z)
\det[\mathcal H_R(z_c,w_d)]_{c,d=1}^r
\mathcal B_J(\mathbf w)
\prod_{c=1}^r\frac{dz_c}{2\pi i}
\prod_{d=1}^r\frac{dw_d}{2\pi i}.}
\tag{8}
\]
The last determinant has rows w_d and columns j_b, fixing the ordering and sign. All integrals are absolutely convergent in contour parameters at this fixed compact scope; positivity of the contour measures is not needed for the finite expansion. Both factors r! are retained. This is the requested separate-variable representation of the wedge pairing: each source family has its own variables and is coupled through an r-particle determinant kernel.

This step is algebraic separation, not a new sign theorem. In particular the actual contours are complex. A Gram-positive kernel for real exterior points would not sign this complex contour pairing or its source factors. A useful next gain must identify a source-sensitive kernel property, contour relation or inequality with its exact signed consumer.

## 5. Endpoints and the original halfline

At finite R, M_ij^R is generally not c_{j-i} or just the truncated moment c_{j-i}^R. Integration by parts gives, for i>0,
\[
M_{ij}^R=
\sum_{k=0}^{2i-1}(-1)^k
[\Phi^{(2i-1-k)}b_j^{(k)}]_0^R
+\int_0^R\Phi(u)b_j^{(2i)}(u)\,du.
\tag{9}
\]
All origin terms vanish by complete-source evenness and the polynomial parity. The upper terms remain. At fixed indices, canonical double-exponential decay makes the upper terms and omitted real tail vanish as R tends to infinity. The remaining polynomial derivative yields c_{j-i}, with zero for j<i. Consequently
\[
M_{ij}^R\longrightarrow c_{j-i},\qquad
\det[M^R_{i_a j_b}]\longrightarrow\det[c_{j_b-i_a}].
\tag{10}
\]
This proves convergence of the finite representations through equality to the original real integrals. It does not justify a single fixed unbounded-contour formula, interchanging unbounded limits under the separated integrals, or dropping outer sides. In particular b_j(w) grows polynomially, so boundary terms at infinity cannot be discarded without payment. No uniformity in response order or particle number is asserted.

## 6. What v still does, and what it has not contributed

For v>0 the coefficient weights
\[
p_n(v)=c_nv^n/F(v),\qquad \sum_np_n(v)=1,
\qquad K_v=\sum_np_n(v)S^n
\]
organize a bounded contraction on coefficient space and support the earlier realization. They are step weights in this representation, not automatically Born probabilities for the original source states. With D=v partial_v,
\[
D\log F=E_{p(v)}n,\qquad D^2\log F=\operatorname{Var}_{p(v)}n.
\tag{11}
\]
But every ordered amplitude has
\[
A_{I,J}(v)=\frac{v^d}{F(v)^r}C_{I,J},\quad d=\sum J-\sum I,\quad C_{I,J}=\det[c_{j_b-i_a}].
\tag{12}
\]
Thus its sign is independent of v>0; when nonzero,
\[
D\log|A|=d-rE_p n,\qquad D^2\log|A|=-r\operatorname{Var}_p n.
\]
The unknown signed determinant has disappeared from these responses. For the rectangular pilot, whenever its denominator is nonzero,
\[
\frac{A_{r,k-1}(v)A_{r,k+1}(v)}{A_{r,k}(v)^2}
=\frac{D_{r,k-1}D_{r,k+1}}{D_{r,k}^2}.
\tag{13}
\]
Varying v therefore supplies no change in this target ratio. This supports the author's concern at the specific scope of the missing signed comparison. It does not prove every operator estimate using v useless. Its established utility is representation, normalization and realization; no additional utility for the missing source-state signed inequality has been established.

For the present kernel discussion one can fix v or omit it and work directly with (2). The activity clock and its engineered Hamiltonian should not be carried into a source-pairing argument without a named use. This keeps earlier results separate as the author requested.

## 7. Assessment and continuation

The author's reconstruction analogy supplies a mathematically appropriate alternative interpretation. A direct compact analogue exists, with an explicit kernel and exterior-power formula. It is a classical analytic representation of the mixed source pairing and requires no quantum interpretation. It is not yet a new estimate or RH gain: the known all-minor target remains the target, and generic rewriting does not establish it.

Read with [result summaries](../../../../../../../../result-summaries/README.md), especially [theta/bookkeeping](../../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [controls](../../../../../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid](../../../../../../../../avoid/README.md), especially [reformulations](../../../../../../../../avoid/01_restating_the_target.md), [re-realizations](../../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [joint signed estimates](../../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [unchecked imports](../../../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md). Any proposed sign inequality must name the extra canonical source premise it uses and screen it against the source-compatible controls. No uncomputed sign or analytic premise is assigned to another control family by this generic identity.

**Next conceptual discussion: [B] MC08-B03 — Astra**, the author-proposed source-kernel interpretation, before a new Hamiltonian choice. Decide whether the explicit compact kernel has a source-sensitive property worth pursuing, or whether a different geometric reconstruction is needed; preserve both source preparations and the complete signed consumer. Do not repeat the generic representation as a sign result. The downstream B04 model/energy choice remains unexecuted, and E07 remains reserved for its original B04 model/domain route. A kernel execution would need its own explicitly identified bounded request; none is issued here. [Handoff09](../../research-progress/handoffs/09_SOURCE_PAIRING_KERNEL_AND_MODEL_CONTINUATION_20261103.md) carries the exact formulas, endpoint obligations and model-change guidance. The [sole MC08 register](../../research-progress/01_OPEN_QUANTUM_DYNAMICS_RESEARCH_PROGRESS_20261102.md) owns current routing. Preserve chat/history 0002 on a model change; the unpublished author draft and all frozen E06 records remain unchanged.
