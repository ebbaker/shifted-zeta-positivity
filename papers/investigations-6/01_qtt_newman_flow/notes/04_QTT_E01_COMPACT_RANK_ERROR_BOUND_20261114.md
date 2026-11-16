# QTT-E01 — Compact rank and scaled observation error

13–14 November 2026, America/New_York. Prepared for **Edward Baker**
with substantial OpenAI Codex LLM assistance. Tool dispatch
**gpt-6.1-sol / ultra**. Separate backend verification unavailable.

**Proved in-note.** The first tuple \((d,m,L)=(512,64,72)\) gives an exact
polynomial QTT state with bond dimensions at most \(641\) and a uniform
scaled absolute observation error less than \(2^{-36}<10^{-8}\). The
bound covers \(0\le\lambda\le1/2,\ 40\le x=\Re z\le80,\ |\Im z|\le8\).
It applies to formal exact coefficients and contractions on the fixed
compact box. This is a quantitative approximation estimate. The
[fixed target](03_QTT_B01_FIXED_ANALYTICAL_TARGET_20261113.md) and
[frozen request](../research-progress/handoffs/QTT-E01-r1.md) specify
the norm and comparison. See the [result index](../../../../result-summaries/README.md),
[avoid index](../../../../avoid/README.md), [controls 12](../../../../result-summaries/12_collision_controls_and_screening.md)
and patterns [01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md) and
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## 1. Source and complex envelopes

Use the [complete even theta source](../../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/02_source.tex).
On the positive half-line, set \(\rho_u=\pi e^{4u}\),
\(r_n=n^2\rho_u\) and
\[
 W_\lambda(u)=e^{\lambda u^2+u}
              \sum_{n\ge1}(2r_n^2-3r_n)e^{-r_n},\qquad
 H_\lambda(z)=\int_0^\infty W_\lambda(u)\cos(zu)\,du .
\]
The integral uses the complete even reflection and is exactly the
full-line Fourier integral with factor \(1/2\). Put
\(\tau=1/2-\lambda\); then \(W_\lambda=e^{-\tau u^2}W_{1/2}\).
The positive-half-line series gives the holomorphic extension needed
below.

For complex \(v\) with \(-1/16\le\Re v\le33/16\) and
\(|\Im v|\le9/40\), put \(t=|r_n(v)|=\pi n^2 e^{4\Re v}\).
Then \(t>2n^2\) by \(\pi>3\) and \(e^{-1/4}\ge3/4\).
Also \(\Re r_n=t\cos(4\Im v)\ge t/2\), using
\(\cos b\ge1-b^2/2\) for \(|b|\le9/10\). The elementary maxima of
\(t^2e^{-t/4}\) and \(te^{-t/4}\) occur at \(t=8\) and \(t=4\),
respectively. Since \(e>2\),
\[
 (2t^2+3t)e^{-t/2}
 \le (128/e^2+12/e)e^{-t/4}<38e^{-n^2/2}.
\]
The sum of \(e^{-n^2/2}\) is at most \(1/(e^{1/2}-1)\le2\).
Thus the series converges locally uniformly on a neighborhood
of the closed rectangle. For example, the strict uniform margins in
\(t/n^2>2\) and \(\cos(4\Im v)>1/2\) persist on a sufficiently small
enlargement. The prefactor has modulus at most
\(\exp(33/16+(33/16)^2/2)<e^5<2^8\) there on the closed rectangle.
Consequently \(76\cdot 2^8<2^{15}\) bounds \(|W_\lambda(v)|\)
on that rectangle, uniformly in \(\lambda\).

Let \(\rho=5/4\). The ellipse \(v=1+(w+w^{-1})/2\) for \(|w|=\rho\)
has real range \([-1/40,81/40]\) and imaginary semiaxis \(9/40\).
We may take \(M_\rho=2^{15}\) for the ellipse and \(M_0=2^{15}\)
for \(\sup_{[0,2]} W_{1/2}\). For \(0\le u\le2\), a circle
\(|v-u|=1/16\) lies in the rectangle. On it,
\[
 |\Im(zv)|\le 80/16+8(33/16)<22,\qquad
 |\cos(zv)|\le e^{22}<2^{33}.
\]
Here \(e<11/4\) follows from its series by bounding the tail from
\(1/3!\) with ratios at most \(1/4\), and \(e^2<8\) follows.
Cauchy's derivative estimate therefore permits
\[
 M_2=2^{57}\ \ge\ \sup_{D,\ 0\le u\le2}
       |\partial_u^2[W_\lambda(u)\cos(zu)]|,
 \qquad 2!/(1/16)^2=2^9 ,
\]
where \(D\) denotes the fixed parameter box.

