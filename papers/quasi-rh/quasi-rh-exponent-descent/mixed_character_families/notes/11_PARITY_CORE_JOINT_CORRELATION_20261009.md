# Parity cores, legal cubic blocks, and the cost of recombination

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Same-model derivations and checks are internal validation, not independent
specialist review or formal proof verification.

**Result.** The current expanded remainder has an exact decomposition by
the squarefree parity cores of both original columns. Below the exterior
radical threshold \(U^{71/125}\), all remaining terms are cross-core
terms, with a second restriction that still depends on the square factors.
Above that threshold the component predicates are automatic, but the
cross-core terms remain. A legal application of de Faveri's squarefree
cubic operator, followed by power extraction, gives a useful bound for
one core with the actual bounded coefficients. Recombining the cores by
positive norm estimates loses the required gain. At the surviving raw
\(pq^2\) geometry it gives middle exponent \(21/50\), versus the
affordable \(0.173181072367\ldots\). This is a method deficit, not an
energy lower bound.

The bounded-coefficient extraction below avoids a power loss within one
core; it does not prove an arbitrary sextic operator. Its native cubic
application retains the finite-presentation transfer obligation. No new
unbounded selected moment or zero-free result is claimed.

## 1 Exact decomposition of the original columns

Use the notation and selectors of [note 8](8_JOINT_MIDDLE_COMPONENT_CONDUCTORS_20261009.md).
Write \(s=s_\chi\in\{1,-1\}\) for the common orientation, and put
\[
 c_k=|B(\mathrm Nk/N)|^2|\nu(k)|^2,
 \qquad d_{u,k}=c_k\chi_k(u)^s.
\]
The fixed ray factor \(\nu\) has already canceled between the two
legs of each complete kernel, leaving its exact modulus squared in
\(c_k\). Its prescribed zeros remain. No replacement of \(\nu\)
by an everywhere nonzero character is made.

Every original good column has a unique factorization
\[
                 k=\alpha r^2,
 \qquad \alpha\text{ squarefree},
 \qquad r\text{ an arbitrary integral good ideal}.
 \tag{1}
\]
The factors can share primes. The original annular condition is
\(\mathrm N\alpha(\mathrm Nr)^2\asymp N\), and the exact coefficient
is \(d_{u,\alpha r^2}\). Define the partial complete kernel
\[
 K_\alpha(u,v)=N^{-1}\sum_r
     d_{u,\alpha r^2}\overline{\chi_{\alpha r^2}(v)}^{\,s}.
 \tag{2}
\]
Then \(K(u,v)=\sum_\alpha K_\alpha(u,v)\), with the full original
columns and normalization.

For \(k=\alpha r^2\), \(l=\beta t^2\), the quadratic component is
\[
 f_2(k,l)=f_2(\alpha,\beta)
        =\alpha\beta/(\gcd(\alpha,\beta))^2.
 \tag{3}
\]
The cubic component is
\[
 f_3(\alpha r^2,\beta t^2)=
 \prod_{v_{\mathfrak p}(\alpha)+2v_{\mathfrak p}(r)
            -v_{\mathfrak p}(\beta)-2v_{\mathfrak p}(t)
                   \not\equiv0\pmod3}\mathfrak p.
 \tag{4}
\]
In particular, the second predicate cannot be replaced by a predicate
on \(\alpha,\beta\) alone.

Let \(\mathcal R_8(u,v,h)\) be precisely the row-only complement
through note 7: pairwise distinct primitive row characters, all six
inherited row complements, \(\mathrm N\xi_{u,h}(v)>U^{103/200}\),
and \(\Phi>\sigma_\kappa(m)\). Keep its original native classes,
physical supports and zeros. For each actual middle row put
\[
 Z=\mathrm N\operatorname{rad}_{\rm good}\xi_{u,h}(v),
 \qquad \Lambda(v)=U^{142/125}/Z^2.
\]
The latest remainder is exactly
\[
 \begin{split}
 J_{\rm rem,comp}=N^{-2}
 \sum_{u,v,h}w_uw_vw_h\overline{S_u}S_h
 \mathbf1_{\mathcal R_8}(u,v,h)
 \sum_{\alpha,\beta}\sum_{r,t}
 d_{u,\alpha r^2}\overline{d_{h,\beta t^2}}
 \overline{\chi_{\alpha r^2}(v)}^{\,s}
                 \chi_{\beta t^2}(v)^s\,
 \mathbf1_{\mathrm Nf_2(\alpha,\beta)>\Lambda(v)}
 \mathbf1_{\mathrm Nf_3(\alpha r^2,\beta t^2)>\Lambda(v)}.
 \end{split}
 \tag{5}
\]
Equation (5) is a reindexing, not a positive enlargement.

