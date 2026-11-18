# VCD-GT-CM-E08 r1 — Conjugation and the negative-axis branch defect

17 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Requested helper dispatch **gpt-6.1-sol /
ultra**. Independent serving-model and actual reasoning-effort metadata
were unavailable.

**Proved in-note on the frozen local and slice domains, pending E04
assessment.** These are representations, with a finite branch-angle
bound and uniform fixed-height divisor tails. The intended consumer is
folding the weighted contours in E03. An upper bound on the signed forcing
or its transport cost remains open. [Frozen E08][request] ·
[B01 §3][decision] · [E01 audit][audit] · [CM overview][overview] ·
[CM plan][plan] · [Result index][results] · [Cluster18][cluster] ·
[Controls12][controls] · [Avoid index][avoid] · [Classification01][class] ·
[Premises02][premises] · [Scope07][scope]

## 1. Conjugate local logarithms with integer multiplicities

Use the unchanged complete theta field \(H_t=-H_{zz}\) on the independently
paid compact real count-two tube \(I\subset[0,1/2]\). Freeze \(T\ge64\),
\(L=\log T\), \(\ell=L^{-1}\), and \(r_0=a\ell\) with
\(\max(2,4\sqrt d)\le a\le L\). The selected pair consists of the two
occurrences \(c\pm\sqrt D\), counted also at \(D=0\), with real
\(c\in[T,2T]\), real \(|D|\le d\ell^2\le r_0^2/16\) and distances at most
\(r_0/4\) from \(c\). For an exterior occurrence put \(w_j=\rho_j-c\) and
\(a_j=Q(t,w_j)\) for \(Q(t,w)=w^2-D(t)\). The collar gives
\[
 |a_j|\ge(15/16)|w_j|^2,\qquad |w_j|\ge r_0 .
\]
The inherited strip gives \(|\Im w_j|\le1\). The canonical field is
real under spatial conjugation at real times, and the target multiset is
closed under conjugation for either sign of \(D\). Hence the exterior
multiset is closed under conjugation, with equal multiplicities at
distinct conjugate locations. [Parent Note41 §§1–2][n41] ·
[Assessment19][a19] · [GR Note03 §§1–3][gr] · [GR E05][gra]

Write \(w=x+iy\). Then \(Q=x^2-y^2-D+2ixy\). A real exterior location
has \(Q=x^2-D\ge 15r_0^2/16>0\). A negative-real denominator therefore
has \(x=0\) and \(y\ne0\). Conversely an exterior occurrence at \(w=iy\)
has \(Q=-y^2-D<0\), since \(y^2\ge r_0^2\). These locations are distinct
from their conjugates, even when multiple roots lie at each. In
particular, assigning \(+\pi\) and \(-\pi\) to their respective logs is
compatible with conjugation. Equal denominators at distinct locations
can carry different logs.

At a reference time \(t_*\), use the two cleared cuts of B01, with
centered ordinates \(|\Im w|\le4\) on their finite connectors and with
centered abscissas to the right of \(5\) and left of \(-5\). For this
local construction a cut can be chosen in each bounded distant window
outside the finitely many zero projections. The connectors stay
zero-free on a smaller real-time neighborhood by compactness.
In the right and left domains between the safe horizontal lines
\(\Re Q>0\), so take the principal log there. The finite middle set has
disjoint small fixed disks \(U\) about each distinct exterior location
\(w_*\), avoiding the pair and all zeros of \(Q\). Use conjugate disks,
with disks at real locations invariant under conjugation. The boundaries
stay zero-free and keep their counts after shrinking the local time
neighborhood, by Rouché and continuity for the centered field
\(H(t,c(t)+w)\). The counted moments in Note41 provide the local
analytic \(c,D\) used here.

