# RSCT-B01 r6: exact coefficient circles still admit the negative correlation

11 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance, RSCT chat0003, “Continue R6 investigation.” Actual backend model and reasoning effort are unavailable in the recorded configuration; recommendations are separate from provenance.

**Status: proved in-note from named inherited approximation inputs; same-assistant checking only.** The tested extra constraint is the exact magnitude of every coefficient. A full set of free phases, with no attenuated or omitted mode, satisfies both local event equations exactly and retains the actual correction, yet has signed Poisson value at most \(-\kappa_\beta/L^2\), with an explicit \(\kappa_\beta>0\). **This is a negative value in the independent-circle class, not a canonical arithmetic value or a canonical event.** The construction explicitly violates \(u_4u_1=u_2^2\), a necessary relation for the common logarithmic phases. No zero-exclusion region or executable E01 method results.

Read the [result index](../../../../result-summaries/README.md), [cluster11](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md), [controls12](../../../../result-summaries/12_collision_controls_and_screening.md) and [avoid index](../../../../avoid/README.md), especially [classification01](../../../../avoid/01_restating_the_target.md), [premises02](../../../../avoid/02_shape_only_arguments_and_the_controls.md), [scope07](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [separate bounds12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md). [Decision06](../brainstorm/notes/06_RSCT_B01_R6_EXACT_CIRCLE_DECISION_20261111.md) records the bounded return.

## 1. Retained data and the stronger estimating class

Use [Note06](06_RSCT_B01_R4_MICROSCOPIC_EVENT_EXPANSION_20261111.md), [Review04](../reviews/04_RSCT_B01_R4_SAME_ASSISTANT_CHECK_20261111.md) and [Note07](07_RSCT_B01_R5_SIGNED_CORRELATION_DISK_TEST_20261111.md) at their recorded evidence level:
\[
 L=\log(a/(4\pi)),\quad T=c/L,\quad c\in[1/2,1],\quad
 N=\lfloor e^{L/2}\rfloor,\quad z=a+w/L,
\]
\[
 d_n=n^{-1/2}\exp\!\left\{\frac{c}{4L}[(\log n)^2-L\log n]\right\},
 \quad \lambda_n=\frac14-\frac{\log n}{2L}\in[0,1/4],
 \quad \phi_n=\Theta(T,a)-(a/2+\pi T/8)\log n.                 \tag{1}
\]
The physical normalized field \(f(w)=H_T(a+w/L)/A(T,a+w/L)\) has complete approximant
\[
 q_{\rm can}(w)=\sum_{n\le N}d_n\cos(\phi_n+\lambda_nw)+K(w),
 \quad \|\partial_w^j(f-q_{\rm can})\|_R\le C_Ra^{-3/4},
 \quad j=0,1,2.                                             \tag{2}
\]
Here and below \(R\) is fixed independently of \(a,c\). The same exact normalized gamma/RS correction is retained, real on the real scaled axis, with
\[
 \|\partial_w^jK\|_R\le C_R\chi,\quad
 \chi=a^{-1/4}e^{-cL/16},\quad j=0,1,2.                       \tag{3}
\]
Both reflected arms, the heat phase, quadratic heat weights, fixed local cutoff, source buffers and full exterior payment remain as in Note06. No new approximation theorem or independent audit of the inherited provider is claimed. The exact underlying reflected formula is [Polymath v2 §4 (35)–(39)](https://arxiv.org/html/1904.12438v2#S4); its value theorem is not silently differentiated.

For arbitrary real phases \(\theta_n\), put
\[
 x_n=d_n\cos\theta_n,\quad y_n=d_n\sin\theta_n,\quad
 q_\theta(w)=\sum_{n\le N}[x_n\cos(\lambda_nw)-y_n\sin(\lambda_nw)]+K(w),
 \quad S_\theta=q_\theta-q_\theta(0)-wq_\theta'(0).
\]
Test the nonnegative lower bound on
\[
 {\cal C}_\epsilon=\left\{(x,y):
 x_n^2+y_n^2=d_n^2\ \hbox{for every }n\le N,\quad
 |\sum x_n+K(0)|\le\epsilon,\quad
 |-\sum\lambda_n y_n+K'(0)|\le\epsilon\right\},\quad
 \epsilon=C_Ra^{-3/4}.                                     \tag{4}
\]
Canonical events of **any** multiplicity \(m\ge2\) satisfy these necessary conditions. Higher event jets and global all-realness are not imposed on this estimating class. Unlike r5's disks, (4) preserves every exact magnitude; it still allows independent phases instead of the actual \(\phi_n\).

For fixed \(\beta>0\), write \(S_\theta(i\beta)=X-iY\), with primes on \(X,Y\) differentiating \(\beta\). The full consumer from Note07 is
\[
 D_a(S_\theta)=\mathfrak d_a(X^2+Y^2)-\beta(XX'+YY'),\qquad
 \mathfrak d_a=2k_a+\frac{\beta}{L}\Im(A_z/A)(T,a+i\beta/L)
             =2+O_\beta(a^{-2}L^{-2}),
\]
\[
 k_a=1+\frac{(\beta/L)^2}{4a^2+(\beta/L)^2}.                 \tag{5}
\]
No cross term or correction is dropped. The physical all-real event still gives
\[
 D_a(f)=\left[(2-m)k_a-\frac{\beta^2}{L^2}
 \sum_{r\ne\pm a}\frac1{(a-r)^2+\beta^2/L^2}\right]|f(i\beta)|^2<0.
                                                                    \tag{6}
\]
Every copy of both event roots is removed; all other multiplicities remain. The inherited event-conditioned acquisition allowance is
\[
 \eta_a=O_\beta\!\left(a^{-3/4}e^{(1/4-c/16)L}/L^2+a^{-3/2}\right)
       =o(L^{-2}).                                         \tag{7}
\]
These physical assertions apply to \(f,q_{\rm can}\), not to an arbitrary point of (4).

**Classification and method.** The candidate is a lower bound on an explicitly specified, nonconvex product of circles with two equations, using the additional exact-magnitude information that r5 discarded. It is a falsifiable estimating method, not another all-domain RH-equivalent criterion. The underlying endpoint reformulation remains stated once in Note03. We test the stronger class analytically by consecutive triples before attempting an inequality certificate.

## 2. Three exact circles can satisfy the two event equations

For \(1\le x\le e^{L/2}\),
\[
 -\frac34\le\frac{d\log d(x)}{d\log x}
 =-\frac12-\frac c4+\frac{c\log x}{2L}\le-\frac12.
\]
Thus the \(d_n\) strictly decrease, \(d_n\le n^{-1/2}\), and for every complete consecutive triple \(j,j+1,j+2\),
\[
 d_{j+1}+d_{j+2}\ge
 d_j\left[(1+1/j)^{-3/4}+(1+2/j)^{-3/4}\right]
 \ge d_j(2^{-3/4}+3^{-3/4})>d_j.                           \tag{8}
\]
The last strict inequality is exact: \(2^{-3/4}>7/12\) and \(3^{-3/4}>5/12\), as follows by fourth powers. No floating check is needed.

For this paragraph abbreviate the triple's data by \(b_i=d_{j+i-1}\), \(r_i=\lambda_{j+i-1}\), \(i=1,2,3\). We have \(r_1>r_2>r_3\ge0\), with \(r_2>0\). Set \(\rho=r_3/r_2\). There is a unique \(v\in(0,b_3)\) such that
\[
 A_2(v)+A_3(v)=b_1,\quad
 A_2(v)=\sqrt{b_2^2-\rho^2v^2},\quad
 A_3(v)=\sqrt{b_3^2-v^2}.                                 \tag{9}
\]
Indeed the left side is continuous and strictly decreasing; it exceeds \(b_1\) at zero by (8), and at \(v=b_3\) is at most \(b_2<b_1\). Both \(A_i\) are strictly positive at its solution. Choose
\[
 (x_j,y_j)=(b_1,0),\quad
 (x_{j+1},y_{j+1})=(-A_2,\rho v),\quad
 (x_{j+2},y_{j+2})=(-A_3,-v).                              \tag{10}
\]
Every circle equality holds exactly, and
\[
 \sum_{\rm triple}x_n=0,\qquad
 \sum_{\rm triple}\lambda_n y_n=0.                        \tag{11}
\]
This construction includes \(r_3=0\): then \(\rho=0\), and the last mode has zero frequency but retains its full coefficient magnitude. No division by \(r_3\) is required in (9)–(11).

Let \(p_j(w)\) denote the triple's cosine/sine sum. At \(i\beta\) its real and negative-imaginary parts are
\[
 X_j=A_2[\cosh(\beta r_1)-\cosh(\beta r_2)]
       +A_3[\cosh(\beta r_1)-\cosh(\beta r_3)]>0,
\]
\[
 Y_j=v r_3\left[\frac{\sinh(\beta r_2)}{r_2}
                      -\frac{\sinh(\beta r_3)}{r_3}\right]\ge0.       \tag{12}
\]
The quotient at zero means its continuous value \(\beta\); when \(r_3=0\), \(Y_j=0\).

For \(r>s\ge0\), the power series of \(\cosh(\beta r)-\cosh(\beta s)\) has positive coefficients in degrees \(2,4,6,\ldots\). Consequently
\[
 \beta X_j'-2X_j>0,\qquad \beta Y_j'-2Y_j\ge0.              \tag{13}
\]
For the second assertion the difference of the two \(\sinh(\beta r)/r\) series starts in degree three and has positive subsequent coefficients; equality is allowed when \(r_3=0\). The signs in (13) are exact for every fixed \(\beta>0\), not a small-\(\beta\) approximation.

## 3. Assemble every complete triple without losing the sign

Let \(J=\lfloor N/3\rfloor\), and apply (10) to \(j=1,4,\ldots,3J-2\). Define
\[
 p(w)=\sum_j p_j(w),\qquad p(0)=p'(0)=0.
\]
Write \(p(i\beta)=X-iY\). All summands of \(X,Y,\beta X'-2X,\beta Y'-2Y\) are nonnegative. Therefore, for \(D_2(g)=2|g(i\beta)|^2+\beta\Im(g'(i\beta)\overline{g(i\beta)})\),
\[
 D_2(p)=-X(\beta X'-2X)-Y(\beta Y'-2Y)<0.                 \tag{14}
\]
This pays the cross terms in the combined field: they have the same adverse sign. It does not infer a sign for the canonical field by adding signs of unrelated canonical sectors.

The full artificial field and its derivatives are small despite the growing number of modes:
\[
 \|\partial_w^k p\|_R=O_R(L^{-1}),\qquad k=0,1,2.           \tag{15}
\]
To prove this without discarding the population, write each block as
\[
 p_j(w)=A_2[\cos(r_1w)-\cos(r_2w)]
       +A_3[\cos(r_1w)-\cos(r_3w)]
       +v r_3\left[\frac{\sin(r_3w)}{r_3}
                         -\frac{\sin(r_2w)}{r_2}\right].
\]
The last quotient is \(w\) at zero. On \(0\le r\le1/4\), \(|w|\le R\), the displayed functions and their first two \(w\)-derivatives have bounded derivatives in \(r\). Each block is consequently bounded by
\[
 C_Rd_j(\lambda_j-\lambda_{j+2})
 \le \frac{C_Rd_j}{jL}\le\frac{C_R}{Lj^{3/2}}.
\]
Summing this convergent majorant proves (15), uniformly in \(c\). No fixed-mode approximation replaces the full sum.

The first block alone supplies a quantitative margin. Its \(A_2\), now denoted \(A_{2,h}\), obeys
\[
 A_{2,h}=1-A_{3,h}\ge1-d_3\ge\alpha,\qquad
 \alpha=1-1/\sqrt3>0.
\]
Put \(r=1/4,\ h=(\log2)/(2L)\), and
\[
 U=\cosh(\beta r)-\cosh(\beta(r-h)),\qquad
 G=\beta U'-2U>0.
\]
By (12)–(14), \(D_2(p)\le-A_{2,h}^2UG\le-\alpha^2UG\). At fixed \(\beta>0\),
\[
 UG=\frac{C_\beta}{L^2}+O_\beta(L^{-3}),\quad
 C_\beta=\frac{(\beta\log2)^2}{4}\sinh^2(\beta/4)
                 [(\beta/4)\coth(\beta/4)-1]>0.             \tag{16}
\]
This is the same elementary positive coefficient as Note07 (15), not a new scaling claim. For completeness, if \(x=\beta/4\), then
\[
 U=h\beta\sinh x+O_\beta(h^2),\quad
 G=h\beta(x\cosh x-\sinh x)+O_\beta(h^2).
\]
The second leading factor is positive since its derivative in \(x\) is \(x\sinh x>0\) and it vanishes at zero.

## 4. Retain the last modes and the actual correction exactly

There are at most two ungrouped indices \(3J+1,\ldots,N\). Assign phase zero to each, retaining its full magnitude, and let their sum be \(b(w)\). These are the final one or two indices, not a discarded tail. Since
\[
 d_{N-\ell}=\exp[-(1/4+c/16)L+O(e^{-L/2})]=O(\chi),
 \qquad \ell=0,1,
\]
we have \(\|\partial_w^k b\|_R=O_R(\chi)\), \(k\le2\), and \(b'(0)=0\). This covers every residue class of \(N\) modulo three and fractional-cutoff positions.

Only the phases of modes 2 and 3 will now be adjusted. Leave phase 1 equal to zero and every later phase as already assigned. For the first triple define
\[
 F(\theta_2,\theta_3)=
 \big(1+d_2\cos\theta_2+d_3\cos\theta_3,\
       \lambda_2d_2\sin\theta_2+\lambda_3d_3\sin\theta_3\big).
\]
At the phases in (10), \(F=(0,0)\), and its Jacobian determinant is
\[
 \det DF=-\lambda_3 y_2x_3+\lambda_2 y_3x_2
        =v\left(\frac{\lambda_3^2}{\lambda_2}A_{3,h}
                         +\lambda_2A_{2,h}\right)>0.       \tag{17}
\]
The inverse is bounded uniformly for large \(L\) and \(c\in[1/2,1]\). Indeed the head data tend uniformly to
\[
 (\lambda_2,\lambda_3)\to(1/4,1/4),\quad
 (d_2,d_3)\to(2^{-s},3^{-s}),\quad s=1/2+c/4\in[5/8,3/4].
\]
The limiting triangles are strictly nondegenerate throughout this compact interval by (8) and \(|2^{-s}-3^{-s}|<1\). Hence their \(v\)'s are uniformly positive, and (17) tends to \(v/4\). The smooth finite-dimensional map and bounded second derivatives therefore have uniform inverse neighborhoods.

Using (3), the inverse-function theorem now permits phase changes of size \(O(\chi)\) solving exactly
\[
 F(\theta_2^*,\theta_3^*)=(-K(0)-b(0),\,K'(0)).            \tag{18}
\]
This is a small adjustment **along** the two circles, not a change of their radii. Let \(\Delta p_h\) be the change of the first triple. With all \(n\le N\) retained, set
\[
 q_*=p+b+\Delta p_h+K=p+E,\quad
 \|\partial_w^kE\|_R=O_R(\chi),\quad k\le2.
\]
Equations (18) give \(q_*(0)=q_*'(0)=0\) exactly, so \(S_*=q_*\) and its coefficient point belongs to \({\cal C}_0\subset{\cal C}_\epsilon\). The whole holomorphic \(K\), including its actual values at the center, is present.

Combining (5), (15) and (16), including every cross term with \(E\), gives
\[
 D_a(S_*)\le-\frac{\alpha^2C_\beta}{L^2}
 +O_\beta\!\left(L^{-3}+\chi/L+\chi^2+a^{-2}L^{-4}\right).
                                                                    \tag{19}
\]
Here the carrier correction costs \(O(a^{-2}L^{-4})\) because \(p=O(L^{-1})\). The other perturbation costs are \(O(\chi/L+\chi^2)\), not an unquantified continuity claim. Since \(\chi L\to0\) uniformly in \(c\), for a finite uninstantiated onset,
\[
 \boxed{\inf_{{\cal C}_\epsilon}D_a(S)
       \le D_a(S_*)\le-\frac{\kappa_\beta}{L^2}<0,\qquad
       \kappa_\beta=\tfrac12(1-1/\sqrt3)^2C_\beta>0.}        \tag{20}
\]
Also \(D_a(S_*)=O_\beta(L^{-2})\) by (15). Thus this witness has negative magnitude of order \(L^{-2}\), uniformly in the declared \(c\)-band. Equation (20) is a feasible-point bound, not the optimum of (4). It exceeds the magnitude of the physical acquisition allowance (7) eventually; (7) is not assigned as an approximation theorem for this noncanonical witness.

## 5. The exact arithmetic relation the witness fails

For actual unit phases \(u_n=e^{i\phi_n}\), the common logarithmic law implies
\[
 u_{mn}u_1=u_mu_n\quad(mn\le N),\qquad
 u_4u_1=u_2^2.                                           \tag{21}
\]
For the constructed point and sufficiently large \(N\), \(u_1=u_4=1\): these are first modes of the first and second triples. The adjusted phase \(\theta_2^*\) remains strictly between \(\pi/2\) and \(\pi\), uniformly away from the endpoints, by the compact nondegenerate head construction and its \(O(\chi)\) change. In particular
\[
 |u_4u_1-u_2^2|=2|\sin\theta_2^*|\ge\delta>0              \tag{22}
\]
at a uniform finite onset. Thus the common-phase premise fails explicitly, including a necessary elementary multiplicative identity, even though every exact amplitude is preserved. These \(u_n\) describe the constructed phases only in (22).

The result rules out a nonnegative lower bound using only the constraints of (4), including arbitrary sound multiplier or sum-of-squares certificates over that set. It does **not** rule out estimates using (21), the actual linked values of \(\Theta,\nu=a/2+\pi T/8\), additional event jets, global all-realness, a tighter set of actual lifted correlations, or another consumer. Multiplicative unit phases alone are still weaker than the actual height-dependent logarithmic law; this pass tests neither of those smaller classes.

No theta source perturbation, globally even field in physical \(z\), all-real canonical slice, reflected event pair or Newman trajectory is constructed. Keeping the actual \(K\) in an algebraic test does not identify that test with the canonical source. The physical source, clock, arbitrary multiplicity and reflected event remain intact in the inherited formulas (1)–(7); the altered phases are confined to the explicitly declared estimating-class test.

## 6. Control screen, ownership and bounded return

The [catalog](../../../../result-summaries/12_collision_controls_and_screening.md) is screened analytically on its actual witness domains; no numerical certificates are rerun.

| Control class | Premise failed or limitation relevant here |
| --- | --- |
| R6 circle construction | Every \(d_n\), local frequency and both equations survive; (21) fails by (22). Canonical source/trajectory, global all-realness and physical reflection are not supplied. |
| R5 disk witness | Exact circles fail. R6 supplies a new proof for that added constraint; r5 alone never excluded it. |
| Euler-factor / translated | Unchanged complete theta coefficients fail; a time with nonreal zeros is not itself an all-real threshold event. |
| Weighted-square / finite-tail / finite-prime orbit | Full reflection and/or the complete canonical sequence fail. Their local events do not supply all-realness; finite-tail controls have no all-real time. |
| Reflected super-Gaussian / smooth shape / positive primitive | Canonical square-series arithmetic fails; their recorded local collisions alone do not give the all-real hypothesis in (6). |
| Atomic / exact finite-profile / compact-source thresholds | Genuine all-real events and the negative geometric sign can survive. Exact theta coefficients, full profile growth and eventual threshold simplicity fail. |
| RH-conditional endpoint | Construction is conditional and at time zero; ordinary Dirichlet arithmetic fails. It is not an unconditional positive-time canonical event. |
| Variable readout / heat counter-kernels | Literal cosine readout, full source and/or physical heat generator fail. |
| Relaxed profile / zero populations | Exact canonical integer zero multiset and simultaneous complete-field identification fail. |

The [BW-01 positive three-atom threshold family](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/01_local_double_winding/notes/04_EVENT_CONDITIONED_POSITIVE_SOURCE_OBSTRUCTION_20261020.md), used at \(q=1/2\) and frequency \(2\pi/3\) in Note06 §6, still has genuine all-real events \(a_j=1+3j\) at a chosen \(T=c/\log(a_j/(4\pi))\), and the negative geometric sign at \(\beta/L_j\). It is a different control from (10); its positive atoms do not acquire our \(d_n\), correction or arithmetic phases.

HDA/GNP-RS owns (2)–(3), HCB retains [first-jet/Poisson acquisition](../../03_heat_flow_collision_bounds/research-progress/02_POST_CALIBRATION_RESEARCH_PROGRESS_20261028.md), and the collision manuscript/S04 retain the population and microscopic-scaling facts cited in Note06. HCB's actual signed-remainder result at \(tL=2\) is not this free-phase witness. [OA's restart gate](../../08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/03_collision_constraints/notes/11_TND_OA_AFTER_E02_CONTINUATION_AND_MODEL_CHANGE_20261109.md) remains parked. No ownership is transferred.

**Return:** r6 is complete with a scoped failure for the independent exact-circle/event-equation class. The new quantitative content is the all-mode construction (9)–(20), including cutoff leftovers, the exact correction and explicit arithmetic defect (22). The first failed premise is that restoring individual magnitudes suffices to force the desired signed lower bound. No canonical margin, new covered zero region, finite onset, numerical campaign, agents, manuscript or E01 method is obtained. The full objective still includes every \(0<T\le1/2,\ a>0,\ m\ge2\); nothing places an unknown threshold in our intermediate band.

A future author-requested B pass must test a method that actually uses a further relation absent here, or a materially different mechanism. The relation \(u_{mn}u_1=u_mu_n\) is an identified discriminator, **not** a proved favorable estimate or a frozen proof method. Stop independent-circle certificates for this lower bound, alongside the earlier disk test, fixed-height matrix constant optimization and fixed-order absolute envelopes. [Review06](../reviews/06_RSCT_B01_R6_SAME_ASSISTANT_CHECK_20261111.md) and [Continuation01](01_RSCT_CONTINUATION_AND_PROMPT_20261111.md) preserve the evidence and model-change boundary.
