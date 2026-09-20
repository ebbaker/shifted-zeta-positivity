# Checks and records

Subsequent localization research has separate programs and records:

- [check_localization_hemisphere.py](check_localization_hemisphere.py) and
  its [record](records/localization-hemisphere-checks-20260920.json) audit
  the preceding hemisphere/Mellin control at quadrature orders 24 and 40.
- [check_spatial_radial_descent.py](check_spatial_radial_descent.py) and
  its [record](records/spatial-radial-descent-checks-20260920.json) audit
  the [fixed-sector radial obstruction](../notes/SPATIAL_RADIAL_DESCENT_OBSTRUCTION_20260920.md).
  All 83 cases pass at orders 24 and 40: 57 exact rational checks and 26
  floating-point checks. The code imports the preceding program's
  standard-library quadrature helper. It does not derive the external
  supersymmetry transformations or an arithmetic transfer.

Run these explicitly with `python3 numerics/check_localization_hemisphere.py`
and `python3 numerics/check_spatial_radial_descent.py` from the investigation
directory. Both accept `--output` for a disposable replay record. Their
provenance companions pin inputs, model identity and the unexposed effort
setting. They are inventoried in the live package but are not part of the
version-0.4 manuscript's 299-case replay below.

[check_smooth_variation.py](check_smooth_variation.py) uses the Python standard
library and prints JSON. Its [preserved record](records/smooth-variation-checks.json)
contains 102 cases, all passing in the recorded run.

[check_defect_endpoints.py](check_defect_endpoints.py) adds 99 cases in its
[record](records/defect-endpoint-checks.json), all passing.

[check_reflected_junction.py](check_reflected_junction.py) adds 67 cases in
its [record](records/reflected-junction-checks.json), all passing. It imports
the standard-library matrix helpers from the endpoint checker. There are
268 cases across these three programs.

[check_fixed_window_response.py](check_fixed_window_response.py) adds 31
research diagnostics in its [record](records/fixed-window-response-checks.json),
all passing. It checks the full local/pole arithmetic comparison and the
unequal-radius Gaussian Wilson variation from the
[fixed-window research note](../notes/FIXED_WINDOW_WILSON_RESPONSE_OBSTRUCTION_20260920.md).
It uses the standard library and imports the existing reflected-junction
quadrature. Version 0.4 and the live research inventory both register 299 cases
across four programs. Historical manuscript version 0.3 retains 268.

| Group | Scope |
|---|---|
| Geometry and bulk charge | Inversion of semicircles, Loewner inverse maps, fixed-charge residuals, nonvertical failures with constant-driver controls |
| Ordered transport | Noncommuting matrix backgrounds; independent finite differences versus curvature/scalar insertions; moving endpoints; mesh refinement and reparameterization |
| Abelian controls | The same undeformed holonomy with different curvature response; a pure-gauge background integrated along deformed paths |
| Varying scalar | Nonzero common Clifford projector for arbitrary tangent; cancellation of the equal-propagator free bulk exchange |
| Chiral defect charges | Explicit 32-dimensional matrices and independent row reduction; correct and wrong triplets; all eight scalar-map orientation choices; one common charge over angular directions |
| Endpoint polarizations | The two transformation nullspaces, zero same-charge contraction, nonzero physical-adjoint control and residual R-charge phases |
| Adjoint transport | Three noncommuting Hermitian matrix segments; opposite scalar map under adjoint; plain reversal gives the inverse; the zero-scalar control restores unitarity |
| Physical reflection | Reflected field pullback and ordered transport; color gluing; distinct ket/bra projectors; Cauchy endpoint Gram and scalar/R-twist counterexamples |
| Junction and response | Time-normal reference tangent, continuous scalar direction, locally bounded bulk exchange; exact bulge coefficient, independent quadrature and finite Gaussian cross-response Gram |

Run a program directly, or replay all four live research programs with
`python3 validation/check_package.py check --replay`.

The note supplies the analytical derivations. These finite diagnostics do
not establish quantum operator existence, reflection positivity, quantum
Ward identities, stochastic rough-contour limits, contraction, or RH.
The endpoint derivation uses the complexification of the physical
hypermultiplet transformations; numerical nullspaces alone do not certify
that physical input. The bulk response checker omits endpoint and defect
diagrams. The three original programs use neither zeta zeros nor the target transfer.
The fixed-window diagnostic explicitly uses the arithmetic transfer for
comparison; it does not construct that transfer from field data.
