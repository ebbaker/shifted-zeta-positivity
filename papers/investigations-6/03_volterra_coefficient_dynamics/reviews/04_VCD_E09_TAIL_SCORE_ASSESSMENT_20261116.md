# VCD-E09 r1 assessment of the tail and score proofs

16 November 2026, America/New_York. Prepared for Edward Baker with OpenAI
Codex LLM assistance. Separate assessment worker, recorded tool dispatch
**gpt-6.1-sol / ultra**. Separate runtime model and effort attestation
unavailable. The assessment uses the same tool-selected model and inherited
premises as the proof tasks. It is an internal LLM review.

**Disposition: accepted without mathematical correction within the stated
scope.** All five note hashes in the [frozen E09 request][request] match. The
earlier E04/E05 setup manifest and the E06 r2, E07 and E08 request hashes
also match. I read those tasks and returns, checked the derivations against
the retained source and coefficient bounds, and inspected the proofs cited
for the relevant controls. E10 is outside the frozen bundle. See the
[result index][results], [coefficient cluster][cluster], [collision
catalog][catalog] and [avoid index][avoid] for context.

## E04 and E05

- Retaining the endpoints preserves the full scalar readout. Replacing the
  propagator with the finite block removes the two-step boundary excursion
  from the matrix and first affects the scalar at length \(2N\). The unique
  shortest removed scalar walk has weight \(\prod_{j=1}^N\beta_j\) and
  Fourier derivative sign \((-1)^N\). A bounded edge deletion preserves
  self-adjointness and the finite head splits its domain. In the tail core
  proof, a nonzero deficiency vector would give a lower bound proportional
  to \(1/a_{L+1}\) for \(|f_Lf_{L+1}|\), incompatible with summability.
  The real Duhamel sign, the first tail link index \(n+1\), and the Laplace conversion
  \(-i m_n(-is)=i m_n(is)\) all agree with the stated conventions. The
  last equality uses spectral symmetry. [E04 §§1–3][e04]
- The support of each tridiagonal power gives the logarithmic bound with
  \(j+p+2\). Both the vector Taylor series and the nonnegative cosh
  moment series converge at each fixed site uniformly in the time band.
  The bound \(k_N(ib)\ge1+b^2\beta_{N+1}/2\), together with unbounded
  support at each fixed \(\lambda\), excludes an absolute bound uniform
  over moving sites on a fixed complex neighborhood for these unscaled
  kernels. It still allows the uniform real-axis bound and convergence
  of the scalar quadratures on fixed disks. Their nonnegative walk
  moments and the common majorant \(W_{1/2}/Z_0\) give uniform convergence.
  Rouché gives the forward strip implication, and under RH a diagonal
  exhaustion of compact sets away from the real line gives the converse
  for unspecified windows and widths. A prescribed rate or finite-stage
  reality claim would require additional work. [E04 §§4–5][e04]
