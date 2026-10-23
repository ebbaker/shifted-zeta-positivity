# Height dependent heat contour computations

23 October 2026. Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra (Codex), effort max**.

Store reproducible scripts and small execution records here after the [research contract](../research-progress/01_HEIGHT_DEPENDENT_HEAT_CONTOURS_PROGRESS_20261023.md) specifies the target. Distinguish exact algebra, floating diagnostics and interval-certified theta evaluations. Pay complete source tails and all boundary contributions in any certificate.

The inherited [material-jet check record](../../brainstorm/numerics/MATERIAL_JET_ENERGY_CHECKS_20261023.json) remains an algebra diagnostic. Follow [LARGE_FILES.md](../../../../LARGE_FILES.md); large regenerable data and third-party PDFs stay outside Git.

23 October execution, **gpt-6-astra (Codex), effort ultra**: [exact diagnostic script](01_check_boundary_and_relative_energy_20261023.py) and [record](01_BOUNDARY_AND_RELATIVE_ENERGY_CHECKS_20261023.json) check boundary determinants, reference algebra, polynomial path cancellation, the relative-energy sign control, quadratic endpoint and sine source derivatives. Python standard library; run the script to regenerate its sibling JSON. These are exact finite algebra checks, not theta certificates.

Analytical research support, 23 October 2026, **gpt-6-astra, ultra**:

- [Pair-filter script](02_check_pair_filter_20261023.py) and [record](02_PAIR_FILTER_CHECKS_20261023.json): 594 exact rational assertions, Python standard library.
- [Contour script](03_check_curved_transport_20261023.py) and [record](03_CURVED_TRANSPORT_CHECKS_20261023.json): exact controls plus floating complex-matrix, wall-log and graph-area diagnostics; requires NumPy.
- [Backward script](04_check_backward_transport_20261023.py) and [record](04_BACKWARD_TRANSPORT_CHECKS_20261023.json): 268 exact rational assertions, Python standard library.

Run each script with Python 3; these three scripts print the small JSON record to standard output. There is no large data output. The 862 exact assertions and the floating checks verify finite algebra, not a theta certificate or a simplicity claim. Proofs and conditions are in Notes 07–10.

Coefficient-filter continuation, 23 October 2026, **gpt-6-astra, ultra**: [forest script](05_check_forest_filter_20261023.py) and [record](05_FOREST_FILTER_CHECKS_20261023.json) pass **219 exact rational assertions** using the Python standard library. Exhaustive labeled forests for N=2 through 5, 36 matrix evaluations, cubic/double controls and Hermite discriminants through degree seven check the finite formulas. Default output is JSON on stdout; an explicit `--output` is optional. Together with the 862 prior assertions, this research round has **1,081 exact assertions**, plus the separate floating diagnostics. No theta certificate or simplicity claim follows from these controls.

The [validation record](VALIDATION_ANALYTICAL_ROUND_20261023.json) records successful link/delimiter/file-size checks and the exact replays, with hashes for the forest continuation artifacts. These checks do not replace the mathematical review.

Complete coefficient transport, 23 October 2026, **gpt-6-astra, ultra**: [script](06_check_coefficient_transport_20261023.py) and [record](06_COEFFICIENT_TRANSPORT_CHECKS_20261023.json) pass **252 exact rational assertions**, including repeated-root remainders, sharp heat norms, forced backward formulas, 21 complete nonzero-unit heat-field cases, commuting moment propagators and microscopic precision. Python standard library; default JSON on stdout, optional explicit `--output`. The four counted exact replays now total **1,333 assertions**, in addition to the separate contour diagnostics. These are finite algebra controls, not a theta acquisition.

The [coefficient-transport validation record](VALIDATION_COEFFICIENT_TRANSPORT_20261023.json) records 710 checked local links, clean mathematical delimiters/control characters and file sizes, the 252-assertion final replay, and hashes of the saved Note 12 artifacts.

Complete-source acquisition, 23 October 2026, **gpt-6-astra, ultra**. The following new replays require Python 3 and **python-flint 0.9.0** (Arb ball arithmetic). They use 192-bit precision and portable sibling imports; no downloaded zero database or root disk is an input. Default output is JSON on stdout; `--output` saves a small record.

- [Core](hdc13_theta_core.py), [source checks](07_check_complete_theta_source_20261023.py) and [record](07_COMPLETE_THETA_SOURCE_CHECKS_20261023.json): complete xi initial field, spatial Cauchy and heat Taylor errors, 46 independent source/algebra checks.
- [Wall certificate](07_certify_complete_theta_wall_20261023.py) and [record](07_COMPLETE_THETA_WALL_CERTIFICATE_20261023.json): 109 checks, full original wall/count/discriminant and matched direct filter.
- [First-jet cover](08_certify_complete_first_jet_floor_20261023.py) and [record](08_COMPLETE_FIRST_JET_FLOOR_20261023.json): five cover/floor checks, 31 accepted rectangles and 61 cell calls.
- [Complete cap](08_enclose_complete_physical_cap_20261023.py) and [record](08_COMPLETE_PHYSICAL_CAP_COMPARISON_20261023.json): pass `--floor 08_COMPLETE_FIRST_JET_FLOOR_20261023.json`; it rechecks that geometry and the entire floor. Fixed default/maximum 512 spatial leaves; all faces paid. Both positivity flags are false. This is a valid bounded enclosure, not a successful positive-cap certificate.
- [Microscopic-reference algebra](09_check_microscopic_reference_20261023.py) and [record](09_MICROSCOPIC_REFERENCE_CHECKS_20261023.json): 74 controls for phase cancellation, removable points and independently differentiated heat defects. No high-height theta wall is certified by these algebra checks.

The prior 1,333 exact-rational assertions remain a separate class of verification. Do not combine their count with source/cap evaluations to imply formal proof verification. Notes 13–15 and Reviews 11–13 give the mathematical domains and conclusions.
