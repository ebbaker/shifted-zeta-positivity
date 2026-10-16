# Squarefree rough parity and the high-conductor triple sector: scoped review

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This same-model mathematical audit is internal validation, not independent
specialist review or formal proof verification.

## Scope and conclusion

[Note 21](../short_families/notes/21_SHORT_FAMILY_ROUGH_PARITY_20261008.md)
shows that the squarefree coefficient at the actual buffer
\(\theta=11/20\) admits
a complete small-prime/rough-prime split. When the complete small-prime
part fits below the adaptive threshold, an odd number of rough prime
factors makes the coefficient exactly zero. This gives a new nonempty
signed zero-sector with three rough primes and a small cofactor of
growing power width on high-conductor rows. Its complete Schwartz-weighted
energy is arbitrarily small.

The conclusion is local to this selected response and these rows. Balanced
semiprimes retain coefficient \(+2\) on every significant row, and balanced
triples retain coefficient \(-6\) on the coherent inner rows. The generic
physical operator still supplies only its existing exponent \(16/15\)
for the retained response. No full-moment or zero-free improvement follows.

## 1. Exact parity calculation and necessary endpoints

On the fixed profile annulus, for sufficiently large \(D\), write
\[
 z=\sqrt{CD},\qquad Y_u=D^{9/20}/L_u<z,
\]
and retain the manuscript's zero extensions. For squarefree \(n\),
\[
 t_{z,Y}(n)=\mu_K(n)+
       \sum_{d\mid n,\ Nd\le Y}(-2)^{\omega(d)}.
 \tag{1}
\]
The prefix formula is valid because \(Y<z\); it must not be extended
beyond that range with the same untruncated coefficient.

For \(Y\ge1\), let
\[
 b_Y(n)=\prod_{p\mid n,\ Np\le Y}p,
 \qquad r_Y(n)=n/b_Y(n).
\]
These are ideals, so distinct primes of equal norm remain distinct. If
\(Nb_Y(n)\le Y\), precisely the divisors of \(b_Y(n)\) occur in
the prefix, including all of their products. Consequently
\[
 t_{z,Y}(n)=\mu_K(b_Y(n))\bigl(\mu_K(r_Y(n))+1\bigr).
 \tag{2}
\]
Thus saturated odd rough parts vanish and saturated even rough parts have
coefficient \(2\mu_K(b_Y(n))\). The rough part \(1\) is even.
If \(Y<1\), the prefix is empty and the coefficient is \(\mu_K(n)\);
this case is unsaturated and is not covered by (2).

Knowing separately that all primes in a proposed small part are at most
\(Y\) is insufficient: its **whole norm** must be at most \(Y\).
Equality belongs to the small side. A rough prime must have norm strictly
greater than \(Y\), and squarefreeness and coprimality are essential to
the stated formula. Complex twists and deletion zeros cause no problem:
every term at a fixed total ideal has the same \(\lambda_u(n)W(Nn/D)\).

For example, in the free divisor model with prime norms \(7,13,19,31\),
take \(z^2=2\cdot7\cdot13\cdot19\cdot31\). At \(Y=10\), the
small part has norm \(7\), the rough part has three primes, and the
coefficient is zero. At \(Y=20\), the small-prime part has norm
\(7\cdot13\cdot19>Y\), and the coefficient is \(-4\), despite
the one remaining rough prime. These are finite algebra examples, not
asymptotic character calculations.

## 2. Audit of the growing cofactor theorem

Fix the annulus and \(\kappa>0\), and let \(\mathcal G(D)\) contain
each squarefree ideal \(n\) once when it has a representation
\[
 n=bq_1q_2q_3,\qquad Nb\le D^{1/40},
 \qquad Nq_i\ge\kappa D^{13/40},
 \tag{3}
\]
where the \(q_i\) are distinct good prime ideals and are coprime to
\(b\). Restrict the actual projected tail to rows
\[
 L_u\ge D^{1/8+\delta},\qquad 0<\delta<11/40,
 \tag{4}
\]
and put \(H=D^{2/5}\). The upper restriction on \(\delta\) keeps
the lower conductor threshold below the inner row scale; the estimate
itself also holds in ranges where the selected inner rows are empty.

