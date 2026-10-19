# UAR-01: corrected residual and coherent transition contract

19 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**, reasoning effort **ultra**. Separate same-model derivation and adversarial review; internal LLM work, no specialist human review.

**Status: shared analytic contract; no new residual estimate.** This completes the definition and bookkeeping task in the [UAR program][program], subject to the linked [review][review]. It selects the corrected S03 approximation throughout S04's sector, fixes its analytic charts and physical prefixes, and identifies the inequalities UAR-02/03 must supply. Those estimating tasks become Ready when this contract is accepted. UAR-04 still requires useful estimates, not definitions.

Read the [result summaries][results] and [patterns to avoid][avoid], especially [collision controls][controls], [theta bookkeeping][theta], [target reformulations][a01], [scoped exclusions][a07], [normalization][a08] and [signed recombination][a12]. Classification: a local analytic interface and research contract, not an RH-equivalent criterion or a quantitative research gain. The cutoff identity below is established prior work from [transport Note 22][matching], also used by S02; it is not claimed as a new theorem.

## 1. One source, one approximation

Use the complete level-one theta field H of the existing manuscript, satisfying H_t=-H_xx. For complex physical coordinate z put s=(1-iz)/2 and

\[
\begin{aligned}
M(s)&=s(s-1)\pi^{-s/2}\Gamma(s/2)/16,\\
m_0(s)&=\log s+\log(s-1)-s\log\pi/2
 +\log(2\pi)/2-\log16+(s/2-1/2)\log(s/2)-s/2,\\
\alpha(s)&=m_0'(s)=1/(2s)+1/(s-1)+\tfrac12\log(s/(2\pi)),\\
m_t(s)&=m_0(s)+t\alpha(s)^2/4,\\
\mathcal A&=\exp\{[m_t(s)+m_t(1-s)]/2\},\qquad
\theta=[m_t(s)-m_t(1-s)]/(2i).
\end{aligned}                                                    \tag{1}
\]

Use the principal logarithmic branches in the respective upper/lower half-planes, continuously throughout each chart; a logarithm of Gamma, when used, is its analytic Stirling branch, not the principal logarithm of its value. The arguments s and 1-s stay off all logarithmic cuts on the disks below. Thus A is holomorphic and never zero, and is positive on the real axis. Write Q=H/A and omega=theta_x<0 on the real chart windows.

For integer n and fixed t define

\[
g_n(s)=\exp\{m_0(s)-s\log n+t(\alpha(s)-\log n)^2/4\},\qquad
G_N(z)=\sum_{n=1}^N[g_n(s)+g_n(1-s)].                         \tag{2}
\]

Both channels are analytic; `2 Re` is used only on the real axis. Set

\[
\tau=z/2+\pi t/8,\quad a=\sqrt{\tau/(2\pi)},\quad p_N=2N+1-2a,
\]
\[
D(p)=\frac{\cos\pi(p^2/2+3/8)}{2\cos\pi p},\qquad
B(p)=\frac{\sin\pi(p^2/2+3/8)-\sqrt2\cos(\pi p/2)}{2\cos\pi p},
\]
\[
\widehat C_N^{an}(t,z)=(-1)^{N+1}\frac{\sqrt\pi}{4}
 e^{-\pi z/8-\pi^2t/64}\sqrt\tau\{\tau D(p_N)-B(p_N)\}.
                                                                    \tag{3}
\]

The square roots use the principal branch in Re tau>0. D and B denote their analytic removable continuations at half-integers; they are not `Re F(p)` and `Im F(p)` at complex p. Every real half-integer zero of the denominator has a matching numerator zero (check its integer residue class modulo four). In particular the sector crosses p=+-1/2. Direct numerical division there is inadmissible. A future profile implementation must use removable values or proved local Taylor charts covering the whole needed p range; S03's fixed Taylor chart is not imported.

The **selected approximation and complete residual** are

\[
f_N=(G_N-\widehat C_N^{an})/\mathcal A,\qquad r_N=Q-f_N.
                                                                    \tag{4}
\]

