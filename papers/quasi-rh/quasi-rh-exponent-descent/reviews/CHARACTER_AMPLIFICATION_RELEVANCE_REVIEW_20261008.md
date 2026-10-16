# Review: character amplification and the exponent-descent continuation

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is a scoped same-model review, not independent specialist refereeing.

## Scope and conclusion

The user requested a detailed review of the relevance of
papers/quasi-rh-character-amplification/, followed by a broad continuation
note for Codex. The resulting
[continuation](../notes/CODEX_CONTINUATION_20261008.md)
integrates three parallel audits: the latest selector-preserving arithmetic,
family and common-signal transfer, and geometry/parameter dependence.
It also consults the current prime-variance and height-adapted reductions.

**Relevant mechanisms exist, but none currently closes a quasi-RH-to-RH
argument.** The nearest mixed estimate is precisely localized. The
short-family transfer has a genuine conditional exponent contraction.
Neither is supplied by the presently imported estimates. The existing
geometry also has limitations that prevent an unchanged iteration to RH.

The review did not re-prove the source's deep reflection/moment machinery,
validate its seven-eighths theorem independently, or replay Lean.
The source's scope statement was checked as a statement of claimed scope.
The current local boundary \(7/8-1/24000\) is a conditional candidate;
the target \(7/8-1/20000\) additionally requires a new mixed estimate.
No new zero-free result is asserted.

## Records reviewed and what transfers

Paths in the following table refer to the neighboring amplification project.
Its [overview](../../quasi-rh-character-amplification/README.md) links all
the named records and their existing reviews.

| Records | Relevant content | Limit on reuse |
| --- | --- | --- |
| Current manuscript; SELECTOR_PRESERVING_PLAIN_CONDUCTOR; SELECTOR_PRESERVING_SUBCASES; SELECTOR_ENERGY_LOCALIZATION | Exact remaining signed sum, three distinct conductors, local masks, positive deletion order, proved strips, and buffered application triangle | The remaining mixed saving is open; the triangle is not itself an analytic saving |
| MIXED_MOMENT_REDUCTION; MIXED_KERNEL_CONDUCTOR_REDUCTION; SATURATED_MIXED_ARITHMETIC | Earlier diagonal, row-conductor, and total-ratio removals | The newest two-ratio target supersedes the older \(U^{4/5}\) target |
| JOINT_WITNESS_REDUCTION; AMPLITUDE_PROFILE_REDUCTION | Simultaneous inverse/plain witnesses, capped identities, whole-slot choices, two rebalances | Shared zeros and heights do not yield phase independence or compatible selected rectangles for free |
| CHARACTER_FAMILY_TRANSFER | Sextic replicated rows, omitted-prime recurrence, scale-uniform completion | Short row ranges are new hypotheses; source estimates in \(h>1\) cannot be shortened by restricting the sum |
| COMMON_SIGNAL_PROBE_SCOUT | Full signal normalization and actual signed mixed kernel | Unknown Gram minimization is not an estimate; fixed filters do not remove every possible coherent mode |
| GEOMETRY_OPTIMIZATION; OFF_BALANCE_GEOMETRY_SCOUT; PARAMETER_EXTENSION | Current candidate, high-bin obstruction, low envelope, dual-length and Euler-domain costs | Replacing the global boundary does not extend the moment parameter range or remove the interior obstruction |
| SELECTOR_FEASIBILITY; LIVE_DIVISOR_TRANSFORM; structural and transfer reviews | Added principal rows, residual divisor coefficient, actual canonical widths | Complete-family enlargement and source-theorem import still require new estimates |

The existing audits were used to check the actual coefficient class,
physical prime profiles, allowed derivative families, and order of choices.
The new note deliberately avoids repeating the completed selector and
live-divisor scouts as though they had not been attempted.

The prime-variance checks used this project's four opening research notes,
the original program overviews, and the newer Gaussian/cofactor-aware and
carrier-centered height-adapted records. The resulting portfolio includes
fixed-scale covariance, family amplification, common-signal combinations,
all-height detection, collision exclusion, and the earlier alternative
positivity/approximation programs.

## New deductions checked for the handoff

### Refined removable conductors

The original total-ratio deletion uses the full-bin count \(R_0\).
Replacing it by the available sharper \(R^*\le R_0\) gives

\[
\tau_*=2(1+dm-\eta-\gamma-R^*)
=\tau_0+2(R_0-R^*).
\]

