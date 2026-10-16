# Oscillation-preserving product Poisson transformation

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model family: GPT-6 (Codex); the exact serving variant and configured
reasoning effort are not exposed and are not inferred. This is an internal
analytical derivation, not independent mathematical validation. No numerical
sweeps are used.

This continues the [centered arithmetic reduction](2_CENTERED_COLLISION_JETS_AND_RATIO_PRODUCT_CORRELATIONS_20261010.md),
the [complete dual kernels](3_PAID_DUAL_KERNELS_AND_ACTUAL_FREQUENCY_RELAXATION_LOSS_20261010.md),
and [common-factor smoothing](6_ANALYTIC_COMMON_FACTOR_SMOOTHING_AND_PRIMITIVE_SIGNED_FRONTIER_20261010.md).
It complements the [diagonal-annihilating kernel](7_DIAGONAL_ANNIHILATING_PAID_KERNELS_AND_NEAR_PAIR_BOUNDS_20261010.md)
and [coupled primitive frontier](9_COUPLED_MOBIUS_PRIMITIVE_FRONTIER_AND_RESONANT_SUBLATTICES_20261010.md).
The [central continuation](../../notes/22_SIGNED_PAIR_TRANSFORMS_AND_STATIONARY_REFLECTION_20261010.md)
proves the exact physical stationary-reflection mismatches used at the end.
Unlike the absolute Euler–Maclaurin derivative envelope of Note 6, the present transformation
retains the large product oscillation throughout. A finite Poisson formula,
an exact quadratic phase coordinate, and two integrations by parts on
uniformly nonstationary modes give finite incomplete-Fresnel expressions
with a globally vanishing remainder. Every cutoff floor, block/complement
term, product sine term, and actual carrier remains in the formula. The
transformed signed sum still needs an arithmetic estimate; no opposite
threshold sign, collision exclusion, or RH conclusion is proved.

## 1. Complete product channel and literal intervals

Use the complete physical center of Note 6:
\[
1\le\kappa\le3/2,\quad L=\kappa/t,\quad0<t\le1/20,
\quad x=4\pi e^L,\quad
N=\lfloor\sqrt{e^L+t/16}\rfloor,
\]
\[
w(v)=v^{-\sigma}e^{t\log^2v/4},\quad
\rho_v=\log v-\mu,\quad\mu=\Omega/c,
\quad\phi_n=\theta_t+T\log n,\quad
T=(x-t\alpha_i)/2>0,\quad\epsilon=d/c.
\]
The exact physical frequency satisfies \(T\asymp N^2\) uniformly
as time tends to zero on the closed \(\kappa\) interval. In this note
all physical quantities, the dual parameters, and the cutoff are frozen.
Auxiliary-index derivatives below are not raw spatial derivatives.

For the dual matrix of Notes 3 and 6, write
\[
R=r(\rho_n)^T\mathbb Qr(\rho_m),\quad
S=s(\rho_n)^T\mathbb Qs(\rho_m),\quad
C_{nm}=r(\rho_n)^T\mathbb Qs(\rho_m),
\]
\[
P_c(n,m)=(R-S)/2,\qquad
P_s(n,m)=(C_{nm}+C_{mn})/2.
\tag{1}
\]
The features are exactly
\(r(v)=(1,\epsilon v,v^2,0,v^4)^T\) and
\(s(v)=(0,v,0,v^3,0)^T\). Retain the actual \(\epsilon\).
Both product polynomials have total degree at most six. Define the complex
amplitude
\[
A_{a,b}(u)=w(ua)w(ub)
              \{P_c(ua,ub)-iP_s(ua,ub)\}.
\tag{2}
\]
The product kernel's real part then has the correct sine sign:
\(\Re[(P_c-iP_s)e^{i\Phi}]=P_c\cos\Phi+P_s\sin\Phi\).
Unique common-factor decomposition gives exactly
\[
\mathcal P_{\Lambda,B}
=\Re\left[e^{2i\theta_t}
 \sum_{(a,b)=1\atop\max(a,b)\le N}e^{iT\log(ab)}
 \sum_{j=1}^{\lfloor N/\max(a,b)\rfloor}
                    A_{a,b}(j)e^{2iT\log j}\right].
\tag{3}
\]

