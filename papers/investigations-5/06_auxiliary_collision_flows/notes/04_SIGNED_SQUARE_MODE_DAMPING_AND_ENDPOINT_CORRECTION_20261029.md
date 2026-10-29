# Signed square mode damping and one endpoint correction

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.
Investigation06 chat0003, **Compare auxiliary collision flows**.

**ACF-B01 R2 return: scoped failure of two fixed relative-recovery
comparisons.** Damping distinct-mode interactions by exp(-s(n-m)²)
produces a positive auxiliary observation. For the raw modes its diagonal
has size a⁻⁴. Removing the first odd endpoint derivative from each mode
improves that size to a⁻⁸, while preserving the exact complete source.
In both cases the physical first-jet energy is smaller than every
algebraic fraction of that diagonal, uniformly on compact time slabs
inside [0,1/2]. The same failure holds relative to the auxiliary
observation at the fixed time s=1.

Consequently neither version supplies the proposed fixed or algebraic
relative recovery margin. **No C1 or E01 request is selected.** These
are analytical statements with **same-assistant checking only**; no
finite onset, certificate, theta exclusion region or cost improvement
is acquired. The failure concerns the two specified decompositions and
their relative margins, not all coherent arithmetic estimates.

The raw time-zero cancellation is already proved in [BW10 Note14][bw14]
and assessed in its [separate same-model review][bw-review]. R2 applies
that obstruction to the chosen pair flow, supplies the compact-time
accounting, and tests the one explicit endpoint correction. The previous
[circle lift][circle] also distinguishes averaged energy from physical
point evaluation. These are inherited constraints, not new discoveries
of this round. [Progress01][progress] owns status; [Continuation05][next]
records the stop boundary and model guidance.

## 1 Complete source and the two frozen decompositions

For u>=0 write
\[
Y_n=\pi n^2,\quad y_n(u)=Y_ne^{4u},\quad
\phi_n(u)=e^u(2y_n(u)^2-3y_n(u))e^{-y_n(u)},
\quad \Phi=\sum_{n\ge1}\phi_n.
\tag{1}
\]
All square coefficients are one. The physical field is
\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\quad H_t=-H_{zz},\quad H(0,z)=\xi((1+iz)/2)/8.
\tag{2}
\]
Set
\[
A_n=\phi_n'(0)=e^{-Y_n}(-8Y_n^3+30Y_n^2-15Y_n),
\qquad \chi(u)=u e^{-u^2}.
\tag{3}
\]
The complete source is even by modular reflection; in particular
\(\sum_n A_n=0\), with absolute convergence. Test exactly
\[
\psi_n^{(0)}=\phi_n,
\qquad \psi_n^{(1)}=\phi_n-A_n\chi,
\qquad
h_n^{(r)}(t,z)=\int_0^\infty e^{tu^2}\psi_n^{(r)}(u)\cos(zu)\,du.
\tag{4}
\]
Here r=0 is the raw decomposition; r=1 is the single prescribed
correction. Its components need not be positive. Both complete sums
are exactly H on their common domain. The correction changes no
physical source coefficient: its entire added source is
\(-\chi\sum A_n=0\). No other correction order or profile is tested.

The raw modes are entire in t,z. The corrected modes are holomorphic
for Re t<1 and entire in z there, because their additional tail is
u exp(-(1-t)u²). Use real physical times 0<=t<=1/2; this pays that domain
restriction. The total H has a larger domain, but cancellation before
integration is not permission to extend each corrected integral beyond
its convergence domain.

## 2 Pair evolution and exact physical recovery

