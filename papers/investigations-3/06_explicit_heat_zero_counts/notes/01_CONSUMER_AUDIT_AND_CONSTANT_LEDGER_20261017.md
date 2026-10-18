# Opening ledger: explicit heat zero counts

17 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded coordinating model: **gpt-6.1-sol (Codex)**;
reasoning effort: **ultra**, verified from this conversation's metadata.
Three same-model subagents assisted with the consumer inventory, source
audit and separate checking. These are internal LLM checks, not Claude
review, specialist review or formal verification.

**Status: opening consumer audit and constant ledger completed; application
and unconditional explicit count remain staged.** Section 4 proves a
conditional extraction lemma. Its essential comparison hypothesis has not
been made numerical on the proposed domain. No new zero coverage,
computational saving, noncollision result or Newman bound is claimed.

This is the first bounded execution of the [proposal](../research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md).
Read alongside the [result index](../../../../result-summaries/README.md),
especially [11](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md)
and [12](../../../../result-summaries/12_collision_controls_and_screening.md),
and the [avoid index](../../../../avoid/README.md), especially
[01](../../../../avoid/01_restating_the_target.md),
[08](../../../../avoid/08_normalization_and_constant_slips.md),
[10](../../../../avoid/10_numerics_ahead_of_the_question.md) and
[16](../../../../avoid/16_unchecked_imports_and_novelty_claims.md).
The local-count task is quantitative infrastructure, not an RH-equivalent
criterion. Its next acceptance test is an applicable numerical bound.

## 1. Consumer audit and phase decision

The inventory below concerns the current files on 17 October 2026. It is
not an exclusion of future consumers.

| Candidate | Actual quantity and tolerance | Disposition |
| --- | --- | --- |
| Family velocity tail | The newest [Investigation 01 contract](../../01_dirichlet_newman_families/notes/round-1/01_NORMALIZATION_AND_TRANSFER_CONTRACT_CLAUDE_20261017.md), Section 6 item 4, says that counts belong to dormant Route C. There is no selected zero, cutoff, time interval or allowed tail error. | No active consumer. A character-family version would also require conductor-dependent estimates. |
| Theta winding interior | [Physical-jet Note 06](../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/06_WALL_FLUX_AND_CERTIFIED_THETA_WINDING_20261015.md) already certifies two roots on each time face of the box, with spatial range [25,45] and times [0.01,0.2]. It needs exact integers in its winding identity. Its Taylor error is below 4.923e-17 and smallest boundary-coordinate margin exceeds 1.906e-9. | Completed pilot below X=200. A local upper bound cannot substitute for its exact counts. Any replacement must identify the unique integer 2. |
| Outer carrier | [Carrier Note 58](../../../investigations-2/active/21_quaternion_theta_geometry/notes/01_weighted_outer_remainders/58_EXPLICIT_CARRIER_PHASE_AND_CONDITIONAL_HEIGHT_20261015.md) requires d_C(L)=1728 B_C(L)+409/L <= 1/8. Its unresolved input is an exponent-pair constant package. | Does not consume a zero count. |

Consequently no application has passed the proposal's consumer gate. There
is no honest numerical consumer budget to run yet. Retain the default
analytic scope, record the extraction obligations below, and stop before
optimizing a cutoff or launching a zero survey. The downstream arithmetic
check in Section 6 is a check of this ledger, not an application budget.

## 2. Normalization and counting conventions

Use Polymath's physical coordinate and heat time:

\[
 H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
 \qquad H_0(z)=\tfrac18\xi(\tfrac12+iz/2),
 \qquad \partial_tH_t=-\partial_z^2H_t.
\]

An ordinate of magnitude T corresponds to physical height x=2T.
All logarithms below are natural. Define, with multiplicity,

\[
 N_t(X)=\sum_{0<\Re\rho\le X}\operatorname{mult}(\rho),\qquad
 K_t(X)=N_t(X+1)-N_t(X).
\]

Thus the unit window is (X,X+1]. A zero on its right wall is included;
one on its left wall is excluded. Complex conjugates are distinct counted
zeros; a double real zero contributes two. There are no zeros on the
imaginary axis because H_t(iy)>0. The imported strip bound is
|Im rho|<=1 for 0<=t<=1/2. The present target remains 0<t<=1/2, X>=200;
we do not silently extend the source estimates to t=0.

For comparison with cumulative counts retain

\[
 g(X,t)=\frac{X}{4\pi}\log\frac{X}{4\pi}-\frac{X}{4\pi}
       +\frac{11}{8}+\frac{t}{16}\log\frac{X}{4\pi}.
\]

The heat drift is t/16, and 11/8 is the comparison function's constant.
The averaged 7/8 convention does not replace it here. A future contour
count must move a zero-containing boundary outward or use a stated
limiting convention. The upper-count proof below does not require a
zero-free vertical wall.

## 3. Source audit and constant obligations

