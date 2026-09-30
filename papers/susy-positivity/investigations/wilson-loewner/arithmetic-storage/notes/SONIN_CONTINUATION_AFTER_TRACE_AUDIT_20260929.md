# Sonin continuation after the trace audit

29 September 2026. Prepared for Edward Baker with LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
not exposed. This is a research handoff, not independent human review.

**Current result.** The [canonical audit](SONIN_CANONICAL_COMPARISON_AUDIT_20260929.md)
passes the recovered comparison on compact smooth sources. The
[continuation analysis](SONIN_PLACE_ADDITION_AND_ERROR_CONTROL_20260929.md)
adds an exact signed place-addition formula, a Chebyshev return expansion,
and a one-sided Galerkin trace error identity. The [critical review](../reviews/SONIN_TRACE_AUDIT_REVIEW_20260929.md)
records the limits. This supersedes the 28 September handoff as the immediate
starting point; keep that earlier source and the completed Weil certificates.
CCM remains temporarily closed.

## What is established internally

- The error sign in `B_infinity=Gamma+E_infinity`, gamma contact, pole
  separation, source Mellin convention, and direction of `D_S` all check.
  The actual orthogonal projection needs the inverse compressed metric.
- `C_H Pi` is trace class for every compact smooth kernel; the simpler
  Hilbert–Schmidt compressed-product proof suffices for finite-place traces.
  The pole-neutral source class remains RH-equivalent on an unbounded
  exhaustion of supports, with no additional parity restriction.
- Place addition has a signed covariance formula. For the complete target
  at fixed support, the residual changes by minus the change of `B_S`.
  An explicit new prime-power subtraction occurs only for the separately
  defined partial arithmetic form. Conflating these double-counts primes.
- The Chebyshev return expansion needs 64 trace terms for the crude
  `10^-8 B_infinity[f]` tail bound at prime 2, versus 373 for the inherited
  Neumann series. The small standard-library record certifies only these
  scalar majorants.
- Exact actual-Sonin trial spaces give positive `B_N` increasing to `B_S`
  for each fixed source and finite `S`. The error is an energy norm of the
  full Hilbert–Schmidt residual, with the finite-matrix identity (A16).
  This is convergence to `B_S`, not to the full arithmetic form `Q`.

## Next single task

Prove and implement certified enclosures for the quantities in (A16) of
the continuation analysis, using a small nonzero trial space obtained by
applying the actual Sonin projection to compact smooth seed vectors, at
`S={infinity,2}` and on the two normalized sources (A17), `L=1`.

The central missing bound is the **full** Hilbert–Schmidt residual,
including the infinite spatial tails. Its matrix reduction uses an
archimedean scalar trace of `D_S F`, plus actual-Sonin matrix entries.
Do not replace the actual projection by a finite cosine projection or
claim operator-norm convergence of finite-rank projections to `Pi`.

If that lemma succeeds at a useful scale, independently enclose the
Chebyshev return moments, prolate error, and prime correlation as in
(A19), and report all pieces of (A18) with a total error budget. Do not
define the residual solely by subtracting a direct Weil evaluation.
No source energies or actual Sonin traces have yet been evaluated for
the new family; old unrestricted weak-vector scales do not determine them.

If the certified quantities remain too coarse, record the precise failed
bound and stop that numerical extension. Increasing source support or
building another finite Weil certificate is not the next step.

The longer-term question remains a signed, Sonin-specific control of
the covariance defect and its explicit prime-power contribution, or an
arithmetic fixed-test limit. Generic positivity and the finite-place
condition-number bounds supply neither. No residual sign theorem,
new positivity interval, or RH claim was obtained in this session.

Save research in this `notes/` folder, computations in `numerics/`, and
reviews in `reviews/`. Update indexes as results change. No manuscript
or draft snapshot is needed, and no commit or push is requested.
