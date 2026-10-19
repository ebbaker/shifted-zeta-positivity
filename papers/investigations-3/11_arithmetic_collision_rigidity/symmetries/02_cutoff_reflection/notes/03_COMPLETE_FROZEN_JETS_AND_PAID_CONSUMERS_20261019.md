# S02-T2: complete jets, Schur-coupled physical tests and S03 handoff

19 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. **gpt-6.1-sol (Codex), actual reasoning effort ultra**, verified from root session metadata. Separate delegated mathematical, code and control checks are internal same-model LLM review; no specialist review.

**Outcome.** Complete value, first and second jet enclosures now cover every closed cell of B. Both the selected frozen family and the coherent full formula certify the first jet and L0>E/100 on all 4,096 cells when the residual's real Schur coefficient constraints are retained. Independent residual boxes certify that signed inequality on only 1,770 frozen cells. However, the **full formula gives a stronger complete first-jet lower bound** than the frozen family, and the fresh complete-source consumer gives a substantially stronger bound than either. S02-T2 is complete as an evaluated interface, correlation-aware finite certificate and bounded consumer comparison. No new region or advantage over the strongest complete-source consumer is claimed. C is not activated.

The [T2 contract](../../notes/03_S02_COMPLETE_JET_EVALUATION_CONTRACT_20261019.md) fixes the domain, comparison, stopping rule and storage policy. [S02 Note 02](02_MATCHED_FROZEN_AND_ANALYTIC_CORRECTIONS_20261019.md) supplies the source-pinned complete analytic residual allowances and the earlier frozen/full comparison. Its frozen selection concerned disk error envelopes; this execution assesses actual paid consumers and preserves that distinction.

## 1. Fixed domain, representation and closed-cell evaluation

Use B=[1/100,1/5] x [999,1001], N=8 and disk radius R=1/2. The unchanged S03 geometry has 32 equal closed time slabs and 128 equal closed spatial cells, with exact rational seams and 4,096 cells in total. There is no adaptive refinement or height scan. Retained runs use 192 and 256 bits. C remains a separately declared, unexecuted stage because no strongest-consumer advantage motivates extending this evaluation.

Let k=pi/8, A be the original nonvanishing symmetric normalizer, Q=H/A, b=(log A)_x, omega=theta_x and omega_x=partial_x omega. All physical derivatives keep the integer cutoff fixed. The frozen family at center X holds its correction coefficient fixed while differentiating in z:

\[
 F_{fr,X}(t,z)=\frac{G_8(t,z)-C_8(t,X)e^{-k(z-X)}}{A(t,z)}.
\]

The full formula F_an=(G8-C8_an)/A is one coherent analytic function. From the matched record, the complete Q-disk allowances on B are

\[
 \eta_{fr}<0.226298331,\qquad \eta_{an}<0.226299246.
\]

These include the complete two-sum error, corrected published residual and paid holomorphic continuation; there is no natural-cutoff transition on B. The current source pins of that record and its generating code are checked before use. The published approximation theorem remains an imported analytic input. No new numerical source truncation or quadrature is introduced into these arithmetic formulas.

The [evaluator](../numerics/evaluate_complete_frozen_jets.py) retains every mode 1–8 in the stable normalized sum

\[
 G_8/A=2\Re(e^{i\theta}P),
\]

and differentiates the complete P, its phase and normalizer. It uses the exact P, Px and Pxx formulas from the existing S03 implementation. Phase is recentered at a cell midpoint using the true omega derivative at fixed t, to avoid unnecessarily wide subtraction of large phases. No source channel or mixed derivative is dropped.

Every returned jet image is an outward enclosure over the entire closed t/x cell. Its image radius includes both genuine parameter variation and arithmetic rounding; it is not described as rounding error alone. Separate exact-point/input-rounding radii at x=999,1000,1001 are retained in the small record, together with agreement against direct analytic series at all three points. The residual payment (eta,2eta,8eta) is added to these exact-approximant images. Archive rows also expose physical jet images and all physical return allowances.

