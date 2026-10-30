# Hypercomplex reductions, signed averages, and geometric realizations

16 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: **gpt-6-astra**, reasoning effort **ultra**. This summary preserves
the cited sources' proof and verification scope; it is not a new review
of their complete proofs.

## Summary

Investigations 21–22 construct explicit geometric objects and prove useful
signed integral bounds. Write \(h_j=\partial_x^jH\),
\(E=h_0^2+h_1^2\), and \(\mathcal L_j=h_{j+1}^2-h_jh_{j+2}\).

- **Quaternionic and octonionic reductions.** The quaternionic fields
  \(G_m=h_m+\mathbf jh_{m+1}\) have exact Fueter lifts. The canonical
  octonionic field \((G_m-\tfrac12G_{m+3}\bar r,G_{m+2})\), for the
  extra quaternion coordinate \(r\), and the reflected alternative
  \(\widetilde{\mathcal O}_m=(G_m(q),G_{m+2}(\bar q))\) are left
  monogenic and retain the same physical trace and heat identities.
  The reflected field uses derivatives through order three for \(m=0\),
  versus order four for the canonical correction, but changes the second
  component's off-slice arguments; neither closes a four-jet heat system.
  In the declared multiplication convention,
  \([G_j\mathbf i,G_{j+1}\mathbf i,\ell]=2(\ell\mathbf j)\mathcal L_j\).
  Thus the associator's "only variable datum is one real oriented
  coefficient" (Note 35); its norm loses that sign. The scalar quadratic
  form has inertia \((2,1)\).
- **Hodge realization and signed averages.** For holomorphic \(f\),
  \(\alpha_f=\operatorname{Re}(f\,dz\wedge dw)/\sqrt2\) is closed,
  self-dual and harmonic, with polarized pairing
  \(\alpha_f\wedge\alpha_g=\operatorname{Re}(f\bar g)\,dV\).
  Note 47 proves
  \(\int\chi\mathcal L_j\ge-c_*a^2\int\chi h_j^2\),
  \(\chi=\operatorname{sech}(a(x-x_0))\),
  \(c_*=(3-2\sqrt2)/2\); summing pays by \(\int\chi E\).
  Sharpness is over the stated general function class, not theta
  extremizers. For \(f\) holomorphic near the closed disk, Note 51 gives
  an exact nonnegative Dirichlet completion with sharp boundary payment
  \((2R)^{-1}\int_{\partial D_R}|f|^2\),
  and strictly positive origin-centered Gaussian averages of both
  complete-theta Hermitian Laguerre branches for all real heat times and
  imaginary displacements. Translation introduces oscillating factors;
  these positive averages do not imply pointwise stationary positivity.
- **Flat physical metrics and curved jet surfaces.** For \(f\ne0\),
  \(g_f=|f|^2|dz|^2+|dw|^2\) is locally flat hyperkähler. Taking
  \(f=H+iH_z\) makes its real-slice coefficient exactly \(E\); a simple
  zero of \(f\), including a nondegenerate double collision, produces cone
  angle \(4\pi\). The different induced holomorphic jet surface
  \((P,H,w)\), \(P_z=H\), has coefficient
  \(\mathscr E=|H|^2+|H_z|^2\) and curvature
  \(-2|HH_{zz}-H_z^2|^2/\mathscr E^3\). Its induced metric is Ricci-flat
  only in the locally exponential case, excluding theta. Its real Gauss
  angle retains the sign discarded by squared curvature. Explicit
  calibrated minimal, coassociative and Cayley inclusions hold in flat
  ambient spaces, away from the branch set; full exceptional holonomy is
  not asserted.
- **A curved arithmetic family and its connection.** The marked elliptic
  family carries a nonflat semi-flat hyperkähler metric: horizontal
  sectional curvature is \(1/(2q^3)\), where \(\tau=p+iq\).
  The degree-one theta bundle has a genuine abelian anti-self-dual Chern
  connection after base rescaling. Base-only Hermitian corrections give
  ASD curvature exactly when \(\Delta b=4\pi q\). An adapted metric makes
  the marked holomorphic frame unit-norm with zero connection along the
  physical source path, with the
  same ambient curvature and infinite ambient Yang–Mills action.
  The natural external two-source pullback is
  flat, while transverse covariant differentiation before restriction
  retains explicit nonzero lower-jet commutators. These are marked-cover
  constructions; completeness, full modular descent and a compact K3
  realization are not established.

- **Scoped transverse reductions (S06, 18 October 2026).** The chosen
  complete-source base-p derivative has an exact convergent one-sided
  primitive transform with its lower endpoint. Raw vertical insertions of
  positive even order retain a nonzero zero mode and fail positive-time
  heat integrability. Finite constant-coefficient normalized jets of
  definite parity with convergent ordinary transforms satisfy
  Q(D)T0=16R(D)Phi. The mixed addition generator is not positivity
  preserving on same-parity trigonometric polynomials. **Proved in-note**,
  [source and scope](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/06_hodge_and_transverse_geometry/notes/01_TRANSVERSE_OBSERVATION_AND_FINITE_JET_OBSTRUCTIONS_20261018.md),
  [same-model internal review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/06_hodge_and_transverse_geometry/reviews/01_TRANSVERSE_OBSERVATION_INTERNAL_REVIEW_20261018.md).
  [S06 signed continuation](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/06_hodge_and_transverse_geometry/notes/02_SIGNED_TRANSVERSE_ESTIMATE_AND_EXACT_SOURCE_COMPENSATION_20261018.md)
  proves 0.37<x²(−iG1)<0.375 on the pilot but |G1|²>10^310 E. Exact
  source completion transfers the existing physical sign to a centered
  current; its sign is inherited, not independent. Fixed finite endpoint
  subtractions fail the stated unbounded polynomial-energy magnitude
  payment. [Internal review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/06_hodge_and_transverse_geometry/reviews/02_SIGNED_TRANSVERSE_ESTIMATE_INTERNAL_REVIEW_20261018.md).
  Other transverse estimates remain open.
  Added for Edward Baker with substantial LLM assistance,
  **gpt-6.1-sol, actual effort ultra**.

