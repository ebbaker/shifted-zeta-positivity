# Nonprincipal conductor-neighbor sectors of the actual open chain

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Status: conditional estimates for specified potentially nonzero sectors of the actual
distinct-character chain. The complementary chain estimate and original
mixed energy target remain unproved. Same-model audits and finite checks
are internal validation, not independent specialist review or formal
proof verification.

This carries out the bounded task in the short-family
[continuation note 26](../../short_families/notes/26_SHORT_FAMILY_COFACTOR_CONTINUATION_20261008.md).
The new ingredient is a local count of physical rows in a primitive
row-ratio conductor neighborhood, and a stronger intersection count for
two neighborhoods sharing a middle row. Both preserve the actual sixth-
power-free family and all canceled-ramification zeros. They control parts
of the pairwise-inequivalent open chain; they are not additional
coefficient-zero sectors.

## 1. Exact frame, conditional inputs and target exponent

Keep the conventions, selectors, actual inverse/plain/physical-prime
polynomials, common separating parameters, profiles and height costs of
[notes 1](1_MIXED_CONDUCTOR_REFINEMENT_20261008.md),
[2](2_SELECTED_INVERSE_DISTRIBUTION_20261008.md), and
[3](3_ACTUAL_PROBE_CUBIC_TARGET_20261008.md). In particular,
\[
 w_u=\mathbf1_{u\in\mathcal C_+}|M_r(u)Q_I(u)|^2,
 \quad A=\sum_u w_u,\quad W=\max_u w_u,\quad N=U^m.
 \tag{1}
\]
The physical rows are sixth-power-free elements with \(Nu\ll U\).
Write \(c(u)\) for their inducing primitive character, and let
\(Q_{uv}\) be the norm of the primitive conductor inducing the
quotient \(\psi_u\overline{\psi_v}\). It is symmetric in \(u,v\).
The kernel and actual endpoint plain sums are
\[
 K(u,v)=N^{-1}\sum_k |B(Nk/N)|^2
                    \psi_u(k)\overline{\psi_v(k)},\qquad
 S_u=N^{-1/2}\sum_k\psi_u(k)B(Nk/N).
 \tag{2}
\]
Every column exclusion and zero mask stays in these expressions.

The exact positive functional is
\[
 J=\sum_{u,v,h}w_uw_vw_h\overline{S_u}K(u,v)K(v,h)S_h.
 \tag{3}
\]
Its pairwise-inequivalent part \(J_{\ne}\) restricts to three distinct
primitive characters. Use the target exponent
\[
 h_3=3[1-(1-d)m-s],\qquad T=h_3+m.
 \tag{4}
\]
An upper bound \(\operatorname{Re}J_{\ne}\ll
U^{T+\varepsilon}\mathcal H^a\) is sufficient by note 3.

The following analytic inputs remain conditional, with precisely their
source scope:

- The source global family and quantitative primitive growth/deleted-
  Euler-factor inputs give
  \(|K(u,v)|\ll U^\varepsilon\mathcal H^aN^{-1/8}\) when
  \(c(u)\ne c(v)\).
- The buffered plain hypothesis for the actual profiles gives
  \(|S_uS_h|\ll U^\varepsilon\mathcal H^aN^d\) on selected rows.
- The selected positive inverse mass and physical-profile envelopes give
  \(A\ll U^{1-\mu+\varepsilon}\mathcal H^a\) and
  \(W\ll U^{g+\varepsilon}\mathcal H^a\), where
  \(g=d(r+z)\) and \(\mu\ge0\) are those of notes 1--2.
- The source's exact local sextic ramification formula, common orientation
  and fixed ray presentation identify the good part of \(Q_{uv}\)
  as the product of primes where the sixth-power-free row valuations
  differ. Fixed bad-prime conductor factors have bounded norm.
- The native primitive-Poisson input, in the all-scale masked form of
  [the short-family manuscript](../../short_families/short_family_reductions.tex),
  Lemma `sfac:lem:completion`, is additionally used in section 6.
  Its order-zero branch bounds a nonprincipal masked sum by
  \(\tau(E)\sqrt Q\), independently of the size of the full deletion
  modulus. Its applicability to the row quotient and profile
  \(|B|^2\), with the permitted derivative and height costs, is
  part of this native source input.

