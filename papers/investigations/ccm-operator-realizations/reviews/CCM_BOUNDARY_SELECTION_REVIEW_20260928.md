# Review of CCM boundary selection and complement analysis

Date: 28 September 2026. Prepared for Edward Baker with LLM assistance.

Model: GPT-6 (Codex); exact serving variant and reasoning effort were not exposed. Two analytic agents reviewed each other's derivations, a numerical agent reviewed the diagnostic claims, and the lead agent checked the synthesis. These are separate readings within the same model context, not independent human refereeing or formal verification.

## Disposition

The [main continuation](../notes/CCM_BOUNDARY_SELECTION_AND_COMPLEMENT_20260928.md) supports a restricted selection theorem and several precise limitations of extrapolating it. No substantive error remained after the checks below. It does not establish a true-ground overlap lower bound, a simultaneous rank/support theorem, a positive infinite complement, or RH.

## Boundary-selection checks

The [boundary note](../notes/CCM_DERIVATIVE_BOUNDARY_SELECTION_20260928.md) uses ordinary derivatives before hard restriction; it does not confuse them with distributional derivatives of a cutoff, which would add endpoint terms. These restrictions belong to the logarithmic multiplier operator domain.

The first theta summand gives
\[
k_1''/k_1=4t^2-22t+33/4+6/(2t-3),\quad t=\pi e^{2x}.
\]
This verifies the two scaled profiles. Their L1, L2, and variation estimates control the gamma logarithmic remainder, including low scaled frequencies and both boundary packets. The leading matrix
\[
\begin{pmatrix}1/2&-9/4\\-9/4&85/8\end{pmatrix}
\]
has determinant 1/4. Prime and pole terms are lower order on this fixed family with its exponentially localized tails; they are not discarded on arbitrary vectors. The generalized Gram matrix and the energy Schur calculation give the stated coefficient and smallest trial eigenvalue. The error estimate is made in the cancellation-adapted basis, so it remains meaningful for the small direction.

The fourth-derivative expansion has leading ratio \(16t^4-240t^3+934t^2+O(t)\). The explicit three-profile combination cancels the first two boundary terms and has energy \(O(h_b/A^4)\). The assertion is about reoptimized energy; it does not identify the correction on the old two-dimensional Ritz vector.

The fixed-rank extension was separately checked. The boundary-jet matrix tends to the Vandermonde matrix on \(0,4,\ldots,4(m-1)\). Its inverse is controlled for each fixed m. The Taylor remainder, after multiplication by the theta tail, is \(O_m(A^{-1})\) in the required profile norms. The resulting moment matrix is positive definite. Constants depend on m, and no uniform-rank assertion is implied.

## Complement and density checks

For a finite-dimensional S in the operator domain, the cross blocks are bounded. Subtracting them identifies the operator represented by the form compression to its complement and justifies
\(\|W-(0\oplus D)\|\le2\|W|_S\|\). The direct negative-test estimate preserves any fixed negative direction when the all-input residual tends to zero. The same reasoning covers growing rank only if that uniform residual hypothesis is proved.

Dimension counting with additional independent approximate-null vectors supplies actual near-zero spectrum in every fixed-rank complement. Without positivity it does not locate those values at the bottom.

The [form-core proof](../notes/CCM_COMPLEMENT_DENSITY_AND_WEIGHTED_GAP_20260928.md) correctly uses the logarithmic form topology. Compact smooth functions are dense by inward dilation followed by mollification. A continuous functional annihilating all restricted even derivatives defines a compact-support distribution. Analytic translation in the strip \(|\operatorname{Im}a|<\pi/4\), followed by Fourier uniqueness, makes that functional zero. This supports fixed-support Rayleigh convergence. It does not support interchanging rank and support limits.

Combining the core theorem with fixed-rank eventual positivity gives a meaningful counterfactual: if RH fails, the minimum derivative rank detecting a negative direction must grow with support. No fixed-rank boundary-selection theorem can exclude that branch.

## Weighted jump form and normalization

The literal kernel in the programs has \(\widehat k=\Xi/4\), as proved by its Mellin integral. A separate numerical integral gave \(\int k/\Xi(0)=1/4\) and \(\int k\cosh(x/2)=1/8\), consistently with the exact calculation. The two earlier scalar statements were corrected; their annihilator and normalized conclusions are invariant under this correction. The real-zero-division illustration was rescaled consistently; the separate off-axis witness construction, defined using Xi itself, was preserved.

The positive-k identity retains the pole subtraction. In the general case it is
\[
Q(ku)=\mathcal E(u)-2M\operatorname{Var}_\mu(u)
-2|\textstyle\int u\,d\nu|^2,
\]
where the variance is the unnormalized integral against μ. The last term vanishes for even u; since M=1/8, the remaining threshold is 1/4. This factor and the gamma/prime jump factors were checked directly by symmetrization.

Jump measures do not charge either-coordinate μ-null sets, including the prime-shift measures. The almost-everywhere subsequence argument and Fatou's lemma justify closability. Cutoff approximation of constants and the derivative-ratio functions justifies the operator interpretation of their threshold eigenvalue. The threshold eigenspace alone does not exclude lower spectrum.

For a fixed finite prime list, narrow even pairs of normalized bumps escaping to ±R give variance tending to one and jump energy tending to zero. The gamma estimate splits short, medium, and long jumps; the finite shifts are bounded by the far theta tail. This establishes zero gap for the transformed whole-line truncation. The conclusion does not concern the original finite-window Weil prime sum: deleting long jumps from the transformed form also deletes diagonal terms used in the annihilator cancellation.

## Numerical checks and presentation corrections

The [diagnostic](CCM_DERIVATIVE_CLUSTER_DIAGNOSTIC_20260928.md) constructs projected analytic derivatives independently of the eigenvectors, includes integration-by-parts endpoint terms, and tests them against derivative quadrature. It uses the mass \(I+Z^*Z\) in the harmonic-lift pencil. The conditional eigenvalue bracket has the required full positivity and complement hypotheses and makes no unsupported angle claim.

The 130/160-digit runs agree in all retained observables at the 45-digit serialization precision, excluding precision and roundoff-check fields. The generator and its two repository dependencies are hash-bound. This is multiprecision consistency, not interval certification. Reference grounds are described as numerically computed, and no trend is inferred from two cutoffs at the same support.

The very accurate finite harmonic lift uses the entire finite complement inverse. It demonstrates that the correction matters, not that the correction has been analytically controlled. Its cancellation scale is a whole-block norm ratio, not a certified relative error for the smallest eigenvalue.

## Remaining obligation

The new work establishes how a prescribed arithmetic trial space selects a Xi-like vector and why this can happen without RH. The missing step remains quantitative control of growing rank and the complement, or the exact global weighted jump inequality. Further finite exact elimination without a signed remainder would not discharge that obligation.