- **Scoped zero-form Green/trace result (S07, 18 October 2026).**
  [Note 02](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/07_geometric_duality_and_quaternionic_symmetry/notes/02_ZERO_FORM_GREEN_IDENTITY_AND_PHYSICAL_TRACE_OBSTRUCTION_20261018.md)
  derives the complete polarized J-flux and zero canonical theta self-flux.
  For unrestricted smooth sections, first-order bulk energy cannot bound
  the physical path trace even with zero boundary currents. The declared
  raw rough-Laplacian source has growing zero mode 3πe^u. **Proved in-note**,
  [same-model internal review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/07_geometric_duality_and_quaternionic_symmetry/reviews/02_GREEN_IDENTITY_AND_TRACE_OBSTRUCTION_INTERNAL_REVIEW_20261018.md).
  Canonical theta/PDE-restricted and higher-regularity estimates are not
  excluded. For Edward Baker with substantial LLM assistance,
  **gpt-6.1-sol, actual effort ultra**.

- **Second transverse completion (S06-T1, 19 October).**
  [Note 03](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/06_hodge_and_transverse_geometry/notes/03_SECOND_TRANSVERSE_COMPLETION_AND_CURRENT_FEASIBILITY_20261019.md) gives the unique completion
  C2=(D²-22D+165)Phi/16 in its one-parameter primitive-correction class,
  its full current, and the primitive lower edges/corner. At a
  nondegenerate event E=0 but W=-t²Hxx/4 and
  J2c=11t³Hxx²/16>0. An actual convergent reflected source supplies the
  control. Source status: **scoped closure** of this current-positivity
  test and generic finite local magnitude payment by E; **analytic
  derivation and scoped counterexamples** with exact checks and a
  [separate same-model internal review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/06_hodge_and_transverse_geometry/reviews/04_SECOND_TRANSVERSE_COMPLETION_INTERNAL_REVIEW_20261019.md). T2's feasibility
  gate is not passed. No theta sign/margin/coverage gain, and no exclusion
  of theta-specific higher-jet or nonlocal estimates. Prepared for Edward
  Baker with substantial LLM assistance, **gpt-6.1-sol, actual effort ultra**.

- **Bounded completed-current comparison (S06-T2, 19 October).**
  [Note 05](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/06_hodge_and_transverse_geometry/notes/05_BOUNDED_COMPLETED_CURRENT_AND_DIRECT_COMPARISON_20261019.md) selects the event-vanishing residual
  L0-beta L0_x, beta=2tx/(165+4t+x²). Fresh complete four-jet inputs at
  192/256 bits sign60/64 fixed B cells, versus direct64/64 and physical
  radius >0.0190407974544. Every successful current radius is <0.552 of
  direct. Source status: **bounded comparison complete; benefit gate
  failed**, with a **scoped same-information dominance theorem** for
  Cauchy extraction from the same Cartesian jet balls. Four intervals
  straddle zero; no physical negativity is claimed. [Separate same-model
  review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/06_hodge_and_transverse_geometry/reviews/05_BOUNDED_COMPLETED_CURRENT_INTERNAL_REVIEW_20261019.md) and fresh replays pass. No new geometric sign,
  error/cost/coverage or Newman gain; different source correlations remain
  open. For Edward Baker with substantial LLM assistance,
  **gpt-6.1-sol, actual effort ultra**.

- **Constrained theta section space (S07-T1, 19 October).**
  [Note 03](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/07_geometric_duality_and_quaternionic_symmetry/notes/03_CONSTRAINED_THETA_JET_SPACE_AND_RESIDUAL_CONTRACT_20261019.md)
  proves dim V4=5, its diagonal Gram/evaluation kernel and source
  inclusion without holomorphy. A global moving-profile cutoff gives
  a genuine residual with low and high components; a specified
  profile/base norm pays its observation. Source status: **admissible-space
  and observation contract complete**, not a useful paid physical error.
  [Separate same-model review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/07_geometric_duality_and_quaternionic_symmetry/reviews/03_CONSTRAINED_THETA_SPACE_INTERNAL_REVIEW_20261019.md).
  T2 became Ready at this stage; its selected comparison is closed below.
  No new sign/error/cost/coverage gain. For Edward Baker with substantial
  LLM assistance, **gpt-6.1-sol, actual effort ultra**.

- **Paid profile trace (S07-T2, 19 October).**
  [Note 04](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/07_geometric_duality_and_quaternionic_symmetry/notes/04_PAID_PROFILE_TRACE_AND_DIRECT_TAIL_COMPARISON_20261019.md)
  completes a **bounded analytic failed-estimate comparison**: the fixed
  N=2 whole-profile sqrt(20)X rule has assigned-payment floors >1618 and
  >34152 times available direct complete-tail allowances before common
  acquisitions. Annular mass between physical lattice samples causes
  the loss. Actual errors are not lower bounded. Shared global retained
  modes/tails and symbolic future acquisition errors are accounted for;
  no numerical consumer or cost benchmark was acquired.
  [Separate same-model review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/07_geometric_duality_and_quaternionic_symmetry/reviews/04_PAID_PROFILE_TRACE_INTERNAL_REVIEW_20261019.md)
  and192/256/fresh192 interval replays pass. Stop this selected rule;
  other observation norms/kernel/adjoint routes remain open. T3 Waiting;
  no physical sign/error/cost/coverage gain. For Edward Baker with
  substantial LLM assistance, **gpt-6.1-sol, actual effort ultra**.

