# Preserving the starting factor through a coupled parity decomposition

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**, verified from the current session. This note supplies an exact cutoff rule and an actual-theta cancellation diagnostic for the coupled-product experiment. It proves no theta signed-core bound.

## 1. The physical product fixes the cutoff geometry

Use the [coupled-product note](06_COUPLED_THETA_PRODUCT_AND_PARITY_SECTORS_20261015.md) and the [exponential-average target](../02_signed_turning_control/04_EXPONENTIAL_AVERAGE_AND_SHRINKING_CHORD_TARGETS_20261015.md). Write

\[
\ell_{j,n}(t,x)=\int_0^\infty
\phi_n(u)e^{tu^2}u^j\cos(xu+j\pi/2)\,du,
\quad W=h_j=\sum_{n\ge1}\ell_{j,n},
\quad W_L=\sum_{1\le n\le L}\ell_{j,n}.
\]

Here W_0=0 and every start, including its stationarity condition, is complete. Put `y=x+δ`, `α=e^(−δ)`. The target is

\[
\mathcal A_{j,\delta,N}=W(t,x)^2-\alpha W(t,x)W_N(t,y).
\tag{1}
\]

In the complete two-source theta series let n be the starting index and m the endpoint index. The coupled variables

\[
p=n+m,\qquad k=n-m
\]

range over integer pairs of the same parity. The inverse map is `n=(p+k)/2`, `m=(p−k)/2`. Therefore an endpoint-only cutoff is exactly the **infinite diagonal strip**

\[
\boxed{p\equiv k\pmod2,\qquad |p-k|\le2N.}
\tag{2}
\]

There is no bound on p+k. The zero-index rows n=0 or m=0 contribute zero only after the complete physical source operators are applied. The two-source mode weight is `φ_|n|(u)φ_|m|(v)/4`, with φ_0=0; pairing both signs recovers the positive-index physical sums.

For the full untruncated source, the addition variables separate into even and odd parity sums at equal source parameters. The strip (2) still couples those indices. Replacing it by two independent finite theta sums changes the cutoff product, even in that equal-parameter case.

## 2. A precise algebraic criterion for retaining the factor

Let B_nm be a prescribed coefficient mask, and let a and b be arbitrary finitely supported real or complex sequences. The identity

\[
\sum_{n,m}B_{nm}a_nb_m
=\left(\sum_na_n\right)\left(\sum_md_mb_m\right)
\quad\text{for every }a,b
\tag{3}
\]

holds if and only if `B_nm=d_m` is independent of the starting index n. Necessity follows by testing a and b on individual coordinate vectors; sufficiency is direct. Equivalently, all vectors with `sum a_n=0` must be annihilated after fixing any endpoint coordinate. Testing `a=e_n−e_l` forces `B_nm=B_lm`.

Thus the transformed mask for a universally factor-preserving endpoint rule has the form

\[
B(p,k)=d_{(p-k)/2}
\]

on the same-parity lattice. This is a statement about exact bilinear factorization for arbitrary signed observations. It is not a classification of every identity that could exploit additional theta constraints. Physical mode transforms do have oscillatory signs, so entrywise source positivity does not make this issue disappear.

This also gives a sharp test for a proposed remainder bound: a bilinear remainder satisfying `|R(a,b)|≤ε(b)|sum a_n|` for all a must vanish on that same kernel. A generic mask cutting the starting index does not have this property.

## 3. What a rectangular parity cutoff actually computes

Let M,N be integers with M≥N≥1. Suppose a computation retains the strip (2) but also imposes

\[
|p|\le M,\qquad |k|\le M,\qquad M\ge N.
\]

The identity `max(|n+m|,|n−m|)=|n|+|m|` shows that this is a diamond in the original indices. Pairing signs gives the exact truncated product

\[
\boxed{Q_{j,N,M}(t;x,y)
=\sum_{m=1}^N\ell_{j,m}(t,y)W_{M-m}(t,x).}
\tag{4}
\]

Different endpoint modes now see different incomplete starting fields. The omitted term is

\[
W(t,x)W_N(t,y)-Q_{j,N,M}
=\sum_{m=1}^N\ell_{j,m}(t,y)
\{W(t,x)-W_{M-m}(t,x)\}.
\tag{5}
\]

On bounded heat-time ranges, the earlier source tail gives

\[
|W-W_L|\le B_j e^{-\pi(L+1)^2/4},\qquad
\sum_{m\ge1}|\ell_{j,m}(t,y)|\le L_j<\infty,
\]

uniformly for real x,y. One explicit choice is

\[
L_j(T_*)=2\pi^2\left(\sum_{m\ge1}m^4e^{-\pi m^2/2}\right)
\int_0^\infty u^j e^{T_*u^2+9u-(\pi/2)e^{4u}}\,du.
\]

Consequently

\[
\boxed{|W W_N-Q_{j,N,M}|
\le L_jB_j e^{-\pi(M-N+1)^2/4}.}
\tag{6}
\]

This is a **pure absolute tail**. It does not contain √E. Equation (5) must be recombined exactly, or its cost must be paid through a separate pure-tail argument. The mixed-error theorem cannot silently be applied to (6).

A formal cancellation example makes the failure quantitative. Retain endpoint mode m=1 and starting observations a_1=1, a_3=−1+ε, all others zero. Their complete sum is W=ε. With N=1,M=3, the parity box retains n=1 but omits n=3. Its product is 1 while the complete product is ε, so the error is `1−ε`, not O(|ε|). This is an algebraic test of the mask, not a newly constructed theta field. The infinite strip retains both starting terms and gives ε exactly.

