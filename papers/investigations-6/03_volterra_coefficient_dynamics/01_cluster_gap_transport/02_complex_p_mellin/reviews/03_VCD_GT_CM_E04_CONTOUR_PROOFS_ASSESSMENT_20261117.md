# VCD-GT-CM-E04 r1 — Assessment of the complex-power and damped Cauchy proofs

17 November 2026, America/New_York. Prepared for Edward Baker with OpenAI
Codex LLM assistance. Requested dispatch **gpt-6.1-sol / ultra**. Independent
serving-model and actual reasoning-effort metadata were unavailable. The
assessor did not author the three proofs. This separate-agent internal
assessment shares repository premises with the proofs. [Shared premises05][shared]

**Accepted within the frozen domains, with the qualifications below.**
All five SHA-256 pins in the [E04 request][request] matched before assessment.
One full pass checked the three proofs, their inherited proof and assessment
pairs, and the E01/E02/E03/E08 requests and returns against the [CM plan][plan]
and [B01][b01]. One bounded correction check rechecked the cross-reference,
the range on the derivative constants and the branch-fold cancellation.
No mathematical correction or structural change is required. The E02,
E08 and E03 identities are representations. Their convergence and error
bounds are intermediate estimates. [Result index][results] · [Cluster18][cluster] ·
[Avoid index][avoid] · [Classification01][class]

## 1. Inherited inputs and common domain

Use the unchanged complete canonical \(H(t,z)\), \(H_t=-H_{zz}\), on an
independently paid compact real count-two tube \(I\subset[0,1/2]\). Freeze
\(T\ge64\), \(L=\log T\), \(\ell=L^{-1}\), \(d\ge0\),
\(\max(2,4\sqrt d)\le a\le L\), \(r_0=a\ell\), \(c\in[T,2T]\) and
\(|D|\le d\ell^2\le r_0^2/16\). At the reference slice the physical circle of
radius \(r_0/2\) separates \(c\pm\sqrt D\), at radius at most \(r_0/4\), from
all exterior occurrences, at radii at least \(r_0\). Fixed-circle moments
give local analytic \(c,D\), including a target double. The real slice has
\(|\Im\rho|\le1\). Use the inherited unit-count and \(\Im z=\pm4\) safe-line
logarithmic derivative bounds with the same \(C_{\rm u}\ge1\). Conjugation
gives the lower safe line. The inherited order-at-most-one product and
convergent once-subtracted log derivative are available for the full
canonical field. These are paid premises. A time-continuous labeling of
exterior roots is unnecessary. [Audit E01][e01] · [Note41 §§1–3][n41] ·
[Assessment19 §§3–4][a19] · [Safe line][safe]

For \(w_j=\rho_j-c\), \(a_j=w_j^2-D\) and \(q_0=16/15\), the reverse
triangle inequality gives \(|a_j|\ge |w_j|^2/q_0\). In particular
\(\mu_j=\ell^2/a_j\) satisfies \(|\mu_j|\le q_0/a^2<1\). The assessed
pair and interaction laws give \(M=-K_{\rm phys}=S_1\),
\(D'=2-4MD\) and \(M'=2M^2-12S_2-16DS_3\), where
\(S_n=\sum_j a_j^{-n}\). GR supplies the assessed integer second-moment
law with \(+4T_2^2\), \(T_2=\sum_j w_ja_j^{-2}\). Complete passage for
these integer identities uses the fixed reference-slice products and
heat jets. The estimates below use the exact field for every real slice
and pay their own time derivative. Both signs of \(D\), target and
exterior multiples, and inward derivatives at endpoints are included.
[GR Note02][gr02] · [GR Note03 §§2–3][gr03] · [GR E05][gr05]

## 2. E02 complete local law and constants

**Accepted.** The two projection-cleared cuts can be chosen independently
in \([6,7]\) and \([-7,-6]\) in centered coordinates. At either cut the
three-unit window count is at most \(3C_{\rm u}\log(4+|U|)\) and the
deleted length is at most \(1/2\) with E02's \(\epsilon_U\). The fixed
connectors and cluster circles stay zero-free on smaller neighborhoods.
On \(|\Re w|\ge6,\ |\Im w|\le4\),
\(\Re Q\ge x^2-16-1/16\ge x^2/2\), so both half-strips use the principal
branch. Central enclosing disks can be disjoint and separated from the
two target occurrences and from \(Q=0\). The argument principle accounts
for every exterior occurrence in the central rectangle. The ratio
logarithm in (2) keeps one analytic branch per disk and a common
\(\Theta=3\pi/2\) cap, including a cluster with repeated occurrences.
This argument works after refining charts around a merger. Compactness
gives a finite cover with compact subcharts for the bounds.
[Note03 §§1, 3, 5][e02]

