# Research continuation: realizing the shift flow and continuing cumulative positivity

20 September 2026. Prepared for Edward Baker for continuation in a new chat.

**Model:** OpenAI GPT-6 (Codex). **Reasoning effort:** the configured effort level is not exposed to the assistant in this session; no level is inferred.

**Status:** prioritized research handoff. The arithmetic identities and existing calculations cited below are inherited. The proposed experiments and the elementary consistency observations in Section 4 are directions for investigation, not a Wilson realization, a new numerical certificate, or an all-depth positivity result. No new numerical experiment was performed for this note.

## 1. Start here: the recommendation and the current state

The most promising immediate step is to make the proposed Wilson transfer into a precisely defined linear boundary operator, then test its normalization and first shift derivative on a small interval. The exact shifted-zeta equation should constrain the choice of observable and contour family from the outset. Choosing a new Loewner driver without an observable-to-operator dictionary would leave the central matching problem untouched.

The strongest complementary mathematical direction is cumulative-storage continuation using the full spatial coupling and signed changes in its defect metrics. It has an exact finite-step criterion and existing numerical infrastructure. It can be investigated without first completing the physical model, but success there would not by itself establish the Wilson interpretation.

The working manuscript has just been split into a matched version **0.3**:

- [Main exposition](../manuscript.pdf), [source](../manuscript.tex): 16 pages, *Shifted-zeta evolution and Wilson lines: a Loewner realization program for cumulative positivity*.
- [Supplementary information](../supplementary-information.pdf), [source](../supplementary-information.tex): 26 pages, containing the detailed tools and calculations.
- [Editorial split and reading map](MANUSCRIPT_SPLIT_AND_PROGRAM_20260920.md).
- [Original shift-flow proposal](SHIFT_FLOW_CUMULATIVE_STORAGE_AND_CRITICAL_PATH_20260919.md).

Read main Sections 3, 4, 6 and 7 first. Consult SI S4 for the exact Wilson variation, S6--S8 for endpoint/reflection constraints and the existing bulk response, and S9 for continuation algebra. Main Section 2.2 retains the explicit explanation of the decay rates and local constant.

The [critical-path investigation](../../critical-path/README.md) is still a placeholder. Its intended subject is constructive depth--shift continuation. The active investigations are critical-path, wilson-loewner, wilson-lines, loewner and fractional-dimension; other investigations are under previous/. Preserve that organization.

This note supersedes the *priority order* of the older manuscript handoff: completing the bulge interaction calculation remains useful, but it should now test a specified effective transfer or norm identity. It is no longer the automatic first task regardless of the operator definition.

## 2. The exact target to carry into the new chat

Use \(I_L=(-L/2,L/2)\), zero-extended inputs, and ordinary unweighted \(L^2\) norms. Write