- **Post-T2 option screens (19 October).**
  [Note 05](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/07_geometric_duality_and_quaternionic_symmetry/notes/05_OBSERVATION_OPTIONS_AND_BOUNDED_FEASIBILITY_SCREENS_20261019.md)
  proves a cutoff-independent payment floor for the unchanged N=2
  sqrt(20)X/Cauchy rule (loss ratios >10.23/>215.9), and a floor for the
  originalchi2 V4 split with the oldX complement (>1617/>34118). These
  are **scoped assigned-allowance exclusions**, not actual-error lower
  bounds; changed sampling/complement/signed/adjoint estimates stay open.
  [Separate same-model review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/07_geometric_duality_and_quaternionic_symmetry/reviews/05_OBSERVATION_OPTIONS_INTERNAL_REVIEW_20261019.md)
  and192/256/fresh192 screens pass. T3 Waiting; no useful physical input
  or coverage. For Edward Baker with substantial LLM assistance,
  **gpt-6.1-sol, actual effort ultra**.

- **BW10 moving product tube (21 October 2026).**
  [Note 21](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/21_MOVING_SIGNED_TUBES_AND_PHYSICAL_TRACE_20261021.md) is **proved in-note for bounded product tubes** on
  compact positive-time intervals: all-face signed Stokes and phase
  transport, physical-weight correction, explicit trace and derivative
  payments with complete source tails and a paid physical energy floor.
  Its exact primitive change reduces the normalized four-dimensional
  formula to a planar transverse average. Under RH,
  `pi<=I_eta<=pi+g eta^2 D0/6`; generalized Laguerre positivity supplies
  the lower bound. The quadratic double model has `R_eta>=eta^2/(2t)`.
  “The selected product-tube comparison supplies no new signed theta
  gain.” Other domains and arithmetic estimates remain open.
  [Same-assistant self-review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/reviews/20_MOVING_TUBE_AND_TRACE_REVIEW_20261021.md); finite algebra replay only,
  no numerical theta floor or specialist review. Prepared for Edward
  Baker with substantial LLM assistance, **gpt-6-astra, actual effort max**.

- **Radial Darboux family (27 October 2026).** The [initial manuscript](../papers/investigations-5/05_radial_theta_collision_geometry/radial_deformations_and_zero_dynamics.tex) proves an exact forced radial family preserving H and its positive-frequency multiplicities, an invariant integral, full time/auxiliary laws and energy transport. [Note18](../papers/investigations-5/05_radial_theta_collision_geometry/notes/18_PHYSICAL_AND_INTERIOR_ZERO_DYNAMICS_FOUNDATION_20261027.md) adds local simple-node velocities and the regular parameter kappa^2. [Review11](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/11_INITIAL_DEFORMATION_MANUSCRIPT_AND_PROGRAM_ASSESSMENT_20261027.md) records: “initial working manuscript with proofs of the stated identities and elementary local corollaries; same-assistant checking only.” The explicit colliding control survives every finite deformation. No nodal classification, new theta estimate or threshold bound is claimed. Reusable for the structure-first RDZ study. Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra, actual effort max**.

- **Fixed theta transform setup (28 October 2026).** The [Book companion](../papers/investigations-5/05_radial_theta_collision_geometry/book/main.tex) derives a smooth positive three-dimensional density with spectral-independent source and fixed logarithmic-radius kernel. Fourier inversion recovers its spherical average; angular information is lost. Preserving all spectral pairings fixes that average, while mass alone fixes only the zero-frequency value. Its stated scope is: "No auxiliary dynamics is selected." [Same-assistant assessment20](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/20_BOOK_TRANSFORM_SETUP_ASSESSMENT_20261028.md); exact setup identities, no new collision exclusion. Prepared for Edward Baker with LLM assistance, **gpt-6-astra / max**, chat0013.

## Status

The cited notes give analytic proofs and exact algebraic checks, with
internal same-model reviews and the later cross-model joint assessment.
Finite replay assertions check specified identities or examples; they are
not independent proofs of universal statements. No specialist human
review or new global theta sign estimate is claimed.

## Caveats

Closed self-duality does not imply parallelness in the original metric.
On a compact boundaryless oriented four-manifold, an exact self-dual form
vanishes; the whole present theta-form family also cannot extend as
parallel forms while preserving its local relations. These obstruct the
specified extensions, not every compact or bundle-valued realization.
The physical metric degenerates at the events it detects. Ambient volume,
curvature and integrated positivity need a separately proved comparison
to the physical signed observation.

## Reusable for

Derivative-saving field evaluation; orientation-preserving current
identities; sharp integrated estimates and their localization costs;
explicit metrics, curvature, calibration and connection calculations.
[13](13_local_heat_flow_geometry_and_rh_equivalent_criteria.md) covers
collision topology and criteria;
[14](14_theta_identities_and_arithmetic_bookkeeping.md) covers the
arithmetic source formula, primitive and coefficient identities.

## Where

