# Continuation after the mixed conductor-neighbor sectors

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Same-model derivations, audits and finite checks are internal validation,
not independent specialist review or formal proof verification.

Continue in the current checkout at
`/Users/ebbaker/Documents/shifted-zeta-positivity`. This continuation and
the preceding short/mixed additions remain uncommitted on session base
`6c343e8`. Preserve the working tree; starting afresh from HEAD would omit
these results. The new notes, record and scoped review are small source
artifacts; no snapshot or commit was created.

## 1. Completed bounded task

The task in [short-family note 26](../../short_families/notes/26_SHORT_FAMILY_COFACTOR_CONTINUATION_20261008.md)
was to test one actual mixed open-chain conductor regime and retain its
complement. [Mixed note 4](4_CONDUCTOR_NEIGHBOR_SECTORS_20261008.md)
does this for six growing conductor sectors whose coefficients need
not vanish. It uses the actual sixth-power-free physical rows, actual
inverse/prime weights and plain endpoints, with every deletion zero.

At fixed separating parameters, keep the notation of
[note 3](3_ACTUAL_PROBE_CUBIC_TARGET_20261008.md):
\[
 J=f^*G^2f\ge0,\qquad E=\|f\|^2,\qquad E^3\le L_N^2J,
 \qquad N=U^m,\quad L_N\ll N,
\]
\[
 J_{\ne}=\sum_{c(u),c(v),c(h)\ \mathrm{pairwise\ distinct}}
 w_uw_vw_h\overline{S_u}K(u,v)K(v,h)S_h.
\]
The sufficient exponent is \(T=h_3+m=3(1+dm-s)-2m\). Every
repeated-character pattern already has a fixed reserve below \(T\).
Let \(Q_{u,v}\) be the inducing primitive **row-ratio** conductor
norm, rather than either physical row conductor or a column-ratio
conductor.

Write \(P=Q_{u,v}Q_{v,h}\), \(F=Q_{u,h}\). The final controlled
cuts and uniform reserves below \(T\) are

| Sector | Conductor condition | Reserve |
| --- | --- | --- |
| Any neighboring edge | \(\min(Q_{u,v},Q_{v,h},F)\le U^{6/25}\) | \(47/12500=0.00376\) |
| Any two-edge product | \(\min(P,Q_{u,v}F,Q_{v,h}F)\le U^{17/20}\) | \(19/12500=0.00152\) |
| Coupled middle rows | \(P/F\le U^{12/25}\) | \(47/12500=0.00376\) |
| One kernel leg with masked completion | \(\min(Q_{u,v},Q_{v,h})\le U^{39/100}\) | \(219/25000=0.00876\) |
| Kernel-leg product with masked completion | \(P\le U^{103/100}\) | \(163/25000=0.00652\) |
| Coupled middle rows with masked completion | \(P^2/F\le U^{15/8}\) | \(313/50000=0.00626\) |

Assign each sector outside all preceding ones, as in note 4, to avoid
double counting. The endpoint edge belongs to the first two cuts even
though it is not one of the two displayed kernels. Those cuts must not
be replaced by conditions on the displayed legs alone.
A useful explicit part of the coupled middle sector is
\[
 Q_{u,v},Q_{v,h}\le U^{3/5},\qquad Q_{u,h}\ge U^{3/4}.
 \tag{1}
\]
Its ratio is at most \(U^{9/20}\), and its stronger reserve is
\(469/25000=0.01876\).
Dyadic partitions cost logarithms, absorbed by the allowed analytic loss.
These are conductor-sector estimates, not a bound for the complete
mixed energy or an improved zero-free boundary.

## 2. The arithmetic count, completion gain and exact complement

