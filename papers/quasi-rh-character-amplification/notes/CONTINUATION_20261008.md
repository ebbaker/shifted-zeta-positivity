# Continuation: the remaining signed mixed moment

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.

## Where the investigation stands

The [working manuscript](../manuscript.tex), *Conductor localization of a
mixed inverse–plain moment in a sextic character family*, records a
conditional reduction with an explicit remaining arithmetic estimate.
The [manuscript review](../reviews/MANUSCRIPT_REVIEW_20261008.md) records
its scoped checks and successful native compilation. Those checks are
same-model reviews, not independent specialist or formal verification.

The current conditional candidate remains **7/8 − 1/24000**. The proposed
**7/8 − 1/20000** requires a new uniformly proved mixed-moment saving of
**1/5000**, followed by the two rebalances already calculated. That saving
has not been proved. Neither candidate is an independently established
new zero-free theorem in this investigation.

The imported analytic machinery is from the
[September 30 companion preprint](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf).
The consulted PDF has SHA-256
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
This is distinct from the October 5 `paper2.pdf` that prompted the original
comparison. Its deep reflection, moment, and zero-free results remain
assumed; no Lean proof was replayed.

## The exact next target

Use the manuscript's definitions, actual coefficients, and fixed buffered
zero/profile bin. The relevant parameter box is

\[
9/25\le\delta\le21/50,\quad 49/100\le q/\delta\le1/2,\quad
7/10\le r\le37/50,\quad9/25\le m\le1/2.
\]

The inverse and plain lengths are \(D=U^r\), \(N=U^m\). The total length
\(z\) of selected whole physical prime slots lies just below \((1-r)/2\),
subject to the manuscript's two strict capacity inequalities. Set
\(K=1+\delta m-1/5000\) and

\[
\mathcal C_+=\{u\in\mathcal C:Q_{\psi_u}>U^{2m-1/1000}\}.
\]

Three parts are already controlled from the stated source assumptions:

| Removed contribution | Margin below exponent K |
| --- | --- |
| Smaller primitive row conductor | at least 1/6250 |
| Entire plain-variable diagonal k = k′ | at least 647/5000 |
| Remaining column-ratio conductor through U^(4/5) | at least 23/1250 |

Consequently, with all coefficients and zero masks retained,

\[
\sum_{u\in\mathcal C}|M_r(u)S_m(u)Q_I(u)|^2
=\operatorname{Re}T_{\rm large}
+O_\epsilon\!\left(U^{K-1/6250+\epsilon}(1+T_1)^A\right).
\]

