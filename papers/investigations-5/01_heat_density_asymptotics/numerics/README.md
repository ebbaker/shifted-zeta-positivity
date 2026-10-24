# Numerics

24 October 2026. Prepared for Edward Baker with substantial LLM assistance,
gpt-6-astra (Codex), recorded effort max.

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
