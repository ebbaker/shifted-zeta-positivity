# A shift-uniform extension of the explicit odd factor

11 September 2026. Background research accompanying the
[round-4 review](REVIEW_round4_20260911.md). This is not a manuscript version.

## Statement and normalization

Use the form and shift convention of the committed
[manuscript](../../manuscript.tex), equations labelled `eq:weil` and
`eq:shift`. The total interval length is `L`; put `ell=L/2`,

$$
j(t)=\frac{e^{-t/2}}{1-e^{-2t}},\qquad
R(t)=2\cosh(t/2)-j(t),\qquad
R_\omega(t)=\cosh(\omega t)R(t).
$$

**Proposition.** For `0<L<=7/10` and `0<=omega<=1/2`, define

$$
\phi_L(x)=x\left(1-\frac{4x^2}{5\ell^2}\right),\quad
h_{\omega,-}(x,y)=R_\omega(x+y)-R_\omega(|x-y|),\quad
v_{\omega,L}=\frac{Q_{\gamma,\omega,L}^{-}\phi_L}{\phi_L}.
$$

Then `h_{omega,-}>0` off the diagonal, `v_{omega,L}>1/200`, and every
odd input in the logarithmic form domain satisfies, with
`g=sqrt(2) f|_(0,ell)`,

$$
Q^\gamma_{\omega,L}[f]
=\frac12\int_0^\ell\!\int_0^\ell
h_{\omega,-}(x,y)\phi_L(x)\phi_L(y)
\left|\frac{g(x)}{\phi_L(x)}-\frac{g(y)}{\phi_L(y)}\right|^2dx\,dy
+\int_0^\ell v_{\omega,L}(x)|g(x)|^2dx
\geq\frac1{200}\|f\|_2^2.
$$

The two displayed positive terms define an explicit closed norm factor.
The usual off-diagonal graded block gives its self-adjoint supercharge.
This is the full shifted Weil form only for `L<=log(2)`; above that cutoff
the proposition concerns gamma alone. The central bound `1/100` from
round 3 remains stronger when `omega=0`.

## 1. The shifted folded conductance stays positive

For `t>0`,

