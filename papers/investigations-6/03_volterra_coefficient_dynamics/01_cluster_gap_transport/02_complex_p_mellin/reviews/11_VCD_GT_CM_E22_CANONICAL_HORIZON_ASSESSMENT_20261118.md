# E22 — Canonical horizon proof and acquisition-scope assessment

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual serving model and effort unavailable;
assessor settings inherited. The assessor authored none of Note21,
Note20 or source audit04. A bounded read-only helper checked the OC
source crosswalk; it made no file changes. This is a separate internal
shared-premise LLM assessment, not specialist validation or cross-model
independence.

**Disposition: accepted within the stated canonical positive-slab
asymptotic and one-step comparison-limitation scope. No required
mathematical correction.** One proof/source/scope pass was performed;
no correction check was needed. The source imports remain published
inputs, while the full-interaction transfer is the new in-note derivation.
No Lambda improvement, compact gap-tail acquisition, effective cutoff,
time-zero tail theorem or E16 approximation theorem is accepted here.

The [E22 request][request] fixes the scope. All six files in the
[original manifest][pins] matched their recorded bytes and SHA-256 hashes
before assessment; all remained unchanged at completion. Hashes bind the
review to inputs and do not prove mathematics. In particular Note21 is
14,933 bytes with SHA-256
`3890ad3a86c4d4d0e75b4f5335397018eb21be472257c1670e1b81ac7e3197cf`.

Read-first routing: [result summaries][results], [cluster18][cluster],
[controls12][controls], [avoid][avoid], [classification01][class],
[premises02][premises], [scope07][scope], [joint12][joint] and
[shared-premise05][shared]. The proof supplies an explicit asymptotic
constant/rate for a defined comparison, not an RH-equivalent criterion.

## 1. Published input and uniformity

The primary [Polymath v2][poly] passages checked independently are
Theorem1.5(i)–(iv), its absolute-constant convention, and the §9 proof
around (102)–(105). The constants are uniform in positive t up to 1/2;
(i) has a height onset and (ii) an index onset. The latter's argument
principle counts one zero with multiplicity, hence a simple zero.
The proof of (i), after (104), actually gives displacement
O(x_n^(−ct)/log x_n), stronger than Note21's retained error. It places
all high zeros in the counted disjoint disks after increasing the
absolute onset constant. The unit-window bound counts occurrences and
has no exponential onset. No t=0 localization theorem is imported.

These checks support source audit04's positive-slab quantifiers.
Converting the index threshold by G(x,t)~x log x/(4π), and imposing the
minimum time t0>0, supplies one common high cutoff. Note21 also permits
further enlargement before using small normalized localization error.
The constant required for such a further enlargement is not numerically
computed. In particular no numerical exp(C/t0) budget is being certified.

The proof only uses positivity of M at the explicitly stipulated globally
real-simple slice. Its uniformity over such slices does not assume the
whole desired backward interval is real. The mention of t*=1/2 is a
classical all-real example; the simple-start premise remains explicit.
The local first-collision consumer is used only under its stopped regime.
The conclusion therefore makes no circular import of backward reality.

## 2. Local head and complete exterior passage

**Accept.** Let a=ξ_n, d=1/G_x(a,t), L=log(a/(4π)), and
η=L a^(−ct0)+1/a. For every actual zero in a fixed radius-two window,
source localization and G_x=O(L) give clock-value error O(L a^(−ct0)).
Subtracting the equation for a cancels its clock index and adds only
another error of this size. Taylor's remainder is O(1/a), since
G_xx=1/(4πx)−t/(16x²) throughout the fixed window. This proves the
normalized position equation (1), uniformly in all local indices.
No derivative bound is inferred by differentiating the localization
error. The three successive-gap formulas follow by subtracting these
position equations and retaining both errors for h_R.

In the near sum the excluded indices are exactly 0 and 1. Both integer
factors k and k−1 are bounded away from zero, so bounded absolute
perturbations of the factors yield the uniform relative error in (3).
The sum of absolute reference terms is finite and equals two. The
unit-radius index endpoints are of order L because d~4π/L; exhaustion
and consecutivity of the local labels justify the interval structure.
Their omitted lattice tails contribute O(1/L). This proves (4), including
the finite-window boundary payment.

For the far sum, r>=1 and g<1/4 imply
|ρ−b|>=r−g>=(3/4)r. The inherited unit-window count then gives a complete
shell allowance C Σ log(3+a+j)/j². Its logarithmic majorization and the
convergent Σ log(1+j)/j² prove O(log a). Negative zeros and the low-height
population are included; no unseen complete tail is discarded.
If a window crosses zero, splitting it into its nonnegative and reflected
parts changes only the absolute count constant. Half-open shells and the
explicit assignment of r=1 to the far set count every boundary occurrence;
using closed upper bounds can only overcount harmlessly.

Multiplication by d² makes that far payment O(1/L), exactly the ε used in
(6). Converting d to the actual gap g multiplies by 1+O(η), preserving
ε=1/L+L a^(−ct0). Thus DM=1/2+O(ε), whereas the two-neighbor mass obeys
Db_3=1/4+O(η). The sharper local error and the coarser complete-tail error
are correctly distinguished. Fixed t0>0 makes both vanish uniformly;
no limit t0↓0 is used.

## 3. Horizon constants, optimality and failure class

**Accept.** For fixed Δ>=0 the score R(d,b;Δ) is monotone in both d and b
on the admissible nonnegative lower-data rectangle. The exact pair D,M
therefore provides the largest score in this class, independently of how
its lower bounds were acquired. Eventual DM<1 makes the strict horizon
D/[2(1−DM)] finite. Substitution gives

    τ_3=(g²/6)(1+O(η)),
    τ_full=(g²/4)(1+O(ε)),
    τ_full/τ_3=3/2+O(ε).

