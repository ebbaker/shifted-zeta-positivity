# Productwise recombination and the fixed profile prime pair barrier

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Derivations and same-model review are internal checks, not independent
specialist validation or formal proof replay.

This note uses the arithmetic conventions and explicitly imported analytic
inputs of the organized short-family manuscript, especially its adaptive-
factorization and primepair-obstruction sections. It does not assume the
open tail moment.

## 1. Results and their scope

At the test parameters
\[
 h=a=\frac25,\qquad \theta=\frac1{40},\qquad H=D^{2/5},
\tag{1}
\]
the desired normalized tail moment is \(D^{4/5+\varepsilon}\).
These parameters give the conditional extraction boundary \(13/15<7/8\),
if the full moment is proved.

The new observations are:

1. Recombining **all factor tuples with the same total product** does not
   eliminate the existing primepair obstruction. On every inner row,
   the entire product sector with at most two prime factors has an exact
   description. On coherent rows it equals a complete ordered primepair
   sum, including its prime-square diagonal.
2. For every nonzero fixed smooth complex profile, that ordered primepair
   sum has a nonzero term at some finite logarithmic order. No fixed
   nonzero profile can remove the obstruction to all logarithmic orders.
   Extra derivative profiles only postpone the first nonzero term.
3. Genuine prime powers of exponent at least two have an affordable
   moment under the **complete Schwartz row weight**. The prime-only
   contribution to the adaptive tail is negligible under that weight.
   Consequently prime powers cannot compensate the coherent primepair
   amplitude.

These statements concern selected components. They give **no lower bound
for the full signed tail**. Cancellation with products having at least
three prime factors remains possible and necessary in any proof of the
useful full moment.

## 2. Conventions and explicit inputs

All ideals below are integral good ideals of the fixed Eisenstein field;
the fixed bad-prime set is \(S\). Write \(Nn\) for ideal norm,
\(\Omega(n)=\sum_p v_p(n)\), and \(\mu_K\) for the ideal Möbius function.
Primes mean prime ideals. The fixed twist is trivial, \(\nu=1\), when
establishing the obstruction. This is a permitted specialization of the
physical family. The prime-power upper bound also permits any fixed
finite-order twist.

Let \(W\in C_c^\infty((c,C))\), with \(0<c<C\), be fixed and nonzero,
possibly complex. Set
\[
 z=(CD)^{1/2},\quad m_z(n)=\mu_K(n)\mathbf1_{Nn\le z},
 \quad c_z=m_z*m_z,\quad
 \lambda_u(n)=\nu(n)\chi_n(u).
\tag{2}
\]
Zero extension is retained throughout, so \(\lambda_u\) is completely
multiplicative, including at deleted primes. Let
\[
 L_u=Q_uNE_u,\qquad
 Y_u=D^{39/40}/L_u.
\tag{3}
\]
The arithmetic input from the manuscript gives
\[
 1\le L_u\ll_{\nu,S} Nu.
\tag{4}
\]
The actual adaptive tail is
\[
 T_u(D)=-\sum_{Nd>Y_u}c_z(d)\lambda_u(d)
              \sum_m\lambda_u(m)W(Ndm/D).
\tag{5}
\]
No new squarefreeness or coprimality conditions are imposed on its factors.

The fixed row weight \(\Phi\) is nonnegative, Schwartz, and at least one
on the inner norm ball. Ideal and lattice counting give
\[
 \sum_{u\ne0}\Phi(Nu/H)\ll_\Phi H,\qquad
 \sum_{Nu>R}\Phi(Nu/H)\ll_{A,\Phi}H(R/H)^{-A}
 \quad(R\ge H\ge1)
\tag{6}
\]
for every fixed \(A>0\), after increasing the decay order used for
\(\Phi\).