Choose \(\eta=1/80\) and first retain \(Nu\le D^{2/5+\eta}\).
The imported comparison \(L_u\ll_{\nu,S}Nu\) gives
\[
 Y_u\gg D^{3/80}>D^{1/40}\ge Nb,
 \qquad
 Y_u\le D^{13/40-\delta}<\kappa D^{13/40}\le Nq_i.
 \tag{5}
\]
Both strict comparisons hold for sufficiently large \(D\), with the
threshold depending on the fixed data, \(\kappa\), and \(\delta\).
Thus the canonical small part is exactly \(b\), its norm is saturated,
and (2) makes the complete coefficient zero. No arithmetic selector has
been inserted into a completed character kernel: this is pointwise
finite divisor algebra before taking an absolute value.

The far rows are retained in the estimate. Uniformly in the row and its
cutoff, \(|t_{z,Y}(n)|\le\tau_3(n)\ll_\varepsilon(Nn)^\varepsilon\),
so ideal counting bounds the selected amplitude by
\(O_{W,\varepsilon}(D^{1+\varepsilon})\). The complete Schwartz
tail then gives, for arbitrary fixed \(A>0\),
\[
 D^{-1}\sum_{Nu>D^{2/5+\eta}}
       \Phi(Nu/H)|\text{selected amplitude}_u|^2
 \ll D^{7/5+2\varepsilon-\eta A}.
 \tag{6}
\]
Choosing \(A\) after the requested error power proves arbitrary decay.
The conductor row restriction in (4) only reduces this nonnegative sum.

This is actual signed tail cancellation, rather than exclusion because
a giant prime cannot fit in either truncated factor. Indeed (3) and the
annular upper bound imply, uniformly,
\[
 Nq_i\ll D^{7/20}<z,
 \qquad N(q_iq_j)\gg D^{13/20}>z.
 \tag{7}
\]
For \(b=1\), each singleton convolution divisor has coefficient
\(-2\), and each pair has coefficient \(+2\); all six divisors
lie above \(Y_u\). Their tail coefficients are \(+6\) and \(-6\).
For nonunit \(b\), the additional cofactor divisors are retained in (2).

The \(b\)-range has genuine power width. Fixed narrow prime windows
near \(D^{1/3}\) already supply nonempty examples with \(b=1\);
the imported fixed-field prime ideal theorem can supply such examples
for growing cofactor norms as well. No prime-counting assertion is
needed for the zero-sector estimate.

## 3. Coherent-row stress tests and all conductor budgets

For balanced semiprimes \(n=pq\), \(Np\le Nq\le z<Nn\), the
complete truncated coefficients are \(1,-2,-2,+2\). Their exact tail
table is

| Threshold range | \(t_{z,Y}(pq)\) |
| --- | ---: |
| \(Y<1\) | \(+1\) |
| \(1\le Y<Np\) | \(+2\) |
| \(Np\le Y<Nq\) | \(0\) |
| \(Nq\le Y<N(pq)\) | \(-2\) |
| \(Y\ge N(pq)\) | \(0\) |

At the actual buffer, \(Y_u\le D^{9/20}\), while both balanced
prime norms are comparable to \(D^{1/2}\). Thus \(+2\) survives
on every row with \(Y_u\ge1\). The \(Y_u<1\) rows have
\(L_u>D^{9/20}\), hence \(Nu\gg D^{9/20}\), and are negligible
under the complete weight because \(9/20-2/5=1/20>0\).

For balanced triples with prime norms ordered \(p\le q\le r\),
where \(Nr\le z<N(pq)\), write prime letters for their norms in
the following table. The complete coefficients are \(c_z(1)=1\),
\(c_z(p_i)=-2\), \(c_z(p_ip_j)=+2\), and \(c_z(pqr)=0\).

| Threshold range | \(t_{z,Y}(pqr)\) |
| --- | ---: |
| \(Y<1\) | \(-1\) |
| \(1\le Y<p\) | \(0\) |
| \(p\le Y<q\) | \(-2\) |
| \(q\le Y<r\) | \(-4\) |
| \(r\le Y<pq\) | \(-6\) |
| \(pq\le Y<pr\) | \(-4\) |
| \(pr\le Y<qr\) | \(-2\) |
| \(Y\ge qr\) | \(0\) |

