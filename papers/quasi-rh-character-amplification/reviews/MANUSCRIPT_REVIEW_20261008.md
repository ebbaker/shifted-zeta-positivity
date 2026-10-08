# Scoped mathematical review of the mixed-moment manuscript

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred.

Reviewed the full source of [manuscript.tex](../manuscript.tex), titled *Conductor localization
of a mixed inverse–plain moment in a sextic character family*, and compared
its central arguments with the investigation's mixed-moment, primitive-row,
kernel, joint-witness, and marked-transfer records. Source comparisons use
the September 30 companion preprint, especially Sections 4 and 8, Lemmas
17.1–17.2, and Section 19. Its consulted PDF has SHA-256
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.

**Verdict:** the main conditional reduction, its elementary pair count,
and the conditional two-rebalance calculation pass this scoped review.
All four requested exposition/quantifier corrections below were applied
and verified in the revised source. They do not change the reduction or
its exponents. No unresolved mathematical correction remains within this
review's scope. This is a same-model parallel review,
not independent specialist refereeing, proof of the imported analytic inputs,
or formal verification. Compilation and page-layout checks are separate.

## Precision corrections applied and verified

1. Write the remaining open estimate as an explicitly one-sided inequality
   `Re(T_large) <= C_epsilon U^(1+delta*m-1/5000+epsilon) H^A`.
   For a signed real quantity, the notation `<<` normally denotes an
   absolute bound. The complete block is real, and the main identity already
   bounds its negative part by the smaller error; consequently a modulus
   bound for the whole summed block is equivalent at the target scale once
   the reduction is known. State that it is also sufficient, rather than
   categorically stronger in this setting. Taking absolute values separately
   for individual pairs does remain a stronger request.
2. In the transformed-coefficient discussion, say that the fixed ray factor
   `nu(v)` has first been separated before identifying the remaining arithmetic
   coefficient with `mu_F(v) h(v)`. The tuple coefficient defined earlier
   contains `nu(v)` explicitly.
3. Explicitly require nonnegative physical slot lengths `w_i`, with their
   number fixed before the row scale tends to infinity. All length ranges
   used in uniform estimates should remain fixed and bounded.
4. Describe the profile-refinement gain `31/260000` as the value before
   arbitrarily small capacity and whole-slot losses, or write
   `31/260000 - epsilon`. Its positive surplus over `1/10000` is unchanged.

The revised profile paragraph also explicitly defines the weighted mean,
the range `0 <= g* <= delta/2`, and the fixed supply margin
`L_slot > 1/5`. These additions clarify the stated application without
altering the main theorem. Native compilation is managed separately;
this review makes no claim of rendered-page inspection.

## Main theorem and dependencies

The manuscript cleanly separates three analytic hypotheses: the marked
inverse norm, the conductor-sensitive buffered plain bound, and a count
of the full fixed bin. It proves the reduction from these hypotheses
without silently assuming the desired mixed saving. The full-bin count
can be used at a prescribed inverse/plain length pair even though its
earlier proof chooses detector witnesses separately for each row. This is
noncircular. The amplitude-profile restriction is application context and
is correctly unnecessary for the algebraic theorem itself.

The characters, common orientation, actual annular profiles, original zero
extensions, and disjoint row-independent prime supports are retained.
Both strict inverse widths are stated. A fixed finite sum of presentations
is handled by Cauchy before applying the single-presentation statement;
the exact equality is not incorrectly asserted after omitting cross terms.

The primitive row conductor is distinguished from the column-pair
conductor. The inequality `Q_psi << U` is stated with its constant, so no
unjustified assertion `theta <= 1` is made. The good-prime hypothesis
includes every prime above 6, as required for an exact-order-six local
residue character. Primitive inducing characters must be nonprincipal,
which the setting requires.

At fixed separating parameters, the tuple expansion is exact. Its use for
rowwise choices is explicitly conditional on uniform estimates for the
derivative profiles arising in the prescribed Sobolev step. Heights remain
as a fixed polynomial cost; the manuscript does not silently hide unrelated
row-specific coefficient arrays inside the restricted kernel. The choice
of preliminary losses and then sufficiently slowly growing height range
is consistent with the source's finite-height method.

## Pair count, masks, and coefficients

