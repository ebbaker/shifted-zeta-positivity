# A ready prompt for the next session

**Prepared by Claude Opus 5 (Anthropic), model `claude-opus-5`, 18 September
2026**, at the end of the fifth session of this investigation --- the one that
wrote the manuscript. Paste the block below into a fresh chat with the repository
folder connected. **It does not open a new front. The investigation's question is
answered, the manuscript is written and reviewed at working draft 0.1, and what
remains is a short list of small items plus whatever a reader of the draft asks
for.**

---

```
Continue the fractional-dimension investigation in the shifted-zeta-positivity
repo: papers/susy-positivity/investigations/fractional-dimension. It was opened
18 September 2026 from the closed Loewner investigation, whose manuscript "The
Markov part of the shifted Weil transfer" (working draft 0.3) is the
consolidated report of everything inherited. There is no manuscript here yet;
five dated notes and six check programmes are the whole record.

READ THIS FIRST. The investigation's own question -- is d a dimension, or a
parameter? -- is ANSWERED, and the answer is: a parameter. The manuscript is
written: "A scattering matrix without a space", working draft 0.1, 21 pages,
reviewed, recorded and snapshotted at drafts/2026-09-18-v01, with all six check
programmes registered in validation/drafts.py and replayed with it at 1522 cases.
So do not open a new front. Read the manuscript before anything else; if I have
given you comments on it, they take priority over everything below. Otherwise
take the small open items in the order given, and change the manuscript only in
the ways the BUILD.md workflow allows -- rebuild, re-review, re-record, and save a
new snapshot rather than editing an old one.

Read first, in this order, and don't re-derive the framing from them:
  manuscript.pdf                                 - the consolidated report, 21
                                                   pages. Section 1.2 is the whole
                                                   argument in five paragraphs;
                                                   Section 8 is what is settled,
                                                   what is open, and the status of
                                                   every statement
  BUILD.md                                       - how to rebuild, re-record and
                                                   snapshot it, and what the two
                                                   provenance artefacts refuse
  notes/README.md                                - the map, the reading order,
                                                   and the xi/Lambda warning
  notes/THE_TRADE_IS_NOT_IT_20260918.md          - the last note, whose Section 5
                                                   is where this task list came
                                                   from
  notes/PAST_THE_WALL_20260918.md                - Section 0: the wall, the
                                                   two-Blaschke decomposition,
                                                   and why the criterion is
                                                   vacuous past omega = 1/2
  notes/THE_RANK_AND_THE_LATTICE_20260918.md     - sections 1 and 3: the
                                                   primitive-Epstein scattering
                                                   matrix and the point count
  notes/WHICH_DIMENSION_AND_THE_VOLUME_20260918.md - why the dimension is 2*omega
  notes/OPENING_NOTE_20260918.md                 - the dictionary
  ../loewner/manuscript.pdf, sections 2 and 3    - the dichotomy (2.3) and the
                                                   decomposition

WHERE THINGS STAND, in one paragraph. With d = 2*omega, m = d+1, a = 1/2 - omega,
b = 1/2 + omega, c = -a, the transfer is K_om = R_om Ktilde_om with
Ktilde_om = Lambda(p+a)/Lambda(p+b) completely monotone on (b, infinity) at every
omega > 0, and R_om = (p+a)(p-b)/((p+b)(p-a)) = B_b . (p+a)/(p-a). At integer d,
Ktilde_om is the primitive-Epstein scattering matrix of the unimodular lattices of
rank d+1, and p -> -p is its functional equation. EVERYTHING TURNS ON THE SIGN OF
a = (2-m)/2. At a = 0, i.e. m = 2, three things happen at once: the second pole of
Ktilde_om -- which is the ARCHIMEDEAN factor's, the Gamma pole at p+a = 0, while
p = b is the comb's -- crosses into the right half-plane; (p+a)/(p-a) stops being
completely monotone and becomes a Blaschke factor B_c, so R_om becomes inner; and
the poles of K_om leave the closed right half-plane, which by the parent's
dichotomy makes every V_{om,L} a contraction UNCONDITIONALLY, by the Euler product
alone for omega > 1/2. So the criterion is VACUOUS on [1/2, infinity) and has
arithmetic content on exactly (0, 1/2), i.e. m in (1,2): the Euler product is its
value at rank two and RH is its DERIVATIVE at rank one, where Ktilde = 1, V = I and
the first-order law gives the Weil form. Complete monotonicity of Khat_om survives
everywhere, by two groupings of the Gamma factors that are exchanged at the wall.
The interpolated lattice point count fails on (1,2) AND on (2,3), by Lagrange's
theorem read through the binomial series: on the gap (k,k+1),
sign binom(m,j) = (-1)^max(0,j-k-1), so r_m(n) > 0 for free when n <= k+1 and the
first FORCED negative coefficient sits at N_k, the least integer needing k+2
POSITIVE squares -- 2, 3, 7, and none at all for k >= 3 because s(n) <= 4 always.
The transfer, by contrast, has exactly ONE positivity threshold in m and it is at
m = 2. So the two positivity statements are NOT one statement; the coincidence of
intervals on (1,2) is the first gap and nothing more. What explains the split is
where the rank sits: in the transfer it is an EXPONENT -- (2 sinh tau)^(om-1),
(1-e^-t)^(beta-alpha-1), p^-d -- where positivity is a local inequality at one tau
or one prime that continuation cannot break; in the point count it is a BINOMIAL
INDEX, where it can. The transfer's positivity was never inherited from a lattice,
so the lattice's failure leaves no trace in it.

THE TASK.

0. READ THE MANUSCRIPT before anything else, and act on my comments if I have
   given any. A revision goes through the BUILD.md workflow in full: rebuild,
   actually look at the rendered pages, record with an honest --review-note saying
   which pages were read and how, save a NEW snapshot, and run
   `python3 validation/drafts.py check --replay`. Never edit a saved snapshot and
   never bump the version without re-reviewing.

1. THE COMPLEX-HYPERBOLIC LINE. (alpha, beta) = (omega-1, 0) with rho = omega is a
   Heckman-Opdam parameter, where a transform theory exists at arbitrary
   multiplicity. Proposition 4.1 of the fifth note now explains why the archimedean
   half continues at all -- its positivity is a Beta density with omega in the
   exponent, and an exponent of a positive quantity is positive at every real
   value. So the concrete question is whether Heckman-Opdam supplies anything
   beyond a name for that: a transform, an inversion, a Plancherel measure that the
   Beta density does not already give. The honest prior is that it supplies a name;
   say so plainly if that is what you find, and close the item.

2. CONVENTION HYGIENE. The first three notes here write xi for what the parent
   manuscript calls Lambda (Lambda has the poles at 0 and 1; xi = (1/2) u (u-1)
   Lambda is entire). The two differ by exactly R_om. The manuscript uses the
   parent's convention and warns about the clash in its Remark 2.1; the notes have
   not been converted. Convert them, update the notes index's warning, and then
   decide whether Remark 2.1 can be reduced to a sentence -- which is a manuscript
   edit and goes through the full BUILD.md workflow.

3. TWO CLEAN CONJECTURES ABOUT SUMS OF SQUARES, recorded and NOT to be chased
   here: that r_m(n) >= 0 for every n and every real m >= 4; and that the negative
   coefficients on (3,4) come from competition between terms rather than from
   forcing. Neither is about zeta. If you find yourself working on them, stop --
   they belong to whoever wants them, not to this investigation.

DO NOT run the contraction criterion at omega >= 1/2 expecting information: it is
vacuous there (fourth note, Proposition 3), contraction follows from the Euler
product, and a computed margin is not evidence for or against anything. Do not
look for a factorization of the transfer that exhibits the point count's failure:
there is none, and the fifth note says why (no factor of the transfer carries the
rank as a binomial index). Do not pursue Bost-Connes at fractional d. Do not
re-open the Loewner proposal -- three independent obstructions, all in the parent
manuscript. Do not look for a conformal realization of the archimedean Beta law;
the quantization argument excludes it. Do not try to make CH^omega a space: it is
one only at integer omega, which the family's range never reaches.

TRAPS, each of which cost time in the sessions of 17-18 September:
  - xi MEANS TWO DIFFERENT THINGS in this repository. Parent manuscript:
    Lambda(u) = pi^(-u/2) Gamma(u/2) zeta(u) has simple poles at 0 and 1 with
    residues -1 and +1, and xi(u) = (1/2) u (u-1) Lambda(u) is entire. The first
    three notes here write xi for the parent's Lambda. They differ by exactly
    R_om. Check which convention a formula is in before using it.
  - R_j(n) IN THE FIFTH NOTE COUNTS ORDERED TUPLES OF POSITIVE SQUARES, not the
    classical r_j(n) over all integers with signs and zeros allowed. The sign law
    and everything built on it use the positive-square version; substituting the
    classical one gives a different polynomial and the argument collapses.
  - THE THEOREM IS ABOUT FORCED negativity -- coefficients at which no positive
    term is present at all. Negativity elsewhere (on (3,4), say) is competition
    between terms of both signs and is NOT covered. Do not extend the statement
    past what forcing gives.
  - CONTRACTION AT omega >= 1/2 IS NOT EVIDENCE. The poles of K_om sit at
    Re p <= 1 - b = a, which is negative as soon as omega > 1/2, by the trivial
    strip alone (at omega = 1/2 exactly, a = 0 and the classical zero-free region
    is what puts them strictly inside). Any margin computed there is a property of
    the Euler product.
  - lambda_min(D_N) OVERSTATES the margin. For f in E_N,
    <f, D_N f> = ||f||^2 - ||P_N V f||^2 >= ||f||^2 - ||V f||^2, so
    lambda_min(D_N) >= lambda_min(D_{om,L}): a positive computed value does NOT
    certify contraction. Every recorded margin in this program is a trial-space
    Rayleigh quotient. State, every time, which direction a value certifies.
  - THE ASSEMBLY DOES NOT USE THE BLASCHKE FACTORIZATION. It uses the partial
    fractions R_om = 1 - 4 om b/(p+b) - 4 om a/(p-a), which are the same algebra at
    every omega. If you think the assembly needs changing because a factorization
    changed, check first whether it ever saw the factorization.
  - gauss_jacobi_unit writes the k = 0 Jacobi recurrence coefficient as
    (be^2 - al^2)/(d (d+2)) with d = al + be, which is 0/0 at omega = 1 EXACTLY.
    Its removable value is (be - al)/(al + be + 2). Patched in
    numerics/check_two_blaschke.py; the parent programme still raises there.
  - tau = log|t+i| is a BUSEMANN function, not a distance. The hyperbolic
    distance is 2 arcsinh(t/2) and tau ~ r^2/2 is a square. Reading
    (sinh tau)^(omega-1) as a hyperbolic radial Jacobian gives dimension omega
    and is wrong; the dimension is 2*omega. The two normalized limits differ by
    exactly 2^(1-omega).
  - |S^d| is the unit sphere of R^(d+1), not of R^d. A helper that returns
    |S^(m-1)| for input m needs sphere(d+1). This produced wrong residues once.
  - The completed Epstein integral
    Lambda_m(s) = 1/(s-m/2) - 1/s + int_1^inf (theta_m(x)-1)(x^(s-1)+x^(m/2-s-1))dx
    is symmetric in s <-> m/2 - s BY CONSTRUCTION. Checking the functional
    equation with it is tautological. Test it against direct lattice summation
    with the exact continuum tail, and test Poisson summation on its own.
  - A residue in p is TWICE a residue in s, because dp = 2 ds. That the two
    residues nevertheless agree is a cancellation against E*(0) = 2, not a free
    identity.
  - The archimedean kernel k^Gamma_omega(tau) dtau is the pushforward of
    |t+i|^(-b) dt, not of Lebesgue measure. Dropping the weight gives a relative
    error near 400.
  - u^(2 omega - 1) has an unresolved endpoint singularity at small omega.
    Substitute u = v^(1/2 omega) on [0,1]; crude quadrature is off by 12% at
    omega = 0.1 and looks like a real discrepancy.
  - The inherited assembly's true defect is below double precision at the larger
    horizons (2.6e-19 at L = log 5, 2.1e-24 at log 7), and lambda_min(D_N) there
    comes out of either sign at the 1e-14 level. Assert | ||V|| - 1 | < 1e-12 and
    state the floor; do not assert ||V|| < 1 and do not read the sign.

STANDARDS. Classify every statement as a written proof, a proof sketch, a
labelled numerical computation, an observation, or a reading, and label anything
conditional on RH. Check the algebra independently rather than inheriting it.
Prefer a sharp negative result to a vague positive one. If the direction looks
wrong to you, say so plainly -- the last five sessions each ended by contradicting
or strengthening the handoff that set them up, and that was the useful part. The
fourth note's content was that the third's head item had a premise that does not
hold; the fifth note's was that the fourth's head item has the answer "no".

ZETA HYGIENE. This investigation evaluates zeta at REAL arguments only, by
convergent series or a convergent theta integral. The real segment of the
critical strip is unavoidable once you are computing a scattering matrix, and
that is fine; computing values off the real axis, or locating zeros, is not.
Say in each programme's docstring exactly where zeta is evaluated.

CONVENTIONS. Research notes in notes/, reviews in reviews/, with the Claude
model named at the top of anything you write. Check programmes are standard
library only, print JSON to stdout, and keep a preserved record under
numerics/records/, and are registered in the CHECKS dictionary of
validation/drafts.py, which replays them with the manuscript and requires
byte-identical output. A new programme must be added to CHECKS in the same pass. Anything needing mpmath
goes in numerics/exploratory/ and is labelled unregistered. Verify each
programme is deterministic across repeated runs and that its record matches a
fresh run. Everything under 1 MiB per the repo's LARGE_FILES policy. Update
notes/README.md, numerics/README.md, the investigation README, the program
README row and CHANGELOG.md in the same pass. Bare | inside $...$ breaks a
markdown table row; use \lvert ... \rvert. If a git command leaves a stale
.git/index.lock, tell me.

Write results to notes first, and fold them into the manuscript only once they
have settled. End the session with a continuation note in notes/ and an updated
version of this prompt.
```

