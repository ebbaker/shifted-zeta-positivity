# MC11-AR-E01 r1: angular/radial identity assessment

5 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**. Thread `01a1aa23-3513-7681-bad6-d8c15b6914fb`, MC11 history0003. **E — execution**, request r1, one analytic pass and at most one local correction. The author requested supporting research notes in `notes/`; [Note05](../notes/05_MC11_AR_E01_R1_ALL_INDEX_OPERATOR_AND_GREEN_DERIVATIONS_20261105.md) contains the derivations.

**Disposition: complete; accepted within the qualified operator/observable scope, with one local readout clarification R1.** No displayed Note06 equation needs an algebraic correction. The all-index full-line identity is valid for the specified complete product cylinder. Half-line D/N image terms remain, the Euclidean formula is a differential-expression result on r>0, and source-coordinate heat evaluation remains external. BR01 is ready for model selection. No signed determinant estimate is established.

## Inputs and review provenance

The [sole live register](../research-progress/02_ANGULAR_RADIAL_THETA_MODEL_RESEARCH_PROGRESS_20261105.md) froze seven inputs: Brainstorm Notes03–06, the reference catalog, download manifest and radial companion. Every hash matched at activation. The [version record](../research-progress/handoffs/05_MC11_AR_E01_R1_INPUT_VERSIONS_20261105.json) records the exact bytes, Overview02, register at activation, and the source versions checked. Issued Note06 and request r1 are preserved. Subsequent reference annotations are dated output, not substituted input.

This is a different-model internal LLM assessment of gpt-6-astra/xhigh Note06 by gpt-6.1-sol/ultra. A read-only Sol/ultra supporting agent supplied the Euclidean/Jacobi check and R1; the root chat is sole artifact writer. The supporting derivations and this assessment share author, model and imported spectral premises. Neither a model change nor a separate process supplies independent specialist review. See [avoid/05](../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md).