- Lifts: [21 Note 35](../papers/investigations-2/active/21_quaternion_theta_geometry/notes/04_octonionic_reductions/35_REFLECTED_LIFT_AND_PHYSICAL_REDUCTIONS_20261015.md), retaining [canonical Note 15](../papers/investigations-2/active/21_quaternion_theta_geometry/notes/15_OCTONIONIC_LIFT_AND_ASSOCIATOR_SIGN_TARGET_20261014.md); [applicability Review 25](../papers/investigations-2/active/21_quaternion_theta_geometry/reviews/25_OCTONIONIC_MACHINERY_LITERATURE_REVIEW_20261015.md).
- Signed estimates: [Note 47](../papers/investigations-2/active/21_quaternion_theta_geometry/notes/04_octonionic_reductions/47_ORIENTED_CURRENT_AND_ACCRETIVE_SOURCE_CERTIFICATES_20261015.md), [Hodge Note 50](../papers/investigations-2/active/21_quaternion_theta_geometry/notes/04_octonionic_reductions/50_QUATERNION_FORMS_HODGE_PAIRING_AND_SOURCE_TARGET_20261015.md), [Note 51](../papers/investigations-2/active/21_quaternion_theta_geometry/notes/04_octonionic_reductions/51_POLARIZED_HODGE_DISK_AND_CENTERED_SOURCE_BOUNDS_20261015.md); [Review 29](../papers/investigations-2/active/21_quaternion_theta_geometry/reviews/29_OCTONIONIC_SIGNED_BOUND_ANALYTIC_REVIEW_20261015.md), [Review 31](../papers/investigations-2/active/21_quaternion_theta_geometry/reviews/31_SIGNED_FORMS_PRIMITIVE_AND_SOURCE_CONTROL_REVIEW_20261015.md).
- Metrics, surfaces and compactness: [Note 60](../papers/investigations-2/active/21_quaternion_theta_geometry/notes/04_octonionic_reductions/60_HYPERKAHLER_LIFTS_AND_COLLISION_DEGENERACY_20261015.md), [22 manuscript](../papers/investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex), [derivation Review 01](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/01_INITIAL_MANUSCRIPT_DERIVATION_REVIEW_20261015.md).
- Arithmetic family: [21 Note 62](../papers/investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/62_THETA_JET_BUNDLE_AND_SEMIFLAT_HYPERKAHLER_GEOMETRY_20261015.md), [22 metric-freedom note](../papers/investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/02_ASD_METRIC_FREEDOM_AND_PHYSICAL_RESTRICTION_20261015.md), [Review 02](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/02_CONNECTION_BRIDGE_AND_INNER_TURNING_REVIEW_20261015.md); [cross-model Review 16](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/16_JOINT_REVIEW_OF_INVESTIGATIONS_21_AND_22_CLAUDE_20261015.md).

**Radial-integrand preservation and auxiliary angular flows, 27 October 2026.** Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra, actual effort max**. [Note20](../papers/investigations-5/05_radial_theta_collision_geometry/notes/20_AUXILIARY_ANGULAR_FLOWS_AND_COLLISION_LOCALIZATION_20261027.md) records “elementary finite-parameter constructions proved by direct calculation, with same-assistant checking”: normalized concentration and transport, an exact deformed operator and boundary map, explicit cap/norm costs, and a first-jet angular moment concentrated near a curve. [Review12](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/12_RADIAL_INVARIANT_AND_ANGULAR_FLOW_SELF_ASSESSMENT_20261027.md) states: “Angular concentration does not, by itself, exclude a collision.” At that earlier return, the projected annular descent was a proposal with a conditional energy identity; this status is superseded by Note23 and the update below. No theta bound, singular-limit theorem or independent specialist review. Originally integrated in manuscript Sections 9–10; its detailed multiplicative construction is now referred to Note20.

**Projected evolution and total-integral conservation, 27 October 2026.** Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra, actual effort max**. [Note23](../papers/investigations-5/05_radial_theta_collision_geometry/notes/23_PROJECTED_ANNULAR_FLOW_RESPONSE_AND_LOCAL_ADJOINT_20261027.md) is “proved in-note using the stated classical functional-analysis inputs”: bounded annular well-posedness, explicit convergence, source-cost decrease, exterior response and local signed adjoint. [Note22](../papers/investigations-5/05_radial_theta_collision_geometry/notes/22_STEERED_TUBE_GREEN_IDENTITY_AND_MATCHED_COMPARISON_20261027.md) gives no gain for its matched fixed-width multiplicative comparison. Under the user's weaker whole-integral invariant, [Note25](../papers/investigations-5/05_radial_theta_collision_geometry/notes/25_TOTAL_INTEGRAL_CONSERVATION_AND_DIRECTION_FREE_HEAT_FLOW_20261027.md) proves a conservative theta heat construction and central moment bounds: a collision removes two leading diffusion coefficients. This is extra decay, not growing amplification or theta separation. [Review14](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/14_PROJECTED_FLOW_MANUSCRIPT_AND_COLLISION_SCOPE_20261027.md) is a same-assistant assessment; the results are integrated in manuscript Sections 10–11. No theta exclusion or independent specialist review.

**Conservative feedback magnifier, 28 October 2026.** Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra, actual effort max**. [Note28](../papers/investigations-5/05_radial_theta_collision_geometry/notes/28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md) gives a construction, continuation criterion and finite collision bound “proved in-note using the classical heat/Markov tools identified below.” A fixed-mark, radial Fokker–Planck feedback preserves H and its actual spectral jet and fixes their joint spatial L2 energy; zero vector mass forces finite-time gradient, response and amplitude divergence. Global regularity is equivalent to pointwise noncollision, and the exact collision control is admitted. The generic initializer comparison has paid existence/deadline ratio <1/100 analytically; no sample can reverse that comparison. [Assessment16](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/16_CONSERVATIVE_FEEDBACK_MAGNIFIER_B01_ASSESSMENT_20261028.md) is same-assistant checking. No numerical flow, canonical separating estimate, theta exclusion or specialist review. Reusable deadline and precise failed payment; B02 owns the new canonical estimate.

