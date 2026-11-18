# Positive-time source audit for B07 r2

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Bounded source-audit helper; settings inherited,
actual serving model and effort unavailable. This is selected-passage
inspection and an input/scope audit, not a full-paper proof review.

**Status: checked source inputs and proof ingredients.** The existing
positive-time theorem does give a common exterior cutoff on every slab
bounded away from zero. The complete-interaction asymptotic and its precise
comparison consequence are proposed E21 derivations, not quoted literature
theorems or accepted results of this source receipt.

Read-first routing: [result index][results], [cluster18][cluster],
[controls12][controls], [avoid index][avoid], and particularly
[classification01][classification], [premises02][premises],
[scope07][scope] and [imports16][imports]. The finite quantitative consumer
under consideration is the certified duration in [CM Note17][note17].
It is neither a new RH-equivalent criterion nor a statistical law.

## 1. Canonical source and inspected passages

D. H. J. Polymath, *Effective approximation of heat flow evolution of the
Riemann ξ function, and a new upper bound for the de Bruijn–Newman constant*,
arXiv:1904.12438v2, 4 August 2019; DOI 10.1007/s40687-019-0193-1.
[Primary HTML][html] · [version-pinned PDF][pdf]. Existing bibliography and
reading-copy ownership remain in the [canonical catalog][catalog] and
[parent bibliography][bib]; this is a new use receipt, not a second catalog.

Newly checked online: Theorem 1.5(i)–(iv), printed pp.9–10, its absolute
constant convention; Proposition 9.1; and §9 proof of Theorem 1.5,
especially (102)–(105), printed pp.60–61. The proof counts a single zero
with multiplicity in each clock disk. Normalization is
H0(z)=ξ((1+iz)/2)/8, physical H_t=−H_zz.

Source data: for 0<t≤1/2, with absolute constants C,c,A, high zeros are
real, simple and associated one-to-one to clock positions y_n satisfying
G(y_n,t)=n, with displacement at most A y_n^(−ct), once the stated
exponential height/index onsets are met. Here

    G(x,t)=x/(4π) log(x/(4π))−x/(4π)+11/8+(t/16)log(x/(4π)).

Theorem 1.5(iv) separately gives unit-window upper counts O(log(2+X))
and cumulative discrepancy O(log(2+X)), without that exponential onset.
Its convention explicitly says: “A is independent of t and C”.
Proposition 9.1 and (102)–(104) provide the local two-carrier/Rouché
route; (105) and the following safe-line/Jensen argument provide the
count route. No numerical value of C,c,A is extracted here.

The [parent count receipt][count] already checked the latter interface;
the [positive-threshold discussion][threshold] already uses uniform
exterior localization to confine a hypothetical positive threshold to a
finite event. This work does not claim either argument as new.

Existing external reading copy rehashed, without downloading or changing:

    /Users/Shared/szp-archive/height-dependent-heat-contours/references/1904.12438v2.pdf
    bytes: 2158176
    SHA-256: 60d0d2d381227d32f98535a5c43dedb86e333a9006d6819f0bdebdd734085603

Hash agreement identifies bytes, not mathematical validity. No third-party
PDF or large data is added to the repository.

## 2. Uniformity that follows, and the endpoint that does not

