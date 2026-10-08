# Review of the initial exponent descent investigation

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Review type: separate same-model derivation and cross-checks, followed by
integration review. This is not independent specialist refereeing or
formal verification.

## Scope and conclusion

The package contains four research notes, a small exact-arithmetic script
and record, an overview, and a concise history index. The results are
conditional on the explicitly cited parent-project theorems or imported
published theorems where indicated. No actual-prime contraction, new zero
strip, or proof of quasi-RH implying RH is established.

The review found no outstanding mathematical error in the scoped
calculations. The central open step is a signed arithmetic estimate with
a genuine power gain. The source papers' full proofs and the inherited
prime-variance manuscript were not independently replayed in full.

## Fixed multiplicative scale criterion

The [descent note](../fixed_scale_descent/notes/1_FIXED_SCALE_DESCENT_CRITERION_20261008.md) received
a separate check of the normalization
\(\|F_X\|_2^2=X^{-2-\delta}\mathcal V_g(X)\), the arithmetic difference
profile, and the signed norm identity. Iteration to a compact initial
range works for all real \(X\), not only a geometric sequence. The three
geometric-sum cases yield the stated power, including the logarithm when
the contraction rate equals the forcing rate.

Applying a strict improvement at the attained optimal exponent is valid
without assuming that any zero attains the spectral edge. The note
correctly treats the arithmetic recurrence as a sufficient unproved input.

## Spectral edge and subpower improvements

The [spectral note](../fixed_scale_descent/notes/2_SPECTRAL_EDGE_AND_LOG_SAVINGS_20261008.md) was
checked against the parent's absolutely summable zero expansion. The
weighted shell substitution has exponent \(2+D\); nonedge terms vanish
by dominated convergence, and Fourier averages isolate each nonzero
boundary residue. This proves the little-o criterion for \(0<D<1\).
The normalized Cesàro-energy identity follows by absolute double-series
summation and distinct frequencies, with multiplicities combined first.

The symmetric model has no finite spectral accumulation, nonzero probe
coefficients, a normally convergent meromorphic Laplace series, and
stretched-exponential decay after removing the optimal power. Its
nonzero poles prohibit every smaller variance power. The note explicitly
does not claim Euler-product structure or the full zeta zero density.

## Arithmetic feedback and the moving cutoff

The [arithmetic note](../fixed_scale_descent/notes/3_ARITHMETIC_FEEDBACK_AND_RESONANCE_20261008.md)
was checked by a separate agent against the parent centering, mixed
feedback, scalar detector, and Vaughan identities. Replacing the prime
counting error by \(\psi(t)-t\) retains higher prime powers and preserves
the density cancellation and increment calculations. At \(U=X^{11/24}\),
the scalar errors have exponents \(-91/24\), \(-7/12\), and \(-2/3\),
so their sum is \(O(X^{-7/12})\).

The resulting Mellin error is holomorphic for \(\Re z>5/12\), leaving
the original residue \(-m_\rho D(\rho)\) at each forbidden zero. The
argument retains the finite initial cap and does not substitute a moving
cutoff into an identity proved only for fixed cutoffs. The delay factors,
filtered probe multiplier, and logarithmic continuum moment were checked.
A definition of \(c_w\) was added for clarity.

## Newman flow and the explicit kernel

The [Newman note](../newman_collisions/notes/1_NEWMAN_FLOW_AND_COLLISION_SCOUT_20261008.md)
received a separate check of the compactness argument, Bessel spectral
proof, positive-kernel construction, threshold argument, and rescaling.
Polymath's uniform positive-time cutoff is essential: pointwise finiteness
of nonreal zeros alone would not justify compactness as time varies.
The proof now states \(\Lambda\le1/2\) explicitly before applying the
cutoff theorem in its prescribed time range.

The collision expansion follows from real Weierstrass preparation and
the heat equation. The general de Bruijn theorem's symmetry, decay, and
integrability hypotheses are checked for the constructed kernel and its
Gaussian multiples. The positivity certificate and monotonicity
polynomial were checked algebraically; the two ranges \(1\le c\le8\)
and \(c\ge8\) prove monotonicity. The general-kernel counterexample is
explicitly separated from zeta and actual prime arithmetic.

The primary source statements checked in this session were
[Polymath, Theorem 1.5 and Proposition 3.1](https://arxiv.org/html/1904.12438),
[Newman–Wu, Theorems 7, 13 and 14](https://arxiv.org/html/1901.06596), and
[Gasper's real-zero result for the Bessel transform](https://arxiv.org/abs/0801.2996).
The stronger strip theorem's real-zero count condition is stated explicitly.

## Reproducible finite checks

[check_initial_identities.py](../numerics/check_initial_identities.py) ran
successfully with Python 3.10 and standard-library exact rational arithmetic.
The [retained record](../numerics/initial_identity_record_20261008.json)
contains the fourth derivative polynomial, positivity and monotonicity
identities, quartic-root check, three recurrence regimes through 32 steps,
the factor-scale counterexample, and the scalar remainder exponents.
These checks support only those finite algebraic identities.

All local links were checked against the intended repository destination.
The package has no large derived files or copied third-party PDFs. It
introduces no manuscript snapshot and makes no release or publication claim.
