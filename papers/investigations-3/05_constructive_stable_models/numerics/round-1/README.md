# Round 1: bounded odd-dilation certificate

17 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.

The [script](certify_harmonic_obstruction.py) and its small
[certificate](HARMONIC_SIGN_CERTIFICATE.json) support
[round-one Note 01](../../notes/round-1/01_INDEPENDENT_SPIN_HEAT_FAMILY_AND_ODD_DILATION_OBSTRUCTION_CODEX_20261017.md),
section 4. They evaluate the complete theta field at two rational endpoints
and over the entire tripled interval using the exact xi identity. No theta
cutoff, cached zero list, fitted parameters or large data are used.

## Declared finite question and budget

Determine the signs of \(H_0(28.26945)\), \(H_0(28.26946)\), and the whole
interval \(H_0([84.80835,84.80838])\). The baseline is the exact identity
\(H_0(x)=\xi((1+ix)/2)/8\), in the repository's normalization.
Use exactly three evaluations at **160 bits**, with a **30-second** maximum,
no adaptive precision or subdivision. Stop if a finite enclosure or a
required sign is unavailable.

An initial sign scout produced definite signs. Before the retained
quantitative replay, add the requested radius **at most \(10^{-15}\)** for
each real and imaginary output, and require the signed margins to exceed
the exact rational **\(36/10^{14}=3.6\cdot10^{-13}\)**. The replay checks
this new quantitative conclusion; these two numerical thresholds were
not declared before the initial scout. The JSON preserves that distinction.

## Reproduce

Use Python with `python-flint` installed, then run from this directory:

```sh
python3 certify_harmonic_obstruction.py
```

The script prints its record and replaces the adjacent
`HARMONIC_SIGN_CERTIFICATE.json` only after all arithmetic checks pass.
Recorded environment: Python 3.10.0, python-flint 0.9.0, FLINT 3.6.0.
The finite evaluator uses rigorous Acb enclosures for gamma, zeta and the
remaining elementary functions; its dependency is described in the
[official documentation](https://python-flint.readthedocs.io/en/latest/general.html#inexact-numbers-and-numerical-evaluation).
Input decimals are rational values enclosed by Arb, not binary float inputs.

The endpoint signs prove the existence of a real zero in the first
interval. The entire tripled interval has a negative margin exceeding the
declared delta. The note's intermediate-value argument converts these
finite signs into a dimension-independent approximation obstruction.
The computation alone does not prove that implication, nor RH, simplicity,
or an obstruction to initially interacting spin models. The script hash
identifies its source; elapsed time can vary on replay. All artifacts are
small and comply with [LARGE_FILES.md](../../../../../LARGE_FILES.md).

## Alternatives examined before review

The [alternatives replay guide](ALTERNATIVES_REPLAY.md) records the nine-node source screens and the four-integral coupled-quartic coefficient certificate for Note 02. The contracts distinguish floating scouts from retained interval runs. Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol**, effort **ultra**, 17 October 2026; no formal round review.

The [field-growth continuation and exact convolution check](FIELD_GROWTH_REPLAY.md) support Note 03 and the requested unreviewed manuscript. The two new exclusion results need no new numerical theta run; a small standard-library rational certificate separately verifies the local potential coefficients of X+Y/4. Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol**, effort **ultra**, 17 October 2026.
