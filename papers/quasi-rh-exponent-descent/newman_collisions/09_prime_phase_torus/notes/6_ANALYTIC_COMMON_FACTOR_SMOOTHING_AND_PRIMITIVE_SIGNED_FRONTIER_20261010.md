# Analytical common-factor smoothing and the primitive signed frontier

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. This is an internal analytical
derivation, not independent mathematical validation.

This continues project 09's
[centered arithmetic reduction](2_CENTERED_COLLISION_JETS_AND_RATIO_PRODUCT_CORRELATIONS_20261010.md),
[paid dual kernels](3_PAID_DUAL_KERNELS_AND_ACTUAL_FREQUENCY_RELAXATION_LOSS_20261010.md),
[prescribed weight hierarchy](4_PRESCRIBED_HEAT_WEIGHT_COVARIANCE_AND_SIGNED_HIERARCHY_20261010.md),
and [one-sided payments](5_SHARP_ONE_SIDED_DUAL_PAYMENTS_ON_CORRELATED_CANDIDATES_20261010.md).
It supplies an analytical coefficient transformation for the signed target
in [Heat Note 20](../../notes/20_ANALYTIC_SCHUR_CONES_AND_DENSITY_STRENGTHENED_THRESHOLDS_20261010.md),
with [Heat Note 21](../../notes/21_DEFLATED_LOCAL_GROWTH_AND_THRESHOLD_MULTIPLICITY_20261010.md)'s
threshold counting input retained below. The result is an Euler–Maclaurin transformation of the
**actual prescribed common-factor coefficients**, with all physical block
and complement terms and every floor endpoint retained. A cutoff of the
common factor gives a uniformly vanishing global transformation remainder.
The primitive and small-common-factor signed correlation remains exact.
No sign of that correlation, collision exclusion, RH, or novelty claim is
established.

## 1. Complete dual and the coefficient being transformed

At a physical center retain

\[
0<t\le1/20,\quad 1\le\kappa\le3/2,\quad L=\kappa/t,
x=4\pi e^L,\quad N=\lfloor\sqrt{e^L+t/16}\rfloor,
\]
\[
\mu=\Omega/c,\quad\rho_n=\log n-\mu,\quad
w_n=n^{-\sigma}e^{t\log^2n/4},\quad
\sigma=1/2+t\Re\alpha/2,
\quad\phi_n=\theta_t+T\log n,\quad\epsilon=d/c.
\]

All physical quantities, the cutoff, and the selected dual parameters are
frozen in the transformation below. Its derivatives are with respect to
the auxiliary common factor, **not raw spatial derivatives**. Physical
Bell residuals and heat approximation errors remain the separate payments
of the earlier notes.

Write

\[
\mathbb Q=\begin{pmatrix}\Lambda&B\\B^T&Q\end{pmatrix},
\qquad Q=\begin{pmatrix}-\Gamma&0&3/2\\0&2&0\\3/2&0&0\end{pmatrix},
\quad\Gamma=\gamma/c^2,
\]
\[
r(v)=(1,\epsilon v,v^2,0,v^4)^T,\qquad
s(v)=(0,v,0,v^3,0)^T.
\]
For variables \(v_a,v_b\), define the genuine difference-channel
polynomials

\[
\begin{aligned}
\mathfrak h_c(v_a,v_b)
 &=\tfrac12\{r(v_a)^T\mathbb Qr(v_b)
                    +s(v_a)^T\mathbb Qs(v_b)\},\\
\mathfrak h_s(v_a,v_b)
 &=\tfrac12\{r(v_b)^T\mathbb Qs(v_a)
                    -r(v_a)^T\mathbb Qs(v_b)\}.
\end{aligned}\tag{1}
\]

Thus \(\mathfrak h_c\) is symmetric and \(\mathfrak h_s\) is
antisymmetric. The latter multiplies \(\sin(T\log(a/b))\), with the
same orientation as project 09 Note 3. Each polynomial has total degree at
most six. In particular the fixed threshold block has no \(X_4^2\)
entry, so a degree-eight term is absent; the dual additions have degree at
most five.

