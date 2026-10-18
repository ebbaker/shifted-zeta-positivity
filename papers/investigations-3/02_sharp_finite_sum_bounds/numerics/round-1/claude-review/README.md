# Round-one review checks (Claude)

17 October 2026. Prepared for Edward Baker with LLM assistance. Model:
Claude Opus 5.5 (configured identifier `claude-opus-5-5`), Claude Cowork,
reasoning effort max; the serving model may differ from the configured
identifier.

These are the support computations for the
[round-one cross-model review](../../../reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md).
Nothing here alters the round's programs or records.

| File | Content |
| --- | --- |
| [`review_checks_claude_20261017.py`](review_checks_claude_20261017.py) | Independent checks, standard library only |
| [`REVIEW_CHECKS_CLAUDE_20261017.json`](REVIEW_CHECKS_CLAUDE_20261017.json) | Its record: script hash, environment, digests of the reviewed and inherited files, and all outputs |
| [`replay_completion_suffix_relaxed_wall.py`](replay_completion_suffix_relaxed_wall.py) | The wrapper used for the completion replay of the review's §4: the round's completion call on the same hash-checked engine, box cap and depth, with only the wall budget raised; exits nonzero unless the recorded digest is reproduced |
| [`COST_PROBE_PILOT_N1974864_CLAUDE_20261017.json`](COST_PROBE_PILOT_N1974864_CLAUDE_20261017.json) | One run of the round's unchanged pilot at \(N=1974864\), wrapped with the executor's attribution (the program writes its author's model into its own record); a cost measurement for the review's §3.3, not a coverage claim |
| [`REPLAY_ON_EDWARDS_MACHINE_20261017.json`](REPLAY_ON_EDWARDS_MACHINE_20261017.json) | Field-by-field comparison of a replay of the check program on Edward's machine with the committed record |

The program has seven sections:

- **A.** SHA-256 digests of the reviewed notes, programs, records and
  manuscript source, and of the two inherited audit helpers.
- **B.** Float64 rows by a code path independent of the round's pilot
  (gcd class outer, cofactor inner, `math.fsum`): the sharp first row at
  \(t=157/1000\) against the certified pilot enclosure; the plain first row
  at \(t_0=129/800\) against the audit's certified value; the audit's
  floating values at the leg starts; and the first-row boundary in \(t\)
  (sharp floor negative at \(t=0.1569\), positive at \(0.15695\)).
- **C.** The transfer engine's gate numerator (8), evaluated by the engine
  itself on point boxes at one actual integer pair per pattern and three
  values of \(y\) (1,080 points), against an 80-digit finite difference of
  the summand computed from its definition. This tests the formulas the
  engine encodes; it is not a coverage certificate.
- **D.** Fault injection in the engine, modified in memory after its hash
  is checked: with the \(n^{-\sigma}\) decay removed, actual points must be
  rejected with strictly positive numerators (negative control, D1). With
  `--slack`: the slope bound \(\sigma'\ge\tfrac12\) halved to \(\tfrac14\) on
  legs 3, 2 and 1 (interval slack probe, D2), and a float64 scan of the
  required slope \(\partial_y\log U/\log n\) over sampled actual integer
  terms (D3; a sampled supremum bounds the true one from below only).
- **E.** Exact rational checks of the properties of \(U_g\) used by the
  activation lemma of the review: subadditivity, homogeneity,
  monotonicity in \(g\), and the closed form of \((1-g)U_g(1,a)\).
- **F.** Activation-lemma planning in float64: the lemma's bookkeeping on
  two spans; greedy meshes per leg for the sharp lane at \(t=157/1000\)
  with exact activation sums, with cap-lemma bounds, and with cap-lemma
  bounds except on each leg's last span; and the inherited plain lane at
  \(t_0=129/800\). **Planning values only, not a certificate.**
- **G.** Contract arithmetic: the first natural window contains
  \(X+\sqrt{1-y_0^2}\) at the new time (60-digit `Decimal`); exact checks of
  the tail's \(y\)-box, \(y_1^2=1-2t\), the target value and the barrier
  containment.

Status: section E and the exact items of G are rational arithmetic;
section C compares interval enclosures with high-precision finite
differences; sections D1–D2 run the round's own engine; sections B, D3 and
F are floating. The program exits with status 1 if a comparison leaves its
tolerance, an exact check fails, or a negative control fails to fail.

To reproduce from this folder:

```sh
python3 -I review_checks_claude_20261017.py --slack --output /tmp/REVIEW_CHECKS.json
```

The repository root is found from the script's location; `--repo-root`
overrides it, `--sections` with a subset of `ABCDEFG` runs part of the
program, and `--legs` restricts section F. The full run with `--slack`
took 616 seconds on one core of the cloud workspace (Python 3.13.16).
In the Linux VM on Edward's machine (Python 3.10.12, aarch64) sections A,
B, C, E and G take about
a minute, section D with `--slack` about 30 seconds, and section F one to
two and a half minutes per leg; that replay, run by sections, matched the
record in all 775 compared fields, floating fields included (see the
comparison file above). The record's runtime and environment fields
change on a replay. The replays of the
round's own programs described in the review (§4) used the round's
commands, with the wall caps raised where the review says so, and the
wrapper above for the completion suffix; their outputs reproduced the
committed records and are not stored here. All files are small, under
[LARGE_FILES.md](../../../../../../LARGE_FILES.md).