$$
-\frac{j'(t)}{j(t)}=\frac12+\frac{2}{e^{2t}-1}.
$$

Thus `cosh(omega t) j(t)` is strictly decreasing when
`0<=omega<=1/2`, since its logarithmic derivative is

$$
\omega\tanh(\omega t)-\frac12-\frac2{e^{2t}-1}<0.
$$

Meanwhile `2 cosh(omega t) cosh(t/2)` is increasing. Therefore
`R_omega` is strictly increasing. Since `x+y>|x-y|` on the open positive
quadrant, the folded conductance is positive. This argument in fact holds
for all `t>0`; the length restriction enters the potential estimate.

## 2. A uniform derivative bound for the bounded shift kernel

Set

$$
k_\omega(t)=(\cosh(\omega t)-1)R(t),\qquad
r(t)=j(t)-\frac1{2t}.
$$

Round 3 proved on `0<t<=7/10` that

$$
r(0)=\frac14,\qquad -D\leq r'(t)\leq0,\qquad D=\frac{31}{480}.
$$

In particular `r(t)>=1/4-Dt>0`. We claim

$$
k_\omega'(t)\leq\omega^2
\left(-\frac14+\frac74t+\frac1{10}t^2+\frac{13}{20}t^3\right).
\tag{1}
$$

Here are details, including the negative linear-kernel contribution that
would be lost in a crude absolute bound. Put `C=17/16`. The rational
exponential check gives `cosh(7/20)<C`. For `0<omega<=1/2`,

$$
\frac{\sinh(\omega t)}{\omega t}\leq1+\frac{Ct^2}{24},\quad
\cosh(t/2)\leq1+\frac{Ct^2}{8},\quad
\frac{\cosh(\omega t)-1}{\omega^2}\leq\frac{Ct^2}{2}.
$$

The first bound follows from the Taylor remainder for `sinh`; the other
two follow from the second-derivative bound for `cosh`. Consequently the
derivative of the positive `2 cosh(t/2)` part, divided by `omega^2`, is at
most

$$
2t+\left(\frac C3+\frac{C^2(7/10)^2}{96}+\frac{C^2}4\right)t^3.
$$

For the singular term, its power series with positive coefficients gives

$$
\frac{d}{dt}\frac{\cosh(\omega t)-1}{2t}
=\frac{\omega t\sinh(\omega t)-\cosh(\omega t)+1}{2t^2}
\geq\frac{\omega^2}{4}.
$$

The derivative of `-(cosh(omega t)-1) r(t)`, divided by `omega^2`, is at most

$$
-\frac t4+D\left(1+\frac C2\right)t^2.
$$

Finally,

$$
D(1+C/2)<\frac1{10},\qquad
\frac C3+\frac{C^2(7/10)^2}{96}+\frac{C^2}4<\frac{13}{20},
$$

which proves (1). At `omega=0` the shift kernel vanishes identically.

## 3. Integrating the derivative bound against the fixed cubic

The bounded perturbation identity gives exactly

$$
v_{\omega,L}(x)-v_{0,L}(x)
=\frac1{\phi_L(x)}\int_0^\ell
[k_\omega(|x-y|)-k_\omega(x+y)]\phi_L(y)\,dy.
\tag{2}
$$

An antiderivative of the polynomial on the right of (1) is

$$
p(t)=-\frac t4+\frac78t^2+\frac1{30}t^3+\frac{13}{80}t^4.
$$

Write `z=x^2/ell^2`, `d(z)=1-4z/5`, and

$$
P(z)=\frac3{10}-\frac z6+\frac{z^2}{25},\qquad
U(z)=\frac7{10}+\frac35z-\frac{z^2}{10}+\frac{2z^3}{175}.
$$

Direct polynomial integration, splitting at `y=x` for odd powers, gives

$$
\begin{aligned}
\frac1x\int_0^\ell[(x+y)-|x-y|]\phi_L(y)dy&=2\ell^2P(z),\\
\frac1x\int_0^\ell[(x+y)^2-|x-y|^2]\phi_L(y)dy&=\frac{52}{75}\ell^3,\\
\frac1x\int_0^\ell[(x+y)^3-|x-y|^3]\phi_L(y)dy&=\ell^4U(z),\\
\frac1x\int_0^\ell[(x+y)^4-|x-y|^4]\phi_L(y)dy&=8\ell^5\left(\frac{13}{75}z+\frac3{35}\right).
\end{aligned}
$$

Hence (1)–(2) imply

$$
v_{\omega,L}(x)-v_{0,L}(x)\geq-\omega^2 B_\ell(z),
$$

where

$$
B_\ell(z)=\frac{
-\ell^2P(z)/2+(91/150)\ell^3+\ell^4U(z)/30
+(13/10)\ell^5[(13/75)z+3/35]}{d(z)}.
\tag{3}
$$

The length-uniform step must account for the negative coefficient of
`ell^2`; replacing every occurrence of `ell` by its maximum termwise is
not justified. Instead fix `z`. The numerator is of the form
`-a ell^2+b ell^3+c ell^4+e ell^5` with all four constants positive. Its
derivative divided by `ell` is strictly increasing and has at most one
positive zero, a minimum. Therefore its maximum on `[0,7/20]` occurs at
an endpoint. Thus

$$
B_\ell(z)\leq\max(0,B_{7/20}(z)),\qquad
v_{\omega,L}(x)\geq v_{0,L}(x)-\frac14\max(0,B_{7/20}(z)).
\tag{4}
$$

## 4. Rational certification of the remaining scalar bound

With `ell_*=7/20`, the central proof supplies

$$
\mathcal V(z)=-\gamma_E-\log(7\pi/10)-\frac12\log(1-z)
+\frac{7/5-22z/15-2D\ell_*^2P(z)-(13/75)\ell_*^3(33/32)}{d(z)}.
$$

It is enough to certify

$$
\mathcal V(z)-\frac14\max(0,B_{\ell_*}(z))>\frac1{200}
\quad(0\leq z<1).
\tag{5}
$$

The [reproducibility note](REPRODUCIBILITY_round4_20260911.md) contains the
entire checker. It uses exact fractions and the baseline exponential,
logarithm, arctangent, and Euler-constant enclosures. It checks all 1980
closed cells `[k/2000,(k+1)/2000]`, `k=0,...,1979`, and handles
`[99/100,1)` by `-log(1-z)>=log(100)`. Denominators stay at least `1/5`.
This covers the continuum, including the unbounded endpoint logarithm.

The smallest certified cell lower bound was approximately `0.0075953566891`
(cell 1748); the endpoint-tail lower bound was approximately
`0.525642130229`. Comparisons with `1/200` were performed on exact rational
endpoints. These decimal summaries are not themselves certificates.

## 5. Identity, domain, and limits of the result

Expand the weighted square on the odd smooth core. Its off-diagonal kernel
is `R_omega(|x-y|)-R_omega(x+y)`, and (2) supplies exactly the change in
the diagonal potential. This proves the displayed factor identity.
One can first truncate away the singular diagonal and then pass to the
form limit. Positivity follows from (5).

The shift perturbation is bounded on a fixed interval and preserves the
logarithmic form domain. The positive factor's graph norm on the core
equals `||f||^2+Q^gamma_{omega,L}[f]`, equivalent to the closed form norm.
Closure therefore gives the asserted domain. Almost-everywhere subsequences
identify its two closed components with the displayed weighted differences
and potential. There is no assumed square root of the unknown target in
this construction.

Independent autocorrelation and folded-integral checks on a complex odd
polynomial, using two quadrature orders and both nonzero test shifts,
agree after division by the input norm squared to better than `6e-17`
for the shift correction. They support the identity implementation;
the sign proof is (1)–(5), not the quadrature.

The construction continues to use an explicit trial cubic and reflection.
It does not derive that cubic from an arithmetic selection principle,
complete the even sector, or account for the first-prime correction.