This is S03's corrected approximation with a general frozen N; S04's raw scalar is G_N/A. No gamma correction is silently added to (4). Its prescribed signed gamma/heat contribution stays in the model for r_N below. Unlike S02's frozen-center exponential, (3) differentiates its full analytic profile.

## 2. Sector, disks, overlaps and derivative budget

For each fixed real 0<t<=1/20 choose the entire closed physical interval

\[
J_t=[a_t,b_t]=[4\pi e^{1/t},4\pi e^{2/t}].                    \tag{5}
\]

At real center c in J_t set L_c=log(c/(4pi)), kappa_c=t L_c, R_c=1/L_c. Use the closed complex disk D_c={|z-c|<=R_c} and its closed real half-window W_c={|x-c|<=R_c/2}. The analytic definition extends to a neighborhood of the closed disk. Centers obey 1<=kappa_c<=2; disk excursions need not obey that same center restriction. Constants proved only at sector centers may not be reassigned to the excursions.

Let nu_t(x)=floor sqrt(x/(4pi)+t/16), right-continuous at equality. Each D_c real projection meets at most one cutoff: R_c<=1/20, whereas successive crossing gaps are 4pi(2n+1). Freeze N as either extremal nu on that projection; across a crossing both choices are permitted as analytic definitions. The source error for each choice must be proved and paid separately. Charts with the same N use exactly the same f_N on overlaps. No center-dependent polynomial or center-frozen correction changes that identity.

The crossings are

\[
\xi_n(t)=4\pi(n^2-t/16).                                    \tag{6}
\]

At a crossing use both N=n-1 and n on D_(xi_n). A closed cover by W_c exists for each fixed t by compactness; it is not an algorithmic cost claim. For endpoints of J_t a crossing disk may be centered at that endpoint, with its analytic extension outside J_t. Freeze t and N in spatial derivatives. In particular L_x=1/x, rather than zero. The center c and R_c are parameters, not differentiated.

The estimating budget is value plus **one** spatial derivative of one complete analytic error. The filtered integral uses the exact second derivative, but the endpoint estimate needs no second-derivative error payment. A later Laguerre or second-jet consumer must explicitly extend this budget. From the inherited S04 phase estimates, on W_c,

\[
|\omega(x)|>L_c/4.001.                                     \tag{7}
\]

This is the same real-window argument as [S04 Note 03][s04-3], independent of cutoff choice. It is not a bound for 1/omega on an unproved complex domain. A disk error epsilon for one real-symmetric holomorphic function d implies at c: |d_x|<=epsilon/R_c; on W_c use the remaining distance to the disk boundary, or the stronger applicable Schwarz-Pick inequality. Do not use the center Cauchy factor unchanged throughout W_c.

## 3. Exact residual split and ledger

Let T_t h(w)=pi^(-1/2) integral_R e^(-v^2) h(w+sqrt(t)v) dv. Define exact heat modes R_n(w)=T_t[M(w)n^(-w)]. The exact RS contour E_N(w) is M(w) times the descending contour crossing (N,N+1), in precisely the [Polymath section 4][polymath] convention used in [S03 Note 06][s03-6]. Its orientation/sign is fixed equivalently by

\[
E_N(w)-E_{N-1}(w)=-M(w)N^{-w}.                             \tag{8}
\]

Use reflected analytic channels, not conjugation of the variable. For an analytic function h write h^sharp(w)=overline{h(overline w)} (conjugating its coefficients, with the reflected contour), and put w_+=1-s. Define

\[
\begin{aligned}
P_N&=\sum_{n\le N}[R_n(s)+R_n(1-s)],\\
\mathscr E_N&=T_t E_N(w_+)+(T_t E_N)^\sharp(s),\quad H=P_N+\mathscr E_N,\\
r_N&=(P_N-G_N)/A+(\mathscr E_N+\widehat C_N^{an})/A.
\end{aligned}                                                   \tag{9}
\]

