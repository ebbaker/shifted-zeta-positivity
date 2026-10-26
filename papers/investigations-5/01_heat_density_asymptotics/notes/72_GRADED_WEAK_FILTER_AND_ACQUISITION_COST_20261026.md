# Graded weak filtering and complete acquisition cost on a fixed positive family

26 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**, heat-density chat0028. Turn `01a17a77-a411-7830-b635-ad2915e0fb2b`.

**Status: proved in-note from named analytical inputs at the fixed-family scope below; same-model internal assessment only.** This returns [HDA-17-AN06 r2](../research-progress/handoffs/HDA-17-AN06.md). It replaces Note71's generally O(e^-6) uniform-grid consumer by graded integration and pays source construction, exact admissible phase selection, local root enclosures, normalized field evaluation and signed post-filter arithmetic. For the explicit scalar encodings below, the sufficient work is polynomial jointly in numerical height, source demand and requested evaluation bits. Constants are enormous and uninstantiated; no computation, measured crossover or implemented certificate is claimed.

Read the [result index](../../../../result-summaries/README.md), [heat cluster11](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md), [collision controls12](../../../../result-summaries/12_collision_controls_and_screening.md), [geometry13](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md) and [avoid index](../../../../avoid/README.md), especially [classification01](../../../../avoid/01_restating_the_target.md), [control premises02](../../../../avoid/02_shape_only_arguments_and_the_controls.md), [scope07](../../../../avoid/07_scoped_exclusions_read_as_universal.md), [coupled costs12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), [unchecked imports16](../../../../avoid/16_unchecked_imports_and_novelty_claims.md) and [gain20](../../../../avoid/20_volume_without_a_gain.md). This is approximation/evaluation complexity, with no sign conclusion, RH criterion or collision exclusion. [Inputs72](72_SCALED_INTEGRATION_INPUTS_20261026.json) pins the source versions; [Review47](../reviews/47_GRADED_WEAK_FILTER_COST_ASSESSMENT_20261026.md) states the review limits.

## 1. Frozen family, encodings and theorem

Fix the existing IC23 constants, positive eta and already selected finite upper time b first. Use the actual global IC23/[Note49 SW15](49_SWITCH_UNIFORM_MOVING_GAP_ASSEMBLY_20261025.md) family, with phase label anchored at **t=64**, and restrict it to J=[95,97]. The original free dyadic onset is selected by [Note60](60_EXACT_PHASE_INDEX_BY_DYADIC_ONSET_SELECTION_20261025.md), then X0 solves Theta(64,X0)=n*pi. The same n determines X(t); its width sigma is frozen. This is an existing family allowed by r2. Note48's separately anchored literal ceiling at t=96 is not evaluated using a t64 theorem.

Choose one dyadic source tolerance epsilon satisfying **every** IC23 clause, before requesting any evaluation accuracy. Use Note58's fixed polynomial-square source f and its exact field G in the unchanged blend F. Keep physical q=epsilon_g², K=k_1 k_1, actual B=F_barz and E=F_t+F_zz, unnormalized observables and actual covariance. Let R>=2 be a certified rational upper bound for the selected union core radius plus the established horizontal collar/source enlargements. For the SW15 restriction one may take R>=X0+308; for the general fixed-b construction use its declared Dmov_b and corresponding enlargement. Write

    ell=1+log(2+R), q_s=1+log(1/epsilon),
    T=1+R+q_s+p+I.                                    (SI1)

Here p>=1 requests additional absolute **evaluation** error 2^-p, and I is the rational query encoding length. The allowed query set is the finite fixed-width seam/slack neighborhood of this family, with |y|<=1 and full supports/slack inside |y|<=3. One can also include the original fixed central rectangle using its fixed e0 floor. The width of the seam neighborhood depends on the already fixed b, not R. Source and phase label remain fixed as p changes. This is not a theorem of arbitrary total H-approximation error at fixed R: the inherited model and source errors remain separate addends.

For exact rational/dyadic independent scalar encodings and the explicit canonical providers of Notes58–61, there is a specified acquisition/evaluation algorithm with

    work <= C T^80, working storage <= C T^32,         (SI2)
    quadrature nodes <= C R^6(p+ell+log C)^7.           (SI3)

