# Scoped audit of mixed conductor-neighbor sectors

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This audit independently derives the conductor counts and exponent
transfers from the existing local inputs. It is same-model internal
validation, not independent specialist review or formal proof verification.

## 1. Scope and source assumptions

The audited continuation is
[mixed note 4](../mixed_character_families/notes/4_CONDUCTOR_NEIGHBOR_SECTORS_20261008.md),
building on the [actual-probe criterion](../mixed_character_families/notes/3_ACTUAL_PROBE_CUBIC_TARGET_20261008.md).
The new result controls specified nonprincipal conductor sectors of its
actual open chain. It does not prove the full distinct-character target,
the original mixed energy target, or a new scalar or zero-free exponent.

The existing inputs were checked in their local source formulations:

- [Mixed note 1](../mixed_character_families/notes/1_MIXED_CONDUCTOR_REFINEMENT_20261008.md)
  supplies the buffered application region, actual selected positive
  inverse mass, physical-profile envelope and all permitted height costs.
- [Mixed note 2](../mixed_character_families/notes/2_SELECTED_INVERSE_DISTRIBUTION_20261008.md)
  supplies the exact local valuation consequence of sextic reciprocity,
  bounded primitive fibers for sixth-power-free physical rows, the
  conditional nonprincipal masked kernel bound, and the certified
  repeated-cycle reserve used below.
- The [amplification manuscript](../../quasi-rh-character-amplification/manuscript.tex),
  Hypothesis “Buffered plain input,” equation `eq:plain-input`, supplies
  the actual endpoint bound. Its
  [energy-localization note](../../quasi-rh-character-amplification/notes/SELECTOR_ENERGY_LOCALIZATION_20261008.md)
  retains the physical prime-polynomial envelopes and their derivative
  requirements.

The Sept. 30 global family theorem, quantitative primitive growth,
deleted-factor estimates and exact local sextic reciprocity remain
imported assumptions with the same source scope as note 2. This audit
does not reprove those external inputs or infer them from zeta-only
quasi-RH. The new finite conductor counting itself needs no prime ideal
theorem or cancellation estimate for arbitrary coefficients.

## 2. Actual frame, weights and the legal point of partition

Keep the actual sixth-power-free physical rows and
\[
 w_u=\mathbf1_{u\in\mathcal C_+}|M_r(u)Q_I(u)|^2,
 \quad A=\sum_u w_u,
 \quad W=\max_u w_u,
 \quad N=U^m.
 \tag{1}
\]
The selected inverse and physical prime polynomials are assembled
before using positivity or their envelopes. They are not replaced by
arbitrary row amplitudes. At common fixed separating parameters,
\[
 A\ll U^{1-\mu+\varepsilon}\mathcal H^a,
 \quad W\ll U^{g+\varepsilon}\mathcal H^a,
 \quad g=d(r+z),\quad \mu\ge0.
 \tag{2}
\]
Every kernel remains the complete original masked kernel
\[
 K(u,v)=N^{-1}\sum_k |B(Nk/N)|^2
                   \psi_u(k)\overline{\psi_v(k)}.
 \tag{3}
\]
For unequal inducing primitive characters the inherited conditional
bound is \(K(u,v)\ll N^{-1/8}U^\varepsilon\mathcal H^a\).
The actual buffered endpoint input gives
\( |S_uS_h|\ll N^dU^\varepsilon\mathcal H^a\).
Consequently an absolute majorant for a distinct-character triple
has the common factor \(N^{d-1/4}\), multiplying its original
three nonnegative weights.

The exact open-chain functional is
\[
 J=\sum_{u,v,h}w_uw_vw_h\overline{S_u}K(u,v)K(v,h)S_h.
 \tag{4}
\]
Its pairwise-distinct primitive-character part \(J_{\ne}\) is
partitioned **after** this exact expansion. No conductor cutoff is
inserted into a Gram matrix or into the positive inverse weight.
The new sector sums may be signed. Their absolute estimates are
legitimate; they are not asserted to inherit positivity from \(J\).
The stated union conditions are invariant under reversal \(u\leftrightarrow h\),
so each complete sector sum is real.

