# VCD-GT-E05 r5 — Assessment of the complete xi evaluator

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Reviewer dispatch selected
**gpt-6.1-sol / ultra**. Separate backend attestation and the lead's actual
recorded configuration are unavailable. The reviewer did not contribute to
the assessed proof. This is an internal assessment with shared source
premises and model selection. [Shared-premise review limits](../../../../../avoid/05_same_model_reviews_and_shared_premises.md)

**Accepted within scope.** The fixed-domain evaluation bound in Note12
§§1–3 remains **proved in-note**. The contour and time bounds in §§4–5
remain conditional on their stated acquisition and error premises. This
assesses a finite quantitative evaluation contract. The canonical count,
modulus, buffer, angular and time allowances, and gain comparison remain
to be acquired. [Note12][note] · [B04 decision][decision] ·
[Result index](../../../../../result-summaries/README.md) ·
[Avoid index](../../../../../avoid/README.md)

The four SHA-256 values in the [frozen request][request] matched on entry.
The request SHA-256 is
`3bc8bf11678aa9e6bc67538e1ce181645fad415bbfd8e0aa88ce6844094ad316`.
The assessment covers the proof, the selected literature passages, and
the error contract. Numerical acquisition and the wider-disk/interpolation
work are separate.

## Normalization and analytic imports

- On \(u\ge0\), \(r_m\ge\pi\) gives
  \(0<(2r_m^2-3r_m)e^{-r_m}\le 2r_m^2e^{-r_m}\).
  Splitting \(e^{-\pi m^2 e^{4u}}\) at \(m=1\) gives the summable
  envelope (2). Extra powers of \(u\), a bounded heat tilt, and a
  bounded factor \(e^{|\Im z||u|}\) preserve domination. This supplies
  local differentiability and \(\partial_t H_t=-\partial_z^2 H_t\).
  The series for the primitive and its derivatives also converge
  locally uniformly for real \(u\).
