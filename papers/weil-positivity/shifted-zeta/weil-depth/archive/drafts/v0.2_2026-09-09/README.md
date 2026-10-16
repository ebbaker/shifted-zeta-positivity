# Finite-horizon Weil coercivity and shifted-zeta contraction

Edward Baker. Working review draft v0.2, 9 September 2026.

The reviewed paper establishes computer-assisted central coercivity through
total horizon `log(7)`, retaining the stronger existing bound through `9/5`:

| Total horizon | Central floor | Shift interval | Transfer norm bound |
|---|---:|---:|---|
| `0 < L <= 9/5` | `1e-26` | `0 < omega <= 3e-14` | `exp(-5e-27 omega)` |
| `0 < L <= log(7)` | `1e-34` | `0 < omega <= 3e-18` | `exp(-5e-35 omega)` |

Read `FINITE_HORIZON_WEIL_REVIEW_v0.2_20260909.pdf`, `REVIEW_20260909.md`,
and `STATUS.md`. The editable source is `manuscript/finite_horizon_weil.tex`.
Build it with `latexmk -pdf -interaction=nonstopmode -halt-on-error`.
The numerical commands and evidence are in `numerics/README.md`.

Both horizons pass full rebuilds and a separately written Arb construction.
The bounds include the analytic infinite tail and profile remainder. Neither
floating-point eigenvalues nor zeta zeros decide the certificate signs.

The continuation guide has been updated: `log(7)` is completed; `log(8)` and
the proposed storage/structured-tail recursions remain next research targets.
No all-depth positivity, RH result, external human audit, or formal verification
is claimed. Text is covered by the repository's CC BY 4.0 license and code by
its MIT license.

The original v0.1 PDF and ZIP in the repository are preserved as the baseline.
`SHA256SUMS.txt` identifies this revision's deliverable files. Historical
reports and their original source hashes are retained under
`numerics/background/`, with their earlier status statements unchanged.
