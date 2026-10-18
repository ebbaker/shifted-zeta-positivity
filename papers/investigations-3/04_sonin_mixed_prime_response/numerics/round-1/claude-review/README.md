# Round-one review checks (Claude)

17 October 2026. Prepared for Edward Baker with LLM assistance. Model:
Claude Opus 5.5 (configured identifier `claude-opus-5-5`), Claude Cowork,
reasoning effort max; the serving model may differ from the configured
identifier.

These are the support computations for the
[round-one cross-model review](../../../reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md).
The round itself has no programs; nothing here alters its records.

| File | Content |
| --- | --- |
| [`review_checks_claude_20261017.py`](review_checks_claude_20261017.py) | Independent checks, standard library only |
| [`REVIEW_CHECKS_CLAUDE_20261017.json`](REVIEW_CHECKS_CLAUDE_20261017.json) | Its record: script hash, environment, digests of the reviewed and inherited files, and all outputs |

The program has seven sections:

- **A.** SHA-256 digests of Notes 01–02, the round README, the manuscript and its README, the project README, draft history and proposal, and of the seven inherited sources the review relies on.
- **B.** Exact rational finite models (commuting rotations, a commuting source operator, a generic rational projection): the four corner traces of Note 01 (8) against directly computed projections; the mixed formula (10), the resolvent step (11), the defects (12) and the return (13); normalized transport and the signed Gram decomposition of Note 02 (4)–(7) with its coefficient (5); the one-prime law (A3) of the place-addition note; the 3×3 coefficient matrix; a commuting-projection model in which every increment vanishes and the metric correction is exactly minus the signed Gram term; the second-order coefficient \(\mu_2\) of the mixed response; the generic a priori bound; negative controls that must fail.
- **C.** The two-dimensional control of Note 01 §6: formula (23) exactly, with the third-order bound; the actual weights at \(t=\pi/\log2\); second order for a balanced and a tilted projection.
- **D.** Note 02 (21) / manuscript Proposition 7.1 on exact symmetric involutions: the resolvent identity exactly, the norm bound in floating point, including an instance where it is attained.
- **E.** Note 02 (17)–(18) / manuscript (3.4) in exact Gaussian-rational polynomial arithmetic, by three routes (boundary trace, kernel integral, source operator), with orientation and factor-two negative controls.
- **F.** Floating gamma-sector asymptotics on box-spline bumps: the diagonal \(\Gamma[F_\tau]\); the signed Gram gamma term of Note 02 (12) for \(p=2,q=3,L=6/5\); the gamma part of the one-prime source transport \(B_S[J_2F]-B_S[F]\); an inaccessible-shift illustration.
- **G.** Constants: the first-pair coefficients; the inherited gap bounds and the error amplification of the enclosure contract at the four corners; a priori bounds; condition growth along \(S_L=\{p\le e^L\}\).

Status: sections B, C and E and the identities of D are exact rational
arithmetic; the operator norms in D and sections F–G are floating
diagnostics. The finite models check the operator algebra of the round's
identities, which holds for any commuting unitaries, positive source
operator and projection; they contain no actual Sonin projection. The
program exits with status 1 if an exact check fails or a negative control
fails to fail.

To reproduce from this folder (about 13 seconds on one core):

```sh
python3 -I review_checks_claude_20261017.py --output /tmp/REVIEW_CHECKS.json
```

The repository root is found from the script's location; `--repo-root`
overrides it, `--sections` with a subset of `ABCDEFG` runs part of the
program, and `--quick` shortens section F. The record was produced in the
cloud workspace with Python 3.13.16 and replayed on Edward's machine with
Python 3.10.12: identical in every exact field, with floating fields
agreeing to within \(9\cdot10^{-13}\) absolute. The record's runtime field
changes on a replay. All files are small, under
[LARGE_FILES.md](../../../../../../LARGE_FILES.md).