Primary source: D.H.J. Polymath, *Effective approximation of heat flow
evolution of the Riemann xi function, and a new upper bound for the de
Bruijn-Newman constant*, [arXiv:1904.12438v2](https://arxiv.org/pdf/1904.12438v2),
4 August 2019. Printed pages 4, 6, 9-10, 56-58 and 61 were visually
checked against the [HTML](https://arxiv.org/html/1904.12438). Third-party
PDFs remain outside the repository under LARGE_FILES.md.

Theorem 1.5(iv) already supplies time-uniform local and cumulative
asymptotics. It does not give the numerical constants requested here.
The local proof uses the logarithmic derivative above the zero strip;
the cumulative proof adds argument variation and Jensen. Choose the
local route first, with the explicit disk in Section 4.

| Obligation | Source location | Present state |
| --- | --- | --- |
| Paired Hadamard logarithmic derivative, multiplicities and zero strip | Proposition 3.1 proof, Theorem 3.2, equation (105) | Imported classical analytic inputs; no assumed RH or simplicity. |
| Nonzero comparison function and branches | Equations (6)-(11), (100) | Explicit; checked on the chosen disk below. |
| Off-axis comparison | Proposition 9.1(ii), x sufficiently large and 3<=y<=4 | The published relative error is 0.7, but its absolute height cutoff is unspecified. |
| Extended Riemann-Siegel inputs | Theorem 1.3, equations (20)-(24), and the proof around (99) | Printed numerical constants are for y<=1. The extension used in Section 9 adjusts constants without evaluating them. Recompute bounds for gamma, kappa, Re s_*, e_A, e_B and e_C,0 on 3<=y<=4. |
| Main sum and remaining reserve | Proposition 9.1(ii) proof | Its limiting main-sum majorant is zeta(2)-1. The reserve to 0.7 is 17/10-pi^2/6 > 79/1470. All remaining finite-height errors must fit in this reserve after correcting the coefficient below. No evaluated cutoff is supplied here. |
| Cauchy radius, denominator and local kernel | Section 4 of this note | Explicit: radius 1/2, comparison denominator 3/10, kernel floor 9/41. |
| Carrier derivative | Equations (9), (10), (100); Section 4 below | Explicit: at most (2003/8000) log(X+2). |
| Compact height gap | Source's compactness steps in the proof of (iv) | Unresolved if the extracted cutoff exceeds 200. Must obtain a uniform numerical estimate on the omitted time-height rectangle, or restrict the asserted domain explicitly. |
| Optional cumulative count | Proposition 9.1(iii), Lemma 9.2, final proof of (iv) | Deferred. Needs numerical growth prefactor and exponent, fixed horizontal widths, Jensen radii and denominator, upper-edge phase error, and bounded-height argument variation. These are not obligations of the selected local disk route. |

There is a **printed coefficient discrepancy** on page 57, after (99):
the displayed lower bound for Re s_* uses (t/2) log(x/(4pi)), whereas
the definitions (9), (17) and explicit (21) give t/4. Directly, with
s=(1+y-ix)/2,

\[
 \Re s_* = \frac{1+y}{2}+\frac t2\Re\alpha(s),\qquad
 \Re\alpha(s)=\tfrac12\log\frac{x}{4\pi}+O(x^{-2}).
\]

Related exponent displays on pages 57-58 inherit that discrepancy. Keep
the exact identity

\[
 b_n^t n^{-\Re s_*}
 =n^{-(1+y)/2-(t/2)\Re\alpha(s)+(t/4)\log n}
\]

when rebuilding the off-axis majorants. This identifies a normalization
repair before extraction; it does not refute Theorem 1.5(iv). None of the
conditional proof below uses the discrepant estimate.

## 4. Conditional local bound with all downstream constants evaluated

**Lemma (conditional comparison-to-count extraction).** Fix
0<t<=1/2 and X>=200. Put

\[
 U=X+\tfrac12,\quad w=U+\tfrac72i,\quad
 B_t(z)=M_t((1-iz)/2),\quad F_t(z)=H_t(z)/B_t(z).
\]

Suppose the following quantitative premise is proved on the *whole* disk:

\[
 \sup_{|z-w|\le1/2}|F_t(z)-1|\le\tfrac7{10}. \tag{C}
\]

Then

\[
 K_t(X)\le\frac{82123}{72000}\log(X+2)+\frac{574}{27}
          \le\frac65\log(X+2)+22. \tag{1}
\]

Uniformity of (1) in time and height requires uniformity of (C) over
those times and disks. **Condition (C) has not been established here for
all X>=200.** No displayed numerical A,B in this note is an unconditional
answer to the proposal.

*Proof.* The disk lies in x>=X>=200, 3<=y<=4. The map s=(1-iz)/2
sends it to Re s>=2, away from all branch cuts and zeros of M_t.
Thus F_t is holomorphic on a neighborhood of the closed disk. Cauchy's
estimate applied to F_t-1 and (C) give

\[
 |F_t'(w)/F_t(w)|\le\frac{7/10}{(1/2)(3/10)}=\frac{14}{3}. \tag{2}
\]

At the center s=9/4-iU/2, let L=log(U/(4pi))>0. From (9),

\[
 |\alpha(s)|\le \tfrac L2+\tfrac\pi4+\frac3U+
                    \frac{81}{16U^2}<\tfrac L2+1
                    <\tfrac12\log(X+2),
\]

using log(1+a)<=a, pi<22/7, U>=200 and 4pi>e^2.
Direct differentiation gives

\[
 |\alpha'(s)|\le\frac1U+\frac6{U^2}
                  \le\frac{103}{20000}<\frac3{500}.
\]

With time held fixed, the exact chain rule is

\[
 \frac{B_t'}{B_t}(w)
 =-\frac i2\alpha(s)\left(1+\frac t2\alpha'(s)\right),
 \qquad
 |B_t'/B_t|(w)\le\frac{2003}{8000}\log(X+2). \tag{3}
\]

Evenness, order one and H_t(0)>0 give the paired Hadamard sum.
Its imaginary part at w is the nonnegative scalar sum

\[
 D_t(U):=-\Im\frac{H_t'}{H_t}(w)
  =\sum_\rho\frac{7/2-\Im\rho}
    {(U-\Re\rho)^2+(7/2-\Im\rho)^2}. \tag{4}
\]

Multiplicities occur in the sum. Its absolute convergence follows from
the strip bound and the order-one zero growth, independently of the
count estimate being proved. For a zero in the unit window, set
a=7/2-Im rho and h=U-Re rho. Then 5/2<=a<=9/2, h^2<=1/4, and

\[
 \frac{a}{a^2+h^2}\ge\frac9{41}.
\]

For example, after multiplying positive denominators this follows from
41a-9a^2-9/4=9(9/2-a)(a-1/18)>=0. Summing over just the
window gives K_t(X)<=(41/9)D_t(U). Equations (2)-(4) imply

\[
 K_t(X)\le\frac{41}{9}
       \left(\frac{2003}{8000}\log(X+2)+\frac{14}{3}\right),
\]

which is (1). No root separation, reality or simplicity is used. The
closed horizontal distance bound includes both walls and therefore also
bounds the specified half-open window. This proves the lemma.

An explicit comparison cutoff X_0 would give (1) for
X>=max(200,X_0). The radius already has the correct half-unit allowance:
the leftmost disk point has real part X. The t-dependent real-zero regime
x>=exp(C/t) cannot supply a fixed cutoff uniform as t decreases to zero.

## 5. Collision-control screen and scope

The [control inventory](../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid 02](../../../../avoid/02_shape_only_arguments_and_the_controls.md)
apply to any later noncollision claim. Here a count is allowed to remain
valid at a collision. No control needs to fail the generic implication
from its stated analytic premises to a multiplicity-count upper bound.

| Control family | Premise/scope check |
| --- | --- |
| Euler-factor controls | Their modified source is not the theta source from which a zeta-specific comparison must be derived. Generic Hadamard/strip counting applies whenever those premises hold; no assertion is made that (C) fails at their collision. |
| Weighted-square and reflected controls | Positive-time collisions do not contradict total upper counts. Do not infer theta's comparison to M_t from square support, reflection or positivity alone. |
| Smooth and positive-primitive controls, and the earlier counter-kernels | Their shared shape and positivity properties do not imply theta's arithmetic comparison. If the generic counting premises hold, count the multiple root with its multiplicity. |

This distinguishes an unavailable theta-specific input from a proved
failure of a numerical inequality. No untested control is reported as
rejected. As an exact collision check of the kernel step, the even
polynomial P(z)=(z^2-a^2)^2 has double zeros at +/-a. At U=a, v=7/2,

\[
 -\Im(P'/P)(a+iv)=2/v+2v/(4a^2+v^2),
\]

so the positive double zero contributes two to the local count and obeys
the same kernel inequality. P is the collision-time slice of the heat
solution e^{-(t-T)D^2}P. This check supplies no comparison premise (C)
and no additional zeta evidence.

## 6. Checks, review and next gate

The [exact arithmetic checker](../numerics/check_local_count_reduction.py)
checks the rational constants, kernel factorization, multiplicity handling
and the corrected t/4 chain-rule coefficient. A deliberately excessive
kernel floor 9/40 must fail at the endpoint 9/41 and return a nonzero
exit status. Its small [run record](../numerics/LOCAL_COUNT_REDUCTION_CHECKS_20261017.json)
is an arithmetic check, not a certificate of (C) or of an infinite-domain
count. The [separate review](../reviews/01_OPENING_LEDGER_REVIEW_CODEX_20261017.md)
records the same-model audit and remaining gate.

Reopen constant extraction when a consumer specifies its domain, kernel
or exact-count requirement, numerical error allowance and baseline.
Then derive explicit off-axis bounds with the corrected heat coefficient,
evaluate X_0, address any gap below X_0, and obtain the proposal's Claude
analytic review. Until then retain this staged ledger. No manuscript
milestone has been accepted; no result-summary or avoidance entry is
promoted from this conditional calculation.