On each disk and a sufficiently small time neighborhood put \(q_*=Q(t_*,w_*)\)
and arrange \(|Q/q_*-1|<1/2\). The spatial logarithm
\[
 \mathcal L_U(t,w)=L_*+\log\big(Q(t,w)/q_*\big),\qquad e^{L_*}=q_*,
\]
uses the analytic log through \(1\) in its second term. At a real center
take \(L_*=\log q_*\) real. For a nonreal conjugate pair of disks take
conjugate \(L_*\), using the principal argument at a non-cut center
and, for example, \(+\pi\) in the upper disk and \(-\pi\) in the lower
disk at a negative-real center. For real time this gives
\(\mathcal L_{\bar U}(t,\bar w)=\overline{\mathcal L_U(t,w)}\), including a
self-conjugate real disk. The ratio log has argument magnitude less
than \(\pi/4\). A common angle cap for these local charts is
\(\Theta=5\pi/4\), including the principal far logs. The choice can be
made at every reference time, so the compact paid real interval admits
a finite cover with this cap. This is a cover by local branches.

For fixed \(U\), the cluster contribution to \(S\) is
\[
 S_U(p,t)=\frac1{2\pi i}\oint_{\partial U}
    e^{-p\mathcal L_U(t,w)}\frac{H_z(t,c(t)+w)}{H(t,c(t)+w)}\,dw ,
 \tag{1}
\]
with positive orientation. The logarithmic derivative has residue
equal to the zero multiplicity. Holomorphy of the weight on the disk
therefore counts each occurrence with that same analytic branch.
The boundary integral is locally analytic in \(t\) and entire in
\(p\), using the canonical joint holomorphy and local zero-free contour.
When locations merge inside a disk they share the branch on that disk.
This argument uses the spatial cluster and requires no differentiable
zero labels. Near the negative axis the chart continues the logarithm
through the cut. Reassigning principal arguments at each real time
would be a different prescription. A pair whose denominator passes
transversely through the cut can have a corner in
\(2|a_j|^{-p}\cos(p\operatorname{Arg}a_j)\) at a noninteger \(p\).

## 2. Complete sum and the Schwarz identity

For \(p=u+iv\), the modulus of an occurrence in \(S\) is
\[
 |e^{-p\mathcal L_j}|=|a_j|^{-u}e^{v\Im\mathcal L_j}.
 \tag{2}
\]
For \(u\in[b,r]\), \(b>1/2\), take \(N\ge2\) integral and beyond the
finite-chart cuts. The two shells \(n\le|\Re w_j|<n+1\) have combined
count at most \(2C_{\rm u}\log(3+2T+n)\) by the inherited unit count.
On the tail \(\Re Q>0\) at the occurrences. Thus, for the cutoff keeping
all occurrences with \(|\Re w_j|<N\), including each conjugate and every
multiplicity there,
\[
 \begin{split}
 \sum_{|\Re w_j|\ge N}|e^{-p\mathcal L_j}|
 &\le 2C_{\rm u}(16/15)^r e^{(\pi/2)|v|}
      \sum_{n\ge N} n^{-2u}\log(3+2T+n) \\
 &\le 2C_{\rm u}(16/15)^r e^{(\pi/2)|v|} N^{1-2u}
 \left[\frac{\log(3+2T)+\log N}{1-\eta}
                  +\frac{\log 2}{(1-\eta)^2}\right],
 \qquad \eta=2^{1-2b}.
 \end{split}
 \tag{3}
\]
For the last inequality group the integers in
\(2^kN\le n<2^{k+1}N\) and use \(\log(3+2T+n)\le
\log(3+2T)+\log(n+1)\). For a cutoff by \(|\rho_j|\) beyond \(4T+4\),
the omitted occurrences have \(|\Re w_j|>N/2\) by the strip and
\(c\le2T\), so (3) also applies with the smaller shell cutoff once it
passes the chart cuts. Equation (3) is uniform in time where the far
branches apply, and a maximum of the cut sizes works on the finite
cover. For \(Z=\ell^{2p}S\) it is multiplied by \(\ell^{2u}\), with
\(\log\ell\) real. For a fixed integer \(N_0\) beyond the cuts,
the part \(|\Re w_j|<N_0\) has absolute sum at most
\[
 2 C_{\rm u}N_0\log(3+2T+N_0)
       \big(16/(15r_0^2)\big)^u e^{\Theta |v|},
\]
by the same unit counts, (2) and the collar. Thus the divisor
limit is locally uniform on compact
\(p\)-sets of \(\Re p>1/2\). This proves slice holomorphy and absolute
convergence with those tails. The differentiated complete tail and
complete time law belong to E02.

