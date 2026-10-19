# Paid profile trace versus direct arithmetic tails: S07-T2

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual model **gpt-6.1-sol (Codex)**, actual
reasoning effort **ultra**, verified from this turn's metadata. Analytic
bounded comparison with outward interval constants and separate delegated
same-model review; no independent specialist human review.

## Result and precise scope

**S07-T2 is Complete as a bounded analytic failed-estimate comparison.**
The selected N=2 whole-profile observation rule from [Note 03][space] has
an explicit, finite, uniform first-jet error payment. However even its
intrinsic assigned allowance, before any overestimate of its norm, exceeds
an available direct arithmetic-tail allowance by factors **>1618** for
value and **>34152** for first derivative on the whole pilot B. No
refinement of the norm computation can reverse this comparison for this
particular rule and residual.

The source of loss is specific: the automorphic smooth cutoff has
nonzero residual mass between lattice points, while physical sampling
sees only integers. The bulk profile norm pays that mass. This closes
the **N=2, whole-profile sqrt(20)X trace followed by Cauchy** attempt, not
finite-kernel projection, a different cutoff, observation-adapted norms,
signed integration, mixed adjoints or every theta-geometric estimate.
There is no lower bound here on the actual approximation error.

Stop this selected attempt. **S07-T3 remains Waiting**, because T2 has
not supplied a useful error improvement or signed input. T4 remains
Deferred and no extension is activated. No new physical sign, matched
cost gain, region or Newman bound is claimed.

Read the repository [result summaries][summaries] and [patterns to
avoid][avoid], especially [collision controls][controls], [geometric
results][geometry], [target reformulations][a01], [scope][a07], [premature
numerics][a10] and [separate-bound losses][a12]. This is a quantified
comparison of an estimating rule, not another global nonvanishing
criterion. The [overview][plan] and [tracker][tracker] retain its task ID.

## Frozen comparison contract and complete object

Retain precisely

\[
 \Omega=[-1/4,1/4]_p\times[1,4]_q\times T^2,\quad
 B=[1/100,1/5]_t\times[999,1001]_x,\quad U=\log4/4.
\]

Use Note 03's metric, unitary gauge, profile transform Z and smooth cutoff
chi2 without retuning. Write

\[
 a_q(y)=q^{1/4}(\pi^2q^2y^4-\tfrac32\pi qy^2)e^{-\pi qy^2},\quad
 \rho=1-\chi_2,\quad g(p,q,y)=e^{\pi p^2q}a_q(y)\rho(y).
\]

On the physical path, the exact residual is
\(R_2|_\gamma=2\sum_{n\ge3}a_q(n)\). All these terms are positive
for q>=1. There is no extra factor between the full integer sum and Phi.
The shared **global analytic approximant** is

\[
 \widehat H_2(t,x)=\int_0^\infty e^{tu^2}
       2\sum_{n=1}^2a_{e^{4u}}(n)\cos(xu)\,du. \tag{1}
\]

In particular the retained n=1,2 integrals beyond q=4 are part of (1).
They are not silently omitted. Only n>=3 is paid in the common outside-
tube error below. Both routes compare the same function and its x
derivative with H,Hx, in physical units. The primary metric is the
complete componentwise first-jet approximation allowance.

No numerical acquisition of (1) or signed consumer was performed. For
any subsequent common numerical approximation to (1), let eps_j>=0 be
its complete acquisition error, including quadrature, rounding and
whole-cell propagation. The comparison below holds for every such common
pair. Thus this losing analytic branch can be decided without acquiring
an expensive oscillatory approximant. No timing or cost superiority is
claimed, and no numerical lower margin is reported.

## A fully paid, uniform whole-profile upper estimate

Keep Note 03's norms exactly:

\[
 Y(f)=\int_{\mathbb R}(1+y^2)(|f|^2+|f_y|^2)dy,\quad
 X(f)^2=\int_1^4\frac{dq}{4q}\int_{-1/4}^{1/4}
                         [4Y(f)+Y(f_p)]dp. \tag{2}
\]