Equal norms merely make some intervals empty. The pair-threshold part
of this table uses the actual \(c_z\), rather than extending the
prefix coefficient \((-2)^{\omega(d)}\) past \(z\). At
\(\theta=11/20\), \(Y_u<z\), so only the first five rows can occur.
For \(b=1\), the transition for prime norms comparable to
\(D^{1/3}\) is \(L_u\asymp D^{7/60}\): below that transition all
three singleton divisors can be small and the coefficient is \(-6\);
above it the rough triple is odd and the coefficient is zero.
Constant-width transition bands retain the exact individual thresholds.

The conductor ranges at the stated parameters are therefore budgeted as
follows. Write \(L_u\asymp D^\ell\) when discussing power exponents.

| Range or rows | Threshold/response consequence | Available control |
| --- | --- | --- |
| Coherent inner rows \(u=v^6,\ Nu\le D^{2/5}\) | \(L_u\ll D^{1/15}\), so \(Y_u\gg D^{23/60}\); balanced triples have \(-6\), semiprimes \(+2\) | Remain in the unresolved low-conductor response |
| \(0\le\ell<7/60\), away from transition | Balanced triples can have all singleton norms below \(Y_u\) | No new signed moment bound |
| \(\ell>7/60\), away from transition | Balanced triples with \(b=1\) vanish while \(Y_u\ge1\) | Exact parity cancellation |
| \(L_u\ge D^{1/8+\delta},\ Nu\le D^{33/80}\) | All of (3) are saturated odd rough sectors | Exact zero, with margins \(1/80\) and \(\delta\) |
| \(Nu>D^{33/80}\) | Saturation need not persist | Arbitrary decay from (6) |
| \(L_u>D^{9/20}\) | \(Y_u<1\), so the unit prefix disappears | Arbitrary decay from \(Nu\gg D^{9/20}\) |

The row-count bound \(\#\{Nu\le H:L_u\le R\}\ll_\varepsilon
RH^\varepsilon\) does not make the low-conductor response affordable:
the elementary amplitude estimate gives energy as large as
\(D^{1+\varepsilon}R\). Fixed-character estimates cannot be made uniform
through a growing conductor cutoff without an additional hypothesis.

The exact zero mechanism does not extend to all rows. The following
coherent selected-piece example shows the compensation still required;
it does not disprove an all-row bound for the complete triple sector.
With the trivial fixed twist, choose three narrow
prime windows near \(D^{1/3}\) whose products lie in a part of the
profile with one fixed nonzero phase. The imported prime ideal theorem
supplies \(\asymp D/\log^3D\) triples; none of their primes divides
\(v\) when \(Nv\le D^{1/15}\). Their selected coefficient \(-6\)
therefore gives selected-piece energy of order at least
\(DH^{1/6}/\log^6D\). This remains a selected-piece obstruction,
not a lower bound for the full response, because cross terms with
other products remain.

## 4. Audit of the generic bound for retained parity sectors

The saturated-even and unsaturated responses can still be bounded by
\(D^\varepsilon B(D,H)\), with the existing imported operator. A
uniform bound on coefficients alone would not justify this for
row-dependent coefficients. The required additional fact is finite
variation in the common threshold \(Y\).

For each fixed squarefree column \(n\), the original coefficient changes
only at divisor norms, and its total variation is bounded by
\(\sum_{d\mid n}|c_z(d)|\ll_\varepsilon(Nn)^\varepsilon\).
For the auxiliary step function on the entire common threshold list,
one may use the original \(-\sum_{Nd>y}c_z(d)\) at all \(y\);
\(|c_z(d)|\le2^{\omega(d)}\) gives total variation at most
\(3^{\omega(n)}\). Alternatively the low-prefix function can be
extended past \(z\), with the same variation bound, but the two
extensions must not be identified there. They agree at every actual
adaptive threshold \(Y_u<z\), which is all the operator argument needs.
The canonical small part changes only at its prime norms. Between two
successive prime norms it is fixed, and saturation changes only when
\(Y\) reaches the norm of that fixed part. Thus the saturated-even or
unsaturated indicator has \(O(\omega(n)+1)\) jumps. Multiplying the
original coefficient by either indicator preserves a bound
\(O_\varepsilon((Nn)^\varepsilon)\) for its supremum and total
variation, after reallocating epsilon. Coincident thresholds are grouped
with their exact weak endpoint convention.

