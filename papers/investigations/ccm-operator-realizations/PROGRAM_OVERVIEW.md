# CCM operator realizations: program overview

Date: 28 September 2026. Status: round 9 completed; bounded endpoint-energy route obstructed, one-sided threshold inequality still open.

Drafted for Edward Baker with LLM assistance. Model: GPT-6 (Codex); the exact model variant and reasoning-effort setting are not exposed in this session. This document summarizes the research record and current priority. The linked round-6 through round-9 notes supply residual, restricted selection, complement, weighted-gap, whole-line spectral, and endpoint-energy obstruction results; no true-ground overlap lower bound, RH proof, or determinant-limit theorem is claimed. This is not independent peer review.

**Resume here:** [round-9 findings and decision](notes/CCM_THRESHOLD_ENERGY_OBSTRUCTION_20260928.md) and [sequential review](reviews/CCM_THRESHOLD_ENERGY_REVIEW_20260928.md). The bounded endpoint-operator route in the bare archimedean energy norm is suspended: even after exact ground removal its signed operator is unbounded below. Further work needs a one-sided signed estimate or a new comparison after physical threshold compression. Sonin residuals remain deferred.

**Saved baseline:** `8eaabbf5ab409422827013b6bc83ad0c1bbb92bc` contains the completed research through round 8. Round 9 and the preceding handoff refresh are uncommitted working-tree additions after that baseline; inspect the actual checkout before continuing and preserve later work.

## Purpose and present assessment

The investigation seeks a realization of the Connes–Consani–Moscovici (CCM) spectral construction that makes its limiting behavior easier to prove. The eventual target is convergence of appropriately normalized spectral functions to the Riemann Xi function as the support grows. Finite self-adjointness and agreement with selected zeros do not establish that target.

The early work developed finite realizations and the removal of the Fourier cutoff at fixed support. It produced useful identities, a conditional determinant limit, and a certified infinite Fourier-tail bound at one support length. The latest round adds unconditional whole-line tail control for the weighted jump operator. This does not identify the limiting CCM determinant or supply a uniform inverse-moment bound for it.

The [bounded audit](notes/CCM_INFINITE_L_BOUNDED_AUDIT_20260926.md) is complete. Its round-5 decision was to change approach to the arithmetic ground-state comparison and suspend automatic enlargement of the fixed-support certificate. Rounds 6–8 developed that investigation into the current weighted threshold-index target. The proposed 4096-mode Schur certificate remains a local question; the audit proves why merely improving its gap input cannot repair the existing support-dependent trace estimate.

The [ground-selection continuation](notes/CCM_GROUND_SELECTION_TARGET_20260928.md) now constructs unconditional arithmetic approximate-null vectors and proves why they do not select the ground state. A weaker sufficient target for RH is available: the bottom even spectral projection of the truncated Xi kernel must have norm that dominates its known operator residual. This avoids needing full profile convergence for the RH implication, but the needed overlap lower bound is unproved. Identification of the CCM determinant still requires stronger control. A bounded diagnostic favors resolving the weak even cluster rather than dividing a full residual norm by the second-even separation.

The [round-7 continuation](notes/CCM_BOUNDARY_SELECTION_AND_COMPLEMENT_20260928.md) now proves selection toward Xi within the two-profile derivative space and eventual positivity at every fixed derivative rank. Its complement analysis proves that fixed-support derivative spaces form a core, while fixed-rank growing-support energies always tend to zero unconditionally. A uniform joint limit is essential. The new exact weighted-jump formulation supplies a sharp alternative inequality, including the obstruction that every fixed finite-prime truncation has gap zero. These are concrete advances in identifying and testing the missing estimate, not a proof of that estimate.

The [round-8 continuation](notes/CCM_WEIGHTED_TAIL_AND_DISCRETE_OBSTRUCTION_20260928.md) now proves the full weighted exterior threshold and identifies 1/4 as the essential spectral lower edge. Any additional spectrum below it consists of discrete eigenvalues. Exact pole cancellation gives superexponential exterior bounds without PNT, while a separate prime-return argument explains the arithmetic mechanism. The remaining sharp inequality becomes a compact eigenvalue-count problem at every fixed distance below 1/4, with uniform control as that distance tends to zero still missing.

