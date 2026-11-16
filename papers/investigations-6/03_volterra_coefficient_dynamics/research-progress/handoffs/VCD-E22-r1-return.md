# VCD-E22 r1 — Quantitative error phase and corrected-model return

16 November 2026, America/New_York. Prepared for Edward Baker with
OpenAI Codex LLM assistance. Recorded dispatch **gpt-6.1-sol / ultra**.
Separate backend model and effort attestation unavailable.

**Complete, proved in-note for the defined error law.**
[Note21][note] implements the [frozen E22 request][request]. All seven
input SHA-256 hashes matched. The request SHA-256 is
`67f8f78cd6ffcbd29c70bafbb718b479614b695023fb63f027a0ba410c0020e5`
and Note21 SHA-256 is
`411d1c484db9ee78ea8db00c210370a04403b9d74e118e67a77318806fcc94da`.
The one correction pass clarified the simplex change of variables
and the direct \(N=1\) exponential payment. The proof for the law is
independent of E21. The consumer uses E21's identity as specified
in the addendum.

- The beta split and elementary Dirichlet moments give exact
  second and fourth moments. The paired-node power series has
  nonnegative even coefficients. Replacing each \((2N)_k\) by
  \((2N)^k\) in the denominator pays the bounded-node exponential
  through its full product. The unbounded \(U\) uses the complete
  E01 cosh moment instead. The convexity step pays
  \(\mathbb E e^{2Y X_N}\) by the degree-only \(\mathcal A_N(Y)\)
  of Note21 (6), with \(\overline L_N<N\) for \(N\ge2\) and a
  degenerate zero node for \(N=1\).
- With the fourth-moment allowance \(\mathcal Q_N\) of Note21 (7),
  the error-factor radius is
  \(\epsilon_N(r,Y)=r^2\sqrt{2\mathcal A_N(Y)\mathcal Q_N}/2\).
  It is \(O(r^2\log^2(N+1)/N)\) uniformly for
  \(|\Im z|\le Y\le1,\ r=|z|\). The bound allows growing real
  height and implies uniform convergence of the factor to one
  when \(r_N\log(N+1)/\sqrt N\to0\) in the strip.
- The corrected \(C_N=G_N+L_N\) gives the disk
  \(|F-C_N|\le |L_N|\epsilon_N\). The boundary comparison
  \(|C_N|>|L_N|\epsilon_N\) transfers zero counts with
  multiplicity on piecewise smooth simple contours.
  [Topping, §9.9, Theorem 9.21, printed p.104][topping] was
  directly checked. The model requires the actual links through
  \(\beta_N\). The degree-only budgets need no deeper links.
  The variance bound gives strict real-axis error sign
  \((-1)^N\) on \(0<|x|<\sqrt{2/\mathcal V_N}\) and
  consecutive even/odd bracketing on the common range.
- The comparison needs one qualification. The bare disk with
  radius \(|L_N|(1+\epsilon_N)\) deduced from the centered disk
  contains it. The centered disk and a separately paid bare disk
  need not be nested. In particular the independent real bare
  radius is \(|L_N|\), and for \(x\ne0\) and \(0<\epsilon_N<1\)
  neither disk contains the other. This corrects an unqualified
  reading of the request's comparison language. All proposed
  moment and exponential constants and domains are retained.

The weighted-square collision controls share the cosh moment and
the recurrence envelope and pass the phase bound. Their failure
of full reflection and complete canonical arithmetic is outside
the estimate's premises. The other catalog families keep the
scopes in Note21 §6. The canonical contour modulus margin and
model zero count remain unproved. This is a quantitative phase
estimate and a conditional zero-count consumer. No coefficient
acquisition, numerical scan, or manuscript revision was performed.

## Completed E21 dependency addendum

The finalized [E21 return][e21return], SHA-256 `c018e9ca4e92531fa9148dad4fd28c111872356cebd26c3a5c93e78b924e81c5`,
reports the identity (9) of Note21 for every \(N\ge1\) and every
\(z\in\mathbb C\), for the unchanged time-zero normalized theta source.
The [E21 proof][e21note], SHA-256 `483ad9c88c8a07d833903e941dda5e9bc9520e94e8b64e99713c0c9b119002a9`,
matches the simplex law, sign and monic norm used here.
Consequently Note21's disk, strict contour transfer and real-axis
parity comparisons apply to the literal \(F\). The contour test
still requires its own strict model margin. This dependency was
added after the independent estimate for the law.

[request]: VCD-E22-r1.md
[note]: ../../notes/21_VCD_E22_QUANTITATIVE_ERROR_PHASE_20261116.md
[e21return]: VCD-E21-r1-return.md
[e21note]: ../../notes/20_VCD_E21_COMPLETE_ERROR_PROBABILITY_LAW_20261116.md
[topping]: https://warwick.ac.uk/fac/sci/maths/people/staff/peter_topping/teaching/ma3b8_cplxanal_24_07_29.pdf#page=104