The selected bounded-tube payments are

\[
 G_j(t,x)=\sqrt{20}\,X(g)C_j(t,x),\quad
 C_j=\|e^{tu^2}\partial_x^j\cos(xu)\|_{L^2([0,U],du)},\quad j=0,1.
 \tag{3}
\]

The complete residual is used, not just its high-level projection.
Its p derivative and the mixed derivative are
\(g_p=2\pi pqg\), \(g_{py}=2\pi pqg_y\); thus the adapted base metric
factor and derivative are paid.

The actual cutoff satisfies **|rho'|<=2**. To prove it, let
v=|y|-2 in (0,1), d=2v-1 and z=2d/(1-d^2). Then

\[
 \rho'=\frac{2(1+d^2)}{(1-d^2)^2\cosh^2z}\le2,
\]

where the formula is for increasing |y|. Indeed cosh^2z>=1+z^2 gives
the upper bound 2/(1+d^2). Outside the annulus the derivative is zero.
The smooth endpoint limits are retained. Consequently

\[
 |g|^2+|g_y|^2\le e^{2\pi p^2q}
             (9a_q^2+2(a_q)_y^2)\,1_{|y|\ge2}. \tag{4}
\]

Here \((a_q)_y=q^{1/4}(-2\pi^3q^3y^5+7\pi^2q^2y^3-3\pi qy)
 e^{-\pi qy^2}\). On y>=2,q>=1 its magnitude is bounded by
\(2\pi^3q^{13/4}y^5e^{-\pi qy^2}\), while
\(a_q\le\pi^2q^{9/4}y^4e^{-\pi qy^2}\).
The q powers in their squares times exp(-2 pi q y^2) decrease for q>=1.

Set \(M_k=\int_2^\infty y^ke^{-2\pi y^2}dy\). Use an upper bound for
M0 and the positive recurrence

\[
 M_0\le\frac{e^{-8\pi}}{8\pi},\qquad
 M_k=\frac{2^{k-1}e^{-8\pi}}{4\pi}
                  +\frac{k-1}{4\pi}M_{k-2},\quad k\ge2\text{ even}.
 \tag{5}
\]

The equality is for the exact moments; substituting the M0 upper bound
propagates upper bounds. Put

\[
 J_* =2\{9\pi^4(M_8+M_{10})+8\pi^6(M_{10}+M_{12})\}.
\]

Integrating p before taking the base maximum gives

\[
 X(g)^2\le X_+^2:=e^{\pi/2}(2+2\pi^2/3)U J_* . \tag{6}
\]

For example the intermediate p factor is
\(e^{\pi q/8}(2+\pi^2q^2/24)\), since integral p^2 dp=1/96.
Thus the crude but complete uniform bounds are

\[
 X(g)<0.026484,\quad
 G_0<0.071421,\quad G_1<0.014291, \tag{7}
\]

using \(C_0\le e^{U^2/5}\sqrt U\),
\(C_1\le e^{U^2/5}\sqrt{U^3/3}\).
These upper bounds intentionally need no mesh or numerical quadrature.
Their coarseness is not the reason for the stop: the next independent
lower bound applies to the exact norm used by (3).

No Green identity is used in (2)-(7), so no boundary current has been
dropped. No Jacobi-residual or higher B derivative is invoked, so no
unpaid chi'' or higher cutoff derivative is hidden. Those costs would
have to be added if such an operator were subsequently selected.

## An unavoidable floor for this assigned allowance

On q in [1,17/16], |y| in [9/4,5/2], all p, one has
\(\rho\ge(1+e^{8/3})^{-1}\) and
\(a_q(y)\ge a_{17/16}(5/2)\). The latter follows by differentiating
q^{1/4}(w^2-3w/2)e^{-w}, w=pi q y^2: both q and |y| derivatives are
negative in this rectangle (already for w>=4 pi). Discarding positive
derivative contributions in X gives

