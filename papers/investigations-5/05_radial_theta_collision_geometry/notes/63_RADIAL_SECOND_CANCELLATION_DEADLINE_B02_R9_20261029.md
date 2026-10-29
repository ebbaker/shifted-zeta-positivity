# CTF-B02 R9: radial second cancellation shortens a paid upper deadline

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort
max**, Investigation05 **chat0030**, **Assess CTF-B02 deadline control**.

**Status: proved in-note; same-assistant checks only.** This single route
reduces a carrier-paid **conditional collision upper deadline** by the
explicit fraction
\[
 \varepsilon_9=\frac{41}{441}
       \left[1-\left(\frac{2873}{2880}\right)^{4/5}\right]>0.
 \tag{1}
\]
It is about 0.018082 percent of the comparator, a constant-only decimal
illustration. The comparator already optimizes the old first-moment
Fourier split. No source-specific lower lifespan, finite compression at
the new deadline, or larger collision-free domain is obtained. Positive
weighted-square collision controls share the sufficient premises.

The [R9 intake][progress] was recorded before derivation under
[Continuation62][n62]. It selected one radial second-cancellation test,
including the drift's second variation, at the unchanged theta mark
\(p=(T,A)=(1/4,2)\). The optimized first-moment comparator below strengthens
the intake's original half-energy comparator within that same test.
No second mechanism, mark search or numerical acquisition was introduced.
[Self-assessment33][review] is distinct from the unexecuted [E08 packet][packet].

## 1. Fixed data, target and exact scope

Keep [Note28][n28]'s common fixed-mark evolution and unit preparation:
\[
 W=(U,V),\quad W_s=\Delta W+\alpha\operatorname{div}(vW),\quad
 v=X+\frac{X}{1+|X|^2},\quad
 E_0=\|W_s\|_2^2>0,
\]
\[
 G=\|\nabla W\|_2^2,\quad D=\int (\operatorname{div}v)|W|^2,
 \quad\alpha=2G/D,\quad B(s)=\int_0^s\alpha,
 \quad3E_0\le D\le6E_0.
 \tag{2}
\]
Here V is the actual derivative in the running frequency, holding the
mark and common feedback path fixed. Set \(q(u)=e^{u^2/4}\Phi(u)\), with
the complete theta source, \(u=\log r/2\), and
\[
 \rho=\mathbf1_{r\ge1}\frac{q(u)}{8\pi r^3},\quad
 W_0=K_1*\{\rho(\cos(2u),-u\sin(2u))\},\quad
 h_0=K_1*\{\rho(1+u^2)\}.
\]
The full Jacobian is \(4\pi r^2\rho\,dr=q\,du\). Define the carrier data
\[
 M=\int h_0=M_0+M_2,\quad M_j=\int_0^\infty u^jq(u)\,du,
\]
\[
 R_0=\int |X|^2h_0
   =\int_0^\infty e^{4u}(1+u^2)q(u)\,du+6M,
 \qquad \overline P=\sqrt{MR_0}.
 \tag{3}
\]
Thus \(|W_0|\le h_0\), \(P_0:=\int|X||W_0|\le\overline P\),
\(\int |X|^2|W_0|\le R_0\), and
\[
 E_0\le(8\pi)^{-3/2}M^2.
 \tag{4}
\]
These are complete initial-data costs. An eventual numerical upper
deadline would also need a positive rigorous lower budget for E0; no
numerical deadline is claimed here.

The theorem proved below is conditional on
\(m=\int W_0=(H,H_a)=0\), in the inherited radial prepared solution class,
and on \(R_0/M\le9\). It states
\[
 \boxed{S_{\max}\le \overline S_9
  :=(1-\varepsilon_9)\overline S_{1,\mathrm{opt}}
  <\overline S_{1,\mathrm{opt}},\qquad
 \overline S_{1,\mathrm{opt}}
  =6\left(\frac7{20\pi^2}\right)^{2/5}
       \frac{\overline P^{4/5}}{E_0^{2/5}}.}
 \tag{5}
\]
The concentration premise is paid for the full theta source in Section2.
It is also shared by positive weighted-square sources at T=1/4, at
their own frequencies. Their known collisions make the theorem's class
nonempty; it is not a theta collision assertion.

