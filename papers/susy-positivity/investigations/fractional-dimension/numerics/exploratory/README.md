# Exploratory computations

Programmes here are **not registered check programmes**: they may use `mpmath`,
which the repository's conventions exclude from registered checks, and nothing
replays them automatically. They exist so that every number quoted in the notes
is reproducible.

No exploratory programme yet.

The instrument for the compressed transfer already exists in the parent
investigation and should be used rather than rebuilt: the registered assembly
[`check_contraction_margin.py`](../../../loewner/numerics/check_contraction_margin.py)
in double precision, and
[`contraction_margin_gj.py`](../../../loewner/numerics/exploratory/contraction_margin_gj.py)
at arbitrary precision, which computes $\lVert V_{\omega,L}\rVert$,
$\lambda_{\min}(D_{\omega,L})$ and the Cayley data at any horizon and any
$\omega\in(0,\frac12]$.

See the [checks index](../README.md).