- The first-mode lower bound and differentiated-series upper bound put
  \(V' q_j\) in the multiplication domain. Normalized integration by
  parts gives \(n/a_n\) in the adjacent entry and the derivative pairing
  on the whole head. For an odd polynomial of degree at most \(2d+1\),
  the adjacent path can reach link \(a_{n+d}\). A retained cross-cut path
  requires at least \(2N-i-j\) steps and opposite parity forces
  \(i+j\le2N-3\), so the last possible omitted link there is
  \(a_{N+d-1}\). This checks the tighter cross-cut limit and the cubic
  coefficient \(4a_{N-1}\beta_N\). Recovering the retained score
  compression from the exact head is distinct from estimating its signed
  full-minus-node residual with unsupplied links. The weighted Cauchy
  bounds lose the sign and the full/discrete cancellation as stated.
  [E05 §§1–4][e05], [manuscript §§2–5][ms]

## E06 and E07

- The fixed-polynomial path estimate uses \(a_j\le\sqrt{B_{j-1}}\),
  at most \(2^k\) paths of length \(k\), and one exterior factor \(a_n\).
  This yields the stated \(n+O_p(\log^{d+1}(n+2))\) signed residual for
  fixed \(p\) of degree \(d\), uniformly in the physical time band. It
  excludes a negligible relative residual for that polynomial class.
  The score reference follows from
  \(4\rho-8\pi\sinh(4u)=4\pi e^{-4u}\), the ratio bound
  \(w_m\le2m^4e^{-(m^2-1)\rho}\), and monotonicity of
  \(\rho e^{-(m^2-1)\rho}\) for \(m\ge2\), \(\rho\ge\pi\).
  The explicit \(C_b\), heat-independent odd extension and positive-side
  limit \(-9\) check out. The normalized adjacent allowance is
  \(C_ba_n/n=O(\log(n+2)/n)\). [E06 §§1–2][e06]
- Continuing the finite projected equation to \(x=-it\) gives a positive
  memory term, with one \(-i\) from differentiation and one from the
  oriented convolution. The
  \(\beta_N[t^2P/2+t^3(AP+PA)/6]\) expansion matches the two- and
  three-step paths. Taking the odd part produces the coefficient
  \(4\pi\) at \(t=\pm4\) in the score correction. Its cross-cut
  paths are nonnegative entrywise on opposite-parity sites, and the
  bounded-symbol correction has norm at most \(2C_b\). These are
  fixed-entry exponential-multiplier statements. The integrals still
  contain the full tail and yield no signed cosine margin.
  [E06 §§3–4][e06]
- The homogeneous finite constraints in E07 keep the requisite Gram data
  and probability normalization before the score entries are compared.
  The least nonzero perturbed mode proves independence. A small nonzero
  scale preserves positivity and the first mode, and the logarithmic
  derivative of \(1+\epsilon f/\Phi\) yields the arbitrarily small
  essential sup norm bound. The positive modewise mean keeps the same
  confinement and envelope. Exact rows and head are imposed at time zero,
  while the relative error allowance holds uniformly for
  \(0\le\lambda\le1/2\). The first uncancelled odd endpoint is finite
  and survives every real heat tilt. The inherited finite-change theorem
  gives eventual algebraic sign on the real axis and order one of
  infinite type from positivity and the first-mode tail on the imaginary
  axis. This proves infinitely many nonreal zeros at each fixed real
  heat time in this finite-change class. [E07 §§1–2][e07],
  [finite-source proof §3][finite]
- The catalog checks distinguish the premises used by different controls.
  The weighted-square examples share the envelope and a bounded score
  difference with control-dependent constants. Euler translates change
  the normalized second moment by \(ca^2/(1+c)\) and have leading score
  \(4\pi e^{-4a}e^{4u}\). The reflected super-Gaussian has polynomial
  score growth. The small-damping smooth families have leading score
  \(4\delta\sinh(4u)\), so the comparison to theta misses by an
  unbounded amount when \(\delta<2\pi\). The orbit theorem accepts the
  exact linear observations, and the extended bounded-coefficient tail
  estimate applies there. Its high-gap events and failure of full
  reflection come from its own proof. The RH-conditional endpoint
  control preserves a completion normalization, while the physical mass
  ratio at zero is \(a^4/(b^2c^2)=1+2e/(b^2c^2)>1\). Atomic and compact
  triangular examples fail the global positive-density premise, the
  varied observation fails the literal readout, and the profile
  relaxation does not supply the physical source. The scope ledger
  keeps untested exact head and row comparisons open. [E07 §3][e07],
  [catalog][catalog], [orbit proof][orbit], [endpoint proof §3][endpoint]
- E07 obstructs a global all-real implication from its fixed finite
  measurements and all-degree relative allowance in the positive
  finite-change class. Each perturbation can depend on the chosen
  measurement list. Neither a nonreal zero in a prescribed bounded
  window nor a failure of a growing-degree compact confinement scheme
  follows. The compact stability estimate is only for sets with a
  positive lower modulus for the canonical field. [E07 §4][e07],
  [scope pattern][scope]

## E08

For an even measure of infinite support, derivative orthogonality gives
\(\int(q_nq_{n-1})'\,d\nu=n/a_n\). Consequently the leading coefficient
in the adjacent-to-Stein map is
\(a_n\kappa_n\kappa_{n-1}=\kappa_{n-1}^2\). Parity makes the even tests
automatic. The first \(N\) adjacent equalities are equivalent to all odd
tests through \(2N-1\), and the next row adds \(u^{2N+1}\) modulo lower
tests. The conversion is triangular at every finite degree and gives no
uniform conditioning estimate. Full consistency makes every polynomial
Stein defect vanish. The
weighted exponential integrability justifies the Taylor test for
\(e^{itu}\) and its derivative. Fourier inversion against compact smooth
tests yields \(\nu'=-V'\nu\). The integrating factor works on a locally
finite measure, and zero distributional derivative characterizes a
constant multiple of Lebesgue measure. The probability normalization
then uniquely gives \(\mu_\lambda\). [E08 §1][e08]

The defect matrix commutes entrywise by the polynomial recurrence in
either argument, with finite sums. Cutting the two full products gives
\(-a_N\mathbf e_{N-1} E_{N,H}+a_N E_{H,N}\mathbf e_{N-1}^{\mathsf T}\)
for \([J_N,E_N]\). Symmetry cancels the shared last product, so
\(a_NE_{N,N-1}=e_N\) is invisible to this commutator. For \(i<N-1\),
the odd \(q_iq_N\) products have degree at most \(2N-3\), and replacing
\(a_Nq_N\) by \(uq_{N-1}-a_{N-1}q_{N-2}\) shows that the weighted
off-endpoint column comes from retained data. At \(N=1\) the head
commutator vanishes. For the regular-density subcase, the bounded
multiplier norm estimate follows from orthonormality. These formulas
account for the missing next test. All-degree identification concerns the
source and leaves its Fourier zeros as a separate problem. [E08 §§2–3][e08]

The accepted results are exact identities, an approximation estimate,
scoped fixed-information obstructions and a source characterization.
The unspecified-strip equivalence records the target. No result here
proves those strips, a quantitative next-row estimate or an RH claim.
[Target pattern][target]

[request]: ../research-progress/handoffs/VCD-E09-r1.md
[e04]: ../notes/04_VCD_E04_TAIL_FOUNDATIONS_20261116.md
[e05]: ../notes/05_VCD_E05_SOURCE_SCORE_RESIDUAL_20261116.md
[e06]: ../notes/06_VCD_E06_EXPONENTIAL_SCORE_RESIDUAL_20261116.md
[e07]: ../notes/07_VCD_E07_FINITE_CANONICAL_SCORE_CONTROLS_20261116.md
[e08]: ../notes/08_VCD_E08_FULL_SCORE_RIGIDITY_20261116.md
[ms]: ../manuscript/main.tex
[results]: ../../../../result-summaries/README.md
[cluster]: ../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[catalog]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[target]: ../../../../avoid/01_restating_the_target.md
[finite]: ../../../investigations-3/07_source_measurement_audit/notes/round-2/01_REVIEW_RECONCILIATION_AND_ENDPOINT_NONREALITY_CODEX_20261017.md#3-every-nonzero-finite-change-has-non-real-zeros-at-every-heat-time
[orbit]: ../../../investigations-3/11_arithmetic_collision_rigidity/notes/03_FINITE_PRIME_COMPATIBLE_COLLISION_CONTROLS_CODEX_20261018.md
[endpoint]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/05_CLOSE_POSITIVE_SOURCES_AND_NORMALIZED_DOUBLE_ZEROS_20261020.md#3-a-double-zero-with-unchanged-residue-and-leading-tail
