# Current ansatz, AN06 assessment, and next research steps

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.
Ansatz chat0004, thread `01a1765a-5c4e-7dd1-9de8-d70dd1725e34`.

**Scope:** internal source-level analytical and planning review. This is
a different-model reading of Sol's AN03--AN06 work, sharing its classical
inputs and some inherited premises. It is not independent specialist
validation or the parent's HDA-20 full-chain audit. No new asymptotic
theorem, numerical experiment, manuscript edit, or task dispatch.

## Evidence and disposition

Read the complete [current manuscript](../manuscript/main.tex), current
[Overview02](../research-overview/02_EVOLUTION_ASYMPTOTICS_RESEARCH_OVERVIEW_20261025.md)
and [Progress02](../research-progress/02_EVOLUTION_ASYMPTOTICS_RESEARCH_PROGRESS_20261025.md),
[Note10](../notes/10_FIRST_NEGATIVE_TIME_EVOLUTION_CORRECTION_20261025.md),
[Note12](../notes/12_COMPACT_NEGATIVE_TIME_FAMILY_20261025.md),
[whole-chat Note14](../notes/14_CHAT0003_RESEARCH_SUMMARY_20261025.md),
Reviews07,09,10 and the prepared [A08-AN01 r1](../research-progress/handoffs/HDA-A08-AN01.md).
Checked the supersession notices in the older overview/progress, parent
Note27's source-versus-estimate domains, the parent Summary62, and the
repository result and avoidance controls.

The current TeX and PDF hashes match the [AN06 build record](../manuscript/BUILD_RECORD_20261025_A02_AN06.json):
source `aa7ec6e94e9478a3aa11f4b821b2c56477caeeaaf477063b6e57b4b0f9019037`,
PDF `49e9db41dcd59733c177dae73fe73bd4842c69b83bbe80e14f99caafefe612bd`.
That record reports 33 pages, no warnings, and all-page visual inspection.
This review did not repeat compilation or visual QA. Hash agreement
identifies the reviewed version; it does not validate mathematics.

No blocking inconsistency was found in the selected correction/residual
algebra, its error accounting, or the live scope statements. In particular,
hand expansion of Note12 CF14 agrees with the product residual, the
Gaussian-moment normalizations retain their transverse/inverse-time costs,
and the error ledger separates initial mismatch from evolution error.
The full inherited classical proof chain was not independently audited.
Preserve the source status: **proved in-note from named inputs**, with the
existing same-model assessments; this additional internal review does not
close physical transfer, endpoint uniformity, or HDA-20.

## What has improved

AN03 improves the field, spatial derivatives through three, and first time
error from `C|G|X^-3/4` to `C|G|X^-5/4` on 1<=T=-t<=2. The actual
residual and its first spatial derivative are `C|G|X^-7/4`. AN05 extends
those powers to every declared fixed 0<tau<=T<=B with displayed endpoint
factors and sufficient height conditions. AN04 and AN06 integrate those
results; they add no further estimate.

The gain has two indispensable parts: the first mode-curvature correction
reduces the arithmetic evolution error to `G X^-7/4`, while K=1 real RS
data reduce the initial mismatch to `G X^-5/4`. The latter is the limiting
displayed term. Improving only the mode residual while keeping K=0 would
leave the earlier initial allowance. Fixed-radius complex buffers pay
spatial derivatives without logarithmic losses.

## The current negative-time formula

Let s=(1+iz)/2, M(w)=w(w-1)pi^(-w/2)Gamma(w/2)/16, alpha=M'/M,
and G(z)=[M(s)M(1-s)]^(1/2), positive at the real chart center. Freeze
L=log(X/(4pi)), N=floor(sqrt(X/(4pi))) and
V_B=8 sqrt(max(1,B)) L. With epsilon=+1,-1, define

\[
w_\epsilon=(1+\epsilon iz)/2,\quad
h_{\epsilon n}=M(w_\epsilon)n^{-w_\epsilon},\quad
\beta_{\epsilon n}=\frac{\epsilon i}{2}(\alpha(w_\epsilon)-\log n),
\quad\gamma_\epsilon=-\frac14\alpha'(w_\epsilon).
\]

The full retained-integral ansatz is

\[
F_{X,B}^{[1]}(-T,z)=
\sum_{\epsilon=\pm1}\sum_{n\le N}h_{\epsilon n}e^{T\beta_{\epsilon n}^2}
\{1+\gamma_\epsilon(T+2T^2\beta_{\epsilon n}^2)\}
+\int_{X-V_B}^{X+V_B}\frac{e^{-(z-u)^2/(4T)}}{\sqrt{4\pi T}}
Q_{X,1}(u)\,du.
\]

Here S_j(u)=sum_(epsilon,n<=j) M((1+epsilon i u)/2)n^(-(1+epsilon i u)/2),
Q_(X,1)=S_(m(u))-S_N+R_(m(u),1), and m(u)=floor(sqrt(u/(4pi))).
Writing a_u=sqrt(u/(4pi)), p_u=1-2(a_u-m(u)), and
U_u=exp(-i[(u/4)log(u/(4pi))-u/4-pi/8]),

