# Exponential averages reduce the chord to a two value observation

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from the current session metadata. These are analytic collision criteria and exact polynomial controls. No signed-core bound for the theta field is proved.

The positive-average route has a particularly simple explicit member. Exponential weighting integrates the endpoint derivative exactly and turns the original chord into a difference of two products of field values. Keeping the complete starting factor preserves the useful square-root-energy tail. A quantitative comparison of the spatial scale and tail also permits cutoff-dependent shrinking windows, under a condition supplied by Gaussian tails and algebraically shrinking lengths.

## 1. The exact exponential average

Let `W=h_j`, `j=0,1`, and `e=E(t,x)=H(t,x)^2+H_x(t,x)^2`. For `delta>0` define

\[
\mathcal A_{j,\delta}(t,x)
=W(t,x)^2-e^{-\delta}W(t,x)W(t,x+\delta).
\tag{1}
\]

The fundamental theorem of calculus gives, without any stationary assumption,

\[
\boxed{\mathcal A_{j,\delta}(t,x)
=\int_0^\delta e^{-z}\mathcal C_j(t;x,x+z)\,dz.}
\tag{2}
\]

Indeed `d_z[e^{-z}W(t,x+z)]=e^{-z}(W_x-W)`. The normalized positive average is `A/(1-e^{-delta})`. In the unit-interval notation of [Note 03](03_FACTOR_PRESERVING_AND_AVERAGED_CHORD_TARGETS_20261015.md), its density is

\[
\rho_\delta(v)=\frac{\delta e^{-\delta v}}{1-e^{-\delta}},
\qquad 0\le v\le1.
\]

This density is positive and has integral one. It does not vanish at the endpoints, so the rapid Fourier-decay statement for a compactly supported smooth density is not being imported. The explicit integration in (2) is its advantage. The density may depend on the prescribed scale because each collision limit fixes that scale first.

## 2. Collision law at a fixed scale

Suppose an analytic backward-heat field has a spatial zero of multiplicity `2r+j` at `(T,a)`, with `r>=1`. Put

\[
a_0=\frac{\partial_x^{2r}W(T,a)}{(2r)!}\ne0,
\]

and let `chi(s)` be the full stationary predecessor of W. The manuscript gives

\[
W(T-s,\chi(s))/\sqrt{E(T-s,\chi(s))}
\longrightarrow\operatorname{sgn}(a_0).
\]

For every sufficiently small fixed positive delta, continuity and `W(T,a)=0` therefore give

\[
\boxed{
\frac{\mathcal A_{j,\delta}(T-s,\chi(s))}
{\sqrt{E(T-s,\chi(s))}}
\longrightarrow-d_{j,\delta},\quad
d_{j,\delta}=e^{-\delta}\operatorname{sgn}(a_0)W(T,a+\delta)>0.}
\tag{3}
\]

In particular,

\[
d_{j,\delta}=e^{-\delta}|a_0|\delta^{2r}(1+O(\delta)).
\tag{4}
\]

To justify the vanished diagonal term in (1), `W^2/sqrt(e)<=sqrt(e)->0`. For the cross term use the predecessor ratio and the fixed-endpoint limit. The full interval `[chi(s),chi(s)+delta]` is W-zero-free for sufficiently small s by the manuscript's positive heat-polynomial argument. Thus the same zero-free restriction may be retained in an attempted estimate. The energy is the complete physical energy on both branches; for `j=1`, it is not the auxiliary norm `h_1^2+h_2^2`.

A lower bound `A>=-o(sqrt(e))`, locally uniform through each event on a prescribed sequence of sufficiently small fixed scales, consequently excludes every covered finite multiplicity. This is a direct specialization of the positive-average method, with no endpoint derivative left to estimate.

## 3. The complete physical kernel and its cutoff

Set `mu_t(u)=e^{tu^2}Phi(u)` and `c_j(x,u)=u^j cos(xu+j pi/2)`. The exact symmetric kernel of A is

\[
\begin{aligned}
U_{j,\delta}(x;u,v)
={}&c_j(x,u)c_j(x,v)\\
&-\frac{e^{-\delta}}2
 [c_j(x,u)c_j(x+\delta,v)+c_j(x,v)c_j(x+\delta,u)].
\end{aligned}
\tag{5}
\]

Then `A=int int mu_t(u)mu_t(v)U du dv`. Complete-source decay justifies the products. In primitive variables `8h_j=I_j+delta_(j0)/2`, put `X_j=I_j(t,x)+delta_(j0)/2` and `Y_j=I_j(t,x+delta)+delta_(j0)/2`. Every lower-edge and corner contribution remains in

\[
\boxed{64\mathcal A_{j,\delta}=X_j^2-e^{-\delta}X_jY_j.}
\tag{6}
\]

Let `W_N(t,y)=sum_(n=1)^N partial_y^j H_n(t,y)` truncate only the endpoint. Define

\[
\mathcal A_{j,\delta,N}
=W(t,x)^2-e^{-\delta}W(t,x)W_N(t,x+\delta).
\tag{7}
\]

The complete starting field and complete stationarity `h_(j+1)(t,x)=0` remain unchanged. The tail proof in Note 03 gives, for `t<=T_*` and every real y,