## 3. Single-neighbor count from exact local valuations

Let \(Q_{uv}\) be the norm of the primitive inducing character of
the row quotient \(\psi_u\overline{\psi_v}\). Outside the fixed bad
set, write physical valuations as \(a_p,b_p\in\{0,\ldots,5\}\).
The imported local character has exact order six, so a good prime
ramifies in the primitive quotient precisely when \(a_p\ne b_p\).
The fixed common ray twist cancels there. The fixed-prime and unit
choices contribute only a fixed factor.

For fixed \(u\), let \(q\) be the good radical of the quotient
conductor. If \(Q_{uv}\le R\), then \(Nq\le R\), and outside
\(q\) all good valuations of \(v\) are forced to equal those of
\(u\). At each prime of \(q\) there are at most five different
choices for \(b_p\). Thus
\[
 \#\{v\in\mathcal C_+:Q_{uv}\le R\}
 \ll_S\sum_{Nq\le R}5^{\omega(q)}
 \ll_{\varepsilon,S}R^{1+\varepsilon}.
 \tag{5}
\]
The last inequality is elementary ideal counting and the ideal divisor
bound. It is an upper count: it does not assert that every choice
lies in the norm annulus, ray class or selected amplitude bin. Retaining
those restrictions only reduces the count. The actual sixth-power-free
restriction is essential; without bounded valuations, sixth powers
would give additional unbounded fibers.

Taking the actual maximum weight after this count yields
\[
 \sum_{v:Q_{uv}\le R}w_v\ll U^\varepsilon W R.
 \tag{6}
\]
For the reversal-invariant sector in \(J_{\ne}\) where any one of
\(Q_{uv},Q_{vh},Q_{uh}\) is at most \(R\), (6) gives total
weight \(\ll U^\varepsilon A^2WR\), with only a factor three
for the union. Hence
\[
 |J_{\mathrm{one}}(R)|
 \ll U^\varepsilon\mathcal H^a N^{d-1/4}A^2WR.
 \tag{7}
\]
The endpoint conductor \(Q_{uh}\) need not occur as a kernel in
(4) to be counted this way. Both actual chain kernels are still
nonprincipal because the three primitive characters are distinct.

## 4. Two edges forming a tree and the improved product cutoff

Any two of the three conductor edges form a tree. Summing over its
two leaves using (6), with its center fixed, gives
\[
 \sum_{Q_{e_1}\le V_1,\ Q_{e_2}\le V_2}w_uw_vw_h
             \ll U^\varepsilon A W^2V_1V_2.
 \tag{8}
\]
This remains true for each of the three possible trees and after
enlarging from distinct characters to all rows in this positive count.
Only the original kernels in (4) are used for the later character
bound; the conductor tree is a counting device.

For a product restriction \(Q_{e_1}Q_{e_2}\le U^\sigma\), split
the first conductor into dyadic intervals. On an interval
\([2^j,2^{j+1})\), bound the second by \(U^\sigma/2^j\).
Equation (8) costs \(O(U^\sigma)\) for each of \(O(\log U)\)
intervals, giving
\[
 |J_{\mathrm{tree}}(\sigma)|
 \ll U^\varepsilon\mathcal H^a N^{d-1/4}AW^2U^\sigma.
 \tag{9}
\]
The logarithm and the fixed union over trees are absorbed into a
previously chosen arbitrarily small loss. No independence assumption
on the conductors is used.

