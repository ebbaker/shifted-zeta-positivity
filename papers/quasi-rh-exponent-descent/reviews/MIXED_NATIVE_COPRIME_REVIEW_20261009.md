# Review of the native coprime inverse and response-tail test

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Reviewer: GPT-6 (Codex). Reasoning effort: inherited configuration, not
exposed; the exact serving variant is not inferred. Same-model internal
review, not independent specialist validation or formal verification.

Reviewed staged mixed note 17. Re-read complete printed pages 56–59 of
the primary September 30 PDF in memory; SHA-256 again matches
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
The deep reciprocal-growth proof is an imported input, not independently
verified here. No source PDF or long extraction is saved.

**Assessment:** the native coprime Euler resummation, double Mellin identity,
literal contour exponent, rational target displacement, and fixed-buffer
response-tail correction are correct. They diagnose the limit of the
existing absolute-contour method; they do not prove a selected moment
or a lower bound. Three small presentation clarifications are recommended.

## Algebra and analytic domain

For each good prime, squarefreeness and coprimality allow exactly the
absent, left-only and right-only states. The local factor is
\(1-x-y\). Dividing by the two reciprocal-L local factors
\((1-x)(1-y)\) gives exactly
\(1-xy/[(1-x)(1-y)]\). Thus the claimed correction has the proper sign
and excludes the common-prime state. A physical zero makes both x and y
zero and retains the factor one.

The stated domain \(\Re s,\Re t\ge\sigma_0>0\),
\(\Re(s+t)\ge1+\delta\) gives uniformly nonzero local denominators and
an absolutely summable correction. Uniform boundedness and holomorphy of
the product follow. Finite correction zeros are allowed. It supplies
meromorphic continuation of the complete expression via the reciprocal
L-functions, not a bound through their poles or a lower bound for C.
The double Mellin normalization is \(D^{s+t}\); the later physical
normalization is \(D^{-1}\). The conjugated profile transform is correctly
\(\overline{\widehat A_0(\bar t)}\).

**Orientation clarification:** at fixed ray factor \(\nu\), replacing
\(\chi^+\) by \(\chi^-\) is not necessarily conjugation of the entire
\(\psi=\nu\chi^+\). The Euler identity holds independently in both
orientations. Whole-character conjugation also conjugates \(\nu\).
The source's \(X_u\) is closed under this joint operation, as verified
on page 56. Replace “by conjugation” with that precise statement.

## The truncated double contours

Source 8.1 gives reciprocal control for every presentation in \(X_u\)
at \(\Re s\ge a+6e\) and \(|\Im s|\le(3i+2)T_1\). Source 8.2 places
pure twists of height at most \((3i+1)T_1\) in the L-argument, with one
cumulative allowance \(T_1/2\) for added frequencies in that argument.
The conjugate presentation satisfies the same conditions. The two central
variables can be truncated within their assigned argument budgets;
the uniformly bounded collision factor creates no new height allowance.

An iterated finite rectangular shift controls central pieces and horizontal
joins inside those same rectangles. Separate vertical tails remain on
the absolute lines. The collision factor is uniformly bounded on all
these combinations of real parts, so it does not obstruct the source's
tail mechanism.

**Untwisted-transform clarification:** explicitly write, when appropriate,
\(A_0(y)=W(y)y^{i\omega}\) and change variables so the transforms in
the tail estimates are those of W and its conjugate. Then the two
L-arguments carry the opposite pure shifts, and each uses its own
cumulative source allocation. Applying late-order tail differentiation
directly to the twisted A0 would create a height factor whose order
grows with the external tail order, contrary to the source quantifier
order. The source permits the external tail order after the positive
\(\tau\) in \(T_1=Z^\tau\), without changing the already fixed internal
height order. Note 17's contour statement is valid with this explicit
implementation.

Both central real parts equal \(a+6e\), so the normalized scale power is
\(2a+12e-1=d+12e\), exactly as stated. A fixed preliminary e therefore
gives \(\rho=12e\); \(\rho\le10^{-5}\) requires
\(e\le1/1200000\), in addition to the source's e0 and height conditions.

**Deleted-g clarification:** if extending the direct Euler formula to
\((ab,g)=1\), define \(C_{u,g}\) by omitting correction factors at
\(p\mid g\). The expression is
\[
 \frac{C_{u,g}(s,t)}{L_u(s)L_u^{\rm conj}(t)}
 \prod_{p\mid g}[(1-x_p)(1-y_p)]^{-1}.
\]
The two separate deletion products have the source's arbitrary small
power bound, and \(C_{u,g}\) remains uniformly bounded. This avoids
implicitly dividing by a possibly zero correction factor. The original
q-smooth deletion proof in note 14 also avoids that issue.

## Target displacement and weighted tail

An absolute central bound at the mixed target requires total real part
at most \(2a-\chi/r\). The symmetric displacement below a is
\(\chi/(2r)=1/(1080r)\). For \(7/10\le r<73/100\), its exact range is
\(5/3942<\chi/(2r)\le1/756\); the strict lower endpoint and inclusive
upper endpoint are correct. The required real parts remain in the
collision correction's analytic domain but lie below the source inverse
contours. A matching presentation can have its witnessed zero in
\([a,a+e)\), so the stronger reciprocal shift has no source justification.
The note correctly does not assume correction zeros cancel that pole.

The response-tail implication is also correct. The complement threshold
\(U^{dr-2\chi}\) leaves twice the requested low-response saving, while
the high-response contribution uses the actual pointwise inverse envelope.
At fixed buffer \(\rho\), that contribution needs weighted mass saving
\(\chi+\rho r\), with any additional allocation margin retained. The
low-response spare does not pay the fixed buffer in the high-response term.
The layer-integration identity is exact for the finite selected family.

Neither the g=1 diagnostic nor the sufficient tail mass closes the other
low-gcd sectors or establishes the missing selected dependence. The note's
stated limitations and next-input audit are appropriate.

## Follow-up: native nonvanishing and resolved clarifications

The current staged note 17 incorporates all three presentation
clarifications above: whole-character conjugation, untwisted tail
transforms with cumulative argument heights, and direct deleted-g
correction products. No outstanding correction remains from this review.

Its added native nonvanishing conclusion is correct. The underlying
field is Q(sqrt(-3)), and the original good set excludes the primes above
6. Hence every remaining prime ideal has norm at least 7. For both real
parts >1/2, |x_p|+|y_p|<2/sqrt(7)<1, so neither 1-x_p-y_p nor either
denominator can vanish. Locally uniform absolute convergence of the
correction product makes C holomorphic and nowhere zero. On real parts
at least 1/2+delta0, the summable estimates for C_p-1, together with the
uniformly nonzero finitely many initial factors, give upper and positive
lower bounds independent of row and imaginary parts.

Therefore C itself cannot cancel a reciprocal-L pole in that native
bidomain. Profile zeros or signed residue averages are separate possible
mechanisms and remain unproved. Finite correction zeros are still
permitted in the broader domain of positive individual real parts with
sum >1; that earlier caveat must not be transferred to the narrower
native domain.
