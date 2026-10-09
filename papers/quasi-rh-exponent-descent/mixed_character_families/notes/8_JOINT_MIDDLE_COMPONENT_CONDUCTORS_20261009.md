# Joint middle sums and coupled component conductors

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel derivations and audits are same-model internal validation, not
independent specialist review or formal proof verification.

**Result.** Expanding the two complete kernels gives a new controlled
piece of the actual mixed chain. Its predicate couples the exterior
radical of the middle row to the quadratic or cubic component conductor
of a pair of plain columns. The uniform reserve is \(927/500000\).
The exact remaining sum retains all eight row conditions from
[note 7](7_VALUATION_FACTOR_SECTORS_AND_INVERSE_RATIO_FOURTH_20261009.md)
and requires both coupled component conductors to exceed the new cutoff.
This is a column-pair refinement, rather than a bound for another entire
physical row sector. The full joint \(pq^2\) sum remains open.

The deduction uses elementary ideal-pair counting and the inherited
selected mass, pointwise weight and endpoint estimates. A check of the
primary sextic-sieve source also identifies a genuine joint cubic
operator; its hypotheses do not supply the remaining sextic estimate.
The separate operator norms and the global inverse mass do not provide
the needed joint gain. The active investigation remains mixed character
families, with session base `6c343e83622e194268399033b2eee68cc7e5fbcd`.

## 1 The two-kernel expansion with its actual weight

Retain the notation, original physical rows, selector, smooth annulus,
inverse cutoff, prime slots and finite presentation of note 7. In
particular,
\[
 N=U^m,\quad w_u=\mathbf1_{\mathcal C_+}(u)|M_r(u)Q_I(u)|^2,
 \quad A=\sum w_u\ll U^{1-\mu+\varepsilon}\mathcal H^b,
 \quad W=\max w_u\ll U^{g+\varepsilon}\mathcal H^b.
\]
The endpoint product has bound \(N^dU^\varepsilon\mathcal H^b\),
and the sufficient cubic-probe exponent is \(T=3(1+dm-s)-2m\).
After the fixed native presentation, put
\[
 c_k=|B(\mathrm Nk/N)|^2|\nu(k)|^2,
 \qquad \Gamma_{k,l}(v)=\overline{\chi_k(v)}^{s_\chi}
                                      \chi_l(v)^{s_\chi}.
\]
Here \(s_\chi\in\{1,-1\}\) is the common orientation. Each
character is zero-extended; every original deletion zero is included.
The two complete kernels give exactly
\[
 K(u,v)K(v,h)=N^{-2}\sum_{k,l}c_kc_l
           \chi_k(u)^{s_\chi}\overline{\chi_l(h)}^{s_\chi}
           \Gamma_{k,l}(v).
 \tag{1}
\]
The original row predicate in \(J_{{\rm rem},8}\) can therefore be
retained in this finite column expansion. No coefficient or selector
is changed. Profiles supply the same bounded seminorms and polynomial
height costs as in the previous notes.

For fixed endpoints, let \(\xi=\xi_{u,h}(v)\) be the exterior
middle ideal of note 6 and define its **radical norm**
\[
             Z_{u,h}(v)=\mathrm N\operatorname{rad}_{\rm good}\xi.
 \tag{2}
\]
This differs from the full physical norm used by the sieve in notes 6--7.
It is used here only in an elementary count. The actual row still has
its original valuations, physical norm and weight.

If \(v=a p q^2\) on a fixed endpoint-supported/unit/bad-prime
class, the exact middle sum in (1) contains
\[
 \sum_{p,q\ {\rm actual}}w_{a p q^2}\,
       \Gamma_{k,l}(a)\Gamma_{k,l}(p)\Gamma_{k,l}(q)^2,
 \tag{3}
\]
with squarefree, pairwise-coprime \(p,q\), their original physical
norm coupling, and all eight row conditions. Equation (3) does not
factor into independent \(p\) and \(q\) sums with this weight.

## 2 Good quadratic and cubic component conductors

For \(j=2,3\), define the good ideals
\[
 f_j(k,l)=\prod_{\substack{\mathfrak p\ {\rm good}\\
             v_\mathfrak p(k)-v_\mathfrak p(l)\not\equiv0\pmod j}}
                 \mathfrak p.
 \tag{4}
\]
They are symmetric in \(k,l\). For the sixth-order ratio, \(f_2\)
is the growing conductor of its quadratic projection, and \(f_3\)
of its cubic projection. Their least common multiple is the good
sixth-order ratio conductor \(f_6\). Fixed bad-prime and unit/ray
factors remain in the actual quotient and are not used to define these
good-part cuts. A statement about the full primitive order would need
those fixed factors too.

