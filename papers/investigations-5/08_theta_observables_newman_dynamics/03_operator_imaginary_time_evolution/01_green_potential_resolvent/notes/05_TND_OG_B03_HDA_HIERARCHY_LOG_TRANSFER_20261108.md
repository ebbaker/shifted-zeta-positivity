# B03: heat-density hierarchies and the boundary-logarithm consumer

8 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual model and reasoning effort
are not recorded in this chat's capture metadata.

**Status:** bounded relationship audit and analytical transfer consequence,
derived below from named existing inputs, with same-assistant checking
only. This is not an independent reassessment of the HDA or B02 proofs.
The all-order Riemann–Siegel remainder is an imported classical input.
No complete Green assembly, favorable canonical value, numerical run or
cost theorem is established.

The author asks whether investigations-5/01_heat_density_asymptotics
(HDA) was carried into the overview and whether the relationship is
useful. The answer is **partly carried over, and concretely useful as a
source of boundary approximants**. The useful order need not be a
factorial zero-statistic order.

## 1. What was already recorded

The parent [locator20](../../brainstorm/notes/20_TND_O_PRIOR_HIERARCHY_LOCATOR_20261107.md),
§4, explicitly identifies the author's HDA hierarchy. The
[correlation overview](../../02_localized_zero_correlations/research-overview/01_TND_OC_RESEARCH_OVERVIEW_20261107.md),
§5, carries this identification and its transfer obligations. The
[Green overview](../research-overview/01_TND_OG_GREEN_RESOLVENT_RESEARCH_OVERVIEW_20261107.md)
previously linked locator20 only when discussing the older regulated
Wirtinger field. It did not develop the HDA connection. Its new §7
supplies that missing direct account.

The locator's strong negative-time warning is correct for the theorem
it names. It is not a statement that all HDA approximations exclude
time zero. The [current HDA Book overview][book] and
[Summary67][summary67] include the signed crossover and the later
retained-arithmetic positive band. These must be read alongside the
recurrence overview.

## 2. The different hierarchies and their clocks

HDA uses the same complete canonical source and normalization:
H(t,z)=H_t(z), H(0,z)=xi((1+iz)/2)/8 and ∂t H=−∂z²H.
Its forward heat clock T satisfies t=−T. The Green branch's Newman
parameter λ is this t; positive T is negative λ.

[Ansatz Note15][a15] gives the exact source moments
\[
 \mu_j(T,z)=\frac12\int_{\mathbb R}u^j e^{-Tu^2+izu}\Phi(u)\,du,
 \qquad \partial_T\mu_j=-\mu_{j+2},\quad
 \partial_z\mu_j=i\mu_{j+1},\quad \mu_0=H_{-T}.
 \tag{1}
\]
On a zero-free patch, the current resolvent is exactly
\[
 R_{-T}=i\mu_1/\mu_0.
 \tag{2}
\]
Equation (2) identifies the objects; it does not acquire its denominator.

[Ansatz Note16][a16] reorganizes local gamma-carrier corrections through
\[
 Q_T=d+2T\partial_d,\qquad
 D_r=\frac{\kappa_{r+1}}{(r+1)!}Q_T^{r+1},\qquad
 jU_j=\sum_{r=1}^{j}rD_rU_{j-r}.
 \tag{3}
\]
Here κr are derivatives of the logarithm of the exact gamma carrier,
not assumed probability cumulants. Every finite coefficient is defined
algebraically; the formal generating exponential is not a claimed
globally convergent operator series. The base retains both arithmetic
arms and all modes.

Keep four indices separate: arithmetic mode n, gamma fluctuation order
j, Riemann–Siegel completion order K, and factorial zero-statistic order.
The last belongs to the correlation branch. A generic source-moment or
heat recurrence is not a closed equation for zero correlations.

The quantitative HDA regimes are:

| Existing input | Domain and error scale | Permitted conclusion here |
| --- | --- | --- |
| [Recurrence Note05][r05], [Review04][rr04] | Growing order p=floor(L/2), K=2p; outer field/jets error exp(−L²/4) on 1≤T≤2 | Controlled simultaneous order growth, not hidden fixed-order constants. |
| [Recurrence Note20][r20], [Review14][rr14] | Same target on 1/L≤T≤2, with stronger onset and full endpoint costs | Still excludes T=0; cannot simply be continued there at the same rate. |
| [Ansatz Note04][a04], [Review03][ar03] | Exact-gamma zero-time remainder O(X^−3/4) in its gamma envelope; signed crossover abs(t)L≤8 | Time-zero field data do exist. |
| [Ansatz Note26][a26], [Review20][ar20] | Same retained-arithmetic family on 4/L≤t≤1 at (1+log X)²X^−3/4 | With Note04 covers 0≤t≤1; later atlas covers each fixed compact positive range. This does not carry the strong recurrence error through zero. |

