# Theta centered residual and shared arithmetic

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded current-turn model: **gpt-6-astra (Codex)**; reasoning effort
**ultra**, verified from the local turn metadata. Parallel LLM analytic,
computational, and internal review work supported this continuation.

The residual target in [Note 15](15_OCTONIONIC_LIFT_AND_ASSOCIATOR_SIGN_TARGET_20261014.md)
now has an exact theta-specific arithmetic representation and a bounded
whole-cell realization. A fixed contour gives a derivative drift that
vanishes in each scalar stationary observation. A relative cone for the
resulting centered residual yields both required bounded-loss estimates
by explicit sum-of-squares identities. The accompanying certificate proves
this cone on \(0\le t\le1/2,\ 100\le x\le104\), and separately proves
both stationary signs and a physical norm gap there.

The all-height estimate remains open. The common arithmetic representation
identifies its logarithmic weights and retains their complete cancellation;
it does not assign them a sign. Combined with the established height-100
gap, the bounded result excludes positive-time collisions through
\(|x|\le104\) in the possible threshold time range.

## 1. Contour centering adapted to genuine stationarity

Write \(h_k=\partial_x^kH(t,x)\), \(F=h_0+\mathbf jh_1\),
\(E=h_0^2+h_1^2\), and \(L_j=h_{j+1}^2-h_jh_{j+2}\) for \(j=0,1\).
The complete-source identity from
[Note 12](12_SHIFTED_CONTOUR_FOUR_JET_PAYMENTS_20261014.md) is

\[
h_k=e^{-ax}\operatorname{Re}\int_0^\infty
(iz)^k e^{tz^2}\Phi(z)e^{ixu}\,du,
\qquad z=u+ia,\quad 0<a<\pi/8.
\tag{1}
\]

For fixed real \(b\ge0\), put \(\mu=a^2+b^2\) and define

\[
C_j=e^{-ax}\operatorname{Re}\int_0^\infty
(u^2-b^2)(iz)^j e^{tz^2}\Phi(z)e^{ixu}\,du.
\tag{2}
\]

Since \(u^2-b^2=-(iz)^2-2a(iz)-\mu\), this is exactly

\[
\boxed{C_j=-h_{j+2}-2ah_{j+1}-\mu h_j.}
\tag{3}
\]

Consequently,

\[
\boxed{h_{j+1}=0\quad\Longrightarrow\quad
L_j=\mu h_j^2+h_jC_j.}
\tag{4}
\]

The derivative drift in (3) is useful because it disappears under the
original stationary constraint. These are physical derivatives, not
ordinary derivatives of an exponentially normalized observation. The
complete source is shifted before individual theta indices are separated;
no individual raw index is assigned the vanishing vertical contribution
that holds for the complete even source.

In quaternion form \(C=C_0+\mathbf jC_1\) and
\(F_t=2aF_x+\mu F+C\). The radial derivative drift vanishes on \(h_1=0\),
and equals \(2ah_0h_1\) on \(h_2=0\). The component identity (4) gives
sharper bounds than paying this last term by \(aE\).

## 2. A cone that pays both stationary losses

Let \(\eta>0\) be prescribed independently of the unknown physical norm.
The sufficient relative cone is

\[
\Delta=\eta^2E-C_0^2-C_1^2\ge0.
\tag{5}
\]

It need only hold on the stationary union, although the finite certificate
below establishes it on whole cells. On the respective stationary sets,

\[
L_0\ge(\mu-\eta)E\quad(h_1=0),\qquad
L_1\ge-\frac{\eta^2}{4\mu}E\quad(h_2=0).
\tag{6}
\]

The first follows from \(|C_0|\le\eta\sqrt E\) and \(E=h_0^2\).
For the second, complete the square in
\(\mu h_1^2-\eta|h_1|\sqrt E\). Neither argument divides by \(E\).
Since \(\eta-\mu\le\eta^2/(4\mu)\), a sufficient common loss is

\[
K=\eta^2/(4\mu).
\tag{7}
\]

