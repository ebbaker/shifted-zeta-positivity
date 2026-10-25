# Numerics

24 October 2026. Prepared for Edward Baker with substantial LLM assistance,
gpt-6-astra (Codex), recorded effort max.

## GPT numerical owner and manual return

Within GPT research, **GPT-6.1 Sol (`gpt-6.1-sol`) owns all new numerical
work**, including code,
execution, numerical debugging, computational checks and reruns. GPT-6
Sol also owns routine and moderately difficult analysis and interpretation;
Astra is reserved for extra high difficulty analytical bottlenecks.
The author coordinates the chats. Use the
[request/return workflow](../../../../GPT_RESEARCH_MODEL_WORKFLOW.md)
and read the current packet in the existing progress register before work.
A run needs a bounded question and stop rule; Sol may supply routine
derivations and scope details within an analytical assignment. Sol may
resolve routine mathematical issues and record a disposition. Revise a
frozen contract explicitly; escalate only a named extra high difficulty
issue. The root workflow supersedes the earlier analysis-only Astra rule.
Historical records below retain their actual model attribution.

## Current role: support analytical results at infinite height

The author's 24 October clarification gives priority to analytical estimates
extending to unbounded height. HDA-19 outer-height and HDA-16 endpoint
comparisons now exist at their stated scopes; the bounded HDA-17 task
supports their finite-core use and HDA-18 global assembly.
See the [current handoff](../research-progress/handoffs/HDA-17-AN01.md)
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

## Current bounded request

[HDA-17-AN01 r1](../research-progress/handoffs/HDA-17-AN01.md) is READY_FOR_SOL
for routine coefficient derivation and a bounded weak/local transfer
comparison. It tests Note 34's fixed-filter source orders 0/2, including
post-switch adaptive terms, against predeclared diagnostic targets. No
run has been executed. The prior 192-cell trial remains failed; its data
are a baseline only. The live progress register owns assignment status.

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


## HDA-17-AN01 r1 — completed diagnostic, failed acceptance budgets

24 October 2026; prepared for Edward Baker with LLM assistance,
**gpt-6.1-sol, actual effort ultra**, chat 0011.
[Decision note](../notes/35_WEAK_TRANSFER_BUDGET_DECISION_20261024.md),
[diagnostic](weak_transfer_diagnostic.py), [coefficient maps](weak_coefficients.py),
[exact controls](exact_controls.py), [control record](EXACT_CONTROLS_20261024.json),
[index record](WEAK_TRANSFER_DIAGNOSTIC_20261024.json),
and [assessment](../reviews/18_WEAK_TRANSFER_BUDGET_ASSESSMENT_20261024.md).
The index hashes T64/T96/T128 JSON records, each below 1 MiB, with all
requested coefficient/allowance rows and refinements. Uses only the twelve
centers, 192/384/768 cells, source rules 6/10, filters 16/32/64, and two
80/120-digit selected checks. Exact selected identities pass; source and
filter allowances fail, nodal/evaluation rounding remains unproved.
Local/default with componentwise weak gains is the decision; no continuous
core, endpoint join or certificate. Run the controls first, then the
diagnostic with --repo and an external/ignored --output; the index and
three per-time parts are regenerated. NumPy and mpmath are required.


## AN02 — source curvature and peak integration

24 October 2026; prepared for Edward Baker with LLM assistance,
**gpt-6.1-sol, ultra**, chat 0011. [Note 36](../notes/36_SOURCE_CURVATURE_AND_PEAK_INTEGRATION_20261024.md),
[source caps/weights](source_accuracy_improvements.py),
[diagnostic](source_peak_diagnostic.py), [controls](check_source.py),
[control record](SOURCE_CONTROLS.json),
[record](SOURCE_PEAK_DIAGNOSTIC_20261024.json) and
[assessment](../reviews/19_SOURCE_CURVATURE_AND_PEAK_ASSESSMENT_20261024.md).
Three uniform source-budget counts plus one a priori adaptive 768 mesh;
only t=64,x=4,y=0 or 1/2 fields, uniform 192/768 and adaptive 768.
Continuous curvature/chord formulas are evaluated in floating arithmetic.
Composite 8/12 uses 16384/36864 field points. Source allowance gain 24.37
times, but the Delta Q source budget remains 2056.73 times its allocation.
Actual weak/direct filter indicators and positive-envelope indicators are
separate; no continuous or rounding certificate. Main run 132.47 seconds.
Run check_source.py first, then source_peak_diagnostic.py with --repo and
an external/ignored --output. Frozen AN01 modules are imported read-only.


## AN03 — positive cubic-Hermite source and explicit remainders

