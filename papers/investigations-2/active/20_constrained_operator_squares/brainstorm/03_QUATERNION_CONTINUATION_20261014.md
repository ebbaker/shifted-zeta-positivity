# Continuation of the quaternion research lead

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.

Continue the quaternion branch of investigation 20 in a new conversation.
The immediate question is whether its exact first-order rewriting exposes
a theta-specific signed identity. The quaternion packaging and operator
identities below have been checked; no required arithmetic sign estimate
has yet been obtained.

## Read first and preserve the scope

Work in `/Users/ebbaker/Documents/shifted-zeta-positivity` and follow its
`AGENTS.md`, `LARGE_FILES.md`, and `tools/CHAT_HISTORY.md`. A new research
chat should normally register in this investigation's `chat-histories/`,
unless its own existing registration determines another destination.

Read these sources in order:

1. [Quaternion brainstorm note](02_QUATERNION_JET_AND_HEAT_OPERATOR_20261014.md).
2. [Investigation overview](../README.md) and the background, stationary-sign,
   bounded-loss, and bottleneck sections of the
   [current manuscript](../manuscript/constrained_operator_squares.tex).
3. [Vertical-path lead](01_VERTICAL_SPECTRAL_PATHS_20261014.md) and the
   [detailed complex Laguerre note](../notes/COMPLEX_LAGUERRE_AND_VERTICAL_PATH_CRITERIA_20261014.md),
   if pursuing a whole-plane sign target.

Keep the continuation formula-focused. Numerical results should only be
mentioned through references to their dedicated notes. Save research
extensions in `notes/`, tentative leads in `brainstorm/`, and assessments
in `reviews/`. Revise the existing manuscript only if asked; create no
replacement manuscript or snapshot folder. The quantum-energy branch is
outside this handoff's scope.

## Scalar setup and quaternion convention

Here z always denotes the spectral variable. The theta heat family is
jointly entire in complex t,z:

\[
H(t,z)=\int_0^\infty e^{tr^2}\Phi(r)\cos(zr)\,dr,
\qquad H(0,z)=\frac18\xi\left(\frac12+\frac{iz}{2}\right),
\qquad \partial_tH=-\partial_z^2H.
\]

The manuscript fixes the positive theta source \(\Phi\). Reality and evenness
hold at real Newman time. RH is equivalent to all zeros of H(0,z) being
real. Define

\[
u=h_0=H,\quad v=h_1=H_z,\quad f=u+\mathbf jv,
\qquad u_z=v,\quad u_t=-v_z.
\]

Both fields share the same independent variables. Use Hamilton units
\(\mathbf i^2=\mathbf j^2=\mathbf k^2=\mathbf i\mathbf j\mathbf k=-1\),
with the original complex i identified with \(\mathbf i\). The bold
\(\mathbf j\) is a quaternion unit; the plain index j below is a derivative
level. Right complex coefficients satisfy
\(\mathbf ja=\overline a\,\mathbf j\) for \(a\in\mathbb C_i\).
All complex derivatives of f are componentwise.

## Exact equations already available

Write \(t=s+ia\), \(z=x+iy\), and identify
\(q=t+\mathbf jz=s+\mathbf ia+\mathbf jx-\mathbf ky\).
Component holomorphy gives \(f_a=f_s\mathbf i\),
\(f_y=f_x\mathbf i\), and \(\partial_tf=\partial_sf\). With left
multiplication in the Fueter operators,

\[
D_F=\partial_s+\mathbf i\partial_a+\mathbf j\partial_x-\mathbf k\partial_y,
\qquad
D_F^-=\partial_s-\mathbf i\partial_a-\mathbf j\partial_x+\mathbf k\partial_y,
\]
\[
D_Ff=-2v_x+2\mathbf jv_s=2f_s,
\qquad \boxed{\partial_tf=\tfrac12D_Ff},
\qquad \boxed{D_F^-f=0}.
\]

Under component holomorphy, \(D_F^-f=2(u_s+v_x)\). Thus this equation
encodes the heat relation, while \(u_z=v\) remains an independent
constraint. The simple two-term operator \(\partial_t+\mathbf j\partial_x\)
does not give this evolution. Also
\(D_FD_F^-=\Delta_{\mathbb R^4}\), which is a full Laplacian square.

The matrix operator instead retains both jet equations and squares to heat:

\[
\mathcal D=
\begin{pmatrix}\partial_z&-1\\-\partial_t&-\partial_z\end{pmatrix},
\qquad
\mathcal D\binom uv=0,
\qquad
\mathcal D^2=(\partial_t+\partial_z^2)I.
\]

