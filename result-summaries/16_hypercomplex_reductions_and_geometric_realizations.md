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
