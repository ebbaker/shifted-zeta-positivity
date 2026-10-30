# E08 R16 assessment: mass-free comparison and the specified closure failure

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**, Investigation05 **chat0039**, *Continue radial theta collision
research*.

**Disposition: accepted without mathematical correction.** All seven
obligations of the [issued packet][packet] are supported. [Note101][proof]
proves its denominator-safe pointwise envelope and the failure of its
specified unsigned-norm constant-ceiling bootstrap. It does not prove
failure of the actual theta path or of every possible replacement estimate.
The physical-mass premises of R10–R15 remain unreplaced.

This is a different-model internal assessment of Astra/ultra's return,
with three read-only Sol contributing audits and parent synthesis. The
contributors share inherited premises; this is not independent specialist
review, formal verification or a new interval certificate. [Record43][record]
binds the inputs and preservation checks. [Progress05][progress] alone owns
live status. The R6-integrated manuscripts are preserved.

## 1. Dependency separation and consumer — pass

Note101 §§1–2 selects Note90 (9), the original-feedback defect estimate,
and one consumer: an upstream original-alpha ceiling from the prepared
carrier seed. Note67's Fourier lower alpha bound and carrier upper moment
bound are available without a positive physical vector-mass floor on each
regular compact interval. Its lower carrier moment floor, uniform B
increments and global upper alpha bound require that floor. Note82 imports
the resulting global bound before its decay argument; Note90 additionally
uses n>=n_*>0 in its feedback comparison and scalar-energy selection.
Note98's attraction proof imports this chain.

In contrast, E0>0, 3E0<=D_W<=6E0, h>=|W|, M>0, prepared moments and
Note98 §2's source/preparation seed are paid before that global chain.
Local reuse of a differential calculation under alpha<=L does not reuse
its global conclusion. R16 respects this distinction. As Note28 states,
unquantified global auxiliary regularity is a pointwise noncollision
reformulation; it is not an additional result. This satisfies the
[target classification][a01] and [dependency warning][a14].

## 2. Both defects and complete signed expansion — pass

With a=(int W)/M constant, n=|a|², and e=W-ah, expansion of ah=W-e gives

\[
 nG_h=G_W-2\langle\nabla W,\nabla e\rangle+G_e,
 \qquad
 nD_h=D_W-2\langle dW,e\rangle+\int d|e|^2.
\]

Thus both minus signs in Note101 (4) are correct. Since 2G_h=beta D_h,

\[
 2\Delta G-\beta\Delta D
 =2G_W-\beta D_W=(\alpha-\beta)D_W.
\]

The denominator D_W>=3E0>0 is independently protected even at n=0.
For Q_beta(f)=2||grad f||²-beta int d|f|², expanding W=ah+e and
Q_beta(h)=0 gives precisely

\[
 (\alpha-\beta)D_W=Q_\beta(e)+2\sum_j a_j
 \{2\langle\nabla h,\nabla e_j\rangle-\beta\langle dh,e_j\rangle\}.
\]

Integration by parts changes the mixed term to
-2 sum_j a_j int e_j(2 Delta h+beta d h). Its multiplier varies in
space, so int e_j=0 does not cancel it. At n=0, a=0 and e=W; the formula
is valid and tautological. No sign or error smallness follows from it.

## 3. Completed envelope and its constants — pass

Cauchy–Schwarz yields
|Delta G|<=2 sqrt(G_W G_e)+G_e and
|Delta D|<=12 sqrt(E0 E_e)+6E_e. Divide the exact identity by
D_W>=3E0 and use G_W=alpha D_W/2<=3alpha E0. With
x=G_e/E0 and y=E_e/E0 this gives

\[
 |\alpha-\beta|\le\frac4{\sqrt3}\sqrt{\alpha x}
          +\frac23x+\beta(4\sqrt y+2y).
\]

For t=sqrt(alpha), the resulting quadratic upper root is

\[
 t\le2\sqrt{x/3}+
 \sqrt{\beta(1+4\sqrt y+2y)+2x}.
\]

The x coefficient under the radical is 4/3+2/3=2, as claimed.
Squaring proves Note101 (7), monotone in its three nonnegative inputs.
This pointwise comparison has no inverse physical mass. Actual x,y
remain inputs; their appearance on the right pays neither decay nor a
global original-alpha estimate.