Since g~4π/L, the physical-time leading constants are respectively
8π²/3 and 4π² after multiplying by L². There is no extra normalization
factor. Expanding the scores at fixed Δ gives limiting values −3Δ/2
and −Δ, respectively. Thus all sufficiently high eligible pairs fail
the unchanged strict score, even with exact initial M. For a family of
nonempty blocks containing only such pairs, every block is conservatively
bad; the probability-one conclusion concerns this sufficient-score event,
not actual collision events.

The algebraic lattice subsum gives
b_n=2n/[(n+1)g²] and τ_n=g²(n+1)/[4(n+2)], including n=1 and the complete
limit. The cosine heat field has stationary zeros and satisfies the
physical heat sign, so it directly checks that the finite scalar horizon
is not a dynamical lifetime. The missing positive moment terms balance
2M² in that exact field. The quadratic check retains the strict endpoint
condition. Neither example is substituted for the canonical proof.

The explicitly stated excluded class is the one-step Riccati lower
envelope based only on initial D,M. The result does not exclude repeated
anchors, divided steps, improved time-dependent interaction estimates,
or direct use of exterior simplicity. Its conclusion concerns an
allowance; no failure of canonical dynamics is inferred.

## 4. OC acquisition audit and control screen

**Accept within source-audit scope.** The bounded support check inspected
OC Proof17, source Note19, cell Note22 and the later finite-projection
Note25. The original Proof17 formulas retain fixed blur, externally
supplied initial enclosure, unassigned canonical constant A, and
L2,LC=O_A(log^5 T). Its e_M and the two derivative-truncation allowances
match Note20. Source Note19 (11)–(14) confirms the spatial, frequency,
source and joint-contraction ledger. No one of those fixed-observable
payments is silently treated as a sharp void-event payment.

OC Note22 §1 records the 388 singleton cells, rectangle
(988,2012)+i(−3/2,3/2), stated widths and minimum horizontal separation
5085/8192. The later finite P_1000 at time zero is a certified scalar with
radius 2.0584963350931e−5 in its inherited winding-certificate scope.
Note20 preserves that actual acquisition and does not claim that all
canonical statistics remain unevaluated. It correctly denies a supplied
transfer from this one fixed-time projection to the proposed positive-time
three-consecutive-gap or void law. This assessment does not replay the
underlying numerical source arithmetic or broaden its existing certificate.

The original controls and Note21's table are used at application-premise
level. Altered theta arithmetic, incomplete reflection, changed physical
readout, missing integer realization or absent common canonical dynamics
are concrete failures; shared local identities need not fail. For the
reflected super-Gaussian family, the cited source explicitly proves absence
of the required integer-square theta expansion. That failed source premise
suffices for this screen; this assessment imports no separate quantitative
zero-population theorem for that control. The finite-source no-all-real
statement is restricted to the documented endpoint-defective subclasses.
The cosine and quadratic examples check only the comparison and its scope.

## 5. Usable return and remaining work

The usable return is a canonical high-height interaction asymptotic with
complete tail payment and the exact leading horizons of the frozen
comparison. The imported positive-time exterior theorem supplies a
separate way to protect that high tail. A finite application still needs
an effective cutoff or other certified exterior coverage, a complete
compact pair-label cover including moving window boundaries, a simple
all-real start, and a source estimate strong enough for zero exceptions.
Those are not supplied by this proof or by the checked OC scalar.

No required correction remains. E21 may be recorded complete within this
scope, and B07 r2 may retain its precise source/consumer disposition.
No larger numerical campaign follows from this acceptance. E16 r2 remains
independently ready and unexecuted; a stronger joint-in-time or compact
acquisition mechanism requires a separately specified B decision.

[request]: ../research-progress/handoffs/VCD-GT-CM-E22-r1.md
[pins]: ../research-progress/handoffs/VCD-GT-CM-E22-inputs-r1.json
[note]: ../notes/21_VCD_GT_CM_E21_CANONICAL_HEIGHT_HORIZON_20261118.md
[poly]: https://arxiv.org/html/1904.12438v2
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[shared]: ../../../../../../avoid/05_same_model_reviews_and_shared_premises.md


## 6. Bounded final scope-clarification check

18 November 2026. Prepared for Edward Baker with OpenAI Codex assistance;
actual settings unavailable. This is the single correction check permitted
by E22, requested after the completed first-pass acceptance in
[clarification r1](../research-progress/handoffs/VCD-GT-CM-E22-clarification-r1.md).
The first-pass verdict above is preserved: no mathematical correction
was required. The lead nevertheless narrowed one control-screen sentence
to distinguish the proved failure of theta square arithmetic from an
unacquired canonical population/clock input, and changed the header to
route acceptance status to E22/the sole register.

**Both clarifications accepted; no required correction remains.** They
make no change to the equations, domain, proof, quantitative conclusions
or assessed failure class. Reversing exactly those two text replacements
recovers the original Note21 SHA-256
`3890ad3a86c4d4d0e75b4f5335397018eb21be472257c1670e1b81ac7e3197cf`.
The other five original pinned inputs remain byte-identical. The final
[one-file manifest](../research-progress/handoffs/VCD-GT-CM-E22-clarification-inputs-r1.json)
was checked: Note21 is 15,017 bytes, SHA-256
`5248285405a8441d0ba06c58e2c899d02c139f88b55b6fca7156d00e98e4256a`.
This is the final assessed Note21 binding; the original manifest and
first-pass checks remain historical evidence. No new research or review
of later integration prose was performed in this check.
