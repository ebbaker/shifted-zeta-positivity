# Exact finite scout checks

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are unavailable and are not inferred. Internal LLM checks are not
independent mathematical validation.

Run from the repository root:

```bash
python3 papers/quasi-rh-exponent-descent/newman_collisions/07_automorphic_scattering/numerics/check_automorphic_scout.py
```

The checker uses only the Python standard library, with exact `Fraction`
coefficients in sparse formal polynomials. It writes
[automorphic_scout_record_20261010.json](automorphic_scout_record_20261010.json) with its own source SHA-256,
assertion count, and check families. The retained run passed 19
assertions. A fresh repeat reproduced the record byte for byte.

Completed incoming extraction, heat/completion commutator, cusp-gauge drift, eigenwave residual, and critical-line modular eigenvalue.

The checker verifies algebra, not a Maass–Selberg identity, Eisenstein domains, a positive flux theorem, or any heat-collision sign.
Assertion counts and source hashes establish reproducible finite algebra,
not independent mathematical evidence for the missing research theorem.
The analytic domain and interchange arguments are in
[Note 1](../notes/1_EISENSTEIN_EXTRACTION_HEAT_COMMUTATOR_AND_SPECTRAL_SLICE_20261010.md). A failed assertion exits without reporting
success; no floating root searches or uncertified numerical signs are used.

All retained files are small. No external archive is needed for these
checks; follow [LARGE_FILES.md](../../../../../LARGE_FILES.md) if future
experiments generate large derived data.
