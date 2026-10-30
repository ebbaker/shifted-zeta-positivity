# R16: mass-free feedback defect and the failed norm-only slope closure

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort
ultra**, Investigation05 **chat0038**, *Test original-alpha mass estimate*.
Parent synthesis with two read-only same-model contributing audits;
shared premises remain, no independent specialist or formal review.

**Disposition: one scoped failed replacement route, with a valid
mass-free pointwise comparison proved in-note.** Replacing R13's
`n D_h` denominator by `D_W >= 3 E0` removes the explicit inverse physical
mass from an exact identity. Completing its norm estimate does not pay
an upper bound for the original feedback: it leaves an unsigned error
budget that cannot close the selected carrier-slope bootstrap. The
source-paid slope seed also admits a genuine weighted-square collision.
No physical-mass hypothesis is removed from the accepted R10–R15 theorems.
The fixed [E08 R16 assessment][packet] is pending.

[Progress05][progress] records this single R16 test before analysis.
[Note100][n100] and the [accepted R15 continuation][accepted] authorize
this branch; [Review50][r50] accepts R15 without correction. We use
R15's independently proved preparation seed, not its downstream
attraction, error decay or global upper slope as an upstream input.
This note follows the [result index][results], [avoid index][avoid],
[target classification][a01], [control screen][controls] and
[circular-premise warning][a14].

## 1. Exact estimate, proposed replacement and consumer

The original target for replacement is [Note90][n90] (9),

    |alpha-beta| <= d1 exp(-B/4) + d2 exp(-B/2),

whose constants use both the mass-paid R10 upper alpha bound and
`n >= n_* > 0`. The proposed consumer is an a priori original-alpha
ceiling derived from the initial carrier slope, before invoking R10.
Only that route is tested. An unquantified global-alpha assertion
would restate Note28's pointwise noncollision condition; no such
assertion is counted as progress. The fixed physical scope remains
`(T,A)=(1/4,2)`; other frequencies below are controls, not an expansion
of the target domain.

Keep the complete source, unit preparation and actual common path:
\[
 q(u)=e^{u^2/4}\Phi(u),\quad u=\tfrac12\log r,\quad
 \rho=\mathbf1_{r\ge1}\frac{q(u)}{8\pi r^3},
\]
\[
 W_0=K_1*\{\rho(\cos(2u),-u\sin(2u))\},\qquad
 h_0=K_1*\{\rho(1+u^2)\},
\]
\[
 W_s=\Delta W+\alpha\operatorname{div}(vW),\quad
 h_s=\Delta h+\alpha\operatorname{div}(vh),\quad
 v=X+\frac{X}{1+|X|^2},\quad d=\operatorname{div}v\in[3,6].       \tag{1}
\]
The second equation uses the original alpha; it is not an independent
scalar feedback evolution. On every compact interval before `Smax`,
[Note28][n28] and [Note29][n29] give smooth weighted decay,
\[
 E_0=\|W\|_2^2>0,\quad G_W=\|\nabla W\|_2^2,\quad
 D_W=\int d|W|^2,\quad \alpha=2G_W/D_W,
\]
\[
 3E_0\le D_W\le6E_0,\qquad h\ge|W|,\quad M=\int h>0.        \tag{2}
\]
All spatial integrals include the entire inner ball. Define
\[
 a=\frac{\int W}{M},\quad n=|a|^2,\quad e=W-ah,\qquad
 \int e=0,\quad 0\le n\le1,
\]
\[
 E_e=\|e\|_2^2,\quad G_e=\|\nabla e\|_2^2,\quad
 D_h=\int dh^2\ge3E_0,\quad \beta=2\|\nabla h\|_2^2/D_h.     \tag{3}
\]
Only M, E0 and protected energy denominators are divided by. No
individual physical jet or vector mass is assumed positive in (1)–(3).
The conserved coefficient a is used exactly, without differentiating
it with respect to the mark.

## 2. Dependency inventory before the test

