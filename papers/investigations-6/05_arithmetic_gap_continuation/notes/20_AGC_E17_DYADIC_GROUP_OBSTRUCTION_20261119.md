# AGC-E17 r1: common dyadic phase envelope obstruction

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Execution-helper dispatch explicitly recorded
**gpt-6.1-sol / ultra**; independent serving-backend model and effort
attestation is unavailable. **Type E**, under the
[frozen E17 r1 request](../research-progress/handoffs/AGC-E17-r1-request.md),
following [B05 Note19](19_AGC_B05_PHASE_GROUP_DECISION_20261119.md).
One analytical proof pass and one bounded correction pass; no numerical
scan, phase evaluation, new rational-witness campaign or source change.

**Status: proved in-note; accepted within the frozen scope by
[Review09](../reviews/09_AGC_PHASE_GROUP_ASSESSMENT_20261119.md).** Root reconciled this status after the
proof-author return; the mathematical text is unchanged. The
odd-core grouping retains one common dyadic phase across all groups before
taking its full-circle supremum. Nevertheless its signed arithmetic lower
function and complete allowance satisfy

\[
\boxed{\ell_{\rm dyad}<-\frac1{400},\qquad
       m_{\rm dyad}<-\frac1{400}}
\tag{1}
\]

throughout the closed segment

\[
\mathcal F_0:\quad t=\frac1{10},\quad y=\frac15,\quad
x_0=14000+\sqrt{24/25}\le x\le30000.
\tag{2}
\]

The theorem concerns the fixed `{2,3,5}` multiplier, anchor one, odd-core
dyadic groups, independent core rotations, a single common full-circle
dyadic-phase envelope, and separate kappa/correction/source payments. It
does not upper-bound the actual reference or field magnitude, exhibit a
zero, determine the exact direct margin, or exclude actual-height phase
estimates or all arithmetic methods.