The proof below uses only the degree-six polynomial envelope, not the
particular feature-matrix representation in (1). Consequently it also
applies to Note 7's extended diagonal-annihilating product kernel, provided
\(\mathfrak M\) bounds its polynomial coefficients and their fixed
physical drift factors. Its additional finite moments do not require a
new heat approximation or raw derivative estimate.

The inner interval is partitioned into the four literal integer masks of
Note 6. Explicitly put \(K_N=\lfloor N/2\rfloor\),
\(k_a=\lfloor K_N/a\rfloor\), \(k_b=\lfloor K_N/b\rfloor\),
and \(J=\lfloor N/\max(a,b)\rfloor\). Their endpoints are
\[
\begin{array}{c|cc}
\text{class}&\ell&v\\\hline
\mathcal C\times\mathcal C&1&\min(J,k_a,k_b)\\
\mathcal B\times\mathcal B&\max(1,k_a+1,k_b+1)&J\\
\mathcal B\times\mathcal C&\max(1,k_a+1)&\min(J,k_b)\\
\mathcal C\times\mathcal B&\max(1,k_b+1)&\min(J,k_a).
\end{array}
\tag{4}
\]
Discard an empty interval, not any pair contribution. Intersect each
nonempty interval with the disjoint integer dyadic cells
\([U,2U-1]\), \(U=2^h\), \(h\ge0\). Write its resulting endpoints
as \([p,q]\); then
\[
U\le p\le q<2U,\qquad qa,qb\le N.
\tag{5}
\]
All terms belong to exactly one interval and one dyadic cell. No floor is
approximated and no shared integer is counted twice. A singleton is kept
exactly. Everything below applies to a nonsingleton \(p<q\).

## 2. A generic exact finite Poisson formula

For a positive oscillation parameter \(\tau\), distinct from the heat
time \(t\), consider
\[
\Sigma[A;p,q]=\sum_{j=p}^q A(j)e^{2i\tau\log j},\qquad
I_k=\int_p^q A(u)e^{i\psi_k(u)}\,du,
\quad\psi_k(u)=2\tau\log u-2\pi ku.
\tag{6}
\]
For a smooth amplitude, the exact finite Poisson identity is
\[
\Sigma[A;p,q]
=\tfrac12\{A(p)e^{2i\tau\log p}+A(q)e^{2i\tau\log q}\}
        +\lim_{M\to\infty}\sum_{|k|\le M}I_k.
\tag{7}
\]