The preferred computation should therefore keep the complete starting row sum analytically. If a second finite cutoff is unavoidable, it must retain the explicit correction (5) and state the new error criterion. Choosing a cutoff from an observed small denominator is not a substitute for a locally uniform proof through a possible event.

## 4. Actual theta parity sectors cancel at a much smaller physical scale

The parity problem is visible in the actual theta field, without assuming a collision. Split the source into even and odd positive indices:

\[
\Phi_e=\sum_{n\ge1}\phi_{2n},\qquad
\Phi_o=\Phi-\Phi_e.
\]

With `a=(log 2)/2`, the equal theta coefficients give the exact dilation relation

\[
\boxed{\Phi_e(u)=e^{-a}\Phi(u+a).}
\tag{7}
\]

Its physical transform includes a shifted lower endpoint:

\[
h_{j,e}(t,x)=e^{-a}\int_a^\infty
\Phi(v)e^{t(v-a)^2}(v-a)^j
\cos\{x(v-a)+j\pi/2\}\,dv.
\tag{8}
\]

The heat tilt, spectral shift and lower limit a are all essential. For example, if

\[
F_t(z)=\int_0^\infty\Phi(v)e^{tv^2+izv}\,dv,
\quad B_{t,a}(z)=\int_0^a\Phi(v)e^{tv^2+izv}\,dv,
\]

then

\[
H_e(t,x)=e^{ta^2-a}\operatorname{Re}
\left[e^{-iax}\{F_t(x+2ita)-B_{t,a}(x+2ita)\}\right].
\tag{9}
\]

F_t is the complete **one-sided complex transform**, not the cosine transform H. Dropping its imaginary part before the phase multiplication or omitting B would change the identity.

Define the strictly positive constant

\[
\beta=-\Phi_e'(0)
=-\sum_{n\ge1}e^{-4\pi n^2}P_1(4\pi n^2)>0,
\quad P_1(\lambda)=-8\lambda^3+30\lambda^2-15\lambda.
\tag{10}
\]

Indeed `P_1(λ)=−λ(8λ²−30λ+15)<0` for λ≥4π. The polynomial in parentheses is already positive and increasing for λ≥12. The source series and all required derivatives converge absolutely.

Fix real t. The even-index heat density `f_e(u)=e^(tu²)Φ_e(u)` has `f_e'(0)=−β`, independent of t, and integrable derivatives of every order. Repeated half-line integration by parts yields

\[
\boxed{h_{j,e}(t,x)
=(-1)^j(j+1)!\,\beta x^{-j-2}+O_{t,j}(x^{-j-4}),
\qquad j=0,1.}
\tag{11}
\]

For j=0 the first two terms are `−f_e'(0)/x²+f_e'''(0)/x⁴`; differentiating, or applying the corresponding sine integration by parts, gives j=1. The full theta source is even and smooth across zero with double-exponential decay. Its heat density is Schwartz on the whole real line, hence every full h_j is Schwartz in real x. Therefore

\[
h_{j,o}(t,x)=-h_{j,e}(t,x)+O_{t,j,M}(x^{-M})
\quad\text{for every fixed }M.
\tag{12}
\]

The two arithmetic parity components have opposite algebraic tails even though their sum has superalgebraic decay.

To see the effect on the **complete-endpoint** amplitude, let `W_+=W_e+W_o=W`, `W_-=W_e−W_o`, and define

\[
A=W_+(x)^2-\alpha W_+(x)W_+(x+\delta),\qquad
B=W_-(x)^2-\alpha W_-(x)W_-(x+\delta).
\]

The same-parity and opposite-parity sectors of the coupled source are exactly

\[
A_{\rm same}=\tfrac12(A+B),\qquad
A_{\rm cross}=\tfrac12(A-B).
\tag{13}
\]

For each fixed δ>0, (11)–(12) imply

\[
\boxed{B(t,x)
\sim4[(j+1)!\beta]^2(1-e^{-\delta})x^{-2j-4}>0
\quad(x\to+\infty).}
\tag{14}
\]

In contrast A, E and √E decay faster than every inverse power. Thus separate absolute estimates for these parity sectors cannot satisfy a bound `|A_same|+|A_cross|≤P(x)√E` on an unbounded real half-line for any polynomial P. The polynomially sized difference channel must cancel before the physical amplitude is recovered. This is an actual-theta asymptotic statement; it is stronger than a formal arbitrary-vector example.

The statement concerns fixed t and fixed δ, with complete endpoint sources in (13)–(14). It does not assert uniformity in a simultaneous N,x limit. It also does not forbid coefficients growing faster than polynomials in height, or coefficients merely locally finite through each finite event. The local collision criterion still permits such coefficients. The practical conclusion is to preserve the parity cancellation rather than assume a physical-energy bound for the separate sectors.

## 5. Research decision and verification

The coupled addition formula supplies real coefficient relations, but the implementation has two independent requirements: retain the infinite starting-direction strip, and recombine both parity channels before paying a remainder by physical energy. The [physical reflection control](../05_control_families/04_REFLECTION_POSITIVE_SOURCE_COLLISION_AND_MIXED_SECTORS_20261015.md) gives a complementary exact reason to retain the exchange-odd sector when only the endpoint is truncated.

The [standard-library checker](../../numerics/check_parity_strip_cutoff.py) verifies the lattice inverse and cutoff masks, the exact box product and correction, the row-factorization tests, parity amplitude algebra, endpoint-polynomial sign margin and integration-by-parts leading coefficients. Its [receipt](../../numerics/PARITY_STRIP_CUTOFF_CHECKS_20261015.json) distinguishes these finite checks from the general analytic statements. The arbitrary-mask characterization, source convergence, full theta Schwartz decay and asymptotic theorem are proved above; no assertion count substitutes for them. No theta stationary sign domain or collision exclusion is claimed.