L=log(X/(4π)); buffers, source populations and the source's original
assessment limits remain. The narrower real-boundary reuse below needs
neither the evolved negative-time theorem nor a new positive-time theorem.

## 3. Exact normalization and the local logarithmic transfer

Use the branch's time-zero field
\[
 s_-(z)=\frac{1-iz}{2},\quad
 F(z)=q(s_-(z))\zeta(s_-(z))=D(z)H_0(z),\quad
 q(s)=\frac{s-1}{s},\quad
 D(z)=\frac{16\pi^{s_-/2}}{s_-^2\Gamma(s_-/2)}.
 \tag{4}
\]
Let
\[
 M(s)=\frac{s(s-1)}{16}\pi^{-s/2}\Gamma(s/2),\qquad
 s_+(x)=\frac{1+ix}{2}.
\]
For real x, M(s+)=conjugate M(s−), |q(s−)|=1, and
\[
 D(x)M(s_-(x))=q(s_-(x)),\quad
 |D(x)|\,|M(s_+(x))|=1,\quad
 |D(x)|\bigl(|M(s_+)|+|M(s_-)|\bigr)=2.
 \tag{5}
\]
This is an exact cancellation of the gamma scale, not an asymptotic
lower bound for H. In particular the HDA zero-time bound from Note04
converts directly to a field error at most 2C X^−3/4 for F on its
real chart. One must not multiply a gamma-relative error by an unrelated
coarse absolute gamma bound.

For I_v=[v−1/2,v+1/2], take any measurable approximation \(\widehat H\)
whose converted error obeys
\[
 \sup_{I_v}|D(H_0-\widehat H)|\le\delta.
\]
Then \(\widehat F=D\widehat H\) can be inserted directly into
[B02 Note04][og04], (15)–(18). With its unchanged constants
\[
 \kappa=\log(27/26),\ B=26/3,\ c_0=\frac35\frac{\zeta(5)}{\zeta(5/2)},
\quad M_v=2|v|+26,\ A_v=\log(M_v/c_0),
\]
\[
 n_v=\max\{2,\lceil A_v/\kappa\rceil\},\quad
 C_v=2Bn_v e^{51A_v/n_v},\quad P_v=\frac{C_v n_v^2}{n_v-1},
\]
we have
\[
 0\le\int_{I_v}
   [\log(|\widehat F|+\delta)-\log|F|]\,dx
 \le P_v(2\delta/M_v)^{1/n_v}.
 \tag{6}
\]
No derivative error, zero-free real segment, simplicity, or holomorphic
approximant is required. In particular a piecewise real arithmetic
formula with its actual cutoff changes is admissible. This is the useful
addition to locator20's earlier source-to-H′/H route, which still needs
a separately paid denominator.

Equation (6) is local. Its integral retains the approximant's signed
logarithm. The compact weighting, exact remote log tail, prime tail and
evaluation allowances are distinct payments; this note does not execute
the frozen E03 full-source assembly.

## 4. Why fixed accuracy order is insufficient for this bound

Write ℓ=log v for v→+∞. The explicit B02 constants give
\[
 n_v=\ell/\kappa+O(1),\qquad P_v=\Theta(\ell^2).
 \tag{7}
\]
If the available field allowance is δ=Cv^−a with fixed a>0, then
\[
 (2\delta/M_v)^{1/n_v}\longrightarrow e^{-\kappa(a+1)}.
 \tag{8}
\]
Thus substituting that allowance into (6) does not yield a vanishing
logarithmic error bound at unbounded height. This says nothing about a
lower bound on the actual error and does not rule out a sharper transfer.

For a desired local tolerance h>0, a sufficient field allowance is
\[
 \delta\le \frac{M_v}{2}(h/P_v)^{n_v}.
 \tag{9}
\]
For fixed h the logarithm of M_v/δ therefore costs
\((2/\kappa+o(1))\ell\log\ell\) at the level of this sufficient rule.
The required scale is stronger than any fixed power of v. The old
exp(−L²/4) recurrence error would be more than sufficient after a
compatible normalization/domain transfer, but its negative-time theorem
is not available at zero.

## 5. The existing completion hierarchy already supplies a local route