For coprime positive integers \(a,b\), put \(A=\log a\), \(C=\log b\),
\(J_{a,b}=\lfloor N/\max(a,b)\rfloor\). For \(u>0\), define

\[
\begin{aligned}
W_{a,b}&=(ab)^{-\sigma}
               \exp\{t(A^2+C^2)/4\},\\
\beta_{a,b}&=2\sigma-\tfrac t2\log(ab),\\
H_{a,b,\chi}(z)&=\mathfrak h_\chi(z+A-\mu,z+C-\mu),
\qquad\chi=c,s,\\
f_{a,b,\chi}(u)&=W_{a,b}u^{-\beta_{a,b}}
                e^{t\log^2u/2}H_{a,b,\chi}(\log u).
\end{aligned}\tag{2}
\]

Direct expansion of the prescribed weights gives

\[
f_{a,b,\chi}(j)=w_{ja}w_{jb}
               \mathfrak h_\chi(\rho_{ja},\rho_{jb}).\tag{3}
\]

Consequently the complete difference part is exactly

\[
\mathcal D_{\Lambda,B}
=\sum_{(a,b)=1\atop\max(a,b)\le N}
 \left\{\Big(\sum_{j=1}^{J_{a,b}}f_{a,b,c}(j)\Big)
                   \cos(T\log(a/b))
       +\Big(\sum_{j=1}^{J_{a,b}}f_{a,b,s}(j)\Big)
                   \sin(T\log(a/b))\right\}.\tag{4}
\]

There is one actual \(T\); no independent prime phases are introduced.
The full dual is \(\mathcal K_{\Lambda,B}=\mathcal D_{\Lambda,B}
+\mathcal P_{\Lambda,B}\), where both product sine/cosine channels
remain exactly as in Note 3. Nothing below replaces or discards them.

## 2. Exact common-factor intervals for every block/complement term

Set \(K=\lfloor N/2\rfloor\), with physical block
\(\mathcal B=\{K+1,\ldots,N\}\) and complete complement
\(\mathcal C=\{1,\ldots,K\}\). For a fixed ordered pair \((a,b)\),
write \(k_a=\lfloor K/a\rfloor\), \(k_b=\lfloor K/b\rfloor\).
The four disjoint integer intervals are

\[
\begin{array}{c|cc}
\text{pair class}&\ell&v\\\hline
\mathcal C\times\mathcal C&1&\min(J_{a,b},k_a,k_b)\\
\mathcal B\times\mathcal B&\max(1,k_a+1,k_b+1)&J_{a,b}\\
\mathcal B\times\mathcal C&\max(1,k_a+1)&\min(J_{a,b},k_b)\\
\mathcal C\times\mathcal B&\max(1,k_b+1)&\min(J_{a,b},k_a).
\end{array}\tag{5}
\]

An interval is empty when \(\ell>v\). Every \(1\le j\le J_{a,b}\)
belongs to exactly one row. This follows by imposing the two literal
conditions \(ja>K\) or \(ja\le K\), and \(jb>K\) or \(jb\le K\).
In particular both mixed classes are retained.

For a positive integer common-factor cutoff \(J_*\), retain the terms
\(j\le J_*\) exactly. In each nonempty row of (5), transform only

\[
\ell_*:=\max(\ell,J_*+1)\le j\le v.\tag{6}
\]

All cutoffs in (5)–(6) are literal floors. They are never replaced by
\(N/a\), \(N/b\), or a moving continuous cutoff. Endpoint changes at
cutoff transitions therefore remain in the formula.

## 3. Euler–Maclaurin formula and an exact derivative recurrence

Fix a positive integer order \(r\). For any nonempty integer interval
\([p,q]\), define

