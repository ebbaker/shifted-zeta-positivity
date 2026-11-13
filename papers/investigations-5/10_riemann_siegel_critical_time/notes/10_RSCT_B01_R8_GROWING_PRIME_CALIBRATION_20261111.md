# RSCT-B01 r8: growing calibration of actual prime phases

11 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance, RSCT chat0003. Actual backend model and reasoning effort are unavailable in the recorded configuration.

**Status: proved in-note from named classical and inherited approximation inputs; same-assistant checking only.** The signed lower bound still fails when every prime up to
\[
 Y_\gamma(L)=\gamma L^2(\log L)^2,\qquad
 0<\gamma<9/256,\qquad L=\log(a/(4\pi)),
\]
has its actual same-height phase. All multiplicative identities, exact coefficient magnitudes, the actual leading phase, both local event equations, every cutoff mode and the full correction are retained. The conclusion is uniform for \(c=TL\in[1/2,1]\) at a sufficiently large, uninstantiated onset. **This is a counterexample in the stated growing-calibration class, not a canonical arithmetic value or a physical collision.** The constant \(9/256\) specifies a sufficient range for this construction; no sharp boundary for possible estimates is established.

This is a quantitative extension of [R7 / Note09](09_RSCT_B01_R7_MULTIPLICATIVE_PHASE_TEST_20261111.md), not a new isolated-prime mechanism. The [collision manuscript](../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex), sc:character and sc:remaining, owns the earlier complete multiplicative-twist first-jet obstruction; [Note08](08_RSCT_B01_R6_EXACT_CIRCLE_TEST_20261111.md) owns the signed triple algebra. R7 paid fixed finite calibration. Here every dependence on the calibrated set is displayed before permitting it to grow.

