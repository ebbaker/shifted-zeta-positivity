# Off-balance geometry: the retained dual-length cost

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. This is a bounded source-scoped
algebraic audit. It is conditional on the external reflected-energy and
additive-Gram estimates; it does not independently verify their proofs.

## Result

Moving to M+ell>1 incurs an additional low-side cost in the existing
reflected-energy envelope. Near the current geometry this raises, rather
than lowers, the matching zero-free boundary. Simply continuing the balanced
low exponent into this region is invalid. This rules out an automatic gain
from this direction using the displayed envelope, not an improvement from a
stronger estimate of the actual arithmetic rows.

## 1. Parameters and assumptions

Use the September 30 companion paper's exact physical operation (12.5),
reflected row energy (14.14), completed-row proof (15.3), additive Gram (15.4),
and tuple summation (15.8):
https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf

The PDF SHA-256 is
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.

Let tau>0 denote the imbalance, so it is not confused with the complex
Mellin variable s. Put

\[
M=1-\ell+\tau,\qquad
l_x=(M-b)/2,\qquad l_y=(M+b)/2,
\]
\[
h=1-l_x+\ell=(1+3\ell+b-\tau)/2.
\]

Work in a fixed small neighborhood of the current admissible geometry,
retaining positive scales, fixed disjoint slot windows, all original masks,
and the additive-Gram condition
\(l_y-\ell>11b/6\). The two physical profiles and all source support
conditions are otherwise unchanged. Small annular and dyadic losses can be
chosen independently and absorbed in epsilon exactly as in the source.
The calculation below compares main real exponents only.

For a rescaled subset of total slot length d in [0,ell], set

\[
M'=M-2d,\qquad \ell'=\ell-d,
\qquad M'+\ell'-1=\tau-3d.
\]

## 2. Retain the complete maximum in the row energy

The source uses an actual residual row length H, a powerful-part length O,
and deficit Delta_H=M'-O-H, with nonnegative main parts. Its actual dual
length is

\[
T_d=2H+2A_0+2z_a-1-\ell'-N_0-3B_0
\]

before the already-budgeted annular shift. The inequalities
\(2A_0\le O\), \(z_a\le\ell'\), and \(H\le M'-O\) give

\[
T_d\le H+\tau-3d.
\tag{1}
\]

Retained dual dyads satisfy
\(v+3\ell_b+e_\lambda\le T_d\). Consequently

\[
\max(H,v+\ell_b)
\le H+(\tau-3d)_+.
\tag{2}
\]

The source's step replacing this maximum by H cannot be used when tau>0.

Insert (2) into (14.14), retaining its hybrid saving and squared kernel
saving. In the branch u=z_a, the remaining terms are nonpositive, and the
energy is at most
\(M'+(\tau-3d)_+\).
In the other branch the argument giving (15.3) still applies. Before the
extra term in (2), its excess is at most

\[
\frac{1+3\ell'-2M'-2\Delta_H}{4}.
\]

Since Delta_H>=0 and
\(1+3\ell'-2M'=5\ell-1-2\tau+d\), both branches are bounded by

\[
\boxed{
E_{\rm ref}\le M'+(\tau-3d)_+
 +\frac{(5\ell-1-2\tau+d)_+}{4}
}
\tag{3}
\]

up to the independently chosen epsilon losses. This is a conservative upper
bound: no equality for every actual dyad is asserted.

## 3. Complete tuple cost and matching boundary

The additive Gram has the same ratio exponent b because
\(l_y-l_x=b\). Its use and the original tuple count and coefficient give
base exponent \(l_x/2+b/12\), together with

\[
f(d)=-d+\frac{(\tau-3d)_+}{2}
       +\frac{(5\ell-1-2\tau+d)_+}{8}.
\tag{4}
\]

On each linear interval the derivative is one of
\(-1,-7/8,-5/2,-19/8\). Every slope is negative. The function is
continuous at its kinks, so its maximum on [0,ell] is at d=0. Therefore the
low exponent supplied by this envelope is

\[
\boxed{
L=\frac{l_x}{2}+\frac b{12}+\frac\tau2
 +\frac{(5\ell-1-2\tau)_+}{8}.
}
\tag{5}
\]

Definition 10.1 gives the full affine signal exponent

\[
\boxed{
C(s)=s+\frac{l_x}{2}-1+\frac h6
=s-\frac23+\frac{\tau-b}{6}.
}
\tag{6}
\]

Matching C(sigma)=L consequently yields

\[
\boxed{
\sigma=\frac{11}{12}-\frac\ell4+\frac{7\tau}{12}
 +\frac{(5\ell-1-2\tau)_+}{8}.
}
\tag{7}
\]

Near the current ell=1001/6000<1/5, the positive part is zero for tau>=0.
At fixed ell and b, increasing tau worsens the matching boundary with slope
7/12. The independent high-side comparison would still have to be redone;
there is no claim here of any better complete zero-free theorem.

## 4. A formal endpoint really incurs the new term

The cost in (2) is not solely an artifact of applying its maximum inequality.
At d=0, choose the formal reflected-energy parameters

\[
O=\Delta_H=A_0=N_0=B_0=S_0=\ell_b=e_\lambda=0,
\qquad H=M,\quad z_a=\ell,
\]
\[
v=T_d=2M+\ell-1=M+\tau.
\]

Near the current geometry, v>=2z_a, so the hybrid quantity in (14.13) is
\(u=\min\{v,z_a,(v+z_a)/3\}=z_a\). The kernel saving vanishes because
v=T_d. Equation (14.14) is then exactly

\[
E_{\rm ref}=\max(M,M+\tau)+z_a-u=M+\tau.
\tag{8}
\]

More generally the same formal endpoint gives M'+tau-3d where tau-3d>=0
and v>=2ell'. Thus an extra tau in the squared row-energy exponent, and
tau/2 after Cauchy--Schwarz, is genuinely present in this displayed envelope.
These values satisfy the displayed exponent constraints. This is not a
claim that an actual dyad reaches this bound, or an arithmetic lower bound;
a stronger estimate can potentially save on the relevant endpoint family.

## 5. Consequence for the research order

The off-balance direction should remain separate from the current conditional
candidate. A useful next lemma here would improve (14.14) on the family
exhibited in (8), for example by exploiting the relation between the long
dual polynomial and the actual active slots. Without such input, the
conservative continuation increases the low cost and supplies no automatic
improvement. The joint inverse/plain witness route remains the first priority.

See the [localized joint-witness target](LOCALIZED_JOINT_WITNESS_TARGET_20261008.md)
for the prioritized route and its conditional payoff.
