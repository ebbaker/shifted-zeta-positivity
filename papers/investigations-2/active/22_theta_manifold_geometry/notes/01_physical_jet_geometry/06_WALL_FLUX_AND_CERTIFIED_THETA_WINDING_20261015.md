# Wall flux and a certified theta boundary winding

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from the current turn metadata. Internal mathematical review is not external refereeing or formal verification.

The spacetime criterion in [Note 04](04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md) can be implemented using signs of the two jet coordinates on boundary segments. Ordinary real roots may cross the spatial walls if their flux is retained. A complete-theta pilot on \([0.01,0.20]\times[25,45]\) certifies winding zero, with both \(H\) and \(H_x\) changing sign. A direct interior-strip certificate also succeeds. The pilot establishes feasibility and a reproducible comparison, without a demonstrated general computational advantage or progress on the global theta estimate.

## Root transport through moving walls

Let \(H_t=-H_{xx}\) be real analytic near the compact closure of

\[
D=\{(t,x):t_-<t<t_+,\ a(t)<x<b(t)\},
\]

where \(a,b\) are real analytic, \(a<b\), and no spatial slice of \(H\) is identically zero. Assume \(J=(H,H_x)\ne0\) on \(\partial D\) and \(H\ne0\) at the four corners. Let \(N_-,N_+\) count the simple real zeros on the two time faces.

For a wall \(c=a,b\), set \(F_c(t)=H(t,c(t))\). Its zeros are finite, since it is analytic and nonzero at the endpoints. At each zero \(t_j\), \(H_x\ne0\). Define

\[
\epsilon_j=\frac{\operatorname{sgn}F_c(t_j+\delta)
-\operatorname{sgn}F_c(t_j-\delta)}2,
\qquad
Q_c=\sum_j\operatorname{sgn}H_x(t_j,c(t_j))\epsilon_j, \tag{1}
\]

for sufficiently small positive \(\delta\). Tangential contacts of even order have \(\epsilon_j=0\); odd-order crossings have \(\epsilon_j=\pm1\). For transverse crossings,

