# Outward translated-probe checks

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); serving variant and reasoning effort not exposed.

This small package tests one necessary ingredient of an all-window
mechanism: signed long-range covariance between two translates of the
same prepared source. It is **not** another full-source window certificate.
See the [analytic probe criterion and preflight](../../notes/ALL_WINDOW_TRANSLATED_PROBE_CRITERION_20261003.md).

The source is the normalized form-domain function

    g=(-d²/dx²+1/4)d/dx [(1-16x²)^8 on |x|<1/4, zero outside].

Its three moments vanish exactly by preparation and endpoint integration
by parts. It is C4, not compactly smooth, and is approximable in the
logarithmic form norm by smooth exactly neutral sources. Its autocorrelation
on nonnegative shifts is an exact rational polynomial of degree 31, stored
in the small record. No sampled source grid or matrix archive is used.

## Reproduce

Dependencies: Python and python-flint. The recorded runtime is Python 3.10.0,
python-flint 0.9.0, FLINT 3.6.0. From this directory:

```sh
python3 -B certify_translated_probe.py --bits 192 --output /tmp/probe-192.json
python3 -B certify_translated_probe.py --bits 256 --output /tmp/probe-256.json
```

The originating Python 3.10 runtime found flint through
`PYTHONPATH=/private/tmp/sonin-moment-python-deps`; discover compatible
dependencies in a fresh environment instead of assuming that path exists.

Both precisions use exactly five separations 4,6,8,10,12 and a sieve limit
268338. The script has no adjustable window or separation sweep. Every
prime power is included, not merely primes. The diagonal Q[g] is computed
with Acb validated integration after removing the apparent singularity
analytically. The long-range archimedean term is bounded by an explicit
exponentially decaying formula. Prime sums, absolute sums, and all strict
Gram comparisons use Arb arithmetic.

`probe_192.json` and `probe_256.json` contain rational enclosures and bind
the source hash. `probe_replay_check.json` records the separate-agent
replay and bindings. The [final mechanism audit](../../reviews/ALL_WINDOW_MECHANISM_FINAL_REVIEW_20261003.md)
checks the analytic reduction and implementation. No previous full-source
certificate, inherited prolate input, or floating eigenvalue is an input
to these scalar checks.

`cost_preflight.py` and `cost_preflight.json` separately reproduce the
pessimistic counting-bound table in the effective-relative-tail note.
This standard-library floating calculation works only with logarithms;
it constructs no high-rank objects. Its values are sufficient-bound
diagnostics, not certified necessary ranks. Run `python3 -B cost_preflight.py
--help` for its output argument.

## Scope of the result

The diagonal lies between 1.46694003100528 and 1.46694003100529. All five
two-dimensional Gram matrices are positive. At separation 12, the signed
prime sum is about-0.777399, its absolute majorant is about 90.360169,
and the certified Gram margin is greater than 0.68954.

This isolates an arithmetic cancellation that survives exact moment
preparation. It does not establish positivity for all translates of this
source, all finite translate combinations, all sources on a larger
window, or arbitrarily large windows. The growth assertion for the absolute
majorant follows from a separate prime-number-theorem argument in the note;
it is not inferred by extrapolating these rows.
