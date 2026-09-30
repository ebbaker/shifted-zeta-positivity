# Arithmetic-storage project summary

**Status: 29 September 2026, direct positive approximation is the active priority.**
Prepared for Edward Baker with substantial LLM assistance. Model: GPT-6
(Codex); exact serving variant and configured reasoning effort not exposed.
This summary distinguishes research-note derivations and internal interval
certificates from specialist review, which remains outstanding. It is the
current entry point; detailed history and proofs remain in the linked notes.

## Objective and current position

The active goal is to construct a specified family of independently positive
forms converging to the complete arithmetic Weil form on every fixed compact
smooth pole-neutral source:

\[
P_j[F]\ge0,\qquad P_j[F]\longrightarrow Q[F].
\]

The source class ranges over arbitrarily large supports. Positivity must come
from the construction; identifying the arithmetic limit is a separate theorem.
Finite-stage domination, monotonicity, a uniform positive gap, and whole-line
operator-norm convergence are not prerequisites.

The Sonin route already has an audited comparison formula, actual
infinite-dimensional projections with certified numerical tools, scalar
smoothed traces, and a first compressed metric moment for two sources.
The direct-limit analysis below adds a regularized positive baseline and
identifies why the final limit must allow spectral concentration. No
arithmetically identified global positive limit, all-support positivity
theorem, first-prime storage mechanism, or RH proof has been obtained.

The [direct positive-limit program](notes/SONIN_DIRECT_POSITIVE_LIMIT_PROGRAM_20260929.md)
is the active research plan. The [original program and goals](notes/ARITHMETIC_STORAGE_PROGRAM_AND_GOALS_20260924.md)
remain the broader context.

## Active plan and first limit results

The first candidate is the independently positive family

\[
P_R[F]=\mathcal B_{S_R}[F]=\|C_F\Pi_{S_R}\|_{\rm HS}^2,
\qquad S_R=\{\infty\}\cup\{p:p\le R\},
\]

using the actual transported Sonin projection and inverse compressed metric.
For a fixed pole-neutral source, every active prime power must be retained,
and the exact discrepancy is

\[
P_R[F]-Q[F]=\mathcal E_\infty[F]+\Delta_{S_R}[F]+\mathcal W[F].
\]

The finite arithmetic sum W[F] stops changing once all active primes are
included, while the geometric trace can continue changing. The required
identification is Delta_(S_R)[F] -> -E_infinity[F]-W[F]. Convergence to an
unidentified positive form would not suffice. Increasing numerical resolution
at fixed R only approximates P_R; it does not establish the arithmetic limit.

**The odd-source domination bound is not a gate for this program.** A
convergent positive family may lie above Q at finite stages. The odd source
and earlier moment bounds remain calibration tools, to be used only when
they discriminate a specified asymptotic mechanism. Further precision or a
higher moment is not the default next task.

The first direct-limit investigation establishes the following internal
analytic results:

- For every fixed sigma>1, replacing p^(-1/2) by p^(-sigma) gives an
  unconditional infinite-place positive form, with quantitative convergence
  after source smoothing. This is a controlled baseline, not the critical
  arithmetic limit.
- A bounded phase continuation defines intersection projections Pi_sigma
  even where bounded inverse-Euler transport is unavailable. The functional
  equation gives Pi_sigma -> 0 strongly as sigma decreases to 1/2. Smoothed
  traces need not tend to zero; spectral concentration may survive.
- The source-independent finite-rank forms
  P_(sigma,N)[F]=||C_F Pi_sigma E_N||_HS^2 are always finite and positive.
  For fixed N they tend to zero at the endpoint. A nonzero arithmetic limit
  requires a justified coupled growth N=N(sigma)->infinity. No such schedule
  or arithmetic identification is proved yet.
- A single fixed bounded compression on ordinary logarithmic L2 cannot
  realize Q on the full all-support pole-neutral class. The frequency measure
  of a fixed compression is absolutely continuous, whereas equality would
  imply RH and the atomic arithmetic sampling measure. This excludes an
  overly strong endpoint requirement, not singular limits of positive forms.
