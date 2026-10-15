# Review of the connection bridge and inner turning profile

15 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**, verified from the coordinating session. Collaborating derivations inherited that configuration. This is internal LLM-assisted comparison, not external refereeing or formal verification.

## Disposition

The three continuation notes pass the analytic and exact-algebra checks described below. They establish a classification of base-only ASD metric changes, a physical-path normalization and restriction result, complete signed transform identities, and an all-multiplicity local angular profile. They do not establish the theta-specific inequality required for collision exclusion.

The existing manuscript's quarter-turn and stationary-predecessor proofs pass review. Its displayed ASD metric and curvature are correct. The new adapted metric changes the interpretation of its cusp growth: the growth is a property of that particular metric, not an invariant consequence of ASD curvature.

## Analytic checks

| Claim | Review result and boundary of the claim |
| --- | --- |
| ASD base-metric classification | Direct differentiation gives `F_b=−2*pi*i dr wedge ds+(i/2)Delta(b) dp wedge dq`. The declared Hodge star makes ASD equivalent to `Delta(b)=4*pi*q`. Harmonic conjugation on the simply connected upper half-plane gives the full base-only class. No classification of all total-space ASD connections is claimed |
| Adapted metric | The holomorphic cubic `g=−pi*i*tau³/3` gives `h_tilde=exp(2*pi*p²*q)h`. Its curvature and vertical operator agree with the original ASD representative, while its path norm is one and its connection vanishes. The isometry multiplies sections by `exp(g)`; fixing the arithmetic section while changing its metric is correctly distinguished from this transport |
| Cusp integrability | The leading `n=1` term gives the stated source asymptotic. Its adapted norm is integrable against both `du` and induced path length, with fixed polynomial and compact-time heat weights. The original norm diverges. Infinite ambient action and lack of modular descent remain |
| Flat restrictions | The external product has curvature equal to the sum of the two pulled-back curvatures, each zero. The conclusion concerns tangential derivatives on this product only. Transverse curvature and global boundary conditions are not ruled out |
| Complete signed kernels | Both branches' cosine factors, signs and factor `1/4` check by direct symmetrization and independently through the full-line change of variables. The covariant source insertion has factor `1/(256*pi^4)`. The energy kernel retains `H²+H_x²` |
| Primitive transfer | Two integrations by parts retain `−psi'(0)f(0)+psi(0)f'(0)`. Separate evenness eliminates the latter term. Branch 0 retains `−I_2/2`, branch 1 has no edge term, and energy retains both `I_0` and corner `1/4`. All upper limits vanish for the convergent primitive with the declared weights |
| Transverse commutators | The chart-local vector field is specified before restriction. `[N_b,D^k]` retains `−k(k−1)(pi/q)D^(k−2)` at the zero section. A base-only correction commutes with the vertical operator. No global horizontal-field assertion is made |
| Jet recurrence and source derivatives | Independently derived using the covariant-jet generating function and direct commutator transport. The displayed `Phi'` and `Phi''` agree with direct differentiation of an arbitrary paired lattice mode, including constant-mode cancellation |
| Inner angular profile | Analytic heat Taylor counting after `x=chi(s)+s*xi` gives all three leading jets with differentiable errors uniform on each fixed compact `xi` interval. The fixed sign of `W` controls the lift. The Cauchy profile is positive there for small `s` |
| Turning mass and conditional targets | The pi mass is an iterated finite-window limit; no unproved uniform tail or weak-measure limit is asserted. The larger parabolic interval gives net turning via endpoints without a pointwise positivity claim. Strict quarter-turn-gap and positive-part integrability criteria remain conditional |
| Odd-branch denominator | `H=O(s^(r+1))` throughout a fixed inner window while `h_1` and `h_2` both contribute at order `s^r`. Therefore `E_1^jet/E -> 1+r²*xi²`, agreeing with the central comparison but preventing an unjustified whole-window identification |

Three subtasks developed the geometry, signed correlation, and turning analysis separately. The coordinator checked all formulas; the turning reviewer independently checked the correlation and geometry notes and replayed their checker. The geometry reviewer checked the turning argument and its checker. Three minor issues found before delivery were repaired: the branch-1 jet norm was explicitly distinguished from physical energy, a differential in the displayed edge integral was corrected, and the profile width was specified as a half-width at half maximum. These changes did not alter the derived identities.

## Exact replay

The [manifest](../numerics/CONNECTION_BRIDGE_AND_INNER_TURNING_CHECKS_20261015.json) records source and output hashes. All seven scripts complete successfully using the Python standard library.

| Group | Assertions | Scope |
| --- | ---: | --- |
| Four unchanged initial checkers | 344 | Existing manifold, finite parabolic-profile, Chern and ASD algebra |
| [Adapted metric checker](../numerics/check_asd_path_metric.py) | 35 | Base potentials, holomorphic difference, path normalization and external curvature restriction |
| [Signed bridge checker](../numerics/check_theta_signed_bridge.py) | 59 | Exact phase kernels, heat-retaining transfers, primitive endpoints, finite jet recurrence, arbitrary paired-lattice-mode source derivatives |
| [Inner profile checker](../numerics/check_inner_turning_profile.py) | 792 | 72 finite heat-polynomial cases, both parity branches, `r=1,...,12`, asymmetric and negative-amplitude germs, stationary-center coefficients and leading numerator/denominator |

The total of 1,230 includes overlapping assertions. Finite checks do not prove the analytic all-order limits or infinite theta convergence; those are justified in the notes. No interval arithmetic, new theta sign calculation, or global collision-exclusion premise was verified. The stable manuscript and its compiled artifacts were not edited or rebuilt.

## Remaining mathematical obligation

Produce a complete-theta estimate for the signed physical observation with coefficients locally bounded through every candidate event, or an adequate uniform angular gap with both branch denominators handled correctly. Any transverse or global geometric proposal must show how its arithmetic data reaches that observation and must retain its endpoint and cancellation costs.

The [continuation handoff](../notes/00_research_coordination/02_CONNECTION_BRIDGE_AND_INNER_TURNING_CONTINUATION_20261015.md) states the exact target and next gate.