For \(p=u+iv\), on each fixed strip \(1/2<b\le u\le r\), the shell count
is \(2C_{\rm u}\Lambda(n)\) for \(n\ge1\), with
\(\Lambda(x)=\log(3+2T+|x|)\), and \(4C_{\rm u}L\) in the near shell.
Dyadic blocks yield (4)–(5) with
\(E_k(\gamma)=\sum_{j\ge0}2^{-j\gamma}(1+(j+1)\log 2)^k\) and
\(\gamma=2u-1\). Equation (6) counts all occurrences, with the branch
factor \(e^{v\Im\log Q}\). Its monotonicity follows from
\(|\mu_j|<1\). At a canonical modulus cutoff \(N>4T+8\) integer,
every omitted occurrence has \(|\Re w_j|>N-1-2T>N/2\).
Using \(\lfloor N/2\rfloor\ge N/3\) gives (7), including the
\(3^{2r-1}\) factor and far phase \(e^{\pi|v|/2}\).
For a centered cutoff \(|\Re w_j|<N\) with integer \(N\ge8\), start the
shell estimate at \(N\) and omit that factor. Both bound values uniformly
on paid real slices and compact \(p\)-sets. They give normal convergence
and \(p\)-holomorphy for \(\Re p>1/2\). [Note03 (4)–(7)][e02]

The residue decomposition (8) runs counterclockwise on each circle and
each closed spatial tail rectangle. The lower safe rays run rightward and
the upper rays leftward. The finite right connector goes down and the
finite left connector goes up. The removed distant right and left edges
go up and down respectively. The difference in (9) cancels the regularizer
for each occurrence before summing. The near-shell distance factors are
\(\epsilon_U,3\) and the numerator is at most 8. This gives
\(16C_{\rm u}\lambda/(3\epsilon_U)\) with \(\lambda=\log(3+|v_0|)\).
The far shells contribute at most \(32C_{\rm u}\lambda+48C_{\rm u}\)
using \(\sum n^{-2}\le2\), \(\sum n^{-2}\log(n+1)\le3\).
With \(1/\epsilon_U\le4+24C_{\rm u}\lambda\), \(C_{\rm u},\lambda\ge1\)
and the safe-line bound, the stated \(240C_{\rm u}^2\lambda^2\)
dominates the log derivative on that edge. The edge length 8 gives
(10) before Cauchy normalization. A slice-wise sequence of distant cleared
cuts suffices for the limit giving (11). [Note03 (8)–(11)][e02]

