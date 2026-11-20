# AGC-E18 r1: actual-height recurrence of a negative dyadic allowance

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Execution helper explicitly dispatched
**gpt-6.1-sol / ultra**; independent serving-backend model and effort
attestation is unavailable. **Type E**, under the
[frozen E18 r1 request](../research-progress/handoffs/AGC-E18-r1-request.md)
following [B06 Note22](22_AGC_B06_ACTUAL_PHASE_DECISION_20261119.md).
One analytical pass and one bounded correction pass. No numerical
sample, transcendental execution, rational-witness replay or source
change is used.

**Status: proved in-note; accepted within the fixed actual-phase recurrence scope by [Review10](../reviews/10_AGC_ACTUAL_PHASE_ASSESSMENT_20261119.md).**
For every closed length-19 interval in one fixed natural-cutoff chart of

\[
\mathcal F_0:\quad t=\frac1{10},\quad y=\frac15,\quad
x_0=14000+\sqrt{24/25}\le x\le30000,
\tag{1}
\]

there is an **actual height** \(x_*\) in that interval at which the
actual-dyadic-phase cost and its complete allowance satisfy

\[
\boxed{C_{\rm act}(x_*)-(1-g(x_*))>\frac1{100},\qquad
\ell_{\rm act}(x_*)<-\frac1{800},\qquad
m_{\rm act}(x_*)<-\frac1{800}.}
\tag{2}
\]

This excludes uniform positivity on (1) for the fixed three-prime,
separate-anchor, independently relaxed odd-core-rotation estimator
even after its common dyadic phase is restricted to the actual height.
It does not assert failure at every height, at \(x_0\), or at any seam.
It does not upper-bound the actual reference or field magnitude or
exhibit a physical zero. Joint core rotations and signed aggregation
with the anchor remain outside the theorem.

