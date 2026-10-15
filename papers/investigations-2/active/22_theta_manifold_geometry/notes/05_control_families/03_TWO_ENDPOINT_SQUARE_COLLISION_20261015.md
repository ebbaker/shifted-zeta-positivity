# Two odd source endpoints still permit a positive weighted-square collision

15 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**. This note contains an analytic endpoint reduction and a validated four-mode collision certificate. It is a non-theta control, not a theta sign result. The manuscript is unchanged.

## Result

There are fixed positive weights on the first four square nodes and a fixed positive normalization such that

\[
 \Phi_a'(0)=\Phi_a'''(0)=0,\qquad
 \psi_a'(0)=\psi_a'''(0)=\psi_a^{(5)}(0)=-\tfrac12,
\]

while, at the fixed time `T=1/100`,

\[
 H_a(T,x_*)=H_{a,x}(T,x_*)=0,\qquad H_{a,xx}(T,x_*)>0,
 \qquad83.5323729<x_*<83.5323730.
\]

The next odd source endpoint does not vanish: after normalization,
`Φ_a^(5)(0)` lies within `8.0×10^-8` of `−2.65684411198`. Thus the source is not even; its even half-line extension is `C^4` and not `C^5`. The physical transform is nevertheless entire in spectral coordinate and heat time, as for the earlier finite-square control.

This rejects support-only nonnegative-polynomial localizers even after imposing **both** `Φ′(0)=0` and `Φ‴(0)=0` and primitive normalization. It does not reject the full endpoint hierarchy, modular reflection, full elliptic translation, or the actual equal theta coefficients.

## 1. The exact endpoint geometry

Use the manuscript's modes

\[
 \lambda_n=\pi n^2,\quad
 \phi_n(u)=e^u(2\lambda_n^2e^{8u}-3\lambda_ne^{4u})e^{-\lambda_ne^{4u}},
 \quad \Phi_a=\sum_{n\ge1}a_n\phi_n.
\]

Write `φ_n^(k)(0)=exp(−λ_n)P_k(λ_n)`. Differentiation gives the polynomial recurrence

\[
 P_{k+1}(z)=(1-4z)P_k(z)+4zP_k'(z),\qquad P_0(z)=2z^2-3z,
\]

and in particular

\[
 P_1(z)=-8z^3+30z^2-15z,
\]
\[
 P_3(z)=-128z^5+1440z^4-4232z^3+3270z^2-375z.
\]

Set `d_n=P_1(λ_n)` and `r_n=P_3(λ_n)/P_1(λ_n)`. The exact identity

\[
 P_3(z)=(16z^2-120z+49)P_1(z)+360z
\]

yields

\[
 r(z)=16z^2-120z+49-\frac{360}{8z^2-30z+15},
\quad
 r'(z)=32z-120+
 \frac{360(16z-30)}{(8z^2-30z+15)^2}>0\quad(z\ge4\pi).
\]

The denominator is positive at `4π` and increasing thereafter. Also `d_1>0` and `d_n<0` for every `n≥2`. Arb encloses

\[
 r_1=1067.272372995146223307\ldots,\quad
 r_2=1067.254837985498397370\ldots,\quad
 r_3=9447.022516199873461683\ldots.
\]

For any nontrivial nonnegative finite source satisfying the first endpoint, `a_1>0`. Rescale to `a_1=1` and put

\[
 v_n=a_ne^{-(n^2-1)\pi},\qquad v_1=1,
 \quad b_n=-\frac{v_nd_n}{d_1}\quad(n\ge2).
\]

The two endpoint conditions are exactly

\[
 b_n\ge0,\qquad\sum_{n\ge2}b_n=1,\qquad
 \sum_{n\ge2}b_nr_n=r_1.
\]

Consequently

\[
 \sum_{n\ge3}b_n(r_n-r_2)=r_1-r_2,
 \qquad
 \boxed{\sum_{n\ge3}b_n\le
 \frac{r_1-r_2}{r_3-r_2}
 =2.0925412638125107308864751207449729\ldots\times10^{-6}.}
\]

The argument also applies to nonnegative infinite sources when these endpoint sums converge absolutely. This stringent bound controls the **endpoint-normalized masses** `b_n`, not the original coefficients `a_n`; it does not prohibit very large high-node coefficients.

There is an exact convex description. Set

\[
 c_n=-d_1/d_n>0,\qquad
 \eta_n=\frac{r_1-r_2}{r_n-r_2}\in(0,1)\quad(n\ge3),
 \qquad G_n(t,x)=e^{\pi n^2}H_n(t,x),
\]

