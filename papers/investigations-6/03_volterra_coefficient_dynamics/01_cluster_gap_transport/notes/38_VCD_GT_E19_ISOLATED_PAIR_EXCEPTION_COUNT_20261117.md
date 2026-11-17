# VCD-GT-E19 r1 — Exception counts for isolated-pair interactions

17 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Recorded executor dispatch
**gpt-6.1-sol / ultra**. Independently exposed serving-model and
actual effort metadata were unavailable.

**Proved in-note, pending separate E18 internal assessment.** This is
the fixed execution of [E19 r1][request] under [B10 Decision18][decision].
The packet and its six input pins matched. The outputs are quantitative
intermediate estimates for a prescribed class of isolated pairs.
[Result index][results] · [Controls12][controls] · [Avoid index][avoid] ·
[Classification01][classification] · [Premises02][premises] · [Scope07][scope]

## 1. Pair class and common zero-band inputs

Use the complete canonical \(H_t\) on \(0\le t\le1/2\) with
\(\partial_tH_t=-\partial_z^2H_t\) and zeros \(\rho=u+iy\) satisfying
\(|y|\le1\). Every divisor count and sum includes integer
multiplicities. Fix \(T\ge16,\ L=\log T,\ \ell=1/L,\ d\ge0\), and
\[
 \max(2,4\sqrt d)\le a\le L,\qquad 3\le R\le T/4,\qquad r_0=a\ell.
\]
At one time let \(\mathcal P\) be the distinct unordered conjugation-
invariant target pairs of occurrences \(\{z_1,z_2\}\) with
\[
 c=(z_1+z_2)/2\in[T,2T],\qquad
 D=(z_1-z_2)^2/4\in\mathbb R,\qquad |D|\le d\ell^2,\qquad
 |\rho-c|\ge r_0\ \text{for every exterior occurrence}.
 \tag{1}
\]
Here exterior means outside the two selected occurrences, and
\(|z_j-c|=\sqrt{|D|}\le r_0/4\). At \(D=0\) the two occurrences at
\(c\) form one pair. Relabeling them leaves the pair count unchanged.
The collar is an independent application hypothesis. Both \(D>0\)
and \(D<0\) are admissible, as is \(D=0\).

For \(w=\rho-c=x+iy\) and \(r=|w|\) write
\[
 q=\Re\frac{1}{w^2-D}=\frac{r^2-D-2y^2}{|w^2-D|^2},\qquad
 S_R(P)=\sum_{\rho\ {\rm exterior},\,|x|\le R}q,\qquad
 M(P)=\sum_{\rho\ {\rm exterior}}q.
 \tag{2}
\]
The collar gives \(|w^2-D|\ge r^2-|D|\ge(15/16)r^2>0\). In the
deflated interaction of [VCD-GT Note21 §1][product], conjugate
terms have equal real part and cancel each other's imaginary part.
The reciprocal formula applies to both signs of \(D\) and gives
\(w^{-2}\) at a double. The full series is absolutely convergent.
In particular, the canonical unit count gives
\(O(A[\log(2+c)+\log(n+2)])\) occurrences per shell
\(n\le|x|<n+1\), \(n\ge1\). The reciprocal has magnitude at most
\((16/15)n^{-2}\) there, and the \(|x|<1\) population is finite.

For a fixed \(0<b<1/2\), [TND-O Note21 (2), (7)–(9)][density] gives
the canonical unit count with constant \(A\), the dyadic transverse
density with constant \(B_b\), and the dyadic second moment with
\(C_b^{\rm moment}=2B_b/b^2\). These inputs hold on the whole closed
time slab and count closed real endpoints. The density uses the
strict transverse threshold. See [Assessment07 §5][assessment] and
[Source-use06][source].

