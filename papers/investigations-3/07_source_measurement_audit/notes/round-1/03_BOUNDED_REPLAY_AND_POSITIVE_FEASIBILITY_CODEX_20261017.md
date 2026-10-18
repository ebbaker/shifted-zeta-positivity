# Bounded measurement replay and nonnegative feasibility

17 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model **gpt-6.1-sol (Codex)**, reasoning effort
**ultra**, verified from the session. Three same-model collaborators developed
the evaluation, constrained solves and analytic majorants. These are research
and verification contributions within round one; formal review is deferred
to the round boundary under the user's revised workflow.

**Review correction, 17 October 2026:** [round-two Note 01](../round-2/01_REVIEW_RECONCILIATION_AND_ENDPOINT_NONREALITY_CODEX_20261017.md)
reconciles [Claude's review](../../reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md).
The following tables are prescribed-abscissa results. Within a zero gap,
the sufficient radius can be attained, and nearby positive double jets
can exist. Historical numerical values are unchanged. Prepared for Edward
Baker with substantial LLM assistance, gpt-6.1-sol, effort ultra.

**At the prescribed abscissae, the six-point conditioning table largely
reproduces, but its sufficient radii are far smaller than the actual
equality distances.** Across the 24
fixed combinations, \(r_M/\eta\) ranges from approximately
\(1.64\times10^5\) to \(3.08\times10^{11}\). At \(x=85\), unanchored
recurrence measurements give \(\eta\approx1.1363\times10^{-7}\) and
\(r_M\approx5.90781\). Small sufficient radii therefore do not measure
nearby feasibility at these prescribed abscissae.

The separate coefficient problem has **6 nonnegative feasible cases and
26 infeasible cases** among the 32 declared combinations. All infeasibility
claims now have interval-checked separating witnesses. These statements
concern the fixed supports, tails, anchors and observation points below;
they are not a global exclusion of source approximations.

This executes [Deliverable 2][proposal] and the [opening contract][opening],
using the [result-summary index][results], [control screen][controls] and
[avoid index][avoid]. In particular [avoid 04][a04], [07][a07] and
[09][a09] govern the distinction between certificates, finite scope and
extrapolation. No new height grid, support sweep or \(x=140\) test ran.

## 1 Evaluation and validation

The implementation in [numerics/round-1][numerics] imports no original
solver. Floating production uses 80- and 120-decimal-digit tanh-sinh
quadrature, thin QR and singular values. A separate 448-bit Arb calculation
encloses the integrals and verifies inverse identities, rank, distances and
separating signs. Its secondary Gram identities do not replace the stable
QR/SVD producer. The [summary][summary] binds the code and small records
with hashes; hashes identify files, while interval arithmetic and the
analytic majorants establish the enclosures.

For \(a_n=\pi n^2\), \(k_n=4a_n-9>0\), the elementary bound

\[
e^{tu^2}\phi_n(u)\le2a_n^2e^{-a_n}e^{-k_nu}
\quad(0\le t\le\tfrac14)
\]

gives \(|H_n|\le2a_n^2e^{-a_n}/k_n\) and
\(|H_{n,x}|\le2a_n^2e^{-a_n}/k_n^2\). A geometric majorant sums omitted
nodes. The certified evaluation includes nodes 1 through 10 for the
complete theta jet; only nodes 1 through 6 are free coefficients. Thus
adding evaluation terms is not increasing the approximation space.

Finite integrals use \(0\le u\le U=9/5\). With
\(q_U=a_ne^{4U}\), \(\lambda_U=4q_U-9-2tU\),
\(A_U=2a_n^2e^{9U+tU^2-q_U}\), the omitted integral tails are bounded by

\[
\frac{A_U}{\lambda_U},\qquad
A_U\left(\frac U{\lambda_U}+\frac1{\lambda_U^2}\right).
\]

The first retained integral tail is below \(10^{-1822}\) for the value
and derivative; the omitted coefficient tail after node 10 is included
separately. The ball record contains each allowance, so cancellation is
not protected merely by increasing printed precision. All five time-zero
jets also overlap independent enclosures of
\(\xi((1+ix)/2)/8\) and its physical derivative.

Precision comparison is diagnostic: the maximum relative 80/120 change
in \(C\) is below \(1.5\times10^{-79}\), and in \(r_M\) below
\(4.6\times10^{-70}\). The certified conclusions use the separate ball
records, not these agreement figures. The entire reproducible run takes
about 30 seconds on the recorded environment, within the declared
30-minute limit; the largest child process reports about 32 MiB peak RSS.

## 2 Sufficient radius and actual measurement distance

Use \(N=6\), \(\beta\cdot\delta=0\), separately with \(\delta_1=0\).
Measurement errors are absolute Euclidean errors in the original seven
recurrence rows or twelve reflection rows, without rescaling. With a basis
\(Q\) of the exact tangent constraints, thin QR gives \(MQ=UR\), and
\(A=BQR^{-1}\). The three distinct outputs are

\[
C=\sigma_{\max}(A),\qquad \eta=\|h\|/C,\qquad
r_M=\|A^\dagger h\|.
\]

Both measurement maps are injective on both tangent spaces at the declared
design, and the two-jet map has rank two at all six observations. The
[measurement certificate][measurement] encloses these quantities and
the equality minimizer. The following unanchored values are rounded for
readability; full outward enclosures are in that record.

| \((t,x)\) | Recurrence \(\eta\) | Recurrence \(r_M\) | Reflection \(\eta\) | Reflection \(r_M\) |
| --- | --- | --- | --- | --- |
| \((0,30)\) | 7.92121 | \(3.51006\times10^8\) | 2.14475 | \(2.27234\times10^7\) |
| \((0,44.1303)\) | 0.114025 | 534308 | 0.0308736 | 34590.1 |
| \((1/4,44.1303)\) | 0.121704 | 83529.6 | 0.0329528 | 5407.49 |
| \((0,60)\) | \(6.01494\times10^{-4}\) | 48523.0 | \(1.62861\times10^{-4}\) | 3141.27 |
| \((0,70)\) | \(5.05416\times10^{-5}\) | 1116.03 | \(1.36847\times10^{-5}\) | 72.2492 |
| \((0,85)\) | \(1.13632\times10^{-7}\) | 5.90781 | \(3.07672\times10^{-8}\) | 0.382459 |

The worst jet direction in \(C\) is poorly aligned with the particular
baseline jet that must be cancelled. The least singular direction also
matters to \(r_M\); substituting the largest singular value alone loses
that information. The ratio is even larger in the anchored cases.

Only the unanchored recurrence minimizer at \((1/4,44.1303)\) already has
all resulting coefficients positive. The negative minimizers in the
other 23 measurement problems do not establish positive infeasibility;
the separately declared coefficient feasibility cases below supply that
calculation only at their two fixed points.

## 3 Nonnegative coefficient feasibility

The 32 cases use only \((t,x)=(1/4,44.1303),(0,60)\), supports
\(N=2,3,4,6\), theta or zero tails, and anchoring off or on. The exact
normalization is \(\sum\beta_na_n=1/2\). The theta-tail class keeps
\(a_n=1\) beyond \(N\); the zero-tail class keeps \(a_n=0\) there.

After eliminating the fixed first coefficient when anchored, let \(J\)
be the free nodes, \(m\) the available primitive mass and \(r\) the
remaining target jet. Here \(m>0\). Define

\[
p_n=B_n/\beta_n,\qquad q=r/m.
\]

Nonnegative feasibility is exactly
\(q\in\operatorname{conv}\{p_n:n\in J\}\). Each infeasible case has a
stored decimal multiplier \(y\) whose interval evaluation proves

\[
y\cdot(p_n,1)>0\quad(n\in J),\qquad y\cdot(q,1)<0.
\tag{1}
\]

This is a strict Farkas contradiction, not a sign check on an unconstrained
minimizer. All 26 witnesses pass. In the six feasible cases the exact
equality minimizer for the first-\(N\) coordinate Euclidean norm is itself
strictly positive on the free nodes, so it is also the nonnegative optimum
for that coordinate norm. No boundary
optimum needs to be inferred from a numerical tolerance.

| Observation and anchor | \(N=2\) | \(N=3\) | \(N=4\) | \(N=6\) |
| --- | --- | --- | --- | --- |
| \((1/4,44.1303)\), unanchored | Equality infeasible | Nonnegative feasible | Nonnegative feasible | Nonnegative feasible |
| \((1/4,44.1303)\), anchored | Equality infeasible | Equality infeasible | Equality feasible, nonnegative infeasible | Equality feasible, nonnegative infeasible |
| \((0,60)\), unanchored | Equality infeasible | Equality feasible, nonnegative infeasible | Equality feasible, nonnegative infeasible | Equality feasible, nonnegative infeasible |
| \((0,60)\), anchored | Equality infeasible | Equality infeasible | Equality feasible, nonnegative infeasible | Equality feasible, nonnegative infeasible |

Every entry holds for both declared tails. Equality infeasibility is
verified by a nonzero augmented minor, not by counting equations. Of the
32 cases, 20 admit real equality solutions. The
[feasibility certificate][feasibility] encloses their Euclidean minima and
the source endpoint, and verifies all positive/infeasible classifications.

For the unanchored theta-tail \(N=6\) problem at \((1/4,44.1303)\),

\[
a\approx(1.000034707892,\ 0.879260345485,\ 57641.757060421,
1.000039471614,\ 1,\ 1),
\]

with first-six-coordinate Euclidean distance approximately
\(57640.75706055\). Its full \(\beta\)-weighted \(\ell^1\) value is
approximately \(4.14874985\times10^{-5}\), evaluated at that Euclidean
minimizer. It has not been optimized in the weighted metric. At \((0,60)\)
the unanchored third coefficient is approximately \(-33482.9898\), and
the separate witness excludes every nonnegative feasible coefficient vector
in the declared finite class.

For zero-tail sources the full raw \(\ell^2\) distance from theta is
infinite, despite a finite first-\(N\) coordinate distance. The full
weighted distance includes \(\sum_{n>N}\beta_n\). The zero-tail solution
near the inherited three-square control is not identified as exactly that
control: the original control also imposes a source endpoint condition
and uses its own interior collision abscissa. The replay fixes the bracket
endpoint \(44.1303\), and does not add that endpoint constraint.
In fact the unanchored three-node source has first odd source derivative
approximately \(6.25850\times10^{-6}>0\) for either tail, whereas the
canonical three-square control makes that derivative exactly zero.

## 4 Disposition within the current round

The inherited constants \(C\) agree to roughly eleven relative decimal
places. The original \(x=85\) baseline jet has about
\(1.14\times10^{-5}\) relative discrepancy, illustrating why its printed
digits did not establish quadrature accuracy. These observations repair
the diagnostic record without turning it into a uniform height theorem.

The bounded replay supports a precise finite-space conclusion and the
[quantitative analytic note][bounds] supports the unbounded asymptotic
construction. Their quantifiers differ: finite positive infeasibility
at the prescribed \(x=60\) does not contradict feasibility at another
abscissa in the same zero gap or eventual high-height feasibility.
An error description such as sixteen digits still needs row units and
an absolute or relative observation model. The \(x\approx140\) threshold
is left as an extrapolation, outside the conclusions.

The inherited [collision controls][controls] retain their exact tail,
reflection and arithmetic qualifications from the opening note. A
near-control coefficient solve is an implementation check, not arithmetic
discrimination; the reflected and Euler-factor controls are not silently
inserted into this finite coefficient space.

The research round continues without a note-by-note review gate. Its next
analytic decision is whether a concrete direction pair makes the explicit
onset budget useful, or whether to record that budget as too coarse. Any
round review should assess the accumulated analytic and numerical record
together; no formal review or cross-model reconciliation is claimed here.

[proposal]: ../../research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md
[opening]: 01_OPENING_ANALYTIC_AUDIT_AND_REPLAY_CONTRACT_CODEX_20261016.md
[bounds]: 02_EXPLICIT_THETA_JET_AND_ENDPOINT_BOUNDS_CODEX_20261017.md
[numerics]: ../../numerics/round-1/README.md
[summary]: ../../numerics/round-1/REPLAY_SUMMARY.json
[measurement]: ../../numerics/round-1/CERTIFIED_MEASUREMENTS.json
[feasibility]: ../../numerics/round-1/CERTIFIED_FEASIBILITY.json
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a04]: ../../../../../avoid/04_counts_and_precision_as_evidence.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a09]: ../../../../../avoid/09_round_floors_and_fitted_laws.md
