# A power bound for the nonsquarefree tail and a squarefree residual

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
The derivation and separate same-model audits are internal mathematical
checks, not independent specialist validation or formal proof replay.

## Result and its scope

There is a proved power bound for the **entire nonsquarefree total-product
sector** of the adaptive tail, under the manuscript's existing analytic
inputs. Write

\[
 B(D,H)=H+DH^{1/6}+H^{5/6}D^{1/3}+H^{1/3}D^{5/6}.
\]

For each fixed \(0<\theta<1\), zero-integral annular profile, and
\(1\le H\le D\), the sector has normalized weighted energy

\[
 \boxed{\mathcal E_{\mathrm{nsq}}^{(\theta)}(D,H)
 \ll_{\varepsilon,\theta,W,\Phi}
 D^\varepsilon\min\{HD^{1-\theta},D^{-\theta/2}B(D,H)\}.}
 \tag{1}
\]

The first bound uses the existing free-character completion and elementary
ideal counting. The second additionally uses the already imported physical
sextic operator on arbitrary sixth-power-free columns. It handles the
row-dependent cutoff through fixed-interval maximal partial sums.

At \(H=D^{2/5}\) and **\(\theta=11/20\)**, (1) gives

\[
 \mathcal E_{\mathrm{nsq}}^{(11/20)}(D,D^{2/5})
 \ll_\varepsilon D^{19/24+\varepsilon},
 \qquad \frac45-\frac{19}{24}=\frac1{120}>0.
 \tag{2}
\]

Thus this sector is affordable in the proposed \(D^{4/5+\varepsilon}\)
moment budget. The remaining tail can be restricted to squarefree total
products, equivalently squarefree pairwise-coprime factors, with a proved
error bound. **The moment of that remaining signed response is still open.**
There is no new full-moment exponent or zero-free boundary.

The cutoff in (2) differs from the \(\theta=1/40\) packet geometry in
note 15. The two projected sectors must not be treated as bounds for one
unchanged tail. The full response vectors at the two cutoffs are close,
but their projections need not be. This tradeoff is discussed below.

## 1. Definitions and retained inputs

Use the good ideal monoid, complex completely multiplicative zero-extended
\(\lambda_u\), \(z=\sqrt{CD}\), and \(c_z=m_z*m_z\) from the manuscript.
Fix \(W\) supported on \([c,C]\) with \(\int W=0\), and put

\[
 S_u(X)=\sum_m\lambda_u(m)W(Nm/X),\qquad
 Y_u^{(\theta)}=D^{1-\theta}/L_u,
\]
\[
 I_u^{(\theta)}=-\sum_{Nd\le Y_u^{(\theta)}}c_z(d)\lambda_u(d)S_u(D/Nd),
 \qquad
 T_u^{(\theta)}=-\sum_{Nd>Y_u^{(\theta)}}c_z(d)\lambda_u(d)S_u(D/Nd).
 \tag{3}
\]

On the profile, for sufficiently large \(D\), the exact factorization is
\(A_{u,W}=I_u^{(\theta)}+T_u^{(\theta)}\). The retained inputs are

\[
 |S_u(X)|\ll_{A,W}\tau(E_u)\sqrt{Q_u}(L_u/X)^A,
 \qquad
 \sum_{u\ne0}\Phi(Nu/H)\frac{\tau(E_u)^2Q_u}{L_u^2}
 \ll_\delta H^\delta,
 \tag{4}
\]

and, for every fixed coefficient vector on sixth-power-free good ideals
\(Nn\le X\),

\[
 \sum_{u\ne0}\Phi(Nu/H)\left|\sum_n b_n\chi_n(u)\right|^2
 \ll_\eta(HX)^\eta B(X,H)\sum_n|b_n|^2.
 \tag{5}
\]

