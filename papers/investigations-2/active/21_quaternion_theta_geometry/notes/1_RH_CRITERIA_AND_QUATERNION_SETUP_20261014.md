# RH criteria and the quaternion theta state

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.

Investigation 21 uses the [standard Fueter lift with independent time](3_STANDARD_FUETER_LIFT_WITH_INDEPENDENT_TIME_20261014.md).
The field F has quaternion argument \(q=z_0+\mathbf jz_1\);
the symbol f below denotes its trace at \(z_1=0\).

This is the formula baseline for investigation 21. It consolidates the
[quaternion proposal](../../20_constrained_operator_squares/brainstorm/02_QUATERNION_JET_AND_HEAT_OPERATOR_20261014.md),
the [continuation handoff](../../20_constrained_operator_squares/brainstorm/03_QUATERNION_CONTINUATION_20261014.md),
and the RH criteria clarified in the founding conversation. The
equivalences below use the genuine theta family and its stated analytic
inputs; they do not provide the missing arithmetic sign theorem.

## Scalar source and quaternion conventions

Fix the complete theta source

\[
\Phi(r)=\sum_{n\ge1}
\bigl(2\pi^2n^4e^{9r}-3\pi n^2e^{5r}\bigr)
e^{-\pi n^2e^{4r}},\qquad r\ge0,
\]
\[
H(t,z)=\int_0^\infty e^{tr^2}\Phi(r)\cos(zr)\,dr,
\quad H(0,z)=\frac18\xi\!\left(\frac12+\frac{iz}{2}\right),
\quad \partial_tH=-\partial_z^2H.
\]

The source is positive and has an even extension. Its double exponential
decay makes H jointly entire in complex t,z. At real t, each slice is
real entire, even, of order at most one, with \(H(t,0)>0\).
Every zero has finite spatial multiplicity.

Use Hamilton units \(\mathbf i,\mathbf j,\mathbf k\), identify the
original complex i with \(\mathbf i\), and put

\[
u=H,\quad v=H_z,\quad f=u+\mathbf jv,
\qquad u_z=v,\quad u_t=-v_z.
\]

The coefficients lie in \(\mathbb C_i\), on the right of the basis
units, and \(\mathbf ja=\overline a\,\mathbf j\).
Complex derivatives of f are componentwise. The derivative-level index
j below is distinct from the quaternion unit \(\mathbf j\).

## Standard Fueter lift with time separate

Write \(q=z_0+\mathbf jz_1\), with \(z_0=a+ib\) and \(z_1=c+id\).
In real quaternion coordinates q is \(a+\mathbf ib+\mathbf jc-\mathbf kd\),
so the usual normalized left operator is

\[
\bar\partial_q=\frac12(\partial_a+\mathbf i\partial_b
+\mathbf j\partial_c-\mathbf k\partial_d).
\]

Keep t as an independent real parameter and define

\[
\tau=t+\overline{z_1},\qquad
U=H(\tau,z_0),\quad V=H_z(\tau,z_0),\quad F(t,q)=U+\mathbf jV.
\]

The general component formula is

\[
\bar\partial_qF=U_{\bar z_0}-V_{z_1}
+\mathbf j(V_{z_0}+U_{\bar z_1}).
\]

Here the first two terms vanish and the last pair is
\(H_{zz}+H_\tau=0\). Thus F is standard left Fueter-regular for
each real t, while retaining \(U_{z_0}=V\) throughout quaternion
space and the external evolution
\(\partial_tF=-\partial_{z_0}^2F\).
The [convention note](3_STANDARD_FUETER_LIFT_WITH_INDEPENDENT_TIME_20261014.md)
gives the derivation and the failure of separated evaluation.

On \(z_1=0\), the trace is the original state
\(f(t,z)=F(t,z)=H(t,z)+\mathbf jH_z(t,z)\), so its products below
retain their signs. For real quaternion argument q=x,
\(F(t,x)=H(t,x)+\mathbf jH_x(t,x)\).

The old embedding \(q=t+\mathbf jz\) in investigation 20 used
complexified time as a quaternion coordinate and a conjugate Fueter
operator. It is a separate exact rewriting, not this convention.
For the usual operator and its conjugate,
\(4\partial_q\bar\partial_q=\Delta_{\mathbb R^4}\);
this factorization does not itself control the physical sign.

The complex matrix formulation retains both equations:

\[
\mathcal D=\begin{pmatrix}\partial_z&-1\\-\partial_t&-\partial_z\end{pmatrix},
\qquad \mathcal D\binom uv=0,
\qquad \mathcal D^2=(\partial_t+\partial_z^2)I.
\]

Its nilpotent coefficient matrices are endomorphisms of the complex pair,
not fixed Hamilton quaternion units. These factorizations do not by
themselves specify a selfadjoint operator, a positive quadratic form,
or a sign for the physical observation.

## Exact RH endpoint through positive time

The normalization identifies RH with all zeros of \(H(0,\cdot)\)
being real. For the genuine theta flow, the
[manuscript's collision reduction](../../20_constrained_operator_squares/manuscript/constrained_operator_squares.tex)
gives

\[
\boxed{\mathrm{RH}\iff
H(t,x)=H_x(t,x)=0\text{ has no solution with }t>0,\ x\in\mathbb R.}
\]

Since f(t,x) equals F(t,x) for real x, the quaternion endpoint is

\[
\boxed{\mathrm{RH}\iff f(t,x)\ne0\text{ for every }t>0,\ x\in\mathbb R}
\quad\iff\quad
\mathcal E(t,x)=H(t,x)^2+H_x(t,x)^2>0
\text{ throughout that domain}.
\]

This is pointwise nonvanishing; it requires no uniform positive lower
bound for \(\mathcal E\). It allows multiple real zeros at t=0.
At time zero, nonvanishing of \(f(0,x)\) only excludes multiple real
zeros and does not exclude simple nonreal zeros of H.

The imported ingredients are the de Bruijn--Newman threshold, uniform
localization of nonreal zeros at times bounded away from zero, and local
Hermite splitting at a multiple real zero. If RH fails, the positive
threshold has a finite common real zero. If RH holds, a positive-time
multiple zero would force a nonreal zero at a slightly earlier positive
time. These inputs are identified in the manuscript and
[Polymath's heat-flow paper](https://arxiv.org/abs/1904.12438v2).

## Signed quaternion observations and stationary criteria

Set \(h_j=\partial_z^jH\) and
\(\mathscr L_j=h_{j+1}^2-h_jh_{j+2}\).
Quaternion conjugation gives

\[
\overline f\,f_z
=\overline H H_z+\overline{H_z}H_{zz}-\mathbf j\mathscr L_0,
\]
\[
\overline{f_z}\,f_{zz}
=\overline{H_z}H_{zz}+\overline{H_{zz}}H_{zzz}-\mathbf j\mathscr L_1,
\]
\[
\overline{\partial_tf}\,f_z
=\overline{\partial_tH}H_z+
\overline{\partial_tH_z}H_{zz}-\mathbf j\mathscr L_1,
\qquad
\det_{\mathbb C}\frac{\partial(H,H_z)}{\partial(t,z)}=-\mathscr L_1.
\]

On real t,x the coefficients are real and the quaternion components carry
oriented signs. Norms or the squared real Jacobian
\(|\mathscr L_1|^2\) lose those signs.

The collision-excluding targets are

\[
H_x=0\ \Longrightarrow\ \mathscr L_0=-HH_{xx}\ge0,
\qquad
H_{xx}=0\ \Longrightarrow\ \mathscr L_1=-H_xH_{xxx}\ge0.
\]

If these hold on an open positive-time domain, they exclude common zeros
within that domain. For RH, the domain must cover every possible positive
threshold collision and its predecessor curves. Along a differentiable
stationary curve \(x_j(t)\) of \(h_j\), the unnormalized heat equation gives

\[
\frac12\frac{d}{dt}h_j(t,x_j(t))^2=\mathscr L_j(t,x_j(t)),\qquad j=0,1.
\]

An even multiple zero of H has a predecessor stationary branch of H with
\(HH_{xx}>0\). An odd multiple zero of order at least three has a
predecessor stationary branch of \(H_x\) with \(H_xH_{xxx}>0\).
The two signs exclude these respective branches. A sign only at the
collision is insufficient: the products \(HH_{xx}\) and
\(H_xH_{xxx}\) vanish there. At a double zero,
\(\mathscr L_1=H_{xx}^2>0\); that point is not on the second stationary
set \(H_{xx}=0\). The contradiction comes from the predecessor branch.

## Locally bounded stationary loss

Use \(K_0,K_1\) for the nonnegative loss coefficients, reserving
\(\mathcal C_j\) for spectral curvature. A weaker sufficient target is

\[
H_x=0\ \Longrightarrow\ \mathscr L_0\ge-K_0\mathcal E,
\qquad
H_{xx}=0\ \Longrightarrow\ \mathscr L_1\ge-K_1\mathcal E.
\]

Each \(K_j\) must remain locally bounded through candidate joint zeros
on an open domain covering the predecessor curves. At an even collision
of order \(2r\), its predecessor branch has
\(-\mathscr L_0/\mathcal E=r/(T-t)+O(1)\). At an odd collision of
order \(2r+1\), the corresponding branch has
\(-\mathscr L_1/\mathcal E=r/(T-t)+O(1)\). Either divergence contradicts
the proposed bounded loss. Division occurs only along branches where
\(\mathcal E>0\); defining an uncontrolled quotient at the collision
does not establish boundedness. The detailed proof is in the
[bounded-loss section](../../20_constrained_operator_squares/manuscript/constrained_operator_squares.tex)
of investigation 20's manuscript.

## Exact spectral curvature alternative

Keep t real, let \(z=x+iy\), and define

\[
\mathcal C_j(t,z)=|h_{j+1}|^2-\operatorname{Re}(h_{j+2}\overline{h_j})
=\frac12\partial_y^2|h_j(t,x+iy)|^2.
\]

For this theta family,

\[
\boxed{\mathrm{RH}\iff\mathcal C_0(0,z)\ge0\text{ for every }z\in\mathbb C.}
\]

Equivalently, \(\partial_y|H(0,x+iy)|^2\ge0\) for every real x and
y>0. The real-entire growth class is important for necessity. Under RH,
the paired canonical product is a locally uniform limit of real-rooted
polynomials, whose vertical squared moduli are products of
\((x-\rho)^2+y^2\), hence convex. For sufficiency, a nonreal zero and
its conjugate would force the nonnegative convex vertical squared modulus
to vanish throughout the interval between them, contradicting the identity
theorem. See the
[detailed vertical-path note](../../20_constrained_operator_squares/notes/COMPLEX_LAGUERRE_AND_VERTICAL_PATH_CRITERIA_20261014.md)
and [Csordas and Escassut, Theorems 2.3 and 2.4](https://www.numdam.org/item/AMBP_2005__12_2_331_0.pdf).

On the real slice \(\mathcal C_j=\mathscr L_j\), but away from it
\(\mathscr L_j\) is complex and is not the Hermitian observation.
Moreover,

\[
\frac12\partial_y^2|f|^2=\mathcal C_0+\mathcal C_1.
\]

Convexity of the sum cannot establish the required sign of
\(\mathcal C_0\). Signs on the pure imaginary axis also do not cover
all translated vertical lines.

## Polynomial control

Let \(P(t,z)=z^2-2t+1\) and \(f_P=P+\mathbf jP_z\). P and its
first jet satisfy the heat, jet, and matrix equations. Their coupled lift
\(F_P\) is standard left Fueter-regular, as shown in the
[convention note](3_STANDARD_FUETER_LIFT_WITH_INDEPENDENT_TIME_20261014.md).
Nevertheless P(0,z) has
zeros \(\pm i\), while \(\mathscr L_1(P)=4\) and its complex Jacobian
does not vanish. At t=0,

\[
\mathcal C_0(P)=2x^2+6y^2-2,
\qquad \frac12\partial_y^2|f_P|^2=2x^2+6y^2+2>0.
\]

The exact endpoint correctly detects its collision:
\(f_P(1/2,0)=0\). For \(h=1/2-t>0\), at x=0,
\(\mathscr L_0(P)=-4h\), \(\mathcal E_P=4h^2\), and
\(-\mathscr L_0(P)/\mathcal E_P=1/h\).
Thus the identities, \(\mathscr L_1\) alone, and norm convexity cannot
provide a general certificate. This is a heat-equation control, not a
counterexample to a theorem using the complete theta source.

## Remaining arithmetic obligation

Derive an identity or estimate that controls a declared signed observation
using complete theta information, with every oscillatory contribution and
boundary term retained. A local sign certificate must state its coverage;
a whole-plane criterion must control \(\mathcal C_0\) itself. The initial
[research program](2_INITIAL_RESEARCH_PROGRAM_20261014.md) makes the first
construction task and its validation conditions explicit.
