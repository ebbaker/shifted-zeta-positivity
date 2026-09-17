# Continuation note, 17 September 2026, second session

**Author: Claude Opus 5 (Anthropic).** Handoff. Read in this order:
§§1--3 here; then [the frame-bound note](FRAME_BOUND_AND_THE_DENSITY_20260917.md),
which is this session's whole output; then, if you have not read them,
[the first continuation note](CONTINUATION_20260917.md) for the manuscript's
state and the eight facts, and [the sampling note](SAMPLING_AND_THE_DEFICIT_20260917.md)
**with its new status header**, parts of which are withdrawn.

**Manuscript 0.4 now carries this session's results.** The frame-bound note was
written first and the manuscript folded in afterwards, in the same session:
Section 8, *The margin is a sampling constant, and the density sets it*, is new;
the old Sections 8--10 are now 9--11; the abstract, the introduction's road map,
the end of Section 7.5, Section 10.4, the outlook and the checks appendix are
revised; and eight references are added. 37 pages, recorded and snapshotted at
`drafts/2026-09-17-v04`, with `drafts.py check --replay` passing over **542**
cases in two registered programmes. Version 0.3 is preserved at
`drafts/2026-09-17-v03`.

---

## 1. What this session did

The task was to settle or sharply bound the lower frame bound of the Riemann
zeros as a sampling set for $PW_{L/2}$, in four steps. All four were done. Three
gave negative answers and one gave a structural result that changes the
programme's reading of its own central number.

**(a) Literature.** Closed. The de Branges route supplies no constant: Suzuki's
structure function is $\xi(\frac12-iz)+\xi'(\frac12-iz)$, not $\Xi$, and the
paper is purely structural; Ortega-Cerdà--Seip characterise sampling sequences
through de Branges theory but produce a dichotomy; Beurling's gap theorem gives
an explicit constant only for $L<\pi/\gamma_1=0.2223$. There is no theorem to
chase through the structure function.

**(b) Deficit-band trial space.** Negative, with a positive by-product. The
literal construction --- band $|\tau|<\tau_c$ plus exact vanishing at the
sub-critical zeros --- captures $100,100,76,59,53$ percent of
$\log\lambda_{\min}$ at $L=1.6,2.0,2.4,2.8,3.0$: a shrinking fraction, so no
decay law can be calibrated against it. The by-product is that the band
*without* the vanishing constraint has a **universal frequency profile in
$W/\tau_c$**, constant to $\pm1\%$ across $L\in[1.6,3.0]$, confirming $\tau_c$ as
the right scale.

**(c) Control.** This is the result. With the zeros replaced by **Gram points**
--- same counting function exactly, $S(T)\equiv0$, no arithmetic --- and by
jittered Gram points at three strengths, all in the same basis and truncation,
every arithmetic-free set collapses superexponentially at essentially the same
rate. The ratio $\ln\lambda_{\rm zeros}/\ln\lambda_{\rm Gram}$ falls monotonically
from $2.100$ at $L=0.6$ to $1.049$ at $L=2.8$. **The collapse is a density
effect.** The arithmetic is worth about three orders of magnitude, growing like
$\log L$, against a total growing like $e^L$.

**(d) The rate.** No one-parameter law survives $L\in[0.6,3.0]$; the best is
$22\%$ in the exponent. Zhu's law and the programme's $D$-law each fit their own
window and fail outside it. Given (c), what is left of the rate question is a
question about time--frequency localization with no arithmetic in it, and the
function it needs --- Kulikov's $\gamma_\varepsilon$ --- is stated by him to be
open.

Along the way: **a units error was found and corrected**, and the infimum was
shown to be **positive** rather than merely the form definite.

