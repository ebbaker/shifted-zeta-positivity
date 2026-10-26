# HDA-A03-AN01 r1 — corrected one-arm models and regulator-center sensitivity

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Parent ansatz chat0001 records
**gpt-6.1-sol (Codex), actual effort ultra**, thread
`01a175aa-a487-79a1-85a8-6f465fdb36bf`; execution metadata must be
recorded again in the return.

Parent task **HDA-A03**. Next owner **Analysis — Sol**. Prepared,
not dispatched. The [ansatz register](../01_HIGH_HEIGHT_ANSATZ_RESEARCH_PROGRESS_20261025.md)
owns live status. This is a new bounded regulator-center comparison,
not an extension of the negative-time bridge request.

## Read first and preserve the inherited center

Follow repository AGENTS.md, LARGE_FILES.md, GPT_RESEARCH_MODEL_WORKFLOW.md
and tools/CHAT_HISTORY.md. Read [ansatz Note03](../../notes/03_OUTER_CORRECTION_AND_SIGNED_REAL_BRIDGE_20261025.md),
especially CB4--13; the maintained ansatz manuscript's exact regulator
section; and these parent inputs:

- [Note20](../../../notes/20_GLOBAL_REGULATOR_AND_FINITE_SOURCE_BRIDGE_20261024.md),
  FB1--2: the actual physical regulator, including its flat switch.
- [Note28](../../../notes/28_JOINT_OUTER_REGULATOR_TRANSFER_AND_SWITCH_LAYER_20261024.md),
  JT22--33: the inherited linear-gamma model center, its sensitivity,
  rounding scale and resolved law. Retain its stated proof/review status.
- [Note30](../../../notes/30_FULL_GAMMA_SADDLE_AND_INNER_OVERLAP_20261024.md),
  FS3--4 and its branch/domain proof: the full implicit gamma saddle.
- [Note31](../../../notes/31_POSITIVE_ALL_HEIGHT_EVOLUTION_AND_COVARIANCE_20261024.md):
  inherited full-saddle evolution and physical-transfer domains. Its
  existing results are neither retracted nor automatically sharpened here.

Read the [result index](../../../../../../result-summaries/README.md)
and [avoid index](../../../../../../avoid/README.md), particularly the
heat-flow/collision-control clusters and normalization, separate bounds,
same-model review and evidence-status patterns. Pin actual input versions.
Any new classical input must be checked in its primary source.

The historical center is **exactly**

    A_lin(t,X)=|M(s_X) exp(t alpha(s_X)^2/4)|,
    b_lin(t,X)=log(epsilon_g(t,X)/A_lin(t,X)),
    b_lin(t_c,lin(X),X)=0,  s_X=(1+iX)/2.

Do not silently rename it as a full-saddle, elementary, canonical-field
or observed-density center. No amplitude center is defined by zeros of H.
The existing exact implicit center and its JT33 scope remain historical
inputs. A short inverse-logarithmic expansion of t_c,lin is still too
coarse for that law unless its omitted error is separately paid.

## Frozen bounded request

Study only

    63<=t<=65, X>=X0, physical |y|<=1,

with the complete fixed averaging, collar and analytic buffers declared.
As in the ansatz notes take r=ell+2, b=1+h+2 and reserve one extra
analytic unit. Keep the canonical complete H, H_t=-H_zz and
H(0,z)=xi((1+iz)/2)/8; physical q=epsilon_g^2; fixed physical
K=k_ell k_h; and unnormalized observables and signed covariance.
No RH, reality/simplicity assumption or unknown-remainder positivity may
replace an estimate. This packet does not include a new physical tuple
transfer theorem.

### A. Pay corrected one-arm comparisons on the switch neighborhood

Use M(w)=w(w-1)pi^(-w/2)Gamma(w/2)/16 and alpha=M'/M. Distinguish:

1. **Linear gamma arm:** G_t(w)=M(w)exp(t alpha(w)^2/4).
2. **Specified exact truncated gamma heat arm:** choose one fixed V_0
   from the complete buffer as in Note03 CB6, and use

       J_V0(t,w)=(pi t)^(-1/2) integral_[V_0,infinity)
                         exp(-v^2/t) M(w+v) dv.

   Freeze V_0 in z,t. Retain the other arm, middle, complete arithmetic
   tails and omitted Gaussian pieces when comparing their sum with H.
   This named arm is a decomposition-dependent reference, not an
   intrinsic amplitude extracted from the true oscillatory field.
3. **Full gamma saddle:** use exactly the branch of parent Note30,

       p=w+(t/2)alpha(p), B=1-(t/2)alpha'(p),
       S_t(w)=M(p) exp(-(p-w)^2/t) B^(-1/2),

   with its square root near one and its actual domain gates.
4. **Elementary arms:** C_pm=A_o exp(+-iTheta_o)/2 and their Note03
   first corrections C_pm(1+D_pm). At real X a positive exponential
   rewrite of the corrected upper-arm modulus may be convenient, but
   its difference from |C_+(1+D_+)| must remain inside the paid error.

Extend Note03's method from [32,33] to this new fixed interval by
rechecking its constants and every contribution, rather than substituting
the new t into an old domain. Candidate checkpoints, to be proved with
uniform spatial/time remainders, are

    log J_V0 = log M + t alpha^2/4
                 +t alpha'/4+t^2 alpha^2 alpha'/8
                 +O((1+L_X^4)/X^2),

and the matching expansion of log S_t. Use a continuously chosen
nonzero-arm ratio/logarithm; do not take a logarithm of H or a cosine.
For the elementary real upper arm, recheck the candidate real correction

    log A_el,1 - log(A_o/2)
          = [7pi t/16+pi t^2 L_X/32]/X
            +O((1+L_X^4)/X^2).

This is a checkpoint, not a packet assumption. Include gamma curvature,
the Gaussian determinant, exact gamma-to-elementary conversion and
ordinary arithmetic/middle/tail errors before identifying any correction
to the true H comparison. All arithmetic coefficients remain canonical.

Deliver a full buffered two-arm field comparison, spatial jets through
order three and a direct first time comparison at the actual paid scale.
Keep exact heat residuals separate from field comparisons; any boundary
term from the fixed truncated arm must be paid if its residual is used.
An inherited full-saddle result can be consumed only on its established
domain and at its own rate.

### B. Compare named centers using the exact physical protocol

Retain without simplification

    epsilon_b(t)=eta C(1+t^2)^(-1/4), C=Phi(0)sqrt(pi)/2,
    epsilon_g(t,X)=epsilon_b(t), t<=64,
    epsilon_g(t,X)=epsilon_b(t)^(1-chi_reg(t))
                       epsilon_+(t,X)^chi_reg(t), t>64,
    epsilon_+(t,X)=M_0(t)/kappa(t) exp[-X^2/(2kappa(t))].

Here chi_reg is the exact flat switch of Note20: for
nu=(t-64)/64 in (0,1),

    chi_reg=exp(-1/nu)/[exp(-1/nu)+exp(-1/(1-nu))].

The source-saddle quantities M_0 and kappa are precisely those of parent
Note19/Note20, distinct from M(w), L_X and the gamma saddle. Equivalently,

    epsilon_g=E_0(t) exp[-beta(t) X^2/2],
    E_0=epsilon_b^(1-chi_reg)(M_0/kappa)^chi_reg,
    beta=chi_reg/kappa  (beta=0 below64).

For each positive named one-arm modulus A, define only its **comparison
center** t_c,A by log(epsilon_g/A)=0 near the inherited t_c,lin.
Prove existence/uniqueness in the stated local neighborhood and quantify
all differences using paid amplitude and direct time-derivative estimates.

