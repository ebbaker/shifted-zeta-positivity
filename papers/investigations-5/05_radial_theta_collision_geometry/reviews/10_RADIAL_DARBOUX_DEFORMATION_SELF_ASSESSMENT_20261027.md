# Assessment of the radial Darboux deformation

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Investigation05 chat0006, **Review radial collision progress**. Same-assistant internal assessment; no separate reviewer or specialist review.

**Finding.** [Note17][note] provides a concrete family of different forced radial equations retaining exactly H and all positive-frequency multiplicities. This answers the construction part of the proposed deformation direction. It supplies no improved estimate preventing simultaneous cancellation. The standard complete energy identity is transported with the exact boundary terms in equation (11).

The calculation was checked analytically in two forms where available:

- The Riccati identity w'+w^2=kappa^2 factors the original and transformed differential operators. Applying their intertwining identity to the forced equation retains h=(partial_x-w)g.
- The readout U(0)=Y'(0) follows from w(0)=0; lambda differentiation commutes with the transformation. For a>0, H_a=-a V(0)/16, so all multiplicities transfer without a double-event assumption.
- The inverse Y=[g-(partial_x+w)U]/(lambda+kappa^2) is nonsingular for the declared range lambda>0, kappa>=0. The family at kappa=0 starts from the differentiated free realization, not an identity map on Y.
- The integral kernel satisfies p'+wp=cos(sqrt(lambda)x), p(0)=0 and p'(0)=1. Integration by parts proves exact integral preservation with no unknown physical residual in its definition.
- The radial conjugation contributes the required 1/4. The additional potential is 2kappa^2 sech^2(kappa log r)/r^2. The transformed forcing and its changed parity are displayed, so the original positive Poisson source is not silently being replaced by an identical one.
- Newman differentiation contributes x g/2 in addition to x^2 h/4. The physical observation retains its heat equation; the auxiliary deformation is not radial diffusion.
- Direct integration of the two quadratic terms agrees with the complete transformed Wronskian: I_kappa=(lambda+kappa^2)I-Y(0)B-g(0)B_lambda. Only at an event do both additional terms vanish. No source or boundary term was omitted to infer positivity.
- The explicit Gaussian-polynomial control still has U(0)=V(0)=0. Its transformed forcing and response have fixed signs, yet the norm and forcing integrals cancel. The other smooth control families are retained at their actual differentiability and convergence scopes; atomic cases need a different formulation.

The complete theta tails justify every operation uniformly on compact t, positive-lambda and kappa sets. No numerical calculation or interval certificate was needed. The external Darboux factorization was inspected in a primary source; the physical normalization, forced extension, invariant integral and control formulas were derived here. No novelty claim is made for the classical transformation.

**Decision.** Retain this as an exploratory RLC-04 construction. The same energy identity, including its deformation derivatives, supplies no further event condition. This does not decide whether another estimate in the transformed system could be stronger. A subsequent task should select one complete source-dependent estimate and compare it with its original-system pullback. No new collision range, global transfer, or homogeneous characteristic realization is recorded.

The [result index][results], [avoid index][avoid], [collision controls][controls] and [scoped-conclusion guidance][scope] determine that status. No DRAFT_HISTORY milestone is created.

[note]: ../notes/17_RADIAL_DARBOUX_SYSTEMS_PRESERVING_PHYSICAL_OBSERVATION_20261027.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
