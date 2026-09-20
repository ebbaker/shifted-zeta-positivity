# Checks and records

[check_smooth_variation.py](check_smooth_variation.py) uses the Python standard
library and prints JSON. Its [preserved record](records/smooth-variation-checks.json)
contains 102 cases, all passing in the recorded run.

[check_defect_endpoints.py](check_defect_endpoints.py) adds 99 cases in its
[record](records/defect-endpoint-checks.json), all passing.

[check_reflected_junction.py](check_reflected_junction.py) adds 67 cases in
its [record](records/reflected-junction-checks.json), all passing. It imports
the standard-library matrix helpers from the endpoint checker. There are
268 registered cases across the three programs.

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

Run a program directly, or replay all three with
`python3 validation/check_package.py check --replay`.

The note supplies the analytical derivations. These finite diagnostics do
not establish quantum operator existence, reflection positivity, quantum
Ward identities, stochastic rough-contour limits, contraction, or RH.
The endpoint derivation uses the complexification of the physical
hypermultiplet transformations; numerical nullspaces alone do not certify
that physical input. The bulk response checker omits endpoint and defect
diagrams. None of the programs uses zeta zeros or the target transfer.
