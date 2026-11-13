# RSCT-B01 r5: signed correlation with event equations, and a phase-disk failure

11 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance, RSCT chat0002. Actual model and reasoning effort are unavailable in the capture registry; recommendations are separate from provenance.

**Status: proved in-note from named inherited approximation inputs; same-assistant checking only.** This pass tests one proposed signed-correlation estimate: a nonnegative lower bound for the complete Poisson quadratic expression on the product of coefficient disks, intersected with the two local event equations. The estimate is false in that relaxed class, by an explicit feasible point whose value is negative of order L^(-2), even with the retained correction and carrier. **The witness attenuates modes and does not have the actual unit-modulus arithmetic phases. It is not a canonical event.** No zero-exclusion region or executable E01 method is obtained.

Read the [result index](../../../../result-summaries/README.md), [cluster11](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md), [controls12](../../../../result-summaries/12_collision_controls_and_screening.md) and [avoid index](../../../../avoid/README.md), particularly [01](../../../../avoid/01_restating_the_target.md), [02](../../../../avoid/02_shape_only_arguments_and_the_controls.md), [07](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md). [Decision05](../brainstorm/notes/05_RSCT_B01_R5_SIGNED_CORRELATION_DECISION_20261111.md) is the bounded return.

## 1. Fixed objects, candidate and its exact information class

Retain all of [Note06](06_RSCT_B01_R4_MICROSCOPIC_EVENT_EXPANSION_20261111.md):
\[
 L=\log(a/(4\pi)),\quad T=c/L,\quad 1/2\le c\le1,
 \quad z=a+w/L,\quad N=\lfloor e^{L/2}\rfloor,
\]
\[
 d_n=n^{-1/2}\exp\{c[(\log n)^2-L\log n]/(4L)\},\quad
 \lambda_n=\frac14-\frac{\log n}{2L},\quad
 \phi_n=\Theta(T,a)-(a/2+\pi T/8)\log n.                  \tag{1}
\]
The full physical field is f(w)=H_T(a+w/L)/A(T,a+w/L). Its complete approximant is
\[
 q(w)=\sum_{n\le N}d_n\cos(\phi_n+\lambda_n w)+K(w),
 \qquad |\partial_w^j(f-q)|\le\epsilon=C_Ra^{-3/4},\quad j\le2. \tag{2}
\]
K is exactly the normalized gamma/RS correction in Note06 (3). On each fixed scaled disk its derivatives through order two are O_R(χ), where
\[
 \chi=a^{-1/4}e^{-cL/16}.                                \tag{3}
\]
Time and cutoff remain fixed in every spatial derivative. All source buffers, complete Gaussian exterior, reflected arms, heat phase and quadratic heat weights in Note06 are inherited with their recorded evidence level. No new derivative provider or Euler product is imported. Since the branches are continued from positive a, K is holomorphic locally and real on the real w-axis; K(0), K′(0) are real.

Write the **actual** quadratures x_n=d_n cos φ_n, y_n=d_n sin φ_n. Then
\[
 q(w)=\sum_{n\le N}[x_n\cos(\lambda_nw)-y_n\sin(\lambda_nw)]+K(w),
\quad x_n^2+y_n^2=d_n^2.                                \tag{4}
\]
At any event of multiplicity m≥2, f(0)=f′(0)=0, so
\[
 |\sum_n x_n+K(0)|\le\epsilon,\qquad
 |-\sum_n\lambda_n y_n+K'(0)|\le\epsilon.               \tag{5}
\]
These are necessary local equations for every m≥2, not a restriction to double events. They do not encode the other m−2 equations, global all-realness or the reflected −a event.

**Selected method.** Keep the entire signed quadratic expression below, but replace the exact circle and common-logarithmic-phase conditions by the convex constraints
\[
 \mathcal F_\epsilon=\{(x,y):x_n^2+y_n^2\le d_n^2\ (n\le N),
               \text{both residuals in (5) at most }\epsilon\}. \tag{6}
\]
The tested estimate is that D_a(S_{x,y})≥0 throughout this set, ideally with a margin exceeding the paid error, where S=q−q(0)−wq′(0). Actual event quadratures would belong to this set. A valid positive lower bound here would therefore provide an exclusion in the stated band. Proving it by constrained quadratic positivity or multipliers of (5) is a concrete candidate method, not an assumed arithmetic inequality.