The intended remaining consumer is an independently proved finite B
bound through the **closed** time \(\overline S_9\). This note reduces
that target; it does not pay it. [R8][n59] still supplies its existing
closed local horizon and open extended lifespan only. This is a finite
constant milestone under [avoid01][a01], with the [result index][results],
[spatial cluster][spatial], [controls][controls], [avoid index][avoid],
[premise screen][a02], [scope rule][a07] and [utility rule][a20] retained.

## 2. Complete source payment: the prepared carrier has R0/M < 9

[Note55][n55] proves for the complete sum
\(q'\le(1/5-74u)q\), by summing a bound valid for every positive square
summand. Set \(p(u)=(1+u^2)q(u)\). Since \(2u/(1+u^2)\le1\),
\[
 p'(u)\le(6/5-74u)p(u),\qquad
 p(u+t)\le p(u)e^{6t/5-74ut-37t^2}.
\]
For the probability density p/M on the half-line this gives
\(\Pr\{u\ge t\}\le e^{6t/5-37t^2}\). Integration of the positive tail,
with every source term retained, yields
\[
 \frac1M\int e^{4u}p(u)\,du
 \le1+4\int_0^\infty e^{26t/5-37t^2}\,dt
 \le1+4e^{169/925}\sqrt{\pi/37}<\frac83.
 \tag{6}
\]
The last bounds are elementary: \(\pi<4\) gives
\(\sqrt{\pi/37}<1/3\), and
\(e^{169/925}\le(1-169/925)^{-1}=925/756<5/4\).
Consequently
\[
 \boxed{7<R_0/M<26/3<9.} \tag{7}
\]
All moment, differentiation and endpoint justifications are those of
Note55's complete double-exponential tail. The extra six in (3) is the
second moment of the unit preparatory Gaussian, not a discarded cost.
No first-jet value is used in (6).

## 3. The full second variation of the common transition kernel

On any compact interval within the existing lifespan, regard its scalar
alpha path as fixed. The forward density kernel is that of
\[
 dX_s^y=-\alpha(s)v(X_s^y)\,ds+\sqrt2\,d\mathcal B_s,
 \qquad X_0^y=y.
\]
This is the same transition used in Note28. Differentiation is in its
starting **spatial point**, not in the marked source or feedback solution.
The additive Brownian term has zero such derivatives. Subtracting it
leaves an ordinary integral equation with smooth globally bounded drift
derivatives; difference quotients and Gronwall justify the following
first and second variation equations pathwise. Bounded variations then
justify differentiating expectations.

Write \(J_s=D_yX_s^y\), \(K_s[h,k]=D_y^2X_s^y[h,k]\), and
\(\kappa=7/8\). The inherited bounds \(Dv\ge\kappa I\) and
\(\|D^2v\|\le20\) give
\[
 J'=-\alpha Dv(X_s)J,\quad J_0=I,\quad \|J_s\|\le e^{-\kappa B},
\]
\[
 K'=-\alpha Dv(X_s)K-\alpha D^2v(X_s)[Jh,Jk],\quad K_0=0,
\]
\[
 \|K_s[h,k]\|\le\frac{20}{\kappa}
 e^{-\kappa B}(1-e^{-\kappa B})|h||k|.
 \tag{8}
\]
The second line is essential for the non-affine drift. For the backward
test \(f_{s,\xi}(y)=\mathbb E e^{-i\xi\cdot X_s^y}\), put
\(\tau=e^{-\kappa B}\). Its Hessian has the uniform bound
\[
 \|D_y^2 f_{s,\xi}\|\le |\xi|^2\tau^2
       +(20/\kappa)|\xi|\tau(1-\tau).
 \tag{9}
\]
Radial W0 has \(\int y_iW_0(y)dy=0\). Under m=0, subtract both the
constant and linear Taylor terms of f at zero from
\(\widehat W_s(\xi)=\int W_0(y)f_{s,\xi}(y)dy\). Taylor's integral
remainder and (3) give the fully paid estimate
\[
 \boxed{|\widehat W_s(\xi)|\le
 \frac{R_0}{2}\left\{|\xi|^2\tau^2+
              \frac{20}{\kappa}|\xi|\tau(1-\tau)\right\}.}
 \tag{10}
\]
It is valid together with Note28's first-moment allowance
\(|\widehat W_s(\xi)|\le\overline P|\xi|\tau\). In particular,
radiality does **not** license dropping the curvature term in (10).
At large compression this estimating route still has a term linear in
frequency. No uniform quadratic-frequency improvement is inferred.

## 4. Match the optimized first-moment comparator

Use the unnormalized forward Fourier transform. Plancherel and the old
allowance imply, for every frequency cutoff R,
\[
 G\ge E_0R^2-\frac{\overline P^2\tau^2R^7}{10\pi^2}.
\]
The right side has its global maximum over R>=0 at
\[
 r(B)=r_0e^{2\kappa B/5},\quad
 r_0=\left(\frac{20\pi^2E_0}{7\overline P^2}\right)^{1/5}.
\]
At this cutoff the low-frequency energy allowance is \(2E_0/7\), so
\[
 G\ge(5/7)E_0r(B)^2,\quad
 \alpha\ge c_1 e^{\beta B},\quad
 c_1=(5/21)r_0^2,\quad \beta=4\kappa/5=7/10.
 \tag{11}
\]
Its upper deadline is \(1/(\beta c_1)=\overline S_{1,\mathrm{opt}}\).
Note28's half-energy split, using the same Pbar and E0, is larger by
the reciprocal of \((7/10)(7/4)^{2/5}\). That elementary optimization
is credited to the comparator, not to the new second-cancellation gain.
Optimality here refers only to this displayed one-power Fourier split.

## 5. A paid initial compression window and its complete deadline saving

Fix \(k=21/20\). Minkowski's inequality in the low-frequency ball and
(10) give
\[
 \left[(2\pi)^{-3}\int_{|\xi|\le R}|\widehat W_s|^2\right]^{1/2}
 \le\frac{R_0}{2}\left\{
 \frac{\tau^2R^{7/2}}{\sqrt{14\pi^2}}+
 \frac{20}{\kappa}\frac{\tau(1-\tau)R^{5/2}}{\sqrt{10\pi^2}}
 \right\}. \tag{12}
\]
Set R=kr(B), divide by \(\sqrt{2E_0/7}\), and put
\(Z=(R_0/M)r_0^2\). The resulting bound is
\[
 k^{7/2}\sqrt{5Z/28}\,e^{-3\kappa B/5}
 +\frac{80}{7}\sqrt{R_0/M}\,k^{5/2}(1-e^{-\kappa B}).
 \tag{13}
\]
Every quantity is paid. Equations(4),(7) imply
\[
 Z^5=\frac{400\pi^4E_0^2R_0^3}{49M^7}
 \le\frac{400\pi}{49\cdot512}(R_0/M)^3<3^5.
\]
Also \(k^7<3/2\), \(k^{5/2}<k^3<6/5\), and
\(45/56<81/100\). The first term of (13) is therefore <9/10.
The second is at most1/10 whenever
\[
 0\le B\le b_0:=\frac87\log\frac{2880}{2873},
 \quad 1-e^{-\kappa B}\le\frac7{2880},
\]
because \((80/7)\,3\,(6/5)\,(7/2880)=1/10\).
On this entire compression window, (12) is <\(\sqrt{2E_0/7}\).
Hence
\[
 \boxed{\alpha\ge k^2c_1e^{\beta B}\quad(0\le B\le b_0),
 \qquad \alpha\ge c_1e^{\beta B}\quad(B>b_0).} \tag{14}
\]
This is a compression window, not an assumed physical-time interval.
Under m=0 Note28 already ensures finite breakdown and B tending to
infinity. G>0 for a nonzero L2 field, so B is strictly increasing and
may be used as a clock. Integrating \(ds/dB=1/\alpha\) through both
ranges gives
\[
 S_{\max}\le\frac1{c_1}\left[
 k^{-2}\int_0^{b_0}e^{-\beta b}db+
 \int_{b_0}^\infty e^{-\beta b}db\right]
 =\overline S_{1,\mathrm{opt}}
   [1-(1-k^{-2})(1-e^{-\beta b_0})].
\]
Since \(1-k^{-2}=41/441\) and \(\beta b_0=(4/5)\log(2880/2873)\),
this proves (1),(5). No local restart, non-summable time series or
unknown exponential upper allowance is used.

## 6. Matched direct comparison and retained costs

The gain in (5) compares upper deadlines using the **same carrier-paid
Pbar**, exact E0 and optimized first-moment splitting. It is not a claim
that \(\overline S_9\) is smaller than Note28's deadline formed with
the exact \(P_0=\int|X||W_0|\), which can be much smaller than Pbar.
If P0 is separately known, use the minimum with its optimized old bound;
no ranking against that additional payment or acquisition advantage is
established. The new formula pays the second moment R0, whose cost is
explicit in (3), and uses its source-derived concentration bound.

More strongly, the same complete-source input at this theta mark already
gives \(-H_a\ge35M_2/18>0\) by Note55. With
\(r_\mu=c_3(35M_2/18)^{7/3}E_0^{-2/3}\),
\(c_3=(3/7)(15/(14\pi))^{2/3}\), [Note29][n29] gives
\[
 B(s)\le\tfrac12\log(R_0/r_\mu)+3Ms/r_\mu
\]
on **every finite horizon**, and then its explicit G and alpha bounds.
This directly known margin excludes the hypothetical collision before
the present deadline argument. No improved physical domain, dynamical
theta separator, measured cost saving, or evidence about RH follows.
The smaller conditional target is a supporting estimate only.

The source operator, cutoff, residual and actual higher jets are unchanged:
\(\mathcal R_0=[\mathcal A_T,K_1*](F_0,F_1)\ne0\),
\(\mathcal R_s=L_s\mathcal R+[\mathcal A_T,L_s]W\), and
\(J_{2,s}=-\mathcal P_s^pK_1*(u^2F_0)\).
Multiplication precedes preparation. Both commutators of Notes31/40,
all cutoff derivatives, the combined \(\Theta+\mathcal R=0\) at r=1,
and the whole inner ball remain. This argument changes no residual
estimate and supplies no bound for its energy through S9. Integrations
use the inherited prepared weighted class and the whole spatial domain.

## 7. Controls and disposition

| Comparison | Premises and scope of this one route |
| --- | --- |
| Positive weighted-square | The per-summand inequality from Note55 survives positive weights. Thus (6),(7),(4), radiality and the second-variation argument apply at T=1/4 for every fixed frequency. The registered three-square collision near44.13 shares the sufficient premises and receives a shorter upper deadline, not exclusion. Full unit coefficients/reflection fail but are unused as a separator. |
| Exact Gaussian-polynomial cosine | Radial cancellation and transition bounds hold. Its carrier concentration fails: at T=1/4, (M2+M4)/(M0+M2)=97/248; e^(4u)>=1+8u² gives R0/M>=7+97/31=314/31>9. It lacks canonical square arithmetic. Failure of this sufficient concentration condition does not rule out a different payment for that control. |
| R6 fixed-amplitude polynomial kernels | Full cosine/Newman compatibility fails. The bound by rho(1+u²) used in (3),(4) is not supplied for those polynomial kernels. Their prepared radial fields still satisfy the generic second-variation argument with their actual moments; no general failure of (10) is claimed. |
| Finite-prime orbit | Full reflection/unchanged source fail. Prepared radial finite-moment cases share the kernel argument; R0/M<=9 is not acquired here. High-gap event qualifications remain. |
| Reflected super-Gaussian | Full square source fails; radial cancellation and preparation remain. No concentration value is asserted; the registered pi/4 event is outside the theta application mark. |
| Smooth shape / positive primitive | Canonical source fails. Smooth preparation on the inherited moment domain shares the generic argument; shape or primitive positivity does not by itself provide (7). |
| Euler-factor | Source/conductor are modified. Admitted radial cases share the generic argument; concentration is not evaluated. A Laguerre witness is not automatically a double event. |
| Atomic/profile / continuous compact | Atomic inputs remain outside the imported source-function theorem. Admitted continuous prepared sources may use the theorem if its quantitative concentration premise is established; no such new instance is claimed. |
| RH-conditional endpoint | Retain the original RH condition, altered arithmetic and escaping heights. The concentration premise is not evaluated. |

For an admitted zero-mass control satisfying (4),(7), R8 and (5) imply
\(L_{\rm new}\le S_{\max}\le\overline S_9\). This consistency does not
pay a lower lifespan through the deadline. The global-curvature estimate
does not justify a purely quadratic Fourier bound for all B; only the
finite window (14) was used. Stronger kernel estimates remain outside
this bounded comparison.

**Stop R9 with the paid gain (5). Parent B02 remains partial.**
**Next: [E] CTF-E08 R9 — Sol**, the fixed proof/cost/control assessment.
No E07 is needed for an already supplied proof; E03/B03 remain gated.
No manuscript expansion, source quadrature, PDE evolution or model
dispatch occurred. The [constant check][check] is exact rational
bookkeeping plus explicitly labeled floating illustrations, not a source
certificate or proof substitute.

Actual thread `01a18980-963d-7950-9620-bd1694a4cc30`, research turn
`01a18981-1939-7193-b0ba-f183b5120fa8`, **gpt-6-astra / max**.
[Chat0030][history] retains its own identity, including the interrupted
Sol/ultra opening. No research result or independent review is attributed
to that opening; no subagents were used. [Continuation64][next] carries
the model-change guidance.

The second-variation estimates are derived above from the inherited
transition representation, not imported as a nonlinear-feedback theorem.
The Fourier normalization was rechecked in the already cataloged
[Hunter, Theorem5.71, printed p.171](https://www.math.ucdavis.edu/~hunter/pdes/pde_notes.pdf),
29 October 2026; his normalized forward transform is converted to the
unnormalized convention here. [Reference11][ref11] retains the classical
context. No novelty search or specialist verification is claimed.

[n28]: 28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md
[n29]: 29_POSITIVE_CARRIER_COMPARISON_AND_QUANTITATIVE_REGULARITY_20261028.md
[n55]: 55_COSINE_JET_CORRELATION_B02_R7_20261029.md
[n59]: 59_DIFFUSION_VARIANCE_COMPRESSION_BOUND_B02_R8_20261029.md
[n62]: 62_COMPRESSION_HORIZON_AND_MODEL_CONTINUATION_20261029.md
[next]: 64_RADIAL_DEADLINE_AND_MODEL_CONTINUATION_20261029.md
[review]: ../reviews/33_RADIAL_SECOND_CANCELLATION_B02_R9_SELF_ASSESSMENT_20261029.md
[packet]: ../research-progress/handoffs/CTF-E08_RADIAL_SECOND_CANCELLATION_ASSESSMENT_REQUEST_R9_20261029.md
[progress]: ../research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md
[check]: ../numerics/26_RADIAL_DEADLINE_CONSTANT_CHECKS_20261029.json
[history]: ../chat-histories/0030_2026-10-29T21-11-08Z_assess-ctf-b02-deadline-control.json
[ref11]: ../references/11_CONSERVATIVE_FEEDBACK_AND_DIFFUSION_CONTRACTION_20261028.md
[results]: ../../../../result-summaries/README.md
[spatial]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a20]: ../../../../avoid/20_volume_without_a_gain.md
