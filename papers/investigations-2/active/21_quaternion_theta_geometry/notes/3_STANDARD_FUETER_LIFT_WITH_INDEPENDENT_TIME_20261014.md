# Standard Fueter lift with independent Newman time

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.

The adopted convention keeps Newman time t as an independent real
parameter and writes the quaternion argument as \(q=z_0+\mathbf jz_1\),
with independent complex coordinates \(z_0,z_1\). A coupled extension of
the theta first jet is standard left Fueter-regular and recovers the
physical first jet at real quaternion arguments. Its nonvanishing there
for every positive time is exactly the existing RH collision criterion.

This replaces the mixed time-spectral embedding used in the
[original handoff](../../20_constrained_operator_squares/brainstorm/03_QUATERNION_CONTINUATION_20261014.md)
as investigation 21's working convention. It is an exact reformulation;
the theta-specific estimate excluding zeros remains open.

## Standard operator in the requested complex coordinates

Let \(z_0=a+ib\), \(z_1=c+id\), and use Hamilton units with complex
i identified with \(\mathbf i\). Since the complex coefficient is on
the right of \(\mathbf j\),

\[
q=z_0+\mathbf jz_1=a+\mathbf ib+\mathbf jc-\mathbf kd.
\]

Thus the standard real quaternion coordinates are
\((q_0,q_1,q_2,q_3)=(a,b,c,-d)\). The usual left
Cauchy--Riemann--Fueter operator, normalized by one half, is

\[
\bar\partial_q=\frac12\left(
\partial_{q_0}+\mathbf i\partial_{q_1}
+\mathbf j\partial_{q_2}+\mathbf k\partial_{q_3}\right)
=\frac12\left(\partial_a+\mathbf i\partial_b
+\mathbf j\partial_c-\mathbf k\partial_d\right).
\]

The minus sign on \(\partial_d\) comes from \(q_3=-d\), not from a
different regularity convention. All quaternion units multiply on the
left. A field is left Fueter-regular when \(\bar\partial_qF=0\),
with t held fixed. See
[Perotti, Section 1](https://www.numdam.org/item/10.1016/S1631-073X%2803%2900284-X.pdf)
and the [normalized definition](https://link.springer.com/article/10.1007/s40315-023-00485-5).

For complex-valued U,V, direct quaternion multiplication gives

\[
\bar\partial_q(U+\mathbf jV)
=U_{\bar z_0}-V_{z_1}
+\mathbf j\bigl(V_{z_0}+U_{\bar z_1}\bigr).
\tag{1}
\]

The subscripts here are ordinary Wirtinger derivatives of the complex
coefficients, and t is an independent parameter.

## Why separated evaluation does not supply regularity

The independent-coordinate expression

\[
F_{\mathrm{sep}}(t,q)=H(t,z_0)+\mathbf jH_z(t,z_1)
\]

is well-defined, but (1) gives
\(\bar\partial_qF_{\mathrm{sep}}=-H_{zz}(t,z_1)\), which is generally
nonzero. Its zeros are independent zeros of H and \(H_z\), rather than
zeros of the common first jet. At real \(q=x\), one has \(z_0=x,z_1=0\)
and \(H_z(t,0)=0\), so it reduces to H(t,x) and loses the derivative
component. Restricting instead to \(z_0=z_1=x\) recovers the first jet
but does not make the full separated field regular.

## Coupled heat translation preserves the full first jet

Use the jointly entire theta heat family with
\(\partial_\tau H=-\partial_z^2H\), and put

\[
\tau=t+\overline{z_1},\qquad
U(t,z_0,z_1)=H(\tau,z_0),\qquad
V(t,z_0,z_1)=H_z(\tau,z_0),
\]
\[
\boxed{F(t,q)=H(t+\overline{z_1},z_0)
+\mathbf jH_z(t+\overline{z_1},z_0),
\qquad q=z_0+\mathbf jz_1.}
\tag{2}
\]

The parameter t remains real and independent. The independent coordinate
\(z_1\) acts through a complex heat-time displacement inside H; it is
not a separate spectral evaluation of the derivative field. Joint
entireness makes (2) a globally defined real analytic quaternion field.

Holomorphy of H in its two complex variables gives

\[
U_{\bar z_0}=0,\qquad V_{z_1}=0,\qquad
V_{z_0}=H_{zz}(\tau,z_0),\qquad
U_{\bar z_1}=H_\tau(\tau,z_0).
\]

Consequently (1) and the heat equation give

\[
\boxed{\bar\partial_qF
=\mathbf j\bigl(H_{zz}+H_\tau\bigr)(\tau,z_0)=0.}
\tag{3}
\]

The jet constraint holds throughout quaternion space:
\(U_{z_0}=V\). The field also satisfies, componentwise,

\[
\partial_tF=\partial_{\bar z_1}F=-\partial_{z_0}^{\,2}F.
\tag{4}
\]

Regularity in (3) is unconditional. It uses the heat relation and the
specified coupled extension; it does not assume RH or imply nonvanishing.

## Compact RH criterion at real quaternion arguments

For \(q=x\in\mathbb R\), the quaternion decomposition has
\(z_0=x,z_1=0\). Hence

\[
F(t,x)=H(t,x)+\mathbf jH_x(t,x),\qquad
|F(t,x)|^2=H(t,x)^2+H_x(t,x)^2.
\]

Using the genuine theta family's
[positive-time collision reduction](../../20_constrained_operator_squares/manuscript/constrained_operator_squares.tex),

\[
\boxed{\mathrm{RH}\quad\Longleftrightarrow\quad
F(t,x)\ne0\quad\text{for every }t>0,\ x\in\mathbb R.}
\tag{5}
\]

Thus the precise compact formulation is: the explicitly defined theta
lift F is left Fueter-regular for each real time, and RH is equivalent
to its having no zeros at real quaternion arguments for any positive
time. There is no claim of nonvanishing throughout quaternion space or
of simplicity at time zero. The collision equivalence retains its
threshold, uniform localization, and local Hermite-splitting inputs.

On the complex slice \(z_1=0\), define the trace
\(f(t,z)=F(t,z)=H(t,z)+\mathbf jH_z(t,z)\).
Its signed products and norm are exactly the original first-jet
observations in the [criteria note](1_RH_CRITERIA_AND_QUATERNION_SETUP_20261014.md).
Their \(-\mathbf j\mathscr L_j\) coefficients do not change under this
adopted lift. Off that slice, the Laguerre observations are evaluated
at \((\tau,z_0)\); real stationary signs are imposed on the physical
\(t>0,q=x\) slice, where \(\tau=t\).

## Polynomial control and research scope

For \(P(\tau,z)=z^2-2\tau+1\), the same lift is

\[
F_P(t,q)=z_0^2-2t-2\overline{z_1}+1+2\mathbf jz_0.
\]

It is standard left Fueter-regular and obeys (4), but
\(F_P(1/2,0)=0\) and P(0,z) has zeros \(\pm i\). The mechanism
therefore embeds arbitrary jointly entire backward-heat solutions;
a theta-specific signed estimate remains necessary to exclude the
physical zeros in (5).

The lift is a declared extension choice, not a uniqueness theorem.
For example, adding a scalar entire \(g(z_1)\) with g(0)=0
preserves regularity, the physical trace, the full jet constraint, and
external heat, while changing the field away from the trace. Such an
addition need not preserve the chosen antiholomorphy in \(z_1\).
The investigation adopts (2) explicitly and retains that dependence
when applying quaternion identities.