The sharper exponent comparison uses the existing note 2 reserve
**before** its useful \(2\mu\) improvement:
\[
 M_0=1-g-(11/4-3d)m-3s\ge147/12500.
 \tag{10}
\]
Let \(t=h_3+m=3-(2-3d)m-3s\) be the actual-probe target exponent.
The exact gap between \(t\) and the exponent in (9) is
\[
 2M_0+(15/4-4d)m+\mu+3s-\sigma.
 \tag{11}
\]
Using \(d\le21/50\), \(m\ge2/5\), \(\mu\ge0\), \(s\ge0\),
\[
 2M_0+(15/4-4d)m+\mu+3s
 \ge \frac{2\cdot147}{12500}
       +\left(\frac{15}4-\frac{84}{50}\right)\frac25
 =\frac{10644}{12500}=0.85152.
 \tag{12}
\]
Thus the product cutoff \(\sigma=17/20\) leaves reserve
\(19/12500=0.00152\). The weaker transfer from the old all-equal
coarse margin would reach only \(\sigma=16/25\); it is not the
final cutoff used here.

For comparison, the exact single-edge gap from (7), at \(R=U^\rho\),
is
\[
 M_0+(1-d)m+2\mu-\rho.
 \tag{13}
\]
Its lower bound before subtracting \(\rho\) is
\(147/12500+(1-21/50)(2/5)=3047/12500\).
At \(\rho=6/25\), the reserve is \(47/12500\).

These gaps are uniform on the already certified operational region.
All conductor-count losses, source analytic losses and finite height
costs must be allocated in the same prescribed order as notes 1--3.
The reserves are positive, so a fixed sufficiently small allocation is
possible. The proof does not claim an endpoint theorem with no losses.

## 5. Coupled middle-row count with the endpoints fixed

The local conductor identity supplies a stronger conditional count.
Use good conductor ideals
\(F=\mathfrak f_{uh}\), \(P=\mathfrak f_{uv}\),
\(Q=\mathfrak f_{vh}\). At a good prime, let endpoint valuations
be \(a_p,c_p\) and the middle valuation be \(b_p\).

If \(a_p\ne c_p\), then the prime occurs in exactly one of
\(P,Q\) when \(b_p\) equals an endpoint, and occurs in both
when \(b_p\) equals neither endpoint. If \(a_p=c_p\), it occurs
in both exactly when the middle valuation differs. Therefore exactly
\[
 PQ=F A_0 B_0^2,\qquad A_0\mid F,\qquad(B_0,F)=1.
 \tag{14}
\]
Here \(A_0\) consists of endpoint-different primes at which the middle
equals neither endpoint, and \(B_0\) consists of endpoint-equal primes
at which it differs. Every allowed valuation, including zero, is
retained. The quotient phases do not erase original deletion zeros;
(14) concerns primitive good conductors only.

For fixed endpoints and legs bounded by \(V_1,V_2\), (14) implies
\(NB_0\le\sqrt{V_1V_2/NF}\). Choices on \(F\) contribute at most
\(6^{\omega(F)}\), and choices on \(B_0\) at most
\(5^{\omega(B_0)}\), up to the fixed ray/unit factor. Since the
endpoint norms are of order \(U\), \(NF\ll U^2\), and the ideal
divisor estimate absorbs the first factor into \(U^\varepsilon\).
Summing the second over \(B_0\) proves
\[
 \#\{v:Q_{uv}\le V_1,\ Q_{vh}\le V_2\}
 \ll U^\varepsilon\left(1+\sqrt{V_1V_2/Q_{uh}}\right).
 \tag{15}
\]
Passing from good conductor ideals to full primitive conductors changes
only fixed bad-prime constants. With the exact good norms the set is
empty when \(V_1V_2<NF\); with full norms this has a corresponding
fixed-constant threshold. The additive one in (15) safely covers small
norms, not a claim that the impossible range is populated.

