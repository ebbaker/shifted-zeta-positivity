# Review of parity core extraction and cross core costs

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex). Reasoning effort: inherited configuration, not exposed.
This is a same-model cross-review, not independent expert review or formal
verification.

The [parity core note](../mixed_character_families/notes/11_PARITY_CORE_JOINT_CORRELATION_20261009.md)
has a useful conditional analytic deduction: bounded original coefficients
permit cubic power extraction without a fixed power loss within a parity
core. It also shows that recombining those cores by the permitted positive
estimates does not close the latest mixed remainder. The native cubic
presentation transfer and the deep squarefree cubic sieve remain inputs.

## Exact identities and masks

The factorization \(k=\alpha r^2\), with squarefree \(\alpha\), is unique
and does not impose \((\alpha,r)=1\). The note correctly keeps the
quadratic predicate on the two parity cores and the cubic predicate on
the full \(\alpha r^2,\beta t^2\). Fixed ray factors cancel only in
phase inside a kernel; their modulus-squared zeros remain in \(c_k\).

Below or at \(Z=U^{71/125}\), the strict quadratic condition excludes
equal parity cores because \(f_2=1\). Equal cube cores are excluded by
the cubic condition. Above the threshold both component conditions
are automatic. The source's indefinite-filter observation therefore
applies in the first range, and the unfiltered cross-core problem
returns in the second.

For a fixed core and endpoint-supported factor, the varying square-root
coefficient contains only fixed endpoint phases, masks and profiles.
The common \(\chi_\alpha(pq^2)\) phase has modulus at most one and is
removed only inside a nonnegative square. This is a valid step for the
individual block bound, but not a deletion of its cross-core phase in
the original signed sum.

## The bounded coefficient extraction

Write \(r=d e^2z^3\), with \(d,e\) squarefree and coprime. The factor
\(z\) can share primes with either one. Its cubic phase contributes the
mask \(1_{(pq,z)=1}\); the frozen \(e\) contributes its actual phase
and zeros. For fixed \((e,z)\) the varying \(d\)-vector is squarefree,
fixed, and supported at \(L/R\), with \(R=(\mathrm Ne)^2(\mathrm Nz)^3\).
Thus the cited squarefree-column theorem applies at its proper scale.

Cauchy weights \(R^{-1/2-\delta}\) have a convergent first factor for
every fixed \(\delta>0\). Applying the operator and bounded coefficient
mass \(O(L/R)\) produces
\[
 PQ L\sum_{R\le L}R^{-1/2+\delta},\qquad
 C_1L^2\sum R^{-3/2+\delta},\qquad
 C_2L^{5/3}\sum R^{-7/6+\delta}.
\]
For \(0<\delta<1/6\), the first sum is \(O_\delta(L^\delta)\);
the other two double ideal sums converge. Allocating \(\delta\) and
the imported sieve loss inside the requested \(\varepsilon\) proves
the displayed bounded-coefficient consequence. This is not an
unchanged unrestricted-column arbitrary-vector cubic operator.

## Recombination and scope

A core range of norm \(A\) has \(O(A)\) cores and root length
\((N/A)^{1/2}\). The diagonal aggregate and the Cauchy recombination
in the note have, respectively, one and two factors of \(A\).
The range \(A\asymp N\), with bounded root length, consequently
costs \(PQ\) after normalization. Original long prime columns lie
in precisely that range and can pass both component restrictions.

The rational comparison at the surviving raw geometry is consistent:
the recombined exponent is \(21/50\), exceeding the affordable
middle exponent by \(41749421609/169150000000\). That is a deficit
of the method, not a lower bound for a selected physical energy.
The better diagonal estimate below the radical threshold concerns
terms already removed by the component cut.

The general valuation grouping preserves the cubic exponent classes
modulo three. Freezing the valuation-three roots pays their radical
count; no uncharged replacement of physical norm by radical is used.
The analysis supplies no estimate for the filtered cross-core form,
the actual selected inverse distribution, or the signed endpoint
aggregate. Those are stated as new theorem targets.

## Verification

The accompanying [checker](../numerics/check_mixed_parity_core.py)
and [record](../numerics/mixed_parity_core_check.json) test the exact
local phases and rational budgets. The replay checks those identities;
the analytic deduction additionally uses the stated native transfer,
de Faveri's Proposition 8.1, and elementary ideal counting.
The full mixed moment and RH descent remain open.