- For the raw prime-cutoff family, new moving-tail and signed-covariance
  criteria give sufficient conditions for convergence. Their hypotheses
  along the growing family, and the arithmetic value of the limit, remain
  unproved.

The phase continuation and the raw critical prime-cutoff sequence are
separate candidates; their limits have not been shown equivalent. For
1/2<sigma<=1, finiteness of the full phase-family smoothed trace is also
open here. Finite-rank forms avoid assuming that finiteness.

See the [regularized family](notes/SONIN_REGULARIZED_POSITIVE_FAMILY_20260929.md),
[topology and fixed-compression analysis](notes/SONIN_POSITIVE_LIMIT_TOPOLOGY_20260929.md),
[moving-tail criteria](notes/SONIN_DIRECT_PLACE_TAIL_CRITERIA_20260929.md), and
[internal review](reviews/SONIN_DIRECT_LIMIT_REVIEW_20260929.md).

## Latest numerical calculation

For the same normalized, smooth, pole-neutral even and odd sources at `L=1`,
the first source-weighted compressed metric moment has now been certified:

\[
m_1=\operatorname{Tr}(AH)=\mathcal B_\infty[D_2^2F]-\mathcal C[F],
\quad A=\Pi D_2^*D_2\Pi|_{\operatorname{Ran}\Pi}.
\]

The correction is reduced to compact boundary integrals containing the
actual Sonin projection. The certified polynomial resolvent covers the
infinite complement; source interpolation, cosine truncation, and arithmetic
errors are separately enclosed. This supplies projection information that
the earlier scalar trace did not contain.

| Quantity | Even `f0` | Odd `f1` |
|---|---:|---:|
| First compressed moment `m1` | `[3.75661571, 3.76549116]` | `[2.65433908, 2.66382398]` |
| First-prime trace `B2` | `[1.03644381, 8.67999475]` | `[0.79696516, 6.86726714]` |
| Direct arithmetic form `Q1` | `[1.439237951, 1.439237964]` | `[1.047808580, 1.047808594]` |
| Complete residual `Q1-B2` | `[-7.24075680, 0.40279415]` | `[-5.81945856, 0.25084343]` |

The positive spectral measure with mass `h0` and first moment `m1` gives
`h0^2/m1 <= B2 <= 12h0-4m1`. The trace interval widths fall by about 66%
and 63%, respectively. Both residual signs remain unresolved.

There is also a proved limit to this particular calculation: even exact
mass and first moment, without further information about the measure,
allow inverse moments on both sides of the direct arithmetic value. More
digits in those two quantities alone cannot settle the sign. This is a
limitation of the available information, not a Sonin counterexample.

The structural companion identifies two requirements for a finite Mellin
penalty: residual positivity on the constrained subspace and bounded cross
terms in its residual seminorm. Neither is established for the Sonin
residual here. These are requirements of the stronger full finite-penalty
inequality; direct positivity on a fixed permissible moment-zero class would
not additionally need cross-term control for the restricted criterion. The
odd source is exactly mean-zero and can test a mean-only defect hypothesis,
but that alternative is not a prerequisite for the active convergence route.

See the [first-moment derivation](notes/SONIN_COMPACT_FIRST_MOMENT_20260929.md),
[finite Mellin-defect gate](notes/SONIN_FINITE_MELLIN_DEFECT_20260929.md),
[internal review](reviews/SONIN_FIRST_MOMENT_REVIEW_20260929.md), and
[combined interval record](numerics/records/sonin_first_moment_bounds.json).

## Earlier scalar calibration

For the fixed compact smooth, normalized, pole-neutral sources `f0,f1` at
`L=1`, the actual cutoff-1 Sonin trace obeys

\[
\mathcal B_\infty[H]=\Gamma[H]+\mathcal E_\infty[H]
=\|C_H\Pi\|_{\rm HS}^2.
\]

