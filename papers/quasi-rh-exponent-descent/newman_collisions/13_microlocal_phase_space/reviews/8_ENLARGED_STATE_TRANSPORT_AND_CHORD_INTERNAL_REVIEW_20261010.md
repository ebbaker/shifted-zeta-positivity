# Enlarged-state transport and chord dynamics: internal review

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); the exact serving variant and configured reasoning
effort are unavailable and are not inferred. Parallel cross-readings and
exact algebra replays are internal LLM checks, not independent mathematical
validation.

## Scope and disposition

Reviewed the final [Heat Note 25](../../notes/25_ENLARGED_STATE_TRANSPORT_CHORD_DYNAMICS_AND_THETA_GLUING_20261010.md).
The program 09 analytical agent confirmed Sections 1--3 and 7--8. The
program 13 analytical agent cross-read Sections 4--6, checked the revised
wording and signs, and independently verified the new asymptotic exponent
target in Section 8. The root agent also replayed the finite algebra source.
No correction to the final printed identities was identified. The result
is a conditional certificate lemma and a revised proof program, not a
constructed visibility certificate or a signed theta estimate.

## Analytical findings

- The prescribed divisor edges and the source anchor uniquely prepare the
  genuine finite state. Constant twists preserve diagonal bulk evolution
  but fail those same fixed physical edges. All tangent identities retain
  the spatial carrier and amplitude drift.
- The anchored operator is positive definite; its hidden coordinate blocks
  are invertible independently of observation nonvanishing. Exact Schur
  elimination therefore does not presuppose the desired conclusion. Its
  spectrum is independent of the carrier frequency only at fixed time and
  amplitude parameter; that parameter also moves on the physical orbit.
  Source coercivity alone does not imply observation coercivity.
- Pairing the adjoint certificate with the complete realified state gives
  the stated lower bound. The residual is paid by the full weighted sum
  of block norms. The correlated first-jet body gives the candidate norm
  upper bound eta/2 and its directional support refinement. These statements
  exclude every multiplicity on a domain where useful, uniform multipliers
  and residual bounds have actually been supplied.
- The chord generator has the correct backward sign. The transverse jet
  source coefficient is r(2r-1)/2. The derivative-state overlap obeys
  (partial_ell^2+k^2/4)A=-B and B_t=L B-(k partial_k+ell partial_ell+1)A.
  The scalar slice remains autonomous; the higher channels supply no
  automatic feedback or positivity theorem.
- The score identity D=4C+Fourier[m(W'-beta u)^2] and its conditional
  threshold quadratic have the printed signs and coefficients. Beta must
  be frozen under spatial differentiation. The elimination uses both exact
  collision equations; approximate candidates need all lower-jet defects
  and normalizer payments restored. The negative k-squared coefficient
  cannot be detached from its compensating mixed and derivative terms.
- Fourier injectivity turns the proposed finite constant-coefficient
  transverse closure into a polynomial condition on W''. The genuine
  exponential theta tail violates that condition. This excludes the stated
  closure, not nonlocal or arithmetic relations.
- The Gaussian control has Fourier prefactor sqrt(pi) alpha^(-9/2), the
  printed quartic numerator, and discriminant 96 alpha^2(1-alpha^2).
  At alpha=1 it has ordinary doubles at plus/minus sqrt(6); for
  0<alpha<1 both squared roots are positive. It is a bounded-time
  positive-threshold control with pure-state completion, not an all-time
  super-exponential theta family. Its scope is sufficient to reject local
  exclusion based solely on purity and the exact chord lift.
- The angular relation includes the required endpoint source and the
  positive 2it T_z term. The shift z-4i supplies the factor e^(4u).
  The explicit kernel identity (partial_u^2-1)k(u,0)/16=Phi(u) correctly
  identifies its cosine readout. The full theta coefficients and Jacobi
  gluing select more data than the periodic heat PDE alone. The complex
  shift needs a separate quantitative payment beyond the small Cauchy disk.
- The reflection map is a linear unitary involution on the stated L2
  space; adding conjugation is a different antiunitary map. Its stationary
  coefficient is local leading data, not an endpoint-uniform theorem.
  Reflected literal blocks, exterior channels, and all boundary payments
  remain necessary.

## Verified asymptotic visibility target

Suppose R_up <= 1-delta and Y_up <= C N^alpha with constants delta>0
and C>0 uniform on kappa in [1,3/2] and small positive time. The natural
cutoff has log N=kappa/(2t)+o(1), with the o(1) uniform on that closed
subsector. The imported complete error majorant gives

\[
 \eta Y_{\rm up}\le5C\exp\left\{
 -\frac{\kappa(\kappa+4-8\alpha)}{16t}+o(1)\right\}.
\]

For alpha<5/8, let epsilon=5-8alpha>0. Since kappa>=1,

\[
 \eta Y_{\rm up}\le5C\exp\{-\epsilon/(16t)+o(1)\}\longrightarrow0
\]

uniformly. Eventually eta Y_up<2delta, which implies the strict
certificate criterion (1-R_up)/Y_up>eta/2. This verifies the stated
exponent threshold. It does not establish R_up, Y_up, an effective starting
time, or uniform cutoff matching. Those are the proposed proof obligations.

## Exact algebra replay and its limits

The checker [check_enlarged_state_identities.py](../numerics/check_enlarged_state_identities.py)
passed a fresh review-agent replay with **15446 exact Fraction assertions**:
257 graph controls, 27 Gaussian controls, 162 chord controls, and 15000
score controls. Its SHA-256 matches the root replay:

`645292360a4afc8edb49a6ffec550ec4277d4c74c8497164050aaf1f058b2435`.

The small [record](../numerics/ENLARGED_STATE_IDENTITY_RECORD_20261010.json)
identifies the anchored three-node Schur example, Gaussian numerator and
threshold factorization, chord commutator on monomials through degree
eight, and the score dictionary on rational jet configurations. This is
finite algebra validation. It does not certify the infinite theta state,
the imported holomorphic interface or counting theorem, analytic domains
by execution, a huge-height sign, or numerical candidate coverage.

## Remaining proof task

The immediate task is an explicit regular adjoint multiplier construction
with a residual gap and multiplier growth within the verified exponent
budget, retaining every disconnected source sector and cutoff boundary.
The parallel chord task is a genuinely theta-specific signed gradient/score
correlation controlling the complete current or joint threshold expression.
Neither useful multiplier bounds nor that correlation have been obtained.
Generic parent positivity, purity, and leading reflection do not supply
them. Global parameter coverage and any higher-multiplicity obligations
outside a first-jet visibility theorem remain open. No RH or new collision
exclusion follows from this note and replay alone.
