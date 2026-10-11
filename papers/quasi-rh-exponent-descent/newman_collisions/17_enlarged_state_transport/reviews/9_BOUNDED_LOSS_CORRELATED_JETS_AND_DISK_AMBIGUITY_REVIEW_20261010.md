# Internal review of bounded loss and correlated disk ambiguity

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); active reasoning effort is not exposed to this session
and is not inferred. This is an internal separate-agent LLM review and
arithmetic replay, not independent mathematical validation.

## Scope and outcome

The continuation comprises the [bounded-loss criterion](../notes/16_NEXT_STEPS_AND_BOUNDED_LOSS_COLLISION_CRITERION_20261010.md),
[multiplicity budget and Hölder extension](../notes/17_MULTIPLICITY_BUDGETS_AND_HOLDER_LOSS_CRITERION_20261010.md),
[exact correlated jets and local heat ambiguity](../notes/18_CORRELATED_ERROR_JETS_AND_LOCAL_HEAT_AMBIGUITY_20261010.md),
and [stationary survey with outward ambiguity certificate](../notes/19_STATIONARY_SURVEY_AND_CERTIFIED_DISK_AMBIGUITY_20261010.md).

The local analytic criteria, exact error-jet formulas, and stated ambiguity
result pass this scoped review. They do not establish a signed genuine-theta
bound, complete stationary-set coverage, or a new collision-free region.

## Analytic checks

For odd multiplicity \(2r+1\), the predecessor expansion has
\(H_x=ch^r+O(h^{r+1})\), \(H_{xxx}=rc h^{r-1}+O(h^r)\), and
\(H=O(h^{r+1})\). The last assertion follows because every heat Taylor
term with total exponent at most \(r\) uses a spatial jet of order at
most \(2r\), hence vanishes. Thus using \(E=H^2+H_x^2\) in the
bounded-loss denominator is valid for both parities.

The Hölder ratio is exactly of asymptotic order
\(h^{2r\delta-1}\); the strict requirement
\(\delta<1/(2\lfloor M/2\rfloor)\) is correct. The paired Blaschke
proof gives denominator \(2\log(R/|x|)\), since both \(x\) and
\(-x\) are removed. The disk maximum equals the positive imaginary-axis
theta integral. Time monotonicity supplies the uniform finite-window bound
without information about the other zeros. The heat-polynomial endpoint
controls retain both stationary conditions and demonstrate the claimed
sharpness for a multiplicity budget alone.

The exact Schur recursion retains every coefficient through order three
and all degenerate parameter faces. Eliminating the normalized second
coefficient using physical stationarity gives the third-jet drift terms
\(\lambda''-2\lambda^3\) and \(3(\lambda'-\lambda^2)\), as printed.
The one- and two-variable robust tests optimize the last free coefficient
with its sign aligned to the physical multiplying jet. The zero-radius
Schur boundaries require the separate cases explicitly stated in Note 18.

The local heat-ambiguity proof does not apply a Cauchy–Kowalevski theorem
across the time surface. It first constructs a strictly admissible analytic
spatial interpolant, approximates it by Taylor polynomials preserving the
required center jets, then evolves the polynomial by a finite heat series.
Strict disk slack and joint continuity extend the estimate to nearby times,
centers and radii. The fixed-cutoff and open-patch restrictions matter.
The alternative solutions need not have the theta initial condition,
positive theta source or global parameter estimates.

## Computation checks

The [exact rational checker](../numerics/check_correlated_jet_geometry.py)
was independently replayed by the main worker. Its
[record](../numerics/CORRELATED_JET_GEOMETRY_RECORD_20261010.json) reports
625 formal-series comparisons, 9,375 principal minors, 400 degenerate
boundary cases, 225 conditional intervals, 1,875 physical product checks,
and 1,875 stationary drift-elimination checks. These finite checks support
the printed algebra; the analytic proofs remain separate.

The floating [survey](../numerics/survey_stationary.py) retained every
detected sign-change root. It uses a frozen locator followed by full
physical refinement and explicitly allows missed even roots or pairs
within one grid gap. Derivative recurrence checks passed, and a final-source
replay reproduced all 815 first-run root tuples. The
[small retained summary](../numerics/STATIONARY_SMALL_JET_SURVEY_RECORD_20261010.json)
keeps parameters, validations, hashes and weakest rows; full root arrays
remain regenerable output outside the repository. No floating sign or
naive payment count is called a genuine-stationary certificate.

The [outward checker](../numerics/check_stationary_disk_ambiguity.py)
regenerated all 22,066 finite terms and both retained source hashes passed.
Its [record](../numerics/STATIONARY_DISK_AMBIGUITY_RECORD_20261010.json)
reports PASS. The generating formulas match the earlier high stationary
checker, including finite spatial transport, normalizer drift and interval
integer powers. Four frozen moments suffice because the evaluation offset
is exactly zero; the Taylor remainders have positive powers \(4-j\)
for every \(j\le3\), so vanish. The finite transport error is still paid.

For the normalized perturbation \(\eta(a_2w^2+dw^3)\), the lower two
error jets are zero, the second physical jet is cancelled by
\(a_2=-f_2/(2\eta L^2)\), and the third physical jet changes by
\(-3\lambda f_2+6\eta L^3d\). The outward norm is below 0.511521
for \(d=\pm1/2\); the common slope is negative, and the alternative
third jets have strict opposite signs. An independent agent checked both
the source construction and the retained arithmetic inequalities without
performing a second complete summation.

## Scope decisions and next target

The ambiguity is for the printed coarse error envelope. It does not assert
that a sharper proven remainder would also permit both signs. The chosen
center has positive energy about 7.69 and its value is separated from the
value error; it is neither a collision candidate nor a violation of the
bounded-loss criterion. The separate general interior-candidate theorem
in Note 18 supplies the collision-related limitation.

These results justify pursuing a theta-specific bound on the remainder or
signed source response. Arbitrary bounded holomorphic error, even with
local heat compatibility, does not contain enough information to exclude
strict interior first-jet candidates. The Hölder criterion relaxes the
required vanishing rate when an independent multiplicity budget is used;
the actual signed estimate remains open. Existing coverage obligations and
the parent approximation dependency retain their stated status.