The new counting input is elementary once the imported exact local
reciprocity and ramification description are retained. For fixed \(u\),
the good conductor ideal of the quotient specifies the primes at which
the sixth-power-free valuations of \(v\) can differ from those of
\(u\). There are at most five alternative valuations at each such
prime and finitely many fixed bad-prime/unit choices. Thus
\[
 \#\{v:Q_{u,v}\le V\}\ll_\varepsilon V^{1+\varepsilon},
 \qquad \sum_{Q_{u,v}\le V}w_v\ll W V^{1+\varepsilon}.
\]
The actual selector only reduces these counts; it is not replaced by a
new family when estimating a signed kernel. Any one edge therefore costs
\(A^2WV\), and any specified two-edge tree with caps \(V_1,V_2\)
costs \(AW^2V_1V_2\), before applying the two kernel and endpoint
bounds. The tree may include the endpoint edge.

The coupled count is stronger than two independent degree bounds. For
fixed endpoints let \(\mathfrak f\) be their good ratio conductor
ideal and \(\mathfrak p,\mathfrak q\) the two good leg conductors.
Prime by prime,
\[
 \mathfrak p\mathfrak q=\mathfrak f A_0B_0^2,
 \qquad A_0\mid\mathfrak f,\qquad(B_0,\mathfrak f)=1.
\]
At a prime outside \(\mathfrak f\), the endpoints have the same
valuation: a different middle valuation puts the prime in both legs.
At a prime of \(\mathfrak f\), a middle valuation different from
both endpoints supplies the additional factor \(A_0\). The possible
valuations number at most
\(6^{\omega(\mathfrak f)}5^{\omega(B_0)}\), apart from the fixed
presentation factors. Consequently, for \(P=Q_{u,v}Q_{v,h}\) and
\(F=Q_{u,h}\),
\[
 \#\{v:Q_{u,v}\le V_1,\ Q_{v,h}\le V_2\}
 \ll_\varepsilon U^\varepsilon
       \left(1+\sqrt{V_1V_2/F}\right),
\]
\[
 \#\{v:P/F\le R\}
 \ll_\varepsilon U^\varepsilon(1+\sqrt R).
\]
The fixed-prime conductor factors are paid in the implied constant.
The norm of \(\mathfrak f\) is polynomial in \(U\), so its divisor
factors are absorbed by \(U^\varepsilon\). No physical deletion mask
has been canceled by this conductor count.

For leg exponents \(q_1,q_2\) and an endpoint lower exponent \(a\),
write \(\kappa=\max\{0,(q_1+q_2-a)/2\}\). The count, actual
endpoint bound \(|S_u|^2\ll N^d\), and nonprincipal kernel bound
\(|K(u,v)|\ll N^{-1/8}\) give
\[
 |J_{\rm sector}|\ll U^\varepsilon\mathcal H^b
                  N^{d-1/4}A^2W U^\kappa.
\]
The same argument with the actual energy in place of its pointwise
endpoint envelope gives \(N^{-1/4}A E W U^\kappa\). The rectangle
in section 1 has \(\kappa=9/40\); the larger direct-ratio sector has
\(\kappa=6/25\).

The additional completion input is the order-zero branch of the source
masked primitive-Poisson lemma. Expanding the deletion mask gives a
nonprincipal sum bounded by \(\tau(E_{u,v})\sqrt{Q_{u,v}}\), even
when the full mask modulus is large. Its divisor cost is
\(U^\varepsilon\) for these physical rows. With the actual profile
\(|B|^2\) and its permitted derivative/height costs, the two valid
kernel estimates combine as
\[
 |K(u,v)|\ll U^\varepsilon\mathcal H^b
       \min\{N^{-1/8},\sqrt{Q_{u,v}}/N\}.
\]
Using completion on one displayed leg, or on both, respectively gives
\[
 |J_{\min(Q_{u,v},Q_{v,h})\le V}|
 \ll U^\varepsilon\mathcal H^b
             N^{d-9/8}A^2W V^{3/2},
\]
\[
 |J_{P\le V}|
 \ll U^\varepsilon\mathcal H^b
             N^{d-2}AW^2 V^{3/2}.
\]
For the final coupled sector, fix endpoints and partition \(P\) into
binary bins. The local geometry gives \(F\ll P\) on a nonempty
bin. Multiplying its middle-count bound by the two completion kernel
bounds costs
\[
 \frac{WU^\varepsilon\mathcal H^b}{N^2}
       (1+\sqrt{P/F})\sqrt P
       \ll \frac{WU^\varepsilon\mathcal H^b}{N^2}
                        \frac P{\sqrt F}.
\]
Thus \(P^2/F\le U^{15/8}\) costs at most \(U^{15/16}\), and
\[
 |J_{P^2/F\le U^{15/8}}|
 \ll U^\varepsilon\mathcal H^b
                 N^{d-2}A^2W U^{15/16}.
\]
Binary partitions have logarithmically many bins; implied fixed-prime
constants do not change any exponent. These bounds justify the last
three reserves in the table without asserting positivity of their
restricted chains.

