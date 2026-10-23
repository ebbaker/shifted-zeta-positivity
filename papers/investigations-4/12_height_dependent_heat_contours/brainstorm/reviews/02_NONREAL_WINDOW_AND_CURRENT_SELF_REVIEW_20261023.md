# Self-review of nonreal window transport and the current interface

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**, reasoning effort **xhigh**. This is the deriving assistant's own proof audit, **not an independent review**, formal verification, numerical certificate, or specialist review.

Reviewed source: [Note 07 — finite nonreal window transport and the missing small-value estimate][note]. The author requested the analytic opening deliverable in [Continuation 05][continuation]. The [result index][results], [control register][controls], and [avoid index][avoid], specifically [classification][a01], [scope][a07] and [coupled estimates][a12], set the status vocabulary.

**Disposition:** the finite theorems and explicit error inequalities are supported by the arguments below under their stated hypotheses. OBF-01 is complete at that finite level. OBF-02 has a selected representation and source-error theorem, while its useful aggregate estimate remains open. No negative-time theta inflow bound of useful size, enlarged width, or simplicity conclusion is established.

## Proof audit

1. **Population and endpoints.** The hard count includes every interior zero with multiplicity, and every crossing occurrence. Interior real heat births contribute 2 floor(m/2); an event at 0 is included and one at a is excluded. Spatial endpoint zeros are excluded. Off-real collisions preserve nonreal multiplicity. The real endpoint consumer does not need RH; interpreting it as a consumer for all canonical endpoint sites does.
2. **Local integrability.** In the parabolic leading polynomial the rescaled Hermite roots are simple. Perturbation gives one-sided square-root analytic root branches and speeds bounded by C/sqrt(|t-t_e|). This is integrable. The odd central branch is real at a real event. Finite local zero disks and a finite time cover justify summing the complete weighted populations. No fixed zero-free working wall is used by the smooth theorem.
3. **Wall multiple events.** The note does not assign them the transverse weight. Its optional extension assumes stabilized one-sided cluster counts, adds the actual jump Δ_e, and conservatively pays [Δ_e]_+≤m_e. The local disk/event block is additional data. There is no asserted universal half-event correction.
4. **Smooth event balance.** Differentiate ψ along each regular nonreal branch, integrate its finite variation, and add the real-event jumps. Off-real collisions and support crossings have no weighted jump. This proves Note 07 (5) with B_ψ in (a,0]. The inequality (6) discards only nonnegative terms. It is not inferred from the conserved total divisor.
5. **Signs and constants.** The quadratic pair enters the unit disk at -1/2 with radial speed -1. The cubic pair enters at -1/6 with speed -3; its endpoint multiplicity is three while its nonreal resource is two. The positive wall Jacobian has sign -n·v. These check the inward convention and the sharp 3/2.
6. **Smooth current.** For H=p+iq, H_z=A+iB, H_zz=C+iD, and H_zzz=E+iF, the current's components are k(CA+DB), k(DA-CB). Its divergence has derivative-of-k part (k_p C+k_q D)(A²+B²), plus 2k(AE+BF). The time derivative of k|H_z|² is the negative of this expression. Thus continuity holds even where H_z=0, without an H_z denominator. The same calculation for an arbitrary holomorphic time-dependent field uses -f_t instead of H_zz.
7. **Positive current limit.** At a regular simple zero, changing target variables w=H(z) cancels |H_z|² and the target kernel has mass one. Fatou in time gives only the inequality used in (11); no unproved uniform convergence through critical times is invoked. Inclusion of real motion is conservative and can be expensive. The note does not equate signed total variation with gross nonreal inflow.
8. **Near-real cutoff.** The allowed order is first ρ→0 at a fixed δ, then δ↓0. Alternatively the uncut full current includes the whole strip. A finite omitted strip pays (12), with local jet and clearance constants explicitly described as field-dependent. No uniform high-height estimate for those constants is asserted.
9. **Approximation error.** Positive part is 1-Lipschitz. The kernel maximum is 1/(πρ²), and the maximum radial derivative occurs at |w|=ρ/sqrt(5), giving 125/(54 sqrt(5) πρ³). The coupled product difference is subtracted before bounds. The reference need not solve heat when its spatial jets are used; its defect is additionally paid if its time current is used. A fixed field error cannot be sent through ρ=0.
10. **Actual negative-time budget.** For t≤0, the exponential Taylor remainder is bounded by (|t|u²)^(K+1)/(K+1)!. Inserting the complete positive theta source gives (18), including the first two spatial derivative errors. Direct differentiation of the truncated heat Taylor polynomial leaves exactly (-t)^K H_0^(2K+2)/K!, so the defect sign in (19) is positive. These absolute moment budgets have no useful high-height amplitude estimate built in.
11. **Carrier normalization.** H=Bf gives -f_t=f_zz+2(B_z/B)f_z+(B_t/B+B_zz/B)f. Its true current retains this entire operator. The corresponding product error is bounded by (19b). Omitting the drift or the finite-ρ zeroth-order term is unjustified. No positive-time reference error is continued to negative time merely because B or the reference formula is analytic.
12. **Conditional small-value theorem.** The weighted sublevel measure has no atom at zero. Integration by parts against its radial cumulative distribution, followed by the assumed W(r)≤π L_h r², gives exactly the finite-ρ bound (22); its tail tends to zero using the acquired upper mass (21). This proves the stated conditional conclusion. It does not prove the assumed small-value bound. The normalized variant has the same proof with the full carrier operator.

