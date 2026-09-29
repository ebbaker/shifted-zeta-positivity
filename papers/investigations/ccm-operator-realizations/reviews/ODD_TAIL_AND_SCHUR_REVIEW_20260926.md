# Review of the odd-tail certificate and structured Schur reduction

Date: 26 September 2026.

Model: GPT-6 (Codex). Exact model variant and reasoning-effort setting are not exposed in this session.

Scope: same-agent adversarial review of [continuation round 4](../notes/CCM_ODD_TAIL_CERTIFICATE_AND_STRUCTURED_SCHUR_20260926.md), its rational certificate, closed-form numerical builder, and claim boundaries. This is LLM-assisted research for Edward Baker, not independent refereeing.

## Verdict

The infinite odd Fourier tail above mode 4096 at L=log13 has a proved lower bound 2/5 in the unshifted Weil form. The arithmetic constants and two witnesses for failure of a scalar Schur test are enclosed by exact rational computations. The finite-rank coupling expansion has an analytic bound on its entire infinite remainder.

The full odd-sector gap remains unproved. A positive compression on the high subspace does not control coupling to the low subspace. The note makes that limitation explicit, retains the ground-energy threshold, and does not invoke the previous conditional convergence theorem as if its missing hypothesis had been verified.

## 1. Fourier normalization and leakage

For the normalized sine basis on [0,L], direct integration gives the Fourier transform magnitude in (5). The full Plancherel integral is divided by 2*pi. After symmetry in the continuous frequency variable, the factor is 8/(pi L), not twice that number. Integrating sin-squared gives the numerator LT-sin(LT), which is bounded above by LT+1. The series sum over n>M is bounded by 1/M after extracting L^2/(4*pi^2). These factors produce (6).

The calculation estimates the Hilbert--Schmidt norm of the band projection on the whole high sine subspace. Consequently it controls combinations of modes, including coherent low-frequency leakage. Treating every zero-extended high sine mode as spectrally supported outside its discrete frequency would be false; the new proof does not make that shortcut.

The archimedean multiplier is twice the derivative of the Riemann--Siegel theta function, as required by the original form normalization. Its monotonicity in absolute frequency follows directly from the digamma series. The lower estimate allows the global symbol minimum to be negative. At the chosen split eta<1, so the direction of the bound using A=6 and a_*=-6 is correct.

## 2. Prime and pole estimates

Translations on a finite interval decompose into finite path fibers. Their maximum vertex count is ceil(L/h) almost everywhere. At an exactly integral ratio, the possible longer endpoint fiber is null and does not affect an L2 operator norm. In particular h=L gives a zero operator, so the prime power 13 is excluded from the norm sum rather than overcharged.

The prime sum uses the norm of a translation plus its adjoint. There is no missing factor of two: the path norm already includes both directions. The prime coefficient is log(p)/sqrt(p^j). The path lengths and resulting radical constants are checked by integer inequalities, and the remaining logarithms and square roots are enclosed rationally.

On odd functions, the pole term is negative rank one. Its restricted norm is twice the squared L2 norm of the projected sinh profile. Computing its sine coefficients gives precisely (10); the bound is on the full infinite tail. The proof therefore does not use the much larger full-space pole norm or omit a negative contribution.

## 3. The special-function enclosure is an analytic bound

The digamma recurrence is combined with a bound on the integral remainder, not a truncated asymptotic series with an unspecified remainder. The identity from DLMF 5.9.13 is rearranged correctly. The inequality for its kernel follows term by term from the hyperbolic power series and implies an absolute complex remainder at most 1/[12(Re z)^2]. It is valid after the four recurrence steps used at T=2700 and after the 64 steps used for the matrix witnesses.

For T=2700, the sum of the four recurrence numerators is 7, and the half reciprocal's numerator is 17/8. Their total is 73/8. Replacing each denominator by 1350^2 gives a lower bound in the required direction. The exact quarter-argument digamma value and elementary gamma<1 bound give a valid global floor -6.

The five loose rational constants in (11) combine to 2009/5000, leaving a strict margin above 2/5. No numerical optimization of T or rounding of a displayed decimal enters the proof.

## 4. Rational arithmetic audit

The certificate uses Python Fraction and integer square roots. Each arithmetic interval is rounded outward to multiples of 10^-40. Logarithms use a positive atanh series with a geometric remainder; pi uses an alternating-series Machin enclosure. Sine/cosine values are reduced by an integer multiple of the enclosed true 2*pi, then bounded by Taylor polynomials and explicit real-variable remainders.

During development, a denominator in the cosine remainder was changed to exact integer division so that no floating-point value enters the bound. The final interval constructor and remainder inflation reject float inputs, and running with disabled assertions is rejected. Final records were regenerated after these changes. The saved certificate and numerical source hashes correspond to these final versions.