## 2. Frozen-family derivatives and paid midpoint propagation

Write q=B_t exp(-kX)/A(X), c=qJ8(X), u=qJ8'(X), and h=k+b. For the local frozen Q jets f0,f1,f2,

\[
 \partial_Xf_0=f_1-u,\qquad
 \partial_Xf_1=f_2+hu. \tag{1}
\]

Thus the frozen jets are not the derivatives of their diagonal center-value function. Treating them as a coherent analytic jet would omit actual terms, even though the two formulas agree in value at each center. The evaluator verifies (1) by independently differentiating analytic series.

Set W=f0-i f1/omega and Rloc=f0+f2/omega^2-omega_x f1/omega^3. Along the diagonal family,

\[
 \partial_XW=i\omega(W-R_{loc})-u(1+ih/\omega). \tag{2}
\]

Rloc is a local-jet expression, not a global rotation defect of the changing-center family. The complete derivative payment used for midpoint propagation is

\[
 |\partial_XW|\le |\omega|(|W|+|R_{loc}|)
 +|u|\sqrt{1+(h/\omega)^2}. \tag{3}
\]

The second term is paid on every frozen cell; its maximum is below 0.003313926. For the coherent full formula it is absent. The midpoint norm minus half-width times this uniform derivative bound supplies a second valid radius lower bound. The code takes the better of that bound and direct rectangle norm evaluation, using Acb's rectangle modulus lower bound. This changes neither the grid nor the analytic source data.

The complete first-jet residual payment in J=(Q,-Qx/omega) coordinates is

\[
 e_J\le\eta\max\{1,(R|\omega|)^{-1}\}. \tag{4}
\]

This follows from the disk's first two coefficient constraints, not independent error boxes. It is subtracted once from the approximant radius. The code also evaluates the real Schwarz–Pick necessary condition for a joint zero, in division-free form:

\[
 f_0^2+\eta R|f_1|-\eta^2\le0.
\]

A strictly positive lower bound excludes a joint zero. The source-neutral helper handles eta=0 separately and never divides by a zero allowance.

## 3. Physical return and the complete second-jet correlation

The exact physical return is

\[
 (H,H_x,H_{xx})/A=(Q,Q_x+bQ,Q_{xx}+2bQ_x+(b^2+b_x)Q).
\]

In particular,

\[
 L_0/A^2=Q_x^2-QQ_{xx}-b_xQ^2,\qquad
 E/A^2=Q^2+(Q_x+bQ)^2. \tag{5}
\]

The b^2 terms cancel in L0; the evaluator uses (5), retaining that correlation rather than first expanding independent physical component boxes. All normalizer derivatives and signed mixed terms remain present.

Independent componentwise Cauchy boxes are valid but discard further information: the same analytic disk residual supplies all three errors. The following self-contained two-step Schur argument provides a complete enclosure of their joint class.

For a fixed real t,X, let r=(H-G8+C*)/A(z), where C* is that disk's chosen holomorphic correction, and put g(w)=r(X+Rw)/eta. Then g is analytic, real-symmetric, and |g|<=1 on the unit disk. Let a=g(0), real. If |a|<1, the disk automorphism and Schwarz lemma make

\[
 g_1(w)=\frac{g(w)-a}{w(1-ag(w))}
\]

another real-symmetric Schur function. Put beta=g1(0). A second Schwarz step gives g1'(0)=(1-beta^2)gamma for a real gamma in [-1,1]. Expanding the inverse g=(a+w g1)/(1+a w g1) yields

\[
 g_0=a,\quad g'_0=(1-a^2)\beta,
\]
\[
 [w^2]g=(1-a^2)\{(1-\beta^2)\gamma-a\beta^2\}.
\]

If |a|=1, g is constant. If |beta|=1, g1 is constant. The same coefficient formulas extend to both boundary cases. Hence every permissible real residual jet belongs to