The bound includes constructing the source once, selecting an admissible exact phase index with the existing onset freedom, acquiring every needed actual outer root enclosure and evaluating the complete WF2–8/EV59 tuple and its equation-component sums and fixed traces at their paid orders. C is independent of R,p,q_s,I, the selected onset exponent/index and the resulting source degree. It depends only on fixed b,eta, fixed lower onset thresholds and normalized margins, kernel and finite circuit inventory; varying rectangle diameters and source cancellation are paid explicitly below. Uniform time-coordinate balls are not added here; Note71's extra time-jet requirements remain. Rational query times are evaluated directly.

For arbitrary computable external fixed scalars, multiply the work bound by `1+C_ext(C T²)` and add `S_ext(C T²)` to storage, where these are their stated provider costs. Their digit costs cannot be hidden in C. The primary encodings are those of Note61 PC1. Constants/onsets and analytic input validation are not acquired from an oracle: use the explicit fixed recipe data of Notes54–55, or retain their input/bootstrapping cost separately as a fixed constant. No bound uniform in b,eta or an arbitrary incoming descriptor is asserted.

Polynomial here means in the **numerical height R**, not its binary length log R. Under IC23's fixed-b source policy, q_s=pi R/8+O(log²R+log(1/theta_s)); thus SI2 also gives a joint polynomial in R,p and source-reserve bits. It is a deliberately coarse sufficient bound, not practical runtime evidence.

## 2. Named geometry and finite constant construction

Note49 SW1 extends the full-buffer comparison and EB collar table to [63,97]. SW15–16 give the unchanged t64 family, |X'|<=8, |X-X0|<=264, sigma=(64L)^-1, collar/band separation at least1/(4L), and every moving B/E addend. Note54 C1 and Note55 IC21–23 give the fixed-b replacements. The source comparison G-H holds on **all real x, |y|<=4**, at every t<=b. The local source demand IC14/IC23 pays IC6's actual real simple G collars and the zero-free complement; it is not replaced by the larger model error.

On each larger outer disk in u=L_c(z-a), the analytic unit of G or P and its reciprocal have fixed dimensionless caps from EB/IC6. Away from collars and on bands, the actual normalized field has a fixed positive relative floor. Every collar meeting the entire query/slack union is included; their number is

    N <= C ell.                                      (SI4)

This is a fixed-width spatial seam/slack union at each queried rational time; the bound is uniform on J. Actual root enclosures are acquired at that queried time. Across the entire growing core there can be O(R ell) collars; that larger simultaneous acquisition task is not needed for SI4. There are no omitted unknown roots in the selected outer supports: EB/IC6 and the band floor supply the count, simplicity and complement coverage analytically. The central multiple-event region keeps its fixed floor rather than acquiring simple-root data.

All constants used below have a finite positive-expression recipe. Start with the coefficients in Note55 IC12 (including K0,e0,R0,C_H,W_b,Lprof,Dmod,K_*), the EB/IC6 unit and inverse-unit caps, Note54 C1/C2, SW15's speed/width and PC3's profile constants. Add the finite fixed-jet recurrences through order8 and apply the explicit positive Gevrey rules in PC2. Take a common upper bound of these finitely many expressions before choosing p. C denotes an enlargement of that list, never an unnamed supremum. Expressions containing the fixed e0 inverse remain permitted. No inverse of an expanding outer physical q floor is inserted.

## 3. Uniform scaled spatial derivatives

First derive the global weak identities WF2–8 exactly as in [Note71](71_WEAK_FILTER_PUNCTURE_CONSUMER_20261026.md), including `-delta_E T_C`, direct rho_t, both curvature rows, D_B, signed stress and actual full mean products. All region splitting in this note happens **after** that reduction. No indicator or numerical boundary is differentiated in a field equation.

### Analytic leaves rather than absolute moment caps

For fixed t, the value estimate for G-H on strip4 gives every spatial derivative on smaller disks by Cauchy. On outer disks of radius c/ell, use the full-buffer H-P comparison and the arm logarithmic derivative bound O(ell). Normalize by a constant carrier frame for each small cell: the sum of arm magnitudes at its center, with an outward relative enclosure. Cells have side at most c/ell, so each arm and the carrier sum change by bounded factors on their c/ell enlargement. One may split at y=0 and use the dominant arm on each half as an equivalent guard. This avoids normalizing a whole transverse strip by one remote arm.