The only non-elementary analytic input used for the obstruction is the
quantitative fixed-field prime ideal theorem already imported
in the manuscript:
\[
 \pi_K(x)=\operatorname{Li}(x)
             +O_K(xe^{-c_K\sqrt{\log x}})
\tag{7}
\]
for sufficiently large \(x\). This is the same fixed-field consequence
of [Das--Kadiri--Ng, Corollary 1.4](https://arxiv.org/html/2508.09480v1), used in the preceding factor-selection
note. Any fixed exceptional-zero contribution has already been absorbed
in the threshold for (7). Its proof is not replayed here.

## 3. Exact recombination by total product

Complete multiplicativity permits the exact finite identity
\[
 T_u(D)=\sum_n t_u(n)\lambda_u(n)W(Nn/D),\qquad
 t_u(n)=-\sum_{\substack{d\mid n\\Nd>Y_u}}c_z(d).
\tag{8}
\]
The coefficient \(t_u(n)\) includes every factorization
\(n=abm\) from (5); it is not a selected tuple coefficient.
The row dependence of \(Y_u\) is retained pointwise.

For all inner rows \(0<Nu\le H=D^{2/5}\), (3)--(4) give
\[
 Y_u\gg_{\nu,S}D^{23/40},\qquad
 Y_u\le D^{39/40}.
\tag{9}
\]
Consequently
\[
 z<Y_u<cD
\tag{10}
\]
on **every inner row**, for sufficiently large \(D\).
This conclusion does not require the row to be coherent.
For comparison, on coherent inner rows \(u=r^6\) the sharper radical
bound gives
\[
 Y_u\gg D^{109/120},\qquad
 Nm\ll D^{11/120},\qquad
 Na,Nb\gg D^{49/120}
\tag{11}
\]
for surviving tuples. The full inner family only gives the weaker
free-factor and factor bounds \(Nm\ll D^{17/40}\) and
\(Na,Nb\gg D^{3/40}\).

### Proposition 1. The sector \(\Omega(n)\le2\)

Define the selected **product** amplitude
\[
 B_u(D)=
 \sum_{\substack{n\\\Omega(n)\le2}}
       t_u(n)\lambda_u(n)W(Nn/D).
\tag{12}
\]
For every inner row, sufficiently large \(D\), and products on the
profile, its coefficients are as follows:

| Total product | Actual coefficient \(t_u(n)\) |
| --- | --- |
| A prime \(p\) | \(0\) |
| Distinct primes \(pq\), both \(Np,Nq\le z\) | \(-2\) |
| Distinct primes \(pq\), one prime norm greater than \(z\) | \(0\) |
| A prime square \(p^2\) | \(-1\) |

In particular,
\[
 B_u(D)=
 -\sum_{\substack{p,q\ \mathrm{good}\\Np,Nq\le z}}
       \lambda_u(p)\lambda_u(q)W(NpNq/D),
\tag{13}
\]
where the prime variables are ordered and equality \(p=q\) is included.

**Proof.** On the profile, \(Nn\ge cD>Y_u>z\).
The local convolution coefficients are
\[
 c_z(1)=1,\quad
 c_z(p)=-2\quad(Np\le z),\quad
 c_z(p^2)=1\quad(Np\le z).
\tag{14}
\]
For a prime \(p\) on the profile, \(Np>z\), so \(c_z(p)=0\).
Its only other divisor is \(1<Y_u\), hence \(t_u(p)=0\).

For distinct primes with \(Np,Nq\le z\), their proper divisors have
norms at most \(z<Y_u\), while \(Npq\ge cD>Y_u\).
There are precisely two allowed factorizations contributing to
\(c_z(pq)\), namely \((p,q)\) and \((q,p)\), both with coefficient one.
Thus \(t_u(pq)=-c_z(pq)=-2\).
If, say, \(Np>z\), no allowed factorization of \(pq\) can place \(p\)
in either factor, so \(c_z(pq)=0\); the remaining possible divisor
coefficients are zero or occur below \(Y_u\).

For \(p^2\) on the profile, \(Np\le\sqrt{CD}=z\), its proper divisors
are below \(Y_u\), and the only allowed full-product factorization is
\((p,p)\). Hence \(t_u(p^2)=-1\).
These cases prove (13), including the diagonal. \(\square\)

The proof works with the actual row-dependent coefficient in (8).
It does not insert a product or row selector into a completed row
kernel.

## 4. The exact continuum primepair kernel

Put
\[
 P_W(D)=\sum_{\substack{p,q\ \mathrm{good}\\Np,Nq\le z}}
                    W(NpNq/D),
\tag{15}
\]
including the diagonal. Every contributing prime norm lies in
\[
 \frac{c}{\sqrt C}\sqrt D\le Np,Nq\le\sqrt{CD}.
\tag{16}
\]
Thus all fixed bad primes are absent for sufficiently large \(D\).

Two-variable partial summation using (7) gives
\[
 P_W(D)=
 \int_2^z\int_2^z
       \frac{W(xy/D)}{\log x\log y}\,dx\,dy
       +O_W\!\left(De^{-\gamma\sqrt{\log D}}\right)
\tag{17}
\]
for some fixed \(\gamma>0\). The fixed lower integration limit is
irrelevant for large \(D\), because of (16).

For clarity about the error in (17), on the contributing rectangle
both variables are comparable to \(\sqrt D\). The prime-counting error
in one variable is \(O(\sqrt D e^{-\gamma\sqrt{\log D}})\);
the relevant supremum and total variation of the profile in that
variable are bounded by fixed seminorms of \(W\).
Summing the resulting error over the other prime variable costs
at most \(O(\sqrt D)\). For the second replacement, the profile
obtained by integrating over the first variable has supremum and
total variation \(O_W(\sqrt D)\), so its prime-counting replacement
also costs \(O_W(De^{-\gamma\sqrt{\log D}})\).
The sharp upper limits at \(z\) are included by the boundary terms in
partial summation. This argument bounds absolute errors and therefore
also applies to complex \(W\).

Define
\[
 B=\log z=\tfrac12\log(CD),\qquad v(t)=\log(C/t).
\tag{18}
\]
The change of variables \(t=xy/D\), followed by \(s=\log x\), gives
the exact continuum identity
\[
 \begin{aligned}
 \int_2^z\int_2^z\frac{W(xy/D)}{\log x\log y}\,dx\,dy
 &=D\int_c^C W(t)
       \int_{Dt/z}^{z}
       \frac{dx}{x\log x\log(Dt/x)}\,dt\\
 &=D\int_c^C W(t)
       \int_{B-v(t)}^B
       \frac{ds}{s(2B-v(t)-s)}\,dt\\
 &=D\int_c^C W(t)F_B(v(t))\,dt,
 \end{aligned}
\tag{19}
\]
where, for sufficiently large \(D\),
\[
 \boxed{F_B(v)=\frac{2}{2B-v}\log\frac{B}{B-v}.}
\tag{20}
\]
All denominators are positive on the integration domain.
The interval for \(s\) has length \(v\).
Partial fractions in \(s\) establish the last equality directly.

Since the support of \(W\) is compact inside \((c,C)\),
\(v\) lies in a fixed compact interval
\([v_{\min},v_{\max}]\subset(0,\infty)\).
Expanding the two elementary factors in (20) gives a uniformly
convergent series for \(B>v_{\max}\):
\[
 \boxed{
 F_B(v)=\sum_{k\ge1}\alpha_k\frac{v^k}{B^{k+1}},
 \qquad
 \alpha_k=\sum_{j=1}^k\frac{2^{-(k-j)}}j>0.
 }
\tag{21}
\]
Indeed
\[
 F_B(v)=\frac1B
        \left(\sum_{r\ge0}\frac{v^r}{2^rB^r}\right)
        \left(\sum_{j\ge1}\frac{v^j}{jB^j}\right).
\tag{22}
\]
The first six coefficients are
\[
 \alpha_1=1,\quad\alpha_2=1,\quad\alpha_3=\frac56,\quad
 \alpha_4=\frac23,\quad\alpha_5=\frac8{15},\quad
 \alpha_6=\frac{13}{30}.
\tag{23}
\]

### Lemma 2. A nonzero fixed profile has a first nonzero moment

For every nonzero \(W\in C_c^\infty((c,C))\), possibly complex, some
finite positive integer \(k_0\) is the least index for which
\[
 M_{k_0}(W):=\int_c^C W(t)\log^{k_0}(C/t)\,dt\ne0.
\tag{24}
\]

**Proof.** Under \(t=Ce^{-v}\), write
\[
 f(v)=Ce^{-v}W(Ce^{-v}).
\]
If every moment in (24), for \(k\ge1\), vanished, then
\(\int f(v)vP(v)\,dv=0\) for every complex polynomial \(P\).
On the compact support interval \(v\ge v_{\min}>0\), polynomials
approximate the continuous function \(\overline{f(v)}/v\) uniformly.
Taking the limit would give \(\int|f(v)|^2\,dv=0\), contrary to
\(W\ne0\). The positive integers are well ordered, so a least such
index exists. This does not require \(M_0(W)\ne0\), or positivity or
reality of \(W\). \(\square\)

Combining (17), (19), and the finite expansion of (21) at this first
nonzero moment yields
\[
 \boxed{
 P_W(D)=
 \frac{D\alpha_{k_0}M_{k_0}(W)}{B^{k_0+1}}
       +O_W\!\left(\frac{D}{B^{k_0+2}}\right).
 }
\tag{25}
\]
The error in (17) is smaller than \(D/B^J\) for every fixed \(J\).
The expansion remainder in (25) is uniform because \(v\) remains
in a fixed compact interval. For complex \(W\), the leading
coefficient in (25) may be complex but is nonzero, so its modulus
still dominates the error for sufficiently large \(D\).

The distinct-prime version of (25) has the same leading term:
its omitted diagonal is \(O_W(\sqrt D/\log D)\), which is smaller
than every fixed logarithmic order of \(D\).

## 5. A barrier after complete productwise recombination

### Theorem 3. The selected product sector cannot meet the useful budget

Keep (1), let \(\nu=1\), and let \(W\ne0\) be any fixed smooth complex
profile supported compactly in \((c,C)\).
For \(k_0\) from Lemma 2, the actual product-sector amplitude (12)
satisfies
\[
 \boxed{
 \frac1D\sum_{u\ne0}\Phi(Nu/H)|B_u(D)|^2
 \gg_{W,\Phi}
 \frac{DH^{1/6}}{(\log D)^{2k_0+2}}.
 }
\tag{26}
\]
In particular this selected sector fails a
\(D^{4/5+\varepsilon}\) estimate for every sufficiently small fixed
positive \(\varepsilon\).

**Proof.** Restrict the nonnegative sum of squares in (26) to coherent
inner rows \(u=r^6\), \(Nu\le H\).
There are \(\gg_K H^{1/6}\) distinct such rows, accounting for the
finite unit multiplicity of the sixth-power map.
Every prime in (16) has norm \(\gg\sqrt D\), whereas
\[
 Nr\le H^{1/6}=D^{1/15}.
\]
Consequently no contributing prime divides \(r\), and the original
zero extensions give \(\lambda_{r^6}(p)=1\).
Proposition 1 therefore gives the exact identity
\[
 B_{r^6}(D)=-P_W(D)
\tag{27}
\]
on every one of these rows.
Equation (25), including the modulus conclusion for complex \(W\),
gives
\[
 |B_{r^6}(D)|
 \gg_W D/(\log D)^{k_0+1}.
\]
The weight is at least one on the inner ball. Squaring, counting
these rows, and dividing by \(D\) proves (26).
At \(H=D^{2/5}\), its power is \(D^{16/15}\), above \(D^{4/5}\)
by \(D^{4/15}\), regardless of the fixed logarithmic denominator.
\(\square\)

This argument uses a nonnegative sum of squares of the **selected
amplitude \(B_u\)**. It does not discard negative cross terms from
the full tail square.
Writing \(T_u=B_u+R_u\), where \(R_u\) has \(\Omega(n)\ge3\),
gives
\[
 |T_u|^2=|B_u|^2+2\Re(B_u\overline{R_u})+|R_u|^2.
\tag{28}
\]
The cross term is not controlled here. It can cancel the lower bound
for the selected component. Thus (26) is a barrier to bounding
this product sector separately, not a counterexample to the full
tail target.

### Corollary 4. Extra derivative profiles only change logarithms

Let \(J\ge1\), \(V\ge0\) be fixed, smooth, compactly supported in
\((c,C)\), and nonzero, and put
\[
 W=(1+t\partial_t)^J V.
\tag{29}
\]
Repeated integration by parts gives
\[
 M_k(W)=
 \begin{cases}
 0,&0\le k<J,\\
 k(k-1)\cdots(k-J+1)
       \displaystyle\int_c^C V(t)\log^{k-J}(C/t)\,dt,&k\ge J.
 \end{cases}
\tag{30}
\]
In particular \(k_0=J\) and \(M_J(W)=J!\int V>0\).
Hence
\[
 P_W(D)=
 \frac{D\alpha_JJ!\int V}{B^{J+1}}
       +O_V(D/B^{J+2}).
\tag{31}
\]
For \(J=1\), this recovers the preceding
\(4D(\log D)^{-2}\int V\) leading term.
Every fixed \(J\) leaves the power obstruction in (26).

## 6. Prime powers are affordable under the full Schwartz weight

### Proposition 5. Prime powers cannot supply the needed compensation

Let \(C_u(D)\) be the part of (8) whose total product is a prime
power \(p^k\) with \(k\ge2\). Then, uniformly in the row-dependent
cutoff,
\[
 \frac1D\sum_{u\ne0}\Phi(Nu/H)|C_u(D)|^2
 \ll_{\varepsilon,W,\Phi}HD^\varepsilon.
\tag{32}
\]
Let \(P_u^{\mathrm{tail}}(D)\) be its prime-only analogue, with \(k=1\).
At (1), for every requested \(N>0\),
\[
 \frac1D\sum_{u\ne0}\Phi(Nu/H)
       |P_u^{\mathrm{tail}}(D)|^2=O_N(D^{-N}).
\tag{33}
\]

**Proof.** From (8) and the divisor bound,
\[
 |t_u(n)|\le\sum_{d\mid n}|c_z(d)|
 \le\sum_{d\mid n}\tau(d)=\tau_3(n)
 \ll_\varepsilon (Nn)^\varepsilon,
\tag{34}
\]
uniformly in \(u\) and \(Y_u\). There are
\(O_\varepsilon(D^{1/2+\varepsilon})\) prime-power ideals of exponent
at least two with norm at most \(CD\), by ideal counting and the
\(O(\log D)\) possible exponents. Since
\(|\lambda_u(n)|\le1\),
\[
 |C_u(D)|\ll_{\varepsilon,W}D^{1/2+\varepsilon}.
\tag{35}
\]
Square, divide by \(D\), sum the complete row weight using (6),
and reallocate epsilon to obtain (32).

A prime \(p\) on the profile has norm greater than \(z\), so
\(c_z(p)=0\). Its only possible tail contribution comes from
\(d=1\), and therefore \(P_u^{\mathrm{tail}}=0\) whenever
\(Y_u\ge1\).
If \(Y_u<1\), then \(L_u>D^{39/40}\); (4) forces
\[
 Nu\gg_{\nu,S}D^{39/40}.
\tag{36}
\]
The prime-only amplitude is \(O_W(D)\) by ideal counting, uniformly
in \(u\). Its normalized energy is thus bounded by
\[
 D\sum_{Nu\gg D^{39/40}}\Phi(Nu/H)
 \ll_{A,W,\Phi}DH
       (D^{39/40}/H)^{-A}.
\tag{37}
\]
Here \(D^{39/40}/H=D^{23/40}\).
Taking the Schwartz decay order \(A\) sufficiently large for each
requested \(N\) proves (33). \(\square\)

The square-root amplitude in (35) is smaller than the coherent
primepair amplitude \(D/(\log D)^{k_0+1}\) from (25).
Thus even before comparing moments, the pure prime powers cannot
cancel that leading amplitude on coherent rows.
Products with repeated factors involving more than one distinct prime
are not covered by (32); they belong to the remaining \(\Omega\ge3\)
sector and must retain their actual coefficients.

## 7. Consequence for the next signed estimate

The all-fixed-profile obstruction strengthens the earlier nonnegative-
\(V\) example, and the \(\Omega\le2\) formulation survives exact
recombination within each total product. The next argument cannot
avoid the issue merely by changing a fixed detector profile, grouping
all tuples with the same product, or disposing of pure prime powers.

The remaining possibility is cancellation **across different total
products**, involving the \(\Omega\ge3\) terms with their true Möbius
factor coefficients, smooth profile, and adaptive threshold. The
ordinary free-character completion theorem supplies no corresponding
transform estimate for the two Möbius-weighted factors.
Applying Cauchy and the existing generic physical sextic sieve still
retains \(DH^{1/6}\), as in the preceding factor-selection analysis.
No new signed bilinear estimate, full tail moment, zero-free boundary,
or implication from zeta-only quasi-RH to RH is established here.

## 8. Verification and dependencies

The exact continuum formula (20) follows from the displayed partial
fractions. The coefficients in (21)--(23) follow by multiplying two
absolutely convergent series. The product coefficients in Proposition 1
are finite convolution calculations with the original cutoffs.
The moment argument treats complex profiles by their nonzero complex
leading coefficient and by polynomial approximation to
\(\overline f/v\).

The [standalone checker](../../numerics/check_short_family_product_barrier.py)
prints deterministic JSON and writes no files. Its
[record](../../numerics/short_family_product_barrier_record_20261008.json)
contains 182 exact assertions in ten groups; two fresh runs reproduced it
byte-for-byte. Checks passed for the four product-coefficient cases
at \(z=100,\ Y=200\), using formal prime generators with norm products
\(5011,\ 61\cdot97,\ 109\cdot61,\ 73^2\), respectively. All five
generator norms are split rational primes of the Eisenstein field;
the check concerns the free multiplicative divisor algebra, not a
reciprocity or bad-prime certificate. The same check reproduced the first
six rational coefficients in (23), the partial-fraction identity in
(19), the two support exponents in (9) and (11), the extraction exponent
\(13/15\), and the power gap \(4/15\). It also tests the derivative-profile
moment formula for orders one through five, using a polynomial bump with
sufficient vanishing endpoint derivatives. That bump is a finite calculus
diagnostic, not a smooth compactly supported analytic test profile.
These finite checks test the
specified algebra; they do not verify (7), the moment-density argument,
or an asymptotic signed estimate.

See the [scoped review](../../reviews/SHORT_FAMILY_SIGNED_PACKET_REVIEW_20261008.md)
for the separate same-model mathematical audit and remaining obligation.

The arithmetic conventions, conductor/deletion bound, and Schwartz
row counting retain their source status from the organized manuscript.
The quantitative prime ideal theorem (7) is an imported analytic input,
not certified by a finite check. No large derived data or asymptotic
numerical evidence is used.

Relevant repository records:

- short_families/short_family_reductions.tex, adaptive factorization,
  generic sextic baseline, and selected-factor obstruction.
- short_families/notes/11_SHORT_FAMILY_MEAN_ZERO_ADAPTIVE_REDUCTION_20261008.md.
- short_families/notes/12_SHORT_FAMILY_FACTOR_SELECTION_BARRIER_20261008.md.
- short_families/notes/13_SHORT_FAMILY_ADAPTIVE_CONTINUATION_20261008.md.
- notes/RESEARCH_LEDGER_20261008.md.