Uniformity is required over the original operational buffered region and
permitted derivative/height profiles. All arbitrary small analytic losses
and finite polynomial height costs must be allocated in the order of
notes 1--3, before the positive Sobolev step. The combinatorial deductions
below neither prove these inputs nor extend them to arbitrary coefficients.

Two previously certified bounds will be used without another continuous
parameter certificate. On that region, \(d\le21/50\), \(m\ge2/5\),
\(s>0\), and
\[
 M_0:=1-g-(11/4-3d)m-3s\ge147/12500.
 \tag{5}
\]
This is note 2's two-equal cyclic margin before its favorable \(2\mu\)
term. The endpoint-equal open-chain margin of note 3 is at least
\[
 T-\{2(1-\mu)+g+(d-1/4)m\}\ge3047/12500.
 \tag{6}
\]

## 2. A physical row-ratio conductor neighborhood

For good prime ideals define
\[
 f_{uv}=\prod_{\substack{p\notin S\\v_p(u)\ne v_p(v)}}p.
 \tag{7}
\]
The valuations of both rows lie in \(\{0,\ldots,5\}\). The native
local quotient has exact exponent \(v_p(u)-v_p(v)\) modulo six,
up to the fixed common invertible orientation. Thus a good prime is
ramified exactly when these valuations differ. Fixed ray phases cannot
cancel its ramification. Consequently
\[
 f_{uv}\mid\mathfrak q_{uv},\qquad
 Nf_{uv}\le Q_{uv}\le C_S Nf_{uv}.
 \tag{8}
\]
Only the right-hand comparison uses the bounded fixed bad part. This
statement concerns the primitive inducing conductor; no equality of the
imprimitive deletion masks is asserted.

Fix \(u\) and a squarefree good ideal \(f\). If \(f_{uv}=f\),
the good valuations of \(v\) outside \(f\) equal those of \(u\).
At each prime of \(f\) there are at most five alternative valuations.
At fixed bad primes there are at most six choices, and a fixed ideal has
at most six element generators. Therefore
\[
 \#\{v\text{ sixth-power-free}:f_{uv}=f\}
       \le6^{|S|+1}5^{\omega(f)}.
 \tag{9}
\]
Imposing the physical dyad or the actual selected amplitude bin can only
decrease this count. Elementary ideal counting and the divisor bound give,
for every \(V\ge1\),
\[
 \#\{v\in\mathcal C_+:Q_{uv}\le V\}
   \ll_{\varepsilon,S}V^{1+\varepsilon},\qquad
 \sum_{\substack{v\in\mathcal C_+\\Q_{uv}\le V}}w_v
   \ll_{\varepsilon,S}W V^{1+\varepsilon}.
 \tag{10}
\]
The case \(f=1\) includes different primitive characters supported only
at fixed bad primes. They remain bounded in number. Equality of primitive
characters is the special bounded-fiber case of note 2, rather than the
whole neighborhood in (10).

## 3. Any one small edge of the distinct-character triangle

For pairwise-inequivalent \((u,v,h)\), both kernel factors in (3) are
nonprincipal. The conditional bounds in section 1 give
\[
 |\overline{S_u}K(u,v)K(v,h)S_h|
       \ll U^\varepsilon\mathcal H^aN^{d-1/4}.
 \tag{11}
\]
This retains the actual endpoints before majorizing their moduli.

If any one of \(Q_{uv},Q_{vh},Q_{uh}\) is at most \(V\), summing
its neighbor weight by (10) and the remaining free row by \(A\) gives
\[
 \sum_{u,v,h}w_uw_vw_h\mathbf1_{\text{some edge }\le V}
       \ll U^\varepsilon A^2W V
 \tag{12}
\]
for polynomial-size \(V\), after reallocating epsilon. The same proof
works for the endpoint edge \(u,h\); it does not require that the
small edge be one of the displayed kernels.

Let \(\Gamma_1\) denote the pairwise-inequivalent triples with
\[
 \min\{Q_{uv},Q_{vh},Q_{uh}\}\le U^{6/25}.
 \tag{13}
\]
Their actual signed contribution obeys, by (6),
\[
 \boxed{|J_{\Gamma_1}|
 \ll U^{T-47/12500+\varepsilon}\mathcal H^a,\qquad
       3047/12500-6/25=47/12500.}
 \tag{14}
\]
This is a growing nonprincipal conductor sector. It includes different
primitive characters and is not a coefficient identity forcing zero.

