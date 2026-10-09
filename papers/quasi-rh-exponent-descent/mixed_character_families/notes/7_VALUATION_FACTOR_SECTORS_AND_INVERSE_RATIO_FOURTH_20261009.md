# Valuation-factor middle sectors and the direct inverse-ratio fourth moment

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel derivations and audits are same-model internal validation, not
independent specialist review or formal proof verification.

**Result.** Separating the exterior middle ideal by its five possible
valuations gives an eighth conditional sector estimate for the actual
distinct-character open chain. It uses the already imported sextic sieve
on sixth-power-free rows, with uniform reserve \(4031/1500000\), and
controls the higher-valuation example that survived
[note 6](6_WEIGHTED_MIDDLE_SIEVE_AND_DIRECT_ENERGY_20261009.md).
A different explicit raw valuation pattern survives the new estimate,
including the original primitive-conductor gate. In the parallel direct
fourth-moment route, the original coefficients and ideal-pair lemma
control small inverse-ratio conductors, leaving an exact signed
large-inverse-ratio correlation. Neither remaining correlation is proved.

This completes the bounded factor-separation and direct coefficient
expansion proposed in note 6. The research remains in mixed character
families; further short-family cofactor work stays deferred. Existing
working-tree results are retained, with session base
`6c343e83622e194268399033b2eee68cc7e5fbcd`.

## 1 The inherited chain and a sharper row operator

Use the original physical sixth-power-free rows, good/bad prime
conventions, unit/ray presentation, selector \(\mathcal C_+\), smooth
plain annulus, inverse polynomial, and whole physical prime slots of
notes 1--6. In particular,
\[
 w_u=\mathbf1_{\mathcal C_+}(u)|M_r(u)Q_I(u)|^2,
 \quad A=\sum w_u\ll U^{1-\mu+\varepsilon}\mathcal H^b,
 \quad W=\max w_u\ll U^{g+\varepsilon}\mathcal H^b,
\]
\[
 N=U^m,\quad g=d(r+z),\quad
 K(u,v)=N^{-1}\sum_k|B(\mathrm Nk/N)|^2
                         \psi_u(k)\overline{\psi_v(k)}.
\]
The actual endpoint factor satisfies
\(|S_m(u)S_m(h)|\ll N^dU^\varepsilon\mathcal H^b\).
The sufficient cubic-probe target is
\[
 T=3(1+dm-s)-2m,
\]
for the open chain with summand
\(w_uw_vw_h\overline{S_m(u)}K(u,v)K(v,h)S_m(h)\).
All three primitive row characters in this part are pairwise inequivalent.

