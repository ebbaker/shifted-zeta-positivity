# Numerics

24 October 2026. Prepared for Edward Baker with substantial LLM assistance,
gpt-6-astra (Codex), recorded effort max.

## GPT numerical owner and manual return

Within GPT research, **GPT-6.1 Sol (`gpt-6.1-sol`) owns all new numerical
work**, including code,
execution, numerical debugging, computational checks and reruns. GPT-6
Astra supplies the analytical request and reviews the returned evidence.
The author coordinates the chats. Use the
[request/return workflow](../../../../GPT_RESEARCH_MODEL_WORKFLOW.md)
and read the current packet in the existing progress register before work.
No ready packet means no numerical assignment. Sol may repair implementation
within the packet's scope and budget; mathematical changes return to Astra.
Historical records below retain their actual model attribution.

## Current role: support analytical results at infinite height

The author's 24 October clarification gives priority to analytical estimates
extending to unbounded height. HDA-19 outer-height analysis and HDA-16
endpoint estimates lead; numerical refinement of HDA-17 is supporting work.
See the [current handoff](../notes/22_CONTINUATION_FOR_FINITE_TRANSITION_CONTRACT_20261024.md)
and [progress register](../research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md).

Before each new run, record:

- The named analytic estimate or theorem using the result, and its
  height/time scope.
- The question, possible decision, finite regime, precision and work budget.
- The stopping rule and the error or remaining range controlled analytically.

Use numerics to test a proposed bound or regime, evaluate explicit
constants, check derived identities, or certify a finite input to a global
argument. Samples do not establish an infinite-height theorem. Stop once
the question is answered, a declared gate fails, or numerical uncertainty
is below the dominant analytical allowance. Expanding the height range,
mesh or precision requires a remaining analytic question; a better table
alone is not a research milestone. Reuse existing records where possible.

The 192-cell Note 23 trial remains a failed diagnostic. Further source or
filter refinement is not scheduled by default. The reproduction commands
below document existing work and do not constitute a new campaign.
See [avoid 10](../../../../avoid/10_numerics_ahead_of_the_question.md).

## Existing records

The opening [check script](check_cosine_average.py) compares the analytic
cosine period-average density with direct quadrature, and checks its
transverse mass. The [execution record](COSINE_AVERAGE_CHECKS_20261024.json)
contains the parameters and errors.

Run from this directory:

~~~sh
python3 check_cosine_average.py --output COSINE_AVERAGE_CHECKS_20261024.json
~~~

These opening checks concern the cosine slice model only.

## First actual-theta averaging pilot

[averaged_theta_round1.py](averaged_theta_round1.py) and its
[small execution record](AVERAGED_THETA_ROUND1_20261024.json) supply:

- 17 finite theta samples with spatial, temporal or combined averaging;
  exact and gradient-model covariance, analytic Laplacian covariance,
  density/potential consistency defects and current checks;
- source and filter quadrature refinements, including a failed initial
  differentiated tolerance and its repair;
- negative-time density crossover and covariance scaling checks;
- 12 cosine covariance checks and a colliding polynomial control.

See [the contract](../notes/03_FIRST_BOUNDED_AVERAGING_CONTRACT_20261024.md)
and [the findings](../notes/04_GRADIENT_CLOSURE_AND_ACTUAL_THETA_PILOT_20261024.md).
The evaluator is scoped to those bounded cases; it is not a general
large-positive-time or arbitrary-height source oracle. It uses eight
theta terms and a finite integration cutoff without interval enclosures.
The small-width defect comparisons are not evolved-solution error bounds.

Requires Python 3 and NumPy; the exact tested versions and script hash
are in the record. Recompute from this directory into a temporary file:

~~~sh
python3 -B averaged_theta_round1.py --output /tmp/AVERAGED_THETA_ROUND1_RECHECK.json
~~~

No coefficient fitting, root finding, peak matching, interval certification
or independent implementation was performed. Further full-source bounds,
coarse-averaging experiments and residual propagation belong here.
Keep large regenerable arrays outside Git under the repository's
[large-file policy](../../../../LARGE_FILES.md).