For a slice function \(B\), write \(B^\sharp(p)=\overline{B(\bar p)}\).
On the conjugation-compatible chart, conjugation permutes the exterior
occurrences and conjugates their logs. It fixes the log of each real
occurrence. This gives \(S^\sharp=S\) first under conjugation-closed
cutoffs and then by (3). Since \((\ell^{2p})^\sharp=\ell^{2p}\), it
also gives \(Z^\sharp=Z\). For real \(p>1/2\) these sums are real on
the chart, of unrestricted sign by this argument. The index map in
the identity is \(p\mapsto\bar p\). Spatial evenness reflects the center
to \(-c\) and excludes the reflected target; it preserves the powers
when comparing the two centered divisors with transported logs. B01
selects no \(p\mapsto\kappa-p\) completion or relation.

## 3. The \(+\pi\) slice defect and finite chart changes

On a fixed slice define \(S_+\) using principal logs off the negative
real axis and argument \(+\pi\) at every negative-real \(a_j\). Put
\[
 A_-(p,t)=\sum_{j:\,a_j<0}|a_j|^{-p}
        =2\sum_{y>0:\,c+iy\ {\rm exterior\ zero}}
                 m_y(y^2+D)^{-p},
 \tag{4}
\]
with real logs in these powers. Here \(m_y\) is the multiplicity of the
zero at \(c+iy\). The sum is finite since these locations have \(x=0\)
in the strip. Both conjugate locations enter (4), each with all its
occurrences.

Off the cut the principal logs are conjugate. On the cut
\((|a_j|^{-p}e^{-i\pi p})^\sharp=|a_j|^{-p}e^{+i\pi p}\). It follows
that the defect, in the convention \(B-B^\sharp\), is
\[
 \mathcal D_S=S_+-S_+^\sharp=-2i\sin(\pi p)A_-(p,t),
 \qquad \mathcal D_Z=Z_+-Z_+^\sharp=\ell^{2p}\mathcal D_S .
 \tag{5}
\]
The formulas are slice identities. On a single slice with principal
values elsewhere and opposite boundary arguments at each negative-real
conjugate pair, the compatible \(S\) equals
\((S_++S_+^\sharp)/2\). For continued chart logs the finite transition
below accounts for any further differences from those slice values.

For two overlapping choices \(A,B\), the common far principal logs
agree. At a shared slice refine the finite spatial clusters, if
needed, into disks about the distinct zero locations, each within both
of its branch neighborhoods. On each connected common neighborhood
\(U\) the difference of the analytic logs is \(2\pi i k_U\), for an
integer \(k_U\) constant there. Include all multiplicities. With the
\(A\)-branch traces from (1) this yields
\[
 S_B-S_A=\sum_U\big(e^{-2\pi i k_U p}-1\big)S_{A,U},\qquad
 Z_B-Z_A=\sum_U\big(e^{-2\pi i k_U p}-1\big)Z_{A,U}.
 \tag{6}
\]
The same algebra compares \(S_+\) to a local chart at a slice by
grouping occurrences with the same shift, including the cut
assignments in (5). This use of \(S_+\) requires only the values
at that slice. Each expression in (6) is a finite sum of entire
functions of \(p\); a repeated root within an analytic chart carries
one shift for all its occurrences. The formulas apply locally on
overlaps and leave global continuation of a single branch unspecified.