\[
\begin{split}
\mathsf E_r[f;p,q]
={}&\int_p^q f(u)\,du+\frac{f(p)+f(q)}2\\
 &+\sum_{h=1}^r\frac{B_{2h}}{(2h)!}
                      \{f^{(2h-1)}(q)-f^{(2h-1)}(p)\}.
\end{split}\tag{7}
\]

Then, exactly,

\[
\sum_{j=p}^q f(j)=\mathsf E_r[f;p,q]+R_r[f;p,q],\qquad
R_r=-\frac1{(2r)!}\int_p^q
                \widetilde B_{2r}(u)f^{(2r)}(u)\,du,\tag{8}
\]
\[
|R_r|\le\frac{2\zeta(2r)}{(2\pi)^{2r}}
                       \int_p^q|f^{(2r)}(u)|\,du.\tag{9}
\]

Here \(\widetilde B_{2r}(u)=B_{2r}(u-\lfloor u\rfloor)\).
Formula (8) follows from the Euler–Maclaurin identity by including its
last endpoint correction; the periodic Bernoulli Fourier series gives
(9). For \(p=q\), (7) is exactly \(f(p)\) and the remainder is zero.
Thus singleton intervals need no special estimate. See
[NIST DLMF, Euler–Maclaurin formula](https://dlmf.nist.gov/2.10.E1)
and [Bernoulli Fourier series](https://dlmf.nist.gov/24.8.E1).

For the actual functions (2), all derivative corrections and the
remainder integrand have an explicit finite recurrence. Set

\[
P_0(z)=H_{a,b,\chi}(z),\qquad
P_{k+1}(z)=P_k'(z)+(tz-\beta_{a,b}-k)P_k(z).\tag{10}
\]

Then induction using \(d/du=u^{-1}d/dz\) proves

\[
f_{a,b,\chi}^{(k)}(u)
 =W_{a,b}u^{-\beta_{a,b}-k}
                      e^{t\log^2u/2}P_k(\log u).\tag{11}
\]

This includes the derivative of the genuine quadratic heat weight; a
pure power coefficient is not substituted. The actual \(\epsilon\)
is retained in (1), and the common height/carrier stay in the outer
phases of (4).

## 4. Explicit main integrals

If \(H(z)=\sum_{m=0}^6 h_mz^m\) and \(\lambda=1-\beta_{a,b}\),
the integral in (7) is

\[
W_{a,b}\sum_{m=0}^6h_m\partial_\lambda^m
 \int_{\log p}^{\log q}e^{tz^2/2+\lambda z}\,dz.\tag{12}
\]

For \(t>0\) the zeroth integral is explicitly

\[
\sqrt{\frac\pi{2t}}e^{-\lambda^2/(2t)}
\left[
 \operatorname{erfi}\left(\frac{tz+\lambda}{\sqrt{2t}}\right)
\right]_{\log p}^{\log q}.\tag{13}
\]

Equations (7), (10), and (12)–(13) give finite analytical endpoint
expressions for every transformed coefficient. They introduce no new
phase variables and do not assert positivity of those expressions.

## 5. Uniform centered weighted moments for a real common factor

The following elementary estimate removes a needless power of \(L\)
from the global remainder. Use the physical asymptotics established in
project 09 Notes 2 and 4:

\[
\mu=\log N+O(N^{-1}),\qquad
\sigma-\tfrac t2\log N=\tfrac12+o(1),\qquad
Nw_N\asymp e^{\mathfrak a/t},\quad
\mathfrak a=\kappa(4-\kappa)/16.\tag{14}
\]

All asymptotics are uniform in the stated closed \(\kappa\) interval.
For every fixed integer \(d\ge0\), uniformly for real \(1\le u\le N\),

\[
\sum_{a\le N/u}w(ua)(1+|\log(ua)-\mu|)^d
                 \le C_d\frac Nu w_N.\tag{15}
\]

Here \(w(v)=v^{-\sigma}e^{t\log^2v/4}\) is the actual positive
real-index extension of the prescribed weight. To prove (15), set
\(A_u=N/u\), \(y_a=\log(A_u/a)\), and
\(c_\sigma=\sigma-(t/2)\log N\). Exactly,

\[
w(ua)/w_N=\exp(c_\sigma y_a+t y_a^2/4).\tag{16}
\]

For sufficiently small time, uniformly in \(\kappa\), choose the
reserves
\(7/16\le c_\sigma\le9/16\), \(t\log N\le13/16\), and
\(|\log N-\mu|\le1\). Then
\(c_\sigma+t y_a/4\le49/64\). The bin
\(h\le y_a<h+1\) has at most \(A_ue^{-h}\) indices, its weight
ratio is at most \(e^{49(h+1)/64}\), and its polynomial factor is
at most \((h+3)^d\). Summing gives the explicit admissible constant

\[
C_d=e^{49/64}\sum_{h\ge0}e^{-15h/64}(h+3)^d<\infty.\tag{17}
\]

The same estimate applies when the final bin reaches \(a=1\); no
unpaid low-index exception is omitted. The constants can be enlarged
on any compact remaining time interval if one needs a statement up to
\(t=1/20\); the asymptotic assertion only requires small time.

## 6. Global remainder theorem

The uniform theorem in this section and its asymptotic consequences hold
for all sufficiently small positive \(t\), uniformly for
\(\kappa\in[1,3/2]\). The exact transformations (1)–(13) themselves
hold at every physical center in the stated positive-time range.

Assume the chosen dual family is bounded; more generally keep its
explicit scale

\[
\mathfrak M=(1+|\epsilon|)^2
                 (1+|\Gamma|+\|\Lambda\|+\|B\|).\tag{18}
\]

For a fixed derivative order \(k\), the recurrence (10) implies

\[
|f_{a,b,\chi}^{(k)}(u)|
 \le C_k\mathfrak M\,u^{-k}w(ua)w(ub)
       (1+|\log(ua)-\mu|)^6(1+|\log(ub)-\mu|)^6,
\quad ua,ub\le N.\tag{19}
\]

Here is why the constants are uniform. The two kernels in (1) have
degree at most six and coefficients bounded by a constant times
\(\mathfrak M\). Every log derivative of these polynomials has the
same polynomial envelope. In (10),

\[
\beta_{a,b}-t\log u
=2c_\sigma+\frac t2
 \left(\log\frac N{ua}+\log\frac N{ub}\right),\tag{20}
\]

which lies in \([7/8,31/16]\) under the reserves above; its log
derivative is \(-t\), bounded by \(1/20\), and all higher log
derivatives vanish. Induction over the finite recurrence now proves
(19), with a constant depending only on \(k\) and the selected matrix
norm convention.

Let \(\widetilde{\mathcal D}_{\Lambda,B}^{(r,J_*)}\) be obtained
from (4) by preserving every term \(j\le J_*\), and replacing each
tail interval (6), for both \(\chi=c,s\), by (7). Then

\[
\boxed{
|\mathcal D_{\Lambda,B}
   -\widetilde{\mathcal D}_{\Lambda,B}^{(r,J_*)}|
 \le C_r\mathfrak M (Nw_N)^2 J_*^{-2r-1}.
}\tag{21}
\]

Proof: the outer sine/cosine factors have absolute value at most one.
The four tail intervals for a fixed \((a,b)\) have disjoint interiors,
so their derivative integrals sum to at most the integral over all
\(u\ge J_*\) with \(ua,ub\le N\). Drop the coprimality condition
only in this positive remainder envelope. By (19) and then (15),

\[
\begin{split}
\sum_{a,b\le N/u}|f_{a,b,\chi}^{(2r)}(u)|
 &\le C_r\mathfrak M u^{-2r}
 \left(\sum_{a\le N/u}w(ua)
         (1+|\log(ua)-\mu|)^6\right)^2\\
 &\le C_r'\mathfrak M (Nw_N)^2u^{-2r-2}.
\end{split}\tag{22}
\]

Integrating over \([J_*,N]\) and using (9) gives (21). This proof
pays all floors and mixed terms through their literal endpoint
expressions. It never bounds the block separately and then pays the
full cross interference by a large moment product.

In particular, define the full transformed dual by

\[
\widetilde{\mathcal K}_{\Lambda,B}^{(r,J_*)}
=\widetilde{\mathcal D}_{\Lambda,B}^{(r,J_*)}
                         +\mathcal P_{\Lambda,B}.\tag{23}
\]

Both product channels remain exact, including every divisor-product
and block/complement term. Thus (21) is also the complete dual
transformation error. A separate analytical product transformation may
be added only with its own proved remainder.

## 7. Comparison with the physical payment scale

Since \(\log N=\kappa/(2t)+o(1)\), (14) gives

\[
(Nw_N)^2\asymp N^{1-\kappa/4}.\tag{24}
\]

For \(J_*=\lceil N^\alpha\rceil\), bounded duals therefore satisfy

\[
|\mathcal K_{\Lambda,B}
  -\widetilde{\mathcal K}_{\Lambda,B}^{(r,J_*)}|
 =O_r\left(N^{1-\kappa/4-(2r+1)\alpha}\right).\tag{25}
\]

The remainder is uniformly \(o(1)\) for
\((2r+1)\alpha>3/4\). At the stronger choice
\(\alpha=1/(2r+1)\), it is \(O_r(N^{-\kappa/4})\).
For any fixed \(0<\delta<2r\), taking
\(\alpha=(1+\delta)/(2r+1)<1\) gives

\[
O_r(N^{-\kappa/4-\delta})
       =o(N^{-\kappa/4}),\tag{26}
\]

uniformly. This is smaller than the displayed physical upper-budget
scale

\[
L^4e^{-\kappa^2/(8t)}+L^6e^{-2\mathfrak b/t}
\asymp L^4N^{-\kappa/4}
       +L^6N^{-(\kappa+4)/4},\qquad
\mathfrak b=\kappa(\kappa+4)/16.\tag{27}
\]

This compares with an **upper-budget scale**, not a positive lower
bound for the actual measured physical error. For \(r=1\),
\(J_*=\lceil N^{1/3}\rceil\) already gives a uniform vanishing
remainder and the same \(N\) power as the first term in (27), without
its \(L^4\) factor. For \(r=2\), \(J_*=\lceil N^{1/5}\rceil\)
does the same. Increasing a fixed order reduces the common-factor
range that must remain exact; its order-dependent constants are
retained in (21).

If dual parameters grow with \(N\), their factor \(\mathfrak M\)
must remain in (21)–(26); no free choice of large dual coefficients is
permitted. Their one-sided candidate payment remains in addition.

## 8. What this transformation does and does not resolve

This is more than the earlier exact regrouping: it replaces every large
common-factor coefficient by explicit integrals and boundary corrections,
with a uniformly vanishing global error on the same sector and a stated
comparison to the available physical upper-budget scale.
It is a fully analytical coefficient transformation, with no sampled
height, grid optimizer, or new numerical certificate.

Its scoped limitation is structural. Along \(n=ja,m=jb\), the ratio
phase is

\[
T\log(n/m)=T\log(a/b),\tag{28}
\]

which is independent of \(j\). Smoothing the common factor introduces
no ratio-phase cancellation by itself. A strictly negative full dual
bound still requires signed summation of the outer coprime ratio
frequencies jointly with the actual product phases, conditional on the
two true candidate coordinates. In particular every primitive pair
\((n,m)=1\) lies in the exact \(j=1\) part, and all pairs with
\(\gcd(n,m)\le J_*\) remain there. Those terms cannot be declared a
small discarded tail.

Starting the same absolute remainder estimate at a fixed \(J_*\)
gives \(O_r((Nw_N)^2)\), an exponentially growing available upper
bound. That failure of the bound is not a lower bound on the true
remainder and is not a no-go theorem for signed use of its periodic
Bernoulli integrals. The theorem instead states precisely how a growing
common-factor cutoff makes an absolute transformation error harmless
while isolating the unresolved primitive/small-common-factor correlation.

The new sufficient signed criterion would be

\[
\widetilde{\mathcal K}_{\Lambda,B}^{(r,J_*)}
 +C_r\mathfrak M(Nw_N)^2J_*^{-2r-1}
 +\Pi^-_{\Lambda,B}
 +\widehat\Delta/(4c^6)<0,\tag{29}
\]

or its higher-Schur replacement for the holomorphic part, with the same
dual parameters in the estimate and in the payment. Formula (29) is a
criterion, not an established inequality. Physical amplitude/frequency
Bell residuals, the exact normalizer, higher multiplicity, complementary
parameter coverage, and the small-time endpoint remain the obligations
of the original investigation.

## 9. Three scoped structural checks

### 9.1 A macroscopically large primitive coefficient sector survives

For zero dual parameters and the **original** base threshold normalizer
\(\Gamma=\gamma/c^2=O(x^{-2})\), the unsmoothed primitive part has
a positive coefficient envelope of order \((Nw_N)^2\). This is a
statement about coefficients before the actual signed phases are applied.
It is not asserted for the density-strengthened normalizer in Section 10.

Take ordered coprime pairs
\(N/2<a,b\le3N/4\). Here \(J_{a,b}=1\), so their entire ratio
coefficient is the exact \(j=1\) term. For small time,
\(\rho_a,\rho_b\le-a_0\), with for example
\(a_0=\tfrac12\log(4/3)>0\). The prescribed weights satisfy
\(w_a,w_b\ge w_N\) because (16) has \(c_\sigma>0\).
For the base threshold kernel,

\[
D_c(a,b)=\frac{\rho_a^2\rho_b^2}{8}
       \{5(\rho_a+\rho_b)^2+(\rho_a-\rho_b)^2\}
                 -\frac\Gamma2\rho_a^2\rho_b^2.\tag{30}
\]

The actual \(\Gamma=O(x^{-2})\) is eventually at most \(a_0^2\).
Consequently (30) is at least \(2a_0^6\).

The number of these pairs is

\[
\begin{split}
\sum_{d\le3N/4}\mu_{\rm Mob}(d)
 \left(\left\lfloor\frac{3N}{4d}\right\rfloor
       -\left\lfloor\frac N{2d}\right\rfloor\right)^2
 &=\frac{N^2}{16\zeta(2)}+O(N\log N).
\end{split}\tag{31}
\]

Indeed the parenthesis is \(N/(4d)+O(1)\), the summed cross error
is \(O(N\log N)\), the squared error is \(O(N)\), and the tail
of the absolutely convergent series
\(\sum\mu_{\rm Mob}(d)/d^2=1/\zeta(2)\) contributes \(O(N)\).
Thus these exact primitive coefficients alone have mass at least
\(c(Nw_N)^2\). The reverse upper bound follows from the complete
centered moment estimate. Their coefficient envelope is therefore
\(\Theta((Nw_N)^2)\), uniformly as time tends to zero.

This is **not** a lower bound for the signed ratio channel, which may
cancel through \(\cos(T\log(a/b))\), and is not a lower bound for
an arbitrary dual's primitive coefficients. It proves that the base
primitive sector cannot be omitted as a small absolute tail.

### 9.2 The complete sixth-degree product kernel cannot be removed by a dual

In \(h=\rho_n+\rho_m\), \(\delta=\rho_n-\rho_m\), the base
homogeneous degree-six coefficients are

\[
D_c^{[6]}=\frac{(h^2-\delta^2)^2(5h^2+\delta^2)}{128},\qquad
P_c^{[6]}=\frac{(h^2-\delta^2)^2(h^2+5\delta^2)}{128}.\tag{32}
\]

Their \(h^6\) coefficients are respectively \(5/128\) and
\(1/128\). Every candidate-null dual addition has degree at most five:
each lower feature has degree at most one and each upper feature at most
four. The \(\Gamma\) term has degree four. Both sine kernels from
the dual have degree at most five. Therefore no selection of
\(\Lambda,B\) can identically annihilate either complete sixth-degree
cosine kernel as a polynomial. Large dual coefficients do not change
this degree argument, though they may cancel values on a particular
restricted arithmetic state and then incur their candidate payment.

This prohibits a proposed exact kernel elimination, not a useful signed
bound or cancellation after summation.

### 9.3 The same absolute derivative method loses the product oscillation

If one applies the common-factor grouping to the product channel as well,
its phase is

\[
e^{i(2\theta_t+T\log(ab))}u^{2iT}.\tag{33}
\]

The recurrence (10) then acquires \(+2iT\) in its linear factor.
An absolute \(2r\)-derivative envelope has the extra factor
\((1+|T|)^{2r}\). The same proof as (21) gives only

\[
C_r\mathfrak M(1+|T|)^{2r}(Nw_N)^2J_*^{-2r-1}.\tag{34}
\]

For the physical height, \(|T|\asymp N^2\). Even at the largest
nontrivial power scale \(J_*\asymp N\), the expression in (34)
has size \(N^{2r-\kappa/4}\), which grows for every fixed
\(r\ge1\) on the stated interval. Taking \(J_*=N\) removes the
tail entirely and retains everything exact, so it furnishes no smoothing
gain. This diagnoses the loss of the specified absolute derivative
envelope; it is not a lower bound on the actual oscillatory remainder.
An oscillation-preserving transformation of the product phase needs an
additional method, such as the proposed complete stationary-phase or
divisor summation analysis. Formula (23) leaves that phase exact.

## 10. The density-strengthened threshold and its recalculated payment

[Heat Note 21](../../notes/21_DEFLATED_LOCAL_GROWTH_AND_THRESHOLD_MULTIPLICITY_20261010.md)
uses the imported uniform counting theorem
\[
|N_\tau(R)-p_\tau(R)|\le C_{\rm count}\log(2+R),
\quad 0<\tau\le1/2,\quad R\ge4\pi,
\]
where \(\tau\) is the heat-time parameter, distinct from the actual
arithmetic frequency \(T\), and \(C_{\rm count}\ge0\) is an
absolute symbolic constant. Set
\[
D_0=8\pi(4C_{\rm count}+1),\qquad
X_0=\max\{(4\pi)^2,2D_0,3\}.
\]
At an actual all-real threshold collision with \(x\ge X_0\), its
counting block gives the strengthened necessary condition
\[
2q_3^2-3q_2q_4-\gamma_{\rm count}q_2^2\ge0,
\qquad
\gamma_{\rm count}=\gamma+\frac{9\log x}{2D_0^2}.
\tag{35}
\]
The coefficient is defined at every physical center; the implication in
(35) uses the all-real threshold hypothesis and the genuine zero count.
The complete derivation and higher-multiplicity extension are in the
linked note. The count theorem is the imported
[Polymath Theorem 1.5(iv)](https://arxiv.org/html/1904.12438v2#S1).

To use (35) in the present complete dual, replace \(\Gamma\) everywhere
in its fixed block by
\[
\Gamma_{\rm count}=\gamma_{\rm count}/c^2=O(L).
\tag{36}
\]
The smoothing proof still applies, because it already retains the factor
\(\mathfrak M\). For bounded \(\Lambda,B\), the modified fixed block
gives \(\mathfrak M=O(L)\). With \(r=1\) and
\(J_*=\lceil N^{2/5}\rceil\), equation (21) therefore gives
\[
|R|=O\left(LN^{-\kappa/4-1/5}\right)
                       =o(N^{-\kappa/4})
\tag{37}
\]
uniformly on the closed \(\kappa\) interval. In particular the
density-strengthened normalizer does not destroy the vanishing
common-factor transformation error. The general theorem may also track
any additional growth of the selected dual parameters.

The physical threshold perturbation payment must be recomputed with
\(\gamma_{\rm count}\); the measured old
\(\widehat\Delta\) cannot automatically be reused. For the genuine
leading centered jets \(g_2,g_3,g_4\), keep the complete
\(\widehat\delta_j=j!L^j\eta_N+E_j\) of project 09 Note 2 and set
\[
\begin{split}
\widehat\Delta_{\rm count}={}&
4|g_3|\widehat\delta_3+2\widehat\delta_3^2\\
&+3\bigl(|g_2|\widehat\delta_4
         +|g_4|\widehat\delta_2
         +\widehat\delta_2\widehat\delta_4\bigr)\\
&+|\gamma_{\rm count}|
            \bigl(2|g_2|\widehat\delta_2
                        +\widehat\delta_2^2\bigr).
\end{split}\tag{38}
\]
Equivalently, if \(s=\gamma_{\rm count}-\gamma
=9\log x/(2D_0^2)\ge0\), then the triangle inequality gives
\[
\widehat\Delta_{\rm count}\le\widehat\Delta
       +s\bigl(2|g_2|\widehat\delta_2+\widehat\delta_2^2\bigr).
\tag{38a}
\]
Its original derivative and residual bounds give the still-admissible
upper-budget scale
\[
\widehat\Delta_{\rm count}
=O\left(L^4N^{-\kappa/4}+L^6N^{-(\kappa+4)/4}\right)=o(1).
\tag{39}
\]
To check the extra normalizer terms, use
\(g_2=O(e^{\mathfrak a/t})\),
\(\widehat\delta_2=O(L^2e^{-\mathfrak b/t}+e^{\mathfrak a/t}/x)\),
and \(\gamma_{\rm count}=O(L)\). Their new upper bounds are
\(O(L^3N^{-\kappa/4})\) and
\(O(L^5N^{-(\kappa+4)/4})\), together with smaller powers of
\(L\) at the latter \(N\) exponent, and are absorbed by (39).
This remains a comparison to an **upper-budget scale**, not a lower
bound for the measured physical error.

Accordingly, the strengthened signed criterion uses the transformed
\(\Gamma_{\rm count}\) dual and the same one-sided payment parameters:
\[
\widetilde{\mathcal K}_{\Lambda,B,\rm count}^{(r,J_*)}
 +C_r\mathfrak M_{\rm count}(Nw_N)^2J_*^{-2r-1}
 +\Pi^-_{\Lambda,B}
 +\widehat\Delta_{\rm count}/(4c^6)<0.
\tag{40}
\]
[Heat Note 20](../../notes/20_ANALYTIC_SCHUR_CONES_AND_DENSITY_STRENGTHENED_THRESHOLDS_20261010.md)
gives analytical Schur sufficient cones for the full holomorphic part;
the separate physical Bell residuals still require their own payments.
Neither (40) nor membership of the prescribed jets in those cones is
proved here. The base primitive coefficient lower bound in Section 9.1
was specifically for the original small \(\Gamma=O(x^{-2})\); it is
not asserted unchanged for the density-strengthened kernel.

## 11. Review items

The identities and bounds above are proved in text. A meaningful
independent mathematical review should check: the difference-sine
orientation in (1); the floor partition (5); the sign of the periodic
Bernoulli remainder (8); the weight derivative recurrence (10); the
uniform centered moment bound at \(a=1\) and \(u\) near \(N\); and
the conversion of the physical budget to the \(N\) powers in (27).
No finite numerical sweep is part of those proof steps.