\[
 r_0=\eta a,\qquad r_1=2\eta(1-a^2)\beta,
\]
\[
 r_2=8\eta(1-a^2)\{(1-\beta^2)\gamma-a\beta^2\},
 \qquad a,\beta,\gamma\in[-1,1]. \tag{6}
\]

The factor 8 includes the second derivative's factorial and R=1/2. The method does not choose the three errors independently or assume a physical sign. It evaluates (5) on f+(r0,r1,r2) over a fixed closed 8-by-8 rational cover in a,beta and the full unsplit gamma interval [-1,1]. Every physical cell therefore receives all 64 residual parameter boxes, or 262,144 boxes per formula. These are interval boxes with complete coverage, not point samples or an optimization over favorable residuals. The fixed parameter mesh was selected after a delegated feasibility diagnostic and before the retained implementation; it is not represented as independent preregistration.

This proves a uniform physical lower bound from the declared source allowance without requiring more source information. The independent-box comparison remains visible to show what the coefficient correlation contributes.

## 4. Paid results and strongest comparisons

The [small execution record](../numerics/S02_COMPLETE_JETS_20261019.json) contains both precisions, 32-slab ledgers, extrema, exact checks, setup costs and external table identities. Conservative lower bounds valid at both precisions are:

| Complete result on B | Frozen local jets | Full coherent jets | Fresh complete-source reference |
| --- | ---: | ---: | ---: |
| Phase-scaled first-jet radius | >0.9686625938 | >0.9702739184 | >1.3473946960 |
| (L0-E/100)/A^2 | >0.2747031086 | >0.2780996132 | >3.0153583623 |
| Complete signed cells | 4096/4096 | 4096/4096 | 4096/4096 |

The maximum phase-jet residual allowance is below 0.413732966 for frozen, below 0.413734640 for full, and below 2.349e-10 for the fresh complete-source reference. These are paid analytic/source errors, separate from cell image widths. The source-informed reference uses additional complete-source midpoint data and is identified as a different information class.

For the frozen formula, independent Q-error boxes give L0>0 on 2,169 cells and L0>E/100 on only 1,770 cells; the complete real-Schur enclosure gives both inequalities on all 4,096. The corresponding full-formula counts are 2,197 and 1,789, then 4,096 under (6). The failed box tests are inconclusive tests, not evidence of a negative theta quantity or failure of the disk source information.

Although the frozen eta is slightly smaller, its evaluated first-jet radius is weaker than the full formula's on this cover. Its different local derivatives and the extra diagonal payment matter. **The T1 envelope choice therefore does not remain the best paid consumer choice.** Keep the full coherent formula for S03 and the frozen interface for local disk/correlation applications. The older analytic-only bound >0.967290 and source-informed bound >1.336516 remain historical reference computations. The fresh full-formula and source re-evaluations improve these displayed lower bounds through their enclosure/phase evaluation, not through a new arithmetic residual theorem. Neither an existing-box pass nor the higher precision is called new coverage.

The fresh reference rebuilds the original complete reflected-source midpoint setup once per precision, paying its quadrature radii, retained-source and mode tails, Taylor propagation and fixed Gc return. Its setup uses the original 60-second/two-million-callback bounds and about 173,700 callbacks. That cost is recorded, not hidden. The inherited setup's 512-call field belongs to the old adaptive consumer; this task explicitly declares 4,096 direct enclose calls on the fixed cover. No factor-two timing or matched-cost experiment was selected, so no speed claim follows from these records.

Both precisions give the same positive gates and counts. Some conservative lower endpoints differ slightly because outward interval radius arithmetic can change with precision. They need not overlap: they are lower bounds, not enclosures of one exact optimizing scalar. A separate fresh 192-bit replay matches the retained mathematical cell content exactly.

## 5. Direct and S03 interfaces; storage

