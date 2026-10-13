# Decision on the first 09-to-06 factorization candidate

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: `gpt-6-astra` (Codex); reasoning effort **ultra**. This is an
internal assessment of the current derivation and replay, not an
independent mathematical review.

The [09 complete two-coset reduction](../../09_rank_two_theta_addition/notes/1_COMPLETE_TWO_COSET_REDUCTION_20261013.md)
successfully transports the unequal-scale theta product and its actual
differential insertions into both complete paired kernels. It retains
both parity cosets, zero-axis annihilation, the unequal-scale mixed
term, the signed `J_1` insertion, and the physical normalization.

The proposed continuation through independent positive coset
factorizations fails. The [06 analytic note](../notes/1_FOLDED_PARITY_CUSP_AND_FACTORISATION_OBSTRUCTION_20261013.md)
identifies two distinct obstructions:

- In the modular-folded split, the opposite source slopes at zero create
  a nonzero cusp channel. The same-parity Fourier responses have strict
  negative tails `-4c²/x^6` and `-24c²/x^8`, respectively, with higher
  order remainders uniform on compact time intervals. This is a complete
  analytic obstruction. The matrix parity-contrast direction is negative
  as well, so an invertible change of those two source coordinates does
  not make the entire polarized response matrix positive semidefinite.
- In the smooth resummed raw split, the same-parity responses are both
  negative at `t=x=0`, as certified by complete moments. Averaging a raw
  kernel with its reflection leaves that zero-frequency value unchanged,
  so this simple Hermitianization does not repair the factorization.

The shared [outward replay record](../../09_rank_two_theta_addition/numerics/RANK_TWO_TO_PAIRED_RECORD_20261013.json)
also certifies both folded negative signs at `t=0,x=60`. Its retained
terms, quadrature remainders, omitted theta terms, and source tails
are all paid. These certificates concern Fourier responses of specific
sectors, not negative values of the complete source kernel, and do not
impose sectorwise stationarity.

The full physical response cancels the folded cusp terms exactly.
Its two stationary targets remain `L_0(H)>=0` on `H'=0` and
`L_1(H)>=0` on `H''=0`. No counterexample to either target, no full
positive-definiteness theorem, and no global RH conclusion has been
obtained. The low-order kernel normalization and parity bookkeeping
are now explicit enough to test a different proposed factorization.

**Decision:** stop the independent positive coset route in these two
realizations. Continue 06 only through a source-derived construction
that retains and controls the cross-coset cancellation, or through a
new direct estimate on the complete stationary quadratic form. A larger
finite Gram survey is not needed to reject the candidate just tested.
