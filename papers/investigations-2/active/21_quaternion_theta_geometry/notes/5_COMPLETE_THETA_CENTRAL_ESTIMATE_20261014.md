# A complete theta estimate on the central spectral domain

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.

The complete theta source gives an explicit physical norm gap for the
adopted Fueter field:

\[
\boxed{|F(t,x)|>\frac1{120000}
\quad(0\le t\le1,\ |x|\le8).}
\tag{1}
\]

This is an analytic estimate with every theta index and integration tail
included. It does not use Fourier sign samples or a table of zeta zeros.
Its bounded spectral domain leaves the high-height RH target open.

## Source and signed moment target

Use the normalization and independent-time lift in
[Note 3](3_STANDARD_FUETER_LIFT_WITH_INDEPENDENT_TIME_20261014.md). Put

\[
\Phi(r)=\sum_{n\ge1}\phi_n(r),\qquad
\phi_n(r)=(2\pi^2n^4e^{9r}-3\pi n^2e^{5r})
e^{-\pi n^2e^{4r}},\qquad r\ge0,
\]
\[
w_t(r)=e^{tr^2}\Phi(r),\qquad
M_j(t)=\int_0^\infty r^jw_t(r)\,dr.
\]

Every summand is positive on this half-line. The quantitative source
estimate proved below is

\[
\boxed{M_2(t)-\frac{25}{2}M_4(t)
>\frac{2413193}{268912000000}>\frac1{120000},
\qquad 0\le t\le1.}
\tag{2}
\]

The negative fourth-moment payment is retained. No nonnegative square is
substituted for that signed integral.

## Positive core of the complete source

For \(0\le r\le1/10\), retain the first positive theta summand and write

\[
q=\pi e^{4r},\qquad
\phi_1(r)=e^r g(q),\qquad g(q)=q(2q-3)e^{-q}.
\]

Here \(3<q<33/7\), using \(\pi<22/7\) and \(e^{2/5}<3/2\).
Moreover

\[
g'(q)=-(2q-1)(q-3)e^{-q}<0.
\]

Since \(e<11/4\) and \(e^{2/7}>9/7\),

\[
\Phi(r)\ge\phi_1(r)>g(33/7)
>\frac{1485}{49}\frac97\left(\frac4{11}\right)^5
>\frac6{25}.
\tag{3}
\]

Thus the core has a uniform positive lower bound, with no subtraction of
the remaining positive indices.

## Entire tail of the heated source

For y=\(\pi e^{4r}\ge\pi\), successive terms of
\(n^4e^{-yn^2}\) have ratio at most \(16e^{-3\pi}<1/2\).
Dropping the negative term inside each \(\phi_n\) and summing the full
geometric majorant gives

\[
\Phi(r)<4\pi^2e^{9r-\pi e^{4r}}.
\tag{4}
\]

Take \(b=7/25\) and \(L_t(r)=9r+tr^2-\pi e^{4r}\).
The elementary inequalities \(e^{28/25}>153/50\), \(\pi>25/8\) give,
uniformly for \(0\le t\le1\),

\[
L_t(b)<\frac{1624}{625}-\frac{153}{16}<-\frac{69}{10},
\qquad
L_t'(b)<9+\frac{14}{25}-\frac{153}{4}<-28,
\]
\[
L_t''(r)=2t-16\pi e^{4r}<0\quad(r\ge b).
\]

Finally \(4\pi^2<40\) and

\[
e^{69/10}>\left(\frac83\right)^6
\left(1+\frac9{10}+\frac12\left(\frac9{10}\right)^2\right)>800.
\]

The complete tail therefore satisfies

\[
\boxed{w_t(r)<\frac1{20}e^{-28(r-b)}
\quad(r\ge b,\ 0\le t\le1).}
\tag{5}
\]

## Signed moment with its negative tail paid

On \([0,b]\), the factor \(r^2(1-25r^2/2)\) is nonnegative.
Beyond b it has the lower bound

