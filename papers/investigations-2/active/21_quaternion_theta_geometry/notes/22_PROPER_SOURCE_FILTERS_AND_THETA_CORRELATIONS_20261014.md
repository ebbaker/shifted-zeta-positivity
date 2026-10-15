# Proper source filters and theta correlations

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded current model: **gpt-6-astra (Codex)**; reasoning effort **ultra**.
Parallel analytic, numerical, and independent internal review work supported
this continuation of [Note 21](21_ONE_SIDED_STATIONARY_ESTIMATES_AND_THETA_PILOT_20261014.md).
The full source and outer asymptotic inputs are
[Note 12](12_SHIFTED_CONTOUR_FOUR_JET_PAYMENTS_20261014.md),
[Note 17](17_UNIFORM_OUTER_CUSP_SIGNS_AND_THRESHOLD_FOUR_20261014.md), and
[Note 19](19_OSCILLATORY_BLOCKS_AND_PAIRED_LAGUERRE_FORMS_20261014.md).

**Results.** A prescribed proper two-index filter absorbs a genuinely adverse
complement on both stationary branches in the finite pilot; a one-index
filter fails. For the fixed sharp rectangular filters considered here, endpoint terms
rule out uniformly small separate payments at arbitrary heights. A separate
Fourier argument rules out finite rational-coefficient jet identities for
nonzero compact source filters. A complete-source
Gaussian filter avoids those sharp endpoints and gives an exact time-shift
relation; its signed products pass a second finite pilot. None of these
results extends the height-104 cover or proves the unresolved all-height
stationary estimate.

## 1. The direct product criterion

Write \(h_k=\partial_x^kH(t,x)\), \(E=h_0^2+h_1^2\),
\(\mu=a^2+b^2>0\), and
\[
 C_j=-h_{j+2}-2ah_{j+1}-\mu h_j,\qquad
 \mathcal L_j=h_{j+1}^2-h_jh_{j+2},\qquad j=0,1.
\]
Use the same definition of \(C_k\) for every integer \(k\ge0\).
For a prescribed exact source split \(C_j=G_j+R_j\), fix
\(0\le\lambda\le1\) and a nonnegative loss \(K_j\). On the genuine
stationary set \(h_{j+1}=0\), the conditions
\[
 h_jG_j\ge0,\qquad h_j(R_j+\lambda G_j)\ge-K_jE                 \tag{S1}
\]
imply
\[
 \mathcal L_j=\mu h_j^2+(1-\lambda)h_jG_j
                 +h_j(R_j+\lambda G_j)\ge-K_jE.              \tag{S2}
\]
For use through a candidate collision, \(K_j\) must be prescribed without
an observed energy denominator and remain locally bounded there. Unlike
Note 21's residual-square condition, (S1) does not force \(R_j=0\) at
\(h_0=h_1=0\). It still requires substantive control in a neighborhood
of that point. A favorable retained product alone is insufficient.

All finite tests below prescribe \(\lambda=1/2\) and \(K_0=K_1=0\).
Their paired observations multiply a full physical jet by a complete
retained or complementary integral. Thus every arithmetic and integration
cross term remains present.

## 2. Proper rectangular filters: a successful adverse-product comparison

### Predetermined protocol and exact split

Before computing the partial integrals, the following family was fixed:

\[
 a=\pi/16,\quad b=1/4,\quad\mu=a^2+b^2,\quad
 \lambda=1/2,\quad K_0=K_1=0,
\]

\[
 (N,U)\in\{(1,1),(1,3/2),(2,1),(2,3/2)\}.
\]

For the individual theta source term \(\phi_n\), define the genuinely
proper retained source

\[
 g_k=e^{-ax}\Re\sum_{n=1}^N\int_0^U
 [i(u+ia)]^k e^{t(u+ia)^2+ixu}\phi_n(u+ia)\,du,
\]

\[
 G_j=-g_{j+2}-2ag_{j+1}-\mu g_j,\qquad R_j=C_j-G_j.
\]

Thus \(G_j\) is exactly the source filter with multiplier
\((u^2-b^2)\mathbf1_{n\le N,\,0\le u\le U}\). In Note 19's shared
coordinates its domain is \(n\le N,\ d_n\le v\le d_n+U\); this is an
original-coordinate rectangular filter, rather than a single shared
\(v\)-cutoff. No source multiplier was selected using a physical jet,
energy floor, or an observed sign.

