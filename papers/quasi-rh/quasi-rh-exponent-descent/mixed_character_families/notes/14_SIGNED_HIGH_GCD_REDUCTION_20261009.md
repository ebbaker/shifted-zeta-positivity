# A high gcd reduction of the selected signed fourth correlation

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex). Reasoning effort: inherited configuration, not exposed;
the exact serving variant is not inferred. Same-model derivations and reviews
are internal validation, not independent specialist review or formal verification.

Equation (5) of [note 13](13_MIXED_FOURTH_CONTINUATION_20261009.md) admits a
new controlled sector. Under the original source's buffered all-length
inverse hypotheses, the part with common gcd norm at least
\(cU^{1/125}\) is affordable with reserve greater than \(1/1000\).
The retained signed correlation has
\[
 \mathrm Ng<cU^{1/125},\qquad
 \mathrm Nf>U^{2r-2/125},\qquad D=U^r.
 \tag{1}
\]
Here \(\operatorname{supp}A_0\subset[c,C]\), with fixed \(0<c<C\).
Thus only nearly coprime inverse pairs with nearly maximal balanced ratio
cores remain. This proves an additional removal, conditional on the
existing source analytic package. It does not prove the remaining
correlation, a mixed moment, or a new zero-free boundary.

The key step is to restore all ratio cores at a fixed gcd before applying
coprimality inversion. That inversion retains cancellation in shorter
inverse squares. The original ratio cutoff is then restored by subtracting
its already controlled small-core part.

## 1 The original weight and the required source scope

Retain the original native characters and physical zeros, whole slots,
annular inverse profile, and sharply selected weight
\[
 V_u=\mathbf1_{\mathcal C_+}(u)|S_u|^4|Q_J(u)|^2,
 \qquad \sum_u V_u\ll_\varepsilon U^{1+\varepsilon}H^b.
 \tag{2}
\]
The legal selected fourth mass and every profile, derivative and height
condition remain as in [note 10](10_MOBIUS_RATIO_CORE_FOURTH_20261009.md).
All ideals below are good. The requested fourth saving is
\(\chi_*=1/540\).

The local inverse input used here is the underlying all-length statement
of Lemma 8.2 of the
[30 September companion paper](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf),
pp. 57–58, with its original buffered row hypotheses. It permits a fixed
bounded nonnegative range of inverse lengths, uniform annular profiles,
and the original pure twists and cumulative frequency allocation. In
the present notation it gives
\[
 \left|\sum_n\mu_F(n)\psi_u(n)A_0(\mathrm Nn/X)\right|^2
 \ll_\varepsilon U^\varepsilon H^{b_1}X^{1+d},
 \qquad d=2a-1,
 \tag{3}
\]
uniformly for \(1\le X\le CD\) within that enclosing range. Its preliminary
buffers and finite height orders must be chosen in the source's prescribed
order. The original height admissibility and derivative-profile families
are retained. No all-height extension beyond that source scope is inferred.

The bound at only the original length \(X=D\), as displayed in the mixed
manuscript, would not alone imply (3). This deduction uses the source's
all-length pointwise lemma, and does not import a marked moment at a
smaller physical row scale. Its deep analytic proof remains an input.
The primary PDF inspected in memory has SHA-256
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.

Equations (3) and (8) use the source's procedure that selects its preliminary
buffer for the requested small loss before fixing the final height order.
If that buffer has already been fixed, its literal contour exponent must
instead be retained as \(d+\rho\), \(\rho\ge0\); it cannot be absorbed
into every arbitrarily small loss. The high-gcd power then becomes
\(1+dr-d/125+\rho(r-1/125)\). A sufficient concrete allocation is
\(\rho\le1/100000\), followed by a separate allocation for the remaining
small losses: the reserve is still greater than \(1/1000\), since
\[
 \frac{347}{337500}
 -\frac1{100000}\left(\frac{73}{100}-\frac1{125}\right)
 >\frac1{1000}.
 \tag{3a}
\]
The application must either make this choice in the permitted source order
or use its actual \(\rho\) in the inequalities. Availability of a fixed
buffer satisfying this requirement is not inferred from a single
pointwise bound. The global fallback in section 6 needs only its stated
global family scope.

## 2 The shortened inverse retains a growing deletion mask

