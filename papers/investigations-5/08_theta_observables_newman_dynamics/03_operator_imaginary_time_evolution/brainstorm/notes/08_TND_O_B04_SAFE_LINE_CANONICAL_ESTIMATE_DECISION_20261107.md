# B04 r1: acquire a gap-independent canonical transport bound

6 November 2026, America/New_York (7 November UTC). Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Lead tool-selected dispatch configuration: **gpt-6-astra, ultra**, not independent backend verification.

**Decision:** use the canonical logarithmic derivative on the safe line Im z=4 to pay the far velocity; combine it with the E08 local Hessian cancellation. The target is a uniform absolute modulus for the local transverse moment, not a collision exclusion. E10 will be activated on the exact E08/E09 versions after their returns.

| Mechanism compared | Quantitative cost | Decision |
| --- | --- | --- |
| Absolute source or absolute intermediate zero sum | The source majorant does not give a relative denominator on the real axis; an absolute far sum from distance one to height X can lose an extra log X and cannot discard opposite pairing at infinity | Retain source completeness; do not use this as the local far-velocity estimate |
| Safe-line resolvent subtraction | Polymath §9 proof(iv) gives H'_lambda/H_lambda(x+4i)=O(log(2+x)); the difference of far resolvents is absolutely summable as distance^{-2} | Select: it pays the full distant field without a near-axis denominator or minimum gap |

## Fixed prospective estimate

For chi in C_c^2([-1,1]), 0<=chi<=1, X>=10 and 0<R<=1, define

    Q_{X,R}(lambda)=sum_j chi((Re z_j(lambda)-X)/R) (Im z_j(lambda))^2.

The fixed H normalization and heat sign are unchanged. On simple intervals, the target is

    |d Q_{X,R}/d lambda| <= C (||chi||_infinity+||chi'||_infinity+||chi''||_infinity)
                                 R^{-2} log^2(2+X),

with an absolute C uniform in X,R and 0<=lambda<=1/2. The exact norm combination can be sharpened. The later B06/E12 task will pay crossing multiple-root times and give an integrated estimate; it is not silently assumed here.

For an active zero z=x+iy, |x-X|<=R, remove the finite cluster |Re z_k-X|<=3. Compare its exterior resolvent at z with that at w=x+4i. Since the exterior horizontal separation is at least two,

    |(z-z_k)^{-1}-(w-z_k)^{-1}| <= C/(x-Re z_k)^2.

Unit-interval zero counts make this sum O(log(2+X)); the removed terms at w are also O(log(2+X)). Thus the paired exterior field is O(log(2+X)), not an absolute harmonic sum. There are O(log(2+X)) active/nearby zeros. E08's small-gap bound costs ||a||+||a''|| for each nearby pair. Exterior endpoint terms cost ||a'||+||a|| times the paid field. This gives the displayed O(R^{-2}log^2 X) candidate bound with no arbitrary minimum zero spacing.

## Primary-source input and time-zero endpoint

D.H.J. Polymath, *Effective approximation of heat flow evolution of the Riemann xi function, and a new upper bound for the de Bruijn–Newman constant*, [arXiv:1904.12438v2](https://arxiv.org/html/1904.12438v2), Theorem 1.5(iv) and its §9 proof, equations (105) and the following paragraphs. Fresh selected-passage inspection on this date verified both the unit-window count and the explicit safe-line logarithmic derivative estimate. Their constants are independent of 0<lambda<=1/2; the x>=exp(C/lambda) restriction belongs to the stronger tail-realness assertions and is not imposed on this coarse bound. At lambda=0 the safe-line bound follows by local uniform H_lambda→H_0 and the zero-free line Im z=4. Counts pass by argument-principle continuity on enclosing rectangles, or classical time-zero zero counts. The proof must spell out the endpoint rather than cite the positive-time statement unchanged. [Receipt10](../../references/10_TND_O_B03_R4_BENCHMARK_SOURCE_CHECK_20261106.md) records the root's separate selected-passage check; no full-paper or specialist review is claimed.

## What the bound can and cannot do

At fixed R it controls every height with log^2 X cost; at the mean-spacing H width R~1/log X it costs log^4 X. This is an explicit fixed-order, unbounded-height theorem target. Complete source and zero index are paid separately by E08 and the primary resolvent estimate. It supplies no small upper mass or favorable sign. A local pair can have positive production or negative window flux in generic heat controls. Canonical zero-count/safe-line bounds alone are shared by broad control classes and need not distinguish such behavior.

The first useful consumer is collision-stable regularity and an error-controlled integrated moment identity. An RH/time-envelope consumer would additionally need an independently acquired endpoint mass, spatial flux or stronger geometry estimate. Defining that unknown estimate as a new sufficient criterion would not be progress. B05 must decide this explicitly after E10. The task is worth executing because it removes a concrete artificial min-gap loss, pays the full distant field and states the exact width/height loss; it is not claimed to improve Polymath's real/simple exp(C/lambda) benchmark.

## Controls and bounded execution

E10 should include a sharpness/scope diagnostic if it follows from the same fixed estimate: an even real polynomial configuration with O(log X) zeros in the relevant unit interval, strip height at most one and safe-line logarithmic derivative O(log(2+x)), showing that localized negative flux may be of the same R^{-2}(log X)^2 order. If that sharpness claim requires new assumptions or is not obtained in the one bounded attempt, return the exact failure while retaining the canonical upper bound. No numerical campaign. Literal canonical arithmetic is not shared by the control; the tested premise class consists only of the coarse count, strip and safe-line estimates actually used.

Mandatory context: [result index](../../../../../../result-summaries/README.md), [control cluster](../../../../../../result-summaries/12_collision_controls_and_screening.md), [local geometry](../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [patterns index](../../../../../../avoid/README.md), [classification](../../../../../../avoid/01_restating_the_target.md), [scope discipline](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [B03 decision07](07_TND_O_B03_R4_LOCALIZED_TRANSVERSE_DECISION_20261107.md). The eventual E10 request will freeze the actually consumed versions and disjoint ownership.


## Frozen sharpness construction for E10 to verify

Take chi(t)=(1-t^2)^3 for |t|<1, zero otherwise. For m>=2 choose distinct t_j in [7/10,4/5], for example t_j=7/10+j/[10(m+1)]. Put Y=1/2 and prescribe the 4m simple roots

    +(X+R t_j) +/- iY,  -(X+R t_j) +/- iY.

Let P be their even real monic polynomial and let P_s=P_zz be its exact finite heat orbit through that snapshot. Only the +X window is active. Since chi''>=3 on the specified t interval, the same-height active interactions give at most

    - (3/2) m(m-1)/R^2.

The opposite-height active interactions contribute at most 4m^2; the reflected inactive group contributes at most 6m^2/(RX)+2m^2/X^2, using ||chi'||<=6. Thus the candidate bound for X>=10 and 0<R<=1/10 is

    dQ/ds <= -m^2/(2R^2).

E10 must check every coefficient, pair count and inequality. With m=floor(log(2+X)), the absolute negative rate has order R^{-2}log^2 X. Unit-interval counts and the safe-line estimate are uniform across these snapshots: near |x|>=X/2, log X is controlled by log(2+|x|), while for |x|<X/2 the total resolvent is O(m/X). The strip is strict at the snapshot and remains so on a parameter-dependent short heat interval. **No claim is made that this polynomial orbit satisfies the canonical strip bounds for the entire [0,1/2] interval.** The sharpness class is instantaneous estimates using the explicitly paid slice-wise coarse premises, not all-time canonical heat families.