Here \(T_{\rm large}\) is the exact tuple-pair sum defined by manuscript
label `eq:Tlarge`: its rows lie in \(\mathcal C_+\), its plain ideals
satisfy \(k\ne k'\), and its moving ratio conductor satisfies
\(\mathrm Nf>U^{4/5}\). The open target is

\[
\operatorname{Re}T_{\rm large}
\le C_\epsilon U^{1+\delta m-1/5000+\epsilon}(1+T_1)^A.
\]

The complete retained sum is real by swap symmetry. The reduction already
controls its negative part by the smaller error. Thus a modulus bound for
the **whole sum** is equivalent at this target scale; taking absolute
values separately for each pair is a stronger request and can lose the
cancellation being sought.

Read the [mixed reduction](MIXED_MOMENT_REDUCTION_20261008.md),
[kernel and conductor calculation](MIXED_KERNEL_CONDUCTOR_REDUCTION_20261008.md),
and [localized payoff](LOCALIZED_JOINT_WITNESS_TARGET_20261008.md) for the
full statements. The manuscript contains the corrected one-sided wording.

## Ordered continuation

### 1. Settle the row-selector feasibility gate

This is a dependency refinement of the proposed divisor-first plan: test
how the exceptional-row restriction will be handled before building a long
transformed induction. The currently available transformed expression
comes from a complete smooth family. It does not automatically represent
the sharply restricted \(\mathcal C_+\) family.

Compare two precise routes:

- Preserve the actual row selector in a new weighted or restricted estimate.
- Enlarge the whole positive norm to a smooth complete family, then prove
  the resulting sufficient bound, including any extra rows it introduces.

For the enlargement route, first test principal-character and sixth-power
rows with every original coprimality mask. In the principal-twist test case
\(\nu=1\), rows \(u=a^6\) satisfy
\(\chi_n(a^6)=\mathbf1_{(a,n)=1}\). Untwisted nonnegative admissible plain
and prime profiles can retain principal main terms. The resulting demand
on the masked inverse Möbius sum must therefore be derived explicitly.
This tests a proposed uniform enlargement; it does not assert that the
actual fixed profiles have those main terms or that the original
restricted estimate is false.

**Deliverable:** a short selector-feasibility note defining the enlarged
family or retained weight, its profile and height uniformity, and the
precise positive inequality. Extract the sixth-power contribution without
duplicate unit parametrizations and write its exact weighted norm, of the
form

\[
\sum_a\Phi((\mathrm Na)^6/U)
|M_r^{(a)}|^2|S_m^{(a)}Q_I^{(a)}|^2,
\]

where the superscript retains every original coprimality mask. Evaluate the
plain and prime factors with their actual coefficients, including possible
cancellation or vanishing profile integrals, before assigning an exponent
budget against K. Distinguish the primitive row conductor from the ratio
conductor of two columns. Identify which available estimate meets the
budget, state the new estimate required, or explain why profile dependence
leaves this test inconclusive.

**Decision:** proceed with a complete-family transform only if the extra
rows are controlled or removed by a justified positive decomposition.
An unmet budget redirects work toward a selector-preserving estimate; it
is an obstruction to that proof route, not a disproof of the target.

### 2. Track the live plain divisor through the transform

On the squarefree, mutually coprime core, after separating the fixed ray
factor \(\nu(v)\), the coefficient is \(\mu_F(v)h(v)\). Source substitutions
\(v=tfn\) leave \(h(tfn)\), which depends on both an averaged label and the
residual ideal. In this paragraph f denotes the source's transformed label;
do not identify it silently with the ratio conductor in the target.

Where the required coprimality holds, split uniquely

\[
k=k_0k_1,\qquad k_0\mid tf,\qquad k_1\mid n,
\qquad\lambda=\log_U\mathrm Nk_1\in[0,m]
\]

at exponent scale, allowing the harmless annular endpoint constants.
Retain the Möbius signs and coupled plain-scale cutoff. Check the endpoint
strata first, especially \(\lambda\approx m\), where almost all plain
length remains in the residual ideal. Recompute the true support,
conductor, masks, coefficient dependence, and summation costs in each
stratum. A formal split does not restore the inverse-only width.

**Deliverable:** an exact transformed coefficient formula and a table of
lengths and proposed estimates by lambda range. Every claimed saving must
survive Cauchy steps, summation over strata, and the selector treatment
chosen in step 1. A formal calculation for the complete-family branch can
be studied separately, but must be labeled conditional on that branch.

**Decision:** develop a new estimate only where the arithmetic structure
yields an actual gain. If a surviving stratum retains the old deficit,
record it precisely instead of applying the old recursion outside its
coefficient class.

### 3. Prove a subcase, then recover application uniformity

Start with the surviving squarefree coprime subcase and fixed admissible
profiles. State a complete theorem with its exact hypotheses. Then handle
overlaps, prime powers, all required length ranges, original prime lists,
heights, and derivative profiles needed for rowwise parameter choices.

A positive saving on a genuine subcase is useful research progress. To
claim the proposed new boundary, however, the full required uniform saving
must reach 1/5000 with room for the prescribed small losses. A gain only at
a numerically identified bottleneck does not cover the continuous box.

**Deliverable:** either a proved partial theorem with a sharply stated
remaining class, or the full uniform estimate and a checked rerun of its
conditional two-rebalance payoff. Save exact arithmetic checks in
`numerics/`; finite experiments do not establish analytic cancellation.

### 4. Validate the inputs and consolidate the manuscript

Run this alongside the arithmetic research where possible. Seek specialist
review of the elementary ideal-pair count and the exact application
hypotheses of the imported reflection, moment, and contour results. A fresh
LLM critique is useful, but does not replace that validation.

Incorporate checked advances into the existing manuscript in place. Record
later meaningful Git commits or tags in [DRAFT_HISTOR.md](../DRAFT_HISTOR.md),
with links to the detailed notes and reviews. Do not create new manuscript
snapshot folders. This continuation note is a plan, not a new theorem or
commit milestone.

## Constraints that a continuation must preserve

The [transfer audit](../reviews/MARKED_MIXED_TRANSFER_AUDIT_20261008.md)
and manuscript explain the failed shortcuts:

- The source's Lemma 17.2 excludes the residual coefficient h(tfn).
  A divisor bound on h does not make that signed theorem applicable.
- Appending the plain factor adds 2m to the first dual-row width. At
  z = (1−r)/2−rho, the formal margins are 2rho−m and
  2r−1−2m+8rho. Their deficits are macroscopic; even deleting every prime
  slot leaves r+m ≥ 1.06 where the naive transfer requires r+m < 1.
- The sharp exceptional-row selector cannot be inserted into a Schwartz
  Poisson kernel or discarded term by term from a signed pair sum.
- When a column-ratio phase cancels modulo six, its zero support can
  survive. Keep the E-mask as well as the primitive conductor radical.
- Complete convolution μ*1 does not cancel a selected annular rectangle.
  Common height and exponent saturation do not establish phase alignment.

## Codex or ChatGPT?

**Use Codex in the local repository as the primary continuation workspace.**
The next deliverables couple source-level mathematics, exact exponent
checks, review records, and eventual edits to one LaTeX manuscript. Keeping
these together in the existing checkout gives the next session a concrete
record to inspect. Official documentation describes local Codex work as
operating directly in the project directory.
[OpenAI: Codex environments](https://learn.chatgpt.com/docs/environments/modes)
(accessed 8 October 2026).

**Use a fresh ChatGPT session as an optional focused critic.** Supply this
note, the manuscript, and the relevant source statements; ask it to attack
one specific claim, such as the selector enlargement or the lambda ≈ m
stratum. Ask for a counterexample or the earliest unsupported inference,
not a general endorsement. Bring any resulting argument back into the
repository and check it before adopting it.

This division is a workflow judgment, not a claim that either interface is
intrinsically better at mathematics. Current official guidance describes
Chat as suitable for discussion and idea development, Codex as exposing
technical and review tools, and substantial overlap between ChatGPT Work
and Codex. ChatGPT Work can also use code and repositories when its chosen
environment permits it.
[OpenAI: choosing Chat, Work, or Codex](https://learn.chatgpt.com/docs/use-chatgpt)
(accessed 8 October 2026).

Switching interfaces alone does not guarantee a different model or an
independent mathematical check. For the immediate next session, stay in
Codex and begin with the selector-feasibility note.

## Suggested next-session request

> Continue the quasi-RH character-amplification investigation from
> `notes/CONTINUATION_20261008.md`. Read the current manuscript and its
> review first. Begin with the row-selector feasibility gate: define the
> proposed positive enlargement, test principal and sixth-power rows with
> the actual profiles and masks, and compare the resulting inverse-sum
> requirement with the estimates we really have. Separate exact statements
> from diagnostic examples. Then, if that route is justified, track the
> plain divisor k = k0*k1 through h(tfn), testing the lambda ≈ m stratum
> first and keeping the genuine widths. If enlargement needs an unavailable
> input, state it and formulate the selector-preserving alternative. Save
> research in notes/, reproducible calculations in numerics/, and checks
> in reviews/, including model and effort metadata when known. Keep the
> current conditional candidate and the unproved target distinct. Do not
> promote a conjectural saving into the manuscript as a theorem.

Canonical investigation directory:
`papers/quasi-rh-character-amplification/` in the local
`shifted-zeta-positivity` repository. Follow the root
[LARGE_FILES policy](../../../LARGE_FILES.md). The synced ChatGPT project
`sources/` directory is read-only reference material.
