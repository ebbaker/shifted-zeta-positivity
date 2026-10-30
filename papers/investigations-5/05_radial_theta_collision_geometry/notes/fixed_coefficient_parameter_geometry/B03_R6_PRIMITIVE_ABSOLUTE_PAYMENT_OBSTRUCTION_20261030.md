# B03 R6: testing absolute payment after the complete primitive transfer

30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Parent **gpt-6-astra / ultra**, actual session metadata, Investigation05 **chat0049**, thread `01a18dc4-d540-7f43-8874-81dafca23151`. Independent Sol work was explicitly authorized by the author. This is a B design and proof, with the finite comparison initially unmeasured; E01 R3 owns acquisition and E02 R6 owns assessment. [Progress06](../../research-progress/06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_PROGRESS_20261030.md) is the sole live register.

**Question and class.** Can the complete primitive formula help when its signed integrand is combined exactly but then paid by its absolute value before source integration? We choose the **outer-bidisk bound on G** as consumer. The theorem below gives a necessary cost for this class, even when the supremum over parameters is taken *after* integrating the absolute value. A fixed scalar lower-bound computation will compare that necessary cost with the accepted IBP bound. This is a sufficient-bound cost comparison, not an RH criterion, a theta nonvanishing theorem, or a universal rejection of the primitive representation.

## 1. Fixed inputs and exact identity

