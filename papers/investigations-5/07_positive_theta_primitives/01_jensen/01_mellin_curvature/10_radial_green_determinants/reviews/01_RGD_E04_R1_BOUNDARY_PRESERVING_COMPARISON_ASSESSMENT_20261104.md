# RGD-E04 r1 — boundary-preserving comparison assessment

4 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded reviewer **gpt-6.1-sol
(Codex), reasoning effort ultra**, research chat0003, thread
`01a1a77f-2607-7832-9902-29399c58b442`, turn
`01a1a77f-28bf-7121-a260-46291cd2f2a4`.

**Disposition: accepted without correction within this internal assessment.**
RGD-E04 r1 is complete; RGD-E03 r1 is analytically ready. The author has
explicitly requested its execution after acceptance in this chat. This
assessment itself contains no new numerical sign measurement.

**Relationship:** a different-model internal assessment of Astra/max
Note01 by Sol/ultra, with one fresh read-only same-model contributing
check of obligations 1, 2, 3 and 6. The coordinator checked all eight.
The source normalization, inherited identities and lower-order inputs are
shared premises; this is not independent specialist review.

## Scope and locked inputs

The [frozen Packet01](../research-progress/handoffs/01_RGD_E04_R1_AND_E03_R1_BOUNDARY_PRESERVING_COMPARISON_20261104.md)
owns the eight obligations and diagnostic limits. No formula, source,
comparator, index or payment is revised. Assessed [Note01](../notes/01_BOUNDARY_PRESERVING_FIRST_MODE_COMPARISON_20261104.md)
SHA-256: `556a97aa60f7a3448acbd00cf8bfa4c3e2916e428f67d03dbb97889077bc9847`.
Packet01 SHA-256: `da639d27f073b6ec4cf7291263da4756c1ccff7133fb7ccf6e47786928c9fd6a`.
All six inherited inputs match Note01's input-version table, including
its overview, Note06, checker/25-case record, accepted Jensen Review01
and parent balance note. These are working-tree versions, not a clean
commit. The inherited exact record is reused without replay and supplies
normalization evidence only.

