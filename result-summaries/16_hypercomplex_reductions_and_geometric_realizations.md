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