Order the finite union of all thresholds for columns on the annulus,
and include the initial coefficient as a jump before the first threshold.
A fixed binary partition expresses each adaptive prefix as at most
\(O(\log D)\) interval sums. Cauchy on the selected intervals and then
positivity permit summation over every fixed interval before applying
the physical operator. If \(b_I(n)\) is its fixed interval coefficient,
then
\[
 \sum_I|b_I(n)|^2
 \ll \log D\left(\sum_j|\Delta_j(n)|\right)^2
 \ll_\varepsilon D^\varepsilon.
 \tag{8}
\]
There are \(O(D)\) ideal columns on the annulus, all squarefree and
therefore sixth-power-free. With the fixed factors \(\nu(n)W(Nn/D)\)
absorbed, their summed squared norm is \(O(D^{1+\varepsilon})\).
The operator and the normalization by \(D\) give
\[
 \mathcal E_{\rm even},\ \mathcal E_{\rm unsat}
       \ll_\varepsilon D^\varepsilon
       \left(H+DH^{1/6}+H^{5/6}D^{1/3}+H^{1/3}D^{5/6}\right).
 \tag{9}
\]
There is no new power saving here. At \(H=D^{2/5}\), the four
exponents are \(2/5,16/15,2/3,29/30\), so the maximum remains
\(16/15\). Deleting the zero-sector leaves the coherent semiprime
obstruction intact.

The parity decomposition is an identity of response vectors. Squaring
its separate pieces creates cross terms; (9) does not justify replacing
the full moment by an additive sum of sector energies. Similarly, the
existing nonsquarefree bound \(D^{19/24+\varepsilon}\) is a difference
vector bound, with gap \(1/120\) below the proposed \(D^{4/5}\) budget.

## 5. Validation limits

The audit checked finite convolution algebra, all endpoint conventions,
the conductor exponents, the complete Schwartz remainder budget, and
the fixed-vector requirement of the physical operator. Small exact
divisor calculations reproduce both tables and the saturated/unsaturated
counterexample above.

The [companion checker](../numerics/check_short_family_rough_parity.py)
was read and run twice from the saved source. Both runs matched its
[saved record](../numerics/short_family_rough_parity_record_20261008.json)
byte for byte: 32,815 assertions, 177 inverse-profile cases, 3,173
cutoff cases, 12 phase/deletion cases, and 420 nonempty zero tails.
Its explicit nonunit-cofactor witness has 36 actual ordered tail tuples,
18 of each sign, and coefficient zero. The record SHA-256 is
`7f9d59da7861e28d186ed4cce3af019f43c93bfe55efd148c1f7444b6fc3bcc1`.
The equal-norm prime symbols remain distinct in all divisor and phase
operations. Off-profile algebra in the checker is explicitly separated
from the on-profile truncated inverse. The binary-level checks test
fixed interval sums; they do not themselves certify the analytic operator.

These checks do not independently prove native reciprocity, the conductor
comparison, Poisson completion, ideal counting, the imported de Faveri
operator, the prime ideal theorem, or an unbounded signed moment.
Those retain their manuscript source status. No new conductor-uniform
Mertens estimate, full moment exponent, scalar exponent, or zero-free
boundary is established.

## 6. Supporting audit of the squarefree discrepancy bridge

A separate same-model mathematical reading of
[note 22](../short_families/notes/22_SHORT_FAMILY_SQUAREFREE_DISCREPANCY_20261008.md)
checked its exact masked bridge. For fixed coprime squarefree outer factors
\(c,m\), the completely multiplicative character
\(\lambda_{u,cm}\), including its zero extension, gives
\[
 (\mu_K\lambda_{u,cm})*(\Lambda_K\lambda_{u,cm})
 =-\mu_K\lambda_{u,cm}\log N.
\]
Consequently the inner product is automatically squarefree and coprime to
\(cm\) after recombination. The separate prime-power terms must remain:
at a repeated prime the two possible nonzero Möbius terms cancel before
the squarefree bridge is recovered. The logarithmic derivative of the two
truncated Möbius factors has the factor \(-2\); combining it with the
tail's minus sign gives the factor \(+2\) in note 22's bridge. The
unit divisor contributes its separately retained negative term only when
\(Y_u<1\).

