# Coupled Möbius primitive frontier and resonant sublattices

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model family: GPT-6 (Codex); the exact serving variant and configured reasoning
effort are not exposed and are not inferred. This is an internal analytical
derivation, not independent mathematical validation. No numerical sweeps were
used.

This continues [Note 6](6_ANALYTIC_COMMON_FACTOR_SMOOTHING_AND_PRIMITIVE_SIGNED_FRONTIER_20261010.md)
on the primitive signed frontier, retaining the exact kernels of
[Note 3](3_PAID_DUAL_KERNELS_AND_ACTUAL_FREQUENCY_RELAXATION_LOSS_20261010.md).
It applies both to the original degree-four feature vector and the
degree-six extension in
[Note 7](7_DIAGONAL_ANNIHILATING_PAID_KERNELS_AND_NEAR_PAIR_BOUNDS_20261010.md).
Its coupled sublattice representation complements the product-channel
transformation of
[Note 8](8_OSCILLATION_PRESERVING_PRODUCT_POISSON_TRANSFORM_20261010.md)
and the reflection discussion in
[Heat Note 22](../../notes/22_SIGNED_PAIR_TRANSFORMS_AND_STATIONARY_REFLECTION_20261010.md).

The result is an exact Möbius decomposition of the actual small-common-factor
frontier, followed by an oscillation-preserving finite Poisson transformation
of its coupled ratio and product channels. Every literal block/complement
endpoint is retained. The global transformation error is uniformly smaller
than the available physical upper-budget scale. The resonant oscillatory
integrals remain in the main expression; no sign of that expression, collision
exclusion, or RH conclusion is established.

## 1. Actual coefficients and a general finite feature vector

Freeze a physical center in the sector of Notes 2–6:

\[
0<t\le1/20,\quad 1\le\kappa\le3/2,\quad L=\kappa/t,\quad
x=4\pi e^L,\quad N=\left\lfloor\sqrt{e^L+t/16}\right\rfloor.
\]

Retain the actual common arithmetic frequency \(T>0\), carrier \(\theta_t\),
centering \(\mu\), and prescribed real-index weight

\[
w(u)=u^{-\sigma}e^{t\log^2u/4},\quad
\rho_u=\log u-\mu,\quad \phi_u=\theta_t+T\log u,\quad
P=\frac{T}{2\pi}\asymp N^2.
\tag{1}
\]

The heat time \(t\) is distinct from the arithmetic frequency \(T\). Every
derivative below concerns an auxiliary summation variable with these physical
quantities fixed; it is not a raw spatial derivative.

Let \(v(\rho)\) be a complex vector polynomial of a fixed dimension and
degree at most \(D\), with real-coefficient real and imaginary parts. Choose
\(A_v\ge1\) so that all its coefficients have norm bounded by \(A_v\), and
let \(Q\) be a real symmetric matrix acting on its real feature vector.
Constants below may depend on \(D\), the fixed dimension, and the selected
norm convention; all dependence on \(A_v\) and \(\|Q\|\) remains explicit.

For the original five features,

\[
v(\rho)=r(\rho)-is(\rho),\quad
r(\rho)=(1,\epsilon\rho,\rho^2,0,\rho^4)^T,\quad
s(\rho)=(0,\rho,0,\rho^3,0)^T,
\]

and \(Q=\mathbb Q_{\Lambda,B}\) from Note 3. Thus \(D=4\) and one may
take \(A_v=C(1+|\epsilon|)\). The extension with \(X_6,Y_6,Y_5\) has \(D=6\);
the same theorem applies to its appropriately enlarged matrix.

Define

\[
z_n=w(n)e^{i\phi_n}v(\rho_n),\qquad y_n=\operatorname{Re}z_n.
\tag{2}
\]

The complete signed quadratic dual is

\[
\mathcal K=\sum_{n,m\le N}y_n^TQy_m
=\left(\sum_{n\le N}y_n\right)^TQ\left(\sum_{n\le N}y_n\right).
\]

