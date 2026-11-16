# VCD-E02 — Assessment of the logarithmic coefficient envelope

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Tool dispatch **gpt-6.1-sol /
ultra**. Separate backend verification unavailable. Separate same-worker
internal assessment sharing the E01 source and mathematical premises.
See [shared-premise review guidance](../../../../avoid/05_same_model_reviews_and_shared_premises.md).

**Disposition: accepted without correction within scope.** The
[proof](../notes/01_VCD_E01_LOGARITHMIC_ENVELOPE_20261113.md) establishes
E1 and E2 as stated. All four input hashes in
[frozen assessment r1](../research-progress/handoffs/VCD-E02-r1.md)
and all nine inherited manifest entries matched. Assessment request
SHA-256 `1fb69f9bda698a5cc472402ce7dc54ea044bb0c10c7b0761cf31f721e2f5afa9`.
There is no independent specialist review.

- **Score and constants.** Differentiating \(r(2r-3)e^{-r}\) with
  \(r'=4r\) gives the stated \(9+12/(2r-3)-4r\) for the full summand
  including \(e^u\). The positive weights preserve the common score
  bound because \(r_m\ge\pi e^{4u}>3\) and \(2\lambda\le1\). The
  small-region allowance is adequate since \(-27/4>-7>\cosh2-11\).
  In the other region \(t\ge1/2\) makes \(4\pi t-1>10t\) and
  \(10e^{4t}\ge10+40t\ge13+t\). These give the full-line offset \(11\).
- **Tails and monicity.** The differentiated summand degree is three,
  and the Gaussian majorant in the square index controls the complete
  series and both fixed derivative bounds. The negative
  \(-\pi e^{4|u|}\) dominates \(u^2/2\), polynomial powers and the extra
  \(e^{4|u|}\) for Jensen. Thus the boundary term is zero and the
  \(V_\lambda'\) term is absolutely integrable via \(W_\lambda'\).
  The top term of \(uP_n'\) is \(nP_n\) modulo lower degree, giving
  \(2n+1\), also at \(n=0\). The coefficient of \(P_{n-1}\) in the monic
  recurrence is \(h_n/h_{n-1}\) by symmetry of multiplication, while
  parity removes the diagonal. Its squared norm gives the sum of
  adjacent \(\beta\)'s, with only the \(P_1\) term at \(n=0\).
- **Jensen and regime.** Every partial sum of \(\cosh(4\sqrt v)\) has
  nonnegative second derivative on \(v\ge0\). Jensen and the score
  expectation give \(2n+1+11=2n+12\) before inversion. The argument
  applies at every finite degree and every allowed \(\lambda\); the
  constants are common and a simultaneous tail cutoff is unnecessary.
  The inherited lattice sign agrees with the positive derivative
  \(\partial_\lambda W_\lambda=u^2W_\lambda\): differentiating
  \(\log h_n\) gives \(\beta_{n+1}+\beta_n\), since the derivative
  of the monic polynomial is lower degree. Subtraction at adjacent
  degrees gives \(\partial_\lambda\beta_n=\beta_n(\beta_{n+1}-\beta_{n-1})\).
  The clock \(\tau=1/2-\lambda\) reverses this sign. The proof of E1
  does not require differentiation in time.
- **Consumer.** The positive ratios telescope to \(h_N/h_0\), the
  squared norm for \(W_{1/2}du/h_0(1/2)\) and the fixed chain \(J(1/2)\).
  Monotonicity puts the largest factor at \(2(N-1)+12=2N+10\).
  The estimate replaces the unknown norm factor by the explicit
  product, or by its coarser \([\operatorname{arcosh}(2N+10)/4]^{2N}\)
  bound. JCH owns the remaining readout factor and its error domain,
  with \(Z_*/2\) still needed for an unnormalized field error.
- **Controls.** The three-atom failure at \(n=1\) and the Euler-factor
  \(p=23,\lambda=0\) failure at \(n=0\) follow from the displayed strict
  elementary comparisons. The three- and four-square witnesses keep
  every score premise used by the weighted-sum and two half-line
  proof, so both pass at the collision. The reflected quartic source
  fails the exponential score lower bound. The small-damping sources
  lack the exact summand formula, finite-prime modifications fail full
  reflection with admissible even extensions potentially passing,
  atomic/compact profile families lack the global positive density
  premise, and RH-conditional endpoint sources lack the unchanged
  arithmetic formula. The note preserves the untested coefficient
  comparisons and RH and small-damping qualifiers. Altering the
  observation alone leaves the coefficient bound unchanged and
  fails the physical oscillator/Newman equation. These checks support
  the stated approximation allowance and delimit its collision scope.

No routine correction or response check was needed. The fixed VCD round
ends at this assessment.