These are the manuscript's all-scale masked completion, radical-weighted
row mass, and physical-operator corollary. The deep Poisson and de Faveri
sieve inputs retain their explicitly imported status. No new Möbius PNT,
Hecke zero-free strip or conductor-uniform reciprocal estimate is assumed.
The proof also uses ideal/lattice counting and the divisor bounds.

Define projection by total ideal: for example,

\[
 I_{u,\mathrm{nsq}}^{(\theta)}=
 -\sum_{\substack{d,m\\Nd\le Y_u^{(\theta)}\\dm\ \mathrm{nonsquarefree}}}
 c_z(d)\lambda_u(dm)W(N(dm)/D),
 \tag{6}
\]

with the analogous \(T_{u,\mathrm{nsq}}^{(\theta)}\). Since the original
Möbius coefficient is zero on every nonsquarefree ideal,

\[
 \boxed{T_{u,\mathrm{nsq}}^{(\theta)}
       =-I_{u,\mathrm{nsq}}^{(\theta)}}
 \tag{7}
\]

pointwise in the actual physical row. Finally,

\[
 \mathcal E_{\mathrm{nsq}}^{(\theta)}(D,H)=
 D^{-1}\sum_{u\ne0}\Phi(Nu/H)|T_{u,\mathrm{nsq}}^{(\theta)}|^2.
 \tag{8}
\]

## 2. Square-divisor projection at small square roots

The finite divisor identity

\[
 \mathbf1_{n\ \mathrm{nonsquarefree}}
 =-\sum_{\substack{k^2\mid n\\k\ne1}}\mu_K(k)
 \tag{9}
\]

is valid for every ideal. Only squarefree \(k\) have nonzero weight.
Choose \(R=D^\rho\), with \(0<2\rho<\theta\), and split (9) at
\(Nk\le R\), equality included on the small side.

For fixed \(d,k\), let

\[
 j(d,k)=k^2/(k^2,d).
 \tag{10}
\]

Ideal valuations give \(k^2\mid dm\iff j(d,k)\mid m\), and
\(Nj(d,k)\le (Nk)^2\). Complete multiplicativity, including every zero,
therefore gives exactly

\[
 \sum_{m:k^2\mid dm}\lambda_u(m)W(N(dm)/D)
 =\lambda_u(j(d,k))S_u\!\left(\frac D{Nd\,Nj(d,k)}\right).
 \tag{11}
\]

There is no coprimality assumption on \(d,k,j\). For \(Nd\le Y_u\)
and \(Nk\le R\), the completion ratio is at most

\[
 \frac{L_uNd\,Nj}{D}\le D^{-\theta}R^2.
 \tag{12}
\]

