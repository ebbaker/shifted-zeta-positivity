# Round 1 continuation: field growth and an exact quartic-convolution check

17 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.
Same-model authoring checks; formal round review remains pending.

[Note 03](../../notes/round-1/03_FIELD_GROWTH_AND_QUARTIC_NETWORK_OBSTRUCTIONS_CODEX_20261017.md)
and the [working manuscript](../../manuscript/constructive_stable_models.tex)
give two analytic results: the no-persistent-site condition for interacting
quartic networks, and the exclusion of independent pure-quartic arrays
with an added Gaussian. The latter has an analytic proof and a
weak-convergence corollary. Neither requires a new numerical theta run.

The separate [exact checker](certify_unequal_quartic_convolution.py) and
[small record](UNEQUAL_QUARTIC_CONVOLUTION_CERTIFICATE.json) clarify the
scope of the local potential screen: the stable source of \(X+Y/4\),
with \(X,Y\) independent pure-quartic variables, has positive quartic and
negative sixth potential coefficients.

Run with the Python standard library:

    python3 certify_unequal_quartic_convolution.py --output UNEQUAL_QUARTIC_CONVOLUTION_CERTIFICATE.json

The retained contract is fixed before exact verification: \(\delta=1/4\),
Taylor degree six, exactly three coefficients, fractions.Fraction
arithmetic, no quadrature, no special-function evaluation, no grid and
no refinement. An analytic derivation and floating scout preceded it.
The calculation uses the strict Cauchy inequalities
\(1/12<m^2<1/4\), \(m=\Gamma(3/4)/\Gamma(1/4)\), rather than computing
gamma values.

The record encloses the quadratic, quartic and sixth potential
coefficients in \((.09,.19)\), \((.97,.99)\), and \((-.25,-.11)\),
respectively. These are deliberately broad exact rational intervals.
The source hash identifies the checker, not a mathematical implication.
The integrated proof supplies the implication and the independent-array
obstruction; a local sign pattern is not theta approximation.

All records are small. No large data, external archive or manuscript
snapshot folder is created; see [LARGE_FILES.md](../../../../../LARGE_FILES.md).