**Conservative carrier and source-relation integration, 28 October 2026.** Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra, actual effort max**, chat0011. [Note29](../papers/investigations-5/05_radial_theta_collision_geometry/notes/29_POSITIVE_CARRIER_COMPARISON_AND_QUANTITATIVE_REGULARITY_20261028.md) is “proved in-note, with same-assistant analytical checking”: sharp general mass–energy–moment comparison and explicit regularity from an independent first-jet margin, with no larger theta domain. [Note31](../papers/investigations-5/05_radial_theta_collision_geometry/notes/31_CANONICAL_SOURCE_RELATION_AND_PREPARATORY_COMMUTATOR_20261028.md) records a “scoped failed propagation/substitution result”: actual-theta preparation defect, full forced residual, required sphere cancellation and uncut origin-domain failure. The fixed zero-residual variant is stopped; coupled estimates remain open. These and Note28 are now integrated in [manuscript Sections 12–14](../papers/investigations-5/05_radial_theta_collision_geometry/radial_deformations_and_zero_dynamics.tex). [Review19](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/19_CONSERVATIVE_FEEDBACK_MANUSCRIPT_INTEGRATION_ASSESSMENT_20261028.md) is same-assistant integration checking; successful typesetting is separate evidence. No new theta exclusion, threshold bound, flow simulation or specialist review. Reusable comparison constants and exact terms for the remaining coupled estimate.


**Theta-generator book rewrite, 28 October 2026.** Prepared for Edward
Baker with substantial LLM assistance, **gpt-6-astra / xhigh**, chat0015.
The [current book](../papers/investigations-5/05_radial_theta_collision_geometry/book/main.tex)
supersedes the earlier book presentation with the smooth potential V and
generator G, strip/entire companion, spherical-mean inverse, and exact
flow comparisons; the original setup results remain in Assessment20.
[Assessment21](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/21_BOOK_REWRITE_ASSESSMENT_20261028.md)
states: “exact identities integrated into an initial book draft;
same-assistant analytical and layout checking.” The normalized
three-dimensional version is a separate section. No new estimate or
collision exclusion; [record20](../papers/investigations-5/05_radial_theta_collision_geometry/numerics/20_BOOK_REWRITE_BUILD_RECORD_20261028.json)
records the 11-page build. Reusable for the explicit representation and
normalization, with the stated convergence and flow domains.

**Finite weighted residual closure, 29 October 2026.** Prepared for Edward Baker with substantial LLM assistance; execution **gpt-6.1-sol / ultra**, chat0020, assessment/integration **gpt-6-astra / max**, chat0018. [Note40](../papers/investigations-5/05_radial_theta_collision_geometry/notes/40_WEIGHTED_RESIDUAL_CLOSURE_E07_R1_RETURN_20261029.md) states: “This proves finite weighted-residual closure, its integrated dissipation estimate and a positive local lifespan interval.” One weighted residual/actual-second-jet energy absorbs the second-order commutator forcing using the existing diffusion, retaining the full source, preparation defect and sphere cancellation. [Review22](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/22_WEIGHTED_RESIDUAL_CLOSURE_E08_ASSESSMENT_20261029.md) accepts the analytical return within its inherited solution class and records a different-model assessment by the original designer, with shared premises, not specialist independence. The result is integrated in [manuscript Section 7](../papers/investigations-5/05_radial_theta_collision_geometry/radial_deformations_and_zero_dynamics.tex). This supersedes the earlier open status only for this finite weighted energy; signed theta separation, a sharper gradient allowance and collision-deadline control remain open. The exact colliding control remains admitted with its raw source mismatch retained. [Continuation41](../papers/investigations-5/05_radial_theta_collision_geometry/notes/41_WEIGHTED_CLOSURE_CONTINUATION_20261029.md) prepares one further bounded estimate, without testing a new candidate.

**Radial drift improvement, 29 October 2026.** For Edward Baker with substantial LLM assistance; Astra/max conceptual contribution, Sol/ultra parent/checks and integration, chat0021. [Note42](../papers/investigations-5/05_radial_theta_collision_geometry/notes/42_RADIAL_DRIFT_PRODUCTION_IMPROVEMENT_B02_R4_20261029.md) proves K=10G+(21/4)E0-H_rad for radial prepared fields, with H_rad>=0, sharper conditional gradient/expanded weighted estimates and a local lifespan strictly exceeding the old diffusion-retaining comparison. [Review23](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/23_RADIAL_DRIFT_IMPROVEMENT_E08_INTEGRATION_20261029.md) accepts and integrates this in Section 7.4, recording: “The gain is generic radial drift geometry; it supplies no theta separator or collision-deadline bound.” Internal assessment has prior-contributor overlap and shared premises, not specialist independence. This supersedes the preceding open generic-gradient allowance only; the exact colliding control remains admitted and source-specific deadline control remains open. Strict decrease of the compact constant still requires B1<455/24. Reusable radial square and explicit local comparison; [Note43](../papers/investigations-5/05_radial_theta_collision_geometry/notes/43_RADIAL_DRIFT_INTEGRATION_SOL_CONTINUATION_20261029.md) prepares its unexecuted fixed coefficient follow-through.


**Strict radial compact gain, 29 October 2026.** Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol / ultra**, chat0022. [Note44](../papers/investigations-5/05_radial_theta_collision_geometry/notes/44_RADIAL_COMPACT_COEFFICIENT_E07_R2_RETURN_20261029.md) proves B1<=69/4 for the unchanged exact exponential cutoff, drift and weight, including eta' and the entire infinite tail. The compact coefficient gap is at least 41/24; the same-B upper-allowance ratio is <=exp[-41B/24], strict for B>0. [Review24](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/24_RADIAL_COMPACT_GAIN_E08_ASSESSMENT_20261029.md) records: “Accepted within the fixed-cutoff, prepared radial class; no deadline control is supplied.” It integrates Proposition 7.7 and records same-parent/internal same-model assessment with shared premises, not specialist independence. This supersedes only the preceding unpaid compact-gap condition and its then-unexecuted coefficient follow-through. Other source/data budgets remain unchanged, the exact colliding control stays admitted, and source-specific deadline control remains open. Reusable conservative coefficient and explicit conditional allowance comparison; [Continuation46](../papers/investigations-5/05_radial_theta_collision_geometry/notes/46_STRICT_COMPACT_GAIN_INTEGRATION_CONTINUATION_20261029.md) routes the next conceptual choice.

