# VCD-B01 — Select a logarithmic coefficient envelope

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Author-selected and tool-dispatched
configuration: **gpt-6-astra / ultra**. No separate backend attestation was
available; dispatch metadata is not inferred backend verification.

**B01 disposition: complete with one frozen E01 contract.** This is a
conceptual choice and proof plan; the target below awaits E01 derivation
and E02 assessment. No numerical run, coefficient asymptotic, collision
exclusion or manuscript is produced by B01.

| Next task | Type/model | Readiness | Expected output |
| --- | --- | --- | --- |
| VCD-E01 r1 | E — GPT-6.1 Sol / Ultra | Ready; frozen request linked below | Prove the one coefficient envelope and its norm-product consequence, or name the exact failed step |
| VCD-E02 | E — GPT-6.1 Sol / Ultra | Depends on E01 return | Assess constants, all-degree quantifiers, source boundaries and the consumer |

Read the [result index](../../../../../result-summaries/README.md) and
[avoid index](../../../../../avoid/README.md); the applicable clusters are
[controls 12](../../../../../result-summaries/12_collision_controls_and_screening.md),
[classification 01](../../../../../avoid/01_restating_the_target.md),
[premises 02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[coordinate changes 03](../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
and [scoped exclusions 07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).
The [source crosswalk](../../../notes/02_BRANCH_SOURCE_CROSSWALK_20261113.md)
retains inherited identities and evidence ownership. This estimate is an
intermediate quantitative milestone, not an RH-equivalent criterion.

## One round, three candidate questions

1. **Finite-prefix moment bounds.** Tractable but confined to a prescribed
   degree range, with conditioning costs if moment determinants are used.
   Parked in this round because the source gives a direct all-degree upper
   envelope without evaluating ill-conditioned determinants.
2. **Logarithmic upper envelope from the source score. Selected.** Use the
   exact positive theta summands to bound the logarithmic derivative, then
   polynomial integration by parts and convexity. This fixes an explicit
   degree dependence and supplies the monic norm product needed by fixed-chain
   scalar quadrature. No special solution of Volterra is assumed.
3. **A leading large-degree asymptotic or finite nonlinear closure.** Parked:
   the inherited material supplies neither the required asymptotic theorem
   with verified hypotheses nor a justified closure. This is a research
   choice for this round, not an impossibility result for either class.

## Fixed target and one consumer

Use the complete unchanged source and monic conventions in the
[branch plan](../../research-plan/01_VOLTERRA_RESEARCH_PLAN_20261113.md).
For every integer n>=0 and every 0<=lambda<=1/2, the selected target is

\[
 \beta_n(\lambda)+\beta_{n+1}(\lambda)
 \le B_n:=\frac{\operatorname{arcosh}^2(2n+12)}{16},
 \qquad \beta_0=0.                                      \tag{T}
\]

The sole consumer is the monic norm product at the fixed initial chain:

\[
 \frac{h_N(1/2)}{h_0(1/2)}
 =\prod_{j=1}^N\beta_j(1/2)
 \le\prod_{j=0}^{N-1}B_j
 \le\left[\frac{\operatorname{arcosh}(2N+10)}4\right]^{2N},
 \quad N\ge1.                                           \tag{C}
\]

This is an explicit replacement for unknown recurrence coefficients in
a fixed-chain quadrature error factor. JCH owns the proof and usefulness
of its scalar observation/error estimate; TN6 owns any shared transfer.
VCD does not infer a field sign, relative error, transport estimate or
computational advantage from (C). The exact field remains
H_lambda(z)=Z_lambda <e0,exp(iz J(lambda))e0>/2; at lambda=1/2 the
coefficients are those of the fixed J_* used by JCH. The normalized monic
norm is h_N/h_0, not the unnormalized h_N. No moving-basis time derivative
is used by this consumer.

The new input beyond the generic Volterra law is the **quantitative
source-score confinement** of the complete positive square-mode source.
It is not exclusive to theta: positive weighted-square reflected sources
can share it. The bound is useful as an approximation allowance even
when it does not distinguish a collision control.

## Frozen route and feasibility check

Put V_lambda=-log W_lambda and r_m=pi m² exp(4u) on u>=0.
For the positive summand s_m=e^u(2r_m²-3r_m)e^(-r_m),

\[
 (\log s_m)'=9+\frac{12}{2r_m-3}-4r_m,
 \quad V_\lambda'(u)\ge4\pi e^{4u}-13-u.       \tag{S}
\]

The derivative of the complete sum is its positive weighted mean of these
scores. The inherited complete-source domination must be used to justify
it, without replacing the sum by m=1. The target elementary consequence is

\[
 uV_\lambda'(u)\ge\cosh(4u)-11\quad(u\in\mathbb R).       \tag{D}
\]

Use |u|<=1/2 and |u|>=1/2 as the two cases. In the first, the discarded
positive term in (S) leaves at worst -27/4 and cosh(2)<4. In the second,
4pi-1/|u|>10 and 10exp(4|u|)>=|u|+13 suffice. These are feasibility
checks for the fixed route, not a substitute for E01's completed proof.

Under dnu_n=P_n²W_lambda du/h_n, the exact integration-by-parts identity is
E_n[u V_lambda']=2n+1 and E_n[u²]=beta_n+beta_(n+1).
The function v -> cosh(4sqrt(v)) is convex for v>=0 by its nonnegative
power series. Jensen applied to that function, rather than to log²,
converts (D) into (T). E01 must check boundary terms, integrability,
monicity and uniformity in lambda. One algebraic proof covers all n;
no finite degree sample is evidence for its all-degree quantifier.

## Actual control-premise screen

This is an analytical screen of the catalog witnesses, not a rerun of
existing numerical certificates. Absence of the exact theta identity
alone is not represented as failure of (T).

| Control family | Applicable test and precise scope |
| --- | --- |
| Three-atom F_lambda=2+2exp(lambda-T)cos x | No positive absolutely continuous density or source score. At its event beta_1+beta_2=1, whereas B_1=arcosh²(14)/16<1 (cosh4>14). Thus this actual coefficient envelope fails at n=1; regular Volterra evolution still holds. |
| Euler-factor translated theta source | The untranslated summand score (S) is not its score. There is also a direct failed coefficient instance at lambda=0, c=1/2, p=23: beta_1(control)=beta_1(theta)+(log23)²/12>3/4, while B_0<3/4 since cosh(sqrt12)>12. The certified catalog includes p=23. No pass/fail result is assigned here to the other small-prime witnesses. |
| Positive weighted-square three/four-node controls | Their positive half-line summands obey the same score bound; even reflection is locally absolutely continuous, and the factor u kills the integration-by-parts junction at zero. They can therefore share the proposed envelope despite their certified collisions. Full smooth reflection and complete canonical coefficients fail, but those are not needed by this bound. This is the decisive reason no collision separation is claimed. |
| Reflected super-Gaussian control | Its logarithmic score grows polynomially at infinity, so the exponential lower bound (D) fails eventually. It also lacks the exact square-mode score formula. No numerical beta comparison is asserted. |
| Smooth shape/positive-primitive controls | They use a freely small damping coefficient in exp(-delta cosh4u), rather than the theta summand formula (S). That exact score premise fails. Their satisfaction of the weaker inequality (D) or (T) is not decided for every allowed damping; no rejection claim is needed for an approximation allowance. |
| Finite-prime-orbit square-source controls | Modified positive square coefficients may retain the same score comparison on the half-line. Their full reflection fails. Under an admissible even locally absolutely continuous extension the general coefficient argument can still apply; this bound does not enforce infinite arithmetic compatibility. |
| Atomic and finite-profile threshold families | Atomic sources fail the density/score premise; triangular compact extensions fail the globally positive full-line score premise. No blanket numerical failure of (T) is asserted for every profile family. |
| RH-conditional endpoint controls | Their ordinary Dirichlet arithmetic fails, while the present exact theta sum-to-score derivation is unavailable for the perturbed source. Their actual (D)/(T) value is untested; the source construction retains its RH condition. |
| Fixed theta amplitude with altered readout | The coefficient bound is unchanged and can hold. The literal Fourier/Newman observation fails; coefficient estimates cannot validate the altered readout as a theta field. |

The source-score method is consequently a quantified bound for its stated
positive-density class, not a canonical arithmetic discriminator. The
weighted-square controls specifically prevent promoting it into a general
collision exclusion. No broader coefficient route is ruled out.

## Disposition and handoff

Issue [VCD-E01-r1](../../research-progress/handoffs/VCD-E01-r1.md), with
[exact input manifest](../../numerics/01_VCD_B01_E01_INPUTS_20261113.json).
The manifest identifies working-tree inputs; hashes establish identity,
not mathematical validity. No new literature import, PDF retrieval or
numerical experiment is needed for the elementary fixed route. The
existing Van Assche citation remains the inherited Volterra precedent,
not a theta-growth theorem.

**Next: [E] VCD-E01 — GPT-6.1 Sol / Ultra**, complete (T), (C) or an exact
failed-step return within r1. B01 stops at that dispatch boundary.
