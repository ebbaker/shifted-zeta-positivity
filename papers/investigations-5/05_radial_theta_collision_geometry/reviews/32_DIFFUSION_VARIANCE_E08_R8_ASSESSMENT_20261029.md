# CTF-E08 R8: diffusion-variance proof, costs and scope assessment

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**, Investigation05 **chat0029**, **Assess CTF-E08 R8 Sol**.

**Verdict: accepted without mathematical correction at the fixed mark
(T,A)=(1/4,2), within the inherited prepared radial solution class.**
All eight checks of the [issued packet][packet] pass. [Note59][n59] is
proved in-note and now separately assessed; [Self-assessment31][r31]
remains its author's check. This is a generic finite-horizon compression
improvement. It pays no collision deadline or new physical domain.

## 1. Initial variance and full-source preparation

Ordered spatial derivative tensors have Fourier norm |xi|^(2j), so
H2=||nabla^2 W||2^2=||Delta W||2^2=N. With the stated unnormalized
Fourier convention, Note59(5) is exactly
\[
\nu_0=\operatorname{Var}_{\mu_0}(|\xi|^2)
 =\frac12\iint(|\xi|^2-|\zeta|^2)^2d\mu_0(\xi)d\mu_0(\zeta)>0.
\]
For nonzero H2 data, mu0 has an absolutely continuous probability
density. Zero variance would put that density on one sphere, which has
Lebesgue measure zero. Also g0>0: a zero-gradient L2 field is zero.
Neither argument uses a physical first-jet margin or nonzero mass.

[Note40][n40], Section 1, supplies all weighted raw moments, Schwartz
regularity after unit Gaussian preparation, and nonvanishing by heat
injectivity. Its full theta tail, raw cosine and first derivative are
unchanged. The **initial variance fact** holds for nonzero H2 fields;
the **whole lifespan theorem** is used only in Note28's prepared radial
Schwartz/finite-moment class. No extension of that theorem to arbitrary
H2 or H3 data is inferred.

## 2. Initial costs and Gaussian constants

The spherical Jacobian is rho(X)dX=q(u)du. The raw vector norm is bounded
by q(u)(1+u^2), so its L1 norm is at most mfrak=M0+M2, with no extra
component factor. Tensor Young and direct Gaussian integration give
\[
\|\nabla^jK_1\|_2^2=(8\pi)^{-3/2}\frac{(3/2)_j}{2^j},
\quad (c_0,c_1,c_2,c_3)=(1,3/4,15/16,105/64).
\]
Their sum is 277/64, proving Note59(6). Exact S3, or its displayed upper
budget with K replaced consistently, pays every initial derivative cost.
A rigorous positive lower bound for nu0 can replace nu0 throughout the
construction: h<=lower_nu/(2M) still gives nu>=lower_nu/2, and the
restart saves lower_nu*h. No numerical nu0, h or lifespan gain was
acquired. Strict positivity of an exact integral is not a numerical
lower-bound certificate.

## 3. All-radius tensors and C3

For f=(1+r^2)^(-1), singleton/pair partitions give exactly the majorants
F=(1,2,12,96,1056). Differentiating Xf costs F_m+2mF_(m-1), since the
identity tensor has Frobenius norm sqrt3<=2; the linear X adds2 at m=1.
Thus V=(6,20,168,1824). Tracing costs at most sqrt3<=2, giving
D=(40,336,3648). These are conservative whole-space bounds.

The ordered Leibniz remainder in Note59(8) has all binomial terms and
only derivative orders at most3. Hilbert tensor contraction introduces
no missing dimension factor. Spatial derivatives never differentiate
alpha. In the leading energy term, integration of 2v dot nabla removes
one of the two d terms; the resulting coefficient is d<=6.
Using sum_(k=m)^3 binom(k,m)=binom(4,m+1) gives
\[
\mathcal H'\le C_3\alpha\mathcal H,\qquad
C_3=6+12(46)+8(356)+2(3816)=11038.
\]
The H3 identity has nonpositive order-four dissipation, which is
discarded. Smooth preparation justifies that identity; an initial H4
norm is not required in the budget.

## 4. Paid short-time persistence

Because 0<1-2^(-7/C3)<1, h0 is strictly inside L(g0). Substitution gives
delta(h0)=2^(-7/C3), so Note42's established interior estimate pays
B(h0)<=log2/C3. Therefore mathcal H/E0<=K=2S3 on the **closed** [0,h0].
There is no use of the new endpoint estimate to establish this bootstrap.

