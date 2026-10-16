# Localized joint-witness target and its conditional payoff

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); the exact serving variant and configured reasoning
effort are not exposed and are not inferred.

## Status

The current conditional candidate remains `7/8 - 1/24000`, as recorded
in [the geometry extension](GEOMETRY_OPTIMIZATION_20261008.md). This note
does **not** raise that boundary. It proves an exponent implication for
the next target `7/8 - 1/20000`, conditional on a specific NEW estimate
for a restricted exceptional-row class. The external detector, reflection,
moment, contour, and seven-eighths results remain imported assumptions.

The new progress is a profile refinement obtainable from the existing
moment inputs, a precise mixed estimate sufficient for the remaining
class, and an exact continuous certificate for its proposed payoff.
The other two scouts identify limits of common-signal cancellation and
off-balance geometry with the current estimates.

The external input is the [September 30 companion paper](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf),
especially Proposition 8.3, Sections 14–19, and the contour argument.
The consulted PDF has SHA-256
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
These calculations do not independently validate its deep proofs or Lean
formalization.

## First mixed-moment calculation completed

The [mixed-moment reduction](MIXED_MOMENT_REDUCTION_20261008.md) now
expands the actual coefficient and removes three contributions with existing
inputs: smaller primitive row conductors, the complete plain-variable
diagonal, and column-ratio conductors through `U^(4/5)`. The remaining
signed term is specified in its equation (12), with all masks and physical
prime labels retained. Its estimate is still open. The payoff below and
the current conditional candidate are unchanged.

## 1. Proposed geometry and exact open hypothesis

Keep the balanced identity and set

\[
\ell=\frac16+\frac1{5000}=\frac{2503}{15000},\quad
b=\frac18,\quad
l_x=\frac{5311}{15000},\quad l_y=\frac{3593}{7500},\quad
h=\frac{508}{625}.
\]

Then \(l_x+l_y+\ell=1\), the full signal exponent remains
\(C(s)=s-11/16\), and the low exponent is

\[
L=l_x/2+b/12=\frac{3749}{20000}.
\]

Matching these exponents gives the proposed boundary

\[
\sigma=\frac{17499}{20000}=\frac78-\frac1{20000},
\qquad 1+2\sigma=\frac{11}{4}-\frac1{10000}.
\tag{1}
\]

At row scale \(U=Z^d\), use the source's buffered zero bin with
\(\delta=2a-1\), and let \(q\) be its weighted mean physical-slot
amplitude. Put \(x=q/\delta\), \(y=1/2-x\), and \(\alpha=5/6\).
With fixed legal \(\kappa=3/4\), the scalar count is

\[
D_x=3-17x/9,\quad B_x=2-8x/9,\quad P_x=B_x(1-x),
\quad J=(\alpha-\delta)D_x+\delta P_x,
\]
\[
t_0=1+\frac{\delta P_x}{2J},\qquad
R^*=1-\delta+\frac{(\alpha-\delta)\delta P_x}{2J}.
\tag{2}
\]

Let \(G\) be the integrated decreasing amplitude profile and let
\(H_G(t_0)\) be the improvement of the optimized short-witness count
at the original cutoff, as defined in the
[profile reduction](AMPLITUDE_PROFILE_REDUCTION_20261008.md).
The NEW hypothesis needed here is the following count estimate, uniform
with the source's physical coefficients, masks, fixed subdivisions and
height conventions:

\[
\#\mathcal B\ll
U^{R^*-1/10000+\epsilon}(1+T_1)^A
\tag{3}
\]

only on the residual class

\[
\boxed{
\frac9{25}\le\delta\le\frac{21}{50},\qquad
0\le y\le\frac1{100},\qquad
H_G(t_0)<\frac1{5000}.}
\tag{4}
\]

Here \(\epsilon>0\) can be prescribed sufficiently small before the
mesh, strict capacity decrement, fixed smoothness orders, and thresholds
are chosen. A strict surplus over the displayed count gain is convenient
for absorbing these losses. Equation (3) is not an established input.