24 October 2026; prepared for Edward Baker with LLM assistance,
**gpt-6.1-sol, actual effort ultra**, chat 0011.
[Note 37](../notes/37_POSITIVE_HERMITE_SOURCE_AND_REMAINDERS_20261024.md),
[source module](hermite_source.py), [main diagnostic](positive_hermite_diagnostic.py),
[exact controls](check_hermite.py), [control record](HERMITE_CONTROLS.json),
[r1 record](POSITIVE_HERMITE_DIAGNOSTIC_20261024.json),
[directional caps](hermite_directional_caps.py),
[r2 record](HERMITE_DIRECTIONAL_CAPS_20261024.json) and
[assessment](../reviews/20_POSITIVE_HERMITE_SOURCE_ASSESSMENT_20261024.md).
Uniform 192 and adaptive 384/768 sources; exactly t=64,x=4,y=0,1/2.
Positive stored Bernstein coefficients, paid fallback interpolation,
complete fourth-derivative/tail and ideal-Gauss truncation formulas;
source/nodal/evaluator rounding and continuous filter integration unpaid.
Same-mesh interpolation gain about 1963 times is not storage-neutral;
comparable-storage 384 still fails. R1's best source ratio 1.10507 remains;
r2 tightens only covariance caps and gives worst source ratio 0.688748.
All 91 rows retained/inherited. Eight exact polynomial families pass.
Numerical debit 160.042 seconds, below the 1800-second cap.

For reproduction with NumPy/mpmath, run a copy of check_hermite.py in an
external output folder (it writes its record beside itself), then run
positive_hermite_diagnostic.py and hermite_directional_caps.py with --repo
and external/ignored --output paths. R2 reads and hash-checks the frozen
r1 record in numerics; do not replace it during regeneration. Source arrays
are regenerated in memory, and every retained artifact is below 1 MiB.


## Fixed-gap local identity controls — HDA-18-AN01 r1

24 October 2026; prepared for Edward Baker with LLM assistance,
**gpt-6.1-sol, actual effort ultra**, chat 0015.
[Script](exact_gs8_gs12.py) and [record](EXACT_GS8_GS12_20261024.json)
contain six polynomial cases with 76 exact Fraction assertions: GS5,
GS9/GS11/GS12 and the exact TC time-product derivative. Covariance
mean-product algebra is checked separately, without convolution claims.
Final execution 0.9357732501 seconds; three bounded executions total
2.8043347919 seconds; no failures or theta sampling. See
[Note 43](../notes/43_FULL_SUPPORT_FIXED_GAP_TRANSFER_20261024.md) and
[Review 24](../reviews/24_FIXED_GAP_FULL_SUPPORT_ASSESSMENT_20261024.md).
For reproduction, copy the script to an external temporary output folder
and pass --investigation-root pointing to this investigation; it imports
the unchanged rational helper and writes its record beside the copy.


## Finite-input elementary majorants — HDA-18-AN02 r1

24 October 2026; prepared for Edward Baker with LLM assistance,
**gpt-6.1-sol, actual effort ultra**, chat 0015.
[Script](finite_input_rational_bounds.py) and
[record](FINITE_INPUT_RATIONAL_BOUNDS_20261024.json): five exact-rational
scalar checks, all passed in one 0.0001837501-second execution, no failures.
Complete-source fourth-derivative majorant/tail ratio, kernel coefficient
sums, regulator beta' bound and saddle-bracket arithmetic only. No
Phi/H/gamma/model-gap samples, source node evaluation, numerical search
or full theorem certificate. Note 44's finite source recipe was derived
and not run. Reproduce with a script copy in an external output folder;
it writes its record beside itself and needs only Python's standard library.


## Effective outer constant margins — HDA-18-AN03 r1

25 October 2026; prepared for Edward Baker with LLM assistance,
**gpt-6.1-sol, actual effort ultra**, chat 0015.
[Script](effective_outer_scalar_bounds.py) and
[record](EFFECTIVE_OUTER_SCALAR_BOUNDS_20261025.json): exactly six scalar
rational/integer checks, all passed in one 0.0000686250-second execution,
no failures. Alpha derivative, left/middle quadratic, arithmetic decay,
final field constant and initial FI23 margins only. No theta/source/
gamma/field sampling, numerical search or interval theorem certificate.
[Note 45](../notes/45_EFFECTIVE_FULL_BUFFER_OUTER_FIELD_20261025.md) proves
the uniform estimates; [Review 26](../reviews/26_EFFECTIVE_FULL_BUFFER_OUTER_FIELD_ASSESSMENT_20261025.md)
records the proof checks. Reproduce with a script copy in an external
output folder; it writes its record beside itself using Python's standard library.