The resulting analytic component leaves satisfy

    |partial_i^n(component/A_frame)|
                      <= C(C ell)^n n!, i=x,y.       (SI5)

On rings, `log|F|²=constant+2log|z-a|+log|b|²`; a local logarithm on each nonencircling cell and the unit bounds give level-independent positive-order scaled derivatives. The constant log s disappears. On bands apply PC2 to `log|F/A_frame|²` with the fixed relative floor, then add the constant carrier logarithm.

The source contribution uses its **complex-strip comparison**, not the raw `exp(bU²)/A_frame` bound. The latter would falsely introduce a quasipolynomial or exponential smoothness prefactor. On the fixed central region, Cauchy on radius1/2 applied to G-H and the fixed canonical moment cap gives a bound independent of R; the fixed e0 inverse then pays the original circuit.

For first time leaves use exact heat for G and `P_t=-P_zz+E_P`; thus `(P-G)_t=-(P-G)_zz+E_P`. The frozen-width moving cutoff has `lambda_t=-sgn(x)X'lambda_x`, |X'|<=8. PC3 and the fixed-order derivative rule give G3 spatial bounds for every cutoff and first-time cutoff leaf, including E_barz and E_zbarz in delta_E T_C. These can need profile orders beyond the earlier low-order source-variation shorthand, and they are explicitly included. No X'' or second time derivative is needed to integrate an already supplied first time row.

### Large logarithmic offsets do not enlarge the logistic derivative scale

For real v let sigma(v)=1/(1+exp(-v)). It is holomorphic on the strip |Im v|<pi/2 and has modulus<=1 on each radius-one disk centered on the real line. Cauchy gives `|sigma^(k)(v)|<=k!`. If, for n>=1 only,

    |partial_i^n L|<=V A^n(n!)³,

Faà di Bruno and `product_j(j!)^(2m_j)<=(n!)²` give

    |partial_i^n sigma(L)|
       <=[A(1+V)]^n(n!)³.                            (SI6)

Indeed the sum with k parts is `binom(n-1,k-1)V^k`, after the k! factors are collected. Softplus has the same positive-order estimate since its kth scalar derivative is sigma^(k-1) for k>=1. Its value bound is treated separately. No bound on the constant value of L is needed in SI6.

Use `L=r-log|F|²`, w=sigma(L), g=1-w and the stable WF7 formulas. Here r=a(t)-beta(t)x² has r and its fixed first-time coefficients O(R²). Logarithmic cell/radius constants in log|F|² do not appear in positive-order derivatives. In particular the term log(radius) does not enter V in SI6. Never apply PC2's generic exp rule to exp L: that would reintroduce exp(CR²).

### Area pays each simple pole

On an annular cell at root distance s, with side at most Cs, map affinely to [-1,1]² and include the area Jacobian J_cell in the integrand. The analytic unit representation is

    F=A_frame L_c(z-a)b(z),
    N/F=[N/(A_frame L_c b)]/(z-a).                    (SI7)

The numerator/unit quotient has the Cauchy bounds from SI5 on the larger disk. On a retained ring the root distance is at least3s/8. A pure-axis radius1/4 disk in the mapped variable moves a point physically by at most s/16, including on a clipped cell. Cauchy therefore bounds the area-scaled derivative by `C ell^k s 4^n n!`. More generally scaled derivatives of N/F are at most `C ell^k s^-1 C^n n!` for the fixed numerator order k. Multiplication by `J_cell<=Cs²` leaves `C ell^k s C^n n!`. This applies to F_zz/F and each retained E addend/F; it is done before taking a quadrature smoothness constant. Every expanded collar term in WF2–8 is linear in at most one V/Z simple pole times bounded weight factors. Nonlinear ratio products occur only on paid zero-free bands or in the fixed central fallback; full mean products are formed after integration. Thus no unfiltered double-pole product is hidden in the area payment.

In the regular complement use cells of side<=c/ell and the fixed normalized field floor. Products, normalized inverses and all band corrections use PC2, then SI6 for w/chi. Regulator coefficients are polynomial in x; direct-time weights have degree at most four in R. Kernel factors are fixed-degree **interior** polynomials after the support-edge split below. The actual S magnitude is <=C R², from log q and the field magnitude cap, even when two logarithmic expressions used to evaluate S have large cancelling offsets.

