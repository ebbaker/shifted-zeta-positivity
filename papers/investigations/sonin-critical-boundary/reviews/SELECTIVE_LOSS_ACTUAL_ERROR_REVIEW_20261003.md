# Internal review of the actual prime error continuation

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Separate agents using the inherited model configuration checked algebra,
domains, source hypotheses, and frequency normalization. These checks are
internal, not independent specialist refereeing or a novelty assessment.

The [new note](../notes/selective-loss-program/09_actual_error_projection_and_frequency_20261003.md)
does not establish the requested global positive-remainder bound. It proves
a quadratic bound for the actual remainder's negative part, removes four
explicit harmless Chebyshev-error trends, and bounds the outer additive
frequencies unconditionally. The central signed projection remains open.

## Diagonal refinement and actual negative part

The stronger cumulative diagonal main is \(t\log t-t\), whose derivative
is \(\log t\). Thus the actual diagonal matches note 08's continuum
logarithmic diagonal through its constant-order term. No additional
\(-3X^2/2\) subtraction is present. The effective PNT error is uniform
on the fixed proportional band; integration against the vanishing weight
and its \(O(X)\) total variation gives \(o(X^2)\).

[Platt and Trudgian](https://arxiv.org/pdf/1809.03134), Theorem 1 and
Corollary 1, are unconditional bounds beyond their stated large-log
thresholds. They supply the required stronger PNT consequence. Their
finite-height verification input is a published finite theorem, not a
global RH assumption.

The resulting identity is
\(\mathcal R=\mathcal V-\beta_gX^2+o(X^2)\). Nonnegativity of the actual
variance gives \(\mathcal R_-=O(X^2)\), irrespective of any numerical
sign determination of \(\beta_g\). It gives no positive-part bound.
The original draft's phrase suggesting actual unboundedness of the
positive side was corrected to say that this side remains uncontrolled.

Both the regularized autocorrelation formula and Fourier logarithmic
formula for \(\beta_g\) have the correct constants. The damped Frullani
calculation justifies the spectral interchange. Mean zero and sixth-power
decay give a finite absolute logarithmic spectral moment; raw conditional
cosine integrals are not passed through absolute Fubini.

## Four trend removal and its scope

The exact operator is
\(Tf(s)=-s^{-1}\int_A^{2B}f(u)w'(u/s)du\). Boundary values vanish for
every \(s\in[1,2]\), so it retains both caps. The identities
\(T1=Tu=T\sqrt u=T\log u=0\) follow from the three prepared moments.
The Mellin multiplier \(zs^zG(z-1/2)\) confirms the double zero at zero
and the other two real zeros. Additional oscillatory null modes exist;
the note correctly treats the four-dimensional span as a subspace of the
nullspace.

The fixed Gram is positive definite. Its projection does not assume
arithmetic positivity or invert a Sonin metric. The exact Hilbert--Schmidt
value is \((\log2)\|w'\|_2^2\), including the \(e^{2v}\) weight in the
derivative norm. Coefficient rescaling between \(u\) and physical \(t=Xu\)
is invertible; the constant term absorbs \(\log X\). Thus
\(\mathcal H=X\|(I-\Pi)E(X\cdot)\|_2^2\), and the variance comparison
has no missing factor of \(X\).

[Brent, Platt, and Trudgian](https://arxiv.org/pdf/2008.06140), Theorem 1,
explicitly assumes RH for the upper mean-square estimate. It supplies
the conditional converse and is not used as an unconditional input.
The fitted target remains RH-equivalent. The discrete PNT countermodel
still has \(\widetilde{\mathcal H}\asymp X^{1+2\beta}\): the projected
cosine and sine profiles are independent modulo the four trends, giving
a positive two-dimensional Gram uniformly over their rotating phase.
This barrier concerns the generic counting model, not actual primes.

## Fourier localization and arithmetic input audit

The centered coefficient array includes every integer in \((AX,2BX)\),
with coefficient \(\Lambda(n)-1\). Poisson aliases have kernel size
\(O(X^{-5})\); pairing with the centered coefficient polynomial contributes
amplitude \(O(X^{-9/2}\sqrt{\log X})\), rather than \(O(X^{-5})\).
The lattice density alone has the latter size. These distinctions are
retained in the final note.

The rescaled Parseval identity has factor \(X\), giving total squared
frequency norm \(O(X^2\log X)\). Sixth-power Fourier decay gives outer
variance \(O(X^3\log X L^{-11})\). Therefore \(L=X^{1/11}\) supplies
the target bound for the outer contribution. The triangle inequality in
both directions proves equivalence of the central projection target and
the original variance target; no assertion about the sign of their cross
term is needed.

The central kernel remains a joint positive Gram in two frequency
variables. Scalar absolute spectral norms can charge endpoint terms that
the exact smoothing annihilates. The artificial oscillatory coefficient
example has squared coefficient norm of order \(X\) but variance of order
\(X^3\), so a coefficient-only bound cannot yield the missing improvement.
It is not a model of the actual von Mangoldt coefficients.

The [Montgomery--Vaughan author-hosted draft](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf),
Theorem 17.1, provides the stated prime exponential-sum bound. Testing its
denominators at frequency \(1/X\) leaves terms of order \(X\); the result
does not give the needed centered square-root cancellation. The note does
not claim this rules out all circle-method approaches. Effective PNT gives
the actual \(X^3\) variance envelope with a decaying square-root-logarithm
factor, which is still too large. No audited theorem closes the central
estimate unconditionally.

## Numerical replay and saved artifacts

Both scripts in the [new numerical package](../numerics/selective_loss_arithmetic_remainder_20261003/README.md)
were run by their author and rerun by the coordinating agent with the
existing Python 3.10 and NumPy 1.25.1. The arithmetic script keeps every
shift, prime power, and signed cap block in five noninteger shells through
\(X=501.125\). The signed remainder takes both signs. Its independent
variance-decomposition residual is below \(1.03\times10^{-8}\) absolute
at the largest shell, approximately \(4.1\times10^{-14}\) after division
by \(X^2\).

The fitted-error script splits at all integer breakpoints and kernel caps.
It uses weighted SVD least squares because the Gram condition is about
\(1.76\times10^7\). Raw squared norms have an independent affine-piece
check. Direct response and fitted-error response differ by less than
\(4.20\times10^{-13}\) at the sampled points; all four null-basis responses
are below \(3.69\times10^{-14}\). Orthogonality and Pythagorean residuals
are retained with the conditioning information. No outward enclosures,
real-interval certificates, frequency-tail numerical certificate, or
global fitted-error bound are inferred.

The records retain both script and imported-definition hashes. New files
are below the repository's one-megabyte convention. Local links and math
delimiters were checked. The overview, investigation index, and handoff
link the current target. Existing manuscript edits were preserved; no
new manuscript milestone, snapshot, commit, or push was created.