All eight closed time slabs \([r/16,(r+1)/16]\), \(0\le r\le7\), were
predeclared. Even-index slabs were labeled development and odd-index slabs
holdout. Every filter was evaluated on both, without changing the filter,
centering, absorption fraction, or loss after seeing the results. The
holdout cells have disjoint interiors from the development cells; their
shared boundary times remain covered.

The tests are the direct product conditions

\[
 h_jG_j>0,\qquad h_j(R_j+\tfrac12G_j)>0
 \quad\text{on }h_{j+1}=0.
\]

Together they imply
\(h_jC_j=h_j(R_j+G_j/2)+h_jG_j/2>0\), and hence the one-sided estimate
with the predetermined \(K_j=0\). They do not require the complement
\(R_j\) itself to be favorable or zero.

### Both stationary sets are genuinely populated

The pilot uses the already certified full-source rectangles
\([101,102]\times[0,1/2]\) for \(j=0\) and
\([103,104]\times[0,1/2]\) for \(j=1\).

The exact paid endpoint transport from the first pilot proves one unique
\(h_1=0\) point in \((101,102)\) for every time. For the second branch,
the same transport gives opposite signs of \(h_2\) at 103 and 104, while
the whole-cell enclosure of \(h_3\) is strictly positive. Therefore for
every \(t\in[0,1/2]\), exactly one genuine \(h_2=0\) point lies in
\((103,104)\). In the respective constant normalizations, safe endpoint
bounds are

\[
 Z_1(t,101)>37,\quad Z_1(t,102)<-20,
\]

\[
 Z_2(t,103)<-26,\quad Z_2(t,104)>14.
\]

Here \(Z_k=e^{\pi x_c/8}h_k\), with \(x_c=101.5\) for the first
branch and \(x_c=103.5\) for the second. The normalization is held constant
across each cell and is positive. These are physical derivative conditions,
not derivatives of a varying normalization or selected approximate zeros.

### Complete-source transport and payment

For each filter and each of the 16 branch/time cells, the new calculation
encloses all retained center derivatives through order 28. Fixed filter
endpoints preserve the exact physical derivative and heat identities
\(\partial_xg_k=g_{k+1}\) and \(\partial_tg_k=-g_{k+2}\).

The Taylor transport uses space order 12 and time order 8. Its absolute
moment majorants are the original *complete-source* majorants. This is
valid because the retained source, complementary source, and absorption
factor source have multipliers

\[
 \chi_A,\qquad1-\chi_A,\qquad1-\tfrac12\chi_A
\]

respectively, each between zero and one. Their centered residual moment
payments are bounded by the corresponding full-jet payments combined as
\(P_{j+2}+2aP_{j+1}+\mu P_j\), for both spatial and temporal errors.
No extra omitted-source approximation is introduced.

The full residual center jets already include the original finite
quadrature error, every omitted theta index, and the infinite integration
tail. Subtracting the newly enclosed finite retained integral defines the
complete complement \(R=C-G\). The absorption factor is transported
directly as \(C-G/2\), preserving its cancellation. On the true stationary
set, its enclosure can be intersected with
\(-h_{j+2}-\mu h_j-G_j/2\); the analogous intersection is used for
\(R\). This uses the actual stationary constraint without redefining the
source filter.

Each product then multiplies the full physical jet by the retained,
complementary, or absorption integral. Consequently every inter-source
cross term is retained. No individual raw theta index is assigned the
vanishing vertical contour integral possessed by the complete even source.
The partial integral is defined directly on the shifted horizontal contour.

### Results of all 64 closed-cell tests

Both values of \(U\) give the same classifications. All development and
holdout cells agree. The inequalities below use normalized products
\(Z_j\widehat G_j\), \(Z_j\widehat R_j\), and
\(Z_j(\widehat R_j+\widehat G_j/2)\), each equal to the physical product
times \(e^{\pi x_c/4}\).

| Filter | Stationary branch | Favorable retained product | Complement product | Absorption product |
|---|---|---:|---:|---:|
| \(N=1\), either \(U\) | \(h_1=0\) | positive | negative | less than \(-1{,}200{,}000\) |
| \(N=1\), either \(U\) | \(h_2=0\) | positive | negative | less than \(-250{,}000\) |
| \(N=2\), either \(U\) | \(h_1=0\) | greater than \(7800\) | between \(-212\) and \(-120\) | greater than \(3800\) |
| \(N=2\), either \(U\) | \(h_2=0\) | greater than \(3800\) | between \(-46\) and \(-25\) | greater than \(1900\) |