**Then items 1 and 2 of the revised pathway were run as well.** Item 1 returns a
negative: see [the delay-test note](THE_DELAY_TEST_20260917.md). In closed form
the group delay of a ray-frame defect two-point function of dimension $\Delta$ is
$\pi\operatorname{Re}\cot(\pi(\Delta+i\tau))$, exponentially small and
**identically zero** for every protected operator of the $\frac12$-BPS
Wilson-line defect CFT. The failure is structural --- a positive spectral measure
makes the causal symbol a Stieltjes transform, which has no zeros on the axis and
so cannot wind --- and the clause is satisfied by a *free* Hamiltonian, the
half-line inverted oscillator, whose phase shift misses $2\theta'$ by exactly
$\log\pi$. **And then the Liouville dictionary was fixed** --- item 1 of the pathway as the
delay-test note left it --- which turns the negative into a selection rule: see
[the expansion note](THE_ARCHIMEDEAN_EXPANSION_20260917.md). Matching the leading
coefficient forces $\tau=4QP$ with nothing left to tune but $b$, and the
$\tau^{-2}$ coefficient then comes out $+Q^2/3\geq\frac43$ against the target's
$-\frac1{24}$: **Liouville is excluded at every coupling and every $\mu$.** The
general form is a graded sequence of invariants --- leading coefficient = degree,
$\tau^{-2}$ coefficient = archimedean shift, constant = conductor --- with a
**rigidity theorem**: at a common shift the first two force a single $\Gamma$
with $a\in\{\frac14,\frac34\}$, the archimedean factor of a degree-one
$L$-function and nothing else.

**Manuscript 0.5** carries all of it: new Section 11, *The delay test, and what
the archimedean expansion selects*; Condition 10.1 rewritten with four clauses;
abstract, introduction and outlook revised; five new references; and
`check_delay_test.py` registered, so `drafts.py check --replay` now runs **742**
cases in three programmes. 43 pages, snapshotted at `drafts/2026-09-17-v05`.

---

## 2. The four facts a new session needs, beyond the first note's eight

**(i) Zhu's $L$ is half of ours.** arXiv:2608.24827 supports $f$ in $[-L,L]$;
this investigation supports $f$ in $(-L/2,L/2)$. His certified enclosure
$8.9\times10^{-18}\le\lambda^*\le2.27\times10^{-17}$ at his $L=0.8$ belongs at
**our $L=1.6$**, and his $3.19\times10^{-283}$ at our $L=4$. Group E of the new
check programme verifies the identification exactly. This cost the programme one
wrong conclusion; quote his numbers with the conversion attached.

**(ii) The recorded margins are right.** Recomputed independently from the
explicit formula in a sine basis: $5.657\times10^{-8}$, $9.590\times10^{-18}$,
$6.790\times10^{-28}$ at $L=\log3,\log5,\log7$, against the recorded
$5.537\times10^{-8}$, $9.293\times10^{-18}$, $6.802\times10^{-28}$. The sampling
note's basis warning is withdrawn; its *method rule* is not.

**(iii) $\lambda_{\min}(Q_{0,L})>0$, and there is no upper frame bound.** The
archimedean symbol grows like $\log|\tau|$, so the form domain embeds compactly
in $L^2(I_L)$, the spectrum is discrete and the infimum is attained; the
Cartwright counting argument then forbids a null vector. The same divergence
makes the form unbounded above, so the zeros are not relatively separated and
$\lambda_{\min}$ is the constant in the **lower** sampling inequality only.
Frame-bound language should be corrected wherever it appears.