This is deliberately a *stronger* estimate than one on the actual phases. The relaxation permits attenuation, including zeroing a mode; it does not preserve the exact coefficient magnitudes. Its failure stops only this method. Merely retaining signed cross terms while enlarging their feasible phase set does not guarantee that the enlargement preserves a lower sign. Classification under avoid/01: the new test is a finite-dimensional estimating method with a falsifiable sign prediction; the underlying all-domain Poisson criterion was already classified in Note03 and is not new progress.

## 2. The full signed correlation, before any estimate

Fix β>0 independently of a,c. Put y_phys=β/L, z=a+iβ/L and retain the physical coefficient
\[
 \mathfrak d_a=2\left(1+\frac{y_{\rm phys}^2}{4a^2+y_{\rm phys}^2}\right)
             +\frac\beta L\Im(A_z/A)(T,z)
             =2+O_\beta(a^{-2}L^{-2}).                  \tag{7}
\]
For any q of (4), define S(w)=q(w)−q(0)−wq′(0), and write S(iβ)=X(β)−iY(β). With
\[
 C_n=\cosh(\beta\lambda_n)-1,\quad B_n=\sinh(\beta\lambda_n)-\beta\lambda_n,
 \quad R_n=\lambda_n\sinh(\beta\lambda_n),\quad
 V_n=\lambda_n[\cosh(\beta\lambda_n)-1],
\]
\[
 K^\circ(w)=K(w)-K(0)-wK'(0),
\quad X=C\cdot x+\Re K^\circ(i\beta),\quad
 Y=B\cdot y-\Im K^\circ(i\beta),
\]
we have X′=R·x+(Re K°(iβ))′, Y′=V·y−(Im K°(iβ))′, where these primes differentiate β. Direct substitution, using ∂_βS(iβ)=iS′(iβ), gives
\[
 \boxed{D_a(S)=\mathfrak d_a(X^2+Y^2)-\beta(XX'+YY').}     \tag{8}
\]
This is precisely Note06 (11). No derivative of the β-dependent coefficient \(\mathfrak d_a\) is taken in (8).

In particular the quadratic blocks, with all n,m cross terms retained, are
\[
 Q_x=\mathfrak d_a CC^t-\tfrac\beta2(CR^t+RC^t),\qquad
 Q_y=\mathfrak d_a BB^t-\tfrac\beta2(BV^t+VB^t).          \tag{9}
\]
The retained correction contributes its exact linear cross terms and constant term through (8). For actual x,y, their products include both difference and sum phases:
\[
 x_nx_m=\tfrac12d_nd_m[\cos(\phi_n-\phi_m)+\cos(\phi_n+\phi_m)],
\quad
 y_ny_m=\tfrac12d_nd_m[\cos(\phi_n-\phi_m)-\cos(\phi_n+\phi_m)].
\]
Here φ_n−φ_m=−(a/2+πT/8)log(n/m) and φ_n+φ_m=2Θ−(a/2+πT/8)log(nm). Neither reflected sum phase nor any diagonal is dropped. Thus (8)–(9) test a signed-correlation estimate, rather than the termwise absolute allowance of r4.

For the **physical** all-real event, Note06 (12) remains
\[
 D_a(f)=\left[(2-m)k_a-y_{\rm phys}^2\sum_{r\ne\pm a}
        \frac1{(a-r)^2+y_{\rm phys}^2}\right]|f(i\beta)|^2<0,
 \quad k_a=1+\frac{y_{\rm phys}^2}{4a^2+y_{\rm phys}^2}.     \tag{10}
\]
All copies of both reflected event roots are removed; other multiple zeros remain. The complete acquisition error in passing from f to S at an event is
\[
 \eta_a=O_\beta(a^{-3/4}e^{(1/4-c/16)L}/L^2+a^{-3/2})
                      =o(L^{-2}),                      \tag{11}
\]
uniformly in c, by Note06 (13)–(14). No denominator floor is used. This transfer is asserted for the physical field only, not for arbitrary relaxed quadratures.

## 3. A feasible negative point, with the exact correction retained