\[
r^2(1-25r^2/2)\ge-\frac{25}{2}r^2(r^2-b^2),
\]

because \(1-25b^2/2=1/50>0\). Use (3) on the core, discard only
the nonnegative remainder inside \([0,b]\), and use (5) for the negative
tail. This gives

\[
M_2-\frac{25}{2}M_4
>\frac6{25}\int_0^{1/10}r^2(1-25r^2/2)\,dr-\frac58I,
\]
\[
I=\int_b^\infty r^2(r^2-b^2)e^{-28(r-b)}\,dr
=\frac{2b^3}{28^2}+\frac{10b^2}{28^3}
+\frac{24b}{28^4}+\frac{24}{28^5}
=\frac{3497259}{33614000000}.
\]

The exact retained difference is
\(37/500000-(5/8)I=2413193/268912000000\), proving (2).

## Physical slope, curvature and norm bounds

For all real y, \(\cos y\ge1-y^2/2\). Integrating this inequality
once gives \(\sin y\ge y-y^3/6\) for all y\(\ge0\).
These are global inequalities; their use does not discard oscillatory
tails. Equation (2) implies

\[
-H_{xx}(t,x)\ge M_2-\frac{x^2}{2}M_4>\frac1{120000}
\quad(|x|\le5),
\tag{6}
\]
\[
-H_x(t,x)\ge x\left(M_2-\frac{x^2}{6}M_4\right)
>\frac{x}{120000}
\quad(0<x\le8).
\tag{7}
\]

The latter actually holds through \(x=5\sqrt3\); the rational endpoint
8 is used here. Reflection handles negative x.

For \(|x|\le1\), the core has \(\cos(xr)\ge199/200\), and the
discarded interval \([1/10,b]\) still has \(\cos(xr)>0\).
The complete remaining tail costs at most \(1/560\). Hence

\[
H(t,x)>\frac{597}{25000}-\frac1{560}
=\frac{7733}{350000}>\frac1{50}.
\tag{8}
\]

For \(|x|\le1\), (8) bounds the scalar component. For
\(1\le|x|\le8\), (7) bounds the derivative component.
Since \(|F(t,x)|^2=H^2+H_x^2\), these prove (1).

On \(|x|\le5\), the only \(H_x=0\) point is x=0, while
\(H_{xx}=0\) has no points. At the origin, source positivity gives
\(H(t,0)>3/125\), and (2) gives \(M_2>1/120000\). Consequently

\[
\boxed{\mathscr L_0(t,0)=H(t,0)M_2(t)>
\frac1{5000000}.}
\tag{9}
\]

Thus both stationary targets are covered on this bounded domain: the
first has a strict origin margin and the second stationary set is empty.
The [Euler stationary control](../../20_constrained_operator_squares/notes/2_CERTIFIED_STATIONARY_THETA_AND_EULER_CONTROLS_20261014.md)
has \(H_x=0,H_{xx}>0\) inside this central region and fails the source
concentration conclusion. No preservation of the theta tail envelope is
asserted for that shifted source.

## Verification and remaining domain

The [exact checker](../numerics/check_theta_central_moment_bound.py) and
[small execution record](../numerics/THETA_CENTRAL_MOMENT_BOUND_20261014.json)
verify the rational constants using finite exponential-series bounds.
The complete source inequalities and their implications are analytic
arguments above, internally cross-checked in the
[review](../reviews/3_THETA_SPECIFIC_ESTIMATES_INTERNAL_REVIEW_20261014.md).
No numerical quadrature or finite theta-tail assumption decides the sign.

This estimate uses quantitative concentration of the complete theta
source, not full imaginary-gluing rigidity. It is a bounded check of the
physical observation; it does not address unknown high-height collisions.
The [companion gluing note](6_IMAGINARY_GLUING_STABILITY_AND_HEIGHT_OBSTRUCTION_20261014.md)
gives an actual arithmetic defect estimate, a robust version of this
bounded norm gap, and the obstruction to extending an absolute bound to
all heights.