The [sole register](../research-progress/01_AGC_RESEARCH_PROGRESS_20261119.md)
owns status. The [result index](../../../../result-summaries/README.md),
[pattern index](../../../../avoid/README.md),
[Cluster18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
[Controls12](../../../../result-summaries/12_collision_controls_and_screening.md)
and patterns [01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[11](../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md)
and [12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
govern interpretation. Classification: a quantitative failure theorem for
one stated information reduction, judged by (1), rather than a new
RH-equivalent criterion or desired positivity rewritten as a premise.

Inputs are Notes14 and17–19, Review08 and manuscript Section11. All six
prerequisite SHA-256 identities in the issued request match, and the
request's own identity is
`45ced08998a51742fc817f649def81bc7a9f3783cbd52b4c4752c9e6203a762f`.
The source interface and eight-prime witness are reused from accepted
[Note17](17_AGC_E16_THREE_PRIME_ELLIPSE_OBSTRUCTION_20261119.md) and
[Review08](../reviews/08_AGC_ARITHMETIC_FLOOR_ASSESSMENT_20261119.md).
No new imported source theorem, source version or parameter-specific
published numerical bound is needed or checked in this execution.

## 1. Unchanged retained reference and complete payments

Keep the literal theta field and Note17's exact normalization:

\[
s_0=\frac{1+y-ix}{2},\quad s_1=\frac{1-y+ix}{2},\quad
\alpha(w)=\frac1{2w}+\frac1{w-1}+\frac12\operatorname{Log}\frac w{2\pi},
\quad s=s_0+\frac{\alpha(s_0)}{20}=\sigma+i\tau,
\]
\[
\mathcal B=\mathfrak M_t(s_0),\quad
\gamma=\frac{\mathfrak M_t(s_1)}{\mathfrak M_t(s_0)},\quad
g=|\gamma|,\quad
\kappa=\frac{\alpha(s_1)-\overline{\alpha(s_0)}}{20},\quad
b_n=e^{\log^2n/40},\quad
N=\left\lfloor\sqrt{\frac{x}{4\pi}+\frac1{160}}\right\rfloor.
\tag{3}
\]

Here `M_t`, its nonzero carrier, branches and all source constants are
unchanged. With

\[
S=\sum_{n\le N}b_n n^{-s},\qquad
T=\sum_{n\le N}b_n n^{y-s},\qquad
f=\frac{P_N}{\mathcal B}
 =S+\gamma\sum_{n\le N}b_n n^{y-\overline s-\kappa},
\]
\[
W=x/2+\pi/80,\quad
J_N=(-1)^{N+1}\frac{\sqrt\pi}{4}e^{-\pi z/8-\pi^2/640},\quad
c=\frac{J_NA_N(W)}{\mathcal B},\qquad
q=\frac{Q_{\rm val,N}}{\mathcal B}=f-c,
\tag{4}
\]

the retained value correction is exactly Note14's `A_N`. This is its
pointwise value formula, with no spatial differentiation assertion.

For explicit accounting put `T_0=x/2`, `sigma_±=(1±y)/2`,
`w_±=sigma_±+iT_0`, `a_RS=sqrt(W/(2pi))`, and retain

\[
\epsilon_n(t,w)=\exp\left(
\frac{(t^2/8)|\alpha(w)-\log n|^2+t/4+1/6}{T_0-3.33}\right)-1,
\]
\[
\delta_\sigma=\left(\frac{0.397\,9^\sigma}{a_{\rm RS}-0.865}
                     +\frac5{3(T_0-6)}\right)e^{3.49/(T_0-4)},
\quad L_N=\frac{|J_N|}{2}\sqrt W\sqrt{W^2+1},
\]
\[
V_{\rm val,N}=\sum_{n=1}^{N}\sum_{\nu\in\{-,+\}}
 |p_n(t,w_\nu)|\epsilon_n(t,w_\nu)
 +L_N(\delta_{\sigma_-}+\delta_{\sigma_+}),\quad
v=\frac{V_{\rm val,N}}{|\mathcal B|}.
\tag{5}
\]

Thus both entire finite-term error sums and both whole retained delta
payments remain. The accepted retained source enclosure is

\[
\left|H_t/\mathcal B-q\right|\le v.
\tag{6}
\]

No omitted-correction `+L_N` payment is introduced and no part of (5) is
removed. The separate arithmetic replacement, with `F=S+gamma conjugate(T)`,
still costs

\[
|f-F|\le D_\kappa,\qquad
D_\kappa=g\sum_{n\le N}b_n n^{y-\sigma}
                    \bigl(e^{|\kappa|\log n}-1\bigr)\ge0.
\tag{7}
\]

Paying `|c|` below is a restriction of the arithmetic estimator, not a
change of q or its physical source budget.

## 2. Exact convolution and odd-core phase decomposition

Retain exactly

\[
E=\prod_{p\in\{2,3,5\}}(1-b_p p^{-s})
  =\sum_{d\mid30}\lambda_d d^{-s},\qquad
\lambda_d=\prod_{p\mid d}(-b_p),\quad\lambda_1=1,
\]
\[
\beta_m=\sum_{\substack{d\mid(m,30)\\m/d\le N}}\lambda_d b_{m/d},
\qquad
a_m=\sum_{\substack{d\mid(m,30)\\m/d\le N}}
             \lambda_d(m/d)^y b_{m/d},\quad 1\le m\le30N.
\tag{8}
\]

These real coefficients have `beta_1=a_1=1`. Exact finite multiplication
gives `U=ES=sum beta_m m^(-s)` and `V=ET=sum a_m m^(-s)`, including
every cutoff edge with `m>N`. Only the exponent and its phase are
multiplicative; `b_(dn)=b_d b_n` is not assumed.

Where `E!=0`, put

\[
\rho=\gamma E/\overline E=g e^{i\theta}.
\quad\text{Then}\quad EF=U+\rho\overline V.
\tag{9}
\]

Let `R_N` be the odd positive integers at most `30N` and define

\[
I_1=\{j\ge1:2^j\le30N\},\qquad
I_r=\{j\ge0:r2^j\le30N\}\quad(r\ge3\text{ odd}),
\]
\[
B_r(u)=\sum_{j\in I_r}\beta_{r2^j}2^{-j\sigma}e^{iju},\qquad
A_r(u)=\sum_{j\in I_r}a_{r2^j}2^{-j\sigma}e^{iju},
\]
\[
G_r(\eta,u)=r^{-\sigma}
       \{e^{i\eta}B_r(u)+g e^{-i\eta}\overline{A_r(u)}\}.
\tag{10}
\]

Every integer `m>=2` has a unique representation `r2^j` included here.
At the **actual** observation set

\[
u(x)=-\tau\log2,\qquad
\eta_r(x)=-\tau\log r-\theta/2.
\]

Substitution into (10) reproduces every term of the rotated (9), so

\[
e^{-i\theta/2}EF
 =Z_0+\sum_{r\in R_N}G_r(\eta_r(x),u(x)),\qquad
Z_0=e^{-i\theta/2}+g e^{i\theta/2}.
\tag{11}
\]

The missing `r=1,j=0` term is precisely the separate anchor `Z_0`.
The common dyadic phase and all within-core phase relations are exact.

## 3. Exact group radii and the common-phase allowance

For `0<=g<1` use Note17's norm

\[
\|w\|_g^2=\left(\frac{\Re w}{1+g}\right)^2
          +\left(\frac{\Im w}{1-g}\right)^2,
\qquad |w|\ge(1-g)\|w\|_g.
\tag{12}
\]

The anchor in (11) has norm one. Define all auxiliary phase suprema on
`[0,2pi]`, with `N,sigma,g,beta,a` frozen at this actual observation:

\[
R_r(u)=(1-g)\sup_\eta\|G_r(\eta,u)\|_g,\qquad
C_{\rm dyad}=\sup_u\sum_{r\in R_N}R_r(u),\qquad
C_{\rm sep}=\sum_{r\in R_N}\sup_uR_r(u).
\tag{13}
\]

These are maxima of continuous finite expressions over compact circles.
They do not recompute coefficients at hypothetical heights. Writing
`B_r=B_R+iB_I`, `A_r=A_R+iA_I`, direct expansion in `cos eta,sin eta`
gives

\[
M_r(u)=\begin{pmatrix}
\dfrac{B_R+gA_R}{1+g}&-\dfrac{B_I+gA_I}{1+g}\\[4pt]
\dfrac{B_I-gA_I}{1-g}&\dfrac{B_R-gA_R}{1-g}
\end{pmatrix},\qquad
\boxed{R_r(u)=(1-g)r^{-\sigma}\|M_r(u)\|_2.}
\tag{14}
\]

Indeed the real and imaginary coordinates of `G_r` after the diagonal
scaling (12) are `r^(-sigma) M_r(u)(cos eta,sin eta)^T`. The latter
unit vectors trace the whole unit circle, proving the real operator-norm
formula exactly.

Apply reverse triangle to (11) and then (13):

\[
|EF|\ge(1-g)\|e^{-i\theta/2}EF\|_g
\ge1-g-\sum_rR_r(u(x))\ge1-g-C_{\rm dyad}=:K_{\rm dyad}.
\tag{15}
\]

The inequalities hold even if their right sides are negative. Paying
(7), dividing by the **exact positive** `|E|`, and paying the retained
correction gives

\[
\boxed{\ell_{\rm dyad}=\frac{K_{\rm dyad}}{|E|}
                   -D_\kappa-|c|\le|q|,\qquad
       m_{\rm dyad}=\ell_{\rm dyad}-v\le|H_t/\mathcal B|.}
\tag{16}
\]

No upper estimate for `|E|` is substituted into this signed definition.

For comparison let

\[
h_m=\max\left\{|\beta_m-ga_m|,
               \frac{1-g}{1+g}|\beta_m+ga_m|\right\},\qquad
C_{\rm ind}=\sum_{m=2}^{30N}h_m m^{-\sigma}.
\]

The contribution to `M_r(u)` at a single `j` is `2^(-j sigma)`
times the diagonal matrix with entries
`(beta_(r2^j)+g a_(r2^j))/(1+g)` and
`(beta_(r2^j)-g a_(r2^j))/(1-g)`, followed by rotation through `ju`.
Its operator norm is `2^(-j sigma)h_(r2^j)/(1-g)`. The matrix triangle
inequality therefore proves, for every u,

\[
R_r(u)\le\sum_{j\in I_r}h_{r2^j}(r2^j)^{-\sigma}.
\]

The unique dyadic partition and the elementary supremum inequality give

\[
\boxed{C_{\rm dyad}\le C_{\rm sep}\le C_{\rm ind},\qquad
       m_E\le m_{\rm dyad}\le m_{\rm dir}:=|f-c|-v.}
\tag{17}
\]

The first comparison improves E16's reduction weakly; strict improvement
is not asserted. The last follows directly from (16). Exact direct
evaluation receives all these polynomials, the actual phases, gamma,
kappa, correction and complete source error, and may use the same
grouping. No runtime or all-implementation ordering is proved.

## 4. Independent Fourier mean and the quantitative failure

Write `mean_u=(1/(2pi)) integral_0^(2pi) du`. For odd `r>=3`, all
positive-frequency exponentials in (10) have mean zero and its constant
coefficients are the real numbers `beta_r,a_r`. Thus

\[
\operatorname{mean}_u M_r(u)
=\operatorname{diag}\left(
\frac{\beta_r+ga_r}{1+g},\frac{\beta_r-ga_r}{1-g}\right).
\tag{18}
\]

The operator norm is convex: for any unit vector e, the integral triangle
inequality gives
`|(mean M)e|<=mean|Me|<=mean||M||_2`; taking the supremum over e proves
`||mean M||_2<=mean||M||_2`. Combining this with (14) and (18),

\[
\operatorname{mean}_u R_r(u)
\ge(1-g)r^{-\sigma}\|\operatorname{mean}_u M_r(u)\|_2
=h_r r^{-\sigma}.
\tag{19}
\]

For `r=1` the mean matrix is zero because `j=0` was removed; its radius
cost remains nonnegative. A supremum dominates the mean of the same
finite sum, so

\[
\boxed{C_{\rm dyad}\ge\operatorname{mean}_u\sum_rR_r(u)
       \ge\sum_{\substack{r\ge3\ {
m odd}\\r\le30N}}
                         h_r r^{-\sigma}.}
\tag{20}
\]

This finite Fourier calculation and norm inequality are independent
inputs about the relaxed envelope, with no physical nonvanishing premise.
For the particular signed allowance (16), positivity is equivalent to
the explicit fully paid threshold

\[
C_{\rm dyad}<1-g-|E|(D_\kappa+|c|+v)\le1-g.
\tag{21}
\]

We do not assume (21). In fact the mean argument prevents it here.

Reuse Note17/Review08's accepted uniform constants on (2):

\[
N\ge33,\qquad \frac35<\sigma<\frac45,\qquad
0<g<\frac35,\qquad0<|E|<8,
\]
\[
\mathcal P_*:=\{7,11,13,17,19,23,29,31\},\qquad
\sum_{p\in\mathcal P_*}b_p p^{-4/5}>\frac{21}{20}.
\tag{22}
\]

The last strict inequality is the existing exact rational witness in
[Record08](../numerics/08_AGC_E16_RATIONAL_WITNESS_20261119.json), not a
new computation. For every such prime the sole divisor of30 is1 and
`p<=N`, hence (8) gives

\[
\beta_p=b_p,\qquad a_p=p^{1/5}b_p\ge b_p,\qquad
h_p\ge\frac{1-g}{1+g}(b_p+gp^{1/5}b_p)\ge(1-g)b_p.
\]

Each p is its own odd core. Its mean cost cannot be eliminated by the
positive dyadic harmonics, regardless of their signs. From (20)–(22),

\[
C_{\rm dyad}\ge\sum_{p\in\mathcal P_*}h_p p^{-\sigma}
>(1-g)\frac{21}{20},\qquad
K_{\rm dyad}<-\frac{1-g}{20}<-\frac1{50}.
\tag{23}
\]

All other core costs are nonnegative. Ignoring them weakens this upper
bound on the defined lower-allowance numerator; it does not discard a
term from a lower bound on the physical sum. Only now use `|E|<8` to
upper-bound the already-defined negative quotient:

\[
\frac{K_{\rm dyad}}{|E|}<-\frac1{50|E|}<-\frac1{400}.
\]

The other three payments are nonnegative, proving (1) on all of (2).
The clipped lower function `max(0,ell_dyad)` is zero there and cannot
exceed `v>=0` strictly. Neither `|q|` nor `|H_t/B|` is upper-bounded
by this negative number.

The actual-phase cost

\[
C_{\rm act}(x)=\sum_rR_r(u(x))\le C_{\rm dyad}
\]

gives a separately valid allowance by replacing `C_dyad` in (15)–(16).
That allowance is at least `m_dyad` and may succeed; its sign is not
decided by (19)–(23). A lower bound on a circle mean or on its supremum
is not a lower bound on the value at `u(x)`. No simultaneous worst
core phases or common maximizing u is asserted to occur at an actual
height. Independent core rotations and the full circle are the stated
relaxations, despite the common u retained in (13).

## 5. Exact cells, seam transfers and unacquired coverage

The natural seam at this time is

\[
x_j=4\pi j^2-\pi/40,\qquad
N=j-1\ \hbox{on the old side},\quad N=j\ \hbox{at the new seam}.
\tag{24}
\]

The permissible rational bounds `25/8<pi<22/7` give

\[
x_{33}<4(22/7)33^2<14000<x_0<14001
 <(25/8)(4\cdot34^2-1/40)<x_{34},
\]
\[
x_{48}<4(22/7)48^2<30000
 <(25/8)(4\cdot49^2-1/40)<x_{49}.
\tag{25}
\]

Consequently exactly `N=33,...,48` occur on (2), with internal seams
`j=34,...,48`. Apply the finite convolution, dyadic partition and proof
separately to each half-open cell `[x_N,x_(N+1))` intersected with
`[x0,30000]`; the final included endpoint30000 has `N=48`. At each
internal seam reconstruct (8)–(13) using the old index `j-1` and new
index j separately. Both retain all eight primes. The old complete
source enclosure holds by its continuous one-sided limit from Note14;
the new index owns the included endpoint. Thus (1) holds for both
one-sided references. There is no floor differentiation or asserted
global holomorphy of the naturally selected value reference.

A fixed-reference transfer still uses Note14's signed jump

\[
\Delta Q_{\rm val}=d_j-2J_jA_j(W),\qquad
d_j=p_j(t,s_+(z))+p_j(t,s_-(z)),
\]

and `E_src,new=E_src,old-Delta Q_val`. Retain that difference exactly
or pay its full magnitude, bounded by `V_val,old+V_val,new`. Every
successive seam is payable. This pointwise proof invokes no unpaid
transfer.

The eventual consumer remains `t=.1,x>=x0,.2<=y<=sqrt(.8)`. The rest
of its two-dimensional finite strip and an effective infinite-tail
onset with paid overlap or common included join remain **unacquired**.
Moving a join cannot alter (1) at the included x0; a hybrid using a
different successful estimator needs that additional proved input.
Classical eventual two-carrier coverage is inherited, not newly acquired.
The initial zeta verification through height7000 and full intermediate
barrier for `0<=t<=.1` remain separate source-criterion obligations.
No new coverage or Newman bound follows; the earlier finite-circle
pair certificate and retained-value gain are unchanged.

## 6. Collision screen and precise scope

Apply Controls12 separately to **S**, the complete literal theta
source/enclosure (3)–(6); **P**, its actual arithmetic coefficients and
phase identities (8)–(11); and **M**, a strict complete margin such as
(21). Generic dyadic identities alone do not identify the theta source.

| Control class | Named failed or unprovided premise |
| --- | --- |
| Euler-factor translates | Changed coefficients and shifted fields require their own S enclosure; selected multiplicative P identities may survive. With an honest enclosure, an included control zero defeats M. |
| Weighted-square and finite-source controls | Full theta weights/reflection/remainder in S are absent; support or some P identities do not restore them. The documented finite-source class has no all-real heat anchor, and its event is not a finite Newman threshold. |
| Finite-prime orbit and finite canonical-score controls | Selected P identities, finite coefficient heads or measurements can survive, but not the complete S arithmetic and remainder. Preserve their construction-dependent event and location qualifiers; no common fixed compact event is assigned. |
| Reflected super-Gaussian, smooth shape and positive-primitive controls | Shape, reflection, Gram or primitive positivity does not supply S or the actual coefficients in P. Their own included zeros defeat M, with no claim about this unrelated fixed strip. |
| Atomic fixed-event and finite-profile threshold controls, including continuous extensions | Selected finite profiles do not supply full theta arithmetic/profile growth or eventual simplicity at threshold. Their included threshold events defeat M. |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet-series arithmetic in S fails. Keep the RH premise and escaping-height scope; a time-zero real double is not an event on (2). |
| Fixed theta amplitude with changed observation kernel | A changed readout needs its prepared forcing; omitting it invalidates S. These observations are not physical theta collision examples. |
| Fractional finite-profile relaxation; static divisor surgery | Physical integer multiplicity or a common physical heat path, respectively, is absent. Neither provides a counterexample to an actual theta phase estimate. |
| Reflection rigidity | Its full normalized conjunction identifies theta within its stated class, without giving quantitative M. |

A changed-source premise failing is not a claim that every coarse
inequality fails. Quantitatively any genuine included zero satisfies

\[
H_*(z_*)=0,\quad |H_*/B_*-q_*|\le v_*,\quad
\ell_*\le|q_*|\quad\Longrightarrow\quad\ell_*-v_*\le0.
\tag{26}
\]

The exact generic check `H_*=Q_*=(z-x_c)^2-2(t-1/4)`, `B_*=1,v_*=0`
satisfies `H_t=-H_zz` and at `t=.1` has the zero
`z=x_c+i sqrt(3/10)`. Since `1/25<3/10<4/5`, this is in the actual
full strip for `x_c>=x0`. It fails M despite perfect approximation;
it does not have S or the theta arithmetic premise P.

The negative theorem excludes exactly the fixed multiplier/anchor,
odd-core dyadic grouping, independently relaxed core rotations, one
common **full-circle** dyadic phase, and the separate payments tested
here. It does not exclude actual `u(x)`, short height arcs, correlations
among odd cores or with the anchor, signed correction coupling, larger
products, other grouping geometries, or contour/heat estimates.

## 7. Correction pass and disposition

The single bounded correction pass re-expanded the cosine/sine columns
in (14), checked the missing core-one constant and anchor norm, proved
the operator-norm triangle and mean steps directly, and checked the
negative-denominator direction without replacing its definition. It
also checked the actual-phase distinction, both complete source sums,
both deltas, the full kappa payment, the exact seam formula and every
endpoint in (25). No mathematical target or contract change was needed.

All six analytical proof targets pass. No new computation, coefficient
sample, imported numerical bound or certificate supports this proof.
The concise [Section12](../manuscript/sections/12_dyadic_group_obstruction.tex)
inherits Section11's accepted source estimates and eight-prime witness,
and proves the new grouped norm/mean argument. The separate nonauthor assessment accepts the proof within this scope;
its final integration check and root production receipt record manuscript
milestone status. Root owns
production, the sole register, shared navigation, history and summaries.

A later **B06 / Astra ultra** decision would need a specific independent
quantitative input escaping this envelope: either enclose the actual
joint curve `(u(x),eta_r(x))` together with changing `sigma,g,beta,a`
and every cutoff, or retain a signed aggregate coupling the anchor and
chosen cores, plus the correction if claimed. Its independently
checkable bound must cross the full paid threshold, with the exact
direct comparator given the same information. Naming a phase or favorable
correlation acquires neither input. This return chooses no new grouping,
phase campaign or numerical packet; root's continuation owns the B06
specification.
