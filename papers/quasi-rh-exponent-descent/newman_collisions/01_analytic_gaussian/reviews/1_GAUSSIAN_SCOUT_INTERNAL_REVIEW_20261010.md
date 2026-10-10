# Internal review of the first Gaussian analytic scout

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6.1-sol (Codex). Reasoning effort: ultra, verified from this
chat's recorded configuration. Parallel LLM checks are internal checks,
not independent mathematical validation.

[Note 1](../notes/1_GAUSSIAN_REDUCTION_JOINT_KERNEL_AND_POSITIVITY_OBSTRUCTION_20261010.md)
implements the first bounded scout in
[Heat Note 14](../../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md).
It supplies the exact Gaussian reduction and a precise obstruction to
Gaussian norm or positivity as a universal lower-bound mechanism. Its
contour refinement pays the normalized Gaussian tail through order six
on one closed parameter rectangle. It supplies no new signed inequality
specific to the actual theta state.

## Mathematical checks

The fixed-field moving projection and the evolving analytic transverse
field have the correct backward heat sign in the real coordinate. The
derivative moment kernel has multiplier `-iy/(2t)`. The normalized second
coordinate retains the full amplitude drift. The observation kernel and
Gram determinant agree with the Gaussian value and first-moment map.
The positive Gram determinant shows independence of the observations;
the Pythagorean identity shows exactly why it supplies no lower bound
on an unrestricted nonzero state.

The repeated integration-by-parts Hermite formula, its Parseval identity,
the quartic Hermite expansion and norm, the positive shifted-kernel
construction, and the fourth-jet normalizer cancellation received parallel
internal algebra checks. The positive kernel model is a designed
non-theta control. Its collision can be placed in the parameter rectangle,
and its bulk Gaussian norm is finite and positive. The claim does not
require or assert monotonicity of that kernel.

The elementary real theta envelope and Gaussian complementary-error-function
tail were checked. The normalizer is exactly the manuscript's symmetric
one, and the pointwise lower bound retains the spatial archimedean decay.
The radius-one logarithmic derivative estimate gives the stated Cauchy
bound on every inverse-normalizer derivative. The complex spectral contour
stays strictly inside the kernel's holomorphic strip, with its vertical
sides paid by an explicit double-exponential envelope. The theta-sum
interval comparison and the split integral defining `D_j` give conservative
closed-form constants through order six.

The uniform jet prefactor is below `exp(300)` and the Gaussian exponent
at radius 9 is `-384.75`, giving error below `exp(-84)` without relying
on floating-point arithmetic. The truncated moving-projection equation
retains its boundary flux; the moment derivative retains its endpoint
term; the normalized equation retains the time derivative of the
normalizer. These boundary payments are explicitly bounded.

The final audit clarified that theta modularity supplies evenness before
analytic continuation to the strip, specified the positive observation
scale, and kept the explicit Gaussian moment majorant within its stated
domain. No sign or constant correction was required.

The existing full arithmetic approximation, fixed integer cutoff, and
measured quadratic threshold payment are imported unchanged from Heat
Notes 8 and 13. Gaussian truncation errors and arithmetic approximation
errors are distinguished. Comparing the two approximations pays their
sum; using either one alone uses its own payment. A small Gaussian tail
is not a signed exclusion theorem.

## Validation and limits

Additional checks evaluated the normalizer's real-axis formula against its
complex definition at several heights, verified the fourth-jet cancellation
with exact rational arithmetic, and verified the quartic energy identity
with exact rational Gaussian moments. Floating-point evaluations of the
explicit constants served only as diagnostics: the largest logarithm of a
jet prefactor through order six was approximately 274.524, below the
proved conservative bound 300. The analytical inequalities, rather than
these floating-point diagnostics, establish the tail payment.

Local Markdown links and mathematical delimiters were checked. All new
files are below 1 MiB, with no large derived data or manuscript snapshots.
The investigation is based on repository commit
`ef162fd8033a0ded9a13814f2779a2dd28fa9023`; no commit or tag is created by
this scout.

No numerical quadrature certificate, actual-theta collision exclusion,
signed threshold contradiction, or global parameter coverage is asserted.
The next step must add an explicit relation for the genuine theta Hermite
observations, with the appropriate quadratic payment and multiplicity
hypotheses. Improving representation constants alone does not add that
relation.
