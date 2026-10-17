# Oscillatory blocks and paired Laguerre forms: threshold three

> **Chat-history routing update, 17 October 2026.** Current histories: [Chat 12 — Continue quaternion theta rewrite](../chat-histories/0012_2026-10-14T23-49-23Z_continue-quaternion-theta-rewrite.json), [Chat 11 — Summarize quaternion theta results](../chat-histories/0011_2026-10-14T22-15-11Z_summarize-quaternion-theta-results.json). Use this investigation’s [local registry](../chat-histories/index.json) and [relocation receipt](../CHAT_HISTORY_RELOCATION_20261017.json) for current numbers and preserved provenance; this supersedes the routing and numbering below. All future investigation 21 chats belong in this investigation’s `chat-histories/` folder.

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded parent model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**,
verified from the active turn metadata. Parallel analytic derivation and
independent internal LLM review used the inherited configuration. This is
research with internal review, not external peer review or formal verification.

This continues [Note 18](18_MANUSCRIPT_REWRITE_AND_CONTINUATION_20261014.md).
Oscillatory cancellation improves the sufficient asymptotic threshold from
four to three. The exact paired formulas below then specify the full
signed observation still needed in the remaining region. The companion
[Note 20](20_EXPLICIT_OUTER_HEIGHT_BOUND_20261014.md) makes the earlier
threshold-five region explicit. The [internal review](../reviews/14_OSCILLATORY_BLOCKS_AND_EXPLICIT_HEIGHT_REVIEW_20261014.md)
checks these distinct scopes.

## Main result

Use the theta heat family and analytic functions \(M_t,\alpha,w_\pm\)
of [Note 17](17_UNIFORM_OUTER_CUSP_SIGNS_AND_THRESHOLD_FOUR_20261014.md).
Set \(h_k=\partial_x^kH_t\),
\(\mathcal L_j=h_{j+1}^2-h_jh_{j+2}\), \(E=h_0^2+h_1^2\), and for
positive \(x\),
\[
 L=\log(x/(4\pi)),\qquad \omega=L/4,\qquad
 Q=M_t((1+ix)/2)\zeta\big((1+ix)/2+(t/2)\alpha((1+ix)/2)\big).
\]
For every fixed \(\varepsilon>0\), there is \(X^{(3)}_\varepsilon<\infty\)
such that, uniformly for
\[
 x\ge X^{(3)}_\varepsilon,\qquad 0<t\le\tfrac12,
 \qquad tL\ge3+\varepsilon,
\]
\(Q\ne0\), and with \(\phi=\arg Q\),
\[
\frac1{2|Q|}\left(h_0,\frac{h_1}{\omega},\frac{h_2}{\omega^2},
\frac{h_3}{\omega^3}\right)
=(\cos\phi,-\sin\phi,-\cos\phi,\sin\phi)+O_\varepsilon(L^{-1}).
\tag{T1}
\]
Consequently \(E>0\) and both \(\mathcal L_0,\mathcal L_1>0\)
throughout that region, after increasing the threshold. Reflection gives
the same sign conclusion at negative heights. For every hypothetical
sequence of positive-time real collisions \((T_k,a_k)\) with
\(0<T_k\le1/2\) and \(|a_k|\to\infty\),
\[
\limsup_{k\to\infty}T_k\log(|a_k|/(4\pi))\le3.
\tag{T2}
\]
The constants defining \(X^{(3)}_\varepsilon\) have not been evaluated.
Three is a sufficient threshold of this proof; no optimality or priority
claim is made, and the boundary case \(\varepsilon=0\) is not included.

## 1. A maximal logarithmic-phase block estimate

For T>=1, M>=1 and any interval I of integers contained in (M,2M],

\[
\left|\sum_{n\in I}n^{-iT}\right|
 \ll T^{1/6}M^{1/2}+T^{-1/6}M. \tag{B1}
\]