## 2. What the existing moments already remove

For physical slot widths \(w_i\) at base U, sorted amplitudes \(g_i\),
and available length \(L_{\rm slots}=\sum w_i\), define
\(G(z)=\int_0^z g^*(v)\,dv\). Selecting the largest amplitudes gives
the actual short-count branches

\[
A_G(r)=1-\delta r-2G((1-r)/2),
\]
\[
S_{G,t}(r)=1-2\delta(t-r)
-2G\bigl(2(1-2(t-r))/9\bigr).
\]

Fractional selection is only a comparison: discard its last partial slot
and use whole original physical slots in the source moments. The loss is
at most \(\delta\max_iw_i\), plus the strict capacity allowance.
The needed supply threshold is \(L_{\rm slots}>1/5\), which this
geometry satisfies throughout the required row range.

Keeping t fixed would leave the long inverse branch unchanged. Retuning
by a decrement of \(H/(\alpha-\delta/3)\), for a certified lower bound
H on the short-branch gain, gives complete-count gain at least
\((\alpha-\delta)H/(\alpha-\delta/3)\), while the cutoff stays legal.
On the rectangle in (4), this ratio is at least \(31/52\).
Consequently every profile with \(H_G(t_0)\ge1/5000\) already gives

\[
\frac{31}{260000}=\frac1{10000}+\frac1{52000}
\]

before small losses. This proves why the additional arithmetic input is
needed only on (4).

The residual class has a useful necessary saturation condition: at least
80 percent of physical slot length has amplitude at least 90 percent of
its maximum \(\delta/2\), and zero-amplitude slots occupy at most
2 percent. These conditions alone do not estimate its row count. A fully
saturated profile has \(G(z)=qz\) and zero profile gain, so it survives
the reduction exactly.

## 3. A sufficient mixed-moment estimate

The [joint-witness note](JOINT_WITNESS_REDUCTION_20261008.md) identifies
a smaller object than the previously suggested mixed sixth moment:

\[
\boxed{
\sum_{u\in\mathcal C}|M_r(u)S_m(u)Q_I(u)|^2
\ll U^{1+\delta m-1/5000+\epsilon}(1+T_1)^A.}
\tag{5}
\]

The sum is over a buffered zero/profile class in (4), before restricting
to rows on which both witnesses are large. \(M_r,S_m\) are the actual
common-character, common-height detector witnesses. \(Q_I\) is a
permitted product of whole physical prime slots of length just below
\((1-r)/2\), selected from that fixed profile. Uniformity is needed
for \(7/10\le r\le37/50\), \(9/25\le m\le1/2\), and for all
the source's separating parameters with its original height conventions.
It is not a theorem about arbitrary row-dependent coefficient arrays.

The existing inverse moment times the plain pointwise bound has exponent
\(1+\delta m\). Thus (5) asks for a modest additional correlation
saving. It improves only the inverse count branch directly. Rebalancing
the inverse/plain crossing, then the short/long crossing, gives full gain

\[
F\eta_{\rm mix},\qquad
F=\frac{(\alpha-\delta)B_x}{J},\qquad
\eta_{\rm mix}=\frac1{5000}.
\]

The exact minimum over (4)'s rectangle is

\[
F\ge\frac{1091200}{2012413},\qquad
F\eta_{\rm mix}>0.000108446924>\frac1{10000}.
\tag{6}
\]

This leaves more than \(8.4\times10^{-6}\) at count level for losses.
The joint note checks the complete witness range: outside the requested
r-band the old marginal lines already have fixed slack, and long witnesses
use the original amplified estimate at the retuned cutoff.

The exact coefficient of \(M_rS_m\) is a windowed, truncated
\(\mu_K*1\) convolution. Its selected semiprime coefficients do not
vanish. Full convolution cancellation cannot be inserted after dyadic
selection; its missing boundary is part of the zero detector. Moreover,
the separate moment inequalities admit a maximally correlated abstract
model saturating both of them. Recombining those same inequalities by
Hölder cannot prove (5). An arithmetic correlation estimate is needed.