A new through-zero heat theorem is unnecessary for this narrower
real-boundary question. Use the real initial data already retained in
[HDA Ansatz Note05][a05], (FN12)–(FN14), and
[Recurrence Note02][r02], (R1.12). For x>0 set
\[
 a_x=\sqrt{x/(4\pi)},\quad N_x=\lfloor a_x\rfloor,\quad
 \theta_x=1-2(a_x-N_x),\quad
 U_x=\exp\{-i[(x/4)\log(x/(4\pi))-x/4-\pi/8]\}.
\]
Retaining the exact gamma carrier and both arithmetic arms, define
\[
 f_K(x)=2\Re\!\left\{M(s_+(x))
 \left[\sum_{n=1}^{N_x}n^{-s_+(x)}
 +(-1)^{N_x-1}U_xa_x^{-1/2}
       \sum_{k=0}^{K}C_k(\theta_x,1/2)a_x^{-k}\right]\right\}.
 \tag{10}
\]
The Ck are the existing named Riemann–Siegel coefficient functions.
The imported remainder, for every positive integer K, is
\[
 |H_0(x)-f_K(x)|
 \le \frac{2^{7/4}}7 |M(s_+(x))|
 \Gamma((K+1)/2)\,1.1^{K+1}a_x^{-(K+3/2)}.
 \tag{11}
\]
The factor two counts both conjugate pieces. The source is
[Polymath v2, (36)–(38), Proposition 6.2 (56)][polymath],
reopened for this bounded check; this is not a new classical theorem
or an independent audit of its underlying proof.

For v>1/2, put \(a_-=\sqrt{(v-1/2)/(4\pi)}\) and
\[
 \delta_{v,K}=\frac{2^{7/4}}7
 \Gamma((K+1)/2)\,1.1^{K+1}a_-^{-(K+3/2)},\qquad
 \widehat F_K(x)=D(x)f_K(x).
 \tag{12}
\]
Equations (5) and (11) give a uniform F-error δv,K on I_v. Therefore
(6) applies with this explicit allowance, including intervals that cross
an arithmetic cutoff. Holomorphy belongs to the exact F; no derivative
of Nx is being taken.

Here is a concrete growing-order consequence. Take K=2p and, for
sufficiently large v,
\[
 p(v)=\left\lceil\frac4\kappa\log\log v\right\rceil.
 \tag{13}
\]
The elementary bound
\(\Gamma(p+1/2)=\sqrt\pi(2p)!/(4^pp!)\le\sqrt\pi\,p^p\)
and (12) give
\[
 \log(2\delta_{v,2p}/M_v)
 \le -(p+7/4)\log v+O(p\log(p+2)).
\]
Combine this with (7). Since p=O(log log v),
\[
 P_v(2\delta_{v,2p}/M_v)^{1/n_v}
 \le O((\log v)^2)e^{-\kappa p+o(1)}
 =O((\log v)^{-2}).
 \tag{14}
\]
Thus the existing real completion hierarchy, composed with B02, gives
a vanishing local one-sided log allowance with K=O(log log v).
More generally p=ceil(c log log v), c>2/κ, pays the bound
O((log v)^{2−κc}). These are sufficient, nonoptimal order choices.

The retained coefficient costs have not disappeared. In fact
\[
 \delta_{v,2p+2}/\delta_{v,2p}
   =(p+1/2)\,1.1^2/a_-^2.
 \tag{15}
\]
Our order choice lies eventually in the decreasing regime, but the
asymptotic expansion is not asserted to converge as K→∞ at fixed v.
There remain O(sqrt v) arithmetic modes, exact gamma factors and K+1
coefficient functions. No implemented provider, certified evaluation,
cheap bit complexity or small numerical onset follows. Reflection
handles negative height. The finite-height core is a separate input.

This is a local analytical transfer consequence, with proof-author
checking only. It uses the **completion-order component** of the HDA
organization, not a claim that its gamma fluctuation or factorial-zero
hierarchies have been identified.

## 6. The second possible use: mean and fluctuation equations

The HDA [filtered evolution note][h02] has a separate, informative link.
For fixed regulator ε and a fixed nonnegative normalized translation
average A, commuting with the displayed derivatives, it
uses Sε=log(|H|²+ε²), U=A Sε and
\[
 Q=A(S_x^2)-U_x^2-A(S_y^2)+U_y^2,
\]
and derives the Newman-time identity
\[
 U_\lambda=-\tfrac12(U_{xx}-U_{yy})
           -\tfrac12(U_x^2-U_y^2)-\tfrac12Q.
 \tag{16}
\]
The covariance matrix is positive semidefinite; its displayed difference
Q has no automatic sign. HDA's exact cosh control has zero density
variance but Q=900/1681, so density variance alone cannot close that
equation. The example is noncanonical and its exclusion is scoped to the
stated closure rule.

This is useful guidance for any averaged resolvent/Green dynamics:
retain the signed fluctuation term, harmonic/boundary data, regulator
limit and derivative commutators. The physical regulated density is not
the unregulated Green potential, and fixed-regulator smoothing can lose
resolution of high zeros. The current record supplies no canonical
signed closure that makes the Green value favorable. For the present
task this is a secondary bookkeeping connection, not the selected route.

## 7. Controls, classification and the remaining work

