# Conservative heat baseline: CTF-E01 R1 return

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**. Investigation05 chat0009, **Continue conservative theta flow**.

**Status: bounded floating measurement complete.** All 55 prescribed
source/time/frequency/auxiliary-time cases, comprising 110 scalar heat
values, were acquired at 30 and 50 decimal digits. No subdivision refinement
was needed. The moment-corrected diagnostic becomes informative sooner than
the mass-only diagnostic on the small theta signals, but this fixed heat
measurement supplies no collision exclusion or demonstrated cost advantage
over the matched direct observations. Stop E01 here.

| Next task | Type | Recommended model | Readiness | Deliverable |
| --- | --- | --- | --- | --- |
| CTF-B01 | B — brainstorm | Astra: flow/observable choice remains conceptual | Ready; E01 is supporting evidence | One conservative candidate with complete invariant/jet/domain accounting and an E02 contract, or a scoped failure of the examined classes |
| CTF-E02 | E — execution | Sol | Gated by B01 | Routine identities and the selected candidate's fixed finite comparison |

The [sole live register][progress] owns status. This returns the frozen
[R1 request][packet] using [Note25][n25], whose SHA-256 matches the issued
request. [Code][code], [record][record] and [assessment][review] retain the
calculation and its limits. The manuscript was not changed.

## 1. Calculation and interpretation

Use exactly the packet's epsilon=1 and central normalized quantity F, with
r=exp(2u). The source implemented is

\[
\rho_t(u)=\pi e^{tu^2+5u}\sum_{n\ge1}
 n^2(2\pi n^2e^{4u}-3)e^{-\pi n^2e^{4u}}.
\]

Indeed spherical volume gives H=(1/8) integral r^(3/2)Q_t(r)cos(a log(r)/2)dr;
dr=2r du gives rho=(1/4)r^(5/2)Q_t. This checks the coordinate factor.
The computation retains n<=6 on u<=2 for theta, and u<=6 for the control.
The complete source is the mathematical input; omitted terms and outer
tails are paid below. Positive moments C_0,C_2,C_4 are reused across a and s.
The a=0 first derivative is identically zero and is supplied by symmetry.

The record stores all H_k, M_(2,k), C_(m,k), F_(s,k), physical densities,
R0=F-H, R1=F-H+M2/(4s), their allowances B0=C2/(4s), B1=C4/(32s^2),
and acquisition diagnostics. Reported C2/C4 allowances include their
floating acquisition diagnostics, as well as source tails. This is not a
rigorous numerical upper enclosure.

An allowance is called **informative in the tables below** only when its
ratio to |H_k| is below one and H_k is resolved by the stated floating
diagnostic. R0 uses B0/|H|; R1 uses B1/|H|. This merely compares finite
sampled scales. Ratios are undefined for zero or unresolved denominators.
The record also gives B0/|F| and B1/|M2/(4s)|, with their denominators named;
these answer different questions. Recovering H from F+M2/(4s) requires the
extra signed moment and is included in the cost accounting.

This is a quantitative diagnostic milestone under [avoid01][a01], not an
RH-equivalent criterion. The [result index][results], [avoid index][avoid],
[control screen][controls], [geometric-result scope][geometry],
[finite numerical question][a10] and [known-result test rule][a11] govern
its interpretation. The pre-existing decay theorem is an implementation
check, not the substantive finding of this run.

## 2. Moment sizes and useful listed scales

Rounded positive majorants are:

| Source/time | k | C0 | C2 | C4 |
| --- | --- | --- | --- | --- |
| Theta, t=0 | 0 | 0.0621401 | 0.0909863 | 0.144292 |
| Theta, t=0 | 1 | 0.00538218 | 0.00952368 | 0.0182553 |
| Theta, t=1/4 | 0 | 0.0623203 | 0.0913507 | 0.145088 |
| Theta, t=1/4 | 1 | 0.00541227 | 0.00959127 | 0.0184185 |
| Control, t=T_c | 0 | 3.98802 | 58.9887 | 5854.05 |
| Control, t=T_c | 1 | 1.75000 | 54.4398 | 7983.82 |

For theta, k=0 at a=0 and both components at a=2sqrt(6) have B0/|H|<1
and B1/|H|<1 at every listed s, beginning at 1. At a=0,k=1 every
signed quantity is exactly zero; that symmetry is not a collision.
For the smaller theta signals, the first useful listed s is:

| t | a | k | H_k (rounded) | First s: B0/abs(H)<1 | First s: B1/abs(H)<1 |
| --- | --- | --- | --- | --- | --- |
| 0 | 28 | 0 | 2.51618e-5 | none | 16 |
| 0 | 28 | 1 | -1.00561e-4 | 64 | 4 |
| 0 | 30 | 0 | -8.82122e-5 | none | 16 |
| 0 | 30 | 1 | -2.26622e-5 | 256 | 16 |
| 1/4 | 28 | 0 | 1.15516e-5 | none | 64 |
| 1/4 | 28 | 1 | -9.59665e-5 | 64 | 4 |
| 1/4 | 30 | 0 | -9.44448e-5 | 256 | 16 |
| 1/4 | 30 | 1 | -1.98269e-5 | 256 | 16 |

