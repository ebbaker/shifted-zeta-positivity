# Exact checks and execution records

> **17 October 2026 — history routing update.** Historical formal-replay routing below is superseded. Chats [20](../chat-histories/0020_2026-10-15T15-16-42Z_brainstorm-theta-geometry-paths.json), [22](../chat-histories/0022_2026-10-15T18-10-39Z_review-theta-manifold-geometry.json) now use this investigation's [local registry](../chat-histories/index.json), as recorded in the [relocation receipt](../CHAT_HISTORY_RELOCATION_20261017.json). Original identities, provenance and public messages are preserved. All future Investigation 22 chats belong in this local history folder.

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

## Joint source current and signed quotient replay

The [checker](check_joint_source_current.py) passes **3,803 rational assertions** in the [receipt](JOINT_SOURCE_CURRENT_CHECKS_20261015.json). It checks all finite rectangular boundaries, killed-current/source commutation, symbolic source reduction, cutoff-aware source lower traces, exact signed matrix thresholds, and a degenerating analytic matrix example. It uses the Python standard library and accepts `--output PATH`. Rational source parameters and normalization weights are stand-ins for finite algebra, not theta numerical sign data. The [continuation manifest](JOINT_SOURCE_CONTINUATION_CHECKS_20261015.json) binds the files, independent replay, and unchanged manuscript identities.

## Scalar stationary geometry review

The [checker](check_stationary_scalar_geometry.py) passes **1,291 rational assertions** in the [receipt](STATIONARY_SCALAR_GEOMETRY_CHECKS_20261015.json), using the existing joint-current polynomial engine and the Python standard library. It accepts `--output PATH`. Checks cover finite heat expansions, leading predecessor coefficients, gauge identities, cone bounds and non-theta controls. The [manifest](SCALAR_STATIONARY_GEOMETRY_REVIEW_CHECKS_20261015.json) records the byte-identical independent replay, analytic review and unchanged manuscript identities. The arbitrary-order analytic theorem and infinite-current limits are proved in the note; no theta sign is certified.

## Scalar manuscript integration and positive-tail pilot

The [combined manifest](SCALAR_MANUSCRIPT_AND_TAIL_CONE_CHECKS_20261015.json) binds the 49-page source/PDF, new notes and reviews, two byte-identical exact replays totaling **5,094 assertions**, and the [positive-tail checker](check_positive_tail_cone.py). The latter passes **52 exact or validated assertions** using 32 Arb/Acb integrals at 160 bits; its [receipt](POSITIVE_TAIL_CONE_CHECKS_20261015.json) includes all source and mode tails, full parameter errors, the limit vector, root bracket and both ordinary-cutoff comparisons. It requires python-flint 0.9.0 and accepts `--output PATH` and `--bits`. Independent mathematical receipts match after removing only runtime timings. Neither the finite box nor its broader positive-mixture sign provides the missing global theta inequality.

The [spacetime topology checker](check_spacetime_topology.py) uses only exact standard-library rational arithmetic and Sturm isolation. Its [receipt](SPACETIME_TOPOLOGY_CHECKS_20261015.json) records 1,573 assertions on 60 polynomial rectangles through multiplicity 16. The [review manifest](TOPOLOGICAL_REFORMULATION_REVIEW_20261015.json) records the clean-process replay and source identities. These are polynomial controls, not theta integration or RH verification.

## Arithmetic dilation continuation

The [dilation checker](check_arithmetic_dilation.py) passes **47 exact assertions** in its [receipt](ARITHMETIC_DILATION_CHECKS_20261015.json). It uses only the Python standard library and accepts `--output PATH`. Checks cover finite divisor/sieve masks, source and transform scaling, complete lower intervals, endpoint-specific source traces, the complete first factor, and rational coarse remainder constants. The [manifest](ARITHMETIC_CONTINUATION_CHECKS_20261015.json) records the independent replay and unchanged manuscript/PDF identities. Infinite convergence, positive-time divergence and universal arithmetic statements are analytic arguments in the notes, not conclusions of finite enumeration. No theta quadrature or signed-domain certificate is supplied.

## Arithmetic manuscript integration

The [integration manifest](ARITHMETIC_MANUSCRIPT_INTEGRATION_CHECKS_20261015.json) binds the final 56-page source/PDF, review and handoff, a replay of all **47 exact arithmetic assertions**, 274 unique labels, 35 bibliography entries and individual inspection of every rendered page. It preserves the identities of earlier research notes and receipts. The [separate history audit](ARITHMETIC_MANUSCRIPT_CHAT_HISTORY_VERIFICATION_20261015.json) passes **37 read-only checks** on formal replay identity 22, public-message fidelity, stored/canonical hashes and the preceding final capture. History counts and hashes are audit snapshots, not mathematical certificates. Analytic convergence and divergence statements rely on their manuscript proofs and review.

