# Riemann–Siegel research state and promising next steps

12 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Current chat: “Review Riemann–Siegel
research,” thread `01a1d0f2-d298-7bb0-8216-92b682abb5b2`, registered as
chat0005 in this investigation's [chat-histories](../../chat-histories/README.md).
The actual backend model and reasoning effort are absent from the recorded
configuration; neither is inferred.

**Status: research review and brainstorm.** The strongest current Green
result controls an actual canonical observable in mean. The next bounded
opportunity is a quantitative mean with a growing Euler cutoff. A separate
exceptional-center estimate remains necessary for pointwise exclusion.
The critical-time investigation has useful local approximation and strong
controls, but no favorable canonical arithmetic sign. No new execution
task, manuscript milestone, or full growing-cutoff theorem is claimed here.

This review uses the requested [overview][overview], [progress register][progress],
and [external RSCT comparison][comparison], with their supporting Notes03,
14, 17, 19, 20 and selected RSCT manuscript sections. It is not an independent
audit of the inherited HDA provider. The [result index][results], especially
[heat-flow cluster11][cluster11] and [collision controls12][controls], and
the [avoid index][avoid] govern interpretation. Apply [target classification][avoid01],
[premise screening][avoid02], [scoped exclusions][avoid07], and
[signed versus separate estimates][avoid12].

## 1. Two questions sharing one field

The common field and clock are
\[
 H_\lambda(z)=\int_0^\infty e^{\lambda u^2}\Phi(u)\cos(zu)\,du,
 \qquad H_0(z)=\tfrac18\xi((1+iz)/2),\qquad
 \partial_\lambda H_\lambda=-\partial_z^2H_\lambda.
\]
The complete theta source, reflected contribution, gamma normalization,
correction and remainder are retained. On the real boundary, the physical
coordinate is twice the classical zeta height.

GNP-RS studies every sufficiently large center on
\[
 L_X=\log(X/(4\pi)),\qquad \lambda=c/L_X,
 \qquad \tfrac12\le c\le1.
\]
RSCT instead assumes a positive Newman threshold and tries to contradict
\[
 \Lambda>0,\qquad H_\Lambda(a)=H_\Lambda'(a)=0,
 \qquad\text{all zeros of }H_\Lambda\text{ real},\qquad a>0.
\]
The event can have any multiplicity at least two. Its finite attainment
follows from the published uniform positive-time bound and compactness;
it is not a new result of either investigation. Nothing establishes
\(\Lambda L_a\in[1/2,1]\). The two questions have different domain and
time quantifiers.

## 2. What the Green branch has obtained

For the strip \(0<\Im z<8\), the observation point is \(X+4i\). Set
\[
 K(t)=\frac1{16\cosh(\pi t/8)},\qquad \int_{\mathbb R}K=\tfrac12.
\]
The exact observable is
\[
 \begin{split}
 J_\lambda(X)&=\int_{\mathbb R}K(x-X)
  \bigl(\log|H_\lambda(x)|+\log|H_\lambda(x+8i)|\bigr)\,dx
       -\log|H_\lambda(X+4i)|\\
 &=\sum_{y_j>0}\operatorname{atanh}
    \frac{\sin(\pi y_j/8)}{\cosh(\pi(X-x_j)/8)}\ge0.
 \end{split}                                                    \tag{1}
\]
Zeros are counted with multiplicity, and the canonical strip gives
\(y_j\le1\). This is a positive measurement of nonreal zeros, not their
unweighted count. A zero with \(|x_j-X|\le r\) and \(d\le y_j\le1\)
forces
\[
 J_\lambda(X)\ge m(d,r)
       :=\frac{d\sin(\pi/8)}{\cosh(\pi r/8)}.                  \tag{2}
\]
The selected consumer has \(d=1/2,r=1\). A sufficiently small upper bound
would exclude that depth and neighborhood. The all-center identity
\(J_0\equiv0\) is RH-equivalent; it is the endpoint target, not an
intermediate gain.

The uniform outer estimate [E01][e01] is
\[
 \left|J_{c/L_X}(X)-I_{c/L_X}(X)+P_{c,c/L_X}(X)\right|
       \le C_{\rm out}/L_X.                                   \tag{3}
\]
Here \(V_\lambda=H_\lambda/C_-\) uses the explicit nonvanishing carrier,
\(I_\lambda=\int K(x-X)\log|V_\lambda(x)|\,dx\), and
\[
 P_{c,\lambda}(X)=\sum_{n\ge2}\frac{\Lambda_{\rm vM}(n)}{\log n}
 \frac{n^{-5/2-c/4}}{1+n^{-4}}
 \cos\bigl((X/2+\pi\lambda/8)\log n\bigr).
\]
Thus the outer boundary, carrier and prime baseline are controlled.
The signed value of the critical-boundary logarithm remains the issue.
The constants and onset are finite analytical quantities, not numerically
certified values. The result retains the inherited provider's review scope.