The ratio identity is correct on both units and nonunits. At a prime with
valuation difference zero modulo six, its phase disappears but its zero
extension remains in `E`. At a nonzero residue, the local character is
nonprincipal modulo that prime and has primitive conductor equal to the
prime. Thus the moving conductor is `rad(c)` rather than `c`, and mask
primes do not become additional primitive conductor primes.

For the pair-count proof, extracting the ideal gcd gives coprime residual
ideals. Their unique sixth-power decompositions leave ten possibilities
at each prime of the ratio conductor: two sides and five nonzero exponents.
Counting the gcd by the reciprocal maximum and then by the reciprocal
geometric mean gives the product of two convergent norm sums with exponent
three. The remaining squarefree-conductor sum is bounded by the ideal
divisor bound and partial summation. This proves
`O_epsilon(X V^(1/2+epsilon))`; no annular lower bound or cancellation is
needed. When the allowed gcd norm is below one its count is zero, so the
positive majorant remains valid.

The sum of absolute weights over factorizations of a fixed column is
divisor-bounded because there are finitely many factors and the actual
annular coefficient factors are bounded. A tuple restriction such as
`k != k'` reduces this positive majorant even though the resulting
coefficient no longer factors by columns. The proof uses this distinction
correctly and does not invoke an arbitrary-coefficient version of the
marked moment.

## Removed terms and exact margins

Retaining `Q_psi` in the source's primitive functional equation yields
the conductor-sensitive reflected plain bound. On the stated hard box,
the reflected real part is at least `29/100 - 6e > 0`. The original deleted
Euler radical has norm `O(U)`, so its absolute product costs an arbitrarily
small power of `U`. The finite-height contour argument must retain its
cumulative frequency allowance and tails, which the manuscript says.

On the lower primitive-conductor rows, the pointwise saving is at least
`delta/1000`; positivity then permits application of the original marked
inverse norm over the larger physical row family. The resulting margin
below the target is exactly at least `1/6250`. No moment theorem is
applied at the unjustified smaller physical scale `U^theta`.

The complete plain-variable diagonal is nonnegative only after summing
its inverse and prime factors; the manuscript forms that expression before
dropping its coprimality mask. Its normalized plain coefficient square mass
is bounded by ideal counting. The resulting exponent is `1`, giving margin
at least `647/5000` below the target.

The remaining small-ratio-conductor block has absolute size bounded by
the full-bin count times `U^(2/5+epsilon)`. The smallest target margin is
`23/1250`. The row partition, then the plain diagonal, then the ratio
conductor partition are disjoint and exhaustive. Their common error margin
is therefore `1/6250`. Swap symmetry makes the complete retained block
real; no positivity of that block is asserted.

## Conditional application and limitations

The scalar-count paragraph distinguishes the investigation's fixed
`kappa=3/4` comparison from the source's dynamic-parameter statement.
The simple bound `t_0 - 1 < 3/20` correctly implies the count exponent
used in the main theorem. The two-rebalance factor and its partial
derivatives are correct. Its minimum is `1091200/2012413`, and multiplication
by `1/5000` gives `5456/50310325`, with the displayed positive surplus over
`1/10000`. The stated interval and outside-band slack values agree with
the retained exact arithmetic record.

The transformed-proof obstruction accurately identifies two separate
issues: inadmissible widths and the residual annular divisor coefficient
`h(tfn)`. It is presented as failure of this proof transfer, not a lower
bound on the actual moment or a proof that the desired saving is false.
The row-selector caveat correctly prevents termwise replacement of the
restricted kernel by a smooth complete-family Poisson kernel.

The manuscript repeatedly identifies the remaining signed estimate as
open and does not claim a new zero-free theorem. Its bibliography identifies
the September 30 source actually consulted, rather than transferring that
source's numbering to the user's different October 5 file. The mathematical
status is therefore accurately conveyed.

## Build and source record

The final saved standalone source compiled successfully with the desktop
editor's native compiler on 8 October 2026 after the reviewed corrections.
The source contains 58 unique labels and 62 resolved cross-references;
both bibliography keys used by citations are present. The record does not
claim a rendered-page visual inspection or an exported PDF file.

Final source SHA-256: `0f81b300268e2f291c726c2e1b7d32db7bb9d4846c145b710b3efb96157f97fb`.
