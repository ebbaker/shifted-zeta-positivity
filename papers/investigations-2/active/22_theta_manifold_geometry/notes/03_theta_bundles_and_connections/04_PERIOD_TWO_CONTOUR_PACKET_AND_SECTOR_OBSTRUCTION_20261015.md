# Period-two contour packet and an exponential sector obstruction

15 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**. This bounded calculation derives an exact identity and a limitation of a proposed estimate; it proves no new theta sign region or collision exclusion.

## Result and decision

The transverse period-two experiment closes exactly, including its bottom edge, shifted heat weight, shifted polynomial factors, and every bilocal cross term. It does not yield a positive term by itself. In fact the shifted ray and bottom edge each grow exponentially with spectral height while their complete sum stays bounded. Even their separate Laguerre expressions have exponentially large modulus after their first rank-one cancellation. Estimating these sectors independently therefore introduces a serious artificial cost.

The identity also holds for arbitrary fixed polynomial-growth weights on the square lattice. Period two, Jacobi heat, and square support do not impose the missing coefficient-shift relation. The separately certified positive weighted collision control consequently passes this contour identity. Full elliptic quasi-periodicity, or square support combined with complete modular reflection, imposes stronger relations and is not rejected by this experiment.

The appropriate decision is to retain the identity as a checked tool, but stop the proposed independent-sector estimate. A renewed use must identify a cancellation-preserving inequality for the complete packet and specify the additional relation between coefficients that supplies its sign.

## 1. Holomorphic source and declared class

Let a_{-n}=a_n be coefficients of at most polynomial growth. On Re z>0 set

