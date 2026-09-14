# The even sector: a positive mean-zero subspace and one remaining scalar

11 September 2026. Background research; no new manuscript version.
See the [review](REVIEW_round4_20260911.md) and
[reproduction code](REPRODUCIBILITY_round4_20260911.md).

All statements in this note concern the **central gamma form**. Its equality
with the full Weil form is limited to `L<=log(2)`.

## 1. Isolate the singular energy without flattening the smooth terms

Let `I=(-ell,ell)`, `L=2ell`, and use the normalization of the baseline
[manuscript](../../manuscript.tex). Set

$$
\mathcal E_s[f]=\frac14\int_{I^2}\frac{|f(x)-f(y)|^2}{|x-y|}\,dx\,dy,
\quad V(u)=-\frac12\log(1-u^2),\quad
c_L=-\gamma_E-\log(\pi L).
$$

For an even input,

$$
Q^\gamma_{0,L}[f]
=\mathcal E_s[f]+\int_I[c_L+V(x/\ell)]|f(x)|^2dx
-\int_{I^2}r(|x-y|)\overline{f(x)}f(y)dx\,dy
+2\left|\int_I f(x)\cosh(x/2)dx\right|^2,
\tag{1}
$$

where `r(t)=j(t)-1/(2t)`. This follows by inserting

$$
F(t)=\log2+\pi/4-\tfrac12\log t-\int_0^t r(s)ds
$$

