# Assessment: corrected outer carrier and signed real-axis bridge

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**, ansatz chat0001, thread `01a175aa-a487-79a1-85a8-6f465fdb36bf`.

**Review type: same-model internal analytical assessment.** Parallel
same-model derivation and obligation checks informed this assessment;
they are not cross-model, independent specialist or human review.
No numerical, symbolic, exact-arithmetic or interval checks were run.

## Evidence and decision

Reviewed [AN01 r1](../research-progress/handoffs/HDA-A01-AN01.md), the
[opening overview](../research-overview/01_HIGH_HEIGHT_ANSATZ_RESEARCH_OVERVIEW_20261025.md),
the [input manifest](../notes/03_CALIBRATION_BRIDGE_INPUTS_20261025.json),
and [Note03](../notes/03_OUTER_CORRECTION_AND_SIGNED_REAL_BRIDGE_20261025.md),
including its source/contour/tail ledgers. Primary DLMF5.11,
DLMF25.10.3--4, Polymath Theorem1.3 equations (23)--(24), corrected
equation (69), exact Gaussian formula (35), and Proposition9.1 were
reopened. Parent estimates retain their earlier internal-review status.

Accept the compact outer calibration, including its first correction,
buffered spatial jets and direct time derivative on **32<=t<=33**.
Accept the **real-axis field** bridge CB27 on
`|t| log(X/(4pi))<=8`, with the retained correction and fixed chart
cutoff. Accept CB29 as a precise failure of one absolute complex-kernel
bound. The requested full signed-time strip/jet comparison remains open.
Close AN01 at its explicitly permitted bounded partial-return scope;
HDA-A01 itself becomes **Partial**, with AN02 r1 prepared for Sol.

## Checks that determine the conclusion

1. **Normalization and branch.** One exact-gamma arm has leading
   coefficient `pi^(1/4)/32`; the full cosine has `pi^(1/4)/16`.
   Its unwrapped phase has constant `7pi/8`, and zeta height is `X/2`.
   Expanding `s=iz/2+1/2` gives `i/(24z)` in `log M`. Principal
   reduction of the gamma phase would lose the prescribed phase lift.

2. **Actual heat correction.** Under the tilted Gaussian the second
   moment is `t/2+t^2 alpha^2/4`. Multiplication by `alpha'/2` gives
   both `t alpha'/4` and `t^2 alpha^2 alpha'/8`. The first is the
   determinant term; the second comes from displacement. Squared
   curvature and the cubic Taylor remainder are within
   `O((1+log^4 X)/X^2)`. CB8--10 include Stirling as well. Full
   arithmetic has size `O(X^(-t log2/4))`; at t>=32 it is below
   this error, so the correction is to the true canonical H at this
   bounded scope. This arithmetic ordering is not extended toward zero.

3. **Fixed contour and complete tails.** The gamma arms use a fixed
   endpoint `V=(B+3)/2`; the source is split and reflected exactly.
   The complete arithmetic remainder, bounded middle, missing lower
   Gaussian part and both infinite right tails are separately retained.
   A draft issue was corrected before acceptance: with these endpoints,
   the middle reaches real part `B+2`. Its coarse polynomial power must
   depend on B. Note03 now uses `X^(B+6)`, rather than the fourth power
   sufficient for the narrower middle in parent Note27. This changes
   only the linear-log term in its superpolynomial error.

4. **Jet and time scope.** Strip estimates use the sum of carrier
   moduli, including the off-axis height powers. Cauchy disks have
   radius comparable to `1/log X`, yielding one log factor per jet.
   CB11 is an exact elementary residual; CB12 cancels its `1/z`
   term for the corrected model. The identity
   `partial_t(H-F)=-(H-F)_zz-(partial_t+partial_zz)F` proves the
   time bound from spatial estimates and the actual residual. No
   big-O allowance is differentiated or propagated by a residual alone.

5. **RS sign and cutoff.** Since `H(0,X)=-|M|Z(X/2)`, the first
   field correction has sign `(-1)^N`. The quotient C in CB14 has
   removable denominator zeros. Its exact recurrence matches the
   added adjacent mode, with `O(G X^-5/4)` error over a fixed real
   window. Thus freezing N produces a real `O(G X^-3/4)` corrected
   remainder without differentiating a floor.

6. **Negative-time window and mode count.** The exact forward Gaussian
   convolution is used. The whole `|v|<=16` window is paid; the tails
   up to `X/2` retain the height exponential and the distant tail uses
   the global complete-source bound. The finite-arm Taylor error sums
   over all N modes. The population bound
   `sum w_n<=C X^(1/4) exp(T L^2/16)` is essential.

7. **Why retaining the correction matters.** Absolute-to-carrier
   conversion costs up to `exp(T L^2/16)<=C X^1/2`. The bare RS
   remainder `X^-1/4` would fail to give decay throughout the requested
   window. The corrected remainder `X^-3/4` gives `X^-1/4`. The
   correction evolves to leading order as `exp(pi^2 T/64) R_N`,
   with its smoothing error inside the latter allowance. The retained
   term itself can exceed the outer carrier; it is not placed in the
   error budget.

8. **Positive side of the common real model.** Polymath(23)--(24) in
   its actual positive-time, real-axis domain give the requisite
   `O(X^-1/4)` field error when `t L<=8`. Stirling replacement and
   the whole mode population are paid; an adjacent cutoff term and
   the added explicit correction are within that coarse allowance.
   This does **not** identify the common correction as the exact
   positive-time `C_t` at an accuracy finer than CB27's error.

## Boundaries retained

- CB27 is real-axis field control. The local formula is holomorphic
  at fixed N, but its **error bound** has not been proved on the full
  complex averaging/differentiation buffer. Choosing a fresh floor
  globally at every x also leaves small truncation jumps; that
  piecewise representation is not a spatial-jet theorem.
- CB28 is a sufficient unproved zero-time complex remainder, with
  the correct two-arm envelope, fixed buffers and uniform cutoff
  handling. An `X^epsilon` loss with epsilon<1/4 would suffice for
  the bounded negative-time field gain. CB29 shows why the naive
  real-line absolute kernel bound does not supply it. This is a
  scoped failed route, not a universal exclusion of complex estimates.
- No signed-time spatial jet or direct time derivative through zero
  is accepted. A naive kernel derivative costs `1/T`; smoothness
  of the displayed model in t does not bound the error derivative.
- Constants and finite onsets are given by the analytical gate
  ledger and inherited finite constants, without numerical
  instantiation. The full-strip signed onset is not supplied.
- No physical density/current/covariance transfer, useful runtime,
  collision conclusion or all-real-time covering theorem follows.
  Parent HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled remain.

The source-specific control screen in Note03 names the canonical
coefficient/completion/RS premises absent from the collision controls.
It is an analytical premise screen, not a new control computation.
See [result summaries](../../../../../result-summaries/README.md) and
[avoid](../../../../../avoid/README.md), particularly scope07,
normalization08, cancellation12 and unchecked-imports16.

**Next owner: Analysis — Sol.** Execute
[AN02 r1](../research-progress/handoffs/HDA-A01-AN02.md): the fixed-cutoff
complex remainder and its full buffered small-time consumers. A contour
or local three-lines proof remains a routine focused candidate. Reserve
Astra for a specific resistant mechanism after that attempt.