The inherited ratio identity in \(\Gamma_{k,l}\) retains the
canceled-phase mask at primes where both columns have positive valuation
and their difference is zero modulo six. Projecting further to order two
or three can cancel other phases, but their zero extensions remain.
In particular, replacing either projection by its primitive character
and dropping those extra masks is not part of this argument. The bound
\(|\Gamma_{k,l}(v)|\le1\) is used on the whole original product.

For \(V\ge1\), good column ideals of norm at most \(C_BN\)
satisfy the elementary pair estimate
\[
 \boxed{\#\{k,l:\mathrm Nk,\mathrm Nl\le C_BN,
                      \mathrm Nf_j(k,l)\le V\}
       \ll_\varepsilon N^{1+\varepsilon}V^{1/2+\varepsilon},
                \qquad j=2,3.}
 \tag{5}
\]
To prove this, write \(k=gA,l=gB\), \((A,B)=1\), and extract
\(j\)-th powers uniquely:
\[
             A=a_0a^j,\quad B=b_0b^j,
             \quad f_j=\operatorname{rad}(a_0b_0).
\]
At each prime of \(f_j\) there are \(2(j-1)\) allocations to
one side and a valuation \(1,\ldots,j-1\). Counting \(g\)
gives the positive majorant
\[
 \frac{C N}{\max\{\mathrm Na_0(\mathrm Na)^j,
                         \mathrm Nb_0(\mathrm Nb)^j\}}
 \le\frac{C N}{\sqrt{\mathrm N(a_0b_0)}(\mathrm N(ab))^{j/2}}
 \le\frac{C N}{\sqrt{\mathrm Nf_j}(\mathrm N(ab))^{j/2}}.
\]
If the allowed norm of \(g\) is below one, its actual count is
zero. For \(j=3\), both ideal series at exponent \(3/2\)
converge. For \(j=2\), keep the physical bounds
\(\mathrm Na,\mathrm Nb\ll\sqrt N\); the harmonic ideal sums
cost at most \(O(\log^2(2N))\). Summing \(f_j\) with its
bounded-allocation divisor factor proves (5), by the same ideal-counting
and partial-summation argument as `lem:pair-count` in the
[character-amplification manuscript](../../../quasi-rh-character-amplification/manuscript.tex).

In particular, \(f_2=1\) or \(f_3=1\) allows only
\(O(N^{1+\varepsilon})\) pairs. Small projected conductors are
more general: a ratio may have both order components nontrivial while
one has small good conductor. The union of the two conditions in (5)
costs only a factor two.

## 3 The coupled norm and component-conductor cut

For fixed endpoints, the number of actual middle rows with
\(H\le Z<2H\) is
\[
                          O(U^\varepsilon H).
 \tag{6}
\]
Indeed endpoint-supported valuations have
\(6^{\omega(\operatorname{rad}_{\rm good}(uh))}\ll U^\varepsilon\)
choices. For each exterior squarefree radical, its valuations have
\(5^{\omega(\operatorname{rad}\xi)}\ll U^\varepsilon\) choices.
Ideal counting gives \(O(H)\) radicals in that norm range, and
unit/fixed bad-prime classes are bounded. The original physical norm,
selector, primitive-conductor gate and earlier cuts only restrict this
positive count. No physical sieve is indexed by \(Z\).

In the expanded \(J_{{\rm rem},8}\), assign the new removed piece
\(J_{\rm comp}\) by the actual coupled predicate
\[
 \boxed{Z_{u,h}(v)^2\min\{\mathrm Nf_2(k,l),\mathrm Nf_3(k,l)\}
                            \le U^{142/125}.}
 \tag{7}
\]
Equality belongs to this side. On a dyadic interval \(H\le Z<2H\)
the admitted columns have at least one projected conductor at most
\(V_H=U^{142/125}/H^2\). If \(V_H<1\), there are no admitted
tuples. Otherwise, (5)--(6) bound their number by
\[
 U^\varepsilon H\cdot N^{1+\varepsilon}\sqrt{V_H}
                           \ll U^\varepsilon N U^{71/125}.
 \tag{8}
\]
Thus the exterior radical and the column-pair count are paid together.
The automatically bounded range \(Z\le U^{71/125}\), the last
partial dyadic interval and logarithmically many intervals cause only
fixed constants and \(U^\varepsilon\) costs.