in the full-output jump formula. The diagonal integrals of `r` cancel,
leaving its bounded convolution term. Both the endpoint logarithm and the
even pole amplitude remain exact. Suzuki's equation (4.4) gives the same
singular energy and boundary-logarithm structure in rescaled coordinates;
the bounded terms in (1) are kept in this project's normalization.
[Suzuki v2, Section 4.2](https://arxiv.org/html/2606.09096v2).

## 2. A short proof of the even mean-zero singular gap

On `(-1,1)`, the operator of the singular form is

$$
(D_s p)(u)=\frac12\int_{-1}^1\frac{p(u)-p(v)}{|u-v|}\,dv.
$$

It preserves polynomials of degree at most `n`, is symmetric, and has
leading coefficient `H_n` on the monomial `u^n`. Explicitly,

$$
D_s u^n=H_nu^n-
\sum_{\substack{0\leq k<n\\k\text{ odd}}}\frac{u^{n-1-k}}{k+1},
\qquad H_n=\sum_{j=1}^n\frac1j,
\quad H_0=0.
$$

Polynomial division and splitting the integral at `v=u` prove this formula.
Symmetry and degree preservation then imply `D_s P_n=H_n P_n` for the
Legendre polynomials: the image is orthogonal to every lower-degree
polynomial, and its leading coefficient identifies the multiple.

For smooth inputs, the integral action lies in `L^2`; its coefficients
against the complete Legendre basis are `H_n` times the input coefficients.
Parseval gives the corresponding form identity. It extends to the relevant
closed form domain by core approximation. Scaling changes neither these
eigenvalues nor the Rayleigh quotient of the singular form.

An even input of mean zero has no degree-zero or odd Legendre components.
Therefore

$$
\mathcal E_s[f]\geq H_2\|f\|^2=\frac32\|f\|^2.
\tag{2}
$$

## 3. A certified positive subspace

Let

$$
\mathcal H_0=\{f\in L^2(I):f(-x)=f(x),\ \int_I f=0\}.
$$

On this subspace the constant part `r(0)=1/4` has zero quadratic form.
Using the reviewed bound `|r(t)-1/4|<=Dt`, `D=31/480`, Schur's kernel
estimate gives

$$
\left|\int_{I^2}[r(|x-y|)-1/4]\overline{f(x)}f(y)dxdy\right|
\leq\frac{DL^2}{2}\|f\|^2,
$$

because `sup_x integral_I |x-y|dy=L^2/2`. The boundary logarithm and even
pole term in (1) are nonnegative. Thus for every `f` in `H_0` and the
logarithmic form domain,

$$
Q^\gamma_{0,L}[f]\geq
\left(\frac32-\gamma_E-\log(\pi L)-\frac{DL^2}{2}\right)\|f\|^2
>\frac{11}{100}\|f\|^2,
\qquad 0<L\leq\frac7{10}.
\tag{3}
$$

The scalar lower bound decreases with `L`. Exact rational evaluation at
`7/10` gives a lower endpoint approximately `0.115005312753`, exceeding
`11/100`. This is an infinite-dimensional subspace estimate, not a
truncated-matrix eigenvalue calculation.

## 4. An exact scalar condition for the remaining even direction

Let `e=L^(-1/2)` be the unit constant input, and let `P` be orthogonal
projection onto `H_0`. Define

$$
a_L=Q^\gamma_{0,L}[e],\qquad b_L=P Q^\gamma_{0,L}e.
$$

The constant belongs to the operator domain: its image is `e kappa_L`,
where

$$
\kappa_L(x)=w_0+F(\ell+x)+F(\ell-x)
+8\sinh(\ell/2)\cosh(x/2).
$$

Only logarithmic endpoint singularities occur, so this image is in `L^2`.
In particular `a_L` is the average of `kappa_L` and
`b_L=e(kappa_L-a_L)`.

Let `F_L` denote the self-adjoint operator on `H_0` associated with the
restriction of the gamma form. Inequality (3) establishes `F_L>=11/100`
independently of positivity on the full even space. Hence its inverse
exists and is bounded. For `f=t e+u`, `u in H_0`, completion of the square
gives the exact identity

$$
Q^\gamma_{0,L}[f]
=Q^\gamma_{0,L}[u+tF_L^{-1}b_L]+s_L|t|^2,
\qquad
s_L=a_L-\langle b_L,F_L^{-1}b_L\rangle.
\tag{4}
$$

In the first term the argument belongs to `H_0`. Thus the even form is
nonnegative if and only if `s_L>=0`; strict positivity follows if `s_L>0`.
This reduction does not prove the remaining inequality. It also does not
by itself give an explicit norm factor for `F_L`.

For a proposed approximation `v` in the operator domain of `F_L`, put
`r_v=b_L-F_L v`. The exact variational identity yields the useful bracket

$$
2\Re\langle b_L,v\rangle-\langle v,F_Lv\rangle
\leq\langle b_L,F_L^{-1}b_L\rangle
\leq2\Re\langle b_L,v\rangle-\langle v,F_Lv\rangle
+\frac{100}{11}\|r_v\|^2.
\tag{5}
$$

This is a concrete next target: specify `v`, its domain, and the residual,
then use (5) to decide `s_L`. An inverse or factor assumed positive on the
entire even target would bypass precisely the scalar condition that remains.

## 5. Why the smooth terms cannot simply be replaced by constants

Consider the deliberately simplified form

$$
Q_{\rm flat}[f]=\mathcal E_s[f]
+\int_I[c_L+V(x/\ell)]|f(x)|^2dx
+\frac74\left|\int_I f(x)dx\right|^2.
$$

It replaces `r` by `1/4` and the even pole amplitude `cosh(x/2)` by `1`.
No order relation between this form and the true form is asserted.

At `L=log(2)` take the unit even polynomial

$$
f(x)=\sqrt{\frac{15}{8L}}\left(1-\frac{4x^2}{L^2}\right).
$$

Since `1-u^2=(2/3)(P_0-P_2)`, the Legendre identity and elementary
logarithmic moments give the exact value

$$
Q_{\rm flat}[f]
=-\gamma_E-\log(\pi\log2)+\frac{31}{30}+\frac{11}{24}\log2<0.
\tag{6}
$$

For example the required moments can all be derived from

$$
\int_0^1u^{2k}V(u)du
=\frac{\sum_{j=0}^k(2j+1)^{-1}-\log2}{2k+1}.
$$

The exact certificate encloses (6) in approximately
`[-0.008308003,-0.000495502]` (endpoints here rounded outward), with the
stronger rational assertion that its upper endpoint is below `-1/2500`.
A higher-accuracy floating-point evaluation is about `-0.0044068390793`.

On the same input, a separate gamma-form quadrature gives approximately
`+0.00554468259865`. That positive decimal is a diagnostic, not an additional
rational sign certificate. The roughly `0.00995152` correction is large
enough to reverse this input's sign. Negativity of the simplified form
therefore blocks using it alone as an independently positive baseline;
it says nothing adverse about the sign of the actual Weil form.

## What remains

Evaluate or control (4) without dropping the smooth structure. A rational
function with the endpoint logarithm in its denominator is a candidate
response ansatz, not a result established here. Then investigate how the
exact cap-reflection prime operator changes both the constrained operator
and the scalar coupling. None of (1)–(6) establishes a joint first-prime
factor, an all-length positivity theorem, or a new arithmetic selection rule.
