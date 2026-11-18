# Scale and moment hierarchies: preliminary algebra for discussion

17 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Chat0007, thread
01a1eb96-c257-77a3-96be-ee1cb0279757, turn
01a1ec23-2a18-7653-aca5-eb33ced7ef51. Actual recorded model and effort
are unavailable. No collaborator was dispatched.

**Discussion-stage derivations and same-assistant checks only.** Edward
proposed Gaussian scale splitting and continuous/complex interaction
moments. This note supplies exact elementary decompositions and a finite
polynomial hierarchy calculation. It supplies no new canonical estimate,
accepted proof assessment, scientific milestone or B12 activation.
The [discussion22][discussion] records the interpretation and recommendation.

Read [result summaries][results], especially [cluster18][cluster] and
[controls12][controls], and [avoid][avoid], especially [classification01][a01],
[premises02][a02], [scope07][a07] and [joint bounds12][a12].
Classification under avoid01: these are representations and exploratory
identities, not an RH criterion or a quantified improvement to the current
interaction allowance. The control screen in Section 7 states their limits.

## 1. Notation and edge-inclusive transport

The current manuscript uses \(K\) in Section 12 and explicitly introduces
\(M=-K\) in Section 15. Thus \(D'=2+4KD=2-4MD\). No equation or time
orientation changes. Equation (12.9) already covers either sign and zero
\(D\), and its following paragraph explicitly treats equality.

On a persistent counted-pair tube, let
\[
W(t,v)=\exp\!\left(-4\int_t^vM(s)\,ds\right)>0.
\]
Then
\[
W(t,v)D(t)=D(v)-2\int_t^vW(s,v)\,ds. \tag{1}
\]
For exact quantities the right side's sign equals the sign of \(D(t)\).
Strict positivity is equivalent to \(D(t)>0\); equality gives \(D(t)=0\).
A nonnegative margin suffices for \(D(t)\ge0\). Strict separation of
independent lower/upper *bounds* is a sufficient certificate, not a
necessary condition for the exact margin to be positive.

Direct integration also gives the Volterra identity
\[
D(t)=D(v)-2(v-t)+4\int_t^vM(s)D(s)\,ds. \tag{2}
\]
It divides by neither \(D\) nor \(M\). For a double at \(t_*\),
\[
D(t)=2\int_{t_*}^{t}
 \exp\!\left(-4\int_s^t M(u)\,du\right)\,ds. \tag{3}
\]
Integrals are oriented, so this holds on both sides. On the same isolated
tube \(D(t)>0\) for \(t>t_*\) and \(D(t)<0\) for \(t<t_*\). A double
at the endpoint \(t=0\) is consistent with a nonnegative-gap objective
on \(t\ge0\); an interior double is different. These conclusions are
conditional on the tube, and do not cover arbitrary higher clusters.

For the growing-height normalization the band is \([T,2T]\), while
\(c(t)\) is a point in it. The fixed reference \(T\) defines
\(L=\log T\), \(\ell=L^{-1}\); for every center in the band,
\(L\le\log c\le L+\log2\). This makes the scale and constants uniform and
keeps the scale fixed while differentiating in time. It is also the
domain of the ordinary-center integrals and broad moment counts.
The band is not an average hidden in the definition of \(L\).

If instead \(\ell=\ell(t)\) and \(d\sigma/dt=\ell(t)^{-2}\), then
\[
m_\sigma=2m^2-\mathcal F+2\ell\ell' m,\qquad
\delta_\sigma=2-4m\delta-2\ell\ell'\delta.
\]
These terms are absent for the manuscript's frozen scale.

Edward's forcing expansion is exactly correct:
\[
\mathcal F=12\ell^4S_2+16\delta\ell^6S_3
           =\ell^4(12S_2+16DS_3),\qquad \delta=D/\ell^2. \tag{4}
\]

## 2. Relation to the author's continuum-sigma notes

Inspected all nine pages of Edward B. Baker III, *Notes on the continuum
sigma limit*, 22 November 2017, supplied [PDF][pdf]. Its size and SHA-256
match the existing [source manifest][manifest]: 168201 bytes,
86501d524918776df3ed425363ccc1772bec7fc77ddb4f74ec599acc4a451421.
This is an identity check, not validation of every source claim.

The relevant seed is equations (5)–(11), pages 1–2: telescope error-function
cutoffs at successive lengths, then recover the Coulomb kernel by an
integral of Gaussian heat kernels. The correct change of variables is
at the level of the measure:
\[
v(r,\sigma)\,d\sigma=K_\tau(r)\,d\tau,\qquad \sigma=2\sqrt\tau.
\]
The [existing source review][source-review] separates this valid seed
from the later unfinished operator-conjugation claims. Those later claims
are not imported here. The present application concerns a complex signed
zero interaction, rather than a positive Coulomb kernel on real distances.

## 3. An exact Gaussian partition of the exterior interaction

Fix a slice with real \(c,D\), an isolated pair, exterior displacements
\(w_j=\rho_j-c\), and absolutely convergent
\[
M=\sum_j a_j^{-1},\qquad a_j=w_j^2-D.
\]
For a positive physical length \(R\), set
\[
\chi_R(w)=e^{-|w|^2/R^2},\qquad
M_R=\sum_j\frac{\chi_R(w_j)}{a_j}. \tag{5}
\]
The conjugate groups make \(M_R\) real, but it need not be positive.
For \(0<R_0<\cdots<R_n\),
\[
M=M_{R_0}+\sum_{k=1}^n(M_{R_k}-M_{R_{k-1}})
       +(M-M_{R_n}). \tag{6}
\]
The corresponding weights
\[
\chi_{R_0},\quad \chi_{R_k}-\chi_{R_{k-1}},\quad 1-\chi_{R_n}
\]
are nonnegative and sum to one at every exterior occurrence. The
weights, rather than the numerical lengths, form the partition of unity.
All sums are legitimate by \(\sum|a_j|^{-1}<\infty\).

There is also a continuum scale density:
\[
\frac{\partial M_R}{\partial\log R}
 =\sum_j\frac{2|w_j|^2}{R^2}
       \frac{e^{-|w_j|^2/R^2}}{a_j},\qquad
M=\int_0^\infty\frac{\partial M_R}{\partial\log R}\frac{dR}{R}.
\tag{7}
\]
For each nonzero \(w\),
\(\int_0^\infty2|w|^2R^{-3}e^{-|w|^2/R^2}\,dR=1\).
Applying this to absolute summands proves the interchange in (7).
The endpoint limits are \(M_R\to0\) as \(R\downarrow0\), and
\(M_R\to M\) as \(R\uparrow\infty\), by dominated convergence.
An exterior collar guarantees \(w_j\ne0\).

This retains every scale and every signed exterior contribution.
Substituting (6) into the gap law is exact. It adds no inequality until
the scale terms or their joint evolution are estimated. In particular,
\(2M^2=2(\sum_k M_k)^2\) includes all cross-scale products. Independent
absolute bounds on the pieces can destroy the proposed benefit.

### Holomorphic versus radial Gaussian

For the literal proposed weight with \(\alpha>0\),
\[
|e^{-\alpha w^2}|=e^{-\alpha x^2+\alpha y^2},
\qquad w=x+iy. \tag{8}
\]
At each fixed \(\alpha\), a fixed zero strip still permits a convergent
weighted sum and finite telescoping decomposition. However, this is
not a positive decreasing radial cutoff. It can amplify the near
vertical configurations whose signed interaction is adverse; the
small-length endpoint need not vanish.

The radial choice (5) gives a positive partition and avoids that
amplification. It is nonholomorphic, so the manuscript's contour proof
of analytic time evolution cannot simply be reused. At simple roots,
\[
\frac{d}{dt}\frac{e^{-|w_j|^2/R^2}}{a_j}
=e^{-|w_j|^2/R^2}
 \left[
 \frac{D'-2w_jw_j'}{a_j^2}
 -\frac{2\Re(\overline{w_j}w_j')}{R^2a_j}
 \right] \tag{9}
\]
for fixed \(R\). The second term is transport across scales. At multiple
exterior roots, weak/integrated evolution and possible nonsmoothness
need treatment; no smooth radial hierarchy through them is asserted.
If \(R\) varies in time, its derivative contributes another explicit term.

## 4. Continuous powers and the connection to Gaussian transforms

For integer \(p\ge1\), \(S_p=\sum a_j^{-p}\). A candidate continuous
extension is
\[
\mathcal S(p,t)=\sum_j e^{-p\operatorname{Log}a_j(t)}. \tag{10}
\]
On a fixed slice, choose branches for the finitely many near terms and
the principal tail branch. The strip and \(O(X\log X)\) count give
absolute convergence and local analyticity in \(p\) for \(\Re p>1/2\).
Indeed the tail is bounded by a constant times
\(\sum n^{-2\Re p}\log(2+n)\), uniformly on compact \(p\)-sets.
This statement is local in the chosen branches; an evolving branch
choice and behavior at exterior mergers require additional care.

Negative-real \(a_j\) are allowed by the current hypotheses. Fractional
powers are branch-dependent, and naive principal branches need not
preserve the real conjugate sum. Integer \(p\) has no such ambiguity.
No continuation to \(\Re p\le1/2\) or global branch prescription is
claimed here.

For \(\Re a>0,\ \Re p>0\), the checked gamma integral is
\[
a^{-p}=\frac1{\Gamma(p)}\int_0^\infty s^{p-1}e^{-sa}\,ds.
\tag{11}
\]
This is [DLMF 5.9.1](https://dlmf.nist.gov/5.9.E1) with its exponent
parameter equal to one. For the complete sum, \(\Re p>1/2\), a persistent
positive-sector condition and the count give the needed convergence and
interchange. It relates reciprocal powers to Gaussian/Laplace scale
transforms, because \(e^{-s(w^2-D)}=e^{sD}e^{-sw^2}\).

The full near exterior need not satisfy \(\Re a_j>0\). Thus (11) cannot
be applied to it on the positive real integration ray without further
work. It can be used on a suitable far part, with the excluded near
terms retained, or with justified sector contours. Neither all-zero
positivity nor a contour construction is supplied by the identity.
For a purely radial positive denominator, the analogous Mellin
representation has no sector issue but loses the interaction phase
unless that phase is retained explicitly.

## 5. A branch-free generating function for the integer hierarchy

For \(|\eta|<\inf_j|a_j|\), define
\[
\mathcal R(\eta,t)=\sum_j\frac1{a_j-\eta}
 =\sum_{n=0}^\infty\eta^nS_{n+1}(t). \tag{12}
\]
The collar makes the indicated radius positive. Uniform absolute
convergence justifies the expansion. In particular,
\[
M=\mathcal R(0),\quad S_2=\mathcal R_\eta(0),\quad
S_3=\tfrac12\mathcal R_{\eta\eta}(0),
\]
and the existing physical equation reads
\[
M'=2M^2-12\mathcal R_\eta(0)-8D\mathcal R_{\eta\eta}(0). \tag{13}
\]
This packages the second proposal without selecting fractional-power
branches. It does not yet give an autonomous evolution equation for
\(\mathcal R\).

## 6. The next moment equation in finite polynomial heat flow

The following calculation is exact for a real polynomial heat field
with a separately counted conjugation-invariant target pair. Begin
with simple roots and write
\[
P=\sum_jw_jm_j,\quad
T_q=\sum_jw_jm_j^q,\quad m_j=a_j^{-1}.
\]
The manuscript's finite root calculation gives
\[
c'=-2P,\qquad
w_j'=4w_jm_j+2P+2\sum_{k\ne j}(w_j-w_k)^{-1}.
\]
For integer \(p\ge1\), direct differentiation and symmetrization give
\[
S_p'=-p(6+4DM)S_{p+1}-8pDS_{p+2}-4pP T_{p+1}
 -4p\sum_{j<k}
 \frac{w_jm_j^{p+1}-w_km_k^{p+1}}{w_j-w_k}. \tag{14}
\]
Let \(u=w_j,v=w_k,A=m_j,B=m_k\). The divided difference
\[
\frac{uA^3-vB^3}{u-v}
=-AB(A+B)-(D+uv)AB(A^2+AB+B^2)
\]
follows from the corresponding first-power identity and the recurrence
\(h_{n+1}=(A+B)h_n-ABh_{n-1}\).
Summing it for \(j<k\) gives
\[
\sum_{j<k}h_3
=-MS_2+\tfrac52S_3-DMS_3-\tfrac D2S_2^2
 +3DS_4-P T_3-\tfrac12T_2^2.
\]
Substitution in (14) yields
\[
\boxed{S_2'=8MS_2-32S_3+4DS_2^2-40DS_4+4T_2^2,}
\qquad
T_2=\sum_j\frac{w_j}{(w_j^2-D)^2}. \tag{15}
\]
The singular exterior pair differences have disappeared. Finite
symmetric rational sums extend through multiple roots as long as
the target/exterior separation persists; equivalently one can use
finite contour formulas. This includes a target double.

Thus the next equation has an additional signed spatial moment.
For example, at \(c=0,D=1/4\), take exterior roots \(\{2,3\}\) or
\(\{2,-3\}\), and the same target roots \(\{-1/2,1/2\}\). Both
denominator multisets are \(\{15/4,35/4\}\); hence their complete
\(\mathcal S(p)\) agrees on the natural branch for every \(p\).
Nevertheless their \(S_2'\) values are respectively
\[
-\frac{37876736}{121550625},
\qquad
-\frac{48714752}{121550625}. \tag{16}
\]
This excludes an autonomous instantaneous evolution determined only by
\(c,D,\mathcal S(\,\cdot\,)\) in this generic polynomial class. It does
not exclude a larger hierarchy or a closure using additional canonical
constraints. The examples are not globally even canonical theta fields.

The [exact checker][checker] obtains \(c',D'\) from the polynomial
identity \(F_t=-F_{zz}=Q_tA+QA_t\) modulo \(Q\), and exterior velocities
from \(F_{zz}/F_z\). It then checks the gap, \(M\), and (15) on 18
rational cases with positive, zero and negative target discriminant.
It also checks (15) at the even quartic's simultaneous target and
exterior doubles from its explicit symmetric coordinates.
[Record25][record] retains the outputs and precise scope.

No complete-theta extension of (14)–(15) is claimed as an assessed
result here. Integer contour formulas
\[
S_p=-\left\langle\frac{F_z/F}{Q^p}\right\rangle,\qquad
T_2=-\left\langle\frac{(z-c)F_z/F}{Q^2}\right\rangle
\]
suggest the same finite-product passage as manuscript Theorem 17.1.
The full limiting derivative argument is a concrete follow-up, along
with deciding which extra observables a useful closed bound needs.

## 7. Controls, scope, and the next quantitative question

The representations above make no exclusion claim. The screening of
[discussion20][previous] was reapplied to their actual premises:

| Control | What the present construction does, and the failed/missing stronger premise |
| --- | --- |
| Quadratic heat collision | \(M=S_p=0\), \(D'=2\); the integral identity includes equality and the collision exactly. Canonical growing counts are absent. |
| Even quartic heat collision | Gaussian splitting and integer identities coexist with \(M>0\) and a double. It fails the incoming-gap budget across its collision and the canonical growing counts. |
| Euler-factor controls | A valid convergent split remains an identity; canonical projected-count discrepancy fails because the extra zeros add a linear counting term. No new theta-sensitive inequality has yet been asserted. |
| Endpoint-defective weighted-square, finite-source and finite-prime controls | They fail full reflected unit-weight theta equality and the fixed global zero strip. A finite slice decomposition does not repair either premise. |
| Reflected super-Gaussian | The order-at-most-one premise used for this complete inverse-square framework fails; its full convergence must be checked separately. |
| Smooth-shape and positive-primitive controls | Unchanged theta arithmetic fails; the required strip/count/density transfer remains untested. Generic finite or convergent scale identities do not distinguish them. |
| Fixed-event atomic and finite-profile controls | Canonical growing counts and unchanged theta preparation fail; generic heat identities can still hold. |
| RH-conditional endpoint mergers | Retain their RH premise and changed arithmetic; an endpoint double is permitted by the nonnegative-gap objective. |
| Changed observation / fractional-profile controls | Fail, respectively, the physical cosine/Newman law or the integer multiplicity-counted divisor. |
| Exact-count opposite-sign examples | The current projected counts and broad moments pass in their fixed-slice class; a partition or power transform does not change the total sign. No canonical common-time family is provided. |

This is a documentary premise screen plus the explicitly recorded
polynomial checks, not a rerun of every control certificate.

The proposed analytical value is that different scales can be compared
jointly and phase/angular information retained. The next gain would be
a stronger one-sided or integrated estimate for the complete forcing
or backward cost, including cross-scale terms and the initial layer.
No requirement that every band be separately positive is imposed.
The scale and moment descriptions may be complementary; neither
transformation by itself supplies the missing source information.

[discussion]: ../brainstorm/notes/22_VCD_GT_AUTHOR_SCALE_HIERARCHY_DISCUSSION_20261117.md
[previous]: ../brainstorm/notes/20_VCD_GT_MANUSCRIPT_AND_B12_STRATEGY_DISCUSSION_20261117.md
[checker]: ../numerics/vcd_gt_hierarchy_discussion_checks.py
[record]: ../numerics/25_VCD_GT_HIERARCHY_DISCUSSION_CHECKS_20261117.json
[pdf]: ../../../../investigations-2/active/20_constrained_operator_squares/source_documents/Continuum_sigma.pdf
[manifest]: ../../../../investigations-2/active/20_constrained_operator_squares/SOURCE_DOCUMENTS.json
[source-review]: ../../../../investigations-2/active/20_constrained_operator_squares/reviews/THREE_SOURCE_NOTES_REVIEW_20261014.md
[results]: ../../../../../result-summaries/README.md
[cluster]: ../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