With `D2=I-2^(-1/2) U_log(2)`, the newly certified outward intervals are:

| Source | `B_infinity[F]` | `h0=B_infinity[D2 F]` |
|---|---:|---:|
| Even `f0` | `[1.13835123, 1.13835393]` | `[1.97553031, 1.97553814]` |
| Odd `f1` | `[1.19636220, 1.19636522]` | `[1.45704321, 1.45705196]` |

Every interval has width below `10^-5`. The full gamma/contact terms were
enclosed through an Arb FFT with analytic bounds for source sampling,
frequency discretization, and the infinite frequency tail. The Sonin epsilon
correction was integrated using the certified polynomial resolvent and exact
spline-correlation formulas, with source interpolation and all operator tails
bounded. Agreement between runs was used as a check, never as the error bound.

The epsilon contributions are negative for all four inputs, approximately
`-0.10999`, `-0.18414`, `-0.14145`, and `-0.13477` for
`f0,D2f0,f1,D2f1`, respectively. This does not imply a negative arithmetic
residual. The sum with gamma is the positive trace above. Cancellation is
manageable here; source interpolation dominates the final numerical width.

This also resolves the scale of the previous trial-space failure. For the
actual Sonin space generated by degrees 20 and 24, the captured fraction of
the first-prime positive trace is **below 1.090% for `f0` and 2.422% for `f1`**.
The omitted positive trace is greater than **0.67382** and **0.49172**,
respectively. These improve the earlier one-direction witness. Increasing
arithmetic precision cannot make that fixed space capture the missing trace.

The transformed scalar `h0` is **not** the semilocal trace `B2`: the latter
contains an inverse compressed metric. At this scalar-only stage, the
rigorous `B2` bounds were approximately `[0.68124,22.89784]` and
`[0.50392,16.71659]`; the first-moment bounds above supersede them.
No complete arithmetic residual has been assigned a sign.
See the [scalar calculation and error proof](notes/SONIN_SCALAR_TRACE_CALCULATION_20260929.md),
[review](reviews/SONIN_SCALAR_TRACE_REVIEW_20260929.md), and
[small reproducible records](numerics/records/sonin_scalar_summary.json).

## Results retained from the preceding stages

**Finite joins and their limitation.** The inherited prime-free append has
an internally certified all-input relative coupling below `0.951`.
The first-prime joined window of length `3/4` is also internally closed:
`Q_(0,3/4) >= (123/250000)I`, central coupling below `0.99980037`, and
cumulative normalized coupling below `0.99981859` at shift `10^-3`.
These establish particular finite-window benchmarks. The append hypothesis
itself is equivalent, under the stated coercivity/domain assumptions, to
positivity on the joined window; it does not supply a new inductive mechanism.
A chain with join lengths bounded below cannot retain a fixed positive
margin. Shrinking joins remain open. See
[join equivalence and prime rigidity](notes/FIRST_PRIME_JOIN_EQUIVALENCE_AND_PRIME_WEIGHT_RIGIDITY_20260924.md)
and the [first-prime review](reviews/review_claude_first_prime_session_20260924.md).

**Arithmetic cancellation and model constraints.** The prime-free gamma/pole
form changes sign between tested supports `0.74` and `0.745`; the prime
contribution becomes indispensable. At `log 3`, the tested prime-2 weight
perturbations force a very narrow permitted range, roughly `-8.18e-5` to
`+3.16e-6` relative; these are exclusion bounds, not an exact classification
of admissible weights. A certified witness also rejects the inherited
128-mode instantaneous-energy lower-bound device. It does not reject the
complete Weil form. Any proposed mechanism must preserve the full arithmetic
cancellation. See the
[first-prime analysis](notes/FIRST_PRIME_CONTINUATION_ANALYSIS_20260924.md).

**Canonical Sonin comparison.** The local audit fixes normalization, full
contact and poles, source preparation, transport direction, actual projection,
and inverse compressed metric. It proves compressed trace-class identities
and separately proves the stronger smooth trace assertion. For finite `S`,

