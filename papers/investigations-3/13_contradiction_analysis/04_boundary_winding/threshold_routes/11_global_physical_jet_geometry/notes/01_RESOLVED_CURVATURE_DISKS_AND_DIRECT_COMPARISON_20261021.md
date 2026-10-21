# Resolved curvature disks and the direct complete-jet comparison

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from this research chat's metadata.
**Status: analytic derivation conditional on a finite multiple endpoint;
same-assistant review and finite exact checks.** No specialist review,
evaluated theta certificate, or simplicity conclusion.

The first bounded comparison resolves the original first-jet curvature
into all \(m-1\) stationary neighborhoods. It gives explicit mass bounds
on complex disks of radius \(2tC/m\), and captures the full defect to
error \(O(\sqrt t)\) in a union of disks of radius \(O(t^{3/4})\).
The regular outer curvature is retained. These are quantitative
diagnostics: the required lower bound already certifies that \(H\ne0\)
on each tested disk, and the same curvature profile occurs in colliding
controls. No exclusion advantage is obtained for this selected monitor.

The stationary locations and width \(2t/m\) are inherited from
[BW10 Note 12, Section 4][n12]; the complete-source normal-form allowance
is [Note 22, HT2–HT3][n22]; the total defect and fixed-circle error are
[Note 24, GA5–GA7][n24]. The contribution here is their finite
two-dimensional mass enclosure, a growing-window capture bound, and the
explicit comparison with direct exclusion. It is not a claim of a new
general theory of Gauss maps.

Read with the [result index][results], [local geometry summary][local],
[control register][controls], and [avoid index][avoid], especially
[classification][a01], [matching controls][a02], [scoped conclusions][a07],
and [numerics after the structural question][a10].

## 1. Fixed comparison and information contract — GPJ-01

Retain the unchanged source
\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\quad H_t=-H_{zz},\quad 8H(0,z)=\xi(1/2+iz/2).
\]
For this conditional calculation suppose
\(H(0,a+z)=a_m z^m+O(z^{m+1})\), where \(a\in\mathbb R\),
\(m\ge2\), and \(a_m\ne0\). Put
\[
\tau=\sqrt{2t},\qquad
p_\tau(y)=\frac{H(\tau^2/2,a+\tau y)}{a_m\tau^m},
\qquad P(y)=\operatorname{He}_m(y).
\tag{G1}
\]
Only \(0<\tau\le\tau_*\) is compared; time zero is a limiting endpoint,
not a point at which a positive physical-jet floor is assumed. RH is
not needed for this local calculation. If the original endpoint is
studied under RH, that is an additional premise, not used below.

The observable is the Gauss area of the original pair \((H,H_z)\),
\[
d\mu_t=\frac{|HH_{zz}-H_z^2|^2}
{(|H|^2+|H_z|^2)^2}\,dA_z.
\tag{G2}
\]
Its domain will be an explicit union of moving complex disks inside a
fixed \(D_R(a)\). The four-dimensional product is normalized by its
auxiliary area; no derivative or coordinate is added to the physical pair.

**Direct reference.** Use the same complete-source enclosure of
\(p_\tau,P\) to prove \(H\ne0\) on the same disks, and hence
\((H,H_z)\ne(0,0)\). Before any source quadrature, the benefit gate is:
does the geometric certificate extend the certified domain or time range
beyond this direct reference, or supply an independently justified
endpoint budget below \(\pi(m-1)\)? Explicit control constants below
are transcription checks, not a theta performance benchmark.