Consequently every complete area-scaled raw weak integrand has the common sufficient pure-axis bound

    G3(V_R,A_R), V_R<=C R^8,
                    A_R<=C ell(1+R²).                (SI8)

These are deliberately loose. They are independent of puncture radius and level, the physical rounding width sqrt(q)/|F_z(a)| and requested p. Only fixed component jet orders are evaluated at nodes; arbitrary n in SI8 is a remainder bound from analytic leaves/Gevrey profiles. No stronger source-to-H error premise is imported.

## 4. Rational graded partition and complete error sum

Note71's primitive L1, tail and actual-mean post-filter maps admit loose common caps

    C_tail, A_post, (1+M_mean)² <= C R^8.              (SI9)

This follows by inserting the EB/IC6 simple-pole caps into WF9–10, N<=C ell, the O(R²) physical coefficients, and the actual EV18 mean products. There is only a fixed finite inventory of linear maps and these mean products. Enlarge C for every equation-component target. Set

    e=2^-p/(C R^8),
    h comparable to min(H_min,e/(8 C_tail)),          (SI10)

using a certified dyadic lower choice within a factor two. Then `log(1/h)<=C(p+ell+log C)`. Acquire rational actual-root centers c_j with error<=h/8 before building the partition.

Choose dyadic outer square radii H_j comparable to c/ell with `H_j<=H_analytic,j/(16sqrt(2))` and a comparable fixed lower bound, where H_analytic,j is the paid analytic collar radius. Keep their larger squares disjoint and separated from bands. This quantitative margin pays the annular Cauchy enlargements. Put

    Q_j,k=c_j+[-s_j,k,s_j,k]²,
    s_j,k=H_j 2^-k,
    stop at first L_j with h/2<s_j,L_j<=h.            (SI11)

The omitted square is contained in a true-root disk of radius3h, so WF9 pays at most e/8 per raw integral. Each ring `Q_j,k minus Q_j,k+1` consists of twelve rational squares of side s_j,k/2. The true-root distance on each retained ring is comparable to its level radius because the center error is at most h/8.

Partition the complement of the disjoint Q_j,0 by their boundary lines and a rational regular grid of mesh at most c/ell. Split along y=0 if using dominant-arm frames. Finally intersect each retained rectangle with the exact rational kernel-support square for the query. Empty pieces are skipped. This step is essential for the pure fourth kernel derivative: it jumps across the support edge, so the zero extension is not Gevrey on a cell crossing that edge. Each clipped rectangle uses the interior polynomial trace; its side lengths only decrease. Hard numerical holes and this clipping create no commutators because no integration by parts is performed after removing them.

Write P0=p+ell+log C. The number of rectangles satisfies

    B_cells<=C[(ell+N)²+sum_j L_j]
                         <=C ell P0.                (SI12)

For each scalar raw integral use the same rational interpolant order and panel count from PC9, with per-cell target `e_box=e/(8 B_cells)`, SI8's common V_R,A_R and

    n=max(1,ceil log2(64 V_R/e_box))<=C P0,
    M=max(1,ceil[2^16 A_R(n+1)²]),
    nodes/cell <=2^34 A_R²(n+1)^6.                   (SI13)

The shared order and counts can use safe integer upper bounds. PC8–12 pay interpolation, signed-weight amplification, node error and exact summation on every scaled rectangle. Each node value includes the affine Jacobian. Use node error<=e_box*2^(-6n-10). Total integration/arithmetic error over cells is <=e/8, in addition to omission<=e/8. The original post-filter circuit with SI9 then gives every final scalar's additional error below2^-p; source/model errors remain unchanged.

From SI8/SI12–13,

    total nodes <=C R^4 ell³ P0^7 <=C R^6 P0^7.      (SI14)

All nodes and boundaries are rational. Round area-scaled integrands to a common dyadic grid and use shared n,M. PC12 gives one common weight denominator

    2^B M² W², W=2^n n!(n+1)!,                      (SI15)