## 4. Weighted integrands and orientations

Fix the B01 parameters \(1/2<b<2<3<r\) and \(\epsilon>0\). Define
\[
 K_\epsilon(p,\delta)=\frac{12e^{\epsilon(p-2)^2}}{p-2}
                  +\frac{16\delta e^{\epsilon(p-3)^2}}{p-3},
 \qquad \delta=D/\ell^2,\qquad J=K_\epsilon Z .
\]
Here \(K_\epsilon^\sharp=K_\epsilon\) at a real slice, including the
second term and either sign of \(\delta\). Thus \(J^\sharp=J\) on a
compatible chart. For the \(+\pi\) assignment, \(J_+=K_\epsilon Z_+\)
has defect
\[
 \mathcal D_J=J_+-J_+^\sharp
       =-2i\,K_\epsilon(p,\delta)\,
            \ell^{2p}\sin(\pi p)A_-(p,t).
 \tag{7}
\]
For arbitrary overlaps the change in \(J\) is \(K_\epsilon\) times
the full difference in \(Z\) in (6). The same algebra applies to
the separate compact \(m\)-kernel \(1/(p-1)\) and to its damped form
\(e^{\epsilon(p-1)^2}/(p-1)\).

For a directed \(p\)-path \(\gamma\) put
\(\mathscr C_\gamma B=(2\pi i)^{-1}\int_\gamma B(p)\,dp\).
Writing \(\bar\gamma\) for the pointwise reflected path with unchanged
parameter direction, one has
\[
 \overline{\mathscr C_\gamma B}=-\mathscr C_{\bar\gamma} B^\sharp.
 \tag{8}
\]
Conjugation reverses a closed contour's orientation. Restoring
positive orientation cancels the minus sign in (8). In particular,
on the counterclockwise rectangle \(\Gamma_Y\) with vertical edges
at \(\Re p=b,r\) and horizontal edges at \(\Im p=\pm Y\), let
\(\gamma_U\) run from \(r\) via the top to \(b\).
The lower arc \(\gamma_L=-\bar\gamma_U\)
runs from \(b\) via the bottom to \(r\). If \(B=J_+\) and
\(E_B=B-B^\sharp\), the full folded expression is
\[
 \mathscr C_{\Gamma_Y} B
     = 2\Re \mathscr C_{\gamma_U}B+\mathscr C_{\gamma_L}E_B .
 \tag{9}
\]
For a compatible chart set \(E_B=0\). Equation (9) retains the
horizontal segments in both arcs.

For \(q\in\{b,r\}\) and \(V_q(Y)\) upward from \(q-iY\) to \(q+iY\),
parameterization gives
\[
 \mathscr C_{V_q(Y)} B =
 \frac1\pi\int_0^Y \Re B(q+iv)\,dv
 +\frac1{2\pi}\int_0^Y E_B(q-iv)\,dv .
 \tag{10}
\]
Indeed \(B(q-iv)=\overline{B(q+iv)}+E_B(q-iv)\). The
counterclockwise rectangle uses \(V_r(Y)\) **minus** \(V_b(Y)\),
with the bottom horizontal from left to right and top from right
to left. In using (10) with the cut assignment, the difference of
the two vertical defect integrals is part of the representation.

