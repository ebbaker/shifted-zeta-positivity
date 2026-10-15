# Elliptic translation inside the physical chord core: exact insertion and a bounded limitation

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**. This bounded experiment implements the first coefficient-translation task from Review 05. It proves exact source, transform and primitive formulas, then tests the natural finite-shift ansatz. No theta signed-core inequality is proved.

## 1. The experiment and its outcome

The [factor-preserving target](../02_signed_turning_control/03_FACTOR_PRESERVING_AND_AVERAGED_CHORD_TARGETS_20261015.md) leaves the complete stationary starting factor `W=h_j(t,x)` untouched. Only the endpoint source is cut off. The question here is whether direct elliptic translation of that endpoint introduces a favorable signed bulk term.

It does not in the tested ansatz. After the complete physical fourth-jet operator, one shift merely replaces half the highest retained mode by half the next mode. Every fixed finite combination of shifts whose coefficients sum to one similarly changes only a finite boundary band. Its remainder retains W and decays at Gaussian rate, but the unresolved physical core remains indefinite. This is a limitation of this direct finite-shift construction, not an impossibility theorem for all uses of elliptic translation.

The bounded pivot to the complete, weighted projected relation reveals another useful distinction. The physical zero-section source sees a discrete second difference of the weights, and its one-shift kernel includes `a_n=a_0+b|n|`. The normalized primitive endpoint, with `a_0=1`, removes this additional slope. A second shift also detects the slope. Thus the projected arithmetic relation can identify theta once its missing endpoint information is restored; it still supplies no signed transform estimate.

## 2. Complete fourth-jet insertion

Write `q=e^(4u)`,

\[
\Theta_N(z,\tau)=\sum_{n=-N}^N e^{\pi i n^2\tau+2\pi inz},\qquad
(\mathsf T F)(z,\tau)=e^{\pi i\tau+2\pi iz}F(z+\tau,\tau).
\]

The complete source operator at the physical zero section is

\[
\mathscr S_q[F]
=\left.e^u\left(\frac{q^2}{16\pi^2}\partial_z^4
 +\frac{3q}{8\pi}\partial_z^2\right)F(z,iq)\right|_{z=0}
=\left.\frac{e^u}{16\pi^2}(q^2\mathcal D^4-3\pi^2)F\right|_{z=0}.
\tag{1}
\]

The second equality is a zero-section operator identity, with `D=∂_z+2πi Im(z)/q`; it does not omit the derivatives of its connection coefficient. Put `φ_0=0` and

\[
\phi_m(u)=e^u(2\pi^2m^4q^2-3\pi m^2q)e^{-\pi m^2q}
\quad(m\ge1).
\]

Each integer Fourier mode contributes `φ_|m|/2`, so `S_q[Theta_N]=Phi_N=sum_(m=1)^N φ_m`.

Differentiating the multiplier in `T` gives the following explicit shifted operator:

\[
\begin{aligned}
\Phi_N^+(u):=\mathscr S_q[\mathsf T\Theta_N]
=\frac{e^{u-\pi q}}{16\pi^2}
\big[&q^2\partial_z^4+8\pi i q^2\partial_z^3
 +(6\pi q-24\pi^2q^2)\partial_z^2\\
 &+(24\pi^2iq-32\pi^3iq^2)\partial_z
 +16\pi^4q^2-24\pi^3q\big]\Theta_N(z,iq)\big|_{z=iq}.
\end{aligned}
\tag{2}
\]

Equivalently, by covariance this is `e^(u-pi q)(q²D⁴-3pi²)Theta_N/(16pi²)` evaluated at `z=iq`. At a general vertical point the fourth jet on an exponential mode has the polynomial `X⁴+6cX²+3c²`, where `X=2πin+2πi Im(z)/q`, `c=π/q`. This verifies the connection terms in (2).

After reindexing `m=n+1`, (2) gives the complete identity

\[
\boxed{\Phi_N^+=\Phi_N+\tfrac12(\phi_{N+1}-\phi_N),\qquad N\ge1.}
\tag{3}
\]

This is the source-level form of the two boundary modes. It is a neighboring-mode replacement, with no additional interior term.

There is an essential cancellation before integration. The `n=-1` term of `Theta_N(z,iq)|_(z=iq)` becomes the translated zero mode. The bracket in (2) annihilates it exactly. Its separate displayed derivative terms have contributions growing like `e^u q²` or `e^u q`; multiplying by `e^(tu²)` makes their separate half-line integrals divergent when `t>=0`. Thus integrating or estimating those pieces independently is invalid. The combined operator has the decaying source (3).

## 3. Heat transforms, complete stationarity and primitive endpoints

For `j=0,1` set `c_j(y,u)=u^j cos(yu+jπ/2)` and allow `η=0` or `1`:

\[
f_{j,\eta}(u)=e^{tu^2}\{c_j(y,u)-\eta c_{j+1}(y,u)\},\quad
\ell_{j,m}^{\eta}=\int_0^\infty\phi_m(u)f_{j,\eta}(u)\,du,
\quad D_{j,N}^{\eta}=\sum_{m=1}^N\ell_{j,m}^{\eta}.
\]