The edge's reflected contour is essential: E_N need not itself have real coefficients. On real x the edge is 2 Re T_t E_N((1+ix)/2). The finite M modes do have real symmetry, so P_N uses the simpler pair in (9). The fixed-contour Gaussian integrals converge on these charts; their exact representations are inherited inputs. Uniform computable tail inequalities as t tends to zero and N grows are still estimating obligations.

The finite retained correction is fixed without fitting:

\[
\chi_n(w)=\frac1{6w}+\alpha'(w)
 \left\{\frac t4+\frac{t^2(\alpha(w)-\log n)^2}{8}\right\},
\quad K_N=\sum_{n\le N}[g_n(s)\chi_n(s)+g_n(1-s)\chi_n(1-s)]. \tag{10}
\]

Define d_(AB,N)=(P_N-G_N-K_N)/A and e_(edge,N)=(\mathscr E_N+\widehat C_N)/A exactly. Then

\[
r_N=K_N/A+e_{edge,N}+d_{AB,N}.                              \tag{11}
\]

UAR-03 must specify and bound a computable signed edge model ehat_(edge,N), including its full gamma prefactor, before UAR-04 uses rhat_N=K_N/A+ehat_(edge,N). Set d_N=d_(AB,N)+(e_(edge,N)-ehat_(edge,N)). Until that model and its payment exist, rhat_N has no usable complete allowance. No source-inferred edge from H is an independent model.

| Source term | Retained destination | Error destination / owner |
| --- | --- | --- |
| Every finite heat mode, both channels, n<=N | g_n and prescribed g_n chi_n | Exact d_(AB,N); UAR-02 proves uniform central expansion, higher Stirling/curvature terms and both shifted Gaussian tails. |
| Complete fixed-contour heat RS edge | Leading analytic Chat in f_N; actual discrepancy e_(edge,N) in r_N | UAR-03 supplies ehat and complete error, with true gamma factor, RS truncation, negative-u order conditions, Gaussian tails, coherent continuation and profile-chart conversion. |
| Profile, moments, finite sums, quadrature and rounding used in a future implementation | Explicit signed enclosure of that same model | Charge every replacement to d_N or an identified retained-model evaluation error; zero only for an exact operation. No fixed-B constants transfer. |
| Phase and varying normalizer | Equations (1), Z below and physical return | Exact derivatives retained; any numerical enclosure errors charged once in their actual normalized units. |
| Entering mode plus edge change | h_n below, recombined before a norm | Coherent disk payment plus signed-prefix/evaluation error; UAR-03/04. No independent full mode disk. |
| Approximation forcing, anchors and physical sign | Exact forcing below; anchor deferred to UAR-05 | No homogeneous heat assumption, no inferred positive anchor and no uncharged physical return. |

## 4. Adjacent models and the transition that must be paid

The inherited entire identity F(p+2)+F(p)=exp(i pi(p^2/2+p+3/8)), F=D+iB, gives

\[
\Delta C_n=\widehat C_n-\widehat C_{n-1}
 =(-1)^{n+1}\frac{\sqrt\pi}{4}e^{-\pi z/8-\pi^2t/64}
 \sqrt\tau\{\tau\cos\psi_n-\sin\psi_n\},
\quad\psi_n=2\pi(a-n)^2-\pi/8.                              \tag{12}
\]

Consequently, on the common disk, exactly

\[
h_n=f_n-f_{n-1}=\{g_n(s)+g_n(1-s)-\Delta C_n\}/A,
\qquad r_n-r_{n-1}=-h_n.                                   \tag{13}
\]

In particular h_(n,x) includes the derivative of 1/A. At the exact edge p_(n-1)=-1 and p_n=1. The analytic expressions do not generally join continuously: small nonzero jumps are already documented in [Note 22][matching]. Equation (8) makes the jump of the **exact** finite-plus-edge source zero. This explains the required cancellation without assuming that (13) vanishes.

