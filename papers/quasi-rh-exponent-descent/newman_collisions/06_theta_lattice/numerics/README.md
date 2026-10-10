# Exact finite scout checks

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are unavailable and are not inferred. Internal LLM checks are not
independent mathematical validation.

Run from the repository root:

```bash
python3 papers/quasi-rh-exponent-descent/newman_collisions/06_theta_lattice/numerics/check_theta_lattice_scout.py
```

The checker uses only the Python standard library, with exact `Fraction`
coefficients in sparse formal polynomials. It writes
[theta_lattice_scout_record_20261010.json](theta_lattice_scout_record_20261010.json) with its own source SHA-256,
assertion count, and check families. The retained run passed 11
assertions. A fresh repeat reproduced the record byte for byte.

Rotor insertion, zero-mode differential identity, first four spatial derivatives, backward-heat compatibility, and formal spectator endpoint mismatch.

No actual oscillatory theta moments are numerically evaluated. Formal endpoint data do not certify a signed lower bound or the infinite trace interchange.
Assertion counts and source hashes establish reproducible finite algebra,
not independent mathematical evidence for the missing research theorem.
The analytic domain and interchange arguments are in
[Note 1](../notes/1_ROTOR_ZERO_MODE_WARD_IDENTITY_AND_SECTOR_MISMATCH_20261010.md). A failed assertion exits without reporting
success; no floating root searches or uncertified numerical signs are used.

All retained files are small. No external archive is needed for these
checks; follow [LARGE_FILES.md](../../../../../LARGE_FILES.md) if future
experiments generate large derived data.

## Conditional continuation

    python3 /absolute/path/to/06_theta_lattice/numerics/check_conditional_endpoint.py

Replay on 10 October 2026 passed 25 exact Fraction-polynomial checks.
The source-bound conditional_endpoint_record_20261010.json records
the conditioned higher-jet Jacobian, two opposite-sign formal jet
examples, and the zero-radius rational-anchor coefficient ratios.
These examples do not claim theta or positive-kernel realization.
The analytic Green representation and normalized positive control
are proved in Note 2; no numerical zero search is involved.