For all sufficiently large a, N≥2. Let
\[
 r=\lambda_1=1/4,\quad h=\frac{\log2}{2L},\quad
 \lambda_2=r-h,\quad t=d_2/2.
\]
Define the following point of the **relaxed** coefficient set:
\[
 x_1=t-K(0),\quad x_2=-t,\quad y_1=4K'(0),\quad y_2=0,
 \qquad x_n=y_n=0\quad(n\ge3).                         \tag{12}
\]
Then ∑x_n+K(0)=0 and −∑λ_ny_n+K′(0)=0 exactly. Moreover
\[
 2^{-7/4}\le t\le 2^{-3/2}
\]
after L≥log 2: the exponent in d_2 is between −(3/4)log 2 and −(1/2)log 2. Since χ→0 uniformly, (x_1,y_1) lies strictly inside its radius-one disk at a finite onset. The second point has modulus t=d_2/2 and all other points have modulus zero. Hence (12) belongs even to the exact-equation subset \(\mathcal F_0\subset\mathcal F_\epsilon\).

Its q, whose constant and linear jets already vanish, is
\[
 q_*(w)=t[\cos(rw)-\cos((r-h)w)]+J(w),
\quad J(w)=K(w)-K(0)\cos(rw)-4K'(0)\sin(rw).             \tag{13}
\]
Thus S_*=q_*. On each fixed scaled disk J,J′=O_β(χ). Both the numerical values of K(0), K′(0) and the whole holomorphic K(w) remain in (13); no favorable sign for them is assumed.

First take the two-mode part p(w)=t[cos(rw)−cos((r−h)w)]. Set
\[
 U(\beta)=\cosh(\beta r)-\cosh(\beta(r-h)),\qquad x=\beta/4.
\]
At iβ the value p=tU is real and its w-derivative is −itU_β. Consequently
\[
 D_a(p)=t^2[\mathfrak d_a U^2-\beta UU_\beta].            \tag{14}
\]
Taylor expansion in h, at the fixed positive β, gives
\[
 U=h\beta\sinh x+O_\beta(h^2),\quad
 U_\beta=h(\sinh x+x\cosh x)+O_\beta(h^2).
\]
Define the explicit positive constant
\[
 C_\beta=\frac{(\beta\log2)^2}{4}\sinh^2(\beta/4)
                  [(\beta/4)\coth(\beta/4)-1]>0.        \tag{15}
\]
Positivity follows from x cosh x−sinh x>0 for x>0, whose derivative is x sinh x>0. Equations (7) and (14) yield
\[
 D_a(p)=-\frac{t^2C_\beta}{L^2}+O_\beta(L^{-3})
                                      +O_\beta(a^{-2}L^{-4}).
\]
Since p,p′=O_β(L^(-1)) and J,J′=O_β(χ), restoring the correction costs O_β(χ/L+χ²). In total
\[
 \boxed{D_a(S_*)=-\frac{t^2C_\beta}{L^2}
       +O_\beta(L^{-3}+\chi/L+\chi^2+a^{-2}L^{-4}).}     \tag{16}
\]
All bounds are uniform in c∈[1/2,1]. As χL→0 and t²≥2^(-7/2), a finite uninstantiated onset gives
\[
 \boxed{\inf_{\mathcal F_\epsilon}D_a(S)\le D_a(S_*)
                    \le-\frac{2^{-9/2}C_\beta}{L^2}<0.} \tag{17}
\]
This is an upper bound on the relaxed infimum from a displayed feasible point, not a claim to compute its optimum. The negative value is asymptotically larger in magnitude than the error allowance (11). Assigning a smaller approximation uncertainty cannot make the proposed lower bound on this feasible set true.

Without K the mechanism has the exact factorization cos(rw)−cos((r−h)w)=−2 sin((r−h/2)w)sin(hw/2). It is a double zero at w=0 with all real zeros, and at iβ its squared modulus grows faster than β^4. This explains the sign in (14); the quantified proof above is needed because the two actual frequencies coalesce and the complete correction is nonzero. No new general fact about sine products is claimed.

## 4. What this disproves, and what it leaves open

The tested nonnegative signed-correlation bound on (6) is false, even after imposing both local event equations exactly and retaining the correction. Therefore a sound quadratic or sum-of-squares certificate, with arbitrary multipliers of just these event equations and disk inequalities, cannot prove that bound: its claimed inequality would apply to (12). This does not rely on a limitation of a particular optimization solver.