## Independent recomputation (Claude review, 15 October 2026)

The [recomputation script](recompute_controls_claude_20261015.py) and its [record](INDEPENDENT_RECOMPUTATION_CLAUDE_20261015.json) accompany the [joint review of Investigations 21 and 22](../reviews/16_JOINT_REVIEW_OF_INVESTIGATIONS_21_AND_22_CLAUDE_20261015.md). Prepared for Edward Baker with LLM assistance; model Claude Fable 5.1 (`claude-fable-5-1`; configured identifier `claude-opus-5-5`). It recomputes, with mpmath tanh–sinh quadrature at 45 digits and no interval arithmetic, the three-square and four-square collision controls (Wronskian root, mixing parameter, raw weights, double zero, curvature, source and primitive endpoints), spot-checks the positive-tail inequality of Note 03/10 and the endpoint-only source tail bound, and reproduces the fixed-endpoint chord limit on a heat polynomial. All certified digits are reproduced. It is a floating-point cross-check by an independent method, not a validated certificate, and it says nothing about the theta sign estimate. Dependency: mpmath; runtime about three minutes; `--output PATH` saves the record. The same session replayed twenty-four of the twenty-five checkers in this folder (all pass; python-flint 0.9.0 is required by five of them, and `check_stationary_scalar_geometry.py` must be run from this directory because it imports a sibling module); `check_recurrence_manuscript_chat_history.py` needs the local registry lock file and was not replayed.

## Heat-germ degrees and indices (Claude reply, 15 October 2026)

The [check programme](check_heat_germ_degrees_claude_20261015.py) and its [record](HEAT_GERM_DEGREES_CLAUDE_20261015.json) accompany the [reply to Response 17](../reviews/18_REPLY_TO_RESPONSE_17_CLAUDE_20261015.md). Prepared for Edward Baker with LLM assistance; model Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork. It passes **120 assertions** (112 exact rational, 8 labelled floating point), using only the Python standard library; `--output PATH` saves the record and `--m-max M` sets the largest multiplicity (default 9); runtime about one second. For the Hermite heat germs of multiplicity \(m=2,\dots,9\) it verifies the heat equation, the isolation of the origin as the only common zero of \((H,H_z)\), the four-dimensional local degree \(m(m-1)/2\) as the exact degree in \(s\) of a Sylvester resultant at two rational values, the real spacetime index \(-\lfloor m/2\rfloor\) for both signs of the perturbation through exact Sturm isolation of the Hermite roots, and the Jacobian identity \(\det_{\mathbb C}=\mathcal L_1\). It also reproduces the two polynomial controls and the \(m=3\) example of Response 17, the endpoint behaviour of the strict and weak stationary signs on a double-collision germ, and (floating point) the heat-deformed dilation law \(H_{D_d\Phi}(t,x)=d^{-1/2}e^{ta^2-iax}H_\Phi(t,x+2ita)\) on a Gaussian source. Polynomial germs and closed-form transforms only: nothing here evaluates the theta field, certifies a theta sign, or bears on RH.

## Spacetime boundary and geometric continuation

The [wall-flux checker](check_spacetime_wall_flux.py) passes 2,122 exact assertions on 88 moving/fixed-wall domains plus two nontransverse-contact controls; it uses the sibling spacetime checker and the Python standard library. The [complex-multiplicity checker](check_complex_heat_multiplicity.py) passes 198 exact assertions with python-flint, verifying discriminants through order 16 and 27 asymmetric controls. The [complete-theta checker](check_theta_boundary_winding.py) passes 786 interval or exact assertions on [0.01,0.20] × [25,45], with 234 certified boundary segments, winding zero, both components changing sign, and a successful 128-strip interior baseline. Its receipt retains all tails, the uniform Taylor error, exact rational polygon and comparison counts.

All three scripts accept `--output PATH`; the theta checker additionally accepts `--bits` (default 160). The latter two were replayed with python-flint 0.9.0. Receipts are [wall flux](SPACETIME_WALL_FLUX_CHECKS_20261015.json), [complex multiplicity](COMPLEX_HEAT_MULTIPLICITY_CHECKS_20261015.json), and [theta boundary](THETA_BOUNDARY_WINDING_PILOT_20261015.json). The [manifest](SPACETIME_GEOMETRY_CONTINUATION_CHECKS_20261015.json) binds independent replays and unchanged inputs. The analytic results and limitations are in [Review 18](../reviews/18_SPACETIME_BOUNDARY_AND_GEOMETRIC_CONTINUATION_REVIEW_20261015.md). No new global theta sign or general speed advantage is claimed. Prepared for Edward Baker, 15 October 2026, with substantial LLM assistance; coordinating model **gpt-6-astra**, effort **ultra**.
