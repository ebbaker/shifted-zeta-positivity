---
research_program: PR02-CORR
parent_program: PR02
secondary_programs: [ALG, PR03]
status: exact_identity_and_rejected_global_split
---

# A parity–Poisson identity and a positive-time splitting obstruction

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**. This is an incremental internal research note, not external refereeing or formal proof verification.

This continues [Note 36](36_COMPLETE_THETA_CORRELATIONS_AND_SIGN_TARGETS_20261015.md) and [Note 37](../00_research_coordination/37_OCTONIONIC_CORRELATION_INTEGRATION_AND_CONTINUATION_20261015.md). It supplies a genuinely two-coordinate theta identity and identifies a precise obstruction to using its axis and mixed pieces as separate global correlation kernels. It proves no new stationary sign region. The obstruction rejects the indicated global split, not the complete Poisson identity or all possible regularized/localized uses of it.

## 1. Exact arithmetic transformation

Write

\[
\Theta(y)=\sum_{n\in\mathbb Z}e^{-\pi n^2y},\qquad
P(u)=e^u\Theta(e^{4u}),\qquad \Phi(u)=(P''(u)-P(u))/16.
\]

For independent real coordinates \(s,r\), set

\[
u=s+r,\quad v=s-r,\quad y_+=e^{4u},\quad y_-=e^{4v},
\quad C=2\cosh(4r),\quad \tau=\tanh(4r).
\]

The complete product \(\Pi(s,r)=P(s+r)P(s-r)\) has the exact expansion

\[
\boxed{
\Pi(s,r)=\frac1{\sqrt C}\sum_{p,k\in\mathbb Z}
\exp\!\left[-\frac\pi C\{e^{4s}p^2+e^{-4s}k^2\}\right]
(-1)^{pk}\cos(\pi pk\tau).
}
\tag{1}
\]

To derive (1), in the product of the two theta sums use
\(p=m+n,q=m-n\). This is a bijection from \(\mathbb Z^2\) to
\(\{(p,q)\in\mathbb Z^2:p\equiv q\pmod2\}\), and

\[
y_+m^2+y_-n^2=
\frac A4(q+(B/A)p)^2+\frac{y_+y_-}{A}p^2,
\qquad A=y_++y_-,\quad B=y_+-y_-.
\]

