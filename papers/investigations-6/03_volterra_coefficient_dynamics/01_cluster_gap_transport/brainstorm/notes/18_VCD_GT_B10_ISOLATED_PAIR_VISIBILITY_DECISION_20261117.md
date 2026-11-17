# B10: count negative isolated-pair interactions through transverse zeros

17 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Conceptual collaborator explicitly dispatched
**gpt-6-astra / ultra**; actual lead model and effort unavailable. Dispatch
is not an independent backend attestation. This is a conceptual decision
and fixed analytical contract, pending proof and internal assessment.

**Select negative-kernel incidence as the primary signed estimate.** A
negative near interaction at a tightly localized, independently isolated
pair requires an exterior zero with a transverse mark comparable to the
collar radius. The established canonical exponential transverse density
then bounds the number of such pairs. Retain spatial visibility as the
second, broader option: it bounds the number of pairs with large
transverse loss, even when their signed interaction is positive.

| Follow-through | Type / recommendation | Fixed deliverable |
| --- | --- | --- |
| VCD-GT-E19 | E / Sol6.1 ultra | Shared pair-packing proof; exponential count of negative interactions; polynomial count of large transverse losses; matched comparisons |
| VCD-GT-E18 | E / Sol6.1 ultra | Pinned internal assessment of E16/E17/E19 and the later synthesis, owned by the lead |

The [sole register][progress] owns live status. The source-moment
[proof return][e17proof] is available under [E17 r1][e17], following
[Decision17][b09]; this note does not promote it to accepted status. Read the
[result index][results], [controls12][controls], and [avoid index][avoid],
particularly [classification01][a01], [premises02][a02], [scope07][a07],
[joint estimates12][a12] and [sibling reuse15][a15]. The proposed outputs
are quantitative counts with explicit hypotheses, not an RH-equivalent
criterion or an every-pair exclusion. Only the two options below are
selected; no additional source mechanism or numerical campaign is opened.

## 1. Fixed domain and source inputs

Use the unchanged complete theta field with

\[
 \partial_tH=-H_{zz},\quad 0\le t\le1/2,\qquad
 T\ge16,\quad L=\log T,\quad\ell=L^{-1}.
\]

Fix (d\ge0), (h>0), and a nonempty parameter range

\[
 \max\{2,4\sqrt d\}\le a\le L,\qquad 3\le R\le T/4,
 \qquad r_0=a\ell.
 \tag{1}
\]

At each time count distinct unordered, multiplicity-counted, conjugation-
invariant pairs (P=\{z_1,z_2\}), with

\[
 c=(z_1+z_2)/2\in[T,2T],\quad
 D=(z_1-z_2)^2/4\in\mathbb R,\quad |D|\le d\ell^2,
 \quad |\rho-c|\ge r_0\quad\text{for every exterior occurrence }\rho.
 \tag{2}
\]

An isolated double is counted once with multiplicity two; different
choices of labels for its two copies do not create different pairs.
The count-two contour and exterior collar are independent premises.
The result does not acquire them, count all canonical pairs, or require
simple target/exterior zeros. Target roots obey
(|z_j-c|\le\sqrt d\ell\le r_0/4). Both signs of D and D=0 are allowed.

For each pair keep the original near interaction (S_R(P)), full
interaction M, and transverse loss

\[
 \Xi(P)=\ell^2\sum_{\rho\text{ exterior},\ |\Re\rho-c|\le R}
                \frac{(\Im\rho)^2}{|\rho-c|^4}.
 \tag{3}
\]

The canonical input is [TND-O Note21, (7)–(8)][density]. With one fixed
(0<b<1/2), it bounds the multiplicity-counted zeros throughout the
closed time slab. Three dyadic bands cover
(\mathcal B_T=[T/2,5T/2]), giving constants independent of t,T:

\[
 \begin{split}
 N_{\mathcal B_T}(v)&\le B_b^*TL e^{-bLv},\quad 0<v<1,\\
 \sum_{\Re\rho\in\mathcal B_T}(\Im\rho)^2&\le B_2T/L,\\
 \#\{\rho:\Re\rho\in\mathcal B_T\}&\le B_0TL.
 \end{split}                                                   \tag{4}
\]

For example (B_b^*=5B_b) follows from the source's dyadic density
constant when (T\ge16); the proof must verify the endpoint conventions.
The first two bounds are source-specific inputs. The last is the matched
count-only input. No conditioning law for selected pairs is assumed.

## 2. Shared geometry: distinct pairs cannot overlap

The fixed proof must first show that distinct qualifying pairs cannot
share one zero occurrence. If they did, their centers would be within
(2\sqrt d\ell), and the remaining occurrence of the second pair would
be exterior to the first at distance at most (3\sqrt d\ell<r_0),
contradicting (2). The same argument includes repeated locations and d=0.
Sharing both occurrences is the same pair and is not counted twice.

For two distinct pairs, take any target occurrence of the second. It is
exterior to the first, so their real centers satisfy

\[
 |c_1-c_2|\ge(a-\sqrt d)\ell\ge3r_0/4.
 \tag{5}
\]