Read the [result index](../../../../result-summaries/README.md), [cluster11](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md), [controls12](../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../avoid/README.md), especially [01](../../../../avoid/01_restating_the_target.md), [02](../../../../avoid/02_shape_only_arguments_and_the_controls.md), [07](../../../../avoid/07_scoped_exclusions_read_as_universal.md), [12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [16](../../../../avoid/16_unchecked_imports_and_novelty_claims.md). This is an information-class test with a quantitative counterexample, not an RH-equivalent criterion or a favorable arithmetic estimate.

## 1. Fixed field, consumer and proposed calibration

Use the inherited local coordinates and exact model coefficients
\[
 T=c/L,\quad N=\lfloor e^{L/2}\rfloor,\quad z=a+w/L,\quad
 \nu=a/2+\pi T/8,\quad u_1=e^{i\Theta(T,a)},
\]
\[
 d_n=n^{-1/2}\exp\!\left\{\frac{c}{4L}
       [(\log n)^2-L\log n]\right\},\qquad
 \lambda_n=\frac14-\frac{\log n}{2L}.                       \tag{1}
\]
For a completely multiplicative unit function \(\omega\), put
\[
 q_\omega(w)=\frac12\sum_{n\le N}d_n
 \left[u_1\omega(n)e^{i\lambda_nw}
       +\overline{u_1\omega(n)}e^{-i\lambda_nw}\right]+K(w),
 \qquad S_\omega=q_\omega-q_\omega(0)-wq_\omega'(0).         \tag{2}
\]
The actual canonical choice is \(\omega(n)=n^{-i\nu}\). Every phase, \(T\) and \(N\) is held fixed in spatial derivatives. The same actual correction \(K\), real on the real axis, satisfies
\[
 \|\partial_w^jK\|_R=O_R(\chi),\quad
 \chi=a^{-1/4}e^{-cL/16},\quad j\le2,                       \tag{3}
\]
on each fixed scaled disk of radius \(R>\max(1,\beta)\). [Note06](06_RSCT_B01_R4_MICROSCOPIC_EVENT_EXPANSION_20261111.md) supplies the canonical field approximation and its analytic \(O_R(a^{-3/4})\) errors. This provider is inherited, not independently audited here.

Fix \(\beta>0\) and keep the exact physical carrier:
\[
 D_a(g)=\mathfrak d_a|g(i\beta)|^2+
       \beta\Im[g'(i\beta)\overline{g(i\beta)}],\qquad
 \mathfrak d_a=2+O_\beta(a^{-2}L^{-2}).                    \tag{4}
\]
Its exact definition is Note09 (4); \(D_2\) denotes replacement of \(\mathfrak d_a\) by 2. For an actual all-real event of any multiplicity \(m\ge2\), the inherited identity is
\[
 D_a(f)=\left[(2-m)k_a-\frac{\beta^2}{L^2}
 \sum_{r\ne\pm a}\frac1{(a-r)^2+\beta^2/L^2}\right]
 |f(i\beta)|^2<0,\quad
 k_a=1+\frac{(\beta/L)^2}{4a^2+(\beta/L)^2},                \tag{5}
\]
where \(f=H_T/A\) and all copies of the two reflected event roots are removed. The canonical acquisition error remains
\[
 O_\beta(a^{-3/4}e^{(1/4-c/16)L}/L^2+a^{-3/2})=o(1).
\]
Neither (5) nor a twisted physical approximation is asserted for an arbitrary \(\omega\).

The tested lower-bound method adds the actual same-height constraints
\[
 \omega(p)=p^{-i\nu}\quad\hbox{for every prime }p\le Y(L)   \tag{6}
\]
to full multiplicativity, exact magnitudes and the two local event equations. In particular (6) fixes every retained integer whose prime factors are all at most \(Y(L)\), including its prime powers. It does not fix the entire height orbit.

## 2. A uniform calibration-cost lemma

Retain R7's reserved primes \(\mathcal R\): choose
\[
 M=\left\lfloor\frac{N}{40\log N}\right\rfloor
\]
primes in each of the three intervals
\[
 [11N/20,3N/5],\quad[7N/10,3N/4],\quad[17N/20,9N/10],
\]
and match them into triples. The classical prime number theorem supplies enough primes eventually. Each reserved prime exceeds \(N/2\), so its only multiple among \(n\le N\) is itself. Define
\[
 b_L=e^{-(1/4+c/16)L},\quad
 W=M b_L,\quad \delta(c)=1/4-c/16,
\qquad
 \frac{e^{\delta L}}{80L}\le W\le\frac{e^{\delta L}}{10L}.  \tag{7}
\]

Let \(\mathcal Q=\mathcal Q(a,c)\) be **any** finite set of primes at most \(N/2\), with arbitrary prescribed unit phases. Its size and members may vary. Set
\[
 C_{\mathcal Q}=\prod_{p\in\mathcal Q}(1-p^{-1/2})^{-1},
 \qquad \mathcal E_{\mathcal Q}=\frac{C_{\mathcal Q}L^4}{W}.
                                                                    \tag{8}
\]
The empty product is 1. Constants below depend on \(\beta\), the fixed disk and inherited provider constants, but not on \(\mathcal Q\), its phases or \(c\).

**Uniform lemma.** If \(\mathcal E_{\mathcal Q}\to0\) uniformly over the considered parameter family as \(a\to\infty\), the prescribed phases can be extended to a completely multiplicative unit function with
\[
 q_\omega(0)=q_\omega'(0)=0,\qquad
 D_a(S_\omega)\le-\frac{\Gamma_\beta}{2}\frac{W^2}{L^6}
 \le-\kappa_\beta\frac{e^{(1/2-c/8)L}}{L^8},               \tag{9}
\]
where
\[
 \begin{split}
 a_0&=\sqrt{17/12}-1,\quad
 \ell_1=\tfrac12\log(5/3),\quad \ell_2=\tfrac12\log(3/2),\\
 \Gamma_\beta&=\frac{a_0^2\beta^6}{24}
       (\ell_1^2-\ell_2^2)(\ell_1^4-\ell_2^4)>0,\qquad
 \kappa_\beta=\Gamma_\beta/12800.
 \end{split}                                             \tag{10}
\]
The hypothesis is a sufficient counterexample budget for a specified estimating class, not a favorable canonical criterion.

### Complete complementary sum

Let \(B\) be the sum in (2) over \(n\notin\mathcal R\), without \(K\). Assign independent uniform unit phases to all remaining unprescribed primes. The inequalities from Note09 (11) are uniform:
\[
 d_n^2\le n^{-9/8},\quad \sum_{n\le N}d_n^2\le9,\quad
 d_{rm}\le r^{-1/2}d_m\quad(rm\le N).
\]
Group \(n=rm\), with \(r\) supported on \(\mathcal Q\) and \(m\) divisible by none of its primes. Distinct complementary \(m\)'s have distinct characters of the free primes. A reserved prime cannot occur in them because it has no other retained multiple. The coefficient of each character is at most
\[
 e^{\beta/4}d_m\sum_{r:\,\mathcal Q\text{-supported}}r^{-1/2}
 =e^{\beta/4}C_{\mathcal Q}d_m
\]
for either arm at \(0,i\beta\), including the first derivative since \(0\le\lambda_n\le1/4\). Finite character orthogonality and the convex bound for the two reflected arms give a choice satisfying
\[
 |B(0)|^2+|B'(0)|^2+|B(i\beta)|^2+|B'(i\beta)|^2
 \le36e^{\beta/2}C_{\mathcal Q}^2.                        \tag{11}
\]
This proof holds for each finite \(\mathcal Q\) with the **same displayed constant**; no fixed-cardinality compactness is used. The deterministic smooth-integer group \(m=1\) is included. All composites and the \(n=1\) mode remain. Auxiliary phase integration proves existence of a complement, not a height average or a bound for the actual canonical complement.

### Uniform inverse and event-subtracted repair

For each reserved triple use the exact-circle quadratures of Note09 (14). Their sum \(p\) obeys
\[
 p(0)=p'(0)=0,\quad
 D_2(p)\le-\Gamma_\beta W^2/L^6,\quad
 |p(i\beta)|+|p'(i\beta)|\le C_\beta W/L^2.                \tag{12}
\]
The signs include all cross terms between triples. These primes and coefficients do not depend on \(\mathcal Q\). The separated proportional intervals place their normalized weights and scaled frequencies in a compact nondegenerate family.

Shift all second members' phases by \(t\), all third members' by \(s\). The map
\[
 F(t,s)=\left(W^{-1}\sum_{\mathcal R}x_n,\,
             LW^{-1}\sum_{\mathcal R}\lambda_n y_n\right)
\]
has \(F(0)=0\), uniformly bounded second derivatives and a Jacobian
\[
 DF(0)=\begin{pmatrix}-A_J&B_J\\-C_J&-D_J\end{pmatrix},
 \quad A_J,B_J,C_J,D_J\asymp1,\quad
 \det DF(0)=A_JD_J+B_JC_J>0.                              \tag{13}
\]
Every bound here is independent of the calibrated set. By (3) and \(C_{\mathcal Q}\ge1\), (11) bounds the complete target
\[
 F(t,s)=\left(-\frac{B(0)+K(0)}W,\,
             \frac{L(B'(0)+K'(0))}W\right)
\]
by \(C_\beta L C_{\mathcal Q}/W=C_\beta\mathcal E_{\mathcal Q}/L^3\).
The same quantitative local inverse/contraction therefore gives
\[
 |t|+|s|\le C_\beta\,\frac{L C_{\mathcal Q}}W              \tag{14}
\]
once this target is sufficiently small. The inverse radius and constant do not depend on the number or choice of calibrated phases. Reserved-prime isolation ensures that the phase change preserves all of (11) and every prescribed phase.

Writing the changed reserved sum as \(p+\Delta p\), the complete field
\(q_*=B+p+\Delta p+K\) has both event equations exactly. Let \(h^\circ=h-h(0)-wh'(0)\). Then
\[
 q_*=p+E,\qquad E=B^\circ+K^\circ+(\Delta p)^\circ.
\]
Each changed, subtracted mode and its first derivative at \(i\beta\) cost at most \(C_\beta d_n(|t|+|s|)\lambda_n^2\). Since reserved frequencies are \(O(L^{-1})\), (14) yields
\[
 |(\Delta p)^\circ(i\beta)|
   +|((\Delta p)^\circ)'(i\beta)|
 \le C_\beta C_{\mathcal Q}/L,\quad
 |E(i\beta)|+|E'(i\beta)|\le C_\beta C_{\mathcal Q}.         \tag{15}
\]
Equation (11) pays \(B^\circ\) and its derivative at that observation, while (3) pays the whole correction. No uniform complex-disk estimate for the chosen complementary sum is asserted.

The complete product error is consequently
\[
 D_a(q_*)\le-\Gamma_\beta\frac{W^2}{L^6}
 +C_\beta\left(\frac{C_{\mathcal Q}W}{L^2}
                 +C_{\mathcal Q}^2
                 +a^{-2}\frac{W^2}{L^6}\right).           \tag{16}
\]
The last term pays \(\mathfrak d_a-2\); mixed/background carrier terms are absorbed into the first two terms. Dividing the allowance by \(W^2/L^6\) gives
\[
 C_\beta\left(\mathcal E_{\mathcal Q}
          +\frac{\mathcal E_{\mathcal Q}^2}{L^2}
          +a^{-2}\right)\longrightarrow0.                \tag{17}
\]
This proves (9). It explicitly replaces R7's fixed-\(\mathcal Q\) constants; substituting a growing set into that notation alone would not have proved this lemma.

## 3. A growing initial segment of actual prime phases

The only external arithmetic input is the classical prime number theorem, freshly checked at [NIST DLMF 27.2.3](https://dlmf.nist.gov/27.2#E3). Partial summation gives
\[
 \sum_{p\le Y}p^{-1/2}
 =\frac{\pi(Y)}{\sqrt Y}+\frac12\int_2^Y\frac{\pi(t)}{t^{3/2}}\,dt
 \sim\frac{2\sqrt Y}{\log Y}.                            \tag{18}
\]
The first term and the integral each contribute \(\sqrt Y/\log Y\); for the latter use \(\int_2^Y t^{-1/2}/\log t\,dt\sim2\sqrt Y/\log Y\). For \(0\le z\le1/\sqrt2\),
\[
 0\le-\log(1-z)-z\le z^2/(1-1/\sqrt2).
\]
The higher logarithmic terms therefore cost \(O(\sum_{p\le Y}p^{-1})=O(\log Y)\), using only the harmonic sum. Since \(\log Y=o(\sqrt Y/\log Y)\),
\[
 \log\prod_{p\le Y}(1-p^{-1/2})^{-1}
 =(2+o(1))\frac{\sqrt Y}{\log Y}.                         \tag{19}
\]
No Mertens estimate, short-interval theorem, RH or effective PNT remainder is imported.

Choose a fixed \(0<\gamma<9/256\) and
\[
 Y=\gamma L^2(\log L)^2.
\]
The prime number theorem also supplies a prime \(q_0\in(Y,2Y]\) for every sufficiently large \(Y\). Set
\[
 \mathcal Q=\{p:p\le Y,\ p\text{ prime}\}\cup\{q_0\},
 \quad \omega(p)=p^{-i\nu}\ (p\le Y),\quad
 \omega(q_0)=-q_0^{-i\nu}.                               \tag{20}
\]
Since \(2Y<N/2\) eventually, none of these primes is reserved. The additional factor for \(q_0\) changes \(\log C_{\mathcal Q}\) by \(O(Y^{-1/2})\), uniformly for the choice in \((Y,2Y]\). Equation (19) gives
\[
 \log C_{\mathcal Q}=(\sqrt\gamma+o(1))L,\quad
 \mathcal E_{\mathcal Q}
 \le80L^5\exp\!\left[-(3/16-\sqrt\gamma+o(1))L\right]
 \longrightarrow0,                                     \tag{21}
\]
uniformly in \(c\in[1/2,1]\), because \(\delta(c)\ge3/16\). The lemma now constructs an \(\omega\) satisfying (6), both event equations and the negative margin (9). Its explicit defect from the canonical phase at the same height is
\[
 |u_1\omega(q_0)-u_1q_0^{-i\nu}|=2.                      \tag{22}
\]
The defect prime moves with the height; it is not a fixed prime left outside all growing initial segments.
The onset may depend on the fixed \(\beta,\gamma\) and inherited constants. No uniform onset as \(\gamma\uparrow9/256\) is asserted.

A convenient concrete choice is
\[
 \boxed{Y(L)=\frac{L^2(\log L)^2}{64}.}
\]
Here \(\log C_{\mathcal Q}=(1/8+o(1))L\), hence eventually \(C_{\mathcal Q}\le e^{5L/32}\) and
\[
 \mathcal E_{\mathcal Q}\le80L^5e^{-L/32}\to0.             \tag{23}
\]
The number of calibrated primes is
\[
 \pi(Y)\sim \frac{L^2\log L}{128}\to\infty.
\]
More generally it is \((\gamma/2+o(1))L^2\log L\). Every \(Y\)-smooth retained integer has the actual unit phase as well. Nevertheless \(Y/N\to0\), and the number of calibrated primes is a vanishing fraction of the retained primes. No almost-complete calibration is proved.

## 4. Scope, controls and next boundary

The theorem stops the proposed nonnegative lower bound on this particular growing-calibration class, including the explicit cutoff (23). It does not show that every growing calibration fails. The endpoint \(\gamma=9/256\), larger cutoffs, arbitrary calibrated sets failing the sufficient budget (8), all actual phases simultaneously, global all-realness and additional event jets are outside the conclusion. In particular, failure of (8) is not evidence that a favorable estimate exists. Optimizing its constant alone supplies no canonical sign or event exclusion.

For each fixed prime, (6) eventually enforces its actual phase. This pointwise statement in the prime index is not uniform control of the full population as both the height and cutoff tend to infinity. The witness \(\omega\) may vary with \(a,c\); no common twist, heat trajectory, global reflected pair or all-real zero set is constructed. A phase realization at another height would also change \(\Theta,\nu,d_n,N,K\), and no such transfer is paid. The nonmultiplicative weights remain exactly those in (1):
\[
 d_{mn}/(d_md_n)=e^{c\log m\log n/(2L)}\quad(mn\le N).
\]
The finite calibration product is an elementary sum over supported integers, not an Euler product for the canonical heat field.

The [control catalog](../../../../result-summaries/12_collision_controls_and_screening.md) is screened analytically, without rerunning numerical certificates:

| Control class | Relevant failed premise or scope |
| --- | --- |
| Present growing-calibration point | All tested constraints pass; actual same-height phase fails at the moving \(q_0\) by (22). Global all-realness and a physical event are not constructed. |
| Earlier multiplicative control / R7 | The isolated-prime mechanism is inherited. R7 alone has no uniform growing-set claim; (11)–(17) supply that payment. |
| R5 disks / R6 circles | Exact magnitudes fail in R5; phase multiplicativity fails in R6. Their conclusions are not silently broadened. |
| Euler-factor / translated controls | Unchanged complete theta coefficients fail. A nonreal witness time need not be an all-real threshold. |
| Weighted-square / finite-tail / finite-prime source-orbit controls | Full canonical reflection and/or complete canonical source fail; finite tails lack an all-real time. Their source constraints differ from (6). |
| Reflected super-Gaussian / smooth-shape / positive-primitive controls | Canonical square-series arithmetic fails; local collisions alone do not establish the global premise in (5). |
| Atomic / exact finite-profile / continuous compact-source thresholds | Genuine all-real events survive, but full theta arithmetic, profile growth and eventual threshold simplicity fail. |
| RH-conditional endpoint controls | The RH assumption and failure of ordinary Dirichlet arithmetic remain; no unconditional canonical event follows. |
| Variable-readout / heat counter-kernels | Literal cosine readout, complete source and/or physical Newman generator fail. |
| Relaxed zero/profile populations | Exact canonical integer zero multiset and simultaneous full-field identification fail. |

The inherited physical consumer retains arbitrary \(m\ge2\) and both reflected events. The algebraic witness satisfies the two equations necessary for every such event, but no other multiplicity equations or global all-realness are imposed. HDA/GNP-RS retains provider ownership; the collision manuscript/R6/R7 retain the cited construction ownership. [HCB](../../03_heat_flow_collision_bounds/research-progress/02_POST_CALIBRATION_RESEARCH_PROGRESS_20261028.md) retains unconditioned first-jet and actual signed-remainder acquisition; [OA](../../08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/03_collision_constraints/notes/11_TND_OA_AFTER_E02_CONTINUATION_AND_MODEL_CHANGE_20261109.md) stays parked.

**Return:** R8 completes with a uniform calibration budget and the explicit growing-cutoff counterexample. No favorable canonical margin, new zero coverage, finite onset, numerical campaign, agents, manuscript or executable E01 method is produced. The eventual target still includes every \(0<T\le1/2,\ a>0,\ m\ge2\); nothing places an unknown threshold in the tested asymptotic band. A further conceptual pass should select a concrete estimate using actual phase information beyond this budget or materially different event information. See [Decision08](../brainstorm/notes/08_RSCT_B01_R8_GROWING_CALIBRATION_DECISION_20261111.md), [Review08](../reviews/08_RSCT_B01_R8_SAME_ASSISTANT_CHECK_20261111.md) and the [continuation](01_RSCT_CONTINUATION_AND_PROMPT_20261111.md).
