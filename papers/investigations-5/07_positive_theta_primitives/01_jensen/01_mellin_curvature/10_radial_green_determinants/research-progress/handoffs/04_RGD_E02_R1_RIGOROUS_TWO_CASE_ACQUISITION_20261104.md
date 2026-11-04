# RGD-E02 r1 — rigorous two-case acquisition request

4 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance; actual **gpt-6.1-sol (Codex), effort ultra**,
chat0003, turn `01a1a789-4831-75e3-ac1d-91bbab495d0d`.
Issued under the author's explicit request to continue RGD-E02. Frozen
before the first certificate acquisition. The [sole register][progress]
owns live status; [Continuation03][prior] supplies the accepted prerequisites.

**Type E — execution; recommended Sol.** The source, comparison, finite
cases and error theorem are fixed. Interval integration and outward
polynomial evaluation implement the existing route. No changed mechanism,
index range or tail payment is authorized.

## Question and acceptance

At exactly k=1,4, rigorously certify a strictly positive lower bound for
Note01 (19), L_(k,2)=P_k(1/16,x^[2])-R_k(x^[2],E+B(2)), and consequently
for canonical Q3,k=D4,k*D2,k. Keep moments 0,...,7, exact b=1/16, U=2,
all n>=2 and u>2 payments. Do not acquire any additional index or source.
The reference's small positive atom and lack of a proved PF property
remain as in Note01. The existing PF44 baseline makes this a method and
quantitative-bound test, not a new finite-order positivity range.

Success requires finite rigorous input balls and **strictly positive
final lower endpoints after every error payment** for both cases.
A tolerance request, floating agreement or saved status string cannot
accept a case. Preserve any successful case if the other is unresolved.
A nonpositive computed lower endpoint means this acquisition did not
certify the claim; it does not establish a negative exact determinant.

## Fixed acquisition and proof chain

1. Reuse the exact sparse polynomial/binomial construction of E03,
   preserving its already-collected neighboring-product cancellation.
   Regenerate its formal D4*D2 permutation checks, k=1 eight terms and
   factorization, k=4 b-independence, and Taylor monomial counts/hashes.
   The frozen E03 artifact is read-only; use a new E02 script.
2. For each j=0,...,7, integrate the entire function
   f_j(z)=z^(2j)*exp(z-pi*exp(4z))/(8*(2j)!) on the five exact rational
   intervals with endpoints [0,1/8,1/4,1/2,1,2], using python-flint
   acb.integral. Integer powers and nested exponentials are entire;
   the analytic flag therefore needs no branch-cut handling. Use a
   certified Arb pi ball and complex ball operations. Sum segment
   enclosures outward, require finiteness and imaginary balls containing
   zero, and retain real balls X_j containing the exact compact moments.
3. Compute Note01 (6) E_j and (18) B_j(2) in Arb, retaining nonzero B
   separately. Add E+B outward. All real bases/denominators must be
   certified positive. No tiny tail may be set to zero.
4. Evaluate P and each collected Taylor coefficient polynomial on X.
   Put q^- = lower(P(X)), A_alpha = abs_upper(t_alpha(X)), and
   T_j=upper(E_j+B_j). Sum A_alpha*T^alpha in Arb and take an outward
   upper endpoint U_k. Then
   Q3,k >= L_(k,2) >= ell_k := q^- - U_k.
   Every acquisition occurrence uses X, so its uncertainty is already
   propagated into both q and the Taylor coefficients; do not add an
   estimated quadrature error in place of an enclosure. Preserve all
   nonzero terms in degrees 1,...,6.
5. Serialize exact dyadic midpoint/radius pairs for moments, segment
   integrals, constants, E, B, E+B and output bounds. Decimal displays
   are only reading aids. Provide a standard-library record verifier
   that checks code/input hashes and serialized positive endpoints,
   and independently recomputes polynomial intervals and a residual
   upper bound using Fraction arithmetic. It may round positive tail
   upper bounds **upward** to an absolute grid 2^-384 to bound integer
   sizes; this explicitly pays B even if it is much smaller than the grid.
   The verifier still trusts the identified Arb acquisition and its
   analytical error theorem; it is not a formal proof of FLINT.

The imported library contract is the [python-flint integration API][acb]
and [Arb interval and endpoint API][arb]. The callback's entire-function
proof and positivity of the required denominators must be written in the
return. Integration tolerances are accuracy goals, not certificates of
attaining those goals; acceptance is by final enclosures.

