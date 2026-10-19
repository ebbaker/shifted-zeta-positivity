# Local heat-flow geometry, marked topology, and RH-equivalent criteria

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

Coverage and scope revised 16 October 2026 for Edward Baker with substantial
LLM assistance: **gpt-6-astra (Codex)**, reasoning effort **ultra**.

## Summary

Write \(h_j=\partial_x^jH\), \(E=h_0^2+h_1^2\), and
\(\mathcal L_j=h_{j+1}^2-h_jh_{j+2}\) for a real analytic backward-heat
field \(H_t=-H_{xx}\). The local results concern a spatial zero of exact
finite order \(m=2r+j\), \(r\ge1\), \(j\in\{0,1\}\).

- **Stationary collision geometry (22 §2).** For \(s=T-t\), the relevant
  stationary predecessor is one analytic curve, the opposite-parity
  stationary set is locally empty before the event, and the physical jet
  has a scalar factor: \(E=W^2Q(s)\), with positive analytic \(Q\).
  The signed ratio has the universal pole \(\mathcal L_j/E=-r/s+O(1)\).
- **Chord and turning laws (22 §7).** The fixed-endpoint chord satisfies
  \(\mathcal C_j/\sqrt E\to-d_\delta<0\); an independently established
  starting-energy estimate with uniform \(o(\sqrt E)\) loss excludes the
  covered event, and the exponent \(1/2\) is sharp. The exponential-average
  version retains its endpoint-only cutoff error
  \(\le B_j(T_*)e^{-\pi(N+1)^2/4}\sqrt E\). Quarter-turn concentration and
  explicit scaled profiles describe the same local degeneration.
- **Circle cancellation loss (21 Note 57).** On full holomorphic circles
  and nearby time slices, taking the boundary density's negative part
  separately creates a fixed-radius loss of order \(s^{-r}\) relative to
  \(E\), versus the exact stationary pole of order \(s^{-1}\). The excess
  is the discarded positive boundary mass. Radius \(R\asymp\sqrt s\)
  removes the extra pole order, not the divergence; an event-dependent
  radius is a diagnostic, not a prescribed certificate.
- **Real index, walls and projective data (22 Notes 04, 06, 07).** Each
  collision has real index \(-\lfloor m/2\rfloor\), so zero boundary
  winding excludes every interior collision when the boundary jet is
  nonzero. Moving-wall root counts retain signed wall fluxes, including
  tangencies. The real projective jet \([H:H_x]\in\mathbb{RP}^1\) has
  degree twice the jet winding; it retains the obstruction. Unrestricted
  filling in \(\mathbb{CP}^1\) does not. The completed theta pilot is in
  [11](11_newman_heat_flow_reductions_and_certificates.md). With regular
  positive initial time, terminal time above \(1/2\), and the stated boundary
  and uniform-confinement hypotheses, stabilized negative theta winding counts
  nonreal zeros in the upper-right quadrant with multiplicity.
- **Complex and embedded multiplicities (22 Notes 04, 08).** The holomorphic
  pair \((H,H_z)\) has local intersection multiplicity \(m(m-1)/2\),
  positive complex degree and negative degree in the declared quaternion
  orientation. At fixed time, the primitive curve \((P,H)\), \(P_z=H\),
  has embedded link \(T(m,m+1)\) and Milnor-fiber genus \(m(m-1)/2\);
  its normalization is a disk. These are distinct germs. Real and complex
  degree magnitudes agree only for a double collision; their parity always
  agrees. Degree alone proves no general advantage or disadvantage for a
  four-dimensional boundary estimator.
- **Compact real surfaces (22 Note 05).** For
  \(f(z)=\xi(1/2+\sqrt z)=\sum\gamma_k z^k/k!\), define
  \(J_d(X)=\sum_{k=0}^d\binom dk\gamma_kX^k\), with positive complete-theta
  moment coefficients. RH is equivalent to every smooth projective
  normalization of \(y^2=J_{2g+1}(x)\) having exactly \(g+1\) real
  components. The count uses the original degree, not the possibly smaller
  normalization genus. RH gives strict Jensen hyperbolicity without
  assuming simple zeta zeros. This is a proved reformulation using classical
  ingredients, not a proof that the component condition holds.
- **Surface deficit and polynomial heat (22 Note 07).** For an odd-degree
  real polynomial \(Q\) of degree \(2g+1\),
  \(g+1-b_0(C_Q(\mathbb R))=N_{\rm nonreal}(Q)/2+
  \sum_{a\in\mathbb R}\lfloor\operatorname{mult}_aQ/2\rfloor\), counting
  nonreal roots with multiplicity. This equals its remaining polynomial-heat
  collision weight, including initial-slice events. The reciprocal
  Hermite–Jensen deficits increase with degree and decrease with auxiliary
  heat time. Every finite polynomial eventually regularizes; a uniform
  finite threshold across all degrees is already RH-equivalent. Auxiliary
  polynomial heat time is not physical theta heat time.
- **Observation equivalences (Review 16 and Reply 18).** Under RH every
  **positive-time** slice is Laguerre–Pólya with simple zeros and satisfies
  the observation criteria with zero loss. The all-event loss criteria on
  \((0,1/2]\) are RH-equivalent; on \([t_0,1/2]\), they characterize
  \(\Lambda\le t_0\), while strict pointwise signs require
  \(\Lambda<t_0\). The prescribed-trace equivalence retains its stated
  two-sided locally bounded scalar coefficient and remainder control.

