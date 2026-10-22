# BW-14 numerical records

21 October 2026. Prepared for Edward Baker with substantial LLM assistance;
actual model **gpt-6-astra (Codex)**, reasoning effort **max**.

[check_two_endpoint_tail.py](check_two_endpoint_tail.py) verifies the exact
source polynomial algebra and outward interval constants for
[Note 01](../notes/01_TWO_ENDPOINT_TAIL_CONSTRAINT_20261021.md).
Requires Python 3.10+ and `python-flint==0.9.0`.

```sh
python3 check_two_endpoint_tail.py --bits 192 --output /tmp/BW14_REPLAY.json
```

The [saved receipt](TWO_ENDPOINT_TAIL_CHECK_192_20261021.json) records the
runtime, script hash, fixed complex domain, complete arithmetic tails,
sharp relaxed mass cap and same-envelope direct comparison. The code has
no machine-specific paths, external data, oscillatory quadrature, or zero
search. It writes only the requested small JSON output. Full tails are
bounded analytically, not omitted after a finite sum. The proof, not the
number of checks, supplies the theorem. Review is same-assistant only.

## Full-reflection adjoint audit

[check_reflection_adjoint.py](check_reflection_adjoint.py) accompanies
[Note 02](../notes/02_FULL_REFLECTION_ADJOINT_AND_CONNECTOR_AUDIT_20261021.md).
It independently encloses the real half-line transform, paired shifted
transform and finite vertical connector for value and first derivative.
The frozen cases include real and complex t,z. It also checks the known
reflected super-Gaussian double event and the complete theta shifted
mode-tail constants on the stated complex-time domain.

```sh
python3 check_reflection_adjoint.py --bits 192 --output /tmp/BW14_REFLECTION_REPLAY.json
```

The [receipt](REFLECTION_ADJOINT_CHECK_192_20261021.json) records the
script hash, runtime versions, quadrature calls, interval enclosures and
full source exteriors. Requirements remain Python 3.10+ and
`python-flint==0.9.0`. All callbacks are entire and every unbounded
integral has a proved exterior payment. The control's exact collision is
proved analytically; zero-containing balls are only a regression check.
This is not a theta sign pilot, global search or measured cost comparison.
See the [self-review](../reviews/02_FULL_REFLECTION_ADJOINT_SELF_REVIEW_20261021.md).

## Finite-reflection algebra checks

[check_finite_reflection_algebra.py](check_finite_reflection_algebra.py)
accompanies [Note 05](../notes/05_FINITE_REFLECTION_JETS_AND_HEAD_TAIL_STABILITY_20261021.md).
It uses exact rational polynomial arithmetic to compare the source's
formal Taylor series with a separate derivative recurrence and to check
the heat/spectral signs of finite connector subtraction. It also checks
the conservative exponent arithmetic. Only Python's standard library
is needed.

```sh
python3 check_finite_reflection_algebra.py --output /tmp/BW14_FINITE_REFLECTION_REPLAY.json
```

The [receipt](FINITE_REFLECTION_ALGEBRA_20261021.json) records the runtime
and script hash. These are transcription checks for an analytic theorem,
not a numerical theta experiment, interval certificate, or independent
proof review. No new theta values or exclusion margins were acquired.