The following is an elementary quantifier inference from the checked
source, not an additional source statement. Fix 0<t0≤t*≤1/2. For t in
[t0,t*], exp(C/t)≤exp(C/t0), while X^(−ct)≤X^(−ct0).
Enlarge the absolute onset constant to pay both the height and index
conditions, plus any fixed window buffer. This gives one finite X0(t0)
for the entire slab, of the form exp(C'/t0). It also gives one common
displacement error A'X^(−ct0) on every fixed-width window at height X≥X0.
The index/height conversion uses G(x,t) of order x log x; it is not an
unproved identification of the numerical index with its height.

Thus a fixed positive slab has a directly paid eventual-real/simple
exterior. No global all-real assumption is needed for that exterior
theorem. A first-loss application must still cover the remaining compact
region and its boundaries, starting from an independently known simple
all-real slice. A practical finite certificate needs numerical constants
and an actual cutoff; asymptotic existence alone does not supply those.

For [0,t*], this argument loses both the finite common onset and decay
in the displacement error. Even if upper counts have been extended to
t=0 by the already accepted parent argument, those counts do not repair
the missing lower spacing or simplicity. This is a limitation of the
checked positive-time localization mechanism, not a theorem denying any
other time-zero exterior estimate. It is also stronger and more useful
than merely observing a separate finite exceptional set for each t>0.

## 3. Ingredients for the bounded complete-interaction derivation

These are proof obligations passed to E21. They must be proved in its
research note and separately assessed before being used as new results.
Choose an all-real simple slice t in [t0,t*], a high adjacent pair a<b,
and X=a. Put L=log(X/(4π)) and

    d = 1/G_x(X,t) = 1/[L/(4π)+t/(16X)],
    g = b−a,
    M = sum over exterior occurrences 1/[(rho−a)(rho−b)].

The source clock plus the mean-value theorem should yield g/d→1 and
the same statement for the adjacent exterior gaps. On a fixed-width
window around X, relative clock-density variation is O(1/(X L)); its
accumulated position error divided by d is safely O(1/X). Root
displacement divided by d is O(L X^(−ct0)). The one-to-one localization
and its separation must be paid before using these estimates for
consecutive labels. Merely subtracting the coarse count asymptotic is
insufficient.

To pass from finite local gaps to complete M, keep a local clock head
and bound the full exterior. In unit shells at distance at least one
from the pair, the inherited upper count gives an absolute tail bounded
by a constant times

    sum_{m≥1} log(2+X+m)/m² = O(log X).

Negative zeros, the bounded low-height part and multiplicities are included.
Multiplication by d² makes this O(1/L). A fixed-width local clock head
has order L entries; its omitted infinite-lattice tail has the same
normalized O(1/L) size. Pair endpoints require a smaller inner cutoff
handled by the individually separated adjacent labels, not by this shell
bound. An alternative proof first fixes a finite normalized head, then
controls the remaining near shells and the far population uniformly.

The lattice benchmark is the exact telescoping identity

    sum_{k in Z, k≠0,1} 1/[k(k−1)] = 2.

This suggests the quantitative target

    d²M = 2 + O(1/L + L X^(−ct0)),
    g/d = 1 + O(L X^(−ct0) + 1/X).

The constants and the localization/head/tail decomposition belong in
E21's proof. The source theorem itself does not state this M estimate.
The all-real condition supplies positivity for the Note17 consumer;
the asymptotic estimate must not silently assume that all smaller times
are already all real.

If those limits are proved, Note17's exact duration formula would give
three-gap duration asymptotic g²/6 and the best duration available from
its exact initial-M Riccati comparison asymptotic g²/4. Both are of
order L^(−2), so neither pays a fixed positive physical descent at every
height. This would be a scoped quantitative finding about that initial-data
comparison, not an obstruction to the actual dynamics or to a sharper
environment-conditioned evolution estimate. Direct source localization
already protects the high exterior on a fixed positive slab.

## 4. Control-premise screen

This source audit applies the analytical control screen in [controls12][controls]
and [CM Note17 §4][note17]; no certificate is recomputed. The generic
initial-M comparison can hold for noncanonical real-rooted heat fields.
The source theorem here imports the unchanged complete canonical field,
not positivity, shape or a generic count bound alone.

| Control family | Premise not supplied for this canonical source import |
| --- | --- |
| Euler-factor controls, every prime in their stated families | Original zeta coefficients and unchanged complete theta source are modified. No claim is made that every derived clock bound fails for them. |
| Weighted-square and finite-tail controls | Full reflected canonical expansion fails; these finite-source families also have no all-real heat time. |
| Reflected super-Gaussian and smooth/positive-primitive controls | Full canonical arithmetic fails; their shared reflection, shape and asymptotic data do not import this complete population theorem. |
| q and q_(T,a) positive-kernel controls | Exact canonical theta source is absent. |
| Finite-prime, finite-profile and canonical-score controls | Their specified finite matches do not supply the unchanged complete source; finite-atom profiles also fail its eventual population/simplicity properties. |
| RH-conditional endpoint controls | Ordinary Dirichlet arithmetic is altered; their endpoint doubles are not a canonical-theta conclusion. |
| Changed readout kernels, fractional measures and static surgery | Respectively fail the physical cosine equation, integer zero realization, or common canonical heat evolution. |

None of these failed import premises is itself an acquired favorable
statistical tail. The precise quantitative distinction remains for the
new proof and its consumer. There is no random-matrix assignment,
independence assumption, or new bound on Lambda in this receipt.

[html]: https://arxiv.org/html/1904.12438v2
[pdf]: https://arxiv.org/pdf/1904.12438v2
[catalog]: ../../../../../investigations-5/02_heat_flow_rh_applications/references/sources.json
[bib]: ../../../references/induction.bib
[count]: ../../references/05_VCD_GT_UNIFORM_COUNT_SOURCE_USE_20261117.md
[threshold]: ../../../../../investigations-5/02_heat_flow_rh_applications/notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md
[note17]: ../notes/17_VCD_GT_CM_B07_REGIONAL_GAP_STATISTICS_AND_BACKWARD_COMPARISON_20261118.md
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[classification]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[imports]: ../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
