# Continuation after version 0.4

10 September 2026. Begin with `README.md`, `STATUS.md`, the v0.4 manuscript, and
`numerics/README.md`. Earlier continuation guides are under `archive/drafts/`.

## What is established

Two-sided enclosures of $\lambda_{\min}(Q_{0,L})$ at $L=\log2,\log3,\log4,\log5,\log6,9/5,\log7$
(Table 1 of the manuscript; machine-readable in `numerics/output/enclosure_summary.json`),
with sector-wise floors and upper bounds, the even ground state certified at every
horizon, and small-shift contraction with the constants of Table 1. All floors are exact
rationals passing the ball Schur test; all upper bounds are ball Rayleigh quotients.
Compression covers all shorter horizons. The `log 5` row is consistent with Zhu's
certified floor at total length 1.6 (compatible lower bounds by different methods; not a
cross-check of either implementation). The enclosures fall rapidly along the profile, but no
decay law at unbounded depth is proved.

## Conventions

`L` is total input length, the centered input is `(-L/2, L/2)`, autocorrelation support is
`[-L, L]`, Suzuki's cutoff is `a = exp(L/2)`. At a logarithmic endpoint the endpoint delay
is zero on `(0, L)`. Generator indices at `log 7`: 2, 3, 4, 5; reflected ordered overlaps
`(2,2), (2,3), (3,2)`; at `log 5` and `log 6` only `(2,2)`; none at `log 4` and below.

## Next experiment: log 8

Generator indices become 2, 3, 4, 5, 7; the endpoint delay 8 vanishes; `n = 2` acquires a
three-step chain (norm `sqrt 2`, exact endpoint case). The scalar tail floor at `N = 128`
is negative (`≈ -0.20`), `0.52` at `N = 256`, `1.22` at `N = 512`; the required coupling
diagnostic has been rising along the profile (0.17 at `log 2`, 0.59 at `log 7`) and will
rise again with the new prime. Plan on `N = 512`. The target floor will be of order
`1e-32` to `1e-34` (a local extrapolation of Table 1, not a prediction), so keep the profile error far below it:
`M ≈ 300` gives `eta ≈ 1e-47` at `L = log 8`; use about 2000–2500 bits. Matrix assembly
scales like `N (N+M)^2` ball products, so expect tens of minutes, not seconds. Then:

1. `python certify_arb.py --N 512 --M 300 --bits 2304 --log-horizon 8 --floor 1e-40 --output output/log8_N512`
   (any small floor; the enclosure step finds the real one).
2. `python enclose_certificate.py output/log8_N512`, then `certify_arb.py --reuse` at the
   reported floor and `analyze_certificate.py` with the reported constants.
3. `independent_arb.py` at the same parameters and `compare_implementations.py` (add the
   pair to `PAIRS`).
4. `make_tables.py` regenerates the manuscript tables (lower values rounded down, upper
   values rounded up from the full ball); add the row to the text.

Use the sharper leakage error of Remark 5.3 only if the ordinary error becomes a
constraint; at these parameters it is not.

## Beyond log 8

The figures here are resource projections for the present implementation, not
impossibility bounds: at any fixed `L < 3` the scalar tail floor `a_(N,L)` tends to `+∞`
as `N → ∞`, so what grows is cost, and whether a floor near 0.6 suffices at a horizon with a
new prime is not known. Keeping the scalar tail floor near 0.6 would need roughly
`N ≈ 950` at `log 11`, `1900` at `log 13`, `4400` at `log 16` and `27,000` as `L → 3`, the
boundary of the proved profile remainder (Section 7.2 of the manuscript). The only idea on
record that could change this
scaling is a structured tail bound that keeps the prime–gamma cancellation instead of
paying the full arithmetic loss; a frequency-band (prolate or band-limited) tail basis is
the natural first experiment, and it is genuinely open whether it is easier than the
original problem. For horizons past 3, validated piecewise polynomial profiles replace the
origin-centered expansion (Section 7.2).

## Formalization entry points

Lemma 4.1 (fractional tail), Lemma 5.1 (parity leakage) and Proposition 5.2 (Schur test)
are self-contained statements; the archived dyadic ball matrices with the LDL replay
specification are a realistic target for a verified checker. The analytic normalization
(Section 2) and the written-out Proposition 3.4 are the prerequisites a formalizer will
need.

## Open qualifications

- No certificate beyond `log 7` is asserted.
- No storage induction from a preceding slab alone has been proved; Appendix B records
  the identities such an induction would carry, and the 2×2 example shows scalar margins
  are insufficient.
- The diagonal all-depth implication (Prop. 7.2) is valid; the required sequence has not
  been constructed. No RH or zero-free-region result follows.
- The interior shift ranges of the companion first-slab and second-slab manuscripts of
  this repository are separate; the small-shift intervals here do not connect to them.
- Head eigenvalue lists and relative-coupling diagnostics are floating-point diagnostics.
  Sign decisions use Arb enclosures, the infinite-tail proof and the analytic profile
  remainder only.