## 4. Two edges with a bounded conductor product

Any two edges of the three-vertex triangle form a tree. For fixed edge
caps \(V_1,V_2\), choose their common vertex as the first row. Its
weight sums to \(A\), and (10) bounds the two other neighbor masses
independently. Thus
\[
 \sum_{u,v,h}w_uw_vw_h\mathbf1_{\text{two specified edges}\le V_1,V_2}
       \ll U^\varepsilon A W^2 V_1V_2.
 \tag{15}
\]
For a product cap, partition the two conductor norms into fixed binary
intervals. If their product is at most \(U^\sigma\), the interval
upper bounds have product at most \(4U^\sigma\). There are
\(O(\log^2U)\) relevant pairs because \(Q_{uv}\ll U^2\).
Combining (11) and (15), and summing the three trees, gives
\[
 |J_{\text{some two-edge product}\le U^\sigma}|
       \ll U^\varepsilon\mathcal H^a
                      N^{d-1/4}A W^2U^\sigma.
 \tag{16}
\]

The available exponent reserve is stronger than the coarse all-equal
cyclic comparison. A direct identity from (4)--(5) is
\[
 \begin{split}
 T-\{(1-\mu)+2g+(d-1/4)m\}
 &=2M_0+(15/4-4d)m+\mu+3s\\
 &\ge\frac{294}{12500}
       +(15/4-4\cdot21/50)\frac25
       =\frac{10644}{12500}.
 \end{split}
 \tag{17}
\]
Let \(\Gamma_2\) consist of pairwise-inequivalent triples outside
\(\Gamma_1\) satisfying
\[
 \min\{Q_{uv}Q_{vh},Q_{uv}Q_{uh},Q_{vh}Q_{uh}\}
                  \le U^{17/20}.
 \tag{18}
\]
Equations (16)--(17) prove
\[
 \boxed{|J_{\Gamma_2}|
       \ll U^{T-19/12500+\varepsilon}\mathcal H^a,
       \qquad10644/12500-17/20=19/12500.}
 \tag{19}
\]
Restricting to the disjoint set outside \(\Gamma_1\) does not enlarge
the absolute majorant. No conductor cutoff has been inserted into an
asserted positive Gram identity: this is a sector bound after the exact
open-chain expansion.

## 5. Coupled middle-row intersection, conditioned on the endpoints

There is a more specific count retaining the endpoint conductor. Fix
\(u,h\), and put \(F=f_{uh}\), \(P=f_{uv}\), \(Q=f_{vh}\).
At a good prime where the endpoint valuations differ, \(v\) either
equals one of them, giving that prime in precisely one of \(P,Q\),
or equals neither, giving it in both. Let \(A_0\mid F\) be the
product of primes of the second kind. At a prime outside \(F\), the
endpoints agree; if \(v\) differs, that prime occurs in both \(P,Q\).
Let \(B_0\) contain these latter primes. Then exactly
\[
 PQ=F A_0B_0^2,\qquad A_0\mid F,\qquad(B_0,F)=1,
 \tag{20}
\]
with all three ideals squarefree except the displayed square of \(B_0\).
This is a local identity of ideals, not an independence assumption.

If \(Q_{uv}\le V_1\), \(Q_{vh}\le V_2\), then
\[
 NB_0\le\sqrt{V_1V_2/NF}.
 \tag{21}
\]
There are no solutions if \(NF>V_1V_2\). For each \(B_0\),
the valuations on \(F\) have at most \(6^{\omega(F)}\) choices
and those on \(B_0\) at most \(5^{\omega(B_0)}\); everything
else is fixed. Since \(NF\ll U^2\), the divisor bound absorbs the
first factor into \(U^\varepsilon\). Summing \(B_0\) by (21)
and using (8) proves
\[
 \boxed{
 \#\{v\in\mathcal C_+:Q_{uv}\le V_1,Q_{vh}\le V_2\}
 \ll_{\varepsilon,S}U^\varepsilon
        \left(1+\sqrt{V_1V_2/Q_{uh}}\right).}
 \tag{22}
\]
Here \(V_1,V_2\ll U^2\); their small preliminary counting losses
are absorbed into the displayed \(U^\varepsilon\). The count is
zero if \(Q_{uh}>C_SV_1V_2\). The \(+1\) and fixed constant
keep (22) correct at the bad-prime and unit boundaries.