After the six disjoint removals, the exact distinct-character remainder
satisfies **all** of
\[
 \min\{Q_{u,v},Q_{v,h},F\}>U^{6/25},
 \qquad\min\{P,Q_{u,v}F,Q_{v,h}F\}>U^{17/20},
\]
\[
 P/F>U^{12/25},\qquad
 \min\{Q_{u,v},Q_{v,h}\}>U^{39/100},\qquad
 P>U^{103/100},\qquad P^2/F>U^{15/8}.
\]
Equality belongs to a removed side. Every condition is retained even
where another condition makes part of it redundant. In particular the
first two conditions include the endpoint edge and cannot be replaced
by displayed-leg conditions. The exact partition is
\[
 J_{\ne}=J_{\rm rem}
       +O(U^{T-19/12500+\varepsilon}\mathcal H^b).
\]
All original weights, profiles, masks and physical row selectors remain
in \(J_{\rm rem}\). The sufficient unproved task is its one-sided
real upper bound at exponent \(T\). The sector estimates use absolute
majorants only after retaining their exact arithmetic conditions.

## 3. Why positivity alone does not finish the task

Let \(G_0\) be the block diagonal part of \(G\), grouping rows by
their inducing primitive character, and put \(G_1=G-G_0\). The
identity
\[
 f^*G_1^2f=J_{\ne}+J_{\rm end},\qquad J_{\rm end}\ge0
\]
is exact. Hence weighted Schur gives the valid bound
\[
 J_{\ne}\le\|G_1f\|^2
       \ll U^\varepsilon\mathcal H^b N^{-1/4}A^2E.
 \tag{2}
\]
This preserves the actual probe but does not save a power beyond the
available absolute estimate: using \(E\le A N^d\) returns
\(N^{d-1/4}A^3\). Combining (2) with spectral Jensen and the cheap
repeated patterns would give at best \(E\ll A N^{7/8}\), which is
weaker than that buffered plain envelope.

For \(A\ll U^{1-\mu}\), the deficit of the absolute bound relative
to \(T\) is
\[
 (7/4-2d)m+3(s-\mu).
 \tag{3}
\]
When \(\mu\ge s\), the elementary bound \(E\le A N^d\)
already reaches the desired energy exponent. In the remaining region
\(\mu<s\), (3) is at least \(91/250=0.364\). Binning endpoints
by their physical primitive conductors cannot recover this: the selected
set has \(\theta(u)>2m-1/1000\), so the reflected plain estimate
can improve the endpoint-product exponent by at most
\(d/1000\le21/50000=0.00042\). This is a limitation of the stated
positive and entrywise estimates, not a lower bound for the energy.

## 4. A remaining count exponent is sharp in the physical family

