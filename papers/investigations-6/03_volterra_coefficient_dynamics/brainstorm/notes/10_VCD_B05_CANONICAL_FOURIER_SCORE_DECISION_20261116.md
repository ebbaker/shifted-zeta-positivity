# B05 pass 1 — the complete canonical score on the Fourier scale

16 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Lead actual model/effort unavailable in accessible archive configurations; fixed helper dispatches gpt-6.1-sol/ultra, distinct from separate backend attestation. Continuation of research chat0003.

**Decision and proposed estimates, not an established zero theorem.** Read the [result index](../../../../../result-summaries/README.md), [cluster18](../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md), [control catalog12](../../../../../result-summaries/12_collision_controls_and_screening.md), [avoid index](../../../../../avoid/README.md), particularly [classification01](../../../../../avoid/01_restating_the_target.md), [controls02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [scope07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [separate bounds12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md). E15's one-kernel comparison and E12/E16's finite-data scopes remain in force.

## Two formulations of one complete-source test

Fix lambda=0 and retain the complete canonical Phi, Z=integral Phi, mu=Phi/Z, F=integral exp(izu)dmu=xi((1-iz)/2)/(4Z). Write V'=8πsinh(4u)+b(u) with the exact canonical b from E06. Define B(z)=integral b(u)exp(izu)dmu; this is the literal orbit matrix element <e0,b(J)exp(izJ)e0>, on its fixed-vector domain.

1. **Complete-source contour bound for B.** Instead of the height-independent ||b|| bound, use g=b Phi=-Phi'-8πsinh(4u)Phi. The product g, rather than the meromorphic quotient b, is analytic on |Im u|<π/8 and retains the complete arithmetic sum. Shift the Fourier contour by v sign(x). Preserve the exact cancellation of the cubic first-mode term before taking absolute values. Freeze E17 to derive an explicit complete-source majorant and its optimal asymptotic order within this stated termwise-absolute contour class.

2. **A phase-sensitive score equation with two exterior anchors.** Integration by parts should give 4π[F(z-4i)-F(z+4i)]+B(z)=izF(z). At z=x+iy with fixed 0<y<1, both shifted xi values can be estimated using functional equation and Euler product in Re s>2. The candidate reverse-triangle consumer |B|<4π(|F(z+4i)|-|F(z-4i)|) would exclude F(z)=0 when the difference is positive. Freeze E18 to compare this actual signed equation, anchor sizes and E17's paid allowance; also express the normalized B exactly in terms of the complete arithmetic ratio zeta(s)/zeta(s+2). This is a specific sufficient dominance estimate, not an assumption that the desired zero theorem holds, and no equivalence to RH is asserted for it.

These are not new approximants or a source/readout change. The two formulations test whether complete-source score information yields a usable Fourier-scale budget. The zero consumer is explicit. No degree update or terminal condition is supplied by them; failure of the consumer ends this particular route to an induction, not the chain program.

## Proposed quantitative E17 target

For real u>=0 put r_m=πm² exp(4u). Expanding g after its first-mode cancellation gives the positive termwise majorant
\[
 A_Y(\delta)=\frac2Z\int_0^\infty e^{(1+Y)u}\sum_{m\ge1}
 \{8(1-m^{-2})r_m^3+(30-12m^{-2})r_m^2+15r_m
       +8\pi e^{-4u}r_m^2+12\pi e^{-4u}r_m\}e^{-\delta r_m}\,du,
\]
for 0<=Y<1 and 0<delta<=1. The proposed bound is |B(x+iy)|<=exp(-v|x|) A_Y(cos(4v)), |y|<=Y, 0<=v<π/8. The predicted asymptotic is A_Y(delta)~15/[Z(1-Y)] delta^(-7/2). The m>=2 cubic terms create this leading order; no nonzero mode has been discarded. Its optimized allowance should be asymptotic to 15/[Z(1-Y)] (e|x|/14)^(7/2) exp(-π|x|/8). This is a proposed theorem for E17 to prove or correct. Its lower asymptotic is for the displayed majorant, not for |B| or the unsplit contour integral.

## E18 target and evidence test

For s=(1-iz)/2 and fixed 0<y<1, the larger exterior anchor has magnitude comparable to exp(-πx/8)x^((11+y)/4), and the smaller/larger ratio should be O(x^(-y/2)). Thus if E17's order is confirmed, its best displayed allowance loses the factor x^((3-y)/4). E18 must check signs, constants, normalization and primary gamma/Euler inputs; no numerical scan will decide this analytical comparison.

The exact normalized remainder should be
\[
 \frac{B(z)}{4\pi F(z+4i)}=1-\frac{F(z-4i)}{F(z+4i)}
 -\frac{(2s-1)(s-1)}{2(s+2)(s+1)}\frac{\zeta(s)}{\zeta(s+2)}.
\]
It preserves the signed arithmetic instead of replacing it with the contour allowance. For Re s>1 the ratio has the positive Dirichlet coefficients product_{p|n}(1-p^{-2}); their absolute sum diverges for Re s<=1. Verify the exact scope before interpreting this as a boundary of an estimating class. This formula alone is not progress toward a sign; its purpose is to identify the precise arithmetic information lost by the proposed bound. A subsequent pass may test the proposed consumer itself on the actual canonical source, rather than respond only by improving an inadequate majorant.

## Control premises and retained scope

This exact theta score and xi/ordinary-zeta normalization fail for the distinct E07/E10/E12 sources; finite score matches do not supply equality of the orbit B. The E07 nonreal-zero conclusion remains in its finite square-change class, while smooth E10/E12 zero locations are open. Euler translates change the canonical summand formula and xi multiplier. Weighted-square/finite-prime controls lose full canonical reflection; reflected super-Gaussian and smooth/primitive sources lack the canonical arithmetic source, with their individual confinement scopes unchanged. Atoms/compact triangular sources fail positive full-line density; varying-observation controls fail the literal Fourier readout; the actual-profile relaxation supplies no corresponding full source/readout; RH-conditional endpoint controls fail ordinary Dirichlet arithmetic. These are premise comparisons from catalog12, not claims that an untested derived inequality rejects every control.

A successful upper bound is an intermediate number/rate. A failed termwise contour estimate or a failed absolute reverse triangle has only that estimating-class scope. Do not promote either to impossibility of correlated canonical estimates, and do not manufacture a new RH-equivalent criterion supported by checks.
