# Angular and radial models for theta overlaps

**Research overview and plan · 5 November 2026 · revision 1.** Prepared for **Edward Baker** with substantial LLM assistance from OpenAI Codex, actual recorded model **gpt-6-astra**, reasoning effort **xhigh**. Affiliation: MC11 history0002, thread `01a1a9d4-3d44-7472-ae0f-54705423d86b`.

This program asks whether a three-dimensional model with angular Dirac modes and a radial coordinate can explain the theta source and supply useful analytic information about its signed determinants. Spherical symmetry permits separation into angular channels, while the radial Green response can supply an inverse-multiplicity weight. The immediate task is to assess that exact construction, then decide which geometry, boundary conditions, potential and observable give a coherent model.

The author's direction is **analytic calculations and conceptual improvements**. Work should address complete spectral families and arbitrary determinant order. Numerical work and low-order or low-index calculations are permitted only as bounded tests of an explicitly stated hypothesis intended to extend to all orders. A succession of finite cases is not a research objective.

The [current progress register](../research-progress/02_ANGULAR_RADIAL_THETA_MODEL_RESEARCH_PROGRESS_20261105.md) is the investigation's sole live register. The [original overview](01_ENERGY_FILTERED_THETA_OVERLAPS_RESEARCH_OVERVIEW_20261104.md) retains the energy-filter comparison and its task contracts. This plan continues the angular direction from [Brainstorm Note05](../brainstorm/notes/05_MC11_RADIAL_QUANTIZATION_MODEL_COMPARISON_20261104.md) and [Note06](../brainstorm/notes/06_MC11_ANGULAR_WEIGHT_DIRAC_SQUARE_AND_RADIAL_GREEN_20261104.md), preserving MC11-BR01 and the distinct MC11-B01/E05 determinant-transfer tasks.

| Next task | Type | Recommended model and reason | Dependency | Expected output |
| --- | --- | --- | --- | --- |
| **MC11-AR-E01 — default first** | E | **Sol**; assess specified operator and Green identities by a fixed analytic route | Note06 and the existing references are available | Claim-by-claim assessment for all angular indices, including domains and boundary qualifications |
| MC11-BR01 — model selection | B | **Astra**; geometry, physical observable and confinement remain consequential choices | Accepted AR-E01 premises, or its named structural failure | One selected model contract, or a scoped stop |
| MC11-B01 — alternative existing route | B | **Astra**; select an estimate that controls signed cofactors as order grows | E04 is accepted; can proceed independently if the author selects it | At most two analytic routes and one E05 proof contract, or a scoped stop |

These recommendations follow [GPT_RESEARCH_MODEL_WORKFLOW](../../../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md). Edward Baker chooses the actual model, effort and chat. Issuing this plan does not activate the research tasks or dispatch other chats.

## Starting evidence and the unresolved problem

The original box Hamiltonian has energies \(E_n=\pi n^2\). Its filter retains the ground level and gives every excited level weight \(s\in[0,1]\). [E01](../reviews/01_MC11_E01_R1_STARTING_RESULTS_ASSESSMENT_20261104.md) accepts that every excited level lowers the order-two unnormalized determinant, with total fractional loss below \(10^{-4}\). [E04](../reviews/02_MC11_E04_R1_THREE_ORBITAL_RETURN_ASSESSMENT_20261104.md) accepts the completed order-three comparison: every excited level raises that determinant throughout the common filter path, and its fractional increase is about \(1.340206\times10^{-5}\). These are scoped internal LLM assessments with shared numerical premises, not evidence of an order-induction law.

The new angular/radial formulas in Note06 have **proof-author checks only**. They recover a source trace but supply no new signed determinant estimate. Three distinct aims must be kept separate:

1. **Spectral completeness:** derive an identity or estimate for every angular index \(n\), with the entire infinite sum justified.
2. **Model consistency:** specify a Hilbert space, self-adjoint operator, domains and observation map whose physical interpretation is precise.
3. **Determinant transfer:** prove a useful bound with explicit dependence on every determinant order \(q\), and on coefficient shifts when the downstream application needs them.

Success on the first two aims is a conceptual or representation result. It does not establish the third. The repository's [result index](../../../../../../../result-summaries/README.md), [theta cluster](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [patterns index](../../../../../../../avoid/README.md), [target-reformulation caution](../../../../../../../avoid/01_restating_the_target.md) and [re-realization caution](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md) set that distinction.

## Fixed source and auxiliary pairing

