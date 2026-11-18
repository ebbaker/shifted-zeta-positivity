# B05 r1 — Reconsidering BBGKY-style closure for the S/T hierarchy

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual model/effort unavailable in chat0002's
guarded registry; one helper checked the algebra and feasibility with
inherited settings, without independent serving attestation.

**Status: bounded conceptual decision, with elementary finite-head algebra
and a scoped comparison calculation. The proposed finite-divisor
approximation theorem is not yet proved here.** [Request][request] ·
[Sole register][register] · [Results][results] · [Avoid][avoid]

The author's suggestion is useful: the new hierarchy makes the closure
error explicit. The preferred next step is a finite reconstruction whose
moments come from an actual polynomial heat field, with a proved error
against the unchanged canonical field. Merely discarding higher moments
and propagating independent absolute bounds has an identifiable difficulty.
This is an approximation milestone, not an RH criterion or a signed gain.
[Classification01][classification] · [Scope07][scope] · [Joint12][joint]

## 1. What was considered before, and what is different now

The earlier [VCD discussion, §7][earlier] eliminated a Jacobi-chain tail
exactly. Its retained amplitude obeyed a Volterra memory equation. That
evolution variable was observation height, not Newman time, and the
omitted amplitudes initially vanished. The [later overview, §5][old-plan]
kept three open closure options: source-constrained tail responses,
correlated residuals, and a response approximation with controlled error.
It established neither short memory nor finite theta closure.

The new [Note09][hierarchy] evolves complete rational divisor moments in
physical Newman time. It has explicit nonlinear coupling, regularity at
mergers and geometric high-order bounds from the exterior collar. Its
omitted moments generally do **not** vanish at the initial time. It is
not a density-matrix hierarchy: the inverse quadratic zero locations are
complex, and no positive-semidefinite moment matrix or small-correlation
parameter is supplied.

The previously catalogued sources were rechecked: [Akbari et al.][akbari],
§II.2, §III and conclusion, distinguish inter-level compatibility from
stability/physical realizability of a closure; their fermionic examples
are not theta obstructions. [Chorin–Hald–Kupferman][chk], §2 (2.4)–(2.7),
retain memory and unresolved initial information in a specified projection
framework. Importing that framework for arbitrary S/T sequences would
need a phase space, flow and projection not proved by componentwise closure.
We use these as organizational guidance only. The existing
[source-use catalog][catalog] owns their bibliography; no new PDF or
external theorem is added to the repository.

## 2. The new finite-head residual is explicit

Use `s_n=ell^(2n)S_n`, `v_n=ell^(2n−1)T_n`, normalized time sigma,
`delta=D/ell²`, `m=s_1`, and `F=12s_2+16delta s_3`. Fix P≥3 and retain

    x_P=(delta,s_1,...,s_P,v_2,...,v_P).

Define the finite polynomial vector field f_P by setting moments of index
greater than P to zero **only in the formula defining the approximation**.
For the actual canonical projected head,

    x_P'=f_P(x_P)+r_P.                                    (1)

All products in the n-th hierarchy row have indices at most n. The only
omitted entries are the linear next-two-moment terms. Thus r_P vanishes
except in four rows:

    r_(s,P−1)=−4(P−1)(P+2) delta s_(P+1),
    r_(s,P)=−4P(P+2)s_(P+1)−4P(P+3)delta s_(P+2),
    r_(v,P−1)=−4(P−1)(P+2) delta v_(P+1),
    r_(v,P)=−4(P²+P−1)v_(P+1)−4P(P+3)delta v_(P+2).       (2)

This is a finite algebraic projection of the accepted canonical equations,
not an assertion that f_P's solutions realize a divisor. With
`q0=16/15`, `gamma=q0/a²<1`, the complete collar/count bounds are

    |s_n|≤B_1 L gamma^(n−1),
    |v_n|≤sqrt(q0) B_1 L gamma^(n−3/2), n≥2.

