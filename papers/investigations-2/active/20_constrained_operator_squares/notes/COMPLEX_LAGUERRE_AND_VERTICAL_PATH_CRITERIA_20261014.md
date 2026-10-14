# Complex Laguerre criteria and vertical spectral paths

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.

Status: formula-level reformulation and independent derivation, with a
cross-check of the classical complex Laguerre criteria. No numerical
claims, new positivity certificate, or manuscript revision is made here.
This note records the author's question about imaginary spectral paths.

## 1. Fix real Newman time; complexify the spectral variable

Use the setup in the [current manuscript](../manuscript/constrained_operator_squares.tex):

\[
f(z)=H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\qquad t\in\mathbb R,
\qquad \partial_tH=-\partial_z^2H.
\]

All time derivatives use partial-derivative notation; subscripts on
M_t below label a time slice. For a fixed real time, f is nonzero, real
entire and even.
The theta source's double exponential decay gives a bound of the form
\(\log\max_{|z|\le r}|f(z)|\le C_t(1+r\log(2+r))\), so its order is at
most one. Its value at zero is strictly positive.

Define the real nonnegative observation

\[
M_t(x,y)=|H(t,x+iy)|^2,
\qquad x,y\in\mathbb R.
\]

It is even in y by Schwarz reflection. Positivity is imposed on this
real observation with t real; it is not a proposed ordering of complex
values or of complex Newman time.

## 2. Exact equivalent conditions

For this fixed-time function, the following conditions are equivalent:

1. All spectral zeros of f are real.
2. \(\partial_y M_t(x,y)\ge0\) for every x and every y>0.
3. \(\partial_y^2 M_t(x,y)\ge0\) for all real x,y.
4. \(-\operatorname{Im}(f'(z)/f(z))\ge0\) for every z in the upper
   half-plane where the quotient is defined.

The division-free formulas are

\[
\partial_y M_t=-2\operatorname{Im}(f'(z)\overline{f(z)}),
\qquad
\frac12\partial_y^2 M_t
=|f'(z)|^2-\operatorname{Re}(f''(z)\overline{f(z)}).
\tag{1}
\]

These whole-plane inequalities are the classical complex Laguerre
criteria. A primary reference is G. Csordas and A. Escassut,
[*The Laguerre inequality and the distribution of zeros of entire functions*](https://www.numdam.org/item/AMBP_2005__12_2_331_0.pdf),
Annales mathematiques Blaise Pascal 12 (2005), 331--345, Theorems 2.3--2.4.
Their stated class includes a nonpositive quadratic exponential and a
bounded zero strip. The following direct argument uses only the
order-at-most-one factorization and reality of f.

At t=0, each of these conditions is therefore equivalent to RH under the
manuscript's normalization \(H(0,z)=\xi(1/2+iz/2)/8\). At general real t,
each is equivalent to the corresponding slice having only real zeros.

### Independent proof in this setting

If all zeros are real, evenness and the order bound give the paired
product

\[
f(z)=f(0)\prod_{\gamma>0}(1-z^2/\gamma^2),
\]

with multiplicities and \(\sum\gamma^{-2}<\infty\). Every finite product
has squared modulus along a vertical line equal to a positive constant
times a product of factors \(((x-\rho)^2+y^2)\). This is a polynomial in
y squared with nonnegative coefficients. It is nondecreasing for y>0
and convex for all y. Local uniform convergence, including derivatives,
passes these inequalities to f.

Conversely, if f(a+ib)=0 with b>0, vertical nondecrease and M_t>=0 force
M_t(a,y)=0 throughout 0<y<b. The identity theorem contradicts f being
nonzero. Convexity gives the same contradiction because reflection also
gives M_t(a,-b)=0, and a nonnegative convex function must vanish on the
interval between these endpoints. Thus either condition excludes every
nonreal zero.

Away from the zeros, division of the first identity in (1) by 2M_t
identifies condition 4 with condition 2. Any upper-half-plane zero makes
the imaginary part of its logarithmic-derivative pole take both signs
nearby, so condition 4 cannot silently admit a pole. Under real-rootedness,
the partial-fraction identity is

\[
-\operatorname{Im}\frac{f'(x+iy)}{f(x+iy)}
=\sum_{\rho\in\mathbb R}\frac{y}{(x-\rho)^2+y^2}>0,
\qquad y>0,
\]

where the sum includes multiplicities. This is a consequence of
real-rootedness, not a representation available for proving it without
further work. In Herglotz terminology, -f'/f then maps the upper
half-plane into itself. The division-free versions avoid assuming
zero-freeness before proving it.

The growth hypothesis matters for the necessity direction: the real,
zero-free entire function \(e^{z^2}\) has vertically decreasing modulus.
The converse implications from nondecrease or convexity do not require
that growth hypothesis.

## 3. Relation to the existing derivative-level expressions

For fixed real x, elementary Taylor expansion gives

\[
|f(x+iy)|^2=f(x)^2+y^2\bigl(f'(x)^2-f(x)f''(x)\bigr)+O(y^4).
\tag{2}
\]

Apply (2) to \(f=h_j=\partial_z^jH(t,\cdot)\). Its coefficient of y
squared is precisely the manuscript's
\(\mathscr L_j=(H^{(j+1)})^2-H^{(j)}H^{(j+2)}\).
Higher even-power coefficients are the generalized Laguerre expressions;
their coefficient index is distinct from the manuscript's derivative-level
index j.

Equivalently, the continuous boundary value of
\(\partial_y|h_j(x+iy)|^2/(2y)\) is \(\mathscr L_j(t,x)\).
The complex curvature expression for H itself is

\[
\mathcal C_0(t,z)
=|H_z(t,z)|^2+\operatorname{Re}(\partial_tH(t,z)\overline{H(t,z)}).
\]

It agrees with \(\mathscr L_0\) at real z. Replacing H by H_z gives
\(\mathcal C_1=|\partial_tH|^2+
\operatorname{Re}(\partial_tH_z\,\overline{H_z})\), with boundary value
\(\mathscr L_1\). Real-rootedness of a fixed time slice implies these
signs for all its derivative fields; in particular, RH implies them at
t=0. Real-rooted functions of this growth class remain in the
Laguerre--Polya class under differentiation. For the whole-plane
criterion, H alone suffices; the two stationary levels are a separate,
more economical collision target on real predecessor neighborhoods.

## 4. The pure imaginary axis is already positive

Source positivity directly gives

\[
H(t,iy)=\int_0^\infty e^{tu^2}\Phi(u)\cosh(yu)\,du>0,
\]
\[
\partial_yH(t,iy)=\int_0^\infty u e^{tu^2}\Phi(u)\sinh(yu)\,du>0
\quad(y>0).
\]

The same differentiation gives positive second derivative. Hence the
vertical monotonicity and convexity requirements at x=0 already hold,
without establishing where the other zeros lie. The equivalent criterion
requires every translated vertical line x+iy. Values on a single line
determine the entire function analytically, but these particular sign
properties on that line do not supply the global condition.

## 5. Forward heat and the remaining sign term

Put \(F(t,x,y)=H(t,x+iy)\). Holomorphy and the physical heat equation imply

\[
\partial_tF=\partial_y^2F.
\tag{3}
\]

Thus imaginary spectral displacement turns the physical backward heat
into forward heat in y. However, its squared modulus satisfies

\[
\partial_tM=\partial_y^2M-2|\partial_yF|^2.
\tag{4}
\]

For the desired vertical derivative \(W=\partial_yM\),

\[
\partial_tW=\partial_y^2W-2\partial_y|\partial_yF|^2.
\tag{5}
\]

The last forcing term has no general sign. For the curvature
\(C=\partial_y^2M/2\), the corresponding forcing is
\(-\partial_y^2|\partial_yF|^2\). A maximum-principle argument therefore
needs a source-specific estimate, boundary conditions, and growth control;
(3) alone does not propagate the target signs. Moreover, reaching t=0
from a known real-rooted large-time slice runs opposite the forward
Newman-time direction, so forward preservation alone would not establish RH.

## 6. Exact paired-source formulas retain the oscillatory obstacle

Let \(d\nu_t(u)=e^{tu^2}\Phi_e(u)\,du/2\), so that
\(H(t,z)=\int_{\mathbb R}e^{izu}\,d\nu_t(u)\). With
A=u-v and S=u+v, symmetry of this measure gives

\[
M_t(x,y)=\iint\cos(xA)\cosh(yS)\,d\nu_t(u)d\nu_t(v).
\]

Consequently,

\[
\frac{\partial_yM_t}{2y}
=\frac12\iint\cos(xA)\frac{S\sinh(yS)}{y}\,d\nu_t(u)d\nu_t(v),
\]
\[
\mathcal C_0(t,x+iy)
=\frac12\iint\cos(xA)S^2\cosh(yS)\,d\nu_t(u)d\nu_t(v).
\tag{6}
\]

The first kernel has its continuous limit \(S^2\) at y=0. The
hyperbolic factors are nonnegative, but cos(xA) retains the signed
observation. These formulas explain both the automatic x=0 signs and
the failure of source positivity alone to settle every vertical line.
A useful constructive task would be an arithmetic identity for (6), or
for the forcing in (5), retaining the complete theta constraints and
all remainders. This records a possible direction rather than a proved
factorization or a decision to launch a new program.