The full Laplacian commutator is Note59(12), including Delta v+2nabla d
and Delta d. Whole-space Plancherel gives H3=||nabla Delta W||2^2. With
||Dv||<=6, ||Delta v||<=40, ||nabla d||<=40 and |Delta d|<=30, it yields
\[
|g'|\le22K+\frac{20}{3}K^2,\qquad
|n'|\le2K+\alpha(30n+240\sqrt{ng}+60\sqrt n)
       \le2K+220K^2.
\]
Consequently
\[
|\nu'|\le M=2K+264K^2+\frac{40}{3}K^3.
\]
Here K>=2 validates the replacements of square roots by K. The cap
h<=nu0/(2M) proves nu>=nu0/2 precisely on [0,h]; no later variance floor
is assumed.

## 5. Signed restart, exact endpoint and continuation

Discarding only Note42's nonnegative radial remainder before using
alpha<=2g/3 gives
\[
g'\le ag^2+bg-2\nu,\qquad a=14/3,\quad b=7/2.
\]
On [0,h], comparison with y'=ay^2+by gives y>=g and
(y-g)'>=nu0, hence g(h)<=g1=yh-epsilon. The cap
h<=g0/(2nu0) gives g1>=g0/2>0 and 0<eta=epsilon/yh<=1/2.

Here is the endpoint algebra for **all** permitted data, independently
of the illustrative rational checks. Put c=a/b=4/3 and E=exp(bh):
\[
e^{b(L(g_0)-h)}-1
=\frac{1+1/(cg_0)-E}{E}
=\frac{\delta(h)}{cg_0E}=\frac1{cy_h}.
\]
Thus delta1(L(g0)-h)=1-g1/yh=eta>0. Also h+L(yh)=L(g0), and
L'(x)=-1/(ax^2+bx), so
\[
L_{\rm new}-S_{\rm tar}=L(g_1)-L(y_h)>0.
\]
The restarted comparison bounds G at any hypothetical maximal endpoint
strictly before L_new, contradicting [Note28][n28], Section 5. Therefore
Smax>=L_new. The target S_tar is strictly inside the actual lifespan;
existence at L_new itself is not asserted.

Since (2/3)/a=1/7, integration of the two scalar comparisons gives
\[
B(S_{\rm tar})\le B_*=-\frac17\log[\delta(h)\eta]<\infty.
\]
Note59(17)'s increasing-branch maximum bar_g bounds G<=E0 bar_g and
alpha<=(2/3)bar_g on the entire closed target interval. The lower
feedback bound alpha>=G/(3E0) proves integral G<=3E0 B*. These are
complete initial-data expressions, with no unknown exp(cB) as input.

## 6. Weighted residual, true jets and boundaries

Let zeta=delta(h)eta in (0,1). Substituting the independent B bound into
[Note47][n47], equation (21), without adding its dissipation to the gradient identity,
gives uniformly for 0<=s<=S_tar
\[
\mathcal F(s)+E_0+\int_0^s(\mathscr D+\alpha\mathscr H_{\rm rad})
\le(\mathcal F(0)+E_0)e^{\kappa_0S_{\rm tar}}
                    \zeta^{-\kappa_{1,\rm src}/7},
\]
where kappa0=8+A2^2+A1+A0 and kappa1,src=274/25+B1+B0 retain their full
source/cutoff definitions. Multiplying the integrated inequality by its
final integrating factor is legitimate: its exponent is nondecreasing,
so all resulting dissipation weights are at least one.

Also Q<=Q0 zeta^(-6/7). Both branches of the accepted R7 minimum are
increasing in X, so X*=Q0 zeta^(-6/7) may be substituted into that minimum
and its optional Theta allowance. On a ball of radius Rb the unweighted
residual squared norm is at most (1+Rb^2)^4Y. No unweighted whole-space
residual estimate is claimed.

The true second jet remains -P_s^p K1*(u^2 F0), with multiplication
before preparation and the feedback mark fixed. The initial residual is
the nonzero preparation commutator. Both complete source commutators,
including -Delta c_T and b_T dot nabla d-v dot nabla c_T, and every cutoff
derivative remain. At r=1 only the combined numerator Theta+R cancels;
separate singular quotients are not bounded. The whole inner ball is in
every energy. Note47's r=2 split partitions a volume integral and adds
no flux. Inherited weighted decay pays distant boundaries. No diffusion
is spent twice in a single estimate.

## 7. Matched comparison and useful scope

With the same E0,G0, Note42's displayed allowance becomes singular at
S_tar. R8 is finite there, at the added cost of initial variance and H3
payment; this is an actual complete-bound gain. Equally informed direct
energy analysis can retain the same variance. No acquisition advantage
or optimality follows.

At this theta mark [Note55][n55], equation (19), already gives
mu=|(H,H_a)|>=-H_a>=35M2/18>0. With
r*=c3(35M2/18)^(7/3)E0^(-2/3), [Note29][n29], equation (13), yields
\[
B(S)\le\frac12\log(R_0/r_*)+3(M_0+M_2)S/r_*
\]
on every finite horizon, and bounded G gives continuation. Its carrier
moment R0 is already paid there. This alternative is stronger in horizon
scope; no numerical cost ranking of the two bounds is established.
R8 does not consume that physical margin and creates no new physical
collision-free region. Small variance or large derivative budgets can
make its strict gain tiny.