Keep s independent of t and retain every ordered pair. For r=0,1 set
\[
K_r(t,s,z,w)=\sum_{n,m\ge1}e^{-s(n-m)^2}
h_n^{(r)}(t,z)h_m^{(r)}(t,w).
\tag{5}
\]
Each pair evolves by multiplication with exp(-s(n-m)²), with its
s=0 product as initial data. Equivalently its equations are
\[
\partial_s K_{r,nm}=-(n-m)^2K_{r,nm},\qquad
\partial_t K_{r,nm}=-(\partial_z^2+\partial_w^2)K_{r,nm}.
\tag{6}
\]
The mode bounds below justify all sums and derivatives on compact
subsets of Re s>−pi/2, with the t domains just stated and z,w complex.
The displayed half-plane is sufficient, not a maximal-domain claim.
For real t the physical slice recovers the actual signed field:
\[
K_r(t,0,z,w)=H(t,z)H(t,w),\qquad
H(t,z)=K_r(t,0,z,0)/H(t,0),\quad H(t,0)>0.
\tag{7}
\]
Define real physical jets, their diagonal and signed interaction by
\[
v_n^{(r)}=(h_n^{(r)}(t,a),\partial_z h_n^{(r)}(t,a)),\quad
D_r=\sum_n|v_n^{(r)}|^2,\quad
X_r=\sum_{n\ne m}v_n^{(r)}\cdot v_m^{(r)}.
\tag{8}
\]
The observable and normalization are
\[
Q_r(t,s,a)=
\left.(1+\partial_z\partial_w)K_r(t,s,z,w)\right|_{z=w=a},
\quad \mathcal P_r=Q_r/D_r,
\tag{9}
\]
where D_r>0; Section 4 proves this uniformly at sufficiently large a.
At s=0,
\[
J(t,a):=H(t,a)^2+H_z(t,a)^2=D_r+X_r=Q_r(t,0,a).
\tag{10}
\]
The spectral derivatives in (9) are formed before setting z=w=a.
A second derivative of K_r(t,s,a,a) would also contain the unwanted
pure second-derivative terms and is not substituted for the mixed jet.

For real s>0 introduce the 2pi-periodic heat kernel
\[
p_s(\theta)=\frac1{2\pi}\sum_{k\in\mathbb Z}e^{-sk^2}e^{ik\theta}
=\frac1{\sqrt{4\pi s}}\sum_{\ell\in\mathbb Z}
e^{-(\theta-2\pi\ell)^2/(4s)}>0.
\tag{11}
\]
Its integral on one period is one. The normalization follows by the
Gaussian Fourier coefficients, or the checked [DLMF theta series][dlmf-series]
and [modular transform][dlmf-transform]; the [catalog][catalog] records
inspection. Put \(V_r(\theta)=\sum_n v_n^{(r)}e^{in\theta}\). Then
\[
Q_r(t,s,a)=\int_{-\pi}^{\pi}p_s(\theta)|V_r(\theta)|^2\,d\theta>0
\quad\text{if }D_r>0.
\tag{12}
\]
This is positivity of an average, not pointwise monotonicity in s.
The exact derivative remains the signed sum
\(Q_{r,s}=-\sum_{n,m}(n-m)^2e^{-s(n-m)^2}v_n\cdot v_m\).

## 3 Collision response and the specific inequality under test

At a hypothetical nondegenerate double event H(T,a)=H_z(T,a)=0,
H_zz(T,a)!=0, equation (10) gives J=0 and X_r=−D_r. In fact the
following response identity only needs the first two vanishings:
\[
Q_{r,s}(T,0,a)=2\left|\sum_n n v_n^{(r)}\right|^2\ge0.
\tag{13}
\]
It follows by expanding (n-m)²; the terms containing sum v_n vanish.
For the raw canonical modes this response is strictly positive on
0<=T<=1/2. The established [positive-packet theorem][packet] gives
h_n^(0)>0 for n>=2, and at H=0
\[
\sum_n n h_n^{(0)}=\sum_{n\ge2}(n-1)h_n^{(0)}
\ge h_2^{(0)}\ge\frac{\kappa}{4096+a^2},
\quad \kappa=\tfrac78(32\pi^2-12\pi)e^{-4\pi}>0.
\]
Hence \(Q_{0,s}(T,0,a)\ge2\kappa^2/(4096+a^2)^2\).
This is an inherited packet bound applied to the response, not an
exclusion: the same strict-positivity reasoning applies to the positive
weighted-square collision controls containing mode 2, with their own
coefficient-weighted lower bound.

