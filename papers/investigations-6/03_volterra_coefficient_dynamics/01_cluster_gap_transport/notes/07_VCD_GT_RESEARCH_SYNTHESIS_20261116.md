# Cluster gap transport — physical residual and fixed-event assessment

16 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance, branch chat0002. The source archive exposes no lead model/effort configuration. Proof and assessment helpers were explicitly dispatched **gpt-6.1-sol / ultra**; this records the dispatch, not separate backend attestation. All review is internal with shared source premises and disclosed contributor overlap, not specialist independence.

**Research synthesis, accepted within scope.** E01/E02 and E03 r1 were accepted in E05 r1/r2. [E05 r3](../reviews/05_VCD_GT_FIXED_EVENT_AND_SYNTHESIS_ASSESSMENT_20261116.md) accepted the fixed-event proof without mathematical correction and this synthesis after restoring an inherited source's height hypothesis; the reviewed versions and correction are recorded there. This status paragraph is the only later synthesis change. The session supplies physical-time error bounds, complete cluster-coordinate transfer, an exact finite-model heat defect, and a conditional fixed-event comparison. It acquires no canonical collision exclusion, useful canonical signed gap margin, numerical tube or completed descent to zero.

Read the [result index](../../../../../result-summaries/README.md), especially [controls12](../../../../../result-summaries/12_collision_controls_and_screening.md), [geometry13](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md) and [approximation18](../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md), and [avoid](../../../../../avoid/README.md), especially [01](../../../../../avoid/01_restating_the_target.md), [02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [15](../../../../../avoid/15_ignoring_sibling_results_and_unfinished_closures.md). The results below are intermediate estimates and a scoped estimator comparison, judged by their constants and rates. No global equivalent criterion is supported by finite checks.

## 1. Supporting obligations completed

[E01 / Note03](03_VCD_GT_E01_PHYSICAL_TIME_SIGNED_ERROR_20261116.md) extends the entire quadrature-error law and the explicit parent phase estimate uniformly over physical heat time 0<=lambda<=1/2. The coefficient and source-cosh bounds already had that time domain; the quadrature/simplex proof now carries it explicitly. The phase allowance remains O(|z|^2 log^2(N+1)/N) on |Im z|<=1, with its stated explicit constant and epsilon<1 gate for useful phase. N remains approximation degree. [Assessment02](../reviews/02_VCD_GT_E01_TIME_EXTENSION_ASSESSMENT_20261116.md) accepts the extension without mathematical correction.

A directed homotopy clearance also gives a log-ratio payment: divide a paid error-numerator bound by a positive lower bound for the homotopy denominator and integrate the homotopy parameter. A certified whole-contour clearance, compactness and holomorphy supply some analytic collar. E02 needs the log bound on the contour and existence of that collar. A specified wider collar or quantitative phase estimate beyond the strip needs its own payment; equal zero counts alone supply neither.

[E02 / Note04](04_VCD_GT_E02_COMPLETE_COORDINATE_TRANSFER_20261116.md) completes the two distinct transfers. On a circle of length L=2pi*rho with inner buffer b, collar-log bound ell_N, model logarithmic-derivative bound M_N and coordinate errors e_N,d_N, it proves

    |K-K_N| <= kappa_N
      = L ell_N/(pi b^3)
        + L M_N ((4rho-2b)e_N+d_N)/(2pi b^4).

The first term uses the same arguments; the second pays the change to the model's own center/discriminant. One may take e_N=rho*ell_N/2 and d_N=rho(2rho-b)ell_N. No reciprocal internal separation occurs. The signed primitive 4 integral K_N is retained, with the full integrated kappa_N and primitive-evaluation errors inside the exponential; outer cost quadrature is paid separately. [Assessment03](../reviews/03_VCD_GT_E02_COORDINATE_TRANSFER_ASSESSMENT_20261116.md) accepts the proof. These are supporting estimates, not evidence of a successful canonical margin.

## 2. The physical model defect and its actual coefficient cost

[B01](../brainstorm/notes/01_VCD_GT_B01_SIGNED_DEFECT_DECISION_20261116.md) selected signed contour transport for a concrete comparison. The alternative direct canonical gap/drift correlation had no acquired joint inequality. [E03 r1 / Note05](05_VCD_GT_E03_PHYSICAL_MODEL_DEFECT_20261116.md) derives, for N>=2,

    R_N := (partial_lambda + partial_z^2 + beta_1)G_N
         = beta_N beta_(N-1) partial_(beta_(N-1))G_N,
    R_N(z) = (-1)^(N-1) h_N* z^(2N-2)/(2N-2)! Psi_N(z),
    Psi_N = chi_N + z chi_N'/(2N-1).

Here chi_N is the transform of the uniform barycenter of the doubled N Gauss nodes, h_N*=product_(j=1)^N beta_j, and Psi_N=1+O(|z|^2 log^2(N+1)/N) on the paid strip, with explicit constants in Note05. At N=1, R_1=beta_1; the retained-edge derivative formula has no meaning there. N=2 is checked exactly against the cosine readout. This is the actual physical-time model residual, not an assumed heat equation for G_N.

For a counted model pair the additional term in its discriminant equation is

    r_N = -(2pi i)^(-1) integral_Gamma (z-c_N) R_N/G_N dz,
    D_N' = 2+4K_N D_N+r_N.

The term remains regular at a model double. The exact residual needs beta_N beyond G_N's first N-1 links. Those same first N links already specify G_(N+1). On any fixed punctured compact subset of the strip, the actual field comparison is

    |R_N(z)| / |F(z)-G_(N+1)(z)|
      = Pi_N / (beta_(N+1)|z|^4) (1+o(1)),
    Pi_N = (2N-1)(2N)(2N+1)(2N+2).

Uniform phase estimates pay the relative o(1); no lower bound for the omitted positive beta_(N+1) is assumed. Actual coefficient families, their certified evaluation over time and all contour geometry are still unacquired.

Note05 (19) gives the full ratio of the specified absolute residual-time allowance to the next-head contour-discriminant allowance, including both model floors, log factor, contour radius and time factor. For comparable fixed geometry it is of order Delta*N^4/log^2(N+1) when the same degree-only envelope pays the omitted link. This is a comparison of those selected allowances. It is not a lower bound for the true signed contour integral or for every transport algorithm. [Assessment04](../reviews/04_VCD_GT_E03_RESIDUAL_ASSESSMENT_20261116.md) accepts r1 without mathematical correction.

The exact signed margin identity also explains what remains to be estimated. With W_N=exp(4 integral_t^v K_N), e=D-D_N and mathfrak R_N=integral W_N r_N,

    W_N(u)e(u) = e(v)+mathfrak R_N
                 -4 integral_u^v W_N(K-K_N)D.

Computing mathfrak R_N through the model's endpoint identity simply recovers the original model signed-cost formula. An advantage requires a paid correlation/evaluation gain; the identity alone supplies none. This echoes the scope lesson of [S03's earlier endpoint comparison](../../../../investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/01_SIGNED_TRANSPORT_AND_DIRECT_JET_COMPARISON_20261018.md), whose separate theorem concerns a first-jet phase/norm and independent endpoint envelopes. That theorem is not asserted to dominate every GT estimator.

