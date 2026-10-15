# Review of theta signed cutoffs and analytic logarithmic loss

14 October 2026 (America/New_York). Prepared for Edward Baker with substantial
LLM assistance. Recorded parent model **gpt-6-astra**, reasoning effort
**ultra**, independently checked in the parent chat's source turn metadata.
The reviewing agent used inherited context; its own model and effort were
not independently checked in source metadata. This is internal LLM review,
not external peer review or formal verification.

**Assessment: approved within the stated conditional scope.**
[Note 30](../notes/30_THETA_SIGNED_CUTOFFS_AND_ANALYTIC_LOG_LOSS_20261014.md)
proves two general implications, derives a conditional cumulative-moment
bound with explicit constants, and proposes missing theta arithmetic
estimates. It establishes no new theta sign inequality, collision exclusion
domain, or finite-height certificate. No mathematical correction is required.

## Analytic rigidity and the collision interpretation

The semianalytic graph argument is valid. Failure of every local relative
bound supplies points with E>0, -L>0 and E/(-L) tending to zero. Analytic
curve selection gives a nonconstant positive graph coordinate of finite
vanishing order. E also has finite positive order along the selected arc,
so the inverse graph coordinate grows as a negative power while the
prescribed logarithmic factor grows only as a fixed power of log(1/rho).
This contradicts bounded K. Defining the logarithmic gauge to be zero at
E=0 is necessary in the general lemma; it already forces L>=0 there.
For the actual j=0,1 stationary forms, E=0 makes L_j=0 directly.

The cited analytic curve-selection statement is indeed Ruiz (7.2), printed
p.40, with its proof following on p.41:
[primary article](https://www.numdam.org/item/PSMIR_1986___4_29_0.pdf).
The conclusion applies to singular stationary points and the stated local
semianalytic restrictions. Compact patching needs the covered stationary
neighborhoods. It supplies no uniform bound at infinity or at an uncovered
time boundary, and no coefficient constructed from theta arithmetic.
This sharpens the interpretation of Note 28 without invalidating its
finite-collision proof. The manuscript's universal pole and Note 28's
finite-part and delayed-cancellation refinements remain correctly separated.

## Integer cutoff transfer and complete source tails

The choice of N in (3)--(4), including B=0 and E=0, is correct. For E>0,
log_+(B/E)<=(1+d)ell implies

\[
 N\le\bigl(N_0+1+c^{-1/2}\sqrt{1+d}\bigr)\sqrt\ell.
\]

Thus the displayed D and C=AD^p+1 are valid; local boundedness requires
the stated bounds on A, B, N_0 and c^{-1}, with fixed p. At E=0 the
inequality follows by taking N to infinity before making any division.

The mapping V_N=(log N)/2 gives e^{4V_N}=N^2. Since the retained domain
includes every index entering before V_N, its complement is exactly the
complete common-coordinate tail. Note 19's moment majorant absorbs the
polynomial and logarithmic factors into a smaller positive exponential
constant. Its pair-tail bound (P7), with bounded complete retained masses
and e^{-2ax}<=1 at positive heights, pays all mixed and omitted sectors.
The claims concerning retained energy and the paid stationary defect also
follow from the same jet tails.

The signed retained inequality (5) remains an additional arithmetic
hypothesis for every N, with full physical energy and stationarity. Tail
smallness, arbitrary block phases, or finitely many tested cutoffs do not
establish it. The note states this limitation explicitly.

## Cumulative identity, explicit constants, and source controls

In (6), exchanging the integrals over 0<=r<=R gives
R^2W^2-W integral_0^R(R^2-u^2)a_j(u)du. Adding the displayed tail leaves
W integral_0^infinity u^2a_j(u)du, which is L_j at full stationarity.
Thus (7) pays exactly A_jR^2E. The full factor W satisfies |W|<=sqrt(E)
for both tested j, and the remaining tail is bounded by the j+2 moment.

The complete real envelope used in (8) is established in
[Note 5, equation (4)](../notes/5_COMPLETE_THETA_CENTRAL_ESTIMATE_20261014.md).
For u>=1 and k<=3, the displayed elementary exponent comparison is valid.
Integrating exp[-(pi/2)e^{4u}] using its decreasing derivative gives exactly
the factor 2pi e^{-4R}; hence B=2pi and c=pi/2 are sufficient.

For R=1+(log ell)/4 and c_0=(pi/2)e^4, the tail payment is bounded by
2pi exp(-c_0)E/sqrt(M), separately for E<M and E>=M. The former uses
c_0>=1/2. Also log ell<=sqrt(ell) and 1<=sqrt(ell) give
R^2<=(25/16)ell. Therefore the q=1 coefficient in (9) is correct.
Retaining R^2 gives the claimed squared iterated-log dependence. Both
conclusions remain conditional on (7), or a suitably integrated substitute.

The two-atom control satisfies backward heat, and all stated collision,
energy, Laguerre, and cumulative-moment expansions have the correct signs
and leading coefficients. Its violation of (7) follows from an order-s
positive overshoot against an order-s^2 budget. It is correctly identified
as outside the theta class. The broader limitation for positive smooth,
even, rapidly decaying sources is also supported by the analytic control
in Note 15, Section 5.

## Research scope and validation boundary

The outer-carrier comparison correctly uses nominal real part
1/2+theta/4: a fixed margin theta>2 places it in the absolutely convergent
region, while the stronger weighted-sum replacement below the existing
threshold remains unproved. The referenced
[Polymath Theorem 1.3](https://arxiv.org/html/1904.12438v2#S1)
is the effective heat-flow approximation; it does not itself prove the
proposed threshold improvement. The recommended strip is an explicit
research target with both stationary tests, not asserted coverage.

This audit checked the new analytic arguments, their source connections,
and the parent configuration metadata. It ran no numerical sweep,
quadrature, finite-height certification, or replay of earlier certificates.
It does not independently certify the chat-capture lifecycle. Only this
review file was created by the reviewing agent; no manuscript, snapshot,
commit, tag, or other project file was modified by it.
