# Internal review of preliminary work across all ten programs

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not inferred. Coordinating review plus
cross-checks by parallel same-model agents; not independent specialist
refereeing. No new global exponent is claimed.

## Scope and outcome

Read the [overview](../notes/PROJECT_OVERVIEW_20261004.md), all ten charters,
the ten new preliminary investigations linked from the
[assessment](../notes/PROGRAM_PREFLIGHT_ASSESSMENT_20261004.md), and selected
parent definitions supporting the new deductions. The review concerns
these new interfaces and calculations; it does not freshly reprove every
inherited Sonin or fixed-probe theorem.

The shortlist 01/02/03 remains appropriate as a judgment of readiness.
Program 01's centered Vaughan block covariance is a precise next target.
The work separates new algebraic deductions, inherited estimates,
conditional targets, finite diagnostics and global assertions throughout.
No missing power-saving estimate is reported as established.

## Mathematical checks

| Program | Checks and result |
| --- | --- |
| 01 | Physical kernel scaling, terminal cofactor caps, full Vaughan coefficients, rank-one subtraction, scalar mismatch, cross-coordinate O(X)/O(X^−1/2) budgets and exact prime-place relation checked. Fixed-prime removal deletes only the corresponding prime powers in the complete response. Separate agent reviewed both note and implementation without findings. |
| 02 | Actual prepared projection and inverse metric retained; prime diagonal contraction constants, signed cross sum and bounded archimedean norm comparison checked. Galerkin residual is orthogonal to the solved head in the required sense, giving the exact two-term identity. No support-locality claim is transferred through the inverse metric. |
| 03 | Good-shift/exception exponents, simultaneous partial-sum qualification, lower-tail cost and shrinking upper-endpoint support cost checked. The positive-part target is distinguished from the stronger absolute sufficient bound. |
| 04 | Sixth-order exponent allowance eta<=1−kappa/12, two lower-order allowances, full covariance normalization and coarse coordinates checked. The positive PNT slow-mode model has a common rank-one response that reconstruction preserves. Mellin sign corrected to G(1/2−s). |
| 05 | Finite convolution binomial identity and strict cutoff Y=(2BX)^(1/3) checked, including nonzero remainders outside the guaranteed band. The 3 c_w M_1(Y)x continuum and O(X^−5/2 log X) discarded norm follow from the inherited lattice lemma. Other sectors are retained in full. |
| 06 | Step-function physical norm, tail budgets, prepared Mellin transform, Hardy norm constants for every b>0, raw Möbius head obstruction and taper sign independently checked. Stronger finite membership is not convergence. |
| 07 | Theta normalization, signed cosine diagonal, boundary derivative, even centered Hadamard grouping and quartic difference checked. The exterior y>=sqrt(b(1−b)) comparison is unconditional; the remaining thin band is still unbounded in real frequency. Positive-density counterexample excludes only the listed generic scalar mechanism. |
| 08 | Elementary/gamma/prime normalization, exact continuum cancellation, endpoint psi−t+1, gamma tail and finite-index prime tail independently checked. The high-zero index scale is not presented as a theorem about the first negative coefficient. |
| 09 | Primary theorem normalization and exponent table checked: formal applicability differs from a useful estimate. Current N/T scales give a bound weaker than counting. The singleton and Type II detector gates are both retained. |
| 10 | Complete arithmetic assembly, strict real cutoffs, signed covariance summaries and continuum split checked. Floating identities/refinement are explicitly distinguished from outward certification. |

Two precision corrections were made during review: the prepared projection
is onto the orthogonal complement of the three moment representers, and
the model Mellin transform uses the manuscript's plus-exponent convention
G(1/2−s). Neither changes the proposed ranking or exponent budgets.

## Reproduced calculations

The coordinating agent ran the following scripts in addition to the
authors' checks:

- [Heath–Brown identity check](../numerics/05_higher_multilinear_identities/check_heath_brown_identity.py):
  8,888 exact integer prime-log coefficient comparisons passed across five
  cutoff cases, including deliberately nonzero remainders.
- [Prepared-step check](../numerics/06_arithmetic_approximation/check_prepared_steps.py):
  2,108 exact rational checks passed; finite raw/tapered norm diagnostics
  reproduced the note's displayed values.
- [Li decomposition check](../numerics/08_generalized_li_positivity/check_li_decomposition.py):
  192 exact rational checks passed; ordinary floating finite-tail budgets
  reproduced the displayed values for n=1,...,4 at tau=1.99.
- [Block-Gram preflight](../numerics/10_finite_certificates_support/block_gram_preflight.py):
  four runs at two noninteger shells and 128/256 quadrature nodes passed.
  Maximum coefficient residual 7.11e-15; maximum energy-split residual/X²
  2.29e-14; maximum listed normalized-energy refinement change 4.80e-7.
  A separate agent also ran X=123.375 at 64/128 nodes; coefficient and
  split diagnostics passed there as well.

The exact checks validate finite algebraic instances; the proofs in the
notes establish the displayed identities. Floating evaluations do not
certify their analytic tail endpoints or unsampled scales. No asymptotic
fit, outward interval certificate, or new finite zero verification was run.

## Source and artifact scope

Primary-source readings are linked in the relevant notes: Heath–Brown's
finite identity, Matomäki–Radziwiłł–Tao's logarithmic pair input,
Delaunay–Fricain–Mosaki–Robert's criterion, Lagarias's shifted dominance,
Romik's theta normalization, Freitas's generalized Li normalization,
DLMF's gamma product and Guth–Maynard's theorem/ranges. These readings
are targeted audits, not an exhaustive search for all subsequent results.

The assessment and navigation link each program's actual preliminary
note. New files are small sources, notes and one diagnostic record with
source hashes; no matrices, sieve arrays, third-party PDFs or large
regenerable files are retained. Existing manuscript and compilation
records remain unchanged. First fixed global saving and exponent descent
remain open.

Final artifact checks found all ten preliminary notes, no broken local
Markdown links in the 33 changed/new files, balanced display/inline math
delimiters, matching diagnostic source hashes, and no file over 1 MiB.
`git diff --check` passed. Changes remain in the working tree; no commit
or publication is part of this preliminary investigation.
