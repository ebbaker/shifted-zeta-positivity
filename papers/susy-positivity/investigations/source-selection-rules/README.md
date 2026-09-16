# Selection rules for a source of the localized Weil form

16 September 2026. A spin-off from
[inverse bulk realization](../inverse-bulk-realization/README.md). Its object is
not a construction. It collects the **necessary conditions** a candidate source
must satisfy, and the presentation of the target that makes them visible and
cheap to test.

It exists because the sibling investigation's exclusions are each of the form
"this particular preparation fails", while Theorem 7.5 there shows that every
term of the target can be matched exactly with no realization existing. What is
wanted instead are conditions that kill whole families before any arithmetic is
computed. Eight are collected in
[the selection rules](notes/SELECTION_RULES.md); four of them are new here.

## The two results the rules rest on

**The archimedean symbol is the smooth zero density.** From (2.6) and (2.7) of
the sibling manuscript, `b(tau^2) + w0 = Re psi(1/4 + i tau/2) - log pi = 2 theta'(tau)`,
so with `Nbar(T) = theta(T)/pi + 1`,

```
 K[E_L f] + w0 ||f||^2 = int_R |F^(tau)|^2 dNbar(tau).
```

The contact constant is not an independent object requiring a mechanism: it is
the `-log pi` inside `theta'`. All archimedean negativity is confined to
`|tau| < tau_L`, a band that shrinks with `L` and is empty above `log 13` — and
the crossing at `p = 13` is exactly where the summed prime contacts overtake the
maximum negativity of the smooth zero density. See
[the density-symbol note](notes/DENSITY_SYMBOL_AND_SYMBOL_SPLIT_20260916.md).

**The elementary Schur algebra carries no arithmetic parameter.** The
representation of Section 6.1 of the sibling manuscript is the generalized
`q`-Weyl algebra with `P(y) = 1 + y`; by Klyuev its twisted-trace space is one
dimensional. So the prime data of Section 6 lives entirely in the chosen
dressing state, which Section 6.5 shows is unconstrained. Non-constructive
existence of a realization is exactly RH and cannot be shortcut; what is
available is rigidity, family exclusion, and finite-moment determination, none
of which the current construction is in a position to use. See
[the q-Weyl note](notes/QWEYL_TRACE_SPACE_20260916.md).

**How far the domination is from failing.** Weil positivity on $I_L$ is
$T_L \preceq K_+$, and the margin $\lambda_{\min}(Q_L;K_+)$ collapses
superexponentially: below $10^{-9}$ at $L=1$, $10^{-17}$ at $L=2$, $10^{-24}$ at
$L=3$. Measured in a smooth basis with $Q_L$ assembled from its spectral form, so
that the eight-order cancellation in (2.9) never occurs. Consequently any
argument — fixed point or otherwise — whose hypotheses supply a margin uniform in
$L$ is proving something false. See
[the fixed-point note](notes/FIXED_POINTS_AND_THE_MARGIN_20260916.md).

## Reading map

| Document | Role |
|---|---|
| [Selection rules](notes/SELECTION_RULES.md) | The living index: eight necessary conditions, ordered by cost, and the rules that were dropped. |
| [Density symbol and symbol split](notes/DENSITY_SYMBOL_AND_SYMBOL_SPLIT_20260916.md) | The density identity, its four consequences, and a sharper presentation of the compression. |
| [q-Weyl trace space](notes/QWEYL_TRACE_SPACE_20260916.md) | What non-constructive arguments can give; the algebra identification; a retraction. |
| [Fixed points and the margin](notes/FIXED_POINTS_AND_THE_MARGIN_20260916.md) | Why this is a membership question, not an existence question; what each family of fixed point theorem would need and which are blocked; and how small the margin really is. |
| [Continuation note](notes/CONTINUATION_20260916.md) | State, ordered next steps, what not to redo, conventions. |
| [Notes index](notes/README.md) | Navigation and reading order. |
| [Checks and records](numerics/README.md) | Three reproducible programmes and their explicitly scoped results. |
| [Reviews](reviews/README.md) | Dated assessments. None yet. |

## What is claimed and what is not

Everything here is a necessary condition or a re-presentation of the target. No
source is constructed, no positivity is proved, and nothing said here bears on
whether a realization exists. The saturation quotients in the checks are
one-sided subspace values: above one they would certify that a domination fails,
below one they certify nothing.

## Reproduction

Run from this directory:

```sh
python3 numerics/check_density_symbol.py
python3 numerics/check_symbol_split.py
python3 numerics/check_qweyl_relations.py
python3 validation/drafts.py check --replay
```

The programmes print small records and do not overwrite the preserved results in
`numerics/records/`. Follow the repository's
[large-file policy](../../../../LARGE_FILES.md).

Related material: [inverse bulk realization](../inverse-bulk-realization/README.md),
the [brainstorm notes this grew from](../../brainstorm/inverse-bulk-brainstorm/),
and the [program overview](../../PROGRAM_OVERVIEW.md).