For an ideal \(q\) of polynomial norm, define
\[
 Z_q(u;X)=\sum_{(v,q)=1}\mu_F(v)\psi_u(v)A_0(\mathrm Nv/X).
 \tag{4}
\]
There is no assertion that arbitrary bounded inverse coefficients obey
(3). Instead, an exact convolution extends (3) to this particular mask.
Let \(b_q(k)=\psi_u(k)\) if every prime factor of \(k\) divides \(q\),
and let it vanish otherwise. Complete multiplicativity, including zero
values, gives
\[
 \mu_F\psi_u\,\mathbf1_{(\,\cdot\,,q)=1}
     =(\mu_F\psi_u)*b_q.
 \tag{5}
\]
At a deletion prime the local series multiply to
\((1-\psi_u(p)t)/(1-\psi_u(p)t)=1\). A physical zero gives the same
identity with both series equal to one. Consequently
\[
 Z_q(u;X)=\sum_{k:\operatorname{supp}(k)\subseteq\operatorname{supp}(q)}
 \psi_u(k)\sum_v\mu_F(v)\psi_u(v)
                 A_0\!\left(\frac{\mathrm Nv}{X/\mathrm Nk}\right).
 \tag{6}
\]
The sum is finite: \(\mathrm Nk\le CX\) is necessary. Each inner profile
is the original \(A_0\) at a shorter length, with the same character and
frequency allocation. There is no new twist or altered physical row set.

Put \(a=(1+d)/2\), so \(a\ge17/25\). For \(X/\mathrm Nk\ge1\), (3)
bounds the inner sum by
\(U^\varepsilon H^{b_2}(X/\mathrm Nk)^a\). For
\(1/C\le X/\mathrm Nk<1\), finite ideal counting gives the same bound
after changing a constant; smaller lengths give zero. Hence
\[
 |Z_q(u;X)|
 \ll U^\varepsilon H^{b_2}X^a
       \prod_{p\mid q}(1-(\mathrm Np)^{-a})^{-1}.
 \tag{7}
\]
For any fixed \(\sigma_0>0\) and arbitrary \(\varepsilon_1>0\), this
product for \(a\ge\sigma_0\) is
\(O_{\sigma_0,\varepsilon_1}((\mathrm Nq)^{\varepsilon_1})\).
Separate finitely many small primes; at each remaining prime its factor
is at most \((\mathrm Np)^{\varepsilon_1}\). Polynomial norm of \(q\)
therefore absorbs the factor into the arbitrary small loss. Squaring
and reallocating losses proves
\[
 \boxed{|Z_q(u;X)|^2\ll_\varepsilon
           U^\varepsilon H^{b_3}X^{1+d}.}
 \tag{8}
\]
This is uniform for \(1/C\le X\le CD\), \(\mathrm Nq\le CD\).
The same argument applies to the original permitted derivative profiles.
Fixed logarithmic factors from differentiating pure norm phases are
absorbed into the loss, with the finite source height order retained.

## 3 Coprimality inversion before imposing the ratio cutoff

For each squarefree original gcd \(g\), \(G=\mathrm Ng\), write
\[
 T_g(u)=\sum_{\substack{a,b\ \mathrm{squarefree}\\
                         (a,b)=1,\ (ab,g)=1}}
 \mu_F(a)\mu_F(b)\psi_u(a)\overline{\psi_u(b)}
 A_0(G\mathrm Na/D)\overline{A_0(G\mathrm Nb/D)}.
 \tag{9}
\]
Both inverse annuli remain unchanged. There is no ratio-core cutoff
inside (9). The original selected moment is exactly
\[
 F_J=D^{-1}\sum_g\sum_u V_u|\psi_u(g)|^2T_g(u).
 \tag{10}
\]
Insert \(\mathbf1_{(a,b)=1}=\sum_{h\mid(a,b)}\mu_F(h)\), then put
\(a=hv,b=hw\). Since \(a,b\) are squarefree, \(h,v,w\) are
squarefree, \((h,g)=1\), and \((vw,gh)=1\); \(v,w\) may share primes.
The two coefficient signs at \(h\) square away, while its character
phase cancels with its conjugate and leaves its zero mask. This proves
\[
 \boxed{
 T_g(u)=\sum_{\substack{h\ \mathrm{squarefree}\\(h,g)=1}}
 \mu_F(h)|\psi_u(h)|^2
 \left|Z_{gh}\!\left(u;\frac D{G\mathrm Nh}\right)\right|^2.
 }
 \tag{11}
\]
The exterior mask \(|\psi_u(g)|^2\) is still present in (10). It combines
with the mask at \(h\) to \(|\psi_u(gh)|^2\), including every canceled
physical zero and fixed ray factor. The profiles make (11) finite and
force \(G\mathrm Nh\le CD\).

