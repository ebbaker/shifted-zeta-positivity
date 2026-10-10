# Coherent covariance requirements and a finite signed cofactor-span barrier

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Status: a new finite-span obstruction under the existing fixed-field prime
ideal theorem, and exact necessary covariance bounds for the full response.
These are internal deductions and finite checks, not independent specialist
validation. No bound for the full short-family moment is proved.

The [comparative review](../../reviews/COMPARATIVE_RESEARCH_DIRECTION_REVIEW_20261009.md)
asks whether broader signed compensation could repair the complete block
in [Note 24](24_SHORT_FAMILY_FINITE_COFACTOR_PAIRING_20261008.md).
This note tests two precise possibilities. Any fixed finite signed linear
combination of those blocks that remains nonzero on coherent rows still
has energy exponent \(16/15\). Canceling its first main term only improves
a logarithm. Compensation by the remaining products is possible, but its
coherent-row mean must match the block to relative power \(D^{-2/15}\),
and its row variance must independently fit the \(D^{4/5}\) target.
This strengthens the reason to require a broader covariance mechanism
before promoting this program above mixed correlations.

## 1. The precise coherent projection

Keep the good ideal monoid, trivial permitted fixed twist \(\nu=1\),
physical deletion zeros, \(H=D^{2/5}\), \(z=\sqrt{CD}\),
\(Y_u=D^{9/20}/L_u\), and the actual squarefree response
\(T_{u,\mathrm{sf}}\) of Notes 24--25. Fix a squarefree good ideal \(M\)
and a nonzero fixed complex profile \(W\) of zero integral on \([c,C]\).
Let \(\mathcal B_{u,M}\) be Note 24's actual total-product projection.
On
\[
 \mathcal C_M(D)=\{u=v^6:0<Nv\le D^{1/15},\ (v,M)=1\},
 \qquad w_u=D^{-1}\Phi(Nu/H),
\]
with duplicate sixth-power images counted once, that note proves exactly
\[
 \mathcal B_{u,M}=P_M(D),\qquad
 |P_M(D)|\gg_{M,W}D/(\log D)^{k_0+1},
 \qquad m_M:=\sum_{u\in\mathcal C_M}w_u\asymp_{M,\Phi}D^{-14/15}.
 \tag{1}
\]
Here \(k_0\ge1\) is the first nonzero moment
\(M_j(W)=\int W(t)\log(C/t)^j\,dt\). The weighted count follows
from the same lattice count and \(1\le\Phi\ll1\) on this inner ball.
All statements below concern this actual row restriction. Other rows
are not removed from the desired full moment.

Write \(R_u=T_{u,\mathrm{sf}}-\mathcal B_{u,M}\), and set
\[
 \bar R=m_M^{-1}\sum_{\mathcal C_M}w_uR_u,
 \quad V_R=\sum_{\mathcal C_M}w_u|R_u-\bar R|^2,
 \quad A=m_M|P_M(D)|^2.
\]
The exact orthogonal decomposition is
\[
 \boxed{\sum_{\mathcal C_M}w_u|T_{u,\mathrm{sf}}|^2
       =m_M|P_M(D)+\bar R|^2+V_R.}                 \tag{2}
\]
No total-product cross term is deleted: it supplies the term
\(2m_M\Re(P_M\overline{\bar R})\) in the first square. Row variation
of \(R\) is orthogonal to the constant coherent block and cannot be
canceled by it.

Consequently, if the desired full squarefree energy is at most
\(Q_D=C_\varepsilon D^{4/5+\varepsilon}\), then, necessarily,
\[
 \left|\frac{\bar R}{P_M}+1\right|\le\sqrt{Q_D/A},\qquad
 V_R\le Q_D,\qquad
 \frac{Q_D}{A}\ll_{M,W,\varepsilon}
      D^{-4/15+\varepsilon}(\log D)^{2k_0+2}.       \tag{3}
\]
For every fixed \(0<\varepsilon<4/15\), the required relative mean
accuracy tends to zero with a power. This is more demanding than a
negative sign or a fixed negative correlation.