Writing \(q=p+2\ell\), [Poisson summation](https://dlmf.nist.gov/1.8.E14) on \(\ell\) gives

\[
\sum_{\ell\in\mathbb Z}e^{-\pi A(\ell+\alpha p)^2}
=A^{-1/2}\sum_{k\in\mathbb Z}e^{-\pi k^2/A}e^{2\pi i k\alpha p},
\qquad \alpha=y_+/A=(1+\tau)/2.
\]

Now \(A=e^{4s}C\), \(y_+y_-=e^{8s}\), and the prefactor
\(e^{2s}A^{-1/2}=C^{-1/2}\). Taking the real part gives (1).
For \((s,r)\) in any fixed compact set, the series and all finite-order
coordinate derivatives converge absolutely and uniformly, since the
Gaussian coefficients are bounded below by positive constants and
differentiation introduces only polynomial factors in \(p,k\).

This uses the arithmetic parity lattice and Poisson summation on its
cosets. It is more than the reflection identity for an arbitrary even
source. Both independent coordinates remain: neither \(s=0\) nor
\(y_+y_-=1\) is imposed.

## 2. Differential factors and heat remain in place

Define the constant-coefficient operator

\[
\mathcal D=(\partial_s^2-\partial_r^2)^2
-8(\partial_s^2+\partial_r^2)+16.
\]

Because \(\partial_u=(\partial_s+\partial_r)/2\) and
\(\partial_v=(\partial_s-\partial_r)/2\),

\[
\boxed{\Phi(s+r)\Phi(s-r)=\mathcal D\Pi(s,r)/4096.}
\tag{2}
\]

Consequently the complete correlations are

\[
K_m(t,s)=\frac{e^{2ts^2}}{4096}
\int_{\mathbb R}r^{2m}e^{2tr^2}\mathcal D\Pi(s,r)\,dr.
\tag{3}
\]

The differential factors act on \(\Pi\), not on a product from which
the heat deformation has been dropped. The multiplier is exactly
\(e^{2t(s^2+r^2)}\). Termwise use of (1) and (2) is justified on compact
coordinate domains. Global interchange with the heat-weighted integral
requires an additional argument and fails for the split below.

## 3. The natural axis/mixed split is not globally integrable at positive time

Let \(f=C^{-1/2}\), and split (1) into the lattice axes, counting
\((0,0)\) once, and the remaining terms:

\[
\Pi_{\rm ax}=f\{\Theta(e^{4s}/C)+\Theta(e^{-4s}/C)-1\},
\qquad \Pi_{\rm mix}=\Pi-\Pi_{\rm ax}.
\tag{4}
\]

One-dimensional Poisson summation gives the particularly useful exact
axis formula

\[
\Pi_{\rm ax}=e^{-2s}\Theta(Ce^{-4s})+
 e^{2s}\Theta(Ce^{4s})-f.
\tag{5}
\]

Fix \(S<\infty\). Uniformly for \(|s|\le S\), as \(|r|\to\infty\),

\[
\Pi_{\rm ax}=2\cosh(2s)-f+
 O_S(e^{-\pi C e^{-4S}}).
\]

The same estimate after any coordinate derivative of total order at
most four has an extra factor at most \(O_S(C^4)\). Indeed,
\(Ce^{\pm4s}\ge Ce^{-4S}\); derivatives of \(C\) of each fixed order
are \(O(C)\); and each differentiated nonconstant theta term is bounded
by a fixed polynomial in \(n^2C\) times
\(e^{-\pi n^2Ce^{-4S}}\). Summing these Gaussian bounds proves the
uniform differentiated estimate for sufficiently large \(C\).

The term \(2\cosh(2s)\) is annihilated by \(\mathcal D\). Set
\(q=\operatorname{sech}^2(4r)\). Direct differentiation gives

\[
(\partial_r^2-4)f=-12qf,\qquad
(\partial_r^2-4)(qf)=(96-140q)qf,
\]

and hence

\[
-\mathcal D f=48fq(24-35q).
\]

It follows that

\[
\boxed{
\frac{\mathcal D\Pi_{\rm ax}}{4096}
=\frac{48}{4096}fq(24-35q)
+O_S(C^4e^{-\pi C e^{-4S}})
=\frac98e^{-10|r|}(1+O(e^{-8|r|}))+o(e^{-10|r|}).
}
\tag{6}
\]

The final little-oh term can be taken uniformly for \(|s|\le S\).
In contrast, source evenness and the complete positive-half-line
source envelope give, for \(r\ge S\),

\[
0<\Phi(s+r)\Phi(s-r)
\le16\pi^4 e^{18r}
\exp\{-2\pi e^{4r}\cosh(4s)\}.
\tag{7}
\]

Thus the differentiated mixed part has the opposite leading term:

\[
\boxed{\mathcal D\Pi_{\rm mix}/4096
=-\frac98e^{-10|r|}(1+o(1)).}
\tag{8}
\]

For every fixed \(t>0\), fixed \(s\), and \(m\ge0\), (6)–(8) imply

\[
\int_{\mathbb R}r^{2m}e^{2t(s^2+r^2)}
\frac{\mathcal D\Pi_{\rm ax}}{4096}\,dr=+\infty,
\qquad
\int_{\mathbb R}r^{2m}e^{2t(s^2+r^2)}
\frac{\mathcal D\Pi_{\rm mix}}{4096}\,dr=-\infty.
\tag{9}
\]

Their pointwise sum is the integrable complete source in (3). The same
obstruction applies to the first and second Laguerre weights
\(r^2\) and \(r^4-s^2r^2\), which are positive for sufficiently large
\(|r|\) at fixed \(s\). Adding a finite nonnegative multiple of the
energy weight \((1-s^2+r^2)/2\) does not remove the obstruction.

Therefore a global proof that treats the axis correlation and mixed
correlation as separately finite quantities, or pays the mixed block
by its global absolute norm, is inadmissible at every positive time.
The cancellation in (6)–(8) must occur before the unbounded integral.
The conclusion does not say that the complete transformed expression
has a wrong sign, or that a cutoff-dependent subtraction cannot work.
The obstruction disappears from this particular tail argument at
\(t=0\), which is another reason not to suppress the heat multiplier.

A simple global counterterm does not resolve the two-coordinate problem.
Replacing \(\Pi_{\rm ax}\) by \(\Pi_{\rm ax}+f\) cancels its bad
\(r\)-tail for bounded \(s\). But at each fixed \(r\), as
\(s\to+\infty\), the original axis formula and scalar Poisson identity
give \(\Pi_{\rm ax}=e^{2s}+o(1)\), with superexponentially small
coordinate derivatives of the remainder. Hence

\[
 \mathcal D(\Pi_{\rm ax}+f)\longrightarrow\mathcal D f(r).
\]

This is nonzero on an open set of \(r\) (at zero it equals
\(528/\sqrt2\)). The heat factor then prevents absolute integrability
in the \(s\) direction. Subtracting only finitely many terms of \(f\)'s exponential expansion
also leaves a tail that cannot beat \(e^{2tr^2}\).
Any compensation must control both independent coordinates and their
joint escape directions, not only the fixed-\(s\) tail in (6).

## 4. An admissible finite-box signed budget

For \(j=0,1\), put

\[
q_0=r^2,\qquad q_1=r^4-s^2r^2,\qquad
b=(1-s^2+r^2)/2.
\]

For a coefficient \(\kappa_j(t,x)\ge0\) prescribed independently of
the unknown energy and locally bounded through every covered candidate
collision, define

\[
W_{j,\kappa}=e^{2t(s^2+r^2)}
\{q_j(s,r)+\kappa_j(t,x)b(s,r)\}\cos(2xs).
\]

On the box \(\mathcal B=[-S,S]\times[-R,R]\), let

\[
M_{j,\mathcal B}=\frac1{4096}\int_{\mathcal B}
 W_{j,\kappa}\mathcal D\Pi_{\rm ax},\qquad
R_{j,\mathcal B}=\frac1{4096}\int_{\mathcal B}
 W_{j,\kappa}\mathcal D\Pi_{\rm mix},
\]

and retain the **complete**, unsplit exterior term

\[
T_{j,\mathcal B}=\int_{\mathbb R^2\setminus\mathcal B}
 W_{j,\kappa}\Phi(s+r)\Phi(s-r)\,ds\,dr.
\]

Then the exact signed remainder identity is

\[
\boxed{\mathcal L_j+\kappa_j E
=M_{j,\mathcal B}+R_{j,\mathcal B}+T_{j,\mathcal B}.}
\tag{10}
\]

The coefficient rule for an initial strict-sign test can be frozen as
\(\kappa_0=\kappa_1=0\). It is a fixed test target, not a fitted quotient
or an established global estimate. No nonzero, valid source-derived
coefficient rule is proved in this note. The intended additional
arithmetic inequality, on each **full** stationary set
\(S_j=\{h_{j+1}=0\}\), would be

\[
R_{j,\mathcal B}+T_{j,\mathcal B}\ge-M_{j,\mathcal B}.
\tag{11}
\]

Equation (10) only makes the signed budget explicit; it does not prove
(11), and the axis term is not assumed positive. A favorable finite
check of the complete stationary sign is not by itself a validation of
an axis-dominance explanation. A collision-exclusion claim would still
need unbounded-domain control and predecessor-neighborhood coverage
for both \(S_0\) and \(S_1\).

The exterior has a source-prescribed absolute bound. Let
\(U=\min(S,R)\),

\[
\mathsf M_k(t)=\int_{\mathbb R}|u|^kw_t(u)\,du,\qquad
\mathsf T_k(t,U)=\int_{|u|>U}|u|^kw_t(u)\,du,
\quad w_t(u)=e^{tu^2}\Phi(u).
\]

The complement of \(\mathcal B\) lies in
\(\{\max(|u|,|v|)>U\}\) after \(u=s+r,v=s-r\), whose Jacobian is
\(ds\,dr=du\,dv/2\). The bounds

\[
|q_0|\le(u^2+v^2)/2,\quad
|q_1|\le(u^4+v^4)/2,\quad
|b|\le1/2+(u^2+v^2)/4
\]

give

\[
|T_{j,\mathcal B}|\le
\frac12(\mathsf T_{2j+2}\mathsf M_0+
             \mathsf T_0\mathsf M_{2j+2})
+\kappa_j\left\{\frac12\mathsf T_0\mathsf M_0+
\frac14(\mathsf T_2\mathsf M_0+\mathsf T_0\mathsf M_2)\right\}.
\tag{12}
\]

All moments here belong to the complete source. For \(0\le t\le1/2\),
\(U\ge1\), and \(0\le k\le4\), the complete envelope \(\Phi(u)\le4\pi^2e^{9u-\pi e^{4u}}\) for \(u\ge0\) yields

\[
\mathsf T_k(t,U)\le4\pi e^{-4U}
\exp\{-(\pi/2)e^{4U}\}.
\tag{13}
\]

For example, use \(k\log u+tu^2+9u\le u^2/2+13u
\le(\pi/2)e^{4u}\) for \(u\ge1\), then integrate the remaining
exponential using its derivative. Formula (12) pays the exterior,
but it is an absolute payment and does not supply the missing
energy-relative sign estimate near a possible collision.

## 5. Boundaries and the original staircase

Equations (10)–(13) leave \(\mathcal D\) on the theta product. They
make no integration by parts and hence discard no boundary term.
If \(\mathcal D\) is moved to the weight, all four edges must be kept.
For clarity, write \([F]_{s=-S}^{S}\) and \([F]_{r=-R}^{R}\) for edge
differences. With \(W=W_{j,\kappa}\), \(G=\Pi_{\rm ax}\) or
\(\Pi_{\rm mix}\), the exact identity is

\[
\int_{\mathcal B}W\mathcal DG
=\int_{\mathcal B}G\mathcal DW+\mathfrak B_s+\mathfrak B_r
-2\mathfrak B_{sr},
\]

where

\[
\mathfrak B_s=\int_{-R}^{R}
[WG_{sss}-W_sG_{ss}+W_{ss}G_s-W_{sss}G
-8(WG_s-W_sG)]_{s=-S}^{S}\,dr,
\]

\[
\mathfrak B_r=\int_{-S}^{S}
[WG_{rrr}-W_rG_{rr}+W_{rr}G_r-W_{rrr}G
-8(WG_r-W_rG)]_{r=-R}^{R}\,ds,
\]

\[
\mathfrak B_{sr}=
\int_{-R}^{R}[WG_{srr}-W_sG_{rr}]_{s=-S}^{S}\,dr
+\int_{-S}^{S}[W_{ss}G_r-W_{ssr}G]_{r=-R}^{R}\,ds.
\tag{14}
\]

This is one ordered integration-by-parts convention. It keeps
tangential derivatives on the edges; if those are integrated further,
the resulting corner terms must also be retained. No limit of the
individual axis and mixed edge terms is asserted.

The finite box is an analytic localization of the **complete**
correlation identity, not a replacement for the manuscript's hybrid
source cutoff. If the full-amplitude observation \(J_{j,N}\) is used,
its original staircase \(n\le Ne^{-2y}\), support \(0\le y\le V_N\),
contour displacement, full stationarity, and complete source-tail
payment all remain as in Note 36. No finite-box identity here is a
proof of an all-\(N\) staircase coefficient rule. No staircase entry,
endpoint, contour, or source-index boundary has been silently moved
or dropped.

## 6. Continuation criterion

The exact theta identity (1) is available for a localized arithmetic
investigation. The natural global axis/mixed mechanism has already
failed the integrability gate by (9); a numerical pilot cannot repair
that definition. Any replacement should first combine enough terms
to cancel (6)–(8), prove the required weighted integrability uniformly
on its declared domain, and state its source-prescribed coefficient
rule and full error budget. A finite, full-stationary strict-sign
pilot with \(\kappa_j=0\) can remain an independent diagnostic, with
its scope clearly distinguished from a validation of the rejected
split. The complete correlation and staircase targets of Note 36
remain open.


## 7. Verification and companion results

The [checker](../../numerics/check_poisson_parity_heat_obstruction.py) and [receipt](../../numerics/POISSON_PARITY_HEAT_OBSTRUCTION_CHECKS_20261015.json) contain 27 exact-algebra or sensitivity assertions and 12 independent ball-arithmetic comparisons of the primitive identity, with complete Gaussian lattice tails at 256 bits. In particular, omitting the parity factor produces a disjoint enclosure at the origin. These finite checks support the normalization and implementation; the analytic argument in Section 3 proves the unbounded-tail obstruction.

[Note 40](../03_effective_bridge/40_FIXED_THETA_STATIONARY_BASELINE_20261015.md) records six fresh full-stationary root checks with the frozen zero-loss rule. They validate a bounded baseline, not the inadmissible sector split. [Review 27](../../reviews/27_POISSON_OBSTRUCTION_AND_WEIGHTED_REMAINDER_REVIEW_20261015.md) records the internal proof and numerical audit.

Replay with Python and python-flint available:

    python3 papers/investigations-2/active/21_quaternion_theta_geometry/numerics/check_poisson_parity_heat_obstruction.py --output /tmp/inv21-poisson-parity-replay.json
