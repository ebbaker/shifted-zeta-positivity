# Quaternion jet and heat operator as a geometric lead

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.

The author's proposal packages the two derivative fields into one
quaternion. It admits an exact first-order formulation and makes the
Laguerre expressions signed quaternion components. Establishing their
sign requires information beyond this packaging.

## Components and multiplication convention

Use Hamilton units \(i^2=j^2=k^2=ijk=-1\), embed the original complex
numbers as \(\mathbb C_i\), and put

\[
u=H(t,z),\qquad v=H_z(t,z),\qquad f=u+jv,
\qquad u_z=v,\quad u_t=-v_z.
\]

Both coefficients are jointly entire in the same complex variables t,z.
Here j is a quaternion unit, unrelated to the derivative-level index.
The side matters: \(ja=\overline a\,j\) for \(a\in\mathbb C_i\), and

\[
jf=-v+ju,\qquad fj=-\overline v+j\overline u.
\]

All complex derivatives of f mean componentwise derivatives. If
\(t=s+ia\) and \(z=x+iy\), holomorphy reads
\(f_a=f_si\) and \(f_y=f_xi\): common complex multiplication acts on the
right. For example, on the real slice the proposed two-term operator gives

\[
(\partial_t+j\partial_x)f=2u_t+j(v_t+v),
\]

which is generally different from \(\partial_tf=u_t+jv_t\).

## An exact four coordinate quaternion equation

Identify the input quaternion as
\(q=t+jz=s+ia+jx-ky\) and use left multiplication in

\[
D_F=\partial_s+i\partial_a+j\partial_x-k\partial_y.
\]

Direct calculation using component holomorphy gives

\[
D_Ff=-2v_x+2jv_s=2f_s,
\qquad\boxed{\partial_tf=\tfrac12D_Ff.}
\]

This is an exact version of the suggested evolution equation. Equivalently,

\[
D_F^-f=0,\qquad
D_F^-=\partial_s-i\partial_a-j\partial_x+k\partial_y.
\]

Under component holomorphy, \(D_F^-f=2(u_s+v_x)\). Hence this equation
encodes the heat relation \(u_t=-v_z\); the jet constraint \(u_z=v\)
must remain imposed separately. The Fueter product
\(D_FD_F^-=\Delta_{\mathbb R^4}\) is a Laplacian factorization.

## A first order operator that squares to heat

A complementary matrix representation retains both equations:

\[
\mathcal D=
\begin{pmatrix}\partial_z&-1\\-\partial_t&-\partial_z\end{pmatrix},
\qquad
\mathcal D\binom uv=0,
\qquad
\boxed{\mathcal D^2=(\partial_t+\partial_z^2)I.}
\]

This acts on the complex coefficient pair, or equivalently by
endomorphisms of quaternion values. Its off-diagonal matrices are
nilpotent; it is not multiplication by fixed Hamilton quaternion units.
[Parabolic Dirac operators](https://onlinelibrary.wiley.com/doi/10.1002/mma.10932)
provide a related literature on first-order factors of heat. The displayed
factorization follows directly by matrix multiplication.

## The determinant as a signed quaternion component

For \(A=a+jb\), \(B=c+jd\), quaternion conjugation gives

\[
\overline A B=(\overline a c+\overline b d)+j(ad-bc).
\]

Thus the determinant observed earlier is present explicitly:

\[
\overline{f_t}f_z
=\overline{H_t}H_z+\overline{H_{tz}}H_{zz}
-j\mathscr L_1,
\qquad
\mathscr L_1=H_{zz}^2-H_zH_{zzz}.
\]

Here \(H_t,H_{tz}\) denote derivatives. The complex Jacobian is
\(\det\partial(H,H_z)/\partial(t,z)=-\mathscr L_1\).
Two further identities recover the derivative-level forms directly:

\[
\overline f f_z
=\overline H H_z+\overline{H_z}H_{zz}-j\mathscr L_0,
\]
\[
\overline{f_z}f_{zz}
=\overline{H_z}H_{zz}+\overline{H_{zz}}H_{zzz}-j\mathscr L_1.
\]

On real t,x the coefficients are real, so these are signed oriented
areas in the (1,j) plane. The quaternion norm instead gives
\(|f|^2=|H|^2+|H_z|^2\), the existing energy. In the usual complex-pair
real coordinates, the real Jacobian is \(|\mathscr L_1|^2\); its magnitude
records invertibility and loses the real-slice Laguerre sign.

## What the rewriting would still need

The elementary control \(H(t,z)=z^2-2t+1\) obeys the heat, jet, and
four-coordinate quaternion equations, with \(\mathscr L_1=4\), while
\(H(0,z)=z^2+1\) has nonreal zeros. These algebraic structures alone are
therefore insufficient. This control tests the rewriting; it is not a
replacement for the theta source.

A possible lead is an arithmetic identity controlling the signed
quaternion components, or the directional curvature in the
[vertical-path criterion](01_VERTICAL_SPECTRAL_PATHS_20261014.md).
Full-Laplacian subharmonicity of a squared norm does not supply the needed
convexity in one imaginary spectral direction.