Its removed cost remains \(R^*+\tau_*/2=1+dm-\eta-\gamma\).
For a tapered saving \(s\), the analogous choices are
\(v_{\rm pl}=2dm-2(s+\gamma)\) and
\(\tau_*=2(1+dm-s-\gamma-R^*)\).
The low-row contribution fits for \(0<s\le\eta\), since
\(d/1000-s\ge\gamma\) on the hard box.
Outside the ideal triangle the actual amplitude/witness loss must be used;
a positive reserve exists only when the required \(s<d/1000\).
This removes an additional affordable block without estimating the complement.

### Conditional short-family map

Given the new family mean square and the prior smoothed inverse bound,
the two output exponents are
\((1+a)/2+5h/12\) and \(\theta(1-h/6)\).
Their crossing is

\[
h_*=\frac{6(2\theta-1-a)}{5+2\theta},\qquad
T_a(\theta)=\frac{\theta(6+a)}{5+2\theta}.
\]

For \(e=\theta-1/2>0\),
\[
T_a(\theta)-1/2=\frac{5e+a(e+1/2)}{6+2e}.
\]
If \(0\le a\le2\lambda e\), \(0\le\lambda<1\), the excess is at most
\((5+\lambda)e/6\). At the maximal loss \(a=2\lambda e\),
the difference between that bound and the exact excess is
\[
\frac{5e^2(1-\lambda)}{3(6+2e)}\ge0.
\]
The \(a=0,\theta=7/8\) step gives \(h_*=2/3\), \(T_0=7/9\).
Fixed positive \(a\) instead leaves the fixed point \((1+a)/2\).
These algebraic conclusions do not establish the new family mean square.

The conditional proposition now requires a profile class with no common
Mellin zero in \(\Re s>1/2\), not merely a class that separates points.
It states the epsilon and per-stage quantifiers. Its initial bound is for
the same Hecke function. Zeta-only quasi-RH does not supply that bound for
the trivial ideal character, because
\(\zeta_K=\zeta L(s,\chi_{-3})\) includes a companion factor.
Trivial counting starts the conditional chain at exponent one if all
the stronger family inputs are available.

### Geometry and low-envelope synthesis

The balanced low expression minimizes algebraically at \(13/15\).
The combined signed-imbalance expression in the continuation has the same
infimum, by its two explicit minimizing branches. It is labeled an
algebraic synthesis: a full new analytic domain has not been validated.
The formal \(\kappa\)-dependent capacity/count formulas specialize to the
current formulas at \(3/4\), but do not extend the source theorem.
The existing contour range and the later change of crossing regime are
stated explicitly.

### Direct replication criterion

The Hilbert-space inequality follows from the triangle inequality in
the direct sum of the row spaces. Smallness of both averaged energies
is a sufficient criterion. It is not presented as a necessary condition
for every possible cancellation argument. No arithmetic lift of the
complete integer prime response has been proved.

## Corrections made during scoped review

Three agents reviewed assigned sections of the draft. Their findings
were incorporated before saving:

- The Gram convention was reversed so that \(c^*Gc\) is the energy of
  \(\sum c_jR_j\) for complex coefficients. The unweighted conclusion now
  uses an unweighted Gram; the weighted version states a total-weight
  hypothesis and concludes weighted \(L^1\).
- The profile hypothesis now excludes common Mellin zeros explicitly;
  \(\theta_0>1/2\) and fixed \(0\le\lambda<1\) are stated.
- The buffered conductor refinement uses the actual profile saving and
  requires a positive remaining low-row reserve.
- The two detector cutoffs are distinguished from selected inverse lengths.
  Each has its own \(-1+o(1)\) formula; exact equality between detectors
  is not claimed. Shared smoothing, terminal weights, and product caps
  are retained.
- The family supremum is explicitly over all primitive finite-order
  Hecke functions over \(\mathbb Q(\sqrt{-3})\), not just the sextic row family.

The reviewers otherwise found the latest residual masks, deletion order,
fixed-delay formulas, geometry qualifications, and Newman interpretation
consistent with the inspected records. This is a scoped correctness
assessment of the continuation, not validation of every external theorem
or every local project claim.

The final package is a research handoff, not a manuscript or proof of RH.
No numerical experiment here establishes an asymptotic arithmetic estimate.
Detailed future work belongs in notes, reproducible calculations in numerics,
and scoped reviews here; milestone history remains concise.