Here “none” means none of {1,4,16,64,256}. Every later listed s after the
first also qualifies because H and the moment constants are fixed. At
s=256, the four k=0 mass-only ratios for (t,a)=(0,28),(0,30),(1/4,28),
(1/4,30) are 3.5313, 1.00727, 7.72274, 0.944570. Their corrected
ratios are 0.00273445, 0.000779980, 0.00598908, 0.000732525.
The improvement is the already specified moment correction, acquired at
additional cost, not a new signed theta inequality.

For the control off collision, at a=2sqrt(6) +/- 1/4, the k=0
mass-only ratio never drops below one on the grid, whereas its corrected
ratio first does so at s=256. For k=1, the mass-only ratio first qualifies
at 256 and the corrected ratio at 64, on both sides. Unfavorable cases
remain in the record.

## 3. Exact collision control

At a*=2sqrt(6), the comparison uses **H=H_a=0 exactly** from the packet's
polynomial Gaussian transform, never a quadrature residual. Independently,
the Gaussian half-line generating function and its derivative provide
nonquadrature references for the signed moments and positive majorants;
all agree within the requested absolute diagnostic target. The code
contains the explicit generating formulas.

At this event, the measured signed moments are
M_(2,0)=0.913928750818 and M_(2,1)=15.4899505545. Absolute normalized
signals and corrected remainders are:

| s | abs(F0) | abs(R1,0) | B1,0 | abs(F1) | abs(R1,1) | B1,1 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.651373 | 0.879855 | 182.939 | 0.190434 | 3.68205 | 249.495 |
| 4 | 0.430692 | 0.487812 | 11.4337 | 0.341516 | 0.626606 | 15.5934 |
| 16 | 0.0985417 | 0.112822 | 0.714606 | 0.207657 | 0.0343732 | 0.974588 |
| 64 | 0.00844666 | 0.0120167 | 0.0446629 | 0.0643378 | 0.00383021 | 0.0609118 |
| 256 | 7.90594e-5 | 8.13449e-4 | 0.00279143 | 0.0157459 | 6.19014e-4 | 0.00380698 |

At s=256, the physical density components are approximately -4.33290e-10
and -8.62965e-8. The k=0 normalized signal is positive at s=64 and negative
at 256; no fixed finite-time sign or monotone signal was assumed.
B1/|M2/(4s)| at s=256 is 3.12762 for k=0 and 0.251670 for k=1:
the displayed k=0 allowance still cannot resolve even the next moment's
leading effect. No lower decay bound is inferred from upper estimates or
from the finite samples.

The control satisfies every premise of the generic heat/moment theorem.
It fails the full canonical theta-source premise. The other registered
smooth controls likewise remain admitted on their stated convergence and
moment domains; their missing arithmetic/reflection inputs are listed in
the [control screen][controls]. Atomic sources remain outside the L1
density formulation. This run introduces no canonical separating premise
and no new claim that excludes any of those controls.

## 4. Truncation and numerical errors

Here are explicit standard tail bounds used in the computation. For theta,
put b=9+2m. The inequalities e^(4u)>=1+8u^2 and positivity give

\[
\rho_t(u)\le2\pi^2 e^{-t/8}e^{9u}
\sum_{n\ge1}n^4e^{-(\pi n^2-t/8)e^{4u}}.
\]

For the omitted indices n>N, set q=N+1,
d=4(pi*q^2-t/8)-b and eta=(1+1/q)^4 exp(-pi(2q+1)).
Linearizing e^(4u) below by 1+4u and summing the decreasing index ratios gives

\[
B_N(m,k)\le\frac{2\pi^2q^4e^{-\pi q^2}k!}
 {d^{k+1}(1-\eta)}.
\]

For u>U, let E=exp(4U), alpha=pi-t/8,
D=1-16exp(-3pi E), lambda=4alpha E-b. The full theta index sum is bounded
by its first term divided by D. The exponential tangent at U yields

\[
B_U(m,k)\le\frac{2\pi^2e^{-t/8+bU-\alpha E}}D
\begin{cases}1/\lambda,&k=0,\\U/\lambda+1/\lambda^2,&k=1.\end{cases}
\]

All displayed denominators are positive for the selected parameters.
For the control, write lambda_p=8U-2m-p/U. The logarithmic derivative of
u^p exp(-4u^2+2mu) is decreasing beyond U, so

\[
B_U^*(m,k)\le e^{-4U^2+2mU}
\left(\frac{64U^{4+k}}{\lambda_{4+k}}+
\frac{6U^k}{\lambda_k}\right).
\]