For time differentiation, \(w\) is fixed. The heat law gives
\(h_t=-h_{ww}-2hh_w+c'h_w\) and the frozen \(\ell\) gives
\((f_p)_t=pD'f_p/Q\). Expanding \(\partial_w\mathcal P_p\) in (13)
cancels the \((f_p)_{ww}h\), \(c'(f_p)_wh\), and \((f_p)_wh^2\)
terms against \(B_p\), yielding the unintegrated time derivative.
The total spatial derivative integrates to zero on each circle.
On each half-strip its primitive agrees across the finite connector
junctions and decays at both ends. Thus (14) retains the whole \(h^2\)
term, including the field data relevant to \(4T_2^2\).
[Note03 (12)–(14), (17)–(18)][e02]

The derivative-tail estimates follow independently of (7).
On either safe line the near shell is at distance at least 3 and
the \(n\)-th shell at least \(n\). The absolutely convergent
reciprocal-square and twice reciprocal-cube sums give (15) with
\(A=24C_{\rm u}\). Note41's deflated-field bound and exact \(c',D'\)
identities give the displayed choices
\[
 C_c\le16C_{\rm u}L^2/a+190C_{\rm u}L,\qquad
 C_D\le2+56d C_{\rm u}q_0 L/a^2.
\]
Writing \(J=1+|p|\), the bound \(|w|\le2|x|\) and (1) give
\(2C_DJ/x^2,8J/|x|,68J^2/x^2\) as relative bounds for
\((f_p)_t,(f_p)_w,(f_p)_{ww}\). The \(68\) is \(4+64\).
Together with \(C_h=A(1+C_c)+2A^2\), these pay both differentiated
integrands with \(C_{\rm sl}=C_h+A(2C_D+68+8C_c)+8A^2\).
On compact subcharts, the finite contour quantities
\(\kappa,W,P,A_{\rm ch}\) give the stated \(R_{b,r},C_{\rm ch}\)
in (16) by (12)–(13). Each finite portion stays in its own branch
domain and remains zero-free. [Note03 (15)–(16)][e02] · [Note41 §3][n41]

At \(X\ge7\), (15a) bounds the omitted four rays with normalization
\(4/(2\pi)=2/\pi\). It retains both connectors and all circles. The
value and physical derivative errors are proportional to
\(X^{1-2u}\Lambda(X)\) and \(X^{1-2u}\Lambda(X)^2\), respectively,
with the displayed \((2\ell^2)^u,E_k(2b-1)\), phase and \(J^2\)
factors. Equation (16) enlarges the full rays to \(|x|\ge6\), bounds
the real-part prefactors by endpoint maxima, and gives
\(C_Z J^2 e^{(3\pi/2)|v|}\) with \(C_Z\) defined by its bracket.
Locally uniform domination for \(p\) on compacts proves chartwise
real-time \(C^1\) and \(p\)-holomorphy of the derivative. At a fixed
\(T,I\) one may take a finite maximum of chart constants. The chart
widths and finite-contour maxima have no growing-\(T\) estimate here.
The spatial cutoff \(X\) needs no new vertical closure. Derivatives
at a sharp divisor cutoff \(N\) are outside the proved estimates.
[Note03 (15a)–(16)][e02]

The overlap proof refines the affected finite occurrences in common
disks. Two analytic logs there differ by \(2\pi i k_C\) with constant
\(k_C\in\{-1,0,1\}\) under the \(3\pi/2\) cap. Multiplication by
\(e^{-2\pi i k_Cp}-1\) gives the value and derivative transitions.
At integer \(p\) they vanish. Equation (18) follows by agreement of
those integer values with the inherited observables on the interval.
The atlas is the usable noninteger time domain.
[Note03 (17)–(18)][e02] · [GR E05][gr05]

## 3. E08 conjugation, slice defect and orientation

**Accepted.** An exterior real \(w\) has \(Q\ge15r_0^2/16>0\).
If \(Q<0\) is real, \(2\Re w\,\Im w=0\) therefore forces \(w=iy\)
with \(y\ne0\). Each such exterior occurrence has
\(|Q|=y^2+D>0\), for either sign of \(D\). The opposite locations
\(c\pm iy\) have equal multiplicities. Conjugate spatial disks and
opposite log arguments there give \(S^\sharp=S\), \(Z^\sharp=Z\),
where \(B^\sharp(p)=\overline{B(\bar p)}\). At a real cluster
the real branch gives the same identity. The ratio log on
\(|Q/q_*-1|<1/2\) has argument magnitude below \(\pi/4\).
The resulting \(5\pi/4\) cap works on conjugation-compatible E02
charts, including mergers. The centered divisor tail (3) uses
dyadic blocks and \(n+1\le 2^{k+1}N\) on the \(k\)-th block.
Its stated modulus-cutoff use requires the reduced shell index
past the finite cuts. E02 (7) is the directly usable modulus
bound for E03. [Note04 §§1–2][e08]

Assigning \(+\pi\) everywhere on the negative axis gives the
fixed-slice defect
\[
 S_+-S_+^\sharp=-2i\sin(\pi p)A_-,\qquad
 A_-=2\sum_{\substack{y>0\\c+iy\ {\rm exterior}}}m_y(y^2+D)^{-p}.
\]
The finite sum counts both conjugate locations and all multiplicities.
Scaling multiplies it by \(\ell^{2p}\); weighting multiplies it by
the entire selected meromorphic kernel, which is Schwarz invariant
for real time and \(\epsilon>0\). Continued compatible logs obey
the finite overlap formula (6). Opposite boundary assignments at
one slice are the symmetrization of the \(+\pi\) sum at that slice
when principal logs are used everywhere off the cut. Resetting to
those principal slice values supplies no time derivative across a
cut. Spatial evenness transports the pair and logs to center \(-c\).
The identity acts by conjugation in \(p\). [Note04 (4)–(7)][e08]

For a directed contour \(\gamma\),
\(\overline{\mathscr C_\gamma B}=-\mathscr C_{\bar\gamma}B^\sharp\).
The lower arc of the CCW rectangle is the reverse of the reflected
upper arc, giving (9) with \(+\mathscr C_{\gamma_L}(B-B^\sharp)\).
Parameterizing an upward vertical gives \(1/(2\pi)\) and the
lower-half defect with the plus sign in (10). Both horizontals
remain in the finite rectangle. The unweighted branch corrections
vanish at the integer residue positions. The corresponding full
weighted corrections have removable poles there and zero integral
on the closed rectangle. Their regular values can be nonzero.
The equality of full vertical defect integrals after E03 passage
does not imply equality of the lower-half defect integrals.
[E08 (8)–(10)][e08] · [E03 (17)–(21)][e03]

## 4. E03 complete verticals and limit ledger

**Accepted.** The fixed \(\epsilon>0\) damping has unit value at
each residue, equals \(e^{-\epsilon v^2}\) in modulus up to
\(e^{\epsilon(u-n)^2}\), and requires both lines. For \(F\) use
\((b,r)=(1,4)\), \(C_\epsilon=(12+16d)e^{4\epsilon}\),
\(\lambda=1\). For the distinct evaluation of \(m\) at \(p=1\)
use \((b,r)=(3/4,3/2)\), \(C_\epsilon=e^{\epsilon/4}\),
\(\lambda=1/4\). These are the maximum Gaussian factors and
minimum real distances in the two rows. The candidate pole at
\(3\) is removable at \(\delta=D/\ell^2=0\). The \(F\) kernel is
regular at \(1\), including on its left edge. Finite rectangles
give right upward minus left upward plus the bottom and top
edges. This yields \(m=Z(1)\),
\(F=12Z(2)+16\delta Z(3)\) and
\[
 M'=2M^2-\ell^{-4}F,\qquad m_\sigma=2m^2-F,\qquad
 \delta_\sigma=2-4m\delta .
\]
The signs follow from Note41 with \(\sigma=(t-t_0)/\ell^2\) and
\(m=\ell^2M\), so \(m_\sigma=\ell^4M'\). The local \(2m^2\)
is outside the contour. [Note05 §§1–2][e03] · [Audit E01][e01]

| Limit or operation | Checked domain and cost |
| --- | --- |
| \(Y\) for values | For \(Y>0\) both horizontal edges have total bound \((r-b)C_\epsilon A_b\Phi_\Theta(Y)/(\pi Y)\). With \(\Phi_\theta(Y)=e^{-\epsilon Y^2+\theta Y}\), \(\kappa_\theta(Y)=2\epsilon Y-\theta>0\), the four vertical tails give \(2C_\epsilon A_b\Phi_\Theta(Y)/[\pi Y\kappa_\Theta(Y)]\). The cap is \(3\pi/2\) generally, \(5\pi/4\) on compatible charts. \(A_b\) is (1). The estimates hold uniformly on the paid real tube for \(Z\) and \(Z_N\). [Note05 (1)–(6)][e03] |
| \(N\) for values | Integer \(N>4T+8\) with all ties and multiplicities. For \(B_N\) in (8), the bound (9) on the full vertical difference is \(2C_\epsilon B_N\sqrt{\pi/\epsilon}\,e^{\pi^2/(16\epsilon)}/(\pi\lambda)\). The exponent comes from the tail argument cap \(\pi/2\) by completing the square. This gives sequential \(N\) then \(Y\), or joint \(N,Y\) limit at fixed \(T,\epsilon\). [Note05 (8)–(9)][e03] |
| Signed residue remainder | On the same rectangle \(Z-Z_N\) has exact forcing residue \(12[Z(2)-Z_N(2)]+16\delta[Z(3)-Z_N(3)]\). For full verticals its magnitude is at most \(12R_2(N)+16dR_3(N)\) with \(R_n=2C_{\rm u}(\ell^2q_0)^n E_1(2n-1)3^{2n-1}N^{1-2n}\Lambda(N)\). This is the sharper value estimate \(O(\ell^4N^{-3}\log N+d\ell^6N^{-5}\log N)\) and has no damping loss. For \(m\) use \(R_1\). Add (6) for cut verticals. The coarser (9) bounds the contour envelope throughout the strip and does not claim this residue rate. [Note05 (6), (8)–(10)][e03] |
| Time derivative and \(Y\) | On a compact E02 subchart use \(C_ZJ^2 e^{\Theta|v|}\) and \(J\le U+|v|\), \(U=1+r\). The kernel term \(K_tZ\) has \(C_{\epsilon,t}=16(C_D/\ell^2)e^{4\epsilon}\) for \(F\) and vanishes for \(m\). This pays dominated differentiation (13) and the horizontal bound (14). The differentiated vertical tails use (15) for \(Y>\Theta/(2\epsilon)\): \((U+v)^2/v\le(1+U/Y)^2v\) and integration of \(v e^{-\kappa_\Theta(Y)(v-Y)}\) gives \(Y/\kappa_\Theta+1/\kappa_\Theta^2\). [Note05 (11)–(15)][e03] |
| \(X\) for values and derivatives | At \(X\ge7\), use \(Z^{[X]}\) on the fixed spatial contours retaining connectors and circles. Its derivative uses the integrand \(\partial_t(f_ph)\); the integrated-by-parts form would have finite endpoint contributions. Both \(2\ell^2<1\) and \(X\ge7\) permit replacing \(u\) by \(b\) in \(U_0,U_1\). The integral (16) has finite Gaussian moments at fixed \(\epsilon>0\), supplying full-vertical bounds for both \(Z-Z^{[X]}\) and the complete derivative difference with the \(K_t\) term. One can also take \(X\) first on each finite rectangle and then \(Y\). [Note05 §4][e03] · [Note03 (15a)][e02] |

**Cross-reference clarification.** Note05 §4 points to E02 (15) for
\(C_D\). The definition and the explicit upper choice for \(C_D\) occur
in the prose immediately following that equation. This is a location
clarification. All frozen source bytes were left intact.

On overlaps \(K\Delta Z\) and \((K\Delta Z)_t\) have removable
integer poles because both \(\Delta Z(n)\) and \(\Delta Z_t(n)\)
vanish there. The full corrections vanish in right-minus-left
differences after the paid horizontal limit. For the \(+\pi\)
slice, the lower defect term in (19) is still part of each fold.
The glued integer time laws include inward derivatives at paid endpoints.
Uniform value constants display their physical height via \(\Lambda\)
and \(L,a,d,C_{\rm u}\). The chart derivative constants and the
justified cutoff limits concern fixed \(T\). The proof keeps fixed
residue orders, real edges and positive \(\epsilon\). It proves no
growing-order, right-edge, zero-damping or half-plane continuation
limit. [Note05 §§4–6][e03]

## 5. Collision controls and B02 disposition

The documentary screen checks the heat law, cleared counted tube,
integer divisor, local logs, strip/count and full product/safe-line
inputs. The difference between the full canonical growth and the coarse
upper count matters in applying these results. No control certificate
was rerun. [Controls12][controls] · [Premises02][premises] ·
[Scope07][scope] · [E01][e01]

| Control class | Premise accounting at these proofs |
| --- | --- |
| Quadratic/quartic heat fields | Lack the canonical growing population. A coarse upper count and a cleared counted local collar can hold. They retain the local contour algebra at a collision. |
| Euler-factor translates | Change theta arithmetic and the canonical endpoint-count discrepancy. The coarser unit upper count can survive. A paid strip, collar and convergent slice series would give the same branch algebra. |
| Weighted-square, finite-source/score/prime perturbations | Full reflected unit-weight theta equality fails. The inherited endpoint-defective subclasses fail the fixed strip. Finite endpoint and prime calibration do not pay full-strip, count or safe-line transfer. |
| Reflected super-Gaussian | The documented control fails order at most one for the inherited canonical product passage. Elementary local Schwarz identities use no product. Convergence of another complete law in this class remains untested here. |
| Smooth-shape and positive-primitive sources | Exact theta square coefficients change. Strip/count/safe-line transfer remains unpaid. Reflection rigidity uses the normalized reflected integer-square class. |
| Atomic and finite/compact-profile controls | Fail the canonical growing population and full profile. The documented fixed-event threshold controls also fail eventual simplicity there. Coarse bounds and local residue algebra can still hold. |
| RH-conditional endpoint mergers | Changed ordinary Dirichlet arithmetic and RH as a premise. A paid counted double is within the local law. |
| Changed observations and fractional profiles | Fail respectively the physical cosine readout and the integer occurrence divisor. |
| GR changed static slices and scalar equilibrium | Changed slices can pass coarse slice bounds and supply no common paid canonical tube. The scalar equilibrium has no realized divisor and has a negative terminal anchor. These are scoped tests of the changed-slice and scalar classes. [GR E07][grscope] |

**B02 may use** E02 (11), (14) and (17)–(18), the value bounds
(6)–(7), the independent derivative bounds (15a)–(16), E08's compatible
Schwarz fold and exact slice defect, and E03's complete two-line
evolution with the stated fixed-\(\epsilon\) error ledger. In comparing
a joint estimate, the equally informed direct method has the same
signed residue combination, the sharper divisor error (10), paid tube
and physical anchors. Reality, vertical decay and branch cancellation
supply the representation and the displayed numerical-independent
tail allowances. The new signed upper forcing or integrated-cost
estimate remains open. Preserve the direct
\(C_F L\), \(C_F=12B_2+16dB_3\), \(B_n=14C_{\rm u}q_0^n/a^{2n}\);
the buffered \(O(\sqrt L)\) negative allowance; and the
\(O(L)\exp(O(\sqrt L))\) transport allowance for fixed collar and fixed
scaled duration. The exact gap identity
\[
 W(x,y)\delta(x)=\delta(y)-2\!\int_x^y W(u,y)\,du,\qquad
 W(x,y)=\exp(-4\!\int_x^y m)
\]
retains the initial layer and needs the paid tube and an independent
gap anchor. Equality with the full cost permits \(\delta(x)=0\),
including at the initial endpoint. There is no new collision exclusion
or quantified transport gain. The next gate is B02. No B03-level failed
premise was identified. [Note41 §§3–4][n41] · [Assessment19][a19] ·
[Joint bounds12][joint]

[request]: ../research-progress/handoffs/VCD-GT-CM-E04-r1.md
[plan]: ../research-plan/01_VCD_GT_CM_RESEARCH_PLAN_20261117.md
[b01]: ../brainstorm/notes/01_VCD_GT_CM_B01_DAMPED_CAUCHY_DECISION_20261117.md
[e01]: 02_VCD_GT_CM_E01_INPUT_AUDIT_20261117.md
[e02]: ../notes/03_VCD_GT_CM_E02_COMPLEX_POWER_TIME_LAW_20261117.md
[e08]: ../notes/04_VCD_GT_CM_E08_CONJUGATION_AND_BRANCH_DEFECT_20261117.md
[e03]: ../notes/05_VCD_GT_CM_E03_DAMPED_CAUCHY_EVOLUTION_20261117.md
[n41]: ../../notes/41_VCD_GT_E21_EXACT_INTERACTION_RICCATI_BOUND_20261117.md
[a19]: ../../reviews/19_VCD_GT_E22_FIXED_COLLAR_ASSESSMENT_20261117.md
[safe]: ../../../manuscript/sections/transverse_interactions.tex
[gr02]: ../../01_gaussian_resolvent_hierarchy/notes/02_VCD_GT_GR_E02_CANONICAL_MOMENTS_20261117.md
[gr03]: ../../01_gaussian_resolvent_hierarchy/notes/03_VCD_GT_GR_E03_GAUSSIAN_EVOLUTION_20261117.md
[gr05]: ../../01_gaussian_resolvent_hierarchy/reviews/03_VCD_GT_GR_E05_INITIAL_PROOFS_ASSESSMENT_20261117.md
[grscope]: ../../01_gaussian_resolvent_hierarchy/reviews/05_VCD_GT_GR_E07_FORCING_AND_SCOPE_ASSESSMENT_20261117.md
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[shared]: ../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md

