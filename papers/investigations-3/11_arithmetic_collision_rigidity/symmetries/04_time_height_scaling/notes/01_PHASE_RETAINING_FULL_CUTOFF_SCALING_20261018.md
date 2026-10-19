# S04: a paid phase-retaining scaling model for the complete first jet

18 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**. Parallel same-model derivation and internal
review; no independent specialist review.

Status: **proved in-note**, conditional on the established fixed-cutoff
Riemann–Siegel contract as an imported analytic input; bounded finite
expressions checked with outward Arb arithmetic. This is an explicit
quantitative completion of known coordinate asymptotics. It supplies no
new cancellation estimate, uniform signed lower bound, or Newman bound.

## Contract and prior work

The chosen observable is the complete signed normalized first jet
\((Q/2,2Q_x/L)\), where \(Q=H/\mathcal A_t\) in the current
[spectral contract][outer]. The primary gate is a uniform error for one
explicit signed scalar approximation and its actual spatial derivative,
through the growing cutoff. The output is available to S02/S03 as a regime
model. No claim of equality between jets at matched kappa is made.

Read the repository [result summaries][summaries] and [patterns to avoid][avoid],
particularly [collision controls][controls], [theta bookkeeping][theta],
[target reformulations][a01], [control premises][a02], [scoped exclusions][a07]
and [preserving cancellations][a12]. A global first-jet lower-bound target
is a reformulation of the desired exclusion; this note proves a replacement
error rather than assuming that target.

The [earlier manuscript][earlier] already contains `sc:paiderror`, the exact
`sc:coefficients`/`sc:vector`, `sc:coordinateasymptotics`, `prop:absmass`,
the derivative-mass calculation, genuine growing-edge cancellation,
`sc:packet`, and `lem:phase`. These remain prior results. In particular,
neither the exponentially small disk remainder nor the exact collision
vector below is new. The new calculation makes the leading-data scalar
and its derivative consistent and pays their *entire* growing-cutoff
replacement with explicit constants.

The primary imported published input is [Polymath, Theorem 1.3][polymath].
The current contract retains its normalization conversion, reflected
channel, correction error and every natural-to-fixed cutoff adjustment.
The numerical records pin the exact local sources and imported S02 code.

## Domain, signs and the scalar model

Throughout let
\[
 1\le\kappa\le2,\quad 0<t\le1/20,\quad
 L=\kappa/t,\quad x=4\pi e^L,\quad
 N=\left\lfloor\sqrt{e^L+t/16}\right\rfloor,
\]
and set
\[
 a_*=\frac{\kappa(4-\kappa)}{16},\qquad
 b_*=\frac{\kappa(\kappa+4)}{16},\qquad
 d_*=\frac{\kappa(\kappa+12)}{16}.
\]
The name \(a_*\) here is an exponent, distinct from
\(a=\partial_x\log\mathcal A_t\). Spatial derivatives hold **t and
the integer cutoff fixed**. In differentiating a formula, however,
\(L(x)=\log(x/(4\pi))\) has derivative \(1/x\); kappa is not held
fixed during that spatial derivative. The displayed scaling of the jet
by L uses its center value.