Let \(J_{u,\le R}\) denote the small-\(k\) contribution to (6),
with the signs from (9). If \(Y_u<1\) it is empty. Otherwise
\(\sum_{Nd\le Y_u}|c_z(d)|\ll Y_u\log(2Y_u)\) and
\(\#\{k:Nk\le R\}\ll R\), so (4) and (11) imply

\[
 |J_{u,\le R}|
 \ll_{A,W}
 R D^{1-\theta}\log(2D)
 \frac{\tau(E_u)\sqrt{Q_u}}{L_u}
 (D^{-\theta}R^2)^A.
 \tag{13}
\]

Consequently

\[
 D^{-1}\sum_{u\ne0}\Phi(Nu/H)|J_{u,\le R}|^2
 \ll_{A,\delta,W,\Phi}
 D^{1-2\theta}R^2\log^2(2D)H^\delta
 (D^{-\theta}R^2)^{2A}.
 \tag{14}
\]

For fixed \(\theta-2\rho>0\), this has arbitrary power decay for
\(1\le H\le D\). The decay is a deduction from (4), not a finite
numerical observation.

## 3. The elementary large-square bound

Write

\[
 w_R(n)=-\sum_{\substack{k^2\mid n\\Nk>R}}\mu_K(k),\qquad
 v_Y(n)=-\sum_{\substack{d\mid n\\Nd\le Y}}c_z(d).
 \tag{15}
\]

The remaining contribution to (6) is

\[
 J_{u,>R}=\sum_n w_R(n)v_{Y_u}(n)\lambda_u(n)W(Nn/D).
 \tag{16}
\]

The divisor bound gives \(|v_Y(n)|\le\tau_3(n)\ll_\eta (Nn)^\eta\),
uniformly in \(Y\), and
\(|w_R(n)|\le\sum_{Nk>R,k^2\mid n}1\). Ideal counting yields

\[
 |J_{u,>R}|
 \ll_{\eta,W}
 D^\eta\sum_{Nk>R}\#\{m:N(k^2m)\le CD\}
 \ll_{\eta,W}D^{1+\eta}/R,
 \tag{17}
\]

since \(\sum_{Nk>R}(Nk)^{-2}\ll1/R\). The complete row weight
has mass \(O_\Phi(H)\), hence

\[
 D^{-1}\sum_{u\ne0}\Phi(Nu/H)|J_{u,>R}|^2
 \ll_{\eta,W,\Phi}HD^{1+2\eta}/R^2.
 \tag{18}
\]

## 4. A sparse-column bound retaining the adaptive selector

A better bound is available for (16) from (5). The selector \(Nd\le Y_u\)
is handled by a maximal prefix in the **divisor index**, not inserted into
a completed row kernel.

Order the good ideals \(d\) with \(Nd\le CD\) by norm, breaking ties
once and for all. Every actual \(Nd\le Y_u\) set is a prefix in this
ordering. A binary partition of these indices expresses every prefix
as at most \(O(\log D)\) fixed intervals. Cauchy gives the corresponding
maximal bound by \(O(\log D)\) times the sum of squares over all tree
intervals. There are \(O(\log D)\) partition levels.

To apply the sixth-power-free column operator, uniquely write

\[
 n=\ell^6 n_0,\qquad n_0\ \text{sixth-power-free},
 \qquad X_\ell=CD/(N\ell)^6.
 \tag{19}
\]

For a fixed interval \(\mathcal J\), its coefficient vector is

\[
 b_{\mathcal J,\ell}(n_0)=
 w_R(\ell^6n_0)\nu(\ell^6n_0)W(N(\ell^6n_0)/D)
 \sum_{\substack{d\mid\ell^6n_0\\d\in\mathcal J}}c_z(d).
 \tag{20}
\]

The physical character factors as
\(\chi_{\ell^6n_0}(u)=\mathbf1_{(u,\ell)=1}\chi_{n_0}(u)\).
For each \(\ell\), its common row mask is retained and then removed
only by enlargement of a nonnegative sum of squares. Thus (5) applies
to the fixed vector (20).

There is useful sparsity after this decomposition. If
\(w_R(\ell^6n_0)\ne0\), there is a **squarefree** \(k\) with
\(Nk>R\) and \(k^2\mid\ell^6n_0\). Put \(g=(k,\ell)\) and
\(k_2=k/g\). Since \(k\) is squarefree,

\[
 k_2^2\mid n_0,\qquad Nk_2>R/N\ell.
 \tag{21}
\]

The number of possible \(n_0\), \(Nn_0\le X_\ell\), is therefore

\[
 \ll X_\ell\min\{1,N\ell/R\}.
 \tag{22}
\]

For \(R/N\ell\ge1\), sum ideal counts over square divisors as in
(17); otherwise use the unrestricted count \(O(X_\ell)\).

On any one partition level the intervals are disjoint in \(d\), and

\[
 \sum_{\mathcal J}
 \left|\sum_{d\mid n,\ d\in\mathcal J}c_z(d)\right|^2
 \le\left(\sum_{d\mid n}|c_z(d)|\right)^2
 \le\tau_3(n)^2.
 \tag{23}
\]

Since \(|w_R(n)|\le\tau(n)\), divisor bounds, (22), and (23) give
the summed coefficient squared norm on this level as

\[
 \sum_{\mathcal J}\|b_{\mathcal J,\ell}\|_2^2
 \ll_{\eta,W}D^\eta X_\ell\min\{1,N\ell/R\}.
 \tag{24}
\]

Apply (5), then the maximal-prefix inequality and sum partition levels.
This bounds the \(\ell\)-channel, with any row cutoff, by the right
side of (24) times \(D^\eta B(X_\ell,H)\), after absorbing logarithms
into a smaller preliminary epsilon.

Finally, weighted Cauchy in \(\ell\) uses
\(\sum_\ell(N\ell)^{-2}<\infty\). After normalization by \(D\),
the bound is

\[
 \begin{aligned}
 D^{-1}\sum_u\Phi(Nu/H)|J_{u,>R}|^2
 &\ll_\eta D^\eta
 \sum_\ell (N\ell)^{-4}\min\{1,N\ell/R\}B(X_\ell,H)\\
 &\ll_\eta \frac{D^\eta}{R}B(D,H)
             \sum_\ell(N\ell)^{-3}\\
 &\ll_\eta D^\eta B(D,H)/R.
 \end{aligned}
 \tag{25}
\]

Only \(X_\ell\ge1\) can contribute. The second line uses
\(\min\{1,N\ell/R\}\le N\ell/R\) and monotonicity of the
operator factor, absorbing the fixed support constant \(C\).
The finite-order twist in (20) has modulus at most one.

This proof permits overlapping divisors and arbitrary nonsquarefree
total ideals. It does not apply (5) directly to an unsupported all-ideal
column class, or apply it to a row-dependent vector. Each vector (20) is
fixed before the operator is used.

## 5. The sector theorem and the new residual

Choose \(\rho=\theta/2-\kappa\), with fixed
\(0<\kappa<\theta/2\). Equations (7), (14), (18), and (25) give

\[
 \mathcal E_{\mathrm{nsq}}^{(\theta)}
 \ll_\eta D^\eta
 \min\{HD^{1-\theta+2\kappa},D^{-\theta/2+\kappa}B(D,H)\}
 +O_N(D^{-N}).
 \tag{26}
\]

For each requested \(\varepsilon>0\), choose \(\kappa\) and the
preliminary divisor/operator epsilons sufficiently small in terms of
\(\varepsilon,\theta\). Choose the completion order afterwards.
This proves (1). The two large-square bounds are independent estimates
of the same vector, so their minimum is legitimate.

At \(H=D^{2/5}\), the four powers in \(B(D,H)\) are

\[
 \frac25,\qquad\frac{16}{15},\qquad\frac23,
 \qquad\frac{29}{30}.
 \tag{27}
\]

Thus \(\theta=11/20\) gives the exponent
\(16/15-11/40=19/24\) in (2). The elementary bound alone gives
\(17/20\), which would exceed the target. The sparse-column step is
essential for affordability at this particular cutoff.

Let \(T_{u,\mathrm{sf}}^{(\theta)}\) retain only squarefree total ideals.
At this cutoff,

\[
 \mathfrak M_W(D,D^{2/5})\ll_\varepsilon D^{4/5+\varepsilon}
 \quad\Longleftrightarrow\quad
 D^{-1}\sum_{u\ne0}\Phi(Nu/D^{2/5})
 |T_{u,\mathrm{sf}}^{(11/20)}|^2
 \ll_\varepsilon D^{4/5+\varepsilon}.
 \tag{28}
\]

Indeed the original full moment and each zero-integral adaptive tail
moment are equivalent by the manuscript's negligible small-sector
theorem, and (2) makes the nonsquarefree vector affordable in either
direction of the weighted triangle inequality.

In the retained factorization, squarefreeness of \(n=abm\) forces
\(a,b,m\) squarefree and pairwise coprime. This is now a justified
restriction **with an explicit error budget**. It was not permissible
to insert these restrictions into the original exact identity.
After the restriction, the \(m\)-sum is no longer free; the original
free-character completion cannot be reapplied to it unchanged.

Since \(Y_u^{(11/20)}\le D^{9/20}<z\), a second exact form of the
remaining coefficient is

\[
 T_{u,\mathrm{sf}}^{(11/20)}=
 \sum_{n\ \mathrm{squarefree}}
 \left[\mu_K(n)+
       \sum_{\substack{d\mid n\\Nd\le D^{9/20}/L_u}}(-2)^{\omega(d)}\right]
 \lambda_u(n)W(Nn/D).
 \tag{29}
\]

For \(Y_u<1\) the inner sum is empty. Formula (29) follows from
the inverse coefficient identity in note 15 and
\(c_z(d)=(-2)^{\omega(d)}\) for squarefree \(d\) with \(Nd\le z\).
It supplies a short-divisor formulation of the remaining signed estimate;
it does not estimate that sum.

## 6. The cutoff tradeoff and what is still missing

The smaller cutoff buffer \(\theta=1/40\) gives much shorter free
factors on coherent rows and supports the packet geometry of note 15.
Equation (1) there still improves the nonsquarefree-sector generic power
by \(1/80\), giving \(D^{253/240+\varepsilon}\) at \(h=2/5\),
but that is not affordable at \(D^{4/5+\varepsilon}\).
The new \(\theta=11/20\) buys complete squarefree reduction at the
cost of a longer free factor and weaker balanced-factor support.

Unlike \(\theta=13/20\), which already makes the elementary bound
affordable, \(\theta=11/20<1-h\) keeps the unit term outside the
significant row range. If \(Y_u<1\), the existing \(L_u\ll Nu\)
comparison requires \(Nu\gg D^{9/20}\), above \(H=D^{2/5}\) by
a fixed power; its full weighted contribution is negligible by Schwartz
decay and an elementary uniform amplitude bound.

For zero-integral profiles, the full vectors
\(T_u^{(\theta_1)}-T_u^{(\theta_2)}
=I_u^{(\theta_2)}-I_u^{(\theta_1)}\) have arbitrary-power small
weighted energy at any two fixed positive buffers. That statement does
not transfer to a product projection: such a projection can destroy the
small-sector cancellation. Accordingly the new squarefree residual in
(28) uses its own stated cutoff and does not silently combine packet
projections from two different representations.

Squarefree products have no repeated-prime involution to exploit. Balanced
semiprimes still have a nonzero coefficient (now \(+2\) when
\(1\le Y_u<\min(Nq,Nr)\)); rough squarefree products of more factors
also survive. Their signed compensation across total ideals is the
unproved task in (28)--(29). The new bound is for the nonsquarefree
sector alone, and proves no smaller exponent for the complete moment.

## 7. Verification

The companion exact checker tests square-divisor projection, overlapping
ideal gcds, the scaled free sum, complex phases and deletion zeros,
adaptive endpoints, sixth-power decomposition and sparse support, binary
prefix regrouping, and the rational power budgets. Its finite model does
not certify Poisson, the imported generic sieve, Euler convergence,
Schwartz decay or an asymptotic signed moment. Those inputs and analytic
deductions are stated and proved separately above.

See the [manuscript](../short_family_reductions.tex),
[completion and adaptive reduction](11_SHORT_FAMILY_MEAN_ZERO_ADAPTIVE_REDUCTION_20261008.md),
[physical generic sieve](6_SHORT_FAMILY_SEXTIC_SIEVE_BARRIER_20261008.md),
[checker](../../numerics/check_short_family_squarefree_projection.py),
[retained record](../../numerics/short_family_squarefree_projection_record_20261008.json),
and [scoped review](../../reviews/SHORT_FAMILY_SQUAREFREE_AND_COFACTOR_REVIEW_20261008.md).
No large derived dataset is required.