**The witness violates the exact equalities x_n²+y_n²=d_n² and the common arithmetic phase law.** It attenuates the two retained coefficients and sets every n≥3 quadrature to zero. The d_n are retained as disk radii only. It is not the complete theta finite sum, a theta source perturbation, an all-real canonical heat slice, a global even function in z, a reflected event pair, or a physical solution of the Newman equation. The small J correction does not establish global all-realness for q_* either. No canonical value of D_a(S) has been shown negative or positive here.

Thus the negative result concerns precisely the phase-disk/event-equation relaxation, not exact-circle constraints, logarithmic phase relations, all-real event-conditioned estimates, every quadratic method or all signed-correlation research. An argument retaining additional global zero information or tighter phase constraints is outside the tested class. Passing to the convex hull of each phase circle while retaining a quadratic objective enlarges the feasible values in a way that can lose the desired sign; no assertion is made about the convex hull of the lifted correlation matrix of *actual event phases*.

The first failed premise is now explicit: a nonnegative quadratic lower bound does not follow from the two event equations and the independent amplitude disks. The missing canonical input remains a bound using the actual simultaneous arithmetic phases (or other information not retained by (6)), rather than another formulation of D_a>0. No tractable method for that sharper bound has been found in this pass.

## 5. Analytical collision controls and ownership

The [control catalog](../../../../result-summaries/12_collision_controls_and_screening.md) is screened analytically; no numerical certificates were rerun. Note06 §6's genuine positive-source threshold control still supplies H(T,a)=H_z(T,a)=0 and the negative physical Poisson expression at every positive observation height, including β/L. It fails canonical theta arithmetic, full profile and eventual simplicity at threshold. The polynomial event control gives equality for the pair-only consumer. Neither is assigned the canonical correction or this disk witness.

| Control class | Failed premise / limit relevant to r5 |
| --- | --- |
| New disk point (12) | Exact coefficient magnitudes, common logarithmic phases, global theta source/clock/zero configuration and reflected physical event fail. It disproves only the stated relaxed estimate. |
| Euler-factor / translated | Unchanged canonical coefficients fail; a nonreal witness time is not automatically an all-real event. |
| Weighted-square / finite-tail / finite-prime orbit | Full reflection and/or the complete canonical sequence fail; local events do not supply all-realness and finite-tail controls have no all-real time. |
| Reflected super-Gaussian / smooth shape / positive primitive | Canonical square-series arithmetic fails; local collision data alone do not establish an all-real threshold. |
| Atomic / finite-profile / compact-source thresholds | Event equations and geometric sign persist; exact theta coefficients, full growth and eventual threshold simplicity fail. |
| RH-conditional endpoint | Conditional time-zero construction; ordinary Dirichlet arithmetic fails. No unconditional positive-time canonical conclusion. |
| Variable-readout / heat counter-kernels | Literal cosine readout, source and/or physical heat generator fail. |
| Relaxed profile populations | Exact integer canonical zero population and simultaneous complete-field identification fail; feasibility is not a physical event. |

[Note06 §4](06_RSCT_B01_R4_MICROSCOPIC_EVENT_EXPANSION_20261111.md) retains the collision manuscript/S04 ownership of population and microscopic-scaling facts. The complete acquisition and Poisson criterion are inherited; (8) is their algebraic expansion, not a new RH criterion. The new scoped calculation is the correction-retaining feasible point (12) and its quantitative negative margin (16)–(17).

[HCB Note14](../../03_heat_flow_collision_bounds/notes/14_SIGNED_LAG_RESONATOR_AND_ACTUAL_REMAINDER_20261028.md) proves an actual signed remainder projection at some centers at tL=2 for a different leading-pair triangle method. Its actual-arithmetic conclusion is **not** being claimed here: (12) is a relaxed coefficient point at c∈[1/2,1]. HCB keeps first-jet/Poisson ownership, HDA/GNP-RS keeps the provider, and [OA](../../08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/03_collision_constraints/notes/11_TND_OA_AFTER_E02_CONTINUATION_AND_MODEL_CHANGE_20261109.md) remains parked.

**Return:** complete r5 with the signed quadratic form, a falsified explicit relaxed estimate, and the first failed premise identified. No new zero-exclusion region, independent provider audit, instantiated onset, numerical campaign, agents, manuscript or E01 method. A future authorized conceptual pass must retain a named additional canonical constraint or use a materially different mechanism; “make the quadratic form positive” is not a frozen proof plan. [Continuation01](01_RSCT_CONTINUATION_AND_PROMPT_20261111.md) carries the model-change handoff.