Here `η=1` is the sharp chord endpoint; `η=0` is the ordinary endpoint amplitude that can also be used in an averaged test. All physical heat weights remain inside `f`. Formula (3) gives

\[
\boxed{D_{j,N}^{\eta,+}
=D_{j,N}^{\eta}+\tfrac12(\ell_{j,N+1}^{\eta}-\ell_{j,N}^{\eta}),}
\quad
\boxed{W D_{j,N}^{\eta,+}
=W D_{j,N}^{\eta}+\tfrac W2(\ell_{j,N+1}^{\eta}-\ell_{j,N}^{\eta}).}
\tag{4}
\]

The factor W and the stationarity condition `h_(j+1)(t,x)=0` are complete. Replacing the latter by truncated stationarity would require retaining and paying its separate tail. For fixed `T_*`, put

\[
J_j(T_*)=\int_0^\infty(u^j+u^{j+1})
 e^{T_*u^2+9u-(\pi/2)e^{4u}}\,du<\infty.
\]

For real y, `t<=T_*` and either η, the mode bound in Note 03 gives

\[
\left|\frac W2(\ell_{j,N+1}^{\eta}-\ell_{j,N}^{\eta})\right|
\le\sqrt{E(t,x)}\,\pi^2J_j(T_*)
\{N^4e^{-\pi N^2/2}+(N+1)^4e^{-\pi(N+1)^2/2}\}.
\tag{5}
\]

Thus the boundary error has exactly the useful factor-preserving form. This supplies no lower bound for either core in (4).

The finite primitive endpoint is not the theta endpoint `1/2`. Define

\[
p_m(u)=e^u e^{-\pi m^2e^{4u}},\quad
\psi_N=\sum_{m=1}^Np_m,\quad
b_m=-p_m'(0)=(4\pi m^2-1)e^{-\pi m^2},\quad b_N^{\rm sum}=\sum_{m=1}^Nb_m.
\]

All these primitives decay at the upper endpoint. Since `8φ_m=p_m''-p_m`, and `f_(j,η)(0)=δ_(j0)`, `f_(j,η)'(0)=0`, exact integration by parts yields

\[
8D_{j,N}^{\eta}
=b_N^{\rm sum}\delta_{j0}
 +\int_0^\infty\psi_N(u)(f_{j,\eta}''-f_{j,\eta})(u)\,du.
\tag{6}
\]

For the shifted source,

\[
\psi_N^+=\psi_N+\tfrac12(p_{N+1}-p_N),\qquad
b_N^+=b_N^{\rm sum}+\tfrac12(b_{N+1}-b_N).
\tag{7}
\]

These are convergent primitive formulas for `N>=1`. In particular, if `I_j(t,x)` denotes the complete starting integral from the manuscript and the finite integral in (6) is `J_(j,N)^η`, then

\[
\boxed{64W D_{j,N}^{\eta}
=\left(I_j(t,x)+\tfrac12\delta_{j0}\right)
 \left(J_{j,N}^{\eta}+b_N^{\rm sum}\delta_{j0}\right).}
\tag{8}
\]

For branch 0 this includes the corner `b_N^(sum)/2`; replacing it by `1/4` before taking the complete limit is incorrect. The derivative of the heat multiplier remains in the primitive integrand throughout.

## 4. Bounded pivot: symmetric shifts and the projected relation

The natural next ansatz averages a bounded number of forward and backward translations before applying the same source operator. Let `k` be an integer and `N>=|k|`. Reindexing gives

\[
\boxed{\mathscr S_q[\mathsf T^k\Theta_N]-\Phi_N
=\frac12\left\{\sum_{r=1}^{|k|}\phi_{N+r}
 -\sum_{r=0}^{|k|-1}\phi_{N-r}\right\}.}
\tag{9}
\]

The formula depends only on `|k|`: the positive and negative shift have the same physical source. Thus symmetric averaging of one shift does not change (3). More generally, a fixed finite linear combination `sum_k gamma_k T^k`, with `sum_k gamma_k=1`, changes only a boundary band of width `max|k|`. It creates no interior signed term. This includes positive averages. Nonconstant arithmetic multiplier insertions, transverse observations, products before restriction, or growing shift ranges are outside this bounded ansatz.

The projected weighted relation explains what arithmetic data this operation actually retains. For an even polynomial-growth coefficient sequence `(a_n)`, define `Theta_a` as in the reflection note. Pairing the modes `m` and `-m` after the source operator gives

\[
\boxed{\mathscr S_q[\mathsf T\Theta_a-\Theta_a]
=\frac12\sum_{m\ge1}(a_{m-1}+a_{m+1}-2a_m)\phi_m.}
\tag{10}
\]

The zero-mode coefficient is annihilated, and the odd part of the first coefficient difference disappears under the even source observation. Therefore a vanishing projected defect for all `q>=1` is weaker than full elliptic translation.