- **Normalized jet rotation comparison (3/11 S03, 18 October).**
  The complete signed oscillator-defect integral has an exact first-jet
  endpoint primitive. The scoped comparison is **proved in-note**: scalar
  transport with independent endpoint residual envelopes is dominated by
  the ideal direct radius test for the same phase, approximant and norm.
  Correlated residual estimates and computational cost comparisons are
  outside that limitation. The fixed height-1000 cover validates direct
  exclusion, gives a certified failure witness for the declared standard
  Cauchy payments, and leaves sharper joint-disk transport inconclusive.
  No new region or global theta estimate. [Proof](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/01_SIGNED_TRANSPORT_AND_DIRECT_JET_COMPARISON_20261018.md),
  [same-model internal review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/reviews/01_SIGNED_TRANSPORT_INTERNAL_REVIEW_20261018.md).
  Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, ultra**.
  The [correlated continuation](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/02_CORRELATED_ARITHMETIC_RESIDUAL_AND_PAID_TRANSPORT_20261018.md)
  supplies an **interval-certified** finite residual increment below
  `0.000266448` versus `0.002011747` for independent endpoints from the
  same source data. Paid transport exceeds `1.124460`; direct exclusion
  remains stronger. Its oscillator calibration has complete real
  phase-scaled first-jet error below `0.000266449`. Earlier finite
  transport uncertainty is resolved with added source information,
  without new coverage or a global bound; [same-model internal review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/reviews/02_CORRELATED_RESIDUAL_INTERNAL_REVIEW_20261018.md).
  Prepared for Edward Baker, **gpt-6.1-sol, actual effort ultra**, 18 October.

- **GEO-T1 matched winding comparison (3/11, 19 October).**
  **Interval-certified bounded validation** on already-covered
  B=[1/100,1/5]x[999,1001]: whole-boundary winding0 uses7segments/10complete
  calls and no source vertex calls. Optimized direct first-jet certification
  covers3full-time strips in7calls. Both use identical complete source/errors
  at192/256bits. Common setup dominates; direct/winding cold ratios
  0.999385/0.999442 fail the declared factor-two gate. Stop this fixed-box
  comparison; no coverage, global sign estimate or S07-T3 input. Thirty-six
  actual-helper/direct controls pass, and fresh192 replay matches mathematical
  content. [Result](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/notes/06_GEO_T1_WINDING_AND_DIRECT_COMPARISON_20261019.md),
  [same-model internal review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/reviews/01_GEO_T1_WINDING_DIRECT_INTERNAL_REVIEW_20261019.md).
  Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol,
  ultra**; no specialist human review. These timing observations do not
  exclude winding advantages on other domains or acquisition models.

## Status

The local laws, indices, surface identities and equivalences have written
analytic proofs with internal LLM reviews. Polynomial-germ replays check
finite examples and conventions; they do not prove universal quantifiers.
The later topology continuation has its own proofs and review outside the
stable manuscript. The theta winding box is separately interval-certified.
The rule to judge an RH-equivalent proposal as a reformulation and a
quantitative milestone by its number is a research policy, not another theorem.

## Caveats

The generic collision laws do not distinguish theta from the controls in
[12](12_collision_controls_and_screening.md). The complete-theta surface
family retains the source's “real involutions” (Note 05); its desired
maximal topology remains unproved.
The earlier blanket description of all geometry as “sign-blind” is too
broad: oriented associators, forms and real Gauss maps retain the sign;
norms and intrinsic curvature can lose it. See the actual constructions
and integrated positive theorems in [16](16_hypercomplex_reductions_and_geometric_realizations.md).
No literature priority or global theta sign theorem follows from these results.

## Reusable for

Local models, multiplicity-safe boundary accounting, marked real topology,
and comparison of certificate geometries. The compact-surface equivalence
is a precise answer to how manifold topology can encode RH, with all
normalization and reality data retained.

## Where

- [22 manuscript](../papers/investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex), §§2, 7, 11; [21 circle-loss note](../papers/investigations-2/active/21_quaternion_theta_geometry/notes/02_signed_cusp_control/57_CIRCLE_DEFECT_MULTIPLICITY_AND_RADIUS_20261015.md) and [Review 33](../papers/investigations-2/active/21_quaternion_theta_geometry/reviews/33_PRIMITIVE_CIRCLE_AND_CARRIER_CONTINUATION_REVIEW_20261015.md).
- [Spacetime index and embedded primitive topology](../papers/investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md); [compact Jensen surfaces](../papers/investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/05_JENSEN_HYPERELLIPTIC_TOPOLOGY_20261015.md); [Review 13](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/13_GEOMETRIC_SIMPLIFICATION_AND_TOPOLOGICAL_RH_REVIEW_20261015.md).
- [Moving-wall flux and theta winding](../papers/investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/06_WALL_FLUX_AND_CERTIFIED_THETA_WINDING_20261015.md); [real-projective jets and surface deficits](../papers/investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/07_REAL_PROJECTIVE_JETS_AND_JENSEN_HEAT_SURFACES_20261015.md); [real/complex multiplicities](../papers/investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/08_REAL_AND_COMPLEX_COLLISION_MULTIPLICITIES_20261015.md); [continuation review](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/18_SPACETIME_BOUNDARY_AND_GEOMETRIC_CONTINUATION_REVIEW_20261015.md).
- [Review 16](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/16_JOINT_REVIEW_OF_INVESTIGATIONS_21_AND_22_CLAUDE_20261015.md), [Response 17](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/17_RESPONSE_TO_JOINT_REVIEW_CLAUDE_20261015.md), and [Reply 18](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/18_REPLY_TO_RESPONSE_17_CLAUDE_20261015.md), §§1–2, 5, for the corrected equivalence and degree scope.