Fix three pairwise coprime good prime ideals \(a,b,c\), all of norm
comparable to \(U^{1/2}\), and choose physical generators for the
endpoint ideals
\[
 u=ab,\qquad h=ac.
\]
Vary a good prime ideal \(d\), coprime to \(abc\), in a fixed narrow
window of norm comparable to \(U^{1/2}\), and put \(v=ad\).
Constants can be chosen so that all three row norms lie in the fixed
physical dyad. These rows are squarefree and hence sixth-power-free.
The imported local conductor description gives
\[
 Q_{u,v}\asymp U,\qquad Q_{v,h}\asymp U,\qquad
 Q_{u,h}\asymp U.
 \tag{4}
\]
Their physical primitive row conductors are also comparable to \(U\),
so they pass the primitive-conductor gate defining \(\mathcal C_+\).
The fixed-field prime ideal theorem supplies
\(\asymp U^{1/2}/\log U\) such middle rows. A fixed unit/ray presentation can be retained by
partitioning the prime rows into its finitely many classes and choosing
\(b,c,d\) in a populated compatible class; only a fixed factor is
lost. No growing-character or ray-class PNT is invoked. Thus the exponent
\(\kappa=(1+1-1)/2=1/2\) in the coupled count is attained up to logarithms in
the actual physical row family.

This is a counting obstruction, not a mixed-energy counterexample.
Membership in the actual selected zero/profile bin and lower bounds for
the actual inverse/prime weights are **not** asserted. No phase has been
replaced by an arbitrary matrix entry. The example shows that improving
the generic neighbor count alone cannot supply a uniform power saving
on this raw family. Distribution of the selected weights or their
correlation with the two kernel phases is additional arithmetic information.
The regime (4) has \(P\asymp U^2\), \(P/F\asymp U\) and
\(P^2/F\asymp U^3\), so it remains after all six removals. Moreover
\(\sqrt{Q_{u,v}}/N\asymp U^{1/2-m}\) is weaker than
\(N^{-1/8}\) in the operational region \(m<1/2\), and the same
holds for the other leg. The valid order-zero completion branch therefore
does not improve this particular remaining regime.

## 5. An exact remaining budget gap at a legal parameter point

Use the operational notation of [note 1](1_MIXED_CONDUCTOR_REFINEMENT_20261008.md).
Take
\[
 d=9/25,\quad x=1/2,\quad a_r=1/20000,\quad b_m=1/40000,
 \quad\eta=1/5000,\quad\ell=1/1000000,\quad\rho=\ell/2.
\]
The source formulas give
\[
 R^*=58601/84575,\quad r_{\rm new}=47749/67660,
 \quad m_{\rm new}=137271/338300.
\]
Put \(r=r_{\rm new}+a_r\), \(m=m_{\rm new}-b_m\),
\(z=(1-r)/2-\rho\), and use the actual universal-envelope quantities
\(g=d(r+z)\), \(s=\eta-d(1-x)a_r+\ell\),
\(\mu=\max(0,1-R^*-\ell-g)\). Explicitly,
\[
 r=\frac{47752383}{67660000},\qquad
 m=\frac{54905017}{135320000},\qquad
 z=\frac{995377467}{6766000000},
\]
\[
 g=\frac{51935541903}{169150000000},\quad
 s=\frac3{15625},\quad
 \mu=\frac{12288947}{169150000000}.
 \tag{5}
\]
These choices satisfy the continuous operational inequalities and strict
inverse capacities; for example \(r+2z=1-\ell<1\). This is a
legal parameter point, not an assertion that a selected arithmetic bin
attains every envelope there.

The required probe exponent is
\[
 T=3(1+dm-s)-2m=\frac{8884236001}{3383000000}.
\]
If a fixed-endpoint middle count costs \(U^\kappa\), its bound has exponent
\(2(1-\mu)+g+(d-1/4)m+\kappa\). Its available middle-count budget is
\[
 \mathcal B=T-\{2(1-\mu)+g+(d-1/4)m\}
 =\frac{92902792407}{338300000000}
 =0.274616590029559\ldots.
 \tag{6}
\]
For the sharp regime (4), the available absolute argument therefore
exceeds the target by
\[
 \boxed{\frac12-\mathcal B
 =\frac{76247207593}{338300000000}
 =0.225383409970440\ldots.}
 \tag{7}
\]
This is an exponent deficit of the available bound. It does not show
that the actual selected energy is large. A stronger weighted endpoint
estimate could also reduce the cost; the point of (7) is to quantify
what the current counting and endpoint envelopes fail to provide.