Bound the original selected middle weight by \(W\) in this positive
tuple majorant, retain the bounded actual column coefficients, use the
\(N^{-2}\) normalization in (1), and sum the actual endpoint weights
and plain amplitudes. This proves
\[
 \boxed{|J_{\rm comp}|\ll
                  A^2W N^{d-1}U^{71/125+\varepsilon}\mathcal H^b.}
 \tag{9}
\]
No signed kernel is enlarged, and no selected sum is fed into a
complete-row Poisson formula. This bound requires no new analytic
large-sieve theorem beyond the inherited inputs for \(A,W\) and the
endpoint amplitudes.

Its reserve below \(T\) is
\[
 \Delta_{\rm comp}=1-\frac{71}{125}-g-(1-2d)m-3s+2\mu.
 \tag{10}
\]
Use \(g\le d(1+r)/2\), \(\mu\ge0\), and the same coarse
operational region as note 7. The resulting lower expression decreases
with \(r,m,s\), and with \(d\), since
\(2m-(1+r)/2<0\). At
\(d=21/50,r=73/100,m=207/500,s=101/500000\), it equals
\[
                  \boxed{\Delta_{\rm comp}\ge927/500000=0.001854.}
 \tag{11}
\]
At the exact point of note 5 it is
\(108685273/9950000000=0.0109231430151\ldots\).
These reserves are subject to the same sufficiently small analytic
losses, fixed-parameter ordering and polynomial height uniformity as
the earlier conditional estimates.

## 4 The remaining expanded chain

Let \(J_{{\rm rem},{\rm comp}}\) retain every original endpoint,
middle and column coefficient, all masks, all eight strict row conditions
of note 7, and both additional conditions
\[
 Z_{u,h}(v)^2\mathrm Nf_2(k,l)>U^{142/125},\qquad
 Z_{u,h}(v)^2\mathrm Nf_3(k,l)>U^{142/125}.
 \tag{12}
\]
Then
\[
 J_{{\rm rem},8}=J_{{\rm rem},{\rm comp}}+J_{\rm comp},
\]
and, since \(927/500000>19/12500\),
\[
 \boxed{J_\ne=J_{{\rm rem},{\rm comp}}
           +O(U^{T-19/12500+\varepsilon}\mathcal H^b).}
 \tag{13}
\]
This is an exact column refinement of the eight-row-cut remainder.
Its retained pairwise-inequivalent row characters and column conditions
must be imposed in the expanded expression (1); it is not written as
two untouched complete kernels. Simultaneous reversal
\((u,h,k,l)\mapsto(h,u,l,k)\) conjugates the summand and preserves
both predicates, so the remainder is real. Its one-sided upper bound at
exponent \(T\) remains unproved.

For the six-prime row pattern in note 7, \(Z\) has power \(21/50\).
Predicate (7) therefore admits component conductors up to power
\[
                    142/125-2(21/50)=37/125=0.296.
\]
This controls proper good-order column quotients and also full good-order
six quotients with one small component. It does not control the full row
pattern. Choose distinct coprime squarefree good prime columns \(k,l\)
in the original plain annulus. Then \(f_2=f_3=kl\), and the two
products in (12) have power
\[
                    21/25+2m>142/125.
 \tag{14}
\]
Thus a raw column range survives together with the row pattern.
Nonzero actual coefficients or weight in a compatible selected bin are
not asserted by this norm bookkeeping.

For \(Z\le U^{71/125}\), the high-component pair indicator has
zero diagonal. If it admits an off-diagonal pair, its two-by-two
principal block is \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\),
which is indefinite. The retained column filter therefore cannot be
treated as a positive Gram form in general. Positive weighted-kernel
averages remain sufficient bounds for the original whole middle block,
but positivity is not inherited by the new high-component restriction.

## 5 What the available joint operators do and do not supply

On an unweighted product rectangle, the column covariance of the
\(pq^2\) family is the entrywise product of the sextic \(p\)
covariance and the cubic-power \(q\) covariance. Positive enlargement
to that rectangle is legal after using \(W\); the actual weight in
(3) does not itself factor. The general positive-matrix entrywise-product
bound recovers count-one-factor/sieve-the-other. Aligned positive block
matrices can attain that bound, so separate operator norms and their
diagonals alone give no forced improvement. This is a matrix-method
limitation, not an arithmetic lower bound for this family.

