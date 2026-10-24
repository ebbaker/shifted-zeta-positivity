# Conserved heat contours: results, accomplishments and remaining obstacles

24 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model: **gpt-6-astra (Codex)**; reasoning effort: **max**. This is a single-assistant internal review, not independent specialist refereeing or formal verification. This conversation is **Review conserved-contour results**, uniquely registered as brainstorm history **0009**, thread `01a16dfd-bc51-7251-91aa-4d3d6a8db609`.

The main advance is a proved RH-conditional outer contour, followed by a complete comparison close to the real axis that permits multiple zeros. The work now has analytic estimates where earlier versions had only a proposed contour or a conditional transfer mechanism. It has not obtained a new simple-zero proportion or proved that RH implies simplicity. The central missing ingredient is a quantitative property of the actual theta field that restricts multiplicity and is not shared by the explicit field with no simple zeros.

This review concentrates on [book.tex](../../manuscript/book.tex), the [arithmetic-inside-contours overview](../../research-overview/04_ARITHMETIC_INSIDE_CONSERVED_CONTOURS_PROGRAM_20261023.md), its [progress register](../../research-progress/04_ARITHMETIC_INSIDE_CONSERVED_CONTOURS_PROGRESS_20261023.md), and [main Note 19](../../notes/19_NEAR_AXIS_CLUSTER_AND_QUADRATIC_EXTERIOR_20261023.md). It also reads the broader manuscript modules and the recent supporting notes. The earlier relative-flux draft is historical; the fixed-offset dated draft is byte-identical to the maintained book. The standards are the [result index](../../../../../result-summaries/README.md), [local heat-geometry summary](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [avoid index](../../../../../avoid/README.md), and specifically [target classification](../../../../../avoid/01_restating_the_target.md), [shared-premise screening](../../../../../avoid/02_shape_only_arguments_and_the_controls.md), and [scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md). This assessment adds no theorem and changes no goal status.

## What the book establishes

**A complete comparison with an acquired nonvanishing bound.** Write \(F(z)=H(0,z)\), \(p=F'/F\), and \(L=\log Y\). Book Theorem 1.1 assumes RH with all multiplicities allowed. At a fixed positive distance from the real axis, for every fixed \(c>0\) and real \(0\le s\le c/L^2\), it proves

\[
\frac{H(-s,z)}{F(z)e^{sp(z)^2}}
=1+sp'(z)(1+2sp(z)^2)+O(L^{-2}).
\]

The significant point is the normalization. At large height the xi field is extremely small. An absolute error that tends to zero can still exceed the entire field. The proof instead bounds the full Gaussian tail after division by \(F\), retains the complex leading exponential, and obtains a relative error. This earns nonvanishing and spatial derivative estimates before using \(H_z/H\). It does not assume the moving zero-free region it intends to construct. The constants depend on the fixed strip and \(c\); the theorem supplies no numerical starting height, complex-time extension, or uniform passage of its floor to the axis.

**Actual conserved contours with controlled geometry.** Book Theorem 3.1 turns that analytic estimate into a continued graph. Over the real time interval of length \(c/L^2\), its position and tangent change by \(O(L^{-1})\); fixed end extensions ensure coverage of the target height band. The graph stays in a finite buffer and moves upward as time runs backward. It preserves \(H\,dz\) and the image under the canonical primitive. These statements resolve existence, graph shape, containment and coverage at the stated scale. The conservation law alone had not supplied those estimates.

**An exact connection to endpoint multiplicity.** A real zero of multiplicity \(m\) receives \(2\lfloor m/2\rfloor\) nonreal labels immediately before its heat collision. The moving-window balance counts that cost, the nonreal population already present, and each inward and outward crossing. With a window covering the endpoint band, the acquired outer corridor removes the upper and lower transition flux. What remains is

\[
\mathcal R_Y=N_{\psi_Y,\mathrm{nr}}(-S)
  +\mathcal F^+_{\mathrm{ends},\mathrm{nr}},\qquad
S=c/L^2,
\]

\[
D_Y\le\mathcal R_Y,\qquad M_Y\le\tfrac32\mathcal R_Y.
\]

Here \(D_Y\) is excess multiplicity and \(M_Y\) counts all labels at nonsimple sites. Both constants are sharp for the general finite balance. A fixed wall in the same zero-free corridor removes the same transition terms. Thus the analytic nonvanishing region is what pays that part of the resource; conservation does not supply an additional smallness estimate.

The resulting implication is quantitative. If \(N_Y\) counts all endpoint labels and an additional estimate gave \(\mathcal R_Y\le\alpha N_Y\), the simple fraction would be at least \(1-3\alpha/2\); a positive lower fraction requires \(\alpha<2/3\). A bound \(\mathcal R_Y=o\(N_Y\)\) would give density-one simplicity on the covered bands. A window covering a particular site with resource below two would exclude a multiple zero there. None of these resource bounds has been acquired. Density-one and every-zero simplicity also remain distinct conclusions.

**Complete-field formulas for the resource.** The appendix identifies the nonreal population and one-sided current with ordered limits of regularized integrals of the full field. It accounts for collisions without excess current concentrated at an event. This makes the quantities available to analysis without assuming individually separated root tracks. The result is for each fixed analytic field and smooth window: the regulator limit precedes the near-real cutoff limit. Uniformity in height, growing cluster degree, or regulator-dependent windows requires further estimates.

## What the newest near-axis note adds

[Note 19](../../notes/19_NEAR_AXIS_CLUSTER_AND_QUADRATIC_EXTERIOR_20261023.md) extends the domain in which a complete comparison is proved. It retains every zero, including multiplicities, in a fixed-radius local cluster \(P\), and writes the remaining factor as \(U\). The reference retains both \(A=(\log U)'(0)\) and the exterior curvature \(B=(\log U)''(0)\le0\). Its Gaussian integral is an explicit transformed polynomial times a quadratic exponential.

For \(|w|\le K/L\), real \(s\le c/L^2\), and degree \(m=O(L)\), the note proves

\[
|H(-s,a+w)-Q_s(w)|
\le C\left(\frac{(m+1)^{3/2}}{L^2}+e^{-\kappa L^2}\right)
\mathcal E_s(w).
\]

The envelope \(\mathcal E_s\) is the integral of the absolute value of the model integrand. The coefficient is \(O(L^{-1/2})\) at the permitted largest degrees and \(O(L^{-2})\) at bounded degree. The full exterior product pays the complete tail; no lower bound on the cluster polynomial, model or actual field is assumed. Consequently the theorem remains meaningful through the possible multiple zero being investigated.

Retaining curvature fixes a demonstrated approximation loss. For the declared real-rooted polynomial family \(v^m(1-v^2/R^2)^n\), with both \(m,n\asymp L\), the linear-exterior model has an order-one relative error. The quadratic model captures the limiting factor. This obstruction concerns that growing-degree information class; it is not a theta counterexample or an exclusion of approximations with additional arithmetic information.

The next limitation is precise: a small error relative to \(\mathcal E_s\) need not be small relative to \(|Q_s|\), because the model integral can cancel. A zero-count comparison on a chosen contour would require a corresponding model-boundary margin, or another justified method. Even that transfer step would still need a multiplicity-sensitive conclusion about the actual cluster. Note 19 supplies neither a zero-count restriction nor a bound on \(\mathcal R_Y\).

## Why the arithmetic obstacle is substantive

The book constructs, under RH,

\[
G_0(z)=F(z/2)^2\left[1+\cos\left(\frac{\log2}{4}z\right)\right].
\]

Every zero has even multiplicity, so this field has no simple zeros. Nevertheless it has a positive even rapidly decaying Fourier source, the same two leading zero-count terms, the logarithmic bounds used by the book, the Gaussian comparison, and the conserved material graphs. It also satisfies the new near-axis comparison. For its real near-axis model, the absolute envelope even equals the positive model value, so the missing discrimination cannot be attributed only to a loose error norm.

The exact canonical theta source is absent from this control. A successful argument must use that difference in an inequality that changes the multiplicity bound. Merely invoking the canonical source while consuming estimates also true for \(G_0\) does not do so. This is a limitation on the stated coarse information, not an impossibility result for theta arithmetic.

The other [registered controls](../../../../../result-summaries/12_collision_controls_and_screening.md) must be screened at their actual hypotheses. Euler-factor controls with parameter below one have added nonreal initial zeros and fail the initial all-real premise; the all-real versions can pass these generic transfers. Finite weighted-square controls fail the all-real initial slice by the finite-source audit. Reflection or positive-primitive data alone do not establish the complete product/count hypotheses for the other families. Their unverified hypotheses are not a claimed rejection by the new estimate. The admitted all-multiple \(G_0\) is the decisive control for the present inference.

## Supporting results and their roles

| Result | What it accomplishes | Remaining limitation |
| --- | --- | --- |
| [Hermite domination, brainstorm Note 12](../notes/12_HERMITE_CLUSTER_DOMINATION_AND_JOINT_CONSUMER_20261023.md) | Promotes the full endpoint spectral cost to every permitted positive time: \(q(t)\ge\sum_a(m_a-H_{m_a})\). The joint bound \(M\le5\mathcal R/8+3q/2\) can improve using either input alone. | No canonical upper bound on \(q\) or \(\mathcal R\); the complete real-root motion is required. |
| [Complete-xi Euler anchor, brainstorm Note 13](../notes/13_COMPLETE_XI_LOGARITHMIC_HEAT_ANCHOR_20261023.md) | Acquires an exterior nonvanishing anchor on negative-time widths of order \(1/\log Y\), improving the particular exponentially small absolute-source continuation bound. | Its offset lies in the Euler region, outside the near-zero problem. It does not bound the complete collision resource; it uses an established Gaussian/Dirichlet mechanism and makes no priority claim. |
| [Discrete arithmetic tests, brainstorm Notes 14–15](../notes/15_BROADER_MOLLIFIER_TESTS_AND_CONJUGATE_MOMENT_20261023.md) | Report no leading gain for specified strongly smoothed fixed prime-rank directions and a normalized inverse-square coefficient test. These results narrow concrete candidate classes. | They do not exclude arbitrary mollifiers, growing families or other observables. The conjugate route still lacks its holomorphic-square moment estimate. No new simplicity percentage follows. |
| [Forest and coefficient methods](../../manuscript/spectral_forest.tex) | Encode collision multiplicity in a bounded spectrum and propagate complete polynomial coefficients without individual inverse-gap denominators. | Denominator margins, degree growth and heat-scale coefficient precision remain. A transfer formula is not an acquired small filter. |
| [Finite theta certificate](../../manuscript/finite_certificate.tex) | Certifies the complete two-root population and simplicity on the specified low-height box, including its complex-time square. | It is a finite calibration. The matched direct terminal calculation is tighter; no growing-height consequence is obtained. |
| [Complete physical-cap comparison](../../manuscript/contours.tex) | Pays all faces and the spatial complement of the declared finite experiment. | Both certified lower endpoints are negative and the deformed interval is slightly wider; it demonstrates no positive cap bound or contour advantage. |

The statistical-mechanical forest interpretation identifies an exact mean and variance for a finite ensemble; it does not establish a thermodynamic phase transition. The Noether and Fourier conservation hierarchy gives exact structural identities. Its existence is compatible with collisions, so it cannot replace the missing arithmetic estimate.

## Assessment of the program and the next advance

The requested overview and progress register accurately separate the completed fixed-offset wall from the unbounded interior resource. Their appended near-axis checkpoint correctly records supporting transfer progress while leaving the arithmetic and simplicity goals open. The natural next advance is one of the two estimates they identify: an actual bound on the complete earlier-mass/end-influx resource, or a multiplicity-sensitive estimate for the true cluster and its exterior factor. A different observable remains legitimate if it gives a stronger result.

For the resource route, earlier mass and one-sided end influx must remain together in the proof; small signed net flux or a small end term alone is insufficient. For the cluster route, the complete approximation error and model cancellation must both be controlled. Either route needs a step that distinguishes \(G_0\), and any cumulative or every-zero statement needs the appropriate height coverage and treatment of exceptions. Improved generic geometry by itself does not discharge these obligations.

## Review findings and verification scope

No blocking mathematical gap was found in this reading of the book's main comparison, material graph, collision balance, or Note 19's comparison. The checks followed the relative tail normalization, complex Gaussian moments, finite-buffer continuation, velocity distinction, endpoint multiplicity constants, translated exterior product, polynomial Gaussian envelope and growing-degree error. This is internal review, not a claim of exhaustive verification.

Two previously reported auxiliary-manuscript defects remain:

1. In [transport_reference.tex](../../manuscript/transport_reference.tex), lines 103–105, the intended hypothesis \(G(u,w)\ne0\) is corrupted into a line break followed by `e0`. The following quotients require nonvanishing on the entire time-wall cylinder. Restore the displayed condition before circulation.
2. [outlook.tex](../../manuscript/outlook.tex), lines 24–39, and the provisional framing in [conserved_contours.tex](../../manuscript/conserved_contours.tex) lag the book's completed fixed-offset theorem. They should refer to its precise scope while retaining the unresolved near-axis and arithmetic obligations. Historical notes referring to the former book title should be read against the preserved relative-flux draft.

The classical product/count normalization was checked against [Elkies's notes](https://people.math.harvard.edu/~elkies/M259.06/zeta2.pdf), and the heat normalization against [Polymath](https://arxiv.org/html/1904.12438v2). The appendix's imported root regularity matches [Parusiński–Rainer, Theorem 1, printed page 1344](https://math.univ-cotedazur.fr/~parus/publis/ens.pdf): its admissible exponent and coefficient hypotheses support the finite-chart application, with no uniform high-height conclusion. The digamma anchor agrees with [DLMF 5.11](https://dlmf.nist.gov/5.11). These are checks of the imported statements, not new audits of those published proofs. The long arithmetic moment derivations in Notes 14–15 were assessed through their statements and existing internal reviews, not fully rederived in this turn.

An independent exact-factorial-moment computation reproduced all five rational rows of the [quadratic-cluster diagnostic](../../numerics/10_QUADRATIC_CLUSTER_DIAGNOSTIC_20261023.json). At \(L=256\), full/linear is approximately \(0.6056409124\), whereas the quadratic model's relative error is approximately \(0.0004926076\). These are polynomial-control data, not theta-zero evidence. All 16 manuscript files match the hashes in the preceding review receipt. No manuscript was edited, no PDF was rebuilt, and the earlier Arb certificates were not rerun or renewed. The [small review receipt](../numerics/16_REVIEW_CHECKS_20261024.json) records this scope. No commit or new manuscript snapshot was created.