The centered Stieltjes identity excludes the adaptive lower endpoint and
includes the truncated upper endpoint with right-continuous cumulative
sums. The artificial lower endpoint \(3/2\) removes no von Mangoldt
atom. In the twice-integrated recovery formula,
\(\mathcal L_k'(R)=K(R)/R\) almost everywhere; integration by parts
therefore yields both displayed endpoint terms and the derivative
\((R\varphi')'\). Substitution of the mixed Riesz identity leaves
the explicit \(K\)-endpoint terms as a genuine remaining obligation.
The principal density coefficient is \(\delta_u\), rather than
the residue of a free-character ideal count. The high/high density,
both low/full and full/low edges, and the low/low correction have the
required inclusion-exclusion signs. The old sufficient empty-overlap
criterion fails because \(UVz>Y_u\) at this cutoff.

For a balanced squarefree semiprime with \(1\le Y_u<\min(Nq,Nr)\),
the two nonunit inner possibilities give
\(2\log Nr/\log N(qr)\) and
\(2\log Nq/\log N(qr)\), totaling \(+2\). If
\(U\ge1\) and \(V<\min(Nq,Nr)\), their expanded von Mangoldt
factors lie entirely in the low/high edge. This is consistent with the
surviving semiprime in the parity decomposition and prevents transferring
note 19's different-cutoff opposing-edge cancellation to this response.

The added mask preserves the primitive inducing conductor but multiplies
the completion modulus by the previously undeleted part of \(cm\).
More strongly, on a nonzero outer term \(\lambda_u(cm)\ne0\),
the whole \(cm\) is coprime to the original conductor and deletion
ideal, so the new modulus is exactly \(L_uN(cm)\). Its norms can be
of order \(D^{7/5+\eta}\) on the significant row shell. For a
zero-integral profile the free-character completion retains these new
parameters; it gives no estimate for either the Möbius cumulative sum
or the von Mangoldt discrepancy in the mixed bridge. Finite prime-power
deletion costs do not change that conclusion. These are exact algebraic
and conductor-accounting checks, with no new analytic bound or separate
formal proof verification.

The saved discrepancy checker was also run twice with identical output.
Its [record](../numerics/short_family_squarefree_discrepancy_record_20261008.json)
reports 1,490 masked convolutions, 22,680 projected-tail and cofactor
regrouping checks each, 2,820 direct original-tuple versus full prime-power
bridge comparisons, 10,416 phase/deletion checks, 128 masked mixed
integrals and complete edge closures each, and 768 centered Stieltjes
comparisons. Exact rational log substitutions are finite diagnostics,
not a proof of the algebraic identity; the displayed derivation supplies
the proof. Integral checks reuse the earlier formal cyclotomic-log ring.

## 7. Saved manuscript and reproducibility

The cofactor parity proposition, growing signed sector theorem and proof,
coherent-row limits and generic retained budget are incorporated in the
[existing manuscript](../short_families/short_family_reductions.tex).
The desktop editor's native compiler returned success for the final saved
source. Its SHA-256 is
`628700359d78202fae5137fafbf4667a73df208c7f738a517f6bc35aebd16e22`.
Static checks found 127 unique labels, 110 resolved references and 19
bibliography entries, with every citation resolved.

Two additional coordinating runs of each new checker reproduced the saved
records byte-for-byte. The discrepancy record SHA-256 is
`b702e558d72cbd2db32bef22463a17ff0cf0f427b54fc5ceed53ff5db52f6bda`.
Hashes identify these small records and source; no proof step depends on
their values. Research links and text hygiene were checked, and all new
files are below 100 KB. The session used the existing checkout based on
`6c343e83622e194268399033b2eee68cc7e5fbcd`. No commit, tag, snapshot
folder or separate PDF was created.
