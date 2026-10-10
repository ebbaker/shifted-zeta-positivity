# Sharp adjoint residuals and the obstruction from restricted primes

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex). Reasoning effort: the active setting is not exposed
to this session; no level is inferred. Derivations and parallel cross-checks
are internal LLM work, not independent mathematical validation.

The complete divisor graph admits explicit, regular adjoint multipliers
whose optimal weighted residual is exactly the scalar observation defect.
This supplies the construction missing from the initial certificate lemma,
but also proves its pointwise limitation. Restricting to primes 2 and 3
has a stronger limitation: once the shrinking-sector scale satisfies
\(L\ge160\), every multiplier pays residual at least one. Thus that
restricted graph cannot furnish the manuscript's strict visibility gap.
The [bounded cell continuation](3_REGULAR_ADJOINT_CELL_CERTIFICATE_20261010.md)
uses the complete graph and an independently enclosed correlated direction.

## State and covector conventions

Use the full physical dictionary in the
[manuscript](../enlarged_state_transport_and_heat_flow.tex). In particular,
\[
q_n=w_ne^{i(\theta+T\log n)},\qquad q_1=e^{i\theta},\qquad
q_n'=g_nq_n,\qquad
g_n=-d\log n+i(c\log n-\Omega).
\]
The observation is \(o=Cq_R=(\Re S,\Re S'/L)\), with
\(S=\sum_{n\le N}q_n\). Represent a real covector by complex coefficients
\(h_n\), acting as \(\Re\sum\overline{h_n}v_n\). Then the covector
\(C^Ty\), for real \(y=(y_1,y_2)\), has coefficients
\[
\gamma_n=y_1+\frac{y_2}{L}\overline{g_n}
=y_1-\frac{d\log n}{L}y_2
 +i\frac{\Omega-c\log n}{L}y_2.
\tag{1}
\]
The source covectors are \(b_1=q_1\), \(a_1=iq_1\), zero elsewhere.
Write
\[
Z=\sum_{n\le N}\gamma_n\overline{q_n};\qquad
\Re Z=y\cdot o,\quad \Im Z=y\cdot C(iq)_R.
\tag{2}
\]
All spatial derivatives freeze time and the integer cutoff. The positive
weights are explicit and never vanish on a finite physical cell.

## A regular construction on a prime division tree

For every \(n>1\), choose one prime divisor \(p_n\), and let
\(\operatorname{par}(n)=n/p_n\). The selected edges form a spanning tree.
Let \(\mathcal T_n\) be the descendants of \(n\), including \(n\),
and set
\[
\lambda_n=-\sum_{m\in\mathcal T_n}
       \overline{\frac{q_m}{q_n}}\,\gamma_m\quad(n>1),\qquad
z_0=-\Im Z,\qquad r=(1-\Re Z)b.
\tag{3}
\]
Assign zero multiplier to every unselected graph edge. Then
\[
b=C^Ty+B_R^T\lambda_R+z_0a+r.
\tag{4}
\]
Here \(\lambda_R\) is the real covector associated to the complex edge
coefficients \(\lambda_n\).

To verify (4), write \(h_n=q_n/q_{\operatorname{par}(n)}\) for the
prescribed edge factor. At a nonroot vertex the adjoint coefficient is
\(\lambda_n-\sum_{j:\operatorname{par}(j)=n}\overline{h_j}\lambda_j
=-\gamma_n\). The coefficient at the root is
\((Z-\gamma_1\overline{q_1})/\overline{q_1}\). Since
\(1/\overline{q_1}=q_1\), inserting \(z_0=-\Im Z\) and the root
residual gives \(b_1\) exactly.

The construction is regular even at \(o=0\). It divides only by the
known nonzero source components \(q_n\), and obeys the explicit bound
\[
|\lambda_n|\le\sum_{m\in\mathcal T_n}
                  \frac{w_m}{w_n}|\gamma_m|.
\tag{5}
\]
There is no claim that these edge multipliers remain small as \(N\)
grows. Their size is not charged in the manuscript's certificate because
the exact transport equations annihilate their pairing. If transport is
approximated instead, its defects must be multiplied by these sizes and
paid separately.

## The sharp residual is the scalar defect

For any fixed \(y\), the minimum weighted residual over all real edge
and phase multipliers is
\[
\inf_{\lambda,z_0}\sum_{n\le N}w_n
 \left\|(b-C^Ty-B_R^T\lambda-z_0a)_n\right\|_2
=|1-y\cdot o|.
\tag{6}
\]
Pairing any certificate with \(q_R\) gives
\(1-y\cdot o=r\cdot q_R\), which proves the lower bound. Formula
(3) attains it because the residual is confined to the unit-modulus
source. This is an attained minimum, not just a dual lower bound.

Consequently \(\mathcal R\le1-\delta\) forces
\(y\cdot o\ge\delta\) and
\(\|y\|_2\ge\delta/\|o\|_2\). At an actual finite joint zero,
\(o=0\), every certificate has \(\mathcal R\ge1\), despite positivity
and invertibility of the anchored parent operator. The sharp reciprocal
choice of \(y\) is an optimization identity, not a construction available
before nonvanishing has been established.

The directional version is equally sharp. Put \(e=\eta_N/2\), and let
\[
K_0=\{(s,v):s^2+|v|\le1\},\qquad
\rho(o)=\frac{|o_2|+\sqrt{o_2^2+4o_1^2}}2.
\tag{7}
\]
The support function of \(K_0\) is the manuscript's
\(h(|y_2|,|y_1|)\). If \(o\ne0\), then
\[
\inf_y\bigl\{|1-y\cdot o|+e h(|y_2|,|y_1|)\bigr\}
=\min\{1,e/\rho(o)\}.
\tag{8}
\]
At \(o=0\) the infimum is one. Indeed
\(|y\cdot o|\le\rho(o)h(|y_2|,|y_1|)\), so minimizing
\(|1-A|+(e/\rho)|A|\) gives the lower bound. For equality, normalize
\((s,v)=o/\rho\), take \(n=(2s,\operatorname{sgn}v)\), with
\(\operatorname{sgn}0=0\), and use
\(y=n/[\rho(1+s^2)]\) or \(y=0\). The normal has
\(n\cdot o=\rho(1+s^2)\) and \(h(n)=1+s^2\).

Thus existence of a strict pointwise directional certificate is exactly
\[
\left(\frac{F}{\eta_N}\right)^2+
\left|\frac{F'}{L\eta_N}\right|>1.
\tag{9}
\]
This rules out an additional pointwise gain from unrestricted graph
optimization. The optimal normal changes sign at \(o_2=0\), so it is
not a globally regular witness. A fixed independently certified direction
on a cell avoids that issue and can retain information lost by the two
separate coordinate hulls.

## Exact payment for a restricted prime graph

Let \(P\) be a set of selected primes. Its components are
\[
\mathcal C_m=\{m\prod_{p\in P}p^{a_p}\le N:a_p\ge0\},
\qquad m\text{ has no prime factor in }P.
\]
Define \(Z_m=\sum_{n\in\mathcal C_m}\gamma_n\overline{q_n}\).
Only the component containing one has the prescribed phase anchor.
The exact optimum is
\[
\mathcal R_P(y)=|1-\Re Z_1|+\sum_{m\ne1}|Z_m|.
\tag{10}
\]
Complex pairing on each component annihilates its internal edge adjoints.
For the component containing one, optimizing the real phase multiplier
removes \(\Im Z_1\), leaving \(|1-\Re Z_1|\). Every other component
retains the full complex defect \(-Z_m\), whose modulus is bounded by
its weighted residual. These are disjoint blocks, so the bounds add.
Equality is achieved by the same tree recursion on each component, with
\[
z_0=-\Im Z_1,\quad r_1=(1-\Re Z_1)q_1,\quad
r_m=-Z_m/\overline{q_m}\quad(m\ne1),
\]
and all other residual coordinates zero. In particular,
\(\mathcal R_P(y)\ge|1-y\cdot o|\).

## An effective obstruction for primes 2 and 3

On the actual manuscript sector
\[
L\ge160,\quad 1\le\kappa\le3/2,\quad t=\kappa/L,\quad
x=4\pi e^L,\quad N=\lfloor\sqrt{e^L+t/16}\rfloor,
\]
the restricted graph with \(P=\{2,3\}\) satisfies the uniform bound
\[
\boxed{\mathcal R_{\{2,3\}}(y)\ge1+82\|y\|_2.}
\tag{11}
\]
The conservative threshold is chosen for an elementary proof; it is not
claimed optimal. No approximation input for \(H_t\) is used in this
obstruction.

Here are the complete coarse estimates. With \(\ell_N=\log N\),
the physical coefficients obey
\[
0.49\le c\le0.51,\quad |\Omega/c-\ell_N|\le0.01,\quad
|d\log n/L|\le0.01,\quad |\gamma_n|\le2\|y\|_2,
\tag{12}
\]
and
\[
w_n\le n^{-1/2},\qquad
w_n\ge w_N\ge\tfrac12N^{-11/16}\quad(n\le N).
\tag{13}
\]
For completeness, the exact real-axis formulas are
\[
\alpha_r=L/2+\tfrac14\log(1+x^{-2})-\frac1{1+x^2},\quad
\alpha_i=\frac{3x}{1+x^2}-\tfrac12\arctan x,
\]
\[
U=\frac{7x^2-5}{(1+x^2)^2},\quad
V=\frac{x(x^2+5)}{(1+x^2)^2},\quad
\mu:=\Omega/c=\alpha_r-
\frac{t\alpha_i V}{2(1+tU/2)}.
\]
They give \(L/2-x^{-2}\le\alpha_r\le L/2\),
\(|\alpha_i|\le1\), \(|\alpha'|\le7/x\), and (12).
The cutoff differs from \(e^{L/2}\) by less than one at this scale;
in particular \(|\ell_N-L/2|\le2e^{-L/2}\).
To prove (13), use \(\log n\le2\alpha_r\) for the upper bound.
The logarithmic derivative of the weight is
\(t\log n/2-\sigma<0\), so the weight decreases. Writing
\(\ell_N=L/2+\epsilon\), \(|\epsilon|\le2e^{-L/2}\), gives
\[
\log w_N\ge-(1/2+\kappa/8)\ell_N+
             \frac{\kappa\epsilon\ell_N}{4L},
\]
which proves the lower bound in (13).

The anchored component is the set of 2,3-smooth indices. Its weighted
mass is at most
\[
\sum_{a,b\ge0}2^{-a/2}3^{-b/2}
=\frac1{(1-2^{-1/2})(1-3^{-1/2})}<9.
\]
Thus \(|\Re Z_1|\le18\|y\|_2\).

Every integer \(m\in(N/2,2N/3]\) coprime to six is a singleton
component. The two residue classes modulo six give at least
\(N/18-2\ge N/20\) such indices at the present scale. For each one,
the coefficient map in (1) is
\[
(y_1,y_2)\longmapsto
(y_1-a_my_2,\beta_my_2),\quad
|a_m|\le0.01,\quad 0.19/L\le\beta_m\le0.37/L.
\]
These bounds follow from (12) and
\(0.4<\log(3/2)<\log2<0.7\).
The matrix has determinant \(\beta_m\) and operator norm at most its
Frobenius norm, which is less than two. Its smallest singular value
therefore exceeds \(1/(20L)\). Equations (13) and the singleton count
give
\[
\sum_{m\ne1}|Z_m|\ge
\frac{N^{5/16}}{800L}\|y\|_2
\ge\frac{e^{5L/32}}{1600L}\|y\|_2
\ge100\|y\|_2.
\tag{14}
\]
The last function increases for \(L\ge160\); at 160, use
\(e^{25}>2^{25}>25{,}600{,}000\). Combining (10),
\(|1-\Re Z_1|\ge1-|\Re Z_1|\), and (14) proves (11).

This eliminates precisely certificates that use only those two primes,
only the source phase anchor at one, and the manuscript's blockwise
absolute residual norm. Adding prescribed information about the other
component roots, adding more edges, or retaining a signed correlated
residual changes the problem and is not excluded by (11).

## Verification and the next research target

The [exact Fraction checker](../numerics/check_adjoint_transport_optimality.py)
and its [small record](../numerics/ADJOINT_TRANSPORT_OPTIMALITY_RECORD_20261010.json)
check 1,878 assertions: full and restricted tree reconstruction, attained
root payments, support normals, a nonzero anchored state with both
observations zero, and disconnected-sector controls. The effective
large-scale inequality (11) is an analytical proof, not a numerical
experiment with an impossibly large cutoff. The shared enlarged-state
checker also passed its 15,446 existing exact assertions unchanged.

The productive next target is a uniform signed estimate for a prescribed
complete direction \(y\), or an effective correlated family of directions,
with a residual gap and multiplier exponent below the manuscript's
threshold. Complete Poisson or matched reflection transforms may make
that estimate economical, but their endpoint and source defects must
remain in the same estimate. The sparse 2,3 graph with absolute residual
payment is no longer a viable standalone asymptotic construction.

No novelty or priority claim is made. The finite optimization and tree
identities are established internally; the genuine theta overlap sign,
uniform multiplier theorem and global collision coverage remain open.