It acts on a complex pair, equivalently through endomorphisms of quaternion
values. Its nilpotent coefficient matrices should not be identified with
fixed Hamilton quaternion units. These are reformulations, with no novelty
claim or selfadjointness or positivity assumption attached to the factors.

## Signed components and the actual targets

Set \(h_j=\partial_z^jH\) and
\(\mathscr L_j=h_{j+1}^2-h_jh_{j+2}\). Quaternion conjugation gives

\[
\overline f\,f_z
=\overline H H_z+\overline{H_z}H_{zz}-\mathbf j\mathscr L_0,
\]
\[
\overline{f_z}\,f_{zz}
=\overline{H_z}H_{zz}+\overline{H_{zz}}H_{zzz}
-\mathbf j\mathscr L_1,
\]
\[
\overline{\partial_tf}\,f_z
=\overline{\partial_tH}H_z+
\overline{\partial_t\partial_zH}H_{zz}-\mathbf j\mathscr L_1,
\qquad
\det_{\mathbb C}\frac{\partial(H,H_z)}{\partial(t,z)}=-\mathscr L_1.
\]

On real t,x these quaternion components are signed oriented areas.
Taking norms loses the orientation. The useful norm is the existing energy
\(\mathcal E=|f|^2=|H|^2+|H_z|^2\).

The collision route in the manuscript seeks the real stationary signs

\[
H_x=0\ \Longrightarrow\ \mathscr L_0\ge0,
\qquad
H_{xx}=0\ \Longrightarrow\ \mathscr L_1\ge0
\]

on open predecessor neighborhoods through potential positive-time
collisions. A weaker sufficient target is
\(\mathscr L_0\ge-C_0\mathcal E\) on H_x=0 and
\(\mathscr L_1\ge-C_1\mathcal E\) on H_xx=0, where nonnegative
\(C_0,C_1\) stay locally bounded through every candidate joint zero.
This permits a possible norm-based estimate without requiring a perfect
nonnegative square; uncontrolled division by f or its norm cannot supply
that boundedness at a collision.

For the whole-plane alternative, keep t real and distinguish the real
Hermitian curvature

\[
\mathcal C_j(t,z)=|h_{j+1}|^2-\operatorname{Re}(h_{j+2}\overline{h_j})
=\frac12\partial_y^2|h_j(t,x+iy)|^2
\]

from the holomorphic bilinear \(\mathscr L_j\). They agree on the real
slice. Nonnegativity of \(\mathcal C_0(0,z)\) throughout the spectral
plane is equivalent to RH. A quaternion coefficient equal to
\(-\mathscr L_j\) does not automatically give a sign for \(\mathcal C_j\).
The scalar modulus \(|H|^2\) cannot be replaced by the total norm
\(|f|^2\) in this criterion.

## A control that every proposed mechanism must distinguish

The polynomial \(H(t,z)=z^2-2t+1\), \(v=2z\), satisfies all the heat,
jet, Fueter, and matrix identities above. Nevertheless H(0,z) has zeros
\(\pm i\), even though \(\mathscr L_1=4\) and the complex Jacobian never
vanishes. Moreover, at t=0,

\[
\frac12\partial_y^2|H|^2=2x^2+6y^2-2,
\qquad
\frac12\partial_y^2|f|^2=2x^2+6y^2+2>0.
\]

Thus even vertical convexity of the quaternion total norm is insufficient.
This is a test of a proposed general implication, not a theta-source
counterexample. Full-Laplacian subharmonicity is also weaker than the
required directional curvature sign.

## Suggested starting tasks for the next conversation

1. Re-derive the convention-sensitive equations and quaternion products
   before building further operators. Preserve the jet constraint.
2. Choose one concrete target: a signed stationary component, a locally
   bounded loss estimate, or the Hermitian spectral curvature. State the
   real slice, domain, source constraint, and normalization explicitly.
3. Look for an exact current or boundary identity in the quaternion or
   matrix formulation that uses the complete theta preparation. Retain
   every oscillatory term and remainder; assess how its proposed sign
   distinguishes the polynomial control and the existing source controls.
4. If seeking a square, identify the operator domain, adjoint, and signed
   observation it controls. A formal heat factorization or positive norm
   alone does not settle that observation. The existing full-core local
   multiplier obstruction remains relevant.

The next deliverable should be a short formula note containing either a
specific candidate identity with its unresolved sign term, or a precise
obstruction for a declared operator class. Avoid treating an equivalent
rewriting as a new positivity theorem.
