# Two-time limits and Vandermonde: same-assistant assessment

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**.

**Review scope:** same assistant rechecked the derivations, source imports,
floating diagnostics and status wording. This is not independent,
specialist, interval-arithmetic, or formal review. The sources are
[Note 11][negative], [Note 12][positive], and the [execution record][data].

## Conclusions supported by the written proofs

1. Negative time now has an all-real-height estimate. The source Taylor
   remainder is bounded before taking its Fourier transform, so it does
   not grow with x. The explicit constant B_2 bounds the entire source's
   second derivative, including every theta index. The exact Gaussian
   density retains epsilon in its denominator. The absolute error is
   O(T^-3) uniformly for |y|<=A sqrt(T), with explicit constants; the
   rescaled profile T^2 rho(-T,sqrt(T)z) has O(T^-1) error on every fixed
   transverse strip and all real rescaled heights. Fixed physical points
   still have the earlier T^-3 regularization background.
2. Positive time has a sharper complex carrier comparison. The remainder
   and carrier have matching exp(mu |y|) growth. Cancelling it in the
   Rouche comparison removes the older artificial exp(mu Y) cost.
   Counting only disks that can meet the averaging support removes the
   whole-population factor from the local density error. Full-source
   weighted moment bounds then give R=L k_h/pi+O(kappa^-1/2+L^-3)
   for centers whose buffers fit in X~kappa^(1/3). Here L is the explicit
   large saddle and kappa~8tL. This is an absolute physical-density
   estimate at fixed epsilon, followed by a stationary-shape interpretation.
3. For every consecutive block of m<=2N~(2/pi)L kappa^(1/3) enclosed
   zeros, the squared Vandermonde divided by
   (pi/L)^(m(m-1)) product_(k=1)^(m-1)(k!)^2 tends to one. The explicit
   logarithmic allowance includes both individual gap perturbations and
   the m(m-1) cost of replacing mu by L. The rescaled inverse-square
   Laplacian satisfies dimension-uniform positive-semidefinite bounds.
4. A nonzero global uniform positive-time clock limit is impossible for
   fixed epsilon, bounded transverse averaging support, and horizontal
   windows that escape to infinity at each fixed t. The field and first
   derivative vanish there. This does not exclude another outer profile,
   changed transverse scaling or a different regulator protocol.
5. The finite xi-derivative hierarchy has a global absolute density
   remainder bounded by 2^(-N-1) times a completely specified source
   majorant. A degree O(t log^2 t) gives a chosen inverse-power tolerance
   at all real heights on a fixed transverse strip. This is a conservative
   existence/construction bound, not a practical computation or simple
   stationary asymptotic. The numerical record does not evaluate it.

## Sensitive points checked

- The coefficient polynomial for Phi'' is b^2-(8b+16)a+16a^2. Its
  absolute majorant gives the 75,330,224,32 coefficients in Note 11.
  The n-tail uses powers no larger than n^8 after n>=2.
- The global density stability estimate works at zeros and uses fixed
  epsilon. Its constants are not uniform as epsilon tends to zero.
- The all-height negative-time conclusion comes from an analytic L1
  bound; the finite height sample grid is only a diagnostic.
- The weighted DS8 extension covers the Gaussian mass below the source
  half-line and the far-left source interval. It also retains the source
  normalization. The signed mean error e_mu=O(kappa^-3/4) is essential:
  the weaker O(kappa^-1/2) estimate would not make the growing-block
  Vandermonde's L-versus-mu error vanish for X~kappa^(1/3).
- The lower bound e^(-s)sin s>=s/2 is used only for s<=1/2.
  The disks remain inside the rectangle and are disjoint. The outside
  lower bound and quotient lower bound pay the regulator transfer.
- The local disk count is an upper bound even for disks intersecting a
  kernel edge. The Laplacian is applied to the kernel as a function of
  integration coordinates with the observation's widths frozen. This
  does not authorize dropping variable-filter derivatives in a PDE.
- The discriminant has a square, hence the factor 4e in the logarithmic
  error. Its normalization has exponent m(m-1). The inverse-square
  matrix scales oppositely to distances; the factor in Note 12 (20) is
  (mu/L)^2. The constant zero mode remains zero.
- The clock description does not delete the exterior force or the
  unfolding derivative in HDC Note 09. It is a slice theorem. No
  backward terminal-to-initial stability has been inferred.

## Floating diagnostics and their limits

The script uses NumPy and the standard library, with its hash and
versions in the record. At epsilon=1e-4, the four-term derivative
majorant is about 616.747, with formula tail allowance about 1.03e-25.
That decimal is not an outward-rounded enclosure.

Negative samples use xi in [0,12] at 49 points and upsilon=0,.5,1.
For T=1e6,1e8,1e10 the largest observed Gaussian density errors are
1.13e-11,1.91e-16,2.91e-22; the corresponding formula allowances are
1.78e-6,4.31e-14,2.58e-20. Both source quadrature orders were compared.
The uniform strip theorem includes negative heights by symmetry and
heights outside that finite sample by its proof, not numerical sampling.

The conservative complete-source saddle gates fail at the sampled
t=1024 and 1e4; those failures remain in the record. The actual-moment
floating carrier gates pass there, which is different evidence. The
conservative formulas pass at sampled t=1e6,1e9,1e12, but none is a
certified numerical onset or continuous-time enclosure. The growing
block log-Vandermonde allowance is still about 2.07 at t=1e12 for the
largest allowed block: the eventual relative asymptotic is not presented
as a tight finite-time estimate at those parameters.

Four source-contour comparisons at t=1e4 and 1e6 include centers as
large as x=223.30. Absolute weak zero-intensity discrepancies from L/pi
are at most 7.90e-6; contour refinements change values by at most
2.33e-11. They measure the zero-measure observable. Finite-epsilon bias
is covered by the analytic transfer, not directly measured by peak
sampling. Theta roots were not fitted. The determinant/matrix checks
use perturbed integer lattices of sizes 8,32,128 and check the algebra;
they are not observed theta determinant data.

The fallback degree bound requires N=406877 already at t=1024 for an
absolute tolerance 1/1025 on |y|<=1.25. This documents its cost rather
than hiding it. No xi derivatives of that order were computed. A separate
atomic cosine control uses epsilon=.5, has a nonzero truncation error,
and passes the generic stability allowance; it is not a theta test.

## Control and status audit

The Hermite and stationary sine controls retain their distinct
equilibria and complete exterior-force laws. Smooth nearby source
controls may share leading asymptotics and still collide. Euler-factor,
weighted-square, reflected and primitive-compatible controls fail the
unchanged source premises as recorded in the notes; the generic stability,
Rouche and matrix estimates are not claimed to exclude collisions.

HDA-03 and HDA-04 advance within partial status. HDA-02 gains a growing-
domain analytic transfer, but no numerical interval certificate. Full
fluctuation/current derivatives, positive outer-height asymptotics and
the mixed-sign boundary solve remain open; HDA-07--09 stay gated.

[negative]: ../notes/11_TWO_TIME_LIMITS_ALL_HEIGHT_ERROR_20261024.md
[positive]: ../notes/12_GROWING_HEIGHT_STATIONARY_CLOCK_AND_VANDERMONDE_20261024.md
[data]: ../numerics/TWO_TIME_LIMITS_ROUND3_20261024.json