and define the three-mode vertex

\[
 F_n=G_1+c_2G_2+\eta_n(c_nG_n-c_2G_2)
     =G_1+c_2(1-\eta_n)G_2+c_n\eta_nG_n.
\]

Every `F_n` has positive weights on nodes `1,2,n` and satisfies both odd source endpoints. Conversely, every normalized admissible finite source is a convex combination of these vertices: define

\[
 q_n=b_n(r_n-r_2)/(r_1-r_2),\qquad
 q_n\ge0,\quad\sum_{n\ge3}q_n=1.
\]

Then its scaled transform is `G=∑q_nF_n`. In particular, the two endpoints do **not** make the positive finite-source class empty. The collision certificate below rules out the stronger hope that their moment constraints alone exclude collisions.

## 2. A certified four-mode collision

At `T=1/100`, put

\[
 D(x)=F_3'(T,x)F_4(T,x)-F_3(T,x)F_4'(T,x).
\]

On the exact decimal interval `I=[83.5323729,83.5323730]`, the complete-integral certificate gives

\[
 D(83.5323729)\in(-2.9090,-2.9089)10^{-29},
 \qquad D(83.5323730)\in(1.8244,1.8245)10^{-29},
\]
\[
 D'(I)\subset(4.7333,4.7335)10^{-22}>0,
 \qquad (F_3-F_4)(I)\subset(-7.7081,-7.7080)10^{-11}<0.
\]

Thus `D` has exactly one root `x_*` in `I`. Define the **fixed** mixing parameter

\[
 q_*=-\frac{F_4(T,x_*)}{F_3(T,x_*)-F_4(T,x_*)},
\qquad
 q_*\in(0.8377475051,0.8377475108).
\]

Then `G=q_*F_3+(1-q_*)F_4` has `G(T,x_*)=0`, and the Wronskian identity gives `G_x(T,x_*)=0`. Its curvature satisfies

\[
 G_{xx}(T,x_*)\in(6.1408328,6.1408349)10^{-12}>0.
\]

All weights are fixed after this construction, and remain independent of heat time. Their endpoint-scaled values are

\[
 v_1=1,\quad v_2=c_2[1-q_*\eta_3-(1-q_*)\eta_4],
 \quad v_3=c_3q_*\eta_3,\quad v_4=c_4(1-q_*)\eta_4.
\]

The raw coefficients `a_n=v_n exp((n²−1)π)` are approximately

\[
 (a_1,a_2,a_3,a_4)
 =(1,\ 1.00000025427610,\ 0.83774751358710,\ 24193346.3659).
\]

The JSON records enclosures, rather than treating these displayed rounded numbers as exact weights. Exact weights are defined by the unique Wronskian root and the displayed formulas. The large fourth coefficient is compatible with the small `b`-mass bound because of its Gaussian endpoint factor.

For these raw weights,

\[
 \psi_a'(0)=-0.500000000034843223\ldots<0.
\]

Multiplying all weights by the fixed positive number `s_a=−1/(2ψ_a′(0))≈0.999999999930313554` imposes `ψ_a′(0)=−1/2`. Since `8Φ_a=ψ_a″−ψ_a`, the two exact source endpoints give `ψ_a‴(0)=ψ_a^(5)(0)=−1/2` as well. Scaling preserves the collision, positivity and nondegeneracy. The next source endpoint is certified nonzero, as stated above.

## 3. Completeness of the integral certificate

The checker uses python-flint 0.9.0 at 160-bit precision. It evaluates 44 Acb integrals on `[0,1]`, adds explicit full tails, and passes 26 explicit scalar, interval and exact-algebra assertions. Root existence follows from opposite endpoint signs and continuity; root uniqueness follows from the interval derivative bound. A sampled near-zero is not substituted for an existence proof.

For `0≤t≤1/2`, `u≥1`, and derivative or moment order `0≤k≤6`,

\[
 k\log u+t u^2+9u
 \le\tfrac12 e^{2u}+15e^u
 \le\tfrac{\pi}{2}e^{4u}
 \le\tfrac{\lambda_n}{2}e^{4u}.
\]

The middle inequality follows by dividing by `e^(4u)`, using monotonicity, and certifying `e^(−2)/2+15e^(−3)<π/2`. Therefore the normalized mode tails obey

\[
 \int_1^\infty u^k e^{tu^2}e^{\lambda_n}\phi_n(u)\,du
 \le\lambda_n\exp\{\lambda_n-4-(\lambda_n/2)e^4\}.
\]