For every ordered pair,

\[
y_n^TQy_m=\frac12\operatorname{Re}
\{z_n^TQ\overline{z_m}+z_n^TQz_m\}.
\tag{3}
\]

The two terms are the complete ratio and product channels. With
\(v=r-is\), their imaginary parts give exactly Note 3's difference-sine
and product-sine orientations. In particular neither channel is omitted.

## 2. An exact coupled Möbius formula

For an integer \(1\le J\le N\), let the small-common-factor frontier be

\[
\mathcal F_J=
\sum_{\substack{n,m\le N\\ \gcd(n,m)\le J}}y_n^TQy_m.
\tag{4}
\]

Write \(\mu_{\rm Mob}\) for the Möbius function, distinct from the
centering \(\mu\), and define

\[
c_J(q)=\sum_{\substack{j\mid q\\j\le J}}\mu_{\rm Mob}(q/j),
\quad
V_q=\sum_{u=1}^{\lfloor N/q\rfloor}z_{qu},
\quad Y_q=\operatorname{Re}V_q.
\tag{5}
\]

Then, exactly,

\[
\boxed{\mathcal F_J=\sum_{q\le N}c_J(q)\,Y_q^TQY_q
=\frac12\operatorname{Re}\sum_{q\le N}c_J(q)
\{V_q^TQ\overline{V_q}+V_q^TQV_q\}.}
\tag{6}
\]

### Proof

The elementary divisor identity gives, for every positive integer \(g\),

\[
\begin{split}
\sum_{q\mid g}c_J(q)
&=\sum_{\substack{j\mid g\\j\le J}}
  \sum_{d\mid g/j}\mu_{\rm Mob}(d)\\
&=\mathbf1_{\{g\le J\}}.
\end{split}
\]

Insert this identity with \(g=\gcd(n,m)\) into (4), interchange finite
sums, and sum over the pairs \(n=qu,m=qv\). This proves the first
equality in (6); (3) proves the second.

Equivalently one may first fix the literal common factor \(j\le J\),
write \(n=ja,m=jb\), and use
\(\mathbf1_{\{\gcd(a,b)=1\}}=\sum_{d\mid a,b}\mu_{\rm Mob}(d)\).
Then \(q=jd\) produces (5). Thus (6) is the outer coprime-ratio sum of
Note 6 with the true coprimality condition preserved, not a free-phase
or independent-coefficient relaxation.

Useful exact checks are

\[
|c_J(q)|\le\tau(q),\qquad c_J(1)=1,\qquad
c_J(q)=0\quad(1<q\le J),
\tag{7}
\]

where \(\tau(q)\) is the divisor-counting function. For \(J=1\),
\(c_J(q)=\mu_{\rm Mob}(q)\); for \(J=N\), only \(q=1\) survives.
The terms with \(q>J\) generally survive and cannot be truncated merely
because the original common factor is at most \(J\).

### Every literal block and complement term

Set \(K=\lfloor N/2\rfloor\), and put

\[
m_q=\lfloor N/q\rfloor,\qquad k_q=\lfloor K/q\rfloor,\qquad
V_q^{\mathcal C}=\sum_{u=1}^{k_q}z_{qu},\qquad
V_q^{\mathcal B}=\sum_{u=k_q+1}^{m_q}z_{qu}.
\tag{8}
\]

Empty sums are zero and \(V_q=V_q^{\mathcal C}+V_q^{\mathcal B}\).
Expanding every quadratic in (6) retains both mixed orientations and
both same-block terms. No floor is replaced by a continuous cutoff.

The two original paid candidate coordinates constrain designated
coordinates of \(Y_1\), the complete moment vector. They do not constrain
each \(Y_q\) separately. Any additional candidate constraint introduced
by a higher-feature kernel also needs its own complete-vector proof.
Moreover \(c_J(q)\) can be negative. Neither a separate sublattice sign
nor sublattice candidate vanishing follows from the actual candidate.