\[
H(p)=\xi(\tfrac12+p),\qquad
K_\omega(p)=\frac{H(p-\omega)}{H(p+\omega)},\qquad
a_\omega(p)=\frac{H'(p-\omega)}{H(p-\omega)}
           +\frac{H'(p+\omega)}{H(p+\omega)}.
\]

The compressed causal realizations \(V_{\omega,L}\) and \(G_{\omega,L}\) are defined on a right Laplace line \(\Re p>1\), not by assuming an unweighted whole-line contraction from the boundary modulus. For \(0<\omega\leq1/2\),

\[
\boxed{\partial_\omega V_{\omega,L}=-G_{\omega,L}V_{\omega,L},
\qquad V_{0,L}=I.}
\]

This equation is already known arithmetic input. The research hypothesis is an independently defined physical operator \(\mathcal V_{\omega,L}\) satisfying it, with the same initial normalization and a proved uniqueness statement in an appropriate causal class.

The zero-shift generator fixes the components to match:

\[
\begin{aligned}
a_0(p)={}&w_0+
2\int_0^\infty n_\Gamma(u)(1-e^{-pu})\,du
+\frac2{p+1/2}+\frac2{p-1/2}\\
&-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}e^{-p\log n},\\
n_\Gamma(u)&=\sum_{n\ge0}e^{-a_nu}
=\frac{e^{-u/2}}{1-e^{-2u}},\qquad a_n=2n+\tfrac12,\\
w_0&=\psi(\tfrac14)-\log\pi
=-\gamma-\tfrac\pi2-3\log2-\log\pi.
\end{aligned}
\]

The \(a_n\) are decay rates, not zeta zeros. The constant \(w_0\) is fixed by the arithmetic normalization, not an adjustable counterterm. The real generator form is the full \(Q_{0,L}\), including the local term, poles and prime-power delays. At finite shift the generator's delay weights include \(\cosh(\omega\log n)\); the finite transfer contains a multiplicative integer comb.

Define

\[
D_{\omega,L}=I-V_{\omega,L}^*V_{\omega,L},\qquad
Q_{\omega,L}[g]=\Re\langle g,G_{\omega,L}g\rangle.
\]

On the stated core, with the form interpretation,

\[
\begin{aligned}
\partial_\omega D_{\omega,L}
 &=V_{\omega,L}^*(G_{\omega,L}^*+G_{\omega,L})V_{\omega,L},\\
\langle f,D_{\omega,L}f\rangle
 &=2\int_0^\omega Q_{s,L}[V_{s,L}f]\,ds,\\
Q_{0,L}[f]
 &=\lim_{\omega\downarrow0}
       \frac{\langle f,D_{\omega,L}f\rangle}{2\omega}.
\end{aligned}
\]

Positive-shift differentiability and the right derivative at zero on smooth tests do not imply an operator-norm derivative at zero. Keep generator domains and form domains distinct.

The sufficient endpoint of the program is

\[
L_j\to\infty,\qquad 0<\omega_j\downarrow0,\qquad
\|V_{\omega_j,L_j}\|\le1
\]

on **every input** at each selected pair. Restriction to a fixed smaller interval followed by the fixed-test limit gives Weil positivity and hence RH. This implication needs neither a smooth path nor a uniform positive margin. Constructing the required sequence remains open.

Sources: [main shift equations](../sections/03_shift_evolution.tex), [shared background](../../../background_section.tex), [main continuation discussion](../sections/07_critical_path.tex).

## 3. Priority order and useful stopping points

| Priority | Direction | Why it is promising | First useful deliverable |
|---|---|---|---|
| 1 | Define and normalize a Wilson boundary response, then test its generator | It attacks the missing connection between a field observable and the prescribed arithmetic operator | An explicit candidate, or a precise obstruction, including its initial operator, causal support and first variation |
| 2 | Identify an independent amplitude for cumulative storage | It asks the reflected construction to explain the actual contraction defect, without demanding positivity of every instantaneous generator | A concrete balance law in a controlled model, or a failure of its normalization or small-shift scaling |
| 3 | Test one spatial/shift step using signed cumulative changes | The Schur criterion is exact and the arithmetic code already exists | An operator inequality with a rigorous complement bound, or a diagnostic clearly identifying the missing bound |
| 4 | Complete the first interacting bulge response for the selected observable | It tests whether the nonzero bulk response survives the physical sum and can enter the required insertion identity | A complete first interaction-order calculation at positive height in one specified scheme |

Priorities 2 and 3 can inform one another. A physical model may provide a useful gluing inequality; the arithmetic weak directions may indicate what an amplitude space must retain. They are not logically interchangeable proofs.

A well-defined negative result is useful. For example, proving that a proposed observable cannot have identity initial transfer is a sharper advance than computing further scalar correlators without a boundary-operator interpretation. Scope any exclusion to the model actually tested.

## 4. Recommended first task: a fixed-window realization test

### 4.1 Specify the operator before selecting the driver

Write down the action of the candidate on an arbitrary input \(f\). A possible starting format is a source-to-response operator,

\[
(\mathcal V_{\omega,L}f)(x)
=\int_{I_L}\mathcal K_{\omega,L}(x,y)f(y)\,dy,
\]

allowing distributional kernels at zero shift. The field observable defining \(\mathcal K\), its regulator, physical adjoint, reference color sector and normalization must be explicit. Determine rather than assume whether it has the required causal support \(y\le x\).

Distinguish three objects:

1. A reflected Gram kernel of endpoint states.
2. A linear boundary response or transfer.
3. A partition-function ratio such as the auxiliary Gaussian gamma ratio.

Each is meaningful, but an identity relating them is needed. The current reflected free kernel \(1/(r+s)\), or \(1/(2\cosh((x-y)/2))\) after radial weights, is not the identity operator at \(\omega=0\). On a finite logarithmic interval this smooth kernel gives a compact operator; it cannot be the identity on the full infinite-dimensional \(L^2\) space. A finite-mode inverse square root may normalize a matrix, but does not establish a bounded continuum normalization. This is an elementary consistency test of the proposed starting observable, not an exclusion of a different source-to-response construction.

The most productive comparison is between a genuine boundary response built from Wilson-dressed fields and a normalized correlator construction with a proved operator interpretation. The auxiliary Robin/Gaussian model is a useful exact control for the gamma factor; a determinant ratio is not already a causal Wilson transfer.

### 4.2 Begin before the first arithmetic delay

Take a fixed \(0<L<\log2\). No nontrivial integer delay acts on that window, so the full compressed transfer reduces to its archimedean kernel **including the rational pole correction**. The local constant and pole terms are still present. This is a manageable exact target, rather than a gamma-only resemblance.

For the candidate:

- Verify \(\mathcal V_{0,L}=I\) in the appropriate strong sense.
- Derive the first variation on a smooth core:
  \[
  \mathcal V_{\omega,L}f=f-\omega G_{0,L}f+o(\omega).
  \]
- Identify separately the gamma difference, fixed local term and pole response.
- Record the assumptions needed to pass from regulated kernels to the operator/core statement.
- Only after this test succeeds, derive or constrain a contour clock and a real Loewner driver.

The full nonsymmetric causal generator is the comparison target. Matching only its real quadratic form would not identify the transfer.

The next arithmetic threshold is equally concrete. For \(\log2<L<\log3\), the zero-shift causal generator adds the delay

\[
-\frac{2\log2}{\sqrt2}\,T_{\log2}.
\]

Its symmetric form contributes
\(-(\log2/\sqrt2)\langle f,(T_{\log2}+T_{\log2}^*)f\rangle\).
At positive shift the generator coefficient acquires \(\cosh(\omega\log2)\). Explain the mechanism producing this coefficient and its sign before extrapolating to every prime power. At \(L=\log2\) itself the delay has no nonzero interval action.

### 4.3 Use the actual Wilson insertion

[SI S4](../sections/05_variation.tex) gives curvature, scalar-gradient, arclength/tangent-map, moving-endpoint and polarization terms. For an averaged observable, include differentiation of its normalization and any shift-dependent measure or boundary action. Closure must come from field equations, a Ward identity or another proved reduction.

For regular inverse Loewner pullbacks,

\[
\partial_tX_t(s)
=-\frac{2f_t'(\zeta(s))}{\zeta(s)-u_t}.
\]

At fixed \(L\), identifying a clock \(\omega(t)\) would require
\(\partial_t\mathcal V=-\dot\omega\,G_\omega\mathcal V\).
The existing abelian counterexample excludes a universal geometry-only variation of bare transport; it does not exclude such an averaged field-dependent closure. Capacity, shift, endpoint log-radius and support length must not be identified by notation.

### 4.4 A second inexpensive test: the storage amplitude near zero

An independent positive amplitude map should satisfy

\[
\|f\|^2=\|\mathcal V_{\omega,L}f\|^2
       +\|\mathcal B_{\omega,L}f\|^2.
\]

After matching the transfer, the fixed-test expansion forces

\[
\|\mathcal B_{\omega,L}f\|^2
=2\omega Q_{0,L}[f]+o(\omega).
\]

Consequently, in any direction with \(Q_{0,L}[f]>0\), its norm must scale as
\(\sqrt{2\omega Q_{0,L}[f]}\). A candidate with
\(\|\mathcal B_{\omega,L}f\|=O(\omega)\) cannot account for that first-order defect. This is a necessary scaling observation; it does not assert convergence of \(\mathcal B_{\omega,L}/\sqrt\omega\) as an operator or construct a positive factorization of \(Q_{0,L}\).

Also avoid building in monotonicity that has not been proved. An ansatz making \(\|\mathcal B_{\omega,L}f\|^2\) nondecreasing for every \(f\) would impose \(\partial_\omega D_{\omega,L}\succeq0\), a stronger condition than \(D_{\omega,L}\succeq0\). A cumulative amplitude may need to retain correlations across shifts. The archived negative instantaneous test alone does not establish nonmonotonicity of \(D\): it uses a fixed input rather than the evolved one.

These normalization and scaling checks should precede a long perturbative calculation.

## 5. The mathematical continuation task for critical-path

### 5.1 Preserve the directional storage data

For a causal split into lengths \(L\) and \(h\),

\[
V_{\omega,L+h}=
\begin{pmatrix}X&0\\Y&Z\end{pmatrix},\qquad
E=I-X^*X,\qquad F_{\rm out}=I-ZZ^*.
\]

With \(\|X\|,\|Z\|<1\),

\[
\|V_{\omega,L+h}\|\le1
\iff
\|F_{\rm out}^{-1/2}YE^{-1/2}\|\le1.
\]

The new slab uses the **output** defect \(I-ZZ^*\) in this criterion. The inverses require strict diagonal bounds. Preserve the full normalized cross map rather than replacing both defect metrics by their smallest eigenvalues.

For a simultaneous shift change, use

\[
P_{\omega,L}
=\frac2\omega\Re[(I-V_{\omega,L})(I+V_{\omega,L})^{-1}],
\qquad
D_{\omega,L}=\frac\omega2(I+V_{\omega,L}^*)P_{\omega,L}(I+V_{\omega,L}).
\]

[SI S9](../sections/s_continuation.tex) defines the reference diagonal metrics, normalized cross block \(\mathcal K\), and signed changes \(H_A,H_F,H_B\). Its joint criterion is

\[
I+H_F\succ0,\qquad
I+H_A-(\mathcal K+H_B)^*(I+H_F)^{-1}(\mathcal K+H_B)\succ0.
\]

Here \(\succ0\) means a coercive lower bound. Comparisons between positive shifts avoid treating the bounded \(P_{\omega,L}\) as an operator-norm approximation to the unbounded central form.

### 5.2 A concrete pilot with existing controls

A useful pilot is

\[
L=\log7,\qquad h=\tfrac14\log(8/7),\qquad
L+h=\tfrac34\log14.
\]

The added slab has \(h<\log2\), so it has no internal prime delay; the enlarged transfer activates the delay at \(\log7\). This is already the first spatial horizon of the storage-depth work. **Do not present reaching this length by the established central-form method as a new result.**

The new question is whether the cumulative criterion can certify a useful step or shift range beyond the available instantaneous-generator argument. Select the reference shift from an actual existing certificate after checking its scope. An optional stress test is a candidate shift \(\beta=10^{-11}\), where the archived log-7 polynomial has negative instantaneous energy but positive cumulative storage. There is no all-input contraction certificate at that pair supplied by the single-vector example.

Such a pilot may compare a very small certified reference shift with a larger candidate shift to test the advantage of cumulative storage. It is a local comparison experiment, not already a decreasing-shift all-depth path. The eventual sequence must still approach zero shift.

Retain weak old-interval directions and the dominant cross-coupling directions, compute the signed changes, and bound the unresolved complement and **complete outputs**. A positive finite matrix, or nested output convergence without a tail estimate, is exploratory evidence only. Report a failed enclosure with the term that dominates the error instead of interpreting an unresolved tiny sign.

The current storage-depth version 0.3 already contains central certificates at this first horizon and at \(L_2=\tfrac12\log56\), with a 96-mode slab refinement. Those results are controls and infrastructure, in their stated working normalization; the independent normalization audit and mathematical review remain open.

### 5.3 State what would make the pilot part of a path

An iteration must carry the diagonal coercivity, cross-coupling bound, admissible shift change and approximation/complement errors. It must eventually establish

\[
L_{j+1}=L_j+h_j,\qquad \sum_jh_j=\infty,\qquad
\omega_j\downarrow0.
\]

Local extension does not rule out finite-depth accumulation. The unconditional innerness anchor at \(\omega=1/2\) does not justify reversing a forward dissipation argument. The term “critical path” denotes a path of controllable estimates, not an assumed boundary of the true contraction region.

The inherited adaptive-generator estimate using
\(\kappa_L=\|X_L\|_{Q_{0,L}\to Q_{0,L}}\) presupposes central coercivity and needs a proved **upper** bound on \(\kappa_L\). Keep it as a comparison route, not a substitute for the spatial positivity step.

## 6. Tools to reuse and directions to defer

| Existing material | Reuse it for | Scope that must remain explicit |
|---|---|---|
| [SI S1](../sections/s_arithmetic.tex), [SI S2](../sections/03_free_kernel.tex) | Exact arithmetic factorization, even angular spectrum, Gaussian/Robin control | A regulated covariance and a partition ratio do not yet give the full physical transfer |
| [SI S3](../sections/04_geometry.tex), [SI S4](../sections/05_variation.tex) | Contour dictionary and exact insertion calculation | Fixed-scalar rigidity is scoped; the variation requires smooth curves and actual fields |
| [SI S5](../sections/06_projectors.tex), [SI S6](../sections/07_endpoints.tex) | Allowed charge spaces and endpoint tests | The vanishing result concerns ordinary scalar endpoints in the constant-map Poincare ansatz; Baker's conformal semicircle lies outside it |
| [SI S7](../sections/08_reflection.tex), [SI S8](../sections/09_response.tex) | Ordinary adjoint, reference junction, positive free controls, bulge response | Interacting reflection is conditional; \(3/2-2\log2\) is only the direct Gaussian bulk coefficient |
| [Parent Loewner checks](../../loewner/numerics/README.md), [exploratory assembly](../../loewner/numerics/exploratory/README.md) | Transfer kernels, weighted quadrature, defect/Cayley assembly and nested output diagnostics | These finite computations are not all-input positivity certificates |
| [Adaptive-shift background](../../../../shifted-zeta/storage-depth/archive/background/1-critical_path_research.md), [cumulative-storage background](../../../../shifted-zeta/storage-depth/archive/background/2-cumulative_storage_path.md) | Relative estimates, signed continuation, archived witness and cumulative example | Preserve working normalization and the distinction between one input and an operator bound |
| [Storage-depth status](../../../../shifted-zeta/storage-depth/STATUS.md), [claims](../../../../shifted-zeta/storage-depth/CLAIMS.json), [numerics](../../../../shifted-zeta/storage-depth/numerics/README.md) | Locate existing certificates, full-output estimates and complement methods | Read current scope before proposing a “new” horizon; large archives are external |

Defer an unrestricted search over stochastic drivers until a regulated observable and parameter dictionary exist. Defer fermionic superconnections or extra charged junction matter unless a specific endpoint obstruction motivates them. They change the operator and require a new analysis; they are not automatic remedies.

The [earlier detailed interaction handoff](CONTINUATION_20260919_SESSION3.md) remains applicable once the observable is selected. Complete endpoint-to-line exchange, defect H-scalar derivative terms, endpoint self-energy and junction/defect counterterms in one scheme. Start at positive bulge height. Analyticity of the direct bulk integral does not establish analyticity of the complete flat-limit response.

A focused independent review of endpoint charge conventions, the physical reference sector and generator/form domains would be valuable before promoting a construction to a manuscript claim. The existing 268 diagnostics do not replace that review.

## 7. A bounded agenda for the next chat

1. Read this note and main Sections 3--4 and 6--7. Restate the exact operator to construct and choose the first fixed-window test.
2. Compare the actual candidate response and normalized-correlator definitions against identity initial data, causal support and the physical adjoint. Eliminate a candidate only within its stated assumptions.
3. Produce one explicit operator/core calculation, or identify the precise missing datum preventing one. Check the normalization and storage-amplitude scaling before further perturbation theory.
4. Save the result in a dated Wilson--Loewner research note. If the main advance is a spatial/shift estimate, begin a separate dated note in critical-path and link the two.
5. Update the manuscripts only after there is a substantive result or clarified hypothesis worth recording. Keep the current matched draft as the starting reference.

Suggested opening request for the new chat:

> Continue the Wilson--Loewner research from notes/RESEARCH_CONTINUATION_20260920.md in papers/susy-positivity/investigations/wilson-loewner. Start with the recommended fixed-window realization test: define a Wilson boundary response with identity initial normalization and causal support, then determine whether its first shift variation can match the full arithmetic generator for \(0<L<\log2\), including the local and pole terms. Use the existing variation and endpoint/reflection tools. Record a concrete calculation or a precisely scoped obstruction in a new research note. Keep cumulative positivity and the later depth--shift gluing problem visible, and do not assume an arithmetic Loewner driver already exists.

## 8. Repository and verification state

The matched [20 September version 0.3 snapshot](../drafts/2026-09-20-v03/README.md) contains both PDFs, all TeX inputs, build records and diagnostic programs. Unified versions 0.1 and 0.2 remain unchanged. The split and this handoff have not been committed by this assistant; check the working tree before beginning further edits and preserve the existing changes.

At the manuscript closeout, both PDFs compiled without unresolved references or overflow warnings, all 42 pages were visually inspected, and all 268 existing diagnostics passed. The package and program structure checks passed. These establish build identity and finite checks, not independent mathematical verification. This handoff adds no numerical result and does not change the manuscript claims.

Follow the [build guide](../BUILD.md) when releasing a later manuscript pair. Preserve dated snapshots. Put incremental research in notes/, calculations in numerics/, and independent reviews in reviews/ for the relevant investigation. Follow the repository [large-file policy](../../../../../LARGE_FILES.md): keep large regenerable matrices outside git with the required small records and archive guide. Check archive availability before scheduling a costly replay; its absence need not block the initial analytic operator-definition work.