Note 22's explicit matching exponent bounds the entering mode minus the **printed** correction exp(-pi i y/8) Delta C_n(t,x) throughout an upper rectangle. Reusing that bound for (13) requires also paying printed-minus-analytic Delta C_n(t,z), and division by the actual complex A. Only the combined holomorphic difference admits Cauchy. Its lower-half disk follows by reflection. This is a reusable source for UAR-03, not a new or already evaluated uniform bound on (13).

## 5. Primary metric: all physical prefixes with signed transitions

For any one analytic scalar v define the real-axis linear map

\[
Z_v=e^{-i\theta}(v-i v_x/\omega),\quad
\mathcal R_v=v+v_{xx}/\omega^2-\omega_xv_x/\omega^3,\\
I_v(u,x)=\int_u^x e^{-i\theta}\omega\mathcal R_v\,dy
        =i\{Z_v(x)-Z_v(u)\}.
\]

Split [a_t,x] at every cutoff xi_n in its interior. On each subinterval integrate the filtered residual with that subinterval's frozen natural integer. The **primary quantity** is the ordinary piecewise integral

\[
\mathcal I_t(x)=\sum_j I_{r_{N_j}}(u_j,u_{j+1}),\qquad
\mathcal B(t)=\sup_{x\in J_t}|\mathcal I_t(x)|.              \tag{14}
\]

The same formula covers all partial prefixes and both limiting descriptions at a cutoff. No countably infinite partition is used at fixed t. From (13), telescoping gives

\[
\mathcal I_t(x)=i\left\{Z_{r_{N(x)}}(x)-Z_{r_{N(a_t)}}(a_t)
                   +\sum_{a_t<\xi_n\le x}Z_{h_n}(\xi_n)\right\}.
                                                                    \tag{15}
\]

At a left-limit description omit the coincident switch and use the old N; the expression agrees. A crossing at a_t uses the chosen initial right-hand chart and is not counted again. This explicit positive sign is essential. Subtracting i sum Z_h defines a different, compensated endpoint increment; it cannot be called a bound for (14).

If the useful UAR-02/03 outputs supply |Z_(d_N)|<=delta_N at the required endpoints, the candidate complete inequality is

\[
\mathcal B(t)\le\sup_{x\in J_t}
 \left|Z_{\widehat r_{N(x)}}(x)-Z_{\widehat r_{N(a_t)}}(a_t)
                    +\sum_{a_t<\xi_n\le x}Z_{h_n}(\xi_n)\right|
 +\sup_{x\in J_t}(\delta_{N(x)}(x)+\delta_{N(a_t)}(a_t)).     \tag{16}
\]

Add retained-model and signed-transition evaluation errors if not already enclosed in the first term. Every transition remains inside the signed expression before its modulus. If a transition is approximated, its complete error must be paid. A center cancellation, an uncomputed signed sum, or exact telescoping alone does not establish a small right-hand side. Equation (16) states the new inequality to prove, not its value. Local analogues restrict (14)-(16) to one W_c; they are separate deliverables from all of J_t.

Physical propagation would use exactly

\[
Z_Q(x)=Z_Q(a_t)+Z_{f_{N(x)}}(x)-Z_{f_{N(a_t)}}(a_t)
          -\sum Z_{h_n}(\xi_n)-i\mathcal I_t(x).             \tag{17}
\]

Thus the approximation's signed variation, a paid nonzero anchor and the complete residual allowance are all needed. No physical acceptance test is introduced here.

## 6. Comparisons, forcing and premise screen

Keep comparisons in |Z|/|I| units. S04's local 46.679 exp(-b*/t) applies to r_raw=Q-G_N/A with **one frozen N=nu_t(c), and prefixes c to y in W_c**. Since r_N=r_raw+Chat_N/A, a valid converted comparator for that same chart is the raw allowance **plus the enclosed signed increment of Chat_N/A**. The constant is not automatically available for the alternate extremal N or a piecewise prefix crossing a cutoff; those need their own conversion and transition payments.

