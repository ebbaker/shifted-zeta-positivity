# Weighted middle kernel estimates and the direct energy budget

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel derivations and audits are same-model internal validation, not
independent specialist review or formal proof verification.

**Result.** The existing physical sextic sieve controls an additional
arithmetic sector of the actual distinct-character open chain: the part of
the middle row supported on primes absent from both endpoints has
physical norm at most \(U^{103/200}\). The uniform reserve below the
cubic-probe target is \(4031/1500000\). This makes the four-prime
counting example in [note 5](5_MIXED_NEIGHBOR_CONTINUATION_20261008.md)
affordable through an averaged kernel estimate, even after paying the
actual maximum inverse/prime weight. The complete mixed energy remains
open. The direct-energy analysis identifies a smaller remaining
correlation target and shows exactly why interpolation of the available
marginal bounds does not supply it.

The active investigation is now mixed character families. Further
short-family cofactor reductions are deferred. All existing files and
working-tree results are retained; the session base is
`6c343e83622e194268399033b2eee68cc7e5fbcd`. No new manuscript, draft
snapshot, commit or tag is part of this continuation.

## 1 The actual quantities and imported operator

Retain the actual sixth-power-free physical rows, fixed good and bad
prime conventions, original plain annulus, common separating parameters,
unit/ray presentation, inverse cutoff, physical prime slots and masks
of [notes 1](1_MIXED_CONDUCTOR_REFINEMENT_20261008.md) through
[5](5_MIXED_NEIGHBOR_CONTINUATION_20261008.md). Write
\[
 w_u=\mathbf1_{u\in\mathcal C_+}|M_r(u)Q_I(u)|^2,
 \quad A=\sum_u w_u,\quad W=\max_u w_u,\quad N=U^m,
\]
\[
 E=\sum_u w_u|S_m(u)|^2,\quad
 K(u,v)=N^{-1}\sum_k|B(\mathrm Nk/N)|^2
             \psi_u(k)\overline{\psi_v(k)}.
\]
The target is \(E\ll U^{e+\varepsilon}\mathcal H^b\), with
\(e=1+dm-s\), \(\mathcal H=1+T_1\). The sufficient actual-probe
target has exponent \(T=3e-2m\). Existing inputs give
\[
 A\ll U^{1-\mu+\varepsilon}\mathcal H^b,\qquad
 W\ll U^{g+\varepsilon}\mathcal H^b,
 \qquad g=d(r+z),\quad \mu\ge0,
\]
and the actual buffered endpoint bound \(|S_m(u)|^2\ll
N^dU^\varepsilon\mathcal H^b\).

An additional input for this mixed lane is the physical operator already
proved conditionally in the [short-family manuscript](../../short_families/short_family_reductions.tex),
Corollary `cor:physical-operator`. For a fixed arbitrary coefficient
vector on sixth-power-free good ideal columns of norm at most \(X\),
\[
 \sum_{0<\mathrm Nt\le H}
       \left|\sum_n b_n\chi_n(t)\right|^2
 \ll_\varepsilon(HX)^\varepsilon
        \mathscr B(H,X)\sum_n|b_n|^2,
\]
\[
 \mathscr B(H,X)=H+XH^{1/6}
                 +H^{5/6}X^{1/3}+H^{1/3}X^{5/6}.
 \tag{1}
\]
A fixed positive Schwartz weight covering the ball gives this sharp-ball
version. Conjugation of the character is permitted by conjugating the
whole coefficient vector. The operator averages physical element rows;
finite unit and fixed bad-prime classes and their zero conventions are
part of the presentation transfer.