Primary-source inspection reused [Camporesi–Higuchi v1](https://arxiv.org/html/gr-qc/9505009), especially (3.54), the end of section 3.1 and (5.35)–(5.36), with the anti-Hermitian-to-self-adjoint convention stated. The existing archived PDF hash was verified. [DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32) was checked at z=0 and τ=ir² with its positive square-root branch. No scalar S³/oscillator result was imported into this angular assessment.

## Claim-by-claim return

Equation numbers in the first column refer to issued Brainstorm Note06. Note05 section numbers identify the supporting proof.

| Premise | Decision | Exact reusable scope and qualification |
| --- | --- | --- |
| Angular spectrum and heat trace (1) | **Accept** | Unit S², both Dirac signs ±n, 2n per sign, hence 4n for D²=n², every n≥1. No zero angular block. Note05 §1. |
| W and weighted trace (2) | **Accept** | W=(4|D|)⁻¹ is positive bounded, not trace class or a trace-one state. Scalar spectral-weight uniqueness follows from equality for every t>0, with convergence hypotheses; an arbitrary operator is fixed only through its block traces. Rotational symmetry alone does not select W. |
| Squared curvature formula (3) | **Accept** | D=-i slash-nabla on the unit sphere; D²=∇*∇+1/2. This is a geometric kinetic/heat operator, not a forced physical Hamiltonian. |
| Product metric and square (4)–(5) | **Accept, realization supplied** | On L²(R;K), the Fourier/direct-sum self-adjoint Dirac realization has weight k²+4n² in its graph domain; its square has squared graph weight. The smooth finite-angular core and Γ anticommutation establish the formula. The constant angular measure normalization does not alter multiplicity. Note05 §2. |
| Full-line Green kernel and jump (6)–(8) | **Accept** | For every n, derivative jump is -1, giving +δ under -∂². The bounded, norm-continuous angular-operator-valued kernel is exp(-2|D||v-w|)/(4|D|); its radial diagonal is W. This is not an unregularized angular point diagonal. Note05 §3. |
| Heat-damped response (9) | **Accept** | Tr_K[e^{-tD²}K(v,v)]=Q(t), t>0, all v∈R. Gaussian domination proves summability and each fixed t-derivative locally away from zero. The corresponding full-space trace is infinite. The square's Green kernel differs from the first-order inverse D_C⁻¹=D_C L⁻¹. |
| Half-line kernels (10) | **Accept as second-order problems** | H² Dirichlet and Neumann channel domains give the stated image terms. Their angular traces are Q(t)∓Σe^{-tn²-4nv}. The terms are nonzero at every finite v>0. No independently chosen self-adjoint first-order boundary problem has been squared in this argument. Note05 §4. |
| Scalar-potential separation (11) | **Accept conditionally as formulation** | A specified scalar V(v) with a valid second-order form/domain separates into channels. The coefficient becomes 4nG_{n,V}(v,v). No exact unit coefficient, confinement theorem, comparison bound or first-order-potential equivalence follows. Those depend on BR01 and AR-E02. |
| Cylinder/Euclidean metric (12) | **Accept** | g_E=4e^{4u}g_C, r=e^{2u}; product angular radius is fixed. Euclidean volume r²dr dΩ differs from cylinder volume. Note05 §5. |
| Euclidean reduction and square (13) | **Accept with explicit spinor identification** | Before radial conjugation D_E=-iΓ(∂_r+1/r)+D/r. Multiplication by r removes the 1/r connection term and changes r²dr to dr. The reduced square is -∂_r²+(D²+iΓD)/r². On each P_n, iΓD has ±n, 2n states each, giving n(n±1). This specifies expressions on r>0, not origin/exterior operator domains or their Green kernels. |
| Frozen-sphere trace preceding (14) | **Accept with R1** | Q(π/r²) uses the dimensionless unit-sphere W held fixed. The rescaled insertion (4|D/r|)⁻¹=rW gives rQ(π/r²). BR01 must name its readout. This is the sole local exposition clarification. |
| Jacobi inversion (14) | **Accept with source and origin scope** | Complete unit-weight source, r>0. Constant and 1/r corrections vanish under Δ_3 away from the origin, equivalently under ∂_u²-1 after source rescaling. The 1/r singularity cannot be ignored in a whole-space distributional claim. The ordinary filtered source has the explicit nonzero defect in Note05 (21). |
| Source construction (15) | **Accept as externally specified map** | t=πe^{4u}, e^u and the derivative observation recover the stated source from Q. The cylinder identity alone derives no spatially dependent physical heat time, radial dynamics, preparation of source functions or scalar-to-spinor encoding. Note05 §6. |
| Positive kinetic/exterior construction | **Accept representation; no sign implication** | D, |D| and D² have different spectral/thermal meanings. A positive Green response or Hilbert metric does not turn the auxiliary cross-pairing into a squared norm. No all-order or neighboring-shift determinant claim is assessed or supplied. |

## Controls and classification

Under [avoid/01](../../../../../../../avoid/01_restating_the_target.md), this return is an operator-domain and representation result, not an RH-equivalent criterion or a quantitative determinant milestone. The [result index](../../../../../../../result-summaries/README.md), [theta cluster](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [patterns index](../../../../../../../avoid/README.md), [re-realization warning](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md) and [control screen](../../../../../../../result-summaries/12_collision_controls_and_screening.md) delimit reuse.

| Control class | What the assessed construction retains | Canonical premise absent |
| --- | --- | --- |
| Positive weighted-square controls | Inserting a bounded nonnegative shell multiplier a_n into (10) yields Σa_ne^{-tn²}; the Green cancellation and positive kinetic operator survive | Exact complete unit shell coefficients; finite endpoint matches do not supply normalized full reflection |
| Euler-factor modifications | Positive source and generic auxiliary Hilbert/exterior representations remain available | Unchanged canonical theta trace and arithmetic source |
| Reflected super-Gaussian control | Reflection and generic Hilbert/Fock positivity | Literal complete integer-square expansion |
| Smooth shape and positive-primitive controls | Positive auxiliary channel, applicable shape/endpoint identities | Exact canonical arithmetic source; positive primitive data do not determine the signed determinant |

This is the analytic premise screen from the issued plan, not a new collision calculation. No new inequality is offered. Merely retaining the canonical source does not establish an inequality that separates these controls. Any later B01 sign proposal must test its actual quantitative hypotheses against them. Boundary and filter qualifications above are restricted to their specified classes, following [avoid/07](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## Completion and permitted continuation

All r1 assessment items have a disposition and supporting analytic argument. No quadrature, finite-mode scan, numerical acquisition, potential search or new determinant sign claim was used. R1 records the only local clarification; the issued equations and sources were not rewritten. The completed E task stops here.

**Next: [B] MC11-BR01 — Astra.** The [model-change continuation packet](../research-progress/handoffs/05_MC11_AR_E01_RETURN_AND_BR01_MODEL_CONTINUATION_20261105.md) identifies the model choice, exact accepted premises, dependencies and pasteable prompt. AR-E02 cannot start until its operator/domain/observation contract is frozen. The previously ready B01 route remains a separate author-selectable alternative.
