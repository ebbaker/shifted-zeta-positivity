# Multiplicative dilation and nonlocal arithmetic review

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from current-turn metadata. Internal independent LLM derivation checks and a separate-process replay are not external refereeing or formal proof verification.

The user clarified that the continuation should pursue arithmetic. No compact-surface note, winding pilot, manuscript revision, or broad numerical search was undertaken in this continuation. The preexisting topology notes retain their historical scope.

## Mathematical outcome

The [multiplicative-dilation note](../notes/03_theta_bundles_and_connections/11_MULTIPLICATIVE_DILATION_AND_COMPLETE_HEAT_PACKETS_20261015.md) derives

\[
 D_d\phi_n=\phi_{dn},\qquad D_d f(u)=d^{-1/2}f(u+\tfrac12\log d),
\]

and applies classical divisor inversion to the complete theta source. Finite prime excision has a positive source remainder starting at the smallest omitted prime. An explicit heat-weighted moment bound controls every fixed endpoint derivative, uniformly in real frequency, and permits the required mixed error after multiplication by the complete starting observation.

The identity has an arithmetic discriminator: weighted square coefficients contribute the exact defect `a_(pn)-a_n`. All prime identities and `a_1=1` force unit coefficients, while a finite prime family leaves freedom. This makes the proposed input stronger than generic source positivity, but it is another exact description of the theta coefficients, not a proof of a physical sign.

The main analytic limitation is proved directly. Under the half-line heat transform, each dilation produces a complete transform at a complex shifted frequency **minus** a lower-interval integral, with its full exponential prefactor. At fixed `t>0`, either separated Möbius series fails the term test. The paired series converges absolutely by Gaussian square-mode decay. Passing to the full source line does not remove the obstruction: the translated mass grows under the positive heat weight, and the inverted first mode no longer has a full-line heat transform. Finite prime sieves also lose even reflection; their far-left sign is the parity of the number of primes.

These are exact formulation and convergence results. Neither the tiny error in the sifted first-mode approximation nor the positive source remainder determines the sign of the main stationary cross observation.

## Independent review of sensitive steps

A separate collaborator checked the full staged dilation note and confirmed the source scaling powers, the least-unsieved-integer argument for arbitrary finite prime sets, the tail estimate, the complex-frequency sign, the Laplace denominator `2ta-iz`, the Dirichlet exponent `s=1/2+iz/2`, the negative-tail factor `Q^(-5)`, and the factor two in the whole-line formula.

The same review checked that the general source lower edge is

\[
 [b_cw(0)+\psi_c(0)w'(0)]/8,
\]

with the **plus** sign on the derivative term. The cutoff-aware scalar lower coefficient is `(1_(j=0)b_c-A/2)/8`. The reviewed version explicitly specifies polynomial-growth masks, `C^2` weights, convergent integrals and a vanishing upper bracket. The additive shift operator used in the boundary composition law is defined separately from the integer-index notation.

The [nonlocal-multiplier note](../notes/03_theta_bundles_and_connections/12_NONLOCAL_ARITHMETIC_MULTIPLIERS_AND_BOUNDARY_OBSTRUCTIONS_20261015.md) records three further audited calculations:

- The massive half-line Green kernel yields a convergent infinite-range recurrence current and error `kappa M(g)|W|`. Its lower trace tends to the original unresolved residual. Positivity of its kernel does not sign the input residual.
- Euler summation produces an exact Bernoulli multiplier whose absolute source majorant is nonintegrable. Subtracting a null multiplier repairs convergence and gives the exact floor-counting representation. Coarse positive envelopes of that representation admit the weighted-square collision controls.
- Poisson duality is valid at a finite source cutoff. Every nontrivial ordinary dual endpoint mode lacks a full positive-time source integral; an exponentially increasing dual range carries the collective theta cancellation. The complete finite-cutoff error is retained.

The rejection statements are limited to these specified uses. No blanket impossibility theorem for nonpolynomial amplitudes, bilocal identities, or other arithmetic estimates is asserted. In particular, the residual equation `w''=w` characterizes only the canonical source reduction used here, not every possible source primitive.

## Finite checks and limits

The [standalone checker](../numerics/check_arithmetic_dilation.py) passes **47 exact assertions** using only the Python standard library. Its [receipt](../numerics/ARITHMETIC_DILATION_CHECKS_20261015.json) includes finite divisor masks, prime-sieve masks, smooth/free factorization, formal transform prefactors, lower-strip substitution, cutoff-aware source edges, complete-first-factor identities, and rational coarse remainder constants. The elementary bounds `3<pi<4` are declared analytic inputs; a positive finite exponential sum verifies the auxiliary lower bound for `e`.

A separate collaborator replayed the checker in a fresh process. The [manifest](../numerics/ARITHMETIC_CONTINUATION_CHECKS_20261015.json) records the receipt comparison, reviewer scope, file identities, manuscript/PDF preservation and link checks. Creation timestamps are provenance, not mathematical output. Enumerated finite divisor cases do not establish universal Möbius inversion, and rational coefficient checks do not prove the analytic interchange or divergence statements. Those arguments are in the notes. No theta quadrature, signed-domain extension, or massive-resolvent numerical certificate is claimed.

## Assessment and next decision

The bounded experiment requested in coordination 11 is complete: there are explicit arithmetic identities, all lower traces and upper remainders, and a reasoned rejection of the proposed separated or positive-envelope estimates. The useful result is a sharper specification of the cancellation a successful estimate must preserve.

The remaining target is still

\[
 W B_\partial\le C W^2+\epsilon|W|
\]

on prescribed positive cones through every candidate stationary event. The errors must tend to zero locally uniformly in the ordering allowed by strategy 07. The new identities do not provide that main inequality, and no computational benefit over ordinary cutoff has been demonstrated. Before numerical optimization, a further proposal must state a signed estimate for the complete coupled dilation terms or the exact lattice discrepancy and identify the premise that excludes the collision controls. The [handoff](../notes/00_research_coordination/12_ARITHMETIC_DILATION_AND_NONLOCAL_CONTINUATION_20261015.md) records this decision.
