# RGD-E04 r2 — two-case certificate assessment

4 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual reviewer **gpt-6.1-sol (Codex), effort
ultra**, chat0003, thread `01a1a77f-2607-7832-9902-29399c58b442`, turn
`01a1a796-7a2f-7e51-9662-d86023ba41b5`.

**Disposition: accepted without correction within this internal assessment;
RGD-E04 r2 is complete.** Under the fixed [Packet05][packet] contract,
[Note03][note] and the identified [certificate][record] establish
\[
Q_{3,1}\ge L_{1,2}>7\cdot10^{-23},\qquad
Q_{3,4}\ge L_{4,2}>10^{-74}.
\]
The source is the complete canonical time-zero source; the bounds apply
only at the two stated indices. No larger positivity range, index/order
extension, Mellin/Gaussian comparison or RH conclusion is accepted.

**Review relationship:** the coordinating reviewer also authored E02.
This is a distinct assessment task by the **same assistant and same model**,
with a fresh read-only same-model contributor checking obligations 2–5
and saved arithmetic. It does not become reviewer-independent because
it is labeled r2. Source, inherited lower-order and library premises are
shared; no independent specialist review or formal proof of FLINT is
claimed. Self-assessment02 remains the original author-check record.

## 1. Versions and scope

All five return hashes locked in Packet05 match current files; its own
SHA-256 is `669d5d500866237e02d274998d6bc29c715d878fa27080c6e74439e75b78360a`.
All six E02 acquisition input hashes also match. Working-tree versions
are intentional; no clean commit or new acquisition snapshot is implied.

| Input | SHA-256 |
| --- | --- |
| E02 code | `b4863a6840cd4d68b10fe993f3f4cdc5e66dd8b3d44903445b306a50c8879db4` |
| E02 certificate, 65,610 bytes | `6db6276d65ea11706286cffa0aef899d1097f8e4bac76cbdd70f0ef40d692298` |
| Packet04, E02 r1 request | `18bf3cfd702a38123bdf22b79f6a0e568b262fac1a4881330443afc95fbf3dd1` |
| Note03, E02 return | `ebc693e1e77ee860fe3f517b5160bdd50876d8668772169f6b0c6e427d5c86c9` |
| Self-assessment02 | `e89e41a30e95f21b9ac001fc4430bbb3aab8d133751d5000aef0c405088a70f7` |

Read with the [result index][results], especially [theta identities][theta]
and [collision controls][controls], and [avoid index][avoid], especially
[shared-premise review][a05], [joint estimates][a12],
[precision evidence][a04], [scope][a07] and [bounded numerics][a10].
The accepted Note01 analytical assessment is reused; no new theta data,
integration replay or extra determinant index was acquired.

## 2. Eight assessment checks

1. **Identity and source — accepted.** The exact common b=1/16, negative
   indices, first-mode compact reference, complete unit-square source
   and k=1,4 cases are unchanged. Q3,k=D4,k*D2,k is an identity; the
   acquired positive lower allowance is the additional quantitative
   input. No reference PF property or individual-mode reflection is used.
2. **Compact acquisition — accepted.** The callback is exactly
   z^(2j)*exp(z-pi*exp(4z))/(8*(2j)!), j=0,...,7. It is entire for each
   real parameter in the enclosing pi ball. The real path and real
   integrand justify real projection; imaginary containment of zero is
   a consistency check. All eight moments have five exact rational
   segments covering [0,2]. All 40 segment balls are finite, their
   imaginary boxes contain zero, and their real sums lie in the saved X.
3. **Integration contract — accepted.** The recorded execution uses
   python-flint 0.9.0 / FLINT 3.6.0, 384 bits, one thread and the frozen
   per-call limits. [The python-flint API][acb] confirms the analytic
   callback requirements and tolerance-goal semantics. Selected
   [FLINT v3.6.0 integration source][flintsource] checks the actual-version
   control flow: direct enclosures, bounded Gauss–Legendre attempts and
   addition of remaining enclosures when stopping. This resolves the
   prior documentation-version caveat without claiming a full library
   audit. The entire-function argument meets the analytic requirement;
   final interval endpoints, not tolerance requests, accept the result.
4. **Source and spatial error — accepted.** E and B match accepted
   Note01 (6), (18), including all factors and factorials. Saved
   denominator constants have positive lower endpoints. Every B is
   strictly positive. Additional direct Fraction checks confirm all
   eight saved E+B boxes contain the full sum of the saved E/B boxes.
   An unchanged midpoint therefore does not discard the spatial payment.
   No finite-domain Green transfer or artificial endpoint is used.
