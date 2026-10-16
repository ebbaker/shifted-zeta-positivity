# Finite-horizon Weil coercivity and shifted-zeta contraction

Review draft, version 0.1, 9 September 2026, Edward Baker.

## Read first

- `manuscript/FINITE_HORIZON_WEIL_REVIEW_20260909.pdf`: the review manuscript.
- `CONTINUATION_WEIL_DEPTH_20260909.md`: current project state and next task.
- `numerics/README.md`: rebuilding and replaying the numerical certificate.

The paper centers on the computer-assisted lower bound
`Q_(0,9/5) >= 1e-26 I`, the associated small-shift contraction, and the exact
parity/full-output method. Its analytic framework is self-contained. Earlier
slab computations are historical context and are not numerical inputs to the
principal theorem.

## Editable manuscript

`manuscript/finite_horizon_weil.tex` and `manuscript/finite_horizon_weil.bib`
contain the complete editable source. The generated `.bbl` is included for
convenience. Build with an ordinary TeX installation:

```bash
cd manuscript
latexmk -pdf -interaction=nonstopmode -halt-on-error finite_horizon_weil.tex
```

This produces `finite_horizon_weil.pdf`. The delivered PDF is the same compiled
content under a dated review filename. Standard packages include amsmath,
amsthm, lmodern, microtype, booktabs, enumitem, geometry, and hyperref.

## Numerical evidence

The complete direct-Arb supplement is under `numerics/`, including its own
research report, code, logs, all saved matrix balls, certificate pivot lists,
exact continuation checks, and original provenance hashes. It was copied from
the verified 9 September numerical supplement without modifying its source or
certificate data during the paper-writing pass.

All finite operations are enclosed by Arb, while the omitted analytic profile
and the infinite-dimensional tail have explicit mathematical bounds. The
ordinary floating-point eigenvalues in the analysis record are diagnostics.
They do not decide any positivity claim. The saved-ball replay and full builder
have different verification scopes, described in the numerical README.

`REVIEW_BUILD_RECORD.json` records the manuscript compilation checks and the
identity of the carried numerical matrix archive. `SHA256SUMS.txt` covers all
other files in this package. The numerical subdirectory's original checksum
list remains relative to that directory.

## Suggested review priorities

1. Central form normalization and the prime-power logarithmic generator.
2. Form-core density, positive-shift regularity, and the strong zero-shift limit.
3. The fractional estimate on arbitrary combinations in the infinite tail.
4. The exact central-parity leakage identity and positive-level Schur test.
5. Moment assembly, outward ball export/reload, and analytic error subtraction.
6. Separation of finite-depth results from the unproved all-depth goal.

The present materials are for review. No independent human audit or
proof-assistant formalization is claimed. No new license is imposed by this
packaging step; publication and repository licensing can be applied by the
author when preparing a release.
