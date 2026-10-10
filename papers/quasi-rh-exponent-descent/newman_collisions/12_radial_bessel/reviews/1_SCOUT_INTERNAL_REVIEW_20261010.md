# Initial scout internal review

10 October 2026. Model: GPT-6 (Codex); exact serving variant and configured reasoning effort unavailable and not inferred. Checks are internal, not independent mathematical review.

Reviewed artifact: [Note 1](../notes/1_POSITIVE_THREE_DIMENSIONAL_THETA_LIFT_AND_NONLOCAL_GENERATOR_20261010.md). This is an author-side derivation and replay audit, not independent review.

## Scope and sign audit

The small-radius proof uses evenness at zero, a negative second-derivative certificate for the first theta summand, and a geometric bound on the rest. Beyond r=0.01 every summand has an increasing logarithmic-decay lower bound, sufficient to dominate 2tr. The center is treated by a removable singularity and remains positive. The result is restricted to t<=1/20 and does not claim optimal time. The exact radial generator contains its full nonlocal correction and has no general positive-cone preservation. The double-zero control is nonnegative, smooth and compactly supported, not strictly positive everywhere, and is not a theta state or a threshold claim. Radial and axis cutoffs are distinguished.

## Recorded checks

Integer polynomial recurrences, rational sign bounds, exponential constants and infinite geometric tail bounds were checked exactly with Fraction and rational Taylor enclosures. The first 18 positive tail terms and sampled theta values are separate floating-point diagnostics; global radius coverage follows from the analytic bounds in the note. The exploratory central value is not an interval certificate.

Replay: `check_radial.py`; [record](../numerics/SCOUT_CHECK_RECORD_20261010.json): **PASS**. All scripts terminate with assertions enabled. Exact rational checks are identified separately from floating-point diagnostics.

## Remaining obligation

Test an explicit theta-specific variation-diminishing or total-positivity property against the conditional signed fourth-jet target, keeping the Volterra correction and radial-cutoff endpoint terms.

The fourth-jet threshold target still requires its measured approximation payment and higher-multiplicity coverage from Note 13. No theta-specific collision inequality, threshold exclusion, improved Newman bound, or RH result is established.