## 3. A fixed-event test of the actual signed contribution

[B02](../brainstorm/notes/02_VCD_GT_B02_FIXED_EVENT_DECISION_20261116.md) did not infer failure from the absolute allowance. It selected an actual contour calculation at one stipulated isolated real double event (T,a), 0<T<1/2, a nonzero. Let F_T(z)=(z-a)^2 A_T(z), A_T(a) nonzero, with a fixed small disk avoiding the origin, inside the strip. The hypothesis supplies local counted geometry, not a measured canonical event.

[E03 r2 / Note06](06_VCD_GT_E03_FIXED_EVENT_DEFECT_20261116.md) uses a fixed-circle logarithm expansion with factorial-small quadratic remainders to prove

    D_N(T) ~ L_N(T,a)/A_T(a),
    r_N(T) ~ -R_N(T,a)/A_T(a),
    r_N(T)/D_(N+1)(T) ~ -Pi_N/(beta_(N+1)(T)a^4).

The relative remainder estimates are essential: absolute o(1) would not justify these ratios. The defect r_N(T) has eventual sign (-1)^N sign(A_T(a)), so a degree-independent favorable sign is unavailable in this fixed-event class. This does not exclude parity-sensitive or jointly compensated methods.

For tau_N>0 with tau_N=o(N^-2), the unordered model roots remain o(1/N) from a on [T,T+tau_N]. Exact root averaging for r_N, uniform unit convergence and the norm-growth identity then give

    mathfrak R_N(T) ~ tau_N r_N(T),
    |mathfrak R_N(T)| / |D_(N+1)(T)|
      ~ tau_N Pi_N/(beta_(N+1)(T)a^4).

