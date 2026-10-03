# A certified first-window relative comparison

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort are not exposed and are not inferred. The analytic argument and outward computation received separate same-model checks. Specialist review remains outstanding. Repository baseline: c943006b5003dad7ac48afc7689e7273f30c267a.

The continuation establishes a rigorous way to accommodate positive correction directions at the first-prime window. For every smooth prepared mean-zero source supported in (-1/2,1/2),

\[
\boxed{Q[F]\ge\frac9{100}\|F\|_2^2,\qquad
Q[F]\ge\frac1{9000}B[F].}
\]

In particular, the explicit revised main term B_new=B/9000 gives

\[
\boxed{Q[F]=B_{\mathrm{new}}[F]
+\left(\frac{8999}{9000}B[F]-K[F]\right),}
\]

and both terms are nonnegative. The source class includes both parities and arbitrary complex sources. The preparation is F=(-d²/dx²+1/4)h with compact smooth h and integral h=0; equivalently F has zero mean and zero exponential moments at plus and minus one half. This is a full-source-space statement, not a finite trial-space result.

## What closed the local comparison

The [arithmetic coercivity proof](LOCAL_COERCIVITY_LOW_BAND_20261003.md) bounds the negative part of the multiplier gamma(t)-sqrt(2)log(2)cos(t log(2)) after the exact moment projection. Its support is contained in |t|<46. A 40-coordinate Legendre calculation encloses the resulting finite matrix below 0.9 times the identity. Analytic bounds retain every omitted source mode and the midpoint integration error. The total error is below 0.008253, leaving the conservative norm gap 0.09.

The [outward generator and records](../numerics/local_weil_gap_20261003/README.md) passed at 192 and 256 bits. Their numerical matrices are regenerated rather than saved. The proof uses the standard digamma series and Legendre integrals, with primary references and all constants recorded in the derivation.

The second ingredient is a new simple bound from the exact crossing factorization:

\[
X=P C_F^*1_I C_F\chi,\qquad
\|X\|_1\le\frac{|I|}{2}\|F\|_2^2.
\]

It yields |K[F]|<=772||F|| squared at length one, using the freshly replayed inherited boundary gap. Therefore

\[
B[F]=Q[F]+K[F]
\le\left(1+\frac{772}{0.09}\right)Q[F],
\]

so Q>=9B/77209, which is slightly stronger than the simpler B/9000 statement. The small fraction is a conservative certificate, not an estimate of the optimal comparison constant.

## Relation to the proposed spectral modification

The earlier proposal subtracted the positive spectral part of the unweighted source correction, seeking B>=K_plus. That stronger inequality remains unproved. The completed result instead establishes the relative estimate K<=(8999/9000)B, which is sufficient to give an explicit positive revised main term and handles the infinitely many positive correction directions.

The [source-operator analysis](CLOSED_SOURCE_RELATIVE_COMPARISON_20261003.md) also establishes a closed realization of B, its logarithmic form domain, a positive fixed-window source gap, and a compact relative correction. It gives complete finite-block and resolvent tests that retain the complementary source space and mixed terms. These are useful foundations for the original spectral route; their general comparison tests are not claimed as completed numerical certificates.

The accompanying [finite source-space pilot](../numerics/revised_B_source_pilot_20261003/README.md) found positive revised margins in its tested matrices. Those calculations retain substantial unresolved state-space truncation error and do not certify B>=K_plus. They are not inputs to the successful arithmetic certificate.

## Scope and useful next target

This proves that the positive correction can be absorbed at L=1 on the prepared mean-zero class. It does not restore the false claim K<=0, remove the zero-mean condition, or prove the all-support Weil criterion. It obtains the comparison from an independent arithmetic estimate, so it is not a new derivation of arithmetic positivity from Sonin geometry. No literature-priority claim is made for local Weil positivity.

The next bounded target is to extend this certified relative comparison through the first new-prime threshold, with the support and prime set changed together. The low-band proof already isolates the three items that must be recalculated: the support-dependent moment projection, the active prime-power multiplier, and the full error budget. A proof for one further window would test how the certified margin changes. A general mechanism controlling all windows remains necessary for the wider program.

The [internal certificate review](../reviews/REVISED_B_CERTIFICATE_REVIEW_20261003.md) records independent checks within the same model family. The manuscript has not been revised; these developments remain in the research notes and numerical records.
