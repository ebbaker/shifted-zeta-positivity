# RSCT-B01 r7: the signed consumer on multiplicative prime phases

11 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance, RSCT chat0003. Actual backend model and reasoning effort are unavailable in the recorded configuration.

**Status: proved in-note from named classical and inherited approximation inputs; same-assistant checking only.** All unit-phase multiplicative identities, every exact coefficient magnitude, the actual leading carrier phase, both local event equations and the actual correction still admit a negative value of the signed Poisson consumer. Any **fixed finite** set of actual prime phases can also be preserved. The constructed phases explicitly disagree with the actual height at another fixed prime. **This is a counterexample to the multiplicative-phase estimating class, not a canonical arithmetic value or physical collision.**

**Prior-work boundary.** The [collision manuscript](../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex), theorem sc:character and discussion sc:remaining, already constructs complete multiplicative twists with a vanishing model first jet using isolated primes, finite character orthogonality, the prime number theorem and phase adjustment. [Arithmetic-collision Review19](../../../investigations-3/11_arithmetic_collision_rigidity/reviews/19_FIXED_FUNCTION_PROGRAM_AND_AMBITIOUS_NEXT_STEPS_REVIEW_ASTRA_20261019.md) records the same limitation. R7 extends that method to **this signed consumer with a negative margin**, retained correction and fixed finite prime calibration. It does not discover the general failure of multiplicativity alone.