For the complete tail, \(n^4e^{-\pi(n^2-1)}\le e^{-2(n-1)}\)
by \(\log n\le n-1\) and \(3(n^2-1)\ge6(n-1)\). Thus for real
\(u\ge0\), \(W_{1/2}(u)\le4e^{u^2/2+u}\rho_u^2e^{-\rho_u}\).
For \(u\ge2\),
\[
 u^2/2+9u+2\log\rho_u\le u^2/2+17u+4
 \le (3/2)e^{4u}<\rho_u/2 .
\]
The first inequality uses \(\log\pi<2\). For the second, the
cubic Taylor polynomial gives \((3/2)e^{4u}\ge3/2+6u+12u^2+16u^3\).
Subtract the required quadratic and use \(u\ge2\). Substitution
\(s=\rho_u\), \(du=ds/(4s)\), now gives
\[
 T=\int_2^\infty e^{8u}W_{1/2}(u)\,du
 \le\int_{\rho_2}^\infty e^{-s/2}\frac{ds}{s}
 \le\frac{2}{\rho_2}e^{-\rho_2/2}<2^{-192}.
\]
In fact \(\rho_2/2>(3/2)2^8>192\). The scale
\(S(x)=e^{\pi x/8}/(1+x)^{7/4}\) has \(S_*\le2^{48}\) on
\([40,80]\) by \(\pi<22/7\), \(10\pi<32\), and \(e^2<8\).

## 2. Polynomial and exact tensor representation

The function \(G(w)=W_{1/2}(1+(w+w^{-1})/2)\) is analytic on an
annulus containing \(\rho^{-1}\le|w|\le\rho\). Its Laurent
coefficients \(b_k\) satisfy \(b_{-k}=b_k\) by the symmetry
\(G(w)=G(w^{-1})\), and \(|b_k|\le M_\rho\rho^{-k}\) for
\(k\ge0\) by the contour \(|w|=\rho\). On the unit circle this is
\(W_{1/2}(1+\cos\theta)=b_0+2\sum_{k\ge1} b_k\cos(k\theta)\).
Truncate the corresponding Chebyshev polynomial after \(k=d\)
to define \(p_d\). Since \(|\cos(k\theta)|\le1\),
\[
 \epsilon_d=\frac{2M_\rho\rho^{-d}}{\rho-1}
 \quad\text{bounds}\quad \|W_{1/2}-p_d\|_{[0,2]}.
\]
With \(q_m=\sum_{j=0}^m(-\tau u^2)^j/j!\) and \(0\le\tau u^2\le2\),
Taylor's remainder is at most \(E_m=2^{m+1}/(m+1)!\).
Writing \(P_\tau=p_dq_m\), use
\(W_\lambda-P_\tau=(W_{1/2}-p_d)e^{-\tau u^2}
+p_d(e^{-\tau u^2}-q_m)\) to get
\[
 \|W_\lambda-P_\tau\|_{[0,2]}
 \le\delta=\epsilon_d+(M_0+\epsilon_d)E_m .
\]

Write \(D_p=d+2m\) for the degree cap, \(h=2/2^L\) and
\(u_b=h/2+\sum_{k=1}^L c_k b_k\), \(c_k=h2^{L-k}\).
Define the column \(v(u)=(1,u,\ldots,u^{D_p})^{\mathsf T}\) and the
matrix \(A(t)\) with \((j,k)\) entry \(\binom jk t^{j-k}\) for
\(0\le k\le j\le D_p\), zero otherwise. The binomial formula gives
\(A(t)v(u)=v(u+t)\). With row \(p_\tau\) of monomial coefficients
of \(P_\tau\), the amplitude
\[
 \sqrt h\,p_\tau A(c_L b_L)\cdots A(c_1 b_1)v(h/2)
\]
is \(\sqrt h\,P_\tau(u_b)\). Taking the transpose of the entire
scalar product yields an ordinary coarse-to-fine matrix product
with cores \(A(c_k b_k)^{\mathsf T}\) and the transposed boundary
vectors. All bonds have dimension at most \(D_p+1=641\).
Each exponential \(e^{\pm iz u_b}\) is the product of
\(e^{\pm iz h/2}\) and \(e^{\pm iz c_k b_k}\). Contract with the state,
include an external \(\sqrt h\) for each exponential, and take the
half-sum for cosine. The result is
\(h\sum_b P_\tau(u_b)\cos(zu_b)\). The half-sum implements the
literal cosine, with the full-line normalization already accounted
for in the half-line integral.

## 3. Error transfer, exact allowance and baseline

For each midpoint cell and \(f(u)=W_\lambda(u)\cos(zu)\),
integrate the Taylor formula from its midpoint. The linear term
integrates to zero and the complex-valued remainder has absolute
integral at most \(M_2 h^3/24\). Summing \(2/h\) cells gives
\(2h^2 M_2/24\). At the nodes the polynomial replacement is bounded
by \(2e^{16}\delta\), because \(|\cos(zu)|\le e^{8u}\) and \(u\le2\).
The remaining omitted integral is bounded by \(T\). Thus
\[
 \sup_D S(x)\left|H_\lambda(z)-
                         h\sum_b P_\tau(u_b)\cos(zu_b)\right|
 \le S_*\left[T+\frac{2h^2}{24}M_2+2e^{16}\delta\right].
\]

