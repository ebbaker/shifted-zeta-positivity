# Initial scout internal review

10 October 2026. Model: GPT-6 (Codex); exact serving variant and configured reasoning effort unavailable and not inferred. Checks are internal, not independent mathematical review.

Reviewed artifact: [Note 1](../notes/1_HUSIMI_READOUT_DRIFT_AND_COHERENT_INTERFERENCE_20261010.md). This is an author-side derivation and replay audit, not independent review.

## Scope and sign audit

The Wigner convention, Gaussian variances, minimum-width relation and coherent-overlap normalization are printed explicitly. Gaussian convolution introduces u squared, 4au partial_u, 2a and 4a squared partial_u squared while negative partial_p squared survives. The inverse smoothing operator is not asserted bounded. Scalar reconstruction and its first four derivatives include all Gaussian product terms and all normalizer derivatives. Time-dependent widths require additional generator and readout terms. The doubled coefficient vector retains phase-sum blocks as well as ordinary density entries. Husimi positivity and weak-limit o(1) error do not imply an exponentially paid coherent lower bound.

## Recorded checks

The four Gaussian jet polynomials were verified exactly over rational numbers. A Gaussian wave amplitude checks the full Husimi generator by finite differences; a finite complex block checks doubled value, derivative and positive-matrix observed squares. Those finite floating-point controls are not a genuine arithmetic sign certificate.

Replay: `check_phase_space.py`; [record](../numerics/SCOUT_CHECK_RECORD_20261010.json): **PASS**. All scripts terminate with assertions enabled. Exact rational checks are identified separately from floating-point diagnostics.

## Remaining obligation

Seek an interference-sensitive inequality for a composite-complete genuine block, recombined with a measured full-sum remainder smaller than the collision or threshold-jet margin.

The fourth-jet threshold target still requires its measured approximation payment and higher-multiplicity coverage from Note 13. No theta-specific collision inequality, threshold exclusion, improved Newman bound, or RH result is established.