Let \(\mathcal B=[T/2,5T/2]\), and write
\(N_t(v;\mathcal B)=\#\{\rho:u\in\mathcal B,\ |y|>v\}\). The three
closed dyadic intervals \([T/2,T]\), \([T,2T]\), \([2T,4T]\) cover
\(\mathcal B\). All scales are at least eight. Shared endpoints can
only add to the upper bounds. For \(0<v<1\) the dyadic density costs
relative to \(B_b TL e^{-bLv}\) are at most \(2^{b-1},1,3\):
\[
 \frac{(T/2)\log(T/2)e^{-b v\log(T/2)}}{TLe^{-bvL}}
 \le 2^{b-1},\qquad
 \frac{2T\log(2T)e^{-bv\log(2T)}}{TLe^{-bvL}}
 \le 2(1+\log(2)/L)\le3.
\]
Consequently
\[
 N_t(v;\mathcal B)\le B_b^* TL e^{-bLv},\qquad B_b^*=5B_b.
 \tag{3}
\]
For the moment, the inequalities
\(\log(T/2)\ge3L/4\) and \(\log(2T)\ge L\) bound the three costs
relative to \(C_b^{\rm moment}T/L\) by \(2/3,1,2\). The broad count
in TND-O Note21 (9) applies to \(\mathcal B\) directly. Thus
\[
 \sum_{u\in\mathcal B}y^2\le(11/3)C_b^{\rm moment} T/L,\qquad
 \#\{\rho:u\in\mathcal B\}\le 6ATL.
 \tag{4}
\]

## 2. Shared packing

If two distinct qualifying pairs share exactly one occurrence, their
centers are within \(2\sqrt d\,\ell\), by the two distances to the shared
occurrence. The remaining occurrence of the second pair is then exterior
to the first and within \(3\sqrt d\,\ell\le3r_0/4<r_0\) of its center.
This contradicts (1). Sharing two occurrences gives the same unordered
pair. The argument uses occurrences even if some locations coincide,
and also applies when \(d=0\). The collar permits exactly two
occurrences inside \(|z-c|<r_0\), so there is no ambiguity from other
label choices at a multiple location.

For distinct \(P_1,P_2\), choose any target occurrence of \(P_2\).
It is exterior to \(P_1\) and lies within \(\sqrt d\,\ell\) of \(c_2\).
Therefore
\[
 |c_1-c_2|\ge(a-\sqrt d)\ell\ge3r_0/4,\qquad
 \#\mathcal P\le1+\frac{4TL}{3a}.
 \tag{5}
\]
The second bound packs the centers into the closed band of length \(T\).
In particular the closed intervals \(I_c=[c-r_0/4,c+r_0/4]\)
are disjoint, since their length is \(r_0/2<3r_0/4\).

## 3. Primary estimate for a negative signed interaction

A negative summand in (2) satisfies
\[
 y^2>(r^2-D)/2\ge (a^2-d)\ell^2/2
       \ge (15/32)r_0^2,\qquad
 |y|>v_0:=\frac{2a}{3L}.
 \tag{6}
\]
Here \(15/32>4/9\) and \(0<v_0\le2/3\). Equivalently, its
numerator \(x^2-y^2-D\) being negative implies \(y^2+D>0\) and
\[
 |u-c|<\sqrt{y^2+D}\le |y|+\sqrt d\,\ell\le |y|+r_0/4.
\]
Although \(D\) can vary with the pair, this last window is uniform
for the given zero occurrence. By (5), an interval of length
\(2(|y|+r_0/4)\) contains at most \(1+2(|y|+r_0/4)/(3r_0/4)
=5/3+8|y|/(3r_0)\) centers.

A negative finite \(S_R(P)\) requires at least one negative summand.
All its summands have \(u\in[T-R,2T+R]\subseteq\mathcal B\).
Thus the incident pair count is at most the sum of the preceding
window bound over every occurrence in \(\mathcal B\) with
\(|y|>v_0\). A pair with several negative summands is counted several
times in this upper bound. In particular conjugate exterior
occurrences and repeated exterior zeros are covered with their
multiplicities. Layer cake gives
\[
 \sum_{\substack{u\in\mathcal B\\|y|>v_0}}|y|
 =v_0N_t(v_0;\mathcal B)+\int_{v_0}^{1}N_t(v;\mathcal B)\,dv
 \le B_b^*TL e^{-bLv_0}\left(v_0+\frac1{bL}\right).
\]
Occurrences at \(|y|=v_0\) are absent from both sides of the identity.
Occurrences at \(|y|=1\) enter the integral through thresholds
strictly below \(1\), so (3) is used only for \(v<1\). Combining
the constant and \(|y|\)-weighted terms proves
\[
 \boxed{\#\{P\in\mathcal P:S_R(P)<0\}
 \le B_b^*\left(\frac{31}{9}+\frac8{3ab}\right)
       TL e^{-2ba/3}\le C_b' TL e^{-2ba/3},}
 \quad C_b'=5B_b\left(\frac{31}{9}+\frac4{3b}\right).
 \tag{7}
\]
The \(31/9\) is \(5/3+(8/3)(2/3)\), and the last inequality uses \(a\ge2\).

For every omitted occurrence \(|x|>R\ge3\). The strip and
\(|D|\le r_0^2/16\le1/16\) give \(x^2-y^2-D>0\) for either sign
of \(D\). Each omitted real term or conjugate group contributes
positively if present. Absolute convergence in (2) gives
\(M(P)\ge S_R(P)\), hence
\[
 \#\{P\in\mathcal P:M(P)<0\}\le\#\{P\in\mathcal P:S_R(P)<0\}.
 \tag{8}
\]

## 4. Secondary estimate for a large transverse correction

Use [Note37][mean]'s center observable
\[
 \Xi_{a,R}(t,X)=\ell^2
 \sum_{\substack{\rho:\,|\rho-X|\ge a\ell\\|u-X|\le R}}
             \frac{y^2}{|\rho-X|^4}.
\]
At an eligible \(c\) the target occurrences are excluded by the radial
cutoff and every nearby exterior occurrence survives it. For
\(X\in I_c\), put \(R'=R+r_0/4\). Each contributing occurrence at
\(c\) satisfies \(|u-X|\le R'\) and
\[
 |\rho-X|\ge3r_0/4>r_0/2,\qquad
 |\rho-X|\le|\rho-c|+r_0/4\le(5/4)|\rho-c|.
\]
All surviving terms, including those originally on either cutoff
boundary, contribute at least the fraction \(\beta=(4/5)^4\) of
their former values. Any additional terms are nonnegative. Thus
\[
 \Xi_{a/2,R'}(t,X)\ge\beta\Xi_{a,R}(t,c)\qquad(X\in I_c).
 \tag{9}
\]

The disjoint intervals \(I_c\) lie in \(J=[T-r_0/4,2T+r_0/4]\).
The enlarged horizontal cutoff at these \(X\) implies
\(T-R-r_0/2\le u\le2T+R+r_0/2\). Since \(R\le T/4\), \(r_0\le1\)
and \(T\ge16\), this entire padded zero band lies inside
\(\mathcal B\). To integrate over \(J\), use Tonelli and extend the
center integral for each occurrence with \(u\in\mathcal B\) to the
real line, retaining the radial cutoff. The one-zero integral
\(I(y,s)=\int_{x^2+y^2\ge s^2} y^2(x^2+y^2)^{-2}\,dx\) is at most
\((\pi/2)\min(1/s,y^2/s^3)\) by [Note37 (3)][mean].
Applying each side of this minimum at \(s=r_0/2\) and using (4) gives
\[
 \begin{aligned}
 \int_J\Xi_{a/2,R'}(t,X)\,dX
 &\le \ell^2\sum_{u\in\mathcal B} I(y,r_0/2)\\
 &\le \frac{\pi\ell^2}{2(r_0/2)^3}\frac{11C_b^{\rm moment}T}{3L}
       =\frac{8C_sT}{a^3},\qquad C_s=\frac{11\pi C_b^{\rm moment}}6,\\
 \int_J\Xi_{a/2,R'}(t,X)\,dX
 &\le \frac{\pi\ell^2}{2(r_0/2)}6ATL
       =\frac{2C_0T}{a},\qquad C_0=3\pi A
       \quad\text{using only the complete count}.
 \end{aligned}
 \tag{10}
\]
For any \(h>0\), each center with \(\Xi_{a,R}(t,c)\ge h\) contributes
at least \(\beta h\, r_0/2\) to the integral over its own \(I_c\).
Writing \(N_\Xi(h)=\#\{P\in\mathcal P:\Xi_{a,R}(t,c)\ge h\}\) gives
\[
 \boxed{
 N_\Xi(h)\le\frac{16C_s}{\beta}\frac{TL}{a^4h},\qquad
 N_\Xi(h)\le\frac{4C_0}{\beta}\frac{TL}{a^2h}
   \quad\text{using only the complete count}.
 }
 \tag{11}
\]
Each bound may be intersected with (5). [Note37 (7)–(8)][mean] also
gives \(\ell^2 S_R\ge
\ell^2\sum_{\rm near}(r^2-D)^{-1}-C_\delta\Xi_{a,R}(t,c)\),
where \(\delta=d/a^2\le1/16\). In particular,
\(C_\delta=2(1+\delta)/(1-\delta)^3\le C_*:=8704/3375\).
If \(\ell^2 S_R\le-\epsilon\) for \(\epsilon>0\), then (11) applies
with \(h=\epsilon/C_*\). The pointwise inequality \(M(P)\ge S_R(P)\)
gives the same conclusion when \(\ell^2M(P)\le-\epsilon\).

## 5. Matched comparisons and scope

The complete count and strip also give a pointwise bound. For
\(|x|\le1\), two closed unit windows contain at most \(4AL\)
occurrences. Each normalized summand retained by the radial cutoff
is at most \(\ell^2/r^2\le a^{-2}\). For \(|x|>1\), the strip bounds
the summand in the \(n\)th shell \(n\le|x|<n+1\) by
\(\ell^2 n^{-4}\) for \(n\ge1\). The two unit windows for that shell
have starts of magnitude at most \(c+n+1\). Their count is at most
\(2A[\log(2+c)+\log(n+2)]\), with \(\log(2+c)\le2L\). Since
\(L\ge1\), this gives
\[
 \Xi_{a,R}(t,c)
 \le \frac{4AL}{a^2}+
       \frac{2A}{L}\sum_{n\ge1}\frac{2+\log(n+2)}{n^4}
 = O(L/a^2+1/L).
 \tag{12}
\]
At any fixed \(h>0\), (12) already eliminates \(\Xi_{a,R}\ge h\)
for sufficiently large \(T\) when \(a/\sqrt L\to\infty\).
For \(a=L^\eta\) with \(0<\eta<1/2\) and fixed \(d\), the source comparison in (11)
gains two powers of \(a\) over the identical visibility argument
using the complete count. The sign test in (7) includes arbitrarily
small negative interactions. A pointwise upper bound tending to zero
on \(\Xi\) controls the size of the negative part via Note37, and
does not exclude its being nonzero. The signed count divided by
\(TL\) has an exponential allowance in \(a\). The count-only packing
allowance divided by \(TL\) is \(O(1/a)\). This rate comparison applies for
\(a=L^\eta,\ 0<\eta<1\). At \(a=L\) the right side in (7) still has
order \(T^{1-2b/3}L\), which grows and leaves room for exceptions.

An equally informed direct evaluator gets the complete canonical source,
strip, count, density, moment, pair coordinates, collar, and the same
packing, visibility and pointwise bound. It can use the same proof,
together with the deflated segment or double-jet formula in
[Note24][jet] for the full interaction. The count-only allowances are
(5), the corresponding bound in (11), and the fixed-threshold
consequence of (12). The normalization by \(TL\) is independent of
the number of qualifying pairs. The result gives slice-wise counts
for (1). A fraction relative to the qualifying population would need
a lower bound for that population. Time events, gap signs, incoming
values and signed integrated costs require other inputs.

## 6. Documentary control replay

The transfer premises are the literal canonical source and its
available quantitative estimates, the complete divisor with integer
multiplicities and its strip, and the independently specified pair
geometry. The count and moment proofs use upper bounds on the
respective populations. Failure of a stronger canonical discrepancy
law alone leaves those upper bounds undecided. The scope of each
test is the documented class. [Controls12][controls] · [Note33 §6][far] ·
[Note37 §5][mean] · [Decision18 §5][decision]

| Control | Tested premise |
| --- | --- |
| Quadratic and even quartic | Can pass local pair geometry, order, and strip in the documented examples. Finite divisors lack the canonical growing cumulative main term and the unchanged theta source. Finite population upper bounds can still pass. |
| Euler-factor translates | Change the theta field and add a linear discrepancy at time zero in the documented class. Some also fail width one. The transverse density inequality for the modified heat family is untested here. |
| Weighted-square, finite-source, finite-score and finite-prime | Fail the complete reflected theta expansion with unit weights. The documented endpoint-defective classes also fail the global fixed-strip premise. Finite matched endpoints, scores or prime data leave the canonical heat-time density input unpaid. |
| Nonzero quadratic-exponential and reflected super-Gaussian | Fail the order-at-most-one input used for the deflated product in the documented classes. The reflected super-Gaussian retains reflection with a changed source. Its strip and canonical density are untested here. |
| Smooth shape and positive-primitive | Preserve the stated positivity or primitive properties with changed arithmetic. The canonical strip, count and heat-time density remain untested. |
| Reflection rigidity and four-family comparison | In polynomially weighted square combs, full reflection and the normalized endpoint force the theta weights. The four-family comparison separates missing full reflection from missing square support. The count and strip tests apply to each documented family individually. |
| Fixed-event finite-atom and compact finite-profile | Lack the unchanged theta source and, under the strip premise, their exponential-type population has at most linear growth in height. The canonical cumulative main term fails in those classes. |
| RH-conditional endpoint mergers | The control assumes RH and changes the ordinary Dirichlet arithmetic. Canonical cumulative discrepancy and the heat-time transverse transfer are untested. |
| Varied observation kernels and fractional-profile relaxation | The varied kernels lack the literal cosine/Newman readout. Fractional profiles lack the complete integer divisor used in pair packing and multiplicity counts. |

**Note34 fixed-slice fields.** Deleting occurrences from \(H_0\)
decreases each nonnegative moment over a positive dyadic band \([U,2U]\).
All added real zeros contribute zero. The only possible added
nonreal contributions have real part \(c+2/\log c\) and marks
\(|y|=2\sqrt3/\log c\). They add at most \(24/(\log c)^2\le3/2\).
Since \(U/\log U\) is increasing for \(U\ge8\), both fields preserve
the dyadic moment bound with constant increased by
\((3/2)\log(8)/8\), uniformly in \(c\ge e^4\).
[Note34 §§1–2][control] · [Note37 §5][mean]

The time-zero density inequality also transfers to these fixed
slices with an enlarged constant. The added conjugate pair counts
only if \(U\le c+2/\log c\) and \(v<2\sqrt3/\log c\). Then
\(\log U\le\log(2c)\le(5/4)\log c\), so \(bv\log U\le5\sqrt3 b/2\).
The two occurrences are bounded by
\(K_b U\log U\,e^{-bv\log U}\) with
\(K_b=2e^{5\sqrt3 b/2}/(8\log8)\), since \(U\log U\ge8\log8\).
The canonical background only loses occurrences, so \(B_b+K_b\)
is a common time-zero density constant for the modified slices.
This checks the form of (7) of TND-O Note21 at time zero for both
fields. No common physical heat tube is given by the control.
The unchanged theta identity fails whenever \(H_0(c)\ne0\), as
the inserted double changes that value to zero.

For each designated double take \(T=c,\ a=2,\ R=3,\ D=0\) with
\(d=0\). Both meet (1), with radial equality for the real
insertion. The closed \(R\) cut includes precisely the inserted
exterior group at positive real part \(c+2/\log c\).
Their normalized near signs are still \(1/2\) and \(-1/16\),
with \(\Xi_{a,R}=0\) and \(3/32\), respectively. Thus these two
fixed-slice fields obey the moment and density upper bounds with
uniform constants, and the opposite signs at their designated
centers coexist with the exception-count estimates. [Note34 §3][control]

[request]: ../research-progress/handoffs/VCD-GT-E19-r1.md
[decision]: ../brainstorm/notes/18_VCD_GT_B10_ISOLATED_PAIR_VISIBILITY_DECISION_20261117.md
[mean]: 37_VCD_GT_E17_AVERAGED_TRANSVERSE_CORRECTION_20261117.md
[control]: 34_VCD_GT_E15_IDENTICAL_COUNTS_OPPOSITE_SIGNS_20261117.md
[product]: 21_VCD_GT_E03_JOINT_CONJUGATE_SOURCE_ESTIMATE_20261116.md
[far]: 33_VCD_GT_E12_UNIFORM_SIGNED_FAR_EXTERIOR_20261117.md
[jet]: 24_VCD_GT_FOURIER_GROUPING_AND_DEFLATED_CURVATURE_20261116.md
[source]: ../references/06_VCD_GT_TRANSVERSE_MOMENT_SOURCE_USE_20261117.md
[density]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/notes/21_TND_O_E11_BROAD_WINDOW_TRANSVERSE_DENSITY_20261107.md
[assessment]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/reviews/07_TND_O_E13_ASSEMBLED_LOCALIZATION_ASSESSMENT_20261107.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[classification]: ../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
