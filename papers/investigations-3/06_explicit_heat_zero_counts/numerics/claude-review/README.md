# Review checks for Notes 01–02 and the manuscript (Claude)

17 October 2026. Prepared for Edward Baker with LLM assistance. Model:
Claude Opus 5.5 (configured identifier `claude-opus-5-5`), Claude Cowork,
reasoning effort max; the serving model may differ from the configured
identifier.

Support computations for the
[cross-model review](../../reviews/02_CROSS_MODEL_REVIEW_NOTES_01_02_AND_MANUSCRIPT_CLAUDE_20261017.md).
They are not part of the project's arithmetic records and do not change
them. The program imports nothing from the project's checkers.

| File | Content |
| --- | --- |
| [`review_checks_claude_20261017.py`](review_checks_claude_20261017.py) | Independent checks, mpmath only |
| [`REVIEW_CHECKS_CLAUDE_20261017.json`](REVIEW_CHECKS_CLAUDE_20261017.json) | Its record: script hash, environment and all outputs |

Sections:

- **A.** \(H_t/M_t(s_+)\) from the heat-kernel convolution of \(\xi\)
  (Polymath (35)) at 26 points with \(x\ge2\cdot10^6\) and \(3\le y\le4\),
  including a stress point where the dominant Dirichlet polynomial nearly
  aligns. Each is compared with the theorem's budget and with the
  Riemann–Siegel main terms.
- **B.** The extraction lemma's disk at the stress abscissa: the maximum
  on the circle, a Cauchy estimate of \(F'/F\), the Poisson sum
  \(D_t(U)\) and the implied count.
- **C.** Sampled margins of the carrier inequalities (4), (5), (6),
  (15), (16) and (17) of Note 02, and of Note 01's bounds at the disk
  centre, for \(x\) up to \(10^{40}\), with precision raised with height.
- **D.** The Gaussian moment formula (9) against quadrature.
- **E.** The three source observations: the inequality before
  Polymath (60), the \(t/2\) display after (99), and the fixed-index
  remainder with its bookkeeping.
- **F.** Benchmarks: mean density, the theorem's bound, and an explicit
  \(t=0\) bound.
- **G.** Planning arithmetic, not proofs: the cutoff and constants
  obtainable from the notes' own ingredients.

Status: floating diagnostics at 30–60 significant digits. The quadrature
in A and B is not outward rounded, and sampled inequalities are not
proved between the samples. Nothing here certifies the theorem. Each
section has a pass condition that can fail.
`--inject-normalization` uses the wrong heat coefficient in the carrier,
and section A must then fail with exit status 1.

Reproduce from this folder. The full run takes about 12 minutes on one
core; sections C–G take a few seconds.

```sh
python3 -I review_checks_claude_20261017.py --output /tmp/REVIEW_CHECKS.json
python3 -I review_checks_claude_20261017.py --sections CDEFG
python3 -I review_checks_claude_20261017.py --sections A --quick --inject-normalization   # exits 1
```

The record was produced in the cloud workspace with Python 3.13.16 and
mpmath 1.4.1. On Edward's machine, with Python 3.10.12 and mpmath 1.3.0,
sections C–G gave byte-identical numerical content, the quick section A
gave the same digits, and the injection exited 1.

The runtime fields of the record change on a replay, but its numerical
content does not. Small files only, under
[LARGE_FILES.md](../../../../../LARGE_FILES.md).