Therefore the unweighted max-norm residual has the explicit bound

    ||r_P||∞ ≤ 4P(P+3)sqrt(q0) B_1 L gamma^(P−1/2)
                 ×max{d,1+d gamma}.                       (3)

The d term is necessary: the P−1 row involves delta times the P+1
moment, without an additional gamma. The collar permits d>1.
For fixed T and collar parameters, (3) tends geometrically to zero.
This is more concrete than an unspecified closure defect.

## 3. Small boundary error is not yet a stable truncation theorem

For a finite solution y'=f_P(y), a convex box containing x_P and y gives
the standard error estimate

    ||x_P(tau)−y(tau)||∞
       ≤e^(K_P tau)e_0+epsilon_P (e^(K_P tau)−1)/K_P,       (4)

where K_P bounds the Jacobian norm and epsilon_P is (3). The box's
validity must also be checked. This gives a finite error certificate
when small, but the scalar bound has an inherent order dependence:

    |partial f_(s,P−1)/partial s_P|=4(P²−1).

Thus this absolute max-norm argument does not establish fixed-duration
convergence by combining (3) with Gronwall as P grows.

Even the obvious componentwise positive comparison has a specific
limitation. Let A_P be an entrywise nonnegative absolute-Jacobian
majorant on the box, and use the independent constant even-boundary
allowance

    rbar_(s,P)=4P(P+2)B_1 L gamma^P
                   +4P(P+3)d B_1 L gamma^(P+1).

The successive entries from s_(n+1) to s_n are exactly `4n(n+2)`;
no nonlinear term contains s_(n+1) in row n. The nonnegative matrix
exponential therefore contains the path P→P−1→...→1, with product

    product_(n=1)^(P−1) 4n(n+2)
       =4^(P−1)(P−1)!(P+1)!/2.

For zero initial error, the comparison solution
`z(tau)=integral_0^tau exp((tau−u)A_P) rbar du` consequently satisfies

    z_m(tau) ≥ (B_1 L/2)(P+2)(P+1)! (4gamma tau)^P.        (5)

This diverges for fixed tau>0 and fixed L,gamma>0. It is a lower bound
on the **chosen positive comparison allowance**, not on the actual error.
It excludes fixed-duration convergence from this independent constant
tail-box/absolute-Jacobian argument alone. It proves neither instability
of the signed truncation nor failure of compatible closures or canonical
dynamics. A shorter time step alone does not remove accumulated error
without a separately paid restart or stability argument.

The desired error consumer is concrete: if an approximation obtains
`|m−m_N|≤eta` on an interval of scaled length Sigma, then

    |log W−log W_N|≤4Sigma eta.                            (6)

The inhomogeneous cost also needs the corresponding bound for every
subinterval and retains the physical ell² factor. Forcing approximation
must pay the joint error in `12s_2+16delta s_3`. Neither consumer acquires
the target tube, initial divisor data or gap anchors.

## 4. Selected alternative: preserve a finite divisor and its heat evolution

A promising reconstruction replaces independent moment values by moments
of a single finite polynomial heat field. At the fixed tube start t0,
let P_N(t0,z) be the complete opposite-paired canonical product truncated
at modulus N, including all ties, conjugates and multiplicities, and with
normalization H(t0,0). Evolve it by the finite polynomial equation

    P_N(t0+tau,z)=exp(−tau partial_z²) P_N(t0,z).            (7)

The coefficient evolution is finite and exact. Its induced S/T moments
retain an actual divisor and the full polynomial hierarchy; higher moments
are not independently set to zero. Conjugation and merger handling remain
available. This is an approximation to the unchanged canonical target,
not a proposed replacement source or an assumption of real zeros.

There is a specific analytical route to a time-uniform error theorem:

1. The initial complete count bounds the truncated products uniformly in N
   by a common envelope `G(r)≤C exp(C(1+r)log(2+r))`. Finite near-origin
   factors and H(t0,0) must be included in its constant.
2. Let `E_N=sum_(omitted opposite pairs)|rho|^(−2)=O(log N/N)`.
   Product expansion gives the candidate global estimate
   `|H(t0,z)−P_N(t0,z)|≤G(|z|)(exp(|z|²E_N)−1)`.
