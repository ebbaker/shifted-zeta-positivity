# Review of the 17–18 October assessment, and whether the direction is the right one

18 October 2026, America/New_York. Prepared for Edward Baker with LLM
assistance. Model: Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork,
reasoning effort max; the session is configured as `claude-opus-5-5` and the
serving model may differ from the configured identifier. This is a
cross-model review of the three Codex documents in this folder, the
[progress assessment](01_PROGRESS_ASSESSMENT_CODEX_20261017.md), the
[research directions](02_RESEARCH_DIRECTIONS_CODEX_20261017.md) and the
[merger and octonionic note](03_PROJECT_MERGER_AND_OCTONIONIC_METHODS_CODEX_20261018.md),
together with the [conductor-rate deduction](notes/01_CONDUCTOR_RATE_FROM_UNIFORM_FLOOR_CODEX_20261017.md),
read against the sources they rest on (Section 8 lists what was read in
full and what was not), the [result summaries](../../../result-summaries/README.md)
and the [patterns to avoid](../../../avoid/README.md). Edward asked whether
the overall research direction seems optimal; Section 2 answers that, and
the rest justifies the answer and proposes changes. Nothing here is a new
result. The one computation is a standard-library planning script,
[`numerics/planning_arithmetic_claude_20261018.py`](numerics/planning_arithmetic_claude_20261018.py),
with its [record](numerics/PLANNING_ARITHMETIC_CLAUDE_20261018.json); its
numbers are floating point and are labelled as planning arithmetic wherever
they appear.

Each statement below carries one of four labels. *Verified*: I rederived
it or recomputed it. *Checked in outline*: I read the argument and found
its structure and the steps I tested sound, without a line-by-line audit.
*Planning*: an arithmetic consequence of the repository's own statements
under a stated assumption. *Opinion*: a research judgment.

## 0. Summary

1. **The assessment's main recommendation is right, and I would sharpen
   it.** The combined 01+03 program has produced what is, in my judgment,
   the clearest theorem with a number in this repository's history:
   unconditional, quantitative, not RH-equivalent, provable with classical
   tools, and apparently new. For
   every primitive Dirichlet character of conductor \(q\ge10^{12}\),
   \(\Lambda_\chi\le T(q)\) with \(T(10^{12})\approx0.2131\) and
   \(T(q)=O(\log\log q/\log q)\). It should be the portfolio's single
   headline, and the next three weeks should go to making it reviewable,
   not to extending it (Section 4).
2. **Is the direction optimal?** For the objective "a correct, publishable
   theorem from this program within a month", yes, with the reordering in
   Section 4. For the objective "progress toward RH", no direction in the
   portfolio claims that, and that is the correct state of affairs: the
   theorem exists precisely because the program stepped down from
   RH-equivalent targets to a milestone judged by its number, which is the
   rule [avoid 01](../../../avoid/01_restating_the_target.md) asks for.
   The direction has a known ceiling (Section 2.3), and the plan should
   say when to leave it.
3. **What I checked.** The restart lemma of
   [03 Note 02](../03_effective_outer_remainders/notes/round-2/02_RESTARTED_STRIP_COMPARISON_CODEX_20261017.md)
   is checked in outline and I found no gap: the Burgers inequality, the
   two majorants \(|u_x|\le S/2\), \(|S_{xx}|\le S/2\), the Riccati floor
   \(m_C\), the paired-kernel inequality with its own-pair correction and
   the sine-lattice floor all rederive (Section 3.2). The
   [conductor-rate deduction](notes/01_CONDUCTOR_RATE_FROM_UNIFORM_FLOOR_CODEX_20261017.md)
   is verified as a deduction from
   [03 Note 01](../03_effective_outer_remainders/notes/round-2/01_UNIFORM_FAMILY_FLOOR_CODEX_20261017.md)
   and Note 02: every number in it reproduces (record G). The uniform
   floor of Note 01 is checked in outline, and its two certified leakage
   figures agree with an independent back-of-envelope (Section 3.1). I did
   **not** audit Proposition 4.5 of the round-one transport note line by
   line, and no Claude session has; that audit is the gating item
   (Section 5).
4. **What I would change in the directions memo.** Drop the
   correlated-Gaussian pilot and the oscillator-coordinate reserve as
   research lanes: the remainder \(E\) they would improve moves \(T(q)\)
   by under one percent (record B). Take instead the two cheap levers that
   are not in the memo: the comparison height, which at \(p=\sqrt5\) gives
   about \(0.197\) instead of \(0.213\) at \(10^{12}\) even if the
   remainder doubled (record C), and the conductor threshold, which the
   mechanism supports from \(q\) of a few hundred; the certificate stops
   at \(10^{12}\) because that is where the envelope was certified, not
   because the mechanism fails below it (record F).
   Treat the faster rate of direction 5 as a remark with the crossover
   arithmetic, not a gate: the mechanism it asks for already exists in the
   transport lemma, and an \(O(1/\log q)\) bound would overtake \(T(q)\)
   only beyond \(q\approx10^{22}\) under an optimistic constant (record E,
   Section 3.4).
