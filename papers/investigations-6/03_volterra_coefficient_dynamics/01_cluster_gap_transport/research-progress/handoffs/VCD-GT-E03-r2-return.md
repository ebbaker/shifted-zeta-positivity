# VCD-GT-E03 r2 — Fixed-event signed-defect return

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Explicit helper dispatch
**gpt-6.1-sol / ultra**. Separate backend attestation and actual
lead configuration are unavailable. The helper authored E01 and
uses that internally assessed result here.

**Complete, proved in-note under the stipulated event assumptions.**
All seven SHA-256 pins in the [frozen request][request] matched.
The request SHA-256 is
`1203f431ddb1bc4114a6f6095a6f310943f3e1873bb1ccc415a96e3a321e11e0`,
and the [proof note][note] SHA-256 is
`539afbdb2c2ca2711582b6e5d67297334ecc0fa21cf5ccbb349d717fd488d99a`.
The [sole register][register] owns the task disposition. The proof
fulfills [B02 decision02][decision] at a fixed real nonzero double
zero of \(F_T\) with \(0<T<1/2\). It acquires no canonical event.

- At \(F_T(z)=(z-a)^2 A_T(z)\), write \(L_N\) for the first
  omitted quadrature term and \(R_N\) for the r1 model heat defect.
  The centered logarithm gives \(D_N(T)\sim L_N(T,a)/A_T(a)\).
  The defect contour gives \(r_N(T)\sim-R_N(T,a)/A_T(a)\).
  Both relative error estimates retain a factorial-small factor
  after division by their own leading terms. The signed ratios are
  \(r_N(T)/D_N(T)\sim (2N)(2N-1)/a^2\) and
  \(r_N(T)/D_{N+1}(T)\sim-\Pi_N/(\beta_{N+1}(T)a^4)\), where
  \(\Pi_N=(2N-1)(2N)(2N+1)(2N+2)\). The r1 four-factor scale
  survives the contour at this event, and the residual sign
  alternates with degree. Computing \(R_N\) and \(G_{N+1}\)
  uses the same first \(N\) links. The first omitted
  \(\beta_{N+1}\) in the next-head error needs no lower bound.
- On a fixed sufficiently small interval, uniform convergence
  of \(K_N,D_N,r_N\) in the exact model equation yields
  physical-time \(C^1\) convergence \(D_N\to D\).
  The model discriminant has exactly one zero there for every
  sufficiently large degree, at
  \(\lambda_N-T\sim-L_N(T,a)/(2A_T(a))\). No slope floor for
  individual roots or physical heat equation for the model is used.
- For \(\tau_N=o(N^{-2})\), \(\tau_N>0\), the root-average
  identity and localization to \(o(1/N)\) at \(a\) give
  \(r_N(t)/r_N(T)\to1\) uniformly on \([T,T+\tau_N]\),
  through any model merger. The bounded model divided difference
  makes the integrating factor converge uniformly to one.
  The actual signed integral is \(\sim\tau_N r_N(T)\).
  Its magnitude divided by \(|D_{N+1}(T)|\) is asymptotic to
  \(\tau_N\Pi_N/(\beta_{N+1}(T)a^4)\). At \(\tau_N=N^{-3}\)
  this is \(\sim16N/(\beta_{N+1}(T)a^4)\), at least of order
  \(N/\log^2(N+1)\). The fixed-circle absolute safety allowance
  exceeds the actual integral's magnitude by a factor of
  order \(((|a|+\rho)/|a|)^{2N-2}\) with fixed valid floors.
- The full r1 signed transport includes the incoming error and
  the force-transfer term. Their combination can cancel with
  the residual, so the result supplies no lower bound on the
  total signed correction and no strict gap margin.

The exact quadratic control exhausts its gap and lacks the infinite
positive Jacobi source. The fixed weighted-square collision controls
share the relevant law and envelopes on their own local event tubes,
even while failing the full canonical reflection and arithmetic.
The proof lists the other controls' scoped premise verdicts.
No numerical acquisition or new source inequality was used.
Source-specific joint compensation, other signed estimators and
independent canonical information remain open. This return records
the bounded proof, with separate assessment to follow.

[request]: VCD-GT-E03-r2.md
[note]: ../../notes/06_VCD_GT_E03_FIXED_EVENT_DEFECT_20261116.md
[decision]: ../../brainstorm/notes/02_VCD_GT_B02_FIXED_EVENT_DECISION_20261116.md
[register]: ../01_VCD_GT_RESEARCH_PROGRESS_20261116.md