Read with the [result index](../../../../../../../result-summaries/README.md),
[theta cluster](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md),
[collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md),
and [avoid index](../../../../../../../avoid/README.md), particularly
[target reformulation](../../../../../../../avoid/01_restating_the_target.md),
[joint payments](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [bounded numerics](../../../../../../../avoid/10_numerics_ahead_of_the_question.md).

## Eight acceptance checks

1. **Source and normalization — accepted.** With
   t_n=pi*n^2*exp(4u), direct differentiation gives
   p_n''-p_n=8*p_n*(2*t_n^2-3*t_n)=8*Phi_n. Twice integrating by parts
   against m_j gives the stated 1/8-scaled primitive differences. Complete
   reflection yields p'(0)=-1/2 and b=1/16; negative indices vanish.
   Individual-mode reflection is never invoked. Keeping b fixed in both
   polynomials preserves every boundary-volume term.
2. **Infinite modes — accepted.** The tangent inequality exp(4u)>=1+4u
   gives (5). The integral of u^(2j)*exp(-lambda*u)/(2j)! equals
   lambda^(-2j-1), with no residual factorial. For integer n>=2,
   n^2-4-5(n-2)=(n-2)(n-3)>=0. Replacing each denominator by
   (16*pi-1)^(2j+1) and summing the geometric numerator proves (6) for
   every integer j>=0; positivity licenses Tonelli. Applying the same
   lattice inequality to n^2-1 proves (7).
3. **Endpoint gain — accepted.** beta_n=-p_n'(0)/8>0 and their complete
   sum is b. Individual-mode Green transfer gives the exact reference
   measure Phi_1 du+(b-beta_1)*delta_0. This measure is positive, without
   proving a PF property. The c0 errors are exactly y0 and tau-y0>0.
   Dividing tau>=beta2 by y0<=E0 yields
   a^2*(1-exp(-5*pi))-1>2200. The elementary lower value 2205.791 is
   correct. This is confined to the two stated c0 approximations.
4. **Joint expression — accepted.** Each F is cubic in b,z, so its
   collected square-minus-neighbor-product polynomial has degree six.
   With b fixed, the multivariate Taylor expansion through degree six is
   exact. Collecting coefficients before summing |t_alpha| E^alpha
   preserves algebraic cancellations and proves (15) componentwise.
   Correlations between residual moments are subsequently discarded.
   No sign of D4 is assumed; a positive L remains a sufficient test.
5. **Two structures — accepted.** Expanding the displayed F1^2 and A^3F2
   cancels A^4D^2 and leaves precisely the eight terms of (16), including
   -2A^3BCD. Multiplication of the stated quadratic and quartic factors
   gives those same terms. Formula (17) is the six-permutation 3-by-3
   determinant with its two equal negative products combined. At k=4,
   F3,F4,F5 use c1,...,c7, so c0 and b are absent. The required primitive
   moments are 0,...,4 at k=1 and 0,...,7 at k=4. Boundary faces at k=1
   remain present. E03 will retain the prescribed separate exact
   permutation checks of D4*D2 before numerical evaluation.
6. **Spatial exterior — accepted.** Put u=U+v; then
   p1(U+v)<=exp(U-pi*exp(4U))*exp(-a_U*v). Expanding (U+v)^(2j)
   and integrating v^h yields exactly (18), including h!, (2j)! and 1/8.
   Here a_U>0 for U>=0. Thus 0<=(x-x^U)+y<=B(U)+E; expanding the same
   joint polynomial at x^U proves (19). No finite-domain Green identity
   or artificial endpoint at U is used. Numerical acquisition errors
   are not paid by these analytical tails.
7. **Consumer and scope — accepted.** The accepted Jensen assessment and
   parent balance note explicitly supply D2,k>0 and D3,k>0 at time zero
   under their stated internal-review status. D4=Q3/D2 is conditional on
   a successful acquired lower bound. Selected primary passages were
   rechecked: [Katkova (4)–(5), Theorem 1](https://arxiv.org/html/math/0505174v1)
   give b_j=8*4^j*c_j and PF44; positive geometric scaling preserves
   minor signs. PF44 supplies nonnegativity, without a new strictness
   theorem from this calculation. [DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32)
   at z=0, tau=iR^2 confirms the inherited reflection. Full external
   proofs and the lower-order certificate were not newly audited.
8. **Diagnostic readiness — accepted.** The fixed sufficient question
   L_(k,2)>0 at k=1,4 has complete analytical n>=2 and u>2 payments.
   Five/eight variables of total degree <=6 allow at most 462/3003
   monomials including the constant. The 80/120-digit comparison, single
   conditional 160-digit pass, degree-10 quadrature ceiling, 250,000
   callback limit and 180-second total computation cap are finite and
   discriminating. [Official mpmath quadrature documentation](https://mpmath.org/doc/current/calculus/integration.html)
   confirms the breakpoint list, tanh-sinh, error estimate and maxdegree
   options. Neither estimates nor precision agreement certify errors.
   Adding tiny B may round to E; B must remain separately recorded.

## Control screen and decision

The new input is the literal complete unit-square expansion and its
quantitative payment, not generic positivity or a repackaged determinant
identity. Weighted-square controls change unit coefficients and require
new endpoint/tail calculations. Euler-factor controls change the literal
series. Reflected and smooth positive-primitive controls do not supply
that square expansion. None has been numerically tested here or asserted
to fail this finite L test. Any source satisfying the same quantitative
box would satisfy the same generic polynomial estimate. A positive-time
collision does not contradict this time-zero finite-order comparison.

**Accepted claims:** the analytical bounds and scoped c0 gain in Note01;
the feasibility signs remain unmeasured at this assessment boundary.
No Mellin/Gaussian bound, unbounded-index result, order induction, new
coefficient range or RH conclusion follows. No correction cycle is needed.
Global result-summary maintenance is deferred: this is an intermediate
method assessment, not investigation closure or a manuscript milestone;
parent/sibling and global ownership is outside this packet.

**Next: [E] RGD-E03 r1 — Sol**, execute the already authorized fixed two-case
floating diagnostic. Preserve exact b, combined cancellation and all tails;
stop at its declared pass/adverse/inconclusive return. E02 remains unissued
and B03 gated. The sole progress register owns the resulting readiness.
