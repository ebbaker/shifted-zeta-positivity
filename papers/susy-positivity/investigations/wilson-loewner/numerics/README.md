# Checks and records

The [arithmetic-source checker](check_arithmetic_loewner_source.py) and [record](records/arithmetic-loewner-source-20260922.json) accompany the [direct Loewner-source note](../notes/ARITHMETIC_SOURCE_AND_GENERALIZED_LOEWNER_EVOLUTION_20260922.md). Run `python3 -B numerics/check_arithmetic_loewner_source.py --output /tmp/arithmetic-loewner-source-replay.json` with mpmath installed. All 60 cases passed: four exact rational controls and 56 floating checks of the complete xi/prime source, normalized source transport, generalized Loewner evolution and its xi linearization, positive measures in finite models, and two obstruction controls. The run uses no xi-zero table. These are analytical-identity diagnostics, not interval certificates or proof of an arithmetic physical realization. They are separate from the WZW and original manuscript counts.

The [22 September WZW pilot checker](check_wzw_loewner_pilot.py) and [record](records/wzw-loewner-pilot-20260922.json) accompany the [SU(2)_2 research note](../notes/SU2_LEVEL2_DETERMINISTIC_LOEWNER_PILOT_20260922.md). Run `python3 -B numerics/check_wzw_loewner_pilot.py --output /tmp/wzw-loewner-replay.json` from the investigation directory, with NumPy installed. All 72 checks passed: seven exact rational identities and 65 floating controls covering representations, algebraic blocks, KZ derivatives, five deterministic drivers, composition, both pairings, and counterexamples to omitted terms and unrestricted contraction. These are separate research controls, not part of the original 299-case manuscript count or an arithmetic certificate.

The 21 September live revision incorporates the
[growing-trace hierarchy checker](check_growing_trace_hierarchy.py) and its
[small record](records/growing-trace-hierarchy-20260921.json). Run
`python3 -B numerics/check_growing_trace_hierarchy.py --output /tmp/growing-trace-replay.json`
with NumPy installed. It checks the linear-driver geometry, exact rational
tip coefficients, noncommuting transport and curvature-insertion identities,
gauge covariance, an Abelian area control and a deterministic remainder
sample. These are separate finite matrix diagnostics, not quantum sampling,
interval certificates or independent specialist review. They are bound by
the live build record; no new draft snapshot has been saved.

The post-version-0.5
[Gaussian pair endpoint checker](check_gaussian_pair_endpoint.py) and its
[small record](records/gaussian-pair-endpoint-checks-20260920.json) accompany
the [bounded interface calculation](../notes/GAUSSIAN_PAIR_INTERFACE_ENDPOINT_RESPONSE_20260920.md).
Run it with `python3 -B numerics/check_gaussian_pair_endpoint.py --output /tmp/gaussian-pair-endpoint-replay.json`
from the investigation directory. It checks four rational couplings,
25 factorial weights, three independent finite squeeze evolutions at two
step sizes, 20 response comparisons and nine regulator identities.
The exact incompatible weight requirements and the floating diagnostics
are distinguished in the record. This adds no arithmetic certificate and
does not change the original 299-case count or any archived build record.

Version 0.5 incorporates localization research with separate programs and records:

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

- [check_hodge_radial_channel.py](check_hodge_radial_channel.py) and its
  [record](records/hodge-radial-channel-checks-20260920.json) check the
  canonical Hodge channel: 13 one-particle levels, 25 protected-degree
  levels, six spatial comparisons and an exact rational tail enclosure.

Run these explicitly with `python3 numerics/check_localization_hemisphere.py`
and `python3 numerics/check_spatial_radial_descent.py` from the investigation
directory. The Hodge program runs with `python3 numerics/check_hodge_radial_channel.py`.
All three accept `--output` for a disposable replay record. Their
provenance companions pin inputs, model identity and the unexposed effort
setting. They are included in the version-0.5 standalone snapshot and inventoried
in the live package; their formats remain separate from the original
299-case replay below.

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
quadrature. Versions 0.4--0.5 and the live research inventory register 299 cases
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