| Input | Available without a positive physical vector-mass floor? |
| --- | --- |
| E0, D_W bounds, h domination and M, finite prepared moments | Yes, on compact regular intervals. R0 includes the full +6M preparation cost. |
| `alpha >= a_*=(1/5)(6 pi² E0/M²)^(2/3)` and `R <= max(R0,3M/a_*)` | Yes, before Smax, by Note67's Fourier bound and carrier moment equation. |
| `y=g+3/4`, `y'<=7 alpha y`, g=G_W/E0 | Yes, before Smax; this does not close an alpha ceiling. |
| `41/304 <= z(0,r) <= 1/2`, z=−h_r/(b h), b=r+r/(1+r²) | Yes: complete-source and unit-preparation calculation in Note98 §2. |
| Positive moment floor `R>=c3 mu_*^(7/3) E0^(−2/3)` | No: this is R10's physical-mass payment. |
| Uniform increments of B, global alpha ceiling, R12 error decay | No: the moment floor first pays the increments and global ceiling; R12 constants then use that ceiling. |
| R13 defect decay, scalar energy E0/n, R15 global upper slope and attraction | No: the accepted dependency chain remains. |

Thus neither beta's accepted global bound nor an R12 error constant is
available to prove the first new alpha ceiling. The positive carrier
mass M and conserved spatial energy E0 are not substitutes for mu.

## 3. The denominator-safe defect and a completed mass-free envelope

Put
\[
 \Delta G=G_W-nG_h
      =2\langle\nabla W,\nabla e\rangle-G_e,\qquad
 \Delta D=D_W-nD_h
      =2\langle dW,e\rangle-\int d|e|^2.                     \tag{4}
\]
Since `2G_h=beta D_h`, direct subtraction gives
\[
 \boxed{(\alpha-\beta)D_W=2\Delta G-\beta\Delta D.}           \tag{5}
\]
Unlike Note90 (6), (5) remains valid when n=0. Its denominator is paid
by (2), without a hypothesized lower mass or attraction limit.

Let `x=G_e/E0` and `y=E_e/E0`. Cauchy–Schwarz and d<=6 give
\[
 |\Delta G|\le2\sqrt{G_WG_e}+G_e,\qquad
 |\Delta D|\le12\sqrt{E_0E_e}+6E_e.
\]
Using `G_W=alpha D_W/2<=3 alpha E0` in (5) proves
\[
 |\alpha-\beta|\le\frac4{\sqrt3}\sqrt{\alpha x}
       +\frac23x+\beta(4\sqrt y+2y).                         \tag{6}
\]
This first estimate still has alpha on its right. Completing the
quadratic in `sqrt(alpha)` removes it, with every constant retained:
\[
 \boxed{\alpha\le\mathcal F(\beta,x,y):=
  \left[\frac2{\sqrt3}\sqrt x+
   \sqrt{\beta(1+4\sqrt y+2y)+2x}\right]^2.}                 \tag{7}
\]
Indeed (6) implies `t²−(4/sqrt3)sqrt(x)t−C<=0`, where
`C=beta(1+4sqrt(y)+2y)+(2/3)x`; the nonnegative root gives (7).
This is a genuine pointwise inequality with no inverse physical mass.
It is **conditional on the actual error norms**, not their independent
uniform control. It neither supplies the R13 decay rate nor proves
smallness of those errors. Using E0/n at n=0 is unnecessary and invalid.

The missing sign can be recorded without a norm loss. For scalar or
vector f define
\[
 \mathcal Q_\beta(f)=2\|\nabla f\|_2^2-\beta\int d|f|^2.
\]
Expanding W=ah+e and using `Q_beta(h)=0` yields
\[
 \boxed{(\alpha-\beta)D_W=
 \mathcal Q_\beta(e)+2\sum_j a_j
  \left(2\langle\nabla h,\nabla e_j\rangle
                      -\beta\langle dh,e_j\rangle\right).} \tag{8}
\]
The cross term is also
`−2 sum_j a_j int e_j (2 Delta h + beta d h)`; the zero mass of e
cannot cancel a spatially variable multiplier. No sign is assigned.
At n=0, a=0 and e=W, so (8) is exactly
`(alpha−beta)D_W=2G_W−beta D_W`. The safe denominator does not turn
this identity into an independent estimate.