## 4. Local vector barriers and spatial endpoints — pass

Fix L>max{alpha(0),1/2,a_*} on its first-exit interval. Raw domination
and |a|<=1 give ||Wraw-ahraw||_{L1(vector)}<=2M=ell. The same positive
conservative kernel contracts the vector norm: integrate its scalar
kernel against |eraw|. No component-count factor is needed. Gaussian
Young estimates give E_e(0)<=c_G ell² and G_e(0)<=3c_G ell²/4, where
c_G=(8pi)^(-3/2).

For the unnormalized Fourier transform, |hat e|<=ell and Plancherel give

\[
 G_e\ge k^2E_e-\frac{\ell^2k^5}{15\pi^2}.
\]

Optimizing k³=6pi²E_e/ell² yields
c_N=(3/5)(6pi²)^(2/3). The transform normalization agrees with
[DLMF 1.14.1](https://dlmf.nist.gov/1.14.E1) and
[Parseval 1.14.8](https://dlmf.nist.gov/1.14.E8), inspected for this
assessment; tensoring its unitary convention gives (2pi)^(-3) for the
unnormalized three-dimensional forward transform. No new Nash theorem
is imported.

Under the assumed local alpha<=L,

\[
 E_e'\le-2c_NE_e^{5/3}\ell^{-4/3}+6LE_e.
\]

The barrier is E_e<=ell²D_L with D_L as issued. Summing Note82's radial
production identity over the vector components gives
G_e'+2N_e+alpha H_rad(e)=alpha(10G_e+nu E_e), nu=21/4.
Since G_e²<=N_e E_e, the gradient barrier reduces to

\[
 G_e'\le-\frac{2G_e^2}{\ell^2D_L}+10LG_e+\nu L\ell^2D_L.
\]

Its normalized positive root is
r_L=(5L+sqrt(25L²+2nu L))/2, solving 2r²-10Lr-nu L=0.
The initializer then gives G_e<=ell²H_L exactly as issued. These are
local energy calculations, not an invocation of R12 synchronization.

Repeat the calculation with ell=M for the scalar carrier. This pays
finite-window H1 integrability before using Note98's bound for
F=h²+|grad h|². The latter satisfies
(partial_s-Delta-alpha v.grad)F<=26L F. Its positive-part cutoff
argument has an L1 space-time bound; boundary errors vanish and
-alpha int d(F-C)_+ has the favorable sign.

For xi_c=h_r/b+ch, Note98's linear commutation has source
-(alpha-c)(2cb'+gamma)h, gamma=-d'/b>=0. The initial seed and
a_*<=alpha<=L give xi_m<=0 and xi_L>=0. At zero h_r/b extends smoothly
as h_rr(0)/2. The apparent 4/r term is the radial R5 comparison device;
its remaining drift is smooth with at most linear growth. Boundedness
of xi and the epsilon exp(Ks)(1+r²) barrier pay infinity. These steps
prove m<=z<=L without dividing by a vanishing spatial lower bound for h.

Integrating the slope bounds gives Gaussian tails for h and grad h and
justifies the integration by parts on the entire R3 domain:

\[
 D_h=2\int z|v|^2h^2,\qquad
 \beta=\frac{\int z^2|v|^2h^2}{\int z|v|^2h^2}\le L.
\]

The denominator is positive; the prepared inner ball remains included.
Every bound in this section depends on the local ceiling L and does
not establish that ceiling.

## 5. Failure of precisely this bootstrap — pass

M,E0,c_G,D_L,H_L are positive, so x_L=ell²H_L/E0>0 and
y_L=ell²D_L/E0>0. For every finite L>0,

\[
 L(1+4\sqrt{y_L}+2y_L)+2x_L>L.
\]

The inner radical of F(L,x_L,y_L) already exceeds sqrt(L), proving
F(L,x_L,y_L)>L. This upper allowance cannot close the proposed
constant ceiling. It does not imply actual alpha>L or divergence of
the unchanged theta path. It excludes neither sharper bounds nor a
separately paid beta gap or signed estimate. Importing R12 decay to
close this upstream ceiling would reverse its dependency. The negative
conclusion obeys the [scope rule][a07].

## 6. Genuine weighted-square screen — pass

The [square-support source][square] fixes positive weights once and
for all through a unique Wronskian root. Its inherited receipt encloses
the double event at T=1/4, A* in (44.1303,44.1304), with a nonzero
second spectral derivative. The source note and receipt were inspected;
the interval computation was not replayed or upgraded to a new certificate.

Each weighted summand retains Note98 (9)'s logarithmic derivative.
Positive averaging preserves R(log f)'<=-19R²/8. Hence the tail excess
is <=16/19, the projection factor is <=35/38, and the same unit Gaussian
tilt gives -h_r/(rh)>=41/152 and z(0,r)>=41/304, with z<=1/2.
At the projected sphere endpoints nu is continuous and tau nu is C1;
internal traces cancel. The Gaussian endpoints and full inner ball
are paid exactly as for the complete source.

This is a different source with the same carrier construction. Its own
h0 is independent of A, hence identical at A=2 and A=A*, but differs
from canonical theta's h0. All raw spatial moments are finite. Gaussian
preparation yields nonzero radial Schwartz W0: the raw first component
is nonzero near r=1 and Gaussian convolution is injective. The source's
even extension being only C2 does not violate Note28's prepared local
class, which requires no full-u reflection here.

At the event the conserved vector mass vanishes. Note28 then gives
finite Smax and B,alpha divergence on this admissible prepared path.
Thus a global-alpha assertion from only the shared qualitative seed,
domination, energy and local-flow premises would fail in that class.
No event at A=2, finite all-real threshold, canonical-theta collision,
or exclusion of a literal-frequency/full-source signed estimate follows.

## 7. Other controls, comparison and preservation — pass

Note101 §6 retains the [control register][controls]'s qualifications.
Gaussian-polynomial controls have no established matching seed here;
R6 observation kernels fail literal cosine and do not automatically
inherit this carrier domination. Positive square-source finite-prime
realizations retain the summand seed only with their paid tails and
distinct high-gap events. Reflected super-Gaussians lack the square-source
representation. Smooth/primitive controls retain damping and time-domain
conditions. Euler/Laguerre witnesses are not double events; atomic sources
need a separate prepared extension; RH-conditional endpoints remain
conditional. The SUSY form obstructions do not instantiate this path.

The direct comparator gets every identity and datum and the same failed
closure. Actual forcing (alpha-beta)div(vh), genuine residual, raw/prepared
mismatch, complete source commutators, sphere cancellation and the whole
inner ball remain. No residual estimate is silently used to pay the
signed feedback numerator.

All four issued R16 hashes and the ten non-manuscript inherited hashes
in record41 match. Its earlier manuscript hash is superseded by the
documented E05 R6 integration: the current main source matches record42's
after-hash; the companion matches both. This is expected provenance,
not an assessment correction. The 243 preexisting investigation artifacts
in record43's protected manifest remain byte-identical during this turn.
No manuscript edit/build, numerical acquisition, event replay, new PDE,
snapshot, commit or tag was performed.

**Next: [B] CTF-B02 source-sensitive signed-feedback decision — Astra.**
Select one independently paid complete-source input, one signed quantity
or ceiling gap, and one finite test for one original-alpha consumer.
[Continuation106][next] updates Note104's ready-after-assessment branch.
E07 remains unready. This assessment stops at its issued boundary.

[packet]: ../research-progress/handoffs/CTF-E08_MASS_FREE_FEEDBACK_CLOSURE_ASSESSMENT_R16_20261029.md
[proof]: ../notes/101_MASS_FREE_FEEDBACK_DEFECT_AND_SLOPE_CLOSURE_TEST_R16_20261029.md
[record]: ../numerics/43_MASS_FREE_FEEDBACK_R16_E08_ASSESSMENT_RECORD_20261029.json
[progress]: ../research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md
[next]: ../notes/106_MASS_FREE_FEEDBACK_ASSESSMENT_AND_MODEL_CONTINUATION_R16_20261029.md
[square]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/05_control_families/01_SQUARE_SUPPORT_ENDPOINT_COLLISION_OBSTRUCTION_20261015.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a14]: ../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md