The strongest actual-value conclusion [E07][e07] is, for every fixed
\(p>0\) and \(0<\alpha<4\),
\[
 \frac1U\int_U^{2U}J_{1/L_X}(X)^p\,dX\longrightarrow0,
 \qquad
 \frac1U\int_U^{2U}e^{\alpha J_{1/L_X}(X)}\,dX\longrightarrow1. \tag{4}
\]
The fourth exponential mean is eventually at most 39; convergence at
exponent four is not proved. These are **proved in-note from named inherited
inputs; same-assistant self-check only**. They have no rate, concern only
\(c=1\), and sample a different time at each outer center. Time remains
fixed inside each spatial integral. They do not count zeros on a fixed
time slice or exclude sparse exceptional centers.

The negative results have precise scope. The quadratic-Jensen allowance
fails the chosen margin at arbitrarily high centers. Every fixed finite
Euler reference has unbounded relative residuals there, defeating the
specified separate residual payment. The tested fixed-reference tangent
also fails, even with a center-selected regulator. These are failures of
those upper estimates, not lower bounds on the actual Green value and not
exclusions of all adaptive or nonlinear methods.

## 3. The remaining arithmetic quantity

Use the unchanged window \(W_X=[X-(32/\pi)\log X,X+(32/\pi)\log X]\).
With \(\sigma_c=1/2+c/4\), \(\nu_\lambda(x)=x/2+\pi\lambda/8\),
\(\phi_\lambda=2\Theta(\lambda,x)\), define
\[
 E_P(x)=\prod_{p\le P}(1-p^{-\sigma_c}e^{i\nu_\lambda(x)\log p})^{-1},
 \qquad S_P^{\rm ref}=E_P+e^{i\phi_\lambda}\overline{E_P},
\]
\[
 R_P(X,c)=\int_{W_X}K(x-X)
       \frac{|V_\lambda(x)-S_P^{\rm ref}(x)|^2}{|E_P(x)|^2}\,dx.
                                                                  \tag{5}
\]
All center data, including time and cutoff, stay fixed in this integral.
For fixed \(P\), [E05][e05] proves
\[
 \frac1U\int_U^{2U}R_P(X,1)\,dX\longrightarrow
 \mu_P=\zeta(3/2)\prod_{p\le P}(1-p^{-3/2})-1\longrightarrow0.
                                                                  \tag{6}
\]
The height limit precedes increasing \(P\). Substituting a growing cutoff
into its \(O_P\) constants would not prove a new statement.

[E06][e06] separately permits \(P(X)=\lfloor L_X^2\rfloor\): the joint
reference/carrier phase cost is at most \(18/L_X\), uniformly in the full
\(c\) band and positive regulator. The reference tails and complete-field
comparison are also paid. Writing \(q_X=\int_{W_X}K\) and
\(b_\delta=(\delta+\sqrt{\delta^2+4})/2\), its bound reads
\[
 J_\lambda(X)\le q_X\log b_\delta+
 \frac{q_X}{2}\log\left(1+\frac{R_P(X,c)}{q_X\delta^2}\right)
        +O(L_X^{-1}),                                          \tag{7}
\]
after absorbing the paid prime and exterior terms. The constant in this
overhead is independent of the regulator. Equation (7) does not estimate
\(R_P\). That is the first unpaid quantity for this particular method.

## 4. What transfers from the critical-time work

At an all-real threshold, (1) gives \(J_\Lambda(X)=0\) even when there
is a multiple real zero. Just below an ordinary double event the upper
zero height is \(\sqrt{2(\Lambda-\lambda)}+O(\Lambda-\lambda)\), and
its Green atom tends to zero. The threshold value alone cannot detect
the collision. This is explained in [Note20][geometry].

