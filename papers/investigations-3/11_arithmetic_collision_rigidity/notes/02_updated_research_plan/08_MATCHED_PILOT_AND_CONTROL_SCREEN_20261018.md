# Matched bounded pilot and adversarial control screen

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance, **GPT-6.1 Sol (`gpt-6.1-sol`), actual effort max**.
Same-assistant internal computation and review. This is Stage 2 of
[overview 02][plan], following the [evaluator derivation][evaluator].

**Decision: validation passed; the performance gate did not pass. No larger
scan is justified by this comparison.** The shifted evaluator reduces the
added propagation error, but its measured cost is higher and the adjoining
region's certified margin improvement is below the predeclared threshold.
This concerns this implementation and configuration, not all contour methods.

Read the [result summaries][summaries] and [avoid index][avoid], especially
[controls][controls], [tests on known coverage][known] and [scoped claims][scope].
All finite regions in this note lie inside already known coverage. Their
exclusion is machinery validation.

## Baseline and fair comparison

The [baseline replay summary][baseline] records a fresh execution of the
original Investigation 22 script at 160 bits. All 786 checks, the 234
boundary segments, zero winding, 128 full-time interior strips, and exact
polygon and segment hashes match the retained certificate. Its original
complete tails and error are paid. The source and original record remain
unchanged.

The new comparison gives the real-source and shifted evaluators the same
D0 rectangle, first-jet conclusion, 160-bit precision, four retained modes,
cutoff one, Taylor degrees 50 and 12, quadrature tolerances and added-error
allowance. Both generate 77 midpoint derivatives through order 76 because
Stage 1 also needs Hxx. The shifted method additionally pays for its two
majorant integrals. Counts and times include rejected cells and construction.
The original 76-derivative boundary pilot is replayed as a separate historical
baseline rather than treated as an artificially expensive two-dimensional scan.

| Quantity | Real source | Shifted source |
| --- | --- | --- |
| D0 accepted strips | 128 | 128 |
| D0 worst added coordinate error | below 4.923e-17 | below 2.751e-18 |
| D0 construction plus strip proof | about 0.660 seconds | about 1.093 seconds |
| Adjoining accepted strips | 342 | 342 |
| Adjoining worst added coordinate error | below 4.923e-17 | below 5.420e-20 |

The adjoining region was declared before its test:
\([1/100,1/5]\times[45,65]\), with the same configuration and a ten-second
per-method budget. Both methods cover it. The shifted/real certified minimum
margin ratio is approximately 1.0000155, below the predeclared useful gain
of 1.1. The D0 real/shifted total cost ratio is approximately 0.604, below
the factor-two speed threshold. These timings are one measured run, not an
optimality or portable-complexity claim.

The [comparison record][record] includes the declaration, complete adjoining
cell covers, source identities and costs. The [driver][driver] reproduces
the original control checkers into temporary receipt files, binds those
fresh bytes, and checks their source hashes before consuming them.

## Source-specific adversarial tests

The same strict coordinate and signed-margin functions consume each
control's own enclosed jet. Theta tail constants are never substituted.
The three- and four-square mixtures are fixed at their proved Wronskian
roots; their interval parameters enclose one frozen source, not a
time-adaptive family. Positive source moments pay for a surrounding time
halo as well as the original spatial event bracket.

| Control | Outcome |
| --- | --- |
| Three-square | Original event certificate replayed; surrounding box at t=1/4 and x in (44.1303,44.1304) rejects both strict gates |
| Four-square | Original certificate replayed; surrounding box at t=1/100 and x in (83.5323729,83.5323730) rejects both strict gates |
| Reflected super-Gaussian | Original normalization and moment certificate replayed; source-specific moment bounds extend the exact event to a box around (1/4,pi/4), which rejects both gates |
| q_{T,a} | Select T=1/4, a=pi/2, x=1; complete Bessel-integral and moment tails give a surrounding event box rejecting both gates |
| Polynomial heat event | The exact solution x squared minus 2(t minus 1/4), on a surrounding event box, rejects both gates |
| Euler factor | The genuine p=41, c=1/2, t=1/5 negative-Laguerre witness is replayed and rejects the signed gate; it is not labelled a double event |

The q family retains its proved positive-threshold status without an
invented event location. Finite-prime orbit controls fail complete normalized
analytic reflection and have no effective event height here. Smooth shape
and positive-primitive controls retain their analytic witness status and fail
theta's square-mode data. The smooth-density and two-channel results apply
only in their proved classes; this theta evaluation certificate is not
extended to them. The [control catalogue][controls] supplies the source
references and scopes.

## Failed control implementation and repair

The initial q_{T,a} test stopped at the finite-jet guard. Direct diagnosis
showed that native `arb ** 2` in the installed python-flint 0.9.0 returned
NaN on a nontrivial interval centred exactly at zero. The quadratures
themselves were finite. No invalid control was accepted.

The repaired shared square operation constructs an outward enclosure from
the squared lower and upper absolute endpoints. It is used in the energy,
Laguerre expression and cosine-square control factor. Explicit finite checks
and bounded subdivisions are retained for control moments. The entire
validation, signed certificate and adversarial replay were rerun after the
change. Regression tests include the zero-centred square and strict equality.

**Stage 2 closes with validated machinery and a measured error improvement,
not a passed performance gate.** The plan permits analytic work to continue;
the local signed estimate is in [Note 09][signed].

[plan]: ../../research-overview/02_UPDATED_RESEARCH_OVERVIEW_AND_SOL_EXECUTION_PLAN_20261018.md
[evaluator]: 07_SHIFTED_EVALUATOR_AND_COMPLETE_ERROR_BUDGET_20261018.md
[baseline]: ../../numerics/BASELINE_REPLAY_SUMMARY_20261018.json
[record]: ../../numerics/SHIFTED_PILOT_COMPARISON_20261018.json
[driver]: ../../numerics/run_plan02_pilot.py
[signed]: 09_COMPLETE_MODULAR_SIGNED_ESTIMATE_20261018.md
[summaries]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[known]: ../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
