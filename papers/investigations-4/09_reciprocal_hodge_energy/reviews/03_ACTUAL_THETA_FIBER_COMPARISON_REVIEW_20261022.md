# Internal review of the actual theta fiber comparison

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**, verified from the current root turn metadata
and inherited by the separate reviewing agent.

**Assessment: no unresolved blocker to the finite-fiber certificate found.**
The reviewer was distinct from the source, geometry and comparison-error
contributors. This is separate same-model internal LLM review, not
cross-model, human or specialist validation. The [note][note], [fixed
contract][contract], [replay][script] and its two local support modules
were audited. Use the [result index][results], [avoid index][avoid],
[control register][controls] and [scope rule][a07].

## Canonical source and geometry

The implemented s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)/16, s=(1+iz)/2,
is exactly xi(s)/8. The normalization agrees with [Rodgers–Tao,
Introduction (1)–(3)][rt], checked against the primary paper.
Positivity of the complete source gives the Cauchy majorant
M=H_0(16i)=H_0(-16i) on the required imaginary strip. This retains
canonical coefficients and reflection without a finite source substitute.

The real sign brackets, positive Rouché margins and derivative floors
prove two distinct real simple zeros. Every outer angular arc is covered
by a convex image rectangle excluding zero; the enclosed phase increments
isolate winding number two. These two local roots exhaust the disk.
Thus the deflated unit is holomorphic and nonzero on the whole disk.
Boundary principal-log avoidance, positive normalization at 43 and the
maximum principle justify its coherent square root. No RH or all-real
global slice is assumed.

## Taylor oracle and complete errors

The degree-64 Taylor construction explicitly sets the series cap to 65.
The field, first derivative and half-second-derivative tail formulas
are correct. Double synthetic divided difference gives P[alpha,beta,z].
Because the exact roots vanish, the true unit is H_0[alpha,beta,z];
the remaining divided difference is bounded by sup|E''|/2 on the convex
physical disk. Root and coefficient errors remain balls throughout.

Centered quadratic evaluation of the deflated polynomial, with the
radius-9 third-derivative coefficient bound, encloses each input rectangle.
Adding the source remainder only on that rectangle's physical subset is
valid: the actual outer arcs, real path and shifted-disk cover images
all lie in the radius-8 physical disk. The API explicitly forbids
treating this subset range oracle as an analytic integration callback.
Unused unsafe raw-branch callback methods were removed before final replay.

Every cell contributes an interval measure times a whole-cell range.
No convergence difference, estimated floating error, failed cell or
singular cap is discarded. Outward Arb operations pay coefficient,
root, map, primitive, product, source-tail and rounding uncertainties.

## Boundary and direct consumers

The positive real unit makes q=iQ and the plus-to-minus relative period
p negative. Thus the phase rotation is exactly one. Reflection gives
Q=2 integral_0^pi Im B and R_ext=4 integral_0^pi v Im B. The running
prefix plus the partial-cell primitive interval encloses all accumulation
error. Q and R_ext are acquired from the same outer cells. Their final
interval addition conservatively relaxes correlation rather than omitting
it. The regularized real transverse integral and signs in E=-Qp+R_ext
agree with Note 03; both physical boundaries and cut payments remain.

The direct U(theta) solves the complete shifted-disk boundary equation.
The hyperbolic cover coordinates remove both branch singularities. The
Jacobian U and two reflection symmetries give the stated factor four.
Every actual direct point is in the physical disk, and no failed cell
is skipped in the delivered replay.

The native boundary energy interval is strictly contained in the native
direct interval, with margins far larger than the reporting precision.
The exterior correction interval is strictly negative on this one disk.
These statements concern actual finite theta data, not an event exclusion.

## Replay and reporting corrections

The separate reviewer ran the final settled scripts successfully under Python 3.10.0, python-flint 0.9.0 and FLINT 3.6.0. All four native energy enclosures exactly reproduced the earlier arithmetic endpoints, and every stored script/contract hash matched. The final canonical [receipt][record] retains that one replay’s timings; no best timing was selected. Both consumers reached the declared 25% target, with passing relative diameters 15.9344% and 18.7038%.

Two reporting details were corrected before final replay. Relative
diameters of negative quantities use the absolute midpoint. The shared
intersection uses exact rational endpoint maxima/minima: rebuilding an
Arb midpoint-radius ball could widen slightly outside the intersection.
Stored hashes identify the delivered scripts and original fixed contract;
they do not replace the replayed arithmetic tests.

## Fairness and continuation

Both native consumers receive the same source, roots, unit information
and arithmetic precision. The common normalized branch chart is an
equal-information contract charge; an optimized direct absolute-energy
implementation may omit that branch work. Fresh reported times include
common acquisition and consumer passes, but exclude process startup,
imports and serialization. Failed earlier meshes remain charged.

After the boundary observations and identity are shared, the equally
informed direct comparator inherits the same intersection. The observed
native width and timing improvement therefore establish an implementation-
specific benefit, not intrinsic Hodge information dominance or optimal
acquisition cost. A collision-free finite control box may pass this same
calculation. Endpoint uniformity, every height, higher multiplicities,
off-line coverage and RHE-05 remain open.

[note]: ../notes/04_ACTUAL_REGULAR_THETA_FIBER_COMPARISON_20261022.md
[contract]: ../numerics/03_ACTUAL_THETA_COMPARISON_CONTRACT_20261022.md
[script]: ../numerics/03_compare_actual_theta_fiber_20261022.py
[record]: ../numerics/03_ACTUAL_THETA_COMPARISON_20261022.json
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[rt]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D4B85BA067E2D5A71D87E4FFB0D21E46/S2050508620000062a.pdf/the-de-bruijn-newman-constant-is-non-negative.pdf