AN04 r1, 25 October 2026, chat 0017: [AN04_ANALYTICAL_WORK_RECORD_20261025.json](AN04_ANALYTICAL_WORK_RECORD_20261025.json)
records zero optional scalar checks and no numerical research execution.
The complete sufficient analytical budget is in Note 47; this record is
not a numerical certificate. Prepared for Edward Baker with LLM assistance,
gpt-6.1-sol, actual effort ultra.


AN05 r1/HDA-22, 25 October 2026, chat 0017:
[AN05_ANALYTICAL_WORK_RECORD_20261025.json](AN05_ANALYTICAL_WORK_RECORD_20261025.json) records no numerical or machine-symbolic research
execution; none is authorized by this revision. Note 48 gives the
analytical fixed-width result. Prepared for Edward Baker with substantial
LLM assistance, gpt-6.1-sol, actual effort ultra.


AN06 r1/HDA-24, 25 October2026, chat0017:
[AN06_ANALYTICAL_WORK_RECORD_20261025.json](AN06_ANALYTICAL_WORK_RECORD_20261025.json) records zero numerical/exact-rational/machine-symbolic
research executions; none authorized. Note49 supplies the analytical
switch-interval proof. For Edward Baker with substantial LLM assistance,
gpt-6.1-sol, actual effort ultra. No source/evaluator executed.


AN07 r1, 25 October2026, chat0017: [AN07_ANALYTICAL_WORK_RECORD_20261025.json](AN07_ANALYTICAL_WORK_RECORD_20261025.json) records zero numerical,
exact-rational or machine-symbolic research executions, sampling or
mesh/precision/interval campaign. Notes50/51 record proof and chat results.
For Edward Baker with substantial LLM assistance, gpt-6.1-sol, actual effort ultra.


- [AN08 analytical work record](AN08_ANALYTICAL_WORK_RECORD_20261025.json):
  25 October2026, gpt-6.1-sol, actual effort ultra, chat0019. Zero research
  numerical/exact-rational/machine-symbolic runs; analytical constants and
  source recipes in Note54, housekeeping hashes/links/sizes only.


- [HDA23 analytical work record](HDA23_ANALYTICAL_WORK_RECORD_20261025.json):
  25 October2026, gpt-6.1-sol, ultra, chat0019. Zero numerical/rational/
  symbolic research executions; analytical source tolerance, description
  and construction-operation bounds in Note55, housekeeping only.


**HDA-17-AN05 analytical-only return, 25 October 2026, chat0021:**
[zero-run work record](HDA17_AN05_ANALYTICAL_WORK_RECORD_20261025.json),
prepared for Edward Baker with substantial LLM assistance, gpt-6.1-sol,
actual effort ultra. Note58 proves positive analytic-source compression
and finite construction bounds on paper. No numerical, exact-rational
or machine-symbolic research execution, source coefficient evaluation
or field/filter samples occurred. Hash/link/size checks are housekeeping.


**Note58 evaluator/filter analytical continuation, 25 October 2026:**
[zero-run record](NOTE58_EVALUATOR_FILTER_ANALYTICAL_WORK_RECORD_20261025.json),
gpt-6.1-sol, actual effort ultra, chat0021; prepared for Edward Baker
with substantial LLM assistance. Note59 derives working precision,
provider and continuous-filter bounds on paper. No numerical/exact-
rational/machine-symbolic research execution, evaluated source data,
mesh/precision search or interval campaign. Literal phase-index
construction remains unpaid; no executed arithmetic/filter acceptance.


**Note59 exact phase-index analytical continuation, 25 October 2026:**
[zero-run record](EXACT_PHASE_INDEX_ANALYTICAL_WORK_RECORD_20261025.json),
gpt-6.1-sol, actual effort ultra, chat0021; prepared for Edward Baker
with substantial LLM assistance. Note60 proves a finite rational selector
on paper, using explicitly authorized existing onset freedom. No rational
research algorithm was executed, no phase integer/source coefficient was
evaluated, and no numerical/machine-symbolic/interval campaign occurred.
Housekeeping hashes/links/sizes do not certify the mathematical claims.


**Complete evaluator/filter analytical improvement and chat summary:**
[zero-run record](COMPLETE_EVALUATOR_COST_ANALYTICAL_WORK_RECORD_20261025.json),
25 October 2026, gpt-6.1-sol, actual effort ultra, chat0021. For Edward
Baker with substantial LLM assistance. Note61's finite rational algorithms
and cost bounds are derived on paper; none was executed. Zero numerical,
exact-rational/machine-symbolic research runs, coefficients, samples or
interval campaigns. Note62 summarizes the chat. Housekeeping hashes,
links, sizes and history capture do not certify mathematical claims.
