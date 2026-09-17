# Continuation note, end of session three

**Author: Claude Opus 5 (Anthropic).** 17 September 2026. Handoff. Supersedes
nothing; read [session two's](CONTINUATION_20260917_SESSION2.md) first for the
frame-bound state, and [session one's](CONTINUATION_20260917.md) for the eight
facts.

---

## 1. What this session did

One item, the first of session two's revised pathway: *find a reflection
amplitude with the archimedean shift at a quarter.* It is answered, and the
answer closes the line rather than opening it. Everything is in
[the quarter-shift survey note](THE_QUARTER_SHIFT_SURVEY_20260917.md) and in
manuscript version **0.8**, recorded and snapshotted as `drafts/2026-09-17-v08`.

**Why there are three snapshots today, and it is the most useful thing in this
note.** Nothing in the mathematics changed between them. What changed is what was
*printed*, and both corrections came from changing instrument rather than
rereading.

*0.6 to 0.7.* Fitting the delay to numerically differentiated phases, instead of
trusting the Bernoulli algebra, showed that Proposition 11.5 --- which 0.6
generalized from the $\tau^{-2}$ term to all orders --- had dropped the universal
prefactor $(-1)^{m+1}/m$ at $m\geq2$. It is $+1$ at $m=1$, which is why the
$\tau^{-2}$-only statement of 0.5 never showed it. The prefactor is the same for
candidate and target, so no comparison changed; the equation was simply wrong.
Group H now carries the check that finds it: the residual left by the correct
truncation falls like $\tau^{-6}$ and the one left by setting the prefactor to $1$
like $\tau^{-4}$, observed $6.00$ and $4.00$.

*0.7 to 0.8.* An adversarial review of §§11.5--11.7 --- briefed to break the
section, not confirm it --- returned **eleven defects, all of which I then
confirmed independently**. Five were substantive:

1. **Proposition 11.12's last clause was false.** The bound
   $\sum n_j\leq(48|B_2(a)|)^{-1/2}$ only forces a single factor when
   $|B_2(a)|\geq\frac1{48}$, that is $a\in[\frac14,\frac34]$. At
   $a=\frac{4-\sqrt5}8$ one has $B_2(a)=-\frac1{192}$ exactly, the bound is $2$,
   and two factors with $n_1=n_2=1$ and equal widths hit $I_2=-\frac1{24}$
   exactly at every common width. **This one is inherited from version 0.5** ---
   it was in the manuscript before this session and survived two rounds of my own
   checking.
2. **The Eisenstein scattering matrix is the $\Lambda_\zeta$ ratio, not the $\xi$
   ratio** of the manuscript's own (2.9). The difference, $\frac{2s-2}{2s}$, is
   unimodular --- so it passes every check of unimodularity --- but its delay is
   $-2\tau^{-2}$, which would move $I_2$ from $-\frac16$ to $+\frac{11}6$. Right
   at the order the whole test lives at.
3. **The modular-surface expansion is of the archimedean factor only.** The
   arithmetic term $2\re\frac{\zeta'}\zeta(1+i\tau)$ does not decay --- it is
   $0.90$ at $\tau=10^4$ where $\tau^{-4}=10^{-16}$ --- and my claim that
   $\arg\zeta(1+2ir)$ is bounded was simply false. The corrected statement is
   better for the thesis, not worse: the term has mean zero and reaches no
   asymptotic coefficient, which makes it the exact counterpart of the prime term
   on the other side.
4. **$\Lambda$ is not dictionary-free**, so "matching says degree one" holds only
   in the normalization $\beta_j=\frac12$. The $\Lambda$ column is gone from the
   survey table.
5. **Sign conventions** in the survey table did not match the manuscript's own
   \eqref{eq:freewinding}. Fixed; by the inversion degeneracy no verdict moved.

The remaining six are precision: the expansion is now asymptotic with a
remainder; the two $I_6$ roots are one amplitude, $P$ double-covering the family;
the duplication identity is printed squared, the halved one being branch-dependent
and false as printed on whole intervals; $H_3^+$'s level-dependent $\Lambda$ is
labelled; the survey triples are printed so the table is reproducible; and the
cigar's tuning mechanism was misattributed to its shifts when it is the level
entering as a width. **No verdict, match or exclusion changed in any of this.**

## 2. Four facts to add to the list

**(13) The delay test is dictionary-free.** The graded quantities
$I_{2m}=\Lambda^{2m-1}\Sigma_{2m}$ are unchanged by the linear change of momentum
relating any candidate's variable to $\tau$ and by any common rescaling of the
widths. Target $I_{2m}=2^{2m-1}B_{2m}(\frac14)=-\frac1{24},\frac7{480},-\frac{31}{2688},\dots$
No dictionary ever has to be argued for again. Manuscript Proposition 11.6.

**(14) For one $\Gamma$-factor the archimedean shift is completely rigid.**
$I_{2m}=2^{2m-1}n^{2m}B_{2m}(a)$, the width absent; matching $I_2$ and $I_4$ is
$576u^2+60u+1=0$ with $u=B_2(a)$; the only solutions are
$(a,n)=(\frac14,\pm1),(\frac34,\pm1),(\frac12,\pm\frac12)$, one orbit of
inversion, parity and Gauss multiplication. Manuscript Theorem 11.9. This
subsumes the old sign window and does not need $n_j>0$.

**(15) Exactly one surveyed amplitude reaches the quarter, and it is the one
already cited.** The half-line inverted harmonic oscillator, even sector
$a=\frac14$ and odd sector $a=\frac34$; its $2$d-string dress is the $c=1$ matrix
model, which is its Gauss-duplication image and not an independent candidate.
Liouville at every coupling, FZZT, ZZ, $H_3^+$, JT/Schwarzian and the cigar at
every level and charge all fail --- most on the sign of $I_2$, the cigar only at
$I_4$. Manuscript §11.7.

**(16) The delay test cannot see the zeros.** The modular surface
$\Gamma\backslash\mathbb{H}$, whose Eisenstein scattering matrix
$\varphi(s)=\xi(2s-1)/\xi(2s)$ has the Riemann zeros themselves as resonances at
$s=\rho/2$, has $I_2=-\frac16$ and fails by a factor of four: its archimedean
factor is $\Gamma_{\mathbb{R}}(2s)$, and its resonances sit at $\re s=\frac14$
while the delay is read on $\re s=\frac12$, where $\zeta$ has no zeros and
$\arg\zeta(1+2ir)$ is bounded. Manuscript Remark 11.14. **Passing the test is not
evidence of having the zeros; having the zeros is not enough to pass it.**

## 3. The retraction, and why it matters methodologically

Manuscript 11.6 previously ended "and so is every amplitude built from
$\Gamma(m+i\,\cdot)$ with $m\geq1$." That is **false** with multiplicities of
both signs, and the counterexample is in closed form:
$\Gamma(1+ir\tau)/\Gamma(1-ir\tau)\cdot\Gamma(1-i\tau)/\Gamma(1+i\tau)$ has
$I_2=-(r-1)^2/3r$, hitting $-\frac1{24}$ at $r=\frac{17\pm\sqrt{33}}{16}$ with
$I_4=\frac5{384}=\frac{25}{28}$ of target. With the multiplicities free there is a
whole one-parameter family matching $I_2$ **and** $I_4$ with both shifts at the
supposedly excluded $a=1$; imposing $I_6$ leaves exactly two points and both are
Legendre duplication of the target.

The lesson is worth carrying: **each restrictive hypothesis in the old §11.5
($n_j>0$; integer multiplicities) excluded precisely the amplitude that matches.**
$H_3^+$ passes the old sign test ($\Sigma_2=-\frac14<0$) and fails the real one
($I_2=+\frac13$), because with $n<0$ the raw coefficient and the invariant have
opposite signs. Hypotheses added for the convenience of a Cauchy--Schwarz step
are where the physics went.

## 4. Where I think the programme now stands

Both halves of the two-sided question have now returned the same answer, from
opposite directions.

- Session two, §8: the frame-bound margin collapses at the same rate for the
  Gram points as for the zeros. **The margin is a density effect and carries
  almost no arithmetic.**
- This session, §11: the delay expansion pins the archimedean shift exactly and
  is provably blind to the primes (Remark 11.13) and, now, to the zeros
  (Remark 11.14). **The delay is archimedean and carries no arithmetic.**

The two quantities the investigation has instruments for are both archimedean.
The arithmetic lives in the bounded fluctuation $\pi^{-1}\arg\zeta(\frac12+i\tau)$,
which is invisible to every asymptotic order of one and washed out of the other.
I would not spend more time on candidate amplitudes; the next real step has to be
an instrument that sees the fluctuation. I do not have one to propose, and I would
rather say so than offer a survey.

## 5. Revised pathway

1. **An instrument for the fluctuation.** The open question. Everything below is
   secondary to it. One concrete sub-question that is at least well posed: the
   frame-bound note's §5 gap --- the *difference* between the zeros and a
   matched-density set is where all the arithmetic is, and it was measured as
   small but nonzero. Is it the same object as the fluctuation? A quantitative
   link would give the first instrument that is not archimedean.
2. **The universal frequency profile of manuscript §8.5.** Still unexplained;
   still the strongest unexplained regularity in the numerics.
3. **Independent re-derivation of the cigar reflection amplitude.** The one row
   of the survey whose $\Gamma$-structure I took from the literature and did not
   check; it is also the only row that survives $I_2$. If it were wrong the
   conclusion of §11.7 would change.
4. **Is $\{I_{2m}\}_{m\geq1}$ rigid in general?** Theorem 11.9 settles one factor.
   The two-factor family shows truncations are defeatable. A general rigidity
   theorem would make the test a genuine classification rather than a filter.
   Cheap to attack; low value, since by (16) a classification of the archimedean
   place still says nothing about arithmetic.

### A methodological note worth keeping

Every error found this session --- the overreaching clause, the dropped prefactor,
and the eleven of the review --- was found by changing instrument, and none by
rereading. The clause fell to a search for counterexamples in a region the
hypothesis had excluded. The prefactor fell to computing the delay a second way,
from differentiated phases instead of from the Bernoulli expansion. The review's
list fell to an adversary briefed to break the section rather than confirm it, who
recomputed every claim from the definitions and looked up the conventions the
prose relied on rather than inheriting them. Note the shape of defect 2: the wrong
$\varphi$ is unimodular, so it passed the check I had written; what caught it was
someone going back to what the symbol $\xi$ means in this repository.

Two rules I would keep. **Verification is a second route to the same number, not a
second reading of the first.** And **an adversarial pass is worth its cost on
anything about to be recorded** --- it found, in one call, more than my own two
rounds of checking had, including an error that had already survived into a
snapshot.

## 6. What not to redo

Everything in session two's list, plus:

- **Do not survey more reflection amplitudes.** Theorem 11.9 says what the answer
  must look like; the survey found the only realization; and (16) says a match
  would not mean much anyway.
- **Do not use the raw $\tau^{-2}$ coefficient as a test.** Use $I_2$. With
  $\Gamma$'s in a denominator the two have opposite signs.
- **Do not assume $n_j>0$ or integer multiplicities.** See §3.
- **Do not read the modular surface as a success of the programme.** Its
  resonances are the zeros and it fails the test; see (16).
- **The Liouville exclusion stands** and does not need redoing --- but it now
  follows from Theorem 11.9 for a single factor, not from the old sign rule.

## 7. State of the repository

- Manuscript **0.8**, 47 pages, recorded (`BUILD_RECORD.json`) and snapshotted at
  `drafts/2026-09-17-v08`; `drafts/2026-09-17-v06` and `-v07` are the superseded
  versions, see §1. Clean build: no undefined references, no overfull boxes, no
  multiply-defined labels.
- `validation/drafts.py check --replay`: **passed**, 1067 replayed cases, 8
  snapshots.
- `numerics/check_delay_test.py`: **525 checks, 8 groups A--H, all pass**, standard
  library only. Group H is new: the expansion checked against the delay assembled
  from $\re\psi$, including the decisive test on the universal prefactor; the
  invariants in exact rational arithmetic, the
  degeneracy to $m=8$, the single-factor classification plus a grid search finding
  nothing beyond the three solutions, every survey row, the closed-form
  counterexample, the bisection sweep of the two-factor family, the Legendre
  duplication identity, and the modular-surface shift. Record in
  `numerics/records/delay-test-checks.json`.
- `numerics/check_sampling_forms.py`: 336 checks, all pass, unchanged.
- New exploratory (unregistered, mpmath): `quarter_shift_survey.py`,
  `quarter_shift_classify.py`, `quarter_shift_twofactor.py`. The $\zeta$-dependent
  modular-surface identities live only there, to keep the registered programme
  free of $\zeta$ and $\xi$.
- Nothing in the tree exceeds 1 MiB.

## 8. Two things left for the author

1. **The two references added to `references.tex`** --- Moore--Plesser--Ramgoolam
   for the $c=1$ row and Iwaniec for the Eisenstein scattering matrix --- are
   cited for structure only and were not read here beyond the formula each
   supplies. Worth a glance before the manuscript leaves the house.
2. **The cigar rows** (pathway item 3). They are the only rows in the survey that
   could change a conclusion if the quoted amplitude is wrong.

See the [notes index](README.md).
