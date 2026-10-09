# Review of the native annular diagonal benchmark

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Reviewer: GPT-6 (Codex). Reasoning effort: inherited configuration, not
exposed; the exact serving variant is not inferred. This is same-model
internal review, not independent specialist validation or formal verification.

Reviewed staged mixed note 18 against the phase-1 source audit of printed
pp. 159–178, particularly the second Gauss transform on p. 165. The
primary PDF SHA-256 is
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.

**Assessment:** the coefficient identity, native prime-product benchmark,
standard comparison rectangle, diagonal normalization, and exact rational
gap are correct with the qualifications already present in the note.
This diagnoses a failed separately positive coefficient majorant; it gives
no lower bound for the full Gauss norm or the selected mixed energy.

## Coefficients and native annuli

The complete identities mu*1=epsilon and mu*1*1=1 are correct on the
good-ideal monoid. Complete multiplicativity, including row zeros, gives
their twisted versions. Three separate physical profiles instead yield
three independent Mellin variables and the exact quotient
L(t)L(w)/L(s). No diagonal restriction of those variables is available.

For fixed nonzero profile windows and r>m, r<2m, a product pq1q2 has only
p in the inverse annulus. The q1q2 divisor lies above that annulus, while
each qi lies below it. Its remaining two plain allocations are the two
orders of q1,q2, with identical complex coefficient. Thus the value -2
in (7) is exact. The fixed-field prime ideal theorem counts distinct
products on the stated windows and gives coefficient mass
DN^2/(log U)^3. The weight phi(v)/Nv tends uniformly to one there.
The argument requires fixed positive window widths and uniform profile
lower bounds if the profiles vary.

At M=1, after the inverse divisor p is fixed, no divisor of q1q2 lies at
the comparison length U^(1/4): its exponents are 0,m,m,2m. The standard
equal-product centered coefficient has the same benchmark on this subset.
This is a no-prime-slot prototype, not a realization of a selected slot
vector J. Its relevance is to a proposed coefficient-majorant closure
that must include this prototype or zero-slot recursive children; it
does not itself disprove a more specialized argument for a fixed
nonempty physical J.

## Exact normalization and scope

For the unpunctured zero-common-support Gauss sector, the source's second
transform gives F(v,v;0)=phi(v). Its inverse roots contribute 1/Nv,
the column normalization contributes U^(-A), and the effective row
factor contributes U^(K+g-ell). This verifies (9).

To majorize this diagonal separately by U^(A+Lambda), its coefficient
norm would need power 2A+Lambda-(K+g-ell). At the upper first-frequency
length K0=2A-1, this is 1+Lambda before the explicit small positive
enlargement allowances. Those allowances can only worsen this requested
coefficient bound. The working-box gap is exactly
(1-d)r+2m-1+1/540 > 1403/6750, using d<=21/50, r>=7/10,
and m>2/5. The strict endpoint is correct.

The transformed off-diagonal terms have signs, so the displayed diagonal
is not a lower bound for the complete positive Gauss norm. First-stage
coprimality inversion also introduced artificial common pairs that cancel
in its full signed Mobius sum. Neither this benchmark nor the prime ideal
count permits isolating a positive contribution from the original
selected correlation. Note 18 explicitly retains both limitations.

The viable unresolved choices therefore remain a joint first-transform
or artificial-Mobius bilinear estimate before the damaging absolute
step, or a direct weighted-response tail. Merely proving a positive
marked coefficient l2 bound or applying unchanged two-plain centering
cannot supply the missing power.

## Finite verification

At this phase-2 review, the staged checker passed all 206 assertions.
The subsequent source-slot refinement extends it to 215 assertions;
the final small record identifies that checker and its operational-record
dependency by SHA-256. The coordinating replay verified the final record.
It checks finite coefficient algebra, exact rational budgets and layer
integration. It supplies neither the asymptotic prime ideal theorem nor
a native selected-bin example. Its stated scope is appropriate.