## Coarse positive-time source transfer and weak current

[coarse_theta_round2.py](coarse_theta_round2.py) and its
[small record](COARSE_THETA_ROUND2_20261024.json) implement
[Note 09](../notes/09_COMPLETE_SOURCE_MOMENT_TRANSFER_AND_WEAK_CURRENT_20261024.md).
The source is evaluated with logarithmic scaling; weighted mass, current
and time derivative are obtained by contour residues, without finding
theta roots or sampling narrow density peaks. The record retains source,
contour, displaced-contour, finite-difference and temporal refinements,
including the failed first contour tolerance. Final contour order is 224.

Run with Python 3 and NumPy, optionally limiting numerical-library threads:

~~~sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -B coarse_theta_round2.py --output /tmp/COARSE_THETA_ROUND2_RECHECK.json
~~~

The gate requires complete-source moments on a finite complex rectangle;
the record supplies floating evaluations, not interval enclosures. The
contour interpretation as real-plane kernel weights uses the real/simple
zero conclusion of that gate. This is not an arbitrary-time evaluator.
Logarithmic regulator bounds do not bound source quadrature or finite-
epsilon current error. No independent implementation or evolved model
is supplied. Reuse the record unless changes or a new question require
recalculation. Prepared for Edward Baker with substantial LLM assistance,
gpt-6-astra, actual recorded effort max, 24 October 2026.

The record’s source-parameter summary describes the refined slice runs.
Temporal averages and time finite differences use order 48 with cutoff 3
and 8 theta terms, as explicit in the script; the slice source refinement
checks the larger cutoff 3.25 and 12 terms.


## Two time limits and growing-height clock

[two_time_limits_round3.py](two_time_limits_round3.py) and its
[record](TWO_TIME_LIMITS_ROUND3_20261024.json) accompany Notes 11--12.
The record contains all-height-bound constant evaluations, finite negative
Gaussian comparisons, complete-source saddle allowances and floating
moments, four larger-height contour observations, and perturbed-lattice
determinant/matrix controls. It retains failed conservative finite gates.
No theta roots were fitted, and the all-height xi-derivative hierarchy
was not numerically evaluated. All computations are floating; the written
analytic proof, not the sample grid, supplies the unbounded-domain claim.

~~~sh
python3 -B two_time_limits_round3.py --output /tmp/TWO_TIME_LIMITS_ROUND3_RECHECK.json
~~~

Requires Python 3 and NumPy. The source uses saddle coordinates to avoid
resolving a shrinking peak on a fixed u grid. Source cutoffs/orders and
contour refinements are explicit in the script and record. See the
[same-assistant review](../reviews/03_TWO_TIME_LIMITS_AND_VANDERMONDE_SELF_REVIEW_20261024.md)
for the conservative bounds, noncertification and unevaluated degree cost.
Prepared for Edward Baker with substantial LLM assistance, gpt-6-astra,
actual effort max, 24 October 2026.

## Variable-epsilon exact identity controls

[variable_epsilon_identity_checks.py](variable_epsilon_identity_checks.py)
and its [small record](VARIABLE_EPSILON_IDENTITIES_20261024.json) accompany
[Note 14](../notes/14_VARIABLE_EPSILON_EVOLUTION_AND_ASYMPTOTICS_20261024.md).
The script uses sparse polynomials over exact rational coefficients and
only the Python standard library. It checks four corrected identities
for four positive regulators on H=z^2-2t, including its double event.
All 16 residual polynomials vanish exactly; nonconstant controls detect
terms that cannot be omitted. The record also retains exact Gaussian
control coefficients derived in the note.

~~~sh
python3 -B variable_epsilon_identity_checks.py --output /tmp/VARIABLE_EPSILON_RECHECK.json
~~~

These are exact algebraic control checks, not canonical-theta enclosures,
an independent implementation, or proof that an adaptive profile extends
outside its analytical domain. Prepared for Edward Baker with substantial
LLM assistance, gpt-6-astra, actual effort max, 24 October 2026.

## Adaptive forcing and differentiated transport

