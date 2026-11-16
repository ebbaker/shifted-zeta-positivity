# JCH-B01 — choose the finite-chain scalar readout

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Dispatch selection: **gpt-6-astra,
ultra**. Actual backend model and reasoning effort are not exposed by the
available session metadata; the dispatch selection is not backend attestation.

**B01 completed with a fixed derivation contract, not a proved estimate.**
The sole live status is the [JCH register](../../research-progress/01_JACOBI_CHAIN_RESEARCH_PROGRESS_20261113.md).
One round compared exactly three formulations. The next task is
**[E] JCH-E01 — GPT-6.1 Sol / Ultra**, under the frozen
[r1 request](../../research-progress/handoffs/JCH-E01-r1.md).

| Formulation | Added information required | Decision in this round |
| --- | --- | --- |
| State mass outside a height-dependent polynomial prefix | A quantitative approximation estimate for the whole prepared state, or growth bounds for the couplings; a separate scalar cancellation argument would still be needed | Park for this round; no obstruction to this class is proved |
| Site-by-site recursive amplitudes | Explicit usable coefficient bounds and propagation argument, beyond the inherited recurrence | Park for this round; the recurrence alone is not a quantitative output |
| Literal scalar readout of a separately evolved finite principal chain | Exact monic polynomial norm at its boundary, with an available moment majorant | **Select**; classical Gaussian quadrature gives an explicit absolute error and a direct coefficient consumer |

The selected question is whether the (N)-site approximation

\[
H_N(\tau,x)=\frac{Z_*}{2}
\langle e_0,e^{-\tau J_N^2}e^{ixJ_N}e_0\rangle,
\quad J_N=\Pi_NJ_*\Pi_N|_{\operatorname{span}(e_0,\ldots,e_{N-1})},
\]

has the quantitative full-source error

\[
|H_{1/2-\tau}(x)-H_N(\tau,x)|
\le \frac{Z_*}{2}h_N S_N(\tau,x),\qquad
S_N(\tau,x)=\sum_{k=0}^N
 \frac{\tau^k x^{2N-2k}}{k!(2N-2k)!},                 \tag{B1}
\]

where (h_N=\int P_N^2d\mu_*=prod_{j=1}^Na_j^2), (P_N) is monic,
and (0\le\tau\le1/2), (x\in[-X,X]), (X<\infty), (N\ge1).
The method is fixed: principal-chain Gaussian quadrature, real cosine
Hermite remainder, then Gaussian averaging in height. E01 must prove it
with full constants and domains; these displayed formulas are the request's
targets, not a substituted proof.

There is a usable unconditional fallback without a new coefficient theorem.
The variational monic norm bound (h_N\le m_{2N}\le N!M_1), with

\[
M_1=\int e^{u^2}d\mu_*
 =\frac{\int e^{3u^2/2}\Phi(u)du}{Z_*}<\infty,
\]

should give the explicit uniform envelope

\[
\sup_{\tau\in[0,1/2],\,|x|\le X}|H-H_N|
 \le\frac{Z_*M_1}{2}\,2^{-N}\cosh(X\sqrt{2N}).       \tag{B2}
\]

E01 will verify this algebra and an explicit sufficient (N(X,\epsilon)).
The extra Gaussian moment is a complete-source integral, not a numerical
certificate. Extending a source moment to exponent (3/2) does not enlarge
the physical heat-time domain. The complete domination in the GNP source
already supplies all such moments.

This is an **intermediate approximation milestone** under
[avoid 01](../../../../../avoid/01_restating_the_target.md), judged by B1/B2
and their actual acquisition cost. It is not an RH-equivalent criterion,
a relative return-amplitude estimate, a transport law for state mass,
or an arithmetic sign gain. It is a specialization of classical quadrature,
not a novelty claim. The one allowed non-chain baseline is exactly the
same (N)-node Gaussian quadrature: identical nodes, weights and scalar
answer mean that this theorem alone offers no evaluation advantage over it.

## Missing inputs and the boundary of the decision

The proof request does not depend on an unproved estimate for (a_n).
To **compute** its sharper right side and finite matrix one would need
certified coefficients (a_1,\ldots,a_N), with moment and rounding costs;
(a_N) is outside (J_N) but inside its error constant. Neither those
numbers nor a numerical certificate are supplied by this decision.
The monic norm is normalized with (d\mu_*); branch 03's unnormalized
(h_N(1/2)) must be divided by (Z_*) before substitution.

An improved all-degree branch-03 upper bound for
\(\prod_{j=1}^N\beta_j(1/2)\) is a **future optional provider input**,
not an assumption of B1 or E01. A proposed logarithmic coefficient bound
reported by the VCD worker is still unproved at this decision. It is not
used to label JCH ready. Any moving-(J(\lambda)) replacement changes the
contract and needs a separate recorded decision.

The [source/control note](../../notes/01_JCH_B01_SOURCE_AND_CONTROL_SCREEN_20261113.md)
applies the actual collision witnesses. None of the positive-source
controls contradicts the generic absolute approximation estimate. At an
exact collision, an absolute error allowance cannot imply a nonzero scalar
value; a separate lower margin would be necessary. No lower margin is
requested or assumed. Parked state and recursive routes are research
choices, not exclusions of those methods.

Read the [result index](../../../../../result-summaries/README.md),
[avoid index](../../../../../avoid/README.md), specifically
[controls 12](../../../../../result-summaries/12_collision_controls_and_screening.md),
[02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[03](../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md),
[07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and
[17](../../../../../avoid/17_parallel_writers_and_broken_registries.md).
The inherited [source crosswalk](../../../notes/02_BRANCH_SOURCE_CROSSWALK_20261113.md)
retains ownership and prior evidence. B01 executed no numerical campaign,
no E01 proof and no independent review.