Read the [result index](../../../../result-summaries/README.md), [cluster11](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md), [controls12](../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../avoid/README.md), especially [01](../../../../avoid/01_restating_the_target.md), [02](../../../../avoid/02_shape_only_arguments_and_the_controls.md), [07](../../../../avoid/07_scoped_exclusions_read_as_universal.md), [12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [16](../../../../avoid/16_unchecked_imports_and_novelty_claims.md). [Decision07](../brainstorm/notes/07_RSCT_B01_R7_MULTIPLICATIVE_PHASE_DECISION_20261111.md) is the bounded return.

## 1. Fixed consumer and the information being tested

Keep [Notes06–08](08_RSCT_B01_R6_EXACT_CIRCLE_TEST_20261111.md), with their named provider and same-assistant review limitations:
\[
 L=\log(a/(4\pi)),\quad T=c/L,\quad c\in[1/2,1],\quad
 X_0=e^{L/2},\quad N=\lfloor X_0\rfloor,\quad z=a+w/L,
\]
\[
 d_n=n^{-1/2}\exp\!\left\{\frac{c}{4L}[(\log n)^2-L\log n]\right\},
 \quad\lambda_n=\frac14-\frac{\log n}{2L},\quad
 \nu=a/2+\pi T/8,\quad u_1=e^{i\Theta(T,a)}.                 \tag{1}
\]
Fix \(\beta>0\); every local disk used for the inherited correction has radius greater than \(\max(1,\beta)\). The complete normalized approximation to \(f(w)=H_T(a+w/L)/A(T,a+w/L)\) uses the actual unit phases
\[
 u_n^{\rm can}=u_1 n^{-i\nu},\qquad
 q_{\rm can}(w)=\frac12\sum_{n\le N}d_n
 [u_n^{\rm can}e^{i\lambda_nw}+\overline{u_n^{\rm can}}e^{-i\lambda_nw}]
 +K(w).
\]
Its value and first two scaled derivatives have error \(O_R(a^{-3/4})\); \(K\) is the same exact normalized gamma/RS correction, real on the real axis, with
\[
 \|\partial_w^jK\|_R=O_R(\chi),\quad
 \chi=a^{-1/4}e^{-cL/16},\quad j\le2.                        \tag{2}
\]
Both arms, the heat phase, quadratic weights, fixed local cutoff and full inherited source/error payments remain in force. No approximation theorem for a twisted physical field is asserted.

For any completely multiplicative \(\omega:\mathbb N\to\mathbb C\), \(|\omega(n)|=1\), \(\omega(1)=1\), set \(u_n=u_1\omega(n)\). Then
\[
 u_{mn}u_1=u_mu_n
\]
for every pair, including all \(mn\le N\). Define \(q_\omega\) by the same full sum and same \(K\), replacing only the unit phases; put \(g^\circ(w)=g(w)-g(0)-wg'(0)\) and \(S_\omega=q_\omega^\circ\). All \(\omega(n),T,N\) are held fixed in spatial derivatives. The candidate method asks for a nonnegative lower bound on this **multiplicative-phase torus**, restricted by
\[
 |q_\omega(0)|,\ |q_\omega'(0)|\le\epsilon,\qquad
 \epsilon=C_Ra^{-3/4}.                                    \tag{3}
\]
This is a smaller estimating class than r6's independent circles. The actual phases belong to it at a physical event, but arbitrary prime phases need not lie at the actual height.

Retain the exact physical carrier and signed expression:
\[
 D_a(g)=\mathfrak d_a|g(i\beta)|^2+
       \beta\Im[g'(i\beta)\overline{g(i\beta)}],\quad
 \mathfrak d_a=2k_a+\frac{\beta}{L}\Im(A_z/A)(T,a+i\beta/L)
             =2+O_\beta(a^{-2}L^{-2}),
\]
\[
 k_a=1+\frac{(\beta/L)^2}{4a^2+(\beta/L)^2}.                 \tag{4}
\]
At an actual all-real event of any \(m\ge2\),
\[
 D_a(f)=\left[(2-m)k_a-\frac{\beta^2}{L^2}
   \sum_{r\ne\pm a}\frac1{(a-r)^2+\beta^2/L^2}\right]|f(i\beta)|^2<0.
                                                                    \tag{5}
\]
All copies of both event roots are removed. [Note06](06_RSCT_B01_R4_MICROSCOPIC_EVENT_EXPANSION_20261111.md) pays the absolute physical acquisition error
\[
 \eta_a=O_\beta(a^{-3/4}e^{(1/4-c/16)L}/L^2+a^{-3/2})=o(1). \tag{6}
\]
The class (3) does not impose global all-realness or the other \(m-2\) event equations. Neither (5) nor a physical approximation assertion is assigned to our artificial phases.

**Classification.** This tests a specific stronger information class for the existing lower-bound method. It is not a new endpoint criterion. Its falsifiable claim is nonnegativity of the full signed form on (3), rather than the mere rewriting of that form.

## 2. The precise negative statement

Let \({\cal P}_0\) be any fixed finite set of primes, possibly empty, and choose a fixed prime \(q_0\notin{\cal P}_0\). At every sufficiently large \(a\), uniformly in \(c\in[1/2,1]\), there is a completely multiplicative \(\omega\) such that
\[
 \omega(p)=p^{-i\nu}\quad(p\in{\cal P}_0),\qquad
 \omega(q_0)=-q_0^{-i\nu},\qquad
 q_\omega(0)=q_\omega'(0)=0,                               \tag{7}
\]
and
\[
 \boxed{D_a(S_\omega)\le
 -\kappa_\beta\,\frac{\exp[(1/2-c/8)L]}{L^8}<0.}            \tag{8}
\]
Here \(\kappa_\beta>0\) will be given explicitly in (20). The onset depends on \(\beta,{\cal P}_0,q_0\) and inherited constants; it is not numerically instantiated. In particular, there is **no uniform growing-prime-set conclusion**. Formula (7) gives the explicit canonical-phase defect
\[
 |u_{q_0}-u_{q_0}^{\rm can}|=2.                            \tag{9}
\]
Every coefficient magnitude and all multiplicative identities survive.

## 3. Isolated prime population and a bounded complete complement

Use three fixed proportional intervals
\[
 I_1=[11/20,3/5],\quad I_2=[7/10,3/4],\quad
 I_3=[17/20,9/10].
\]
The classical prime number theorem \(\pi(x)\sim x/\log x\), checked in [NIST DLMF 27.2.3](https://dlmf.nist.gov/27.2#E3), gives
\[
 \#\{p:p/N\in I_j\}=(1/20+o(1))N/\log N.
\]
Only fixed relative intervals are used, not a short-interval or effective-onset result. Select
\[
 M=\left\lfloor\frac{N}{40\log N}\right\rfloor
\]
primes in each interval and pair them into \(M\) triples \(p_{j,1}<p_{j,2}<p_{j,3}\), one from each interval. Let \({\cal R}\) be their union. Every selected prime exceeds \(N/2\), so it divides **only its own term** among \(n\le N\). Its phase can be changed without changing any complementary term, while complete multiplicativity is preserved.

Put
\[
 b_L=e^{-(1/4+c/16)L},\quad \delta=1/4-c/16,\quad W=M b_L.
\]
For \(p\in{\cal R}\), writing \(v=L/2-\log p\) gives the exact formula
\[
 d_p=b_L e^{v/2+cv^2/(4L)},\quad \lambda_p=v/(2L).
\]
Thus \(d_p\asymp b_L\), \(L\lambda_p\) stays in positive compact intervals separated between the three groups, and
\[
 \frac{e^{\delta L}}{80L}\le W\le\frac{e^{\delta L}}{10L}   \tag{10}
\]
eventually. For the lower bound, \(M\ge N/(80\log N)\), \(N\ge X_0/2\), and \(\log N\le L/2\); the upper bound follows from \(\log N\ge L/4\). All constants are uniform in \(c\).

Write \({\cal Q}={\cal P}_0\cup\{q_0\}\), and take \(N>2\max{\cal Q}\). Fix the phases at \({\cal Q}\) as in (7), and choose independent uniform circle phases for every other unselected prime at most \(N\). Let \(B(w)\) be the **complete** complementary cosine/sine sum over \(n\notin{\cal R}\), including \(n=1\); it omits only the separate reserved prime population, and not a composite or numerical tail.

The weight estimates
\[
 d_n^2\le n^{-1-c/4}\le n^{-9/8},\quad
 \sum_{n\le N}d_n^2\le9,\quad
 d_{rm}\le r^{-1/2}d_m\quad(rm\le N)                       \tag{11}
\]
follow from \(\log n\le L/2\) and the log slope
\(-3/4\le d\log d(x)/d\log x\le-1/2\).
Every integer has a unique decomposition \(n=rm\), with \(r\) supported on \({\cal Q}\) and \(m\) divisible by none of those primes. Define
\[
 C_{\cal Q}=\prod_{p\in{\cal Q}}(1-p^{-1/2})^{-1}<\infty.
\]
Distinct complementary \(m\)'s have distinct characters of the unfixed prime variables. Finite integration of \(e^{ik\theta}\) kills every nonzero exponent. Consequently, for either reflected arm, at \(w=0,i\beta\) and for derivative order \(j=0,1\),
\[
 \mathbb E\left|\sum_{n\notin{\cal R}}d_n\omega(n)
            (i\lambda_n)^j e^{i\lambda_nw}\right|^2
 \le9e^{\beta/2}C_{\cal Q}^2.                             \tag{12}
\]
Indeed each character coefficient is bounded by
\(e^{\beta/4}d_m\sum_{r:\,{\cal Q}\text{-supported}}r^{-1/2}
=e^{\beta/4}C_{\cal Q}d_m\); then use (11).
No reserved prime enters a complementary character because its only retained multiple was removed. The opposite arm has the same bound, and
\(|(A_++A_-)/2|^2\le(|A_+|^2+|A_-|^2)/2\) pays their cross term.

It follows that some choice of the unselected phases satisfies
\[
 |B(0)|^2+|B'(0)|^2+|B(i\beta)|^2+|B'(i\beta)|^2
 \le36e^{\beta/2}C_{\cal Q}^2.                             \tag{13}
\]
Fix such a choice. This is finite auxiliary phase integration, not sampling, a numerical experiment or a height average. It proves existence of an algebraic complement, not a bound for the actual canonical complement. The finite-calibration cost \(C_{\cal Q}\) is displayed rather than hidden in a claim about growing calibrations.

## 4. Prime triples with a negative signed margin

For each selected triple abbreviate \(b_i=d_{p_{j,i}}\), \(r_i=\lambda_{p_{j,i}}\). We have \(b_1>b_2>b_3>0\), \(r_1>r_2>r_3>0\), and \(b_1<b_2+b_3\) uniformly after division by \(b_L\). For example,
\[
 b_1/b_3\le(p_{j,3}/p_{j,1})^{3/4}
 \le(18/11)^{3/4}<2,\qquad b_2>b_3.
\]
Apply the elementary three-circle construction of [Note08 (9)–(13)](08_RSCT_B01_R6_EXACT_CIRCLE_TEST_20261111.md). With \(\rho=r_3/r_2\), choose the unique \(v\in(0,b_3)\) solving
\[
 A_2+A_3=b_1,\quad
 A_2=\sqrt{b_2^2-\rho^2v^2},\quad A_3=\sqrt{b_3^2-v^2},
\]
and set the triple's total quadratures to
\[
 (b_1,0),\quad(-A_2,\rho v),\quad(-A_3,-v).                \tag{14}
\]
Every circle is exact; its sum \(p_j\) has \(p_j(0)=p_j'(0)=0\). All normalized parameters are in a compact nondegenerate family, so \(A_2,A_3,v,\rho v\asymp b_L\). This follows from the strictly separated intervals, the strict triangle margin and the continuous interior solution; no degenerating last frequency occurs here.

For \(p=\sum_jp_j\), write \(p(i\beta)=X-iY\), and put \(G_X=\beta X'-2X,\ G_Y=\beta Y'-2Y\), with \(\beta\)-derivatives. The same positive hyperbolic series as Note08 give
\[
 X>0,\quad Y\ge0,\quad G_X>0,\quad G_Y\ge0,\qquad
 D_2(p)=-XG_X-YG_Y.                                       \tag{15}
\]
This includes all inter-triple cross terms. More quantitatively let
\[
 a_0=\sqrt{17/12}-1,\quad
 \ell_1=\tfrac12\log(5/3),\quad \ell_2=\tfrac12\log(3/2),
\]
\[
 \Gamma_\beta=\frac{a_0^2\beta^6}{24}
          (\ell_1^2-\ell_2^2)(\ell_1^4-\ell_2^4)>0.
\]
The weight slope gives \(A_2\ge b_1-b_3\ge a_0 b_L\). For \(N\ge20\), \(X_0/N\le21/20\), so \(Lr_1\ge\ell_1\), \(Lr_2\le\ell_2\). The quadratic term of the cosh difference lower-bounds \(X_j\); its quartic term, multiplied by \(4-2=2\), lower-bounds \(G_{X,j}\). Therefore
\[
 X\ge\frac{a_0\beta^2}{2}(\ell_1^2-\ell_2^2)\frac W{L^2},
 \quad
 G_X\ge\frac{a_0\beta^4}{12}(\ell_1^4-\ell_2^4)\frac W{L^4},
 \quad D_2(p)\le-\Gamma_\beta\frac{W^2}{L^6}.              \tag{16}
\]
Also \(p(i\beta),p'(i\beta)=O_\beta(W/L^2)\). This follows directly from event subtraction and \(r_i=O(L^{-1})\); for example each even remainder is \(O_\beta(b_L/L^2)\) and each odd remainder is \(O_\beta(b_L/L^3)\).

## 5. Repair the complete event without breaking multiplicativity

In every triple shift the phase of its second member by a common \(t\), and the third by a common \(s\), leaving the first unchanged. For the reserved population define
\[
 F(t,s)=\left(W^{-1}\sum_{{\cal R}}x_n(t,s),\
              LW^{-1}\sum_{{\cal R}}\lambda_n y_n(t,s)\right).
\]
At zero, \(F(0,0)=0\). Its Jacobian has signs and uniform bounds
\[
 DF(0)=\frac1W
 \begin{pmatrix}
  -\sum y_2&-\sum y_3\\
  L\sum r_2x_2&L\sum r_3x_3
 \end{pmatrix}
 =\begin{pmatrix}-A_J&B_J\\-C_J&-D_J\end{pmatrix},
 \qquad A_J,B_J,C_J,D_J\asymp1.                            \tag{17}
\]
Here each sum is over all triples; \(x_2,x_3<0\), \(y_2>0>y_3\). Thus \(\det DF=A_JD_J+B_JC_J\) is uniformly positive, its inverse is bounded, and all second derivatives of \(F\) on a fixed small parameter disk are bounded uniformly. The compactness used in §4 pays every bound in (17).

Solve
\[
 F(t,s)=\left(-\frac{B(0)+K(0)}W,\
                  \frac{L(B'(0)+K'(0))}W\right).           \tag{18}
\]
By (2), (10), (13), the target is \(O_{\beta,{\cal Q}}(L/W)=o(1)\). The uniform inverse-function theorem gives \(t,s=O_{\beta,{\cal Q}}(L/W)\). Explicitly, the bounded inverse and bounded second derivatives make the linearized inverse plus its quadratic remainder a contraction on a ball of radius a fixed multiple of the target norm, once that norm is small. This supplies a uniform neighborhood rather than an unquantified inverse assumption.

Assign the final prime values by \(\omega(p)=e^{i\theta_p}/u_1\) on \({\cal R}\), and retain every previously fixed prime value elsewhere. Prime isolation means this adjustment changes no complementary coefficient; extend completely multiplicatively. The new control sum is \(p+\Delta p\). Its full field
\[
 q_*=B+p+\Delta p+K
\]
has \(q_*(0)=q_*'(0)=0\) exactly by (18), and retains all \(n\le N\) with their exact \(d_n\). Hence \(S_*=q_*\) satisfies (3) even with \(\epsilon=0\), as well as all calibration conditions.

The repair must be paid **after event subtraction**. Bounding its raw value only gives \(O_{\beta,{\cal Q}}(L)\), which is unnecessary. Since \(p(0)=p'(0)=q_*(0)=q_*'(0)=0\),
\[
 q_*=p+E,\quad E=B^\circ+K^\circ+(\Delta p)^\circ.
\]
For a changed mode, subtraction removes the constant and linear terms, so the value and derivative remainders on the fixed scaled disk are bounded by a constant times \(d_n(|t|+|s|)\lambda_n^2\). Thus
\[
 |(\Delta p)^\circ(i\beta)|+|((\Delta p)^\circ)'(i\beta)|
 =O_{\beta,{\cal Q}}(W(L/W)/L^2)=O_{\beta,{\cal Q}}(L^{-1}).
\]
Equation (13) pays \(B^\circ,(B^\circ)'\) at the observation; (2) pays \(K^\circ\). Therefore \(E(i\beta),E'(i\beta)=O_{\beta,{\cal Q}}(1)\), without claiming a uniform complex-disk bound for the chosen background.

Expanding the full quadratic form, including the background/correction cross terms and the exact carrier, now gives
\[
 D_a(q_*)\le-\Gamma_\beta\frac{W^2}{L^6}
 +O_{\beta,{\cal Q}}\left(\frac W{L^2}+1+
                              a^{-2}\frac{W^2}{L^6}\right).
                                                                    \tag{19}
\]
The first relative error is \(O_{\beta,{\cal Q}}(L^4/W)\to0\); every other relative error also tends to zero by (10). Consequently
\[
 D_a(q_*)\le-\tfrac12\Gamma_\beta W^2/L^6
 \le-\kappa_\beta e^{(1/2-c/8)L}/L^8,\qquad
 \boxed{\kappa_\beta=\Gamma_\beta/12800>0}.                \tag{20}
\]
This proves (7)–(8). The whole \(K(w)\), not just two selected jets, remains in the field and the estimate. The physical error (6) is much smaller, but it is not an approximation theorem for this twisted point.

## 6. Interpretation, controls and ownership

The theorem refutes a nonnegative lower bound using only exact magnitudes, complete unit-phase multiplicativity, actual \(u_1\), any fixed finite prime calibration, and the two event equations. A sound certificate over that set must hold at \(q_*\), so it cannot prove the proposed bound. This statement includes the full signed quadratic form and does not depend on limitations of an optimization solver.

It does not exclude estimates using the actual linked \((a,T,\Theta,\nu,N)\), a growing calibrated prime family with paid uniform bounds, additional event jets, global all-realness or another consumer. No common twist across centers or times is supplied. Realizing phases at a different height would also change the cutoff, weights, carrier and correction; no such transfer is established. The explicit defect (9) already rules out realization at the **same** height. The heat weights were never made multiplicative:
\[
 d_{mn}/(d_md_n)=e^{c\log m\log n/(2L)}\quad(mn\le N).
\]
All of them are kept directly; no Euler-product substitution or unproved convergence in the critical strip enters.

The [control catalog](../../../../result-summaries/12_collision_controls_and_screening.md) is screened analytically; no existing numerical certificates were rerun.

| Control class | Failed premise or scope relevant to r7 |
| --- | --- |
| Present multiplicative point | All multiplicative identities and fixed calibration pass; actual same-height phase at \(q_0\) fails by (9). Global all-realness, physical reflected pair and canonical trajectory are not constructed. |
| Earlier complete multiplicative-twist control | Already stops a universal first-jet floor. It does not by itself prove the present signed margin with retained correction and fixed prime calibration. |
| R5 disks / R6 circles | Exact magnitudes fail in r5; phase multiplicativity fails in r6. Neither earlier construction proves r7 without the new extension. |
| Euler-factor / translated | Unchanged complete theta coefficients fail; a nonreal witness time need not be an all-real threshold event. |
| Weighted-square / finite-tail / finite-prime orbit | Full normalized reflection and/or the complete canonical source fail; finite-tail controls have no all-real time. Preserving source identities at finitely many primes is different from the phase calibration in (7). |
| Reflected super-Gaussian / smooth shape / positive primitive | Canonical square-series arithmetic fails; a local collision does not automatically supply the all-real hypothesis in (5). |
| Atomic / exact finite-profile / compact-source thresholds | Genuine all-real events and the negative geometric sign survive; exact theta coefficients, full growth and eventual threshold simplicity fail. |
| RH-conditional endpoint | Conditional time-zero construction and failed ordinary Dirichlet arithmetic; no unconditional positive-time canonical inference. |
| Variable-readout / heat counter-kernels | Literal cosine readout, full source and/or physical heat generator fail. |
| Relaxed zero/profile populations | Exact canonical integer zero multiset and simultaneous full-field identification fail. |

The genuine positive-source threshold control in Note06 §6 still satisfies (5) at the microscopic observation. It is not assigned the present coefficients or correction. The signed value of \(q_*\) is instead a finite-phase-class counterexample, without a physical source or global zero claim.

The collision manuscript owns the isolated-prime multiplicative obstruction; Note08 owns the elementary signed triple algebra. HDA/GNP-RS owns the provider and correction. [HCB](../../03_heat_flow_collision_bounds/research-progress/02_POST_CALIBRATION_RESEARCH_PROGRESS_20261028.md) retains general first-jet/Poisson acquisition and its actual signed-remainder result at a different band. [OA](../../08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/03_collision_constraints/notes/11_TND_OA_AFTER_E02_CONTINUATION_AND_MODEL_CHANGE_20261109.md) stays parked. No source or task ownership is transferred.

**Return:** r7 completes with the signed extension (7)–(20) and a scoped failed-method result. No favorable canonical margin, new zero-exclusion region, instantiated onset, numerical campaign, agents, manuscript or executable E01 packet is produced. The objective still includes every \(0<T\le1/2,\ a>0,\ m\ge2\); this asymptotic band does not locate an unknown threshold.

The next conceptual pass, if requested, should use actual same-height information or a materially different constraint outside the theorem. Adding multiplicative identities or a fixed finite prime calibration to the same relaxation is now a stopped route. A growing calibration is not excluded, but its uniform errors and exceptional-event application would need a new method; the constant \(C_{\cal Q}\) is not such a proof. See [Review07](../reviews/07_RSCT_B01_R7_SAME_ASSISTANT_CHECK_20261111.md) and the [model-change continuation](01_RSCT_CONTINUATION_AND_PROMPT_20261111.md).
