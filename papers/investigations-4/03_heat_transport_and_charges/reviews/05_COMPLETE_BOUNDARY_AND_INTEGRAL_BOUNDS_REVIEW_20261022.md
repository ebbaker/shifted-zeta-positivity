# Complete boundary and topological integral bounds: internal review

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **ultra**, verified from the active turn metadata.

**Verdict: pass in the stated local analytic and parameterized scope.**
[Note 03][n3] completes CHB-04's boundary assembly. [Note 04][n4] supplies
explicit bounds on the regularized nonnegative mass and bounded weighted
versions, and a costed comparison with the spatial Gauss-area density.
No actual theta acquisition, improved arithmetic estimate, new charge
invariant, RH-to-simplicity proof or Atiyah–Singer identification is claimed.

This is **contributing-agent same-model internal review**. The reviewers
contributed mathematical derivations and share context/model; their agreement
is not independent specialist validation. The primary agent checked the
assembled notes and the [reproducible controls][script]. Exact-rational
controls and floating quadrature are separately labeled in [the receipt][receipt].
Neither is a formal analytic proof or a canonical theta certificate.

## Checks and outcomes

| Item | Outcome |
| --- | --- |
| Complete domain | W is a physical heat rectangle times a spatial disk, enclosing the event in its interior. Only its closed boundary is split into ratio charts. No pinched sector is substituted for W. |
| H/H_z chart coverage | The uniform F_p=H_z-pH wall margin excludes all low-ratio points from the outer spatial wall. The unique graph covers exactly the remaining low-ratio heat-face pieces. |
| Seam orientation | Sigma=boundary M_- has orientation -ds wedge d beta. The primitives give kappa n and (1-kappa)n, totaling winding(V). |
| Individual physical faces | I_+(e) includes J(b)-J(a)-K(e). J telescopes and the spatial-wall integral is sum K. The wall is retained and may be nonzero. Both imaginary-time faces remain. |
| Explicit geometry | The chosen radii give theta<=1/8, graph center allowance<=R/4, B error<=h/4, and uniform F_p wall margin>=5hR/8. Spatial Taylor/Rouche bounds give two H roots inside both R/2 and R. |
| Inherited geometry | BW12's existing proper-window theorem remains credited. Its bounds also give the qualitative critical graph; the additional contract here supplies convenient quantitative floors. |
| Whole boundary floor | The critical-value/critical-distance split gives the stated E floor on heat faces; the explicit 5hR/8 margin pays the spatial wall. Interior jet vanishing is not excluded by assumption. |
| Regulator constant | S includes all five physical faces. L is an operator-norm bound obtained from the complex Frobenius norm, not the real Frobenius norm. The e_0 powers use an E floor. |
| Same-data comparison | The critical-value winding equals the existing discriminant winding. V/Delta extends with value -h_2/8; no additional arithmetic information is produced. |
| Weighted mass | Positivity and the complete signed mass identity give W_0(Q+B_delta). Weighted limits require continuity at events, and weighted Stokes retains the dw term. Singular weights need new bounds. |
| Spatial Gauss comparison | The Gram determinant, spatial entry and Schur-complement formulas agree. The resulting estimate is a complex-time area average, not a fixed-time slice bound. The existing source contract supplies a positive Schur floor across the window for each fixed delta; the inverse regularization cost remains explicit. |
| Index scope | No elliptic operator/Fredholm problem is identified with the physical observation. The original AS/APS sources are cited; spectral boundary corrections are not assumed zero. |

## Collision and comparison controls

The quadratic H=z²-2tau has complete charge one. At the specified
R=1, T=Y=1/16, P=1/4, each heat face is 1/4-K and the spatial wall is 4K,
where K approximately equals 0.000794445554866028. Independent direct
pullback integration of all five faces returns 0.9999999999999489 on the
finer grid. This is floating diagnostic agreement, not an outward error
bound. Exact rational checks validate the source-free geometry and chart
constants for this control; the collision remains.

The quartic heat control has exterior neighbors and a fixed separating
circle. Its total enclosed multiplicity stays two while the inner pair
merges into a double. The complete complex spatial-wall margin is
109A⁴/1024 and the critical-value winding is one. This answers the user's
moving finite-height contour proposal: conservation of sum m does not imply
conservation of sum(m-1) or vanishing collision charge. The control lacks
canonical arithmetic; it is not a counterexample to an RH-to-simplicity
argument using an additional theta-specific estimate.

For comparison of integrals, H=z has positive spatial Gauss density and
zero four-dimensional mass. The quadratic also supplies a point where
spatial Gauss density is zero while the bulk determinant is nonzero. These
exclude only the stated generic dominations. They do not exclude a paid
canonical-source or differently weighted comparison.

## Disposition

CHB-04 is complete as the parameterized local full-boundary reduction.
CHB-05 now has a complete-window analytic contract, but actual finite-source
acquisition and a meaningful direct comparison are unperformed. The user's
integral-bounding objective is recorded as CHB-07: basic weighted mass bounds
and the Gauss comparison interface are available; a useful bound for the
selected existing target beyond its inverse cost remains open. Higher
multiplicity, all heights and the inherited BW10/BW12 exclusion gates remain
unresolved. Neither this review nor the control count upgrades those claims.

[n3]: ../../notes/03_COMPLETE_PHYSICAL_BOUNDARY_AND_CRITICAL_VALUE_WINDING_20261022.md
[n4]: ../../notes/04_TOPOLOGICAL_MASS_BOUNDS_AND_INDEX_THEOREM_INTERFACE_20261022.md
[script]: ../numerics/check_chb_full_boundary.py
[receipt]: ../numerics/CHB_FULL_BOUNDARY_CHECKS_20261022.json