across all cells; Jacobians have already been included in rounded node values. Coordinate and area rounding are separately debited before this step. Evaluate the kernel interior polynomial from the exact rational affine node/offset; only the field provider uses its separately paid coordinate rounding. A rounded field coordinate never decides which side of a kernel jump supplies its trace. Denominator lengths from unrelated cells are never multiplied. Operand/grid lengths are polynomial in p+I+ell and the provider precision below. Stream the nodes.

## 5. Actual data acquisition and normalized provider cost

### Exact descriptor and actual roots

Note60 selects one admissible free binary onset among four and obtains the exact literal t64 index; its work is polynomial in the onset exponent, included in SI2. A separately frozen arbitrary onset with an unknown ceiling is outside that selector's contract. The source-demand exponent and recipe integers are selected with outward bounds and the inherited bounded-slack convention, rather than undecidable exact ceilings. Their elementary logarithmic/exponential costs fit the same polynomial ledger. The subsequent moving gap inverse uses the same unwrapped phase and paid derivative floor, including exact-equality-safe bisection from EV11. This preserves the actual family rather than choosing a favorable queried root or zero sample.

Enumerate local P-root phase labels `(k+1/2)pi` using outward enclosures of enlarged-support endpoint phases of width below1/16 and padding by two labels. Endpoint equality leads to overinclusion. This enumeration is made at the queried time; a single cached label range for all J must also include the paid temporal phase/velocity envelope, which adds only C ell labels. EB/IC6 then supplies exactly one real simple actual G or P root for each required collar and none elsewhere in the outer supports; bands have the paid floor. Labels on either side of the fixed gap determine the actual pure component. Root enclosures, coverage and band separation are therefore data produced from named analytical guards, not new unproved favorable margins.

On a real unit collar the factorization `F=(x-a)b` supplies a known sign and lower unit bound m_*. To refine a bracket of width w, evaluate its midpoint with error<=m_*w/16 (using the carrier normalization). If the approximate midpoint value is small, its absolute true value bounds |mid-a| by the same unit floor and gives a shorter interval; otherwise its sign is certified and a half bracket is retained. For example error eta<=m_*w/16 and approximate modulus<=m_*w/8 give `|mid-a|<=3w/16`; use that centered interval. In the complementary case the sign is certified. Both alternatives contract and cover exact midpoint equality. Initial brackets come from the strict EB/IC6 real-type collar geometry. Thus O(p+ell+log C) evaluations per root suffice for h/8 enclosures. All such evaluations are charged, even for edge collars.

### Precision and cancellation

Let eta_node be the full area-scaled node tolerance. The normalized finite circuit has fixed gate count. Here s denotes the annulus root-distance scale (or the regular cell frame scale), not a potentially much thinner clipped side length. On a retained cell at scale s, its inverse field/unit gates have floors at worst a fixed power of `s exp[-Psi_b(R)-32]`, with fixed coefficients. Smooth logistic/softplus outputs are evaluated with exp(-|L|), bounded-argument overlap near L=0 and declared tails. Actual logarithms have magnitude `<=C[1+R²+log(1/s)]`. Do not feed an exponential-valued coarse logarithm cap into another exponential gate.

The finite circuit error recurrence therefore gives a sufficient common absolute source/model leaf request

    P_nu=ceil log2(1/nu)
       <=C[1+log(1/eta_node)+Psi_b(R)
                                  +log(1/s)+ell],    (SI16)

with C including the fixed gate count/powers. This charges carrier cancellation and every retained inverse-unit factor. The separate source power-coefficient cancellation is still **EV5's 6m+4 debit**, not replaced by SI16. Approximating constant carrier frames themselves to a fixed relative precision uses the same paid model providers.

At fixed b the actual source construction gives `U<=C log(2+q_s)`, `m<=C q_s log(2+q_s)`, `beta<=C q_s`. For G's fixed J=8 node jets, EV5–8 may use

    A=99U²+U(R+6), T_e=ceil A,
    p_e=P_nu+6m+4+9ceil log2 U+4,
    N_e=8(T_e+1)+p_e,
    B_coord<=C(P_nu+bU²+log U).                       (SI17)

Use b+2 in place of99 if the guard actually evaluates above t97; on the selected J,99 suffices. Source-coordinate rounding is paid by EV6. Large `exp(bU²)` absolute moment bounds affect these **precision bits**, not SI8's analytic smoothness constants. With SI10–13/SI16, every EV7 parameter is at most C T², so actual source point work is <=C T^22. This explicitly charges expanded coefficients, whole-series cancellation, coordinate/argument rounding, input reading and the final rounding. Nothing is treated as a unit-cost special-function value.