**(v) The delay test is archimedean and cheap, and the manuscript's wording of it
names an object that does not exist.** A two-point function of a unitary defect
theory can accumulate at most $\pi$ of phase, ever; the target accumulates
$2\theta(T)$, which is $4069$ at $T=10^3$. The obstruction is that the dilatation
generator is bounded below --- not that the spectrum is discrete. And
[arXiv:1102.4948](https://arxiv.org/abs/1102.4948) computes expectation values,
not two-point functions, so the phrase "a protected open Wilson line two-point
function in the defect setting of \cite{OWL}" has no referent; the substitute is
the $\frac12$-BPS Wilson-line defect CFT.

**(iv) The margin carries almost no arithmetic information.** That is (c). It
strengthens manuscript Remark 7.7 and it invalidates the framing of
manuscript §7.5, which asks how $\varepsilon_L$ collapses "as the mechanism
question". A Gram-point "zeta" collapses the same way.

---

## 3. Recommended pathway, revised

**1. Find an amplitude with the archimedean shift at a quarter.** This is what is
left after the expansion note, and it is the sharpest instrument the programme
has: a candidate's reflection amplitude must contain a $\Gamma$ whose shift lies
within $\frac1{2\sqrt3}$ of one half. Every amplitude in the reflection
literature is built from $\Gamma(\text{integer}+i\,\cdot)$ and fails. The
structural hint: Liouville has the shift at an integer because its reflection is
off a wall on a half-line; a shift at a quarter needs something whose natural
variable is $s/2$ --- a square root of the radial coordinate, or a two-sheeted
cover. Candidate places to look: the $SL(2,\R)/U(1)$ cigar and $H_3^+$, whose
reflection amplitudes are $\Gamma$-ratios with shifts that depend on the level;
$\mathbb Z_2$ orbifolds and twisted sectors of a half-line; and the Schwarzian,
whose $\Gamma(\Delta\pm ik_1\pm ik_2)$ structure has four shifts at once. The
test is two lines of algebra per candidate, so a survey is cheap.

**2. The new question (c) raises.** If the density fixes the margin, what does
the arithmetic fix? The measured answer is the **gap** between the zeros and
matched-density sets: about $10^3$ at $L=2$, fitted by $1.61\log L+1.93$ in
$\log_{10}$ over $L\in[0.6,2.8]$. That gap is a new, well-defined, computable
object that *does* carry arithmetic, and it is the thing worth a law. Nothing in
the literature treats it.

**3. The universal profile of §4.1 of the frame-bound note.** The obstruction has
a well-defined frequency distribution in units of $\tau_c$, stable to $\pm1\%$
over $10^{80}$ in $\lambda_{\min}$. That is a candidate for an exact statement and
it is the one genuinely new structural fact this session produced.

**4. Manuscript Problems 8.6 and 8.7**, unchanged from the first note.

**5. The conformal congruence at the endpoint**, unchanged.

**What to drop.** Item 1 of the first note's pathway --- "the lower frame bound
of the zeros on $PW_{L/2}$" --- is **closed**, not continued. Its three steps have
definite answers and they are in §1 above.

---

## 4. What not to redo

Everything in §4 of [the first continuation note](CONTINUATION_20260917.md)
still holds. Add:

- **Do not look for the frame bound in de Branges theory.** §3 of the
  frame-bound note says what is there, with reading scope. The machinery
  characterises; it does not bound.
- **Do not build trial functions that vanish at the sub-critical zeros.** It is a
  strictly worse strategy than not constraining them, by $30$ orders of magnitude
  at $L=3$, and the gap grows. The minimiser makes $\widehat F$ small at *every*
  zero, not zero at the undersampled ones.
- **Do not fit a one-parameter decay law on a short range of $L$.** Over any
  factor-$1.25$ window, $D(L)$, $2Le^L$, $N(\tau_c)/\log N(\tau_c)$ and
  $D/\log(2\mathcal N_L/D)$ are indistinguishable at the few-percent level, and
  they diverge by tens of percent outside it. Section 6 of the frame-bound note
  has the table.
- **Do not delete the prime comb and call it a density control.** Archimedean
  plus pole is not a point set and is indefinite for $L\gtrsim0.85$. The control
  has to be a point set with the same counting function.
- **Do not trust a value of $\lambda_{\min}$ computed in a basis smaller than
  about $2.8$ times the Nyquist count $2Le^L$.** A run at $N=200$ looks converged
  to $L\approx2.8$ and is wrong by $121$ orders of magnitude at $L=4$.
- **Do not test a candidate by its leading $\log\tau$.** Every $\Gamma$-ratio
  supplies it, including the free dilatation generator on a half-line. Test the
  constant (the conductor, $\log\pi$) and the fluctuation (the primes, $S(\tau)$).
- **Do not look for the phase in a correlator.** Proposition 3.1 of the
  delay-test note: a two-point function of a unitary defect theory has total
  phase at most $\pi$, whatever the theory, operator or coupling. The object has
  to be a ratio.
- **Do not quote arXiv:2607.24830 as Suzuki's.** It is by six other authors, is in
  math.GM, is floating-point only, and contains a section recording nine false
  claims it caught in itself. The Suzuki companion that matters is
  arXiv:2606.09096, whose Theorem 1.3 (continuity of $\lambda_a$ in $a$) closes a
  gap Bombieri left. Section D2 of the source-selection-rules investigation's
  open-directions note should be corrected accordingly.

---

## 5. Repository state, and two things left for the author

New this session, all under the investigation:

- [`notes/FRAME_BOUND_AND_THE_DENSITY_20260917.md`](FRAME_BOUND_AND_THE_DENSITY_20260917.md), the research note.
- [`numerics/check_sampling_forms.py`](../numerics/check_sampling_forms.py) and
  [`numerics/records/sampling-forms-checks.json`](../numerics/records/sampling-forms-checks.json):
  336 checks in five groups, standard library only, JSON to stdout, deterministic on replay.
- Nine programmes under [`numerics/exploratory/`](../numerics/exploratory/README.md),
  all `mpmath` and all unregistered, which produce every table in the note.
- A status header on the sampling note; new rows in the notes index and in both
  numerics indexes.

**Both of the things left open at the first hand-off are now done.**
`check_sampling_forms.py` is registered in the `CHECKS` dictionary and
`BUILD_RECORD.json` has been rewritten for 0.4; and every recommendation of
Section 10 of the frame-bound note is in the manuscript. **A third check
programme, `check_delay_test.py` (157 checks), was written afterwards and is not
registered**, for the same reason the second one was not at the first hand-off:
registration edits a hashed file and has to be paired with a `drafts.py record`.
Pair it with the manuscript pass that replaces Condition 10.1. The `BUILD_RECORD.json`
that was deleted between sessions had a preserved copy inside
`drafts/2026-09-17-v03/`, so nothing was lost; deleting it was unnecessary ---
`drafts.py record` overwrites it --- and its only cost was that `check` and
`save` failed until 0.4 was recorded.

**Git.** No git command was run this session, so no `.git/index.lock` was left.
The working tree has the investigation as untracked, as it was at the start.

---

## 6. An honest word on direction

The sharpest thing I can say is in §7 of the frame-bound note and I will repeat
its conclusion here, because it is the part most worth disagreeing with. The
programme has treated $\lambda_{\min}(L)$ as the quantity a mechanism must
explain. On this session's evidence that is misdirected: the collapse is what the
density $\frac1{2\pi}\log\frac\tau{2\pi}$ does to the lower sampling constant of
a Paley--Wiener space whose type is far below it, and an arithmetic-free set with
the same counting function does the same thing to within a ratio of exponents
tending to one. Reproducing the collapse is therefore weak evidence for a
mechanism, and being unable to reproduce it is weak evidence against one.

The corresponding good news is that a mechanism is not required to produce an
arithmetic rate. It has to produce a density, and a $\log\tau$ group delay is a
much cheaper thing to ask of a candidate than a superexponential margin law.

The evidence is numerical and spans $L\in[0.6,3.0]$, which is $96$ orders of
magnitude in $\lambda_{\min}$ but only a factor of five in $L$; the ratio of
exponents is decreasing steadily but has not been shown to converge to one, and
one Gram-point family with one jitter draw per strength is not a proof about all
matched-density sets. If you want this load-bearing, the cheap strengthening is
to push the control to $L=3.5$ and to run several jitter draws; the expensive one
is to find out whether the ratio has a limit.