For the sector
\[
 Q_{uv},Q_{vh}\le U^{3/5},\qquad Q_{uh}\ge U^{3/4},
 \tag{16}
\]
the middle weight is at most \(WU^{9/40+\varepsilon}\).
After summing the actual endpoint weights, the open chain therefore
has absolute majorant
\[
 |J_{\mathrm{mid}}|
 \ll U^\varepsilon\mathcal H^a
                    N^{d-1/4}A^2WU^{9/40}.
 \tag{17}
\]
Its target reserve is at least
\(3047/12500-9/40=469/25000\). This bound can be applied to the
part not already included in the first two sectors by a nonnegative
enlargement of its absolute majorant. There is no double-counted
identity: use a disjoint assignment to form the exact partition.

The same local proof gives the more useful product-ratio condition
without individual leg caps. For fixed endpoints, if
\(Q_{uv}Q_{vh}/Q_{uh}\le R\), then (14), together with the bounded
bad-prime factors, gives \(NB_0\ll_S\sqrt R\). Summing its possible
ideals and retaining the \(6^{\omega(F)}\) choices proves
\[
 \#\{v:Q_{uv}Q_{vh}\le RQ_{uh}\}
       \ll U^\varepsilon(1+\sqrt R).
 \tag{17a}
\]
All physical rows and selected-bin restrictions are still imposed.
At \(R=U^{12/25}\), the middle weight costs at most
\(WU^{6/25+\varepsilon}\), so the chain is bounded by
\(N^{d-1/4}A^2WU^{6/25+\varepsilon}\mathcal H^a\).
Its reserve is \(47/12500\). The rectangle (16) is a subregion of
this condition, with its stronger individual reserve \(469/25000\).
This count needs no dyadic leg partition.

The local pattern is compatible with large primitive physical rows.
For disjoint good factors with norms
\(Na\asymp U^{21/50}\) and
\(Nb,Nc,Nd,Ne\asymp U^{29/100}\), take
\(u=abc\), \(v=abd\), \(h=ade\), all squarefree.
Their norms are of order \(U\); the two adjacent quotient conductors
have norms of order \(U^{29/50}\), and the endpoint quotient has norm
of order \(U^{29/25}\). These lie strictly inside the asymptotic
rectangle (16), avoiding a fixed-constant boundary at the leg caps.
The example exhibits an admissible conductor pattern;
it does not establish population of the particular amplitude bin
\(\mathcal C_+\), nonzero original weights there, or a lower bound
for its sector energy.

## 6. All-scale primitive completion and two stronger displayed-leg sectors

The [short-family manuscript](../short_families/short_family_reductions.tex),
Analytic input `input:poisson` and Lemma `sfac:lem:completion`, already
derive the all-scale masked primitive remainder bound
\[
 \left|\sum_k\vartheta(k)\mathbf1_{(k,E)=1}V(Nk/X)\right|
       \ll_V\tau(E)\sqrt Q
       \quad(X>0)
 \tag{18a}
\]
for a nonprincipal native primitive inducing character \(\vartheta\)
of conductor norm \(Q\). The \(A=0\) instance is substantive even
when \(QNE/X\) is large. There is no principal zero frequency here.

For completeness, primitive Poisson at \(t=X/Q\) has prefactor
\(\sqrt Q\,t\). The radial Schwartz lattice sum of its nonzero
frequencies is \(O_V(t^{-1})\) for every \(t>0\), so its absolute
value is \(O_V(\sqrt Q)\) at every scale. For each \(e\mid E\),
the divisor expansion replaces \(X\) by \(X/Ne\) and multiplies
by \(\mu(e)\vartheta(e)\), without changing the primitive
conductor. The same bound then costs \(\sqrt Q\) per divisor.
This proves (18a) without a favorable combined-modulus ratio.