Thus the two-index source filters provide the requested proper-split
example on **both** stationary sets: a genuinely adverse complementary
product is paid by a prescribed half of the favorable retained product.
The loss is fixed at zero; it is never defined through division by an
energy floor. The one-index filters decisively fail the specified absorption
condition, even though their retained products are favorable. Their
negative upper bounds show an actual failure on nonempty stationary sets,
rather than insufficient interval precision.

The enormous one-index retained and complementary terms nearly cancel;
adding the second index changes the balance decisively. This observation
is consistent with raw-index contour boundary effects, but a structural
explanation requires the separate analytic boundary calculation. This
pilot does not by itself identify a uniform all-height source relation.

The [driver](../numerics/certify_predetermined_source_filter_pilot.py) and
[compact receipt](../numerics/PREDETERMINED_SOURCE_FILTER_PILOT_20261014.json)
preserve all 64 cases, including failures. These are tests inside previously
certified branches, not an extension of their height coverage.

## 3. Why fixed sharp filters cannot supply the desired global closure

### 3.1. A proper filter in original contour coordinates

Fix t in (0,1/2], 0<a<pi/8, b>=0, an integer N>=1, and U>0. None of these
parameters depends on x. Set z=u+ia, q=iz=-a+iu, and

\[
 \Phi_N(z)=\sum_{n=1}^N\phi_n(z),\quad
 f_{N,j}(u)=(u^2-b^2)q^j e^{tz^2}\Phi_N(z),\quad j=0,1.
\]

The prescribed retained residual is

\[
 G_j(t,x)=e^{-ax}\Re\int_0^U f_{N,j}(u)e^{ixu}\,du,
 \qquad R_j=C_j-G_j. \tag{O1}
\]

In the exact shared-carrier domain this is the filter
n<=N, d_n<=v<=d_n+U. Thus every index has its own entry v=d_n and upper
endpoint v=d_n+U; it is a proper source filter, not a replacement of the
staircase by an unrelated polynomial.

For frozen t,a,b,N,U this definition is exact. The filtered physical field
itself still obeys the heat equation: differentiation in t multiplies the
integrand by z², while two physical x derivatives multiply it by (iz)².
There is no heat-equation defect caused merely by freezing a proper filter.
The boundary phenomenon below arises from integration by parts in u.

### 3.2. Exact endpoint identity and a complete remainder

For x>0, two integrations by parts give

\[
 \boxed{e^{ax}G_j(x)=\frac{B_j(x)}x+\mathcal E_j(x),\qquad
 B_j(x)=\Im\{f_{N,j}(U)e^{ixU}-f_{N,j}(0)\},} \tag{O2}
\]

with the explicit complete bound

\[
 |\mathcal E_j(x)|\le\frac{M_{N,j}}{x^2},\qquad
 M_{N,j}=|f'_{N,j}(U)|+|f'_{N,j}(0)|+
              \int_0^U|f''_{N,j}(u)|\,du. \tag{O3}
\]