For a source radius \(r_0>0\) and a finite \(Y>0\), take
\[
M=\int_0^\infty e^{r_0^2u^2/2+r_0(Y+1)u}\Phi(u)\,du,
\quad C_0=\frac{2M}{|a_m|r_0^{m+1}},\quad
\delta_j=j!C_0\tau\quad(0\le j\le2).
\tag{G3}
\]
For \(0<\tau\le r_0/2\), [HT3][n22] proves
\(\sup_{|y|\le Y}|p_\tau^{(j)}-P^{(j)}|\le\delta_j\).
Briefly, expand \(H(w^2/2,a+wy)\) in \(w\); the terms below degree \(m\)
vanish, the leading term is \(a_mw^mP(y)\), and Cauchy bounds sum the
remaining series. A unit collar in \(y\) pays the derivative estimates.
The Hermite normalization and equation
\(P''-yP'+mP=0\) agree with [DLMF 18.12.16][dlmf-gen] and
[18.8, row 14][dlmf-ode].

All source and theta-index tails remain part of \(M\). Specifically,
write \(T=r_0^2/2\), \(b=r_0(Y+1)\), and
\(C_\Phi=2\pi^2/(1-16e^{-3\pi})\). For \(L\ge1\),
\(16\pi e^{4L}\ge2T\), and
\(\lambda=4\pi e^{4L}-2TL-9-b>0\), the exterior allowance is
\[
\frac{C_\Phi e^{TL^2+(9+b)L-\pi e^{4L}}}{\lambda}.
\tag{G4}
\]
Truncating after \(N\ge1\) on \([0,L]\) has allowance
\[
\frac{2\pi^2L(N+1)^4 e^{TL^2+(9+b)L-\pi(N+1)^2}}
{1-r_N},\qquad
r_N=\left(\frac{N+2}{N+1}\right)^4 e^{-\pi(2N+3)}<1.
\tag{G5}
\]
These are [Note 21, MT18–MT19][n21] with \(j=0\). A finite quadrature
error must be added if \(M\) is evaluated. No numerical \(M\), event
height, or leading coefficient is acquired here. Height dependence is
retained through \(a_m\) and the fixed outer-boundary data; there is no
uniform lower bound for \(|a_m|\).

## 2. Finite stationary-disk enclosure — diagnostic part of GPJ-02

Let \(\nu_1,\ldots,\nu_{m-1}\) be the simple roots of \(P'\).
Choose \(d>0\) such that the closed disks
\(V_i=\{|y-\nu_i|\le2d\}\) are disjoint, contain no zero of \(P\),
and lie in \(|y|\le Y\). Choose computable polynomial bounds
\[
g\le\min_{\cup V_i}|P|,\quad g>0,\qquad
b_*\le\min_i\min_{|y-\nu_i|=d}|P'|,\quad b_*>0,
\]
\[
B_2\ge\max_{\cup V_i}|P''|+\delta_2,
\qquad h=g-\delta_0>0,
\qquad \delta_1<b_*.
\tag{G6}
\]
Bounds may replace exact extrema. Rouché gives exactly one simple zero
\(x_i(\tau)\) of \(p_\tau'\) in \(|y-\nu_i|<d\). Reality and uniqueness
make it real. The scalar lower bound \(|p_\tau|\ge h\) holds throughout
each \(V_i\); this is already the direct exclusion certificate there.

Choose \(C>0\) with \(\tau C/m\le d\), and set
\[
c_i=a+\tau x_i(\tau),\qquad
B_i(\tau,C)=\left\{|z-c_i|<\frac{\tau^2C}{m}\right\}.
\tag{G7}
\]
The physical disks are disjoint and lie inside \(a+\tau V_i\).
Define
\[
S=p_\tau''-yp_\tau'+mp_\tau,\quad
s_*:=\delta_2+Y\delta_1+m\delta_0,
\]
\[
Q=\frac{B_2C}{mh},\qquad
\eta=\frac{\tau YQ+\tau^2Q^2+s_*/h}{m}.
\tag{G8}
\]
If \(\eta<1\), then each original-jet disk has the fully explicit bounds
\[
\boxed{
\pi\frac{C^2(1-\eta)^2}{1+C^2(1-\eta)^2}
\ \le\ \mu_t(B_i(\tau,C))\ \le\
\pi\frac{C^2(1+\eta)^2}{1+C^2(1+\eta)^2}.}
\tag{G9}
\]

**Proof.** In the complex coordinate \(z=c_i+\tau^2q/m\), put
\[
F_i(q)=\frac{H_z}{H}(t,z)
=\frac{p_\tau'(x_i+\tau q/m)}{\tau p_\tau(x_i+\tau q/m)}.
\]
It is holomorphic because G6 pays the denominator; \(F_i(0)=0\).
Integrating \(p_\tau''\) along the straight segment from \(x_i\) gives
\(|F_i|\le Q\) on \(|q|\le C\). The Hermite differential equation gives
\(|S|\le s_*\), and exact differentiation yields
\[
F_i'(q)+1
=\frac{\tau yF_i-\tau^2F_i^2+S/p_\tau}{m},
\qquad y=x_i+\tau q/m.
\tag{G10}
\]
Thus \(|F_i'+1|\le\eta<1\). Integrating this error along any chord
proves injectivity on the disk and \(|F_i(q)+q|\le\eta|q|\).
Rouché, now applied to \(F_i-w\), gives
\[
D_{(1-\eta)C}\subset F_i(D_C)\subset D_{(1+\eta)C}.
\]
There is no multiplicity factor in the area change of variables because
\(F_i\) is injective. Exactly,
\[
d\mu_t=\frac{|F_i'(q)|^2}{(1+|F_i(q)|^2)^2}\,dA_q.
\]
The spherical area of \(D_s\), in the area-\(\pi\) normalization, is
\(\pi s^2/(1+s^2)\); integration proves G9. This is the standard
pullback-area interpretation, with normalization checked against
[Eremenko, Section 7, p. 21][eremenko].

For fixed \(m,C\) and fixed G3/G6 data, \(\eta=O(\tau)\). Hence
each disk has mass \(\pi C^2/(1+C^2)+O(\sqrt t)\). This is for
the original first jet at **every** critical point, including odd \(m\);
it does not substitute the deflated field \(H_z\) for \(H\).

## 3. Capture of the entire defect and the outer payment

The finite estimate also permits a growing window, without interchanging
two unproved limits. Set \(C=\tau^{-1/2}\), require
\(\sqrt\tau/m\le d\), and require G8's \(\eta\le1/2\).
These conditions hold for sufficiently small positive \(\tau\), with
event-dependent constants: if \(h\ge g/2\) and \(B_2\) is bounded, then
\(\eta=O(\sqrt\tau)\). Let \(U_\tau=\bigcup_iB_i(\tau,\tau^{-1/2})\).
For an explicit inner time range, take
\(K_2\ge\max_{\cup V_i}|P''|+g\), \(A=2K_2/g\), and
\[
L_1=\frac{AY}{m^2},\qquad
L_2=\frac{A^2}{m^3}+\frac{2(m+Y+2)C_0}{mg}.
\]
For the theta allowance G3, it suffices to impose
\[
0<\tau\le\min\left\{\frac{r_0}{2},\frac{g}{2C_0},
\frac{b_*}{2C_0},m^2d^2,\frac1{16L_1^2},\frac1{4L_2}\right\}.
\]
Indeed \(h\ge g/2\), \(B_2=K_2\) is admissible, and
\(\eta\le L_1\sqrt\tau+L_2\tau\le1/2\).
Outer-disk conditions below are additional. For an exact polynomial
allowance \(\delta_j=0\), apply G6/G8 directly.
Equation G9 gives the explicit capture bound
\[
\boxed{
\frac{\pi(m-1)}{1+4\tau}\le\mu_t(U_\tau)<\pi(m-1),\qquad
\operatorname{Area}(U_\tau)=\frac{\pi(m-1)}{m^2}\tau^3.}
\tag{G11}
\]
The disk radius is \(\tau^{3/2}/m=(2t)^{3/4}/m\). The missed amount
relative to the defect is at most
\(4\pi(m-1)\tau/(1+4\tau)\). The leading coefficient has canceled
from the mass, but remains in the permitted time range through G3.

Choose a fixed \(D_R(a)\) isolating the endpoint as in [Note 24][n24],
with the outer jet nonzero and the small-time simple-splitting condition
satisfied. Require \(U_\tau\subset D_R(a)\). Let
\[
\left|\mu_t(D_R)-\pi(m-1)-\mu_{\rm reg}(D_R)\right|
\le\epsilon_R(t)
\tag{G12}
\]
be GA7's explicit paid bound. To make that payment unambiguous, if
\(M_j\ge|H_{z^j}|\), \(0\le j\le4\), on the outer circle and time
interval, set
\[
b_R=2(M_0M_2+M_1M_3),\quad
c_R=2(M_0M_1+M_1M_2),
\]
\[
d_R=2(M_0M_3+M_1M_2+M_1M_4+M_2M_3),\quad
e_R=\min_{\partial D_R}(|H(0,z)|^2+|H_z(0,z)|^2)>0.
\]
For \(t b_R\le e_R/2\), one may use
\[
\epsilon_R(t)=\pi Rt\left(\frac{d_R}{e_R}
+\frac{2c_Rb_R}{e_R^2}\right).
\tag{G13}
\]
Complete moments \(M_j=\int_0^\infty u^j e^{t_*u^2+Ru}\Phi(u)du\)
and [MT18–MT19][n21] pay the outer jets. An evaluated certificate would
also need a certified \(e_R\). Existence at the conditional endpoint is
not a height-uniform numerical floor.

Subtracting G11 from G12 retains the whole moving complement:
\[
\boxed{
\mu_{\rm reg}(D_R)-\epsilon_R(t)
\le\mu_t(D_R\setminus U_\tau)
\le\mu_{\rm reg}(D_R)+\epsilon_R(t)
+\frac{4\pi(m-1)\tau}{1+4\tau}.}
\tag{G14}
\]
In particular the regular curvature is not discarded. The complement
includes every inner disk boundary and the fixed outer region through
exact subtraction of nonnegative measures; it is not assigned zero
flux. The set in G11 has area tending to zero and mass bounded away
from zero, quantitatively exposing the failure of uniform integrability
at a multiple endpoint. In the product surface, multiply Gauss area by
\(2\operatorname{Area}(B)\) to obtain the magnitude of the integrated
Ricci form used in GA15; divide by that factor for this comparison.

## 4. Exact finite controls and the benefit decision — GPJ-03 screen

For the pure Hermite heat polynomials, \(\delta_j=0\). Take \(C=1\)
and \(\tau=1/8\), so \(t=1/128\). The following are exact admissible
constants in G6–G9; the bounds are per disk, with mass divided by \(\pi\).

| Model | \(d,Y,h,B_2\) | \(b_*\) | \(\eta\) | Mass interval |
| --- | --- | --- | --- | --- |
| \(H=z^2-2t\) | \(1/4,1/2,3/4,2\) | \(1/2\) | \(1/18\) | \([289/613,361/685]\) |
| \(H=z^3-6tz\) | \(1/8,5/4,115/64,15/2\) | \(45/64\) | \(131/1587\) | \([1456^2/(1587^2+1456^2),1718^2/(1587^2+1718^2)]\) |

For the cubic, at \(\nu=\pm1\), use
\(|P(\nu+s)|\ge2-3|s|^2-|s|^3\) for \(|s|\le1/4\).
On \(|s|=1/8\), \(|P'(\nu+s)|\ge6|s|-3|s|^2=45/64\).
The double control has the sharper exact mass
\[
\frac{\mu_t(D_t(0))}{\pi}
=1+\frac{t^2-4}{\sqrt{t^4+64}},\qquad
0.5000076<\frac{\mu_{1/128}(D_{1/128})}{\pi}<0.5000077.
\tag{G15}
\]
The [exact checker][checker] verifies the constants and rational
square-root enclosure; the [receipt][receipt] records their scope.
These polynomial cases are not evaluations of the theta source.

**Matched comparison.** Every accepted G9 calculation assumes
\(h=g-\delta_0>0\), which already proves \(H\ne0\) on the larger
sets \(a+\tau V_i\). Consequently the mass monitor adds no
nonvanishing coverage or time range to this direct reference using the
same information. It adds a quantitative curvature diagnostic. This is
a dependency statement about G3–G9, not a lower bound on the cost of
every geometric algorithm or a comparison with optimal root counting.
Both certificates concern positive-time regions shrinking toward the
event; neither extends its nonvanishing conclusion to time zero.

For a whole-disk exclusion test one must use the **completed** boundary
flux
\(\mathcal A_t(D_R)=\frac14\int_{\partial D_R}
\partial_n\log(|H|^2+|H_z|^2)\,ds\).
It retains any common-zero atoms and agrees with \(\mu_t(D_R)\) on
a regular slice. Using only the canceled density at a multiple zero
would be invalid. The sufficient rule \(\mathcal A_t(D_R)<\pi\)
has an exact resolution limitation. For \(z^2-2t\) at \(t>0\),
the slice is regular and Note 24's formula gives
\[
\frac{\mu_t(D_R)}{\pi}
=1+\frac{R^4-4t^2}
{\sqrt{(R^4+4R^2+4t^2)^2-16t^2R^4}}.
\tag{G16}
\]
Whenever \(R^2>2t>0\), the disk contains both simple roots and its
area is greater than \(\pi\). Exact direct factorization certifies their
simplicity, whereas this small-area rule fails even with zero evaluation
error. This screens that rule on the specified quadratic disks; it
does not screen compensated boundary observables or all theta disks.

## 5. Controls, status, and next task

G9–G14 use local heat analyticity plus explicit approximating bounds.
Substituting each recorded real finite event gives the same local
calculation. Controls use their **own** analytic majorants, never G3's
unchanged theta source or unproved equal constants.

| Control | Result of the screen | Theta premise it fails |
| --- | --- | --- |
| Quadratic/cubic and other heat polynomials | G9 passes; G11 retains all \(m-1\) units; G16 gives an exact failed discriminator. | Complete theta source and its infinite arithmetic spectrum. |
| Euler-factor controls | Same disk law at their finite events, with their own source constants. | Unchanged Euler coefficients and completion data. |
| Weighted-square controls | Same local law; no global all-real heat slice is needed. | Full normalized reflection and unchanged coefficients; no all-real slice is supplied. |
| Finite-prime controls | Selected prime identities do not alter the local disk law. | Full source reflection and unchanged coefficients; no all-real slice is supplied. |
| Reflected super-Gaussian controls | Reflection does not prevent G11's shrinking-set concentration. | Canonical normalized integer-square theta expansion. |
| Smooth positive-primitive controls | A positive auxiliary primitive does not change the physical-jet calculation. | Canonical theta square coefficients; use this family's own preservation list. |
| Atomic and finite-profile threshold controls | Their finite moment/profile constraints are compatible with the same local mass. | Complete coefficients/profile growth and eventual simplicity at threshold. |
| RH-conditional close-source endpoints | Their doubles have the same local mass despite source closeness and simple all-real positive-time zeros. | Ordinary Dirichlet-series arithmetic. No closeness of event-normalized constants is inferred. |

The [control register][controls] supplies the event constructions and
their existing review status. No new threshold or damping certificate
for those families is asserted here.

**Progress decision.** GPJ-01 is complete for this comparison. The
diagnostic part of GPJ-02 now has a finite source-dependent error and a
full moving-complement account. Its intended opposing theta estimate
remains open. GPJ-03's leading-mass/direct-exclusion screen fails for
G3–G9; a numerical theta acquisition cannot repair this logical
dependency. The quantitative theta benefit comparison for a different
observable remains open. GPJ-04 remains gated.

The next useful task is to specify a **different compensated boundary
observable** on the fixed disk or its moving complement, retaining G14's
regular term, and a source estimate that uses information beyond G3's
absolute normal-form errors. It must give an independently derived
opposing sign or margin before numerical acquisition. The present
estimate does not establish such a sign and does not change HMC-05 or
HMC-06.

[n12]: ../../10_rh_implies_simple_zeros/notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md
[n21]: ../../10_rh_implies_simple_zeros/notes/21_MOVING_SIGNED_TUBES_AND_PHYSICAL_TRACE_20261021.md
[n22]: ../../10_rh_implies_simple_zeros/notes/22_HEAT_SCALE_SIGNED_TRACE_AND_UNIVERSAL_PROFILE_20261021.md
[n24]: ../../10_rh_implies_simple_zeros/notes/24_GAUSS_AREA_CONCENTRATION_AND_CURVATURE_FLUX_20261021.md
[results]: ../../../../../../../result-summaries/README.md
[local]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../../../../avoid/10_numerics_ahead_of_the_question.md
[dlmf-gen]: https://dlmf.nist.gov/18.12.E16
[dlmf-ode]: https://dlmf.nist.gov/18.8
[eremenko]: https://www.math.purdue.edu/~eremenko/dvi/ahl.pdf
[checker]: ../numerics/check_resolved_curvature_disks.py
[receipt]: ../numerics/RESOLVED_CURVATURE_DISK_CHECKS_20261021.json
