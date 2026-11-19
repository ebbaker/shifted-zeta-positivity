# AGC-E04: analytical draft assessment

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. The parent records the accepted helper
dispatch as **gpt-6.1-sol, reasoning effort ultra**, with
`fork_turns="none"`; independent serving-backend attestation is
unavailable. The lead is recorded as gpt-6-astra/max. This is a separate
internal LLM assessment with inherited source premises, not independent
specialist or human review.

**Final status after the single correction check: accepted within the
stated analytical-background, conditional-interface and research-setup
scope.** The two hypothesis clarifications and two integration repairs
below were implemented. No unresolved mathematical defect remains from
this assessment. No new canonical estimate, numerical certificate, zero
coverage or Newman bound is established by this assessment.

## Request, classification and inspected material

Executed the bounded request [AGC-E04-r1](../research-progress/handoffs/AGC-E04-r1.md):
one complete mathematical pass, followed by one correction check. The
manuscript was read without editing it. No numerical campaign, certificate
replay or additional helper was run. The two author returns were inspected;
their own checks are not counted as independent evidence.

The read-first [result index](../../../../result-summaries/README.md) and
[avoid index](../../../../avoid/README.md) route the relevant limits through
[Controls12](../../../../result-summaries/12_collision_controls_and_screening.md),
[classification01](../../../../avoid/01_restating_the_target.md),
[premise screen02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[shared-premise05](../../../../avoid/05_same_model_reviews_and_shared_premises.md),
[scope07](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[normalization08](../../../../avoid/08_normalization_and_constant_slips.md),
and [source imports16](../../../../avoid/16_unchecked_imports_and_novelty_claims.md).
The draft's output is an exposition of inherited identities, elementary
derivations and conditional quantitative consumers. It does not count an
RH-equivalent reformulation or an unevaluated inequality as acquired
arithmetic progress. Its future milestone is a smaller complete error or
a longer protected interval against a comparison using the same source
information, with the numerical margin and domain stated.

Read all seven sections, `main.tex`, the E02/E03 returns, and the inherited
VCD-GT-CM manuscript's `13_canonical_time.tex`, including its stopped
all-real acquisition and complete-tail argument. Selected primary passages
were opened directly in [Polymath v2](https://arxiv.org/html/1904.12438v2),
[Platt--Trudgian v1](https://arxiv.org/html/2004.09765v1), and the
[pinned Gomila proof note](https://raw.githubusercontent.com/judegomila/dbn-lambda-01787854-candidate-audit/a74738deb6d5e0f76887cb36901da08b68dca705/PROOF_NOTE.md).
This was a selected-passage attribution check, not a complete proof audit
of those publications or the external proof package. The earlier source
receipts and internal audit remain the provenance for package-specific
binding and partial-replay claims.

## First-pass findings, all addressed in the correction check

1. **Make closed-interior holomorphy explicit in Section 6.** At the start
   of “A two-zero contour retains a joint error,” require both fields to
   be holomorphic on a neighborhood of the closed interior of the simple
   contour, as well as nonzero on its collar. Saying that an “analytic
   reference” is nonzero near the contour and has two interior zeros
   leaves its analytic domain implicit. Argument-principle power sums
   count zeros minus poles; the displayed two-zero formulas need the
   pole-free closed interior. For the intended fixed-cutoff reference this
   is supplied by placing the closed interior inside its right half-plane
   domain. This is a hypothesis clarification, not a change to the
   derived identities.

2. **Separate the remainder and heat-defect symbols.** Section 5 uses
   `R_N(t,s)` for the exact Riemann--Siegel remainder, while Section 6
   reuses `R_N(t,z)` for `P_{N,t}+P_{N,zz}`. Use, for example,
   `\mathcal R_N` for the physical heat defect, matching the notation
   table. The equations themselves are correct; the present reuse can
   obscure which object satisfies the forced error equation.

3. **Repair the final Section 6 control-screen reference.** The detailed
   family screen is in `sec:program`, not `sec:continuation`. The exact
   quadratic control appears in both discussions, but the all-family
   routing should point to Section 7.

4. **Repeat the positive-omission premise in the actual head bound.**
   In Section 4's “Finite heads,” begin the robust actual-configuration
   statement explicitly in the all-real adjacent-pair stopped regime.
   The preceding discussion correctly identifies this requirement, but
   the head statement starts only with a lower target gap and upper
   distances to selected neighbors. Those neighbors alone cannot license
   dropping a signed or nonreal remainder from `K`. This simply makes the
   already intended hypothesis local to the displayed bound; its
   constants and proof remain unchanged.

No other mathematical defect was found in this pass. Acceptance does
not waive the explicit assumptions or acquire the open quantitative
inputs listed below.

## Derivations checked

**Source and counted pair.** The theta normalization, `x=2 gamma`,
`H_t=-H_zz`, and reversed-time Gaussian law are consistent. Positive
`H(t,0)` and the compact-time growth estimate justify Jensen counting and
the inverse-square tail. Even order at most one removes the otherwise
undetermined linear exponential in the paired product. Deflation gives
`c_t=R(a)+R(b)` and `D_t=2-4DM`; the sign of the divided difference,
the contour expression for `M`, and `D_t=2` at a cleared target double
agree. The affine remainder has its stated `2 C_3 |D|^2/3` bound.

**Gap chain and scale.** The left and right cumulative distances enumerate
each exterior occurrence once, with denominators `r(r+g)`. Their sum
gives `g_t=4/g-2gM`; the block identity follows by finite telescoping of
the same node fields. The density factor `1/(4 pi)` is consistent with
the doubled height. Frozen rescaling and the additional derivative cost
for a moving reference length are retained. A finite real block does not
license positive omission of unknown real or nonreal exterior terms.

**Integer hierarchy and limits.** Reciprocal-power subtraction gives the
split recurrence after the nonabsolute first-power sums cancel. The
axis formulas, overlap constraint, and conversion to `S_n,T_n` retain
their convergent ranges. Recomputing the divided differences and
diagonal subtractions gives the displayed regular coefficients, in
particular `M_t=2M^2-12S_2-16DS_3` and the positive `4T_2^2` term in
`(S_2)_t`. The finite-product passage uses spatial convergence and the
Burgers time jet on a fixed cleared contour at a single slice. This
justifies each fixed-order equation through exterior multiplicities;
it asserts neither common-time convergence of those approximants nor
uniformity in moment order. Raw split coordinates correctly retain
their possible square-root singularity at a target collision.

**Complex exponent.** The half-plane `Re p>1/2`, the extra strip,
unit-count and safe-line assumptions, local logarithms, and central
branch corrections are stated. The derivative at fixed centered
coordinate includes `c' h_w`. Integration by parts retains the full
`(f_p)_w h^2` interaction. The safe-ray majorants and separated vertical
closures justify the infinite contour passage at fixed real-part
strips. Conjugate logarithms require positive real exterior
denominators; a uniformly assigned negative-real argument has the
displayed sine defect. The Mellin/Laplace representation is restricted
to its positive or right-sector premise. Gaussian damping makes the
two-line recovery absolute and leaves exactly the integer residues;
its branch corrections vanish there. This supplies a representation,
not a stronger forcing bound or an independent complex-split recurrence.

**Continuation.** Integration of the drift needs the supremum over
all preceding cumulative signed allowances. Riccati comparison gives
the stated initial-mass bound and shrinking duration; that duration is
not an actual collision prediction. The equations
`D_u=-2V` and `V_u=(1-V^2-K)/D` give the stated barrier by an integrating
factor on compact stopped intervals. The sufficient `L^-2` and `L^-4`
rates follow from its square root. The finite-head telescoping identity
and constants `18e,6e` check. Comparison with inherited Section 13
confirms that the high-height `V,K` acquisition uses individual clock
localization and a complete tail on a fixed positive slab. It is
restricted to the globally real simple stopped regime when positive
omission is used; it does not extend imported zero coverage or pass
uniformly to time zero.

**Arithmetic reference and forced error.** The two analytic carrier
branches define a fixed-cutoff holomorphic reference on the right
half-plane. The exact Gaussian terms, their star operation and complete
remainder have the stated source domain. The exact term satisfies
`r_t=r_ss/4`; differentiating the actual exponential approximant gives
the displayed defect, including its nonzero `b` term at time zero.
Changing from `s` to `z` and then reversing time gives exactly
`E_u=E_zz+\mathcal R`. The arithmetic damping coefficient is `t/4` by
direct expansion; the draft does not import an onset constant from the
inconsistent intermediate source display. Cutoff transitions are known
reference changes requiring a seam payment.

**Residual propagation and contour consumer.** The Duhamel proposition
uses bounded classical whole-line solutions on each horizontal line;
its explicit global premises justify the norm contraction and interior
Cauchy factor `2/(h-h')^2`. The draft does not claim those premises for
the half-plane reference. The local exponential heat example proves
only failure of the stated local-data bound. The gap readout, joint
numerator `P E_zz-P_zz E`, center-log formula, reference heat-defect term,
and full drift-difference signs check. Every quotient floor is paid in
the stated outer bound. The later log-moment formula retains the full
quadratic center correction. A spatial multiplier cancels from the
joint numerator; its time or spatial defect remains in the full
reference readout. The mollifier convolution and positive division
step are correctly separated from physical heat evolution.

## Imported scope, controls and unpaid conclusions

The selected-source check supports the draft's attribution of the
normalization, exact Gaussian expansion, individual term estimate,
complete value-error theorem and strip-criterion regions. The value
theorem's wider domain is kept distinct from the exponentially late
clock-localization domain. The smaller correction error is attached to
the corrected approximation center. Platt--Trudgian's exact verified
endpoint and its `0.2` corollary are retained; the exact pinned Gomila
row and finite-height reserve are correctly computed. Gomila remains
an attributed package claim awaiting peer review, without a fresh
certificate replay or status upgrade here.

The explicit quadratic has zero residual and still merges exactly when
the strict margin is exhausted. The cosine-plus-constant heat control
has almost uniform initial gaps but loses the whole-time forcing floor.
The Section 7 family screen names failed canonical premises rather than
claiming that generic algebra rejects every control. In particular the
Euler-factor/weighted-square families lack unchanged complete arithmetic,
the reflected super-Gaussian lacks the required order-one product, and
the positive-primitive constructions lack complete theta arithmetic.
The screen is analytical, not a replay of the existing certificates.
The draft expressly says that identifying a missing exact premise is
not proof that a coarse future estimate uses that premise effectively.

Open work remains an actual counted initial reference pair, complete
time-uniform residual and derivative payments, denominator floors,
cutoff seams, heat tails or lateral boundary data, and a strictly useful
final gap/strip margin against direct evaluation from the same
information. Global improvement additionally needs all height and
interface coverage. The text does not upgrade the local-data example,
the initial Riccati allowance, or the retained-correction issue into a
universal obstruction to other estimates.

## First-pass source binding

SHA-256 at the end of the complete first pass, before the lead's
corrections; paths are relative to `manuscript/sections/`:

| Source | SHA-256 |
| --- | --- |
| `01_source.tex` | `077d19c7334ed26f04bd4589ba86a983855a49b5f22a57d064e7dd123d0ef6f1` |
| `02_pair_chain.tex` | `52d7dddd192271857ebf07a67ab7d03f28fef0d0db1499092e7cdceb514330e0` |
| `03_hierarchy.tex` | `1c4f430dec041f8c719e7097cc6771cc23be974e8c5d5e13b6df662248aafd36` |
| `04_continuation.tex` | `930e6ed17d1ebd71379aff63e68bd8bfa8edc59b08401d4695a2cab2e8246766` |
| `05_arithmetic_source.tex` | `b98864ec7ed9b95b210dd4f2ac26a0b756a50473c13e29c9692ae0d3ec24293d` |
| `06_residual_transport.tex` | `cb2707ff4b5bad3bb750776f9d25f3bc4ba83a132cdfa4f8099bb88a9b28160c` |
| `07_program.tex` | `8b4d799215cb4b9ada0c29d6295ca5ed29765c3ef9f9cf01f5b30fc965ddbc75` |

The hashes identify inspected bytes; they do not validate a proof.
The one bounded correction check is recorded below.

## Setup and sustained-continuation assessment

The subsequently supplied investigation README, overview, research plan,
continuation/pasteable prompt, source/status crosswalk, B00 scope decision
and sole progress register were read against the root setup and B/E model
workflows, carrying the author's express modifications. They consistently
distinguish this requested setup/manuscript delivery from future research
activation. B01 is the first unactivated research choice; dependent E
tasks require its frozen reference, domain, consumer and direct comparator.

The sustained-turn policy is coherent: local work packets and their
correction passes remain bounded, while the lead proceeds through ready
authorized choices, derivations, comparisons and integration without using
one helper's completion as an automatic turn boundary. A failed first
estimate can lead to the next documented in-scope decision. The scientific
source remains unchanged theta, analytical work leads, and new zero
coverage requires a separate complete margin and domain. Source provenance,
actual versus requested model settings, old task ownership, and the
founding chat's unique existing home are preserved. No further mathematical
scope correction was identified in these setup texts. This assessment
does not itself activate B01 or authorize an unbounded numerical campaign.

## Single bounded correction check and final disposition

19 November 2026. Per the lead's correction-freeze message, checked the
changed statements in Sections 4--6 and their surrounding arguments,
the symbol replacements, the final routing and the completed bibliography.
Sections 1--3 and 7 retain exactly their first-pass hashes.

- Section 4 now places the robust head statement explicitly in the
  all-real adjacent-pair stopped regime. Positive omission is justified
  within that regime, with unchanged constants and conclusions.
- Section 6 now requires both fields to be holomorphic on a neighborhood
  of the contour's closed interior and nonzero on its collar. The
  argument-principle readout consequently has the required pole-free
  premise.
- The physical defect is consistently `\mathcal R_N` in the fixed-cutoff
  forced equations; `R_N(t,s)` remains the exact arithmetic remainder.
  The final family-screen reference points to `sec:program`.
- Section 5 restricts the displayed strip criterion to
  `0<t0<1/2`, `X>0`, `0<y0<sqrt(1-2t0)`. This is a valid restriction
  to the used regime, not a stronger source claim. The cited criterion
  imposes no additional lower floor on `X`.
- The short new paragraph treats `0.1782354` only as the live author's
  later, separately unreviewed research report. The relevant paragraph
  of the [live page](https://www.judegomila.com/posts/riemann-lambda-0.1787854)
  was opened directly in this correction check. No audit of that later
  research package is claimed or needed for this attributed statement.

The corrected source binding is:

| Source, relative to `manuscript/` | SHA-256 |
| --- | --- |
| `main.tex` | `fae8ce8c9ffb362a16f65754990a57d3b899a0c5e3673425cf4362019590861d` |
| `sections/04_continuation.tex` | `c676909e61948f8d098aba46dea2a46e178931ef24e2fdd10c52213bd59d97bb` |
| `sections/05_arithmetic_source.tex` | `9c2be91c73a85408f15b9e3fd5755c9cbf766c896575a7d716ddb8c235dfcf8c` |
| `sections/06_residual_transport.tex` | `2edf4ac9a5ca64eddfc774db63e8a6ec390bc791721ea1256ebdad83f2741343` |

**Accepted within scope.** The draft accurately separates the complete
field identities, their conditional continuation consumers, inherited
fixed-positive-time acquisition, and the still-open arithmetic gain and
global assembly. The setup supports the author's sustained multi-step
continuation without treating bounded helper returns as turn endpoints.
The complete first pass and this one correction check are finished.
Production/build and visual inspection belong to the lead's separate
E05 task; this mathematical assessment is not evidence of that work.