This bounds every oscillatory jet by its positive absolute moment and covers the complete half-line, not a truncated transform. For `n=1` the displayed allowance is below `7.554×10^-38`, and it decreases rapidly for the remaining modes.

To enclose the whole root bracket without losing the small signed values, the checker first combines each vertex's centered jets through order three. Taylor's formula then bounds its variation using a complete positive fourth absolute moment. The endpoint and corner normalizations enter algebraically through the exact mode definitions and final primitive scaling. There is no missing tail in square index for this finite-support control.

The ratio identity is checked in exact integer polynomial arithmetic. Strict scalar inequalities are certified by Arb; monotonicity for every `n≥2` uses the displayed analytic derivative argument. The saved numerical count is not a count of independent theorems.

## 4. Qualitative continuation to positive weights at every square

The restriction to four support nodes can be removed while preserving both source endpoints. Keep `a_1=1`, add `ε∑_{n≥5}φ_n` with `ε>0`, and allow `v_2,v_3,v_4,x` to vary near the certified values at fixed `T=1/100`. In endpoint-scaled variables the two endpoint equations are linear, with `v_2,v_3` minor

\[
 \Delta_{23}=d_2d_3(r_3-r_2)>0.
\]

The certificate encloses this minor near `1.49267320543305×10^13`. It permits solving the endpoints for `v_2,v_3` in terms of `v_4,ε`.

At `ε=0`, the remaining endpoint-compatible tangent direction satisfies

\[
 \frac{\partial G}{\partial v_4}
 =-\frac{F_3-F_4}{c_4\eta_4}\ne0.
\]

At the collision `G_x=0`, so the reduced Jacobian of `(G,G_x)` with respect to `(v_4,x)` has determinant

\[
 \boxed{\left(-\frac{F_3-F_4}{c_4\eta_4}\right)G_{xx}\ne0.}
\]

Its certified enclosure is centered at `9.27499770825×10^-10` with radius below `1.5×10^-16`. The implicit function theorem therefore continues the two endpoints and double collision for all sufficiently small positive `ε`. The complete added tail and all required derivatives converge locally uniformly. The first four weights remain positive by continuity; every later raw weight equals `ε>0`. Positive primitive normalization is imposed afterward and preserves all zero conditions. The nonzero fifth source endpoint also persists by continuity.

This is a qualitative continuation, **without a certified numerical epsilon radius**. It supplies full positive square support and makes every finite ordinary and adjacent-square localizing matrix strictly positive definite. It does not restore source reflection or the elliptic multiplier.

## 5. Discovery scope, replay and consequences

The exploratory discovery run used the six nodes `1,…,6`, the five fixed times `{0.01,0.05,0.1,0.25,0.5}`, and integer spectral samples `20,…,300`. All five grids were evaluated before candidate refinement was stopped after robust candidates had been found. The run reported 468 pair-Wronskian sign changes; not all were refined, and no claim is made that each yields an admissible collision. The first selected positive mixture used the vertices `F_3,F_4` near `x=83.53237296145` at `T=0.01`. Discovery used 128-bit arithmetic with looser integral tolerances; the saved 160-bit fixed-bracket certificate is a separate, fast replay and is the evidence for the theorem.

The small saved JSON distinguishes this historical search scope from the replay actually executed. The optional search mode is exploratory; the default invocation certifies the fixed bracket and exact endpoint construction. The interrupted broad refinement is not presented as a completed exclusion search.

The [complete checker](../../numerics/check_theta_two_endpoint_control.py) and [160-bit receipt](../../numerics/THETA_TWO_ENDPOINT_CONTROL_20261015.json) retain the exact endpoint construction, tail allowances, interval enclosures, source digest and discovery scope.

From the investigation's `numerics/` directory, run:

```sh
python3 check_theta_two_endpoint_control.py --output THETA_TWO_ENDPOINT_CONTROL_20261015.json
```

The dependency is python-flint 0.9.0. Without `--output`, the checker prints its JSON record; `--search` additionally runs the bounded exploratory discovery mode. No remote data or machine-specific archive path is needed.

The concrete research conclusion is that adding the next odd endpoint is a genuine restriction but still does not supply collision exclusion. The endpoint mass concentration theorem is useful quantitative information; its coexistence with this collision shows that concentration in that norm is not a sufficient physical sign mechanism. The next useful arithmetic target must exploit stronger coefficient coupling, or prove a signed consequence that this four-mode and full-support continuation explicitly fail. No assertion is made about every finite endpoint hierarchy.
