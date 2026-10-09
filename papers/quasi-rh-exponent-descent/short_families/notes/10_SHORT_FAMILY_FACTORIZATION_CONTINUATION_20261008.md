# Short family continuation after centered factorization

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel derivations and reviews are same-model internal checks, not
independent specialist validation or formal proof replay.

Based on repository commit 480581447dcd3e93c9c2f9c22a050d9c5100ff9d.
This is the next starting point after [note 7](7_SHORT_FAMILY_CONTINUATION_20261008.md).

## A negligible centered factorization sector

The [exact factorization](8_SHORT_FAMILY_CENTERED_FACTORIZATION_20261008.md)
preserves the actual Möbius coefficients before expanding the square.
Take \(m_z=\mu_K\mathbf1_{Nn\le z}\), \(c_z=m_z*m_z\), and
\(z=(CD)^{1/2}\), where \(\operatorname{supp}W\subset[c,C]\). Then,
for sufficiently large \(D\),

\[
 A_u(D)=-\sum_d c_z(d)\lambda_u(d)S_u(D/Nd),\qquad
 \lambda_u(n)=\nu(n)\chi_n(u),\quad
 S_u(L)=\sum_{(m,S)=1}\lambda_u(m)W(Nm/L).
\tag{1}
\]

Every overlapping factor tuple and deletion mask is retained.
Individual squarefree restrictions on the free factors would destroy
the nonsquarefree coefficient cancellation.

Split (1) at \(Nd\le Y\), calling that part \(I_u\) and its complement
\(T_u\). Let \(\kappa_u\) be the residue at \(s=1\) of the Dirichlet
series of \(\lambda_u\) on good ideals, and retain

\[
 P_u=-\kappa_u D\left(\int_0^\infty W(t)\,dt\right)
                   \sum_{Nd\le Y}\frac{c_z(d)\lambda_u(d)}{Nd}.
\tag{2}
\]

The combined primitive conductor and extra deletion modulus is
\(O_{\nu,S}(Nu)\). Nonzero Poisson frequencies give, for every fixed
\(A\ge0\),

\[
 \frac1D\sum_{u\ne0}\Phi(Nu/H)|I_u-P_u|^2
 \ll_{A,\varepsilon}D^\varepsilon
       \frac{H^2Y^2}{D}\left(\frac{HY}{D}\right)^{2A}.
\tag{3}
\]

For \(H=D^h\), \(Y=D^{1-h-\eta}\), fixed \(0<\eta<1-h\), this
decays faster than every prescribed power. The desired full moment
is equivalent to the still-unproved recombined estimate

\[
 \boxed{\frac1D\sum_{u\ne0}\Phi(Nu/D^h)|T_u+P_u|^2
                   \ll_\varepsilon D^{h+a+\varepsilon}.}
\tag{4}
\]

The principal main term stays inside the square with the compensating
tail. At \(h=4/5\), use \(Y=D^{1/5-\eta}\) and seek \(a<1/12\);
at \(h=8/9\), use \(Y=D^{1/9-\eta}\) and seek \(a<1/108\).
This is an alternative full-moment target, not an additional selector
for the old transformed residual.

The tail still has free factors of bounded length, including \(m=1\).
When \(d=ab>Y\), \(Na,Nb\le z\), and \(N(abm)\asymp D\), its
free-factor norm satisfies \(Nm\ll D/Y\). For the displayed choices,
grouping the largest of \(a,b,m\) against the other two gives factor
sizes between fixed multiples of \(Y\) and \(D/Y\). The original
cutoffs, overlaps and principal correction must survive that grouping.
This support statement supplies no bilinear moment estimate.

## Signed gcd recombination and its correct scale

The [gcd recombination](9_SHORT_FAMILY_SIGNED_GCD_RECOMBINATION_20261008.md)
expresses the original coprime off-diagonal core exactly as

\[
 C(D,H)=\sum_d\mu_K(d)B_d(D,H),\qquad
 B_d=\frac1D\sum_{u\ne0}\Phi(Nu/H)
       \left|\sum_{d\mid n}\mu_K(n)\lambda_u(n)W(Nn/D)\right|^2.
\tag{5}
\]

For \(T\ge1\), truncation at \(Nd\le T\) has error

\[
 O_\varepsilon\!\left(D^\varepsilon
      [H+\min\{HD/T,D^2/T^2\}]\right).
\tag{6}
\]

When \(a<h\), \(T=D^{1-(h+a)/2}\) makes that error affordable.
The lossless exponents are \(5/9,3/5,2/3\) at \(h=8/9,4/5,2/3\).
They differ from note 4's transformed overlap cutoff because the row
scale and normalization differ. Since \(B_1=\mathfrak M(D,H)\),
triangle-bounding the positive \(B_d\) retains the unresolved target.

## Quantitative limits of cutting out coherent row cores

Write \(u=\eta vr^6\), with \(v\) sixth-power-free, retaining unit
choices and the finite bad-prime splitting as in note 6. Put

\[
 \tau_{\eta,v}(n)=\nu(n)\chi_n(\eta v),\qquad
 C_{\eta,v}(L)=\sum_{(n,S)=1}\mu_K(n)\tau_{\eta,v}(n)W(Nn/L).
\]

The exact Euler completion of the deletion mask is

\[
 A_{\eta vr^6}(D)=
 \sum_{\operatorname{rad}(d)\mid\operatorname{rad}(r)}
             \tau_{\eta,v}(d)C_{\eta,v}(D/Nd).
\tag{7}
\]

