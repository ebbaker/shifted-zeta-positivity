# Selection rules for a source of the localized Weil form

16 September 2026. A spin-off from
[inverse bulk realization](../inverse-bulk-realization/README.md). Its object is
not a construction. It asks what the localized Weil form *is*, and collects the
necessary conditions any source for it must satisfy.

It exists because the companion investigation's exclusions are each of the form
"this particular preparation fails", while its Theorem 7.5 shows that every term
of the target can be matched exactly with no source existing. What is wanted
instead are conditions that exclude whole families before any arithmetic is
computed.

The [working manuscript](manuscript.pdf), *A jump-process presentation of the
localized Weil form*, collects the results in a self-contained draft. Its
[TeX source](manuscript.tex) inputs no shared background; it cites the companion
manuscript for the program's objective and for results quoted by number.
Reviewed versions are preserved in [drafts/](drafts/README.md). See the
[build guide](BUILD.md).

## The results

**The archimedean symbol is the smooth zero density.**
$b(\tau^2)+w_0=\re\psi(\tfrac14+i\tau/2)-\log\pi=2\theta'(\tau)$, so the
archimedean energy together with the contact is integration against
$\bar N=\theta/\pi+1$. The contact constant is not an independent object
requiring a mechanism: it is the $-\log\pi$ inside $\theta'$. All archimedean
negativity sits below $\tau_*=6.2898$, and once the prime contacts join, in a
band that shrinks with $L$ and is empty above $\log 13$ --- the crossing at
$p=13$ being exactly where the summed contacts overtake $-w_0$.

**The target is one jump form.** Adding and subtracting the prime symbol's value
at the origin puts everything but the pole term in Lévy--Khinchine form: the
archimedean density and the prime atoms are the continuous and atomic parts of
one nonnegative measure $\mu_L$, and a source is a jump process whose jumps are
the primes. This is what Theorem 7.5 of the companion manuscript asks for --- one
mechanism, not two channels.

**A Perron--Frobenius structure, broken by the poles.** The jump form's
resolvent is positivity preserving, as Beurling--Deny requires; the rank-two pole
form destroys that at every $L$, by Sherman--Morrison, even in its positive half.
Krein--Rutman adds nothing to the spectral theorem here, Birkhoff bounds a gap
and never a radius, and Collatz--Wielandt --- the one cone theorem that bounds
what must be bounded --- needs the pointwise supersolution the pole removes.

**A necessary condition.** With $S_L$ the pole-free part and
$\alpha_L=-\lambda_{\min}(S_L)$ a Perron-root deficit of an explicitly
nonnegative kernel: if $Q_L\ge0$ on $I_L$ then $\alpha_L\le 2\sinh(L/2)+L$.
A single positive trial function bounds $\alpha_L$ from below, so a trial
function violating the condition would show that the Riemann hypothesis fails.
A scan of 7713 intervals finds no violation; the least relative margin is
$9.5\times10^{-4}$.

**Nine selection rules**, four of them new here, in Section 8 of the manuscript.

## Reading map

| Document | Role |
|---|---|
| [Working manuscript](manuscript.pdf) | The consolidated results, self-contained. |
| [Dated drafts](drafts/README.md) | Complete buildable snapshots with hashes. |
| [Open directions](notes/OPEN_DIRECTIONS_20260916.md) | Everything opened and not finished, ranked, with what is closed and why. |
| [Density symbol and symbol split](notes/DENSITY_SYMBOL_AND_SYMBOL_SPLIT_20260916.md) | Research note behind Sections 3 and 5. |
| [Perron--Frobenius and the jump form](notes/PERRON_FROBENIUS_AND_THE_JUMP_FORM_20260916.md) | Research note behind Sections 4 and 6. |
| [Collatz--Wielandt](notes/COLLATZ_WIELANDT_20260916.md) | Research note behind Section 7, including the disproof test as run. |
| [Fixed points and the margin](notes/FIXED_POINTS_AND_THE_MARGIN_20260916.md) | What each family of fixed point theorem needs, and how small the margin is. |
| [Existence mechanism sweep](notes/EXISTENCE_MECHANISM_SWEEP_20260916.md) | Literature survey: what transports positivity and what manufactures it. |
| [q-Weyl trace space](notes/QWEYL_TRACE_SPACE_20260916.md) | The algebra identification, and a retraction. |
| [Selection rules](notes/SELECTION_RULES.md) | The living index of necessary conditions. |
| [Continuation note](notes/CONTINUATION_20260916.md) | Handoff. |
| [Checks and records](numerics/README.md) | Five reproducible programs and their scoped results. |
| [Reviews](reviews/README.md) | Dated assessments. None yet. |

## What is claimed and what is not

Everything here is a necessary condition or a re-presentation of the target. No
source is constructed, no positivity is proved, and no statement assumes the
Riemann hypothesis. The saturation quotients are one-sided: above one they
would certify that a domination fails, below one they certify nothing. The
Galerkin values of $\alpha_L$ run the other way, which is what makes the
disproof test a test.

## Reproduction

```sh
python3 numerics/check_density_symbol.py
python3 numerics/check_symbol_split.py
python3 numerics/check_qweyl_relations.py
python3 numerics/check_levy_dirichlet.py
python3 numerics/check_collatz_wielandt.py
python3 validation/drafts.py check --replay
```

Three computations quoted in the manuscript are deliberately outside these
programs and are labelled where they appear; porting two of them is item A4 of
the [open directions](notes/OPEN_DIRECTIONS_20260916.md). Follow the
repository's [large-file policy](../../../../../LARGE_FILES.md).

Related: [inverse bulk realization](../inverse-bulk-realization/README.md), the
[brainstorm notes this grew from](../../../brainstorm/inverse-bulk-brainstorm/),
and the [program overview](../../../PROGRAM_OVERVIEW.md).
