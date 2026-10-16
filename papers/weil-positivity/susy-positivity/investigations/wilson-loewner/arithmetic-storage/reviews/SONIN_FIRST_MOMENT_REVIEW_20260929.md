# Review of the first compressed Sonin moment

29 September 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed. Three parallel same-model readings checked the operator
reduction, numerical implementation, and implications. This is internal
mathematical and computer-assisted review, not specialist refereeing.

**Disposition: passes the internal checks.** The
[main note](../notes/SONIN_COMPACT_FIRST_MOMENT_20260929.md) and
[combined record](../numerics/records/sonin_first_moment_bounds.json) supply
the first certified actual compressed metric moment for the two prescribed
sources. The resulting first-prime trace intervals are materially narrower.
Neither complete arithmetic residual has a resolved sign.

## Mathematical checks

The identity m1=h2-C retains the actual Sonin projection. The complement
formula from the two cutoff constraints has block inverse [[M,-CM],[-CM,M]].
For real sources, the source correlation operator and symmetric prime
translation operator commute with the cosine involution. This gives
C=2Tr(MXPL*-(CM)XP Fcal L*), with its signs and operator order intact.
The dilation adjoint is L*v(x)=-v(x/2)/2 on (1,2); omitting that Jacobian
would change the answer. The source compact support restricts every
remaining physical integral to bounded intervals. Trace cyclicity uses
the explicitly localized Hilbert–Schmidt factorization of X.

Independent checks reproduced both exterior projection kernels, the
polynomial coefficient matrices, all three rectangle-moment formulas,
the contact term, and the matrix aggregation. The convention is
P=delta-Apoly; Apoly is the kernel being subtracted. The polynomial model
does not assume the inverse commutes with a finite approximation.

The positive source spectral measure is valid even without commutation
between H and the spectral projections of A. Jensen and the chord bound
give h0²/m1 <= B2 <= ((m+M0)h0-m1)/(mM0). The combination propagates
outward endpoints and intersects only already valid enclosures. The direct
arithmetic form is calculated separately and never defines the moment.

## Numerical error checks

The second-transport scalar uses the exact G² multiplier and correlation
coefficients 13/4, -3/sqrt(2) at the two first shifts, and 1/2 at the
two second shifts. Its support and L1/derivative factors are enlarged
appropriately. Gamma retains the full contact and all Fourier/alias tails.
Epsilon retains the source and polynomial-resolvent errors. A separate
lower-grid/higher-precision replay overlaps the principal intervals.

The compact correction's operator and cosine replacements are bounded
analytically, including the infinite-dimensional complement. The two
terms are below 4.2e-26 and 1.1e-33 for unit source norm. Source error
dominates: a cellwise Dirichlet bound gives
eta <= h²||F''||2/pi² + sqrt(Lh)*nodal_error. Factoring the convolution
through a finite logarithmic interval proves
||X_F-X_Fh||1 <= (1+r)²(a+Lh) eta(2+eta). The correction multiplier
4r/gamma is valid, as are the separate (1+eta)² model-error factors.
Both the true-source coverage and the interpolation-support upper bound
are checked in Arb after any floating candidate index selection.

Exact integer correlation and finite cubic antiderivatives integrate the
source spline. The helpers include all splines crossing zero and log2;
simply truncating a full-half-line polynomial would be wrong. Fourteen
independent Acb cellwise integration controls passed, including zero,
small, large positive, and large negative exponents. These controls check
implementation; the identities and interval arithmetic provide the bounds.

The final compact calculation uses grid 131072 and 1152-bit arithmetic.
Its correction widths are approximately 0.00851197 and 0.00907820.
The independently implemented floating compact quadrature agrees with the
intervals; its output is explicitly diagnostic and supplies no error bound.
No large grid arrays are retained.

Final generator and dependency hashes match current code and records.
An independent replay of the moment combiner was byte-identical to the
principal record. Direct prime-correlation calculations at 192 and 256
bits overlap; their analytic endpoint tails are included. The earlier
gamma/source certificates are inherited inputs, not all rebuilt here.

## Scope and decision

The current B2 intervals are [1.03644381,8.67999475] and
[0.79696516,6.86726714]. Their residual intervals are
[-7.24075680,0.40279415] and [-5.81945856,0.25084343].
Both contain zero. A positive correction C=h2-m1 on these two sources
does not establish positivity of the different arithmetic residual.

The mass-and-mean information ceiling is correct: a point mass at the
mean attains the Jensen lower bound, and a mixture at the spectral
endpoints attains the chord upper bound. The records certify that the
direct Q lies strictly between those extrema throughout the numerical
input ranges. Thus extra precision in these two moments cannot decide
the sign by those data alone. These generic measures are not Sonin
counterexamples. The separate generic commuting-operator construction
also has appropriately limited scope.

The [finite Mellin-defect note](../notes/SONIN_FINITE_MELLIN_DEFECT_20260929.md)
correctly requires both constrained residual positivity and bounded cross
terms in its residual seminorm. A fixed allowed set of Mellin conditions
must retain the all-source, unbounded-support criterion. Neither condition
is proved for the actual residual here; the odd-source mean-only test
remains undecided.

The next work should introduce additional compressed information or a
Sonin-specific comparison. Further precision in the present moment is
not justified by the sign question. No all-source or all-support positivity
theorem, independent physical realization, or RH result is claimed.
