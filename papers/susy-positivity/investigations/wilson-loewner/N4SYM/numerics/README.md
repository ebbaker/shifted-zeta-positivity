# N4SYM checks and records

All five programs use the Python standard library only. Each prints one JSON object to stdout, or writes `--output FILE`. They are deterministic: repeated runs give byte-identical output on a given platform. Run them from `papers/susy-positivity/investigations/wilson-loewner/`. No zeta function is evaluated anywhere.

Every floating case is a diagnostic of an analytic statement, not an interval certificate. The SU(2) background is a classical test connection, not a sample of the quantum measure. The programs are not registered in `validation/drafts.py`, because N4SYM has no manuscript. Register them in the same pass that folds these results into one.

| Program | Record | Cases | Accompanies |
|---|---|---|---|
| [check_straight_line_response.py](check_straight_line_response.py) | [straight-line-response-20260923.json](records/straight-line-response-20260923.json) | 72 | [first note](../notes/STRAIGHT_LINE_RESPONSE_AND_TRACE_COMPLETION_20260923.md), Sections 1–3 |
| [check_trace_completion.py](check_trace_completion.py) | [trace-completion-20260923.json](records/trace-completion-20260923.json) | 77 | first note, Section 4 |
| [check_flipped_return.py](check_flipped_return.py) | [flipped-return-20260924.json](records/flipped-return-20260924.json) | 47 | [flipped-return note](../notes/FLIPPED_RETURN_TRACE_ANALYSIS_20260924.md) |
| [check_near_bps_corner.py](check_near_bps_corner.py) | [near-bps-corner-20260924.json](records/near-bps-corner-20260924.json) | 56 | [corner note](../notes/NEAR_BPS_CORNER_ROUNDING_AND_CLOSURE_20260924.md), Section 1 |
| [check_rounded_and_closure.py](check_rounded_and_closure.py) | [rounded-and-closure-20260924.json](records/rounded-and-closure-20260924.json) | 20 | corner note, Sections 2–3 |

## Case groups

**check_straight_line_response.py**

- S1: tree-level signs of the displacement and tilt correlators.
- S2: Fourier constants of the scale-covariant extensions.
- S3: the one-loop Maldacena–Wilson kernel versus the quadratic formula, including Richardson limits.
- S4: exact rational bookkeeping.
- S5: cutoff impedance positivity and its renormalized failure.
- S6: total and finite-time work, onset negativity and the tilt resistor.

**check_trace_completion.py**

- T1: exact tip series, with c₁–c₁₂ matching the parent record.
- T2: Loewner scaling.
- T3: sliver geometry.
- T4: one-loop trace–chord exchange, with the 1/s law for constant n₀ and the O(s) law when flipped.
- T5: first evolution equations by finite differences, a = 0 controls, gauge covariance and short-time behaviour.

**check_flipped_return.py** (imports `check_trace_completion.py`)

- F1: continuum one loop with vertex excision, testing exactness of the cusp coefficient and the finite part.
- F2: gradient-flow one loop in its three regimes, including the moment identities.
- F3: the second evolution equation.

**check_near_bps_corner.py**

- W0–W5: the weak-coupling generalized cusp (Clausen implementation; small-angle, BPS-slope and antiparallel checks of the transcribed two-loop formula; corner scaling; H).
- S1–S7: the planar classical string (antiparallel and small-angle normalizations; the BPS curve; the CHMS slope; the corner function F and its values; the (π − θ)^{3/2} antiparallel law).

**check_rounded_and_closure.py** (imports `check_trace_completion.py` and `check_flipped_return.py`)

- R0: stadium conventions and normalization.
- R1–R3: the rounded flipped loop, covering fillet geometry, the log(1/δ) coefficient A(s) and the finite part with h.
- C1: closure controls (the scalar-Laplacian counterexample, the transported derivative with commutator, and the flowed-propagator kernels).

Runtimes are a few seconds each. Follow the repository [large-file policy](../../../../../../LARGE_FILES.md); all records are below 20 KB.