The [sole register](../research-progress/01_AGC_RESEARCH_PROGRESS_20261119.md)
owns live status. Read the
[result index](../../../../result-summaries/README.md),
[pattern index](../../../../avoid/README.md),
[Cluster18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
[Controls12](../../../../result-summaries/12_collision_controls_and_screening.md)
and patterns [01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[11](../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md)
and [12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
Classification: a quantitative obstruction for a stated information
reduction, judged by (2), its interval width and its scope. It is not an
RH-equivalent reformulation or a proposed positive floor.

The six prerequisite identities in the issued request match. Its own
SHA-256 is
\( \texttt{f47e78c9da212897902a80a326e2739ee30275eb7182743b92912ee9469ab4a4} \).
The accepted source interface, constants and exact eight-prime witness
are reused from Notes14 and17–21, Review09 and manuscript Sections5/12.
No new external theorem, published parameter-specific numerical bound,
source audit or specialist review is claimed.

## 1. Actual-phase allowance with the complete source payment

Keep all of Note20's definitions. In particular, with \(T=x/2\),

\[
s_0=\frac35-iT,\qquad s_1=\frac25+iT,\qquad
s=s_0+\frac{\alpha(s_0)}{20}=\sigma+i\tau,\qquad
\alpha(w)=\frac1{2w}+\frac1{w-1}
                  +\frac12\operatorname{Log}\frac w{2\pi},
\]
\[
\mathcal B=\mathfrak M_{1/10}(s_0),\quad
\gamma=\frac{\mathfrak M_{1/10}(s_1)}{\mathfrak M_{1/10}(s_0)},\quad
g=|\gamma|,\quad
\kappa=\frac{\alpha(s_1)-\overline{\alpha(s_0)}}{20},\quad
b_n=e^{\log^2 n/40},\quad
N=\left\lfloor\sqrt{\frac{x}{4\pi}+\frac1{160}}\right\rfloor .
\tag{3}
\]

The exact normalized reference and retained value correction are

\[
f=\sum_{n\le N}b_n n^{-s}
  +\gamma\sum_{n\le N}b_n n^{1/5-\bar s-\kappa},\qquad
q=f-c,\qquad
c=\frac{J_NA_N(W)}{\mathcal B},\quad W=x/2+\pi/80.
\tag{4}
\]

Here \(J_N,A_N\) are precisely Note14's real-profile value formula.
There is no spatial differentiation of that formula. The entire
retained physical payment remains

\[
v=\frac1{|\mathcal B|}
\left\{\sum_{n=1}^N\sum_{\nu\in\{-,+\}}
 |p_n(t,w_\nu)|\epsilon_n(t,w_\nu)
 +L_N(\delta_{\sigma_-}+\delta_{\sigma_+})\right\},
\quad
\left|H_t/\mathcal B-q\right|\le v .
\tag{5}
\]

Every function and constant in (5), including both whole delta payments,
is exactly Note20(5): \(w_\pm=(1\pm y)/2+iT\) and
\(L_N=|J_N|\sqrt W\sqrt{W^2+1}/2\).
No omitted-correction \(+L_N\) payment is inserted and no retained
remainder is deleted. Separately, for

\[
S=\sum_{n\le N}b_n n^{-s},\quad
T_{\rm sum}=\sum_{n\le N}b_n n^{1/5-s},\quad
F=S+\gamma\overline{T_{\rm sum}},
\]

the complete arithmetic replacement is

\[
|f-F|\le D_\kappa,\qquad
D_\kappa=g\sum_{n\le N}b_n n^{1/5-\sigma}
                    (e^{|\kappa|\log n}-1).
\tag{6}
\]

The fixed multiplier and exact convolution are

\[
E=\prod_{p\in\{2,3,5\}}(1-b_p p^{-s}),\quad
\lambda_d=\prod_{p\mid d}(-b_p),\quad \lambda_1=1,
\]
\[
\beta_m=\sum_{\substack{d\mid(m,30)\\m/d\le N}}\lambda_d b_{m/d},
\qquad
a_m=\sum_{\substack{d\mid(m,30)\\m/d\le N}}
                 \lambda_d(m/d)^{1/5}b_{m/d},\quad 1\le m\le30N.
\tag{7}
\]

All frequencies, including every \(m>N\) cutoff edge, remain present.
Only \(n^{-s}\) and its phase are multiplied; heat weights are not
assumed multiplicative. Note20 proves \(0<|E|<8\), \(0<g<3/5\),
\(3/5<\sigma<4/5\), and
\[
e^{-i\theta/2}EF=Z_0+\sum_{r\ {\rm odd}\le30N}
 G_r(\eta_r(x),u(x)),\quad
Z_0=e^{-i\theta/2}+g e^{i\theta/2},
\tag{8}
\]
where \(\rho=\gamma E/\bar E=g e^{i\theta}\),
\(u(x)=-\tau(x)\log2\), and
\(\eta_r(x)=-\tau(x)\log r-\theta(x)/2\).
The finite polynomials \(B_r,A_r\), matrices \(M_r\) and core index
sets are exactly Note20(10)–(14), with the anchor excluded only from
core one's \(j=0\) term.

In the norm
\[
\|w\|_g^2=(\Re w/(1+g))^2+(\Im w/(1-g))^2
\]
the anchor has norm one. Put, at this actual observation,
\[
R_r(x,u)=(1-g)r^{-\sigma}\|M_r(x,u)\|_2,\qquad
C_{\rm act}(x)=\sum_rR_r(x,u(x)).
\tag{9}
\]
Reverse triangle in (8), without a supremum over \(u\), proves
\[
|EF|\ge1-g-C_{\rm act}=:K_{\rm act}.
\]
Dividing by the **exact positive** \(|E|\), then paying (6), \(|c|\)
and the whole (5), gives
\[
\ell_{\rm act}=\frac{K_{\rm act}}{|E|}-D_\kappa-|c|\le|q|,
\qquad m_{\rm act}=\ell_{\rm act}-v.
\tag{10}
\]
This derivation is valid when \(K_{\rm act}<0\). All payments are
nonnegative. The exact direct comparator receives the same coefficients,
phases, correction and complete error, so Note20's ordering becomes
\[
\boxed{m_E\le m_{\rm dyad}\le m_{\rm act}
       \le m_{\rm dir}:=|f-c|-v.}
\tag{11}
\]
The middle inequality uses \(C_{\rm act}\le C_{\rm dyad}\) with the
same coefficients. No measured cost or all-implementation ordering
follows. Strict positivity for (10) requires exactly
\[
C_{\rm act}<1-g-|E|(D_\kappa+|c|+v).
\tag{12}
\]

## 2. A frozen eight-core mean

Let \(\mathcal P_*=\{7,11,13,17,19,23,29,31\}\), and define
\[
C_*(x,u)=\sum_{p\in\mathcal P_*}R_p(x,u)
        \le\sum_rR_r(x,u).
\tag{13}
\]
Every such prime is at most \(N\), is coprime to30 and has
\(\beta_p=b_p\), \(a_p=p^{1/5}b_p\).
At fixed \(x=a\), the finite Fourier-mean argument of Note20 gives
\[
\operatorname{mean}_u R_p(a,u)\ge h_p(a)p^{-\sigma(a)},\qquad
h_p=\max\left(|\beta_p-ga_p|,
             \frac{1-g}{1+g}|\beta_p+ga_p|\right)
       \ge(1-g)b_p.
\]
Using the existing accepted exact-rational witness
\(\sum_{p\in\mathcal P_*}b_p p^{-4/5}>21/20\) and
\(\sigma(a)<4/5\), it follows that
\[
\boxed{\operatorname{mean}_u C_*(a,u)>
                     \frac{21}{20}(1-g(a)).}
\tag{14}
\]
This step alone is an auxiliary-phase fact. The following two estimates
pay for converting it into information at an actual height.

## 3. Smooth coefficient and phase velocities

The carrier logarithm fixed in manuscript Section5 is
\[
L_t(w)=L_0(w)+\alpha(w)^2/40,\qquad L_0'=\alpha.
\]
On \(w=v+iT\), \(2/5\le v\le3/5\), \(7000<T\le15000\),
the principal logarithms avoid their cut and satisfy conjugation.
Since \(T\le|w|<15001\) and \(25/8<\pi<22/7\),
\[
1000<|w|/(2\pi)<2500<e^8.
\]
The last bound reuses \(e>8/3\) and
\(2500\cdot6561<8^8\). Also \(0<\arg w<\pi/2\). Therefore
\[
|\alpha(w)|\le\frac3{2T}
 +\frac12\left(\log\frac{|w|}{2\pi}+\frac\pi2\right)
 <\frac3{14000}+4+\frac{11}{14}<6.
\tag{15}
\]
Direct differentiation gives
\[
\alpha'=-\frac1{2w^2}-\frac1{(w-1)^2}+\frac1{2w},
\qquad
\alpha''=\frac1{w^3}+\frac2{(w-1)^3}-\frac1{2w^2}.
\]
Since both \(|w|\) and \(|w-1|\) are at least \(T\),
\[
|\alpha'|\le\frac1{2T}+\frac3{2T^2}<\frac{51}{100T},
\qquad
|\alpha''|\le\frac1{2T^2}+\frac3{T^3}<\frac1{T^2}.
\tag{16}
\]
The same bounds hold at \(3/5-iT\) by conjugation. Differentiating
\(s=s_0+\alpha(s_0)/20\) along \(x\) gives
\[
s'=-\frac i2-\frac i{40}\alpha'(s_0),\qquad
\boxed{|\sigma'|<\frac1{39x},\qquad
       |\tau'+1/2|<\frac1{39x}.}
\tag{17}
\]
Indeed
\[
\frac{|\alpha'|}{40}
\le\frac1{40x}+\frac3{20x^2}<\frac1{39x};
\]
the last comparison already holds for \(x>234\).

Next,
\[
L_t''=\alpha'+\frac{(\alpha')^2+\alpha\alpha''}{20},
\qquad
|L_t''|<\frac{51}{100T}+\frac7{20T^2}<\frac3{5T}.
\tag{18}
\]
Here \(|\alpha'|<1/T\) was used only to simplify the second term.
Conjugation of the inherited carrier logarithm proves the exact identity
\[
\log g=\Re\{L_t(2/5+iT)-L_t(3/5+iT)\}.
\tag{19}
\]
Integrating \(L_t''\) along the horizontal segment of length \(1/5\)
and using \(dT/dx=1/2\) yields
\[
|(\log g)'|<\frac12\frac15\frac3{5T}=\frac3{25x},
\qquad
\boxed{|g'|<\frac9{125x}<\frac1{10x}.}
\tag{20}
\]
The second bound uses \(g<3/5\). These are smooth ordinary derivatives
of the carrier quantities, not derivatives of the cutoff floor.

## 4. A uniform variation budget for the eight cores

For \(m=p2^j\) with \(p\in\mathcal P_*\), only the divisors
\(d=1,2\) in (7) can occur. The possible original indices \(n\le48\)
in those eight cores are exactly
\[
\begin{array}{c|l}
p& n=p2^k\le48\\ \hline
7&7,14,28\\
11&11,22,44\\
13&13,26\\
17&17,34\\
19&19,38\\
23&23,46\\
29&29\\
31&31
\end{array}
\tag{21}
\]
There are16; retain only their \(n\le N\) subset on each chart.
Each original \(n\) contributes at \(m=n\) and \(m=2n\), with
coefficients \(b_n,-b_2b_n\) for \(\beta\) and
\(n^{1/5}b_n,-b_2n^{1/5}b_n\) for \(a\).
Thus this partial convolution has support \(m\le2N\le96\), although
all other cores remain in the full cost.

For the indices in (21), \(\log n<4\), because
\(48<(8/3)^4<e^4\). Hence \(\sigma>3/5\) gives
\[
b_n n^{-\sigma}<n^{-1/2}<\frac25,\qquad
n^{1/5}b_n n^{-\sigma}<n^{-3/10}<\frac35.
\tag{22}
\]
For the second final inequality use \(n\ge7\) and
\((5/3)^{10}<3^5=243<343=7^3\).
The first follows from \(7>25/4\). Also
\[
b_2\,2^{-\sigma}<2^{-1/2}<\frac34.
\]
Triangle applied **only to this variation budget** therefore gives
\[
\begin{split}
B_{\rm abs}&:=\sum_{\substack{m=p2^j\\p\in\mathcal P_*}}
                         |\beta_m|m^{-\sigma}
 <16\frac25\left(1+\frac34\right)=\frac{56}{5},\\
A_{\rm abs}&:=\sum_{\substack{m=p2^j\\p\in\mathcal P_*}}
                         |a_m|m^{-\sigma}
 <16\frac35\left(1+\frac34\right)=\frac{84}{5}.
\end{split}
\tag{23}
\]
Cancellation in a coefficient can only improve these upper bounds.
They include every convolution edge of these eight cores.
Moreover \(\log m<5\), since \(m\le96<(8/3)^5<e^5\).

Put \(k(g)=(1-g)/(1+g)\) and
\(\mathsf Q_p(x,u)=(1-g)p^{-\sigma}M_p(x,u)\), so
\(R_p=\|\mathsf Q_p\|_2\). Each \(m=p2^j\) harmonic of this real
matrix is
\[
m^{-\sigma}
\operatorname{diag}\bigl(k(g)(\beta_m+ga_m),\,\beta_m-ga_m\bigr)
\operatorname{Rot}(ju),
\quad
\operatorname{Rot}(v)=
\begin{pmatrix}\cos v&-\sin v\\\sin v&\cos v\end{pmatrix}.
\tag{24}
\]
On a fixed-\(N\) chart the coefficients \(\beta_m,a_m\) are constant
in \(x\), because \(t,y\) are fixed. Only \(\sigma,g\) vary.
Since
\[
|k'|\le2,\qquad
|(kg)'|=\left|\frac{1-2g-g^2}{(1+g)^2}\right|\le1,
\]
the norm of the \(g\)-derivative of (24) is at most
\[
m^{-\sigma}(2|\beta_m|+|a_m|).
\]
The norm of its \(\sigma\)-derivative is at most
\[
\log m\,m^{-\sigma}(|\beta_m|+g|a_m|).
\]
All these bounds hold at each fixed auxiliary \(u\); its rotation
matrix has norm one and is not differentiated.

Using (17), (20), (23) and \(g<3/5\), the sum of the matrix
derivative bounds is strictly less than
\[
\frac1x\left\{
\frac5{39}\left(\frac{56}{5}+\frac35\frac{84}{5}\right)
 +\frac1{10}\left(2\frac{56}{5}+\frac{84}{5}\right)\right\}
=\frac{6482}{975x}<\frac7x.
\tag{25}
\]
The operator norm need not be differentiable. Instead use
\[
\bigl|\|\mathsf Q_p(x,u)\|_2-\|\mathsf Q_p(a,u)\|_2\bigr|
 \le\|\mathsf Q_p(x,u)-\mathsf Q_p(a,u)\|_2
\]
and integrate the smooth matrix derivative. Uniformly in \(u\), for
\(a\le x\le a+19\) within one chart this proves
\[
\boxed{|C_*(x,u)-C_*(a,u)|\le7\,\frac{x-a}{a},\qquad
|g(x)-g(a)|\le\frac{x-a}{10a}.}
\tag{26}
\]
Both estimates are strict if \(x>a\); at \(x=a\) both are equality
zero. This necessary endpoint clarification of the request does not
weaken the target: the witness below lies strictly before \(a+19\),
and (14) already has a strict excess.

## 5. A physical phase revolution and its paid witness

The elementary identity
\[
\log2=2\int_0^{1/3}\frac{dr}{1-r^2}>\frac23
\]
and (17) show that \(u'=-\tau'\log2>0\) and
\[
u(a+19)-u(a)>
19\left(\frac12-\frac1{39\cdot14000}\right)\frac23
=\frac{19}{3}-\frac{19}{819000}>\frac{44}{7}>2\pi.
\tag{27}
\]
The penultimate inequality follows from
\(19/3-44/7=1/21>19/819000\).
Consequently there is a unique \(b<a+19\) with
\(u(b)=u(a)+2\pi\).

The finite continuous periodic function \(C_*(a,\cdot)\) attains
a maximum on \([u(a),u(a)+2\pi]\). That maximum is at least the
mean in (14). Strict monotonicity and continuity of \(u\) therefore
supply \(x_*\in[a,b]\) attaining a maximizing phase modulo \(2\pi\).
No strict maximum-versus-mean inequality is assumed. Put
\(d=x_*-a\), so \(0\le d<19\). By (14) and (26),
\[
\begin{split}
C_*(x_*,u(x_*))-(1-g(x_*))
&>\frac{1-g(a)}{20}-\frac{71d}{10a}\\
&>\frac1{50}-\frac{71\cdot19}{10\cdot14000}
 =\frac{1451}{140000}>\frac1{100}.
\end{split}
\tag{28}
\]
The uniform strict constants use \(1-g(a)>2/5\), \(a\ge x_0>14000\)
and \(d<19\), including the possible \(d=0\) case.
The full cost is at least (13), proving the first part of (2) and
\(K_{\rm act}(x_*)<-1/100\).
Only now use \(0<|E|<8\) to obtain
\[
\frac{K_{\rm act}(x_*)}{|E(x_*)|}
 <-\frac1{100|E(x_*)|}<-\frac1{800}.
\]
Subtracting the nonnegative \(D_\kappa,|c|,v\) proves all of (2).
The divisor in the defined lower allowance (10) has not been replaced
by an upper bound.

The independently acquired input is the quantitative coefficient
variation (26) together with the actual phase advance (27).
It converts a frozen auxiliary mean into existence at actual heights.
It neither asserts that independent core maximizing rotations are
physical nor controls their joint curve \(\eta_r(x)\); those rotations
are still relaxed in each \(R_r\). The sign of the exact direct
margin (11) remains undetermined.

## 6. Every fixed chart, its endpoints and the remaining consumer

Reuse the exact natural seams
\[
x_j=4\pi j^2-\pi/40,\qquad j=34,\ldots,48,
\]
and indices \(N=33,\ldots,48\). Define
\[
l_{33}=x_0,\quad l_N=x_N\ (N\ge34),\qquad
r_N=x_{N+1}\ (N\le47),\quad r_{48}=30000.
\tag{29}
\]
The reference at \(l_N\) is the new included chart. At \(r_N\) for
\(N\le47\) use the old chart's continuous one-sided limit.
The bounds \(25/8<\pi<22/7\) and \(x_0<14001\) show that all these
closed chart intervals have length greater than38:
\[
\begin{split}
r_{33}-l_{33}
 &>\frac{25}{8}(4\cdot34^2-1/40)-14001>38,\\
r_N-l_N&=4\pi(2N+1)>38\quad(34\le N\le47),\\
r_{48}-l_{48}&>30000-4(22/7)48^2=\frac{7248}{7}>38 .
\end{split}
\tag{30}
\]
The theorem applies to every \([a,a+19]\subseteq[l_N,r_N]\),
including each chart's first and last such interval. If \(a+19=r_N\)
is an excluded old-chart endpoint, the witness satisfies
\(x_*\le b<a+19\); it therefore uses an actual natural reference.
There is no pointwise sign assertion at a seam or at \(x_0\).
In particular \([x_0,x_0+19]\) lies in the first chart and contains a
failure witness, which suffices to prevent uniform use on all of (1).

No charts are glued in this proof. A fixed-reference transfer would
still retain Note14's signed jump
\(\Delta Q_{\rm val}=d_j-2J_jA_j(W)\) and
\(E_{\rm src,new}=E_{\rm src,old}-\Delta Q_{\rm val}\), or pay its
whole magnitude. Each old complete source enclosure holds by its
one-sided limit, and the new chart owns the seam. No cutoff-floor
derivative or unpaid transfer appears.

The larger consumer remains
\[
t=.1,\quad x\ge x_0,\quad .2\le y\le\sqrt{.8}.
\]
Its remaining two-dimensional finite strip, an effective infinite-tail
onset and paid overlap or common included join remain unacquired.
Initial verification through height7000 and the full intermediate
barrier for \(0\le t\le.1\) remain separate source-criterion inputs.
Earlier finite certificates and the retained-correction gain are
unchanged. No new zero coverage, Newman bound or measured runtime
advantage follows.

## 7. Collision screen and exact class excluded

Controls12 is applied to three separate premises: **S**, the literal
theta source and whole enclosure (3)–(7); **V**, the acquired finite
coefficient/phase-velocity estimates (15)–(27); and **M**, a strict
complete margin (12). The proof of failure uses no M assumption.
Passing a coarse part of V is possible for a changed source and does
not provide S or M.

| Control class | Failed or unprovided premise |
| --- | --- |
| Euler-factor translates | Their changed field and coefficients need their own S enclosure. Selected arithmetic relations or coarse velocities can survive; their included zeros defeat M under an honest enclosure. |
| Weighted-square, finite-source, finite-prime-orbit and finite canonical-score controls | Finite supports, heads or arithmetic tests do not give the complete S coefficients, reflection and remainder. Some V inputs may survive. Preserve the finite-source lack of an all-real heat anchor and each construction's event/location qualifications. |
| Reflected super-Gaussian, smooth-shape and positive-primitive controls | Their shape, reflection, Gram or primitive data do not supply S or all the actual coefficients used in V. Their own included zeros defeat M; no event on this unrelated fixed strip is asserted. |
| Atomic fixed-event and finite-profile threshold controls, including continuous extensions | Selected profiles do not supply full theta arithmetic/profile growth or eventual simplicity at threshold. Their included threshold events defeat M. |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet arithmetic in S fails. Keep the RH premise and escaping-height qualifier; a time-zero real double is not a witness on (1). |
| Fixed theta amplitude with a changed observation kernel | Changed readout requires its full prepared forcing; omitting it invalidates S. Raw compatibility or selected finite data do not provide M. These are not physical theta collisions. |
| Fractional finite-profile relaxation and static divisor surgery | Physical integer multiplicity or the common physical heat path is absent. Neither is a counterexample to the actual theta estimates proved here. |
| Reflection rigidity | Its full normalized conjunction identifies theta within its stated class, but gives no quantitative M. |

For any included zero of any honestly enclosed source,
\[
H_*(z_*)=0,\quad |H_*/B_*-q_*|\le v_*,\quad
\ell_*\le|q_*|
\quad\Longrightarrow\quad \ell_*-v_*\le0.
\tag{31}
\]
The exact generic check
\[
H_*=Q_*=(z-x_c)^2-2(t-1/4),\qquad B_*=1,\quad v_*=0
\]
satisfies \(H_t=-H_{zz}\) and has, at \(t=.1\), the zero
\(z=x_c+i\sqrt{3/10}\). Since \(1/25<3/10<4/5\), it lies in the
full final strip for \(x_c\ge x_0\). It fails M despite perfect
approximation. It supplies neither theta arithmetic S nor the full
source-specific V conjunction, and is not called a theta collision.

The negative theorem concerns exactly the fixed \(\{2,3,5\}\)
convolution, separate anchor, odd-core dyadic groups with independent
core rotations, actual common dyadic phase, and separate kappa,
correction and whole-source payments, on (1) and with the interval
quantifiers in (2). It does not exclude joint restrictions coupling
different \(\eta_r\), signed anchor/core or correction aggregation,
other products, other groups, or contour and heat arguments.

## 8. Bounded correction and disposition

The correction pass checked the carrier-log derivative and conjugation,
the count16 and every partial-convolution edge, the two matrix
derivatives and constants in (25), use of norm Lipschitz continuity,
strict phase advance, the possible \(x_*=a\) endpoint, the old-chart
right endpoint and the signed-divisor direction. The only clarification
of the request is the necessary equality at \(x=a\) in (26).
No mathematical target, domain, width, grouping or evidence standard
changed.

All six fixed analytical steps complete. The proof is paired with
concise [Section13](../manuscript/sections/13_actual_phase_recurrence.tex)
and the [execution return](../research-progress/handoffs/AGC-E18-r1-return.md).
The separate nonauthor assessment accepted the fixed proof and Section13;
[Review10](../reviews/10_AGC_ACTUAL_PHASE_ASSESSMENT_20261119.md) owns that status. Root owns shared navigation,
production, the sole register, summaries and public chat capture.

Root reconciled the status after the separate **E / Sol6.1 ultra**
assessment; the author return retains its earlier author-stage hash.
A later conceptual continuation must choose and acquire
information still discarded here, such as a specific joint core-phase
restriction or signed aggregate containing the anchor. No new B task,
phase scan or computational campaign is activated by this proof.