This native argument applies to the common row ratio used in (3).
In the source's fixed ray presentation, the common twist cancels to
its zero mask, and on ideals coprime to the original rows the ratio
is \(\chi_k(uv^5)^{s_\chi}\). Removing its sixth powers gives a
native sixth-power-free numerator with its unit retained; the
opposite orientation is handled by conjugation. This identifies the
same primitive inducing character, rather than modifying the original
zero extension. Its additional squarefree mask \(E_{uv}\) has
polynomial norm in \(U\). Consequently the divisor estimate makes
\(\tau(E_{uv})\ll_\varepsilon U^\varepsilon\). The profile
\(V=|B|^2\) is smooth, radial and annular; the required derivative
profiles have the same permitted finite height costs. Thus (18a)
and the conditional Mellin bound together give
\[
 |K(u,v)|\ll U^\varepsilon\mathcal H^a
          \min\{N^{-1/8},\sqrt{Q_{uv}}/N\},
          \qquad c(u)\ne c(v).
 \tag{18b}
\]
The Poisson part uses the existing native package, with the same
arithmetic scope; it needs no stronger global family hypothesis.

Suppose one of the two displayed leg conductors is at most
\(U^q\). Equation (6) bounds its weighted neighbor mass by
\(WU^{q+\varepsilon}\). Apply the Poisson member of (18b) to
this leg, its Mellin member to the other leg, and retain the actual
endpoint bound. The resulting chain majorant is
\[
 |J_{\text{some displayed leg}\le U^q}|
       \ll U^\varepsilon\mathcal H^a
                   N^{d-9/8}A^2WU^{3q/2}.
 \tag{18c}
\]
The target gap is the single-neighbor baseline in (13), before its
cutoff, plus \((7/8)m-3q/2\). At \(q=39/100\), its uniform
lower bound is
\[
 \frac{3047}{12500}+\frac78\frac25
                  -\frac32\frac{39}{100}
     =\frac{219}{25000}=0.00876.
 \tag{18d}
\]
An endpoint conductor cap alone cannot be substituted here: its
conductor does not occur in either displayed kernel.

For the product of the two displayed leg conductors, apply Poisson
to both kernels. On a dyadic rectangle with caps \(V_1,V_2\),
the tree mass (8) costs \(AW^2V_1V_2\), and the two kernels
cost \(\sqrt{V_1V_2}/N^2\). Hence a dyadic product decomposition
gives
\[
 |J_{Q_{uv}Q_{vh}\le U^\sigma}|
       \ll U^\varepsilon\mathcal H^a
                 N^{d-2}AW^2U^{3\sigma/2}.
 \tag{18e}
\]
At \(\sigma=103/100\), the available tree baseline (12), the
improvement \((7/4)m\), and this product cost leave
\[
 \frac{10644}{12500}+\frac74\frac25
                    -\frac32\frac{103}{100}
    =\frac{163}{25000}=0.00652.
 \tag{18f}
\]
The dyadic logarithms, divisor losses, profile derivatives and height
costs must fit the same preallocated arbitrarily small loss as before.
This product sector concerns the two displayed kernels. It does not
assert (18e) for a tree containing only one displayed leg.

The coupled count also improves when combined with both Poisson
kernel bounds. For fixed endpoints put
\(F_*=Q_{uh}\), \(P_*=Q_{uv}Q_{vh}\). The primitive conductor
of the endpoint quotient divides the product of the two primitive leg
conductors, so \(F_*\le P_*\); the local good-conductor identity
already gives the needed fixed-constant version. On a dyadic range
\(P_*\asymp P\), the count (15) is therefore
\(\ll U^\varepsilon\sqrt{P/F_*}\). The sum over the actual
middle weights times both kernel bounds is at most
\[
 WU^\varepsilon\mathcal H^a
       \frac{\sqrt P}{N^2}\sqrt{P/F_*}
       =WU^\varepsilon\mathcal H^a\frac{P}{N^2\sqrt{F_*}}.
 \tag{18g}
\]
If \(P_*^2/F_*\le U^{15/8}\), the right side is
\(\ll WN^{-2}U^{15/16+\varepsilon}\mathcal H^a\).
Sum the dyadic ranges and the actual endpoint weights, retaining
\(|S_uS_h|\ll N^dU^\varepsilon\mathcal H^a\), to obtain
\[
 |J_{(Q_{uv}Q_{vh})^2/Q_{uh}\le U^{15/8}}|
       \ll N^{d-2}A^2WU^{15/16+\varepsilon}\mathcal H^a.
 \tag{18h}
\]
The target reserve is at least
\[
 \frac{3047}{12500}+\frac74\frac25-\frac{15}{16}
       =\frac{313}{50000}=0.00626.
 \tag{18i}
\]
All product norms are polynomial in \(U\), so the extra dyadic
logarithm fits the same arbitrary small loss. This argument is an
absolute sector estimate for the original weights and endpoints;
it does not introduce a new positive matrix after conductor filtering.