This is locally bounded whenever the prescribed parameters are locally
bounded and \(\mu\) stays positive near each candidate collision. A
strict residual cone is a substantive source estimate, not a consequence
of quaternionic or octonionic regularity.

For audit purposes the exact identities before imposing stationarity are

\[
\begin{aligned}
2\eta[L_0+(\eta-\mu)E]
={}&(C_0+\eta h_0)^2+C_1^2+\Delta\\
&+2\eta h_1[(1-\mu+\eta/2)h_1+2ah_0],
\end{aligned}
\tag{8}
\]
\[
4\mu L_1+\eta^2E
=(2\mu h_1+C_1)^2+C_0^2+\Delta
+4\mu h_2(h_2+2ah_1).
\tag{9}
\]

Each last term is a multiple of the genuine stationary derivative. The
remaining terms are explicit squares and the single theta cone slack.
These homogeneous identities also hold for the normalized physical jets
\(Z_k=e^{\pi x/8}h_k\), with all quadratic observations rescaled by
\(e^{\pi x/4}\). Through Note 15, (6) also places the corresponding
compensated associator on its prescribed nonnegative ray.

A weaker direct test can preserve the sign of the residual. Suppose paid
normalized approximations give \(Z_j=p+\delta\) and
\(e^{\pi x/8}C_j=q+\epsilon'\), with
\(|\delta|\le\varepsilon\), \(|\epsilon'|\le\zeta\). At genuine
stationarity, expanding (4) and retaining \(\mu\delta^2\ge0\) gives

\[
e^{\pi x/4}L_j\ge\mu p^2+pq
-|2\mu p+q|\varepsilon-|p|\zeta-\varepsilon\zeta.
\tag{9a}
\]

Complete cell enclosures may use this signed expression even when the
stronger two-component cone fails. Its errors must include the entire
centered source tail, retained quadrature, and parameter variation.

There is a compatible way to remove the principal phase rotation. For
\(b>0\), define

\[
W=h_0+\mathbf j\frac{h_1+ah_0}{b},\qquad
R=C_0+\mathbf j\frac{C_1-aC_0}{b}.
\]

For \(a,b\) frozen in time, direct four-jet algebra gives

\[
W_t=(b^2-a^2-2ab\mathbf j)W+R.
\tag{10}
\]

Thus \(b^2-a^2\) is the principal heat growth in this balanced metric,
whereas \(a^2+b^2\) is the stationary curvature coefficient in (4).
The skew term changes direction without changing \(|W|^2\). This
prescribed change of variables uses no quotient by a physical jet. If
the parameters vary with time, add
\(\mathbf j(a_t\operatorname{Re}W/b-b_t\operatorname{Im}_{\mathbf j}W/b)\)
to (10). The finite calculation freezes both parameters on each cell.

## 3. The common theta carrier and its logarithmic weights

Write \(\alpha_n=\pi n^2\) and

\[
\phi_n(z)=(2\alpha_n^2e^{9z}-3\alpha_ne^{5z})e^{-\alpha_ne^{4z}},
\qquad\Phi(z)=\sum_{n\ge1}\phi_n(z).
\]

The common exponential phase in the shifted \(n\)-th integrand is
\((x+2ta)u-\alpha_n\sin(4a)e^{4u}\). Its critical location is

\[
b_n=\frac14\log\frac{x+2ta}{4\pi n^2\sin(4a)}
=b_1-\frac12\log n.
\tag{11}
\]

A nonnegative location belongs to the integration half-line. This
identifies a centering choice, not dominance of the first index or a
stationary-phase estimate for the full complex prefactor.

More strongly, the exact translation identity

\[
\phi_n(z)=n^{-1/2}\phi_1(z+d_n),\qquad d_n=\tfrac12\log n,
\tag{12}
\]

puts all four jets into one integral. Set

\[
A_n(t,x;v)=n^{-1/2}
\exp\{td_n^2-2td_n(v+ia)-ixd_n\}.
\]

Changing variables \(v=u+d_n\) in each shifted channel yields

\[
\boxed{h_j=e^{-ax}\operatorname{Re}\int_0^\infty
e^{t(v+ia)^2}\phi_1(v+ia)e^{ixv}
\sum_{n\le e^{2v}} A_n(t,x;v)
[i(v+ia-d_n)]^j\,dv.}
\tag{13}
\]

The staircase cutoff \(n\le e^{2v}\) is part of the exact identity.
It must not be replaced by an unrelated fixed Dirichlet polynomial or
differentiated across its jumps without accounting for the boundaries.
All four jets share the same carrier and arithmetic weights. Expanding
the last power uses only the first four logarithmic moments of the same
sum. At \(v=b_1\), the weights are

\[
A_n=n^{-(1/2+tb_1)-i(x/2+ta)}
\exp\{\tfrac t4(\log n)^2\}.
\tag{14}
\]

Equation (13) is derived from the theta source itself; no approximate
functional equation or unproved relative error is imported.

For centering \(b=b_1\), inserting \((v-d_n)^2-b^2\) into the sum
in (13) gives \(C_j\). The exact split is

\[
(v-d_n)^2-b^2
=\underbrace{-b\log n+\tfrac14(\log n)^2}_{\delta_n}
+2(b-d_n)(v-b)+(v-b)^2.
\tag{15}
\]

Equivalently, let \(f_{n,j}\) be the shifted horizontal channel in (1)
and let \(d_{n,j}^{\rm res}\) be its integral with multiplier
\(u^2-b_n^2\). For finite \(N\),

\[
C_j=\sum_{n\le N}d_{n,j}^{\rm res}
+\sum_{n\le N}\delta_n f_{n,j}+\mathcal T_{N,j}.
\tag{16}
\]

The tail is the omitted part of the common-centered expression (2).
The term \(h_j\sum\delta_n f_{n,j}\) in (4) retains the signed
arithmetic cross terms. Bounding it by the absolute sizes of the
individual channels discards the cancellation that the target needs.

## 4. Complete payments for the new representation

Use \(S_k(q,d)=\sum_{r=0}^k\binom kr d^{k-r}r!/q^{r+1}\)
from Note 12. If a positive majorant on a tail \(u\ge U\) has the
form \(M e^{-q(u-U)}\), then the centered residual payment is

\[
M\{S_{j+2}(q,U+a)+b^2S_j(q,U+a)\},
\tag{17}
\]

because \(|u^2-b^2|\le(u+a)^2+b^2\). Thus Note 12's complete
index and integration payments extend by this same degree-two
replacement, with their original exponential prefactors and hypotheses.
The formula deliberately overpays to retain every omitted index and
the full integration half-line.

For the shared carrier, \(0\le d_n\le v\) and \(0\le t\le\tau\)
give \(|A_n|\le n^{-1/2}\) and
\(\sum_{n\le e^{2v}}n^{-1/2}\le2e^v\). Hence the absolute integrand
in (13) is bounded by

\[
2(2\pi^2+3\pi)(v+a)^j
\exp\{\tau v^2+10v-\pi\cos(4a)e^{4v}\}.
\tag{18}
\]

This proves absolute convergence and justifies rearrangement. For a
cutoff \(V\), put

\[
\beta_V=\pi\cos(4a)e^{4V},\quad
q_V=4\beta_V-10-2\tau V,\quad
Q_V=\tau V^2+10V-\beta_V.
\]

If \(q_V>0\) and \(8\beta_V\ge\tau\), concavity bounds the complete
\(v\ge V\) tail by

\[
e^{-ax}2(2\pi^2+3\pi)e^{Q_V}S_j(q_V,V+a).
\tag{19}
\]

For \(C_j\), replace \(S_j\) by
\(S_{j+2}+b^2S_j\), since \(0\le v-d_n\le v\). A finite shared
integral with \(n\le\min(N,e^{2v})\) and \(v\le V\) is therefore
paid by the original complete-index bound plus (19); overlap may be
overpaid. These analytic formulas have not been used as a substitute for
validated retained quadrature in the certificate below.

There is also a quantitative reason to retain the arithmetic cancellation.
Let \(M=\lfloor e^{2v}\rfloor\), and retain just
\(\lceil M/2\rceil\le n\le M\). Then

\[
\sum_{n\le e^{2v}}|A_n|
\ge (M/2-1)M^{-1/2}e^{-tv^2}.
\tag{20}
\]

Indeed \(td_n^2-2td_nv=t[(d_n-v)^2-v^2]\ge-tv^2\).
For fixed \(a\), \(t=\theta/\log x\), \(v=b_1\), and fixed
\(0\le\theta<4\), the right side grows as a positive constant times
\(x^{1/4-\theta/16}\). The first weight has modulus one. Thus the
remaining arithmetic sum cannot be a uniformly small pointwise absolute
perturbation of its first term in this part of the cusp. This does not
exclude cancellation inside the sum or subsequent oscillatory integration.

## 5. A certified relative cone beyond height 100

The computation uses the 32 closed cells

\[
[k/16,(k+1)/16]\times[m,m+1],\qquad
k=0,\ldots,7,\quad m=100,\ldots,103.
\tag{21}
\]

For each center \((t_c,x_c)\), freeze

\[
a=\pi/16,\qquad
b=\frac14\log\frac{x_c+2t_ca}{4\pi\sin(4a)},\qquad
\mu=a^2+b^2.
\tag{22}
\]

The parameters are independent of the unknown observation. Different
cells may use different centers, while all loss constants below are
uniform. Arb/Acb arithmetic encloses the complete source with \(N=8\),
\(U=3/2\), and 192-bit precision. The exponential normalization is
\(e^{cx_c}\), \(c=\pi/8\), constant across each cell.

Write \(J_r=e^{cx_c}h_r(t_c,x_c)\). Each center enclosure includes
validated finite quadrature and both complete omitted-domain payments
from Note 12, for all required orders through 28. The centered coefficients
\(-J_{r+2}-2aJ_{r+1}-\mu J_r\) are combined before parameter transport.
This keeps their shared cancellation through the Taylor polynomial.

The required complete derivative majorants are

\[
M_r=e^{(c-a)x_c+a\delta_x}\int_0^\infty
(u+a)^r e^{u^2/2}
\sum_{n\ge1}(2\alpha_n^2e^{9u}+3\alpha_ne^{5u})
e^{-\alpha_n\cos(4a)e^{4u}}\,du,
\tag{23}
\]

with \(\delta_x=1/2\). Their retained integrals and complete tails are
also enclosed, through order 29. For centered derivatives use
\(M_r^C=M_{r+2}+2aM_{r+1}+\mu M_r\).

For either sequence \(Y_r=h_r\) or \(C_r\), the frozen parameters
give \(\partial_t^\ell Y_r=(-1)^\ell Y_{r+2\ell}\).
Truncate the time Taylor series at \(\ell<8\), and each retained
coefficient's spatial series at \(m<12\). With \(\delta_t=1/32\),
the whole-cell payments for component \(r\) are

\[
R_r^x=\sum_{\ell=0}^7
\frac{\delta_t^\ell}{\ell!}
\frac{\delta_x^{12}}{12!}M_{r+2\ell+12},\qquad
R_r^t=\frac{\delta_t^8}{8!}M_{r+16},
\tag{24}
\]

and the same formula with \(M^C\) for \(C\). Taylor's theorem first
in time at fixed \(x\), then in space for its retained coefficients,
proves (24). The majorant in (23) is uniform on the complete closed
cell, including its time endpoints.

For whole-cell intervals \(P_0,P_1\) and \(Q_0,Q_1\) enclosing the
normalized physical and centered components, the numerical decision is

\[
E_{\rm low}=\operatorname{dist}(0,P_0)^2+
\operatorname{dist}(0,P_1)^2>0,
\quad
\frac19E_{\rm low}-\sup|Q_0|^2-\sup|Q_1|^2>0.
\tag{25}
\]

All 32 cells pass (25) and \(\mu\ge2/5\). Thus throughout the band,
with the assigned cell parameters,

\[
\boxed{C_0^2+C_1^2\le\frac19E.}
\tag{26}
\]

The largest certified residual-square ratio is below \(0.073\);
that ratio is a diagnostic after certifying a denominator, whereas (25)
is the actual decision. Setting \(\eta=1/3\) in (6) proves the explicit
uniform statements

\[
\boxed{h_1=0\Rightarrow L_0\ge\frac1{15}E,\qquad
h_2=0\Rightarrow L_1\ge-\frac5{72}E.}
\tag{27}
\]

The certificate additionally checks (4) directly on every cell whose
stationary derivative enclosure contains zero. Both signed forms are
strictly positive on their respective stationary sets; all other cells
exclude the relevant stationarity. This second sign is stronger than
the generic cone consequence in (27). These classifications alone do
not assert existence or uniqueness of a stationary branch.

The normalized norm enclosure gives \(e^{\pi x/4}E>2700\) on the
band. Keeping each cell's own constant scale also verifies the stronger
physical floor directly from \(e^{-2cx_c}E_{\rm low}\):

\[
|F|>4\,10^{-16}\qquad(100\le x\le104).
\tag{28}
\]

Evenness supplies the reflected band. Combined with the earlier
height-100 certificate, (28) gives \(|F|>10^{-16}\) on the combined
strip \(0\le t\le1/2,\ |x|\le104\). The existing manuscript has
not been revised.

## 6. Remaining analytic target and replay

The finite calculation proves a theta-specific relative estimate, with
all four jets and complete source errors retained. It uses a certified
finite-cell norm lower bound to verify its cone; it does not establish
relative control through a hypothetical collision in the unbounded region.

The next analytic target is to estimate the signed products in (4), or
the cone slack (5), using the shared logarithmic sums (13)--(16), uniformly
in the padded collision region of
[Note 13](13_NORMALIZED_SIGN_TARGET_IN_THE_COLLISION_CUSP_20261014.md).
The new bounded gap permits its spatial cutoff to be set to 104:
\(0<t\le1/2,\ |x|>104,\ t\log|x|<C'\), with the same unspecified
classical constant and \(C'>C\).
The all-height obligation remains: the loss must stay locally bounded
through every candidate joint zero while all arithmetic cross terms,
staircase endpoints, and contour remainders remain accounted for.

The retained files are the
[whole-cell driver](../numerics/certify_phase_centered_residual.py),
[small certificate](../numerics/THETA_CENTERED_RESIDUAL_100_104_20261014.json),
[exact algebra checker](../numerics/check_theta_centered_residual_identities.py),
its [execution record](../numerics/THETA_CENTERED_RESIDUAL_IDENTITY_CHECKS_20261014.json),
and [internal review](../reviews/11_THETA_CENTERED_RESIDUAL_INTERNAL_REVIEW_20261014.md).
A separate standard-library
[record auditor](../numerics/audit_theta_centered_residual_record.py)
and [audit record](../numerics/THETA_CENTERED_RESIDUAL_RECORD_AUDIT_20261014.json)
check the exact closed cover, outward endpoints, cone and sign decisions,
and stated norm floors after binding the producer and imported source.
From the numerics directory, with python-flint available:

```sh
python3 certify_phase_centered_residual.py --output /tmp/theta-residual-replay.json
python3 check_theta_centered_residual_identities.py --output /tmp/theta-residual-identities.json
python3 audit_theta_centered_residual_record.py --record THETA_CENTERED_RESIDUAL_100_104_20261014.json --output /tmp/theta-residual-audit.json
```

The driver records its source and imported contour-checker hashes. Its
finite certificate and the exact algebra checks have distinct scopes;
neither establishes an arbitrary-height sign or an RH proof.
