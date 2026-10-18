# Opening round assessment of packet matching and finite prime controls

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Reviewer **gpt-6-astra (Codex)**, reasoning effort **max**,
verified from the current turn metadata.

**Review type: self-review by the same assistant that wrote the notes and
checker.** This is not independent LLM review or specialist validation.
Disposition: the stated formulas and class obstruction have written proofs
and passed the bounded checks described here. Theta positivity and the
complete modular estimate remain open. An external mathematical review is
appropriate before manuscript integration or stronger validation language.

## Reviewed sources and exact versions

| Source | SHA-256 |
| --- | --- |
| [Note 02][n02] | ec903feaf280bc264896cfc26a677c8d0e3be651ba6e7fe86edb4214742eb46d |
| [Note 03][n03] | 95d4487a1836e1902755bba5ee743ecfb6ac84cd4dc3f4cfb519805281636ce3 |
| [Checker][code] | 1025065955eb52da0454248fca6f307f2ad8d4e73b23895692761763449e2dd2 |
| [Execution record][record] | ea9c7c9e29cff4c5d20e6b17ef5361c6af92ad72b8523d221e57e9e848618c60 |

The discussion in Note 01 is background, not a new result accepted through
this review. The [result-summary index][summaries], [control summary][s12]
and [avoid index][avoid] supply the scope rules; in particular [same-model
review limitations][a05] and [scoped exclusions][a07].

## Packet calculation and its limits

The source change of variables gives the prefactor and complete lower
interval in Note 02 (1). Differentiating the prefactor yields the shifted
operator (partial_w-i a_d)^j. Reflection yields (-1)^j in (3), so the
first derivative changes sign. The two-prime block retains the d=6 term.
The direct source expressions justify differentiation and convergence;
no infinite unpaired Möbius series is used.

The local remainder is a direct Taylor bound: time error uses g_tt=g_xxxx,
and the spatial errors use third derivatives. The displayed 1/|c| cost
survives normalization. The calculation expands the complete packet in its
base point while retaining its exterior observations. It does not insert
a bounded-domain collision polynomial at a fixed imaginary displacement.

The exterior Wronskian estimate is a necessary consequence of existing
source-tail bounds. It is not a new sign theorem. The attempted curvature
estimate retains the full starting H, but gives only epsilon_2 |H| error.
At a stationary double-event predecessor that is of order sqrt(E), not E.
No energy-scale conclusion was taken from this estimate.

## Audit of the control theorem

The following points carry the proof and its scope:

1. **Exact arithmetic compatibility.** Distinct rough parts give disjoint
   coefficient supports. A coefficient constant on each complete selected
   prime orbit obeys v_(pn)=v_n for every n and every selected p. Thus all
   selected-prime divisible-source identities, not just a finite prefix,
   survive the perturbation.
2. **Exact measurements.** A finite orbit span with dimension exceeding
   the number of real linear conditions has a nonzero kernel. The primitive
   normalization is included as an additional condition. Rough seeds above
   N keep the first N coefficients, including a_1, fixed.
3. **Finite odd endpoint defect.** Bounded coefficients justify real
   analyticity and termwise source differentiation. If every odd derivative
   vanished, the whole source would be even. Together with the zero
   primitive endpoint, the signed version of the imported reflection
   rigidity theorem, with v_0=0, forces v=0. This use of primitive
   normalization is indispensable.
4. **Endpoint expansion.** The first nonzero odd source derivative survives
   multiplication by the even heat weight. Separate integrations for V,
   V',V'' establish the three asymptotics; differentiating an unspecified
   big-O term is not required. The logarithmic curvature is eventually
   positive.
5. **Theta input.** Polymath Theorem 1.5 and its section 9 argument-principle
   proof give eventual real simple zeros at each fixed positive time in
   (0,1/2]. The global strip makes the remaining nonreal zeros finite.
   The order-one product makes each conjugate pair's logarithmic curvature
   negative sufficiently far to the right. For larger time, the known
   upper bound and Hermite splitting supply the required real simple zeros.
   No RH assumption is made.
6. **Frozen event.** The ratio has one nondegenerate critical point in
   each sufficiently high gap. Delta is chosen there and then held fixed
   under time and spatial differentiation. The event is a genuine double
   zero with nonzero second derivative, not a time-dependent fitted source.
7. **Topology.** The coefficient sup norm and the explicitly defined
   weighted source norm tend to zero. The Fourier derivative error is
   uniform in real height and a fixed complex strip. The constructed
   collision heights move to infinity; there is no claim of instability
   at a fixed prescribed point or inside every compact box.

The source is positive on the half-line and the cosine transform is even
in spectral position. The analytic arithmetic source is not even in its
source coordinate. Its reflected extension has only the finite smoothness
actually imposed. This distinction is the failed full-reflection premise,
not a technicality that can be removed from the theorem statement.

The high-gap argument is imported from the existing one-direction result;
the new work extends its admissible directions to complete prime orbits
and proves that the endpoint mechanism survives the finite exact constraints.
No priority claim is made. No finite Newman threshold for a control is used.

## Numerical evidence and boundaries

The retained run used Python 3.12.14, python-flint 0.9.0, and 384-bit ball
arithmetic. The execution record is authoritative for runtime metadata.
It covers t=1/4, z=30+i/3, d=2,3,6, and derivative orders 0,1,2, with
eight original source modes, upper integration endpoint 1.5, and analytic
source-index and integration tails. Numerical identity differences are
enclosed around zero and below 1e-83 in magnitude. The deliberately wrong
reflected derivative sign is rejected for j=1 at each d.

For the complete rough orbits 5,7,11, infinite endpoint sums are enclosed by
the first term plus a rigorous all-integer tail from 2r onward. The matrix
defining the two exact constraints is invertible; the two smaller coefficient
magnitudes are below one; the third odd source derivative is strictly
negative. Exact cancellation of the primitive and first source endpoints
comes from the definitions using the full sums. The decimal values are not
substituted for those definitions.

These checks certify endpoint signs for one direction and diagnose the
finite packet implementation. They do not numerically certify any collision
location, prove the general theorem by sampling, or supply a theta sign.

## Consequence for the investigation

The bounded opening round has met its setup and scoped-obstruction goals.
It has not met the positive arithmetic-estimate goal. The result rules out
deriving all-height collision exclusion for the stated relaxed class from
selected-prime compatibility, finitely many exact linear observations, and
a positive absolute tail tolerance. It does not rule out full reflection,
nonlinear or infinite data, controlled infinite assembly, or a finite
formula using the complete theta source with stronger hypotheses.

The next mathematical consumer should be the particular exterior jet
(A_P,A'_P,A''_P) of Note 02. A continuation should couple it to the complete
normalized modular relation, or identify another premise the new controls
actually fail, and attempt an independent bound on that coupled expression.
Simply adding finitely many prime or endpoint tests does not remove the
proved obstruction for an unbounded-height relaxation. A compact-region
estimate could still be useful and would retain its stated scope.

[n02]: ../notes/02_COMPLETE_PACKET_MATCHING_CODEX_20261018.md
[n03]: ../notes/03_FINITE_PRIME_COMPATIBLE_COLLISION_CONTROLS_CODEX_20261018.md
[code]: ../numerics/check_packets_and_orbits.py
[record]: ../numerics/PACKET_AND_ORBIT_CHECKS_20261018.json
[summaries]: ../../../../result-summaries/README.md
[s12]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a05]: ../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