## Obstruction and control audit

The scale H→cH fixes its roots while its fixed-ρ current tends to zero. This refutes an amplitude-free uniform regulator-removal assertion on that upper-jet class, not a normalized theta estimate.

For the stronger finite-upper-jet obstruction, the bracket e^(k²t)cos(kz-π)-1 solves heat; the displayed exponential/drift transformation preserves it. Its negative-time roots are exactly (25). On -1/k²<t<-1/(2k²), the left wall is crossed by the n pairs with m=n,...,2n-1, and their imaginary parts are below arcosh(e)/k. Multiplying by c_n makes any fixed finite upper derivative budgets hold on a compact neighborhood without changing those entries. This proves unbounded gross nonreal entry for **unnormalized real-type heat fields with only such upper budgets**. It is not a positive-source, fixed-normalization, or theta counterexample. Equal right-wall exchanges also check that net count can vanish while gross entry grows.

The full registered Euler-factor, weighted-square, finite-prime, reflected, positive-primitive and close normalized endpoint controls are screened in the note's table. Generic identities exclude none. Their respective failure of the unchanged theta source, full reflection/arithmetic data, or ordinary Dirichlet series is named. No all-real heat interval is assigned to finite-square controls, and no control is claimed to fail a numerical theta-sized small-value bound that has not been acquired.

Replacing the weighted sublevel expression by an unweighted r² area estimate can quietly exclude an ordinary double: its r² log(1/r) local sublevel volume is compatible with finite weighted root variation. This is a reason to retain the complete product rather than separately replacing its factors by upper bounds.

## Research disposition

The following are **proved finite interfaces**, not theta arithmetic progress: the event balance, the smooth endpoint consumer, the full-field current inequality, the finite-regulator error theorem, and the carrier conversion. The direct theta Taylor remainder is an explicit negative-time approximation budget, with no claim that its absolute error is efficient at growing height. The upper-jet obstruction is a scoped information result.

The opening deliverable ends at a clear missing inequality: a useful, independently derived small-value bound for the unchanged theta field after a specified carrier normalization, or a sharper directional-current estimate with all source errors. This is where theta arithmetic must become load-bearing. The earlier nonreal population, useful width choice, and global coverage remain independent open work. No numerical campaign or new manuscript was needed.

[note]: ../notes/07_NONREAL_WINDOW_TRANSPORT_AND_REGULARIZED_CURRENT_20261023.md
[continuation]: ../notes/05_CONTINUATION_ANALYTIC_OPEN_BOUNDARY_FLUX_20261023.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