An equivalent necessary angle statement is useful for proposed norm
estimates. In the weighted space on \(\mathcal C_M\), let
\(b=(P_M)_u\), \(r=(R_u)_u\), \(C_R=\|r\|^2\),
\(x=\sqrt{C_R/A}\), and
\(\gamma=\Re\langle b,r\rangle/\sqrt{AC_R}\) when \(C_R>0\).
If \(q=Q_D/A<1\), then \(C_R>0\) and
\[
 (x-1)^2+2x(1+\gamma)\le q,
 \quad |x-1|\le\sqrt q,
 \quad 1+\gamma\le\frac{q}{2(1-\sqrt q)}.          \tag{4}
\]
This follows by expanding \(\|b+r\|^2/A\), with Cauchy giving
\(-1\le\gamma\le1\). Thus the norm must match to relative order
\(D^{-2/15+\varepsilon/2}\) up to logarithms, and the normalized real
angle must approach \(-1\) to order \(D^{-4/15+\varepsilon}\).
Bounds on the two separate positive energies do not prove these facts.

The mean in (2) is an actual scalar arithmetic obligation. For every
squarefree total ideal \(n\) on the profile define
\[
 \beta_M(n)=m_M^{-1}\sum_{\mathcal C_M}w_u
         t_{Y_u}(n)\lambda_u(n),\qquad
 \bar T=\sum_n\beta_M(n)W(Nn/D)=P_M+\bar R.        \tag{5}
\]
Both the adaptive cutoff and deletion masks remain inside \(\beta_M\).
The corresponding variance is the quadratic form of the centered
coefficient vectors
\(t_{Y_u}(n)\lambda_u(n)-\beta_M(n)\). It is positive semidefinite
as a whole, with all column cross terms retained. A successful broader
compensation argument must bound this form as well as (5); proving only
the mean cancellation would leave \(V_R\) open.

## 2. Fixed finite signed combinations cannot save a power

The following goes beyond testing one complete block or positive sums.
Let \(M_1,\ldots,M_s\) be any fixed squarefree good ideals and
\(a_1,\ldots,a_s\in\mathbb C\) any fixed scalars. Form the signed
response
\[
 \mathcal L_u=\sum_{i=1}^s a_i\mathcal B_{u,M_i},
 \qquad M_* =\operatorname{rad}(M_1\cdots M_s).
\]
These are complete actual blocks; the scalars may have either sign.
The linear combination is a method test, not automatically a projection
of the full response with its original coefficients. On \(\mathcal C_{M_*}\)
define its finite grouped norm measure
\[
 c_m=\sum_{i=1}^s a_i\sum_{\substack{b\mid M_i\\Nb=m}}\mu_K(b),
 \qquad L_j=\sum_m\frac{c_m}{m}(\log m)^j.        \tag{6}
\]
Grouping by norm is essential: different prime ideals can share a norm.

**Proposition.** If some \(c_m\ne0\), let \(r_0\ge0\) be the
first index with \(L_{r_0}\ne0\). It exists, and is at most the number
of distinct norms in (6) minus one. With \(K=k_0+r_0\) and
\(B=\log z\),
\[
 \mathcal L_u=
 \frac{D\alpha_K\binom{K}{k_0}M_{k_0}(W)L_{r_0}}{B^{K+1}}
 +O_{M_*,a,W}(D/B^{K+2})
 +O_{M_*,a,W}(De^{-c\sqrt{\log D}}+D^{1/2}),     \tag{7}
\]
uniformly for \(u\in\mathcal C_{M_*}\), where
\(\alpha_k=\sum_{j=1}^k2^{-(k-j)}/j>0\). In particular,
\[
 \sum_u w_u|\mathcal L_u|^2
 \gg_{M_*,a,W,\Phi}D^{16/15}/(\log D)^{2K+2}.    \tag{8}
\]
If all \(c_m=0\), the combination is exactly zero on these coherent
rows for every sufficiently large \(D\).