For \(Z\le U^{71/125}\), \(\Lambda(v)\ge1\). Thus
\(\alpha=\beta\) is impossible in (5), including at equality.
The same-cube-core pairs are also absent. The remaining cross-core
matrix need not be positive semidefinite: its diagonal vanishes and
an admitted pair has the indefinite two-by-two pattern already
identified in note 8. For \(Z>U^{71/125}\), \(\Lambda(v)<1\), so
both predicates in (5) are automatic. The inner sum then is
\(N^2\sum_{\alpha,\beta}K_\alpha(u,v)
\overline{K_\beta(h,v)}\), with its actual row selector unchanged.
In both ranges, the simultaneous reversal
\((u,h,\alpha,r,\beta,t)\mapsto(h,u,\beta,t,\alpha,r)\)
conjugates the summand and preserves the restrictions.

## 2 A true cubic block inside one parity core

Fix the endpoints and the endpoint-supported factor \(a_0\) in
\(v=a_0pq^2\). The exterior ideals \(p,q\) are squarefree,
pairwise coprime and coprime to the endpoint radical; their original
physical norm coupling is retained. Define the native cubic symbol
\(\eta_r(x)=\chi_r(x)^2\), with the same zero extension.
Multiplicativity gives the exact identity
\[
 \chi_{\alpha r^2}(a_0pq^2)=
       \chi_\alpha(a_0pq^2)\eta_r(a_0)
                           \eta_r(p)\overline{\eta_r(q)}.
 \tag{6}
\]
It holds when factors share primes and at nonunits. Conjugation
preserves zero. For each fixed \(\alpha,a_0,u\), (2) therefore has
the form of a common row factor of modulus at most one times
\[
 N^{-1}\sum_{\mathrm Nr\le L_\alpha}b_r
                   \eta_r(p)\overline{\eta_r(q)},
 \qquad L_\alpha\ll(N/\mathrm N\alpha)^{1/2},
 \qquad |b_r|\ll_{B,\nu}1.
 \tag{7}
\]
The vector \(b_r\) contains the original annulus, endpoint symbols,
\(\eta_r(a_0)\), and all of their zeros. It is independent of the
varying \(p,q\). Removing the common factor's modulus is permissible
only after forming a nonnegative square; its phase is not deleted
from (5).

Write
\[
 C_1(P,Q)=\min(P,Q)^{2/3}\max(P,Q)^{1/3},\qquad
 C_2(P,Q)=\min(P,Q)^{1/3}\max(P,Q)^{2/3}.
\]
De Faveri's Proposition 8.1 gives, for squarefree cubic columns of
length at most \(L\), the operator
\[
        \Omega_3(P,Q,L)=PQ+C_1(P,Q)L+C_2(P,Q)L^{2/3}.
 \tag{8}
\]
The at-most form follows by dyadic subdivision of its stated annular
form. This is a cubic operator; it is not a sextic \(pq^2\)
operator with varying quadratic twists.

**Bounded-coefficient consequence.** Assuming the exact finite
native-to-canonical cubic presentation transfer, for \(|b_r|\le1\)
and unrestricted original \(r\) of norm at most \(L\),
\[
 \sum_{p\asymp P,q\asymp Q}
 \left|\sum_{\mathrm Nr\le L}b_r\eta_r(p)\overline{\eta_r(q)}\right|^2
 \ll_\varepsilon (PQL)^\varepsilon
          L\bigl(PQ+C_1(P,Q)L+C_2(P,Q)L^{2/3}\bigr).
 \tag{9}
\]
All additional actual row restrictions may be retained before the
positive square is enlarged. No row-dependent coefficient is created.

To prove (9), extract the cubic powers of the original square factor:
\[
 r=d e^2 z^3,\qquad d,e\text{ squarefree},\quad(d,e)=1,
 \qquad z\text{ arbitrary}.
 \tag{10}
\]
The ideals \(z\) may share primes with \(d,e\). For each frozen
\((e,z)\), its common row factor is
\[
       \eta_e(p)^{2}\overline{\eta_e(q)}^{\,2}
                        \mathbf1_{(pq,z)=1},
 \tag{11}
\]
while the remaining varying columns are squarefree \(d\) of norm
at most \(L/R\), where \(R=(\mathrm Ne)^2(\mathrm Nz)^3\).
Their exact coefficients are \(b_{d e^2z^3}\), zero outside the
original support and \((d,e)=1\). Formula (11) retains the zeros of
the cubic powers; replacing \(\eta_{z^3}\) by one before its mask
is kept would be false.