A direct proof avoids a black-box transformation theorem. On
\(0<v<1\), periodize the finitely many unit intervals:
\[
G(v)=\sum_{j=p}^{q-1}A(j+v)e^{2i\tau\log(j+v)}.
\]
Its \(k\)-th Fourier coefficient is \(I_k\), because the integers
in the Fourier phase disappear. Its one-sided values at zero have average
\(\sum_{p<j<q}A(j)e^{2i\tau\log j}
+\tfrac12\{A(p)e^{2i\tau\log p}+A(q)e^{2i\tau\log q}\}\).
The Fourier series of this piecewise smooth periodic function converges
to that average, giving (7). This is the elementary Fourier convergence
input recorded in [NIST DLMF §1.8](https://dlmf.nist.gov/1.8).

In (3), take \(\tau=T\). In the original-index alternative in
Section 8, take \(\tau=T/2\). Thus both use the same physical
frequency and keep its oscillation.

## 3. A finite stationary band and uniform excluded-mode bounds

For a dyadic interval (5), define the literal integer stationary band
\[
\mathcal K_{p,q}(\tau)
=\left\{k\in\mathbb Z_{>0}:
\frac{\tau}{2\pi q}\le k\le\frac{2\tau}{\pi p}\right\}.
\tag{8}
\]
It contains every stationary point of (6) on \([p,q]\), including
endpoint coincidences. For \(k\in\mathcal K\), set
\[
u_k=\tau/(\pi k)\in[p/2,2q],\qquad
\psi_k(u_k)=2\tau\log u_k-2\tau,
\quad\psi_k''(u_k)=-2\tau/u_k^2<0.
\tag{9}
\]

Let \(V_k(u)=\psi_k'(u)=2\tau/u-2\pi k\). Outside the band,
\(V_k\) never vanishes. If \(k\le0\), its magnitude is at least
\(2\tau/q+2\pi|k|\). If \(0<k<\tau/(2\pi q)\), it is at
least \(\tau/q\). If \(k>2\tau/(\pi p)\), its magnitude is at
least \(\pi k\). Consequently, for \(\tau\ge U\),
\[
\sum_{k\notin\mathcal K}|V_k(u)|^{-2}\le C U/\tau,
\quad
\sup_{k\notin\mathcal K}|V_k(u)|^{-1}\le C U/\tau,
\quad p\le u\le q.
\tag{10}
\]
To see the summed bound, the low positive range has \(O(\tau/U)\)
terms of size \(O((U/\tau)^2)\); the nonpositive and high positive
ranges are bounded by the convergent integral of
\((\tau/U+v)^{-2}\). These elementary bounds are independent of
how close an included stationary point is to an endpoint.

## 4. Exact excluded-mode endpoint functions and a paid remainder

Define \(\mathcal L_kA=(A/V_k)'\). Two integrations by parts give
exactly
\[
I_k=\left[e^{i\psi_k(u)}
 \left\{\frac{A(u)}{iV_k(u)}
               +\frac{\mathcal L_kA(u)}{V_k(u)}\right\}
 \right]_p^q
       -\int_p^q e^{i\psi_k(u)}\mathcal L_k^2A(u)\,du,
\tag{11}
\]
\[
\mathcal L_k^2A
 =\frac{A''}{V_k^2}-\frac{3A'V_k'}{V_k^3}
       -\frac{AV_k''}{V_k^3}
                 +\frac{3A(V_k')^2}{V_k^4}.
\tag{12}
\]
At integer endpoints, \(e^{i\psi_k(u)}=e^{2i\tau\log u}\).
Hence the entire excluded-mode boundary contribution is an explicit
function, rather than a discarded absolute endpoint payment. Put
\[
S_m(u)=\sum_{k\notin\mathcal K}V_k(u)^{-m},\quad m=2,3,
\qquad
S_1(u)=\lim_{M\to\infty}
              \sum_{|k|\le M\atop k\notin\mathcal K}V_k(u)^{-1}.
\tag{13}
\]
The latter converges by pairing \(k,-k\) beyond the finite band; their
leading \(1/k\) terms cancel. The boundary expression is
\[
\mathsf B_{\rm out}[A;p,q]
=\left[e^{2i\tau\log u}
 \left\{\frac{A(u)}iS_1(u)+A'(u)S_2(u)
                       -A(u)V_k'(u)S_3(u)\right\}\right]_p^q,
\tag{14}
\]
where \(V_k'(u)=-2\tau/u^2\) is independent of \(k\).

For a finite special-function representation, put \(z=\tau/(\pi u)\)
and freeze the finite set \(\mathcal K\) in this formula. Then
\[
C_1(z)=\pi\cot(\pi z)-\sum_{k\in\mathcal K}\frac1{z-k},
\quad
C_2(z)=-C_1'(z),\quad C_3(z)=\tfrac12 C_1''(z),
\quad S_m=(2\pi)^{-m}C_m.
\tag{15}
\]
At an integer \(z\) occurring between the endpoint values, that integer
belongs to \(\mathcal K\); the singularities in (15) cancel and the
value is taken by its removable limit. Equivalently, one may use the
paired convergent series (13), which has no spurious poles. Formula (15)
is the classical cotangent partial-fraction identity, recorded in
[NIST DLMF §4.22](https://dlmf.nist.gov/4.22.E3).

Suppose on the physical interval an envelope \(W_U\) gives
\[
|A^{(h)}(u)|\le C_h\mathfrak M U^{-h}W_U,
\qquad h=0,1,2.
\tag{16}
\]
Since \(|V_k'|\le C\tau/U^2\) and
\(|V_k''|\le C\tau/U^3\), (10)–(12) imply
\[
\sum_{k\notin\mathcal K}|\mathcal L_k^2A(u)|
                         \le C\mathfrak M W_U/(U\tau).
\tag{17}
\]
For example the \(A''/V_k^2\) term has precisely that bound;
each extra inverse power of \(V_k\) is at most \(CU/\tau\),
which offsets the corresponding factor from \(V_k'\) or \(V_k''\).
The interval length is at most \(U\), so the complete excluded-mode
integral remainder has absolute value at most
\[
C\mathfrak M W_U/\tau.
\tag{18}
\]
This is where phase-aware integration by parts avoids the bad
\(T^{2r}\) absolute derivative factor of Note 6. No excluded-mode
endpoint term is dropped.

## 5. Exact quadratic coordinates and uniform incomplete Fresnel terms

For each retained \(k\), write \(u=u_kv\), and define
\[
\xi(v)=\operatorname{sgn}(v-1)
           \sqrt{2(v-1-\log v)},\qquad \xi(1)=0.
\tag{19}
\]
This function is smooth and strictly increasing on positive \(v\),
including at one; it has a smooth inverse \(v=V(\xi)\). On the
expanded band, all ratios required below lie in \([1/4,4]\). Exactly,
\[
\psi_k(u)=\psi_k(u_k)-\tau\xi^2,
\quad
g_k(\xi)=u_k A(u_kV(\xi))V'(\xi),
\]
\[
I_k=e^{i\psi_k(u_k)}
                  \int_{\xi(p/u_k)}^{\xi(q/u_k)}
                          g_k(\xi)e^{-i\tau\xi^2}\,d\xi.
\tag{20}
\]
The inverse satisfies \(V'(0)=1\), \(V''(0)=2/3\),
\(V'''(0)=1/6\). These follow by substituting
\(V(\xi)=1+\xi+\xi^2/3+\xi^3/36+O(\xi^4)\) into (19).
Thus
\[
g_k(0)=u_kA(u_k),\quad
g_k''(0)=u_k\{u_k^2A''(u_k)+2u_kA'(u_k)+A(u_k)/6\}.
\tag{21}
\]

For any smooth function on an interval containing zero and both
endpoints, define the regular quotient and its derivative
\[
\mathcal Bg(\xi)=\frac{g(\xi)-g(0)}\xi,
\quad\mathcal Bg(0)=g'(0),\qquad
\mathcal Dg=(\mathcal Bg)'.
\tag{22}
\]
Integration by parts uses the actual Gaussian oscillation:
\[
\int_a^b ge^{-i\tau\xi^2}\,d\xi
=g(0)\mathcal F_\tau(a,b)
 -\frac1{2i\tau}[\mathcal Bg(\xi)e^{-i\tau\xi^2}]_a^b
 +\frac1{2i\tau}\int_a^b\mathcal Dg(\xi)e^{-i\tau\xi^2}\,d\xi.
\tag{23}
\]
Applying this identity twice gives the retained finite expression
\[
\begin{split}
\mathsf F_k[A;p,q]=e^{i\psi_k(u_k)}\bigg\{&
\left(g_k(0)+\frac{g_k''(0)}{4i\tau}\right)
                 \mathcal F_\tau(a_k,b_k)\\
&-\frac{[\mathcal Bg_k(\xi)e^{-i\tau\xi^2}]_{a_k}^{b_k}}
                    {2i\tau}
-\frac{[\mathcal B\mathcal Dg_k(\xi)e^{-i\tau\xi^2}]_{a_k}^{b_k}}
                    {(2i\tau)^2}\bigg\},
\end{split}
\tag{24}
\]
\[
I_k-\mathsf F_k
=\frac{e^{i\psi_k(u_k)}}{(2i\tau)^2}
             \int_{a_k}^{b_k}\mathcal D^2g_k(\xi)
                                  e^{-i\tau\xi^2}\,d\xi,
\quad a_k=\xi(p/u_k),\quad b_k=\xi(q/u_k).
\tag{25}
\]
The incomplete Fresnel function is explicit:
\[
\mathcal F_\tau(a,b)=\int_a^b e^{-i\tau\xi^2}\,d\xi
=\frac{\sqrt\pi e^{-i\pi/4}}{2\sqrt\tau}
 \left[\operatorname{erf}(e^{i\pi/4}\sqrt\tau\,\xi)\right]_a^b.
\tag{26}
\]
All quotients in (24) have their regular limits at zero. Thus a stationary
point may coincide with an endpoint or cross it as the physical height
changes. No generic nonresonance hypothesis or full-Gaussian substitution
is used. The sign \(-\pi/4\) in (26) corresponds to the negative
second derivative in (9).

For completeness the remainder needs only four amplitude derivatives,
not an imported stationary-phase estimate. The elementary identity
\[
\mathcal Dg(\xi)=\int_0^1s\,g''(s\xi)\,ds,
\qquad
\mathcal D^2g(\xi)
=\int_0^1\int_0^1 s v^3 g^{(4)}(sv\xi)\,dv\,ds
\tag{27}
\]
gives \(|\mathcal D^2g|\le\|g^{(4)}\|_\infty/8\).
Suppose (16) holds through order four throughout \([U/2,4U]\)
with the same envelope, up to constants. The inverse in (19) has bounded
derivatives on the fixed ratio interval \([1/4,4]\), so
\[
\|g_k^{(4)}\|_\infty\le C\mathfrak M U W_U,
\qquad
|I_k-\mathsf F_k|\le C\mathfrak M U W_U/\tau^2.
\tag{28}
\]
There are at most \(C\tau/U\) retained modes when \(\tau\ge U\).
Their aggregate remainder is therefore \(C\mathfrak M W_U/\tau\),
the same order as (18). The extension to \([U/2,4U]\) is only a
mathematical real-index amplitude extension used in this exact coordinate;
it asserts no separate heat approximation beyond the physical cutoff.

## 6. Finite interval theorem

Combining (7), (14), and (24), define
\[
\begin{split}
\mathsf T_\tau[A;p,q]={}&
\tfrac12\{A(p)e^{2i\tau\log p}+A(q)e^{2i\tau\log q}\}
 +\mathsf B_{\rm out}[A;p,q]
 +\sum_{k\in\mathcal K_{p,q}(\tau)}\mathsf F_k[A;p,q].
\end{split}
\tag{29}
\]
Under the amplitude bounds through order four above,
\[
\boxed{
|\Sigma[A;p,q]-\mathsf T_\tau[A;p,q]|
                  \le C\mathfrak M W_U/\tau.}
\tag{30}
\]
This is a finite oscillation-preserving transformation with a uniform
remainder. The only infinite expressions in its explicit main term are
the classical cotangent/derivative functions (15) or their paired
absolutely convergent representation, and the standard entire function
in (26). All floor endpoints and endpoint-transition terms are retained.
For a singleton, define \(\mathsf T_\tau\) to be the exact one term.

## 7. Global common-factor product theorem

Retain the scale
\[
\mathfrak M=(1+|\epsilon|)^2
                  (1+|\Gamma|+\|\Lambda\|+\|B\|),
\]
where \(\Gamma\) may also be the density-strengthened
\(\Gamma_{\rm count}=\gamma_{\rm count}/c^2=O(L)\).
For any extended polynomial kernel, replace this particular matrix scale
by an explicit bound for all its degree-six-or-lower coefficients; the
proof and its linear dependence on \(\mathfrak M\) are unchanged.
Note 7's extended kernel with the density-strengthened normalizer has
\(\mathfrak M=O(L)\).
For (2), an admissible envelope in (16) is
\[
W_{a,b,U}=w(Ua)w(Ub)
 (1+|\rho_{Ua}|)^6(1+|\rho_{Ub}|)^6.
\tag{31}
\]
To verify it, logarithmic derivatives of the prescribed weight are
\(-\sigma+(t/2)\log v\), with next derivative \(t/2\) and then
zero. On \(v\le4N\), and even \(v\ge1/2\), these coefficients
are uniformly bounded on the stated sector for sufficiently small time.
The kernel has degree at most six with coefficients bounded by
\(C\mathfrak M\). Moving the real index by a factor in \([1/2,4]\)
changes its centered log by a bounded amount and its weight by a bounded
factor. Applying four derivatives gives exactly (16) with (31),
including the extension needed in (28).

Note 6's centered weighted-moment bound proves
\[
\sum_{a\le N/U}w(Ua)(1+|\rho_{Ua}|)^6
                                    \le C(N/U)w_N.
\tag{32}
\]
For each \((a,b)\) and dyadic \(U\), there are at most four
mask intervals, and each has the bound (30) with \(\tau=T\).
Drop coprimality only in the positive error envelope. Equations
(31)–(32) yield
\[
\sum_{a,b\le N/U}W_{a,b,U}
                                      \le C(Nw_N)^2/U^2.
\tag{33}
\]
Since \(\sum_{h\ge0}2^{-2h}=4/3\), summing (30) over every
coprime ratio, every dyadic interval and all four masks gives
\[
\boxed{
|\mathcal P_{\Lambda,B}
         -\widetilde{\mathcal P}_{\Lambda,B}^{\rm CF}|
                       \le C\mathfrak M(Nw_N)^2/T.}
\tag{34}
\]
Here the finite transformed product is obtained by replacing its literal
inner intervals in (3) with (29), keeping their actual
\(e^{iT\log(ab)}\) and \(e^{2i\theta_t}\) factors before taking
the real part. Unlike the earlier common-factor Euler–Maclaurin theorem,
this transforms the **entire** product channel, including \(j=1\).
Singleton contributions remain exact rather than small discarded terms.

Uniformly for sufficiently small positive time and
\(\kappa\in[1,3/2]\), \((Nw_N)^2\asymp N^{1-\kappa/4}\)
and \(T\asymp N^2\). Thus
\[
|R_{\rm product}^{\rm CF}|
=O(\mathfrak M N^{-1-\kappa/4}).
\tag{35}
\]
For bounded dual parameters with the strengthened normalizer,
\(\mathfrak M=O(L)\), giving
\(O(LN^{-1-\kappa/4})=o(N^{-\kappa/4})\). This is below the
available physical upper-budget scale, not below an asserted positive
lower bound for the measured physical error. The recomputed
\(\widehat\Delta_{\rm count}\), the one-sided candidate-null
payment, and all separate physical Bell residuals remain necessary.

## 8. Original-index version and the stationary reflection geometry

The same theorem may be applied directly to the original index \(n\),
holding \(m\) fixed, rather than to the common factor. Put
\[
A_m(u)=w(u)w_m\{P_c(u,m)-iP_s(u,m)\},\qquad \tau=T/2.
\tag{36}
\]
For each actual \(m\), the literal \(n\)-block and complement
intervals are \([1,K_N]\) and \([K_N+1,N]\), and the membership
of \(m\) retains its corresponding class. Partition them into disjoint
dyadic pieces exactly as above. Formula (29) uses phase \(T\log u\)
and stationary points
\[
n_k=P/k,\qquad P=T/(2\pi),
\quad\psi_k(n_k)=T\log(P/k)-T.
\tag{37}
\]
The near-mode expression still uses every incomplete Fresnel endpoint
transition and the same four-derivative proof. An envelope is
\[
W_{m,U}=w(U)w_m(1+|\rho_U|)^6(1+|\rho_m|)^6.
\]
The uniform pointwise weight bound
\(w(U)\le C U^{-s_\kappa}\),
\(s_\kappa=1/2+\kappa/8\), follows because
the exact physical formula gives
\(\Re\alpha-L/2=O(x^{-2})\), while the natural-cutoff floor gives
\(\log N=L/2+O(N^{-1})\). Therefore
\(\sigma-(t/4)\log N=s_\kappa+O(t/N)\). For \(U\le N\),
the possible adverse exponent error after multiplication by
\(\log U\) is \(O(t\log N/N)=O(N^{-1})\), uniformly.
It implies
\[
\sum_{U=2^h\le N}w(U)(1+|\rho_U|)^6\le C L^6.
\tag{38}
\]
Indeed \(|\rho_U|\le C L\) and the dyadic \(U^{-s_\kappa}\)
series is uniformly summable. The complete \(m\)-moment sum is
\(O(Nw_N)\) by (32) at \(U=1\). Therefore the full original-index
product transformation satisfies the stronger, though logarithmically
weighted, error bound
\[
\boxed{
|\mathcal P_{\Lambda,B}
    -\widetilde{\mathcal P}_{\Lambda,B}^{\rm orig}|
                \le C\mathfrak M L^6(Nw_N)/T.}
\tag{39}
\]
This also retains every ordered \((n,m)\) pair, both product channels,
and the genuine carrier and drift. For the density-strengthened matrix,
it is \(O(L^7N^{-1-s_\kappa})=o(N^{-\kappa/4})\).

The leading *full-Gaussian stationary component* of a single-index mode
would have amplitude
\[
w(P/k)\frac{\sqrt P}{k}
=C_{\rm sd}\,k^{-\sigma_{\rm dual}}e^{t\log^2k/4},
\quad
\sigma_{\rm dual}=1-\sigma+\tfrac t2\log P,
\quad
C_{\rm sd}=P^{1/2-\sigma}e^{t\log^2P/4}.
\tag{40}
\]
This is an exact algebraic identity for the leading stationary weight,
with all frozen physical data. Similarly
\[
\rho_{n_k}=-\rho_k+\delta_\mu,
\qquad\delta_\mu=\log P-2\mu.
\tag{41}
\]
Thus the prescribed quadratic log-weight remains quadratic after the
stationary transformation, and the centered log is reflected up to the
explicit displacement. The phase of that stationary component, including
the actual carrier and negative curvature, is
\[
\theta_t+T\log P-T-\pi/4-T\log k.
\tag{42}
\]
Relative to the conjugate actual summand, its constant mismatch is
\(2\theta_t+T\log P-T-\pi/4\). A claim that this is small needs
the physical carrier formula, not a freely selected angle. The
[central continuation](../../notes/22_SIGNED_PAIR_TRANSFORMS_AND_STATIONARY_REFLECTION_20261010.md)
proves with those exact formulas that
\(\sigma-(1/2+(t/4)\log P)=O(tx^{-2}+t^2x^{-1})\),
\(\delta_\mu=O(x^{-2})\), and the phase mismatch plus \(2\pi\)
is \(O(x^{-1})\). Its coefficient reflection payment is separate from,
and may be combined with, the uniformly proved transformation error here
when its stated macroscopic interval hypotheses hold.

Equations (40)–(42) are not a full-cutoff equality. For the physical
block \(N/2<n\le N\), the genuine stationary modes lie in
\(P/N\le k<2P/N\), asymptotically \(N\le k<2N\). For the
whole original cutoff they extend from about \(N\) up to about
\(N^2\). These dual indices need not lie in the original finite
approximant. Moreover (29) retains incomplete rather than full Gaussian
integrals, the derivative correction, and both endpoint families.
Replacing all that by a full conjugate cutoff would discard terms not
paid by (39). The transformed formula may expose a useful correlation
between product and difference phases, but it has not proved its sign.

## 9. Remaining signed task and proof scope

Combining this paid product transformation with Note 6's ratio
transformation gives a complete four-channel signed representation with
uniformly vanishing additional error. To exclude a density-strengthened
all-real threshold candidate, one still needs a rigorously negative upper
bound for the recombined representation beating its one-sided
candidate-null payment and its recomputed physical threshold payment.
Keeping an oscillation is not itself a sign theorem.

The substantial new lemma is the finite interval transformation (29)–(30)
and its global applications (34), (39). Their proofs handle stationary
points crossing integer endpoints without small-denominator exclusions,
retain both mixed block/core classes, and avoid the exponentially growing
absolute phase-derivative envelope. Their retained main terms can be
analyzed symbolically and asymptotically; no numerical mode evaluation is
required to establish the lemma.

Independent mathematical review should check the finite Poisson endpoint
halves; both signs in (11); the \(-iP_s\) convention; the expanded
stationary band bounds; removable poles in (15); the regular quotient
identity (27); the inverse derivatives in (21); and the double/global
summation of the dyadic remainders. All constants in the displayed
asymptotic bounds are uniform only for sufficiently small time on the
stated closed \(\kappa\) interval. Exact formulas retain their literal
physical data at any allowed center.