For \(d=512\), \((4/5)^4<1/2\) gives \(\epsilon_d<2^{-110}\).
For \(m=64\), \(65!\ge2^{270}\), by using the largest power of two
below or equal to each factor, in blocks \(2\)–\(3\), \(4\)–\(7\),
\(8\)–\(15\), \(16\)–\(31\), \(32\)–\(63\), \(64\)–\(65\). Hence
\(E_m\le2^{-205}\). With \(h=2^{-71}\) and \(2e^{16}<2^{25}\),
the scaled allowances are

| Contribution | Upper allowance |
| --- | ---: |
| Complete continuum tail \(S_*T\) | \(2^{-144}\) |
| Midpoint quadrature for the complete integrand | \(2^{-40}\) |
| Chebyshev source approximation | \(2^{-37}\) |
| Heat Taylor remainder | \(2^{-116}\) |

For the last entry, \(M_0+\epsilon_d<2^{16}\) suffices. Their sum
is less than \(2^{-36}<10^{-8}\). These are certified upper
allowances from analytical inequalities. Exact series coefficients
give zero additional arithmetic-source truncation error. The exact
state and readout have zero core rounding, compression, arithmetic
and normalization error. The construction allocates no grid, invokes
no time integrator, and has no separately added time-integrator error.

A computed version may incur a node-uniform error \(e_{\rm node}\)
in the unweighted polynomial values or equivalently in the state
amplitudes divided by \(\sqrt h\). Pay \(2e^{16}e_{\rm node}\).
A subsequent compression with Euclidean error \(e_{\rm TT}\)
relative to that already perturbed state contributes at most
\(\sqrt2 e^{16}e_{\rm TT}\) by Cauchy–Schwarz against the cosine
vector with entries \(\sqrt h\cos(zu_b)\). Add readout arithmetic
error \(e_{\rm out}\) after both steps, then multiply their sum by
\(S_*\). These reference points avoid double counting. With
\(\eta=10^{-8}/4\), sufficient tolerances are
\(e_{\rm node}\le\eta/2^{73}\), \(e_{\rm TT}\le\eta/2^{73}\),
and \(e_{\rm out}\le\eta/2^{48}\). Each reserves at most \(\eta\)
since the corresponding scale times transfer factor is bounded
by the stated divisor. The exact allowance is below the remaining
\(\eta\). No such computed tolerances were demonstrated. If an
implementation changes to an evolved approximate state, its
accumulated evolution residual needs the separate inherited
[contractive estimate](../../../investigations-5/brainstorm/01_MPS_NEWMAN_FLOW_20261113.md).

The matched scalar baseline is the exact polynomial integral
\(\int_0^2 P_\tau(u)\cos(zu)\,du\). Its allowance is
\(S_*[T+2e^{16}\delta]\). It shares the tail and both polynomial
approximations and omits quadrature error. The QTT theorem gives a
representation bound for the midpoint state. It gives no smaller
allowance than the scalar integral and supplies no end-to-end cost
comparison or numerical stability result for the monomial cores.

## 4. Actual control screen

Use the witnesses in the [B01 comparison](../brainstorm/notes/01_QTT_B01_OBSERVATION_NORM_DECISION_20261113.md).
Euler-factor sources have translated modes, and weighted-square
and finite-prime controls change canonical coefficients or fail full
mode reflection. Their own half-line analyticity can still permit a
compact approximation. Reflected quartic and smooth primitive-compatible
controls lack the canonical square series used in the constants.
The latter retain their small-damping qualification. Atomic controls
lack the analytic density and finite-profile continuous extensions
require their own regularity and constants. RH-conditional controls
fail ordinary Dirichlet arithmetic, with their existence conditional.
Altered observations fail the literal cosine/Newman equation even
when their source is fixed. The actual-profile positive-measure
relaxation lacks an integer zero configuration and the literal field
readout. The quantitative \(10^{-8}\) allowance is untested here for
these other sources, and no control certificate was rerun.

The [rank-one event](../../../investigations-5/brainstorm/01_MPS_NEWMAN_FLOW_20261113.md)
has \(F_\lambda(z)=2+2e^{\lambda-T}\cos z\).
At \(T=1/4\) and \(z=17\pi\) its field and derivative vanish,
\(F_{zz}=2\), its two-bit state is rank one, and these time and
height coordinates lie in the fixed box. Its atomic source fails
the analytic-density premise. This witness excludes the generic
inference that low rank with positive amplitudes forbids a collision.
Colliding analytic sources can satisfy a compact approximation theorem
of this form. The result is a scaled absolute-error estimate.