There is also a direct ratio version without separate leg caps. By (8)
and (20),
\[
 \frac{Q_{uv}Q_{vh}}{Q_{uh}}
      \asymp_S NA_0\,(NB_0)^2.
 \tag{23}
\]
Thus a ratio cap \(Q_{uv}Q_{vh}\le RQ_{uh}\) forces
\(NB_0\ll_S\sqrt R\). The same enumeration, with the
\(6^{\omega(F)}\) choices on \(F\) absorbed into
\(U^\varepsilon\), proves for polynomial-size \(R\ge1\)
\[
 \boxed{\#\{v\in\mathcal C_+:Q_{uv}Q_{vh}\le RQ_{uh}\}
       \ll_{\varepsilon,S}U^\varepsilon(1+\sqrt R).}
 \tag{24}
\]
Multiplying by \(W\) bounds the actual weighted middle-row mass.
This is a coupled middle-row estimate from arithmetic counting; it
does not assume an extra signed kernel cancellation.

Let \(\Gamma_3\) consist of triples outside
\(\Gamma_1\cup\Gamma_2\) satisfying
\[
 Q_{uv}Q_{vh}\le U^{12/25}Q_{uh}.
 \tag{25}
\]
Equations (6), (11) and (24) give
\[
 \boxed{|J_{\Gamma_3}|
      \ll U^{T-47/12500+\varepsilon}\mathcal H^a,
 \qquad3047/12500-6/25=47/12500.}
 \tag{26}
\]
For comparison, the narrower rectangle
\(Q_{uv},Q_{vh}\le U^{3/5}\), \(Q_{uh}\ge U^{3/4}\)
has middle-row expense at most \(U^{9/40}\) by (22),
and therefore the stronger reserve
\[
 3047/12500-9/40=469/25000.
 \tag{27}
\]
It lies within (25), because \(2(3/5)-3/4=9/20<12/25\).
The norm geometry can occur outside the earlier cuts. For instance choose
distinct good prime ideals \(a_0,b_0,c_0,d_0,e_0\) with norm exponents
\(21/50,29/100,29/100,29/100,29/100\), and take rows represented by
\(u=a_0b_0c_0\), \(v=a_0b_0d_0\), \(h=a_0d_0e_0\).
They are squarefree with
norms of order \(U\), both displayed leg conductor exponents are
\(29/50<3/5\), and the endpoint conductor exponent is
\(29/25>3/4\). Every pair product then has exponent \(29/25\)
or \(87/50\),
above \(17/20\), and every single edge is above \(6/25\).
Taking narrow fixed norm windows supplies the corresponding asymptotic
norm geometry under the existing fixed-field prime ideal theorem. This
does not assert a lower bound for their actual weights or membership in
the specific selected amplitude bin. It demonstrates that the sector is
not empty merely by the physical row/conductor geometry.

## 6. Native order-zero Poisson bounds and three further sectors

On the original columns coprime to the physical row masks, the common
twist cancels from \(\psi_u\overline{\psi_v}\). Sextic
multiplicativity identifies the quotient with the character indexed by
the sixth-power-free part of \(uv^5\), or its conjugate for the
opposite fixed orientation, up to the fixed ray data. Removing sixth
powers preserves the primitive inducing character. Every canceled
ramification prime remains in the extra deletion ideal \(E\).
Its norm is polynomial in \(U\), because its good part divides
\(\operatorname{rad}_S(uv)\), so \(\tau(E)\ll U^\varepsilon\).
Fixed bad-prime/ray choices contribute bounded factors.

For \(c(u)\ne c(v)\) the primitive quotient is nonprincipal. The
source masked-completion lemma at order zero has no principal frequency
and gives a complete sum of size \(O(\tau(E)\sqrt{Q_{uv}})\)
at every column scale. Apply it to the actual smooth profile \(|B|^2\)
and divide by \(N\). The permitted profile seminorms and height
costs are retained; in particular common separating parameters are fixed
before the derivative estimates and positive Sobolev step. Combining
this additional native input with the global kernel bound gives
\[
 |K(u,v)|\ll U^\varepsilon\mathcal H^a
       \min\{N^{-1/8},\sqrt{Q_{uv}}/N\}.
 \tag{28}
\]
The integral of \(|B|^2\) need not vanish, since nonprincipality
already kills the zero frequency. No deletion prime has been dropped.