The [round-9 investigation](notes/CCM_THRESHOLD_ENERGY_OBSTRUCTION_20260928.md) now proves a structural obstruction to bounded endpoint normalization. The exact threshold profiles are dense in the bare archimedean energy completion; as a result, the ground-reduced Birman–Schwinger family diverges on its negative side, every fixed prime tail has unbounded absolute relative error, and physical projection off the known threshold span is unbounded in that energy norm. These results do not obstruct the desired one-sided upper bound or establish RH. They identify a specific route to suspend and the signed input needed to change approach.

## Parameters and the two limits

Write \(X=\lambda^2\), \(L=\log X=2\log\lambda\), and \(d_n=2\pi n/L\). The Weil form is restricted to an interval of logarithmic length L; its arithmetic sum includes prime powers up to \(e^L\). N is the Fourier truncation parameter.

| Passage | What changes | Current position |
|---|---|---|
| \(N\to\infty\), fixed L | Resolve all Fourier modes on the same interval | Trace-class integrated mass and its approximation are established; determinant convergence has an unproved odd-gap hypothesis |
| \(L\to\infty\) | Enlarge support and include more prime powers | No uniform trace estimate or Xi identification has been established |
| Joint sequence \((L_j,N_j)\to(\infty,\infty)\) | Both effects | The free-tail contribution is understood under specified scaling; the arithmetic determinant remains uncontrolled |

The round-4 phrase “infinite tail” means infinitely many Fourier modes at \(L=\log13\). It does not mean infinite support.

## What the program has established

The finite construction assumes the full Weil matrix has a simple even least eigenvector with nonzero boundary functional, as specified in the source notes. Statements about the CCM interpretation retain these hypotheses.