Equation (11) is an alternating sum of squares, not a positive Gram
form after filtering. It preserves the cross terms inside each shortened
inverse sum before taking an absolute bound.

Applying (8), and then the convergent ideal sum at exponent \(1+d\),
gives
\[
 |T_g(u)|\ll_\varepsilon U^\varepsilon H^{b_3}(D/G)^{1+d}.
 \tag{12}
\]
The convergence is uniform for \(d\in[9/25,21/50]\).

## 4 The newly controlled high gcd sector

Let \(\mathcal A(G_0)\) denote (10) restricted to \(G\ge G_0\), with
all ratio cores retained. For \(G_0\ge1\), (2), (12), and ideal counting
give
\[
 \begin{aligned}
 |\mathcal A(G_0)|
 &\ll U^{1+\varepsilon}H^bD^{-1}D^{1+d}
               \sum_{\mathrm Ng\ge G_0}(\mathrm Ng)^{-1-d}\\
 &\ll U^{1+\varepsilon}H^bD^dG_0^{-d}.
 \end{aligned}
 \tag{13}
\]
The normalization is still the original \(D^{-1}\). Choose
\[
 G_0=cU^{1/125}.
 \tag{14}
\]
It is at least one for sufficiently large \(U\). The fixed factor
\(c^{-d}\) belongs to the profile constant. Thus
\[
 |\mathcal A(G_0)|\ll U^{1+dr-d/125+\varepsilon}H^b.
 \tag{15}
\]
Its reserve against the common target is uniformly at least
\[
 \boxed{\frac{d}{125}-\frac1{540}
  \ge\frac9{3125}-\frac1{540}
  =\frac{347}{337500}>\frac1{1000}.}
 \tag{16}
\]

To control the high-gcd portion of the actual large-ratio sum, subtract
from \(\mathcal A(G_0)\) its terms with \(\mathrm N(ab)\le U^{1/2}\).
The absolute bound for any subset of that old small-core sector is
\(O(U^{5/4+\varepsilon}H^b)\). Therefore
\[
 |F_{J,>1/2;\,G\ge G_0}|
 \ll U^\varepsilon H^b
       \left(U^{1+dr-d/125}+U^{5/4}\right).
 \tag{17}
\]
[Note 9](9_OPERATIONAL_FOURTH_BUDGET_20261009.md) supplies the separate
small-core reserve \(dr-1/540-1/4>1/500\) on its operational wedge.
The combined reserve in (17) consequently exceeds \(1/1000\).
All source buffer, divisor, profile and height losses must be allocated
strictly inside these reserves. This estimates the full high-gcd signed
aggregate; it does not bound each ratio packet separately.

## 5 The exact remaining target

Define
\[
 \mathcal R_{J,\mathrm{near}}=
 D^{-1}\sum_{\substack{g,a,b\ \mathrm{squarefree}\\
                 \text{pairwise coprime}\\\mathrm Ng<cU^{1/125}}}
 \mu_F(a)\mu_F(b)
 A_0(\mathrm N(ga)/D)\overline{A_0(\mathrm N(gb)/D)}
 \sum_u V_u|\psi_u(g)|^2
          \psi_u(a)\overline{\psi_u(b)}.
 \tag{18}
\]
The original supports force
\(cD\le G\mathrm Na,G\mathrm Nb\le CD\). In (18), they imply
\[
 \mathrm Nf=\mathrm N(ab)\ge(cD/G)^2
                       >U^{2r-2/125}.
 \tag{19}
\]
The coarse working domain gives \(2r-2/125\ge173/125=1.384\), so the
old \(\mathrm Nf>U^{1/2}\) restriction is automatic there for \(U>1\).
Pair reversal makes (18) real. With the exact gcd boundary of (14),
\[
 F_{J,>1/2}=\mathcal R_{J,\mathrm{near}}
       +F_{J,>1/2;\,G\ge G_0}.
 \tag{20}
\]
Consequently (5) of note 13 reduces, with the displayed positive reserve,
to the one-sided estimate
\[
 \boxed{(\mathcal R_{J,\mathrm{near}})_+
          \ll_\varepsilon U^{1+dr-1/540+\varepsilon}H^b.}
 \tag{21}
\]
It is still unproved. The restrictions on \(g\) and \(f\) must remain
together. Removing the gcd condition and merely requesting a bound for
all cores above the new edge would define a different signed form.

The \(g=1\) sector survives. Its two cofactor norms are of order \(D\),
and balanced two-prime cores still have positive Möbius sign. The local
inverse envelope at the original length gives only \(U^{1+dr}\) after
the fourth mass, so it supplies no final \(1/540\) gain in this sector.
Entrywise absolute kernels or scalar Möbius sums do not control its
moving selected weight.