3. For real tau≥0 and a standard normal variable X, the exact polynomial
   identity is `P_N(t0+tau,z)=E P_N(t0,z+i sqrt(2tau)X)`.
   The canonical source gives the same formula for H by Fubini. Its
   subquadratic growth should permit a common Gaussian majorant on bounded
   space/time sets; the finite-tail estimate can then yield a constant
   times E_N, once E_N is sufficiently small relative to the time horizon.
4. Cauchy estimates transfer spatial derivatives. The independently cleared
   canonical tube then transfers the count-two pair by Rouché; contour
   moments transfer c,D and each fixed S_n,T_n, including mergers.

These steps are the **selected proof contract**, not an accepted theorem
in this note. They extend the earlier separately initialized slice/first-jet
argument to one initialization over a common interval. An evolved global
strip for P_N need not be assumed: the observable passage uses cleared
local contours. N is the divisor cutoff, not the moment order P. Constants
may depend on the fixed height, horizon, tube clearance and retained order.
No simultaneous T→infinity or order→infinity claim is proposed.

This route uses more initial information than an arbitrary prescribed
moment head: a finite part of the actual canonical divisor and a complete
tail estimate. Acquisition must be explicit. Direct residues receive that
same information, so a computational or signed advantage is a later
question. Uniform approximation alone supplies no RH conclusion.

## 5. Controls, decision and next step

The [documented controls][controls] are screened at the same premises as
[Note13 §5][previous]. Finite polynomial controls satisfy the proposed
finite reconstruction exactly; the method must reproduce their collisions,
not exclude them. Euler translates change the canonical initial field;
weighted-square/finite-source/score/prime controls lose full theta equality
or reflection. Reflected super-Gaussians lose the order-one input; smooth
primitive controls have unpaid canonical growth/strip transfer. Atomic and
finite-profile controls lose the canonical population/profile, RH-conditional
controls retain RH and change arithmetic, changed observation kernels lose
the physical readout, and fractional profiles lose integer realization.
Static surgery supplies no canonical common-time evolution, while scalar
equilibria need not realize a divisor. Approximation and closure compatibility
do not establish a source-specific signed inequality on any of these classes.

**Decision:** BBGKY-style reconstruction is worth revisiting here, with
realizability and error propagation treated explicitly. Select (7) and its
canonical comparison as the first controlled benchmark; do not infer
success from the small residual (3) alone or import a formal memory model.
The old B03 r2 signed-estimate conclusion remains unchanged.

**Next: [E] VCD-GT-CM-E16 — Sol**, prove the fixed-height, common-interval
finite-divisor approximation with complete errors and the pair/moment/
transport transfer. The [frozen contract][e16] is ready but not executed
in this discussion. No numerical campaign is needed for this first step.

[request]: ../research-progress/handoffs/VCD-GT-CM-B05-r1.md
[register]: ../research-progress/01_VCD_GT_CM_RESEARCH_PROGRESS_20261117.md
[earlier]: ../../../brainstorm/notes/03_VCD_INDUCTION_TRUNCATION_AND_ZERO_CONTROL_20261116.md
[old-plan]: ../../../research-overview/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_OVERVIEW_20261116.md
[catalog]: ../../../references/02_INDUCTION_SOURCE_PASSAGES_20261116.md
[hierarchy]: 09_VCD_GT_CM_E10_REGULAR_ODD_EVEN_HIERARCHY_20261118.md
[previous]: 13_VCD_GT_CM_B03_JOINT_TRANSPORT_AND_SUPERZETA_20261118.md
[e16]: ../research-progress/handoffs/VCD-GT-CM-E16-r1.md
[akbari]: https://arxiv.org/html/1204.4395v1
[chk]: https://math.huji.ac.il/~razk/Publications/PDF/CHK00.pdf
[results]: ../../../../../../result-summaries/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[classification]: ../../../../../../avoid/01_restating_the_target.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
