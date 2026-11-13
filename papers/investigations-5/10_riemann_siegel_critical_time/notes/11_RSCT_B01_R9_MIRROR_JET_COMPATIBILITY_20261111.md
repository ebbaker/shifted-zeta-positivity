# RSCT-B01 r9: fourth-jet mirror condition and signed-value compatibility

11 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance, RSCT chat0003. Actual backend model and reasoning effort are unavailable in the recorded configuration.

**Status: proved in-note from named classical and inherited approximation inputs; same-assistant checking only.** Adding the forced-mirror fourth-jet Laguerre condition to R8's growing-calibration class does not repair the proposed signed Poisson lower bound. A complete multiplicative point can be selected with both event equations exact, negative signed Poisson value, and a strictly positive mirror-jet margin. **Passing this one necessary all-real condition does not establish a globally all-real field or a canonical collision.**

The [collision manuscript](../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex), lj:mirror, lj:hierarchy and lj:paidtest, already proves the mirror condition, its multiplicity hierarchy and complete measured-error formula. Its lj:quartic control already shows that the PDE and this condition allow positive thresholds in a polynomial class. Those facts are not new here. [R7](09_RSCT_B01_R7_MULTIPLICATIVE_PHASE_TEST_20261111.md) and [R8](10_RSCT_B01_R8_GROWING_PRIME_CALIBRATION_20261111.md) supply the isolated-prime signed construction and uniform calibration budget. R9 extends the selection to enough observations to control the fourth jet, and proves simultaneous compatibility with this additional necessary condition, preserving all the previously declared arithmetic constraints and correction.

Read the [result index](../../../../result-summaries/README.md), [cluster11](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md), [controls12](../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../avoid/README.md), especially [01](../../../../avoid/01_restating_the_target.md), [02](../../../../avoid/02_shape_only_arguments_and_the_controls.md), [07](../../../../avoid/07_scoped_exclusions_read_as_universal.md), [08](../../../../avoid/08_normalization_and_constant_slips.md) and [16](../../../../avoid/16_unchecked_imports_and_novelty_claims.md). Classification: a bounded information-class test using an inherited necessary condition, not a new endpoint criterion.

## 1. Objects and the additional condition being tested