## 8. Registered controls and stopping boundary

| Control | Actual shared or failed premise and domain |
| --- | --- |
| Gaussian-polynomial cosine | Nonzero radial prepared Schwartz data share variance and H3, including at the true event (1/4,2sqrt6). Theta arithmetic fails but is unused in this generic lemma. |
| R6 polynomial kernels | Full cosine/Newman compatibility fails; their admitted prepared fields share the spatial estimate. No physical theta event follows. |
| Weighted-square | Unit coefficients/full reflection fail; prepared fields share the lemma. Events near44.13 and83.53 stay outside this mark. |
| Finite-prime orbit | Full reflection/canonical source fails. Admitted smooth finite-moment fields share the lemma; high-gap locations retain their qualifications. |
| Reflected super-Gaussian | Full square arithmetic fails; admitted preparation shares the lemma. Its pi/4 event is elsewhere. |
| Smooth shape / positive primitive | Those properties do not identify theta; on the inherited finite-spatial-moment domain the diffusion premises are shared. No event is newly located at A=2. |
| Euler-factor | Modified arithmetic/conductor fails the canonical identity; admitted preparation shares the lemma. A Laguerre witness is not automatically a double event here. |
| Atomic/profile / continuous compact | Atoms remain outside the imported source-function theorem; admitted continuous compact preparation shares the bound. No atomic extension is made. |
| RH-conditional endpoint | Retain RH, altered arithmetic and escaping heights. Within the admitted preparation class there is no new failed diffusion premise. |

For a control tested with the theta operator, its initial residual includes
both the preparation commutator and raw source mismatch, as Note40(23)
requires. For an admitted zero-mass control, the two existing theorems
imply L_new<=S*; this is a consistency consequence, not a new measurement
or a bound through S*. Positive restart increments can have a finite sum.
No global iteration theorem, arithmetic separator, or universal obstruction
to further signed/diffusive methods is proved.

## Evidence, provenance and disposition

All **16** frozen input hashes match at intake and final recheck; both TeX
sources retain their issued bytes. The packet itself retains SHA-256
`6e6b7cadb937889e3fb149b63e6a303422fff403465ac8411c96eb9f26014ebb`.
The [constant script][check] was replayed without --write-record; its
output exactly matches the frozen JSON. Its three rational endpoint
examples are arithmetic checks, not the all-parameter proof above or a
source certificate. No acquisition, PDE computation, mark extension,
new candidate, manuscript edit or build occurred.

Three read-only **gpt-6.1-sol / ultra** contributing-agent audits covered
costs, restart and downstream/control scope; the parent rechecked and
owns this verdict. This is separate-chat, different-model internal
assessment of Astra/max's R8, with shared inherited premises including
Sol's Note40 and Notes28/42/47. It is not specialist or formal independence.

**E08 R8 complete; B02 remains partial; E03/B03 remain gated.**
[Return61][return] records the accepted result and [Continuation62][next]
gives the next B decision and model/history handoff. The [result index][results],
[spatial-flow cluster][spatial], [control screen][controls], [avoid index][avoid],
[target classification][a01], [scoped conclusions][a07] and
[quantitative utility][a20] retain their stated limits.

[packet]: ../research-progress/handoffs/CTF-E08_DIFFUSION_VARIANCE_ASSESSMENT_REQUEST_R8_20261029.md
[n59]: ../notes/59_DIFFUSION_VARIANCE_COMPRESSION_BOUND_B02_R8_20261029.md
[r31]: 31_DIFFUSION_VARIANCE_B02_R8_SELF_ASSESSMENT_20261029.md
[n28]: ../notes/28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md
[n29]: ../notes/29_POSITIVE_CARRIER_COMPARISON_AND_QUANTITATIVE_REGULARITY_20261028.md
[n40]: ../notes/40_WEIGHTED_RESIDUAL_CLOSURE_E07_R1_RETURN_20261029.md
[n47]: ../notes/47_EXTERIOR_SOURCE_RESIDUAL_COUPLING_B02_R5_20261029.md
[n55]: ../notes/55_COSINE_JET_CORRELATION_B02_R7_20261029.md
[check]: ../numerics/25_check_diffusion_variance_constants_20261029.py
[return]: ../notes/61_DIFFUSION_VARIANCE_E08_R8_RESEARCH_RETURN_20261029.md
[next]: ../notes/62_COMPRESSION_HORIZON_AND_MODEL_CONTINUATION_20261029.md
[results]: ../../../../result-summaries/README.md
[spatial]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a20]: ../../../../avoid/20_volume_without_a_gain.md
