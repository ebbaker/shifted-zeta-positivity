# Exact checks and execution records

15 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**.

The [initial execution manifest](INITIAL_MANUSCRIPT_CHECKS_20261015.json) binds four scripts and their output records to their SHA-256 identities. All **344 exact assertions** passed using the Python standard library. The first two scripts are byte-identical copies from Investigation 21, retained here so this manuscript has a local replay package. Their original records remain unchanged.

| Checker | Assertions | Scope |
| --- | ---: | --- |
| [Manifold geometry](check_theta_manifold_geometry.py) | 55 | Closed normalized hyperkähler triple, inverse metric, Ricci tensor, horizontal sectional curvature, totally geodesic slices and theta differential source operator |
| [Finite collision profiles](check_circle_defect_collision_profile.py) | 240 | Exact finite heat-polynomial profiles for orders `r=1,...,12`, both parity branches and the circle-current Fourier coefficients |
| [Chern extension](check_theta_chern_extension.py) | 31 | Direct connection curvature, Hermitian lattice law, covariant second/fourth jets, source cancellation and curvature norm |
| [Independent Chern/ASD check](check_theta_chern_asd.py) | 18 | Separate exact calculation of Chern curvature, base correction, Hodge action, source cancellation and multiplier law |

From this directory, run each script with Python 3. Each prints its result as JSON. The manifold, collision-profile and independent ASD scripts also accept `--output PATH` to save that result. The extension script writes to standard output. The aggregate manifest records the newly executed local copies; its hashes identify these particular files and do not establish mathematical truth.

The two new Chern checkers deliberately overlap so that the connection and source normalization are calculated separately. Their assertion total is not a count of distinct theorems. No arbitrary-order analytic limit, modular descent, theta sign certificate or RH conclusion follows from finite arithmetic alone. Those distinctions are addressed in the [manuscript](../manuscript/theta_manifold_geometry.tex) and [review](../reviews/01_INITIAL_MANUSCRIPT_DERIVATION_REVIEW_20261015.md).

## Connection bridge and inner turning replay

The [continuation manifest](CONNECTION_BRIDGE_AND_INNER_TURNING_CHECKS_20261015.json) records a new replay of the four initial scripts and the following three additions. Their **886 new assertions** bring this replay to **1,230 overlapping exact assertions**. The analytic and theta-sign limitations remain explicit in each record.

| Checker | Assertions | Scope | Execution record |
| --- | ---: | --- | --- |
| [ASD path metric](check_asd_path_metric.py) | 35 | Base potentials, holomorphic metric freedom and physical/external-product restriction | [Record](ASD_PATH_METRIC_CHECKS_20261015.json) |
| [Signed bridge](check_theta_signed_bridge.py) | 59 | Signed phase kernels, full primitive endpoints, heat factors and covariant source recurrence | [Record](THETA_SIGNED_BRIDGE_CHECKS_20261015.json) |
| [Inner turning](check_inner_turning_profile.py) | 792 | 72 exact finite heat-polynomial cases and odd-branch denominator distinction | [Record](INNER_TURNING_PROFILE_CHECKS_20261015.json) |

Each new script accepts `--output PATH`; without that flag it prints its JSON record. All use the Python standard library. No interval arithmetic or new theta sign certificate is supplied.

## Arithmetic, contour and chord replay

The [new manifest](ARITHMETIC_CONTOUR_CHORD_CHECKS_20261015.json) binds four checkers, receipts and analytic notes. The coordinator replayed every checker; a separate collaborator also replayed the weighted-square certificate. Counts include overlapping finite identities and interval assertions, not distinct theorems.

| Checker | Assertions | Scope | Receipt |
| --- | ---: | --- | --- |
| [Chord controls](check_chord_controls.py) | 5,616 exact | 24 heat germs, 144 stationary roots, 1,152 zero-free windows at three scales | [Record](CHORD_CONTROLS_20261015.json) |
| [Reflection algebra](check_weighted_reflection_algebra.py) | 51 exact | Source derivative polynomials and finite endpoint recurrences | [Record](WEIGHTED_REFLECTION_ALGEBRA_CHECKS_20261015.json) |
| [Weighted-square collision](certify_square_support_endpoint_collision.py) | 50 validated | Three-mode non-theta collision with first source endpoint and complete real tails | [Record](SQUARE_SUPPORT_ENDPOINT_COLLISION_CHECKS_20261015.json) |
| [Period-two contour](check_period_two_contour.py) | 73 exact or validated | Complete-theta contour and bilocal identities with all lattice/ray tails | [Record](PERIOD_TWO_CONTOUR_CHECKS_20261015.json) |

Each checker accepts `--output PATH`. The first two use the Python standard library; the last two require python-flint 0.9.0 and use 160-bit and 192-bit arithmetic respectively. All run without remote data. The final weighted-square source is not theta. The contour samples are not stationary sign certificates. General collision exclusion, the fixed-endpoint theorem and reflection rigidity are analytic arguments in the linked notes, not consequences of counting finite checks.

## Manuscript integration and handoff

The [integration checks](MANUSCRIPT_INTEGRATION_CHECKS_20261015.json) record source-reference, saved-research integrity, local-link and PDF checks for the revised manuscript. The [chat-history checkpoint](CHAT_HISTORY_VERIFICATION_20261015.json) is a separate provenance check; its hashes describe the capture at verification time and will change on subsequent legitimate refreshes. Neither record is a theta sign certificate.