Keep
\[
 L=\log(a/(4\pi)),\quad T=c/L,\quad c\in[1/2,1],\quad
 N=\lfloor e^{L/2}\rfloor,\quad z=a+w/L,\quad
 \nu=a/2+\pi T/8,\quad u_1=e^{i\Theta(T,a)},
\]
\[
 d_n=n^{-1/2}\exp\!\left\{\frac{c}{4L}
       [(\log n)^2-L\log n]\right\},\qquad
 \lambda_n=\frac14-\frac{\log n}{2L}.                      \tag{1}
\]
For a completely multiplicative unit function \(\omega\), set
\[
 q_\omega(w)=\frac12\sum_{n\le N}d_n
 [u_1\omega(n)e^{i\lambda_nw}
     +\overline{u_1\omega(n)}e^{-i\lambda_nw}]+K(w),\qquad
 S_\omega=q_\omega-q_\omega(0)-wq_\omega'(0).              \tag{2}
\]
All phases, \(T,N\) remain fixed in spatial derivatives. The canonical choice is \(\omega(n)=n^{-i\nu}\). The complete actual correction \(K\) is that of [Note06](06_RSCT_B01_R4_MICROSCOPIC_EVENT_EXPANSION_20261111.md), real on the real axis. The signed Poisson expression remains
\[
 D_a(g)=\mathfrak d_a|g(i\beta)|^2+
       \beta\Im[g'(i\beta)\overline{g(i\beta)}],\quad
 \mathfrak d_a=2+O_\beta(a^{-2}L^{-2}),\quad\beta>0
 \text{ fixed},                                         \tag{3}
\]
with the exact carrier definition in Note09 (4). The physical all-real event identity retains every multiplicity \(m\ge2\) and both roots \(\pm a\), as in Note10 (5); it forces \(D_a(f)<0\) for the canonical normalized field \(f=H_T/A\). The canonical Poisson acquisition error is still \(o(1)\). No twisted physical approximation is asserted.

R9 adds one consequence of global all-realness: remove two copies of the event at \(a\), retain at least two copies of its mirror at \(-a\), and use the first Laguerre inequality for the deflated function. This is more information than the two event equations, but is not global all-realness itself.

## 2. Exact normalization of the inherited mirror condition

At an actual all-real event let \(H_j=H_T^{(j)}(a)\), with physical \(z\)-derivatives. The paired Hadamard product is recorded in [Polymath v2, proof of Proposition 3.1](https://arxiv.org/html/1904.12438v2#S3); it is locally uniformly convergent, with an absolutely convergent inverse-square sum away from the roots. Deflate
\[
 G(z)=H_T(z)/(z-a)^2.
\]
The mirror roots give, along real nonroots,
\[
 (G')^2-GG''=G^2\sum_{\rho:\,G(\rho)=0}(z-\rho)^{-2}
 \ge \frac{2G^2}{(z+a)^2}.
\]
Take the continuous limit at \(a\). Since
\[
 G(a)=H_2/2,\quad G'(a)=H_3/6,\quad G''(a)=H_4/12,
\]
the inherited condition is exactly
\[
 2H_3^2-3H_2H_4\ge9H_2^2/a^2.                            \tag{4}
\]
This argument does not take a logarithmic derivative at a zero of \(G\). It remains valid for \(m>2\); for \(m\ge4\) both sides of (4) vanish. The higher multiplicity hierarchy requires higher jets and is not replaced by (4).

Use the actual nonvanishing local normalization from Note06:
\[
 A(T,z)=\frac{\pi^{1/4}}{16}z^{7/4}
 \exp\{-\pi z/8+T(L(z)^2-\pi^2/4)/16\},\quad
 b(T,z)=A_z/A=\frac7{4z}-\frac\pi8+\frac{TL(z)}{8z}.
\]
At an event, \(f(0)=f'(0)=0\). With \(T\) held fixed in the physical derivatives,
\[
 H_2/A=L^2f_2,\qquad H_3/A=L^3f_3+3bL^2f_2,
\]
\[
 H_4/A=L^4f_4+4bL^3f_3+6(b^2+b_z)L^2f_2.
\]
These exact identities cancel the \(b\) and \(b^2\) terms in (4). After division by \(A(T,a)^2L^6\), the result is
\[
 \mathcal J_a(f):=2f_3^2-3f_2f_4-\mu_a f_2^2\ge0,
 \qquad f_j=\partial_w^j f(0),                            \tag{5}
\]
\[
 \mu_a=\frac{18b_z(T,a)+9/a^2}{L^2}
 =\frac{-45/2-9c/4+9c/(4L)}{a^2L^2}<0\quad(L\ge1).       \tag{6}
\]
Indeed \(b_z=[-7/4+T(1-L)/8]/a^2\). The \(L^{-2}\) in (6) comes from the fourth-versus-sixth powers in the scaled jets; the factor 9 comes from the two forced mirror copies. The sign in (6) is a property of this normalization, not a removal of the mirror contribution.

The same polynomial \(\mathcal J_a(g)=2g_3^2-3g_2g_4-\mu_a g_2^2\) is defined for any locally analytic real-on-real \(g\). Its nonnegativity alone has no converse asserting all-real zeros.

## 3. Pay the fourth jet and the approximate necessary condition

Note06 bounds the **holomorphic value error** on every fixed larger scaled disk, not merely its first two real derivatives. Fix \(R>\max(1,\beta)\), use its bound on \(|w|\le2R\), and apply Cauchy on \(|w|\le R\). For each \(j\le4\),
\[
 |\partial_w^j(f-q_{\rm can})|
 \le j!R^{-j}C_{2R}a^{-3/4},\qquad
 |\partial_w^jK|\le C_{R,j}\chi,\quad
 \chi=a^{-1/4}e^{-cL/16}.                                \tag{7}
\]
Thus the extension to four derivatives is explicitly paid from the existing larger analytic chart. No moving-cutoff derivative, smaller unproved buffer or independent HDA audit is used.

Let \(\epsilon_j=C_j a^{-3/4}\) be the resulting allowances at zero, \(j=2,3,4\), and \(q_j=q_{\rm can}^{(j)}(0)\). Expanding every product gives
\[
 \begin{split}
 |\mathcal J_a(f)-\mathcal J_a(q_{\rm can})|
 \le\Delta_a(q,\epsilon):={}&4|q_3|\epsilon_3+2\epsilon_3^2\\
 &+3|q_2|\epsilon_4+3|q_4|\epsilon_2+3\epsilon_2\epsilon_4\\
 &+|\mu_a|(2|q_2|\epsilon_2+\epsilon_2^2).
 \end{split}                                             \tag{8}
\]
For fixed \(j=2,3,4\), the complete coefficient moments from Note06 (8) give
\[
 |q_j|\le M_j+O_j(\chi)=O_j(e^{\delta L}/L^j),\qquad
 \delta=1/4-c/16.
\]
Consequently
\[
 \Delta_a=O(a^{-3/4}e^{\delta L}/L^2+a^{-3/2})=o(1),       \tag{9}
\]
uniformly in \(c\). This is a complete absolute product error, not a favorable arithmetic sign. The earlier collision manuscript already establishes the principle of a vanishing full-cutoff fourth-jet payment; (6)–(9) transfer it to this frozen scaled model.

At an actual event, the correct necessary conditions on the approximant are
\[
 |q(0)|,|q'(0)|\le\epsilon,\qquad
 \mathcal J_a(q)\ge-\Delta_a(q,\epsilon),\qquad
 \epsilon=O(a^{-3/4}),                                   \tag{10}
\]
not automatically \(\mathcal J_a(q)\ge0\). Subtracting the first two jets to form \(S\) leaves \(\mathcal J_a\) unchanged. The tested method would use (10), together with R8's calibrated multiplicative constraints, to obtain a nonnegative signed Poisson lower bound. Below the point satisfies the stricter equalities \(q(0)=q'(0)=0\) and \(\mathcal J_a(q)>0\), so it defeats the proposed bound also on the correctly paid class (10).

## 4. Select a complete point with both signed margins

Retain R8's three reserved prime intervals, \(M=\lfloor N/(40\log N)\rfloor\) triples, their union \(\mathcal R\), and
\[
 W=M e^{-(1/4+c/16)L},\qquad
 W\ge e^{\delta L}/(80L).
\]
Let \(\mathcal Q\) be a prescribed prime set below \(N/2\), and
\[
 C_{\mathcal Q}=\prod_{p\in\mathcal Q}(1-p^{-1/2})^{-1},
 \qquad \mathcal E_{\mathcal Q}=C_{\mathcal Q}L^4/W\to0.   \tag{11}
\]
Uniformity is over the parameter family for which (11) is uniform. As in R8, each reserved prime divides only its own term in the cutoff.

### Seven observations of one complement

Let \(B\) be the complete complementary sum, including \(n=1\) and every nonreserved composite, without \(K\). In R8's finite character argument add \(B''(0),B'''(0),B''''(0)\) to the original four observations. For each added derivative, the extra multiplier \(\lambda_n^j\le1\), so the same second-moment bound applies with no new set-dependent constant. One assignment of all unprescribed complementary prime phases therefore satisfies
\[
 \sum_{j=0}^4|B^{(j)}(0)|^2
       +|B(i\beta)|^2+|B'(i\beta)|^2
 \le63e^{\beta/2}C_{\mathcal Q}^2.                        \tag{12}
\]
The grouping into \(\mathcal Q\)-supported and free parts still includes the deterministic smooth-integer group. This is one auxiliary phase selection controlling all seven observations simultaneously, not seven incompatible choices or a height average. It need not be the particular complement selected in an earlier note.

### Second and fourth derivatives of the reserved triples

For each triple use R7's exact quadratures
\[
 (b_1,0),\quad(-A_2,\rho v),\quad(-A_3,-v),\qquad
 A_2+A_3=b_1,\quad \rho=r_3/r_2,\quad r_1>r_2>r_3>0,
\]
where \(r_i=\lambda_{p_i}\) and every magnitude is \(b_i=d_{p_i}\). Write its contribution as \(\sum_i(x_i\cos r_iw-y_i\sin r_iw)\), and let \(p\) be the sum over all reserved triples. Then
\[
 p(0)=p'(0)=0,
\]
\[
 -p''(0)=\sum_{\rm triples}
 [A_2(r_1^2-r_2^2)+A_3(r_1^2-r_3^2)],
\]
\[
 p''''(0)=\sum_{\rm triples}
 [A_2(r_1^4-r_2^4)+A_3(r_1^4-r_3^4)].                   \tag{13}
\]
Set, with the same constants as R7,
\[
 a_0=\sqrt{17/12}-1,\quad
 \ell_1=\tfrac12\log(5/3),\quad \ell_2=\tfrac12\log(3/2),
\]
\[
 h_2=a_0(\ell_1^2-\ell_2^2)>0,\qquad
 h_4=a_0(\ell_1^4-\ell_2^4)>0.
\]
The proved bounds \(A_2\ge a_0e^{-(1/4+c/16)L}\), \(Lr_1\ge\ell_1\), \(Lr_2\le\ell_2\) yield
\[
 p''(0)\le-h_2W/L^2,\qquad p''''(0)\ge h_4W/L^4.          \tag{14}
\]
All signed sums in (13) are retained. The previous signed Poisson proof also gives
\[
 D_2(p)\le-\Gamma_\beta W^2/L^6,\quad
 \Gamma_\beta=\beta^6h_2h_4/24,\quad
 |p(i\beta)|+|p'(i\beta)|=O_\beta(W/L^2).                 \tag{15}
\]

### Complete phase repair and the two final signs

Use R8's collective two-phase inverse on the second and third triple members. Its normalized Jacobian and second derivatives are independent of \(\mathcal Q\). Equation (12) only changes the absolute target constant, so
\[
 |t|+|s|=O_\beta(LC_{\mathcal Q}/W).
\]
The resulting full field \(q_*=B+p+\Delta p+K\) has both event equations exactly. No complementary mode or calibrated prime changes. For \(j=2,3,4\),
\[
 |(\Delta p)^{(j)}(0)|
 \le C_jW(|t|+|s|)L^{-j}
 =O_\beta(C_{\mathcal Q}L^{1-j}).
\]
By (7), (12), all full jets satisfy
\[
 q_*^{(j)}(0)=p^{(j)}(0)+O_\beta(C_{\mathcal Q}),
 \qquad j=2,3,4.                                       \tag{16}
\]
Since \(C_{\mathcal Q}=o(W/L^4)\), (14) now implies
\[
 q_*''(0)\le-\tfrac12h_2W/L^2<0,\qquad
 q_*''''(0)\ge\tfrac12h_4W/L^4>0.                        \tag{17}
\]
In particular the artificial local field has **exactly** a double zero. All jets are real. Because \(\mu_a<0\), both \(2(q_*''')^2\) and \(-\mu_a(q_*'')^2\) are nonnegative, so the complete fourth-jet polynomial obeys
\[
 \boxed{\mathcal J_a(q_*)\ge
       \frac34h_2h_4\frac{W^2}{L^6}
       \ge c_{\rm J}\frac{e^{(1/2-c/8)L}}{L^8}>0,\qquad
       c_{\rm J}=\frac{3h_2h_4}{25600}.}                 \tag{18}
\]
This uses the signs of the complete corrected second/fourth derivatives; no potentially negative cross term is dropped.

The original observation and event-subtracted repair bounds still hold under the stronger selection (12). R8's complete signed payment is therefore unchanged in scale:
\[
 D_a(q_*)\le-\Gamma_\beta W^2/L^6+
 O_\beta(C_{\mathcal Q}W/L^2+C_{\mathcal Q}^2
                   +a^{-2}W^2/L^6).
\]
Its relative allowance is \(O_\beta(\mathcal E_{\mathcal Q}
+\mathcal E_{\mathcal Q}^2/L^2+a^{-2})=o(1)\). Hence simultaneously
\[
 \boxed{D_a(S_*)=D_a(q_*)\le
   -\kappa_\beta\frac{e^{(1/2-c/8)L}}{L^8}<0,\qquad
   \kappa_\beta=\Gamma_\beta/12800.}                     \tag{19}
\]
Both inequalities concern the same complete phase assignment and correction.

### Retain the growing actual-prime calibration

For any fixed \(0<\gamma<9/256\), take \(Y=\gamma L^2(\log L)^2\). Use every prime \(p\le Y\) at its actual phase, and a prime \(q_0\in(Y,2Y]\) at the opposite phase, as in R8:
\[
 \omega(p)=p^{-i\nu}\ (p\le Y),\qquad
 \omega(q_0)=-q_0^{-i\nu}.
\]
The classical PNT product calculation already proved there gives
\[
 \log C_{\mathcal Q}=(\sqrt\gamma+o(1))L,\qquad
 \mathcal E_{\mathcal Q}\to0
\]
uniformly in \(c\in[1/2,1]\). Equations (17)–(19) follow at an onset depending on fixed \(\beta,\gamma\) and inherited constants. The explicit choice \(Y=L^2(\log L)^2/64\) is retained. Every retained \(Y\)-smooth integer phase is also actual, and
\[
 |u_1\omega(q_0)-u_1q_0^{-i\nu}|=2.                      \tag{20}
\]
Thus the full same-height orbit is still not realized. Neither sharpness of \(9/256\) nor uniformity as \(\gamma\) approaches it is claimed.

## 5. Interpretation, controls and continuation boundary

The new intersection of constraints is nonempty with both signs required by the local all-real consumers: negative Poisson value and positive mirror fourth-jet value. Therefore this one extra necessary condition cannot repair the proposed nonnegative Poisson bound over R8's estimating class. The nonnegative fourth-jet value is not a counterexample to the Laguerre theorem; it satisfies the theorem's necessary sign.

This does not exclude an estimate using full canonical phases, an actual global all-real zero set, additional deflated conditions, the higher multiplicity hierarchy or another consumer. It does not establish that every finite collection of jet constraints can be met. The artificial double zero supplies no physical heat collision or global reflected pair. Only the physical consumer, not the constructed point, carries the full canonical source and arbitrary multiplicity. All \(d_n\), including their nonmultiplicative heat cross factors, remain unchanged in the algebraic sum.

The generic compatibility of all-realness, the heat PDE and the mirror inequality with a collision was already established by lj:quartic. R9 adds the complete arithmetic-model constraints, growing calibration, actual correction and simultaneous signed margins. The [control catalog](../../../../result-summaries/12_collision_controls_and_screening.md) is screened analytically:

| Control class | Relevant failed premise or scope |
| --- | --- |
| Present seven-observation multiplicative point | Passes the calibrated phases, exact magnitudes, event equations and strict mirror sign. Actual same-height phase fails at \(q_0\); global all-realness and physical trajectory are not constructed. |
| Earlier quartic threshold heat model | Has a genuine all-real threshold and saturates the mirror inequality. Full theta source, infinite zero population and arithmetic coefficients fail; the generic compatibility is prior work. |
| R7/R8 points | Their existence statements did not control the added jets. R9 selects one complement satisfying all seven observations; no earlier arbitrary realization is retroactively assigned the property. |
| Euler-factor / translated | Unchanged complete theta arithmetic fails; a nonreal witness time need not be an all-real threshold to which (4) applies. |
| Weighted-square / finite-tail / finite-prime source-orbit | Full canonical reflection and/or source fail; local collisions do not supply global all-realness, and finite tails have no all-real time. |
| Reflected super-Gaussian / smooth-shape / positive-primitive | Canonical square-series arithmetic fails; a local event alone does not justify the mirror inequality. |
| Atomic / exact finite-profile / continuous compact-source thresholds | Genuine all-real events satisfy the necessary mirror sign. Full theta arithmetic, profile growth and eventual threshold simplicity fail. |
| RH-conditional endpoint | The conditional assumption and failure of ordinary Dirichlet arithmetic remain; no unconditional canonical event is supplied. |
| Variable-readout / heat counter-kernels | Literal cosine readout, full source and/or physical Newman generator fail. |
| Relaxed zero/profile populations | Exact canonical integer zero multiset and complete full-field identification fail. |

The collision manuscript retains mirror-jet and isolated-prime ownership; R6–r8 retain their construction and uniform-calibration results. HDA/GNP-RS retains provider ownership; [HCB](../../03_heat_flow_collision_bounds/research-progress/02_POST_CALIBRATION_RESEARCH_PROGRESS_20261028.md) keeps general first-jet and actual signed-remainder acquisition. [OA](../../08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/03_collision_constraints/notes/11_TND_OA_AFTER_E02_CONTINUATION_AND_MODEL_CHANGE_20261109.md) remains parked.

**Return:** R9 completes with paid fourth-jet acquisition and a scoped simultaneous-compatibility result. No favorable canonical arithmetic sign, new zero coverage, finite onset, numerical campaign, agents, manuscript or executable E01 method is produced. The full objective still ranges over \(0<T\le1/2,\ a>0,\ m\ge2\); the tested band does not locate a hypothetical threshold. A future pass must specify information beyond this one mirror inequality and the existing calibrated class, rather than equating that inequality with global all-realness. See [Decision09](../brainstorm/notes/09_RSCT_B01_R9_MIRROR_JET_DECISION_20261111.md), [Review09](../reviews/09_RSCT_B01_R9_SAME_ASSISTANT_CHECK_20261111.md) and the [continuation](01_RSCT_CONTINUATION_AND_PROMPT_20261111.md).