Its imported theorem is Alexandre de Faveri,
[*Optimal large sieve for fixed order characters*, Theorem 1.1](https://arxiv.org/html/2610.04045v1#Thmtheorem1.1),
arXiv:2610.04045v1, 2 October 2026. The theorem indexes power-free ideals
by their **physical norm**, not just their radical or conductor norm.
The source theorem and the repository's native presentation transfer
remain explicit assumptions here; the theorem's proof is not revalidated.

## 2 The best existing direct energy envelope

This comparison uses the inputs of the
[selector-energy note](../../../quasi-rh-character-amplification/notes/SELECTOR_ENERGY_LOCALIZATION_20261008.md),
including the fourth moment for an admissible subset \(J\subset I\)
of whole physical prime slots. Let
\[
 R=R^*+\ell,\quad g=dr+\Gamma_I,\quad
 \mu_0=1-R-g,\quad D_J=2dm+\Gamma_J-g.
\]
The constraints are the marked inverse mass \(\sum w_u\ll U\),
the selected row count \(\#\mathcal C_+\ll U^R\), the pointwise
inverse/plain/slot envelopes, and
\[
 \sum_{u\in\mathcal C_+}|S_m(u)|^4|Q_J(u)|^2\ll U.
 \tag{2}
\]
All displays suppress the allowed \(U^\varepsilon\mathcal H^b\)
factor. These are norms of the original polynomials with their masks.

Assign powers \(\alpha\) and \(\beta\) to the two moment
inputs. Feasibility requires \(0\le\beta\le1/2\) and
\(0\le\alpha\le1-\beta\). Bounding the remaining nonnegative
polynomial powers pointwise and applying Hölder with the row count
gives energy exponent
\[
 R+g+dm+\alpha\mu_0+\beta(\mu_0-D_J).
\]
This is affine on a polygon with vertices
\((0,0),(1,0),(0,1/2),(1/2,1/2)\). Its best saving below
\(1+dm\) is exactly
\[
 \sigma_H=\max\{0,\mu_0,D_J/2,(D_J+\mu_0)/2\}
          =\max\{\mu,(D_J+\mu)/2\},
 \quad \mu=\max(0,\mu_0).
 \tag{3}
\]
Combining several legal fourth-moment subsets does not improve this
envelope: for a fixed total fourth-moment power, choose the subset with
largest permitted \(\Gamma_J\). Equation (3) concerns these marginal
inputs and their pointwise/Hölder combinations; it is not a barrier to
using character phases or additional arithmetic moments.

At the parameter point of note 5, the optimistic continuous slot capacity
is \(c_m=2(1-2m)/9=4251661/101490000\). Taking
\(\Gamma_J=dc_m\) gives
\[
 D_J=8859/50000000,\quad
 \sigma_H=165074/1321484375=0.000124915589713\ldots,
\]
\[
 \boxed{s-\sigma_H=88651/1321484375
        =0.0000670844102867\ldots.}
 \tag{4}
\]
This improves the comparison with the simpler mass bound, whose deficit
was \(s-\mu=0.000119348820573\ldots\). The capacity in (4) is a
favorable relaxation. Actual whole-slot selection with shortfall
\(e_{\rm slot}\) reduces the combined branch by
\(d e_{\rm slot}/2\); the overall saving remains
\(\max\{\mu,(D_{\rm cap}-d e_{\rm slot}+\mu)/2\}\),
where \(D_{\rm cap}\) is the optimistic value in (4). The physical mesh and capacity conditions must
still be checked; no exact fractional slot is inserted into the input.

The marginal inequalities alone do not close (4). An abstract amplitude
model takes \(\lfloor U^R\rfloor\) rows with
\[
 |M_r|^2=U^{dr},\quad |Q_i|^2=U^{dw_i},\quad
 |S_m|^2=U^y,\quad y=(1-R-dc_m)/2.
\]
Here the marked inverse mass has exponent \(1-\mu\), and every
legal fourth-moment subset satisfies \(R+2y+dz_J\le1\). The
pointwise envelopes hold, while its energy has precisely the exponent
\(1+dm-\sigma_H>e\). This checks the logical insufficiency of
the listed scalar inequalities. It is not a physical character example
or a selected zero/profile bin, and it asserts no large actual energy.

## 3 A kernel average over a shorter physical middle factor

Fix physical factors \(u,a\), and let \(t\) vary. After finite
unit/bad-prime splitting the native multiplicative presentation gives
exactly
\[
 K(u,at)=N^{-1}\sum_k b_{u,a}(k)
                         \overline{\chi_k(t)}^{\,s_\chi},
\]
\[
 b_{u,a}(k)=|B(\mathrm Nk/N)|^2|\nu(k)|^2
       \chi_k(u)^{s_\chi}\overline{\chi_k(a)}^{s_\chi}.
 \tag{5}
\]
All fixed zeros of \(u,a,\nu\) remain in these coefficients.
Their magnitude is bounded by the permitted profile/height seminorms;
the growing factors \(u,a\) supply only bounded phases and zeros.
Thus (1) has no growing-twist constant in this application.

The plain columns are not assumed power-free. Uniquely write
\(k=\lambda^6k_0\), with \(k_0\) sixth-power-free. Retain the
exact identity
\[
 \chi_{\lambda^6k_0}(t)
   =\chi_{k_0}(t)\mathbf1_{(t,\lambda)=1}.
 \tag{6}
\]
For each fixed \(\lambda\), the latter is a row mask independent of
\(k_0\). The coefficient vector
\(N^{-1}b_{u,a}(\lambda^6k_0)\) has squared norm at most
\[
 C\mathcal H^b N^{-1}(\mathrm N\lambda)^{-6}
\]
by ideal counting; its support is bounded by
\(X_\lambda=C_BN/(\mathrm N\lambda)^6\). Terms with
\(X_\lambda<1\) are empty. Form the nonnegative square over
\(0<\mathrm Nt\le H\), then remove the mask in (6) from that
square and apply (1). Minkowski and monotonicity in the column scale give
\[
 \begin{split}
 \left(\sum_{0<\mathrm Nt\le H}|K(u,at)|^2\right)^{1/2}
 &\ll U^\varepsilon\mathcal H^b
       \sqrt{\mathscr B(H,N)/N}
       \sum_\lambda(\mathrm N\lambda)^{-3}\\
 &\ll U^\varepsilon\mathcal H^b
       \sqrt{\mathscr B(H,N)/N}.
 \end{split}
\]
The ideal series converges. Fixed profile support constants in
\(\mathscr B(H,C_BN)\) are absorbed. Consequently
\[
 \boxed{\sum_{0<\mathrm Nt\le H}|K(u,at)|^2
       \ll U^\varepsilon\mathcal H^b\mathscr B(H,N)/N.}
 \tag{7}
\]
No signed selector has been enlarged. Varying-prime deletion zeros were
retained through (6), and removed only from a positive square with a
fixed column coefficient vector. The physical factor \(t\) need not
be squarefree. Equation (7) uses the physical-row operator, which already
pays possible sixth-power row multiplicity.

## 4 The additional controlled middle sector

For fixed endpoints \(u,h\), let
\(\mathfrak e=\operatorname{rad}_{\rm good}(uh)\). Define the
good exterior part of the actual middle ideal by
\[
 \xi_{u,h}(v)=\prod_{\mathfrak p\nmid\mathfrak e,
                              \mathfrak p\ \mathrm{good}}
                     \mathfrak p^{v_\mathfrak p(v)}.
 \tag{8}
\]
This is its **physical ideal**, including valuations \(1,\ldots,5\),
not its radical or a primitive conductor. Split
\(v=\epsilon v_{\rm bad}a\xi\), where \(a\) is supported on
\(\mathfrak e\). There are at most
\(6^{\omega(\mathfrak e)}\ll U^\varepsilon\) choices for \(a\),
and finitely many bad-prime/unit presentation choices. No actual selected
row is replaced by a different one in this decomposition.

Set \(\kappa=103/200\). Assign the new sector \(\Gamma_7\)
outside all six previously removed sectors by
\[
             \mathrm N\xi_{u,h}(v)\le U^\kappa.
 \tag{9}
\]
For each fixed \(a\) and finite class, retain the actual middle subset,
then use \(w_v\le W\) and Cauchy:
\[
 \left|\sum_\xi w_{a\xi}K(u,a\xi)K(a\xi,h)\right|
 \le W\left(\sum_\xi|K(u,a\xi)|^2\right)^{1/2}
       \left(\sum_\xi|K(h,a\xi)|^2\right)^{1/2}.
\]
Only these nonnegative square sums are enlarged to the physical ball
of radius \(H=U^\kappa\). Apply (7), sum the
\(U^\varepsilon\) endpoint-supported choices, use the actual
endpoint bound, and sum \(w_uw_h\). This proves
\[
 \boxed{|J_{\Gamma_7}|\ll U^\varepsilon\mathcal H^b
                      A^2W N^{d-1}\mathscr B(U^\kappa,N).}
 \tag{10}
\]
There is no extra count of endpoint pairs beyond \(A^2\). The
definition of \(\mathfrak e\) is invariant under swapping endpoints;
the whole assigned sector is therefore real by chain reversal, without
being claimed positive.

The operational region lies inside
\(r<73/100\), \(2/5<m<207/500\),
\(d\in[9/25,21/50]\), \(0<s<101/500000\). In particular
\(m<\kappa<2m\), so the largest term in (1) is
\(H^{5/6}N^{1/3}\). The new exponent is
\[
 2(1-\mu)+g+dm+5\kappa/6-2m/3.
\]
Its reserve below \(T\) is
\[
 \Delta_7=1-5\kappa/6-g-(4/3-2d)m-3s+2\mu.
 \tag{11}
\]
Since \(z\le(1-r)/2\), use \(g\le d(1+r)/2\) and
\(\mu\ge0\). The resulting lower expression decreases with
\(r,m,s\), and also with \(d\), because
\(2m-(1+r)/2<0\) on \(r\ge7/10,m<207/500\).
Corner substitution gives the uniform reserve
\[
 \boxed{\Delta_7\ge4031/1500000
          =0.002687333333333\ldots.}
 \tag{12}
\]
At note 5's exact point the reserve is
\(7362652673/507450000000=0.014509119465957\ldots\).
These margins absorb sufficiently small analytic losses and the fixed
divisor/presentation costs in the usual prescribed order.

## 5 The old counting example is now affordable

For \(u=ab,h=ac,v=ad\) with four distinct good primes of norm
comparable to \(U^{1/2}\), (8) gives \(\xi=d\). Thus the
example lies in (9) for all sufficiently large \(U\), including its
original selected subset if that subset is populated. No lower bound on
its selected weights or bin membership is required for the upper bound.

At its sharper radius \(H\asymp U^{1/2}\), (7) costs
\(U^{5/12-2m/3}\), rather than the entrywise count cost
\(U^{1/2-m/4}\) in the middle sum. At note 5's point the resulting
sector reserve is
\[
 \boxed{13705777673/507450000000
          =0.027009119465957\ldots.}
 \tag{13}
\]
The earlier \(0.2253834\) deficit was a valid diagnosis of the
count-plus-entrywise method; the averaged operator supplies a different
bound for this family.

More generally, when the exterior ideal in (8) is squarefree, the local
conductor identity in note 5 implies
\(\mathrm N\xi\ll\sqrt{P/F}\), with
\(P=Q_{u,v}Q_{v,h}\), \(F=Q_{u,h}\). Therefore every
all-three-conductors-comparable-to-\(U\) chain with squarefree exterior
part is eventually included in (9). An exterior ideal with higher
valuations may have much larger physical norm than this radical bound;
the source sieve does not justify replacing its physical row scale by
its conductor scale.

## 6 The exact complement and the direct correlation target

Let \(J_{{\rm rem},7}\) retain all original weights, masks, profiles
and endpoint sums, three pairwise-inequivalent primitive characters, all
six inequalities of note 5,
\[
 \min(Q_{u,v},Q_{v,h},F)>U^{6/25},\quad
 \min(P,Q_{u,v}F,Q_{v,h}F)>U^{17/20},\quad P/F>U^{12/25},
\]
\[
 \min(Q_{u,v},Q_{v,h})>U^{39/100},\quad
 P>U^{103/100},\quad P^2/F>U^{15/8},
\]
and the additional physical condition
\[
              \mathrm N\xi_{u,h}(v)>U^{103/200}.
 \tag{14}
\]
Equality belongs to the removed side. Since (12) exceeds the old smallest
reserve \(19/12500\), the exact estimate is still
\[
 J_{\ne}=J_{{\rm rem},7}
       +O(U^{T-19/12500+\varepsilon}\mathcal H^b).
 \tag{15}
\]
The sufficient one-sided real bound for this remainder is unproved.
Equation (15) does not imply that its energy or selected weight is small.

The physical complement is not empty merely because all three conductor
norms have order \(U\). For six distinct good prime ideals
\(a_1,a_2,b,c,p,q\), give their norm powers respectively
\(9/20,1/20,1/2,1/2,7/20,1/10\), and put
\[
 u=a_1a_2b,\qquad h=a_1a_2c,\qquad v=a_1p q^2.
\]
All physical norms have power one. The three ratio conductor norms have
power one; the middle primitive conductor has power \(9/10\), so
the primitive-conductor gate is passed throughout the operational region.
Yet \(\mathrm N\xi=(\mathrm Np)(\mathrm Nq)^2\) has power
\(11/20>103/200\). This valuation pattern survives all seven cuts in the raw physical
norm and conductor bookkeeping. Population of a compatible selected
bin and its weights are not asserted. The
example does not preclude treating its two exterior factors separately.

Keep a direct target in parallel. Put \(X_u=|S_m(u)|^2\), and
for \(\tau=s-\mu+\delta\), \(\delta>0\), define
\(\mathcal H_\tau=\{u:X_u>U^{dm-\tau}\}\). In the region
\(\mu<s\), the complementary rows have energy at most
\(U^{e-\delta+\varepsilon}\mathcal H^b\). It remains to bound
\(\sum_{u\in\mathcal H_\tau}w_uX_u\) at exponent \(e\).
A sufficient stronger condition is
\[
             \sum_{u\in\mathcal H_\tau}w_u
                \ll U^{1-s+\varepsilon}\mathcal H^b.
 \tag{16}
\]
The scalar model above can keep all its mass on this high-response set;
the current marginal inputs do not imply (16).

A parallel direct sufficient moment is
\[
 P_I=\sum_u w_u|S_m(u)|^4,\qquad E^2\le A P_I.
\]
The direct energy target follows from
\[
 P_I\ll U^{1+2dm-2s+\mu+\varepsilon}\mathcal H^b.
 \tag{17}
\]
The existing fourth moment (2) gives only
\(P_I\ll U^{1+g-\Gamma_J+\varepsilon}\mathcal H^b\).
The required extra inverse/plain correlation saving is
\(\chi=(2s-\mu-D_J)_+\). At the optimistic capacity of the
displayed point,
\[
 \chi=177302/1321484375=0.000134168820573\ldots.
 \tag{18}
\]
One sufficient route is to test an improved bound for
\(\sum |M_r|^2|S_m|^4|Q_J|^2\) at exponent
\(1+dr-\chi\), then bound the complementary original slots
pointwise. Actual slot losses increase the required saving. Equations
(16)--(18) identify new arithmetic tasks; none is asserted proved.

## 7 Next bounded task and validation scope

The next cubic task is the actual weighted endpoint form on (14).
Separate the exterior middle ideal into primes with valuations
\(1,2,3,4,5\), retain their zero conventions, and test whether a
multivariable operator estimate can use those shorter individual factors
without paying their full product norm. For the all-conductors-of-order-
\(U\) range, the squarefree exterior part is already controlled;
the remaining possibilities require repeated outside valuations and a
physical exterior norm exceeding \(U^{0.515}\). The full remainder
also includes other conductor ranges. No part can be dropped solely from
that all-comparable description.

In parallel, test (17) or the high-response inverse mass (16) with actual
Möbius and physical-prime coefficients. A new inverse-weighted plain
fourth estimate would address the smaller direct budget in (4), with
its actual whole-slot losses. Keep fixed separating parameters first,
then establish the derivative/profile and height uniformity needed by
the source's positive Sobolev step.

The [checker](../../numerics/check_mixed_middle_sieve.py) and
[small record](../../numerics/mixed_middle_sieve_record_20261009.json)
test formal sixth-power column decomposition with nontrivial zero masks,
positive mask removal, fixed-coefficient kernel expansion, Hilbert
Cauchy, exterior middle factorization, exact cut complements and
reversal, the old sharp-family inclusion, and rational sector/direct
budgets. They do not validate native reciprocity, the physical
presentation transfer, the imported sieve theorem, source analytic
growth/plain/inverse inputs, or any unbounded mixed correlation.
Two fresh replays matched the record byte for byte: **141,413 exact
assertions**. The record SHA-256 is
`81db128551bc77b5848a714162db5fa1091535bdce54aac4805ef786ccf6d44c`.
The [scoped review](../../reviews/MIXED_MIDDLE_SIEVE_REVIEW_20261009.md)
records the derivation audit. No new full moment, scalar exponent,
zero-free boundary or RH implication has been proved.