\[
 F_a(z)=a_0+2\sum_{n\ge1}a_n e^{-\pi n^2z},\qquad
 A_a(z)=z^{1/4}\{z^2F_a''(z)+\tfrac32 zF_a'(z)\}.
 \tag{1}
\]

Use the unique branch L(z)=Log z on the right half-plane that is real on the positive axis; define z^{1/4}=exp(L(z)/4) and u(z)=L(z)/4. All differentiated series converge locally uniformly there. In particular

\[
 F_a(z-2i)=F_a(z),\qquad F_a^{(k)}(z-2i)=F_a^{(k)}(z).
 \tag{2}
\]

For the ordinary theta source a_n=1. In the original elliptic notation z=-iτ, so (1) equals

\[
 (-i\tau)^{1/4}(\tau^2\partial_\tau^2+\tfrac32\tau\partial_\tau)
 \vartheta(0,\tau).
\]

The differential factors eliminate the n=0 term. For real u≥0, q=e^{4u}, A_a(q) is the complete physical source Φ_a(u). Put

\[
 c_j(x,u)=u^j\cos(xu+j\pi/2),\qquad
 d\nu_t(z)=\frac14e^{tL(z)^2/16}A_a(z)\frac{dz}{z}.
 \tag{3}
\]

Then

\[
 h_j(t,x)=\int_1^\infty c_j(x,u(q))\,d\nu_t(q).
 \tag{4}
\]

The positive physical heat multiplier remains exactly as written. It is not replaced by Jacobi evolution. For fixed complex t,x the integrals converge, locally uniformly with every fixed parameter derivative: theta-derivative decay exp(-π Re z) dominates logarithmic heat growth and polynomial factors on the strips used below.

## 2. Exact ray-plus-edge identity

Let z_*=1-2i. Orient the edge B from 1 to z_* and the ray V from z_* to infinity-2i. Define

\[
 B_j=\int_B c_j(x,u(z))\,d\nu_t(z),\qquad
 V_j=\int_V c_j(x,u(z))\,d\nu_t(z).
\]

Cauchy's theorem on the rectangle with vertices 1,Q,Q-2i,1-2i gives

\[
 \int_1^Q c_j\,d\nu_t
 =B_j+\int_{1-2i}^{Q-2i}c_j\,d\nu_t
   +\int_{Q-2i}^{Q}c_j\,d\nu_t.
 \tag{5}
\]

The last edge tends to zero as Q→∞, uniformly on compact t,x sets. Thus

\[
 \boxed{h_j=V_j+B_j.}\tag{6}
\]

The sign of the bottom edge in this formula is positive; in the z coordinate its direction is downward. Formula (2) rewrites the ray explicitly as

\[
 V_j=\frac14\int_1^\infty
 e^{tL(q-2i)^2/16}(q-2i)^{1/4}
 \{(q-2i)F_a''(q)+\tfrac32F_a'(q)\}
 c_j(x,u(q-2i))\,dq.
 \tag{7}
\]

All displayed shifted weights are necessary. Periodicity applies to F_a and its derivatives, not to L, the heat multiplier, the phase, or their polynomial coefficients. For an explicit edge parametrization, set z(r)=1-2ir, 0≤r≤1:

\[
 B_j=-\frac i2\int_0^1
 e^{tL(z(r))^2/16}z(r)^{1/4}
 \{z(r)F_a''(z(r))+\tfrac32F_a'(z(r))\}
 c_j(x,u(z(r)))\,dr.
 \tag{8}
\]

The branch stays in Re z=1 on this edge. The sums are real for real data; the individual sectors ordinarily are complex.

## 3. Complete bilocal Laguerre and pi/4 chord packets

Use the formal oriented chain Γ=V+B, with the scalar measure (3). Absolute convergence justifies all products and interchange of the two source variables. For j=0,1,

\[
 \mathcal L_j=h_{j+1}^2-h_jh_{j+2}
 =\int_\Gamma\int_\Gamma
 K_j(x;u,v)\,d\nu_t(z)\,d\nu_t(w),
\]

where u=u(z), v=u(w), and

\[
 K_j=\frac{(uv)^j}{4}
 \{(u+v)^2\cos(x(u-v))+(-1)^j(u-v)^2\cos(x(u+v))\}.
 \tag{9}
\]

This elementary trigonometric identity remains valid for complex u,v. The energy kernel is likewise

\[
 E=\int_\Gamma\int_\Gamma
 \frac{(1+uv)\cos(x(u-v))+(1-uv)\cos(x(u+v))}{2}
 \,d\nu_t(z)\,d\nu_t(w).
 \tag{10}
\]

In terms of sector jets, the exact Laguerre expansion is

\[
 \boxed{\mathcal L_j
 =(V_{j+1}^2-V_jV_{j+2})+(B_{j+1}^2-B_jB_{j+2})
 +2V_{j+1}B_{j+1}-V_jB_{j+2}-B_jV_{j+2}.}
 \tag{11}
\]

For the strategy's actual pi/4 target, set y=x+ℓ and

\[
 \mathcal C_j(t;x,y)=h_j(t,x)\{h_j(t,y)-h_{j+1}(t,y)\}.
\]

Its symmetric bilocal kernel is

\[
 \frac12\left[
 c_j(x,u)\{c_j(y,v)-c_{j+1}(y,v)\}
 +c_j(x,v)\{c_j(y,u)-c_{j+1}(y,u)\}
 \right].\tag{12}
\]

The complete ordered sector identity is

\[
 \boxed{\mathcal C_j
 =V_j(x)[V_j(y)-V_{j+1}(y)]
 +V_j(x)[B_j(y)-B_{j+1}(y)]
 +B_j(x)[V_j(y)-V_{j+1}(y)]
 +B_j(x)[B_j(y)-B_{j+1}(y)].}\tag{13}
\]

The middle terms are distinct ordered products; neither may be dropped. Their symmetrization gives twice one mixed bilocal integral, not twice either directed product.

The angular interpretation uses the **full** condition h_{j+1}(t,x)=0 and the constant sign of h_j on [x,y]. In the contour variables the stationary condition is V_{j+1}(x)+B_{j+1}(x)=0. Neither sector is separately stationary. Equations (11)–(13) impose no such false sector condition. The source has not been integrated by parts into a primitive here, so no primitive endpoint constant has been removed; (8) is an additional contour edge, not a replacement for that constant.

## 4. The artificial exponential growth is unavoidable for this split

Assume now a_n≥0 for n≥1, with at least one nonzero coefficient, and take fixed real t. Set

\[
 L_*=\Log(1-2i)=\tfrac12\log5-i\arctan2,
\quad u_*=L_*/4,
\quad \kappa=iu_*=\frac{\arctan2}{4}+i\frac{\log5}{8}.
\]

Write σ=Re κ=arctan(2)/4>0 and

\[
 C=-\frac{e^{tL_*^2/16}A_a(z_*)}{2i}.\tag{14}
\]

This coefficient is nonzero. Indeed periodicity makes F_a'(z_*)=F_a'(1) real and F_a''(z_*)=F_a''(1)>0; after factoring z_*^{5/4}, the remaining factor in A_a(z_*) is

\[
 z_*F_a''(1)+\tfrac32F_a'(1),
\]

whose imaginary part is -2F_a''(1)<0.

Endpoint integration by parts gives, for every fixed j,

\[
 \boxed{
 V_j(t,x)=C\kappa^j\frac{e^{\kappa x}}x\{1+O(x^{-1})\},\qquad
 B_j(t,x)=-C\kappa^j\frac{e^{\kappa x}}x\{1+O(x^{-1})\}}
 \quad(x\to+\infty).\tag{15}
\]

Here κ≠0. To verify the signs and factors, write dν_t=G(z)dz and split cosine into its two exponentials. For the growing exponential exp(ixu(z)), use u'(z)=1/(4z). The lower endpoint of the ray contributes

\[
 -\frac{4z_*G(z_*)}{2ix}e^{ixu_*}
 =-\frac{e^{tL_*^2/16}A_a(z_*)}{2ix}e^{ixu_*},
\]

which is exactly C e^{κx}/x. The edge has the opposite contribution at its upper endpoint z_*. The exp(-ixu) branch has modulus at most one on these contours. Repeated integration by parts is justified because every differentiated amplitude has integrable exponential cusp decay; the growing branch has modulus at most exp(σx). Two integrations give the stated error. Repeating gives an expansion to any fixed order, with the corresponding differentiated expansions in x. There is no unexamined moving upper endpoint.

By contrast every original real-axis h_j is bounded in x by its finite absolute source moment. Thus the two exponentially growing terms in (15) cancel in the physical observation.

### Laguerre and actual chord consequences

The leading rank-one jets in a single sector cancel in its Laguerre expression. It would be incorrect to infer an x^{-2} Laguerre term directly from (15). Using the next endpoint orders instead gives

\[
 \boxed{
 \mathcal L_j[V]
 =-C^2\kappa^{2j}\frac{e^{2\kappa x}}{x^4}
 \{1+O(x^{-1})\},\qquad j=0,1.}\tag{16}
\]

For example, write V_0=C exp(κx)[x^{-1}+a x^{-2}+b x^{-3}+⋯]. In (V_0')²-V_0V_0'', the x^{-2} and x^{-3} terms cancel, and the x^{-4} coefficient is -1 independently of a,b. The differentiated version gives -κ² for j=1. The same leading term occurs in the B diagonal, since B_j=h_j-V_j and the physical h_j are bounded; mixed terms in (11) cancel these large contributions.

For the actual pi/4 product, rather than a Wronskian chord, fixed ℓ>0 and y=x+ℓ give

\[
 \boxed{
 V_j(x)[V_j(y)-V_{j+1}(y)]
 =(1-\kappa)\kappa^{2j}C^2
 \frac{e^{\kappa(x+y)}}{xy}\{1+O(x^{-1})\}.}\tag{17}
\]

The coefficient is nonzero. The B diagonal has the same leading coefficient and each directed mixed term its negative. These complex sector expressions have no separate real sign interpretation. Equation (17) does not impose stationarity on V or B, and it is distinct from the smaller leading term of an ordinary determinant chord.

### Precise limitation

A bound of the form |V_0|²≤P(|x|)E with P polynomial, or a uniform-in-height version, cannot hold: the left side grows exponentially and E is bounded. The same reasoning rejects polynomial-height payments of the absolute diagonal Laguerre or chord sectors. This is a statement about independently paid sectors, not a proof that the complete signed theta packet fails.

Exponential cost in spectral height x must not be confused with cost in a cutoff parameter N. The current collision-exclusion criterion permits coefficients that are merely locally bounded at every finite event; the large-height result alone does not contradict that criterion. It also does not exclude a new estimate that preserves all cancellations in (11) or (13). The bounded pilot supplies no such estimate.

## 5. What period two leaves undetermined

For the full elliptic extension

\[
 \Theta_a(\zeta,\tau)=\sum_{n\in\mathbb Z}
 a_n e^{\pi in^2\tau+2\pi in\zeta},
\]

period two in τ and Jacobi heat hold termwise for every fixed coefficient sequence. The missing elliptic multiplier has the explicit defect

\[
 \boxed{
 e^{\pi i\tau+2\pi i\zeta}\Theta_a(\zeta+\tau,\tau)
 -\Theta_a(\zeta,\tau)
 =\sum_{n\in\mathbb Z}(a_{n-1}-a_n)
 e^{\pi in^2\tau+2\pi in\zeta}.}\tag{18}
\]

The usual elliptic law is therefore equivalent to a_{n-1}=a_n for all integers. This is absent from the period identity and from every support-only square-gap localizer.

The [companion square-support calculation](../05_control_families/01_SQUARE_SUPPORT_ENDPOINT_COLLISION_OBSTRUCTION_20261015.md) certifies a three-mode positive weighted source retaining the first source endpoint with a nondegenerate collision at t=1/4. It obeys the period identity above and Jacobi heat, while (18) is nonzero. Consequently period two plus those weaker hypotheses cannot establish the required pi/4 chord or stationary exclusion. This control does not obey complete source reflection. The companion reflection-rigidity note proves that square support plus full modular reflection forces constant weights; its conclusion is not contradicted here. The next certificate must use one of these coefficient-coupling relations at the step where it rejects the control, rather than treating input uniqueness as a sign theorem.

## 6. Certified bounded replay and tail bounds

The companion [check_period_two_contour.py](../../numerics/check_period_two_contour.py) uses python-flint Arb/Acb at 192 bits. It records the runtime and script hash. It uses N=6 theta modes and real-ray cutoff Q=32, with the following explicit full-theta error bounds. These bounds hold for 0≤t≤1/2 and real x; the recorded examples use t=1/4. They are not empirical truncation estimates.

For k=1,2 and Re z=q≥1,

\[
 |F^{(k)}(z)|\le3\pi^k e^{-\pi q},\qquad
 |F^{(k)}(z)-F_N^{(k)}(z)|
 \le3\pi^k(N+1)^{2k}e^{-\pi(N+1)^2q}.\tag{19}
\]

To prove these bounds, compare successive absolute summands. Their ratio is at most 2^{2k}exp(-3πq)≤16exp(-3π)<1/3, and the same ratio bound applies to any later starting index. Including the factor two in F and summing the geometric tail gives the constant three.

On q≥Q=32 and -2≤Im z≤0, |z|≤3q, |z|^{1/4}≤q, |u(z)|≤q, and |Im u(z)|≤1/(2q). Also log(3q)²≤q: it holds initially because log96<5 and 25<32, and the derivative of log(3q)² is below one and decreasing there. Therefore the heat modulus is at most exp(q/32), while π-1/32>3. With π<4, the source polynomial factor in (3) is bounded by

\[
 \tfrac14 q(9\pi^2q+\tfrac92\pi)\le41q^2.
\]

Thus the absolute j-jet ray tail is bounded by

\[
 \boxed{R_j(x)=41e^{|x|/(2Q)}e^{-3Q}
 \sum_{k=0}^{j+2}\frac{(j+2)!}{(j+2-k)!}
 \frac{Q^{j+2-k}}{3^{k+1}}.}\tag{20}
\]

This covers both the real and shifted rays. It is intentionally conservative.

On the finite rectangle, |z|≤34, |z|^{1/4}<3, log|z|<4, |u(z)|<3/2, heat modulus<2, and phase modulus≤exp(σ|x|). With r=N+1, (19) gives the finite-contour lattice-tail bound

\[
 \boxed{T_j(x;\mathfrak l)
 =\mathfrak l(2448r^4+27r^2)(3/2)^j
   e^{\sigma|x|-\pi r^2},}\tag{21}
\]

where the path length is 31 for either finite ray and two for the edge. The coefficients follow by substituting the derivative bounds into (3), then using π<4. The endpoint A(z_*) used for asymptotic ratios is separately inflated by

\[
 |z_*|^{1/4}
 [3\pi^2r^4|z_*|^2+\tfrac92\pi r^2|z_*|]
 e^{-\pi r^2}.\tag{22}
\]

Hence those ratios enclose the full theta endpoint coefficient, not a silently truncated coefficient. All logarithms passed to Acb integration carry its analytic-branch flag. The code also checks the finite right-edge identity (5) before applying the infinite-ray tail bounds.

The record contains **73 exact algebra or interval-enclosure assertions**: directed chord and Laguerre expansions; endpoint rank-one cancellation and surviving coefficients; elementary tail gates; four consecutive jets on four finite rectangles; complete-theta infinite contour comparisons; both Laguerre branches; and both full pi/4 chord packets at x=32, y=32.1. None is a stationary-root or theta-sign certificate.

At t=1/4, the enclosures illustrate the artificial cancellation:

| x | physical H, approximate | shifted-ray magnitude, approximate | Laguerre-sector magnitude, approximate |
|---|---:|---:|---:|
| 20 | 4.674×10^-3 | 13.39 | 9.485×10^-2 |
| 40 | -4.155×10^-6 | 2.353×10^3 | 1.351×10^3 |
| 80 | 2.457×10^-12 | 9.373×10^7 | 8.032×10^11 |
| 120 | -4.509×10^-19 | 4.368×10^12 | 9.084×10^20 |

The table is illustrative; use the JSON balls for precision and the analytic argument for the unbounded conclusion. The full physical L_0 at x=120 is approximately 1.713×10^-37, although the separate diagonal has the displayed enormous modulus.

Replay in an environment containing python-flint 0.9.0:

```sh
python3 check_period_two_contour.py --output PERIOD_TWO_CONTOUR_CHECKS_20261015.json
```

This experiment supplies an exact arithmetic contour packet, a demonstrated sector-cost obstruction, and an explicit missing elliptic relation. A signed improvement for the complete theta observation remains open.

See the [full execution record](../../numerics/PERIOD_TWO_CONTOUR_CHECKS_20261015.json) and the [reflection-rigidity proof](../05_control_families/02_WEIGHTED_COMB_REFLECTION_RIGIDITY_20261015.md).