For a fixed \(0<\delta<1/6\), Cauchy over \((e,z)\) with weights
\(R^{-1/2-\delta}\) has a bounded first factor: the ideal series
in \(e\) has exponent \(1+2\delta\), and that in \(z\) has
exponent \(3/2+3\delta\). Proposition 8.1, the bound on the
coefficients and ideal counting bound the second factor by
\[
 \sum_{e,z:R\le L}R^{1/2+\delta}
            \Omega_3(P,Q,L/R)\,(L/R).
 \tag{12}
\]
The three terms are respectively
\[
 \begin{split}
 &PQ L\sum R^{-1/2+\delta}\ll_\delta PQ L^{1+\delta},\\
 &C_1 L^2\sum R^{-3/2+\delta}\ll_\delta C_1L^2,\\
 &C_2 L^{5/3}\sum R^{-7/6+\delta}\ll_\delta C_2L^{5/3}.
 \end{split}
\]
In the first line the \(e\)-series costs \(L^\delta\); the
\(z\)-series converges. The latter two double series converge.
Choose \(\delta\) within the permitted loss and allocate the
large-sieve losses separately. This proves (9). Bounded original
coefficients are essential to the \(L/R\) factor in (12).

For comparison, this argument for an arbitrary coefficient vector
with only its total \(\ell^2\) mass known gives the weaker operator
\[
 PQ L^{1/2}+C_1L+C_2L^{2/3}
 \tag{13}
\]
times that mass, up to small losses. The \(PQ L^{1/2}\) arises from
taking the largest \(R^{1/2}\) in the first operator term. Equation
(9) is a consequence for the present bounded vector, not a claim that
(8) holds unchanged for arbitrary unrestricted cubic columns.

## 3 Why core recombination does not close the current remainder

In a dyadic core range \(\mathrm N\alpha\asymp A_0\), there are
\(O(A_0)\) cores and \(L=(N/A_0)^{1/2}\) possible square roots
per core. From (9), the sum of the individual squared norms,
normalized by \(N^2\), is bounded by
\[
 N^{-2} A_0 L\bigl(PQ+C_1L+C_2L^{2/3}\bigr).
 \tag{14}
\]
Across all dyadic ranges this gives the same-core diagonal bound
\[
        \ll U^\varepsilon(PQ+C_1+C_2)/N.
 \tag{15}
\]
Since \(P,Q\ge1\), the leading term is \(PQ/N\). For the full
sum of the cores, positive Cauchy or Hilbert-norm triangle bounds
multiply (14) by an additional \(A_0\):
\[
 N^{-2} A_0^2 L\bigl(PQ+C_1L+C_2L^{2/3}\bigr).
 \tag{16}
\]
Taking \(A_0\asymp N\) gives \(PQ+C_1+C_2\), dominated by
\(PQ\). In that range \(L\asymp1\): each core contains only
boundedly many columns, so there is essentially no cubic column
average within an individual core. Keeping a quadratic phase common
within one core does not make it common between different cores.

The diagonal estimate (15) is also obtainable from the elementary
\(f_2=1\) pair count in note 8. Its good bound is therefore not a
new solution of the correlation problem. Below the radical threshold
all of those diagonal terms have already been removed. Above the
threshold it can bound the diagonal contribution, but supplies no
estimate for the actual cross-core terms.

For general valuation classes
\(\xi=\xi_1\xi_2^2\xi_3^3\xi_4^4\xi_5^5\), one can group
\(p=\xi_1\xi_4\), \(q=\xi_2\xi_5\) in the cubic block and
freeze \(\xi_3\). Its phase is a zero-preserving cubic power mask.
The allocations of primes back to their valuation groups cost only a
divisor factor, but freezing \(\xi_3\) costs its full count. Thus
the leading diagonal estimate remains \(Z/N\), and the naive full
core recombination remains \(Z\), with all physical couplings
retained until positive enlargement. There is no free gain from
changing physical norm into radical norm.

## 4 Exact cost at the surviving raw geometry

Take the current six-prime geometry of note 7:
\[
 u=a_1a_2b,\quad h=a_1a_2c,\quad v=a_1pq^2,
\]
with exponent vector
\[
 (a_1,a_2,b,c,p,q)=
 (21/50,2/25,1/2,1/2,13/50,4/25).
\]
Here \(\log_U Z=21/50<71/125\), and the actual projected
threshold is \(\log_U\Lambda=37/125\). Both row valuation groups
must be averaged jointly for any improvement on the known freezing
bound. The exact cubic-block constants have exponents
\[
 \log_U C_1=29/150,\qquad \log_U C_2=17/75.
\]
For a parity-core scale \(A_0=U^a\), let
\(\lambda=(m-a)/2\). The middle squared-norm exponents from
(14) and (16), respectively, are
\[
 \begin{split}
 D(a)&=a-2m+\max\{21/50+\lambda,
                   29/150+2\lambda,
                   17/75+5\lambda/3\},\\
 R(a)&=2a-2m+\max\{21/50+\lambda,
                   29/150+2\lambda,
                   17/75+5\lambda/3\}.
 \end{split}
 \tag{17}
\]
At \(a=m\), \(D(m)=21/50-m\) and \(R(m)=21/50\).
The full diagonal bound is consequently excellent at the displayed
point, but it is absent from this low-radical remainder. Original
coprime prime columns \(k,l\) satisfy \(r=t=1\),
\(\alpha=k\), \(\beta=l\), and
\(f_2=f_3=kl\). They pass both component conditions because
\(2m>37/125\). Thus the original long prime columns live entirely
in the large-core cross terms; power extraction cannot shorten them.