The constant is absolute. Both signs of T have the same bound by conjugation. The relevant primary reference is Olivier Robert, *On van der Corput's k-th derivative test for exponential sums*, Indagationes Mathematicae 27 (2016), 559–589, Theorem 2 and its preceding proof (author PDF p.8):
[author PDF](https://perso.univ-st-etienne.fr/rool6510/robert-2015-indag.pdf),
[DOI](https://doi.org/10.1016/j.indag.2015.11.009).

To verify the specialization, let f(y)=-(T/(2pi))log y. On (M,2M], |f'''(y)| is comparable to T/M^3 with an absolute ratio. The third derivative bound on an interval of length J<=M is
J(T/M^3)^(1/6)+J^(1/2)(T/M^3)^(-1/6), which is bounded by the right side of (B1). Empty and one-point intervals are covered by enlarging the constant. This also proves the maximum over all terminal points; no completed-block assumption is needed.

For a direct derivation from the second derivative test, Weyl differencing with a shift cutoff 1<=H<=M gives

\[
 |S|^2\ll M^2/H+\sqrt{MT H}+M^{5/2}/\sqrt{TH}.
\]

Indeed the correlation phase f(y+h)-f(y) has second derivative comparable to Th/M^3. Take H comparable to M T^(-1/3) when that is at least one. If it is smaller, the first term of (B1) already dominates M, so the trivial estimate suffices. Zero padding makes the same calculation work for a shortened terminal block. These steps explain the two exponents used below.

For any continuously differentiable (possibly complex) weight W and R in [M,2M], exact Abel summation gives

\[
 \sum_{M<n\le R}W(n)n^{-iT}
 =W(R)S_M(R)-\int_M^R W'(y)S_M(y)\,dy,
 \quad S_M(y)=\sum_{M<n\le y}n^{-iT}. \tag{B2}
\]

Thus the sum is at most B(T,M)(|W(R)|+integral |W'|), where B is the right side of (B1) with its absolute constant. Formula (B2) retains the actual complex phase; only the later norm estimate loses its sign.

## 2. Uniform weighted sum replacement above three

Use Note 17 notation on the shrinking disc |z-x|<=1/L, L=log(x/(4pi)); write z=u+iv, ell=log(u/(4pi)), theta=t ell, and

\[
 w=w_\pm(z)=\sigma+i\tau,\qquad
 N=\left\lfloor\sqrt{u/(4\pi)+t/16}\right\rfloor.
\]

Fix epsilon>0 and assume tL>=3+epsilon. We may decrease epsilon to at most one. After increasing x, theta>=3+epsilon/2, |tau| is comparable to u, log N<=ell/2+O(1/u), and

\[
 \sigma\ge\tfrac12+\tfrac\theta4-\delta,
 \quad 0\le\delta=O(1/L),\quad \delta\le\epsilon/72.
 \tag{B3}
\]

All constants here are uniform in 0<t<=1/2, including when theta grows with ell.

For any fixed nonnegative integer r (in particular r=0,1,2,3), define

\[
 S_r=\sum_{n\le N}(\log n)^r e^{t\log^2n/4}n^{-w}.
\]

The assertion is

\[
 S_r-(-1)^r\zeta^{(r)}(w)=O_{\epsilon,r}(L^{-1}). \tag{B4}
\]

For r=0 use log(1)^0=1; the n=1 difference below is zero.

Split at the real value Y=e^(ell/3), so n<=Y means its exact integer cutoff. For the small-index discrepancy, e^q-1<=q e^q gives

\[
 \left|\sum_{n\le Y}(\log n)^r
 (e^{t\log^2 n/4}-1)n^{-w}\right|
 \le \frac t4\sum_{n=2}^{\infty}
 (\log n)^{r+2}n^{-(1/2+\theta/6-\delta)}. \tag{B5}
\]

Put theta0=3+epsilon/2 and s=theta-theta0>=0. The exponent in (B5) is at least 1+epsilon/24+s/6 (the stated delta is more conservative than necessary). Consequently its right side is bounded by

\[
 \frac{D_{\epsilon,r}}{4\ell}
 (\theta_0+s)2^{-s/6}=O_{\epsilon,r}(\ell^{-1}),
\]

where D=sum_{n>=2}(log n)^(r+2)n^(-1-epsilon/24)<infinity. This proves uniformity even for unbounded theta.

The omitted ordinary zeta tail is absolutely bounded by

\[
 \sum_{n>Y}(\log n)^r n^{-\sigma}
 \ll_r (1+\log^rY)Y^{-1/4}
 \ll_r \ell^r e^{-\ell/12}, \tag{B6}
\]

because (B3) implies sigma>=5/4 for x sufficiently large.

It remains to bound the weighted high indices Y<n<=N. Partition exactly into intervals (M,min(2M,N)], starting at M=Y and then doubling until N. For y in this range set

\[
 W_r(y)=(\log y)^r e^{t\log^2y/4}y^{-\sigma}.
\]

This nonnegative weight is decreasing for sufficiently large ell, uniformly in theta: its logarithmic derivative multiplied by y equals

\[
 r/\log y+(t/2)\log y-\sigma
 \le 3r/\ell-1/2+\delta+O(1/u)<0. \tag{B7}
\]

Abel summation and (B1) therefore bound each block by

\[
 \ll W_r(M)\{u^{1/6}M^{1/2}+u^{-1/6}M\}. \tag{B8}
\]

Let beta=(log M)/ell. Then 1/3<=beta<=1/2+O(1/(u ell)). Up to bounded constant factors, the two powers in (B8), apart from (log M)^r, have exponents in e^ell bounded by

\[
 E_1=\tfrac16-\tfrac\theta4\beta(1-\beta)+\delta\beta,
 \qquad
 E_2=-\tfrac16+\tfrac\beta2-\tfrac\theta4\beta(1-\beta)+\delta\beta. \tag{B9}
\]

On [1/3,1/2], beta(1-beta)>=2/9, hence E1<=1/6-theta/18+delta/2. For theta>=3+epsilon/2 and delta<=epsilon/72 this is <=-epsilon/48. The harmless extension beyond 1/2 changes the exponents by O(1/u), uniformly because theta<=ell/2; alternatively beta(1-beta)>=2/9 still holds for sufficiently large x. For E2 at theta=3, the convex quadratic has endpoint values -1/6 and -5/48. Increasing theta only decreases it. Thus for sufficiently large x, E2<=-1/16. In particular, with c_epsilon=min(epsilon/100,1/16),

\[
 \sum_{Y<n\le N}(\log n)^r e^{t\log^2n/4}n^{-w}
 =O_{\epsilon,r}(\ell^{r+1}e^{-c_\epsilon\ell}). \tag{B10}
\]

There are O(ell) blocks. Combining (B5),(B6),(B10) proves (B4). The terminal block is shortened at the exact N, and no derivative of N is ever used.

## 3. Imported error payments remain small

Use the effective Riemann–Siegel formula from D.H.J. Polymath, Theorem 1.3, equations (13)–(24), as transcribed and matched to the two analytic branches in Note 17:
[primary theorem](https://arxiv.org/html/1904.12438v2#S1).

The former absolute-summability estimate for the imported error sums is unnecessary. For n<=N the heat multiplier combined with n^(-theta/4) is <=a bounded constant. The disc perturbation factor n^delta is bounded because delta=O(1/L). Thus the complete positive weight sum in e_A+e_B is O(sum_{n<=N}n^(-1/2))=O(u^(1/4)). The per-index error multiplier is O(L^2/u), uniformly in t<=1/2. Consequently

\[
 e_A+e_B=O(L^2u^{-3/4}). \tag{B11}
\]

The complete remaining error satisfies

\[
 e_{C,0}\ll\exp\{-\ell/4-\theta\ell/16\}
 \ll u^{-7/16}. \tag{B12}
\]

These are more than sufficient for the O(1/L) analytic difference. They account for all three imported errors; they are not estimates of a selected remainder only.

With Gamma=|M_t(s_+(x))|, the established disc comparison |M_t(s_pm(z))|~Gamma and (B4) at r=0 give

\[
 H_t(z)-[Q_+(z)+Q_-(z)]=O_\epsilon(\Gamma/L)
\]

on the upper half-disc, and Schwarz symmetry gives the lower half. The zeta arguments stay in Re w>=5/4, so the same uniform zeta upper/lower bounds and fixed-order logarithmic-derivative bounds from Note 17 apply. Cauchy's estimate for this analytic difference gives all four physical jets. The floor cutoff has disappeared before differentiation. The carrier differentiation and quadratic perturbation algebra are unchanged. Hence the strict Laguerre theorem holds for t log(x/(4pi))>=3+epsilon; reflection supplies negative x. Any hypothetical collision sequence with |x| tending to infinity now satisfies limsup t log(|x|/(4pi))<=3.

## 4. Exact common-carrier moments and staircase terms

This is an additional exact reformulation of the Note 16 carrier, valid without the threshold-three assumption. Let d_n=(log n)/2, T=x/2+ta, and

\[
 A_n(v)=n^{-1/2}\exp\{t\log^2n/4-tv\log n-iT\log n\},
 \quad B_r(v)=\sum_{n\le e^{2v}}(\log n)^r A_n(v).
\]

Every dyadic block truncated at R(v)=min(2M,e^(2v)) is exactly (B2) with
W(y)=(log y)^r exp(tlog²y/4)y^(-1/2-tv); if R<M the block is empty. The total-variation version of (B2) always applies, for every real T. Estimate (B1) applies when |T|>=1, using conjugation for negative T; for |T|<1 the trivial count is an available bound. More specifically, for M>=exp(2r), the weight is decreasing on the truncated block because

\[
 y(\log W)'=r/\log y+(t/2)\log y-(1/2+tv)\le r/\log y-1/2\le0.
\]

For r=0 this monotonicity holds for every M>=1. Thus (B8), with u replaced by |T| and sigma by 1/2+tv, is a direct common-carrier block bound whenever |T|>=1. These formulas preserve the entering-index endpoint at R(v). They are complex block estimates, not signed quadratic estimates.

On v>0 the precise distribution identity is

\[
 \frac{d}{dv}B_r(v)=-tB_{r+1}(v)
 +\sum_{n\ge2}(\log n)^r A_n(d_n)\delta(v-d_n). \tag{B13}
\]

At v=0, n=1 is already present and must be included in any integration-by-parts lower endpoint. Here
A_n(d_n)=n^(-1/2)exp(-td_n²-i(x+2ta)d_n).

Let K(v)=exp(t(v+ia)²)phi_1(v+ia)exp(ixv), and lambda_n(v)=i(v+ia-d_n). The jet sum D_j(v)=sum_{n<=e^(2v)} A_n(v)lambda_n(v)^j obeys, between jumps,

\[
 D'_j=-2t(v+ia)D_j-2itD_{j+1}+ijD_{j-1}, \tag{B14}
\]

with the last term omitted for j=0. At v=d_n the jump is A_n(d_n)(-a)^j. The complete entry contribution after multiplication by the carrier is

\[
 K(d_n)A_n(d_n)(-a)^j
 =e^{-ta^2}(-a)^j\phi_n(ia). \tag{B15}
\]

All x-dependent entry phases cancel exactly. This is why these jumps cannot be assigned artificial oscillatory cancellation in x; they must accompany the carrier integration. The equalities use phi_n(z)=n^(-1/2)phi_1(z+d_n), with no individual-index contour-shift assumption. Complete-source tail bounds from Note 16 justify the full integral; bounded subintervals of v have finitely many jumps.

## 5. Exact paired observation with every carrier cross term

This section continues Note 16's exact contour identity. Fix
\(0<a<\pi/8\), and let
\[
\Omega=\{(v,n):v\ge0,\ n\in\mathbb N,\ d_n=\tfrac12\log n\le v\},
\qquad d\nu=dv\times\text{counting measure}.
\]
For \(\alpha=(v,n)\), write
\[
y_\alpha=v-d_n\ge0,\quad q_\alpha=-a+iy_\alpha,
\quad W_\alpha=e^{t(v+ia)^2}\phi_1(v+ia)e^{ixv}A_n(t,x;v).
\]
All parameters are frozen at the observation point. Then exactly
\[
h_k=e^{-ax}\Re I_k,\qquad I_k=\int_\Omega W_\alpha q_\alpha^k\,d\nu(\alpha).
\tag{P1}
\]
No value of a physical jet is used as a denominator. The staircase
\(d_n\le v\) is part of this domain; the two factors below have independent
coordinates and independent entering indices.

**Paired Laguerre identity.** For \(j=0,1\),
\[
\boxed{\begin{aligned}
\mathcal L_j=\frac{e^{-2ax}}4\Re\iint_{\Omega^2}\bigl[&
(y_\alpha+y_\beta)^2W_\alpha\overline{W_\beta}
 (q_\alpha\overline{q_\beta})^j\\
&+(y_\alpha-y_\beta)^2W_\alpha W_\beta
 (q_\alpha q_\beta)^j\bigr]\,d\nu(\alpha)d\nu(\beta).
\end{aligned}}
\tag{P2}
\]
In particular, a calculation restricted to one carrier coordinate or to
equal indices does not evaluate this observation.

For the proof use
\(\Re A\Re B=\tfrac12\Re(A\overline B+AB)\) in
\(h_{j+1}^2-h_jh_{j+2}\), and symmetrize the latter product under
\(\alpha\leftrightarrow\beta\). The Hermitian difference becomes
\[
q_\alpha\overline{q_\beta}
-\tfrac12(q_\alpha^2+\overline{q_\beta}^{2})
=-\tfrac12(q_\alpha-\overline{q_\beta})^2
=\tfrac12(y_\alpha+y_\beta)^2;
\]
the bilinear difference is
\(-\tfrac12(q_\alpha-q_\beta)^2
=\tfrac12(y_\alpha-y_\beta)^2\).
The common drift \(-a\) cancels in both frequency differences.
The conjugate-swapped Hermitian term has the same real integral, which
justifies its symmetrization.

The source majorant from Note 16 is
\[
\sum_{n\le e^{2v}}|W_{(v,n)}||q_{(v,n)}|^k
\le 2(2\pi^2+3\pi)(v+a)^k
 \exp\{\tau v^2+10v-\pi\cos(4a)e^{4v}\},\qquad 0\le t\le\tau.
\tag{P3}
\]
Every polynomial moment is integrable. Since
\((y_\alpha\pm y_\beta)^2\le2(y_\alpha^2+y_\beta^2)\),
the two double integrals are absolutely convergent separately. Fubini,
conjugation and symmetrization therefore require no conditional-limit
prescription, even though their actual signs depend on cancellation.

The nonnegative frequency squares in (P2) do not make the integrals
nonnegative: the two amplitude products retain their actual phases.
For an elementary control, two signed atoms with \(a=0\), frequencies
1 and 2, and weights 1 and \(-1/2\), have \(h_0=1/2,h_1=0,h_2=1\).
Thus \(\mathcal L_0=-1/2\), although the separate diagonal
contributions sum to 2; the two ordered cross terms sum to \(-5/2\).
This is a finite algebra control outside the theta source class and
outside the positive-contour hypothesis, not a theta counterexample.

## 6. Centering, stationarity, and complete pair-tail payments

For any fixed \(b\ge0\), put \(\mu=a^2+b^2\). The residual satisfies
\[
C_j=e^{-ax}\Re\int_\Omega(y_\alpha^2-b^2)W_\alpha q_\alpha^j\,d\nu(\alpha)
=-h_{j+2}-2ah_{j+1}-\mu h_j.
\tag{P4}
\]
The paired residual product is also explicit:
\[
\begin{aligned}
h_jC_j=\frac{e^{-2ax}}4\Re\iint_{\Omega^2}
 &(y_\alpha^2+y_\beta^2-2b^2)\bigl[
 W_\alpha\overline{W_\beta}(q_\alpha\overline{q_\beta})^j\\
 &\hspace{40mm}+W_\alpha W_\beta(q_\alpha q_\beta)^j\bigr]\,d\nu(\alpha)d\nu(\beta).
\end{aligned}
\tag{P5}
\]
Before restricting to a stationary set, the exact discrepancy is
\[
\mathcal L_j-\mu h_j^2-h_jC_j
=h_{j+1}(h_{j+1}+2ah_j).
\tag{P6}
\]
This identifies precisely the original stationary constraint to be imposed
on a future block estimate; approximate stationarity cannot replace it
without a separate payment for the right side.

Let \(A\subset\Omega\) be any retained measurable domain, and form
\(h_k^A\) from (P1) with integration over \(A\). Define the nonnegative
absolute masses
\[
R_k=\int_A|W_\alpha||q_\alpha|^k\,d\nu(\alpha),\qquad
T_k=\int_{\Omega\setminus A}|W_\alpha||q_\alpha|^k\,d\nu(\alpha).
\]
Let \(\mathcal L_j^A=(h_{j+1}^A)^2-h_j^Ah_{j+2}^A\).
Applying (P2) to the omitted pairs, and using
\((y+z)^2+(y-z)^2=2(y^2+z^2)\) and \(y^2\le|q|^2\), gives
\[
\boxed{|\mathcal L_j-\mathcal L_j^A|
\le e^{-2ax}(R_jT_{j+2}+R_{j+2}T_j+T_jT_{j+2}).}
\tag{P7}
\]
Indeed the absolute sum of the two pair integrands, including their
factor \(1/4\), is at most
\(\tfrac12(|W_\alpha||q_\alpha|^{j+2}|W_\beta||q_\beta|^j
+|W_\alpha||q_\alpha|^j|W_\beta||q_\beta|^{j+2})\).
Integrate over \((A\times A^c)\cup(A^c\times A)\cup(A^c\times A^c)\).
This pays every omitted mixed pair and omitted-omitted pair while keeping
all retained correlations intact. No \(T_{j+1}\) estimate is needed.

For \(A=\{(v,n)\in\Omega:v\le V,n\le N\}\), bound \(T_k\)
by the complete omitted-index payment from Note 12 plus the full
\(v\ge V\) payment from Note 16. More explicitly, with
\[
\beta_V=\pi\cos(4a)e^{4V},\quad q_V=4\beta_V-10-2\tau V,
\quad Q_V=\tau V^2+10V-\beta_V,
\]
if \(q_V>0\) and \(8\beta_V\ge\tau\), the integration part of
the unnormalized mass \(T_k\) is at most
\[
2(2\pi^2+3\pi)e^{Q_V}S_k(q_V,V+a),\qquad
S_k(q,d)=\sum_{r=0}^k\binom kr d^{k-r}\frac{r!}{q^{r+1}}.
\tag{P8}
\]
The outside factor \(e^{-ax}\) is absent here because \(T_k\) was
defined before that normalization. The corresponding omitted-index
bound must likewise be used before its \(e^{-ax}\) factor. Overlap of
the index and integration omissions may be overpaid. Retained quadrature
and cell variation still require their own validated errors; (P7) alone
is not a whole-cell certificate.

These formulas give a complete correlation-preserving observation and
its truncation rule. They do not produce a locally bounded loss through
an unknown joint zero. An absolute bound in (P7), however small, cannot
be divided by the unknown \(E\) to supply that missing relative estimate.

## 7. Exact obstacle after the improvement

The block estimate preserves cancellation inside a complex arithmetic block and improves the sufficient outer threshold. It still bounds moduli. For theta<=3 its low/high split no longer makes the common analytic difference uniformly small relative to the nonzero zeta carrier, and it does not provide a sign for the complete integrated products h_j C_j. In particular (B13)–(B15) give identities, not nonnegative endpoint contributions. The residual goal remains a one-sided bound on the full two-coordinate quadratic integral, with a loss locally bounded through every candidate positive-time first-pair zero. The presently proved asymptotic threshold three cannot be used as an actual finite cutoff, and the certificate through 104 does not fill the unknown transition strip.


## 8. Validation, current scope, and continuation

The [exact checker](../numerics/check_signed_carrier_pair_identities.py)
and [small receipt](../numerics/SIGNED_CARRIER_PAIR_IDENTITY_CHECKS_20261014.json)
record **34** exact rational polynomial and endpoint checks: the paired
identities, stationary-ideal correction, error expansions, block exponents,
smooth staircase recurrence, entry-phase cancellation, and the signed-atom
control. They audit algebra. The infinite sums, uniformity, analytic
continuation and sign theorem are justified by the proof above and the
cited primary estimates. The [independent internal review](../reviews/14_OSCILLATORY_BLOCKS_AND_EXPLICIT_HEIGHT_REVIEW_20261014.md)
separately checks those arguments and replays the checker.

From the investigation's `numerics/` directory, using the standard library:

```sh
python3 check_signed_carrier_pair_identities.py --output /tmp/inv21-pair-replay.json
```

No new whole-cell quadrature was run and the finite cover remains
\(0\le t\le1/2,\ |x|\le104\). The stable manuscript and its build
record continue to describe the previous exposition; these research notes
are the subsequent development. The starting checkout was
`f723c7bbd36984e3ca83e0e4e68918373a335a46`.

The next analytic target is (P5), with the full cross-coordinate and
cross-index correlations and actual phases, on the genuine stationary
sets. A proof must establish
\[
 h_jC_j\ge-\mu h_j^2-K_jE\quad\text{on }h_{j+1}=0,
 \qquad j=0,1,
\]
with prescribed, locally bounded loss through each candidate positive-time
joint zero. Equations (B13)–(B15) retain entering-index terms; (P7)–(P8)
pay omitted pairs. Neither supplies this signed relative estimate by itself.
A separate quantitative task is to make the threshold-three constants
explicit and improve the very coarse height in Note 20. Existing finite
coverage must be connected only after an actual bound is established.

This conversation is newly and uniquely registered in the formal replay
lane as number **9**, thread `01a13cd2-1633-7f50-a8bb-d62373ca4e24`:
[history](../chat-histories/0012_2026-10-14T23-49-23Z_continue-quaternion-theta-rewrite.json).
It is distinct from Note 18's number-8 conversation, whose identity is
preserved. The current turn uses the bounded exact-turn final-capture
workflow; native completion-hook activation has not been verified.