---

## Notes on the prompt itself

**What changed in this revision.** The manuscript exists, so the prompt's first
instruction is to read it rather than to ask whether to write it, and the task
list now begins with the revision workflow. The manuscript is
*A scattering matrix without a space*, working draft 0.1, 21 pages: the dictionary
and the rank identification; the primitive-Epstein scattering matrix at every
integer rank; the rank-two wall as the sign of $a$, with the three things that
change there at once; the two-Blaschke decomposition and complete monotonicity at
every $\omega>0$ by two exchanged groupings of the Gamma factors; the vacuity of
the criterion past the wall; the point count's failure with Lagrange as the
threshold; and the exponent-versus-binomial-index reading as the closing section.
It is a paper about why a criterion has content on exactly one interval and why
that interval is not evidence of anything. Every proposition is proved in place,
the inherited ones are listed in its Section 2.3, and Section 8.3 classifies every
statement in it.

**What a next session should watch.** The manuscript's own weak points, in the
drafter's judgement: Remark 2.1 exists only because the notes have not been
converted (task 2), and should shrink when they are; Section 5.3's calibration
table is the one place where numbers appear at all, and Remark 5.5 is what keeps
them honest --- if a reader finds that table doing rhetorical work it should be
cut rather than defended; and Section 7.3 is the paper's one piece of
interpretation, so it is the section most likely to need rewriting after a human
read.

