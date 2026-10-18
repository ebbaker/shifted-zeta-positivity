# Round 2 exact return diagnostic

17 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model: **gpt-6.1-sol (Codex)**; effort: **ultra**.

Question: does the exact normalized return formula in round-two Note 01
agree with all four directly computed corner projections, including its
second-order coefficient and retained return terms?

The [program](round2_checks.py) reuses the declared Fraction matrix helpers
and unchanged rank-three model of the [Claude review program](../round-1/claude-review/review_checks_claude_20261017.py).
It checks the new identity, the symmetric double-return coefficient, the
sharper generic bound, the explicit cubic remainder and a dropped-return
negative control. All comparisons are exact rational arithmetic. This is
an internal same-model diagnostic using shared support code; it neither
models the actual Sonin projection nor certifies an arithmetic sign.

Run from this folder:

```sh
python3 -B round2_checks.py --output /tmp/ROUND2_CHECKS.json
```

The [record](ROUND2_CHECKS.json) includes program and reused-source hashes,
Python version, parameters, rational values and check outcomes. The domain
is one fixed previously used model; the resource cap is one run, with
failure of any identity or failure of the negative control to differ as
the stopping answer. Runtime was below one second. No approximation
tolerance, spectral fit or actual-prime sweep is used.

The [reconciliation record](RECONCILIATION_REPLAY_CODEX_20261017.json)
records a separate full replay of the original seven-section review:
every exact field agrees with the stored record; the largest difference
among floating fields in sections B–G is below 9e-13. Floating fields
remain diagnostics. The full regenerated record is temporary, rather
than a duplicate committed dataset.
