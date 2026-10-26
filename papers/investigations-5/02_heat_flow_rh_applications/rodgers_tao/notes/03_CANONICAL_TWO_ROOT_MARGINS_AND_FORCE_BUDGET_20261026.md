# Canonical two-root margins and a paid exterior-force budget

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**. Rodgers–Tao chat0001, thread
`01a17a51-75b1-7bd1-86ef-6dc9485dced3`.

**Status: RT-03/RT-04 r2 complete at the selected finite-family scope.**
Contour margins, count, initial and uniform real-root data, and the
named exterior-force budget are **interval-certified** using
python-flint 0.9.0 at 192 bits. The analytical transfer and force identities
are proved from the canonical heat equation and named source inputs.
Three separate same-model contributing-agent checks are internal LLM
review, not specialist validation. This is a known-covered compact
acquisition and comparison pilot; no new Newman bound, zero-exclusion
coverage, height-uniform estimate or endpoint discriminator is claimed.

The result executes the request in the
[progress register](../research-progress/01_RODGERS_TAO_RESEARCH_PROGRESS_20261026.md)
using the exact interfaces in
[Note02](02_CORRECTED_PROPAGATION_AND_CONTOUR_FORCE_TRANSFER_20261026.md).
Evidence: [certificate](../numerics/R2_CANONICAL_TWO_ROOT_CERTIFICATE_20261026.json),
[replay](../numerics/certify_rt03_rt04_r2.py),
[input/work record](03_R2_INPUTS_AND_WORK_RECORD_20261026.json), and
[Assessment02](../reviews/02_CANONICAL_TWO_ROOT_ACQUISITION_ASSESSMENT_20261026.md).