**Left out deliberately.** The two sums-of-squares conjectures are in the task list
only as instructions not to chase them. The group-theoretic reading of the third
note's Corollary 1.3 (degenerate Eisenstein series, $c$-function, unipotent
radical) stays out: it is the standard interpretation of verified formulas and
confirming it against the literature is worth an hour but is not a result.

## State of the repository at handoff

- Investigation: `papers/susy-positivity/investigations/fractional-dimension/`,
  opened 18 September 2026. Manuscript *A scattering matrix without a space*,
  working draft 0.1, 21 pages, reviewed and recorded 18 September 2026, snapshot
  `drafts/2026-09-18-v01`.
- Five dated notes, one handoff prompt, six check programmes, **1522 cases**, all
  passing, all deterministic, all matching their preserved records, all registered
  and replayed by `validation/drafts.py check --replay`.
- Parent (`loewner/`) is closed and untouched; its registered replay passes at 96
  cases across 4 snapshots, and its `check_contraction_margin.py` still runs at 53
  cases. The extended copy lives here as `check_two_blaschke.py`.
- Last commit: `eb0007b`, "Pausing on Loewner investigation due to an obstacle,
  starting a new investigation called fractional-dimension". Everything after it
  --- the second through fifth notes, five check programmes and their records, the
  manuscript and its whole package, the handoff prompt, and the index and CHANGELOG
  updates --- is uncommitted. Two
  zero-byte `.git/index.lock*` files are stale leftovers from `git status` run
  without delete permission; delete them before the next `git add`.

See the [notes index](README.md) and the [investigation index](../README.md).
