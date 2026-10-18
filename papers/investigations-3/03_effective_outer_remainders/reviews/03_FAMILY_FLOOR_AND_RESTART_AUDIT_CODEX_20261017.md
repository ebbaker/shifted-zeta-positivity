# Audit of the uniform family floor and restarted comparison

17 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded reviewer: **gpt-6-astra (Codex)**; reasoning effort: **max**.

**Disposition:** no blocking mathematical defect found in the designated
round-two family proof chain. Retain its status: **proved in-note from
named imports, with Arb/exact scalar certificates and internal same-model
checks**. Both certificate outputs reproduced byte for byte. Independent
specialist review remains outstanding. A nonblocking manuscript status and
literature correction is identified below.

This is additional same-model review: the round-two derivation used
gpt-6-astra at ultra effort. A change of effort does not make this
cross-model or independent review. No subagents were used for this audit.

## Scope and source identity

The target is the [uniform floor](../notes/round-2/01_UNIFORM_FAMILY_FLOOR_CODEX_20261017.md)
and [restarted comparison](../notes/round-2/02_RESTARTED_STRIP_COMPARISON_CODEX_20261017.md),
including the family saddle, Gaussian transport and remainder proposition
in the [current manuscript](../manuscript/height_p_transport.tex).
I checked the analytic domination and parameter coverage as well as both
certificate programmes. Project 01's approximation and compact comparison
were checked in its
[review 03](../../01_dirichlet_newman_families/reviews/03_CROSS_MODEL_MATHEMATICAL_REVIEW_CODEX_20261017.md).

The [replay record](../numerics/REVIEW_03_FAMILY_REPLAY_CODEX_20261017.json)
pins every principal source, script and output by SHA-256. The two proof
notes have hashes `a8b1bf8cb2b6cafc00eb51ee19b9a1bc6266a6191ef0f1604922e33a70d03374`
and `4a0f968d770b10621c1d54bc0af030cb72731110e6f806d3a5b9ea78d3f23f02`.
The reviewed numerical records were not overwritten.

The audit does not certify the round-one near-threshold no-loss tables,
the derivative-circle estimates, or the conditional zeta 0.18891 consumer.
It checks the family portion of the inherited analytic machinery, not
every statement in the wider transport manuscript. Published strip
theorems remain named imports; their complete source proofs were not
reconstructed in this audit.

## Analytic floor: checks that matter to the certificate

The domain is h=t/2 in (0,1/8], ell >= 129/5, and
sigma=2+h ell/2. The saddle remains in the right half-plane and its real
part is no smaller than the real saddle in [2,infinity). The contraction
bound and the digamma lower bound give ell >= ell_0 for every real
height, including negative height for a non-even character flow.
The Stirling proxy is used only on its permitted real-part range; the far
reflected tail uses an Euler-product estimate instead.

The shifted Gaussian representation permits a complex saddle: order-one
growth justifies the contour displacement. The denominator is complex,
so positivity of a Gaussian weight cannot replace its lower bound.
Subtracting the pure exponential tilt and performing the two integrations
by parts reproduces the remainder formula, including the boundary term,
the factor (1+hk) on N_L and the denominator (1-hk)d_0. All payments are
needed and are present in the code.

The following steps were checked directly against the formulas and code.

1. **Taylor moments.** The even Gamma derivative bounds dominate both
   parities. The folded Gaussian second moment and 2 Phi(z) <= 1+4z/5
   give the displayed M_2 majorant. Its factors increase in h, c and b.
   The programme's Taylor coefficients for log(zeta) and log(Gamma)
   include the correct factorial and half-argument factors.
2. **Moving cutoff and time cells.** On each cell the lower sigma endpoint
   supplies the larger decreasing coefficient functions. The two explicit
   inequalities involving V_- and h_+ justify monotonicity of the boundary
   density and first Gaussian moment. The first cell covers every
   0 < h <= 1/8000; it does not begin at its positive endpoint. Time zero
   is handled by the exact initial Euler-product bound.
3. **Critical intervals.** With N=ceil(Q/2), the checked cutoff inequality
   gives log N <= ell+2. Partial summation then yields the stated
   (ell+5) exponential bound. Including the numerator weight, the
   prefactor's logarithmic derivative is at most 3/ell, less than the
   magnitude of the negative exponent derivative. Thus replacing ell
   by 129/5 is justified for the whole weighted envelope. The reserved
   inverse-h term and AM–GM payments give the two Z_i,c_i bounds.
4. **Reflection.** At matching real part u, subtracting the Gaussian
   exponents and reflection factor gives exactly
   exp[-3(2u-1)/(2h)] <= 1. This uses sigma=2+h ell/2; omitting the
   saddle relation would lose the cancellation. The common critical
   numerator allowance covers both ordinary and reflected weights.
