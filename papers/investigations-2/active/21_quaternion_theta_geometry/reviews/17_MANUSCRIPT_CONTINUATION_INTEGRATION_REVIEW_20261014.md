# Review of the manuscript continuation integrating Notes 19–22

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Independent reviewing agent: **gpt-6-astra (Codex)**, reasoning effort
**ultra**, inherited from the verified parent session. This is internal
mathematical, source, and rendering review, not external peer review or
formal proof verification.

**Assessment: approved within the stated research scope.** Notes 19–22
are integrated into the standalone manuscript with their proofs,
qualifications, finite certificate scope, and remaining obligations intact.
The 39-page PDF and source pass the mathematical, reference, arithmetic,
and visual checks recorded below. No outstanding correction was identified.

## Scope and separation of claims

The update integrates
[Note 19](../notes/19_OSCILLATORY_BLOCKS_AND_PAIRED_LAGUERRE_FORMS_20261014.md),
[Note 20](../notes/20_EXPLICIT_OUTER_HEIGHT_BOUND_20261014.md),
[Note 21](../notes/21_ONE_SIDED_STATIONARY_ESTIMATES_AND_THETA_PILOT_20261014.md),
and
[Note 22](../notes/22_PROPER_SOURCE_FILTERS_AND_THETA_CORRELATIONS_20261014.md)
into the existing stable manuscript. The associated detailed mathematical
reviews remain
[Review 14](14_OSCILLATORY_BLOCKS_AND_EXPLICIT_HEIGHT_REVIEW_20261014.md),
[Review 15](15_ONE_SIDED_STATIONARY_ESTIMATES_REVIEW_20261014.md), and
[Review 16](16_SOURCE_FILTERS_AND_THETA_CORRELATIONS_REVIEW_20261014.md).
The current review focuses on preservation of those results in the
standalone paper.

The asymptotic threshold-three theorem and explicit threshold-five theorem
must remain distinct. The former is uniform in \(0<t\le1/2\) above
\(t\log(x/(4\pi))\ge3+\varepsilon\), with an unevaluated
\(\varepsilon\)-dependent height. The latter gives
\(X_{\mathrm{exp}}=4\pi\exp(10^9)\) only for \(t\log(x/(4\pi))\ge5\).
The explicit four-jet error is \(108000000/L\), yielding the stated
normalized margins \(1/2\) and \(31/64\) when \(L\ge10^9\).
Neither result covers the intervening finite strip or the remaining
small-time region.

Exact common-source and paired identities are reformulations, not
positivity assertions for arbitrary independent phases. The signed-square
lemma remains auxiliary and requires exact residual vanishing at the
specified joint-zero constraints. The direct-product criterion avoids
that specific square obstruction but still requires a theta-specific
estimate. The finite full-residual, proper-filter, and Gaussian pilots
remain inside the existing height-104 cover and retain their prescribed
parameters and losses.

The sharp-rectangular endpoint obstruction concerns fixed parameters,
fixed positive time, and subexponential separate budgets. It does not
exclude losses locally bounded at every finite point. The finite rational
jet-closure obstruction applies to nonzero fixed compact source filters,
including on a pole-free open interval, but not to arbitrary transcendental
coefficients or moving/noncompact filters.

## Fresh arithmetic and retained numerical provenance

The reviewer freshly reran three standard-library exact checks:

| Check | Count | Result |
|---|---:|---|
| Common-carrier, paired-form, and threshold-three coefficient identities | 34 | Pass |
| Explicit-height arithmetic and half-line polynomial inequalities | 52 | Pass |
| Signed-curvature split identities and collision controls | 14 | Pass |

All 100 checks passed. Their complete records are byte-identical to the
saved receipts. These finite checks verify the specified identities and
elementary inequalities; they do not independently prove the imported
Riemann–Siegel theorem, complex analytic arguments, or theta-specific signs.

The existing full-residual pilot with eight slabs, proper-filter pilot
with 64 cases, and Gaussian pilot with 14 cases have exactly the same
hashes as the records independently replayed in Reviews 15 and 16.
No expensive numerical quadrature was repeated in this integration audit.
The full-source quadrature and analytic contour/tail lemmas remain the
trusted inputs explicitly identified in those reviews.

Fresh replay provenance is recorded in the
[integration audit receipt](../numerics/MANUSCRIPT_CONTINUATION_CHECKS_20261014.json).
Temporary replay files are audit provenance, not required manuscript
dependencies. The durable drivers and receipts remain in numerics/.

## Integration issues checked

The baseline contained stale claims that the sufficient threshold was
four, no outer cutoff had been evaluated, and oscillatory-block improvement
was still only proposed. These were identified for correction in the
abstract, introduction, theorem, collision corollary, remaining-region
discussion, reproducibility appendix, build record, and continuation note.
The separate claim that absolute first-channel dominance fails below four
must be retained as a method obstruction, not changed into a threshold-three
positivity claim.

The integration also needs to retain the two exact pointwise-integrand
counterexamples, complete staircase entries, and all-coordinate pair-tail
payments. Real-multiplier pairing must not be applied unchanged to the
complex Gaussian mask \(e^{-\delta(u+ia)^2}\). Centering parameters remain
frozen, \(C_k\) is defined for all needed derivative orders, and stationarity
is imposed at the current physical point only.

The current task creates no new manuscript snapshot. The previous
user-requested backup remains historical provenance. Research-history
capture and its verification are handled by the integrating agent and are
not independently asserted by this mathematical subagent.

## Mathematical fragment review