H and F use m=0, M2 uses m=2, and C_m uses its corresponding m.
These formulas pay the full source beyond both cutoffs. The theta index
bound is at most 1.11e-65 for k=0 (1.85e-68 for k=1), while its outer
tail is below 1.23e-4015 on this grid. The largest control outer-tail bound
is 2.581e-38, for m=4,k=1. These are floating evaluations of analytic
bound formulas, not directed-rounding certificates.

Numerics used mpmath 1.4.1, Python 3.12.14, Gauss-Legendre quadrature with
maxdegree=5 and the saved fixed panel endpoints. Both precision passes
have their own quadrature estimates. The record separates:

1. theta-index bound;
2. outer-u bound;
3. quadrature error estimate from the library;
4. absolute 30-versus-50-digit difference.

The reported absolute acquisition diagnostic adds the first two, the
larger quadrature estimate, and the precision difference. It is heuristic
as a numerical enclosure because the latter two do not rigorously bound
quadrature aliasing or roundoff. Their separate values are retained. Every
quantity met the requested 1e-12 times its appropriate positive-majorant
target; the largest diagnostic divided by that majorant was about
5.72e-27. The largest absolute precision difference was 2.94e-28, on the
large control C4,1. There were no unresolved quantities or added cases.

Two read-only same-model checks found reporting issues before delivery:
positive-moment acquisition diagnostics needed inclusion in B0/B1, and
ratios needed an explicit unresolved-denominator gate. Those reporting
corrections used the saved raw values without repeating quadrature. The
saved code also preserves single-precision data and earlier attempts on
future budget/refinement paths. The executed and delivered code hashes
are separately recorded. Neither a budget stop nor refinement occurred in
this run; those recovery paths are not claimed as experimentally tested.

## 5. Measured matched cost and disposition

Both columns below include the same 30/50-digit repeats, complete source
tail payment and quadrature method. Counts are actual scalar integrand
calls, not just distinct source nodes. Direct H/H_a are acquired once per
frequency and reused for all five s values. Symmetry-zero observations and
the identity C0,0=H(t,0) avoid redundant integrations.

| Acquisition stage, entire fixed grid | Scalar calls | Measured integration seconds |
| --- | --- | --- |
| Direct H/H_a | 13,176 | 0.343574 |
| Additional positive moments | 10,632 | 0.0990800 |
| Additional signed M2 moments | 13,512 | 0.203460 |
| All five central heat observations | 56,232 | 1.09446 |
| Total | 93,552 | 1.74058 |

The complete run through initial reporting took 1.78331 seconds, well below
250,000 calls and 900 seconds. Source evaluations and Gauss-Legendre nodes
were cached across quantities; direct acquisition ran first and paid the
cold source and initial quadrature setup. Its source computation alone
took 0.130110 seconds; subsequent stages required only 0.000425252 seconds
of new source work. Thus the incremental heat/moment measurements benefit
from warm shared caches. The extra work is primarily the additional
scalar quadratures and their kernels, not repeated theta summation.
Wall-clock timings are one local run, not a stable performance law.

The five-s heat observations plus their extra moments require 80,376
additional calls and 1.39700 measured seconds: 6.10 times the direct call
count and 4.07 times its time. Including direct validation gives 7.10 times
the direct call count. A single listed heat scale itself costs
10,584–11,592 calls across the grid, before the 24,144 calls for extra
moments; it also establishes no acquisition advantage in this setup.
For the control, exact analytic H/H_a formulas are available and avoid
quadrature entirely. The quadrature comparator therefore does not describe
the cheapest available direct control method.

**Disposition:** the baseline is affordable on these low finite samples,
but its mass-only allowance loses small signals and the moment correction
purchases better finite-time information with extra integrals. It provides
no measured saving, canonical separation, zero-free region or threshold
gain. This is a scoped completed E01 return, not an exclusion of other
conservative evolutions; follow [avoid07][a07]. B01 should address what new
flow/observable contract can supply useful information beyond this generic
cancellation, and name the additional canonical comparison it would need.
No new flow, observable, larger scan or numerical campaign was started.

**Next: [B] CTF-B01 — Astra**, under the brief in [Continuation26][continuation].

[progress]: ../research-progress/04_CONSERVATIVE_THETA_FLOW_RESEARCH_PROGRESS_20261028.md
[packet]: ../research-progress/handoffs/CTF-E01_BASELINE_HEAT_MEASUREMENTS_REQUEST_R1_20261028.md
[n25]: 25_TOTAL_INTEGRAL_CONSERVATION_AND_DIRECTION_FREE_HEAT_FLOW_20261027.md
[continuation]: 26_CONSERVATIVE_THETA_FLOW_CONTINUATION_20261028.md
[code]: ../numerics/16_measure_conservative_heat_baseline_20261028.py
[record]: ../numerics/16_CONSERVATIVE_HEAT_BASELINE_MEASUREMENTS_20261028.json
[review]: ../reviews/15_CONSERVATIVE_HEAT_BASELINE_E01_ASSESSMENT_20261028.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../avoid/10_numerics_ahead_of_the_question.md
[a11]: ../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md