5. **The exposure of Project 02.** Its target \(0.1745354\) is a bounded,
   worthwhile completion, but its value depends on two things outside the
   repository: the audited status of Gomila's barrier package, which the
   manuscript's conditional corollary inherits, and the fate of the 7/8 half-plane
   preprint, under which Hakimoglu-Brown's conditional \(0.13963\) would
   become unconditional and supersede it. Finish it as planned, with the
   dependency ledger in the theorem statement, and do not plan further
   zeta constant work after it (Section 2.4).
6. **Process.** The decisive chain was written and audited by one model
   family within twenty-four hours
   ([avoid 05](../../../avoid/05_same_model_reviews_and_shared_premises.md)),
   and the merger note spends 650 lines on pilots worth under one percent
   ([avoid 20](../../../avoid/20_volume_without_a_gain.md)). Neither
   affects the mathematics; both affect how soon it can be trusted.

## 1. What the direction has achieved, and a correction to my setup review

**The mechanism** (checked in outline). In Hakimoglu-Brown's October 2026
draft ([arXiv:2610.12803](https://arxiv.org/abs/2610.12803), read in full
from the project copy), the squared height \(Q\) of the highest zero of the
heat-flowed function obeys
\(Q'\le-2-\tfrac{4Q}{p}S(x,p,t)+\tfrac{8Q}{p^2-Q}\) whenever
\(p^2\ge5Q\), where \(S(x,p,t)=-\operatorname{Im}(H_t'/H_t)(x+ip)\) is a
Poisson-smoothed zero density at height \(p\). The kernel inequality behind
it, \(K_h\ge(h/p)K_p\) for conjugate pairs, is elementary and I rederived
it; Hakimoglu-Brown attributes it also to Gordon's Section 5. For zeta the
floor on \(S\) is \(\tfrac14\log\tfrac{x}{4\pi}-\tfrac12\kappa(\sigma_0)\),
which vanishes at low height, so the zeta argument needs a verification
height, a barrier and Polymath's confinement theorem. For a primitive
character the gamma factor contributes \(\tfrac14\log\tfrac q\pi\) at
**every** height, so the floor is a conductor constant on the whole line,
and no verification, barrier or finite-region lemma is needed. That is the
whole idea, and it is a good one: the conductor supplies at \(x=0\) what
zeta only has at heights \(x\approx4q\).

**The repository's own contributions** (checked in outline). Three steps
are not in Hakimoglu-Brown and are, as far as I can tell, the repository's
in this form (the Gaussian smoothing itself is Polymath's equations
(40)–(41), applied there summand by summand): the transport lemma of
[03 round-one Note 01](../03_effective_outer_remainders/notes/round-1/01_HEIGHT_P_TRANSPORT_AND_LEMMA_AP_CLAUDE_20261017.md),
which expresses \(S\) at positive time as the real part of a logarithmic
derivative of a Gaussian average of \(\xi_\chi\) and bounds the deviation
from the time-zero floor by an explicit remainder \(E\) without any
Riemann–Siegel formula; the uniform envelope of
[03 Note 01](../03_effective_outer_remainders/notes/round-2/01_UNIFORM_FAMILY_FLOOR_CODEX_20261017.md),
certifying \(E<1/5\) for every \(\ell\ge129/5\), every real height and
every \(0<t\le1/4\); and the one-step lemma of
[03 Note 02](../03_effective_outer_remainders/notes/round-2/02_RESTARTED_STRIP_COMPARISON_CODEX_20261017.md),
which replaces the confinement hypothesis H12 by a sine-tail approximant
whose nonreal zeros are confined, propagates the height-three floor over a
short step by a Riccati comparison for the complex Burgers equation, and
restarts at the original time slices. The last of these also removes the
dependence on Polymath's Theorem 1.5(i) that Hakimoglu-Brown's zeta
argument retains, which is worth a remark in the paper.

**Where my 16 October review was wrong** (opinion). Section 2.1 of the
[portfolio setup review](../reviews/01_PORTFOLIO_SETUP_REVIEW_CLAUDE_20261016.md)
priced the per-character route under the barrier architecture, found that
Platt's verification is a fixed budget in the analytic conductor, and
concluded that "the conductor does not trade for height". That was correct
for the barrier architecture and wrong as a verdict on the route: under the
height-\(p\) floor architecture the conductor trades for height at every
\(x\), with no verification at all. The almost-all target of my
[16 October brainstorm, §9.2](../../brainstorm/investigations-3/notes/03_MODIFICATIONS_AND_ALTERNATIVE_DIRECTIONS_CLAUDE_20261016.md)
has been superseded by an all-characters theorem. I record this because
the assessment's claim that the direction "has become a proved comparison"
is the kind of claim a reviewer should test against his own earlier
estimate, and the earlier estimate loses.

**Novelty** (literature reading, not a priority audit). The repository's
ledger has Ki–Kim–Lee, Section 6, Example 1, for a qualitative bound below
\(1/2\) for real primitive characters, and the MathOverflow question of
1 October 2026 posing the conductor limit with a \(\log\log q/\log q\)
heuristic and unfinished steps. Today's searches (de Bruijn–Newman
constants of Dirichlet \(L\)-functions, conductor aspect; the Newman–Wu
survey [arXiv:1901.06596](https://arxiv.org/abs/1901.06596), which has no
\(L\)-function content; the Castillo–Muñoz–Poblete–Salinas "generalized
Riemann zeta heat flow", which is a different flow) found no
conductor-dependent upper bound. The MathOverflow page could not be fetched
from this session; a human should read its answers before the paper claims
anything beyond "not found", and the paper should cite the question
prominently either way. The honest headline is "an explicit upper bound
tending to zero in the conductor aspect", with "first" left to the referee.

## 2. Is the direction optimal?

### 2.1 Against the program's own rule

The portfolio plan's aim is "an applicable estimate, a complete numerical
gain, a useful diagnostic or a precise obstruction". By that rule, which
is the one the whole second portfolio converged on, 01+03 is the first lane
in the program to deliver an applicable estimate whose consumer is a
theorem and not another criterion. Projects 04 and 05 delivered scoped
obstructions, 06 an estimate without a consumer, 07 an approximation-class
theorem; all are legitimate outputs under the rule and none is a theorem
with a number. So within the portfolio the assessment's allocation is
right: two tracks, 01+03 and 02, and the rest dormant or consolidated.

### 2.2 Against the alternatives that were on the table

The 16 October exchange considered six structural directions
(source-space rigidity, constructive stable approximation, collective
prime interactions, surrounding-zero attraction, canonical systems, the
modular deformation) and the family route. Every structural direction
ended at the scale argument or at an RH-equivalent reformulation, and
Projects 05 and 07 have since turned two of them into precise negative
results. The family route is the only one that produced a theorem. I do
not see a structural direction in the result summaries that has a better
expected yield over the next month than consolidating the theorem in hand;
Section 6 lists the candidates I would bring to the brainstorm after the
paper, and none of them is urgent.

### 2.3 The ceiling, stated once

Heat-flow upper bounds cannot reach the conjecture: \(\Lambda\le0\) is RH
and \(\Lambda_\chi\le0\) is GRH, so every result in this direction is a
quantitative shadow of the conjecture. For the family, \(T(q)\to0\) is
consistent with the expectation \(\Lambda_\chi=0\) and says nothing about
any individual zero. For zeta, each constant improvement needs either
exponentially more verification or a new analytic input, and the
unrefereed 7/8 half-plane claim shows what such an input does: it moves
the conditional bound to \(0.13963\) in one step. The direction is
therefore good for one or two papers and then has diminishing returns, and
the plan should say so now rather than discover it in a month (Section 6).
This is a judgment about yield, not an impossibility statement, in the
sense of [avoid 07](../../../avoid/07_scoped_exclusions_read_as_universal.md).

### 2.4 The zeta lane is crowded and exposed; the family lane is not

Three unrefereed 2026 bounds compete on zeta, Gomila's \(0.1787854\),
Gordon's computer-assisted preprint and Hakimoglu-Brown's conditional
\(0.13963\), and the repository's planned \(0.1745354\) would be a fourth; it completes
the sharp-weight option that the repository's own audit of Gomila's
package identified. Project 02's
[manuscript](../02_sharp_finite_sum_bounds/manuscript/sharp_finite_sum_bounds/main.tex)
(the corollary labelled `cor:conditional`, Corollary 7.1 in the Claude
review's numbering) states its conclusion conditionally on "the imported
initial-verification and historical barrier inputs", the barrier being
Gomila's package at the status of the repository's own audit. If the 7/8
claim is accepted, \(0.1745354\) is superseded the same day by
\(0.13963\); if it is not, \(0.1745354\) would be the best bound whose
dependency ledger the repository can vouch for, which is a real but modest
distinction. The family lane has no competitor that today's search found.
Effort should follow that asymmetry.

### 2.5 Verdict

Optimal for the month, with the reordering of Section 4; not a long-term
home; and the assessment should say both.

## 3. The four documents, and the answers to the merger note's six questions

### 3.1 The progress assessment

Its table and per-project readings agree with the sources I read, and its
status language is careful. Two corrections of emphasis.

First, the uniform floor's status line should name the one input that no
cross-model reader has audited: Proposition 4.5 of the round-one transport
note and the envelope of Note 01 that assembles it. The Codex
[audit](../03_effective_outer_remainders/reviews/03_FAMILY_FLOOR_AND_RESTART_AUDIT_CODEX_20261017.md)
is thorough and is same-model, as it says. What I can add (checked in
outline, with one back-of-envelope): the structure of Note 01 is a
Gaussian average centred at the saddle \(\sigma_*=2+h\ell/2\), with the
Euler product majorants on the right, a partial-summation bound on the
critical interval \(\tfrac12\le u\le\tfrac54\), and the functional equation
beyond; the critical-interval density (9) at its worst cell gives, by my
own arithmetic at \(u=5/4\), \(\ell=25.8\), an exponent near \(-18\) at
\(h\approx0.06\) and a prefactor near \(460\), hence a contribution of
order \(7\cdot10^{-6}\), against the certified \(D_{\rm crit}<6.7\cdot10^{-6}\),
and the numerator weight of order \((\sigma+\tfrac14)/h\approx50\) gives
order \(3.5\cdot10^{-4}\) against the certified \(N_{\rm crit}<3.5\cdot10^{-4}\).
The two leakage figures are therefore of the right size; this is not an
audit of the derivation.

Second, the assessment calls the sine-tail construction Project 01's
"essential advance". It is, but the construction is consumed by a
restart that is Project 03's, and the single most important sentence in
the chain is Note 02's "one never assumes that the original positive-time
floor holds for its approximants". The merged manuscript should make that
sentence a displayed remark, because it is the point a referee will probe.

### 3.2 The conductor-rate note and the restart lemma

**Verified.** \(L(10^{12})=25.909075565\), \(C=6.0923\), \(k=7.1230\),
\(T(10^{12})=0.2130631631\), \(\log(9/2)/7=0.21487<43/200\), and the two
exact gates of Note 02 (record G; the terminal gate \(e^{kT}=4.4990\)
against \(1+k/2=4.4973\) is as tight as the note says). The constant-floor
limit \(\tau(C)=\log(1+k/2)/k\) is the correct \(\delta\to0\) limit of the
affine recurrence, and the passage to the endpoint by Hurwitz is standard.
The asymptotic (7) follows from \(k\sim\tfrac13\log q\).

**Checked in outline, with rederivations.** In Note 02's one-step lemma:
(i) for \(\partial_sG=-G''\), \(U=G'/G\) satisfies \(U_s+2UU_x+U_{xx}=0\),
whose imaginary part at height three is exactly the displayed Burgers
equation for \(S\); (ii) with every zero in \(|\operatorname{Im}\rho|\le1\),
\(|u_x|\le\sum|z-\rho|^{-2}\le\tfrac12S\) because \(3-v\ge2\), and
\(|S_{xx}|\le\tfrac12S\) because \(\sup_D(6D-2a^2)/(D+a^2)^2=9/(8a^2)\)
and \(\inf_D=-2/a^2\), both within \(\tfrac12\) for \(a=3-v\ge2\); (iii) \(y'=-y/2-y^2\) from \(y(0)=C\) is \(m_C(s)\);
(iv) at a simple zero \(\dot z=2\sum'(z-\rho)^{-1}\), the own conjugate
contributes \(-1/h\) to the vertical velocity, and the kernel ratio for a
pair tends to \(h/p\) at large distance and exceeds it everywhere, so with
\(p=3\) and \(Q\le1\) the removed pair costs exactly \(8Q/(9-Q)\le Q\),
giving \(k=4c/3-1\); (v) the full sine lattice at height three has Poisson
sum \(\kappa\tanh(3\kappa)\), and the missing \(|j|\le M\) part costs
\(O(1/(hR))\) at \(|x|\ge R/2\). I did not rederive the Rouché confinement
of the approximants' nonreal zeros over the step or the uniform
sub-Gaussian majorant, both of which read correctly.

**One scope remark on the deduction.** Retaining \(C(q)\) rather than
\(6\) is legitimate exactly because Note 01's envelope is monotone in
\(\ell\) at fixed \(h\), including the numerator weight that grows like
\(\sigma/h\). The Codex audit checked this; the Claude review should
rederive the sign of the \(\ell\)-derivative of the complete per-cell
envelope once more, since it is the one place where "retain the conductor
term" could fail and the whole rate depends on it.

### 3.3 The research directions memo

Directions 1 and 2 are right. On 3–6:

- **Direction 3 (couple value and derivative).** This is Hakimoglu-Brown's
  \((\lambda,\mu)\) kernel, which gained 15% for zeta
  (\(0.16408\to0.13963\)). For the family it needs an upper bound on
  \(\partial_pS\), which the current envelope does not certify. A plausible
  10–15% at \(10^{12}\), no change to the rate. Rank it below the two free
  levers of Section 4.
- **Direction 4 (upper transport as a family tail bound).** The memo's own
  stop condition applies: the sine-tail construction's radius \(R\) is
  existential, so there is no consumer. Stop, as the memo says.
- **Direction 5 (a faster conductor rate).** The diagnosis needs
  correcting. The memo says a floor at a height that follows the strip
  "leaves the Euler-product half-plane used by the current proof" and
  needs "a new arithmetic estimate". At time zero that is true. At the
  times that matter, \(t\ge c/\ell\), the transport saddle sits at
  \(\operatorname{Re}s_*=\tfrac{1+p}{2}+\tfrac t4\ell_*\), which is inside
  the half-plane for every \(p\ge0\) once \(t\ell_*/4>\tfrac12+\delta\).
  The estimate the memo asks for is the existing Proposition 4.5 run at a
  lower height, where its cost C3 (Gaussian mass left of
  \(\operatorname{Re}s=1\)) becomes the binding term instead of a
  negligible one. Section 3.4 prices it. The conclusion is the same as the
  memo's, remark not gate, but for a reason that can be written down.
- **Direction 6 (conditional reopenings of 07, 04, 05).** Agreed as
  written, including the finite-domain qualification for 07 and the
  stable-Bessel reverse control for 05.

### 3.4 The faster rate, priced (planning)

Where the \(\log\log q\) comes from: with the floor at the fixed height
three, the push on the highest zero is proportional to \(Q\) (the kernel
ratio \(h/p\)), so \(Q\) decays exponentially at rate \(k\approx\ell/3\)
from \(1\) to about \(2/k\) before the own-pair term finishes it; the
exponential approach costs the factor \(\log(1+k/2)\). A floor at a height
proportional to the current strip removes that factor: with
\(p=\kappa h\), \(\kappa\ge\sqrt5\), one gets \(d\sqrt Q/dt\le-\ell/(2\kappa)\)
and a finish in time \(2\kappa\sqrt{Q_1}/\ell\). Alternatively, as in
Polymath's exterior theorem, first-term dominance at height
\(y_0\asymp1/\ell\) and time \(t_0=c/\ell\) gives a zero-free region, and
de Bruijn finishes in \(y_0^2/2=O(\ell^{-2})\).

What it costs. At height near zero and time \(c/\ell\), the Gaussian mass
on the critical line relative to the saddle is \(q^{-c/16}\), and the
size of \(L\) there relative to \(L(s_*)\) is at most \((q|s|)^{1/2}\) by
the partial-summation lemma the envelope uses, or \((q|s|)^{1/4}\) by
convexity. So the leakage is controlled only for \(c>8\) with the
envelope's own tools and \(c>4\) with the convexity bound; by my estimate
the same threshold \(c\approx4\) appears from the \(n\approx N\) terms of a
Polymath-type mollified sum. Adding the de Bruijn or moving-floor finish,
the achievable constant is between \(7\) and \(12\). Record E: a bound
\(c/\log q\) overtakes \(T(q)\) only for \(q>10^{22}\) at \(c=7\),
\(q>10^{46}\) at \(c=9\), \(q>10^{134}\) at \(c=12\). The faster rate is of
theoretical interest, deserves one remark in the paper with this
arithmetic, and should not open a project. Everything in this subsection
is planning under the stated assumptions; nothing in it is proved.

### 3.5 The merger and octonionic note, and its six questions

1. **Merger.** Yes. One canonical home under 01, 03's notes and records
   left in place with a crosswalk, 03's zeta table kept as a separate
   conditional application. Two constraints the note does not state: the
   merged manuscript should be a **new short paper** of fifteen to twenty
   pages (normalization; time-zero floor; transport and the certified
   envelope; the one-step lemma and restart; the two theorems; remarks on
   constants, the rate and the general class) rather than an edit of
   either existing manuscript with appendices; and the \(0.27\) bound and
   the \((\log q)^{-4/7}\) route should become a remark, since
   \(T(q)\) supersedes both at every conductor.
2. **Does the all-\(\ell\) domination retain the conductor term as the
   deduction uses it?** Yes, on the strength of Note 01's monotonicity
   claims, which the Codex audit checked; see the scope remark in 3.2 for
   what the Claude review must rederive. Both parities are covered because
   \(\psi(3/2)>\psi(1)\) and the even gamma majorants dominate; both height
   directions because the digamma bounds depend on \(|\operatorname{Im}|\)
   only; the endpoint by Hurwitz. Verified: \(\ell_0=L(q)\) for even
   characters, and the odd floor is larger.
3. **Correlated Gaussian remainder.** The disk enclosure (4.1) is correct
   as algebra (Bessel's inequality for the two orthonormal functions) and
   the integrability condition \(2hk<1\) holds comfortably. But the
   consumer does not need it: \(E\) enters \(T(q)\) only through
   \(77/200\), and setting \(E=0\) changes \(T(10^{12})\) from \(0.21306\)
   to \(0.21115\), a gain of \(0.9\%\) (record B). Do not run the pilot for
   the family bound. If any remainder work is wanted, it belongs to a
   consumer with small margins, which is 02, and 02 does not use this
   transport.
4. **Derivative consumer.** See direction 3 above: a bounded task with a
   plausible 10–15%, after the free levers, only if a referee-facing
   constant matters. Compare Parseval and Schwarz–Pick only when the
   derivative envelope exists; neither is needed for the theorem.
5. **Oscillator coordinates.** Verified: with \(y=e^{4u}\),
   \(\partial_y\vartheta=\tfrac1{4\pi}\partial_w^2\vartheta\) gives
   \(\partial_uW=2\eta W_\eta+W_{\eta\eta}\) for
   \(W=\vartheta(\eta\sqrt{y/\pi},iy)\), and the prefactor \(e^ue^{\eta^2/2}\)
   turns this into \(\partial_u\mathscr U=(\partial_\eta^2-\eta^2)\mathscr U\),
   hence \(U_k'=U_{k+2}-k(k-1)U_{k-2}\); Jacobi inversion gives
   \(\mathscr U(u,\eta)=\mathscr U(-u,-i\eta)\). The normalization is
   right. It is the statement that the theta heat flow in \(u\) is the
   quantum oscillator in the Hermite variable, which is classical, and the
   note's own four limits are the correct assessment. No signed estimate
   is visible to me either. One remark in the paper's source section, no
   lane ([avoid 03](../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)).
6. **Distinctive octonionic contribution.** None identified, which the
   note itself concludes. Record the dictionaries (summaries 14 and 16)
   and close the question; this is the third review to reach that answer
   and it should be the last.

A remark on the note's form: its decision content is Section 1 and
Section 8, about a page; the rest re-derives identities already in
summaries 14 and 16 and proposes pilots whose maximal gain is computed
above. Under [avoid 20](../../../avoid/20_volume_without_a_gain.md) the
next such note should begin with the number it would change.

## 4. What I would change: an ordered plan with gates

Three weeks, two tracks, nothing else opens.

**Week 1, gate: no defect.** (a) A Claude cross-model review of the
complete chain, in this order: the normalization and time-zero floor
(01 round-one note), Proposition 4.5 and Lemmas 3.1–4.4 of the round-one
transport note with the manuscript's saddle-domain correction, Note 01's
envelope and program, Note 02's one-step lemma, the conductor-rate note.
Section 5 lists the checkpoints. (b) In parallel, Codex: the \(p=\sqrt5\)
pass (record C: \(0.1965\) at \(10^{12}\) with \(E=0.2\), \(0.1987\) with
\(E=0.4\); the envelope must be re-certified at the new \(\sigma_0\), where
\(\kappa(\sigma_0)\approx1.15\) and the leakage costs grow), and the
manuscript corrections the audit already listed (the Ki–Kim–Lee sentence,
the "transfer outstanding" paragraph). If (a) finds a defect, everything
else waits.

**Week 2, gate: a statement a referee can check.** (c) Lower the
conductor threshold as far as the envelope allows at whatever \(E\) it
gives: the restart is nonvacuous from \(C(q)>3/4\), that is \(q>525\)
(record F), and if \(E<1/5\) extended, the same restart would give
\(T(10^4)\approx0.41\), \(T(10^6)\approx0.32\), \(T(10^8)\approx0.27\).
Round one's grid already found the time-dependent floor above the
time-zero floor from \(q\approx1.3\cdot10^3\) at \(p=3\) in floating point.
Some of the envelope's reductions use \(\ell\ge129/5\) (the \(3/L<1/4\)
comparison, the \(\ell\ge1/h\) case) and would need reworking below it,
so this is a certificate task, not a parameter change; a certified
\(q_0\le10^6\) seems plausible (opinion) and would change the theorem from
a statement about an uncomputable regime to one about all but a finite,
enumerable set of characters. (d) Test the restart lemma on a control that
can refute it. The theorem itself cannot be falsified on actual
characters: for small conductors GRH is verified far beyond the relevant
heights, so the zeros of \(H_{t,\chi}\) are real at every \(t\ge0\) and
any upper bound passes
([avoid 11](../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md)).
The zeta-type collision controls are uninformative for a different
reason: the lemma needs a floor on the whole line, and at small \(x\) the
height-three density of zeta and of the Euler-factor controls of
[Investigation 19](../../investigations-2/active/19_euler_factor_controls/manuscript/euler_factor_controls.tex)
is about \(0.03\), far below the \(3/4\) at which the lemma says
anything. The informative control is the character version of that
construction: multiply \(H_{0,\chi}(z)\) at conductor \(q\) by
\(1+c\cos(az)\), \(a=\tfrac12\log\mathfrak p\), \(0<c<1\), exactly as
Investigation 19 does for zeta (at the kernel level,
\(\Phi_\chi+\tfrac c2[\Phi_\chi(\cdot+a)+\Phi_\chi(\cdot-a)]\)). This keeps
the conductor floor up to the factor's bounded contribution to the
height-three density, has the explicit heat flow of 19's flow theorem, and
starts with a conjugate pair at height
\(\operatorname{arccosh}(1/c)/a\), inside the unit strip for \(c=\tfrac12\)
and \(\mathfrak p\ge17\). The lemma predicts that
the pair is back on the axis by \(\tau(C_{\rm control})\), with
\(C_{\rm control}\) the control's measured floor; a tracked return time
beyond \(\tau\) would refute it. That is a test that can fail, a bounded
numerical task (at \(q=10^{12}\) and \(\mathfrak p=17\) the lemma predicts a return by
about \(0.2\) against de Bruijn's \(0.43\) for the pair's own strip, and the
transport saddle keeps most evaluations in the absolutely convergent
region), and the only end-to-end check of the chain available short of
specialist review. The other testable part is the floor inequality on
actual characters at moderate conductor, which round one sampled at 124
points and which (c) would certify. (e) A one-page feasibility memo on the
general class (Section 6, first item).

**Week 3, gate: the paper.** (f) The short paper of 3.5(1), with the
result summaries 08 and 11 and the avoid entries updated in the same
commit, per [avoid 19](../../../avoid/19_status_files_that_lag_the_findings.md).
(g) Project 02's activation certificate completed in parallel if its
dependency ledger can be stated unconditionally except for Platt–Trudgian
and the audited barrier; its theorem statement carries that ledger. (h)
After (f), the brainstorm of Section 6; until then no new lane.

What this drops from the directions memo: the correlated-Gaussian pilot,
the oscillator reserve, the family tail bound, and the faster-rate gate,
for the numerical reasons in Section 3. What it adds: the height lever, the
threshold, the character-control test, and the general class.

## 5. Checkpoints for the cross-model review of the chain

For the reviewer of week 1, the places where I would expect an error if
there is one, in order of consequence:

1. **Lemma 3.3's contour shift to the complex saddle.** The fixed point
   \(\mu_*\) is complex; the constant \(e^{-\mu_*^2/2\tau^2}\) cancels in
   the ratio, but the justification of the shift uses order-one growth of
   \(F^{(k)}(w+h)\varphi_\tau(h)\) on the vertical sides; check it for
   \(k=1\) and for the family's \(x\)-dependence.
2. **Proposition 4.5's denominator.** \(d_0=e^{-\tau^2\kappa_*^2/2}-P_1-P_2\)
   lower-bounds \(|\int G\varphi_\tau|\) using
   \(|e^{c_1^2\tau^2/2}|\ge e^{-|c_1|^2\tau^2/2}\) for complex \(c_1\);
   confirm that every term moved into \(P_1,P_2\) is bounded in modulus,
   not in real part.
3. **The partial-summation bound in the critical interval (Lemma 4.4)**
   and its insertion as \(Z(u)\le(\ell+5)e^{(1-u)_+(\ell+2)}\) with
   \(N=\lceil\mathcal Q/2\rceil\): check the height proxy
   \(\mathcal Q=2\pi e^{\ell+c_*}\) bounds \(q|s|\) at the saddle's height
   in both height directions.
4. **Monotonicity in \(\ell\) of the complete per-cell envelope**
   including the numerator weight (3.2 above); this carries the
   conductor-rate deduction.
5. **The far reflected tail's three cases** at small \(h\) and the claim
   that they leave no gap near \(h=0\) or at large \(\ell\).
6. **Note 02's Rouché confinement** of the approximants' nonreal zeros
   uniformly over the step, and the real-rootedness of the far sine zeros
   after the heat step.
7. **The multiple-contact exclusion** by backward Hermite splitting, which
   is used at every step; it is local and standard but should be stated
   with the \(O(v)\) barrier motion.
8. **Parity and complex characters:** that Dobner's phase \(\alpha\)
   (\(\alpha^2\) proportional to the inverse root number) makes
   \(H_{0,\chi}\) real on the real axis, that the zero strip is
   \(|\operatorname{Im}z|\le1\), and that no step uses evenness in \(x\).

Each of these is a place to read, not a suspicion; I found no defect in
the parts I rederived.

## 6. After the paper: candidates for the next brainstorm

Listed with their numbers so that the next brainstorm can start from them;
none is a recommendation to open a folder now.

- **The general class.** Nothing in the chain is specific to degree one
  except two constants: \(|L'/L(s)|\le d\,\kappa(\sigma)\) on
  \(\operatorname{Re}s>1\) for a degree-\(d\) Euler product with
  Ramanujan-type coefficients, and the gamma factor's
  \(\tfrac12\log Q_F+\tfrac12\sum\omega_i\operatorname{Re}\psi(\cdot)\).
  Dobner's class \(\mathcal S^\sharp\) already supplies \(\Lambda_F\) and
  \(\Lambda_F\ge0\), the strip is still \(|\operatorname{Im}z|\le1\), and
  Cardon's theorem and the sine tail are generic. A theorem
  "\(\Lambda_F\le T_d(Q_F)\), so de Bruijn–Newman constants tend to zero
  in the conductor aspect in any bounded-degree family with Ramanujan
  bounds, including holomorphic GL(2) forms in the level aspect" would be
  substantially more visible than the Dirichlet case at modest cost; the
  cost is in redoing Note 01's envelope with \(d\kappa\) and general
  \(\omega_i\). Gate: the Dirichlet review passes first.
- **Conditional strips.** Record D: if a half-plane
  \(\operatorname{Re}s>7/8\) held for the character, \(Q_0=9/16\) gives
  \(T(10^{12})\approx0.154\); \(\operatorname{Re}s>3/4\) gives
  \(0.089\). One remark, as Hakimoglu-Brown did for zeta; no dependence
  of the main theorem on any unrefereed input.
- **Almost-all improvements.** A zero-density estimate gives most
  characters a smaller initial strip up to a given height, and the floor
  grows with height through \(\ell_*\); a height-dependent restart could
  convert this into a smaller bound for all but \(O(q^{1-\delta})\)
  characters. This is my earlier §9.2 target in its remaining useful
  form; it is a second paper, not a section.
- **The faster rate** as a remark only (3.4).
- **Leaving the direction.** After the general-class paper, the expected
  yield of further heat-flow upper bounds is low: constants for zeta in a
  crowded field, or asymptotic rates that matter beyond \(10^{22}\). The
  brainstorm after the paper should ask what the next theorem with a
  number is, and should allow the answer to lie outside heat flow. The
  discipline the program has learned, controls first, numbers first,
  classification first, transfers.

## 7. Housekeeping

- Six compiled PDFs (0.30–0.56 MB) sit in the project manuscript folders,
  within `LARGE_FILES.md`; if the October decision to track only `.tex`
  stands, they should go. Decide once and apply to all seven projects.
- The portfolio README's opening table still shows the planning
  checkpoints; the assessment asked to route it to the current state, and
  this review and the week-1 outcome should be linked from it when they
  exist. This note does not edit it, since the README has one writer.
- The brainstorm folder had no `numerics/`; this review adds one with its
  planning script and record, following the layout of the earlier
  [planning brainstorm](../../brainstorm/investigations-3/numerics/README.md).
- Two reviews in 03 and one in 01 are same-model; the folder READMEs say
  so correctly. After the week-1 review, the status lines of 01, 03,
  result summaries 08 and 11 and the portfolio README should move
  together.
- `tools/check_repository_hygiene.py`, run on 18 October, reports four
  broken local links, none from this review: the two pre-existing links
  to the uncommitted PDF of Investigation 19's manuscript, and two links
  in 03 (`chat-histories/claude-cowork/README.md` and
  `source-documents/README.md`) that still point at
  `01_dirichlet_newman_families/notes/01_NORMALIZATION_AND_TRANSFER_CONTRACT_CLAUDE_20261017.md`,
  which moved to `notes/round-1/` on 17 October. The relocation receipt
  should be followed by a link fix.

## 8. Coverage and scope

Read in full: the three Codex documents in this folder and the
conductor-rate note; the brainstorm README and the portfolio README, draft
history and plan; the portfolio setup review; `avoid/01`–`20` and
`result-summaries/07`–`17` in full, `01`–`06` and `15` in summary; 03's
README, round-one Note 01 through Proposition 4.5, round-two Notes 01 and
02, and Review 03; 01's README and source ledger; 02's README, the
dependency passages of its manuscript and the opening of its Claude
review; Hakimoglu-Brown's draft from the project copy; the Newman–Wu
survey's \(L\)-function content (none) by fetch; the abstract of
arXiv:2402.10154. Not read: the remainder of the round-one transport note
(its Section 4 after Proposition 4.5 and Sections 5–10), the 24-page
transport manuscript, 01's manuscript and its round-3 and round-4 notes,
the 02 numerics, and the 04–07 sources beyond the assessment's readings and
the result summaries; the MathOverflow page, which this session could not
fetch. Rederived: the items marked verified or checked in outline in
Section 3, and the identities of question 5. Computed: the planning record,
standard-library floating point, not a certificate; it reproduces
byte-identically under Python 3.10 on Edward's machine and 3.13 in the
session workspace, and the hygiene checker passes on the added files. No
file of the assessment was modified; this review, the numerics folder and
a README entry were added, and nothing was committed to git.