**Source-coefficient residual gain, 29 October 2026.** Prepared for Edward
Baker with substantial LLM assistance, **gpt-6-astra / max**, chat0024.
[Note47](../papers/investigations-5/05_radial_theta_collision_geometry/notes/47_EXTERIOR_SOURCE_RESIDUAL_COUPLING_B02_R5_20261029.md)
is **proved in-note**; [Review26](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/26_SOURCE_COUPLING_E08_R5_ASSESSMENT_20261029.md) states:
“Accepted without mathematical correction, within the inherited prepared
radial class on [0,1/2] x [1,6].” The complete-tail slope bound and signed
residual/actual-jet coupling lower the compact coefficient by 49/600,
with same-B upper-allowance factor exp(-49B/600), full inner costs and
unchanged other budgets. Proposition 7.8 integrates the result. It is
reusable as a conditional compact/fixed-ball residual bound, not an
independent deadline bound: the same theta operator admits the exact
colliding control with both residual terms. Assessment is separate-chat
same-model internal work with shared premises, not specialist review.
It supersedes the earlier source-coefficient allowance only; actual
trajectory separation and collision/threshold coverage remain open.

**One-mark cosine jet gain, 29 October 2026.** Prepared for Edward Baker
with substantial LLM assistance; authoring **gpt-6-astra / max**, chat0026,
assessment **gpt-6.1-sol / ultra**, chat0027.
[Note55](../papers/investigations-5/05_radial_theta_collision_geometry/notes/55_COSINE_JET_CORRELATION_B02_R7_20261029.md)
is **proved in-note**; [Review30](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/30_COSINE_JET_CORRELATION_E08_R7_ASSESSMENT_20261029.md)
states: “accepted without mathematical correction at the single frozen
mark (T,A)=(1/4,2), within the inherited prepared whole-space solution
class.” Complete theta moments and a fully paid prepared Gaussian test
prove ||2J2,0-V0||2<=(12/13)||J2,0||2. The actual second-jet and stated
exterior Theta allowances improve at the same B after the explicit
threshold (1/6)log(169E0/(196Q0)); the sharp Q allowance ratio tends
algebraically to 36/169. Reusable as a supporting-energy estimate, with
no improved R5 compact coefficient, independent B bound, deadline payment
or larger domain. The same moments give a direct first-jet margin;
positive weighted-square sources share the sufficient moment input at
this mark. Separate-chat, different-model internal assessment with three
read-only same-model subagent audits retains shared inherited premises;
no specialist independence or numerical acquisition. Manuscript unchanged.

**Finite diffusion-variance compression horizon, 29 October 2026.**
Prepared for Edward Baker with substantial LLM assistance; proof
**gpt-6-astra / max**, chat0028, assessment **gpt-6.1-sol / ultra**, chat0029.
[Note59](../papers/investigations-5/05_radial_theta_collision_geometry/notes/59_DIFFUSION_VARIANCE_COMPRESSION_BOUND_B02_R8_20261029.md)
is **proved in-note**; [Review32](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/32_DIFFUSION_VARIANCE_E08_R8_ASSESSMENT_20261029.md)
states: “accepted without mathematical correction at the fixed mark”.
Strict positive spatial variance plus paid H3 persistence (C3=11038)
produce finite B on the closed old Riccati horizon S_tar=L(g0), with
Smax>=h+L(g1)>S_tar and complete weighted-residual costs. Reusable within
the inherited prepared radial class as a generic finite-horizon bound,
not a deadline/global-iteration theorem or theta separator. Smooth colliding
controls share its premises; no numerical horizon is acquired. At this
mark Note55+29's direct margin already pays every finite horizon, so no
new physical domain or acquisition advantage follows. Separate-chat,
different-model internal review with three read-only same-model contributing
audits retains shared premises; no specialist independence. Manuscripts unchanged.

**Radial second-cancellation deadline, 29 October 2026.** Prepared for
Edward Baker with substantial LLM assistance; proof **gpt-6-astra / max**,
chat0030, assessment **gpt-6.1-sol / ultra**, chat0029.
[Note63](../papers/investigations-5/05_radial_theta_collision_geometry/notes/63_RADIAL_SECOND_CANCELLATION_DEADLINE_B02_R9_20261029.md)
is **proved in-note**; [Review33](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/33_RADIAL_SECOND_CANCELLATION_B02_R9_SELF_ASSESSMENT_20261029.md)
remains its author's same-assistant check. [Review34](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/34_RADIAL_SECOND_CANCELLATION_E08_R9_ASSESSMENT_20261029.md)
accepts the theorem without mathematical correction within its declared
split comparison. Full carrier concentration and transition curvature
costs give conditional upper deadline S9=(1-epsilon9)S1,opt. The review
also verifies the prior [same-data direct comparison](../papers/investigations-5/05_radial_theta_collision_geometry/notes/CTF_B02_R9_WEIGHTED_DIRECT_COMPARISON_CHAT0029_20261029.md):
Sw=(2/7)^(2/5)S1,opt<S9 from the identical first-moment cap. It states:
“R9's issued deadline does not improve this stronger same-information direct comparator.”
Reuse the scoped theorem and paid source/kernel estimates, with this utility
limit. No independent regularity, theta separator, exact-P0 ranking or
physical-domain gain follows. Weighted-square collision controls share
the premises; the direct first-jet margin already covers every finite
horizon at the theta mark. E08 is complete. Different-model internal review
with three read-only same-model contributing audits has prior contributor
overlap and shared premises, not specialist independence. Manuscripts unchanged.

