# Finite continuum signed-pair certificate

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. Internal same-model research checks.

For the existing norm-one prepared probe, this package encloses constants
which, together with the proofs in the
[research note](../../notes/selective-loss-program/05_quadratic_target_and_finite_sign_20261003.md),
establish

\[
|p(y)|<4.97\quad(1\le y\le225),\qquad J(1)<1.27,
\]
\[
\Theta(Y)<-5\quad(100\le Y\le225),\qquad
\Theta_+(Y)=0\quad(100\le Y\le225).
\]

All endpoints are real and the claims cover the complete intervals.
No grid interpolation or direct enumeration of primes near exp(225) is
used. The global quadratic signed-pair bound remains unproved.

## Contents and scope

- `certify.py`: exact polynomial reconstruction and rigorous Arb/Acb
  constants. It checks the complete count N(500)=269, enumerates the
  first 270 consecutive positive zeros, and encloses the low transform
  mass and sixth-power tails. It installs and downloads nothing.
- `bound_192.json`, `bound_256.json`: separate outward production records,
  including dyadic rational endpoints, input parameters, software versions,
  source hash, and exact final margins. Each is a small scalar record;
  no growing zero cache or dense matrix is retained.
- `replay.py`: standard-library rational record audit. It checks source
  hashes, interval order, cross-precision overlap, rational thresholds,
  the combined envelope, and the increasing finite-sign margin. It also
  independently reconstructs the norm and derivative data and checks the
  cumulative-autocorrelation signs used in
  [mechanism note06](../../notes/selective-loss-program/06_global_mechanism_tests_20261003.md).
- `replay_record.json`: the retained small record of the successful rational audit.
- `PREFLIGHT.md`: calculation scope and cost limits recorded before the
  two production runs; discloses an earlier exploratory low-zero calculation.
- [Internal review](../../reviews/SELECTIVE_LOSS_QUADRATIC_TARGET_REVIEW_20261003.md):
  derivation and implementation audit.

The arithmetic script checks scalar constants. The explicit formula,
diagonal inequalities, and interval monotonicity are mathematical steps
supplied in the note. The finite-height RH verification through
3*10^12 and the global zero-count majorant are published external inputs.
The replay does not prove either published theorem and does not rerun
the zero enumeration. No A/B inverse, full source-space residual, or
global selective allowance is computed.

## Reproduction

Use Python 3 and an existing `python-flint` installation. The two recorded
runs used Python 3.10.0, python-flint 0.9.0, and FLINT 3.6.0. Their recorded
durations were below one second each on this host; this is not a general
runtime guarantee. From this directory:

```bash
python3 certify.py --bits 192 --output /tmp/sonin_quadratic_192.json
python3 certify.py --bits 256 --output /tmp/sonin_quadratic_256.json
python3 replay.py
```

The generator writes to the explicitly supplied output path. Compare
the regenerated enclosures and strict thresholds with the retained
records; interval arithmetic may vary with the software version, and
runtime metadata changes. The source hash identifies the generator,
not a mathematical proof or a guarantee of portable bit identity.
The replay audits the retained records in this directory. A full
regeneration additionally requires the already stated analytic inputs.

## Inputs

- [Platt and Trudgian, finite-height RH verification](https://arxiv.org/abs/2004.09765).
- [Hasanalizade, Shen and Wong, explicit zero count](https://arxiv.org/abs/2107.06506).
- [FLINT rigorous zero enumeration and counting](https://flintlib.org/doc/acb_dirichlet.html).
- [Earlier pole-inclusive zero-tail derivation](../../notes/GLOBAL_GROWTH_ZERO_TAIL_20261003.md)
  and [complete linear response](../../notes/selective-loss-program/04_complete_response_and_signed_pairs_20261003.md).

All retained sources and scalar records are small. No third-party papers,
large derived arrays, or dependency installation are part of this package.
