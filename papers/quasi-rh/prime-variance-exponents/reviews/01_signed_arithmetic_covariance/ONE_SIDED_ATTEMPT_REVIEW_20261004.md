# Internal review: the one-sided arithmetic attempt

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not inferred. Coordinating proof checks
and separate same-model cross-reviews; not independent specialist
refereeing. No global fixed power saving or mathematical priority claim.

## Scope and result

Reviewed the [investigation summary](../../notes/programs/01_signed_arithmetic_covariance/ONE_SIDED_ARITHMETIC_ATTEMPT_20261004.md),
[density-centering derivation](../../notes/programs/01_signed_arithmetic_covariance/PRIME_DISCREPANCY_CENTERING_20261004.md),
[actual-coefficient sign test](../../notes/programs/01_signed_arithmetic_covariance/SIEVE_SIGN_TEST_20261004.md),
[analytic sign tests](../../notes/programs/01_signed_arithmetic_covariance/ONE_SIDED_SIGN_GATE_20261004.md),
and both new exact checkers and small records. The fixed-probe properties,
scalar detector and classical PNT input are inherited from the preceding
notes and source audit; they were not independently reproved in full.

The new unconditional result is a power-small elimination of the
continuous prime density and its cutoff boundary from the complete scalar.
The one-sided inequality for the remaining correlation is still open.
No checked reduction or negative test is described as proving it.

## Density, endpoint, and cutoff checks

- Verified ell'=2ell/v+[w(v)−4w(v/2)]/v; C^5 regularity and finite
  D^7 ell follow from the established C^4 probe with finite D^6 w.
  H=int_v^infinity ell and f=H/v have compact support and finite D^8 f.
  Preparation is essential for H to vanish below A.
- Rechecked int f=int ell log=q c_w, the minus sign in the divisor
  expansion, the extension across m<=U under U²<=AX, and the lattice
  constant 2 zeta(8)/(2 pi)^8=1/1209600. The total density error is
  N^(−8) sum_(d<=U)d^7=O((U²/X)^8), N=X/U.
- Rechecked Stieltjes integration by parts over (U,infinity), using
  right-continuous E(U) when U is prime. The boundary sum uses the
  zero ordinary moment and D^7 ell, giving O((U²/X)^7) after the
  elementary |E(U)|=O(U) estimate. It is not silently set to zero.
- Checked the minus sign in J_0=−I/q+error, the lower integral limit
  mU/X, the terminal band m>AX/U, and all-real-X quantifiers. The
  exchanged-sum formula I=int E(t) K_(X,U)(t)dt retains those caps.
- Checked the scalar Type I error X^(−7)U^7(1+log X), mixed error
  X^(−7)(UV)^7, and u+v<=1−kappa/14 for fixed positive u,v.
  This is not claimed to improve the norm approximation.
- At U=V=X^(1/2−kappa/28), checked the density exponent −4 kappa/7,
  endpoint exponent −kappa/2, and inner-prime-power threshold
  kappa<14/29. For kappa=.01, the cutoff exponent is 1399/2800
  and the factor-ratio exponent is 1/1400.

The arithmetic sign-test agent separately checked the centering proof,
its derivative gains, endpoint signs and cutoff exponents. No actionable
mathematical defect was found. The available quantitative PNT envelope
and the absolute divisor sum supply every logarithmic saving only.
The centering agent also reviewed the final summary's equivalence range
and exchanged-sum kernel. Its small correction to state U>=1 explicitly
was incorporated.

## Actual sign obstruction checks

Checked A_U(m)=sum_(k|m,k<m/U)mu(m/k), including equality in the
sufficient condition P^−(m)>=m/U. Comparable r-prime outer factors
of size X^(1/2), paired with an inner prime of size X^(1/2), have
A_U(m)=(−1)^r in the stated exponent ranges. All outer primes lie
below U; the inner prime is uniquely above U. Consequently grouping
equal products cannot cancel the constructed contributions.

The zero ordinary moment and nonzero logarithmic moment prove both
lobes of the actual ell exist. Disjoint fixed-ratio prime boxes inside
each lobe have weighted count asymptotic to a positive constant times
X/(log X)^r. For r=2, both grouped scalar masses are at least a
fixed multiple of (log X)^−2. With the inherited all-log estimate for
J_0, the exact-continuum sign-deletion majorant and minorant fail every
fixed-power target. This conclusion does not assert that every sieve
method fails.

The extension to the new balanced cutoff was checked separately:
r=2 requires 1/4<u<1/2 and r=3 requires 1/3<u<1/2. Both hold for
u=1/2−kappa/28, 0<kappa<14/29. Scalar Vaughan and prime-power
errors remain power-small, preserving the all-log estimate used here.

## Analytic sign checks

The centering agent separately reviewed the hypothetical-zero oscillation
proof. The nonnegative-tail Landau step yields true absolute convergence
for Re z>beta without assuming a rightmost zero. The inequality
|F(sigma+i gamma)|<=F(sigma) then compares residues and gives both
scalar amplitudes at least m_rho |D(rho)|. Multiplicity, the entire
initial cap, and the analytic real point beta are retained. Transfer to
the complete Vaughan scalar holds for beta>1/2, and to the original
prime-inner scalar for beta>37/48.

Checked the cosine counterexample to an inference from real-axis
transform positivity. Checked both moments under fixed positive log
averaging, the possibility of multiplier zeros on a positive real-part
line, and the detector-preserving exponential-density example. The
removable multiplier value at z=−a is made explicit. The pointwise
majorant statement specifies compact support in the positive half-line;
a strictly larger fixed majorant has a nonzero prime-density limit.
No general impossibility theorem for adaptive averaging is asserted.

## Executed checks and limitations

The coordinating agent replayed both new scripts successfully:

- [Centering checker](../../numerics/01_signed_arithmetic_covariance/check_prime_discrepancy_centering.py):
  386 exact comparisons over 32 rational cases. Deliberately omitting
  the boundary fails in 28 cases. The polynomial kernel and prime
  weights p are synthetic; the actual log weights and fixed-probe
  derivative constants are not numerically certified by this test.
- [Smooth-sign checker](../../numerics/01_signed_arithmetic_covariance/check_smooth_sign_obstruction.py):
  81,043 exact finite arithmetic comparisons, including rational and
  algebraic cutoffs, the strict endpoint, and unique-large-prime grouped
  coefficients represented by formal log-prime dictionaries.

Total: 81,429 exact comparisons. Both analytic asymptotic claims and
their finite checks have explicitly separate scopes. No outward enclosure,
zero computation, fitted exponent, effective asymptotic onset, or
uniform finite-X power certificate is claimed.

No manuscript source or compilation record changed. No third-party paper,
sieve array or Gram matrix was stored. All results are saved in the
working tree; no commit or publication was made.

Final artifact checks passed across all 51 changed/new project files:
local Markdown links resolve, math delimiters balance, Python sources
parse, and `git diff --check` is clean. Both new exact-check records
replay identically and their source hashes match. Every changed/new file
is below 1 MiB; the largest is below 28 KiB.