5. **Joint propagation — accepted.** Exact binomial translation preserves
   the same polynomial hashes as E03, all degrees through six and the
   complete k=1 boundary cancellation; k=4 has no b. Each t_alpha is
   evaluated on X before abs_upper. Positive upper tail endpoints then
   give R_exact<=U, and lower(q_lower-U) is a valid lower allowance for
   exact L. Every occurrence of compact moments uses X, so acquisition
   uncertainty is propagated throughout. Dependency loss is conservative.
6. **Serialization and arithmetic — accepted.** The exact dyadic pairs,
   not short decimal displays, determine signs. [Arb's endpoint and
   man_exp contracts][arb] support this interpretation. One unchanged
   standard-library --verify run passed in **0.741262375 seconds** with
   both witnesses verified. Direct Fraction endpoint checks additionally
   show that both saved dyadic lower allowances and both independently
   propagated rational lower bounds exceed 7e-23 and 1e-74 respectively.
   The verifier's upward 2^-384 tail grid pays the nonzero B. It verifies
   arithmetic from saved balls; it does not reacquire integrals or prove
   transcendental/library correctness. Its polynomial helpers remain
   shared with the producer, so not all algebraic premises are independent.
7. **Consumer — accepted.** Q>=L>lambda is established at k=1,4.
   The inherited accepted D2,k>0 then gives D4,k>lambda_k/D2,k>0.
   No D4 sign was used in obtaining L. No numerical D2, D3 or eta bound
   was acquired, and the known PF44 pilot baseline is preserved.
8. **Scope and disposition — accepted.** The one E02 pass contains all
   40 integrations, 4,546 callbacks, maximum 239 per call, and reported
   total computation 0.713642541 seconds. No 512-bit refinement, failed
   case, cap or post-start correction occurred. The present assessment
   adds record verification only. k=2,3, k>=5 and higher orders remain
   untreated. No new source, comparator, payment or acquisition is needed
   for the accepted two-case claim.

## 3. Controls, limitations and continuation

The claim-specific premise screen from E04 r1 still applies. Weighted-
square controls alter unit coefficients and require new endpoint/tail
payments. Euler-factor controls alter the literal source series.
Reflected and smooth positive-primitive controls lack the complete
canonical unit-square expansion. No uncalculated failure of their finite
L test is asserted, and positive-time collisions do not contradict a
time-zero finite-order bound. The generic polynomial error theorem would
also apply to any source meeting the same quantitative input box.

**Corrections required:** none. **Unresolved premises for this fixed
claim:** none identified beyond the explicitly trusted accepted analytical
inputs and identified rigorous arithmetic library. The library and prior
lower-order proof are not formally re-proved here.

This is an accepted quantitative method pilot, not an induction premise
for all indices or orders. The next conceptual question is whether the
same complete payment can be compared with a justified margin when
r and k change. The [Astra preparation brief][next] gives the requested
parallel option within existing B03. **Next: [B] RGD-B03 preparation — Astra**,
limited to eligibility/order-dependence analysis. Full B03 extension stays
gated until that missing information is supplied. No Astra work was
launched and no B02 repair is presently called for.

The sole register and local navigation are updated. No manuscript
milestone, investigation closure or parent/sibling/global-summary change
is part of this assessment. Qualifying source material now exists for
future coordinated result-summary maintenance, with these evidence limits.

[packet]: ../research-progress/handoffs/05_RGD_E04_R2_AND_MODEL_CHANGE_AFTER_E02_20261104.md
[note]: ../notes/03_RGD_E02_R1_RIGOROUS_TWO_CASE_BOUND_RETURN_20261104.md
[record]: ../numerics/RGD_E02_R1_TWO_CASE_CERTIFICATE_20261104.json
[next]: ../research-progress/handoffs/06_RGD_CONTINUATION_AND_ASTRA_B03_PREPARATION_20261104.md
[acb]: https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.integral
[arb]: https://python-flint.readthedocs.io/en/latest/arb.html
[flintsource]: https://raw.githubusercontent.com/flintlib/flint/v3.6.0/src/acb_calc/integrate.c
[results]: ../../../../../../../result-summaries/README.md
[theta]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a05]: ../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a04]: ../../../../../../../avoid/04_counts_and_precision_as_evidence.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../../../../avoid/10_numerics_ahead_of_the_question.md