At tau_N=N^-3 the ratio is asymptotic to 16N/(beta_(N+1)(T)a^4), hence grows at least as N/log^2(N+1). At the stipulated event D(T)=0, so |D_(N+1)(T)| is the actual next-head discriminant error. Thus the degree loss survives the actual signed contour and time integral for this selected shrinking-slab comparison. The fixed-circle absolute safety allowance overestimates even that term by the geometric factor displayed in Note06 (11). Neither statement lower-bounds the complete correction: the incoming error and transfer terms in the preceding identity can cancel it.

There is also a conditional refinement of parent note27: the exact residual proves D_N'->D' uniformly on one fixed small event interval. Each sufficiently large degree therefore has exactly one model double time there, with

    lambda_N-T ~ -L_N(T,a)/(2 A_T(a)).

This gives its alternating displacement and uniqueness, rather than only the inherited existence/uncertainty window. It is fixed-event resolution; it is not uniform over heights, events or multiplicities and does not establish that any canonical event exists.

## 4. Controls and source scope

The exact quadratic heat control has K=0 and gap D(v)=2(v-T). Its cost is 2(v-u), exhausting the gap at u=T and exceeding it for u<T. It passes the local geometry and fails the infinite positive Jacobi-source premise of the degree asymptotics. It never certifies passage through its own event.

The three- and four-square positive-source controls have isolated events and share the specified uniform error/envelope premises. The fixed-event theorem consequently applies to their own physical fields. Full reflection and unchanged equal theta coefficients fail, but neither is used to obtain the residual comparison. Their local events do not imply finite all-real thresholds. Reflected, smooth/primitive and Euler controls retain their individual shared, failed and untested quantitative premises as listed in Notes03–06; absence of theta arithmetic is not called failure of an untested inequality. Atomic chains terminate. RH-conditional endpoint controls retain RH and lie outside r2's interior-time event hypothesis. Changed observations fail the literal Fourier/heat premise. No control certificate was rerun.

An additional inherited source-sensitive result was checked for relevance: [BW08 Note03](../../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/08_deflated_jet_hierarchy/notes/03_IMAGINARY_AXIS_JET_BOUND_20261019.md) gives a deflated-jet bound at a double of an **all-real** theta slice with T>0 and a>=20. Its status remains restricted analytic, proved in-note, same-assistant review. At the event its deflated curvature is -K(T). The global all-real slice premise is absent from this branch's general two-zero tube contract, and an event value alone is not the required time-integrated gap comparison. It is not discarded as false, imported into a different domain, or counted as a GT discovery.

## 5. Disposition and remaining work

B01/B02 and the authorized supporting/follow-through derivations form one connected session. The tested **absolute residual payment** has a quantified equal-coefficient loss, and its actual fixed-event signed contribution has the explicit comparison above. This is an informative scoped result, not a universal obstruction to signed transport. The extension and coordinate lemmas are reusable support. A canonical joint incoming-gap/exterior-drift inequality remains unproved.

There is no acquired L_v minus complete cost margin, no new canonical tube/count/modulus/buffer, no numerical coefficient family and no numerical certificate. E04 is unissued because no useful new finite diagnostic geometry was selected. E06 is unissued because no useful local margin and finite slab data exist to compose. No parent B07/E25 or sibling task was activated, and no manuscript or snapshot folder was created.

The next scientifically justified decision needs a concrete new source-sensitive joint estimate or an actually specified unresolved canonical tube with a comparator/gain question beyond the old known-covered pilot. Raising precision on that pilot, reissuing the same independent residual payment, or calling arbitrarily short steps a descent to zero is not a successor. Larger clusters, changing contours and high-height coverage retain their separate scope.

The [sole register](../research-progress/01_VCD_GT_RESEARCH_PROGRESS_20261116.md) owns task status. Requests/returns pin the proof inputs, [references](../references/README.md) record the limited de Boor passage check and related internal comparisons, and the [chat registry](../chat-histories/index.json) owns current capture provenance. Model/effort metadata remain unavailable for the lead rather than inferred from the requested setting. The real final reply is captured only after it is recorded and the exact turn completes.