Until a named conceptual task explicitly proposes a different model, the mathematical object to recover is
\[
Q_s(t)=e^{-t}+s\sum_{n\ge2}e^{-tn^2},\qquad
r=e^{2u},\quad u\ge0,
\]
\[
A_s(r)=Q_s(\pi r^2),\qquad p_s(u)=e^uQ_s(\pi e^{4u}),\qquad
\Phi_s(u)=\frac{p_s''(u)-p_s(u)}8.
\]
The complete theta source is \(s=1\). The relation \(\beta=r^2\) describes the old box trace. If \(u\) becomes a spatial coordinate, a physical temperature or evolution time of the new theory is an additional variable; it must not silently be identified with position.

The source functions live in
\[
\mathfrak h=L^2((0,\infty),du),\quad
\langle f,g\rangle=\int_0^\infty\overline{f(u)}g(u)\,du,
\]
\[
f_i=\frac{\Phi_s^{(2i)}}{\sqrt{\Phi_s}},\qquad
g_\ell=\frac{u^{2\ell}\sqrt{\Phi_s}}{(2\ell)!},\qquad
c_j(s)=\int_0^\infty\frac{u^{2j}\Phi_s(u)}{(2j)!}\,du.
\]
With normalized antisymmetrization, \(\langle\bigwedge_i f_i,\bigwedge_j g_j\rangle\) is the determinant of pairwise inner products. The original diagonal block is
\[
D_q(s)=\det[c_{q+j-i}(s)]_{i,j=0}^{q-1}.
\]
It is a cross-pairing, not a squared norm. The [terminology correction](../brainstorm/notes/03_MC11_THERMAL_PARAMETER_AND_ORBITAL_TERMINOLOGY_20261104.md) and [normalization note](../brainstorm/notes/04_MC11_AUXILIARY_INNER_PRODUCT_AND_WEDGE_NORMALIZATION_20261104.md) govern use of these formulas. Call the vectors **auxiliary source functions** until a physical preparation is specified.

A fixed exterior power is one particle-number sector; \(\mathcal F_-(\mathfrak h)=\bigoplus_{q\ge0}\bigwedge^q\mathfrak h\) is the full fermionic Fock space. A Hamiltonian and its second quantization are further choices. Neither an angular spinor label nor positive kinetic energy makes the cross-pairing nonnegative.

## Angular Dirac modes and the radial response

Use the self-adjoint Dirac operator \(D\) on the unit two-sphere. Its eigenvalues are \(\pm n\), with multiplicity \(2n\) per sign. Thus \(D^2\) has eigenvalues \(n^2\) with total multiplicity \(4n\). The ordinary angular heat trace has these multiplicities; recovering \(Q_1(t)\) through a scalar spectral weight requires \(W=(4|D|)^{-1}\). This weight is bounded and positive but is not a trace-one state. Rotational symmetry alone does not select it.

Note06 gives an analytic origin for this weight on the product cylinder
\[
g_C=dv^2+\tfrac14 g_{S^2},\qquad v\in\mathbb R.
\]
For angular chirality \(\Gamma\), the proposed operator and square are
\[
\mathcal D_C=-i\Gamma\partial_v+2D,\qquad
\mathcal L=\mathcal D_C^2=-\partial_v^2+4D^2.
\]
The full-line radial Green kernel in the \(n^2\) block is
\[
G_n(v,w)=\frac{e^{-2n|v-w|}}{4n},\qquad
\operatorname{Tr}_{S^2}\!\left(e^{-tD^2}G_{\mathcal L}(v,v)\right)
=\sum_{n\ge1}e^{-tn^2}.
\]
This is an angular heat-damped radial-diagonal Green response. It is not a full three-dimensional partition function, a full-space resolvent trace, or automatically the propagator of the first-order Dirac field. Squaring supplies a nonnegative Laplace-type operator with square energies; choosing it as a kinetic Hamiltonian is a model decision.

The [radial companion](../../../../../../../papers/investigations-5/05_radial_theta_collision_geometry/book/main.tex) already uses the cylinder metric. Ordinary Euclidean space instead has
\[
g_E=4e^{4u}g_C.
\]
Its sphere at radius \(r\) has angular Dirac scale \(D/r\). Note06's reduced formal square contains centrifugal coefficients \(n(n\pm1)/r^2\). The cylinder and Euclidean realizations therefore require separate operator, measure and boundary calculations.

