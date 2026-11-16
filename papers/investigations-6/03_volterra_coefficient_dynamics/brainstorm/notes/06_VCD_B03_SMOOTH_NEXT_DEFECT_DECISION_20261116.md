# VCD-B03 second pass — test whether smoothness repairs the next-step gap

16 November 2026, America/New_York. Prepared for Edward Baker with OpenAI Codex assistance. Lead backend/effort unavailable; requested Astra/ultra. Helpers explicitly Sol6.1/ultra.

**Fixed next decision after E07 and E08's boundary calculation.** The [result](../../../../../result-summaries/README.md) and [avoid](../../../../../avoid/README.md) indexes apply, particularly [control cluster12](../../../../../result-summaries/12_collision_controls_and_screening.md), [avoid02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md) and [scoped exclusions07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

E07 controls lose smoothness at a high odd endpoint, so they cannot by themselves settle a candidate that retains global smoothness. E08's exact commutator calculation finds a sharper algebraic limitation: the next adjacent score defect cancels out of the finite boundary commutator. It is not an uncontrolled whole column in that equation. This corrects the provisional description in decision05.

Freeze E10 to decide whether smoothness and unchanged source tails force that missing next adjacent defect to vanish. Use positive even compactly supported multiplier perturbations of theta, chosen to preserve all moments through 2N and canonical adjacent equations below N while changing equation N. Linear independence follows from the exponential growth of V_theta' against polynomials. This is a test of an exact forward-step implication; it makes no Fourier-zero claim for the smooth controls and does not preserve the complete arithmetic square expansion.

If successful, finite commutation plus lower canonical defects and smooth theta tails cannot close the new equation. Full exact source information or a genuinely additional quantitative law remains necessary for this tested induction route. This does not exclude every source-sensitive tail induction. The source-identification theorem of E08 remains useful for distinguishing all exact constraints from finite consistency.