Use the power-free-row form of the existing imported operator,
equation `eq:imported-sextic-sieve` and its finite native transfer in the
[short-family manuscript](../../short_families/short_family_reductions.tex):
\[
 \sum_{\substack{\mathrm Nt\le H\\t\ \text{sixth-power-free}}}
       \left|\sum_{\substack{\mathrm Nk_0\le X\\k_0\ \text{sixth-power-free}}}
                   b_{k_0}\chi_{k_0}(t)\right|^2
 \ll_\varepsilon(HX)^\varepsilon\Theta_6(H,X)\sum|b_{k_0}|^2,
\]
\[
 \Theta_6(H,X)=H+X+H^{5/6}X^{1/3}+H^{1/3}X^{5/6}.
 \tag{1}
\]
This is the \(n=6\) case of the already imported
[de Faveri Theorem 1.1](https://arxiv.org/html/2610.04045v1#Thmtheorem1.1).
Its index scale is the physical ideal norm. The row set in (1) is already
sixth-power-free, so the all-physical-row multiplicity term
\(XH^{1/6}\) from note 6 is unnecessary. Finite unit and fixed
bad-prime classes are split as in the existing presentation transfer;
the operator allows an arbitrary fixed coefficient vector in each class.
This note imports no new lower-order character theorem.

For fixed factors and an arbitrary selected subset of these varying rows,
the column treatment of note 6 applies unchanged. Write
\(k=\lambda^6k_0\), retain exactly
\[
 \chi_k(t)=\chi_{k_0}(t)\mathbf1_{(t,\lambda)=1},
 \tag{2}
\]
then remove that mask only after forming the nonnegative row square.
The squared norm of the normalized coefficient vector is
\(O(N^{-1}(\mathrm N\lambda)^{-6})\). Minkowski costs the
convergent ideal series \(\sum_\lambda(\mathrm N\lambda)^{-3}\).
The resulting squared-kernel average is
\[
 \sum_{\substack{\mathrm Nt\le U^y\\t\ \text{sixth-power-free}}}
               |K(u,a t)|^2
 \ll U^{\beta_6(y;m)+\varepsilon}\mathcal H^b,
\]
\[
 \beta_6(y;m)=\max\{y-m,0,5y/6-2m/3,y/3-m/6\}.
 \tag{3}
\]
The same estimate holds if the varying character is conjugated.
The fixed growing factors appear only as bounded phases and zeros in
the fixed column coefficients. All deletion zeros survive until the
positive-square enlargement; no signed selector is enlarged.

## 2 Separating valuations without replacing the actual middle row

For fixed endpoints, put
\(\mathfrak e=\operatorname{rad}_{\rm good}(uh)\), and decompose
the original middle row as in note 6 into a fixed unit/bad-prime class,
an endpoint-supported ideal \(a\), and the exterior ideal \(\xi\).
There are \(U^\varepsilon\) endpoint-supported choices. Uniquely write
\[
 \xi=\prod_{e=1}^5\xi_e^e,\qquad
 x_e=\log_U\mathrm N\xi_e,\qquad R_\xi=\sum_{e=1}^5x_e,
 \tag{4}
\]
where the \(\xi_e\) are squarefree, pairwise coprime good ideals
and are coprime with \(\mathfrak e\). Thus \(R_\xi\) is the
exterior radical exponent, whereas \(\sum e x_e\) is its full
physical exponent.

Choose a nonempty subset \(L\subseteq\{1,\ldots,5\}\) and one
of two orientations, with
\[
 c_+(e)=e,\qquad c_-(e)=6-e,
 \qquad t_{L,\pm}=\prod_{e\in L}\xi_e^{c_\pm(e)}.
\]
Freeze all \(\xi_e\) outside \(L\). Their number on fixed norm
blocks is at most \(U^{\sum_{e\notin L}x_e+\varepsilon}\).
The map from the remaining valuation factors to \(t_{L,\pm}\) is
injective on ideals: its prime valuations recover each \(\xi_e\).
Every such auxiliary ideal is sixth-power-free. The minus orientation
uses the exact zero-preserving identity
\[
 \chi_k\left(\prod_{e\in L}\xi_e^{6-e}\right)
       =\overline{\chi_k\left(\prod_{e\in L}\xi_e^e\right)}.
 \tag{5}
\]
At any common prime both sides are zero. No primitive character is
substituted after deleting a canceled phase. The auxiliary ideal is a
variable in the kernel coefficient representation; the selector and
weight still refer to the original row \(v\).

For a fixed complement, retain the actual selected subset and use
\(w_v\le W\) before Cauchy on the two full kernels. Enlarge only
the resulting squared-kernel sums to the ball of sixth-power-free ideals
of norm at most \(U^{\sum_{e\in L}c_\pm(e)x_e}\), then apply
(3). Coprimality and norm/profile restrictions are removed only inside
these nonnegative sums. Counting the frozen complement gives the cost
\[
 \Phi(\boldsymbol x;m)=
 \min_{\substack{\varnothing\ne L\subseteq\{1,\ldots,5\}\\
                  \pm}}
 \left\{\sum_{e\notin L}x_e+
       \beta_6\left(\sum_{e\in L}c_\pm(e)x_e;m\right)\right\}.
 \tag{6}
\]
There are 62 subset/orientation choices. Dyadic partitioning of the five
norms and assigning a minimizing choice costs only \(U^\varepsilon\).
Equation (6) uses the actual logarithmic norms; on each dyadic block its
upper endpoints change each cost by \(O(1/\log U)\), absorbed by
a fixed constant. It is not necessary that the whole block satisfy the
cut before the selected subblock is put into its positive squares.

For an endpoint-symmetric sector with \(\Phi\le\sigma\), summing
the endpoint weights and using their actual plain bounds proves
\[
 \boxed{|J_\Gamma|\ll A^2W N^dU^{\sigma+\varepsilon}\mathcal H^b.}
 \tag{7}
\]
The endpoint sum costs \(A^2\), with no additional endpoint count.
The sector is real by reversal of the endpoint chain; positivity of
the entire Gram form does not imply sector positivity.

## 3 The eighth cut and its precise remainder

Set \(\kappa=103/200\) and
\(\sigma_\kappa(m)=5\kappa/6-2m/3\). Assign the new sector
\(\Gamma_8\) outside all seven earlier sectors by
\[
                  \boxed{\Phi(\boldsymbol x;m)\le\sigma_\kappa(m).}
 \tag{8}
\]
On the operational region \(2/5<m<207/500\), one has
\(m<\kappa<2m\) and \(\beta_6(\kappa;m)=\sigma_\kappa(m)\).
Taking \(L\) to contain all factors shows that (8) includes both
\(\mathrm N\xi\le U^\kappa\) and the analogous physical cap
on \(\prod_e\xi_e^{6-e}\). The seventh cut is thus included in
the eighth predicate, although its already assigned terms stay in
\(\Gamma_7\).

Equation (7) has exactly the exponent of note 6's seventh-sector bound.
The reserve below \(T\) is
\[
 \Delta_8=1-5\kappa/6-g-(4/3-2d)m-3s+2\mu
               \ge\frac{4031}{1500000}.
 \tag{9}
\]
The continuous lower envelope is the same one audited there, using
\(g\le d(1+r)/2\), \(\mu\ge0\),
\(d\le21/50\), \(7/10\le r<73/100\),
\(m<207/500\), and \(s<101/500000\).
At the exact legal point of note 5 the reserve is
\(7362652673/507450000000\).

Let \(P=Q_{u,v}Q_{v,h}\) and \(F=Q_{u,h}\), with every \(Q\)
the norm of the primitive **row-ratio** conductor. The new exact
remainder retains the original weights, masks, smooth profiles,
primitive-conductor gate and three pairwise inequivalent characters,
and all of
\[
 \min(Q_{u,v},Q_{v,h},F)>U^{6/25},\quad
 \min(P,Q_{u,v}F,Q_{v,h}F)>U^{17/20},\quad P/F>U^{12/25},
\]
\[
 \min(Q_{u,v},Q_{v,h})>U^{39/100},\quad
 P>U^{103/100},\quad P^2/F>U^{15/8},
\]
\[
 \mathrm N\xi>U^{103/200},\qquad
                  \Phi(\boldsymbol x;m)>\sigma_\kappa(m).
 \tag{10}
\]
Equality belongs to the removed side. The physical inequality is
redundant given (6) and the strict \(\Phi\) inequality, but is kept
to display the inherited seven-cut complement. Since the new uniform
reserve exceeds the old minimum \(19/12500\),
\[
 \boxed{J_\ne=J_{{\rm rem},8}
        +O(U^{T-19/12500+\varepsilon}\mathcal H^b).}
 \tag{11}
\]
The required one-sided real bound on \(J_{{\rm rem},8}\) is open.

## 4 The previous survivor is controlled; another raw geometry remains

The note 6 pattern had exterior \(\xi=pq^2\) with
\((x_1,x_2)=(7/20,1/10)\). Average \(p\) with \(L=\{1\}\)
and count \(q\). Since \(m/2<x_1<m\), (6) gives
\[
 \Phi\le\frac1{10}+\frac7{60}-\frac m6
          =\frac{13}{60}-\frac m6,
 \qquad \sigma_\kappa-\left(\frac{13}{60}-\frac m6\right)
          =\frac{17}{80}-\frac m2>0.
\]
Its sharper uniform reserve is \(12281/1500000\); the exact point
reserve is \(6124435399/253725000000=0.0241380841423\ldots\).
This upper bound also applies to its actual selected rows and weights
if present, without requiring a bin-population or weight lower bound.

A new raw support pattern uses six distinct good prime ideals with
norm powers
\[
 (a_1,a_2,b,c,p,q)=
       (21/50,2/25,1/2,1/2,13/50,4/25),
\]
and rows
\[
        u=a_1a_2b,\qquad h=a_1a_2c,\qquad v=a_1pq^2.
 \tag{12}
\]
All three physical norm exponents and all three primitive row-ratio
conductor exponents equal one. The middle primitive conductor exponent
is \(21/25=0.84>2m-1/1000\) throughout the coarse operational
region; the endpoints are squarefree with conductor exponent one.
The exterior radical exponent is \(21/50\), whereas its physical
exponent is \(29/50>103/200\). It survives the six original
conductor cuts and the seventh physical cut.

Only the valuation-one and valuation-two roots are nonunits. The six
distinct group/orientation costs in (6), throughout
\(2/5<m<207/500\), are

| Varying roots | Original orientation | Conjugate orientation |
| --- | --- | --- |
| \(p\) | \(37/150-m/6\) | \(73/50-m\) |
| \(q\) | \(11/30-m/6\) | \(119/150-2m/3\) |
| \(p,q\) | \(29/60-2m/3\) | \(97/50-m\) |

The first entry is smaller than each other entry on the whole interval;
adding unit roots to a group does not change its cost. Consequently
\[
 \Phi=\frac4{25}+\frac{13}{150}-\frac m6
      =\frac{37}{150}-\frac m6,
 \qquad \Phi-\sigma_\kappa=\frac m2-\frac{73}{400}>\frac7{400}.
 \tag{13}
\]
Thus it also survives the eighth cut. At the exact point, the available
middle-cost budget is
\[
 C=T-\{2(1-\mu)+g+dm\}=0.1731810723677\ldots,
\]
while (13) costs \(0.1790429882254\ldots\), missing it by
\[
                 \frac{1487314601}{253725000000}
                   =0.00586191585772\ldots.
 \tag{14}
\]
This is a deficit in this estimate, not a physical energy lower bound
or proof that no stronger operator estimate can work. Prime norms can
be taken in fixed annuli of the indicated powers; strict exponent gaps
absorb their constants. A compatible selected profile/bin and actual
nonzero weights are not asserted.

Even the formal improvement from a cubic root-row sieve for the
\(q^2\) factor would give cost \(13/50\) after counting \(p\),
since \(x_2<m/2\); it does not improve (13). A native lower-order
operator would additionally require its own fixed presentation and
zero-extension comparison. Merely recognizing a cubic or quadratic
character is insufficient to replace the physical index scale by a
conductor scale. Those new transfers are not used in (8)--(11).

## 5 An exact small-inverse-ratio removal in the direct fourth moment

Keep a legal subset \(J\subset I\) of whole original physical
prime slots for the selected plain fourth input. Define
\[
 F_J=\sum_u\mathbf1_{\mathcal C_+}(u)
             |M_r(u)|^2|S_m(u)|^4|Q_J(u)|^2,
 \qquad D_J=2dm+\Gamma_J-g,
 \qquad \chi=(2s-\mu-D_J)_+.
\]
The sufficient route of note 6 asks for
\(F_J\ll U^{1+dr-\chi+\varepsilon}\mathcal H^b\), followed by
the pointwise bound for the complementary original slots. The actual
slot choice enters \(\Gamma_J\); the optimistic continuous capacity
is only a comparison.

Put \(D=U^r\), and retain the original inverse coefficients in
\[
 M_r(u)=D^{-1/2}\sum_d a_d\psi_u(d),\qquad
 a_d=\mu(d)A(\mathrm Nd/D),
\]
with any existing fixed phases absorbed consistently into \(a_d\)
or \(\psi_u\). These coefficients are supported on the original
inverse annulus, with magnitude bounded by its permitted seminorms.
Assemble the positive selected weight first:
\[
 V_u=\mathbf1_{\mathcal C_+}(u)|S_m(u)|^4|Q_J(u)|^2,
 \qquad \sum_u V_u\ll U^{1+\varepsilon}\mathcal H^b.
\]
Expanding only the inverse then gives the exact identity
\[
 F_J=D^{-1}\sum_{d,d'}a_d\overline{a_{d'}}L_J(d,d'),
 \qquad L_J(d,d')=\sum_u V_u\psi_u(d)\overline{\psi_u(d')}.
 \tag{15}
\]
This kernel retains the full \(S_m^4Q_J^2\) weight and the sharp
selector. After the inherited primitive-ratio identity, it also
retains the canceled-phase coprimality mask. Its modulus is at most
\(\sum V_u\). There is no application of complete-row Poisson
to this selected weighted sum.

