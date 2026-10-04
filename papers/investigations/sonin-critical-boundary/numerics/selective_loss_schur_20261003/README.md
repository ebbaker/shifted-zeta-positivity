# Exact source covariance for the selective loss program

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. The derivation and computation have
internal same-model checks, not independent specialist review.

This small package calibrates the continuous source overlaps for the first
Schur completion approach. It uses the existing normalized polynomial
probe g and physical templates at 0,j,j+1/2,j+1 over j<=r<=j+1, j>=2.
It does not calculate the Sonin energy B, B inverse, correction K, relative
complement, or Schur loss.

## Result

The exact four-by-four overlap covariance Xi is independent of j. Its
entries are rational and obey I/32<Xi<=I/2. Consequently a common positive
template allowance Lambda has integrated loss Tr(Lambda Xi), between
Tr(Lambda)/32 and Tr(Lambda)/2, and pointwise loss at most 32 times that
integral. This describes the geometry of a potential certificate; a
certificate for the actual B and K is still needed.

The [detailed derivation](../../notes/selective-loss-program/01_schur_completion_20261003.md)
and [program overview](../../notes/selective-loss-program/overview.md)
state the arithmetic target and remaining obligations.

## Reproduction

Run from this directory:

```sh
python3 calculate.py
```

Only Python's standard library is used. The script regenerates the profile
and its degree-31 autocorrelation polynomial, integrates both half-shells
exactly with rational arithmetic, and checks the structured covariance.
It checks all 15 principal minors of Xi and of Xi-I/32 exactly, and the
moving-block row sums for the upper bound. Decimal eigenvalues are
diagnostics, not proof inputs. The script overwrites the small generated
records in this directory.

| File | Purpose |
| --- | --- |
| [calculate.py](calculate.py) | Standalone source and exact rational checks |
| [result.json](result.json) | Small record with exact constants, covariance, minors, source coefficients, script hash, and diagnostic decimals |
| [RESULT.md](RESULT.md) | Generated readable calculation record |

The script hash binds the record to the generating source. Its Python
version is recorded for reproduction; a hash is not used to prove a sign.
All outputs are small, and no external data or numerical library is
needed. This package is not a finite or global Weil positivity certificate.
