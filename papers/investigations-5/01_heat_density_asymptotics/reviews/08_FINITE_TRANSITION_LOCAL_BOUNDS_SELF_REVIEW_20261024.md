# Finite-transition contract and local bounds: same-assistant review

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
verified from this chat's session metadata. The reviewer is the assistant
that derived the results and wrote the implementation. This is not an
independent or specialist audit and does not complete HDA-20.

**Disposition: HDA-15 is complete at its analytical/diagnostic scope.
The 192-cell trial is not accepted for HDA-17.** See [Note 23][note],
[code][code], [record][record] and [manuscript][main]. No all-time theorem,
certified numerical onset or regulator-to-zero-measure estimate is added.

## Proof audit

The contract fixes the domain, full buffer, kernel, time interval,
regulator and component/derivative tolerances before the diagnostic.
It uses absolute physical quantities and supplies source-generated boundary
traces. The slab ends at 64, where spatial regulator derivatives and
curvature vanish to all orders. The time forcing/current source remain.
The flux convention matches 2 Re(partial_z j)=div(Re j,Im j).
No later spatially adaptive theorem is inferred from this simplification.

LC2 is the interpolation remainder for the complete source, followed by
positive nodal hats. LC3 pays every omitted theta mode at its actual node;
LC5 pays every differentiated source mode. The coefficients
(-75,330,-224,32) were rederived by applying (4a d/da)^2 to
(2a^(9/4)-3a^(5/4))e^-a. The first omitted differentiated mode has
a>17/4, so its endpoint and geometric-ratio tail are applicable.
LC4 uses h^3/12, obtained by integrating the half-quadratic remainder;
the nodal hats integrate to h/2 on each cell. Time-ceiling bounds cover
whole tiles, not just sampled times. The complete tail gates hold for
the chosen cutoff even at t=64. No mode/tail/arithmetic term is removed.

The new cutoff statement follows from an integrable shifted source
majorant. It holds at fixed finite time ceiling and bounded maximum cell
length. It does not assert uniformity as t tends to positive infinity,
nor a better interpolation order than h^2. With exact envelope definitions,
LC2 is dominated by the old allowance. The elementary LC4 bound may
lose this property on a coarse cell; taking its minimum with FB8 resolves
that issue explicitly. Finite numerical evaluation of the constants still
needs outward rounding for use in a certificate.

LC6 maximizes the rational derivatives on an annulus containing the
entire segment between the compared field values. The stationary radii
are epsilon/sqrt(5), epsilon and epsilon/sqrt(3). The derivative norm
of h/(|h|^2+q) is at most 1/(q+m^2). Product differentiation proves the
rho/current bounds, and the exact heat identity proves rho_t independently.
The same pointwise regulator is used for both fields, including its r_t
and r_i terms. Local P_j bounds the full jet segment. There is no division
by H or H_z and no unaccounted change of physical normalization.

LC9--LC10 compare the actual signed gradient covariance. Differentiation
is moved onto the fixed kernel and the differentiated square-of-means
formula; no covariance is defined from an equation residual. Constant
envelopes give 6||Delta K||_1+4(||K_x||_1^2+||K_y||_1^2).
Spatially varying envelopes must be convolved before taking suprema;
sampling them cannot supply a continuous integral bound.

LC13 is an absolute exponential Taylor remainder for each centered cell,
including both Fourier branches and the derivative factor u^j. It controls
truncation only. Observed floating error exceeds that truncation term,
so rounding must be separately paid. The exact finite-source H_f solves
heat; a truncated numerical implementation is not claimed to do so.

## Numerical audit and failures retained

The 48/96/192-cell study shows the intended cost distinction: at t=64,
U_s=1.5,N=4,Y=1, the 192-cell zeroth-jet allowance changes from
3.78785e58 to 5.63935e-2. This large ratio repairs an extremely loose
bound; it is not itself useful absolute accuracy. Interpolation dominates
the new source allowance. Local amplitude helps away from small field
values but does not make the peak region meet the contract.

The first nodal-rounding hypothesis failed by a factor 8.589. The revised
candidate passes the same finite high-precision comparison with ratio
0.08589, but remains uncertified. The raw error-function subtraction fails
near t=1e-8 at z=10+i,u=.25 despite 80-digit arithmetic. These failures
are preserved in the execution record, rather than silently replaced.
The local polynomial evaluator agrees with quadrature to about 1.12e-16
in six cases, with much smaller truncation allowances; this isolates the
remaining arithmetic cost and is not a uniform evaluator certificate.
The 128 deterministic jet checks include double-event jets and test the
implemented rational bounds; they are checks of the formulas, not proofs.

Filtering is unresolved: at t=64,z=4+.5i, increasing each filter direction
from 40 to 64 nodes still changes R_t by 5.93e-4 and Delta Q by 1.38.
The latter is far above its 10^-2 total tolerance and 10% filter allocation.
The sampled errors, including the 64-node Delta Q discrepancy, must not be
presented as converged estimates. Source refinement is substantially
smaller, but it is also empirical. No gaps between times or spatial points
are enclosed. The diagnostic does not meet HDA-17.

## Controls and scope

The quantitative source constants use the canonical theta expansion.
Euler-factor, weighted-square/finite-prime, reflected and positive-primitive
controls fail the unchanged-source/weight/reflection premises as specified
in Note 23. Atomic sources are not C2 densities; polynomial heat fields
are outside that canonical positive-source representation. The generic
stability bounds deliberately pass smooth colliding fields and local
polynomial double-event jets. No simple-root collar is used here.
The work does not distinguish theta from every colliding source or assert
RH/simplicity. The failed trial concerns this mesh, slab, regulator,
contract and evaluation procedure, not every finite-source approximation.

## Production and next work

The maintained analytical manuscript contains the new propositions, with
one short diagnostic paragraph and references to Note 23. The final 28-page export compiled without warnings; all pages were rendered,
with the new proof/equation and diagnostic pages also inspected individually.
All 29 local PDF links resolve. One line overflow was repaired.
These production checks are recorded separately in its build record. They do
not independently validate the mathematics. No snapshot or commit is made.

Next, refine the dominant source-cell contribution or improve interpolation,
provide a controlled evaluator and peak-aware filter integration, and enclose
the resulting errors over continuous tiles. Extending beyond t=64 restores
all spatial regulator corrections. Endpoint covariance/time budgets,
whole-tail onset, endpoint overlaps and joining errors remain HDA-16/18
obligations. A distinct reviewer remains HDA-20.

[note]: ../notes/23_FINITE_TRANSITION_CONTRACT_AND_LOCAL_BOUNDS_20261024.md
[code]: ../numerics/finite_transition_local_bounds.py
[record]: ../numerics/FINITE_TRANSITION_LOCAL_BOUNDS_20261024.json
[main]: ../manuscript/main.tex
