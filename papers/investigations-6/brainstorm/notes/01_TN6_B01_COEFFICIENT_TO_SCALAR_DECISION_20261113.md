# TN6-B01 — coefficient envelope to finite-chain scalar accuracy

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Author-selected and dispatched
configuration: **gpt-6-astra / ultra**; actual backend model/effort not
independently exposed. **Conceptual decision completed. The targets below
are not proved by this decision.**

| Next shared task | Type and selected setting | Readiness at this decision | Expected output |
| --- | --- | --- | --- |
| TN6-E01 | E — GPT-6.1 Sol / Ultra | Reserved until the actual VCD and JCH derivations and explicit review scopes exist; no E packet issued here | One source-matched coefficient-to-scalar bound and sufficient depth rule, or precise failed allowance |

The [sole TN6 register](../../research-progress/01_TENSOR_NETWORK_RESEARCH_PROGRESS_20261113.md)
owns shared status; the [collection plan](../../research-overview/02_TENSOR_NETWORK_RESEARCH_PLAN_20261113.md)
owns the one-round/four-option limit. Read the
[result index](../../../../result-summaries/README.md),
[avoid index](../../../../avoid/README.md), particularly
[controls 12](../../../../result-summaries/12_collision_controls_and_screening.md),
[classification 01](../../../../avoid/01_restating_the_target.md),
[control-premise rule 02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[coordinate caution 03](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
and [scoped exclusions 07](../../../../avoid/07_scoped_exclusions_read_as_universal.md).
Source ownership and inherited evidence remain in the
[crosswalk](../../notes/02_BRANCH_SOURCE_CROSSWALK_20261113.md).

## The comparison and selection

The common consumer is absolute approximation of the **literal real scalar
field** on (0\le\tau\le1/2), (|x|\le X<\infty), with
(\lambda=1/2-\tau). A dimensionless tolerance (0<\epsilon\le1)
means absolute physical error at most (H_{1/2}(0)\epsilon=Z_*\epsilon/2).
It does not divide by the possibly vanishing field at the observation.

| Inherited representation | Information it offers this consumer | Decision in this single round |
| --- | --- | --- |
| QTT source-amplitude tensor train | Finite contraction with quadrature, source, compression and arithmetic allowances | Not selected for the shared round; its own branch owns rank and error acquisition |
| Fixed Jacobi chain | One scalar readout of an (N)-site principal matrix, with a generic Gauss/Hermite error target from JCH-B01 | Select as the consumer mechanism; an absolute error directly preserves the literal observation |
| Moving orthogonal-polynomial coefficients | VCD-B01 specifies an all-degree coefficient/norm envelope, whose (lambda=1/2) specialization could remove an unknown chain error factor | **Select 03 → 02** as the single interface; no differentiation in a moving basis is required |
| Infinite dyadic source/phase products | Exact limiting assembly with a separate finite-resolution/full-line allowance | Not selected; useful convergence/rank information stays with ITP and QTT; no failure of these methods is asserted |

The one matched non-chain baseline is the same (N)-node Gaussian
quadrature of the complete normalized source. It is algebraically identical
to the finite-chain readout, so no computational speed advantage follows.
No Riemann–Siegel, QTT or dyadic performance contest is added to this round.
The scientific addition sought is a coefficient-free sufficient chain
depth, beyond an exact representation and beyond the unknown (h_N)
factor. This is an **intermediate approximation milestone**, judged by
its explicit bound, not an RH-equivalent reformulation or sign criterion.

## Fixed interface and proposed quantitative acceptance

Keep (d\mu_*=e^{u^2/2}\Phi(u)du/Z_*), the complete GNP source and
(H_0(x)=\xi(1/2-ix/2)/8). The finite matrix (J_N) uses sites
(0,\ldots,N-1) of fixed (J_*=J(1/2)) and its own square:

\[
H_N(\tau,x)=\frac{Z_*}{2}\langle e_0,
 e^{-\tau J_N^2}e^{ixJ_N}e_0\rangle.                 \tag{T1}
\]

The two **required provider outputs**, currently derivation targets, are:

\[
\text{JCH:}\quad
\frac{|H_{1/2-\tau}(x)-H_N(\tau,x)|}{Z_*/2}
\le h_N^* S_N(\tau,x),\quad
S_N=\sum_{k=0}^{N}\frac{\tau^kx^{2N-2k}}{k!(2N-2k)!}, \tag{T2}
\]

\[
\text{VCD:}\quad h_N^*
=\frac{h_N(1/2)}{h_0(1/2)}
=\prod_{j=1}^{N}\beta_j(1/2)
\le\prod_{j=0}^{N-1}\frac{\operatorname{arcosh}^2(2j+12)}{16}
\le\left(\frac{L_N}{4}\right)^{2N},\quad
L_N=\operatorname{arcosh}(2N+10).                    \tag{T3}
\]

(h_N^*) is JCH's normalized monic norm; VCD's (h_N) is unnormalized.
The ratio is essential. A coefficient upper bound controls the remainder;
it does not produce the exact matrix entries needed to evaluate T1.

The shared E task should substitute T3 into T2, preserving the sharper
product when useful, and derive the explicit uniform target

\[
\sup_{\tau\in[0,1/2],\,|x|\le X}
\frac{|H_{1/2-\tau}(x)-H_N(\tau,x)|}{Z_*/2}
\le \exp\left[-N\log4+\frac{XL_N}{2}
                          +\frac{L_N^2}{8}\right].  \tag{T4}
\]

The fixed route is coefficient extraction from
(e^{\tau r^2}\cosh(xr)): for any (r>0),
(S_N\le r^{-2N}e^{\tau r^2+Xr}). Set (r=L_N/2).
The request must verify the coefficient identity and inequality, not use
an optimizing parameter without its factors. No branch theorem is reproved
under the parent task.

A concrete sufficient-depth target, to be proved in that E return, is

\[
K=X+\log(1/\epsilon)+1,\qquad
N=\left\lceil4K\log(16K)\right\rceil.              \tag{T5}
\]

Acceptance requires that T5 imply T4 is at most (epsilon), with
all (X\ge0), (0<\epsilon\le1), ceiling and endpoint details.
Use (L_N\le\log(4N+20)), (ell=\log(16K)),
(4N+20\le16K\ell+24\le256K^2), and (ell\le3K)
as the fixed elementary route. Constants need not be optimized.
This is an explicit sufficient size of order
((X+\log(1/\epsilon)+1)\log(X+\log(1/\epsilon)+2)).
The order statement is about the **declared bound**, not a lower bound
on optimal depth, actual state propagation or arithmetic effort.
The existing generic JCH source-moment envelope remains useful but is
not silently treated as an acquisition algorithm or a measured baseline.

## Inputs that must exist before a shared E packet is issued

| Required item | Owner and immutable specification | Gate before TN6-E01 |
| --- | --- | --- |
| T2 full-line finite-chain scalar theorem | [JCH-E01 r1](../../02_jacobi_chain_height_flow/research-progress/handoffs/JCH-E01-r1.md) | Actual proof/return, its exact version and JCH-E02 assessment or explicit pending-review limitation |
| T3 all-degree monic-norm envelope | [VCD-E01 r1](../../03_volterra_coefficient_dynamics/research-progress/handoffs/VCD-E01-r1.md) | Actual proof/return with constants and normalized factor; VCD-E02 assessment or explicit pending-review limitation |
| Same source, time slice and normalization | Complete GNP source already pinned by both branch manifests | Verify both returns use identical (Phi), (lambda_*=1/2), (\beta_j), (Z_*), and index (N) |
| Exact E source identities | Parent coordinator | Pin actual returns and review reports, not just these requests, in the shared request manifest |

At this B decision, the input request SHA-256 identities are:

- JCH-E01 r1: `048d40e9ab7990d9f1da7d08dbb74020c59cd38602e7383c9c09afe9ae4740b7`.
- VCD-E01 r1: `92be531b717ffc823836584b5ad7c5d835d42cc8b05d067b82f4318b61222b06`.
- [VCD B01 decision](../../03_volterra_coefficient_dynamics/brainstorm/notes/01_VCD_B01_LOGARITHMIC_ENVELOPE_DECISION_20261113.md):
  `5482550bd096dd163dffcb91cc82656448ded8725f75016a60539e2132314587`.

These identify requested inputs, **not accomplished provider theorems**.
No TN6-E01 packet is issued while those returns are missing. The coordinator
may freeze the packet and dispatch Sol immediately when the actual
dependencies and their review limitations have been recorded, as the
author has already authorized. A failed provider premise blocks this
interface without blocking the other branches.

## Actual control screen and scope

Reuse the [JCH witness screen](../../02_jacobi_chain_height_flow/notes/01_JCH_B01_SOURCE_AND_CONTROL_SCREEN_20261113.md)
and [VCD screen](../../03_volterra_coefficient_dynamics/brainstorm/notes/01_VCD_B01_LOGARITHMIC_ENVELOPE_DECISION_20261113.md)
at their original status. The shared claim adds no sign conclusion.

- **Atomic (2+2e^{\lambda-T}\cos x).** The event ((T,\pi)) has a
  terminating exact three-site readout. Its coefficient sum at the event
  is (\beta_1+\beta_2=1>B_1); the density/score premise and VCD
  bound fail there, while the generic JCH absolute bound remains compatible
  with zero error. This does not refute T4 for the complete source.
- **Euler-factor family.** VCD's actual (c=1/2,p=23,\lambda=0)
  example fails its all-time coefficient bound at (n=0); the untranslated
  source-score formula also fails. That is not a claim that the fixed
  (lambda=1/2) monic norm or T4 fails for every prime. Other instances
  remain untested. Their generic JCH approximation theorem can hold.
- **Weighted-square witnesses at (T=1/4) and (1/100).** Their positive
  half-line square summands and even locally absolutely continuous
  extension can satisfy the very source-score bound feeding T3, and the
  JCH quadrature mechanism also applies. At their actual certified events
  an accurate scalar approximation still converges to zero. Thus this
  is explicitly **not a collision discriminator**, despite the failures
  of full smooth reflection and unchanged canonical coefficients.
- **Reflected super-Gaussian event ((1/4,\pi/4)).** The generic
  quadrature mechanism applies; the score grows polynomially, so VCD's
  exponential confinement premise fails at infinity. No unsupported
  all-degree coefficient value or T4 failure is assigned to it.
- **Smooth shape/positive-primitive families.** The exact theta
  summand-to-score derivation is unavailable. Whether every freely damped
  witness satisfies the weaker confinement inequality is untested.
  Their moments suffice for generic scalar approximation, and their
  collision existence remains conditional on the recorded small-damping
  construction, not a new damping certificate.
- **Finite-prime-orbit families.** Positive modified square coefficients
  can share the score comparison within its stated extension class;
  full reflection and complete arithmetic fail. Their high-gap events
  need not lie in an arbitrary chosen finite (X). No universal rejection
  or uniform-in-family constant is assumed.
- **Finite-profile families.** Atomic cases fail the density/score
  premise; compact triangular extensions fail a globally positive
  full-line score assumption. No blanket failure of the numerical
  envelope is asserted. **RH-conditional endpoint controls** retain
  their RH condition, fail ordinary Dirichlet arithmetic and have no
  checked value for the score/envelope here.
- **Fixed source with altered observation.** T3 can be unchanged; T2
  needs literal cosine/Fourier observation. The changed-kernel examples
  fail that premise. No derivative payment for them is silently borrowed.

A valid absolute error bound on a domain containing a collision must be
compatible with that event; it is not required to reject it. No actual
theta collision is constructed, and no new zero-exclusion criterion is
introduced. Relative accuracy would require a separate denominator/lower
margin. Full-state prefix tails, complex heights, Green logarithms,
derivatives, coefficient acquisition and certified arithmetic cost remain
outside this selected scalar contract.

## Finite successor and ownership

TN6-E01 is one analytical transfer, one domain, one scalar consumer and
one return, with at most one routine correction pass. **No numerical table
or campaign is selected.** Prove T4/T5 or identify the precise failed
constant/input; standard inequalities and endpoint corrections are routine.
A changed source, coefficient theorem, consumer or regime returns to B01.
After disposition, the selected shared round ends; no manuscript or larger
campaign is automatically opened.

The parent writes the eventual shared packet/return and milestone. Branch
registers remain the sole owners of branch live status. Primary quadrature
attribution stays with the [JCH DLMF record](../../02_jacobi_chain_height_flow/references/01_DLMF_GAUSS_QUADRATURE_20261113.md);
the parent adds no literature inspection or branch proof claim. Internal
LLM assessments share sources and are not specialist independence.
