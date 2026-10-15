# Certified chord controls, fixed-endpoint obstruction, and cutoff transfer

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**. Independent internal analytic derivation and exact-rational replay; not external refereeing or formal verification.

This note continues the [Investigation 22 strategy](../00_research_coordination/03_PRIORITIZED_SIGNED_BOUND_RESEARCH_PATHS_20261015.md). It certifies an adversarial polynomial pilot, proves stronger chord obstructions at parabolic and fixed-endpoint scales, and makes both sub-Gaussian and admissible Gaussian all-cutoff transfers precise. It supplies no signed theta estimate. A correction to the scope of strategy Note 03's cutoff warning is stated explicitly below.

## 1. Exact finite-angle target

Fix `j=0,1`, put `W=h_j`, and assume the **full** stationary condition `W_x(t,x)=0`, with `W` nonzero throughout `[x,y]`, `y>x`. For the continuous angle lift of `(W,W_x)`,

\[
\alpha_j(t,y)-\alpha_j(t,x)=\arctan\frac{W_x(t,y)}{W(t,y)}.
\]

Consequently, for any fixed `0<theta_*<pi/2`,

\[
\Delta\alpha_j\le\theta_*
\iff W(t,x)\{\tan(\theta_*)W(t,y)-W_x(t,y)\}\ge0.
\]

There is no winding ambiguity because `W` has one sign on the full interval. For `theta_*=pi/4`, define

\[
\mathcal C_j(t;x,y)=W(t,x)\{W(t,y)-W_x(t,y)\}.
\tag{1}
\]

The physical energy used below is always the **starting-point** energy

\[
e=E(t,x)=H(t,x)^2+H_x(t,x)^2.
\tag{2}
\]

This choice is material. Neither the endpoint jet energy nor the sum of starting and endpoint energies can silently replace it.

## 2. Two distinct collision scales

Suppose `H_t=-H_xx` is real analytic, with exact spatial multiplicity `2r+j`, `r>=1`, at `(T,a)`. Let `s=T-t`, let `chi(s)` be the full stationary predecessor for `W`, and write `k=partial_x^(2r)W(T,a)/r! != 0`. The established predecessor expansions give

\[
W(T-s,\chi(s))=ks^r(1+O(s)),\qquad
E(T-s,\chi(s))=k^2s^{2r}(1+O(s)).
\tag{3}
\]

For `j=1`, the second identity uses `H=O(s^(r+1))` on the predecessor. It does not identify the endpoint branch energy with the physical energy.

On each fixed inner window `ell=C*s/r`,

\[
\Delta\alpha_j\longrightarrow\arctan C,\qquad
\frac{\mathcal C_j(T-s;\chi(s),\chi(s)+Cs/r)}
 {E(T-s,\chi(s))}\longrightarrow1-C.
\tag{4}
\]

This already excludes any proposed chord bound `C_j>=-K E(start)` whose nonnegative coefficient is locally bounded uniformly over all covered short zero-free intervals: choose a fixed `C>K_*+1` after taking a local upper bound `K_*`, and then let `s` tend to zero. A negative chord is permitted by a finite-loss inequality; the contradiction is obtained by exceeding its prescribed finite loss.

There is a stronger scale appropriate to unbounded subpower losses.

**Parabolic chord theorem.** For each fixed `c>0`,