[adaptive_transport_checks.py](adaptive_transport_checks.py) and its
[record](ADAPTIVE_TRANSPORT_CHECKS_20261024.json) accompany
[Note 16](../notes/16_ADAPTIVE_FORCING_AND_DIFFERENTIATED_CLOCK_20261024.md). The standard-library script verifies 16
polynomial current/time identities, nine exact moment identities and
the signed radial source primitive. It evaluates the finite analytic
allowances through moment degree six, retaining failed gates and large
early derivative budgets. These evaluations are floating, not certificates.
It imports the existing variable_epsilon_identity_checks.py helper.

[adaptive_transport_theta_pilot.py](adaptive_transport_theta_pilot.py)
and its [record](ADAPTIVE_TRANSPORT_THETA_PILOT_20261024.json) add six
zero-measure contour observations at t=10^6 and 10^9. The script uses
NumPy and the existing two_time_limits_round3.py source evaluator;
centered covariance is formed before transport integration. Source,
contour and height refinements are recorded, including discrepancies
at their refinement floor. No roots are fitted or finite-epsilon peaks
sampled; the finite-epsilon transfer is analytical in Note 16.

~~~sh
python3 -B adaptive_transport_checks.py --output /tmp/ADAPTIVE_TRANSPORT_CHECKS_RECHECK.json
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -B adaptive_transport_theta_pilot.py --output /tmp/ADAPTIVE_TRANSPORT_THETA_RECHECK.json
~~~

No interval onset, independent implementation, full covariance closure
or reduced trajectory is supplied. Reuse these records unless a new
question or change justifies a rerun. Prepared for Edward Baker with
substantial LLM assistance, gpt-6-astra, actual effort max, 24 October 2026.


## Explicit saddle clock and finite Gaussian primitives

[explicit_saddle_clock.py](explicit_saddle_clock.py) and its
[record](EXPLICIT_SADDLE_CLOCK_20261024.json) accompany Note 19. They
check 72 exact rational phase/current identities, evaluate the improved
complete-source coefficient and final error budgets, reuse six theta
observations and add four held-out time/height observations. The largest
observed derivative discrepancy is 3.708e-7 of the mean derivative;
conservative bounds are much larger and retain failed/large early cases.
No roots or coefficients are fitted, and no interval onset is supplied.

[finite_bridge_primitive_checks.py](finite_bridge_primitive_checks.py)
and its [record](FINITE_BRIDGE_PRIMITIVES_20261024.json) check Note 20's
two Gaussian primitives in nine small cases. They do not select a source
mesh or evaluate the full finite-time bridge. Both scripts use NumPy;
the clock also imports the earlier source/contour and allowance helpers.

~~~sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -B explicit_saddle_clock.py --output /tmp/EXPLICIT_SADDLE_CLOCK_RECHECK.json
python3 -B finite_bridge_primitive_checks.py --output /tmp/FINITE_BRIDGE_PRIMITIVES_RECHECK.json
~~~

The clock's optional HDA_NUMERICS environment variable selects the folder
containing its recorded dependencies; the default is the script's folder.
The new contour refinements combine source and contour order changes;
contour height is varied separately. Several tiny upper-time errors are
near their refinement scale. Same-assistant implementation only.
Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra (Codex), actual effort max**, 24 October 2026.


## Finite-transition local bounds, HDA-15

[finite_transition_local_bounds.py](finite_transition_local_bounds.py) and
[record](FINITE_TRANSITION_LOCAL_BOUNDS_20261024.json) support Note 23.
Run with Python, NumPy and mpmath:

```sh
python3 finite_transition_local_bounds.py --output FINITE_TRANSITION_LOCAL_BOUNDS_20261024.json
```

The record fixes the contract and parameters, separates interpolation,
theta modes, tail and candidate arithmetic, and retains failed nodal and
primitive checks. Twelve observations and a bounded filter refinement do
not meet HDA-17. No interval arithmetic or continuous-domain enclosure is
used. The local series bound pays truncation only. The retained JSON is
small; no large derived data are stored. Prepared for Edward Baker,
gpt-6-astra (Codex), actual effort max, 24 October 2026.
