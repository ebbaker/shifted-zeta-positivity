# Internal review of the standard Fueter lift

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.

Scope: internal LLM derivation and subagent cross-check of the
[independent-time convention note](../notes/3_STANDARD_FUETER_LIFT_WITH_INDEPENDENT_TIME_20261014.md).
This is not independent specialist review or formal verification.

The standard left Cauchy--Riemann--Fueter definition was checked against
[Perotti, Section 1](https://www.numdam.org/item/10.1016/S1631-073X%2803%2900284-X.pdf)
and its [normalized form](https://link.springer.com/article/10.1007/s40315-023-00485-5).
With \(q=z_0+\mathbf jz_1=a+\mathbf ib+\mathbf jc-\mathbf kd\), the
minus sign on the d derivative is the coordinate conversion from the
usual Hamilton real basis.

## Checked identities and restrictions

- The component equation is
  \(\bar\partial_q(U+\mathbf jV)=U_{\bar z_0}-V_{z_1}
  +\mathbf j(V_{z_0}+U_{\bar z_1})\).
- Separated evaluation \(H(t,z_0)+\mathbf jH_z(t,z_1)\) is generally
  nonregular and loses the derivative component at real q.
- For \(\tau=t+\overline{z_1}\), the adopted pair
  \(U=H(\tau,z_0),V=H_z(\tau,z_0)\) gives
  \(U_{\bar z_0}=V_{z_1}=0\) and
  \(V_{z_0}+U_{\bar z_1}=H_{zz}+H_\tau=0\).
- The full jet \(U_{z_0}=V\) and the external heat equation
  \(\partial_tF=-\partial_{z_0}^2F\) hold throughout the lift.
- At q=x real, \(z_1=0\), so the original physical first jet and
  its norm, signs, and positive-time collision endpoint are preserved.
- The polynomial lift
  \(F_P=z_0^2-2t-2\overline{z_1}+1+2\mathbf jz_0\)
  is regular but has the physical zero \(F_P(1/2,0)=0\).

## Remaining obligation

The lift does not prove nonvanishing or supply a signed theta estimate.
It is not a unique quaternion extension without further restrictions.
The next construction must control the physical stationary signs or a
locally bounded loss on the declared collision domain, retaining full
theta information and signed remainders. The spectral alternative still
concerns scalar \(|H|^2\), not the quaternion total norm.