The defect in \(Z\) and each transition in (6) vanish at every
integer. Multiplying those changes by \(K_\epsilon\) makes the
potential poles at \(2,3\) removable. The weighted corrections can
have nonzero regular values there. At \(\delta=0\) only the pole at
\(2\) is present in the original integrand. The corresponding
weighted corrections for \(m\) are regular at \(1\). Thus the
positively oriented compact contour evaluations
\[
 F=12Z(2,t)+16\delta Z(3,t),\qquad m=Z(1,t)
\]
are independent of these branch choices. Their branch corrections
have zero **closed** integral in the half-plane. Once E03 has paid
the horizontal edges and vertical tails of the full weighted
expressions, the continued contour evaluations have the same
branch-independent values. A correction on an individual vertical
line still appears in its fold. This distinction preserves the
signed combination, with \(2m^2\) outside the forcing integral:
\(m_\sigma=2m^2-F\) and \(M'=2M^2-\ell^{-4}F\) with frozen
\(\sigma=(t-t_0)/\ell^2\) scaling. The residue orders are fixed at
\(2,3\), and separately \(1\). Equations (8)–(10) are finite-contour
identities. The height limit and its quantitative costs are E03 work.

## 5. Premise screen

The proof uses real conjugation of an integer exterior divisor
after a counted conjugation-invariant exclusion, an exterior collar,
and strip/count upper inputs for the complete tail. Merger
compatibility also uses the local analytic spatial field. These
premises give the branch identities for any data that satisfy them.
The unchanged complete canonical source and the paid physical
tube are retained for the intended application.
[Controls12][controls] · [Overview premise table][overview] ·
[Assessment19][a19] · [GR E05][gra]

| Documented control class | Status at the premises used here |
| --- | --- |
| Finite quadratic and quartic heat fields | The conjugation and local branch argument applies on a counted collar. A finite divisor satisfies coarse upper counts and lacks the canonical growing population. |
| Euler-factor translates | The theta source and its documented endpoint count discrepancy change. A direct application of the branch algebra on a slice would still work if its collar and convergence inputs are paid. |
| Weighted-square, finite-source, finite-score and finite-prime perturbations | Full reflected unit-weight theta equality fails. The fixed strip fails in the endpoint-defective subclasses identified in the inherited audit. A finite calibration does not supply the bound (3). |
| Reflected super-Gaussian | The inherited canonical order-at-most-one product premise fails in this class. The elementary conjugation algebra here does not itself use that product. |
| Smooth-shape and positive-primitive sources | Theta arithmetic changes. Transfer of the strip, unit count and safe-line inputs is untested. |
| Atomic and finite-profile controls | The canonical growing population and full theta profile are absent; a coarse upper count and some local branch identities can still hold. |
| RH-conditional endpoint mergers | The ordinary Dirichlet arithmetic changes and the construction assumes RH. A counted merger on a collar does not violate the branch identity. |
| Changed observations and fractional-profile relaxations | The varying observation fails the physical cosine readout; the fractional relaxation lacks the required integer divisor occurrences. |
| GR changed static slices and scalar equilibrium | Changed slices can satisfy the local slice premises with a different source. They supply no common paid canonical time tube. The scalar equilibrium supplies no realized complete divisor. |

The screen supports use of the identity as a representation on the
stated domain. The conjugation and branch-defect formulas need no
numerical campaign or p-reflection premise and supply no signed
improvement over the inherited direct comparator.

[request]: ../research-progress/handoffs/VCD-GT-CM-E08-r1.md
[decision]: ../brainstorm/notes/01_VCD_GT_CM_B01_DAMPED_CAUCHY_DECISION_20261117.md
[audit]: ../reviews/02_VCD_GT_CM_E01_INPUT_AUDIT_20261117.md
[overview]: ../research-overview/01_VCD_GT_CM_RESEARCH_OVERVIEW_20261117.md
[plan]: ../research-plan/01_VCD_GT_CM_RESEARCH_PLAN_20261117.md
[n41]: ../../notes/41_VCD_GT_E21_EXACT_INTERACTION_RICCATI_BOUND_20261117.md
[a19]: ../../reviews/19_VCD_GT_E22_FIXED_COLLAR_ASSESSMENT_20261117.md
[gr]: ../../01_gaussian_resolvent_hierarchy/notes/03_VCD_GT_GR_E03_GAUSSIAN_EVOLUTION_20261117.md
[gra]: ../../01_gaussian_resolvent_hierarchy/reviews/03_VCD_GT_GR_E05_INITIAL_PROOFS_ASSESSMENT_20261117.md
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