## 4. Finite test: the norm-only constant-ceiling bootstrap does not close

Choose any finite ceiling `L>max{alpha(0),1/2,a_*}` and work on its
first-exit interval, where alpha<=L. This is a local bootstrap
assumption, not the desired conclusion. The independently paid seed
and the linear comparison in Note98 §3, applied only on this interval,
give
\[
 m:=\min\{41/304,a_*\}>0,\qquad m\le z(s,r)\le L.
\]
No global R15 bound is being imported: finite-interval alpha bounds
pay the linear common-path estimates and comparison locally. In the
commuted equation for `xi_c=h_r/b+c h`, the forcing is
\[
 -(\alpha-c)(2cb'+\gamma)h,\qquad
 \gamma=-d'/b\ge0,\quad 7/8\le b'\le2.                     \tag{9}
\]
The upper-slope comparison with c=L works precisely because alpha<=L
on the bootstrap interval. This is the dependence that must be closed.
Local H1 estimates and the finite-window bound for h²+|grad h|² pay
boundedness of xi; the R5 radial comparison device in Note98 handles
the origin and infinity without dividing by h there. Integrating the
slope bounds gives Gaussian tails and justifies
\[
 \beta=\frac{\int z^2|v|^2h^2}{\int z|v|^2h^2}\le L.       \tag{10}
\]

For completeness even the error norms in this bootstrap can be paid
without mu, though the payment depends on L. Let
\[
 \ell=2M,\quad c_G=(8\pi)^{-3/2},\quad
 c_N=\tfrac35(6\pi^2)^{2/3},\quad\nu=21/4,
\]
\[
 D_L=\max\{c_G,(3L/c_N)^{3/2}\},\quad
 r_L=\frac{5L+\sqrt{25L^2+2\nu L}}2,\quad
 H_L=D_L\max\{3/4,r_L\}.                                    \tag{11}
\]
The raw error is `Wraw−a hraw`, so its vector L1 norm is <=2M.
Positive common-path propagation gives `||e(s)||1<=ell`. Gaussian
preparation gives `E_e(0)<=c_G ell²`, `G_e(0)<=3c_G ell²/4`.
The Fourier/Nash inequality and the radial production identity, summed
over the two components, give on the same interval
\[
 E_e'\le-2c_NE_e^{5/3}\ell^{-4/3}+6LE_e,
\]
\[
 G_e'\le-2G_e^2/(\ell^2D_L)+10LG_e+\nu L\ell^2D_L.
\]
These are precisely Note82's local barrier calculations; neither their
use here nor their vector sum invokes R12 decay. Scalar comparison yields
\[
 E_e\le\ell^2D_L,\qquad G_e\le\ell^2H_L.                    \tag{12}
\]
The finite-interval carrier H1 bounds needed for the slope comparison
follow by the same calculation with ell=M. Thus the argument has not
assumed that comparison's regularity for free.

Set `x_L=ell² H_L/E0>0`, `y_L=ell² D_L/E0>0`. Formula (7) is increasing
in all its nonnegative arguments, so the available closure is
\[
 \alpha\le\mathcal F(L,x_L,y_L).
\]
But for every finite positive L,
\[
 \boxed{\mathcal F(L,x_L,y_L)>L.}                             \tag{13}
\]
The inner radical already exceeds sqrt(L), and the added square-root
term is positive. Thus **this specified unsigned norm/barrier estimate
never improves its assumed ceiling**. This is one symbolic test for
the closure, not a numerical scan or proof that actual alpha exceeds L.
Even inserting R12's decaying errors would be circular here; moreover,
a positive additive allowance above beta<=L is not itself an invariant
upper barrier. A separately paid gap between beta and L, or a suitable
signed estimate in (8), would be additional information, not a consequence
of (13). No such alternative route is tested in R16.

## 5. A genuine control shares the seed and protected denominator

Use the registered [three-positive-square source][square], with its fixed
positive weights and certified double event
\[
 T=1/4,\qquad A_*\in(44.1303,44.1304),\qquad
 H_{\mathbf w}(T,A_*)=H_{\mathbf w,A}(T,A_*)=0.
\]
Its event certificate is inherited, not numerically replayed here.
It is a different source from canonical theta; it has the **same carrier
construction**, not a numerically identical canonical carrier.

Every positive weighted summand has the logarithmic derivative in
Note98 (9). Its positive weighted average therefore retains
\[
 R(\log f)'\le-\tfrac{19}{8}R^2.
\]
The finite sum pays all derivative/tail interchanges. Note98 §2's
projection, tail-excess and unit-Gaussian integration steps then give
exactly `41/304<=z(0,r)<=1/2`. The projection traces at ±1 still cancel;
the inner ball remains. This seed uses no physical A. For this one
weighted source its h0 at A=2 and at A=A_* is literally the same function.

For every A, `|(cos(Au),−u sin(Au))|<=1+u²`; hence h0>=|W0|.
All raw spatial moments are finite, and K1 gives nonzero radial Schwartz
W0 with E0>0. Nonzeroness follows from the nonzero raw first component
near r=1 and injectivity of Gaussian convolution. The physical source's
even extension is only C2; full reflection in u is not required by this
exterior-source preparation or the imported local R3 theorem.

At its certified event the vector mass is zero. Therefore Note28's
actual conservative-feedback theorem gives finite Smax, with
`B(s)->infinity` and `alpha(s)->infinity`. It shares (2), the seed,
local comparison and all denominator-safe identities above. It fails
unit theta coefficients and full source reflection, neither of which
was used as a discriminator in this seed/norm route. Its event is not
a finite all-real threshold; the auxiliary deadline needs only zero
vector mass and does not require such a threshold.

Consequently a theorem claiming global alpha control **only from these
shared qualitative seed/domination/energy/local-flow premises** would
be false on their admitted class. A new numerical smallness condition,
frequency-sensitive signed estimate or full-coefficient constraint is
outside this exclusion. The actual A=2 theta path is not a counterexample:
Note67 already pays its positive mass, and positive weighted squares
also obey that sufficient low-mark payment. No event at A=2 is asserted.

## 6. Other controls, fair comparison and retained costs

| Control | Exact R16 premise check or limitation |
| --- | --- |
| Gaussian-polynomial cosine | Shares the local prepared flow and zero-mass divergence at 2sqrt(6); its particular R15 slope constants are not established here. |
| R6 polynomial observation kernels | Fail literal cosine; their polynomial jets need not be dominated by this hraw. Same theta amplitude alone does not put them in the full R16 class. |
| Finite-prime orbit | Positive square-source realizations share the per-summand seed at T=1/4 when their recorded tail hypotheses apply. Keep their high-gap events, fixed multipliers and failed full reflection; no same-mark event is inferred. |
| Reflected super-Gaussian | Fails square-source representation; exact event/reflection facts remain. No matching seed constants are claimed. |
| Smooth shape / positive primitive | Retain analytic damping and time-domain qualifications. Their particular seed is untested; primitive positivity supplies no signed estimate in (8). |
| Euler-factor, all p | Shifted source/conductor, no R16 seed evaluation. A negative Laguerre witness is not a double event and does not set mu=0. |
| Atomic/profile / continuous compact | Atomic sources lie outside the inherited source-function theorem; verify any prepared extension separately. No seed or regularity extension is assumed. |
| RH-conditional endpoint | Preserve RH conditionality and escaping double heights; no unconditional or A=2 event. |
| Earlier q and q_(T,a) controls | Preserve their positive-source/threshold statements; check the prepared class before using Note28, and do not invent matching seed constants. |
| SUSY smooth-density / two-channel | These address other Weil forms and factorizations, not an instantiated R16 auxiliary path. No fabricated CTF premise failure is assigned. |

These checks follow the [collision register][controls], [older heat-flow
controls][old-controls] and [form obstructions][form-controls]. A missing
canonical identity is not by itself proof that a derived bound separates
a control; the weighted-square example explicitly retains this bound.

The equally informed direct comparator gets (5)–(13) and the same failed
closure. No primitive-specific or acquisition advantage is demonstrated.
The unchanged source, vector feedback, actual forcing, genuine residual,
raw/prepared mismatch, full source commutators, sphere cancellation and
entire inner ball remain. This test did not use residual bounds to pay
(8); it did not set the residual or forcing to zero. The forcing
`(alpha−beta) div(vh)` is still actual and its coefficient remains unpaid
for this upstream consumer.

## 7. Decision and next boundary

**The denominator replacement succeeds as algebra; the selected
norm-only carrier-slope closure fails.** It removes no physical-mass
premise from R10's global estimate, R12 synchronization, R13 defect decay
or R15 attraction. It does identify the full signed quantity (8) that
this particular route would still need to control. Merely declaring
that quantity small would restate the missing bound.

This is a bounded negative return, not a universal impossibility theorem
for the unchanged theta source. No new parameter family, numerical
acquisition, PDE evolution, independent scalar path or manuscript change
was made. **Next: [E] CTF-E08 R16 — Sol**, the fixed seven-obligation
assessment. No E07 execution is issued because no closing source estimate
has been selected. Parent B02 remains partial; E03/B03 remain gated;
E05 integration needs a separate scope. [Continuation102][next] includes
the model-change and research guidance.

All new calculations above are elementary algebra and inherited local
barrier arguments, with no new convergence theorem or novelty claim.
The inherited Fourier normalization was checked against
[DLMF 1.14.8](https://dlmf.nist.gov/1.14.E8); its unitary convention gives
(2pi)^(-3) for the unnormalized three-dimensional forward transform.
The checked classical-input scope remains [Reference11][refs].

[n28]: 28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md
[n29]: 29_POSITIVE_CARRIER_COMPARISON_AND_QUANTITATIVE_REGULARITY_20261028.md
[n67]: 67_UNIFORM_FEEDBACK_DIRECT_COMPARISON_B02_R10_20261029.md
[n82]: 82_COMMON_CARRIER_SYNCHRONIZATION_R12_20261029.md
[n90]: 90_CARRIER_FEEDBACK_DEFECT_AND_STATIONARY_CANDIDATE_R13_20261029.md
[n98]: 98_RADIAL_LOG_SLOPE_ATTRACTION_B02_R15_20261029.md
[n100]: 100_NEXT_ASTRA_HANDOFF_AFTER_RADIAL_ATTRACTION_20261029.md
[accepted]: CTF_E08_R15_ASSESSMENT_AND_MODEL_CONTINUATION_20261029.md
[r50]: ../reviews/50_RADIAL_LOG_SLOPE_ATTRACTION_E08_R15_ASSESSMENT_20261029.md
[progress]: ../research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md
[packet]: ../research-progress/handoffs/CTF-E08_MASS_FREE_FEEDBACK_CLOSURE_ASSESSMENT_R16_20261029.md
[next]: 102_MASS_DEPENDENCY_DECISION_AND_MODEL_CONTINUATION_R16_20261029.md
[square]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/05_control_families/01_SQUARE_SUPPORT_ENDPOINT_COLLISION_OBSTRUCTION_20261015.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[old-controls]: ../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[form-controls]: ../../../../result-summaries/04_positive_constructions_and_scoped_obstructions.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a14]: ../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md
[refs]: ../references/11_CONSERVATIVE_FEEDBACK_AND_DIFFUSION_CONTRACTION_20261028.md