**Proof.** Note 24's prime-pair continuum, with the original two prime
cutoffs and diagonal removal, gives
\[
 \mathcal L_u=D\sum_m\frac{c_m}{m}
       \int_c^CW(t)F_B(\log(C/t)+\log m)\,dt
       +O(De^{-c\sqrt{\log D}}+D^{1/2}).
\]
All ideals and scalars here are fixed, so every logarithmic shift is
bounded. The convergent expansion
\(F_B(v)=\sum_{k\ge1}\alpha_kv^k/B^{k+1}\) has uniform remainder
\(O(B^{-K-2})\) after order \(K\). Its coefficient at order \(k\) is
\[
 J_k=\sum_{j=0}^k\binom{k}{j}M_j(W)L_{k-j}.
\]
The vanishing conditions imply \(J_k=0\) for \(k<K\) and
\(J_K=\binom{K}{k_0}M_{k_0}L_{r_0}\ne0\). Distinct real numbers
\(\log m\) give an invertible finite Vandermonde matrix, proving the
existence and stated bound for \(r_0\). This proves (7). The same
coprime coherent-row count as (1), with fixed \(M_*\), proves (8).
If the grouped norm coefficients vanish, the exact prime-pair sums
cancel, not merely their continuum main terms: on the profile the two
large primes eventually exceed every prime of \(M_*\), so all their
exclusion conditions are automatic. \(\square\)

For a concrete subtraction take a fixed good prime ideal \(p\),
\(q=Np\), and
\[
 \mathcal L=\mathcal B_{\cdot,p}-(1-1/q)\mathcal B_{\cdot,1}.
\]
Then \(c_1=1/q\), \(c_q=-1\), \(L_0=0\), and
\(L_1=-\log q/q\ne0\). This cancels exactly the Euler-weighted
leading coefficient identified in Note 24. The first surviving order
is \(K=k_0+1\), and the energy still has power \(16/15\).
Thus even successful leading-mode subtraction among fixed cofactor
blocks does not meet the \(4/5\) target.

## 3. What this changes about the next checkpoint

Fixed finite cofactor compensation now has a proved limitation even
when its coefficients are signed and tuned to cancel the first main
term. A useful next result must involve scales or cofactors growing with
\(D\), broader product shapes such as the balanced triples of Note 25,
or a direct arithmetic bound for the actual mean and centered covariance
in (2)--(5). The proposition does not cover a growing number of blocks,
coefficients varying with \(D\), an identically zero coherent combination,
or cancellation with arbitrary remaining products. Those cases remain
possible and require their own complete budgets.

The squarefree target is still open; an individual block or finite-span
lower bound is not a lower bound for \(T_{u,\mathrm{sf}}\). The comparative
review's placement as the strongest alternative arithmetic lane therefore
continues to hold. Its promotion condition is more concrete: prove a
nonzero compensation estimate with the mean accuracy in (3), centered
variance at \(D^{4/5+\varepsilon}\), and the complementary row/product
energy paid. Another finite Euler-product pairing would not pass it.

The [new checker](../../numerics/check_short_quadratic_checkpoint.py)
verifies exact rational complex-vector covariance decompositions, signed
finite-measure moment convolution, norm grouping and the two-block
subtraction. Its [record](../../numerics/short_quadratic_checkpoint_record_20261009.json)
also verifies the rational exponent requirements. It does not certify
the fixed-field prime ideal theorem, lattice asymptotics, or an unbounded
moment. Those analytic inputs retain the source status of Notes 24--25;
no additional external arithmetic theorem is used here.

Two fresh runs reproduce the record byte for byte: 42,049 exact
assertions, including 224 covariance cases, 626 signed cofactor-span
cases, and 36 signed prime/power pair partitions. The spans include
distinct equal-norm prime symbols, exact norm-group cancellation, and
tuned combinations whose first nonzero logarithmic order is one or two.