This last sector also has physical norm geometry outside all five
previous cuts. With distinct good factors of norm exponents
\(Na\asymp U^{71/100}\) and
\(Nb,Nc,Nd\asymp U^{29/100}\), take
\(u=ab\), \(h=ac\), \(v=ad\). All three quotient conductors
have exponent \(29/50\). Their displayed product has exponent
\(29/25>103/100\), its ratio to the endpoint has exponent
\(29/50>12/25\), whereas its squared product divided by the
endpoint has exponent \(87/50<15/8\). The one-edge and any-tree
cuts also fail. This demonstrates the strictly larger raw physical
geometry of the sixth sector, without a selected-bin population or
weight lower bound.

### Why a large mask still blocks a rapid-decay conclusion

For the original untrimmed zero extension, at a good prime dividing either physical row, unequal valuations leave
that prime in the primitive quotient conductor. Equal nonzero
valuations cancel its phase but preserve the original zero at that
prime in the extra deletion mask. Hence the quotient conductor times
its extra deletion ideal contains the entire good radical of the two
rows. Within the imported tame good-prime convention this is comparable
to, and at least a fixed multiple of, either original primitive
conductor. On \(\mathcal C_+\),
\[
 L_{uv}\gg Q_{\psi_u}>U^{2m-1/1000},\qquad
 L_{uv}/N\gg U^{m-1/1000}.
 \tag{18}
\]
Since \(m\ge2/5\), the standard small-completion-ratio argument gives
no decay from this untrimmed modulus, even if \(Q_{uv}\) itself is small. This is a
limitation of that available completion bound, not a lower bound for
the kernel. It is specifically a limitation of the \(A>0\) rapid-decay
member of the completion lemma. It does not obstruct its \(A=0\)
square-root member (18b), which proves the two displayed-leg sectors
above with all zeros intact.

For a fixed compact column annulus, a deleted prime above its upper
norm cap divides no column and can be removed from that mask without
changing the sum. The lower bound (18) does not apply automatically
to this trimmed effective modulus. Exploiting such a smaller mask
would require its own quantitative regime and a proof for the actual
weighted rows; it does not follow from a small primitive quotient
conductor alone. The present theorem does not exclude further gains
from a correctly bounded effective mask.

## 7. Remaining arithmetic target and finite-check status

Assign to the first sector all distinct-character triples with any
quotient conductor at most \(U^{6/25}\); assign next those with
any two-edge product at most \(U^{17/20}\); then assign, in order,
the still unassigned product-ratio sector
\(Q_{uv}Q_{vh}\le U^{12/25}Q_{uh}\), the displayed one-leg
sector \(\min(Q_{uv},Q_{vh})\le U^{39/100}\), and the displayed
leg-product sector \(Q_{uv}Q_{vh}\le U^{103/100}\); finally
assign the still unassigned coupled-Poisson sector
\((Q_{uv}Q_{vh})^2\le U^{15/8}Q_{uh}\).
Reversal preserves each condition and each previous exclusion.
The remaining exact chain therefore satisfies all six complementary
conditions:

- every quotient conductor exceeds \(U^{6/25}\);
- every two-edge product exceeds \(U^{17/20}\);
- \(Q_{uv}Q_{vh}>U^{12/25}Q_{uh}\);
- both displayed leg conductors exceed \(U^{39/100}\);
- their product exceeds \(U^{103/100}\);
- their squared product exceeds \(U^{15/8}Q_{uh}\).

This remaining signed chain has not been estimated at the target
exponent. The rectangle (16) is already inside the product-ratio
sector and supplies a stronger estimate on that specified subregion.

The full repeated-character sector was already controlled by note 3.
Adding these six nonprincipal sectors enlarges the
conductor regimes paid for by the existing conditional inputs. It is
not a coefficient-zero cancellation and does not rely on a new
arithmetic estimate for the original weight \(w\). No asymptotic
nonemptiness assertion for the selected amplitude-bin sectors is used
or proved. The full positive energy and its original signed residual
remain open.

The [standard-library checker](../numerics/check_mixed_conductor_neighbors.py)
was read and run twice by this audit agent, independently of its author.
Both runs reproduced the
[saved record](../numerics/mixed_conductor_neighbors_record_20261008.json)
byte for byte. It reports 26,966 assertions over 216 sixth-power-free
formal rows, with 40 fixed endpoint pairs. Its finite valuation checks
include the exact local identity (14), the coupled norm identity,
the fixed-row multiplicity \(5^{\omega(f)}\), the middle-count
majorant and its empty range, and the direct product-ratio count.
Equal-norm prime symbols remain distinct.

Its separate masked finite frame has 12 rows and retains 60 deleted
entries. The actual endpoint chains satisfy the neighbor and tree
weighted-count majorants; four selected-chain witnesses are nonzero.
The reversal tests verify reality of the one-edge union and all six
disjoint conductor groups. At four formal scales, the complete
distinct-row chain equals the sum of those groups and the remainder
exactly. The sampled partition includes no \(\Gamma_5\) entries;
its theorem is proved analytically above, not by a finite population
claim. These are
formal frames, not a construction of physical residue symbols or of
the source's selected amplitude bins. The general reversal-compatible
disjoint partition, native Poisson and the dyadic product steps are
justified by the analytic and algebraic arguments above; no claim
that these are proved by a finite sample is made.

The reserve identities are checked exactly as
\(47/12500\), \(19/12500\), \(469/25000\),
\(219/25000\), \(163/25000\), and \(313/50000\).
The checker also
tests the algebra transferring the existing baseline margin, rather
than revalidating its continuous application-region certificate. Its
exact legal-point calculation reproduces the raw sharp middle-count
budget and deficit discussed in the continuation note.
Record SHA-256:
`d099d059e7cfb4da6af462a9daecf7222523c18fac64e762ea341d251e9e0934`.
These checks validate finite algebra and budget arithmetic, not physical
reciprocity, the source family/growth or endpoint hypotheses, profile
uniformity, an asymptotic population claim for selected bins, or the
remaining unbounded correlation estimate.

## 8. Continuation audit: positivity, the sharp raw count and its budget

The final [mixed continuation note 5](../mixed_character_families/notes/5_MIXED_NEIGHBOR_CONTINUATION_20261008.md)
was read after its six-sector update. Its table, successive exclusions,
strict complement and order-zero versus positive-order qualifications
agree with sections 3--7 above. The remaining raw-family obstruction is
distinct from a lower bound for the actual weighted energy.

