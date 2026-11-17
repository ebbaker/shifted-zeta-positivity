# VCD-GT-B04 — Complete-source acquisition on a close-pair tube

16 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance, chat0002. Lead actual recorded model/effort unavailable. Fixed analytical/numerical helpers will be explicitly dispatched gpt-6.1-sol / ultra, not separate backend attestation.

**B decision: select a bounded complete-source acquisition and matched comparison.** Recommended Astra/ultra because the input mechanism and useful case were not previously selected. This is a finite quantitative diagnostic/application, not an RH-equivalent criterion or a claim of new zero coverage. Read [results](../../../../../../result-summaries/README.md), [controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md), [approximation18](../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md), [avoid](../../../../../../avoid/README.md), especially [01](../../../../../../avoid/01_restating_the_target.md), [02](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [10](../../../../../../avoid/10_numerics_ahead_of_the_question.md), [11](../../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md), [12](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [15](../../../../../../avoid/15_ignoring_sibling_results_and_unfinished_closures.md).

## Proposals and the selected new input

**A, selected:** evaluate the complete physical theta field through its exact time-zero xi function and an imaginary Gaussian convolution. For real \(t\ge0\),
\[
 H_t(z)=\frac1{\sqrt\pi}\int_{\mathbb R}e^{-r^2}H_0(z+2i\sqrt t\,r)\,dr,
 \qquad H_0(z)=\xi((1+iz)/2)/8 .
\]
The source Fourier representation proves this by the Gaussian moment-generating identity and Fubini; E08 will give the complete proof and an explicit usable quadrature/tail budget. This uses the full canonical source, not just its generic quadrature law. Multiplication by the fixed positive gauge \(\exp(\pi a/8)\) is permitted for numerical conditioning and does not change c,D,K.

The one candidate is the classical first Lehmer pair, near physical coordinates 14010.125732 and 14010.201129 at t=0. Freeze \(a=140101/10\), circle radius \(\rho=9/10\), and \(I=[0,1/10]\). These are proposed acquisition inputs, not a certified tube or an inferred positive-time anchor. The outer count, modulus, pair location/buffer and incoming gap at v=1/10 must be tested/acquired. No global numbering or all-real slice premise is required.

The unmet comparison is the signed budget
\(B=2\int_0^v\exp(4\int_t^vK)\,dt\)
against the same budget with \(|K|\), and against direct D(0) using all the same full-source measurements. A tight time-zero gap makes the sign retention consequential over this finite interval. A positive numerical difference is only floating feasibility until its complete spatial/time/source errors are paid.

**B, disposed without new execution:** use all canonical adjacent score identities as a sign input by themselves. Parent [E08](../../../notes/08_VCD_E08_FULL_SCORE_RIGIDITY_20261116.md) already proves source identification, not a quantitative Fourier/gap margin. Finite-score controls and the unresolved signed readout are retained. Renaming the same unproved inequality supplies no new execution packet.

## Prior stop respected

The [OA Lehmer decision](../../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/03_collision_constraints/notes/08_TND_OA_B03_LEHMER_DIRECTION_AND_ACQUISITION_STOP_20261109.md) found no positive-time certificate or credible evaluated source budget in the inspected references. It also proved that an *upper* exterior inverse-square sum gives the wrong force-bound direction for survival. This work does not import that sum with reversed sign, infer an anchor from time-zero roots, or change the OA register. The proposed new acquisition route is the complete xi convolution, with derivative-free contour logarithms and explicit source-tail payment. E08 must establish its budget; E04 can test feasibility and must report any failed count/cost/payment gate. This is not a claim that the literature already certifies I.

## Fixed contour consumer

If the acquired count is two and H is nonzero on a collar, define a periodic collar log
\(L(z)=\log(\exp(\pi a/8)H_t(z)/(z-a)^2)\).
With \(w=z-a\), normalized contour averages on the circle give
\[
 p_1=-\langle wL\rangle_\theta,\qquad
 p_2=-2\langle w^2L\rangle_\theta,\qquad
 c=a+p_1/2,\quad D=p_2/2-p_1^2/4,
\]
\[
 K=\left\langle\frac{2w(z-c)L(z)}{((z-c)^2-D)^2}\right\rangle_\theta .
\]
The rational factor's contribution from \(2/(z-a)\) integrates to zero. E08 will check every factor and branch convention. This avoids root-slope denominators; it does not remove count/modulus/buffer obligations.

## Finite follow-through and gates

E08 r1 (E, Sol6.1/ultra) derives the source oracle, explicit infinite-grid/tail bounds using xi/gamma/zeta inequalities with exact cited premises, and the log-contour consumer/error interface. No root acquisition in this analytic task.

E04 r1 (E, Sol6.1/ultra) implements one canonical candidate and the exact quadratic control. Use two fixed levels: 160 and 224 bits; source lattice h=1/3 and 1/4, truncation |r|<=12; contour 64 and 128 nodes; time Chebyshev-Lobatto grids 16 and 32 subintervals. Field evaluation and all numerical coding belong to the helper. Conditional rigorous payments from E08 must be distinguished from floating grid/precision agreement. Keep individual zeros unordered; compute moments/K from a consistent contour log. Report source and geometry gates, signed/absolute costs, W(0), normalized transported estimate and direct D(0), with cost counts/runtimes. No wider source, tube, degree/precision scan or new pair is authorized. An implementation failure gets bounded diagnosis; a failed mathematical or resource gate returns to B04/B05 with the evidence.

If the first level is infeasible, do not automatically launch the expensive level. Benchmark source throughput and estimate the fixed packet's work before full acquisition. If source quadrature does not meet the needed uncertainty, return to the lead rather than treating stability as certification. Certification beyond the packet needs a revised finite contract; no whole-time claim from samples.

E05 r5 will assess the returned proofs, code/records and synthesis in a pinned batch. Root owns shared integration/history. No Jacobi coefficient family is acquired: a “same first N links” comparator is not asserted for this source-oracle test. Give the direct source endpoint method all shared oracle data.

## Controls and scientific boundary

The exact quadratic has K=0 and consumes its gap at the collision. Its contour pipeline must reproduce that; no false passage through its event. The positive-source controls retain their own literal heat-convolution identity, but their time-zero transform is not the unchanged canonical xi formula. Weighted-square controls fail full reflection/equal coefficients and have no all-real threshold; this is not asserted to make an untested inequality fail. Euler translates, reflected, smooth/primitive, finite-prime, atomic/compact and RH-conditional endpoint controls retain their distinct source/domain premises from controls12 and Note06. No all-real exterior-zero representation is used. A canonical local positive margin, if certified, would remain a finite known-pair result and not exclude all theta collisions or establish a new Newman bound. A losing comparison is scoped to this one complete-source packet.

