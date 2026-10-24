# Same-assistant assessment: explicit clock and finite-source connection

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**.

**This is a same-assistant assessment, not independent mathematical
review.** It audits [Note 19][clock], [Note 20][bridge], the
[clock record][data] and [primitive record][primitives]. Analytical
claims remain proved-in-note with the stated source/collar premises.
No certified finite onset, optimized transition mesh, all-time theorem,
specialist review or RH/simplicity conclusion is supplied.

## 1. The quantitative gain and its price

The positive reference is now explicit in the large saddle L and its
curvature kappa. Exact periodic Bernoulli polynomials retain finite
lattice phase without a mode truncation or a changing number of terms.
The resulting density error is O(kappa^-1/2), versus the old leading
mean's O(kappa^-1/2+L^-3). The current and density time derivative retain
O(L kappa^-7/6) on the growing inner window.

This improves the formula and its asymptotic phase budget. It does not
decrease every finite bound: replacing the exact source mean costs a
separate coefficient error. At t=1e12 the floating time-error allowance
over L/kappa increases from about .01768 for the complete mean clock to
.03826 for the saddle clock. At 1e6 and 1e9 it is still larger than one.
The failed 1e4 collar gate is retained. No onset is certified by these rows.

## 2. Score identity and coefficient substitution

The crucial improvement is proved before it is used: the complete smooth
source admits a uniformly bounded b'/b, and integration by parts pays
both mu-L and v-1/kappa. The source half-line endpoint p(0) is nonzero;
its signs in SC7 are +p(0) for the mean and -L p(0) for the raw second
moment. The upper bound uses the complete mass floor, not a truncated
numerical mass. The bound |b'/b|<=5 is obtained from all theta modes,
including an analytic geometric bound on their derivative tail.

The exponential remainder requires A_2(4) and A_3(4), not just moments
at the observation strip height. Note 12's weighted proof applies to
this fixed source weight. With those terms retained, mean error is
O(kappa^-1), variance error O(kappa^-3/2), and the exact identity
mu'=2mu v+m3 yields drift error O(kappa^-3/2). No derivative of an
O-bound or formal unbounded saddle expansion is used.

Multiplying the drift error by height X and a local population O(L)
gives O(L kappa^-7/6). The displacement of the two clocks is at most
Xe/L, and its differentiated kernel cost is O(kappa^-4/3). These are
the missing costs that prevented Note 16 from using 2/kappa alone.
Both clocks and actual roots must fit the enlarged buffers; the note
does not replace a carrier-maximal wall by an arbitrary moving wall.

## 3. Phase, current and normalization

The five endpoint derivative integers follow by expanding
(s-1)^4(s+1)^4 at s=1. The half-step shift is +1/2 in both Bernoulli
arguments. Even kernel parity and odd s*k parity give different signs
in SC11 and SC12; these are not interchangeable. The zero-frequency
terms are 1/p and zero, respectively.

The 24 exact rational cases check mass, first moment and time/space
continuity, including negative centers and kernel-edge crossings.
All 72 equalities hold. The degrees used in the Bernoulli Fourier
identity are at least five, so endpoint evaluation and the needed
first derivatives are unambiguous. The zero-extended C3 kernel makes
edge crossings regular. The current is -(2/kappa) times the **position
moment**, not simply -2xR/kappa; omitting D would be an error.

## 4. Actual-theta evidence and its limitations

The six earlier observations were reused. Four new held-out times/heights
use the existing source/contour implementation and no fitting. The new
source and contour refinements are combined, with a separate contour
height change. This is not a new independent numerical implementation.
The largest observed derivative discrepancy in the ten samples is
3.708e-7 of 2L/(pi kappa); the uncorrected continuum reaches .003143.
At higher times some errors approach their refinement scale. Observed
errors are much smaller than the proved allowances, which remain
conservative; neither set is an interval certificate.

These observations concern the zero measure. The finite-epsilon transfer
uses Note 16's analytical bounds and cannot be inferred from the observed
contour discrepancy. No roots are fitted, density peaks sampled, reduced
trajectory evolved, or empirical uniform rate established.

## 5. What the finite-time connection proves

The globally smooth regulator is a definition with paid endpoint
compatibility, not a global solution. Its switching times are not onset
certificates. At negative time its relative regulator change is O(T^-2),
which preserves the existing O(T^-1) scaled density error. At sufficiently
large positive times it is exactly the already analyzed saddle regulator.

The compact piecewise linear source produces an exact heat solution with
a finite error-function expression. Complete source interpolation, mode
tail and spectral tail errors are paid separately; their weighted L1
bound controls jets uniformly over all real heights on a transverse strip.
A positive regulator floor is additionally needed for the nonlinear
density comparison. After height adaptation begins, the stated floor is
on a bounded horizontal buffer, not the entire real line.

The density/current/time bounds retain their powers of the regulator
floor and the time derivative of the regulator. The true covariance
comparison is obtained from the two actual source fields. Moving spatial
derivatives onto the fixed smoothing kernel pays Delta(Q-Q_f); it is not
obtained by differentiating the source error bound. No field is defined
afterward merely to force the covariance equation.

The nine primitive checks include positive, zero and negative time and
complex z. Their maximum floating discrepancy is 7.03e-16. They check
the square-completion normalization and removable limits; they do not
select source mesh parameters, enclose numerical error or evaluate a
transition density/covariance trajectory.

The source-to-field comparison is a direct stability estimate. It makes
no forward-parabolic assumption about the mixed-sign density equation.
Nevertheless an efficient finite representation and informative overlap
remain unproved. A fixed compact source provides a particularly clear
scope check: **zero heat residual does not imply global closeness**.
Its exp(tU^2) growth cannot match theta's growing saddle. The exclusion
is limited to fixed compact cutoffs with this regulator, not growing
source representations or other all-time methods.

## 6. Status and next work

The explicit positive saddle-clock task is complete at its eventual
inner-window scope. The finite-time connection has an analytical
construction, global regulator and paid comparison maps, but no selected
complete-transition mesh or useful overlap theorem. HDA-02--06 remain
partial and HDA-07--09 gated. The maintained manuscript and its build
artifacts are unchanged; no new draft snapshot or commit was made.

The next bounded deliverable should specify a finite transition slab,
representation size and accuracy target, then evaluate the complete
source, arithmetic, filter and regulator budgets. If the global second-
derivative interpolation bound is too expensive, replace it with local
derivative bounds or a higher-order source approximation and prove the
new remainder. Actual clock covariance, positive outer heights,
independent review and finite interval onset remain separate open tasks.

[clock]: ../notes/19_EXPLICIT_SADDLE_CLOCK_AND_EXACT_PHASE_20261024.md
[bridge]: ../notes/20_GLOBAL_REGULATOR_AND_FINITE_SOURCE_BRIDGE_20261024.md
[data]: ../numerics/EXPLICIT_SADDLE_CLOCK_20261024.json
[primitives]: ../numerics/FINITE_BRIDGE_PRIMITIVES_20261024.json