At the manuscript's rational parameter point the affordable middle
exponent is
\[
 C=T-[2(1-\mu)+g+dm]
      =1-g-(2-2d)m-3s+2\mu
      =0.173181072367\ldots.
\]
The existing sextic grouping gives
\(\Phi=37/150-m/6=0.179042988225\ldots\), whose excess is
\(1487314601/253725000000\). In contrast, the recombined cubic
core method gives \(21/50=0.42\), an excess of
\(41749421609/169150000000=0.246818927632\ldots\).
The lower-order theorem helps inside a core, but the permitted
positive recombination loses much more than the original method.
These costs do not show that the actual arithmetic sum attains them.

## 5 The additional theorem that would be useful

For \(v=a_0pq^2\) in this branch, define the exact cross-core middle
form by the inner sum in (5) restricted to \(\alpha\ne\beta\),
with its factor \(N^{-2}w_v\mathbf1_{\mathcal R_8}\), and sum over
the actual \(p,q\) in one physical dyadic box. Its coefficients are
\(d_{u,\alpha r^2}\overline{d_{h,\beta t^2}}\); its two component
predicates use the actual \(\Lambda(v)\), not its dyadic endpoint.
A uniform bound of this form by \(WU^{C-\epsilon_0}\), for a fixed
\(\epsilon_0>0\) and every operational box, would suffice for that
branch after multiplying by \(A^2N^d\) and allocating losses.
It is stronger than necessary: the signed endpoint aggregate against
\(w_uw_h\overline{S_u}S_h\) could instead be bounded directly.

The missing ingredient is the correlation between distinct quadratic
cores coupled to their cubic responses, with the actual selected
inverse weight. On units the varying quadratic ratio on \(p\) is
\(\overline{\chi_\alpha(p)}^{3s}\chi_\beta(p)^{3s}\).
Its phase cannot be put into fixed column coefficients while \(p\)
is averaged. At nonunits it retains the original masks on
\(\alpha\beta rt\), including primes where either projected phase
cancels. The cubic component also depends on \(r,t\) through (4).
An unfiltered fixed-core theorem or an arbitrary PSD claim for the
high-conductor filter does not estimate this form.

The next bounded arithmetic task is therefore a cross-core estimate
on the actual long-column part, or a weighted endpoint aggregate that
uses the original inverse coefficients. Extending a cubic operator
inside already removed low-radical same-core pairs does not advance
that obligation.

## 6 Sources, transfer status, and checks

The primary source is Alexandre de Faveri, *Optimal large sieve for
fixed order characters*, arXiv:2610.04045v1:
[Theorem 1.1 and construction](https://arxiv.org/html/2610.04045v1#S1.SS1),
[Proposition 8.1 and Remark 8.2](https://arxiv.org/html/2610.04045v1#S8).
Theorem 1.1 has sixth-power-free rows and columns for \(n=6\).
Proposition 8.1 is only \(n=3\) with squarefree columns. Remark 8.2
does not prove the cube-free extension. The bounded-coefficient
deduction (9) uses only the squarefree theorem, with all other power
factors explicitly paid.

Its source family is defined through fixed Kummer and ray-class data;
the manuscript's native symbols must be related to that presentation
by an exact finite-class identity. Squaring a native sixth-order local
symbol gives the cubic local symbol, but that local statement alone
does not verify the global finite-ray phases or generator choices.
The source's reciprocity factor depends only on finite ray classes,
which gives the expected route to the transfer. This note assumes
that exact transfer when applying (8); it does not promote it to a
proved input. In particular no frozen growing \(e,z\) character twist
is required by (12): its entire row multiplier is removed inside a
nonnegative norm, with its zeros accounted for first.

The accompanying `check_mixed_parity_core.py` and small
`mixed_parity_core_check.json` record check zero-preserving local
identities, parity and cubic residue predicates, the canceled-phase
mask, boundary strictness, and the exact rational method deficits.
They do not prove the large sieve, native reciprocity transfer,
selected-bin population, or the cross-core bound.
