# Self-review: canonical tail law and coupled analytic enclosure

21 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **max**.
This is the authoring assistant's assessment, not independent specialist
review. No numerical experiment was used.

Reviewed [Note 04](../notes/04_CANONICAL_TAIL_LAPLACE_CONSTRAINT_AND_COUPLED_ENCLOSURE_20261021.md)
against Notes 01–03, the existing positive-carrier and modular-cancellation
theorems, the earlier positive-tail cone, and the finite-prime control
theorem. The status is **proved in-note**, with the limitations below.

## Algebra and complete analytic payments

The ratio identity retains both source monomials. Dividing
(2 lambda_n q-3) by (2 a q-3) leaves the positive remainder
3(lambda_n-a)/(a(2 a q-3)). At q=1+h this is the exponential-law
factor gamma/(gamma+h), with gamma=(2a-3)/(2a)>1/2.
The weights A_n and B_n in the note therefore give the exact ratio,
not a bound obtained by dropping the negative source monomial.

The spectral gap Delta=lambda_(m+1)-lambda_m is removed before defining
the probability measure. Its remaining rates delta_n=lambda_n-lambda_(m+1)
are nonnegative. Only A_(m+1) is a zero atom; B_(m+1) is a translated
exponential density, with no zero atom. This verifies both the source
floor and the total mass E_m.

The half-plane bound pays the full lattice sum. With r=gamma/2,
the geometric ratio is below 81/1024 and the monomial factor below 3,
giving a bound below 3072/943<4. The right source strip follows from
Re(exp(4v)-1)>=sqrt(3)/2-1>-1/4>-gamma/2. The right-half-strip
qualification is essential: no false full reflection of a finite tail
is asserted.

The real derivative calculation removes the zero atom before using
q*s*exp(-s(q-1))<=max(1,s). Its constant uses E_m-A_(m+1)+Q_m,
not E_m+Q_m. All first-moment sums are paid through exact geometric
moments of j and j^2. The explicit L_m is an upper bound with
asymptotic 24/(pi*m^3); that is not claimed to be the exact maximum
derivative or its sharp asymptotic.

## Physical observation and strict comparison

The residual is H-H_(<=m), the unshifted finite-prefix remainder.
No contour is changed. The decreasing multiplier after removing its
limiting floor defines one probability measure, independent of t,x.
Fubini is justified by a double-exponential majorant for the complete
physical value and derivative. Every source ray and lattice index is
included. There is no hidden finite quadrature cutoff.

The closed convex hull of the incomplete-integral curve is sharp for
the declared monotone relaxation. Endpoint atoms at zero and infinity
are included explicitly, or obtained as limits if fixed endpoint values
are imposed. It is not claimed sharp for the actual Laplace measure,
for fixed source moments, or for the canonical coefficients.

The comparator uses the same positive lower and upper envelopes and
the same first gap. It already retains the common pointwise multiplier
for value and derivative. For a negative lobe followed by a positive
lobe, every initial-interval cutoff must either include the former or
omit the latter. This proves the explicit support loss, including its
sign. Taking the opposite covector also improves the lower bound.

Uniformity on compact real parameter sets with x bounded away from
zero follows from continuity and a common integrable majorant, not
sampling. The explicit cosine example has interval length pi/(3x)
and signed cosine at least sqrt(3)/2, giving the factor sqrt(3)*pi/(6x1).
Its source minimum includes the full heat and double-exponential
payments. No positive gap at x=0, across unbounded heights, or for
complex spectral covectors is inferred from this argument.

## Controls, comparison scope and disposition

For bounded positive square weights, the same measure construction
survives. A canonical prefix through m+1 fixes the zero atom. Source
value and first derivative at zero fix E_m and Q_m because
Q_m=-F'(0)-Delta*F(0), with the derivative in h and du/dh=1/4 at zero.
These are permitted finite linear measurements in the cited finite-prime
theorem. Its coefficients can be within 1/5 of canonical, preserving
the bound (6/5)*(3072/943)<4. The displayed regularity constants and
monotone enclosure therefore coexist with its escaping double events.
Full normalized reflection is still absent from those controls.

The note records a useful actual-source restriction and a strict
physical allowance comparison. It does not outperform the established
positive-carrier theorem, the earlier discrete mode cone, or the S01
shifted-tail estimate by assertion. Those methods retain different
information or approximate a different object. No new physical
separator, nonvanishing margin, or theta multiplicity conclusion is
proved. The retained head and tail still cancel every algebraic endpoint
coefficient in the complete reflected field.

**Disposition:** retain the quantitative actual-tail theorem and joint
enclosure. The next sign argument must retain the common tail law in
its relation to the retained head, rather than only adding finitely
many scalar measurements. The program's arithmetic discriminator and
physical exclusion remain open.