The remaining algorithms fit in a conservative common normalized point/provider bound

    C_norm<=C T^40.                                  (SI18)

Here is the degree ledger. Elementary argument magnitudes, rational lengths and sufficient common-denominator Taylor orders can be bounded by C T², giving work<=C T^20. PC6 gamma gives the same bound. Saddle contraction adds at most C T² iterations, giving T^22; the moving phase inverse adds at most another C T² iterations, giving T^24. Profile partial-integral/normalizer evaluation uses O(P_nu³) nodes, each with the stated elementary bound; since SI16 gives P_nu<=C T, this fits T^23. Constant-order normalized F/B/E and mixed first-time algebra adds a fixed number of gates, fitting T^40 with slack. As in PC13, flat endpoint tails avoid inverse-distance work. Direct source/model log and exp providers use actual polynomial logarithmic caps and stable negative exponentials; nested exponential overestimates are not used.

The phase/root acquisition loops and O(ell) collar labels fit T^44 even if generously overcounted. Note58 AC18 adds source-construction work<=C q_s^60 **once**, including modes, coefficient precision, conversion/squaring and source rounding; its upstream fixed recipe inputs remain as stated there. Node count<=C T^13 times SI18 gives T^53. These costs and exact weights/sums/post-filter operations fit SI2's T^80. No descriptor or source is refined when only p changes.

For storage, AC18's K_int<=C q_s^5 and operand cap C K_int^4 can be implemented with at most C K_int² stored operands, giving C q_s^30. The evaluator's common-denominator source series, rational weights, root list and streaming quadrature need smaller powers. T^32 is a sufficient common storage allowance. Store only sources and small records in the repository; an executed large derived grid would follow LARGE_FILES.

## 6. Comparison, controls and disposition

At the **same unchanged tuple/domain/evaluation target**:

| Consumer | Paid result | Remaining scope limit |
| --- | --- | --- |
| Note61 PC1 | Polynomial extra accuracy bits at fixed descriptor/query box | Fixed constants may contain expanding inverse-q smoothness factors |
| Note71 WF13 | Explicit outer-q-inverse-free finite primitive consumer | Uniform-grid h=O(e) generally costs O(e^-6) |
| Present SI2/SI14 | Polynomial joint numerical height/source-demand/accuracy cost for the fixed t64 family restricted to J95–97; source/phase/root/providers charged | Enormous fixed constants, no implementation/crossover, no uniform b/time/global-query theorem |

The concrete improvements are logarithmically many dyadic levels rather than a uniform h-grid, area-scaled pole cancellation before quadrature, and a carrier/cancellation bit ledger for the actual algorithms. The canonical source, regulator, spatial kernel, physical tuple, residuals and means are preserved.

The theorem must allow the repository's collision controls when their local geometric premises hold. It proves no favorable sign. A multiple root fails the outer simple-unit premise, so the fixed central floor remains. Canonical application uses the complete theta source: Euler-factor controls change it; weighted-square/finite-prime controls lack its complete coefficient/reflection data; reflected shape/positive-primitive controls lack that identity; atomic/polynomial heat controls lack the complete smooth source. These source-premise differences do not themselves exclude a collision or validate an RH application.

**HDA-17 remains Partial, HDA-18 Gated and HDA-20 unfulfilled.** The bounded r2 joint-cost problem closes at this family/scope, with same-model assessment only. No theta/source/model/root values, source coefficients, interval certificate or symbolic research checks were executed. Source pins and link/size/hash checks are housekeeping. No manuscript, snapshot, commit or other-chat dispatch was performed.

**Next: Analysis — Sol.** Continue AN06 r3 at pure-P exterior query scope, where no active G source is evaluated: determine whether logarithmic carrier/phase formulas and saturation-aware weight bounds reduce query dependence from numerical R to log R and requested p. Retain full tuple/root/filter costs and the separate global source-construction payment. Return a complete sharper query bound or its first explicit failed derivative/margin payment before proposing a pilot. A full all-time/all-height cost theorem and an independently assigned inherited-chain audit remain separate.