\[
Q_c=\sum_{F_c=0}\operatorname{sgn}\{H_x(-H_{xx}+c'H_x)\}. \tag{2}
\]

With orientation \(dt\wedge dx\), the exact formula is

\[
\boxed{\quad
\operatorname{wind}_{\partial D}(H+iH_x)
=\frac{N_--N_+-Q_a+Q_b}{2}.
\quad} \tag{3}
\]

Consequently the total collision weight is

\[
K(D)=\sum_{(T,A)\in D:\,J(T,A)=0}\left\lfloor\frac{m(T,A)}2\right\rfloor
=\frac{N_+-N_-+Q_a-Q_b}{2}. \tag{4}
\]

**Proof.** A simple root \(x=r(t)\) has velocity \(r'=H_{xx}/H_x\). Near its meeting with a wall, \(\operatorname{sgn}H(t,c(t))\) is \(\operatorname{sgn}H_x\) times \(\operatorname{sgn}(c(t)-r(t))\). Thus \(Q_c\) counts the wall moving from below to above roots. At the lower wall this removes a root from the interval; at the upper wall it adds one. An interior event of order \(m\) adds \(2\lfloor m/2\rfloor\) real roots by local Hermite splitting. Hence

\[
N_+-N_-=2K(D)-Q_a+Q_b.
\]

This proves (4); the same-sign index law of Note 04 proves (3). Simultaneous events at different points add, and one-dimensional local degree handles wall tangencies. ∎

For the theta half-rectangle, \(H(t,0)>0\) makes \(Q_a=0\). If the right wall is fixed at \(R\) and its crossings are transverse,

\[
K(D)=\frac12\left[N_+-N_-+
\sum_{H(t,R)=0}\operatorname{sgn}(H_xH_{xx})(t,R)\right]. \tag{5}
\]

The wall may meet ordinary simple roots; it must avoid actual common zeros of \(H,H_x\). Note 04's no-wall-crossing formula is the special case \(Q_a=Q_b=0\).

## Scalar signs suffice on the boundary

Partition each wall into intervals whose endpoints have \(H\ne0\). If \(H\) has one strict sign throughout an interval, its contribution to \(Q_c\) is zero. If \(H_x\) has a fixed strict sign \(\sigma\), its contribution is

\[
\sigma\,\frac{\operatorname{sgn}H_{\rm end}-\operatorname{sgn}H_{\rm start}}2. \tag{6}
\]

The signed crossing degrees telescope, even with several crossings or tangencies. Thus no evaluation of \(H_{xx}\), or isolation of every temporal wall zero, is needed.

There is also a direct boundary version. Traverse the lower wall with increasing time, the final time face with increasing \(x\), the upper wall with decreasing time, and the initial time face with decreasing \(x\). On each segment certify a strict sign for at least one coordinate. Choose endpoints with \(H\ne0\). A segment with a strict sign of \(H\), or with \(H_x<0\), contributes zero to crossings of the positive imaginary ray. A segment with \(H_x>0\) contributes

\[
-\frac{\operatorname{sgn}H_{\rm end}-\operatorname{sgn}H_{\rm start}}2. \tag{7}
\]

Summing gives the winding. Under the analytic hypotheses above, finitely many zeros on each edge and nonzero corner values permit this endpoint choice. For a general continuous nonzero planar loop the endpoint requirement need not hold; for example its first coordinate could vanish identically. The following polygon method avoids that restriction.

On each segment, enclose the actual jet in an open coordinate half-plane. Choose rational polygon vertices so that both ends of each polygon edge lie in that same half-plane. The straight-line interpolation between the actual boundary segment and its polygon edge then stays in a convex set avoiding zero. These homotopies agree at common endpoints, giving the same winding globally. The rational vertices need not belong to the endpoint interval enclosures: their membership in the certified half-planes is the condition needed. Exact rational ray crossings calculate the polygon's integer degree.

All sign statements must hold on **whole segments**. Neither endpoint sampling nor a visually closed polygon certifies the true boundary map.

## Controls exposing a missing wall term

On \(D=(-1,1)\times(-1,1)\), all three controls below have nonzero boundary jets:

| Heat polynomial | \(N_-\) | \(N_+\) | \(Q_a\) | \(Q_b\) | Winding |
| --- | ---: | ---: | ---: | ---: | ---: |
| \(x^2-2t\) | 0 | 0 | 1 | −1 | −1 |
| \(x^3-6tx\) | 1 | 1 | 1 | −1 | −1 |
| \(x^4-12tx^2+12t^2\) | 0 | 0 | 2 | −2 | −2 |

All newly created real roots except the cubic's persistent central root have exited through the walls before the final slice. Equal endpoint root counts therefore do not imply no collision. For a tangential control, \(H=x\), lower wall \(a(t)=t^2\), and upper wall \(b=2\) give \(Q_a=0\); replacing \(t^2\) by \(t^3\) gives \(Q_a=1\), exactly balancing the lost root. Neither has a collision.

The [wall-flux checker](../../numerics/check_spacetime_wall_flux.py) passes **2,122 exact assertions on 88 domains**, plus two nontransverse-contact examples, using the existing rational Sturm helper. Degrees 2 through 12, both overall signs, fixed and affine moving walls, and enclosing and non-enclosing domains are covered. Direct oriented ray crossings, the flux formula, and the known event index agree. The [receipt](../../numerics/SPACETIME_WALL_FLUX_CHECKS_20261015.json) records finite polynomial controls, not theta data.

## Complete theta evaluation and tails

The [theta checker](../../numerics/check_theta_boundary_winding.py) uses the manuscript normalization

\[
H(t,x)=\int_0^\infty e^{tu^2}\sum_{n\ge1}\phi_n(u)\cos(xu)\,du,
\qquad
\phi_n=(2a_n^2e^{9u}-3a_ne^{5u})e^{-a_ne^{4u}},\quad a_n=\pi n^2. \tag{8}
\]

All terms \(\phi_n\) are positive on \(u\ge0\). The finite integral uses \(n\le4\), \(0\le u\le1\). Let \(T=1/5\) and \(J_*=77\). For \(p_n=e^{u-a_ne^{4u}}\),

\[
\phi_n=(p_n''-p_n)/8,
\qquad
\int_0^\infty\phi_n\,du
=\frac{\beta_n-\int_0^\infty p_n\,du}{8}<\frac{\beta_n}{8},
\quad \beta_n=(4a_n-1)e^{-a_n}. \tag{9}
\]

On \([0,1]\), the omitted modes contribute at most \(e^T B_4/8\) to every moment of order \(0\le j\le77\), where

\[
B_N=\frac{4\pi(N+1)^2e^{-\pi(N+1)^2}}
 {1-4e^{-\pi(2N+3)}}. \tag{10}
\]

Indeed the successive upper-bound terms \(4\pi n^2e^{-\pi n^2}\) have ratio at most the denominator's geometric ratio for \(n\ge N+1\).

On \(u\ge1\), use \(u^j\le e^{j(u-1)}\) and \(\phi_n\le2a_n^2e^{9u-a_ne^{4u}}\). The exponent \(Tu^2+(9+j)u-j-a_ne^{4u}\) has negative second derivative there; its tangent at one gives

\[
\int_1^\infty e^{tu^2}u^j\phi_n(u)\,du
\le \frac{2a_n^2e^{T+9-a_ne^4}}{4a_ne^4-9-J_*-2T}. \tag{11}
\]

Every denominator is positive. The successive majorants have ratio at most \(16e^{-3\pi e^4}<1\), so their sum is bounded by the first majorant divided by \(1-16e^{-3\pi e^4}\). This is a complete source tail over **all** modes, added to the omitted-mode bound on \([0,1]\).

The same split gives a common absolute moment majorant \(M\) through order 77. At the exact midpoint \((t_c,x_c)=(21/200,35)\), the checker computes 76 complete jet enclosures, orders 0 through 75, by Arb/Acb quadrature. For each component \(\partial_x^jH\), \(j=0,1\), it uses the bivariate Taylor polynomial

\[
\sum_{\ell=0}^{50}\sum_{k=0}^{12}
\frac{(x-x_c)^\ell(-(t-t_c))^k}{\ell!k!}
\partial_x^{\ell+2k+j}H(t_c,x_c). \tag{12}
\]

First expanding in real \(x\) at the actual \(t\), then in \(t\) at \(t_c\), bounds the remainder uniformly by

\[
M\left(\frac{10^{51}}{51!}
+e^{10}\frac{(19/200)^{13}}{13!}\right). \tag{13}
\]

The largest derivative order needed by the time remainder is \(50+26+1=77\); the spatial remainder requires at most 52. Thus no higher unbounded moment is omitted. Interval Horner evaluation encloses every full segment or strip, including coefficient and quadrature errors.

## The bounded pilot and comparison

At 160-bit working precision the [receipt](../../numerics/THETA_BOUNDARY_WINDING_PILOT_20261015.json) certifies:

| Quantity | Validated result |
| --- | --- |
| Exact box | \(1/100\le t\le1/5,\ 25\le x\le45\) |
| Complete source plus omitted-mode error per midpoint jet | Less than \(3.729\times10^{-33}\) |
| Uniform Taylor remainder per component | Less than \(4.923\times10^{-17}\) |
| Accepted boundary segments | 234 |
| Smallest certified boundary coordinate margin | Greater than \(1.906\times10^{-9}\) |
| Rational polygon winding | Exactly 0 |
| Scalar coordinate signs | Both \(H\) and \(H_x\) have certified positive and negative boundary values |
| Separate root-count cross-check | Two simple roots on each time face; \(H>0\) on both full spatial walls |
| Direct interior baseline | 128 full-time strips, each with one strict jet-coordinate sign |

The boundary uses 464 segment-range evaluations and 234 vertex evaluations, or 698 enclosures. Two optional whole-wall evaluations support the independent root-count check. The interior baseline uses 255 range evaluations, with time kept at its full width in every strip and subdivision only in \(x\). Both share the same 76 midpoint integrals and identical tail/Taylor estimates. It would be misleading to manufacture a two-dimensional gridding baseline when this simpler interior certificate works.

In a representative execution, shared quadrature took about 0.33 seconds; boundary subdivision and polygon calculation about 0.03 seconds; the interior strips about 0.21 seconds. Wall-clock values depend on machine, caching and interval-expression cost, and are retained only as implementation observations. The boundary has more enclosures but many use cached coefficients at a fixed time. Neither these timings nor this low-height box establish superiority over an optimized stationary or interior method. The meaningful completed result is a full-source, whole-boundary certificate on a sign-changing box and an explicit fair baseline. It supplies no improvement to a de Bruijn–Newman bound.

The checker passes **786 exact or interval assertions**. Independent process replay preserves all mathematical receipt content after removing timing fields. The saved polygon also permits a separate rational winding replay without rerunning quadrature. By Note 04, winding zero excludes interior collisions; the validated boundary and interior baseline separately cover the whole closed rectangle.

## Limits and next decision

The local phase \(\theta=\arg(H+iH_x)\), where defined, obeys

\[
\theta_t=-\theta_{xx}-\frac{E_x}{E}\theta_x,\qquad E=H^2+H_x^2. \tag{14}
\]

This does not give a regular maximum-principle argument across a collision: the phase is undefined there and the drift may diverge. The useful simplification is the boundary sign calculation on an already validated nonzero boundary. The underlying parabolic zero-number/degree mechanism is classical; see [Angenent, §3](https://people.math.wisc.edu/~angenent/preprints/extatic.pdf).

A further computational extension should require a shared-budget case where the boundary certificate succeeds and the optimized interior baseline fails or costs materially more. The present pilot does not meet that stronger threshold. The global theta boundary inequality, or any other arithmetic premise capable of proving an exhaustion, remains open.