| Result | Status and practical limit | Record |
|---|---|---|
| Metric transport and a chiral Hermitian realization | Exact finite algebra under the stated assumptions; does not determine the absolute Weil ground-energy sign | [Founding note](notes/CCM_SPECTRAL_OPERATORS_AND_CHIRAL_REALIZATION_20260926.md) |
| Positive mass–stiffness pair and spectral determinant | Exact finite identities; isolates a trace quantity that controls entire-function growth | [Boundary mechanics](notes/CCM_BOUNDARY_MECHANICS_AND_DETERMINANT_CONTROL_20260926.md) |
| Positive point-mass string and graph Dirac realization | Exact finite realization; coordinates depend on the cutoff and chosen port | [String continuation](notes/CCM_STRINGS_GRAPH_DIRAC_AND_CUTOFF_OBSTRUCTIONS_20260926.md) |
| Integrated mass is trace class at each fixed L; finite masses converge in trace norm | Analytic deductions from the stated Weil-form facts; bounds depend on L | [Fixed-support continuation, Sections 5–6](notes/CCM_ENERGY_PORTS_AND_FIXED_SUPPORT_LIMIT_20260926.md#5-the-integrated-mass-is-trace-class-at-fixed-support) |
| Fixed-support inverse dynamics and determinant convergence | Conditional on a positive continuum odd gap; that gap remains unproved | [Fixed-support continuation](notes/CCM_ENERGY_PORTS_AND_FIXED_SUPPORT_LIMIT_20260926.md) |
| Odd compression above mode 4096 is at least 2/5 at \(L=\log13\) | Infinite-tail inequality with an exact rational certificate; excludes neither low modes nor their coupling | [Odd-tail note](notes/CCM_ODD_TAIL_CERTIFICATE_AND_STRUCTURED_SCHUR_20260926.md) |
| Scalar Schur test based on that tail bound fails; far coupling has a controlled finite-rank expansion | Proved limitations and remainder estimates; full matrix Schur positivity is not established | [Odd-tail review](reviews/ODD_TAIL_AND_SCHUR_REVIEW_20260926.md) |
| Port and block experiments | Multiprecision diagnostics, not interval eigenvalue certificates; recent block data extend to N=64 | [Numerical guide](numerics/README.md) |
| Bounded infinite-L audit | Two method obstructions proved; quantitative prolate transfer and resolution bounds derived; actual ground-state comparison still unproved | [Audit](notes/CCM_INFINITE_L_BOUNDED_AUDIT_20260926.md), [review](reviews/INFINITE_L_BOUNDED_AUDIT_REVIEW_20260926.md) |
| Ground-selection continuation | Unconditional boundary residual and near-zero cluster; escaping arithmetic moments; a weaker sufficient RH overlap criterion, with its lower bound still missing | [Target](notes/CCM_GROUND_SELECTION_TARGET_20260928.md), [review](reviews/CCM_GROUND_SELECTION_REVIEW_20260928.md) |
| Boundary selection and complement | Explicit two-profile selection; fixed-rank positivity and fixed-support form core; complement obstruction; sharp weighted-jump target and finite-prime zero-gap theorem | [Continuation](notes/CCM_BOUNDARY_SELECTION_AND_COMPLEMENT_20260928.md), [review](reviews/CCM_BOUNDARY_SELECTION_REVIEW_20260928.md) |
| Full weighted tail and discrete obstruction | Whole-line exterior coercivity; essential lower edge 1/4; simple zero mode and positive unspecified gap; fixed-depth compact counting criterion, with sharp exclusion unproved | [Continuation](notes/CCM_WEIGHTED_TAIL_AND_DISCRETE_OBSTRUCTION_20260928.md), [review](reviews/CCM_WEIGHTED_TAIL_REVIEW_20260928.md) |
| Threshold energy and deflation obstruction, round 9 | Energy-density theorem; negative endpoint divergence after ground removal; fixed-prime absolute-relative obstruction; physical threshold projection unbounded in bare energy norm | [Analysis](notes/CCM_THRESHOLD_ENERGY_OBSTRUCTION_20260928.md), [review](reviews/CCM_THRESHOLD_ENERGY_REVIEW_20260928.md) |

The string experiments do not establish uniform first-moment tightness. Stable total string mass and a stable first bead do not imply it; an exact counterexample is recorded. String geometry is one possible route, not a necessary prerequisite for determinant convergence.

## A precise sufficient route to infinite support

For the finite parity blocks set
\[
T_{\pm,L,N}=W_{\pm,L,N}-\varepsilon_{L,N}I,\qquad
\mathsf M_{L,N}=J_{L,N}^*T_{+,L,N}J_{L,N},\qquad
\mathsf K_{L,N}=T_{-,L,N},
\]
where \(\varepsilon_{L,N}\) is the least eigenvalue of the full compression and J is inverse differentiation with the prescribed zero endpoint condition. Under the finite hypotheses, both mechanical matrices are positive definite. Define
\[
\tau_{L,N}=\operatorname{tr}(\mathsf K_{L,N}^{-1}\mathsf M_{L,N})
+\frac{L^2}{4\pi^2}\sum_{n>N}\frac1{n^2}.
\]
For the normalized full spectral function,
\[
F_{L,N}(z)=\frac{\det(\mathsf K_{L,N}-z^2\mathsf M_{L,N})}
{\det\mathsf K_{L,N}}
\prod_{n>N}(1-z^2/d_n^2),\qquad
|F_{L,N}(z)|\le e^{\tau_{L,N}|z|^2}.
\]

One sufficient program is to find a sequence \(L_j,N_j\to\infty\) with the required finite hypotheses, prove \(\sup_j\tau_{L_j,N_j}<\infty\), and independently identify \(F_{L_j,N_j}\to\Xi/\Xi(0)\) on a real interval. Normal-family compactness and the identity theorem would then give locally uniform convergence. The arithmetic identification is a separate, substantial obligation. A bounded trace alone does not identify any particular limit.

This criterion only needs bounds along an adequate sequence; demanding uniformity over every pair \((L,N)\) would be unnecessarily strong. It is also a sufficient route, not the only possible route: controlled convergence on the strip \(|\operatorname{Im}z|<1/2\), with the correct nonvanishing normalization factor, is another stated target. Any alternative must specify its topology and normalization.

For the known free tail, \(L_j^2/N_j\to0\) makes its product tend to one. If instead \(L_j^2/N_j\to c>0\), the product tends to \(\exp(-cz^2/(4\pi^2))\). This is a proved scaling restriction on that factor, not an error estimate for the arithmetic block. A schedule satisfying it can still fail every other convergence requirement. See [the determinant criterion and free-tail calculation](notes/CCM_BOUNDARY_MECHANICS_AND_DETERMINANT_CONTROL_20260926.md#6-inverse-spectral-moments-as-a-convergence-criterion).

## The unresolved estimates

At fixed L let
\[
\varepsilon_L=\inf\sigma(W_L),\quad
K_L=W_{-,L}-\varepsilon_L I,\quad
B_L=J_L^*(W_{+,L}-\varepsilon_L I)J_L.
\]
The current determinant theorem assumes \(\kappa_L=\inf\sigma(K_L)>0\). Its elementary estimate uses \(\operatorname{tr}B_L/\kappa_L\). Neither the growth of \(1/\kappa_L\) nor a useful uniform bound on the numerator is known. The mass estimate contains
\[
D_L=4\sinh(L/2)+2\sum_{p^j\le e^L}(\log p)p^{-j/2},
\qquad \operatorname{tr}(J_L^*J_L)=L^2/8.
\]
These coarse positive upper bounds grow with L. Their growth shows that the present estimates do not establish uniformity; it does not show that the actual trace diverges.

A candidate improvement is to estimate the combined quantity
\[
\operatorname{tr}(K_L^{-1/2}B_LK_L^{-1/2})
=\|(W_{+,L}-\varepsilon_L I)^{1/2}J_LK_L^{-1/2}\|_{\mathrm{HS}}^2
\]
directly, where the inverse and form compositions are justified. This retains the interaction of the two energy forms. Writing this identity is not progress by itself: progress requires a bound with controlled L-dependence. A gap bounded below independently of L is not a necessary goal if the mass suppresses the dangerous odd directions sufficiently.

The completed audit exposes the dependence of the prime translation estimate, negative pole term, leakage, Fourier split, and coupling coefficients. It proves that the current scalar mass upper bound divided by the exact positive odd gap is at least L^2/32 for L>=2. It also proves that the existing separate-prime-norm tail test needs a cutoff at least of size L*exp(c*exp(L/2)) for a positive constant c, at thresholds bounded below independently of L. These are limitations of the estimates, not divergence or negativity results for the Weil operator. The fixed value \(|b_n|<2\) remains specific to \(L=\log13\).

Finally, the construction must connect to arithmetic. CCM identifies two remaining issues: the simple-even ground state and sufficiently accurate approximation by its prolate-based candidate. The candidate's transform convergence is distinct from approximation to the actual Weil ground state. Our realizations have not supplied that missing comparison. See [CCM, Sections 7–8](https://arxiv.org/html/2511.22755v1#S7), inspected 26 September 2026.

## Completed audit and conditions for further work

The [historical round-5 brief](CONTINUATION_PROMPT.md#historical-audit-brief) was executed within its two-mechanism scope. It is not the active next-session task. No arithmetic support sweep was needed; exact finite controls checked the new algebra.

1. The direct combined trace is exactly half the normalized second moment of the finite ground function. This follows from the established CCM transform formula and includes the entire free tail. It removes the explicit inverse gap, but a new arithmetic concentration bound is still needed. A nonarithmetic logarithmic comparison family has trace L^2/24 despite the generic positive/simple-even structure.
2. The prolate candidate has controlled concentration under the cited prolate approximation theorem. Its Fourier projection error is at most a constant times sqrt(L)*exp(-L/4)+L/(N+1). Thus N of order at least L^(7/2) gives O(L^(-5/2)) resolution for the candidate. An actual ground-state comparison of that accuracy would suffice for the trace bound and Xi identification, but it remains unproved.

A residual approach would need r/sigma=O(L^(-5/2)), where r is the even Weil-block residual of the projected candidate and sigma is a verified separation of its Rayleigh quotient from the second even eigenvalue. The earlier odd gap does not supply sigma. All simple-even and normalization hypotheses remain explicit.

Further work is justified by a concrete mechanism for this arithmetic estimate or a direct normalized-moment alternative. Larger fixed-L matrices, extra ports, or another equivalent realization should not resume automatically. A failed sufficient bound is not a negative Weil vector; inability to prove the comparison is not a no-go theorem for CCM.

## Overlap target from round 6

Write b=L/2, let v_b be the L2-normalized hard restriction of the Xi kernel to [-b,b], and let E_b project onto the bottom eigenspace of the original even Weil operator W_b^+. The new unconditional estimate is
\[
r_b:=\|W_b^+v_b\|_2
=O((1+L)^{3/2}e^{7L/4-\pi e^L}).
\]
Since \(|\varepsilon_b^+|\|E_bv_b\|\le r_b\), proving
\[
r_{b_j}/\|E_{b_j}v_{b_j}\|\longrightarrow0
\]
along a cofinal sequence implies RH. The proof uses unshifted ground energies, domain monotonicity, and an explicit even negative witness if an off-axis zero exists. It requires no simplicity, odd gap, or identification of the even bottom with the full bottom. **The overlap lower bound is not proved.** This criterion does not identify the determinant or bound its normalized moment.

The same arithmetic annihilator identity holds for translated Xi kernels. It gives arbitrarily large fixed-dimensional near-zero clusters; under RH, every fixed-index even level tends to zero. Positive even approximate-null profiles can also have moments growing like L^2/32. Thus candidate positivity, small residual, and a uniform absolute gap are not suitable substitutes for ground selection.

The small Xi-proxy diagnostic is consistent with this distinction: high candidate–ground overlap coexists with a Rayleigh quotient above the second even level. Minute components outside the lowest few modes dominate the residual. That round motivated resolving an independently specified low arithmetic/prolate space and bounding its effective operator, including the complement correction, on the scale of its level splitting. The later complement results explain why this was insufficient on its own. The exact tail-form identity supplies an object to analyze, not that estimate. See the [main continuation](notes/CCM_GROUND_SELECTION_TARGET_20260928.md) and [diagnostic](reviews/CCM_XI_GROUND_DIAGNOSTIC_20260928.md).

## Boundary and weighted-gap formulation from round 7

For b=L/2 and A=pi exp(2b), the ground direction inside span{1_I k,1_I k''} is proportional to k+c_b k'', where
\[
c_b=-1/(4A^2)-9/(8A^3)+O(A^{-3}/\log A).
\]
Its trial energy is asymptotic to k(b)^2 log(A)/(2A^3 ||k||^2). This is an unconditional restricted selection theorem. Adding the fourth derivative reduces the optimized energy by another vanishing factor. A finite diagnostic finds strong geometric capture by these profiles but substantial cancellation from the full complement; its exact elimination is not an analytic remainder bound.

Every fixed derivative rank is eventually positive, unconditionally. At each fixed support all even derivatives are a form core, recovering the actual even bottom as rank tends to infinity. These facts prove the limit-order obstruction: if RH fails, the minimum derivative rank exposing a negative direction tends to infinity with support. Fixed-rank asymptotics must therefore be supplemented by a quantitative joint rank/support theorem and complementary-space control.

Alternatively, with the literal k of the programs, dmu=k(x)cosh(x/2)dx has mass 1/8. The positive gamma and full prime jump energies obey the exact even identity
\[
Q(ku)=\mathcal E_\Gamma(u)+\mathcal E_p(u)
-\tfrac14\int|u-\bar u|^2d\mu.
\]
The sharp Poincare lower bound at 1/4 is equivalent to RH. Infinitely many explicit derivative-ratio functions are threshold eigenfunctions already; their existence does not exclude lower spectrum. Every fixed finite-prime truncation of this transformed whole-line form has gap zero, so escaping test functions require the infinite prime contribution. This is not the same truncation as the original finite-window Weil sum.

The literal kernel normalization is Xi/4, proved by its Mellin integral. Two earlier supporting notes were corrected; normalized comparisons and the overlap criterion are unchanged. The [round-7 synthesis](notes/CCM_BOUNDARY_SELECTION_AND_COMPLEMENT_20260928.md) records the correction and the complete new results. No lower bound for the actual ground overlap or sharp weighted gap of 1/4 was obtained in round 7. Round 8 subsequently established an unspecified positive weighted gap, as described below.

## Weighted target established in round 8

The full even weighted jump operator J has a simple zero eigenvalue (constants), essential spectral lower edge s=1/4, and an explicit infinite-dimensional eigenspace at that threshold. Its spectrum in (0,1/4), if any, is discrete with possible accumulation only at 1/4. Consequently an unspecified positive spectral gap holds unconditionally, while RH is equivalent to that gap being exactly 1/4. These are working proofs in the linked notes, with same-model checks and no independent human refereeing.

Use the literal normalization
\[
\widehat k=\Xi/4,\quad m(x)=k(x)\cosh(x/2),\quad
M=\int m=\tfrac18,\quad a=\sqrt{k/\cosh(x/2)}.
\]
With Uu=sqrt(m)u, the exact transformed operator is
\[
H=UJU^{-1}=sI+A_0-K,\quad
A_0=M_a(g(D)+6)M_a,\quad K=6M_{a^2}+P_a,
\]
\[
g(t)=\Re\psi(1/4+it/2)-\log\pi,\qquad
P_a=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
M_a(T_{\log n}+T_{-\log n})M_a.
\]
A_0 is the positive closed form with domain av in the logarithmic Fourier space. K is bounded, self-adjoint, generally signed, and relatively form compact; it is not claimed compact on ordinary L2. Constants give the normalized vector v0=sqrt(m)/sqrt(M), with Hv0=0.

The missing statement is **one negative direction for H−s**, equivalently
\[
\boxed{\quad K\le A_0+s|v_0\rangle\langle v_0|
\quad\text{in form sense on the even domain}.\quad}
\]
Equivalently H−s must be nonnegative on v0-perpendicular. This is an RH-equivalent target, not a new established bound.

For spectral energy 0<E<s, put delta=s−E. The compact self-adjoint family
\[
\mathcal T_E=(A_0+\delta I)^{-1/2}K(A_0+\delta I)^{-1/2}
\]
satisfies N(H<E)=n(T_E>1), counting strictly and with multiplicity. The exact target is n(T_E>1)=1 for **every** 0<E<1/4. One count is guaranteed by Hv0=0, but v0 is generally not an eigenvector of T_E; any removal of this mode in those coordinates needs the correct congruence or Schur argument. E here is an energy, not CCM's support parameter lambda>1. J here is the jump operator, not the inverse-differentiation map used in older mechanical formulas.

| Available input | What it permits | What is still missing |
|---|---|---|
| Norm-convergent weighted prime sum, with tail bounded by 2C² sum_(n>P) (log n)/sqrt(n) exp(−2cn), for fixed 0<c<pi/2 | Arithmetic approximation on the whole line while retaining the exact full diagonal | A signed comparison that controls the second eigenvalue count |
| Superexponential exterior error d_R and localization error e_R | For an eigenvalue at most s−delta, mass outside R+1 is at most e_R/(delta−d_R), when d_R<delta | Uniform control as delta tends to zero; a fixed central interval is not justified |
| Local compactness and relative form compactness | A compact eigenvalue-count problem at every fixed spectral depth | Spatial and frequency errors with proved endpoint dependence |
| Infinite exact threshold family k^(2j)/k−4^(−j) | Exact threshold modes that any reduction must respect | Completeness of this family, or a positive gap on its complement, is not established |

A bounded approximation K_N introduces at most ||K−K_N||/delta error in T_E. This exposes the endpoint difficulty even when the prime tail is exponentially small. Positive prime-jump truncation is a different approximation: it deletes the long-jump diagonal and still has gap zero. No bounded inverse for A_0 at delta=0 or compact endpoint T_s is supplied by round 8.

## Round 9: endpoint obstruction and research decision

The [threshold handoff](notes/CCM_THRESHOLD_INDEX_CONTINUATION_20260928.md) was executed. The chosen mechanism removed the ground mode exactly on the H side and attempted to pass to the endpoint using the bare A_0 energy. Its precise failure is proved in the [analysis](notes/CCM_THRESHOLD_ENERGY_OBSTRUCTION_20260928.md) and checked in the [sequential same-model review](reviews/CCM_THRESHOLD_ENERGY_REVIEW_20260928.md). No numerical sweep was needed.

Writing d_j=k^(2j)−4^(−j)k, their span is dense in even H_log with the archimedean energy norm. This does not imply whole-line weighted completeness. A compact cosh-moment-zero test with positive Weil form can therefore be approximated in this energy by threshold profiles while retaining its nonzero Weil form after subtraction. The ground-reduced signed Birman–Schwinger spectral infimum tends to minus infinity as delta tends to zero. Every fixed prime remainder has the same negative divergence. Physical threshold projection is valid but unbounded in the bare energy norm; finite threshold removal also leaves arbitrarily many eigenvalues approaching the counting cutoff from below in the min–max bound.

**Decision:** suspend bounded endpoint-operator and absolute-relative-tail estimates in this normalization. The diverging negative side is compatible with the desired upper bound, so a one-sided signed factorization remains possible. A new round should specify such an estimate on the full form domain, or after exact physical projection off the known threshold span, before any computation. Completeness of that span and a positive complement gap remain unproved. The error ledger separates positive-depth prime and spatial schedules from the still-missing frequency, coupling, and sign control.

## Prospects and resource judgment

The bounded round produced rigorous method limitations and a more precise comparison target. This is methodological progress; it does not supply the missing arithmetic estimate or prove convergence. It also shows that the Fourier resolution of the known candidate can be handled at polynomial cost, while the existing separate-prime-norm tail estimate has much worse support scaling.

The new whole-line tail theorem supplies a usable reduction, but there is still little evidence for expecting a full CCM determinant-limit theorem soon. Most realizations are algebraic transformations available for broad classes of positive finite pencils. The positive high-frequency compression primarily resolves a fixed-support analytic issue. Neither fact supplies the arithmetic cancellation or ground-state comparison that the limiting identification requires. The very small finite odd energies emphasize the need for relative estimates; they do not establish how the continuum gap behaves.

The risk of an unproductive detour remains substantial if each finite calculation simply generates a larger finite calculation. The completed audits redirected the work; further investment is now tied to an estimate that controls the threshold index. There is no defensible numerical probability of success from the current evidence, and model confidence is not mathematical evidence.

## Model and working practice

Record the actual model and effort when exposed; otherwise state that they are unavailable. The current derivations and parallel reviews were produced with GPT-6 (Codex), with exact serving variant and effort unexposed. Same-model agreement does not replace independent mathematical review.

Keep derivations in `notes/`, programs and small numerical records in `numerics/`, and reviews in `reviews/`. Preserve existing work and follow [LARGE_FILES.md](../../../LARGE_FILES.md). Keep [DRAFT_HISTOR.md](DRAFT_HISTOR.md) concise; use commits or tags instead of new manuscript snapshots. The [executed handoff](notes/CCM_THRESHOLD_INDEX_CONTINUATION_20260928.md) preserves the round-9 scope; the [findings](notes/CCM_THRESHOLD_ENERGY_OBSTRUCTION_20260928.md) now give the decision and required next input. The [continuation entry point](CONTINUATION_PROMPT.md) also retains the completed round-5 brief as historical context. Round 9 remains uncommitted; no release or manuscript snapshot was created.