- With \(\Theta(v)=1+2\psi(v)\), Jacobi inversion gives
  \(\Theta(e^{-4u})=e^{2u}\Theta(e^{4u})\). Thus \(p(-u)-p(u)=\sinh u\)
  and \(p'(0)=-1/2\). Differentiating each \(e^{u-r_m}\) twice
  and subtracting the term gives \(8(2r_m^2-3r_m)e^{u-r_m}\).
  Two integrations by parts then give \(8H_0=1/2-(1+z^2)I\).
  The \(\sin(0)\) boundary term vanishes, and the nonzero boundary
  term is \(-p'(0)=1/2\). The even extension converts the half of
  the full Fourier integral to one cosine integral.
  [DLMF 20.2.3](https://dlmf.nist.gov/20.2#E3) ·
  [DLMF 20.7.32](https://dlmf.nist.gov/20.7#E32)
- The elementary part of the Mellin split at one is
  \(1/(s-1)-1/s=1/[s(s-1)]\). Termwise integration initially has
  absolute majorant \(\Gamma(\Re s/2)\pi^{-\Re s/2}\zeta(\Re s)\)
  for \(\Re s>1\). The reflected integral on \([1,\infty)\) is entire
  by double-exponential decay after \(v=e^{4u}\). Its exponents
  are \(2s\) and \(2(1-s)\) in \(u\), giving \(8I\) at
  \(s=(1+iz)/2\). Since \(s(s-1)=-(1+z^2)/4\), the standard
  completion equals \(8H_0\). This matches the stated reflection.
  [DLMF 25.4.3](https://dlmf.nist.gov/25.4#E3) ·
  [DLMF 25.4.4](https://dlmf.nist.gov/25.4#E4)
- The shifted Fourier factor contributes \(e^{-2\sqrt t\,ru}\).
  Completing the square supplies \(e^{tu^2}\); integration in \(r\)
  produces \(\sqrt\pi\) and the \(\Phi\)-envelope pays Fubini.
  This proves the Gaussian identity with the same complete source,
  including \(t=0\). The real physical coordinate is twice the zeta
  ordinate. Multiplying the heat field by the constant
  \(g=\exp(\pi a/8)\) keeps its heat equation, zeros, and logarithmic
  derivative. In a collar log for the moments it adds only a constant.
- The selected pp.107–109 of the catalogued Csordas–Smith–Varga
  reading copy were visually rechecked. Equations (1.1)–(1.3′)
  use the same theta density, heat convention and \(1/8\), and (1.9)
  displays the stated approximate pair in physical coordinates. The
  article's close-pair data locate the candidate. The analytic
  evaluation bound does not use its historical lower-bound theorem,
  root indexing or an all-real slice. [Lehmer source-use record][lehmer]

## Strip majorant and quadrature

The reflection is a pointwise equality of the entire \(\xi\)-values, so
selecting a half-plane by the sign of a real part leaves the contour
integrand entire. For \(r=\nu+i\eta'\), the selected \(s/2\) has
\[
 X=1/4+|\Im z/4+\sqrt t\,\nu/2|,\qquad
 |Y|=|\Re z/4-\sqrt t\,\eta'/2|.
\]
The bounds in (5) follow from \(a/4=140101/40\), disk radius 2,
\(|\eta'|\le2\) and \(\sqrt t<8/25\). The norm estimate in (6) uses
\(|s-1|\le |s|\) when \(\Re s\ge1/2\), and
\(|\omega|\le X+|Y|<3505+(4/25)|\nu|\).

The Binet remainder formula applies with \(X\ge1/4\). Expanding
\(b\cosh b-\sinh b\) and \((1+b^2/3)\sinh b-b\cosh b\) gives the
coefficients listed in Note12, with the coefficient of \(b\) zero
in both cases. This bounds the Laplace kernel by
\(1/12\). Taking the real part gives the phase term
\(-Y\arg\omega\). Its difference from \(-\pi|Y|/2\) is at most
\(X\), cancelling the \(-X\) in the exponent. The branch of
\(\log\Gamma\) may be chosen analytic in the right half-plane and
real on the positive real axis, and the modulus conclusion is
branch independent. The Euler formula at \(N=1\) gives
\(|\zeta(s)|\le |s|(1/|s-1|+1/\Re s)\), which is less than \(3|s|\)
on (5). [DLMF 5.9.10_2](https://dlmf.nist.gov/5.9#E10_2) ·
[DLMF 25.2.8](https://dlmf.nist.gov/25.2#E8) ·
[Import record][imports]

The modulus factor in (8) starts from \(1/16\), the combined
normalization of \(\xi\) and \(H_0\). Since
\(g e^{-\pi |Y|/2}\le e^{(\pi/2)(1/2+\sqrt t)}<4\), the
constant multiplying the cubic and power terms is at most \(27/8\).
The upper power \(1/4+(4/25)|\nu|\) is positive. Hence the power
bound also works when \(X-1/2<0\), using \(|\omega|>1\).
An exact rational check verified the finite exponential sum through
order 24 exceeds 3505, \(27\cdot7010^3<10^{13}\),
\(3505<8^4\), and the linear and added quadratic bounds are
strictly below \(131/100\) and \(1/10000\). The exponential-series
tail used for \(e^{1/3}\) gives \(1+1/3+1/16<7/5\), with
\((7/5)^4<4\). Thus both Cauchy use of \(M_2\) in the stated disk
and the Gaussian strip estimate have the displayed constants.

For (9), multiplication by \(h\) in the periodization cancels the
\(1/h\) in its Fourier coefficient. The contour shifts for the two
frequency signs yield \(e^{-2|\omega|}\) and the strip majorant gives
uniform convergence of the periodization on one period. Absolute
summability of the Fourier coefficients then permits evaluation at
zero. The first alias frequency is \(2\pi/h\), yielding
\(e^{4\pi/h}-1\) in the denominator. Each shifted-line \(L^1\) bound
uses two half-lines, each bounded by a complete Gaussian. At either
fixed step the first omitted node is \(12+h\) on the positive
half-line. Monotonicity pays the tail by integration from \(12\), and
the slope of its tangent there is \(-(24\alpha-\beta)<0\).
Dividing both allowances by \(\sqrt\pi\) yields (10). An ordinary
floating substitution gives \(0.14226079\) and \(4.96112075\cdot10^{-7}\)
for the two steps, with shared truncation term \(9.80898803\cdot10^{-45}\).
These reproduce the stated scales. The exact expressions in (10)
are the error contract for an exact lattice sum.

## Contour and time interfaces

- The log of \(G_t/w^2\) exists on a collar because its winding is
  zero. The moment integration by parts uses \(dz=iw\,d\theta\) and
  gives the minus sign and factor \(k\) in (11). Conjugation of the
  counted divisor gives real moments and coordinates. Newton's
  identities give the squared half-separation in (11) with
  multiplicities included.
- The quotient \(G_t/Q\) is holomorphic and nonzero throughout the
  closed disk under the count and collar hypotheses. The \(K\)
  residue evaluates its logarithmic derivative by divided difference,
  with \(B'(c)\) at a double zero. The \(Q'/Q^2\) term is a total
  derivative, and the integral of \(2/(wQ)\) vanishes as all poles
  lie inside and the decay is \(O(z^{-3})\). Integration by parts
  then gives \(+2w(z-c)L/Q^2\). Constants vanish in the exact
  averages, including the drift since its kernel times \(d\theta\)
  is proportional to \(d(1/Q)\).
- In the Rouché interface, take the holomorphic approximate field
  on a neighborhood of the **closed disk**. The exact finite
  lattice model is entire. A strict approximate modulus floor
  \(m>\delta\) simultaneously gives the count transfer and the
  branch difference bounded by \(-\log(1-\delta/m)\). This uses the
  uniformly convergent series for the logarithm of the analytic
  ratio on a collar, with the collar possibly shrunk. When using a
  collared log only as approximation data, (13)–(15) use its branch
  error directly. Such log data alone do not imply a disk count.
- The common buffer gives \(|Q|,|\widetilde Q|\ge b^2\),
  \(|z-\widetilde c|\le 2\rho-b\), and the \(J\) bound for the
  difference of the pair polynomials. The difference of squared
  reciprocals is at most \(2J/b^6\), multiplying the difference of
  reciprocals by the sum. Together with the reciprocal-product
  derivative bound \(2/b^3\), this proves the constants in (15).
  The squared-center difference supplies \(2(\rho-b)e\) in (14).
  One true center bound suffices for the alternate coordinate
  estimate but the drift estimate still needs the common buffer.
  Check that buffer for the actual computed polynomial if
  projecting the approximate inputs to their real parts.
- For discrete means, the quadrature and arithmetic allowances
  must refer to the branch and kernel used in the actual sampled
  integrand, including any constant centering. A bound by two
  angular strip norms gives the stated alias estimate at \(n\)
  nodes when the integrand is analytic on the enclosed strip.
  Point samples alone supply neither the floor for the log error
  nor the strip and boundary bounds for its angular quadrature.
- Differentiating the contour moments and using heat gives the
  integral of \((z-c)G_t''/G_t\). Upon factoring \(G_t=QA\), the
  \(Q''/Q\) term contributes two, the cross term reduces to
  \(4B+4DB/Q\), and the holomorphic terms integrate to zero.
  Thus \(D'=2+4KD\) including at a double zero. With
  \(S'(t)=-4K(t)\), the derivative of \(e^S D\) is \(2e^S\).
  The integral from \(t\) to the incoming endpoint \(v\) gives
  (17) with the stated orientation. The all-time \(L^1\) error
  in \(K\), pointwise primitive allowance and separate outer
  time quadrature are required for (16). The absolute comparator
  uses the same pointwise error by the reverse triangle
  inequality. A negative lower numerator needs a positive lower
  denominator bound to transport it correctly.

## Controls and disposition

For the polynomial control \(w^2-2(t-1/20)\), the periodic
logarithm's first two moments give \(p_1=0\), \(p_2=4(t-1/20)\).
The drift integrand has purely negative Laurent powers and
zero mean. The whole-interval cost is \(1/5\) versus incoming
\(D(1/10)=1/10\). Starting at the double time makes cost and
incoming gap equal. This checks multiplicity, strictness and time
orientation even with a persistent count and buffer.

The Gaussian transform and local contour identities can also apply to
changed sources with the required integrability and counted geometry.
The xi-specific allowance uses the unchanged complete theta density
and completion. The Euler translates change the arithmetic, weighted
squares fail the full reflection/unit-coefficient conjunction, and
smooth reflected or primitive-compatible sources lack the literal theta
square expansion. Finite-prime and finite-score agreements leave full
canonical identities unpaid. Finite-profile threshold controls lack the
full theta data and eventual simplicity in their recorded classes.
The normalized endpoint control retains its RH premise and changes
ordinary Dirichlet arithmetic. Kernel changes and measure relaxations
fail the literal evolution or complete divisor requirement,
respectively. These distinctions neither test an unproved cost sign for
each noncanonical family nor broaden their recorded exclusions.
[Collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md) ·
[Scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md)

The complete-source consumer does not use an exterior inverse-square
estimate. The sibling OA stop was based on unavailable positive-time
acquisition and the lower-force direction from an upper exterior-sum
allowance. Those premises remain separate. Neither the frozen oracle
proof nor this assessment certifies a Lehmer tube or a positive
canonical signed-cost margin. [OA decision08][oa]

[request]: ../research-progress/handoffs/VCD-GT-E05-r5.md
[note]: ../notes/12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md
[decision]: ../brainstorm/notes/04_VCD_GT_B04_CANONICAL_LEHMER_ACQUISITION_20261116.md
[imports]: ../references/02_VCD_GT_XI_QUADRATURE_BOUND_SOURCES_20261116.md
[lehmer]: ../references/01_VCD_GT_LEHMER_SOURCE_USE_20261116.md
[oa]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/03_collision_constraints/notes/08_TND_OA_B03_LEHMER_DIRECTION_AND_ACQUISITION_STOP_20261109.md