Two unresolved effects are central to the plan. First, on a radial half-line the free Green diagonal acquires Dirichlet or Neumann image terms, \((1\mp e^{-4nv})/(4n)\). Second, a spherical potential preserves angular separation but changes the channel response. For the explicitly second-order cylinder model,
\[
\mathcal L_V=-\partial_v^2+4D^2+V(v),\qquad
R_V(t,v)=\sum_{n\ge1}4n\,G_{n,V}(v,v)e^{-tn^2}.
\]
Whether this observable equals the desired theta source, or differs by a controllable term, is a calculation to perform. A potential added to a first-order Dirac operator is a different contract. A choice of \(V\), boundary weight or readout solely to fit finitely many theta coefficients is outside this plan.

Even the free cylinder identity leaves the source evaluation \(t=\pi e^{4u}\) to explain. For Euclidean spheres, the fixed-time angular trace naturally involves \(Q_1(\pi/r^2)\); Jacobi inversion relates this to \(A_1(r)\), with harmonic correction terms. That identity applies to the complete unit-weight source and must not be silently extended to arbitrary \(s\). The [reference catalog](../references/README.md) records the inspected primary-source conventions; AR-E01 will assess the local derivations and their scope.

## Research plan

The default sequence is **AR-E01 → BR01 → AR-E02 → AR-E03 → B01 → E05 → AR-E04**. A failed premise may complete a task with a scoped obstruction and return the named choice to B. E05 is conditional on an actual all-order proof contract. The existing B01 route remains independently selectable from E04; the new sequence does not erase that earlier option.

### MC11-AR-E01

**Type E; recommended Sol.** The route and formulas are specified, so this is analytic assessment rather than open model design. Inputs are Note06, Notes03–05 for interpretation, the radial companion, and the archived reference versions. It is ready for author-selected execution.

Assess the following in one proof pass with at most one local correction:

- Spectrum, multiplicity, chirality conventions, the product Dirac square and the full-line Green jump condition, for symbolic arbitrary \(n\ge1\).
- A sufficient self-adjoint realization on the complete cylinder; the meaning of its operator-valued radial kernel, heat-damped angular trace, and convergence for \(t>0\). Keep a kernel diagonal distinct from an operator trace on the full noncompact space.
- The stated half-line Dirichlet/Neumann kernels as second-order boundary problems. Do not assume either is the square of an independently chosen self-adjoint first-order boundary problem.
- The Euclidean reduced differential expression, measure change and spin-connection terms on \(r>0\), distinguishing this formal calculation from an origin or exterior-domain realization.
- The scope of Jacobi inversion, the remaining coordinate-dependent heat parameter, and the difference between \(D\), \(|D|\) and \(D^2\) as Hamiltonian choices.

**Deliverable and completion:** a review in `reviews/`, with a supporting analytic note in `brainstorm/notes/` if needed, accepting, correcting or rejecting each premise and recording exactly what BR01 may use. No quadrature, finite-mode scan, potential search or new sign claim. A failure requiring a new geometry, observable or boundary mechanism goes to **BR01**; ordinary normalization corrections remain within this task.

### MC11-BR01

**Type B; recommended Astra.** Preserve the existing brainstorm ID; this is its model-selection continuation, not a new name for MC11-B01. It consumes AR-E01's accepted premises or structural failure. The conceptual difficulty is choosing which features are physical and which belong to the source observation.

Compare at most **two** model contracts on paper: the product-cylinder Green response and a Euclidean spherical response. For each, state the configuration space, measure, spinor bundle, kinetic operator, radial domain, allowed potential class, boundary condition, observation and independent thermal/evolution parameter. Separate confinement of radial motion from the angular label \(n\); radial excitation energies need not equal \(\pi n^2\), and any trace over them must be accounted for.

Choose one route, or stop both within the tested classes. Decide explicitly whether a confining potential is necessary, whether the complete \(s=1\) source or the entire filter family is recovered, and whether the response is a Green observable, a density or a thermal trace. Specify how a spatial coordinate leads to the source argument \(t=\pi e^{4u}\), or retain that substitution openly as an external observation rather than a derived dynamical law. Identify the needed scalar-to-spinor encoding; do not assume a constant spinor on \(S^2\).

**Deliverable and completion:** one frozen analytic contract for AR-E02 and AR-E03, with the exact equations, domain, observation and intended general theorem, or a scoped reason to stop. Select at most one potential class and one boundary realization beyond the assessed free benchmarks. No inverse spectral fitting or numerical optimization. If the surviving construction only re-expresses the source, say what conceptual problem it resolves and leave determinant gain unclaimed. A new geometry or a third candidate requires a dated BR01 revision.