The replacement outer proof preserves the complete low/high index split,
including the maximal third-derivative estimate on shortened blocks,
the split at \(Y=e^{L_u/3}\), the growing-time summability factor,
both high-block exponent bounds, all three imported error payments,
and the holomorphic comparison before Cauchy differentiation. The
reference to Robert's third-derivative test is a primary source, with
its specialization written explicitly in the manuscript. Omitting the
alternative Weyl-differencing derivation does not remove a necessary
step. No substantive regression from Note 19 was found.

The explicit-height appendix preserves the exponent \(17/16\), the
moment bound 8720 rounded to 9000, discrepancy \(31000/L\), positive
weight budget 85, imported-error budget \(2/L\), amplitude comparisons,
and normalized Cauchy and carrier budgets \(107520000/L\) and \(100/L\).
The elementary reductions supporting those constants remain present.
The notation \(X_{\mathrm{exp}}\) avoids conflating this cutoff with the
main theorem's \(\varepsilon=1\) specialization. A minor missing-backslash
spacing defect was reported for correction.

The paired-source fragment preserves the exact entry phases, excluding
the \(n=1\) boundary from the interior distributional sum and retaining it
at the lower endpoint. The coefficient \(1/4\), the Hermitian sum of
frequencies, and the bilinear difference of frequencies are correct.
Its direct omitted-pair payment uses absolute masses before the exterior
factor \(e^{-2ax}\), counts both mixed products and the omitted–omitted
product, and does not require a separate \(T_{j+1}\) payment. The complete
source majorants justify every interchange and all polynomial moments.
Minor differential-spacing and exponent-punctuation defects were reported
for correction before compilation.

The signed-estimate and source-filter fragment preserves the full-residual
comparison, all 64 proper-filter classifications, all 14 Gaussian
classifications, their branch-existence proofs, and their complete
payments. The fixed-time sharp-endpoint stationary sequences and the
rational finite-jet closure argument retain their correct hypotheses
and limitations. Both Gaussian masks and their distinct transport and
remainder formulas remain separate, with current-time stationarity only.
The sole mathematical wording correction was to qualify the exactly
vacuous split by \(\kappa=\mu\): for smaller \(\kappa\), its slack asks
for an additional positive \(h_j^2\) payment. That qualifier was restored
before final integration. No further mathematical correction was found.

## Final standalone source and PDF

The reviewer reread the integrated
[source](../manuscript/quaternion_theta_geometry.tex), including the
abstract, introduction, main theorem, asymptotic collision consequence,
paired formulas, both new signed-estimate sections, explicit-height
appendix, reproduction instructions, and acknowledgment. All reported
qualifications and typesetting corrections are incorporated. The original
collision reduction, hypercomplex constructions, complete-source error
bounds, and height-104 certificate remain part of the argument.

The assembled source has 183 unique labels, with no duplicates or
undefined references. All seven bibliography entries are matched to
defined citation keys. The output PDF contains no unresolved reference
markers. The final stabilized pdfTeX log has zero LaTeX/package warnings,
zero overfull or underfull boxes, and no undefined or multiply defined
references. The integrating agent also reports successful compilation of
the saved source by the desktop LaTeX compiler; the reviewer directly
inspected the separate stabilized export and its log.

All 39 rendered pages were inspected in five contact sheets. The reviewer
additionally inspected full-page renderings of pages 19, 20, 24, 25, 27,
28, 31, 32, 34, 35, and 36. These cover the paired integrals and tail
payment, signed slack and collision controls, stationary-branch and
proper-filter tables, complete-source Gaussian transport, cross-time
target, and explicit-height constant calculations. Equations, superscripts,
tables, margins, page numbers, and cross-reference placement are readable.
No clipping, overlapping text, missing glyphs, or unresolved visual
defect was found.

The final
[PDF](../../../../../output/pdf/quaternion_theta_geometry.pdf) has 39 pages,
592501 bytes, letter-size pages, the stated manuscript title, and author
metadata “Drafted for Edward Baker.” The source is 122202 bytes. Both
remain below the repository's 1 MiB convention.

| Artifact | SHA-256 |
|---|---|
| Final standalone source | d3b4d4cd4f9001f2a9e2d3e8a996a4493f752ee9dde6e43027ebb7f8f604eb58 |
| Final PDF export | 4bfc5659e891d630054a0e446cd970a70e601ad3930778cbad0052bcd83120e5 |
| Fresh paired/staircase/block check receipt | 2aa2de716eaaa52e69fe692223c3f694fc401c25eccb57e0cc311816a5cc65c1 |
| Fresh explicit-constant check receipt | 2c54c5a9ff154bbdf46fc4cc60af75ae8725e191964b69af753b5fa1bfeaa324 |
| Fresh signed-split check receipt | a42e289318bd75ff0d63c545603c655bbcd3807d73fb08fea33905f236115c44 |

The source/PDF hashes identify the reviewed build, not a mathematical
verification mechanism. The source-filter numerical records were
hash-compared to their previous independent replays; the analytic
arguments were checked directly rather than inferred from those hashes.

## Continuation and limits

The reviewer also read
[Note 23](../notes/23_MANUSCRIPT_INTEGRATION_AND_CROSS_TIME_CONTINUATION_20261014.md).
Its mathematical handoff preserves the distinction between the two outer
theorems, the already covered finite stationary branches, the two
Gaussian masks, and the still unproved cross-time estimate. A delay
proportional to time is explicitly a candidate, not a result inferred
from the fixed-delay pilot. Earlier-time stationarity and derivative
terms of adaptive parameters are not silently assumed away.

No new height coverage, new global loss theorem, or RH conclusion follows
from this integration. The explicit bound is enormous, and the finite
transition strip and moving small-time region remain open. The results
are ready for external mathematical scrutiny; this internal LLM review
does not substitute for specialist refereeing or formal verification.
Chat-history closeout is documented separately by the integrating agent.
