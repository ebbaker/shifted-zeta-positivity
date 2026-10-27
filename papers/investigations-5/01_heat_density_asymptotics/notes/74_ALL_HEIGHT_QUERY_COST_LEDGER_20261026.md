# Complete all-height query-cost ledger on J=[95,97]

26 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**, heat-density chat0028. Turn `01a17a9b-eb3e-7ef0-9591-359380c4d336`.

**Status: proved in-note from named analytical inputs at the fixed-family scope below; same-model internal assessment only.** Return to [HDA-17-AN06 r4](../research-progress/handoffs/HDA-17-AN06.md). One fixed global IC23 descriptor now has a complete query-cost ledger at every real horizontal height on J=[95,97], for rational query coordinates and the prescribed fixed-width supports. The sufficient query bound is polynomial in global core/source parameters, requested evaluation bits, input length and **binary query height**. It includes kernels crossing the central proof split or either physical band edge. The constructor is charged once; the field is not rebuilt as the query moves. Constants/onsets remain uninstantiated, and no implementation or numerical certificate is delivered.

Read the [result index](../../../../result-summaries/README.md), [heat cluster11](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md), [collision controls12](../../../../result-summaries/12_collision_controls_and_screening.md) and [geometry13](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), together with the [avoid index](../../../../avoid/README.md), especially [classification01](../../../../avoid/01_restating_the_target.md), [premises02](../../../../avoid/02_shape_only_arguments_and_the_controls.md), [scope07](../../../../avoid/07_scoped_exclusions_read_as_universal.md), [coupled payments12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [gain20](../../../../avoid/20_volume_without_a_gain.md). This is evaluation/approximation complexity without a favorable sign, an RH criterion or collision exclusion. [Inputs74](74_ALL_HEIGHT_QUERY_INPUTS_20261026.json) pins opening sources; [Review49](../reviews/49_ALL_HEIGHT_QUERY_COST_ASSESSMENT_20261026.md) records the bounded internal assessment.

## 1. Fixed field, parameters and theorem

Fix the same t64-anchored global IC23/[Note49 SW15](49_SWITCH_UNIFORM_MOVING_GAP_ASSEMBLY_20261025.md) family used in [Notes72](72_GRADED_WEAK_FILTER_AND_ACQUISITION_COST_20261026.md) and [73](73_BINARY_HEIGHT_PURE_P_EXTERIOR_COST_20261026.md), and restrict queries to J=[95,97]. Its phase integer n, moving inverse X(t), frozen width sigma, physical q=epsilon_g², K=k_1 k_1, source tolerance epsilon and one exact dyadic polynomial-square source are fixed **before** evaluation precision is requested. The upstream fixed upper-time parameter b and all selected canonical recipe data stay fixed. No t96 phase selector is substituted for the t64 selector.

Let R_src be the original buffered radius used in the accepted IC23 tolerance. Select a rational integer R_g>=2, comparable to R_src within a fixed additive enlargement, whose header proves that every moving spatial band and its complete source/collar buffer lies inside |x|<R_g. For SW15, X(t)<=X0+264 and R_c=X0+300; a safe outward integer enlargement of X0+308 supplies such R_g, enlarging it by another fixed amount if the declared coordinate/analytic slack requires it. Source-active locations and their needed comparison disks remain in the **original** paid source buffer. R_g is a cost/dispatch cap; this choice does not demand a newly stricter source tolerance at R_g or at2R_g.

At a rational query (t,x0,y0), |y0|<=1, the original physical convolution and all requested coordinate/analytic slack remain as in Notes71–73 (support/slack within |y|<=3, analytic field buffer through5 where used). Define

    k=ceil log2(2+8+ceil|x0|),
    A_g=1+R_g+q_s+D, q_s=1+log(1/epsilon),
    B_q=1+p+k+I, T_q=A_g+B_q.                       (AH1)

Use an upward rational/integer exponent bound for q_s in an actual algorithm. D is the complete stored descriptor length, including the expanded source if stored; I reads the query and relevant branch header. Header access and source access are specified below. p>=1 requests additional absolute evaluation error2^-p. A real horizontal height means the uniform mathematical coverage; the algorithm input itself is rational, with coordinate balls/time moduli left at their separately paid scopes.

For the explicit rational/dyadic scalar encodings and canonical providers of Notes58–61, the unchanged complete EV59/WF2–8 tuple has an algorithm with

    query work <= C T_q^80,
    streaming working storage <= C T_q^32.           (AH2)

The same bound covers every retained scalar, equation-component sum and fixed trace at its specified order. C depends only on fixed b,eta, the fixed central/geometric recipe constants, normalized margins, kernel and finite circuit inventory. It is independent of chosen onset/index/source degree, R_g,q_s,D,p,I and x0. Arbitrary external scalar providers multiply work by `1+C_ext(C T_q²)` and add `S_ext(C T_q²)` storage; input costs are not buried in C.

More informative than AH2 is the two-lane ledger:

    bounded lane: C(1+R_g+q_s+D+p+I)^80 work,
                  C(1+R_g+q_s+D+p+I)^32 storage;
    exterior lane: C B_q^80 work, C B_q^32 storage.  (AH3)

The exterior lane reads only its certified header and does not evaluate inactive source coefficients. If the input representation forces a monolithic descriptor scan, add O(D) bit reading per uncached access, or do the scan/compilation once. AH2 already permits that charge. Neither AH2 nor AH3 is a polynomial in the binary length of the global core radius: R_g is a numerical global construction parameter. Only the unbounded *query* height has been reduced to its binary length.

The p allowance evaluates the chosen field. It neither refines epsilon nor absorbs the inherited H-to-model/source comparison error. To use EV2's vanishing additional-error schedule on this fixed J, ask for p+2k+O(1+log(1/theta)) evaluation bits instead; its extra height debit is still linear in binary k and changes no polynomial degree. Practical runtime, an executable constant set and independent validation remain open.

## 2. A complete overlapping query cover

Write S_x for a fixed rational upper bound on the horizontal half-width of the full query/support/coordinate/analytic slack. It is fixed by the retained contract, not by p or x0. Enlarge R_g in its header so that R_g exceeds every band edge by S_x+8 and exceeds the fixed exterior onset needed below, unless that onset is absorbed by Note73's fixed compact fallback. Equivalently add these fixed terms when defining the dispatch thresholds; this does not change comparability to R_src except by fixed data.

The following deliberately generous pair of charts avoids any exact test against X(t):

    finite chart valid when |x0|<=2R_g+16;
    pure-P chart valid when |x0|>=2R_g+8.            (AH4)

Increase the fixed constants8,16 by a common amount if S_x requires it. The pure-P support then lies a fixed positive distance beyond every spatial/moving band on all J. Select, for example, the finite chart when |x0|<=2R_g+12 and the exterior chart otherwise. This is an exact rational comparison. Equality goes to the finite chart, and the overlap proves correctness of either choice near the threshold. No arbitrarily close transcendental comparison or non-equality premise enters the dispatch.

Every support that meets a source-active region, either physical band or their boundaries goes through the finite chart. A finite-chart support may also contain pure-P pieces beyond the original source buffer; their P geometry is global and their numerical height is <=C R_g. One invokes G/H relative comparison only where G is active, inside its original paid buffer. **No relative source estimate is extended to the artificial full finite-chart box by simply replacing its radius in IC23.**

This cover selects an evaluation algorithm for a single already defined field. It does not multiply F, an observable, or a weak test by a chart cutoff. In particular it creates no new spatial or temporal defect. The negative-height chart uses the original real/even symmetries. Both time endpoints95,97 are included using the same exact first-time jets, not finite differences across a chart selection.

## 3. Finite chart across the whole core

This section proves the extension needed beyond Note72's fixed-width seam query set; it does not cite that restricted theorem as if it already had the present domain.

### Fixed multiple-event region

Use Note55 IC3's fixed central geometry. Pick once a rational cut c0 in [R0+8,R0+9], with fixed collar/Cauchy slack inside |x|<=R0+16. The integer/dyadic outward recipes can choose this line without deciding an exact equality. The accepted global onset keeps this region away from spatial joining bands. On it F=G is holomorphic and exact heat, but zeros of any multiplicity remain permitted.

Use the unchanged physical positive-q circuit, with the conservative fixed lower floor

    e_fix=min(1,E_sw exp[-(R0+32)²/72]),              (AH5)

from SW9, or a smaller fixed rational lower choice. Explicitly epsilon_g>=e_fix, q>=e_fix² and |G|²+q>=e_fix² on this region. This floor is independent of R_g,source size and p. The value comparison |G-H|<=1 on strip4 and fixed canonical moments bound G on the fixed enlarged central region. Cauchy on radius1/2 gives all positive spatial derivative orders needed for Gevrey quadrature, with fixed constants. Product/inverse/log rules then give fixed G3 bounds for the central weak integrands and supplied first-time rows, with the explicit e_fix inverse.

Thus central smoothness is **not** estimated from exp(bU²), high-degree source coefficients or Note61's unnamed descriptor-dependent box constant. Those quantities are paid in the actual source evaluation precision/algorithm below. This separates uniform analytic smoothness from numerical source cancellation. No central root list, simple-zero premise or regulator-to-zero limit is used.

### Every source-active outer core collar

Outside the fixed central region, Note55 IC2/IC6 supplies the actual simple G collars and zero-free complement over the entire source-active core, not just at the seam. Its proof uses the globally valid strip4 absolute source bound, converting it to a relative bound only inside the original consumed source rectangle. For every such location u,

    epsilon/A_local <= C epsilon exp(Psi_b(R_src)), (AH6)

with the already accepted IC23 gates. This is no worse than the original paid worst-radius guard. The corresponding global P collars/complement apply where the field is pure P. Note49's band floor and all its moving B/E circuits supply the intervening bands. Consequently no unknown simple roots are inserted by extending the query center through the outer core.

At any single fixed-width query support the collar count is

    N_local<=C ell_g, ell_g=1+log(2+R_g).            (AH7)

This follows from the phase derivative bound and fixed support width; centers may vary over the whole core. Acquiring **all** outer roots simultaneously would use O(R_g ell_g) labels, but is unnecessary for a query. A root cache is optional and cannot be counted as free preprocessing. Acquire every collar meeting the enlarged query support, including collars crossing its edges or the proof cut.

The first-time source leaves use G_t=-G_zz. P_t=-P_zz+E_P, and the actual cutoff has lambda_t=-sgn(x)X'lambda_x, |X'|<=8. Source spatial derivatives of any order required for quadrature remainders follow by Cauchy from the strip4 **value** comparison. Evaluating the fixed higher jets of G is a separate provider call, not a stronger source-to-H comparison claim.

### Band edges and the central proof cut

First derive WF2–8 globally for the actual field. Use the **same weak primitives on all pieces**, including in the fixed central region, where quotient-looking expressions are evaluated by their original smooth fractions. For example V0=F_zz conjugate(F)/(|F|²+q) is defined at F=0. Do not integrate raw central density and weak outer log-density as if there were no intervening boundary term.

After that exact reduction, divide only the numerical integration domain at rational lines x=+/-c0, square-ring/grid boundaries and exact rational kernel edges. Central and outer rectangles partition the same weak integrals. Include any collar touching c0 in full when constructing its guard, then clip its numerical pieces to the outer part. The central portion uses its smooth positive-floor formula. The omitted outer portion of a root square is bounded by the full physical omitted-disk debit. There is no double counting of the central portion.

Do not cut at a numerically approximated physical band boundary. The original blend and its flat profile jets are globally smooth across both edges. Regular cells may cross an edge and evaluate the actual circuit. All zero-free band/complement Cauchy/Gevrey bounds and flat endpoint/tail rules remain valid there. Neither derivatives of a numerical indicator nor an interface flux is created, since no integration by parts is performed after partitioning.

The fixed-index phase-label gap gives root ownership: required labels (m+1/2)pi lie strictly on one side of n*pi, and the paid collar/band separation places each full collar in its actual pure-G or pure-P region. Edge query equality merely overincludes a collar. No exact test for lambda=0/1 at a transcendental edge is needed. Constant active-component gates are used only where the inherited strict margins certify a whole neighborhood; in the remaining overlap the complete blend is evaluated. This also avoids attempting P below its defined outer domain.

### Actual moving-band jet payment

For clarity, on J the actual field is F=G+lambda Delta with Delta=P-G. Its separate heat addends and compatibility terms are

    E_c=lambda E_P,
    E_s=lambda_x Delta_z+lambda_xx Delta/4,
    E_m=lambda_t Delta,
    B=lambda_x Delta/2,
    Delta_t=-Delta_zz+E_P.                                  (AH7a)

The nonholomorphic TJ5 variation of T_C requires each actual E addend's spatial and bar jets, not merely E/F. Since Delta,E_P are holomorphic, the relevant mixed entries are

    (E_c)_barz=lambda_x E_P/2,
    (E_c)_zbarz=lambda_x E_P,z/2+lambda_xx E_P/4,
    (E_s)_barz=lambda_xx Delta_z/2+lambda_xxx Delta/8,
    (E_s)_zbarz=lambda_xx Delta_zz/2
                    +3lambda_xxx Delta_z/8+lambda_xxxx Delta/16,
    (E_m)_barz=lambda_xt Delta/2,
    (E_m)_zbarz=lambda_xt Delta_z/2+lambda_xxt Delta/4.        (AH7b)

The remaining z jets follow by ordinary product differentiation of AH7a. For B_t,(B_z)_t use Delta_t=-Delta_zz+E_P and Delta_zt=-Delta_zzz+E_P,z, retaining both residual terms. With v=sgn(x)X', lambda_xt=-v lambda_xx and lambda_xxt=-v lambda_xxx on each band. The inherited fourth spatial profile bound and first-time leaves therefore pay every displayed term without X''. The bands are away from x=0; the cutoff is constant on a neighborhood of0. This is the actual defect inventory, not a claim that all component residuals satisfy heat.

## 4. Complete integration and error ledger

For outer retained cells use Note72 SI5–8: normalized analytic leaves on c/ell_g disks, positive-order logarithmic derivatives, offset-uniform logistic composition and the area payment for at most one V/Z pole per expanded collar term. The central constants from AH5 are fixed; the actual band corrections retain their paid normalized floor. On the whole finite chart, |x|<=C R_g, so the physical coefficient products have degree at most four in R_g. Enlarge the same explicit positive-expression list before p. Sufficient common bounds are

    V<=C R_g^8, A<=C ell_g(1+R_g²),
    C_tail,A_post,(1+M_mean)²<=C R_g^8.              (AH8)

Fixed central inverse-floor constants enter C; an expanding outer inverse-q floor does not. Actual means and their products remain separate post-filter gates.

Apply SI10–15 with global radius R_g as a **cost upper bound**. Choose raw e<=2^-p/(C R_g^8), puncture scale with log(1/h)<=C(p+ell_g+log C), actual root centers to h/8, quantitatively separated outer squares and graded rings. Clip both central/outer numerical pieces at their proof lines and the exact kernel support. Thin clipped sides only decrease scaled derivatives. K4 uses its interior polynomial trace; no fifth bounded weak kernel derivative is assumed.

A single query uses

    B_cells<=C ell_g(p+ell_g+log C),
    N_nodes<=C R_g^6(p+ell_g+log C)^7.               (AH9)

The fixed central portion contributes only fixed-size/polynomial-accuracy quadrature, already dominated by AH9. This is a per-query count, not a sweep over the whole core. Full physical omitted primitives, integration, signed weights, node/coordinate rounding, summation and post-filter arithmetic receive distinct raw allowances, for example e/16 each with unused slack.

The common dyadic value grid and SI15 denominator pay exact signed sums without multiplying unrelated cell denominators. Include each affine Jacobian in the rounded integrand. Kernel factors/edge clipping use exact rational offsets; separately rounded field coordinates never decide a K4 jump side. Full-support enlargement, rather than a queried zero sample, supplies omitted-root coverage.

The actual tuple inventory and cost payments are:

| Targets retained | Complete finite-chart payment |
| --- | --- |
| U,W through4; auxiliary means | Global weak S,w integrals, fixed kernel derivatives and actual post-filter products |
| density R and total calC through2 | WF2–3 with every actual regulator coefficient and compatibility T_C |
| current through2, internal order3 | Weak current, normalized V_m and full T_J |
| U_t,W_t,R_t,calC_t through2 | Direct time primitives, full a',beta', physical q_t, B_t and (B_z)_t |
| actual Q,Delta Q | Signed stress and Xi first, then products of the actual full means |
| calB through2 | Actual regulator forcing, rather than a redefined desired source |
| actual calS and equation-component sums through2 | WF5, D_E,D_B, every component/spatial/moving E/B addend and -delta_E T_C |
| heat-potential correction through4; fixed traces | Full Xi/2 and residual Z rows at exactly the inherited paid orders |

On pure G the actual E/B terms vanish because G solves heat. On pure P only B and its compatibility terms vanish; E_P is retained. On bands none is discarded by an exterior approximation. In particular Note50 TJ5's nonholomorphic heat variation remains. Piecewise integrals are added before the global signed-source and covariance recombination. This pays kernels meeting both sides of a band; it is not a component-covariance substitution.

## 5. Acquisition, providers and the compiled descriptor

### Read/compile once

The canonical descriptor contains the exact phase integer and its t64 lift convention, selected onset/width recipes, a certified rational enclosure of the exact phase-inverse X0 and movement/width bounds, R_src,R_g, fixed active-component evaluation guards, source-tolerance exponent, U,m,beta and dyadic source coefficients (or an indexed coefficient handle). The source policy is not inferred from a hash. The inherited analytical recipes establish its accuracy; reproducing source coefficients and exact recipe choices pays their construction costs.

A compiled header exposes the exterior data without traversing unrelated source coefficients. Reading/copying/indexing the stored canonical data costs O(D) bit reading and at most C(D+1)² elementary bit work/storage; streaming or a retained immutable source handle are both valid. If only compressed coefficients are stored, exact normalized-power conversion/squaring is performed once and its actual AC17/AC18 cost and resulting D are charged. An arbitrary incoming descriptor with unverified analytical annotations is outside this constructor theorem; regenerate from the named certified recipe or keep its validation as a separate required input.

No full root list or all-height field grid is required. The header is fixed as queries move. Under the canonical encoding, the expanded source length is bounded by C q_s² log²(2+q_s), as in AC17, but D remains explicit to charge actual input reading.

### Finite-chart local acquisition and providers

Use endpoint phase enclosures with padded label ranges, then actual G or P root refinement on each paid collar. Complete phase labels are acquired directly near the query; never enumerate from label1. Equality-safe sign/unit contraction handles a midpoint that is exactly the root. Band-center inversion uses the exact frozen n and the same equality-safe EV11 method. Full support-edge guards and all root evaluations are included.

The source evaluator uses EV5–8 with fixed jets through8 and the original 6m+4 coefficient-cancellation debit. At finite-chart nodes the height bound is C R_g; provider coordinate/denominator debits use the actual local scale, not the thinnest clipped cell. SI16's carrier bits are bounded by

    P_leaf<=C[1+p+ell_g+Psi_b(R_src)+log(1/s)+I],     (AH10)

with the signed-node amplification included. Central source requests need only their fixed-floor version. Keep the rational query t exact in moving inverse X(t), X'(t), regulator and profile calls; their own leaf accuracy debits are at that t. Internal source-coordinate rounding uses EV6 and its separately paid higher G jets. It does not round the whole first-time field row in t or require an unproved X'' bound. Source-active outer/band requests use AH6; pure-P requests do not evaluate G. Because Psi_b(R_src)<=C R_g and log(1/s)<=C(p+ell_g+log C), this is polynomial in the finite-chart parameter. Large exp(bU²) moment bounds enter source precision bits and EV6, not AH8's smoothness scale.

The r2 actual algorithm ledger now applies point by point with the global cap: source work degree22, normalized providers degree40 and all local phase/root loops degree44. The node count has total degree13. Thus nodes times providers have degree53; exact weights, reading, output and actual post-filter gates fit the deliberately loose degree80. Source construction is not repeated in this count. Streaming storage is dominated by the previously paid degree32, including source workspace and actual stored coefficients. All finite-chart magnitude/argument reductions, flat endpoints, scalar constants and normalized ratios use those actual providers; no special function is unit cost.

### Exterior acquisition and providers

AH4 certifies the entire enlarged support pure P. Apply BH1–22 unchanged: local comparable radius R=8+ceil|x0|, full weak saturation debit or its precision-dominated complement, reduced-phase logarithmic arm providers, actual local P roots and signed quadrature. Neither source coefficients nor G are read/evaluated after compiled header access. The header index has O(k) bits for such an exterior query; a global seam cannot have a larger height than a query already beyond2R_g.

This gives AH3's binary-height bound, including actual phase/root/provider acquisition. It does not set physical q to zero and does not remove E_P. Note73's fixed compact fallback/constant ordering remains, independent of R_g. No true-floor decision in large-phase argument reduction is used.

## 6. One-time construction and repeated queries

The distinct payments are now:

| Stage | Sufficient charged cost | Repeated when only p or x0 changes? |
| --- | --- | --- |
| Fixed analytical recipe/bootstrapping inputs | W_fixed and S_fixed from the named fixed b,eta/onset recipes; external scalar digit costs explicit | No |
| Exact admissible phase selection | Note60 PI24's explicit polynomial in its onset-exponent precision parameter, not an oracle ceiling | No |
| Fixed chosen source | Note58 AC18: C q_s^60 work, C q_s^30 workspace as in r2 | No |
| Source expansion/header/index compilation | AC17/AC18 conversion if needed, plus actual D reading/indexing and certified outward header guards | No, unless uncached input access is required |
| Query local phase/root acquisition | SI18/EV11 or BH22, included in AH2–3 | Yes, unless a charged cache supplies the requested data |
| Complete evaluation/integration/post-filter tuple | AH2–3, including actual component sums/means | Yes |
| Model/source-to-H comparison | The inherited fixed analytical error column; not evaluation precision p | Not reduced by p |

A coarse combined constructor bound, from the same certified recipes, is

    W_build<=W_fixed+C(1+R_g+q_s+D)^80,
    S_build<=S_fixed+C(1+R_g+q_s+D)^32.              (AH11)

This includes phase inverse/header guards with numerical R_g algorithms and the additive AC18 source cost. PI24's exponent parameter is bounded by the chosen global numerical radius, so its finite polynomial fits AH11. Finding arbitrary sufficient onsets or validating arbitrary incoming analytic claims is not smuggled into PI24: use the existing explicit fixed recipe inputs and onset freedom. No improved global constructor in log R_g is claimed.

For any finite query list, let T_i be AH1's parameter for its ith query. A sequential streamed evaluation satisfies

    W_total<=W_build+C sum_i T_i^80,
    S_total<=S_build+C max_i T_i^32,                 (AH12)

with external scalar costs attached as above. The sharper lane-specific terms in AH3 may replace T_i^80. An uncached monolithic input scan adds its actual O(D) charge per access. Retaining all outputs adds their actual storage; AH12 is workspace with streamed outputs. There is no automatic research sweep in this theorem.

## 7. Gain, scope and next deliverable

The actual new payment is **complete query coverage** on J for one fixed global field. r2 paid a seam neighborhood (plus fixed central fallback), and r3 paid guarded pure-P exterior queries. AH6–10 extend the graded query proof to every source-active outer core support, while AH4 routes every band-crossing kernel to a solver retaining its actual defects. The cost of a new distant query grows polynomially in its binary height, without replacing the source by a new one adapted to that query.

This does not upgrade the inherited analytical H-comparison error, remove the fixed central multiple-event floor, or make the enormous constants practical. It proves no binary-global-core constructor theorem, all-real-time query-cost theorem, time-coordinate-ball upgrade or implementation/certificate. It is uniform only for the named canonical fixed-b family restricted to J, with explicit external scalar costs. In particular the source is active at unbounded x on the earlier pure-G plateau [-T_-,63] and in the actual temporal blend for63<t<64; AH4 is not reused on either region.

The algorithm is a no-sign consumer and must permit the collision controls whenever its local hypotheses hold. Multiple events are allowed in the fixed-floor region; they fail the simple outer-collar premise elsewhere. The canonical complete theta source distinguishes Euler-factor changes, weighted-square/finite-prime coefficient/reflection changes, reflected shape/positive-primitive substitutes and atomic/heat-polynomial controls exactly as in cluster12. None of these premise distinctions excludes a collision or supplies an RH/Newman conclusion here.

**HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled remain.** r4 closes at the stated analytical all-height query-cost scope on J; review is same-model only. [Work record](../numerics/ALL_HEIGHT_QUERY_WORK_RECORD_20261026.json) records zero numerical, exact-rational or machine-symbolic research executions. No source/field/gamma/root values or coefficients were acquired. Hash/link/size checks and public chat capture are housekeeping. No manuscript, snapshot, DRAFT_HISTORY milestone or commit is part of this return.

**Next: Analysis — Sol**, AN06 r5: the same fixed descriptor's binary-height **pure-G** query cost on [62,63], where the source is active at unbounded height and the physical regulator has a positive time-only floor. Determine a stable full source-jet/provider and complete filtering bound in source parameters, requested bits and binary query height, or identify its first exact unpaid oscillatory/provider term. Preserve arbitrary central/source-root multiplicities and actual means. This bounded analytical task decides whether the all-height cost program can approach the physical switch; it does not already cover the temporal blend63<t<64, the approach64<t<95 or all real time. No numerical pilot before finite cases, allowances and runtime/storage stops are selected.