The complete symmetric representation is
\[
 H_\lambda(x)=2\Re\mathcal A_{\lambda,N}(x),
 \qquad H_\lambda'(x)=2\Re\mathcal A_{\lambda,N}'(x),            \tag{8}
\]
with the remainder retained and \(N\) fixed locally. A multiple zero
requires simultaneous cancellation of both real parts. If the complete
arm is nonzero, it requires \(\Im(\mathcal A'/\mathcal A)=0\) at the
zero; the arm-zero case is a separate obligation.

RSCT's [local approximation][rsct-local], for \(z=a+w/L_a\), gives
\[
 f_a(w)=H_\lambda(a+w/L_a)/A(\lambda,a+w/L_a),\qquad
 \|\partial_w^j(f_a-q_a)\|_{|w|\le R}\le C_Ra^{-3/4},
 \quad 0\le j\le4.                                            \tag{9}
\]
At an actual event, subtracting the constant and linear terms of \(q_a\)
improves the value error to \(O_R(a^{-3/4}|w|^2)\). The correction remains
inside \(q_a\). The signed Poisson functional's approximation error is
paid, but its favorable canonical arithmetic sign is not obtained.

The [joint calibrated construction][rsct-mirror] preserves exact
magnitudes, multiplicativity, the actual leading phase, actual prime
phases through \(Y=\gamma L_a^2(\log L_a)^2\), \(0<\gamma<9/256\),
the event equations, the full correction and one necessary mirror
inequality. It still permits the collision-compatible signed value.
Its remaining phases differ from the actual same-height values. This
screens that information class, not the canonical field, all possible
jet constraints, or the integrated Green residual. In particular, its
cutoff exceeding \(L_a^2\) does not refute the proposal in Section 5.

Local deflation is a conditional supporting transfer. For an actual
order-\(m\) zero,
\[
 f(w)=w^m g(w),\qquad \log|f(w)|=m\log|w|+\log|g(w)|.
\]
It still requires a complete actual divisor/root count and a lower bound
for the regular factor \(g\). Small additive error does not supply that
floor. The parent's approximate-knot estimate through second factor
derivatives requires order five for a pair, beyond (9)'s explicitly paid
four; a Cauchy bound on a larger disk must be supplied if used. A fixed
scaled chart also covers only physical width \(O(1/L_a)\), not the full
\(O(\log X)\) Green window.

## 5. Recommended first question and a concrete proof tactic

The external comparison's quantitative mean is the best bounded next
target. Begin with a cutoff fixed on each dyadic block,
\(P_U=\lfloor L_U^2\rfloor\), and seek
\[
 \left|\frac1U\int_U^{2U}R_{P_U}(X,1)\,dX-\mu_{P_U}\right|
       \le\varepsilon(U,P_U),\qquad\varepsilon(U,P_U)\to0.     \tag{10}
\]
This is an **unproved quantitative milestone**, not an RH-equivalent
criterion. A bound \(\varepsilon=O(1/\log U)\) is a useful stronger
target to test, not an established rate. A blockwise cutoff avoids
unproved interchange with the center-dependent schedule. The latter
needs a further comparison or a direct uniform proof.

There is a concrete issue in E05's proof: the reciprocal Euler product
is expanded over divisors of \(D_P=\prod_{p\le P}p\), giving an apparent
polynomial length \(D_P\sqrt U\). Its fixed-\(P\) treatment cannot simply
be reused at \(P\asymp(\log U)^2\). A possible replacement is to truncate
by integer size with a weighted tail bound before estimating height means.

The following elementary bound is derived here only as a proof aid.
At \(c=1\), write
\[
 Q_P=E_P^{-1}=\sum_{d\mid D_P}\mu(d)d^{-3/4}e^{i\nu\log d}.
\]
For \(M\ge1\) and fixed \(0<\eta<1/4\),
\[
 \begin{split}
 \sum_{\substack{d\mid D_P\\d>M}}d^{-3/4}
 &\le M^{-\eta}\prod_{p\le P}(1+p^{-3/4+\eta})\\
 &\le M^{-\eta}\exp(C_\eta P^{1/4+\eta}).
 \end{split}                                                   \tag{11}
\]
Indeed \(d^{-\eta}\le M^{-\eta}\) on the tail, the remaining squarefree
sum factors, and \(\log(1+x)\le x\) plus an integer sum bounds the product.
The analogous positive expansion of \(E_P\) over integers supported on
primes at most \(P\) has the same form, with a different constant, using
\(-\log(1-x)\le x/(1-2^{-3/4+\eta})\). Thus at \(P=O((\log U)^2)\)
and \(M=U^\theta\), fixed \(\theta>0\), these uniform tails are
\(U^{-\theta\eta+o(1)}\).

This avoids charging the largest possible product of retained primes as
the effective support length. It does **not** finish (10). The complete
proof would still have to pay:

- truncation after multiplication by the full growing arithmetic arm;
- diagonal convergence to \(\mu_P\) uniformly in \(P\), rather than fixed-index domination;
- same-arm and reflected cross terms, including the rational-frequency multiplier;
- moving time, all cutoff jumps, spatial and height edges, and the complete correction;
- choosing \(\theta\) small enough for the oscillatory budgets while controlling the discarded terms in the required norm.

The tail calculation is compatible with arbitrary prime phases and does
not distinguish a collision. Its value is in removing one parameter-growth
obstacle from a canonical mean proof. No novelty or literature-priority
claim is made for this elementary weighted truncation.

There is a direct quantitative consumer for a successful (10). Since
every integer greater than one coprime to \(D_P\) exceeds \(P\),
\[
 0\le\mu_P=\sum_{\substack{n>1\\(n,D_P)=1}}n^{-3/2}
       \le\sum_{n>P}n^{-3/2}\le2P^{-1/2}.                     \tag{12}
\]
Let \(\bar r_U=2P_U^{-1/2}+\varepsilon(U,P_U)\). The phase gates in
E06 hold for the blockwise choice too, since \(P_U\le L_X^2\) on
\([U,2U]\). Using \(q_X\log b_\delta\le\delta/4\) and
\(\log(1+t)\le t\) in (7), then averaging, gives the conditional bound
\[
 \frac1U\int_U^{2U}J_{1/L_X}(X)\,dX
 \le\frac\delta4+\frac{\bar r_U}{2\delta^2}+O(L_U^{-1})
 \ll\bar r_U^{1/3}+L_U^{-1},                                 \tag{13}
\]
by taking \(\delta\asymp\bar r_U^{1/3}\). Hence an error
\(O(L_U^{-1})\) in (10) would yield a mean Green bound
\(O(L_U^{-1/3})\). This is an elementary consequence **conditional on
the unproved estimate (10)**, not a rate acquired in this session.

## 6. The harder question after a quantitative mean

A useful rate is not automatically an exceptional-center theorem.
Even at fixed time, one defect with a spatial footprint of bounded width
can contribute only order \(1/U\) to a normalized dyadic average while
having a fixed positive local Green value. The rate in (13) is compatible
with such exceptional contributions.

Furthermore, fixed-time spatial smoothing cannot be applied unchanged
along the moving-time curve. Wherever differentiation is legitimate,
\[
 \frac{d}{dX}J_{1/L_X}(X)
 =\left(\partial_XJ_\lambda(X)
       -\frac1{XL_X^2}\partial_\lambda J_\lambda(X)
        \right)\bigg|_{\lambda=1/L_X}.                        \tag{14}
\]
The small coefficient of the time derivative does not itself control
that derivative near a collision. The ordinary double-event square-root
law illustrates this issue. Equation (14) is a chain rule, not a
regularity theorem at event times.

Two distinct longer-term possibilities remain: a direct bound
for the actual signed logarithm/residual at every center, or a quantitative
argument showing that any relevant defect forces enough mass in a region
where an available space-time estimate contradicts it. The latter must
specify the depth, time interval, persistence width and mass scale; a
dyadic rate without that comparison is insufficient.

For the RSCT endpoint question, any new signed estimate must use data
absent from the calibrated model. The actual phases
\[
 u_n^{\rm can}=e^{i\Theta(\lambda,a)}
       e^{-i(a/2+\pi\lambda/8)\log n}
\]
all arise from the same physical height and time, together with the weights,
cutoff and correction. Quantitative cancellation for that full trajectory,
or stronger jointly used all-real constraints, remains possible but no
working estimate has been identified. Adding another constraint should
start by naming the information it contributes and testing it jointly,
not by assuming the R9 control already covers every finite list.

## 7. Control screen and priorities

This is an analytical premise screen of the recorded witness families,
not a rerun of their numerical certificates. The proposed mean need not
fail on an isolated collision; no exclusion follows from it alone.

| Control class | Missing premise for the unchanged canonical mean or endpoint application |
| --- | --- |
| Euler-factor and translated sources | Exact unchanged theta coefficients, completion and prime subtraction. |
| Weighted squares, finite tails and prefixes | Full canonical square series together with source reflection; their local events need not be finite all-real thresholds. |
| Finite-prime orbits | Full reflection and complete arithmetic beyond the matched finite data. |
| Reflected super-Gaussian, smooth-shape and positive-primitive controls | Literal theta square-series arithmetic, despite their shared positivity or reflection. |
| Atomic, finite-profile and continuous compact controls | Full theta profile and canonical large-height behavior; matching selected floors is insufficient. |
| Conditional endpoint controls | Ordinary Dirichlet arithmetic, with their RH premise still conditional. |
| Heat counter-kernels and variable-readout constructions | Complete canonical source and/or literal cosine readout and physical generator. |
| Relaxed Green profiles | Exact integer zero multiset identified with the complete boundary field. |
| RSCT calibrated multiplicative model | Actual phases at the same height beyond the calibrated set; no full Green-window law or globally all-real canonical field is supplied. |

Generic truncation, Jensen and logarithmic-transfer inequalities may hold
for eligible controls. Naming absent arithmetic premises does not prove
that a proposed quantitative inequality distinguishes the control. That
additional comparison is required before any exclusion claim.

The recommended order is:

1. **Quantify the canonical residual mean.** Produce a dependence ledger
   and (10), or the first precise obstruction. Try weighted size truncation
   before accepting a primorial-length loss. This has the clearest bounded
   theorem target and a measurable consequence (13).
2. **State the exceptional-center requirement quantitatively.** Select
   either a direct signed estimate or a space-time persistence comparison,
   with its required scale. This is the main conceptual gap toward exclusion.
3. **Use RSCT local approximation only for a specified deflation consumer.**
   Identify the divisor, regular-factor floor, derivative order and chart
   coverage before extending the error calculation.
4. **Audit the shared provider before major dependent expansion.** Both
   branches depend on the inherited complete complex approximation. Their
   existing LLM checks share that premise; neither supplies independent
   specialist validation.

Extending mean results to the full c band or investigating the exponent-four
endpoint could be useful later. They are lower priorities than obtaining a
rate with explicit cutoff dependence and identifying the exceptional-set
bridge. Repeating fixed-reference quadratic estimates, fixed-height matrix
tests with the already identified growing background, or sampled-height
verification does not address the present missing input.

The domain obligations also remain: bounded heights, shrinking depth,
other \(\lambda L_X\) regimes, arbitrary event multiplicity and the
time-zero endpoint. No completed estimate in the chosen band silently
covers these. The live progress registers and their existing stopped or
reserved tasks remain unchanged by this discussion.

## 8. Source inspection and verification scope

On 12 November 2026, the version-pinned primary HTML of D. H. J. Polymath,
*Effective approximation of heat flow evolution of the Riemann ξ function,
and a new upper bound for the de Bruijn–Newman constant*,
[arXiv:1904.12438v2](https://arxiv.org/html/1904.12438v2), 4 August 2019,
was reopened. Selected checked statements: (1)–(4), the normalization and
backward heat equation, and Theorem 1.5(i)–(ii), including the absolute
\(e^{C/\lambda}\) high-zero bound used in finite event attainment.
This is selected-passage inspection, not a full-paper or HDA audit.
The existing [reference record](../../references/README.md) and canonical
HDA bibliography retain ownership; no new article or PDF copy was added.

The new elementary deductions (11)–(14) were checked algebraically in this
review. Equation (13) has an explicitly unproved premise. No numerical
research, independent assessment or proof of (10) was performed.

[overview]: ../../research-overview/01_GNP_RS_RESEARCH_OVERVIEW_20261110.md
[progress]: ../../research-progress/01_GNP_RS_RESEARCH_PROGRESS_20261110.md
[comparison]: ../external/01_RSCT_MANUSCRIPT_COMPARISON_AND_PROPOSED_QUESTIONS_20261112.md
[results]: ../../../../../../result-summaries/README.md
[cluster11]: ../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[avoid01]: ../../../../../../avoid/01_restating_the_target.md
[avoid02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[avoid07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[avoid12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[e01]: ../../notes/03_GNP_RS_E01_UNIFORM_OUTER_BASELINE_PROOF_20261111.md
[e05]: ../../notes/14_GNP_RS_E05_FINITE_EULER_RESIDUAL_20261111.md
[e06]: ../../notes/17_GNP_RS_E06_ADAPTIVE_PHASE_AND_TANGENT_20261111.md
[e07]: ../../notes/19_GNP_RS_MANUSCRIPT_AND_AVERAGED_GREEN_VALUES_20261111.md
[geometry]: ../../notes/20_GNP_RS_GREEN_GEOMETRY_AND_CRITICAL_TIME_20261111.md
[rsct-local]: ../../../../10_riemann_siegel_critical_time/manuscript/sections/04_microscopic_acquisition.tex
[rsct-mirror]: ../../../../10_riemann_siegel_critical_time/manuscript/sections/07_mirror_jet.tex