A direct corrected endpoint comparator comes from a newly proved disk envelope epsilon for r_N. Real-symmetric Schwarz-Pick gives at the center the sharper available first-jet radius epsilon max{1,1/(R_c |omega|)}; at real x in W_c it gives epsilon max{1,1/[R_c |omega(x)|(1-u^2)]}, u=(x-c)/R_c. This retains coupling between value and derivative and is stronger than their independent Cauchy boxes. Source-informed direct comparison must use the same source accuracy, domain, approximation and physical normalization, including any stronger retained coupled information. There is presently no numerical comparator for the whole interval (5) in this corrected metric. S03's 0.000854 and 0.000266448 apply on B only.

For UAR-04 the gate is a strictly smaller **complete** allowance than the strongest available matched comparator, or a quantitatively new uniform domain, after (16)'s transition and remainder terms. S04's divergent coefficientwise sum concerns raw entering modes; it excludes that payment rule, not (13) or (16). Retuning fixed-B remainder precision is not selected.

With a0=A_x/A and V=A_t/A+a0_x+a0^2, fixed N gives

\[
r_{N,t}+r_{N,xx}+2a_0r_{N,x}+Vr_N
 =-\{f_{N,t}+f_{N,xx}+2a_0f_{N,x}+Vf_N\}.                  \tag{18}
\]

This follows by substituting H=A(f_N+r_N) in H_t+H_xx=0. The endpoint route does not require an estimate of this forcing, but does not remove it. For any residual error d,

\[
\delta H=A d,\quad\delta H_x=A(d_x+a_0d),\quad
\delta H_{xx}=A\{d_{xx}+2a_0d_x+(a_0^2+a_{0,x})d\}.         \tag{19}
\]

| Control | Missing premise / required interpretation |
| --- | --- |
| Finite-prime orbit; finite weighted squares | Unchanged complete normalized theta reflection and full coefficient sequence. Analytic-only event existence supplies no effective test box. |
| Reflected super-Gaussian, smooth shape, positive primitive | The specific theta integer-square expansion and matching gamma/RS contour. Reflection, regularity and auxiliary positivity do not supply them. |
| Finite Euler deformation | Unchanged level-one completed coefficients. Its negative-Laguerre witness remains a sign witness, not an enclosed collision. |
| Polynomial event, counter-kernel, moving wall | The gamma/RS arithmetic source; generic rotation and transport identities still hold. A future physical consumer must reject its own enclosed events and pay wall flux. |

No theta allowance is applied to another source. The [source-pinned receipt][receipt] checks contract algebra, transition signs and invalid-input/source guards. Its own-envelope polynomial event shows that zero residual does not imply a positive physical margin. Existing source-control replays remain inherited evidence; no unchanged consumer replay is presented as validation of a new estimate. [Separate same-model review][review].

**Next work:** UAR-02 should first derive a height-dependent summed bound for d_(AB,N) and its first derivative using full heat weights, explicit Gaussian shift/tails and growing N. In parallel UAR-03 should select its signed edge model, pay coherent disk matching from (12)-(13), and bound the edge-model error on the identical charts. UAR-04 remains waiting for both useful outputs. The real bridge, complex exterior, new coverage, cost advantage and a new Newman bound remain open.

[program]: ../research-overview/03_UNIFORM_ARITHMETIC_RESIDUAL_RESEARCH_PROGRAM_20261019.md
[review]: ../reviews/02_UAR01_CONTRACT_INTERNAL_REVIEW_20261019.md
[receipt]: ../numerics/UAR01_CONTRACT_CHECK_20261019.json
[s03-6]: ../03_normalized_jet_rotation/notes/06_ARITHMETIC_GAMMA_AND_EDGE_CORRECTIONS_20261019.md
[s04-3]: ../04_time_height_scaling/notes/03_UNIFORM_LOCAL_RESIDUAL_TRANSFER_AND_CUTOFF_PAYMENT_OBSTRUCTION_20261019.md
[matching]: ../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/22_THETA_CUTOFF_MATCHING_AND_UNIFORM_PHYSICAL_JETS_20261011.md
[polymath]: https://arxiv.org/html/1904.12438v2#S4
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[theta]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a08]: ../../../../../avoid/08_normalization_and_constant_slips.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