At \(s=(1-ix)/2\), write \(\alpha=\mathfrak a(s)=\alpha_r+i\alpha_i\),
\(\alpha'=U+iV\), and
\[
 \theta=\vartheta_t(x),\qquad
 \Omega=\tfrac12\Re\{\alpha(1+t\alpha'/2)\},\qquad \theta_x=-\Omega.
\]
The established exact finite scalar is
\[
 F_{t,M}=2\sum_{n\le M}w_n\cos\phi_n,\quad
 w_n=e^{t\ell_n^2/4-(1/2+t\alpha_r/2)\ell_n},\quad
 \phi_n=\theta+(x-t\alpha_i)\ell_n/2,
 \qquad \ell_n=\log n.
\]
For **any prefix** \(1\le M\le N\), define instead
\[
 W_n=e^{t\ell_n^2/4-(1/2+tL/4)\ell_n},\quad
 \psi_n=\theta+(x+t\pi/4)\ell_n/2,\qquad
 \widetilde F_{t,M}=2\sum_{n\le M}W_n\cos\psi_n.                 \tag{1}
\]
The common theta phase and physical normalizer remain exact. All
arithmetic phases and the amplitude factor \(e^{t\ell_n^2/4}\) are retained.
This is a phase-retaining scaling description, not a function of kappa
alone or a claim that the signed sum has a limit.

Differentiating this very scalar gives
\[
 \frac{2\widetilde F_{t,M,x}}L
 =\sum_{n\le M}W_n\left[
 \left(\frac{4\Omega}L-\frac{2\ell_n}L\right)\sin\psi_n
 -\frac{t\ell_n}{Lx}\cos\psi_n\right].                       \tag{2}
\]
Replacing the sine multiplier by \(1-2\ell_n/L\) and deleting the cosine
term would require a further payment. They are not the exact derivative
of (1). This consistency is needed when S03 consumes the model.

## Uniform full-cutoff payment

**Proposition.** For every prefix \(M\le N\) in the domain above,
\[
 \left|\frac{F_{t,M}-\widetilde F_{t,M}}2\right|<0.7e^{-d_*/t},\qquad
 \left|\frac{2(F_{t,M,x}-\widetilde F_{t,M,x})}L\right|<0.7e^{-d_*/t}.
                                                                    \tag{3}
\]
Their Euclidean vector error is less than \(e^{-d_*/t}\).

*Proof.* Here \(L\ge20\), \(x>10^9\), and
\[
 \ell_n\le L/2+t/(32e^L),\qquad t\ell_n<1.000001.
\]
The exact real-axis identities from `sc:realaxis` give
\[
 \delta_r=\alpha_r-L/2=\tfrac14\log(1+x^{-2})-\frac1{1+x^2}
       \in[-x^{-2},0],
\]
\[
 \beta=\alpha_i+\pi/4=\frac{3x}{1+x^2}+\tfrac12\arctan(1/x)
       \in[0,3.5/x],
\]
\[
 U=\frac{7x^2-5}{(1+x^2)^2},\quad
 V=\frac{x(x^2+5)}{(1+x^2)^2},\quad
 |U|\le7/x^2,\quad |V-1/x|\le3/x^3.
\]
Let
\[
 \delta_n=-t\ell_n(\delta_r+i\beta)/2,
 \qquad w_ne^{i\phi_n}=W_ne^{i\psi_n}e^{\delta_n}.
\]
These elementary bounds imply
\[
 |\delta_n|\le1.751/x,\quad
 \Re\delta_n\le0.500001/x^2,\quad
 |e^{\delta_n}-1|\le1.752/x.                                  \tag{4}
\]
For the last inequality use
\(e^\delta-1=\delta\int_0^1e^{v\delta}\,dv\), so the real-part bound
controls the multiplier. At fixed t,
\[
 \delta_{n,x}=-\frac{t\ell_n}{4}\{(V-1/x)-iU\},\qquad
 |\delta_{n,x}|\le1.751/x^2.                                 \tag{5}
\]
Write \((W_ne^{i\psi_n})_x=B_nW_ne^{i\psi_n}\), where
\[
 B_n=-\frac{t\ell_n}{4x}+i(-\Omega+\ell_n/2).
\]
For completeness,
\[
 |4\Omega/L-1|
 \le\frac2{Lx^2}+\frac{3.5t}{x^2}+\frac{\pi t}{2Lx}<0.005/x,
 \qquad |4B_n/L|<1.001.                                      \tag{6}
\]
The derivative bound follows by differentiating
\(W_ne^{i\psi_n}(e^{\delta_n}-1)\), including (5). Thus the two
component errors are at most
\[
 \frac{1.752}{x}\sum_{n\le M}W_n,
 \qquad \frac{1.753753}{x}\sum_{n\le M}W_n.                    \tag{7}
\]
Indeed the second constant dominates
\(1.001(1.752)+(4/L)e^{0.500001/x^2}(1.751/x)\).

The decreasing-weight integral in the prior mass argument gives
\[
 \sum_{n\le N}W_n\le5e^{a_*/t}.                              \tag{8}
\]
One direct ledger is to substitute \(u=e^{L/2-v}\) in
\(\int_1^N W(u)\,du\). Its integrand becomes
\(e^{a_*/t}e^{-v/2+tv^2/4}\). On \(0\le v\le L/2\),
\(tv\le1\), hence it is at most \(e^{a_*/t}e^{-v/4}\), of integral
at most \(4e^{a_*/t}\). If the upper cutoff lies slightly above
\(e^{L/2}\), the extra interval has v-length at most
\(t/(32e^L)\) and integrand less than 1.000001 times its endpoint
factor. The first summand is 1. Since \(a_*/t\ge15/4\), these reserves
fit below \(5e^{a_*/t}\). The logarithmic slope is negative throughout,
so the sum-integral comparison applies.

Finally \(a_*-\kappa=-d_*\) and \(x=4\pi e^{\kappa/t}\).
Both constants in (7), multiplied by \(5/(4\pi)\), are below 0.7.
The Euclidean error is below \(0.7\sqrt2e^{-d_*/t}<e^{-d_*/t}\).
This proof pays the replacement absolutely *after the signed scalar and
its derivative have been specified*. It asserts no size or sign for that
scalar. ∎

## Complete physical jet and cutoff transitions

The inherited disk estimate is
\(\lvert Q-F_{t,M}\rvert\le\eta_M\) on \(|z-x|\le1/L\), hence
\(|Q_x-F_{t,M,x}|\le L\eta_M\) at the center. The fresh checker evaluates
all AB, C and fixed-cutoff corrections from the current contract. For the
natural center cutoff the older `sc:paiderror` also gives the uniform
\(\eta_N\le5e^{-b_*/t}\). Combining it with (3),
\[
 \left\|(Q/2,2Q_x/L)
 -(\widetilde F_{t,N}/2,2\widetilde F_{t,N,x}/L)\right\|
 \le\frac{\sqrt{17}}2\eta_N+e^{-d_*/t}.                       \tag{9}
\]
The **added** scaling payment has
\[
 \frac{e^{-d_*/t}}{5e^{-b_*/t}}=\frac15e^{-\kappa/(2t)}
 \le\frac15e^{-10}<9.08\times10^{-6}.                         \tag{10}
\]
Equation (10) compares two proved upper bounds, not their actual errors.
The main residual is still the inherited Riemann–Siegel payment.

To return to the physical jet set \(\widehat H=\mathcal A_t\widetilde F\)
and \(a=\partial_x\log\mathcal A_t\). Then
\[
 \frac{|H-\widehat H|}{\mathcal A_t}
 \le\eta_M+1.4e^{-d_*/t},
\]
\[
 \frac{|H_x-\widehat H_x|}{\mathcal A_t}
 \le (L+|a|)\eta_M+(0.35L+1.4|a|)e^{-d_*/t}.                 \tag{11}
\]
Here \(M\le N\) and \(\eta_M\) is its own paid disk error; the uniform
\(5e^{-b_*/t}\) assertion above is for the stated natural-center contract,
not for arbitrary short prefixes. No second derivative is supplied here.

At a crossing keep the analytic cutoff fixed and use exactly
\[
 \widetilde F_{M+1}-\widetilde F_M=2W_{M+1}\cos\psi_{M+1},
\]
with the derivative of that same term from (2). The physical disk error
pays the corresponding added/removed *exact* arithmetic mode. The checker
uses a single fixed cutoff 22026 on a disk centered at the exact crossing
\(x=4\pi(22027^2-t/16)\), \(t=1/20\), with natural cutoffs 22026 and
22027. It verifies the model transition derivative independently by series
differentiation. No floor-defined quantity is differentiated.

## Range matching and the limits of this result

For the natural-cutoff scalar split into low modes \(1\le n\le16\),
intermediate modes \(17\le n\le N-\lfloor N^{3/4}\rfloor\), and the
remaining terminal modes. All three ranges use (1)–(2), preserving the
actual phases and derivative coordinate. Sum their signed contributions
before estimating the observable; (7)–(8) give **one common global**
replacement error, without paying the same mass three times.

The known signed-edge estimate may optionally remove the terminal range:
for \(K=N-\lfloor N^{3/4}\rfloor\), the errors for the model core are
\[
 |Q/2-\widetilde F_K/2|\le\eta_N/2+40N^{-1/24}+0.7e^{-d_*/t},
\]
\[
 |2Q_x/L-2\widetilde F_{K,x}/L|
 \le2\eta_N+800N^{-7/24}/L+0.7e^{-d_*/t}.                    \tag{12}
\]
The signed-edge constants and the remaining \(N-o(N)\) core are inherited,
not a new saving. The first checks do **not** use (12) to erase the edge.

The fixed-mode power profile cannot replace W uniformly term by term:
at \(n\sim N\),
\[
 \log\{W_n/n^{-1/2-\kappa/4}\}
 =t\log^2n/4=\kappa^2/(16t)+o(1),
\]
whereas the retained extra phase is
\(t\pi\log n/8=\pi\kappa/16+o(1)\). Neither can be discarded uniformly.
This is a scoped obstruction to the *uniform coefficientwise replacement*;
it does not prove divergence, a lower bound, or failure of another signed
asymptotic for the complete source. The earlier absolute-mass result
already excludes the specified absolute-tail route on \(0<\kappa<4\).

## Bounded checks, controls and next decision

The [192-bit record][r192] and [256-bit replay][r256] evaluate:

| Exact kappa | Exact time | Height (approximately) | Frozen cutoff |
| --- | --- | --- | --- |
| 1 | 1/20 | 6.096765655e9 | 22026 |
| 1 | 1/21 | 1.657272729e10 | 36315 |
| 21/20 | 1/20 | same height as previous row | 36315 |
| \((1/20)\log(22027^2-1/320)\) | 1/20 | exact crossing near 6.097061386e9 | 22026 |

The first two are matched-kappa points; the middle two share height and
have different time. These are point comparisons with complete analytic
residual payments, not a two-dimensional coverage certificate. Signed
low/intermediate/terminal vectors and absolute mass are separately recorded.
The replacement vector differences are below \(4.75\times10^{-11}\) in
all four cases. The complete scaled-jet lower bounds exceed respectively
0.4678, 1.1875, 1.1765 and 2.7399. These are bounded consistency checks;
they are not the uniform lower bound missing from (9).

The [fresh control replay][control-record] rejects all five existing event
boxes and the separate Euler negative-Laguerre witness using their own
source-specific data. It checks the inherited acceptance interface; it
does not apply theta's constants to altered sources or validate (3) by
control numerics. The substantive premise here is the unchanged complete
theta source and its quantitative Riemann–Siegel contract. Finite-prime
controls lack full normalized reflection; finite weighted-square controls
lack full reflection and the unchanged coefficient sequence; reflected
super-Gaussian, smooth-shape and positive-primitive controls lack that
theta expansion; Euler controls change its coefficients and level;
polynomial heat and counter-kernel controls lack the theta source.
Auxiliary positive-channel controls lack the complete signed physical
observation. No effective event height is inferred for analytic-only
finite-prime or smooth-primitive constructions.

**Decision:** the explicit full-cutoff replacement gate is met. This round
does not meet a cost, smaller *total* approximation-error, new region, or
effective exterior-onset gate: it adds a small paid model defect to the
established remainder. The default \(x\in[999,1001]\) box has been changed
because \(L\ge20\) in the chosen shrinking-time contract; its opening
height is already feasible at about 22,000 modes. No escalating height
scan was needed.

The next task is a cancellation-preserving estimate of an actual signed
quantity in (1)–(2), or the S03 residual after this substitution, with a
strict improvement over its existing payment. The dominant unbounded
obligation is the signed intermediate core, not the replacement defect.
Keep the \(0<t\le1/20,\ 1\le\kappa\le2\) restriction: no conclusion
is obtained for all of \(0<\kappa<4\), the unbounded real bridge, or the
complex exterior. See the [internal review][review] before extending this
contract.

[outer]: ../../../manuscript/positive_arithmetic_packets/sections/10_outer_exclusion.tex
[earlier]: ../../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex
[polymath]: https://arxiv.org/html/1904.12438v2#S1.Thm3
[summaries]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[theta]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[r192]: ../numerics/S04_SCALING_192_20261018.json
[r256]: ../numerics/S04_SCALING_256_20261018.json
[control-record]: ../numerics/S04_CONTROLS_20261018.json
[review]: ../reviews/01_FULL_CUTOFF_SCALING_INTERNAL_REVIEW_20261018.md