Thus their intervals ([c-r_0/4,c+r_0/4]) are disjoint, and the ordinary
packing count is at most

\[
 N_{\rm pairs}\le1+4TL/(3a).
 \tag{6}
\]

This is a slice-wise statement about all qualifying groups. It introduces
no trajectories through collisions and no higher-multiplicity extension.

## 3. Primary option: exponential count of negative interactions

For an exterior zero (\rho=c+x+iy), put (r^2=x^2+y^2). The numerator
of its contribution q has the sign of (x^2-y^2-D); the denominator is
positive by the exterior collar. If (q<0), then

\[
 y^2>(r^2-D)/2\ge(a^2-d)\ell^2/2
      \ge(15/32)a^2\ell^2,
 \qquad |y|>v_0:=2a/(3L).
 \tag{7}
\]

Here (v_0\le2/3<1), so the complete density in (4) applies without an
endpoint limit. A negative (S_R(P)) has at least one negative summand:
the near population is finite by the strip and local count. No arbitrary
negative pair is selected or assigned a distribution.

Conversely, a fixed zero occurrence with height y can supply a negative
summand only to pair centers in

\[
 |\Re\rho-c|<\sqrt{y^2+d\ell^2}\le |y|+r_0/4.
\]

The separation (5) bounds the number of such centers by
(5/3+8|y|/(3r_0)). Count all incidences; overcounting a pair with several
negative summands is harmless. Only zeros in ([T-R,2T+R]\subseteq
\mathcal B_T) can occur. Layer cake and (4) therefore give the frozen
E19 target

\[
 \begin{split}
 N_-^{\rm near}(t)
 &:=\#\{P\text{ satisfying (2)}:S_R(P)<0\}\\
 &\le B_b^*TL\,e^{-2ba/3}
       \left(\frac{31}{9}+\frac8{3ab}\right)
 \le C_bTL e^{-2ba/3}.                                  \tag{8}
 \end{split}
\]

The explicit layer-cake step is

\[
 \sum_{|y|>v_0}|y|
 =v_0N(v_0)+\int_{v_0}^{1}N(v)\,dv
 \le B_b^*TL e^{-bLv_0}\left(v_0+\frac1{bL}\right).
\]

The denominator and sign statements include both D signs. Moreover
(|D|\le d/L^2\le1/16), the full zero strip has (|y|\le1), and
(|x|>R\ge3) forces (x^2-y^2-D>0). Thus the far term is nonnegative
and (M<0\Rightarrow S_R<0). The same right side of (8) bounds

\[
 N_-^{\rm full}(t)=\#\{P\text{ satisfying (2)}:M(P)<0\}.
 \tag{9}
\]

This implication uses only the sign of the distant grouped terms, not a
new far asymptotic. The previously accepted full-divisor summability
pays that grouping. A zero interaction is not counted by (8)–(9).

The matched count-only comparator is the packing bound (6). For
(a=L^\eta,\ 0<\eta<1), (8) bounds the negative-pair count normalized by
TL by (C_b\exp(-(2b/3)L^\eta)), while (6) is (O(L^{-\eta})).
This is an actual source-specific rate for **numbers of isolated pairs**,
without an assumed conditional distribution. It is not a fraction of
all isolated pairs: no lower bound for that population has been acquired.

Even at the largest allowed (a=L), the right side of (8) has size
(T^{1-2b/3}\log T\to\infty). The estimate does not force the number
below one, exclude one exceptional pair, or pay the incoming gap/cost.
The improved rate concerns growing collar size; fixed a leaves a
constant proportion of the TL normalization as an allowance.

## 4. Second option: visibility of any large transverse loss