### MC11-AR-E02

**Type E; recommended Sol.** Conditional on BR01 fixing the radial problem, domains and observable. The route is angular separation followed by radial Green or resolvent analysis; the target concerns **all \(n\ge1\)**.

For the selected model, derive the separated channel operators, establish their domains and Green response, retain every boundary contribution, and evaluate or bound the coefficient replacing \(1/(4n)\). For a selected nonnegative second-order cylinder potential, start from the resolvent identity and comparison with the assessed free kernel. For a Euclidean selection, use its actual centrifugal channels and radial measure. Carry any radial trace or ground-sector restriction through the observation explicitly.

**Deliverable and completion:** one analytic theorem giving exact source recovery, or an explicit response defect with hypotheses and uniform remainder bounds, or a proved obstruction for the chosen potential/boundary class. Bounds must support the complete angular sum and the differentiations required by the frozen source contract; pointwise large-\(n\) asymptotics alone are insufficient. Use one selected operator class, one analytic derivation and at most one regrouping. No potential survey or acquisition. If multiplicity cancellation requires altering the readout, the potential class or the source, return to **BR01** before the dependent calculation.

### MC11-AR-E03

**Type E; recommended Sol.** Conditional on BR01's observation contract and the relevant AR-E02 theorem. This is the analytic bridge from the selected response to \(p_s,\Phi_s\), their source functions and exterior pairings.

Derive the source map with every measure factor, endpoint term and derivative. Establish a formula or recurrence for arbitrary derivative/moment index, with estimates that justify the infinite spectral sum and half-line integrals at each finite index. Distinguish a bound valid at each index from one uniform in that index. Cover only the filter settings actually recovered by the model.

Prove the resulting pairing identity for arbitrary finite \(q\), stating membership and domains without requiring source functions to be Hamiltonian eigenstates. Record the standard Fock-space extension and what physical preparation remains external. If the downstream contract calls for shifted blocks
\[
D_{q,k}(s)=\det[c_{k+j-i}(s)]_{i,j=0}^{q-1},
\]
check its precise index range and boundary terms; the neighboring diagonal shifts \(k=q-1,q,q+1\) are the first relevant family, not evidence for arbitrary filtered blocks. An identity for each \(q\) does not itself give an order-uniform sign estimate.

**Deliverable and completion:** one general-index source/pairing theorem with the exact operator-to-observable map, or a scoped incompatibility. One proof pass and one local correction, no moment table or finite-order campaign. A missing observation principle or a change of physical Hilbert space returns to **BR01**. A genuine signed-estimate choice belongs to **MC11-B01**.

### MC11-B01