The primary source does contain a joint arbitrary-coefficient operator:
[de Faveri Proposition 8.1, equation (8.1)](https://arxiv.org/html/2610.04045v1#S8).
For cubic characters and squarefree columns of norm scale \(L\), its
bound for rows \(ab^2\) at scales \(P,Q\) is
\[
 PQ+\min(P,Q)^{2/3}\max(P,Q)^{1/3}L
      +\min(P,Q)^{1/3}\max(P,Q)^{2/3}L^{2/3},
\]
up to the permitted epsilon factor. Its proof uses the cubic identity
\(\chi(b)^2=\overline{\chi(b)}\). That identity fails for a
general sextic character. Remark 8.2 also leaves a cube-free-column
extension as additional work. Neither that proposition nor the fixed-twist
central \(L\)-value moment in Theorem 1.2 is applied here as a
sextic operator.

Algebraically \(\chi_6=\chi_6^3\chi_6^4\), including the original
zero values. In a sextic \(pq^2\) row the quadratic phase varies
with \(p\) and the column. It cannot be absorbed into one fixed column
coefficient vector for a joint cubic operator. Fixing a column parity
core can remove that phase from its positive square, but cross-core
terms remain; their small projected-conductor part is what (7) pays.
Replacing the whole retained sum by independent cubic and quadratic
averages would discard the needed correlation.

## 6 The next bounded correlation test

The next actual joint target is the signed \(pq^2\) sum (3) with
both restrictions (12), including the quadratic moving phase in \(p\).
One concrete way to begin is to resolve the column parity cores while
retaining their cross terms, and determine whether the quadratic
component oscillation can be used together with the cubic \(q\)
average. A joint positive covariance estimate would be sufficient for
the original whole block; the restricted endpoint form needs its own
signed estimate.

At note 7's exact point, put
\(C=29293578391/169150000000\), the middle exponent after paying
\(W\). For the actual selected block \(\mathcal A(u,h,a)\), a
sufficient positive weighted estimate is
\[
 \sum_{v\in\mathcal A(u,h,a)}w_v|K(u,v)|^2
                 \ll WU^{C+\varepsilon}\mathcal H^b,
 \tag{15}
\]
uniformly in its fixed endpoints and factors, together with the analogous
estimate for \(h\). Weighted Cauchy would then control the whole middle
block.
The existing one-factor cost \(37/150-m/6\) exceeds \(C\) by
\(1487314601/253725000000\), approximately \(0.005861916\).
The new removed column piece is below the target, but supplies no saving
on the complementary large-component pairs. A gain of that size must
come from joint phases or the actual weight/kernel correlation.

The global selected inverse mass alone is weaker than the local
count-times-\(W\) bound on this block. Applying the marked inverse
theorem with the shorter \(p\) or exterior physical scale is also
unavailable: the actual inverse length remains \(U^r\), and its
relative length/capacity conditions would fail. The direct large
inverse-ratio fourth-moment target from note 7 remains a parallel open
route. No inverse reflection across a selected zero is used.

## 7 Finite checks and analytic scope

The [checker](../../numerics/check_mixed_joint_component.py) and
[small record](../../numerics/mixed_joint_component_record_20261009.json)
verify formal zero-extended quotient and projection identities, the
actual weighted two-kernel expansion, the coupled predicate and its
strict complement, reversal and exact signed decomposition, formal
\(pq^2\) blocks and surviving column norms, the indefinite high-pair filter and
rational reserves. They check finite algebra and bookkeeping, not the
asymptotic ideal-pair estimate or a native residue-symbol realization.

Two fresh replays match byte for byte: **312,257 exact assertions**.
They include nontrivial canceled-phase zeros, nonzero removed and retained
off-diagonal terms, an exact negative restricted-chain witness and abstract
entrywise-product norm saturation. The record SHA-256 is
`fa96f75c34ee3c0f674b5e054d19ee8f17c814674a8d3e1e0fc7f46b27f68812`.

The [scoped review](../../reviews/MIXED_JOINT_COMPONENT_REVIEW_20261009.md)
audits the pair count, norm coupling, operator scope and retained
correlations. The native presentation, imported selected mass/plain
inputs, continuous parameter certificate and uniform profile/height
requirements retain their conditional status. No new full mixed moment,
scalar exponent, zero-free boundary or RH implication is proved.
