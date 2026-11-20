# AGC-E12: nonauthor numerical implementation assessment

19 November 2026, America/New_York. Prepared for **Edward Baker** with OpenAI
Codex LLM assistance. Reviewing helper originally explicitly dispatched
**gpt-6.1-sol / ultra**; independent actual backend/effort attestation was
unavailable to this helper.

**Assessment status: accepted within the frozen fixed-cell numerical
implementation scope.** One full code pass, one final-script replay and
one correction check completed. No unresolved mathematical implementation
defect was found. This is internal shared-premise checking, with the
theorem-authorship overlap disclosed below.

## Scope and ownership

This is a bounded **nonauthor numerical implementation assessment** of the
[E12 script](../numerics/agc_fixed_cell_comparison.py),
[Record03](../numerics/03_AGC_FIXED_CELL_COMPARISON_20261119.json) and
[Note07](../notes/07_AGC_E12_FIXED_CELL_COMPARISON_20261119.md), under
[E12 r1](../research-progress/handoffs/AGC-E12-r1-request.md) and
[B01 r2](../brainstorm/notes/04_AGC_B01_FIXED_PILOT_ADDENDUM_20261119.md).
The assessor did not author those numerical files.

The assessor **did author** E10's endpoint note04 and E13 note08. This
report therefore does not claim independent review of those theorems.
Their separate contributing-agent assessment is
[Review02](02_AGC_CONTINUATION_ESTIMATES_ASSESSMENT_20261119.md).
The source budget is [Note06](../notes/06_AGC_E11_SOURCE_ALLOWANCE_20261119.md),
with its separate [lead source check](03_AGC_SOURCE_ALLOWANCE_LEAD_CHECK_20261119.md).
Here the checked claim is that the numerical code faithfully implements
the attached source and accepted consumer formulas with their domains and
payments. Polymath's complete proof is not independently replayed.

The [result index](../../../../result-summaries/README.md),
[patterns index](../../../../avoid/README.md),
[Controls12](../../../../result-summaries/12_collision_controls_and_screening.md)
and patterns [04](../../../../avoid/04_counts_and_precision_as_evidence.md),
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and
[11](../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md)
apply. This fixed cell is inside earlier canonical coverage. The result is
a finite comparison of paid allowances, not new zero coverage, a Newman
bound, independent specialist validation or evidence from partition counts.

## Full code pass

The following items were checked against the complete final source.

**Physical reference, scale and defect.** The carrier logarithm, alpha
and its first two derivatives match the manuscript/Note06. Each of the
33 terms on each branch is retained. The finite defect has the correct
physical coefficient $-1/4$ and full polynomial in alpha and its
derivatives. Adding $\pi X/8$ inside every carrier exponential multiplies
$P,E,R,H$ by one constant positive scale, independent of $z,t$; no
normalized drift or potential is discarded.