5. **Far reflection.** Completing the square gives the factor
   exp(-3 ell/2) and shifted Gaussian centred at w=-3. Its whole-line
   moment creates an artificial h^(-1/2) term. The three cases in the
   note remove it uniformly: h >= 1/100; ell >= 1/h; and the remaining
   domain with x >= 7/4. These cases cover arbitrarily small positive
   times and arbitrarily large conductor/height parameters.
6. **Assembly.** The programme forms E separately on each of 1,000
   rational cells; its extremal display is not a substitute for the
   per-cell decisions. Arb comparisons fail if a sign is uncertain.
   No floating conversion determines a mathematical inequality.

The replay certifies hk < 0.033447, d_0 > 0.931777 and
E < 0.192767, hence the advertised rational gates hk < 1,
d_0 > 93/100 and E < 1/5. The critical and far-reflected reserves also
pass. Since ell_0 > 25.909075565 > 129/5 and kappa(2) < 57/100,
the transport law gives

    S_chi(x,3,t) > 129/20 - 57/200 - 1/10 = 1213/200 > 6.

This holds for every real x, 0 <= t <= 1/4 and primitive q >= 10^12.
The computation certifies the scalar envelope; the preceding analytic
arguments establish that the envelope applies throughout the unbounded
family domain.

## The finite restart uses the right object

The intermediate-strip lemma starts with any squared strip q_0 <= 1.
For a step delta and c < m_C(delta), its approximants preserve that
initial strip and satisfy the short-time Burgers floor. The paired-zero
inequality therefore gives Q' <= -2-kQ, k=4c/3-1 > 0, until reality.
Compact contact and Hurwitz pass the resulting strip back to the original
input. When q_0=0 the strip theorem preserves reality directly.

The argument can be reapplied to an original time slice F_t: Gaussian
translation preserves order at most one (apply a sub-Gaussian bound for
every exponent greater than one), nonzeroness and reality, and satisfies
the semigroup identity. At each restart the arithmetic floor 6 is
available for that original slice. It is not assigned to the approximants
for a whole long interval. This distinction closes the possible logical
gap between a floor theorem for characters and a comparison through
non-character approximants.

For delta=1/10000 and c=1499/250, k=2623/375. The exact first gate is

    exp(1/20000) < 19488/19487,

which gives m_6(delta) > c. The terminal gate is

    exp(112789/75000) > 3373/750 = 1+k/2.

The affine recurrence from Q_0=1 therefore reaches zero by 2,150 steps,
at time 43/200 < 1/4. Earlier reality is preserved. Exact rational Taylor
bounds prove both gates; the displayed floating margins are diagnostic
only. They are approximately 1.3150121e-6 and 0.0016584941 respectively.
This proves the stated consumer at the source's current review level.

## Reproduction and controls

Each original programme was run once at its original parameters, with a
60-second stop per programme and no parameter search. Python 3.10.0 and
python-flint 0.9.0 were used; Arb precision was 128 bits. Both exited
successfully with no standard-error output. The floor record reproduced
SHA-256 `d3b409e223ab8f002ee040932029f863bdf13c670bdf18be3966082a4dcd2b34`;
the restart record reproduced
`7fe16236e4432e8c5148ad9fb54a2f3aad75315dadde98806880b45cb33cf416`.

The existing collision screen is appropriate to this arithmetic estimate.
The Euler-factor control's extra prime logarithmic coefficient violates
the zeta allowance. The other shape and positive-primitive controls do
not provide this primitive-character Euler product and partial-sum bound.
They therefore receive no inferred character floor. This is a premise
screen, not a claim that every other class fails the general comparison.

## Nonblocking documentation finding

In `manuscript/height_p_transport.tex`, the relation-to-other-work
paragraph at lines 213–216 still says no unconditional upper bound below
one half is known for Dirichlet L-functions. Project 01's
[source ledger](../../01_dirichlet_newman_families/source-documents/README.md)
already records Ki–Kim–Lee, Section 6, Example 1, for real primitive
characters; that statement must be corrected independently of the new
large-conductor result. The individual complex-character family remains
distinct from their self-dual real combination.

The exterior-input paragraph at lines 378–381 also describes the transfer
as outstanding and says the paper's theorems concern only the exterior
floor. Qualify that as the round-one scope and point to the now-proved
round-two restart. These introductory passages lag the status table and
the round-two notes. They do not invalidate the audited proof chain, but
should be corrected in the manuscript and rebuilt PDF before circulation.

The family floor and 0.215 comparison are accepted for continued internal
research at their existing stated level. Threshold optimization,
derivative-circle certification and specialist assessment remain separate
tasks. No priority conclusion or stronger bound is inferred from this audit.