The importable ClosedJetEvaluator.enclose(t0,t1,x0,x1) accepts only closed cells within B and returns both exact-approximant jet images, physical return data, analytic error payments and consumer metrics. Its frozen output explicitly supplies the diagonal derivative defects from (1). Its full output is the coherent analytic formula required by S03's shared residual construction. Exported phase data include theta, signed omega, omega_x, b,b_x and chi=Gc/A. Source reference jets and all their individual budgets are available in every external row.

For S03's analytic residual or coefficient subtraction, use the full output and eta_an. Frozen local jets can support direct disk tests, but cannot replace derivatives of the shared full analytic approximant. A consumer that uses their variation must include (1)–(3). Neither the normalized residual nor a center-varying frozen family is propagated by the unmodified heat equation.

The full 4,096-cell tables exceed the repository size policy and live outside Git. [ARCHIVES.md](../ARCHIVES.md) records their exact paths, stored and canonical-content hashes, sizes, normal-path/environment lookup and portable regeneration. The canonical content hash covers sorted-key cell rows in fixed time/space order, excluding the header's observational acquisition times. It is independent of compression and those timings; the stored hash identifies the complete gzip including its header. Matching data hashes identify the tested enclosures, not a proof or guaranteed cross-environment arithmetic identity.

load_cell_archive checks stored identity, all canonical mathematical cell content, row count, producer hash and source pins before exposing data. Each row order is checked before yielding that row. A missing archive fails closed with regeneration guidance. Parsed numeric strings are conservative outward enclosures, not exact-dyadic identities. The small summary, code, review and archive guide remain below 1 MiB; no manuscript snapshot is created.

## 6. Validation and disposition

[Review 03](../reviews/03_COMPLETE_JET_INTERNAL_REVIEW_20261019.md) supplies a separate same-model derivation/code audit and [fresh 192-bit replay](../numerics/S02_COMPLETE_JET_REVIEW_REPLAY_192_20261019.json). Exact-series checks verify both jet conventions and frozen diagonal corrections; the separate algebra/code audit verifies the physical return. Analytic polynomial/Schur residual fixtures contain a genuine joint event and must fail strict acceptance; boundary Schur parameters and coefficient-normalization mutations are checked.

The [fresh source-specific control record](../numerics/S02_COMPLETE_JET_CONTROLS_20261019.json) sends each event's own complete jet balls through the **new** first-jet and Schur signed-test helpers, with their already-paid uncertainty and no theta constants. All five event boxes fail strict acceptance; the Euler p=41 witness fails the signed claim. These controls validate the new acceptance interfaces and error handling, not the imported theta approximation theorem.

Finite-prime and finite weighted-square controls lack the complete normalized reflection/coefficient premises. Reflected super-Gaussian and smooth positive-primitive controls lack the exact unchanged theta integer-square expansion. Euler-factor controls lack unchanged level-one source data. Generic heat, rotation or geometric identities do not provide the theta arithmetic remainder constants. Finite-prime/smooth-primitive existence constructions supply no effective event boxes here; their role remains an analytic premise screen. Controls may pass a valid local certificate on a collision-free box.

Classify this as **complete closed-cell interval evaluation and a Schur-coupled finite certificate on an already covered domain**, with a scoped practical no-advantage result for the selected frozen family against the strongest consumer. It is not a universal failure of frozen corrections or a global nonvanishing reformulation. The retained useful output is the coefficient-aware physical test and reusable, correctly differentiated interface. S02-T2 is Complete on B; stop this bounded evaluation. Do not activate C or EXT-01 without a concrete strongest-consumer benefit. S03-T1's separate arithmetic residual derivation remains Ready.

The real bridge 1001<|x|<exp(2000) on the stated time slab and the global complex exterior remain open. Follow the [result summaries](../../../../../../result-summaries/README.md) and [patterns to avoid](../../../../../../avoid/README.md), especially [collision controls](../../../../../../result-summaries/12_collision_controls_and_screening.md), [preserving cancellation](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), [normalization](../../../../../../avoid/08_normalization_and_constant_slips.md), [scoped exclusions](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [target reformulations](../../../../../../avoid/01_restating_the_target.md).