There is also an exact square-aggregate presentation. For squarefree \(q\),
put
\[
 \lambda_{G_0}(q)=\sum_{\substack{g\mid q\\\mathrm Ng<G_0}}
                        \mu_F(q/g).
 \tag{22}
\]
Reindexing (11) by \(q=gh\) gives
\[
 \mathcal R_{J,\mathrm{near}}=D^{-1}\sum_uV_u
 \sum_{q\ \mathrm{squarefree}}
 \lambda_{G_0}(q)|\psi_u(q)|^2
             |Z_q(u;D/\mathrm Nq)|^2.
 \tag{23}
\]
Only \(\mathrm Nq\le CD\) contribute. For \(G_0>1\),
\(\lambda_{G_0}(1)=1\), and \(\lambda_{G_0}(q)=0\) when
\(1<\mathrm Nq<G_0\). Above the cutoff it has both signs.
This form retains all selected fourth correlations across shortened
inverse responses. It introduces no positivity after the signed filter.
Estimating its terms with \(\mathrm Nq\ge G_0\) absolutely via (8)
only recovers that (23) differs from the original fourth moment by an
affordable error; the \(q=1\) term is precisely that original moment.
Thus (23) cannot yield the missing gain by another application of (8).

## 6 A global fallback and finite prime completion

The same algebra works with any shortened inverse exponent \(\kappa>0\):
the full high-gcd cost is \(UD^\kappa G_0^{-\kappa}\).
The inherited global reciprocal strip at \(7/8+\varepsilon\) supplies
\(\kappa=3/4\) instead of the local \(d\). Taking
\(G_0=cDU^{-1/3}\) costs \(U^{5/4}\) and leaves the coupled conditions
\(\mathrm Ng<cDU^{-1/3}\), \(\mathrm Nf>U^{2/3}\).
This is a weaker fallback if the precise buffered local input is not
available. A zeta-only strip cannot replace the required family input.

[Note 15](15_FINITE_PRIME_COMPLETION_20261009.md) completes all states
at a prescribed small-prime mask in a way compatible with (18). For a
row-independent squarefree \(P\) with \(\mathrm NP\le U^{1/25000}\),
put \(K=G_0/\mathrm NP\). Complete the states of \(P\) on pairs whose
\(P\)-free gcd has norm below \(K\). Every completed term still has
full gcd norm below \(G_0\). The complementary boundary is a union of
whole original fixed-gcd sectors with norm at least \(K\), so (12)
controls it without imposing a filter inside an inverse square.
Its cost is \(UD^dK^{-d}\), leaving uniform reserve
\[
 \frac9{25}\left(\frac1{125}-\frac1{25000}\right)-\frac1{540}
 =\frac{17107}{16875000}>\frac1{1000}.
 \tag{24}
\]
The fixed source-buffer allowance \(\rho\le1/100000\) also preserves
reserve greater than \(1/1000\) here. The completed selected correlation
remains unproved. No source estimate is applied to its row-dependent
transformed profile. Note 15 separately records the original half-power
ratio completion and its wider prime-mask budget; its elementary crossing
bound is not used at the nearly maximal core edge.

## 7 Verification and mathematical status

The standard-library
[checker](../../numerics/check_mixed_signed_gcd.py) and its
[record](../../numerics/mixed_signed_gcd_record_20261009.json) make 2,161
exact assertions. They verify deletion convolution, fixed-gcd inversion,
the low-gcd signed square aggregate, both native orientations, complex
profiles, strict ratio cutoffs, essential canceled zero masks, and the
rational reserve. The checker prints JSON and writes no files. It reuses
the exact phase module from note 10 and records both source hashes.

The formal profiles and phases test algebra, not source smoothness,
native reciprocity, a selected zero population, or an unbounded moment.
The analytic deduction (13) uses (3), the legal fourth mass, elementary
Euler-factor bounds and ideal counting. Its reviews distinguish this
conditional proof from the still open estimate (21): see the
[source scope review](../../reviews/MIXED_SHORT_MASKED_INVERSE_SCOPE_REVIEW_20261009.md),
[gcd algebra review](../../reviews/MIXED_SIGNED_GCD_REVIEW_20261009.md), and
[completion review](../../reviews/MIXED_FINITE_PRIME_COMPLETION_REVIEW_20261009.md).
The actual whole-slot
and witness certificate, all original profile/height conditions, complete
bin coverage and the later family-boundary reuse obligations remain.