First use the Poisson estimate on one displayed leg with conductor
at most \(V\), and the global estimate on the other. Equation (10)
then gives
\[
 |J_{\text{one displayed leg}\le V}|
   \ll U^\varepsilon\mathcal H^a
                    N^{d-9/8}A^2W V^{3/2}.
 \tag{29}
\]
Let \(\Gamma_4\) be the triples outside \(\Gamma_1,\Gamma_2,
\Gamma_3\) satisfying
\[
 \min\{Q_{uv},Q_{vh}\}\le U^{39/100}.
 \tag{30}
\]
The reserve in (6) increases by \((7/8)m\ge7/20\), hence
\[
 \boxed{|J_{\Gamma_4}|
  \ll U^{T-219/25000+\varepsilon}\mathcal H^a,\quad
  3047/12500+7/20-(3/2)(39/100)=219/25000.}
 \tag{31}
\]
This estimate concerns a displayed kernel leg. It does not subsume the
endpoint-edge part of \(\Gamma_1\).

Next use (28) on both displayed kernels. On a displayed-product dyadic
bin, their product is bounded by \(U^\varepsilon\mathcal H^a
\sqrt{Q_{uv}Q_{vh}}/N^2\). The tree count (15), followed by
dyadic summation, yields
\[
 |J_{Q_{uv}Q_{vh}\le U^\sigma}|
    \ll U^\varepsilon\mathcal H^a
                      N^{d-2}A W^2 U^{3\sigma/2}.
 \tag{32}
\]
Define \(\Gamma_5\), outside all earlier sectors, by
\[
 Q_{uv}Q_{vh}\le U^{103/100}.
 \tag{33}
\]
The reserve in (17) increases by \((7/4)m\ge7/10\). Thus
\[
 \boxed{|J_{\Gamma_5}|
  \ll U^{T-163/25000+\varepsilon}\mathcal H^a,\quad
  10644/12500+7/10-(3/2)(103/100)=163/25000.}
 \tag{34}
\]
The product in (33) is that of the displayed legs. The earlier
\(\Gamma_2\) still includes either tree involving the endpoint edge.

Finally combine both Poisson kernels with the coupled count, without
individual conductor caps. For fixed endpoints write
\(\Pi=Q_{uv}Q_{vh}\), \(\Phi=Q_{uh}\). The conductor identity
(20) and comparison (8) imply \(\Phi\ll_S\Pi\) for every
nonempty middle-row set. In a dyadic \(\Pi\)-bin, (24) bounds the
middle weight by
\(WU^\varepsilon(1+\sqrt{\Pi/\Phi})\ll_S
WU^\varepsilon\sqrt{\Pi/\Phi}\). Multiplication by the two-kernel
bound gives
\[
 WU^\varepsilon\mathcal H^a\frac{\Pi}{N^2\sqrt\Phi}.
 \tag{35}
\]
There are \(O(\log U)\) bins. If
\(\Pi^2\le U^\lambda\Phi\), the last expression is at most
\(WU^{\lambda/2+\varepsilon}/N^2\). Multiplying the actual
endpoint bound and summing their weights proves
\[
 |J_{(Q_{uv}Q_{vh})^2\le U^\lambda Q_{uh}}|
       \ll U^\varepsilon\mathcal H^a
                      N^{d-2}A^2W U^{\lambda/2}.
 \tag{36}
\]
Define \(\Gamma_6\), outside all earlier sectors, by
\[
 (Q_{uv}Q_{vh})^2\le U^{15/8}Q_{uh}.
 \tag{37}
\]
Now the reserve in (6) increases by \((7/4)m\ge7/10\), so
\[
 \boxed{|J_{\Gamma_6}|
  \ll U^{T-313/50000+\varepsilon}\mathcal H^a,\quad
  3047/12500+7/10-15/16=313/50000.}
 \tag{38}
\]
The dyadic enlargement changes only fixed constants. For example,
\(u=a_0b_0\), \(v=a_0d_0\), \(h=a_0c_0\), with distinct good
prime norm exponents \(71/100,29/100,29/100,29/100\), has all
three edge exponents \(29/50\). It lies beyond the first five cuts
and satisfies (37), since \(3(29/50)<15/8\). This is again a
physical conductor geometry example, without a claim about membership
in the actual selected amplitude bin. The conductor
triangle inequality used in (35) also handles the unit and fixed bad
factors, rather than discarding the \(+1\) without justification.