Retain [Note26](26_ADAPTIVE_RADIUS_AND_PHASE_ALIGNED_IBP_B03_R5_20261030.md), [Note28](28_SHARP_QUADRATIC_RADIUS_PAYMENT_B03_R5_20261030.md), and the [accepted R5 assessment](../../reviews/fixed_coefficient_parameter_geometry/E02_R5_ADAPTIVE_RADIUS_IBP_ASSESSMENT_20261030.md). In particular
\[
 (\tau,a,R)=(1/4,64,1/32),\quad h_j=\partial_A^jH(\tau,a),\quad b=h_2,
\]
\[
 H(T,A)=\int_0^\infty e^{Tu^2}\Phi(u)\cos(Au)du,\qquad
 \psi(u)=e^u\sum_{n\ge1}e^{-\pi n^2e^{4u}},\quad 8\Phi=\psi''-\psi.
\]
The literal observation, full unit-coefficient source, quadratic heat polynomial, drift, unit preparation and spatial R³ are unchanged. Write
\[
 \mathscr R=e^{\tau u^2}\{e^{tu^2}\cos((a+x)u)-\cos(au)+xu\sin(au)
                       +(x^2/2-t)u^2\cos(au)\},
\]
\[
 K=-2b\mathscr R+(h_1+bx)\partial_x\mathscr R,\quad F=K_{uu}-K,
 \qquad G=\int_0^\infty\Phi K\,du.
\]
Both lower endpoint terms vanish because K=O(u⁴). For every fixed U>0,
\[
 G=\frac{\psi'(U)K(U)-\psi(U)K_u(U)}8
       +\frac18\int_0^U\psi F\,du+\int_U^\infty\Phi K\,du. \tag{1}
\]
All three pieces are exact; U is independent of (t,x). There is no phase-based deletion of the boundary or exterior. At infinity the differentiated theta decay dominates the parameter-uniform polynomial/exponential factors. Consequently all formulas and circle integrations below are absolutely dominated on the closed bidisk.

## 2. Precisely delimited absolute-payment class

For finite U≥1 define the smallest payment of the following particular form:
\[
 A_U=\sup_{|t|,|x|\le R}\left\{
 \frac{|\psi'(U)K(U)-\psi(U)K_u(U)|}{8}
 +\frac18\int_0^U\psi(u)|F(t,x,u)|du
 +\int_U^\infty\Phi(u)|K(t,x,u)|du\right\}. \tag{2}
\]
It is a finite upper bound on sup|G|. It retains both terms of the boundary *inside the same absolute value* and the full joint kernel F. The analogous whole-line payment is
\[
 A_\infty=\sup_{|t|,|x|\le R}\frac18\int_0^\infty\psi|F|du. \tag{3}
\]
Any computable upper majorant of (2)/(3), including the usual integral of pointwise parameter suprema, belongs to the tested class. We do **not** test a method that integrates F with its sign over a nontrivial source panel before taking modulus, preserves cancellation between the three pieces of (1), subtracts known Taylor coefficients before estimating the remaining function, changes the reference, or chooses U<1. Those change the premise of this comparison.

## 3. An unavoidable first-parameter-coefficient cost

**Proposition (proved in-note).** Let I⊂[0,1] be measurable and
\[
 v(u)=u^3e^{\tau u^2}\sin(au).
\]
For every U≥1, and also U=∞,
\[
 A_U\ \ge\ \frac{R|h_1|}{8}\int_I\psi(u)|v''(u)-v(u)|du. \tag{4}
\]

**Proof.** Direct differentiation at (t,x)=(0,0) gives
\(\partial_t\mathscr R=0\),
\(\partial_t\partial_x\mathscr R=-u^3e^{\tau u^2}\sin(au)\), and hence
\[
 \partial_t K(0,0,u)=-h_1v(u),\qquad
 \partial_t F(0,0,u)=-h_1(v''-v).
\]
For each fixed real u, Cauchy's coefficient formula on the circle t=Re^{iθ}, x=0 implies
\[
 R|h_1|\,|v''-v|\le\frac1{2\pi}\int_0^{2\pi}|F(Re^{i\theta},0,u)|d\theta.
\]
Multiply by ψ/8, integrate on I and apply Tonelli. For each θ the integral on I is bounded by the nonnegative full payment inside (2), hence by A_U. The boundary and exterior are kept in that payment; their nonnegativity allows them to be dropped only in this **lower** estimate of the cost. The same proof works for (3). This proves (4), without interchanging a supremum and signed integration. □

This argument is more restrictive than bounding the actual first coefficient |h1 h3| of G: (4) measures the cancellation lost by the tested payment. It is not a lower bound for |G| or evidence that any physical collision exists.

## 4. A fixed positive witness requiring no omitted-tail upper bound

Select, before acquisition,
\[
 I=[1/32,1/4],\qquad \psi_1(u)=e^{u-\pi e^{4u}}\le\psi(u).
\]
The exact derivative is
\[
 v''-v=e^{u^2/4}Q(u),
\]
\[
 Q(u)=\left(6u-\frac{8187}{2}u^3+\frac{u^5}{4}\right)\sin(64u)
              +(384u^2+64u^4)\cos(64u). \tag{5}
\]
Define the explicit finite positive integral
\[
 J_I=\int_{1/32}^{1/4}e^{u+u^2/4-\pi e^{4u}}|Q(u)|du,
 \qquad L_I=\frac{R|h_1|}{8}J_I. \tag{6}
\]
Then A_U≥L_I. The omitted primitive modes and source complement are nonnegative in (4), so ignoring them is valid for this lower estimate. This does not replace the full physical source or assert an upper enclosure for a complete-source integral. h1 remains the accepted **complete signed jet**. No primitive quadrature is passed to a holomorphic integrator through an absolute value; real interval panels will enclose (6).

The exponent, interval, center, outer radius, comparison and finite work limit are now fixed. No positive comparison has been presumed. The [E01 R3 packet](../../research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E01_R3_PRIMITIVE_ABSOLUTE_PAYMENT_20261030.md) asks whether a certified lower endpoint for L_I exceeds the accepted upper endpoint for M_G^IBP, using the saved R2 source data. A failure of this inexpensive witness to decide the comparison is an unresolved return, not evidence that A_U is small.

## 5. Matched consumer and exact implication of a successful witness

Use exactly the existing signed finite coefficients and
\[
 F_N(r)=\sum_{1\le m+n\le N}|g_{mn}|r^{m+n},\qquad
 T_N(q)=\frac{q^{N+1}((N+2)-(N+1)q)}{(1-q)^2}.
\]
For any candidate bound M≥A_U, the tested consumer is
\[
 \Gamma_N^{\rm abs}=F_N(r)+M T_N(r/R),\quad
 d_N^{\rm abs}=|D_0|-2b^2r-\Gamma_N^{\rm abs}. \tag{7}
\]
If L_I>M_G^IBP is certified, then for every 0<r<R and every finite N≥1,
\[
 \Gamma_N^{\rm abs}-\Gamma_N^{\rm IBP}
 \ge(L_I-M_G^{\rm IBP})T_N(r/R)>0,\qquad
 d_N^{\rm abs}<d_N^{\rm IBP}. \tag{8}
\]
Thus this class cannot improve any same-radius same-degree margin or minimum passing degree. Where the quadratic rule of Note28 is used with M in place of M_G, its licensed radius is no larger; equal caps can prevent a strict radius comparison. Taking min(M,M_G^IBP) then simply retains the accepted IBP rule. These statements concern the specified allowance, not the optimal true radius.

The separate time penalty 2b²r remains. D0=0 is untouched. Both methods feed the same direct strip, so no spatial-flow/coordinate gain occurs. The accepted scalar comparisons and C01 eventual-convergence dependency remain unchanged; there is no new spatial floor to compute for a dominated allowance. Under Φ→λΦ with λ>0, ψ,h1,b scale by λ, and A_U,L_I,M_G scale by λ². The comparison and the sharp-radius rule are amplitude invariant.

## 6. Controls and scientific scope

This is a cost obstruction for the actual theta data at one specified center and outer radius, conditional at issue on the finite comparison. It does not exclude any source or event. The algebra of the lower endpoint and (4) is generic; positive primitive existence alone is not theta-specific. Distinction in (6) comes from the actual theta primitive summand and saved complete jet.

Apply the [control register](../../../../../result-summaries/12_collision_controls_and_screening.md) with its original scopes: Gaussian-polynomial, weighted-square, Euler-factor, reflected/shape/positive-primitive and finite-prime controls do not inherit the unit theta source or its numerical inputs; their actual event-containing balls reject a positive row margin. Weighted-square/finite-prime sources fail full reflection as recorded, while reflected and positive-primitive examples fail full square arithmetic. Finite-profile/atomic controls need not admit the smooth primitive integrations used here; their direct jet collision identities remain valid. Conditional endpoint controls retain their RH hypothesis and arithmetic failure. Variable-observation controls fail literal cosine/heat reconstruction. Relaxed profile measures are not physical collision events. No event is transferred to (1/4,64), and a negative Laguerre witness alone is not an event location.

## 7. Routing and provenance

B03 R6 supplies one scoped analytical test, not a new coefficient revision. E01 R3 is a fixed lower-cost certification; then E02 R6 assesses the proof and actual result. A certified failure of the absolute-payment class leaves signed source integration open. B04 coverage remains gated because neither this obstruction nor R5 supplies a uniform discriminant/radius estimate. No manuscript, draft-history, reference source, original acquisition or prior issued packet is changed.

The manuscript and book were read by a read-only Sol intake contribution; parent read the relevant analytical sections and R5 chain. A separate read-only Sol contribution checks (4)/(5) and the consumer implication. These are internal LLM checks sharing inherited premises, not specialist or formal independence. Actual acquisition/review provenance belongs in their returns.

Read the [result index](../../../../../result-summaries/README.md), especially [theta identities](../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), and [avoid index](../../../../../avoid/README.md), especially [target classification](../../../../../avoid/01_restating_the_target.md), [separate absolute bounds](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), [scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [noncircular inputs](../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md). This directly tests the lost-cancellation issue instead of treating the positive primitive as a lower margin.
