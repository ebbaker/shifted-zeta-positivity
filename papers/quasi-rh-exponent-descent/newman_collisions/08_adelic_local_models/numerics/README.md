# Exact finite scout checks

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are unavailable and are not inferred. Internal LLM checks are not
independent mathematical validation.

Run from the repository root:

```bash
python3 papers/quasi-rh-exponent-descent/newman_collisions/08_adelic_local_models/numerics/check_adelic_scout.py
```

The checker uses only the Python standard library, with exact `Fraction`
coefficients in sparse formal polynomials. It writes
[adelic_scout_record_20261010.json](adelic_scout_record_20261010.json) with its own source SHA-256,
assertion count, and check families. The retained run passed 440
assertions. A fresh repeat reproduced the record byte for byte.

Six-term valuations, mixed heat polynomial, Gaussian moment coefficients, four raw-jet recurrences, and formal diagonal-rational exponent cancellation.

The six-term model is an algebraic control, not a shrinking-sector cutoff or an infinite adelic realization. Gaussian moments and formal character compatibility do not certify a new actual-phase sign.
Assertion counts and source hashes establish reproducible finite algebra,
not independent mathematical evidence for the missing research theorem.
The analytic domain and interchange arguments are in
[Note 1](../notes/1_SHARED_HEAT_COORDINATE_AND_DIAGONAL_RATIONAL_COMPATIBILITY_20261010.md). A failed assertion exits without reporting
success; no floating root searches or uncertified numerical signs are used.

All retained files are small. No external archive is needed for these
checks; follow [LARGE_FILES.md](../../../../../LARGE_FILES.md) if future
experiments generate large derived data.