\[
 X(g)^2\ge X_-^2:=\frac{97}{64}\log(17/16)
 \left\{\frac{a_{17/16}(5/2)}{1+e^{8/3}}\right\}^2. \tag{8}
\]

The coefficient retains both y intervals, the whole p width, weight
1+y^2>=97/16, and the physical dq/(4q) measure. In particular
X(g)>7.02927e-9.

The oscillatory weights cannot eliminate this norm payment. Uniformly
on B, t>=0 and elementary cosine/sine integration imply

\[
 C_0^2\ge c_0^2:=U/2-1/(4\cdot999),
\]
\[
 C_1^2\ge c_1^2:=U^3/6-U^2/(4\cdot999)
       -U/(4\cdot999^2)-1/(8\cdot999^3)>0. \tag{9}
\]

Therefore the **assigned Cauchy allowances** in (3), even evaluated with
the exact X and exact weight norms, satisfy on every point of B

\[
 G_0>1.30765\,10^{-8},\qquad G_1>2.61274\,10^{-9}. \tag{10}
\]

These are not lower bounds on the actual signed errors H-Hhat2 or their
absolute values. A smooth profile supported strictly between consecutive
integers can even have zero physical sampling and positive X. The present
annular block identifies precisely the information the chosen norm loses.

## Direct arithmetic allowance, including the outside tube

Use the same source and cutoff, without a bulk norm. For q=e^{4u}>=1,
\((\log q)^2\le q\), \(u\le(q-1)/4\), and
\(e^{tu^2}\le e^{q/80}\) on B. The first inequality follows by maximizing
(log q)^2/q; its maximum 4/e^2 is less than one.
After physical measure conversion and dropping only the negative
source-polynomial term, the two omitted-mode integrands are bounded by

\[
 \frac{\pi^2}{2}n^4 q^2 e^{-\lambda_nq},\qquad
 \frac{\pi^2}{8}n^4 q^2(q-1)e^{-\lambda_nq},\quad
 \lambda_n=\pi n^2-1/80. \tag{11}
\]

The factor 2 for the two integer signs and dq/(4q) are included.
For n>=3 consecutive terms, including integration, have ratio at most
\((4/3)^4e^{-7\pi Q}\) on q>=Q. Write

\[
 \lambda=9\pi-1/80,\quad r=(4/3)^4e^{-7\pi},\quad
 r_4=(4/3)^4e^{-28\pi},
\]
\[
 J_2(Q)=e^{-\lambda Q}(Q^2/\lambda+2Q/\lambda^2+2/\lambda^3),
\]
\[
 J_\Delta(Q)=e^{-\lambda Q}\{(Q^3-Q^2)/\lambda
 +(3Q^2-2Q)/\lambda^2+(6Q-2)/\lambda^3+6/\lambda^4\}.
 \tag{12}
\]

These are the exact integrals of q^2 exp(-lambda q) and
q^2(q-1) exp(-lambda q) over [Q,infinity). The direct tube allowances are

\[
 D_0=\frac{81\pi^2}{2}\frac{J_2(1)-J_2(4)}{1-r},\quad
 D_1=\frac{81\pi^2}{8}\frac{J_\Delta(1)-J_\Delta(4)}{1-r}. \tag{13}
\]

Both methods use the identical outside-tube residual payments

\[
 T_0=\frac{81\pi^2}{2}\frac{J_2(4)}{1-r_4},\quad
 T_1=\frac{81\pi^2}{8}\frac{J_\Delta(4)}{1-r_4}. \tag{14}
\]

Only n>=3 is in (14); the retained n=1,2 source beyond q=4 remains in
(1). This is the complete half-line omission, with all positive-source
and mode tails bounded. No source endpoint or spectral derivative
commutator is discarded.

## Certified ledger and stopping decision

[192/256-bit outward interval records][record] give:

| Physical component | Direct tube allowance D_j | Shared outside residual T_j | Intrinsic geometric allowance G_j has floor | Published geometric tube upper bound |
| --- | ---: | ---: | ---: | ---: |
| Value | <8.07803e-12 | <1.84725e-47 | >1.30765e-8 | <0.071421 |
| First x derivative | <7.65021e-14 | <1.40207e-47 | >2.61274e-9 | <0.014291 |