The coefficient witness uses only two distant b-values, not an unverified 4097-mode matrix. Their digamma imaginary-part remainder is much wider than machine accuracy, but still leaves the off-diagonal value strictly below -1/20. The n=1 diagonal is computed from the defining odd autocorrelation through an independent closed expression. Its algebraic-series tail is bounded by a k^-4 integral. Its relatively wide interval still proves the required upper bound 1/1000.

This is a reproducible computational certificate for the listed inequalities, conditional only on the explicit analytic formulas and ordinary correctness of exact integer arithmetic. It is not a formal proof checked in a theorem prover, nor a certificate of the full spectrum. Source hashes bind the saved output to its program; they do not establish the mathematics by themselves.

## 5. Schur signs, domains, and the obstruction's scope

The off-diagonal map E has finite-dimensional domain and square-summable columns; the finite sine functions are in the Weil operator domain. The restricted high form is closed, and (1) gives its coercivity. This justifies the inverse of C-s and the completed-square formula for s<2/5 without treating an unbounded operator as a finite matrix.

The Schur correction is subtracted, and replacing (C-s)^(-1) by (2/5-s)^(-1)I increases that subtraction. Positivity of (16) is consequently sufficient. It is not necessary. The coercivity constant in (17) includes the inverse triangular map norm; just taking the smaller of the diagonal block constants would ignore the coordinate change.

The scalar-test obstruction is certified by two entries: ||E||>1/20 and A_11<1/1000. With h=2/5, the first diagonal of the scalar lower form is below -21/4000 at s=0 and stays negative for 0<=s<h. This proves that particular sufficient test fails. It does not prove an actual negative Weil vector, exclude a sharper high-block bound, or exclude the matrix Gram test. Negative thresholds are not covered by that obstruction and would require their own comparison with a certified even trial energy.

Using an even trial upper bound U is a legitimate way to retain the unknown energy shift: epsilon_infinity<=U, so W_- -U>=gamma I implies the desired gap. The note does not substitute a floating-point Ritz value for a certified U.

## 6. Infinite finite-rank remainder

The odd matrix identity (19) has been checked against the parity transform of the preserved Weil builder. Its geometric expansion has the exact remainder E_nm*(m/n)^(2q). Each partial term separates into a function of n and a function of m, giving rank at most 2q. The uniform coefficient bound |b_n|<2 holds for all n, not just sampled indices: the archimedean sine series is positive and bounded by its first term plus an integral, and prime/pole terms are bounded separately.

The Hilbert--Schmidt remainder estimate sums both m and every n>K. The power-tail integral starts at K, which is the correct upper-bound direction for a decreasing positive summand. Weakening the square-root factors leads to (26); the saved rank bounds are conservative and exact. No finite-window numerical residual is substituted for the infinite remainder.

For the actual 4096 split, using K=8192 leaves 4096 intermediate rows. They remain part of E, and the note does not discard them. The finite-rank Gram coefficients also require verified evaluation of convergent infinite sums. These are genuine remaining parts of the next certificate, not tasks already completed.

## 7. Numerical checks and limits

Both parity blocks from the new closed formulas agree with the old defining-distribution quadrature at N=4. The formula for the odd diagonal's non-exponential sum follows by differentiating the digamma series and uses the correct trigamma factor. The constant even mode is included, so the even Ritz comparison has not silently dropped it.

All 60 saved observables agree at all 45 retained significant digits between the 120- and 160-digit runs. Maximum identity residuals are below 8.12e-121 and 7.83e-161. Checks include the exact finite-rank remainder identity, finite windows against the analytic infinite bound, and inclusion of independent multiprecision values in the rational witness enclosures. Both runs share the same spectral implementation; this is not interval certification of their Ritz values.

The table's global cross-block norms are Frobenius norms, not claimed operator-norm equalities. The tiny coupling values concern the particular lowest Ritz direction. Their finite-window ratio to the finite gap is around one, illustrating why directional estimates matter without proving a uniform relative bound. The finite odd gap at N=64 remains a difference of two Ritz quantities and supplies no certified lower bound on the continuum gap.

## 8. Preservation and next gate

The earlier notes, reviews, numerical programs, and records are retained unchanged. New files are small source files and records; no dense large matrices, third-party PDFs, draft snapshots, commit, or release are added. The investigation and numerical indexes and concise milestone history are updated.

The next required result is a verified positive margin, or a verified failed direction, for the matrix Schur sufficient form with an enclosed even-energy threshold. If that sufficient form fails, the high inverse must be estimated more accurately before drawing conclusions about the underlying Weil operator. The previous determinant limit remains conditional until a genuine limiting odd gap is proved.
