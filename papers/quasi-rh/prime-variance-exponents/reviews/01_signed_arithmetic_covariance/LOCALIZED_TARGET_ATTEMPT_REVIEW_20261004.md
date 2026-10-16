# Review of the localized covariance analytic attempt

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred. Internal
same-model cross-review is not independent specialist refereeing. No new
global exponent or mathematical priority is claimed.

## Outcome and scope

The continuation establishes an unconditional frequency-tail estimate and
an equivalent finite central target. It does not bound that central target
at the required power. Two accompanying calculations identify the stronger
assumption in an uncentered short-interval variance method and preserve
exact arithmetic closure, including all edge corrections. The deterministic
mode diagnostic now handles arbitrary zero multiplicity with an affordable
lower-product remainder; it is still not an expansion of actual arithmetic
errors into zeros.

Reviewed notes:

- [Finite spectral target](../../notes/programs/01_signed_arithmetic_covariance/FINITE_CROSS_SPECTRUM_20261004.md).
- [Short-interval dispersion](../../notes/programs/01_signed_arithmetic_covariance/SHORT_INTERVAL_DISPERSION_GATE_20261004.md).
- [Arithmetic closure](../../notes/programs/01_signed_arithmetic_covariance/ARITHMETIC_CLOSURE_ATTEMPT_20261004.md).

The work continues from commit `62ac139771ae317f6e4b624765783c6856739d8f`
and the preceding uncommitted aggregated-kernel continuation. Those files
were preserved. No manuscript or certificate is revised, and no commit
or draft snapshot is created.

## Spectral estimate

The lattice kernel K_0(v)=sum_k ell(kv) is O(v^6), has support below C,
and has Mellin transform zeta(z)L(z). The preparation zero cancels the
pole at one, with nonzero continued value q c_w. Seventh-order Mellin
decay follows from the same inherited finite derivative measure, not an
assumption of infinite smoothness. Euler summation on Re z=1 gives the
required logarithmic zeta bound without any zero-free-region input.

Substituting the absolutely convergent Mellin inverse directly into the
high-divisor, prime-discrepancy expression preserves the strict lower
cutoffs and terminal endpoints. It is important that these high divisors
range over (U,V], not the complementary band (D,U]. The latter returns
only through the proved scalar comparison. The spectral formula contains
a signed product of transforms, not their absolute square.

The elementary mean-square proof bounds each off-diagonal exponential
integral by its reciprocal frequency separation. The resulting harmonic
sum is O((1+log V)(1+log(V/U))); replacing this with a crude length factor
would lose the useful bandwidth. The continuous density transform is
bounded by 2/|tau| on the tail and is included. Summing the dyadic tail
with the seventh-order multiplier gives the displayed two terms in (8).
With H=X/U^2 and T=H[log(2X)]^(4/7), both are O(X^(-kappa/2)).

The comparison sign is I_(D,U]=-q C_T+O(X^(-kappa/2)). Thus a lower bound
on the localized correlation corresponds to an upper bound on the central
spectral scalar. Both signs separately remain admissible. Neither the
finite cap nor the ratio coherence width removes any fixed frequency.
No claim about an arithmetic lower-product corner follows from a crude
upper bound that is larger than the target budget.

## Smoothing and arithmetic coupling

The prime-discrepancy weight has total variation O(epsilon_X/U), including
both band endpoint jumps. This yields the exact additive smoothing identity
with error O(epsilon_X h/U), rather than a bound losing the factor U/D.
The shifted means near U include atoms above U; they cannot be cut off.
The exact covariance and autocorrelation formulas retain those shifts.

The uncentered variance condition V_h=O(X^(-kappa)) would imply
|M(U)-M(D)|=O(U X^(-kappa/2)). All-real-scale iteration produces the
Mertens exponent delta=14kappa/(14-kappa), strictly larger than kappa/2.
Partial summation then forces the stronger zero-free half-plane. This
is a rigorously checked implication, not a claim that the variance is
false, nor a prohibition on every use of Cauchy's inequality. The
centered decomposition retains its coherent mean. Its weight is not
automatically mean zero by preparation.

The product-coordinate closure was checked by expanding both increments.
The density bracket is r/d-U-U log(r/(Ud)); the two low/high edges are
subtracted and the low/low term is added back once. The identity
mu*Lambda=-mu log is exact. In the prime-only version, the proper-prime-power
correction in the untruncated convolution stays explicit; a bound for a
different high/high sector cannot silently pay for it.

## Deterministic mode boundary and multiplicity

The primitive B_0(v)=q c_w+O(v^8) gives
F(v)=-(v R_ell''(v))'. The power-increment test has a triple zero at its
upper endpoint. Three integrations by parts therefore bound the omitted
product-cap integral by O(H^(-7)), using all endpoint terms; this improves
the previous O(H^(-4)) bound for that deterministic calculation.

The residue of the canonical Mertens mode at a zero of order r_rho is
paired with the corresponding logarithmic-derivative mode. Multiplication
by A(z)=z^2 zeta(z)L(z) cancels the reciprocal-zeta pole before the remaining
residue is taken. Distinct zeros give zero leading cross term; matching
zeros transmit -r_rho L(rho)X^(rho-1)/q. Differentiated cap errors carry
only fixed powers of log U. For any fixed finite set of nontrivial zeros,
they are O(X^(-4kappa/7) log^O(1)X), hence smaller than the target.
This does not justify an infinite zero expansion, a rightmost-zero
assumption, or neglect of the residual part of actual arithmetic errors.

The spectral and arithmetic notes were independently checked by the
parallel agents; the coordinating agent checked their normalization,
cutoff arithmetic, source scope, and common notation. No substantive
mathematical error was found. Minor Fourier-convention and constant-
dependence clarifications were incorporated.

## Finite verification

The [checker](../../numerics/01_signed_arithmetic_covariance/check_localized_target.py)
and [record](../../numerics/01_signed_arithmetic_covariance/localized_target_record_20261004.json)
contain 2,592 exact comparisons:

- 2,304 formal prime-log coefficient comparisons for convolution closure
  and its strict cutoff inclusion-exclusion.
- 12 rational cofactor/density comparisons.
- 180 smoothing, centering, total-variation and shifted-autocorrelation
  comparisons on 36 cases.
- 96 rational checks of the triple endpoint zero and three integrations
  by parts for a synthetic eighth-order primitive.

Negative controls detect 38 missing low/low corrections, 18 missing shifted
endpoint residuals, and 16 incorrect primitive coefficients. The additional
primitive test uses R(v)=v^8 and F(v)=-392v^6; it verifies exact algebra and
scaling, not the fixed-probe asymptotic constant. Source hashes include
both reused kernel modules. No large derived data is saved.

These checks do not certify Mellin inversion, the high-frequency inequality,
fixed-probe variation constants, actual-mode estimates, or a new global
prime-variance bound. Those analytic claims rely on the proofs and the
internal review described above. The remaining one-sided arithmetic
inequality is explicitly unproved.