**Direct uniform feedback from a paid physical margin, 29 October 2026.**
Prepared for Edward Baker with substantial LLM assistance; proof
**gpt-6-astra / max**, chat0031; assessment **gpt-6.1-sol / ultra**, chat0032.
[Note67](../papers/investigations-5/05_radial_theta_collision_geometry/notes/67_UNIFORM_FEEDBACK_DIRECT_COMPARISON_B02_R10_20261029.md)
is **proved in-note**; [Review36](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/36_UNIFORM_FEEDBACK_E08_R10_ASSESSMENT_20261029.md)
states: “Accepted without mathematical correction within the inherited prepared
radial solution class, at the fixed theta mark (T,A)=(1/4,2).” The complete
source slope pays H>(70/73)M. A generic carrier/Fourier/retained-diffusion
argument then pays explicit time-uniform G/E0<=K_infinity<=K_theta and
alpha<=2K_infinity/3. Reusable as a quantitative direct regularity bound;
its min allowance beats the equally informed exponent-7 growing bound
after an explicit crossover. The physical margin precedes evolution and
is essential. B>=a_*s is unbounded; residual/higher-jet control remains
finite-horizon. No source-residual advantage, larger domain, optimized
constant or measured cost saving follows. Weighted squares share the
low-mark sufficient bound; actual admitted events fail positive mass.
This supersedes the horizon-growing displayed direct allowance for this
consumer, not earlier scoped results. Different-model internal assessment
with three same-model contributing audits retains shared premises;
no specialist independence. Frozen inputs/manuscripts unchanged.

**Analytical manuscript consolidation, 29 October 2026.** Prepared for
Edward Baker with substantial LLM assistance, **gpt-6-astra / max**,
chat0031. [Note71](../papers/investigations-5/05_radial_theta_collision_geometry/notes/71_ANALYTICAL_MANUSCRIPT_CONSOLIDATION_20261029.md)
states: “Completed editorial integration; no new mathematical result claimed.”
The [main manuscript](../papers/investigations-5/05_radial_theta_collision_geometry/radial_deformations_and_zero_dynamics.tex)
now leads with the stronger direct deadline and accepted uniform-feedback
bound, retaining the physical-margin premise and finite-horizon residual
scope. Source compatibility, its kernel-freedom limitation and the final
coupled closure follow in dependency order. The [editorial review](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/37_ANALYTICAL_MANUSCRIPT_INTEGRATION_REVIEW_20261029.md)
and [build record](../papers/investigations-5/05_radial_theta_collision_geometry/numerics/27_ANALYTICAL_MANUSCRIPT_BUILD_RECORD_20261029.json)
identify the 28-page checked version. Earlier proof and assessment sources
and the companion remain unchanged; only the active main manuscript is
superseded by this later authorized version. Internal same-assistant
editorial checking, not independent mathematical review.


**Primitive integration, 29 October 2026.** For Edward Baker with substantial
LLM assistance, **gpt-6-astra / max**, chat0031.
[Review38](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/38_PRIMITIVE_MANUSCRIPT_INTEGRATION_REVIEW_20261029.md)
states: “Integrated analytical interface; no improved estimate claimed.”
The [manuscript](../papers/investigations-5/05_radial_theta_collision_geometry/radial_deformations_and_zero_dynamics.tex)
now proves primitive transfer with both endpoint terms and common-path
duality under explicit test hypotheses, following
[Note73](../papers/investigations-5/05_radial_theta_collision_geometry/notes/73_BOOK_INTEGRATION_BY_PARTS_AND_FEEDBACK_PAIRINGS_20261029.md).
It identifies the actual signed drift-production test; bounding its
derivatives and traces remains open. The classical scalar formula is
reused, and colliding controls still admit positive primitives.
All 17 earlier proof blocks and the companion are preserved.
Same-assistant analytical/editorial checks, built-in compilation only;
no independent specialist review or new collision exclusion.

**R11 primitive tests and uniform residual closure, 29 October 2026.**
Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra /
ultra**, chat0033. [Note75](../papers/investigations-5/05_radial_theta_collision_geometry/notes/75_PRIMITIVE_TEST_COSTS_AND_SIGNED_COMPARISON_R11_20261029.md)
and [Note76](../papers/investigations-5/05_radial_theta_collision_geometry/notes/76_UNIFORM_RESIDUAL_AND_FIXED_JET_CLOSURE_R11_20261029.md)
are **proved in-note**, with same-model contributing checks in
[Review39](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/39_PRIMITIVE_TEST_AND_UNIFORM_CLOSURE_INTERNAL_REVIEW_20261029.md).
**E08 R11 is now complete:** [Review40](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/40_PRIMITIVE_TEST_AND_UNIFORM_CLOSURE_E08_R11_ASSESSMENT_20261029.md)
accepts all ten obligations without mathematical correction. Assessment:
for Edward Baker with LLM assistance, **gpt-6.1-sol / ultra**, chat0034,
29 October 2026; different-model internal review with contributing
same-model audits and shared inherited premises, no specialist independence. They pay all actual primitive test derivatives/traces and,
using R10's physical-margin feedback bound, give uniform full weighted
residual energy, each fixed common-path jet and fixed-window complete
dissipation. This supersedes the earlier finite-only residual allowance
at (1/4,2), while preserving it as a valid envelope. The review states:
“The uniform consumer closes directly; primitive test admissibility is
not an arithmetic separator.” No primitive-specific signed gain, larger
physical region, margin-free regularity or specialist review is claimed.
The opposite-sign test concerns a broader coefficient/residual class,
not actual theta trajectories; fixed-order is not uniform-in-order.
Review40 states: “The direct comparator has the same source, physical mass and retained
diffusion.” **E05 R4 integration is complete:** [Return80](../papers/investigations-5/05_radial_theta_collision_geometry/notes/80_UNIFORM_RESIDUAL_MANUSCRIPT_INTEGRATION_RETURN_20261029.md)
and [Review41](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/41_UNIFORM_RESIDUAL_MANUSCRIPT_INTEGRATION_REVIEW_20261029.md)
identify the 35-page manuscript, successful build/layout check and
preservation of 19 prior proofs. Return80 states: “This integration
establishes no additional mathematical result.” Editorial revision for
Edward Baker with LLM assistance, gpt-6.1-sol / ultra, same chat0034,
29 October 2026; same-parent checking with shared premises. [Continuation81](../papers/investigations-5/05_radial_theta_collision_geometry/notes/81_UNIFORM_RESIDUAL_INTEGRATION_AND_MODEL_CONTINUATION_20261029.md)
routes the next conceptual decision.

