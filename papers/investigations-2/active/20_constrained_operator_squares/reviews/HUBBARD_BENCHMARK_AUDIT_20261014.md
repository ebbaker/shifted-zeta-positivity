# Parallel internal audit of the Hubbard heat benchmark

14 October 2026. Prepared for Edward Baker with LLM assistance.
Reviewer model: `gpt-6.1-sol` (Codex); reasoning effort **ultra**.
Reviewed the [benchmark script](../numerics/hubbard_heat_benchmark.py) and
[research note](../notes/HUBBARD_HEAT_RESIDUAL_BENCHMARK_20261014.md).
This is a separate-agent check within the same LLM-assisted research
session, not independent specialist or literature validation.
Final audited script SHA-256:
`917df24bee6e715daa79505016449925f75d294134e4e9dea7a8ea56a284a6dc`.

**Decision.** The positive-interaction residual theorem, fixed-spin
product-Slater optimum, and selected-state rational interval arithmetic
are sound. The bounded quantum gate is supported by a useful correlated
energy certificate plus a clear cost limitation. No global grid optimum
or computational advantage is established or needed for that decision.

The denominator proof correctly uses `Psi=B^-1 rho-B^-1 u(T)` and
`||B^-1 rho||^2>=4Q1`; its positive `ell` condition is retained before
squaring. The numerator uses a nonnegative exact B-flow endpoint overlap
and `V<=V^2/nu` on a known positive spectral gap. These steps require no
commutation of B and V. In the script's `V=4P` specialization the
interaction energy is exactly `||R||^2/4`. The script keeps the terminal
term and certifies positivity of the selected denominator.

The global `-1/2` determinant result is correct for all complex
sector-preserving product orbitals. With fixed up-spin polarization,
optimizing the down-spin orbital gives `2-s-sqrt(5-4s^2)`, `0<=s<=1`.
The displayed square inequality proves the lower bound and equality at
`s=1/2`. Restricting to the declared `N_up=N_down=1` sector is essential
to the precise comparison and is stated in the note.

The interval arithmetic uses exact rational operations, valid alternating
lower/upper bounds for `exp(-1)`, monotone positive integer powers, and
outward integer-square-root bounds. Analytic exponential moments replace
time quadrature for every method. Selected certificates are rigorously
distinguished from floating grid selection and the unproved whole-grid
Cauchy-denominator diagnostic.

**Final replay and resolved corrections.** The current script adds the
full cross-integral energy/norm identities and checks their rational
interval differences contain zero. Those formulas agree with the seed
theorem. It checks the fixed direct-evaluation cost of 122 units *before*
executing each matched-budget candidate and confirms the count afterward;
no rejected pilot evaluation is performed. The note now correctly says
*norm-squared* lower bound, and the sentence fragment is repaired.

An independent replay completed successfully, including all selected
interval assertions and the new identity checks. It reproduced the
certified residual upper endpoint
`-0.50215397612677637283871231969`, below `-1/2`, and the direct comparison
of 225 evaluations using 27,450 of the 27,547 residual work units. The published [execution record](../numerics/HUBBARD_HEAT_BENCHMARK_20261014.json)
retains the certified data. No actionable audit issue remains.

The operation metric is transparently restricted to vector/mode
multiplications and additions. Precomputed common exponentials,
separate square-root counts, excluded scalar post-processing, and
excluded selected-state certification work are all disclosed. It is
appropriate for the stated bounded comparison but is not wall-clock
performance or a general complexity theorem. Residual cross overlaps
are not silently dropped in a larger-state claim.
