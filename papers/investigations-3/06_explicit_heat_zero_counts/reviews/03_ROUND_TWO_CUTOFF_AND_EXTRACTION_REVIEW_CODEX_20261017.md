# Same-model review of the lower cutoff and paired extraction

17 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model: **gpt-6.1-sol (Codex)**, reasoning effort
**ultra**, as verified by the parent session. This is an internal same-model
development review, not cross-model or specialist human review.

**Disposition: the new note is proved in-note from named imports, with
same-model checks only.** No substantive defect was found in its stated
count, changed cutoff or extraction. Cross-model analytic review of this
new proof remains the next gate; Claude Review 02 covers the earlier
Notes 01–02 and original manuscript, not this extension.

## Scope and identities

I read all §§1–7 of
[the round-two note](../notes/round-2/01_LOWER_CUTOFF_AND_PAIRED_EXTRACTION_CODEX_20261017.md),
its complete [checker](../numerics/round-2/check_lower_cutoff_and_paired_extraction.py),
and the supporting baseline notes, manuscript, records and Claude Review 02.
This review checks the reuse of those named analytic imports; it does not
independently verify Arias de Reyna or Boyd at their original sources.

Reviewed SHA-256 identities:

| Artifact | SHA-256 |
| --- | --- |
| Round-two note | `e965f6cfa6233c8a46aca27309fb40c35d3f199d5d70dadd713528d74c53fe6b` |
| Round-two checker | `faaaaab7066b1a26e79f836eaee18efa64ca2d1ce6affc79baa5d9eda67f2397` |

The parent agent authored and integrated the continuation. Two other
same-model subagents separately checked the lower-cutoff/remainder
obligations and the Schwarz–Pick/conjugate-pair extraction. I checked the
review response, scope and controls, and independently re-derived the new
extraction inequalities and audited the revised allowances. Shared model,
source premises and development context limit the independence of these
checks.

## Mathematical and execution findings

- The changed endpoint has `T>=50000` and `a>89`. The note correctly retains
  `97.374/(a-.865)` instead of extending the old `98/a` shortcut below its
  valid range. Gaussian reserves, fixed-index remainder, tail bounds and
  the full rational bracket close below 2. The resulting comparison budget
  is `5094127/7350000<347/500<7/10` on the entire declared band.
- The disk argument uses `0<q<1`, so its normalization by `q` is valid.
  Schwarz–Pick and the minimum modulus give the stated optimized quotient;
  its rational quadratic completion proves the `5/3` allowance. The
  `49/30` witness is correctly called an exact disk-automorphism test,
  without claiming it attains the sharp full quotient.
- The real-entire premise explicitly supplies conjugate zeros with equal
  multiplicity. Convexity of the Poisson kernel in vertical distance gives
  the `7/25` paired floor, including real and multiple zeros. Pairing
  preserves a window defined only by real parts, including the declared
  half-open boundary convention.
- Combining those bounds gives `2003/2240*log(X+2)+125/21` for
  `X>=100000`, hence `9/10*log(X+2)+6`. The original smaller comparison
  budget also gives the stated `75/14` additive corollary on `X>=2000000`.

I actually replayed the current checker with Python standard-library
rational arithmetic. The normal run exited **0** with no failed checks.
The three prescribed injections exited **1**: comparison ceiling `69/100`
failed its budget check; kernel floor `3/10` failed the real endpoint and
multiplicity checks; derivative allowance `3/2` failed both the proved
allowance check and the exact disk-automorphism witness. These executions
check finite arithmetic and explicit class witnesses, not the imported
analytic theorems or a sample of the zeros of `H_t`.

## Scope, review handling and remaining gate

The user's continuation request authorizes this bounded extension despite
Claude's recommendation to freeze. The note states a finite target and
stops at its proof/replay package. It preserves the missing consumer
kernel, domain and tolerance; the result implies no application saving,
lower population, exact interior count, collision exclusion, RH conclusion
or improved Newman bound. The controls discussion names the exact theta
expansion as the additional input and does not claim untested controls
fail the quantitative comparison. The generic extraction remains valid
for any controls satisfying its actual analytic premises. This handling is
consistent with [summary 12](../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid 02](../../../../avoid/02_shape_only_arguments_and_the_controls.md).
The result and scope should be routed through the
[result summaries](../../../../result-summaries/README.md) and
[patterns to avoid](../../../../avoid/README.md), particularly avoid 08, 10
and 20, without upgrading the new proof's review status.

The original manuscript source and PDF remain byte-identical to Claude's
reviewed pair: source SHA-256
`24ad21c235eec1175bb9e515969d027200af689509723100add595c6c2500efb`, PDF
`1980bcbc29780bdfbf156241ec1c8bf60f006ea3aeabe081280e86ff8086c762`.
The addendum states the factor-two Stirling slip, omitted fixed-index
remainder and indirect-source qualifications. Its displayed numerical
comparison explicitly uses rounded theorem allowances, not measured zero
counts. The time-zero Bellotti–Wong benchmark has not been reverified here,
and its addition and the other manuscript editorial integrations remain
**pending**. No claim that all four manuscript corrections are completed
is warranted. The old equality-test label change is arithmetic bookkeeping
and does not amend the historical review digest table.

Accept this scoped same-model development result. Obtain cross-model
analytic review before calling the new proof cross-model reviewed; require
a stated consumer budget before further optimization or application work.

A final provenance check found that baseline Note 01 already had a single
hyperlink repaired in commit `452eee4`, after its reviewed commit
`146b3f9`. Its current SHA-256 is
`adf681d34da5ff9f9e2f1c2613b65dca887ada0d5817f29fc0db159cdcacd539`;
reversing exactly that link replacement recovers the reviewed hash
`46266338f670fde0514ec51029ba85bc34b25a5075c149107abb146fa45e9196`.
The new execution record checks this relation. The review/build record's
older hash is historical provenance, not the current Note 01 byte hash.
No mathematical statement was changed by that pre-existing link repair.
The note and checker hashes above include this final provenance annotation.