## Coefficient core and two-endpoint replay

The [continuation manifest](COEFFICIENT_CORE_AND_TWO_ENDPOINT_CHECKS_20261015.json) records four new installed checkers, receipts, note hashes and independent replays. They pass **2,136 overlapping exact assertions** and **26 mixed or validated assertions**. These counts are not counts of distinct theorems.

| Checker | Assertions | Scope | Receipt |
| --- | ---: | --- | --- |
| [Exponential average](check_exponential_average_chords.py) | 1,620 exact | 36 heat germs, 108 complete stationary starts, 216 whole zero-free intervals, averaged-chord limits | [Record](EXPONENTIAL_AVERAGE_CHORD_CHECKS_20261015.json) |
| [Elliptic core](check_theta_elliptic_core.py) | 481 exact | Full translated fourth-jet operator, cutoff bands, projected ramp controls, finite primitive endpoints | [Record](THETA_ELLIPTIC_CORE_CHECKS_20261015.json) |
| [Outer budget](check_theta_outer_budget_audit.py) | 35 exact | Four low-index ranges, improved constants, conditional height allocations | [Record](THETA_OUTER_BUDGET_AUDIT_20261015.json) |
| [Two-endpoint control](check_theta_two_endpoint_control.py) | 26 mixed or validated | Positive four-square collision with two odd source endpoints; 44 complete integrals with real tails at 160 bits | [Record](THETA_TWO_ENDPOINT_CONTROL_20261015.json) |

Each script accepts `--output PATH` and prints its result. The first three use the Python standard library; the two-endpoint checker requires python-flint 0.9.0. Its default mode certifies the saved bracket; `--search` also performs a bounded exploratory search and is not needed for replay. No remote data or large generated archive is required.

The new collision is non-theta. The outer budget retains unevaluated exponent-pair constants and the original domain restrictions. The general shrinking-window criterion, infinite-series rigidity and outer analytic estimates are proved in the notes, not by assertion counts. No theta signed-core bound, new global sign certificate, or RH conclusion follows from these records.

## Coupled product, parity strip and reflection control

The [continuation manifest](COUPLED_PRODUCT_CONTINUATION_CHECKS_20261015.json) binds three new notes, checkers and independent replays. The new checks pass **3,278 exact assertions** and **38 mixed or validated assertions**, with overlapping algebra explicitly distinguished from general analytic arguments.

| Checker | Assertions | Scope | Receipt |
| --- | ---: | --- | --- |
| [Coupled theta product](check_coupled_theta_product.py) | 1,739 exact | Mixed addition, complete double source operator, coefficient controls, indefinite parity blocks, zero-sum witnesses and primitive endpoints | [Record](COUPLED_THETA_PRODUCT_ALGEBRA_20261015.json) |
| [Parity strip cutoff](check_parity_strip_cutoff.py) | 1,539 exact | Lattice masks, box corrections, full-start factor criterion, parity algebra and asymptotic coefficients | [Record](PARITY_STRIP_CUTOFF_CHECKS_20261015.json) |
| [Center/separation and reflected control](check_theta_center_separation.py) | 38 mixed or validated | Essential mixed sectors and exact-time non-theta collision; six validated complete integrals at 160 bits | [Record](THETA_CENTER_SEPARATION_CHECKS_20261015.json) |

Each script prints its JSON result and accepts `--output PATH`. The first two use only the Python standard library. The last requires python-flint 0.9.0 and includes explicit real-tail allowances. No remote data, root search, or large derived archive is needed.

The [chat-history verification](COUPLED_PRODUCT_CHAT_HISTORY_VERIFICATION_20261015.json) separately checks registration 19, preserved provenance, stored/canonical hashes, the source prefix, and the preceding final's successful deferred capture. Its hashes describe a verification snapshot and legitimately change on later refreshes; they do not validate mathematics.

The actual-theta parity asymptotic and infinite coefficient-rigidity statements are analytic proofs in the notes. The reflected control is rigorously outside the polynomial-growth square-source class. None of these records supplies a theta signed-core inequality or an RH conclusion.

## Adjoint recurrence endpoint experiment

The [exact checker](check_adjoint_recurrence_boundary.py) passes **6,892 rational assertions** in the [saved receipt](ADJOINT_RECURRENCE_BOUNDARY_CHECKS_20261015.json). It verifies killed-walk reflection weights, finite currents, boundary and moment identities, normalization cancellation, recurrence-defect algebra, and finite-hierarchy controls. It uses the Python standard library and accepts `--output PATH`. Rational surrogate weights test the finite algebra; they are not actual-theta numerical sign data. The [manifest](ADJOINT_RECURRENCE_CONTINUATION_CHECKS_20261015.json) records the independent replay and the associated note, review, and manuscript identities. No signed endpoint estimate is certified.

The [recurrence manuscript integration manifest](RECURRENCE_MANUSCRIPT_INTEGRATION_CHECKS_20261015.json) identifies the revised source and 43-page export, current note identities, 12,271 exact replay assertions and page checks. Historical research manifests retain their old manuscript/note hashes. The separate [history audit](RECURRENCE_MANUSCRIPT_CHAT_HISTORY_VERIFICATION_20261015.json), produced by the read-only [history checker](check_recurrence_manuscript_chat_history.py), verifies formal replay identity 20 and prior completed finals without editing the archive.
