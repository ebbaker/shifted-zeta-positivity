# Round two certificates

17 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**.

The question is whether one useful regime of the transport budget can be
certified over its complete continuous domain and consumed by a written
comparison. The regime is p = 3, ell ≥ 129/5, 0 < h = t/2 ≤ 1/8;
the family consequence is q ≥ 10¹². The stopping gates are E < 1/5,
d₀ > 93/100, and the two strict rational restart inequalities. The
programs use no numerical quadrature or external dataset and run in under
a second each in the recorded environment.

| Program | Small record | Arithmetic and scope |
| --- | --- | --- |
| [Uniform floor](family_floor_gate_arb_20261017.py) | [Floor record](FAMILY_FLOOR_GATE_ARB_20261017.json) | python-flint 0.9.0, Arb 128 bits, 1,000 rational time cells and proved monotone endpoints; E < 0.192767. |
| [Restarted comparison gates](certify_restarted_strip_consumer_20261017.py) | [Exact gates](RESTARTED_STRIP_CONSUMER_SCALAR_GATES_20261017.json) | Standard-library fractions; upper and lower Taylor bounds for exponentials; terminal time 43/200. |

Run from this directory with Python 3 and python-flint installed:

```sh
python3 -B family_floor_gate_arb_20261017.py > /tmp/family-floor-replay.json
python3 -B certify_restarted_strip_consumer_20261017.py > /tmp/restarted-strip-replay.json
```

Every numerical decision fails closed; floating fields in the second
record are display-only. The first cell covers every positive h down to
zero; the exact time-zero formula is a separate analytic endpoint. The
unbounded ell range and all integration tails are reduced analytically
in [Note 01](../../notes/round-2/01_UNIFORM_FAMILY_FLOOR_CODEX_20261017.md).
The intermediate-strip transfer and its named strip-theorem import are
proved or identified in [Note 02](../../notes/round-2/02_RESTARTED_STRIP_COMPARISON_CODEX_20261017.md).
Running these programs alone does not validate those analytic premises.

The [validation record](ROUND_TWO_VALIDATION_CODEX_20261017.json) contains
source and output hashes and the replay environment. Replays reproduced
the records byte-for-byte in that environment; a matching hash is identity
evidence, not a proof or a portability guarantee. The
[review](../../reviews/02_UNIFORM_FLOOR_AND_RESTARTED_COMPARISON_REVIEW_CODEX_20261017.md)
records the internal same-model scope. No large derived archive is needed.
