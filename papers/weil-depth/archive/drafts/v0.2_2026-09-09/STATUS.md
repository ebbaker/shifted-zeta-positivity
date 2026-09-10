# Verification status — Weil depth v0.2

9 September 2026. Working draft; not externally reviewed or formally verified.

| Claim or component | Review result | Evidence and limits |
|---|---|---|
| Central normalization and prime-power generator | Analytically reviewed | Suzuki's printed coefficient and transform formulas checked; pole/autocorrelation normalization expanded in the draft; 51 direct coefficient-derivative checks |
| Polynomial form core | Analytically reviewed | Dilation, mollification, C1 polynomial approximation, and boundedness of the finite-rank projection checked |
| Common-domain energy argument | Analytically reviewed | Positive-shift smoothing, interval restriction for Sobolev order below 1/2, and strong zero-shift limit checked; no norm derivative at zero assumed |
| Fractional infinite-tail estimate | Analytically reviewed | Weighted Jacobi norm written explicitly; three arbitrary tail-combination quadratures check the bound diagnostically |
| Full-output parity leakage and Schur test | Analytically reviewed and recomputed | Both exact full Grams retained; finite Toeplitz parity control; no finite-head-only inference |
| `Q_(0,9/5) >= 1e-26 I` | Full numerical rebuild and independent implementation PASS | `numerics/output/length_1p8_N128/`, `numerics/output/independent_1p8/`, and review comparison records |
| `Q_(0,log7) >= 1e-34 I` | New full numerical build and independent implementation PASS | `numerics/output/log7_N128/`, `numerics/output/independent_log7/`, and review comparison records |
| Small-shift and storage bounds at both horizons | Analytic consequence; exact rational checks PASS | Horizon-specific `analysis.json` files; shift bounds are sufficient, not optimal |
| Outward ball serialization and replay | Reviewed; PASS | Dyadic reconstruction containment; saved-ball sign tests; hashes, dimensions, analytic bounds, trace and leakage rechecked |
| Moment formulas | 45 independent numerical integrals PASS | `numerics/review/review_checks.json`; diagnostic quadrature, not interval certification |
| Stronger leakage error estimate | Proved in a new remark | Not used in either reported certificate |
| Storage update and nested Schur formulas | Algebraically proved | Positivity must still be verified at each step; no arithmetic preservation theorem |
| `log(8)` / horizons above `log(7)` | Not certified in this review | Builder accepts `0 < L < 3`; acceptance is not positivity |
| All-depth sequence / RH | Not proved | The diagonal implication does not construct the required sequence |
| Earlier first-slab certificate audit and second-slab shift gap | Outside this review | Neither is resolved by the new endpoint certificate |
| Novelty / external literature audit | Limited source check only | No exhaustive priority search or novelty certification |

Review and code were produced with OpenAI language-model assistance under the
author's direction. Two independently written implementations still share
Arb/FLINT and the same analytic reduction; their agreement is not a separate
proof of that reduction.