Let \(f_{\rm inv}(d,d')\) be the original ideal column-ratio
conductor. The
[character-amplification manuscript](../../../quasi-rh-character-amplification/manuscript.tex),
Lemma `lem:pair-count`, gives
\[
 \#\{\mathrm Nd,\mathrm Nd'\ll D:
                \mathrm Nf_{\rm inv}(d,d')\le V\}
                  \ll D V^{1/2+\varepsilon}.
\]
Applying this to the absolute pair majorant in (15), including the
factor \(D^{-1}\), proves
\[
 \left|F_{J,\le\nu}\right|
 \le D^{-1}\sum_{\mathrm Nf_{\rm inv}\le U^\nu}
          |a_d\overline{a_{d'}}L_J(d,d')|
             \ll U^{1+\nu/2+\varepsilon}\mathcal H^b.
 \tag{16}
\]
It includes the inverse diagonal and nontrivial off-diagonal pairs.
This removal uses bounded actual coefficients, not cancellation of
the Möbius signs or a formal convolution shortcut.

For any \(\nu\ge0\) satisfying
\[
             \gamma_J=dr-\chi-\nu/2>0,
 \tag{17}
\]
(16) is below the sufficient direct target by \(\gamma_J\).
The exact residual is
\[
 F_{J,>\nu}=D^{-1}\sum_{\mathrm Nf_{\rm inv}(d,d')>U^\nu}
                           a_d\overline{a_{d'}}L_J(d,d'),
 \quad F_J=F_{J,>\nu}
       +O(U^{1+dr-\chi-\gamma_J+\varepsilon}\mathcal H^b).
 \tag{18}
\]
Both sectors are real by pair reversal, but are not asserted nonnegative.
A one-sided upper bound at exponent \(1+dr-\chi\) for (18)
is a sufficient new arithmetic target. It is unproved.

At note 5's point and the optimistic continuous slot capacity,
\(\chi=177302/1321484375\). The simple cap \(\nu=1/2\)
has reserve
\[
 \boxed{\gamma_{\rm cap}
       =dr-\chi-\frac14
       =\frac{166737511}{42287500000}
       =0.00394295030446\ldots.}
 \tag{19}
\]
Using the universal slot envelope \(\Gamma_J=d z_J\), for an actual
legal whole-slot subset with length shortfall
\(e_{\rm slot}\ge0\) from that capacity,
\(\chi_J=\chi_{\rm cap}+d e_{\rm slot}\) at this point, so
the reserve becomes \(\gamma_{\rm cap}-d e_{\rm slot}\).
The half-power cap requires this to be positive; otherwise use the
fixed-\(J\) condition (17) with a smaller cap. No fractional slot
is inserted and no uniform half-power claim for arbitrary \(J\)
is made. A different profile-specific \(\Gamma_J\) must be inserted
directly into (17), rather than inferred from length shortfall alone.

## 6 What the next bounded task must resolve

The cubic route now asks for the actual endpoint form on (10).
The squarefree roots \(p,q\) in (12) illustrate why counting one
factor and applying a generic operator to the other can still miss the
budget. A useful next test is a joint estimate for the two-kernel sum
over \(pq^2\), retaining the norm coupling, both deletion masks and
the original \(w_{a p q^2}\). It must improve the cost in (13), or
use the endpoint/weight distribution before its pointwise \(W\)
enlargement. A conductor-ordered cubic \(L\)-value moment theorem
does not by itself give an arbitrary-coefficient estimate for this
two-kernel polynomial.

In parallel, (18) isolates the large **inverse-column** ratio target
with the actual positive plain-fourth/slot weight. This conductor is
different from all three row-ratio conductors in (10). Neither predicate
allows the other branch's selectors or phases to be discarded.
Keep the separating parameters fixed first; the source's derivative,
profile and polynomial height uniformity is still required afterward.

## 7 Finite verification and scope

The [checker](../../numerics/check_mixed_valuation_factors.py),
[direct component](../../numerics/mixed_valuation_direct_checks.py), and
[small record](../../numerics/mixed_valuation_factors_record_20261009.json)
check formal valuation factorization, the injective grouped auxiliary
variable, complementary-power identities with nontrivial deletion zeros,
fixed-coefficient expansions and weighted Cauchy before positive
enlargement. Rational arithmetic checks the operator breakpoints,
new-cut inclusions and complements, the previous and new raw geometries,
sector reserves and the direct inverse-ratio budget. The direct component
checks the actual signed finite Möbius expansion and canceled-phase masks.

Two fresh replays match byte for byte: **133,487 exact assertions**. There are 216 formal exterior rows and 62 grouping choices; the direct component contributes 39,831 assertions. The record SHA-256 is
`d2b1de18298ab3777e77534e343d827cf8b739c2ba4beddd7ed9a40947b3c935`.

These finite checks do not certify native reciprocity, the fixed native
presentation transfer, ideal counting or the imported asymptotic sieve,
the selected plain fourth/inverse/family inputs, profile/bin population,
or either unbounded correlation. The
[scoped review](../../reviews/MIXED_VALUATION_FACTOR_REVIEW_20261009.md)
records the derivation audit. No new full mixed moment, scalar exponent,
zero-free boundary or RH implication is proved.