Read the [result index](../../../../../result-summaries/README.md),
[control cluster](../../../../../result-summaries/12_collision_controls_and_screening.md),
and [avoid index](../../../../../avoid/README.md), especially
[milestones and reformulations](../../../../../avoid/01_restating_the_target.md),
[control premises](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scope](../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[known-region pilots](../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md),
and [matched complete estimates](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

## 1. Frozen family and what is newly acquired

Keep the complete canonical field

\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\quad H_t=-H_{zz},\quad H(0,z)=\xi((1+iz)/2)/8.
\]

The selected exact family is

\[
t\in[u,v]=[1/20000,1/10000],\quad \Delta t=1/20000,
\quad \Omega=(26,46)+i(-2,2),\quad\Gamma=\partial\Omega,
\]
\[
J=[28,43],\qquad |\Gamma|=p=48,\qquad
\operatorname{dist}(J,\Gamma)=b=2.
\tag{1}
\]

Gamma is fixed, positively oriented and symmetric under conjugation.
The family has two **locally labeled** zeros a1<a2 in Omega. No count
on `(0,26)` or global numbering of these zeros is asserted or required.
The whole spatial rectangle lies in `|z-36|<11`, `|Im z|<=2`.

The reusable source is HDC
[Note13](../../../../investigations-4/12_height_dependent_heat_contours/notes/13_COMPLETE_THETA_WALL_AND_COEFFICIENT_CERTIFICATE_20261023.md)
and its
[canonical source core](../../../../investigations-4/12_height_dependent_heat_contours/numerics/hdc13_theta_core.py).
Their complete wall/count certificate already covered the larger complex
time square `|Re t|,|Im t|<=1/10000`. Its existing replay was rerun and
passed with the same source/script hashes and numerical enclosures.
We reuse that paid source rather than reprove known zero coverage.

The new r2 replay independently reacquires the selected-slab wall,
argument-principle count, narrower endpoint and whole-slab roots, and
the exterior budgets below. It uses four validated contour integrals,
16 wall cells, and 32 bisection steps per endpoint root. The direct force
comparison adds two root-jet cells after this shared localization.

This finite-core calibration uses a Taylor/heat polynomial. It does not
instantiate the uncomputed constants of Ansatz Note26's high-height
retained-RS model, and does not change that source's status or task register.

## 2. Complete finite model and source errors

Let P95 be the exact degree 95 Taylor polynomial of the canonical H0
at 36. Freeze its degree, center and coefficients, and define

\[
F_t(z)=\sum_{k=0}^{5}\frac{(-t)^k}{k!}P_{95}^{(2k)}(z).
\tag{2}
\]

Exact canonical coefficients are enclosed by Arb gamma/zeta series;
their rounding intervals remain in every evaluation. F is a finite
analytic polynomial, not a replacement of the theta source by a finite
source population. Its residual is generally nonzero:

\[
(\partial_t+\partial_{zz})F_t
=\frac{(-t)^5}{5!}P_{95}^{(12)}.
\tag{3}
\]

No F-root evolution is used in this note. All velocities and energy
identities use the actual H, so no residual term is being omitted.

For reference, the complete source payment is short. Positivity of Phi
gives `|H0(36+w)|<=H0(24i)` on `|w|<=24`. The degree 95 remainder on
radius12 is at most

\[
E_{\rm sp}=2H_0(24i)2^{-96}.
\]

Radius-one Cauchy disks at physical radius11 pay `j! E_sp` for each
spatial derivative. With `T_*=1/5000`, the six-term heat Taylor remainder
and the spatial truncation give

\[
\delta_j=E_{\rm sp}\sum_{k=0}^{5}
\frac{T_*^k(j+2k)!}{k!}
+\frac{T_*^6}{6!}M_{12+j}(T_*,2),
\quad j=0,1,2,3,
\tag{4}
\]

where `M_j(T,2)=integral u^j exp(Tu^2) Phi(u) cosh(2u) du` is a
complete positive-source moment. The explicit bound retained from
HDC Note13 is

\[
M_j(T,2)\le e^T H_0(2i)+\frac{C_\Phi}{4x}
\exp(B_j^2/(2\pi)-x),
\]
\[
C_\Phi=\frac{2\pi^2}{1-16e^{-3\pi}},\quad
B_j=T/e^2+(11+j)/(2e),\quad x=(\pi/2)e^4.
\tag{5}
\]

Every theta index and the integration tail enter this estimate. It
follows by the complete geometric theta bound, splitting at integration
variable1, then completing a square. We checked this derivation and
the Cauchy/heat factorial payments against the current core. All requested
exact cells satisfy the entire-cell source domain, not only its midpoint.

The replay gives `delta_j<6e-27` for j0–3. More precisely,
`delta0=5.686472982435615e-27` and
`delta1=5.686499255239047e-27` as conservative displayed upper summaries.
The source time disk strictly contains (1), including outward rounding.

## 3. Acquired contour and root data

Each complete wall cell supplies a lower H floor mH, a lower model floor
`mF=mH-delta0`, and an upper model derivative
`M1F=upper|H_z|+delta1`. All cell endpoints and lengths are exact rationals.
Their union is the entire oriented closed Gamma. The resulting minima are

\[
\inf_{[u,v]\times\Gamma}|H|>4.94\cdot10^{-7},\qquad
\inf_{[u,v]\times\Gamma}|F|>4.94\cdot10^{-7}.
\tag{6}
\]

The more precise minima are approximately `4.94250815363207e-7`.
These are computed physical-field lower bounds, not envelope upper
bounds. Their ratio to the complete source error is fully paid.

At t=u the replay integrates the finite analytic quotient `F_z/F`
on the four edges. It then adds the complete quotient error from
Note02, using the same wall cells and (4). The corrected argument-principle
enclosure has a unique integer, **two**. Equation (6) continues this
complete multiplicity count over the connected real time slab.

Uniform sign changes in `(28,29)` and `(42,43)` exhaust this count.
Thus each interval contains exactly one simple real zero for every
t in (1), without RH or a global all-real-flow premise. Endpoint
bisection then gives the following outward decimal summaries; the
certificate stores exact rational endpoints of width `2^(-32)`.

| Time | a1 enclosure | a2 enclosure |
| --- | --- | --- |
| u=1/20000 | (28.26942130178,28.26942130202) | (42.04404152766,42.04404152791) |
| v=1/10000 | (28.26939232042,28.26939232066) | (42.04400377790,42.04400377814) |

For the **whole slab**, intervals of declared radius `1/10000` about
the exact initial-box midpoints pass fresh complete sign tests. Outward
decimal supersets are

\[
a_1(t)\in(28.26932130189,28.26952130190),\quad
a_2(t)\in(42.04394152778,42.04414152779).
\tag{7}
\]

The exact rational boxes in the certificate give

\[
13.77442022588588<g(t)=a_2-a_1<13.77482022588589.
\tag{8}
\]

All pair energies here are **ordered**:
`E(t)=sum_(i!=j)(a_i-a_j)^(-2)=2/g(t)^2`. In particular,

\[
E(u)<0.010540730940217,
\quad E(t)<0.010541037037897,
\quad \int_u^v E(t)dt<5.270518519\cdot10^{-7}.
\tag{9}
\]

The whole-slab root acquisition supplies a sharper integrated energy
allowance than generic Gronwall here. We do not count the prior root
reality conclusion as new covered territory; the narrower boxes and
paid observable are the r2 acquisition.

## 4. Paid contour model and transfer budgets

Write `H=U_H(z-a1)(z-a2)` in Omega and `D_H=2(U_H)_z/U_H`; define
D_F by removing every enclosed F zero with multiplicity. Rouche and
(6) give exactly two enclosed F zeros too. The exterior fields include
the whole analytic unit; no exterior zero tail is truncated.

For wall segment n of length l_n, let m_n,M_n be its model floor and
derivative bound. Put

\[
q_n=\frac{\delta_1+M_n\delta_0/m_n}{m_n-\delta_0},\qquad
\nu_n=-\log(1-\delta_0/m_n).
\]

Note02's contour projection, with b=2, pays

\[
A_F=\frac1{\pi b^2}\sum_n l_n M_n/m_n,\quad
\kappa=\min\left\{
\frac{\sum_n l_nq_n}{\pi b^2},
\frac{2\sum_n l_n\nu_n}{\pi b^3}\right\},
\tag{10}
\]

so `sup_J|D_F'|<=A_F` and `sup_J|(D_H-D_F)'|<=kappa`.
The matched separate-drift allowance is

\[
A_0=\min\left\{
\frac{\sum_n l_nq_n}{\pi b},
\frac{\sum_n l_n\nu_n}{\pi b^2}\right\},
\quad \sup_J|D_H-D_F|\le A_0.
\tag{11}
\]

Every source error, denominator, contour length and inverse-buffer
loss is retained. Segmentwise floors avoid paying the worst floor on
the entire contour. The replay certifies

\[
A_F<10.469690099611,\quad
\kappa<1.181558844689\cdot10^{-20},\quad
A_0<1.181558844689\cdot10^{-20}.
\tag{12}
\]

For the exact raw energy identity `E'=-4E^2+B_H`,

\[
B_H=-2\sum_{i\ne j}
\frac{D_H(a_i)-D_H(a_j)}{(a_i-a_j)^3},
\]

the same-root model contribution satisfies `|B_F[a]|<=2A_F E`.
With `I<=Delta t Emax` from (9) and the exact gap floor g_* from (8),
the complete comparison allowances are

\[
\mathcal A_{\rm model}=2A_F I,
\quad \mathcal A_{\rm paired}=2\kappa I,
\quad \mathcal A_{\rm separate}=8A_0\Delta t/g_*^3.
\tag{13}
\]

| Actual acquired payment | Conservative upper summary |
| --- | --- |
| Model exterior term | 1.103613912e-5 |
| Paired drift-variation error | 1.245486e-26 |
| Separate-drift error, same data and gap floor | 1.808404e-27 |
| Complete contour exterior budget, choosing smaller transfer | 1.103613912e-5 |

The paired error allowance is **6.88721011294 times larger** here.
Both minima select the scalar logarithm route, for which this ratio
is exactly `g_*/b`. Common-motion cancellation improves the singular
small-gap order, but does not improve this wide-gap pilot's constants.
The separate bound is used in the final contour payment. This is a
comparison of sufficient upper budgets, not of true errors.

The approximation error contributes less than `2e-27`; the model-unit
curvature payment is about `1.1e-5`. More source approximation orders
cannot substantially improve this particular budget.

## 5. Equally informed direct force comparator

Once actual root intervals have been acquired, the same source oracle
can enclose `H_z,H_zz` on their two entire time/root cells. These are
two additional cell evaluations, not a new source method. Independent
whole-cell derivative floors are

\[
|H_z(t,a_1)|>8.6414\cdot10^{-5},\qquad
|H_z(t,a_2)|>1.1092\cdot10^{-6}.
\tag{14}
\]

The exact canonical heat equation gives
`a_i'=v_i=H_zz(t,a_i)/H_z(t,a_i)`. There is no division by a model
root slope, no assumption about F's residual, and no omitted infinite
exterior contribution. For `g=a2-a1`, direct differentiation gives

\[
E'=-4(v_2-v_1)/g^3=-4E^2+B_H,
\qquad B_H=-4(v_2-v_1)/g^3+16/g^4.
\tag{15}
\]

This is the same B_H as in (13): the full exterior-unit contribution
in the exact local two-root balance. The certificate obtains throughout
the slab a signed interval approximately

\[
B_H\in[0.0007125444,0.0007130944],\qquad
0<\int_u^v B_Hdt<3.565471\cdot10^{-8}.
\tag{16}
\]

The displayed interval is an outward weakened summary of the full Arb
ball. The contour budget is about **309.53 times larger** than this
direct upper budget. This is a ratio of certified upper allowances,
not a measured speedup or a lower bound for all contour estimators.
Both routes share the canonical coefficient setup, count and root data;
the direct route adds the two jet cells just stated.

For a balance diagnostic, the internal dissipation integral is enclosed
by approximately `2.22214018e-8 +/-1.30e-12`. Combining it with (16)
encloses the actual energy increment. Independently evaluated endpoint
root boxes give

\[
E(v)-E(u)\in
[1.3418960\cdot10^{-8},1.3420388\cdot10^{-8}].
\tag{17}
\]

The two enclosures are consistent. This is a same-source consistency
check, not independent validation. The actual raw energy increases
slightly: forward repulsion inside the pair does not imply monotonicity
of its isolated energy after exterior compression is included.

## 6. Verification, controls and scope

The stored replay uses outward real/complex balls, exact rational
geometry and fails with a nonzero exit on unmet gates. An adversarial
run adding a uniform `1e-6` wall-error allowance fails the contour-floor
gate with exit 1 and writes no PASS record. The source core is hash-bound
before import. Full script/dependency hashes, runtime/library versions,
source-replay comparison and the negative test are retained in the
input/work record. Hashes identify versions; the inequalities decide
the mathematics.

The generic contour and finite heat identities remain valid on the
mandatory control families in Note02 §7. The new premise at issue is
**separated simple real-root cells with derivative floors on the whole
slab**. It fails when the enclosed block contains a multiple-root event
in the slab:
two disjoint one-root cells cannot exhaust a merging pair there, and
the event root slope is zero. An outer contour floor can survive that
collision. In particular the exact `z^2-2s` control still passes outer
isolation and regular unit drift; it fails this stronger root-data
premise at s=0. This identifies the failed quantitative premise rather
than merely saying that the control is not theta.

For q/q_(T,a), Euler-factor, weighted-square/finite-tail,
reflected/smooth/primitive, finite-prime/profile and normalized endpoint
controls, an event-containing application likewise cannot satisfy the
whole-slab separated-root/slope data. Their distinct absent canonical
arithmetic premises and local-event versus finite-threshold status stay
as recorded in Note02 and the control cluster. No earlier control
certificates were rerun and no exclusion outside (1) is inferred.

This is a local finite-core observable with no large R. It supplies no
numeric improvement against the paper's asymptotic dyadic payment:
there is no selected J_R, I^0, boundary iteration, explicit constant in
its `tilde O`, or shrinking-reference-strip assembly. Renormalized
energy has the additional terms in Note02 (12); this raw two-root
payment is not substituted for them. The actual canonical exterior
force is paid on (1), not uniformly toward an unknown threshold or
over all heights.

**Research decision:** stop attempts to obtain a contour-accuracy
advantage on this frozen pilot. Its source error is already negligible;
the observed loss is the absolute model-unit curvature estimate, while
the available root jets pay the same term much more sharply. Preserve
the finite acquisition as reusable calibration. A new RT comparison
must specify a family or information regime where margins, root access
or the corrected dyadic boundary sum differ materially. Wider scans or
extra field orders on the present box are not justified by this return.
