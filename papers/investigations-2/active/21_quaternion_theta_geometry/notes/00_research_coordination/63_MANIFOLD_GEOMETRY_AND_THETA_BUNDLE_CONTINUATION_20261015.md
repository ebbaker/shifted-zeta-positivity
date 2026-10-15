---
research_program: COORD
secondary_programs: [ALG, PR02, PR02-CORR]
status: checked_geometric_constructions_and_conditional_target
---

# Manifold geometry and theta-bundle continuation

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from current-turn metadata. Internal collaborators inherited that configuration.

The user's question about self-dual/ASD forms and special holonomy leads to three exact constructions and a new conditional signed target. These continue [Note 59](59_PRIMITIVE_CONTROLS_AND_COMPLETED_PHASE_BUDGET_CONTINUATION_20261015.md) and the author's quaternion-form ideas already incorporated through Note 50. They do not establish a further theta sign region or an RH proof.

| Construction | Exact content | Remaining requirement |
| --- | --- | --- |
| [Note 60: hyperkähler lifts](../04_octonionic_reductions/60_HYPERKAHLER_LIFTS_AND_COLLISION_DEGENERACY_20261015.md) | Closed SD lifts are harmonic. A nonzero holomorphic coefficient gives a locally flat hyperkähler metric; choosing `H+iH_z` gives real metric coefficient `E`. | The field-dependent metric degenerates at collisions. Compactification cannot retain both nonzero exactness and self-duality. |
| [Note 61: jet surfaces and real Gauss maps](../02_signed_cusp_control/61_JET_SURFACES_REAL_GAUSS_MAP_AND_ORIENTED_TURNING_20261015.md) | The immersed complex surface `(P,H,w)`, `P'=H`, has metric `(|H|²+|H_z|²)|dz|²+|dw|²`. It also admits explicit coassociative/Cayley inclusions. Intrinsic curvature squares the Laguerre quantity; the real tangent angle retains its sign. | A source-prescribed, one-sided modulus of continuity for the real jet angle on short regular segments from full stationary points. |
| [Note 62: theta jets and a semi-flat family](../05_theta_correlation_kernels/62_THETA_JET_BUNDLE_AND_SEMIFLAT_HYPERKAHLER_GEOMETRY_20261015.md) | The complete source is an explicit theta jet on the elliptic family with modulus `i exp(4u)`. This family has an explicit curved local hyperkähler metric with zero Ricci tensor and horizontal sectional curvature `1/(2q³)`. | Global jet transition/connection data and an estimate that survives the complete positive-heat Mellin transform at physical energy scale. |

The central geometric distinction is between the geometry of the **physical transformed jets** and the geometry of the **arithmetic theta source**. The former turns collision exclusion into a question about degeneration and oriented turning. The latter has actual elliptic fibers, a theta line bundle and a nonflat hyperkähler model. A useful continuation must prove an analytic relation between these two structures, rather than identify their heat parameters or infer nonvanishing from special holonomy alone.

## A precise signed target

On regular real intervals let
\[
\alpha_j=\arg(h_j+i h_{j+1}),\qquad
\partial_x\alpha_j=-\frac{\mathcal L_j}{h_j^2+h_{j+1}^2}.
\]
For `j=0` the denominator is exactly `E`. For `j=1` it is a different energy, and may vanish while `E` is positive; the note states all regularity conditions explicitly.

At a finite collision of multiplicity `2r+j`, the full stationary predecessor and its right-hand segment of length `c sqrt(T-t)` have a positive angle increment tending to `pi/2`. The interval stays regular because its leading heat profile has positive coefficients and is bounded below by one. Therefore a uniform source-prescribed upper modulus tending to zero with segment length excludes collisions. This is a proved conditional criterion; its theta premise is open. It is not claimed to follow from the previous stationary-only estimate, nor to be weaker than that estimate.

## Recommended next bounded investigation

Construct the source expression in Note 62 as a theta jet-bundle section with its full transition laws and a declared Hermitian connection. Derive the covariant identities before applying the physical transform. Test whether the resulting two-source identity controls the signed turning integral in Note 61, or the polarized boundary current of Notes 46 and 50, without replacing either by a norm. Retain the integer lattice, complete heat factors, spectral phase, and all connection/cusp boundary terms.

The positive-source collision controls in Notes 53 and 56 must fail at a genuinely theta-specific premise. They already admit the generic flat hyperkähler lifts, holomorphic jet surfaces and calibrated inclusions. No nonabelian or exceptional-holonomy enlargement is justified solely by its algebraic availability.

## Checks and integration status

[Review 34](../../reviews/34_MANIFOLD_GEOMETRY_AND_THETA_BUNDLE_REVIEW_20261015.md) records independent internal proof checks, the correction requiring a nonnegative angular bound coefficient, and the distinction between local constructions and global claims. The [geometry checker](../../numerics/check_theta_manifold_geometry.py) and [small execution receipt](../../numerics/THETA_MANIFOLD_GEOMETRY_CHECKS_20261015.json) verify 55 exact algebraic assertions. These are identity checks, not a theta numerical certificate.

The stable 96-page manuscript still integrates Notes 38–53. Notes 56–62 remain research continuations outside it. No new manuscript snapshot, commit, tag, or sign-domain extension is introduced. The source and build record retain SHA-256 values `ec9cca0a31e4e15f77559db4447fd61a572994b486c8955d0ddd689c059d3c61` and `d35ea783bea0c175975d136e7febfb25719bfc8314cdf0cd42f970fbb0105aab`, respectively.