The derivative and integral in M are finite for the fixed parameters.
To check signs, write I=[fe^(ixu)]/(ix)-[f'e^(ixu)]/(ix)²
+(1/(ix)²) integral f''e^(ixu); Re(-iZ)=Im Z.
Both the artificial upper boundary and the lower raw-index boundary are
present. In particular,

\[
 -\Im f_{N,j}(0)
 =b^2(-a)^j e^{-ta^2}\Im\Phi_N(ia). \tag{O4}
\]

For the complete theta source Phi(ia) is real, so this lower coefficient
vanishes. More generally the complete centered integrand has
f_j(-u)=overline(f_j(u)). Hence f_j^(r)(0) is real for even r and purely
imaginary for odd r, and the real part of every lower-endpoint integration-
by-parts coefficient vanishes. This exact cancellation need not hold for a
finite raw-index sum.

If common-coordinate truncation v<=V is preferred, the same calculation
has upper frequencies U_n=V-d_n>0 and

\[
 B_j(x)=\Im\left\{\sum_{n\le N,\ d_n<V}
 f_{n,j}(U_n)e^{ixU_n}-\sum_{n\le N,\ d_n<V}f_{n,j}(0)\right\}.
 \tag{O5}
\]

The error is the sum of the corresponding complete bounds (O3). The entry
phases remain exactly those in Note 19 B15: after multiplying by the
carrier they have no x phase. An index with d_n=V has an empty integration
interval and contributes zero; it must not be counted as a lone endpoint.

### 3.3. A nonvanishing endpoint condition covering the pilot family

Assume f_{N,0}(U) is nonzero. Then both B_0 and B_1 are nonconstant real
trigonometric polynomials: q(U) is nonzero because a>0. In the original-u
filter each B_j is a single sinusoid plus a constant. Consequently there
are infinitely many intervals of a fixed positive width, tending to
infinity, on which |B_j|>=c_j>0 and its sign is fixed. Constants can be
chosen separately for j=0 and j=1.

This endpoint condition is automatic for

\[
 a=\pi/16,\quad U\ge1,\quad U\ne b,\quad N\ge1. \tag{O6}
\]

Here is a quantitative source proof. Put E4=e^(4U) and
beta=pi cos(4a)E4. Since E4>50 and cos(pi/4)>2/3, beta>100.
For n>=2,

\[
 \left|\frac{\phi_n(U+ia)}{\phi_1(U+ia)}\right|
 \le n^2\frac{2\pi n^2E4+3}{2\pi E4-3}
       e^{-\beta(n^2-1)}
 \le2n^4e^{-100(n^2-1)}.
\]

The denominator is nonzero. For n>=2, n^4<=exp(n²-1), and
n²-1>=3+5(n-2). Therefore the full remaining-index ratio is bounded by

\[
 \sum_{n=2}^\infty2n^4e^{-100(n^2-1)}
 \le\frac{2e^{-297}}{1-e^{-495}}<\tfrac12.
\]

Thus Phi_N(U+ia) cannot vanish for any finite N. Also phi_1(U+ia) is
nonzero: its factor 2pi exp(4(U+ia))-3 has modulus lower bound
2pi exp(4U)-3>0. The remaining endpoint factors in f are nonzero under
(O6). This includes U=1 and U=3/2 with the small fixed b=1/4 used in the
rectangular pilot above. It is a proof from the theta terms, not a numerical genericity
assumption.

For (O5), the distinct U_n are independent frequencies in the trigonometric
polynomial. The n=1 coefficient is nonzero whenever V>0 and V!=b, because
phi_1(V+ia) is nonzero. Hence that common-V endpoint polynomial is also
nonzero. Its positive limiting mean square and bounded derivative give the
same fixed-width sign intervals; strict periodicity is unnecessary there.

### 3.4. Genuine stationary points expose the artificial adverse terms

**Proposition.** Fix the parameters in (O1), suppose f_{N,0}(U)!=0, and use
the actual theta family at the fixed positive time t. For each j=0,1 there
are sequences of genuine stationary points x_k tending to infinity,
h_{j+1}(t,x_k)=0, on which

\[
 h_jR_j<0,\qquad
 \frac{-h_jR_j}{E}
   =\exp\{(\pi/8-a)x_k+o(x_k)\}. \tag{O7}
\]

There are also sequences on the same respective stationary set with
h_jR_j>0 and the same exponential size of the absolute ratio. All these
points lie eventually in Note 19's already proved outer region, where
E>0 and both complete Laguerre forms are positive. The ratios are diagnostic
quantities on a proved nonvanishing region, not definitions of a loss.

**Proof.** At fixed t>0, Note 19 applies for all sufficiently large x. Write
A(x)=2|Q_t(x)|>0, omega=log(x/(4pi))/4, and phi=arg Q. The established
carrier estimates give

\[
 h_k=A\omega^k\{\cos(\phi+k\pi/2)+O(1/\log x)\},\quad k=0,1,2,3,
\]

\[
 \phi'(x)=\omega+O(1)>0,\qquad
 \log A(x)=-\pi x/8+O_t((\log x)^2). \tag{O8}
\]

For j=0 consider phase windows centered at phi=kpi, of fixed half-width
pi/6. The h1 endpoint signs differ, and h2 has a fixed nonzero sign
throughout each window for sufficiently large x. Thus each window contains
exactly one h1=0 point, and h0 alternates sign as k increments. At those
points |h0|~A and E=h0²~A².

For j=1 center the phase windows at phi=pi/2+kpi. The h2 endpoint signs
differ, and h3 has a fixed nonzero sign throughout each window. Thus each
contains exactly one h2=0 point, and h1 alternates sign. At these points
|h1|~A omega, h0=O(A/log x), and E~A² omega².

The distance between these consecutive phase windows tends to zero,
since phi'~log x/4. Every fixed-width sign interval for B_j at sufficiently
large x therefore contains stationary points of both h_j signs. Equations
(O2)–(O3) show that G_j has the sign of B_j there and magnitude comparable
to e^(-ax)/x. Meanwhile C_j is a fixed linear combination of the complete
h_j,h_{j+1},h_{j+2}, so by (O8) it is exponentially smaller than G_j on
these intervals. Hence R_j=C_j-G_j has the opposite sign to B_j and
|R_j|~e^(-ax)/x. Choose either of the two alternating signs of h_j.
The respective energy estimates yield (O7); the powers of x and log x
and the O_t(log² x) carrier correction are o(x) in its logarithm.

**Scope of obstruction.** No uniform constant, polynomial in x, or other
budget beta_j(x)=exp(o(x)) can make
h_jR_j>=-beta_j(x)E hold on the entire high-height stationary set for this
fixed sharp filter. The same is true for h_jG_j, whose large sign is
opposite to that of R_j on the selected sequences. Their sum h_jC_j has
no such artificial endpoint: cancellation is exact.

The conclusion directly obstructs the proposed fixed-fraction absorption test.
Choose the subsequence where h_jG_j>0. For any fixed 0<=lambda<1,

\[
 h_j(R_j+\lambda G_j)=h_jC_j-(1-\lambda)h_jG_j<0,
 \qquad
 \frac{-h_j(R_j+\lambda G_j)}{E}
 =\exp\{(\pi/8-a)x_k+o(x_k)\}. \tag{O7a}
\]

Thus the globally uniform test h_j(R_j+lambda G_j)>=-K_j E cannot hold
with K_j=exp(o(x)) for this fixed sharp filter, even though its favorable
retained condition h_jG_j>=0 holds on the chosen subsequence. The excluded
case lambda=1 is the exact combined product h_jC_j and has no artificial
boundary loss. A lambda(x) tending to one exponentially fast is also outside
the fixed-fraction claim.

This does not exclude locally bounded beta_j at every finite positive-time
point: exponential growth in x is still locally bounded. It also does not
prove an obstruction for a filter whose N,U,a or shape varies with x, or
for t tending to zero inside the unresolved cusp. It shows that a fixed
sharp filter is an unsuitable basis for uniformly small *separate* product
payments, even where the complete target is already favorable.

### 3.5. No rational-coefficient finite-jet closure for a compact source filter

A second exact result rules out a simple proposed identity for R, without
referring to arbitrary jet values.

**Proposition.** Fix t,a,b,N,U as in (O1), with U>0, N>=1. There are no finite
m and real rational functions r_0(x),...,r_m(x) such that

\[
 R_j(x)=\sum_{k=0}^m r_k(x)h_k(t,x) \tag{O9}
\]

on any nonempty open real interval on which the coefficients have no pole.
This includes constant- and polynomial-coefficient identities of the type
R=A h0+B h1+D h_{j+1}. It does not cover general transcendental or merely
locally bounded coefficients, or parameter-dependent moving filters.

**Proof.** Since C_j is itself a constant-coefficient combination of theta
jets, (O9) would express G_j as a rational-coefficient finite combination
of these jets. Clear denominators to obtain

\[
 p(x)G_j(x)=\sum_{k=0}^m p_k(x)h_k(t,x),\quad p\ne0, \tag{O10}
\]

with polynomials. Each side extends to an entire function of x, so the
identity on the interval extends to all real x.

Multiply by exp(ax). Complete theta evenness and reality give the exact
whole-line representation

\[
 e^{ax}h_k(t,x)=\frac12\int_{\mathbb R}
 e^{t(u+ia)^2}\Phi(u+ia)[i(u+ia)]^k e^{ixu}\,du. \tag{O11}
\]

The Fourier density in (O11) is real-analytic in u on the whole real line
and all of its derivatives rapidly decay. Holomorphy follows from the
open theta strip; negative-u decay follows from the complete evenness.
Multiplication by a polynomial in x corresponds to a finite combination
of u derivatives, preserving that real analyticity.

In contrast, e^(ax)G_j is the Fourier transform of the compactly supported
L1 density which equals f_{N,j}(u)/2 for 0<u<U, equals
conjugate(f_{N,j}(-u))/2 for -U<u<0, and vanishes elsewhere. After
multiplication by p(x), its Fourier preimage is a compactly supported
distribution. Fourier injectivity for tempered distributions now makes
(O10) equate this compact distribution to a real-analytic function.
That analytic function vanishes on (U,infinity), hence vanishes everywhere.
Thus p(x)G_j(x)=0 and G_j is identically zero.

This is impossible: f_{N,j} is not identically zero on (0,U). The finite
Phi_N is a nonzero holomorphic function (on the positive real axis every
phi_n is positive), and its other factors have only isolated zeros.
Fourier injectivity therefore gives G_j not identically zero. This proves
the proposition. The only Fourier uniqueness fact used can also be obtained
by Gaussian regularization and the approximate-identity limit; it does not
assume anything about zeros of H.

### 3.6. What a repair has to preserve

The obstruction recommends treating the artificial endpoint contributions
as one combined object before any signed estimate. In C=G+R the large
endpoint term occurs with exactly opposite signs. Paying them separately
by absolute values can cost exp((pi/8-a)x) relative to the physical energy.
A boundary-matched or x-dependent filter may be worth testing, but its
uniform bounds and any moving-boundary derivatives must be included.

An explicit vertical contour correction alone restores an unshifted raw-
index cosine integral; it does not restore complete theta evenness at u=0.
Naively replacing Phi_N(z) by Phi_N(z)+Phi_N(-z) is not a valid positive-time
repair: as real u tends to infinity,

\[
 \Phi_N(-u)=-3\pi\Big(\sum_{n=1}^Nn^2\Big)e^{-5u}+O_N(e^{-9u}),
\]

so multiplying it by exp(tu²) destroys integrability at every fixed t>0.
The evenness needed in the full source is an infinite-index identity.
Smooth compact cutoffs remove the leading sharp-boundary terms only if
the necessary endpoint derivatives match; their success still needs a
new relative or signed estimate and does not follow from smoothness alone.

These are source-specific analytic guardrails. A certified finite proper-
filter pilot remains useful for measuring actual signed cancellation, but
its favorable finite result should not be extrapolated into a globally
uniform separate-block payment. The primary target remains the combined
stationary observation, with source correlations retained.


## 4. A complete-source Gaussian filter and its certified time comparison

Before testing, fix

\[
 \delta=1/16,\quad\lambda=1/2,\quad a=\pi/16,\quad b=1/4,
 \quad\mu=a^2+b^2,\quad K_0=K_1=0.
\]

The complete-source multiplier \(q_\delta(z)=e^{-\delta z^2}\) gives the
exact identity \(e^{tz^2}q_\delta(z)=e^{(t-\delta)z^2}\). It therefore
produces the prescribed split

\[
 G_j(t,x)=C_j(t-\delta,x),\qquad
 R_j(t,x)=C_j(t,x)-C_j(t-\delta,x).
\]

The centering parameters remain fixed at both times. This is a noncompact
source filter; its values on the imaginary segment are real, and multiplying
the complete theta source preserves the symmetry needed for the contour
identity. The finite raw-index endpoint effects of a rectangular source
cutoff are consequently absent from this definition.

On the shifted horizontal contour this is the **complex** multiplier
\(q_\delta(u+ia)=e^{\delta a^2-\delta u^2}e^{-2i\delta au}\).
Replacing it by the real weight \(e^{-\delta u^2}\) would lose the
exact time-shift identity. It is consequently a different class from the
real rectangular multipliers in the compact-filter pilot; a formula
requiring a real multiplier cannot be applied to it unchanged. The proof
here uses the exact full-source time identity directly.

The 14 predeclared cases are both genuine current-time stationary branches
and all seven time slabs \([k/16,(k+1)/16]\), \(1\le k\le7\):
\(h_1=0\) in \((101,102)\), and \(h_2=0\) in \((103,104)\).
The existing paid endpoint transport and derivative signs certify exactly
one point on each branch at every time. No condition of stationarity at
the earlier time \(t-\delta\) is assumed.

For every one of these 14 cases, the exact interval computation proves

\[
 h_jG_j>0,\qquad h_jR_j>0,
 \qquad h_j(R_j+\tfrac12G_j)>0.
\]

Thus both retained and complementary products are favorable in this pilot.
The fixed \(K_j=0\) signed estimate follows without dividing by energy or
fitting a loss. Conservative normalized margins across all seven slabs
are:

| Current branch | \(Z_j\widehat G_j\) | \(Z_j\widehat R_j\) | \(Z_j(\widehat R_j+\widehat G_j/2)\) |
|---|---:|---:|---:|
| \(h_1=0\), \(101<x<102\) | greater than \(8300\) | greater than \(54\) | greater than \(4200\) |
| \(h_2=0\), \(103<x<104\) | greater than \(4200\) | greater than \(7\) | greater than \(2100\) |

Here \(Z_k=e^{\pi x_c/8}h_k\) with \(x_c=101.5\) or \(103.5\), and
all residuals use the same positive constant normalization in a branch.
The source record's even-index slabs are development and odd-index slabs
holdout, with the same fixed parameters evaluated on every one.

The proof uses no new quadrature. The original full-source quadrature
certificate and its analytic contour and tail lemmas remain trusted inputs;
this extraction does not revalidate those analytic inputs. The previous time slab has exactly the
same spatial center and is shifted by \(\delta\), so its stored Taylor
polynomial represents \(G\) with the same time displacement as the current
polynomial represents \(C\). Center coefficient differences are formed
before transport. The complete remainder payments are respectively
\(P_{\rm prior}\) for \(G\), \(P_{\rm current}+P_{\rm prior}\) for
\(R\), and \(P_{\rm current}+P_{\rm prior}/2\) for the absorption factor.
Both spatial and temporal payments are included. Each full center array
already contains the complete index and integration tails. On current
stationarity, the transported enclosure is additionally intersected with
\(C_j=-h_{j+2}-\mu h_j\). Multiplying the integrated observations retains
all cross terms.

The [standard-library driver](../numerics/check_gaussian_source_filter_pilot.py)
and [compact receipt](../numerics/GAUSSIAN_SOURCE_FILTER_PILOT_20261014.json)
record all 14 cases. The proof is a finite comparison for
\(1/16\le t\le1/2\); it does not show that a fixed delay is suitable
as \(t\downarrow0\), or that the correlation persists near an unknown
current-time collision.

## 5. A distinct real Gaussian mask: exact time and position transport



There is a constructive alternative that preserves the complete lower-endpoint
symmetry. The following is a standard Fourier/heat identity specialized to
the complete theta source; it carries no novelty claim. Fix delta>=0 and
take the real full-source multiplier

\[
 m_\delta(u)=(u^2-b^2)e^{-\delta u^2},
\]

with no raw-index or sharp integration truncation in its definition. This
is a proper frequency filter for delta>0, but not a compact source filter.
All numerical truncations of its defining complete integral still require
paid errors. Denote its retained residual by G_{delta,j}. Then, exactly,

\[
 \boxed{G_{\delta,j}(t,x)
 =e^{a^2\delta}C_j(t-\delta,x+2a\delta),\qquad
 R_{\delta,j}=C_j(t,x)-e^{a^2\delta}C_j(t-\delta,x+2a\delta).}
 \tag{O12}
\]

Here a,b remain frozen and the C on the right uses those same parameters.
The identity holds for all real t for which the theta family is defined
(the complete theta integral converges for every real t). Restricting to
0<=delta<=t is needed only when invoking a result proved at nonnegative
time.

To prove (O12), first apply the Gaussian multiplier to the physical jet.
Writing z=u+ia gives

\[
 tz^2-\delta u^2=(t-\delta)z^2+2i\delta a u-\delta a^2.
\]

The complete contour identity therefore yields

\[
 e^{-ax}\Re\int_0^\infty e^{tz^2-\delta u^2}
 \Phi(z)(iz)^j e^{ixu}du
 =e^{a^2\delta}h_j(t-\delta,x+2a\delta). \tag{O13}
\]

Applying the fixed polynomial -partial_x²-2a partial_x-mu gives (O12).
Equivalently this is the forward heat operator conjugated by exp(ax):
e^(-ax) exp(delta partial_x²) exp(ax), evaluated on the backward-heat
solution. This derivation uses the complete source, not an independently
shifted raw theta index. The Gaussian in u is even and real; it preserves
f(-u)=conjugate(f(u)) and all the lower-endpoint cancellations in Section 3.2.

For example, differentiation in the filter parameter gives an exact
remainder representation with every term retained:

\[
 R_{\delta,j}=-\int_0^\delta e^{a^2s}
 [C_{j+2}+2aC_{j+1}+a^2C_j](t-s,x+2as)\,ds. \tag{O14}
\]

This identity trades a sharp-filter endpoint problem for a specific
correlation between complete theta observations at two times and positions.
It does not prove a sign. The shifted point need not lie on the original
stationary branch, so the genuine constraint h_{j+1}(t,x)=0 cannot be
silently imposed at (t-s,x+2as). A signed estimate for the cross-time
product in (O12) or (O14), with prescribed parameters and full physical
stationarity retained, is the remaining analytic obligation. It may be
substantively more suitable than separately paying artificial endpoints.


For clarity, a different complete-source filter uses exp(-delta z²), with
z=u+ia. That multiplier is generally complex on the shifted contour, and
its retained residual is simply C_j(t-delta,x), with no spatial shift or
scalar factor. This is the separate mask used in the certified
Gaussian pilot in Section 4. The real-multiplier paired formula F6 cannot be applied
unchanged to that complex mask; the physical-field identity or a correctly
conjugated polarization supplies its products. The real exp(-delta u²)
filter in (O12) does satisfy F6's real-multiplier hypothesis. No numerical
certificate for this additional real-mask variant is asserted here.

## 6. The remaining analytic objective and validation

The complex Gaussian mask used in Section 4 gives a specific complete-source
correlation target, with no artificial finite-index or upper integration
endpoint:
\[
 \begin{aligned}
 P_j^\delta(t,x)&=h_j(t,x)C_j(t-\delta,x),\\
 Q_j^\delta(t,x)&=h_j(t,x)
       [C_j(t,x)-(1-\lambda)C_j(t-\delta,x)].
 \end{aligned}                                                     \tag{S3}
\]
Proving \(P_j^\delta\ge0\) and \(Q_j^\delta\ge-K_jE\) on both
current stationary sets, for a prescribed delay rule and locally bounded
losses, would supply (S1). The finite pilot proves these inequalities only
on its declared cells. With fixed centering, the complete heat identity also
provides the exact complementary representation
\[
 R_j(t,x)=-\int_0^\delta C_{j+2}(t-s,x)\,ds.                        \tag{S4}
\]
This follows by differentiating \(C_j(t-s,x)\) in \(s\), using
\(\partial_tC_j=-C_{j+2}\). It exposes the particular cross-time product
that needs a theta-specific estimate. The earlier-time point is generally
not stationary. Neither the heat identity nor source symmetry proves its
sign. A delay that varies with \(t,x\) also requires its own derivative
terms in any differential transport argument; pointwise filter identities
must not be differentiated as if the parameters were fixed.

The compact-filter obstructions exclude specific approaches, not the
original locally bounded-loss program. In particular, exponential growth
of a loss as \(x\to\infty\) is compatible with local boundedness at each
finite point. The demonstrated exponential obstruction is at fixed
positive time in an already favorable outer region, not a new theorem
about the unresolved moving small-time cusp. Likewise the rational-jet
closure theorem does not exclude general transcendental coefficients or
a different noncompact/moving source rule.

The [independent internal review](../reviews/16_SOURCE_FILTERS_AND_THETA_CORRELATIONS_REVIEW_20261014.md)
audits the analytic proofs and replays both pilots. It is internal LLM
review, not external peer review or formal verification. New rectangular
quadratures use python-flint 0.9.0 at 192-bit precision. The Gaussian
extraction uses exact rational arithmetic. Both inherit the original
[full-source certificate](../numerics/THETA_CENTERED_RESIDUAL_100_104_20261014.json)
and its analytic contour and tail bounds. Replays match all mathematical
fields; the rectangular runtime field is excluded from identity comparison.

From this investigation's `numerics/` directory, with python-flint available
to the interpreter used for the first command:

```sh
python3 certify_predetermined_source_filter_pilot.py \
  --record THETA_CENTERED_RESIDUAL_100_104_20261014.json \
  --original-driver certify_phase_centered_residual.py \
  --contour-source check_shifted_contour_payments.py \
  --output /tmp/inv21-proper-filter-replay.json
python3 check_gaussian_source_filter_pilot.py \
  --record THETA_CENTERED_RESIDUAL_100_104_20261014.json \
  --original-driver certify_phase_centered_residual.py \
  --contour-source check_shifted_contour_payments.py \
  --output /tmp/inv21-gaussian-filter-replay.json
```

No manuscript revision, new snapshot, commit, or tag is part of this step.