The proposed separating estimate is a **specified quantitative margin**
\[
X_r\ge-(1-\eta(a))D_r,
\quad\text{equivalently }J\ge\eta(a)D_r,
\quad \eta(a)\ge c(1+a)^{-p},\quad c>0,\ p\ge0.
\tag{14}
\]
A corresponding recovery from the smoothed observation would require
\[
J\ge c(1+a)^{-p}Q_r(t,1,a).
\tag{15}
\]
Test these on [0,1/2] or any fixed nonempty compact subslab, with all
sufficiently large a. Auxiliary time 1 is fixed; no time optimization
or height-dependent s is in this round. An unspecified positive eta
chosen after knowing J/D would merely restate noncollision. Equations
(14)–(15), with an independent algebraic scale, are concrete stronger
claims. The unchanged canonical source itself refutes both below.

## 4 Complete endpoint accounting refutes the margins

Use the recurrence from [BW10 Note14][bw14]
\[
P_0(y)=2y^2-3y,\quad
P_{j+1}(y)=(1-4y)P_j(y)+4yP_j'(y),\quad
\phi_n^{(j)}(u)=e^{u-y_n(u)}P_j(y_n(u)).
\tag{16}
\]
On any compact t slab, source derivatives after multiplication by
e^{tu²}, and their fixed polynomial u moments, have summable bounds
of the form C(1+Y_n)^M exp(-Y_n). The change y=Y_n exp(4u) proves
this as in that source; the extra bounded-t log²(y/Y_n) factor is
dominated by the remaining exponential tail. The correction adds
|A_n| times fixed Gaussian derivative norms, uniformly finite for
t<=1/2. All bounds remain summable after any fixed power of n.
This justifies complete sums, endpoint evaluations, the pair derivatives,
and the integrations by parts used here.

