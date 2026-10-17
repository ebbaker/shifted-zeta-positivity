# Round-one review checks (Claude)

17 October 2026. Prepared for Edward Baker with LLM assistance. Model:
Claude Opus 5.5 (configured identifier `claude-opus-5-5`), Claude Cowork,
reasoning effort max; the serving model may differ from the configured
identifier.

Support computations for the
[round-one cross-model review](../../../reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md).
They are not part of the round's replay contract and do not alter its
records; the parent folder's `run_replay.py` hashes only the programs at
its own level, so these files do not enter its summary.

| File | Content |
| --- | --- |
| [`review_checks_claude_20261017.py`](review_checks_claude_20261017.py) | Independent checks, mpmath only; imports nothing from the round's programs |
| [`REVIEW_CHECKS_CLAUDE_20261017.json`](REVIEW_CHECKS_CLAUDE_20261017.json) | Its record: script hash, environment, committed-record digests and all outputs |

Sections: A jets at the six replay observations against the committed
balls (closed forms at \(t=0\), Gauss–Legendre at \(t=1/4\)); B the 24
conditioning combinations (whitened \(2\times2\) and KKT); C the
alignment abscissa in each zero gap, where the equality distance equals
the sufficient radius; D theta-tail feasibility at those abscissae; P the
32 prescribed-abscissa problems by rank and planar Carathéodory; E the
three-square control bracket; F the Note 05 constants by a
Leibniz–Hermite expansion, with remainder tests that can fail; G the Note
02 envelope constants in interval arithmetic; H the height above which a
\(10^{-16}\) reflection-breaking perturbation has no real zeros (interval
arithmetic) and one preregistered floating illustration.

Status: floating diagnostics at 60 digits, except G and H, which use
mpmath interval arithmetic for the displayed inequalities. Agreement with
the round's certificates is evidence about implementation, not an
independent certificate; the review says which statements it relies on.

Reproduce from this folder (about 20 minutes on one core):

```sh
python3 -I review_checks_claude_20261017.py --output /tmp/REVIEW_CHECKS.json --committed-dir ..
```

Use `--sections` with a subset of `ABCDPEFGH` for a partial run. The
record was produced with Python 3.13.16 and mpmath 1.4.1 in the cloud
workspace; sections A, B, E, G and P were also run on Edward's machine
with Python 3.10.12 and mpmath 1.3.0 and gave the same numbers. The
record's runtime fields change on a replay; its numerical content does
not. Small files only, under [LARGE_FILES.md](../../../../../../LARGE_FILES.md).