## Finite arithmetic and resource contract

- Initial precision **384 bits**; relative and absolute integration
  goals **2^-320** for each segment, using exact powers of two.
- One conditional **512-bit** pass with goals **2^-448**, only if a
  returned enclosure is nonfinite, or the final lower endpoint is
  nonpositive and acquisition/rounding uncertainty leaves success
  unresolved. No additional precision pass after a success.
- Per integration call: deg_limit=128, depth_limit=20,
  eval_limit=5000, use_heap=True. The partition stays fixed; FLINT's
  bounded internal adaptivity is permitted.
- Across assembly, all passes and exact record propagation: **180
  seconds and 200,000 total callback evaluations**. Instrument both;
  retain partial completed inputs/cases. Stop on the first cap. There
  are at most 80 segment calls (40 per precision pass). No wider scan,
  different quadrature route, altered cutoff or new theta acquisition.
- Record verification without integration may be run once for a saved
  certificate; its cost is recorded separately. No extra acquisition
  replay is required. Ordinary pre-run implementation review is allowed.
  An implementation defect after starting is retained as a failed step;
  a changed method requires an explicit revised request before a new run.

## Outputs, review and routing

Write numerics/rgd_e02_two_case_certificate.py and one small certificate
JSON, notes/03_RGD_E02_R1_RIGOROUS_TWO_CASE_BOUND_RETURN_20261104.md,
and an identified same-assistant self-assessment in reviews/. Record
actual model/effort, all hashes, library versions, attempts, precision,
callback counts, timings, finite/failed cases and exact rational witnesses.
Update only local progress/navigation, continuation guidance and this
chat's unique history. Do not modify inherited returns, original packets,
parent/sibling registers or source files. Follow LARGE_FILES.md.

If successful, recommend **[E] RGD-E04 r2 — Sol** for separate internal
assessment of this fixed certificate and its consequence; do not execute
that new assessment merely because the certificate succeeded. B03 stays
gated: a two-case certificate supplies no order dependence. If failed or
capped, return the named uncertainty to **B02 — Astra** only when a
mathematical repair is required; preserve the finite failure's scope.
No global result-summary update or manuscript milestone is part of this
acquisition. Read the [result index][results] and [avoid index][avoid],
especially [controls][controls], [joint payments][joint],
[bounded numerics][numerics] and [precision evidence][precision].

## Locked prerequisite versions

SHA-256 identifies inputs, not mathematical validity. Working-tree
versions are intentional; no clean commit is implied.

| Input | SHA-256 |
| --- | --- |
| notes/01_BOUNDARY_PRESERVING_FIRST_MODE_COMPARISON_20261104.md | `556a97aa60f7a3448acbd00cf8bfa4c3e2916e428f67d03dbb97889077bc9847` |
| reviews/01_RGD_E04_R1_BOUNDARY_PRESERVING_COMPARISON_ASSESSMENT_20261104.md | `9000b4c9ba0c62f2d82ecb4a2758dcb0b478d6e84ae580e17f93735faf5ad237` |
| notes/02_RGD_E03_R1_TWO_CASE_FIRST_MODE_DIAGNOSTIC_RETURN_20261104.md | `2673a7f8599776bcbc1990af21448ccd3c9b80dccf4b94ff6556aa5fdd5878b3` |
| numerics/rgd_e03_firstmode_diagnostic.py | `a42db929d82eeeac3aef36b36290e003946c06e1505d81b76c119846576c1f09` |
| numerics/RGD_E03_R1_FIRSTMODE_DIAGNOSTIC_20261104.json | `932fa5164630bbf98c124e3d89d9f3c7501bfcef82d54d28245a72bc91f293b1` |

[progress]: ../01_RADIAL_GREEN_DETERMINANTS_RESEARCH_PROGRESS_20261104.md
[prior]: 03_RGD_CONTINUATION_AFTER_FAVORABLE_E03_AND_MODEL_CHANGE_20261104.md
[acb]: https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.integral
[arb]: https://python-flint.readthedocs.io/en/latest/arb.html
[results]: ../../../../../../../../result-summaries/README.md
[avoid]: ../../../../../../../../avoid/README.md
[controls]: ../../../../../../../../result-summaries/12_collision_controls_and_screening.md
[joint]: ../../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[numerics]: ../../../../../../../../avoid/10_numerics_ahead_of_the_question.md
[precision]: ../../../../../../../../avoid/04_counts_and_precision_as_evidence.md