\[
\boxed{\frac{\mathcal C_j(T-s;\chi(s),\chi(s)+c\sqrt s)}
 {E(T-s,\chi(s))}
 =-\frac{F_r'(c)}{\sqrt s}+O(1),}
\tag{5}
\]

where

\[
F_r(y)=\sum_{l=0}^r\frac{r!}{(r-l)!(2l)!}y^{2l},
\qquad F_r(c)>0,\quad F_r'(c)>0.
\]

The entire interval is `W`-zero-free for sufficiently small positive `s`.

**Proof.** The already proved uniform real heat-profile expansion on `[0,c]` is

\[
\begin{aligned}
W(T-s,\chi(s)+\sqrt s\,y)&=ks^r\{F_r(y)+O(\sqrt s)\},\\
W_x(T-s,\chi(s)+\sqrt s\,y)&=ks^{r-1/2}\{F_r'(y)+O(\sqrt s)\}.
\end{aligned}
\]

Since `F_r>=1`, `W` keeps the sign of `k` on the whole interval. Substitution at `y=c` into (1), followed by division using (3), gives (5). The potentially large term is the differentiated endpoint; its stated remainder contributes only `O(1)` to the quotient. No unbounded-inner-coordinate estimate or weak-limit assertion is required.

**Correction to strategy Note 03.** Its warning that a generic subpower energy loss can swallow the chord defect is correct for the finite limit in (4) on one fixed inner scaled window. It does **not** apply to a bound uniform over every sufficiently short zero-free interval. Such a bound must also hold on the parabolic windows, where (5) has an inverse-square-root pole. An `E(start)^(-o(1))` relative loss cannot absorb that pole. Thus the stationary cutoff transfer below does extend to this stronger, fully quantified chord hypothesis, with starting-point energy and uniform endpoint coverage explicitly retained.

## 2a. A fixed endpoint gives a multiplicity-independent obstruction

The actual target covers every sufficiently short interval of a fixed positive allowed length, uniformly through each candidate event. It therefore permits choosing a small endpoint independent of `s`, not just intervals whose lengths shrink. Under this quantifier, the following is stronger than (5).

**Fixed-endpoint theorem.** For every sufficiently small fixed `delta>0`, the entire interval `[chi(s),a+delta]` is `W`-zero-free for all sufficiently small `s>0`, and

\[
\boxed{\frac{\mathcal C_j(T-s;\chi(s),a+\delta)}
 {\sqrt{E(T-s,\chi(s))}}
 \longrightarrow
 \operatorname{sgn}(k)\{W(T,a+\delta)-W_x(T,a+\delta)\}
 =:-d_\delta<0.}
\tag{5a}
\]

**Uniform zero-free proof.** Write `n=2r`, `a_0=partial_x^n W(T,a)/n!`, and apply ordinary analytic Taylor expansion to `F(eta,z)=W(T-eta²,a+z)`. The heat equation and spatial multiplicity give

\[
F(\eta,z)=a_0P_{2r}(\eta^2,z)
 +O\bigl((|\eta|+|z|)^{2r+1}\bigr),
\]

where `P_m` is the heat polynomial in (9). This is a two-variable remainder on a fixed neighborhood, not merely a bounded parabolic-coordinate expansion. Its leading polynomial obeys

\[
P_{2r}(\eta^2,z)\ge(\eta^2+z^2)^r
 \ge2^{-r}(|\eta|+|z|)^{2r}.
\]

For the first inequality, compare each coefficient with that of `(eta²+z²)^r`; the ratio for the coefficient indexed by `p` is the product of `2(2r-2i-1)`, `i=0,...,p-1`, and is at least one. Thus the remainder divided by the positive leading polynomial is `O(|eta|+|z|)`. Shrinking the fixed neighborhood makes this ratio smaller than `|a_0|/2`. Hence `W(T-s,a+z)` has the sign of `a_0` throughout that neighborhood whenever `s>0` is sufficiently small. Since `chi(s)-a=O(s)`, this includes the whole fixed-endpoint interval.

At time `T`, spatial Taylor expansion gives

\[
W(T,a+\delta)-W_x(T,a+\delta)
 =-2r a_0\delta^{2r-1}+O(\delta^{2r}),
\]

which has the opposite sign from `k` for all sufficiently small positive `delta`. Finally `W(start)/sqrt(E(start))` tends to `sgn(k)` by (3), and the endpoint expression converges by analyticity. This proves (5a).

Choose `delta` smaller than half the allowed interval length and inside the neighborhood where all source coefficients and error bounds are uniform. Then `ell_s=a+delta-chi(s)` remains positive and below the allowed length for all sufficiently small `s`. A bound available only on a prescribed shrinking family does not automatically cover these intervals.

**Consequence.** Any uniform chord lower bound

\[
\mathcal C_j(t;x,y)\ge-\omega(E(t,x)),\qquad
\omega(e)=o(\sqrt e),
\tag{5b}
\]

on all the admissible short intervals excludes every covered finite multiplicity. In particular, `C_j>=-K E(start)^gamma` suffices for any fixed `gamma>1/2` and locally bounded nonnegative `K`, uniformly in the two endpoints. This remains a conditional source target.

This is a substantive difference from the stationary observation. At multiplicity `2r+j`,

\[
\mathcal L_j\sim-\mathrm{const}\,E^{1-1/(2r)},
\qquad
\mathcal C_j(\text{fixed endpoint})\sim-\mathrm{const}\,E^{1/2}.
\]

A fixed power `gamma>1/2` therefore suffices for the chord at every multiplicity. For the stationary target, any fixed `gamma<1` eventually becomes too weak as `r` grows: its permitted loss can dominate `E^(1-1/(2r))`. The advantage requires both starting-point energy and uniform coverage of the allowed fixed endpoints.

## 3. A precise all-N sub-Gaussian lemma

Let `Q` denote either a stationary Laguerre observation or a chord observation on its declared admissible intervals. Let `e>=0` be the associated physical energy, using (2) for chords. Assume that throughout a fixed local neighborhood

\[
Q\ge-Ae\exp(aN^\beta)-B\exp(-cN^2)
\quad\text{for every integer }N\ge N_0,
\qquad 0<\beta<2.
\tag{6}
\]

Here `A,a,B>=0`, `c>0`, and `N_0>=0` is an integer. The coefficient rules must be prescribed independently of the unknown energy and the later cutoff selection. Assume local upper bounds `A_*`, `a_*`, `B_*`, `N_*` for `A,a,B,N_0`, with `N_*>=1`, and a positive lower bound `c_0` for `c`. For a chord these bounds are uniform in **both** endpoints throughout all sufficiently short admissible intervals. The domain must include the required predecessor and test intervals.

Set

\[
M=\max(1,B_*),\qquad
L(e)=1+\log_+(M/e),\qquad
D=N_*+1+c_0^{-1/2}.
\]

For `e>0`, choose only after the entire family (6) is established

\[
N=\left\lceil\max\left(N_*,\sqrt{\log_+(M/e)/c_0}\right)\right\rceil.
\]

Then `B exp(-cN²)<=e` and `N<=D sqrt(L(e))`. Hence

\[
\boxed{Q\ge-(A_*+1)e\exp\{a_*D^\beta L(e)^{\beta/2}\}.}
\tag{7}
\]

At `e=0`, let `N` tend to infinity in (6), giving `Q>=0`. The right side of (7) has the continuous extension zero there.

Because `beta/2<1`, the gauge in (7) is `e^(-o(1))` as `e` tends to zero. Along (3), it is `s^(-o(1))`. Therefore:

- for `Q=L_j`, it contradicts the stationary law `L_j/e=-r/s+O(1)`;
- for `Q=C_j` under the full short-interval hypothesis, it contradicts (5).

The cutoff may depend on `e` only in this deduction, after proving every member of the same source-prescribed family. Finite successful cutoff tests do not establish (6).

The same reasoning works for a locally uniform cost `exp(g(N))` whenever `g(N)=o(N²)`. The displayed power family is a convenient sufficient class. If a **full-amplitude** cutoff observation first has an independently proved error `Q_0 sqrt(e) exp(-c_1 N²)`, Young's inequality changes it into `e/2 + Q_0² exp(-2c_1N²)/2`; it can be absorbed into (6). A separately truncated leading amplitude or an unrelated cutoff convention requires its own complete error analysis.

## 3a. Gaussian cutoff costs are admissible below the tail rate

The fixed-endpoint theorem also accepts some costs of Gaussian size. Suppose the complete chord family is

\[
\mathcal C_j\ge-Ae\exp(aN^2)-B\exp(-cN^2)
\quad\text{for all integers }N\ge N_0,
\]

with the same source-prescription and uniform endpoint-coverage requirements. Assume fixed local bounds `0<=a<=a_*<c_0<=c`, `A<=A_*`, `B<=B_*`, and `N_0<=N_*`, where `N_*>=1`. Put

\[
\kappa=a_*+c_0,\qquad p=\frac{c_0}{a_*+c_0}>\frac12,
\quad M=\max(1,B_*),\quad D=N_*+1.
\]

For `0<e<=M`, set `L=log(M/e)` and choose `N=ceil(max(N_*,sqrt(L/kappa)))`. Since `sqrt(L/kappa)<=N<=D+sqrt(L/kappa)`,

\[
\mathcal C_j\ge
 -M^{1-p}e^p\left[
 A_*\exp\left\{a_*D^2+2a_*D\sqrt{L/\kappa}\right\}+1
 \right].
\tag{7a}
\]

The square-root logarithmic exponent pays the integer rounding and the cutoff threshold. It must not be dropped when claiming an exact `O(e^p)` estimate. Nevertheless, for every fixed `gamma` with `1/2<gamma<p`, (7a) implies a bound `C_j>=-K_gamma e^gamma` for sufficiently small `e`, with a finite prescribed local constant. Equivalently, its full right-hand loss is `o(sqrt(e))`, because `(p-1/2)L` dominates the `O(sqrt(L))` rounding term. The fixed-endpoint theorem excludes collisions.

Thus a uniform local strict gap `a_*<c_0` is sufficient even at cutoff power two. Separate upper and lower bounds are a convenient sufficient formulation; no conclusion is claimed from a nonuniform pointwise inequality `a<c` whose gap can close at the candidate event. The equality case `a=c` below remains a counterexample.

## 4. Why the energy location and cutoff exponent matter

Take the exact double-collision heat field

\[
H(T-s,x)=x^2+2s,
\qquad x=0,\quad y=\ell\ge0.
\]

The interval is zero-free for every `s>0`. Its chord is

\[
\mathcal C=2s(2s+\ell^2-2\ell),\qquad E(start)=4s^2.
\]

For the endpoint physical energy, set `q=H_x(y)/H(y)>=0` and `a=H(0)/H(y)`; then `0<a<=1` and

\[
\frac{\mathcal C}{E(end)}=a\frac{1-q}{1+q^2}\ge-\frac14.
\tag{8}
\]

For `q<=1` the quotient is nonnegative. For `q>=1`, multiplying the negative expression by `a<=1` improves it, and

\[
1-q+\tfrac14(1+q^2)=\tfrac14\{(q-2)^2+1\}>0.
\]

At starting-point square-root scale the same field satisfies `C>=-sqrt(E(start))` on every rightward interval, since `C/sqrt(E(start))=2s+(ell-1)^2-1>=-1`. Thus the exponent `gamma>1/2` in the fixed-endpoint criterion cannot be relaxed to `gamma=1/2` with an arbitrary bounded coefficient.

Thus a bounded endpoint-energy loss, or the weaker loss paid by `E(start)+E(end)`, is compatible with this collision on **every** rightward interval. It is not the criterion proved above. For branch 1 the endpoint physical energy and endpoint jet energy differ; failure already on branch 0 rules out an unqualified replacement.

The limitation at Gaussian cost with no strict rate gap is meaningful. For this same stationary field, `L_0=-4s` and `e=4s²`. For every real `N`,

\[
e\exp(N^2)+\exp(-N^2)\ge2\sqrt e=4s,
\]

so

\[
L_0\ge-e\exp(N^2)-\exp(-N^2)
\]

holds with bounded constants despite the collision. This is the excluded endpoint `beta=2`, with `A=B=a=c=1`. The identity behind the inequality is

\[
4s^2z^2+z^{-2}-4s=(2sz-z^{-1})^2,\qquad z=e^{N^2/2}.
\]

For chords on all `ell>=0`, the same example has `C>=-2s` by completing the square in `ell`, so it also satisfies this Gaussian-cost family. Hence one cannot include `beta=2` in the arbitrary-multiplicity exclusion lemma without further quantitative restrictions.

## 5. Exact adversarial pilot

Define the heat polynomials

\[
P_m(s,x)=\sum_{p=0}^{\lfloor m/2\rfloor}
 \frac{m!}{p!(m-2p)!}s^p x^{m-2p},
\qquad
H(T-s,x)=\sigma\{P_m(s,x)+bP_{m+1}(s,x)\}.
\tag{9}
\]

These satisfy `partial_s H=H_xx` exactly and have exact multiplicity `m` at `(T,0)`. Take the positive event time `T=1/4`. The frozen suite is

\[
m\in\{2,3,4,5\},\quad b\in\{0,1/3,-2/5\},\quad
\sigma\in\{1,-1\},\quad
s\in\{2^{-4},2^{-8},2^{-12},2^{-16},2^{-20},2^{-24}\}.
\]

With `j=m mod 2`, `n=m-j=2r`, one has

\[
W=\sigma a\{P_n+\lambda P_{n+1}\},\qquad a>0,
\quad \lambda=b\ (j=0),\quad\lambda=b(m+1)/m\ (j=1).
\]

For all `s>=0`, coefficient comparison gives

\[
P_{2r}(s,x)>0\quad(s>0),\qquad
|P_{2r+1}(s,x)|\le(2r+1)|x|P_{2r}(s,x).
\]

On `|x|<=R`, the explicit condition

\[
1-|\lambda|(2r+1)R>0
\tag{10}
\]

therefore guarantees that both `W` and `W_xx` have sign `sigma`. For `W_xx`, use the same comparison one degree lower and the exact derivative coefficients. This supplies interval-wide zero-freeness and strict monotonicity of the full stationary observation.

The checker verifies opposite exact rational signs for `sigma W_x` at `-2s` and `2s`, together with (10). The intermediate-value theorem and strict monotonicity prove existence and uniqueness of the full stationary root in that bracket. Sixty-four exact bisections, or an exact rational root when encountered, enclose it. No floating-point approximate root is being treated as certified.

For each root the checker evaluates:

- four inner windows `ell=C*s/r`, `C=1/2,1,2,4`;
- two parabolic windows `ell=c*sqrt(s)`, `c=1/2,1`, with rational square roots for the declared times.

Condition (10) certifies every entire window. Exact rational enclosures give `|W_x(end)/W(end)-C|<=128s` and `|C_j/E(start)-(1-C)|<=128s` on every inner test. Since arctangent is 1-Lipschitz, the former is a rigorous angular error bound about `atan(C)`; the checker does not claim a floating-point arctangent as a certified interval. The parabolic tests give

\[
\left|\sqrt s\,\frac{\mathcal C_j}{E(start)}+F_r'(c)\right|
\le128\sqrt s.
\]

The exact replay passes **5,616 assertions**, covers **24 germs**, isolates **144 full stationary roots**, and certifies **576 inner**, **288 parabolic**, and **288 fixed-endpoint** windows. All **288** inner cases with `C>1` have strictly negative chord, and all **144** cases with `C=1/2` have positive chord. The `C=1` cases are retained without imposing a sign on their vanishing leading limit.

The fixed endpoints are `delta=1/8,1/4`. Their complete intervals satisfy (10). On branch 1, the rational bound `1/sqrt(1+u)>=1/(1+u/2)` for `u>=0` encloses `|W(start)|/sqrt(E(start))`; no numerical square root is needed. The checker bounds the error in (5a) by `128s`. All 240 fixed-endpoint cases with `s<=1/256` are strictly negative. Across all 288 cases, 284 are negative and four are positive; those four earliest-time observations are retained as witnesses, not discarded. The fixed-endpoint theorem is asymptotic and makes no sign promise at those earlier times.

The companion script and small JSON receipt contain the declared parameters, all rational root enclosures, representative signed interval witnesses, error bounds, and script hash. They certify this finite adversarial suite. The all-multiplicity and all-N statements are analytic arguments above; no theta inequality, theta pilot, or unbounded-domain coverage has been established by the replay.

Replay: [exact checker](../../numerics/check_chord_controls.py) and [execution record](../../numerics/CHORD_CONTROLS_20261015.json). The [continuation handoff](../00_research_coordination/04_ARITHMETIC_CONTOUR_AND_CHORD_CONTINUATION_20261015.md) records the implications for the arithmetic and contour experiments.