\[
Q_L=\mathcal B_S+\mathcal R_{S,L},\qquad
\mathcal R_{S,L}=P_L^{\rm pole}-\mathcal E_\infty-\Delta_S-\mathcal W_L.
\]

The sum `W_L` must retain every active prime power. The pole-neutral source
class is sufficient only with all-support quantifiers; one parity or a finite
family at `L=1` does not suffice. See the
[canonical comparison audit](notes/SONIN_CANONICAL_COMPARISON_AUDIT_20260929.md).

**Signed place addition and return control.** The exact place-addition law
exposes a signed translation covariance and retains the changing compressed
metric. Its sign does not follow from positivity of the local factors.
Chebyshev return expansions have explicit, faster truncation bounds. The
first source-weighted compressed metric moment above is now certified;
the signed return quantities in that earlier expansion remain unevaluated.
Complete and partial arithmetic residuals must remain distinct. See
[place addition and error control](notes/SONIN_PLACE_ADDITION_AND_ERROR_CONTROL_20260929.md).

**Actual projection and numerical foundations.** The cosine cutoff obeys
`I-C² >= (57/10^6)I`. A polynomial inverse covers the whole infinite-dimensional
complement with operator error below `9.2e-32`; its smoothed trace-norm error
is below `2.7e-31`. Exact source normalizations and derivatives have certified
endpoint tails. Globally controlled actual Sonin trial vectors and finite
Galerkin matrices are available. These tools survive rejection of the selected
trial space. See the
[projection enclosure analysis](notes/SONIN_ACTUAL_PROJECTION_ENCLOSURES_20260929.md),
[prolate certificate](notes/SONIN_PROLATE_RESOLVENT_CERTIFICATE_20260929.md), and
[source certificate](notes/SONIN_SOURCE_NORM_CERTIFICATES_20260929.md).

## Next work and decision criteria

1. Derive a usable representation of the positive frequency measure or
   source-smoothed discrepancy of a specified candidate family. The central
   question is how the positive measure concentrates and why its action on
   each prepared source should approach the arithmetic expression.
2. Prove arithmetic identification with an error tending to zero on each
   fixed source, preserving contact, poles or their exact preparation, and
   every active prime power. A local distributional limit on prepared
   correlation tests is sufficient. Defining a positive measure from assumed
   real zeta zeros, or merely proving convergence to an unknown form, is not
   an independent construction.
3. Establish the required tails and parameter schedule. For the phase family,
   resolution must grow as regularization is removed; fixed resolution gives
   zero. For the raw place family, investigate the new moving-tail or signed
   covariance estimates without discarding the cancellations they retain.
   Uniform state-space trace compactness forcing a fixed final compression
   is not an appropriate requirement.
4. Choose numerical experiments only after specifying the asymptotic statement
   they can test. Reuse the existing even/odd sources and projection tools for
   calibration. A finite-stage residual sign is optional evidence about a
   particular stronger comparison, not evidence of convergence by itself.

An analytic convergence theorem on a dense prepared-source class, including
linear combinations, would already imply positivity everywhere by the known
fixed-support continuity of Q. Upgrading convergence of the approximants
itself from a dense class to every source needs additional control. Finitely
many numerical tests establish neither statement.

A meaningful next milestone is a concentrating positive family with a
controlled arithmetic discrepancy on a nontrivial source class. If a proposed
family has the wrong limit or an unmanageable domain, revise that family or
its cutoff; do not replace the task with repeated finite domination tests.
Further finite-append certificates, unstructured trial-space enlargement,
and additional digits in the current mass and first moment remain lower
priority. CCM remains temporarily closed; completed finite Weil certificates
are preserved. Physical or canonical-system interpretations should contribute
an unconditional construction or estimate to this same limit question.

Research details belong in `notes/`, reproducible small code and records in
`numerics/`, and audits in `reviews/`. Large generated arrays remain outside
Git under the repository's large-files policy. This continuation creates no
manuscript snapshot, commit, or push.