Put
\[
B_n=\phi_n'''(0)+6A_n.
\tag{17}
\]
The first two odd endpoint derivatives of the corrected heated mode are
\[
(e^{tu^2}\psi_n^{(1)})'(0)=0,\qquad
(e^{tu^2}\psi_n^{(1)})'''(0)=B_n.
\tag{18}
\]
In the second identity the two 6tA_n contributions cancel; the +6A_n
comes from chi'''(0)=−6. Dropping it would test a different correction.
Full reflection gives sum A_n=sum B_n=0. Moreover
\[
B_n=e^{-Y_n}(-128Y_n^5+1440Y_n^4-4280Y_n^3+3450Y_n^2-465Y_n).
\tag{19}
\]
For n>=2, Y_n>12, and this polynomial is negative: group its terms as
−128Y_n⁴(Y_n−45/4)−Y_n²(4280Y_n−3450)−465Y_n.
Thus neither endpoint sequence is identically zero.

Independent integrations by parts for the cosine value and the sine
integral defining its physical derivative give, uniformly in the time slab,
\[
h_n^{(0)}=-A_na^{-2}+O_n(a^{-4}),\qquad
h_{n,z}^{(0)}=2A_na^{-3}+O_n(a^{-5}),
\]
\[
h_n^{(1)}=B_na^{-4}+O_n(a^{-6}),\qquad
h_{n,z}^{(1)}=-4B_na^{-5}+O_n(a^{-7}).
\tag{20}
\]
The O_n bounds are summable with every fixed n weight. For example the
corrected value remainder is bounded by
\((|g_n^{(5)}(0)|+\|g_n^{(6)}\|_1)a^{-6}\), with
g_n=e^{tu²}psi_n^(1). The derivative estimate is obtained separately
from u g_n; it does not differentiate an uncontrolled big-O remainder.
Every infinity boundary vanishes. All surviving zero-endpoint terms
are displayed in (18)–(20).

Define b_n^(0)=−A_n, b_n^(1)=B_n, and
c_r=sum_n(b_n^(r))²>0. Multiplying the summably controlled expansions yields
\[
D_0=c_0a^{-4}+O(a^{-6}),\qquad
D_1=c_1a^{-8}+O(a^{-10}).
\tag{21}
\]
These coefficients do not depend on t. This proves positive denominators
after a finite uninstantiated onset, uniformly in the slab.

In contrast the complete heated source is smooth, even and rapidly
decaying, with uniformly integrable derivatives of every order.
All its odd endpoint derivatives vanish. Repeated integration by parts
of the complete cosine transform, and separately of its sine derivative,
therefore gives, for every N,
\[
0\le J(t,a)\le C_N(1+a)^{-N}.
\tag{22}
\]
Only uniform compact-time bounds are claimed. At t=0 the inherited
BW10 estimate is sharper, J=O(a⁵ exp(−pi a/4)); no positive-time
exponential rate is imported from it.

Combining (10), (21) and (22), for r=0,1 and every N,
\[
\boxed{\frac{X_r}{D_r}=-1+\frac{J}{D_r},\qquad
0\le\frac{J}{D_r}\le C_{r,N}(1+a)^{-N}.}
\tag{23}
\]
Thus (14) fails for every fixed c>0 and finite p at all sufficiently
large heights, uniformly in the stated time slab. The fourth-to-eighth
power improvement in the diagonal does not supply a relative gap.

The same calculation retains the whole damped interaction:
\[
c_r(s)=\sum_{n,m}e^{-s(n-m)^2}b_n^{(r)}b_m^{(r)},\quad c_r(0)=0,
\]
\[
Q_0(t,s,a)=c_0(s)a^{-4}+O(a^{-6}),\qquad
Q_1(t,s,a)=c_1(s)a^{-8}+O(a^{-10}),\quad 0\le s\le1.
\tag{24}
\]
The kernel representation (12) applied to b proves c_r(s)>0 for s>0.
Hence
\[
\mathcal P_r(t,1,a)\longrightarrow c_r(1)/c_r>0,
\qquad
0\le J(t,a)/Q_r(t,1,a)\le C_{r,N}(1+a)^{-N}
\tag{25}
\]
for every N. This refutes (15). In particular the exact signed return
\[
J=Q_r(t,1,a)-\int_0^1Q_{r,s}(t,s,a)\,ds
\tag{26}
\]
pays essentially the entire positive observation:
the integral divided by Q_r(t,1,a) tends to one. No sign of the
integrand at each s is assumed. A positive signal generated by this
flow occurs at every sufficiently large height, irrespective of an event.

## 5 Jets, residuals, controls and matched information

Every physical jet of h_n obeys (h_n)_{t z^j}=−h_n^{(j+2)};
all z,w derivatives of the pair obey (6). Thus
\[
Q_{r,t}=-(1+\partial_z\partial_w)(\partial_z^2+\partial_w^2)K_r
\big|_{z=w=a},\qquad
\mathcal P_{r,t}=Q_{r,t}/D_r-\mathcal P_r D_{r,t}/D_r.
\tag{27}
\]
The higher-jet terms are not closed by the energy observable alone.
Likewise Q_r,a is obtained by applying partial_z+partial_w to the mixed
jet expression before restricting to z=w=a; the derivative of D_r must
also be retained when differentiating the normalized observable in a.
The n,m multiplier commutes with these physical derivatives; there is
no spatial smoothing commutator. The actual preparation (4), its
Gaussian tail, and the +6A_n endpoint payment are retained. This does
not reuse or suppress Investigation05 Note31's different residual.

All source integrals and double sums are complete. If a future
calculation truncates indices, with L=sum_n |v_n| and
epsilon_N=sum_(n>N)|v_n|, its absolute omitted-pair payment for real
s>=0 is at most 2L epsilon_N (a safe bound for all pairs with an omitted
index). Derivatives in s require the corresponding weighted index
tails. Source integration cutoffs require the full theta tail and,
for r=1, the separate Gaussian compensator tail. These are conditional
accounting formulas, not permission to choose a numerical cutoff.

| Control class | Actual application of the pair test | Premise not supplied |
| --- | --- | --- |
| Positive weighted-square controls | At an event sum v_n=0 while the heat average (12) is positive; the raw response (13) is strictly positive when the positive n>=2 modes participate | Unchanged full coefficients and full reflection fail; their finite endpoint matches do not give (22) |
| Finite-prime-compatible controls | The generic pair algebra holds for their admitted coefficient sequences | Selected-prime identities do not supply unchanged coefficients or all reflection endpoints |
| Euler-factor controls | Generic pair averaging applies only after specifying an actual decomposition | The literal canonical mode array and conductor/factors are changed |
| Reflected, positive-primitive and R1 controls | A chosen summable decomposition obeys the generic heat-average identity | No canonical square-mode array is furnished; the canonical A_n,B_n asymptotics are not attributed to these controls |

For changed coefficients a_n the proposed correction sums to
−chi times sum a_n A_n. It preserves that control's physical source
only if its first reflection endpoint is zero. Otherwise that explicit
preparation residual must be retained; it is not set to zero. The
weighted-square examples with the first endpoint matched do pass this
particular preservation condition. At an event they still give Q(0)=0.

The actual-theta bounds (23) and (25), not a substitute source, defeat
the proposed margins. Missing canonical premises in the table are not
advertised as successful separating inequalities. The [control register][controls]
supplies the inherited witness and review scopes.

With exactly the same mode information, direct assembly computes
J=|sum v_n|². The auxiliary comparison computes a larger positive
quantity and its nearly equal signed return payment. The identities
establish no benefit over coherent direct evaluation. They impose no
lower complexity bound on that evaluation, on exponentially small
one-sided margins, or on other representations. Fixed bounded height
windows, shrinking auxiliary times and other compensators remain
outside this failed uniform comparison.

## 6 Disposition

The signed estimate obtained is a scoped obstruction with the explicit
diagonal exponents 4 and 8 and the limiting pair-flow profile (24).
It is not a new RH criterion. There is no independent positive
canonical margin to pass to E01, so **R2 ends with no C1 and all E tasks
gated**. R1's different cosine/quartic conclusions remain unchanged.

Do not extend this round by choosing another subtraction order, damping
time or numerical grid. A future B01 would need a different, named
coherent signed estimate that controls the complete cancellation before
a positive diagonal is used as its scale. No such estimate is selected
here. [Continuation05][next] records what would justify reopening the
design question; no automatic R3 or model change is scheduled.

The recurrence, Gaussian correction, uniform remainder sums, heat-kernel
normalization and response identities were checked by the same assistant.
There is no separate review of this R2 extension. The [result index][results]
and [avoid index][avoid] apply, especially [target classification][a01],
[shared control premises][a02], [scoped conclusions][a07],
[complete cancellation][a12] and [utility before expansion][a20].
No repository-wide result-status promotion or manuscript update is made.

[progress]: ../research-progress/01_AUXILIARY_COLLISION_FLOWS_RESEARCH_PROGRESS_20261028.md
[next]: 05_SIGNED_MODE_R2_CONTINUATION_AND_MODEL_HANDOFF_20261029.md
[bw14]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/14_EXACT_THETA_MODE_GRAM_CANCELLATION_20261020.md
[bw-review]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/reviews/13_STRIP_KERNEL_GAP_REPLACEMENT_AND_THETA_GRAM_REVIEW_20261020.md
[packet]: ../../../investigations-3/11_arithmetic_collision_rigidity/notes/04_POSITIVE_ARITHMETIC_PACKETS_AND_MODULAR_CANCELLATION_CODEX_20261018.md
[circle]: ../../05_radial_theta_collision_geometry/notes/03_CIRCLE_HEAT_LIFT_AND_BOUNDARY_TRANSFER_OBSTRUCTION_20261027.md
[dlmf-series]: https://dlmf.nist.gov/20.2.E3
[dlmf-transform]: https://dlmf.nist.gov/20.7.E32
[catalog]: ../references/sources.json
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a20]: ../../../../avoid/20_volume_without_a_gain.md