This audit follows the [result index][results], especially
[heat-flow cluster11][r11] and [controls12][controls], and the
[patterns index][avoid], particularly [target01][a01],
[control02][a02], [scope07][a07], [coupled payments12][a12rule] and
[status19][a19]. It classifies (1)–(3) as representation identities,
(6) as reuse of an existing local estimate, and (12)–(14) as an analytical
error-transfer consequence. None is a canonical sign estimate.

| Control family | Actual premise absent from the canonical RS application |
| --- | --- |
| Euler-factor/translated-source controls | They change the exact xi field and hence cannot inherit (10)–(11) with unchanged coefficients. |
| Weighted-square, finite-prefix and finite-prime controls | Matched finite data do not supply the complete normalized theta/xi identity and exact RS completion. |
| Reflected super-Gaussian and smooth/positive-primitive controls | Reflection or shape does not supply the canonical gamma/arithmetic expansion. |
| Atomic, polynomial and variable-readout controls | They lack the complete canonical source/profile/cosine-readout conjunction; no canonical constants are assigned to them. |

The heat and recurrence algebra can hold for admissible controls. The
generic B02 theorem can also apply with their own anchors and constants;
accurate acquisition preserves a genuine positive defect signal rather
than eliminating it. Missing a literal identity is not automatic failure
of every inequality derived from it. No new numerical control was run.

The selected use is **field/completion hierarchy → gamma-normalized real
boundary approximation → one-sided logarithmic acquisition**. A future
comparison should assess its complete cost and error against the literal
Fourier-source route on the same signed Green consumer. E03 remains the
already frozen default full-assembly task, unchanged and unactivated.
An alternative RS-based assembly would require its own explicit packet,
not a silent replacement of E03's source contract.

Further obligations are the exact omitted logarithmic tails and prime
tail, finite evaluation and coefficient errors, core/height coverage,
and the actual signed upper value below the defect margin. This audit
does not issue a new numerical or assembly task. It supplies a concrete
local connection for that later decision.

[book]: ../../../../01_heat_density_asymptotics/research-overview/02_BOOK_UNIFIED_HEAT_FLOW_RESEARCH_OVERVIEW_20261026.md
[summary67]: ../../../../01_heat_density_asymptotics/notes/67_CHAT0025_RESEARCH_SUMMARY_AND_HANDOFF_20261026.md
[a15]: ../../../../01_heat_density_asymptotics/ansatz/notes/15_GENERALIZED_TRANSFORMS_AND_HEAT_COMPONENT_HIERARCHIES_20261026.md
[a16]: ../../../../01_heat_density_asymptotics/ansatz/notes/16_GAUSSIAN_FLUCTUATION_HIERARCHY_20261026.md
[r05]: ../../../../01_heat_density_asymptotics/recurrence/notes/05_CONTROLLED_ORDER_GROWTH_AUDIT_20261026.md
[rr04]: ../../../../01_heat_density_asymptotics/recurrence/reviews/04_CONTROLLED_ORDER_GROWTH_ASSESSMENT_20261026.md
[r20]: ../../../../01_heat_density_asymptotics/recurrence/notes/20_MOVING_LOWER_ENDPOINT_20261026.md
[rr14]: ../../../../01_heat_density_asymptotics/recurrence/reviews/14_MOVING_ENDPOINT_ASSESSMENT_20261026.md
[a04]: ../../../../01_heat_density_asymptotics/ansatz/notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
[ar03]: ../../../../01_heat_density_asymptotics/ansatz/reviews/03_COMPLEX_STRIP_AND_BUFFERED_CROSSOVER_ASSESSMENT_20261025.md
[a26]: ../../../../01_heat_density_asymptotics/ansatz/notes/26_RETAINED_ARITHMETIC_MOVING_POSITIVE_BAND_20261026.md
[ar20]: ../../../../01_heat_density_asymptotics/ansatz/reviews/20_RETAINED_ARITHMETIC_MOVING_BAND_ASSESSMENT_20261026.md
[a05]: ../../../../01_heat_density_asymptotics/ansatz/notes/05_FIXED_NEGATIVE_TIME_REPRESENTATIONS_20261025.md
[r02]: ../../../../01_heat_density_asymptotics/recurrence/notes/02_FIRST_FINITE_FLUCTUATION_COMPARISON_20261026.md
[h02]: ../../../../01_heat_density_asymptotics/notes/02_FILTERED_EVOLUTION_AND_FLUCTUATION_IDENTITIES_20261024.md
[og04]: 04_TND_OG_B02_ONE_SIDED_BOUNDARY_LOG_ACQUISITION_20261108.md
[polymath]: https://arxiv.org/html/1904.12438v2#S6.SS2
[results]: ../../../../../../result-summaries/README.md
[r11]: ../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12rule]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a19]: ../../../../../../avoid/19_status_files_that_lag_the_findings.md