**Type B; recommended Astra.** The existing task identity and at-most-two-route limit are retained from the [original contract](01_ENERGY_FILTERED_THETA_OVERLAPS_RESEARCH_OVERVIEW_20261104.md#mc11-b01). E04 already makes it available. Under the default new sequence it also consumes the angular/radial returns before deciding whether they improve an analytic estimate.

Compare at most two proof mechanisms for a specified signed cofactor sum, order-uniform remainder, or neighboring-shift relation. State the quantified hypothesis in \(q\), the coefficient shifts, angular index and filter parameter actually used. Identify the theta-specific premise and screen the controls below. Name an explicit dimension-dependent margin and account for the complete signed remainder; neither positive Green kernels nor small entrywise errors suffice.

**Deliverable and completion:** one noncircular analytic lemma and fixed proof route for **MC11-E05 — Sol**, or a scoped stop showing that the selected representation gives no new estimate. Classify an exact target reformulation as such. The author's 5 November direction narrows any earlier measurement option: a finite calculation is admissible only to test this written all-order hypothesis. No isolated order-four acquisition or increasing-order sign survey. If a potentially useful formula remains an unresolved design choice, retain it in B rather than issuing an unspecified execution task.

### MC11-E05

**Type E; recommended Sol.** Preserve the reserved ID. It is not executable until B01 freezes the lemma, source, domain, proof method, required index ranges, evidence standard and finite work limit.

Prove or refute that lemma analytically, including the order dependence of constants, all omitted spectral contributions and any boundary or neighboring-shift terms. The execution packet may allow one proof pass and one stated reformulation within the same mechanism. Its completion condition is a proof, a counterexample to the exact hypothesis, or a precise failed inequality. A finite list of favorable values cannot complete an all-order claim. Changing the mechanism or weakening the conclusion requires return to **B01**.

A numerical or low-index diagnostic is optional and must satisfy the separate gate below before it is issued. It is not the default E05 deliverable.

### MC11-AR-E04

**Type E; recommended Sol.** Conditional on a finished analytic return: assess the selected model/source results and E05 if activated. The route is a fixed claim-by-claim proof assessment, one pass with at most one local correction.

Check operator domains, normalizations, source equality, exchanged limits, index ranges, explicit order dependence, complete remainders, control failures and the distinction between a representation and a sign estimate. Reuse accepted E04 evidence without reacquiring its moments. **Completion:** an assessment in `reviews/` that accepts or rejects each claimed result and records the exact reusable scope. A structural model gap returns to **BR01**; a signed-estimate gap to **B01**. Record actual review provenance; switching model does not provide specialist independence.

## Controls and admissible hypothesis tests

Apply the [collision-control screen](../../../../../../../result-summaries/12_collision_controls_and_screening.md) and [shape-only caution](../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md) before promoting any proposed mechanism to a sign claim. Note06 already gives the following representation-level screen; it is not a new control computation.

| Control family | What survives the generic construction | Premise not shared with the canonical target |
| --- | --- | --- |
| Positive weighted-square sources | The same cylinder response with a shell multiplier \(a_n\), positive kinetic operator and exterior algebra | The complete unit coefficients; finite endpoint matches do not supply full normalized reflection |
| Euler-factor modifications | Positive even source and generic auxiliary Hilbert/exterior constructions | The unchanged canonical theta trace and arithmetic source; source positivity does not discriminate |
| Reflected super-Gaussian source | Reflection and generic Hilbert/Fock positivity | The literal complete integer-square theta expansion |
| Smooth shape and positive-primitive controls | Positive auxiliary channel, strong shape properties and the applicable endpoint identities | The exact canonical arithmetic source; a positive primitive does not determine the signed determinant |

For every proposed new inequality, B01 must check the actual premises against these controls and name the failed premise or counterexample. Merely insisting that the source is theta identifies the object; it does not prove the inequality. Scoped failures of the chosen Schrödinger or Green class remain scoped, following [avoid/07](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

A diagnostic request must record, **before calculation**:

1. A precise hypothesis quantified over all intended orders or indices, its proposed analytic mechanism, and the remaining proof gap.
2. Which finite case could falsify the hypothesis or decide between the declared mechanisms, and how each possible outcome changes the research decision.
3. A fixed finite case list, arithmetic/evidence standard, existing data to reuse, error and tail requirements, maximum refinement and stop rule. Prefer exact symbolic checks; numerical code and execution are E tasks for Sol.
4. A return to the analytic proof after the diagnostic. A favorable sample is only evidence of that sample. No extrapolated sign law, fitted all-order constant, automatic increase in order, or precision escalation is allowed.

No diagnostic is activated by this plan. The earlier order-two and order-three findings are inherited motivation, not a reason to certify further low orders. See [numerics before a question](../../../../../../../avoid/10_numerics_ahead_of_the_question.md) and [tests of the known](../../../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md).

## Records and continuation

Save discussion and incremental analytic notes from this conversation in `brainstorm/notes/`, as the author requested; save assessments in `reviews/`, and any authorized code and small execution records in `numerics/`. Reuse `references/` and follow [REFERENCE_WORKFLOW](../../../../../../../REFERENCE_WORKFLOW.md) and [LARGE_FILES](../../../../../../../LARGE_FILES.md). No new manuscript snapshot is planned.

The new progress file owns all current MC11 task status, including the inherited B01/E05 IDs. The previous register is historical; its frozen requests and returns remain intact. Record one writer, request revision, input versions, date, actual model/effort, accepted premises, corrections, failed routes and next task at each activation/return. See [shared-premise review](../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md) and [parallel writers](../../../../../../../avoid/17_parallel_writers_and_broken_registries.md).

**Next: [E] MC11-AR-E01 — Sol.** Assess the fixed angular/radial identities for the complete spectral family, returning the premises available for model selection.

> Read GPT_RESEARCH_MODEL_WORKFLOW.md, Overview02 and its sole current progress register. Complete [E] MC11-AR-E01 r1 using Brainstorm Note06 and the listed references. Assess the cylinder Dirac square, all-index Green response and multiplicity cancellation, half-line second-order boundaries, Euclidean differential expression and source-observation limitations. Use one analytic pass and at most one local correction; no numerical acquisition, spectral scan or new potential. Save a claim-by-claim review and return accepted premises or the precise BR01 decision required. Preserve the author’s requirement that low-order calculations only test a written all-order hypothesis.