### Investigation05 R12: common-carrier decay, assessed

29 October 2026, prepared for Edward Baker with substantial LLM assistance,
gpt-6-astra / ultra, chat0033. [Note82](../papers/investigations-5/05_radial_theta_collision_geometry/notes/82_COMMON_CARRIER_SYNCHRONIZATION_R12_20261029.md) states
“proved in-note under the accepted prepared-solution, common-kernel and
R10 uniform-feedback inputs”. **E08 R12 is complete:** [Review43](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/43_COMMON_CARRIER_AND_PRODUCTION_E08_R12_ASSESSMENT_20261029.md)
accepts all ten obligations without mathematical correction. Assessment
for Edward Baker with LLM assistance, gpt-6.1-sol / ultra, existing chat0034,
29 October 2026; internal different-model review with prior contributor
overlap and shared inherited premises, no specialist independence. The first three
centered jets have squared-H1 allowance exp(−B/2).
[Note83](../papers/investigations-5/05_radial_theta_collision_geometry/notes/83_FINITE_CENTERED_PRODUCTION_CORRECTION_R12_20261029.md) pays complete centered dissipation and a
finite alpha-weighted correction in I1. The direct method proves both.
The known physical margin remains, the carrier sign is unpaid and no
full actual-energy or collision-domain improvement is claimed.
[Review42](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/42_COMMON_CARRIER_AND_PRODUCTION_INTERNAL_REVIEW_R12_20261029.md) is same-model contributing checking.
Earlier accepted results keep their existing scope.
Review43 states: “A finite correction for this single term is not an error
theorem for the entire actual production.” **E05 R5 integration is now complete:** [Return87](../papers/investigations-5/05_radial_theta_collision_geometry/notes/87_COMMON_CARRIER_MANUSCRIPT_INTEGRATION_RETURN_20261029.md)
and [Review44](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/44_COMMON_CARRIER_MANUSCRIPT_INTEGRATION_REVIEW_20261029.md)
identify Section 9 and successful built-in compilation, with source checks
and no fresh preview/standalone PDF. Return87 states: “Integration adds no
new mathematical result.” All 21 prior proofs and the companion remain.
For Edward Baker with LLM assistance, gpt-6.1-sol / ultra, existing
chat0034, 29 October 2026; same-parent editorial checking/shared premises.
[Continuation88](../papers/investigations-5/05_radial_theta_collision_geometry/notes/88_COMMON_CARRIER_INTEGRATION_AND_MODEL_CONTINUATION_20261029.md)
routes the next bounded conceptual decision.

### Investigation05 R13: complete carrier transfer, assessed

29 October 2026, prepared for Edward Baker with substantial LLM assistance,
gpt-6-astra / ultra, chat0033. [Note89](../papers/investigations-5/05_radial_theta_collision_geometry/notes/89_COMPLETE_CARRIER_PRODUCTION_TRANSFER_R13_20261029.md) states
“proved in-note from the accepted R11/R12 inputs”. **E08 R13 is complete**:
[Review46](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/46_COMPLETE_CARRIER_REDUCTION_E08_R13_ASSESSMENT_20261029.md)
accepts all ten obligations without mathematical correction. Assessment
for Edward Baker with LLM assistance, gpt-6.1-sol / ultra, existing
chat0034, 29 October 2026; internal different-model review with prior
overlap and shared premises, no specialist independence.
Complete production and exact dissipation differences now have finite
absolute tails. [Note90](../papers/investigations-5/05_radial_theta_collision_geometry/notes/90_CARRIER_FEEDBACK_DEFECT_AND_STATIONARY_CANDIDATE_R13_20261029.md) pays the feedback defect
and dual-Lipschitz scalar forcing, proves a scalar-energy limit and
selects a unique possible radial Gibbs profile. No profile/coefficient
convergence, favorable carrier sign, physical-margin removal or
primitive-specific gain follows. [Review45](../papers/investigations-5/05_radial_theta_collision_geometry/reviews/45_COMPLETE_CARRIER_REDUCTION_INTERNAL_REVIEW_R13_20261029.md)
is same-model contributing checking. R12's selected-term scope remains
historically correct; R13 pays its previously unproved full difference.
Review46 states: “Unique stationary candidate, scalar-energy convergence
and weak integrable forcing do not show an omega-limit is stationary.”
[Continuation93](../papers/investigations-5/05_radial_theta_collision_geometry/notes/93_COMPLETE_CARRIER_R13_ASSESSMENT_AND_MODEL_CONTINUATION_20261029.md)
routes the remaining scalar-attraction decision; both manuscripts remain
at their pre-assessment versions.