The positivity argument retains the actual probe. Let \(G_0\) be the
block diagonal part of \(G\), with blocks indexed by inducing primitive
character, and let \(G_1=G-G_0\). In the expansion of
\(f^*G_1^2f\), each displayed leg joins different character blocks.
Thus its endpoints either differ too, giving exactly \(J_{\ne}\),
or lie in the same block, giving \(J_{\rm end}\). Hence
\[
 f^*G_1^2f=J_{\ne}+J_{\rm end},\qquad J_{\rm end}\ge0.
 \tag{19}
\]
Weighted Schur with test vector \(\sqrt w\) bounds
\(\|G_1\|\ll A N^{-1/8}U^\varepsilon\mathcal H^a\).
Consequently
\[
 J_{\ne}\le\|G_1f\|^2
      \ll N^{-1/4}A^2E U^\varepsilon\mathcal H^a.
 \tag{20}
\]
This is a bound for the full off-block expression. It does not assert
positivity or the same block identity after filtering by a conductor
sector. Using the actual pointwise endpoint bound \(E\ll AN^d\)
returns precisely the coarse distinct-character bound
\(N^{d-1/4}A^3\). There is no concealed cancellation gain.

The analogous actual-energy version of a uniformly counted middle
sector costs \(N^{-1/4}AEWU^\kappa\). Indeed the endpoint sum
after absolute majorization is
\((\sum_u w_u|S_u|)^2\le AE\), by Cauchy--Schwarz. Thus this
variant also preserves the actual original endpoints and weights.

Subtracting the target exponent \(T\) from the coarse absolute
exponent gives exactly
\[
 (7/4-2d)m+3(s-\mu).
 \tag{21}
\]
When \(\mu\ge s\), the simpler positive bound
\(E\ll U^{1-\mu+dm}\) already meets the desired energy exponent.
In the remaining region \(\mu<s\), (21) is at least
\((7/4-2\cdot21/50)(2/5)=91/250\). On the selected rows the
physical conductor exponent obeys \(\theta>2m-1/1000\).
Therefore the reflected plain bound improves the endpoint-product
envelope by at most \(d/1000\le21/50000\), which cannot cover
that deficit. These are failures of the available upper-bound method,
not lower bounds for any arithmetic response.

For the raw sharp count, choose good prime ideals \(a,b,c\) of
norms comparable to \(U^{1/2}\), fix \(u=ab\), \(h=ac\), and
vary \(v=ad\) with \(d\) in a compatible fixed narrow prime
window, distinct from \(a,b,c\). All three physical norms are of
order \(U\), and all three row-ratio conductor norms are of order
\(U\). The imported untwisted fixed-field prime ideal theorem gives
\(\asymp U^{1/2}/\log U\) possible \(d\). Retaining a populated
class of the finitely many presentation choices costs only a fixed
factor; no growing-character PNT is required. The individual primitive
row conductors are also of order \(U\), so the numerical primitive
conductor gate is satisfied on the operational region \(m<1/2\).
Membership in the selected zero/profile bin is a separate condition
and is not inferred from this gate.

This example attains \(\kappa=1/2\) in the raw middle count up to
logarithms. Its leg product, product/endpoint ratio, and squared
product/endpoint ratio have exponents \(2,1,3\), respectively, so
it lies outside all six cuts. At these conductors the Poisson kernel
bound is \(U^{1/2-m}\), whereas the conditional Mellin bound is
\(U^{-m/8}\); the latter is stronger throughout the operational
region. Thus the order-zero extension does not remove this example.
This is an obstruction to improving the uniform unweighted count,
not to a signed weighted correlation estimate. No selected weight
lower bound or asymptotic selected-bin population is asserted.

Finally, note 5's exact operational parameter point reproduces
\[
 \mathcal B
   =\frac{92902792407}{338300000000}
   =0.274616590029559\ldots,
 \qquad
 \frac12-\mathcal B
   =\frac{76247207593}{338300000000}
   =0.225383409970440\ldots.
 \tag{22}
\]
The point satisfies the stated continuous operational inequalities
and strict inverse capacities; its role is a legal exponent-budget
example under those source conventions, not an arithmetic attainment
claim. The exact fractions are independently checked by the replayed
record. The next target remains the original signed two-kernel middle
sum with its selected inverse/physical-prime weight, or a quantitatively
stronger conditional mass bound on that same weight.