\[
|W(t,y)-W_N(t,y)|
\le B_j^{\rm val}(T_*)e^{-\pi(N+1)^2/4},
\]

where an explicit finite source-prescribed constant is

\[
B_j^{\rm val}(T_*)=
2\pi^2\left(\sum_{n\ge1}n^4e^{-\pi n^2/4}\right)
\int_0^\infty u^j e^{T_*u^2+9u-(\pi/2)e^{4u}}\,du.
\tag{8}
\]

Consequently

\[
|\mathcal A_{j,\delta}-\mathcal A_{j,\delta,N}|
\le e^{-\delta}B_j^{\rm val}(T_*)\sqrt e\,
 e^{-\pi(N+1)^2/4}.
\tag{9}
\]

An independently proved bound `A_(j,delta,N)>=-K_N e` would therefore suffice on a fixed-scale domain, with no restriction on the growth of `K_N`. Equivalently the core task is the one-sided product bound

\[
e^{-\delta}W(t,x)W_N(t,x+\delta)
\le W(t,x)^2+K_NE(t,x).
\tag{10}
\]

This formulation uses only values at the endpoint. It still controls the depth of a stationary extremum relative to a nearby same-sign value, and it is not a consequence of source positivity or Cauchy--Schwarz. The latter pays by endpoint energy or an absolute source moment, losing the required starting scale. In the formal two-value coordinates `(a,b)=(W(start),W(end))`, the quadratic form is `a^2-e^{-delta}ab` and has determinant `-e^{-2delta}/4<0`. No positive-form conclusion follows from (1) alone.

## 4. Shrinking windows with a quantified tail comparison

Note 03 correctly warns that a shrinking spatial reach invalidates the argument using one common fixed endpoint unless an additional comparison is supplied. Formula (4) supplies that comparison explicitly for A.

**Proposition.** Let `delta_N>0` be prescribed, tend to zero, and be independent of any hypothetical event. Suppose for each branch, at every candidate event, the admissible full stationary starts eventually satisfy

\[
\mathcal A_{j,\delta_N}\ge-K_NE-\varepsilon_N\sqrt E
\tag{11}
\]

for every sufficiently large fixed N. Each `K_N` has a finite local bound through the event, and `epsilon_N` is a source-prescribed local error bound. The fixed-N domain must include every sufficiently close predecessor and its whole interval of length `delta_N`; its time threshold may depend on N. Assume

\[
\boxed{\varepsilon_N=o(\delta_N^m)
\quad\text{for every fixed positive integer }m.}
\tag{12}
\]

Then no covered finite multiple real zero occurs. No bound on the growth of `K_N` is required.

**Proof.** At a putative multiplicity `2r+j` event, formula (4) gives `d_(j,delta_N)>=c delta_N^(2r)` for all sufficiently large N, with an event-dependent `c>0`. Condition (12) permits choosing one fixed N with `epsilon_N<d_(j,delta_N)/2` and a sufficiently small admissible length. Now let s tend to zero at this fixed N. Divide (11) by square-root energy; the term `K_N sqrt(E)` tends to zero and (3) gives `-d_(j,delta_N)>=-epsilon_N`, a contradiction. There is no simultaneous limit tying N to s. The argument uses only the local analytic collision law and the prescribed errors.

In particular, **a Gaussian tail and `delta_N=N^{-q}` for any fixed `q>0` satisfy (12)**. More generally the same Gaussian tail works whenever `log(1/delta_N)=o(N^2)`. Gaussian spatial shrinkage need not work for all multiplicities; its rate would have to be compared with the tail rate and the order `2r`.

This makes a concrete next core target available at only one length per cutoff:

\[
\boxed{\mathcal A_{j,1/N,N}\ge-K_NE,
\qquad j=0,1,}
\tag{13}
\]

with locally bounded source-prescribed `K_N` for every sufficiently large fixed N. The tail (9) and Proposition supply its collision implication. No proof of (13) for theta is claimed.

## 5. Exact collision controls and the next arithmetic question

The companion [checker](../../numerics/check_exponential_average_chords.py) tests 36 exact backward-heat germs of multiplicities 2 through 7, including asymmetric germs and both signs. Rational root isolation covers 108 complete stationary starts; 216 entire rightward intervals are certified zero-free. Exponential factors are enclosed by alternating rational Taylor sums. All 1,620 assertions pass; the [receipt](../../numerics/EXPONENTIAL_AVERAGE_CHORD_CHECKS_20261015.json) records finite negative averaged chords, physical-energy scaling, and convergence to the negative limit. Analytic heat-polynomial inequalities justify the whole-interval and uniqueness checks. These finite controls do not prove the general proposition or a theta sign; those have the separate scopes stated above.

The next useful arithmetic question is whether full coefficient coupling can establish (10) or (13). The [elliptic-shift continuation](../03_theta_bundles_and_connections/05_ELLIPTIC_SHIFT_CORE_AND_PROJECTION_OBSTRUCTION_20261015.md) tests how much the elementary translation insertion actually supplies. A representation that only changes cutoff boundary modes still needs a signed core estimate. The exponential average simplifies the observation and the endpoint derivative budget; it does not supply that missing sign.