## 7. Exact remaining chain and the completion limitation

Let \(\Gamma_{\rm rem}\) be the pairwise-inequivalent triples
outside these six successively disjoint sectors. Every selector is
invariant under reversal \(u\leftrightarrow h\). Since
\(K(h,v)=\overline{K(v,h)}\), their grouped sums and the
remaining sum are real. The exact partition gives
\[
 J_{\ne}=J_{\Gamma_{\rm rem}}
       +O\left(U^{T-19/12500+\varepsilon}\mathcal H^a\right).
 \tag{39}
\]
The remainder keeps all actual endpoints, weights and zero masks. Its
conductors satisfy all the strict inequalities
\[
 \begin{gathered}
 Q_{uv},Q_{vh},Q_{uh}>U^{6/25},\\
 Q_{uv}Q_{vh},Q_{uv}Q_{uh},Q_{vh}Q_{uh}>U^{17/20},\\
 Q_{uv}Q_{vh}>U^{12/25}Q_{uh},\qquad
 Q_{uv},Q_{vh}>U^{39/100},\\
 Q_{uv}Q_{vh}>U^{103/100},\qquad
 (Q_{uv}Q_{vh})^2>U^{15/8}Q_{uh}.
 \end{gathered}
 \tag{40}
\]
No bound at the target exponent is proved for this remainder. The
remaining sufficient task is its one-sided real upper bound
\(J_{\Gamma_{\rm rem}}\ll U^{T+\varepsilon}\mathcal H^a\).
Equation (39) partitions the expanded scalar chain; it does not infer an
additive energy identity from separate response-vector estimates.

These conductor norms belong to ratios of physical rows. They differ
from the column-ratio conductors of mixed note 1 and the individual row
conductors defining \(\mathcal C_+\). A small \(Q_{uv}\) does
not permit replacing the masked kernel by an unmasked primitive sum.
Its full completion/deletion modulus has good part comparable to
\(N\operatorname{rad}_S(uv)\): unequal valuations give primitive
ramification, whereas equal positive valuations retain deletion zeros.
On selected rows this untrimmed modulus is at least a constant times
either individual primitive row conductor and hence exceeds
\(U^{2m-1/1000}\), while the column scale is \(N=U^m\).
Positive-order completion therefore supplies no rapid modulus/scale
decay merely from small \(Q_{uv}\). The order-zero estimate (28)
remains valid and is exactly what sections 6's sectors use.

Primes above the fixed upper column norm cap may be removed from the
deletion mask without changing the sum. Exploiting this for positive-order
decay requires a further bound on the remaining effective mask and its
distribution among actual weighted rows, which the primitive conductor
cutoff alone does not supply. All six estimates above retain the masks.

## 8. Verification scope

The deterministic standard-library
[checker](../../numerics/check_mixed_conductor_neighbors.py) and saved
[record](../../numerics/mixed_conductor_neighbors_record_20261008.json)
verify the local valuation geometry without identifying distinct
equal-norm prime symbols, the exact identity \(PQ=FA_0B_0^2\),
neighbor and coupled counts, weighted tree bounds, the actual masked
frame expansion and its six-sector partition, and exact rational
reserves. The final record contains **26,966 assertions**, **216**
sixth-power-free valuation rows, **40** endpoint pairs, **60** deleted
frame entries and **four** nonzero one-edge sector witnesses. Two fresh
root replays and two further author replays were byte-identical to the
saved record, whose SHA-256 is
`d099d059e7cfb4da6af462a9daecf7222523c18fac64e762ea341d251e9e0934`.

Finite algebra does not verify the imported global family/growth input,
native primitive Poisson or reciprocity theorem, buffered plain estimate,
physical-profile inverse bounds, derivative/height uniformity, continuous
application-region certificate, or an unbounded mixed correlation.
Same-model audits by the other agents are internal checks. These
conditional estimates remove specified nonprincipal sectors; they do not
establish the full mixed energy, a stronger zero-free boundary, or an
implication from zeta-only quasi-RH.