The sum permits all nonnegative exponents at the primes of \(r\);
profile support makes it finite. Zeros \(\tau_{\eta,v}(p)=0\) at
good primes dividing \(v\) remain. The row weight is still
\(\Phi(Nv(Nr)^6/H)\).

Assume explicitly, for some \(\beta>0\), that at all nonempty scales
\[
 |C_{\eta,v}(L)|\ll_\varepsilon
            C_{\eta,v,\varepsilon}L^{\beta+\varepsilon}.
\tag{8}
\]
For \(1\le V\le H\), this implies

\[
 \mathfrak M_{\le V}(D,H)\ll_\varepsilon
 D^{2\beta-1+\varepsilon}H^{1/6}
 \sum_\eta\sum_{Nv\le V}
             C_{\eta,v,\varepsilon}^{\,2}(Nv)^{-1/6}.
\tag{9}
\]

Indeed (7) bounds each masked row by the core estimate times
\(F_\beta(r)=\prod_{p\mid r}(1-(Np)^{-\beta})^{-1}\), using a
smaller preliminary epsilon. The divisor convolution
\(F_\beta^2=\mathbf1*g_\beta\) has nonnegative squarefree-supported
coefficients and

\[
 \sum_d\frac{g_\beta(d)}{Nd}
 =\prod_p\left(1+
 \frac{(1-(Np)^{-\beta})^{-2}-1}{Np}\right)<\infty.
\tag{10}
\]

Ideal counting gives \(\sum_{Nr\le R}F_\beta(r)^2\ll_\beta R\)
for \(R\ge1\). Dyadic shells bound the unchanged Schwartz row
weight by \(O((H/Nv)^{1/6})\), proving (9). Fixed bad-prime factors
change only constants.

A conductor-uniform hypothesis
\(C_{\eta,v,\varepsilon}\ll_\varepsilon(Nv)^\kappa\), \(\kappa\ge0\),
would therefore give

\[
 \mathfrak M_{\le V}(D,H)\ll_\varepsilon
 D^{2\beta-1+\varepsilon}H^{1/6}V^{2\kappa+5/6}.
\tag{11}
\]

Fixed-character bounds alone supply no such growing-\(V\) uniformity.
Even granting the inherited exponent \(7/8\), a fixed finite core
collection has supplied upper-bound exponent \(3/4+h/6\), exactly
the threshold for extracting \(7/8\). This is not a lower bound for
the actual Möbius energy.

For the complementary cores, the imported generic sieve in note 6 gives

\[
 \mathfrak M_{>V}(D,H)\ll_\varepsilon(DH)^\varepsilon
 \left[H+D(H/V)^{1/6}
       +H^{5/6}D^{1/3}+H^{1/3}D^{5/6}\right].
\tag{12}
\]

For each fixed \(r\), keep its column mask and apply that theorem to
cores \(V<Nv\ll H/(Nr)^6\). The \(D\) term is paid only for
\(Nr\ll(H/V)^{1/6}\); the other three divisor sums converge.
Dyadic row shells preserve the Schwartz weight. The imported theorem
and its family transfer have the status recorded in note 6.

Deleting finitely many cores leaves a fixed good core \(v_0\).
A bounded prime-supported column vector
\(\overline{\chi_p(\eta v_0)}\) aligns every row
\(\eta v_0r^6\) with \(Nr\ll(H/Nv_0)^{1/6}\). For large \(D\),
no supported prime divides these \(r\), and the fixed primes of \(v_0\)
are off the profile. For nonnegative nonzero annular \(W\), prime ideal
counting gives the generic normalized lower bound

\[
 \gg D(H/Nv_0)^{1/6}/(\log D)^2.
\tag{13}
\]

If coefficients are parameterized as \(\mu_K\nu\) times a bounded
extra weight, absorb that fixed factor into the weight. Equation (13)
is an obstruction for that broad coefficient class, not for the actual
unrestricted Möbius coefficients.

Even a growing core cutoff leaves the last term of (12), with exponent
\(5/6+h/3\), above every useful budget \(h+a<3/4+h/6\) by more
than \(1/12+h/6\). This comparison says the generic bound is
insufficient; it is not an actual tail lower bound.

## Next bounded task and evidence

The next estimate is (4) at \(h=4/5\), \(a<1/12\), with the
principal correction retained. The centered long free-factor sector
is negligible; the remaining products need a signed bilinear or
multilinear estimate. Test any proposed argument on nonsquarefree
products and coherent rows before taking absolute values. Note 4's
transformed low-overlap residual remains a parallel target.

The [scoped review](../../reviews/SHORT_FAMILY_FACTORIZATION_REVIEW_20261008.md),
[exact checker](../../numerics/check_short_family_factorization.py), and
[small record](../../numerics/short_family_factorization_record_20261008.json)
separate the new deductions, imported analytic inputs and finite checks.
The checker does not verify asymptotic estimates or imported deep theorems.
The new full moment, a stronger zero-free boundary and RH descent remain open.

## Further continuation

[Notes 11--13](13_SHORT_FAMILY_ADAPTIVE_CONTINUATION_20261008.md)
now give a sufficient zero-integral profile class, remove the principal
correction for that class, and replace the uniform cutoff by the
row-dependent \(D^{1-\theta}/(Q_uNE_u)\). A natural prime-by-prime
part of the remaining tail still exceeds every useful budget. The
adaptive signed tail remains unproved; use note 13 as the next starting point.