This option applies to \(\Xi(P)\ge h\), even when (S_R(P)\ge0).
For (X\in I_c=[c-r_0/4,c+r_0/4]), each original term in (3) remains
within the enlarged horizontal cutoff (R'=R+r_0/4) and has

\[
 3r_0/4\le |\rho-X|\le(5/4)|\rho-c|.
\]

Thus the ordinary, unconditioned aggregate from E17 satisfies

\[
 \Xi_{a/2,R'}(t,X)\ge\kappa_{\rm vis}\Xi(P),\qquad
 \kappa_{\rm vis}=(4/5)^4.
 \tag{10}
\]

Any additional target terms in this aggregate are nonnegative. The radial
cutoff (a\ell/2) is strictly below the lower distance just displayed.
The intervals (I_c) are disjoint by (5). Their union lies in
(J=[T-r_0/4,2T+r_0/4]).

To pay J, repeat E17's exact Fubini argument, not an unproved extension
of its integration domain. Since (r_0\le1), (R\le T/4) and (T\ge16),
all contributing zero real parts remain in (\mathcal B_T). The same
elementary integral used in E17 and (4) give

\[
 \int_J\Xi_{a/2,R'}(t,X)\,dX
 \le4\pi B_2T/a^3,
 \qquad
 \int_J\Xi_{a/2,R'}(t,X)\,dX\le\pi B_0T/a
 \tag{11}
\]

for source and count-only inputs respectively. Integrating (10) over
the disjoint intervals of length (r_0/2) yields

\[
 \begin{split}
 N_h^{\Xi}(t)&\le
      \frac{8\pi B_2}{\kappa_{\rm vis}}\frac{TL}{a^4h},\\
 N_h^{\Xi}(t)&\le
      \frac{2\pi B_0}{\kappa_{\rm vis}}\frac{TL}{a^2h}
        \quad\text{using only the matched counts}.
 \end{split}                                                   \tag{12}
\]

Both can also be intersected with (6). These are deterministic counts,
not estimates for a conditional mean. The source gain relative to the
equally visible count comparison is two powers of a.

E17's signed bridge gives

\[
 \ell^2S_R\ge\ell^2\sum_{\rm near}(r^2-D)^{-1}-C_\delta\Xi(P),
 \quad C_\delta=\frac{2(1+\delta)}{(1-\delta)^3},\quad
 \delta=d/a^2\le1/16.
\]

In particular (C_\delta\le C_*=8704/3375), and
(\ell^2S_R\le-\epsilon\) implies (\Xi(P)\ge\epsilon/C_*).
Equation (12) therefore also gives a polynomial strong-negative count;
(8) is the selected stronger asymptotic sign-count estimate.

The proof must retain the additional elementary **pointwise** comparison

\[
 \Xi(P)\le C(L/a^2+1/L)=O(L/a^2),\qquad a\le L.
 \tag{13}
\]

For (|x|\le1), the unit count is (O(L)) and each normalized term is
at most (1/a^2). For (|x|>1), the strip and inverse-fourth-power shell
sum cost (O(1/L)). Thus for fixed h and (a\gg\sqrt L), sufficiently
large collars already exclude large transverse loss by ordinary counts.
Do not advertise (12) as the only information in that regime. Its
nontrivial power-law comparison for fixed h may use
(a=L^\eta,\ 0<\eta<1/2). By contrast, (13) alone cannot exclude an
arbitrarily small negative sign, so the sign-count comparison after (9)
retains (0<\eta<1).

## 5. Controls, scope and execution boundary

The [Decision17 control table][b09] and [Notes33][far]–[34][control]
retain the full collision-family screen. The new input here is explicitly
the canonical transverse density in (4), not source positivity or a
Vandermonde probability law. Euler, endpoint-defective weighted-square,
finite-score/prime, reflected super-Gaussian, smooth/primitive,
finite-profile, RH-conditional, varied-kernel and fractional-profile
controls retain their previously stated failed or untested source,
order/strip/count, literal-readout or integer-divisor premises. The
exponential density in (4) must not be assigned to a changed source
without proof. Conversely, failure of literal theta equality is not
proof that a control violates that inequality.

There is a useful sharper qualification for Note34. [E17's scope
check][e17proof] observes that deleting zeros reduces the dyadic
second moment, while its inserted conjugate groups add only
(24/(\log c)^2\le1.5), absorbed in (O(U/\log U)) for (U\ge8).
Accordingly those fixed-slice controls preserve the second-moment bound
at time zero uniformly in their parameter; they are not rejected by the
averaged (a^{-3}) estimate. A common physical heat tube and unchanged
theta source remain absent. The present pair-count bounds also permit
one such exceptional group and do not convert this preserved moment
into a selected-pair sign. No stronger exponential-density preservation
is asserted here.

E19 is one fixed analytical packet, **Sol6.1 / ultra**, with one proof
and one correction pass. It must verify the multiplicity/overlap argument,
separation, negative-kernel incidence, dyadic exponential bound and layer
cake, padded visibility integral, exact constants, all cutoff endpoints,
both D signs, D=0, uniform time zero, and the matched pointwise comparison.
The intended outputs are one derivation in notes and a small return; the
lead owns the register, synthesis, control-index updates and history.
E18 supplies the separate internal assessment after the returns are pinned.

No source sample, zero scan, new source family, enlarged-cluster argument,
manuscript revision or every-pair claim is part of the packet. Failure of
a source premise or need for a new conditioned/time-correlated estimate
returns to B work. The physical (D'=2-4MD) and incoming anchor stay
unchanged and separately paid. Give the direct evaluator every source,
count, collar, coordinate, packing and visibility input; it receives the
same bounds. No computational or transport-only advantage is claimed.

[progress]: ../../research-progress/01_VCD_GT_RESEARCH_PROGRESS_20261116.md
[b09]: 17_VCD_GT_B09_SOURCE_NEAR_FIELD_DECISION_20261117.md
[e17]: ../../research-progress/handoffs/VCD-GT-E17-r1.md
[e17proof]: ../../notes/37_VCD_GT_E17_AVERAGED_TRANSVERSE_CORRECTION_20261117.md
[density]: ../../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/notes/21_TND_O_E11_BROAD_WINDOW_TRANSVERSE_DENSITY_20261107.md
[far]: ../../notes/33_VCD_GT_E12_UNIFORM_SIGNED_FAR_EXTERIOR_20261117.md
[control]: ../../notes/34_VCD_GT_E15_IDENTICAL_COUNTS_OPPOSITE_SIGNS_20261117.md
[results]: ../../../../../../result-summaries/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a15]: ../../../../../../avoid/15_ignoring_sibling_results_and_unfinished_closures.md