\[
R_{m,1}(u)=2\Re\left\{(-1)^{m-1}M((1+iu)/2)U_u a_u^{-1/2}
\bigl[C_0(p_u)+a_u^{-1}C_1(p_u,1/2)\bigr]\right\}.
\]

These are the imported classical RS coefficients, with exact adjacent
cutoff transfer. The real initial partitions and endpoints are fixed in
z,T; the integral itself solves the homogeneous heat equation. There are
still order sqrt(X) modes. An integral-free expression for the complete
correction, its coefficient regularity and a useful cost theorem remain
open. The elementary-arm correction is equivalent at the assessed [1,2]
accuracy; its wider compact-family extension has not been separately
claimed. The older growing-order representation retains stronger
outer-scale accuracy on 4/L<=T<=2 and must not be replaced by the new
fixed-order theorem in that role.

## Why the scale distinction determines the next steps

On the real line G(X) is asymptotic to
pi^(1/4) X^(7/4) exp(-pi X/8)/32. Thus the new field allowance is small
relative to this gamma envelope. But conversion to the elementary outer
carrier introduces

\[
X^{-5/4}\exp(TL^2/16-\pi^2T/64).
\]

At each fixed T>0, its logarithm has a positive quadratic term in L,
which eventually exceeds the negative linear term. No fixed algebraic
power X^-p offsets that loss. This observation concerns these displayed
allowances; it neither lower-bounds the actual error nor rules out a
cancellation-preserving resummation. Near-cutoff absolute populations are
not leading asymptotics of the signed field, and none of these estimates
asserts H/F tends to one across zeros.

The endpoint ledger is useful input for future joint limits. Such a
result must verify all endpoint-dependent factors and onset inequalities
along the chosen moving endpoints and prove the desired error decays.
The current fixed-family statement is not that additional theorem.

## Recommended next deliverables

1. **Analysis — Sol: execute existing A08-AN01 r1 on [1/2,1].** Keep its
   flexible o(E_o) field target, full buffers, j<=3, direct first time and
   actual residual. Start from the canonical positive Gaussian identity.
   Parent GO6 holds for all positive t; GO7's original estimate requires
   a compact interval strictly above64. Polymath Proposition9.1 allows
   0<t<=1/2 and |y|<=10, with x>=exp(C/t) for its two-arm estimate.
   Neither directly supplies the requested new slab and arbitrary buffers.

2. **Make arithmetic error determine approximation order.** From the
   existing elementary weights,
   w_2=2^(-1/2) exp(t(log2)^2/4) (X/(4pi))^(-t log2/4).
   At t=1/2 its height exponent is log2/8, much smaller than 1. This
   component envelope is larger than a gamma correction of order
   log^2(X)/X. It is not an actual error lower bound, but it shows why
   an inverse-height gamma expansion alone is not a complete precision
   budget. A leading two-arm formula with a slower proved vanishing error
   is an admissible first outcome; retain more arithmetic modes only when
   the target accuracy requires them. No new remainder rate is asserted.

3. **After one successful slab, seek a parameterized compact-positive
   theorem and paid overlaps.** Avoid treating many isolated slabs as an
   all-time theorem. Preserve the shrinking through-zero domain, the
   existing [-2,0] join and every derivative-of-cutoff residual.

4. **Keep joint limits and physical transfer as distinct next questions.**
   On the negative side choose a specified moving time-height regime and
   an error scale before seeking the large-T Gaussian overlap. For physical
   transfer first prove a concrete regulator-uniform weak/collar comparison,
   retaining actual signed covariance and residual forcing. The t=64 fine
   transition remains supporting work under the current priority order.

No new numerical campaign or further manuscript growth is needed to make
the present next step concrete. A08-AN01 is already prepared and remains
unexecuted. HDA-A02 Partial, parent HDA-17 Partial, HDA-18 Gated and
HDA-20 unfulfilled remain unchanged.

## Sources, controls, and review limits

Reopened [Polymath v2](https://arxiv.org/html/1904.12438v2), equations35--38,
Proposition6.2 and Proposition9.1, and [DLMF5.11](https://dlmf.nist.gov/5.11).
The named C1 construction remains an import through the inspected
restatement; no independent audit of the Arias coefficient provider or
new coefficient derivative theorem was made. Existing reading-copy
provenance remains in the [reference catalog](../references/README.md).

Classification: a quantitative approximation program under
[avoid01](../../../../../avoid/01_restating_the_target.md). Read the
[result index](../../../../../result-summaries/README.md), specifically
[heat-flow11](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md)
and [controls12](../../../../../result-summaries/12_collision_controls_and_screening.md),
and the [avoid index](../../../../../avoid/README.md), especially
[shared premises02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scope07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and
[separate bounds12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
Heat identities also hold for the collision controls. Euler-factor and
finite-prime perturbations fail the unchanged full canonical coefficients;
weighted-square/theta-cutoff controls fail the full completion/RS identity;
reflected, smooth-shape, positive-primitive, counter-kernel and fixed-event
controls lack the same complete canonical gamma/arithmetic identity.
Those failed premises supply no new noncollision conclusion.