**Source budget and source domain.** The code includes both term-error
sums and the entire unretained remainder
$\exp(t\pi^2/64)|\mathfrak M_0(iT')|
(1+\delta_-+\delta_+)$ of Note06. The leading correction is paid by the
$1$. Upper/lower half-plane carrier arguments are conjugates of the
specified source arguments, so the two branch moduli and error factors
are correct. The fixed rectangle has $x\ge200$, $|y|\le1$ and
$0<t\le1/2$. The recorded cutoff interval is approximately
$[1114.7348,1115.0538]$, strictly between $33^2=1089$ and
$34^2=1156$, with the lower inequality in the required non-strict form.
No cutoff seam or source extension across $\Re z=0$ is used.

**Closed domain covers.** Exact rational endpoints partition
$[9/100,1/10]$ into closed time intervals. The interval angles cover each
closed arc $[2\pi j/M,2\pi(j+1)/M]$, including endpoints. Interval sine,
cosine and complex arithmetic enclose the whole arc and time box, rather
than only the quadrature nodes. The radii $4/5,9/10,1$ stay inside the
right-half-plane analytic domain. Source values are evaluated on the
middle circle; the outer annulus only needs reference analyticity.

**Count and logarithm branch.** Positivity of
$\Re(P_{\rm scaled}/(z-X)^2)$ on every closed count-circle arc makes the
quotient's winding zero, so $P_N$ has count two. The same positivity on
both annulus boundaries propagates throughout the annulus by the harmonic
minimum principle, giving one principal holomorphic logarithm there.
The pole of the quotient at $X$ lies outside the annulus; no logarithm
through the interior zeros is assumed. With the complete $q<1$ bound,
Rouché supplies count two and clearance for $H$ on the same circle.

**Relative error is shared.** For each arc, the source upper endpoint
and reference-modulus lower endpoint are acquired on the **same**
space/time box. Taking $\max_k V_k/m_k$ therefore retains valid local
profiles. Both compared gap estimates use that identical $q$. The larger
global-supremum/global-infimum ratio is recorded only as context.

**Two-sided aliases and the full reference discriminant.** If
$L(w)=\sum_j l_jw^j$ on the annulus, the code's radius-weighted
trapezoid for $l_{-k}$ has aliases
$\sum_{\nu\ne0}l_{\nu M-k}r^{\nu M}$. The outer circle bounds the
$\nu>0$ ladder, and the inner circle bounds $\nu<0$. Thus, for $k=1,2$,
the implemented allowance is exactly

\[
M_+r_+^k\frac{(r/r_+)^M}{1-(r/r_+)^M}
+M_-r_-^k\frac{(r_-/r)^M}{1-(r_-/r)^M}.
\]

The exponents, signs, radius powers and both tails are correct. The
complex disk is enclosed in a coordinate rectangle, which safely
overpays it. Sample evaluation retains the whole time interval, so there
is no unpaid time interpolation. The code uses
$c_P-X=-l_{-1}/2$ and
$D_P=-l_{-2}-l_{-1}^2/4$, including the entire complex square and its
arithmetic uncertainty. Exact conjugation symmetry makes the physical
reference discriminant real; every recorded imaginary inclusion contains
zero. The largest final coefficient-alias allowance is below
$5.787\cdot10^{-23}$.

**Compared complete gap allowances.** The baseline is the stronger E10
formula $r^2[\lambda\sqrt{1+d^2}+\lambda^2/4]$, not merely the earlier
separate-moment sum. The refined allowance is the interval minimum of
the accepted E13 Cauchy and parabolic upper bounds, using the same
$d=|c_P-X|/r$ enclosure, $q$, $r$ and reference moments. The parabolic
branch is only used when $\eta<2$ is verified. The entire center and
nonlinear square payments are included. Refinement strictness and
positivity are interval comparisons, not rounded-decimal tests.

**Heat data and all boundaries.** Initial values are bounded at
$t=t_*=1/10$ over $x\in[X-A,X+A]$, $0\le y\le r$, and both lateral
values at $x=X\pm A$ are bounded over the full time interval and the
same height range. Conjugation supplies negative heights. The full
uniform finite defect bound uses the larger $h=1$ rectangle. This is
enough for every horizontal line reaching the contour; no boundary at
the top or bottom is omitted from the horizontal heat problem.

The two-sided erfc influence has the physical denominator $2\sqrt U$.
In the actual record the chosen boundary bound satisfies $M_b<\varepsilon_0$,
so the script correctly uses the safe survival-mass reduction
$\varepsilon_0+U\rho$. It does not multiply a negative
$M_b-\varepsilon_0$ by an upper survival-defect bound. All forcing is
paid on the full rectangle, and the constant scale preserves the
unit-coefficient heat equation.

## Numerical conclusions and manuscript summary

The final saved 64-time-cell, 512-arc attempt at 192 bits supports these
conservative all-time statements:

| Object | Outward statement |
| --- | ---: |
| Complete local relative-error allowance | $q<0.166454$ |
| Reference discriminant | $D_P>0.1418896$ |
| Strong E10 transfer allowance | $B_{\rm E10}<0.1545636$ |
| Refined transfer allowance | $B_{\rm ref}<0.1364749$ |
| Complete refined lower gap allowance | $D_H>0.0054147$ |

The more detailed Note07 lower bound $D_H>0.005414730535$ is also
consistent with the saved endpoints. The worst E10 complete lower
allowance is approximately $-0.012673966044$; only 22 of the 64 final
time cells have a positive E10 lower allowance, whereas all 64 refined
cells do. The negative old allowance is a failure to certify by that
allowance, not a negative actual discriminant. The refined positivity,
counts, source budget and symmetry certify two distinct real zeros in
this fixed circle on every slice of the stated interval.

The manuscript's Section 8 pilot table, cutoff/source/count interpretation,
alias exponent and known-coverage statements agree with the record and
the code. Its greater-than-11-percent worst-allowance comparison is
supported only as a comparison of the **evaluated envelope radii**:
the largest old evaluated allowance has paid lower bound
$>0.154563575877$, and the largest new allowance has paid upper bound
$<0.136474879299$. Thus the comparison uses a lower old denominator,
rather than dividing two upper bounds. It is not an actual-error,
sharp-information, total-cost or coverage percentage.

The scalar heat envelope is approximately $327656.308219$ in the common
scaled units, exceeding the direct contour envelope
$196587.864108$. The acquired initial rectangle bound is already about
$327394.727397$; the small boundary influence
$<7.358\cdot10^{-15}$ does not remove it. This is a loss of that
conservative positive-kernel/supremum allowance only. It does not exclude
spatially dependent, signed or more sharply acquired heat estimates.

The equally informed direct comparator receives the same refined
allowance and all acquired heat information. No transport representation
advantage follows. The quadratic zero-error control still has vanishing
error allowance and vanishing reference discriminant at its merger, so
the strict complete margin fails there. The inherited Cluster12 screen
is not replaced by a numerical test of modified sources against the
unchanged canonical budget.

## Sole replay and correction check

Final author-ready inputs were pinned before replay:

| Artifact | SHA-256 |
| --- | --- |
| Script | 9c6b6fd6f19cd716582f1569cea0d38ba0da3c7a3a2a4847bac78242d3160cda |
| Canonical Record03 | 6f97ba677fd59382dae07ef185e6ab51352a1aae952c761c230a918b3628fb05 |

The single replay imports the final script and changes only its output
destination to a file under /private/tmp before calling its unchanged
main routine. All source evaluations, all three predeclared schedules,
precision and formulas remain unchanged. The canonical script and JSON
are not written by the assessor.

The sole replay completed in **103.389 seconds**, using the recorded
Python 3.10.0, python-flint 0.9.0 and 192-bit precision. Its scientific
JSON payload matches the canonical record **exactly**, after excluding
only all elapsed-seconds fields. All parameters, source hashes, interval
strings, failed earlier attempts, final gates, numerical allowances and
heat outputs agree. Both pinned canonical byte hashes were unchanged
before and after replay.

The scratch replay JSON has SHA-256
2c486db5d9c87fb1dbf53e89c5f0941b96b4cfba3d6e9267294b6d628a483bec.
Its different byte hash is attributable to the differing elapsed-time
fields; it is not a different scientific payload. Scratch JSON, log and
receipt remain outside the repository. No second full-script run was
performed.

The one correction check verified the author's repair of two minor
documentation issues: the opening runtime version now matches the recorded
Python 3.10.0, and modulus pipes no longer break Note07's Markdown table.
It also verified, at 192 bits using exact rational targets, all five
short outward summaries in the table on every final row, the detailed
$D_H>0.005414730535$ bound, the lower-old-envelope percentage payment,
all final protection/strict-improvement/count gates, all current source
hashes and every imaginary discriminant inclusion. All checks passed.
These are checks of the existing saved endpoints, not new source/domain
evaluations. No mathematical code correction was requested. The initial
failed 16-by-128 enclosure and the intermediate 32-by-256 incomplete
margin remain recorded as failures.

Only this review and its assigned return are assessor-owned outputs.
No parameter expansion, new source, precision campaign or canonical-file
mutation is included.