## 6. The deletion-modulus qualification

The full deletion modulus limits arbitrarily rapid completion decay;
it does not invalidate the order-zero completion gain used above. If the
ratio character has extra deletion ideal \(E_{u,v}\), the all-scale
completion estimate at positive decay order sees
\(L_{u,v}=Q_{u,v}NE_{u,v}\), together with its divisor cost.
Common ramification can cancel from the inducing character while its
physical zeros remain. At order zero the source lemma still gives the
valid bound \(\tau(E_{u,v})\sqrt{Q_{u,v}}\). Small primitive
row-ratio conductor can therefore improve a kernel through that branch,
as in the last three sectors, without any effective-mask bound.

Primes larger than the maximum column norm cannot divide any column and
may be removed from that mask. This support simplification must be done
explicitly. It does not follow from a bound on \(Q_{u,v}\).
For example let the common part of two squarefree physical rows be the
product of four good primes, each of norm comparable to \(U^{9/40}\),
and let their two distinct remaining primes have norm comparable to
\(U^{1/10}\). Both row norms are comparable to \(U\); the primitive
ratio conductor has norm comparable to \(U^{1/5}\), but the canceled
common-prime mask has norm comparable to \(U^{9/10}\). Each of its
prime norms is below the plain column scale \(U^m\), \(m>2/5\),
so none is removed merely by the column cap. The full combined-modulus
envelope has size \(U^{11/10}\), even though the primitive ratio
conductor is smaller than the column scale. This blocks an inference of
arbitrarily rapid decay from the primitive conductor alone. It neither
blocks the valid order-zero bound nor rules out a refined mask expansion.

## 7. Next bounded research task and source status

Continue with the **actual weighted two-kernel middle sum** on a remaining
regime such as (4), keeping its endpoint form:
\[
 \sum_{u,h}w_uw_h\overline{S_u}S_h
 \sum_{\substack{v\in\mathcal C_+\\
       Q_{u,v},Q_{v,h},Q_{u,h}\asymp U}}
               w_vK(u,v)K(v,h),
\]
with the three primitive characters pairwise inequivalent and all original
masks present. Test whether the actual inverse/prime weight has a smaller
conditional mass on these conductor intersections, or whether reciprocity
and the Möbius coefficients yield cancellation in its coupled kernel
phase. A pointwise weighted count saving by the amount in (7) would be
one sufficient mechanism at the displayed parameter point; it is stronger
than necessary because the full signed endpoint form can cancel too.
Another improvement to the generic unweighted neighbor count in the
sharp family (4) is not the next task.

Retain fixed separating parameters until the required derivative and
height uniformity is proved. The global family/growth input,
\(N^{-1/8}\) nonprincipal kernel estimate, masked primitive-Poisson
input at order zero for the actual profile \(|B|^2\), buffered actual
plain bound, inverse mass/envelope and continuous operational reserves remain
the explicitly imported conditional inputs of notes 1--4. Exact local
reciprocity and the good-prime conductor description likewise retain their
source status. Elementary ideal counting and the already imported
untwisted fixed-field prime ideal theorem support the neighbor counts and
raw-family sharpness example; no new growing-character PNT is assumed.

The [neighbor checker](../../numerics/check_mixed_conductor_neighbors.py)
and [small record](../../numerics/mixed_conductor_neighbors_record_20261008.json)
test finite valuation identities, masks, conductor partitions, nonzero
finite chain witnesses and rational reserves. Two fresh author replays
matched the saved record byte for byte: **26,966 assertions**, **216**
sixth-power-free valuation rows, **40** endpoint pairs, **60** deleted
frame entries and **four** nonzero one-edge witnesses. The record SHA-256
is `d099d059e7cfb4da6af462a9daecf7222523c18fac64e762ea341d251e9e0934`.
These checks do not certify the source analytic inputs, actual selected-bin
distribution, or an unbounded correlation. No new full mixed moment, scalar exponent, zero-free
boundary or RH implication has been proved.