In particular, re-establish the actual sensitivity from the exact protocol:

    (b_lin)_t=(log E_0)'-(X^2/2)beta'
                        -(1/4)Re(alpha(s_X)^2).

Parent JT28--31 give the candidate asymptotic near its center

    (b_lin)_t(t_c,lin,X)
        =-pi X (log X)^2/512 [1+O(1/log X)].

Derive the uniform neighborhood control needed to consume this statement;
do not differentiate JT30's center allowance, and do not omit the X factor.
For Delta_A=log(A/A_lin), the expected first perturbation has sign

    t_c,A-t_c,lin ~ Delta_A(t_c,lin,X)/(b_lin)_t(t_c,lin,X),

when its remainder is paid. State the actual finite-height first correction
and its error rather than only an order symbol if the analysis supplies it.

Compare every center error with the inherited rounding width

    w_X=128/(pi X log X).

Target an explicitly paid o(w_X) approximation where possible. Do not
presuppose that a first amplitude correction is necessary to reach this
width: the actual sensitivity can already make coarser amplitude changes
sub-width. For example, a constant logarithmic amplitude change and an
O(log X/X) logarithmic correction have very different center effects;
both must be computed with the same actual derivative. Retain the
one-arm versus full-cosine factor two explicitly.

The new comparison centers do not replace the historically defined
t_c,lin inside an earlier theorem. If re-expressing its leading resolved
law around another center, pay the induced scaled-time shift explicitly
and state whether the inherited O(1/log X) error changes. Do not claim
a sharper density law from a more accurate center alone.

### C. State the precise unpaid consumer and stop

Separate the gains in field/amplitude and center accuracy from the
physical layer consumer. Parent JT24 supplies only an O(1) absolute
allowance for the simple two-layer shape. Improved centering does not
by itself improve

    R_H - omega_A/(2pi) [k_h(y-d_A)+k_h(y+d_A)],
    d_A=max(log(epsilon_g/A),0)/omega_A.

The inherited O(1) allowance belongs to the linear-gamma layer. If using
new model data in the displayed consumer, separately pay the change of
layer before assigning even that inherited rate to the new expression.
If no sharper consumer is paid, identify the exact open comparison and
retain the earlier linear-model O(1) status without upgrading it.
Direct density time derivatives, actual current, covariance, forcing,
adaptive regulator terms and spatial joins remain separate obligations.
Do not infer them by differentiating an O(1) density allowance or by
using only a small field residual.

## Evidence standard, outputs and stop rule

Analytical only: no samples, numerical fits, machine-symbolic expansion,
exact-arithmetic checks or interval campaign. Housekeeping and manuscript
production are permitted. Routine fixed-endpoint/sector choices, branches,
Taylor algebra, local implicit-function estimates and finite onset gates
are delegated to Sol. Constants may depend on the fixed buffers and eta;
state dependence and numerical-onset status.

Stop after the corrected compact-switch field/arm comparison and named
center comparison, with the first precise unpaid physical-layer consumer,
or at a specifically identified unpaid estimate after a focused attempt.
No t outside [63,65], growing positive time, Lambert-W replacement,
joint endpoint matching, new regulator, runtime theorem or physical tuple
campaign is authorized by this packet. Escalate to Analytical — Astra only
if a named resistant mechanism remains, with the failed estimate supplied.
No automatic dispatch or model change.

Save research in ansatz/notes/, assessment in ansatz/reviews/ and small
analytical input records in ansatz/numerics/. Append return/disposition
here; update the sole progress register, overview and maintained manuscript
at actual status; and refresh the unique ansatz chat history. Preserve
historical center definitions, review limitations and earlier evidence.
No manuscript snapshots or duplicate chat registration.

## Return / disposition

Pending. HDA-A03 remains Partial at its inherited scope. The current
packet supplies no new center or layer theorem until its return is
written and assessed. Parent HDA-17 Partial, HDA-18 Gated and HDA-20
unfulfilled remain unchanged.
