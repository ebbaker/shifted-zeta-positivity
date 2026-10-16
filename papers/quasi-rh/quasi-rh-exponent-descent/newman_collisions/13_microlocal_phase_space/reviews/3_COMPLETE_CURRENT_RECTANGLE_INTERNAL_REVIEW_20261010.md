# Internal review of the complete current and simple-zero rectangle

10 October 2026. Model: GPT-6 (Codex); the exact serving variant and
configured reasoning effort are unavailable and are not inferred. These
are internal derivation, arithmetic and agent cross-checks, not independent
mathematical review.

Reviewed [Note 3](../notes/3_COMPLETE_CURRENT_AND_PAID_SIMPLE_ZERO_RECTANGLE_20261010.md),
[the new checker](../numerics/check_complete_current_rectangle.py),
[its interval certificate](../numerics/COMPLETE_CURRENT_RECTANGLE_CERTIFICATE_20261010.json)
and [its build record](../numerics/COMPLETE_CURRENT_RECTANGLE_BUILD_RECORD_20261010.json).
The older notes, checker, certificate and build record are preserved.

## Result and scope

The genuine cutoff is complete: all 22066 terms are evaluated at
\(t_0=(2\log22066)^{-1}\), \(x_0=4\pi22066^2\), with the physical
spatial first derivative. At this center the relative-block current is
negative, the complement current is positive, the cross current is
negative, and the recombined complete current is strictly positive.
Both difference-phase and reflected sum-phase cross energies are separately
enclosed. A sign of an isolated block is not inserted into the full test.

The finite rectangle is
\[
 t_0\le t\le t_0+8\cdot10^{-6},\qquad
 x_0+0.3\le x\le x_0+0.4.
\]
The certificate places it in \(1\le\kappa\le2\), \(0<t<1/20\)
and proves its natural cutoff is always 22066. With the full imported
approximation and Cauchy payment included, its left endpoint is strictly
negative, its right endpoint strictly positive, and \(Q_t'>10.20\)
throughout. This proves one unique simple genuine heat zero for each time
and joint nonvanishing of \(H_t,H_t'\) on the entire rectangle. A separate
complete-current reverse candidate inequality also excludes collisions
there. It does not prove a current sign at all sector heights, a uniform
shrinking-sector theorem, a threshold fourth-jet sign, or RH.

## Derivation checks

1. The carrier phase is the principal-branch carrier at the integer height,
   not an adjustable phase. The complete sums are reconstructed from the
   same centered moments as the preserved Note 2 block.
2. The complete current recombination and the real-pair energy
   recombination agree by interval overlap. The energy includes both phase
   channels; the current alone is not called the observed real norm.
3. Spatial transport uses the exact equation
   \(q_n(x_0+h)=q_n(x_0)e^{-i\delta_nh/2}\exp\int r_n\),
   with \(r_n=\gamma_n+i\delta_n/2\). Its bound retains amplitude drift,
   carrier curvature, \(U,V,c,\Omega\), and the full normalizer dictionary.
   The frozen-frequency comparison is paid with explicit value and
   physical first-derivative residuals.
4. The time derivatives are at fixed physical \(x,N\). In
   \(\chi_n=q_{n,t}/q_n\), the \(\alpha_r\alpha_i/2\) phase term is
   included. The mixed derivative uses
   \(q_{n,xt}=q_n(\gamma_{n,t}+\gamma_n\chi_n)\); it does not omit
   the derivative of the spatial multiplier.
5. The midpoint jets retain the actual coherent signs. The sixth absolute
   frequency moment bounds both Taylor remainders on a real height
   interval, since each phase exponential has modulus one there. These
   real transport estimates are not substituted for a holomorphic error
   theorem off the real axis.
6. The genuine remainder uses the full complex-disk estimate of Heat
   Note 13, including normalization, reflection and cutoff change. The
   spatial Cauchy error is \(L\eta\), where each point supplies its own
   central disk. No derivative of the scaling curve or cutoff is taken.
7. On the real axis \(F=2\Re S\), \(F'=2\Re S'\). The holomorphic
   approximant off-axis is the reflected analytic sum. The proof uses
   \(A_t>0\) and nonvanishing; at a normalized zero
   \(H_t'=A_tQ_t'\). This establishes actual simple heat zeros, conditional
   only on the previously proved imported approximation interface.

## Arithmetic and replay checks

The new checker imports the unchanged Note 2 interval source only after
checking its retained SHA-256. A deliberate mismatched-source smoke test
was rejected before executing the substitute module.

The new computation uses a local override for nonnegative integer powers:
repeated directed multiplication of absolute endpoints, followed by exact
sign/parity restoration and explicit zero inclusion for even powers of
intervals crossing zero. This avoids depending on `Context.power`'s less
general C-implementation rounding guarantee. Forty-five exact rational
endpoint/parity inclusion tests passed. An internal agent also replayed the
pre-override computation with 32 exact endpoint-power checks and found no
actual inward power endpoint; the final certificate uses the stronger
directed-multiplication contract regardless.

The final complete interval replay passes its natural-cutoff, sector,
recombination, current, endpoint-sign, monotonicity, full-payment and
displayed-coarse-bound assertions. No ordinary binary float enters those
assertions. Pi, large arctangent, reduced trigonometry, logarithm and
exponential use the same explicitly enclosed mechanisms as Note 2.
Hashes identify the source, imported source and retained small certificate;
the arithmetic establishes the signs. No file requires an external large
archive.

The root agent and another internal agent checked the spatial residual,
time drift, Taylor remainder, holomorphic transfer and finite simple-zero
argument without substantive derivation objections. The arithmetic
contract concern above was addressed locally. These cross-checks do not
replace formal proof verification or independent mathematical review.

## Remaining checkpoint

The remaining arithmetic obligation is a uniform complete candidate-current
margin, or a complete paid threshold-jet inequality, on a specified
shrinking subsector. The actual finite rectangle validates the genuine
coherent calculation and its error scale. Its constants and signs cannot
be extrapolated to untested heights or \(t\downarrow0\).