Precisely, (10) vanishes identically if and only if

\[
\boxed{a_n=a_0+b|n|.}
\tag{11}
\]

To prove necessity, if some positive-index coefficient of the series in (10) were nonzero, choose its least index. As `q->infinity`, its nonzero quadratic polynomial times `exp(-pi m²q)` dominates every later mode. Polynomial coefficient growth bounds the remaining tail exponentially, contradicting zero. Thus each discrete second difference vanishes. Solving that recurrence on the nonnegative integers gives (11); evenness supplies the negative indices. Sufficiency follows by substitution. This is an analytic uniqueness proof, not an inference from finitely many samples.

The slope is a real information loss, but the manuscript's endpoint normalization restores it. With `a_0=1`,

\[
\psi_a'(0)=-\tfrac12+b\sum_{n\ge1}
n(1-4\pi n^2)e^{-\pi n^2}.
\tag{12}
\]

The last sum is strictly negative. Hence `psi_a'(0)=-1/2` forces `b=0`. Without `a_0=1`, that conclusion does not follow from the one endpoint alone. Alternatively, for (11),

\[
\mathscr S_q[\mathsf T^k\Theta_a-\Theta_a]
=b\sum_{m=1}^{|k|-1}(|k|-m)\phi_m,
\tag{13}
\]

so the second shift already gives `b φ_1` and detects the missing slope. These stronger data fix the input; they still do not establish a sign for its oscillatory transform.

## 5. Controls and the exact remaining indefiniteness

The existing three-square collision is rejected by the complete projected law (10). The same applies to any positive finite-support source, including a proposed higher-endpoint collision: if `M` is its highest nonzero index, the coefficient of `φ_(M+1)` in (10) is `a_M/2>0`. Exponential-mode independence prevents an identically zero defect. This conclusion uses only the declared finite support; it does not certify a new collision or its numerical location.

Conversely, the ramp family with `a_0=1`, `b>0` has positive weights at every square and passes the one-shift projected identity exactly, while failing the normalized primitive endpoint and the second shift. It is an exact control for which information the projection loses, not a claimed collision control.

After the translation boundary is removed, the remaining scalar core is still `W D_N`. Without a further relation linking its two physical observations, adding `K W²` gives the quadratic matrix

\[
\begin{pmatrix}K&1/2\\1/2&0\end{pmatrix},
\qquad \det=-\tfrac14.
\tag{14}
\]

On branch 1 the additional term `K H²` does not remove this negative two-dimensional restriction. A stationarity multiplier vanishes on the fully stationary subspace, so it does not change (14) there. This rules out an unconstrained positive-square reading of the remaining scalar form; it does not rule out a new arithmetic constraint or a genuinely bilocal representation.

The heat-polynomial controls make that scope concrete. At `s=T-t>0`, take `H=x²+2s` for branch 0 or `H=x³+6sx` for branch 1. Both have a full stationary start at `x=0` for the appropriate W, and W stays positive on every short rightward interval. For `delta=1/4`, every finite `K>=0` admits sufficiently small s with `C_j+K E<0`. The exact checker uses `s=7/[64(K+1)]`. These controls satisfy the physical heat equation and stationarity but are not asserted to satisfy the theta arithmetic hypotheses. They identify precisely why the unresolved scalar algebra cannot supply the missing sign by itself.

## 6. Decision and verification

The direct finite-shift experiment is complete. It produces the full fourth-jet insertion, its physical heat transform, the correct finite primitive endpoints, and an admissible Gaussian boundary remainder. It does not produce a favorable interior term. Symmetric or other normalized bounded shift combinations retain the same limitation. This ansatz should not be escalated into a larger computation merely by increasing its finite degree.

A useful next arithmetic step must go beyond direct scalar translation: for example, retain a coupled product or a transverse observation before restriction and state exactly which sign relation it adds. The source-projected relation plus normalization may be used as a precise discriminator, but input rigidity is still not the signed-core theorem.

The accompanying [exact checker](../../numerics/check_theta_elliptic_core.py) passes **481 exact assertions** verifying finite polynomial identities, cutoff mode bands, the projected coefficient formula, ramp controls, primitive differentiation and exact heat-polynomial witnesses. Its [receipt](../../numerics/THETA_ELLIPTIC_CORE_CHECKS_20261015.json) records the groups, witnesses and source hash. Infinite-series uniqueness, convergence and the general bounded-shift classification are analytic arguments above; finite checks do not replace them. No numerical theta sign domain, theta collision exclusion or RH conclusion is asserted.

Sources: the manuscript's ordinary/covariant fourth-jet source formula and primitive reconstruction; the [complete signed bridge](03_COMPLETE_SIGNED_CORRELATION_BRIDGE_20261015.md); [reflection rigidity](../05_control_families/02_WEIGHTED_COMB_REFLECTION_RIGIDITY_20261015.md); the factor-preserving note linked above; and Review 05's coefficient-translation experiment.