## 4. Continuous certificate for the proposed payoff

The general endpoint high exponent is

\[
E=h(R^*+1/2+\delta)-1-b(7/12+\delta/2)
+\ell(q-1-\delta/2).
\]

For the geometry above it equals

\[
E=E_{\rm plain}+\frac{h(\alpha-\delta)\delta P_x}{2J},
\quad E_{\rm plain}=-\frac14+\frac{5\ell}{4}+\frac b6
-\delta\left(\frac b2+\ell y\right).
\]

Writing \(p_y=7+18y+8y^2\) and
\(j_y=185+170y+(-138+12y+96y^2)\delta\), one has
\(P_x=p_y/9\), \(J=j_y/108>0\), and the exact polynomial

\[
N=10368J(-E)
=-96j_yE_{\rm plain}-576h(\alpha-\delta)\delta p_y.
\tag{7}
\]

The [exact checker](../numerics/check_localized_target.py) proves
\(E<-10^{-5}\) outside the rectangle in (4), and
\(E-h/10000<-10^{-5}\) inside it, on the full active domain
\(1/50\le\delta\le3/4\), \(0\le y\le1/2\).
The latter inequality uses (3), or the already proved profile reduction
where it applies. It is not a proof of (3).

The proof converts the polynomial to tensor Bernstein coefficients on
four rectangles and bisects three of them once. Positive rational
coefficients on all seven resulting rectangles certify their complete
continuous interiors and boundaries. No floating grid or presumed location
of a minimum is used. The four minimum coefficients are recorded in the
[small exact record](../numerics/localized_target_check.json).

The remaining margins are

| Range | Available exponent margin |
| --- | --- |
| Floor bin | \(4183/750000\) |
| Middle rows | \(74819/3000000\) |
| Small rows | \(9831/125000\) |
| Principal w remainder | \(3593/150000\) |
| Principal z remainder | \(127/93750\) |

All exceed \(10^{-5}\). The frequency extension
\(\zeta=1/1600000\) retains \(\ell/(h+\zeta)>1/5\) and costs
less than a quarter of the high margin. The tuple low excess
\(-d+(5\ell-1+d)_+/8\) is nonpositive; the additive-Gram condition
is strict; and \(\sigma>87/100\) retains the previously audited Euler
domain. Remaining preliminary losses can be chosen below these fixed
margins in the existing order of choices. The
[separate scoped review](../reviews/LOCALIZED_TARGET_PROFILE_REVIEW_20261008.md)
reconstructs (7) and checks the continuous cover and profile compatibility.

## 5. Results of the two other scouts and next arithmetic task

The [common-signal probe scout](COMMON_SIGNAL_PROBE_SCOUT_20261008.md)
constructs two actual admissible prime profiles, uses their finite-prime
normalizers to preserve the complete target signal, and writes the exact
mixed error kernel. A bounded combination can cancel one prescribed
coherent Mellin mode. An analytic filter with signal value one cannot
vanish on a continuum of possible modes, so this construction gives no
automatic uniform power gain. It would need new arithmetic control of
the mixed kernel or concentration of the error into controlled modes.

The [off-balance scout](OFF_BALANCE_GEOMETRY_SCOUT_20261008.md) retains
the dual-length cost when \(M+\ell=1+\tau\), \(\tau>0\). The
matching boundary supplied by the existing low envelope becomes

\[
\sigma=\frac{11}{12}-\frac\ell4+\frac{7\tau}{12}
+\frac{(5\ell-1-2\tau)_+}{8}.
\]

Near the current geometry, positive imbalance worsens that boundary at
slope \(7/12\). This is a limitation of the displayed envelope, not
an arithmetic lower bound or a prohibition on stronger estimates.

The first remaining task is therefore to expand the exact squared
coefficient in (5), retaining the inverse/plain variables, actual prime
labels, and phases, and identify an off-diagonal or transformed term
with a provable saving. The separate
[short-family program](CHARACTER_FAMILY_TRANSFER_20261008.md) remains
a larger open project. None of these scouts supplies its missing estimate.