## 3. Endpoint-paid finite Poisson transformation

Consider one of the literal sublattice sums in (8), with its integer
indices \(p\le u\le r\). Use the half-integer endpoints

\[
a_0=p-\frac12,\qquad b_0=r+\frac12,\qquad a_0\ge\frac12.
\tag{9}
\]

For the complete sum these are \(1/2,m_q+1/2\); for the complement and
block they are respectively

\[
\left[\frac12,k_q+\frac12\right],\qquad
\left[k_q+\frac12,m_q+\frac12\right].
\tag{10}
\]

An empty interval contributes zero. These endpoints preserve exactly the
integer membership conditions \(qu\le K\) and \(K<qu\le N\).

Let

\[
a_q(u)=w(qu)v(\rho_{qu}),\qquad
\Phi_q(u)=\theta_t+T\log(qu),\qquad
I_{q,k}[a_0,b_0]=
\int_{a_0}^{b_0}a_q(u)e^{i\Phi_q(u)-2\pi iku}\,du.
\tag{11}
\]

All resonant integrals will remain exact. Choose an integer \(M\ge1\)
such that \(M\ge4P\). At a half-integer endpoint \(z\), put
\(\omega=P/z\) and define the symmetric tail functions

\[
S_\ell(\omega,M)=
\sum_{|k|>M}^{\rm sym}\frac{(-1)^k}{(\omega-k)^\ell},
\qquad \ell=1,2,3.
\tag{12}
\]

For \(\ell=1\) the paired series is absolutely convergent, since
\[
(\omega-k)^{-1}+(\omega+k)^{-1}
=\frac{2\omega}{\omega^2-k^2}.
\]
For \(\ell\ge2\) the series itself is absolutely convergent. Here
\(|\omega|\le2P\le M/2\), so there is no pole.

The endpoint term is explicit:

\[
\begin{split}
\mathcal E_{q,M}(z)=e^{i\Phi_q(z)}
\bigg\{&
\frac{a_q(z)}{2\pi i}S_1(\omega,M)
+\frac{a_q'(z)}{(2\pi)^2}S_2(\omega,M)\\
&+\frac{T\,a_q(z)}{z^2(2\pi)^3}S_3(\omega,M)\bigg\}.
\end{split}
\tag{13}
\]

Define the finite transformed vector by

\[
\widetilde V_q[a_0,b_0]=
\sum_{|k|\le M}I_{q,k}[a_0,b_0]
+\mathcal E_{q,M}(b_0)-\mathcal E_{q,M}(a_0).
\tag{14}
\]

Under the small-time physical reserves stated in Section 4,

\[
\boxed{
\left\|\sum_{u=p}^{r}z_{qu}
-\widetilde V_q[a_0,b_0]\right\|
\le \frac{C_D A_v}{M}\,
w(q)(1+|\rho_q|)^D.}
\tag{15}
\]

### Exact tail functions without an unevaluated Fourier tail

For \(z>0\), define the elementary integral

\[
F(z)=\int_0^1\frac{s^{z-1}}{1+s}\,ds
=\sum_{n=0}^{\infty}\frac{(-1)^n}{n+z}.
\]

The equality follows by integrating the finite geometric expansion; its
remainder tends to zero. Pairing the two tails in (12) gives

\[
S_1(\omega,M)=(-1)^{M+1}
\{F(M+1+\omega)-F(M+1-\omega)\},
\quad
S_2=-\partial_\omega S_1,\quad
S_3=\tfrac12\partial_\omega^2S_1.
\tag{16}
\]

Thus the boundary coefficients can be written as fixed nonoscillatory
integrals, or equivalently through standard digamma functions. Their
exact values, not an unsigned upper envelope, remain in (14).

### Proof of the finite Poisson identity and tail

Periodize the compactly supported function
\(\mathbf1_{[a_0,b_0]}(u)a_q(u)e^{i\Phi_q(u)}\).
Its periodization is piecewise smooth and is continuous at the integer
evaluation point because the support endpoints are half integers.
Fourier-series convergence there gives

\[
\sum_{u=p}^{r}z_{qu}
=\lim_{R\to\infty}\sum_{|k|\le R}I_{q,k}[a_0,b_0].
\tag{17}
\]

This is the finite-interval version of
[NIST DLMF's Fourier convergence and Poisson formula](https://dlmf.nist.gov/1.8).
No endpoint half weight appears at an integer summand.

For \(|k|>M\), let

\[
g_k(u)=\Phi_q'(u)-2\pi k=T/u-2\pi k,\qquad
\mathcal D_k a=\left(\frac{a}{ig_k}\right)'.
\]

Twice integrating by parts gives the exact identity

\[
I_{q,k}
=\left[e^{i\Phi_q(u)-2\pi iku}
\left\{\frac{a_q}{ig_k}
+\frac{a_q'}{g_k^2}
-\frac{a_qg_k'}{g_k^3}\right\}\right]_{a_0}^{b_0}
+\int_{a_0}^{b_0}\mathcal D_k^2a_q(u)
e^{i\Phi_q(u)-2\pi iku}\,du.
\tag{18}
\]

Since \(g_k'=-T/u^2\) and \(e^{-2\pi ikz}=(-1)^k\) at a half integer,
the symmetric sum of the endpoint terms in (18) is exactly the difference
of (13). The remaining integrand satisfies

\[
\|\mathcal D_k^2a\|
\le\frac{\|a''\|}{|g_k|^2}
+\frac{3\|a'\||g_k'|}{|g_k|^3}
+\|a\|\left(\frac{3|g_k'|^2}{|g_k|^4}
+\frac{|g_k''|}{|g_k|^3}\right).
\]

Because \(u\ge1/2\) and \(M\ge4P\),

\[
|g_k|\ge\pi|k|,\quad
|g_k'|\le\pi|k|/u,\quad
|g_k''|\le2\pi|k|/u^2.
\]

Consequently

\[
\|\mathcal D_k^2a\|
\le\frac1{\pi^2k^2}
\{\|a''\|+3\|a'\|/u+5\|a\|/u^2\}.
\tag{19}
\]

Section 4 bounds the integral of this envelope by
\(C_DA_vw(q)(1+|\rho_q|)^D/k^2\).
Summing \(\sum_{|k|>M}k^{-2}\le2/M\) proves (15). In particular the
remainder has no factor \(T^2\): the actual large phase was integrated,
not differentiated into an absolute coefficient budget.

## 4. Uniform amplitude and sublattice moment bounds

Use the genuine asymptotics already proved in Notes 2, 4, and 6:

\[
\mu=\log N+O(N^{-1}),\qquad
c_\sigma:=\sigma-\tfrac t2\log N=\tfrac12+o(1),\qquad
t\log N=\kappa/2+o(1),\qquad
Nw_N\asymp N^{1/2-\kappa/8}.
\tag{20}
\]

They are uniform on the stated closed \(\kappa\)-interval. For all
sufficiently small \(t\), choose the reserves

\[
\frac7{16}\le c_\sigma\le\frac9{16},\qquad
\frac7{16}\le t\log N\le\frac{13}{16},\qquad
|\mu-\log N|\le1.
\tag{21}
\]

These reserves also give \(|\mu|\le C L\). All auxiliary intervals in
(10) have \(1/2\le u\le N/q+1/2\), hence \(q/2\le qu\le3N/2\).
The logarithmic weight derivative there is

\[
\zeta(qu):=-\sigma+\tfrac t2\log(qu).
\]

Its magnitude is uniformly bounded, and
\(\sigma-\tfrac t2\log(qu)\ge3/8\) throughout this range.
For example the latter follows from
\(c_\sigma-(t/2)\log(3/2)\ge3/8\) using (21) and \(t\le1/20\).
Differentiating only the amplitude in (11) gives

\[
\begin{aligned}
a_q'(u)&=\frac{w(qu)}u\{\zeta(qu)v+v'\},\\
a_q''(u)&=\frac{w(qu)}{u^2}
\{(\zeta^2-\zeta+t/2)v+(2\zeta-1)v'+v''\}.
\end{aligned}
\tag{22}
\]

The polynomial and its first two derivatives have norm at most
\(C_DA_v(1+|\rho_{qu}|)^D\). Therefore

\[
\|a_q^{(j)}(u)\|\le
C_DA_vw(qu)u^{-j}(1+|\rho_{qu}|)^D,\qquad j=0,1,2.
\tag{23}
\]

For \(u\ge1\), the logarithmic derivative bound implies
\(w(qu)/w(q)\le u^{-3/8}\); for \(1/2\le u\le1\) the ratio is
bounded by an absolute constant. Also
\[
(1+|\rho_{qu}|)^D
\le(1+|\rho_q|)^D(1+|\log u|)^D.
\]
Thus

\[
\int_{1/2}^{N/q+1/2}
w(qu)u^{-2}(1+|\rho_{qu}|)^D\,du
\le C_Dw(q)(1+|\rho_q|)^D.
\tag{24}
\]

This proves the integral bound used after (19).

For the discrete sublattice moments, Note 6's bin proof gives

\[
\sum_{u\le N/q}w(qu)(1+|\rho_{qu}|)^D
\le C_D\frac Nq w_N,\qquad
\|V_q\|\le C_DA_v\frac Nq w_N.
\tag{25}
\]

For completeness, set \(A=N/q\), \(y_u=\log(A/u)\). Exactly
\[
w(qu)/w_N=e^{c_\sigma y_u+t y_u^2/4}.
\]
Since \(0\le y_u\le\log N\), (21) gives
\(c_\sigma+t y_u/4\le49/64<1\). The bin
\(h\le y_u<h+1\) contains at most \(Ae^{-h}\) indices, its weight
ratio is at most \(e^{49(h+1)/64}\), and its polynomial factor is at
most \((h+3)^D\). Summing the convergent geometric-polynomial series
proves (25), including the last bin at \(u=1\).

The same reserves give, for integer \(1\le q\le N\),

\[
w(q)\le q^{-s_0},\qquad s_0=\frac{35}{64}>\frac12,
\tag{26}
\]

because
\[
\sigma-\tfrac t4\log q
\ge c_\sigma+\tfrac t4\log N\ge35/64.
\]
The sharper physical value is \(1/2+\kappa/8+o(1)\); the fixed reserve
(26) suffices. Elementary divisor convolution now gives the uniform bounds

\[
\sum_{q\le N}\frac{\tau(q)w(q)}q
\le\zeta(1+s_0)^2,\qquad
\sum_{q\le N}\tau(q)w(q)^2\le\zeta(2s_0)^2.
\tag{27}
\]

Indeed \(\sum_{q\ge1}\tau(q)q^{-s}=\sum_{a,b\ge1}(ab)^{-s}
=\zeta(s)^2\) for \(s>1\). No cancellation of the Möbius function is
assumed in these positive remainder estimates.

## 5. A complete global payment for the coupled primitive transform

Apply (14) to the block and complement intervals, set
\(\widetilde V_q=\widetilde V_q^{\mathcal B}
+\widetilde V_q^{\mathcal C}\), and define

\[
\widetilde{\mathcal F}_J=
\sum_{q\le N}c_J(q)
(\operatorname{Re}\widetilde V_q)^TQ
(\operatorname{Re}\widetilde V_q).
\tag{28}
\]

The endpoint terms at the shared half integer cancel when the two vectors
are added, but retaining them separately keeps every mixed block term
reviewable. The global bound is

\[
\boxed{
|\mathcal F_J-\widetilde{\mathcal F}_J|
\le C_D\|Q\|A_v^2
\left\{\frac{(Nw_N)L^D}{M}+\frac{L^{2D}}{M^2}\right\}.}
\tag{29}
\]

It is uniform for \(1\le J\le N\), and retains all matrix and feature
scales explicitly.

### Proof

By (15), with both intervals included,
\[
E_q:=\|V_q-\widetilde V_q\|
\le C_DA_v M^{-1}w(q)(1+|\rho_q|)^D.
\]
The elementary quadratic perturbation inequality gives
\[
|Y_q^TQY_q-
(\operatorname{Re}\widetilde V_q)^TQ
(\operatorname{Re}\widetilde V_q)|
\le\|Q\|E_q(2\|V_q\|+E_q).
\]
Multiply by \(|c_J(q)|\le\tau(q)\), use (25), and sum. Since
\(1+|\rho_q|\le C L\), the linear-error term is at most
\[
C_D\|Q\|A_v^2\,\frac{(Nw_N)L^D}{M}
\sum_{q\le N}\frac{\tau(q)w(q)}q,
\]
while the squared-error term is at most
\[
C_D\|Q\|A_v^2\,\frac{L^{2D}}{M^2}
\sum_{q\le N}\tau(q)w(q)^2.
\]
Equation (27) proves (29).

With \(M=\lceil4P\rceil\asymp N^2\), (20) gives

\[
|\mathcal F_J-\widetilde{\mathcal F}_J|
=O_D\!\left(\|Q\|A_v^2
\{L^DN^{-3/2-\kappa/8}+L^{2D}N^{-4}\}\right).
\tag{30}
\]

For fixed \(D\) and matrix/feature scales bounded by any fixed power of
\(L\), this is \(o(N^{-\kappa/4})\), uniformly on \([1,3/2]\).
In particular the density-strengthened matrix scale \(\|Q\|=O(L)\)
does not spoil the estimate. For \(D=4\), the powers are \(L^4,L^8\);
for \(D=6\), they are \(L^6,L^{12}\).

This compares the transformation remainder with an available upper-budget
scale, not with a positive lower bound for measured physical error. Physical
Bell residuals, holomorphic remainders, and one-sided candidate payments
remain separate obligations. Any faster matrix or feature growth must remain
in (29), rather than being silently absorbed into a constant.

## 6. Exact resonant geometry and the sublattice reflection

The retained phase in (11) has derivative
\[
T/u-2\pi k.
\]
For positive \(k\), its unique stationary point is

\[
u_*=\frac Pk,\qquad n_*=qu_*=\frac{qP}k.
\tag{31}
\]

It lies in the literal interval precisely when
\[
P/b_0<k<P/a_0;
\]
equalities are endpoint transitions. Negative \(k\) and \(k=0\) have no
interior stationary point. The exact stationary phase value is

\[
\Phi_q(u_*)-2\pi ku_*
=\theta_t+T\{\log(qP)-1\}-T\log k.
\tag{32}
\]

The Gaussian stationary coefficient, when a stationary point is isolated
inside a smooth local cutoff, is

\[
\frac{\sqrt P}{k}\,w(qP/k)\,
v(\log(qP/k)-\mu)\,
e^{i\{\theta_t+T(\log(qP)-1)-T\log k-\pi/4\}}.
\tag{33}
\]

This identifies the standard stationary term
([NIST DLMF, stationary phase](https://dlmf.nist.gov/2.3#iv)).
No uniform replacement of the exact integrals by (33) is used in (29).
Near-endpoint Fresnel terms, nonstationary pieces, and every approximation
error would need their own global payment before such a replacement.

The amplitude and centering in (33) have an exact algebraic reflection:

\[
\begin{aligned}
\frac{\sqrt P}{k}w(qP/k)
&=C_q\,k^{-\sigma_q^*}e^{t\log^2k/4},\\
C_q&=\sqrt P\,(qP)^{-\sigma}
 e^{t\log^2(qP)/4},\\
\sigma_q^*&=1-\sigma+\tfrac t2\log(qP),\\
\mu_q^*&=\log(qP)-\mu,\qquad
\log(qP/k)-\mu=-(\log k-\mu_q^*).
\end{aligned}
\tag{34}
\]

For \(q=1\), the physical leading asymptotics make this close to the
prescribed weight and central logarithmic reflection; the exact physical
mismatch is part of Heat Note 22. For \(q>1\), there are additional shifts
\[
\sigma_q^*=\sigma_1^*+\tfrac t2\log q,\qquad
\mu_q^*=\mu_1^*+\log q,\qquad
\theta_q^*=\theta_1^*+T\log q,
\tag{35}
\]
where \(\theta_q^*=\theta_t+T(\log(qP)-1)-\pi/4\).

The cutoff also changes. For fixed \(q\) in a macroscopic physical block
\(N/2<n\le N\), the stationary modes satisfy
\(k\sim qN\) through \(2qN\), using \(P/N^2\to1\). The exact endpoints
are those in (9)–(10), even when the sublattice has only a few terms.
Reflection does not conserve the original cutoff. In particular it is
invalid to replace all Möbius sublattices by the same \(q=1\) reflected
sum without these shifts and changed ranges.

In the ratio term of (6), the two reflected carriers at a fixed \(q\)
cancel and the logarithmic phase reverses orientation. In its product term,
both carriers remain, including \(2T\log q\). This is a genuine coupled
arithmetic phase relation, not independent prime phases or arbitrary
choices of phases at each sublattice.

## 7. Scoped signed target and remaining obstruction

Equations (6), (14), and (29) transform the actual coprime/small-gcd
frontier while preserving both oscillatory channels. The error is harmless
at the existing physical scale, but the resonant main expression has no
proved one-sided sign. Its Möbius coefficients can have either sign, and
the complete candidate constraints do not apply separately to its factors.
Treating those factors as independent or imposing their own null conditions
would enlarge or alter the actual arithmetic problem.

To recombine without counting a pair twice, split
\[
\mathcal K=\mathcal F_J+\mathcal D_{>J}+\mathcal P_{>J}.
\tag{36}
\]
Here \(\mathcal D_{>J}\) and \(\mathcal P_{>J}\) are exactly the ratio
and product terms with actual common factor greater than \(J\).
For the original kernel and Note 7's diagonal-annihilating kernel, whose
ratio and product polynomials have total degree at most six, Note 6's proof
directly transforms \(\mathcal D_{>J}\), and Note 8 applies to the matching
product intervals; alternatively the latter can remain exact. An arbitrary
quadratic form on degree-six features can have total degree twelve. Its
recombination requires the corresponding fixed-degree smoothing extension
of Note 6's proof and the stated amplitude bounds in Note 8; it is not
covered merely by invoking the degree-six polynomial case. The coupled
form (28) is an alternative representation of the whole
small-gcd piece, not an extra correction added to its already counted
product channel.

A concrete next analytical lemma would give a candidate-conditioned
one-sided bound for the coupled resonant expression in (28), retaining
the \(c_J(q)\), reflected centers and weights, both product/ratio phases,
and literal endpoint functions, after complete recombination in (36).
It must beat the transformation remainders and the same dual's candidate
and physical payments. The most promising restricted starting point is
the \(q=1\) near-endpoint reflection, followed by a paid treatment of the
shifted \(q>1\) terms. Neither a sign for one block nor a freely chosen
sublattice phase would establish that lemma.

This note supplies an exact oscillation-preserving proof framework and a
global vanishing remainder. It does not establish the missing signed
estimate, higher-multiplicity exclusion, complementary parameter coverage,
or the small-time endpoint.
