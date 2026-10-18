# Round-one review checks (Claude)

17 October 2026. Prepared for Edward Baker with LLM assistance. Model:
Claude Opus 5.5 (configured identifier `claude-opus-5-5`), Claude Cowork,
reasoning effort max; the serving model may differ from the configured
identifier.

These are the support computations for the
[round-one cross-model review](../../../reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md).
They are not part of the round's replay contract and do not alter its
records.

| File | Content |
| --- | --- |
| [`review_checks_claude_20261017.py`](review_checks_claude_20261017.py) | Independent checks; mpmath, with python-flint only for the optional Acb signs of section H; imports nothing from the round's programs |
| [`REVIEW_CHECKS_CLAUDE_20261017.json`](REVIEW_CHECKS_CLAUDE_20261017.json) | Its record: script hash, environment, digests of the committed round artifacts, and all outputs |

The program has nine sections:

- **A.** SHA-256 digests of the round's notes, manuscript, programs and records, with the recorded hashes checked.
- **B.** \(H_0\) by the Riemann–Siegel \(Z\) route at the bracket endpoints and on 61 points of the tripled interval.
- **C.** Theta moments by quadrature, against the inherited enclosure.
- **D.** The two source finite differences and the Taylor coefficients of \(-\log\Phi(\sqrt x)\).
- **E.** The coupled two-quartic seed and the \(X+Y/4\) convolution.
- **F.** Exact checks: the Chebyshev polynomial and its discriminant, the binomial envelope, the Bessel identity and the pair example.
- **G.** The theta growth constant, and exact crossover fields for one quartic site.
- **H.** The Bessel seed as a stable control: its zeros, Acb signs at \(r_B\pm10^{-6}\) and on \(3(r_B\pm10^{-6})\), its field growth and its kurtosis.
- **I.** The sub-Gaussian bound on the coupled seed.

Status: floating diagnostics at 20–60 digits, except section F, which is
exact rational arithmetic, and the Acb enclosures in section H, which are
interval arithmetic at 160 bits. Agreement with the round's certificates
is evidence about implementation, not an independent certificate; the
review says which statements depend on which check.

To reproduce from this folder (about 3.5 minutes on one core):

```sh
python3 -I review_checks_claude_20261017.py --output /tmp/REVIEW_CHECKS.json --committed-dir ../../..
```

`--sections` with a subset of `ABCDEFGHI` runs part of the program. The
record was produced in the cloud workspace with Python 3.13.16, mpmath
1.3.0 and python-flint 0.9.0 (FLINT 3.6.0). Sections A–F were also run on
Edward's machine with Python 3.10.12 and mpmath 1.3.0 and gave identical
output. The record's runtime field changes on a replay; its
numerical content does not. All files are small, under
[LARGE_FILES.md](../../../../../../LARGE_FILES.md).
