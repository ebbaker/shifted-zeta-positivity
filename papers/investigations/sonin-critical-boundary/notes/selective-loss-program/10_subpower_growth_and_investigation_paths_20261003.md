# Subpower growth targets and paths for investigation

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration. The exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Separate same-model agents checked the transfer estimates and manuscript
integration. These are internal checks, not independent specialist review.

This note records the quantitative relaxation added to the current
[manuscript](../../manuscript.tex). It follows the exact normalization in
[note 06](06_global_mechanism_tests_20261003.md), the physical weighted-energy
analysis in [note 07](07_weighted_energy_abscissa_20261003.md), and the
central projection in [note 09](09_actual_error_projection_and_frequency_20261003.md).
The transfer theorem is established. The global bound for actual primes
remains unproved and RH-equivalent.

## Exact transfers and equivalent targets

Keep the existing normalized prepared probe and complete smoothing windows.
Write

\[
p_g(y)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}g(y-\log n),\quad
V_g(x)=\sqrt x\,p_g(\log x),\quad
J_g(Y)=\int_0^Y|p_g(y)|^2dy,
\]
\[
\mathcal V_g(X)=\int_X^{2X}|V_g(x)|^2dx,\qquad
J_{g,\varepsilon}=\int_0^\infty e^{-2\varepsilon y}|p_g(y)|^2dy.
\]

For every real X at least one, the change of variables gives

\[
J_g(Y)=\int_1^{e^Y}|V_g(x)|^2\frac{dx}{x^2},\qquad
X^2\Delta J_g(X)\le\mathcal V_g(X)\le4X^2\Delta J_g(X),
\]

where \(\Delta J_g(X)=J_g(\log(2X))-J_g(\log X)\).
For each fixed positive delta, summing logarithmic shells and using
monotonicity for the final partial shell proves the direct equivalence

\[
\mathcal V_g(X)=O_\delta(X^{2+\delta})
\quad\Longleftrightarrow\quad
J_g(Y)=O_\delta(e^{\delta Y}).
\]

The constants and starting thresholds may depend on delta. Tonelli gives
the equality, also for infinite nonnegative integrals,

\[
J_{g,\varepsilon}=2\varepsilon\int_0^\infty
e^{-2\varepsilon Y}J_g(Y)dY.
\]

Thus the fixed-delta bound gives physical finiteness whenever
\(\varepsilon>\delta/2\). Conversely physical finiteness gives
\(J_g(Y)\le e^{2\varepsilon Y}J_{g,\varepsilon}\).
Consequently all-delta subpower variance, subexponential cumulative energy,
and physical finiteness for every positive epsilon are equivalent.

For the actual probe the true Laplace transform, in the manuscript's
plus-exponent convention, equals

\[
P_g(s)=-G(-s)\frac{\zeta'}{\zeta}(1/2+s),\qquad \Re s>1/2.
\]

Physical finiteness makes the transform holomorphic on
\(\Re s>\varepsilon\). The established noncancellation lemma leaves a
nonzero residue at every hypothetical zero with
\(\Re\rho>1/2+\varepsilon\); the preparation zero cancels the zeta pole
only. All-epsilon finiteness therefore implies RH. Conversely RH gives
bounded p_g, hence \(J_g(Y)=O(1+Y)\) and
\(\mathcal V_g(X)=O(X^2)\), by the existing absolute zero expansion.
The all-delta criterion is therefore RH-equivalent.

At one fixed \(0<\delta<1\), the bound excludes zeros strictly right of
\(1/2+\delta/2\). It makes no claim of convergence at the weighted endpoint
\(\varepsilon=\delta/2\), or of exclusion at that zero-location boundary.
Even a fixed positive exponent improvement is a substantial partial theorem.

Quadratic cumulative J directly supplies only
\(\mathcal V_g(X)=O(X^2(\log X)^2)\) through the shell inequality.
The sharper \(X^2\log X\) dyadic condition directly implies quadratic J;
its reverse logical implication for actual primes passes through RH,
which gives the stronger \(O(X^2)\) dyadic estimate.

## Central projection and suggested investigations

Note 09 proves an unconditional outer variance bound
\(O_g(X^2\log(2X))\), including the complete physical caps. Its exact
Fourier identity and the triangle inequality in both directions make the
all-delta target equivalent to

\[
\int_1^2|P_{X,X^{1/11}}(s)|^2ds=O_\delta(X^{1+\delta})
\qquad\text{for every }\delta>0.
\]

This permits logarithmic and subpower losses without a uniform
small-epsilon polynomial rate. It remains an open estimate for actual
coefficients \(\Lambda(n)-1\) over every integer in the complete band.
By note 09's identity
\(\mathcal R_g=\mathcal V_g-\beta_gX^2+o_g(X^2)\), the all-delta bound
for the aggregate positive remainder is another equivalent target.

Prioritize the exact central projection or physical Gram kernel. Translate
one proposed unconditional arithmetic input through its signed weight,
retaining caps, the full shift range, real-X endpoints, and exceptional-set
costs. Report the resulting exponent before undertaking further numerics.
An improvement to one exponent below three in physical variance gives
the fixed zero-free milestone above. Fixed logarithmic savings on an
X-cubed bound, coefficient-only norms, and absolute pair-error summation
do not give that milestone.

The fitted Chebyshev-error norm is a sufficient comparison and diagnostic;
it controls more directions than the exact smoothing. The source dual
energy remains a sharper alternative when unprojected norms are costly,
provided the full prepared-source residual is enclosed. Exact projection
mass survival is a separate operator investigation. Specialist proof and
priority review should accompany these paths. The manuscript's final
section states the proposed tasks and their limitations.

## Integration record

The current manuscript retains the original operator theorem package,
moves selective loss to a dedicated section after the finite translate
certificates, and integrates notes 08–09 with this transfer theorem.
The [integration review](../../reviews/ACTUAL_ERROR_SUBPOWER_MANUSCRIPT_REVISION_20261003.md)
records source checks, internal mathematical audit, and compilation.
No manuscript snapshot folder, commit, or push is part of this revision.