Even G0/(D0+T0)>1618 and G1/(D1+T1)>34152. These compare approximation
allowances before arbitrary common acquisition costs; adding a large
common cost may make the total ratios close to one. Componentwise
ordering nevertheless persists for every eps_j>=0:

\[
 E_j^{direct}=\epsilon_j+D_j+T_j
       <\epsilon_j+G_j+T_j=E_j^{profile}. \tag{15}
\]

Replacing G_j by the published upper bound also loses. The primary
theorem is (15), not that either error estimate is close to actual error.
The direct absolute-tail bound is not claimed to be the strongest existing
spectral consumer. It is already enough to defeat this selected rule;
a sharper comparator cannot rescue the losing rule.

For physical normalization, a common fixed
\(G_c=1000^{7/4}e^{-125\pi}>0\) rescales every allowance in (15) equally.
The direct value allowance is already of order 10^154 in these units;
this raw N=2 source-tail comparison is not a competitive approximation at
x about 1000. No physical exclusion is inferred. If returning instead
to Q=H/A and its phase-scaled first jet, retain the common positive map

\[
 (e_0,e_1)\longmapsto |A|^{-1}
   \left(e_0,\frac{e_1+|b|e_0}{|\omega|}\right),
 \quad b=(\log A)_x,\quad \omega=\theta_x\ne0.
\]

Its monotonicity preserves the componentwise loss; it does not create a
new allowance. There is no unpriced change of normalizer.

This is a completed bounded failed-estimate branch. The finite upper
estimate is proved and paid; the independent annular lower floor shows
why tightening its norm enclosures or quadrature cannot meet the gate.
Stop without a numerical consumer sweep. A different norm or signed
functional would require a new explicit contract and its own comparison.

## Controls and review

The [fresh source-specific control replay][control-record] rejects the
five inherited event boxes at their unchanged strict physical interfaces,
and rejects the separate Euler negative-Laguerre witness at its signed
interface. This is regression screening, not validation of a new strict
acceptance rule: (2)-(15) are upper-error estimates and cannot exclude an
event alone. The source/error identity and cutoff derivative bound are proved above;
the new code checks their supporting finite algebra, interval constants
and positive ratio/weight conditions.

The premise screen from Note 03 remains in force: polynomial/qTa heat
controls share local heat geometry but not canonical theta data;
finite-square and finite-prime controls lack complete theta automorphy
or unchanged coefficients; reflected/smooth/positive-primitive controls
lack the normalized integer-square source; Euler controls change the
conductor-one source; auxiliary density/two-channel controls lack the
complete signed physical comparison. Exact compact concentrating r bumps
fail the Gaussian-profile condition, while alternative-source lifts may
belong. None of these class statements implies that mere membership in
the observation space supplies a sign. No invented event boxes are used
for analytic existence controls.

The [separate internal review][review] checks derivations, complete
shared accounting, interval constants and the scope of the stop. A fresh
reviewer replay agrees. These are same-model internal checks; source
hashes identify files and do not prove mathematical claims. The global
real bridge and complex exterior remain open.

[space]: 03_CONSTRAINED_THETA_JET_SPACE_AND_RESIDUAL_CONTRACT_20261019.md
[summaries]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../../../avoid/10_numerics_ahead_of_the_question.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[plan]: ../../research-overview/01_RESEARCH_OVERVIEW_GOALS_AND_TASKS_20261018.md
[tracker]: ../../research-progress/01_RESEARCH_TASK_TRACKER_20261018.md
[record]: ../numerics/S07_T2_PROFILE_TRACE_192_20261019.json
[control-record]: ../numerics/S07_T2_SOURCE_CONTROLS_20261019.json
[review]: ../reviews/04_PAID_PROFILE_TRACE_INTERNAL_REVIEW_20261019.md
