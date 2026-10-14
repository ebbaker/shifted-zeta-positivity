# Recommended closures, merges and pauses for the active portfolio

## Implemented status and qualifications

13 October 2026. Prepared for Edward Baker with substantial LLM assistance
by `gpt-6-astra` (Codex), reasoning effort **ultra**.
The proposal below is historical. Edward Baker authorized the qualified
[closure review](../brainstorm/reviews/PORTFOLIO_CLOSURE_REVIEW_CODEX_20261013.md),
now implemented in the [current index](README.md) and
[consolidation record](../PORTFOLIO_CONSOLIDATION_20261013.md).

The nine folders have moved to `inactive/`: 04/10/11 under 06, 07/15 under
18, 09 as a distinct completed identity task, 14/16 as dormant proposals,
and 17 as a completed easy-cell calibration. 01/02 are paused at their
explicit gates. The full-gluing gap in 02 is not proved equivalent to
18's Hecke formulation; 09's folded endpoint and obstruction results remain
distinct. Dormancy of 14/16 is not a mathematical exclusion. 17's easy-cell
cost result does not decide the hard-cell question.

The finite-prime control obstruction applies only when the other hypotheses
are also shared by the controls. The table and formal expansion in 19 now
refer to the lowest-pair time `T_0`, with global `Lambda` identification
conditional; the raw witness margin shrinks near an isolated collision.
These corrections supersede broader or ambiguous wording in the proposal.

## Original recommendation

13 October 2026. Prepared for Edward Baker with LLM assistance.
Model: Claude Opus 5.5 (configured identifier `claude-opus-5-5`; the serving
model may differ), Claude Cowork, reasoning effort **max**.

This note gives recommendations only. No folder has been moved, renamed,
closed or deleted. If you accept them, the
[inactive](../inactive/README.md) index is the natural place for closed
folders, each with a one-line pointer to its principal home.

**Inputs.** The [Claude review](../brainstorm/reviews/REVIEW_OF_ACTIVE_LIFTED_THETA_DIRECTIONS_CLAUDE_20261013.md);
the [Codex first research pass](../brainstorm/reviews/PRIORITY_RESEARCH_FIRST_PASS_CODEX_20261013.md)
(`gpt-6-astra`), which arrived with the same pull and completed bounded
tasks in 01, 02 and 17; and the first work in the two new folders,
[18](18_rank_two_automorphic_lift/README.md) and
[19](19_euler_factor_controls/README.md).

## Summary

| Folder | Recommendation | Principal home after the change |
| --- | --- | --- |
| 01 Complete cutoff reflection | **Pause at its gate** | 01 |
| 02 Angular Jacobi gluing | **Pause at its gate**; next identity work moves to 18 | 02 |
| 03 Anchored source observability | Keep as destination only | 03 |
| 04 Chord nonlocal closure | **Merge** as a chart of 06; close as a project | 06 |
| 05 Metaplectic coordinate atlas | Keep as a tool, built on demand | 05 |
| 06 Paired kernel factorization | Keep as destination; receives the rank-two form | 06 |
| 07 Divisor product transport | **Merge** into 18; close as a project | 18 |
| 08 Cusp unit sector saving | Keep as a separate arithmetic track | 08 |
| 09 Rank two theta addition | **Merge** into 18; close as a project | 18 |
| 10 Gaussian Hermite correlations | **Merge** as a chart of 06; close as a project | 06 |
| 11 Stein and SUSY correlations | **Merge** as a chart of 06; close as a project | 06 |
| 12 Canonical boundary reflection | Keep as reading and bridge; add W2 | 12 |
| 13 Stability, Jensen, Lee–Yang | Keep as reading only | 13 |
| 14 Theta Volterra integrability | **Close** | none |
| 15 Adelic and automorphic compatibility | **Merge** into 18; close as a project | 18 |
| 16 Radial geometry and sine moments | **Close** | none |
| 17 Spacetime collision degree | **Close as a completed benchmark** | 17 (records kept) |
| 18 Rank two automorphic lift | **New, active** | 18 |
| 19 Euler-factor controls | **New, active shared screen** | 19 |

After these changes the working set is 18 and 19, with 08 as an optional
arithmetic track; 01 and 02 can reopen only through their stated gates.
Destinations (03, 06), the tool (05) and the reading folders (12, 13) stay
available. Nine folders would close as separate projects.

## Overlap with the Codex first pass

The Codex pass and the Claude review were written independently on the
same day. They agree on the main allocation, and the overlap is mostly
confirmation.

- **02.** The review (§4) predicted that transporting the lattice law
  through the insertion would give an exact, linear coefficient identity
  with no sign, and set a stop rule. The Codex calculation
  ([elliptic transport](02_angular_jacobi_gluing/notes/ELLIPTIC_INSERTION_TRANSPORT_AND_HEAT_OBSTRUCTIONS_20261013.md))
  is that calculation, carried out in full. It confirms the prediction and
  adds two obstructions the review did not anticipate: a single full-line
  period has a growing carrier, so its heat integral diverges, and the
  short-period repair has a negative source value at the origin and a
  cusp. The 02 gate therefore applies. Codex's own allocation then says
  to move the next bounded identity task to "the 09-to-06 calculation";
  that is exactly what 18 does.
- **09.** Codex asks to "transport the actual differential insertions into
  both unequal-scale parity cosets before testing a sign." Folder 18 does
  this. The insertions annihilate the Eisenstein constant term, giving a
  cusp-only formula for both Laguerre expressions at every Newman time.
  The parity-coset identity is the Hecke correspondence at 2. Details are
  in [18, Note 1](18_rank_two_automorphic_lift/notes/1_CUSP_FORMULA_HECKE_AND_CONTROLS_20261013.md).
- **01.** Codex proved that the shared endpoint survives the conjugated
  reflection (magnitude above \(w_N/20\)) and found no special saving in the
  paired tails. The review's re-anchoring (§5: Riemann–Siegel/Mordell form
  of Polymath's exact remainder \(R_{t,N}\)) is the kind of relation that
  the 01 gate asks for. If 01 reopens, that comparison should be its task.
- **17.** The Codex pilot is the benchmark the review asked for. Boundary
  certification costs four pair integrals against one interior pair
  integral on the same rectangle. The direction has done its job.

Where we differ: Codex keeps 04, 10, 11, 14 and 16 as capped supporting
items. I recommend closing them as separate projects for the reasons
below. Their initial notes remain readable, and nothing is lost by
closing.

## Reasons, folder by folder

**01 — pause.** The automatic endpoint-cancellation ansatz failed
quantitatively. Reopen only to compare the exact Riemann–Siegel remainder,
written in Mordell form with the dilation-lemma Newman defect (review §5),
against the current absolute envelope on one cell. Any signed remainder
should also be run on the Euler-factor controls of 19.

**02 — pause.** The transport is complete and exact; the full angular jet
hierarchy is a scalar derivative dictionary; the remaining elliptic
information is the integer lattice law, whose arithmetic content is the
Euler product. Reopen only with a named inequality on the complete
nonlocal channel and its correction (Codex's gate). The same lattice law
now lives in 18 as Hecke relations, where it can be tested prime by prime.

**03 — destination.** The certificate-equivalence fact means 03 can
transmit a relation from elsewhere but cannot create one.

**04 — merge into 06.** Its chord and score targets are differential
operators applied to the readout, so they carry no theta information of
their own. Keep the first note as a chart of 06.

**05 — tool.** Build a chart only when a named identity needs it.

**06 — destination.** 18 now supplies the structured form of the complete
paired kernels: both Laguerre expressions \(\mathscr L_0,\mathscr L_1\) are
moments of one cusp kernel about the fold point (18, Theorem 2). The
stationary signs are still RH-strength; nothing here weakens that.

**07 — merge into 18.** Divisor transport is the dilation and Hecke
structure. Its Newman defect is the dilation lemma (review §1.4), and its
complete form is the divisor-sum Fourier coefficient
\(n^{w-1/2}\sigma_{1-2w}(n)\) of the Eisenstein series in 18.

**08 — separate track.** It is not a lift; keep it if the work turns to
moment estimates.

**09 — merge into 18.** Its first deliverable, the exact two-coset
identity with unequal-scale coupling, is Theorem 3 of 18's first note:
the index-two sublattice (Hecke) identity at 2. Its even–even parity
coset (\(a=n+m\), \(b=n-m\) both even) is the index-two sublattice
\(\{n\equiv m \bmod 2\}\). For the rectangular lattice of shape \(iy\) this
sublattice has shape \((1+iy)/2\), on the geodesic
\(\operatorname{Re}z=\tfrac12\).

**10 and 11 — merge into 06 as charts.** They study the same quadratic
forms in Hermite or Stein coordinates. Neither names a closure mechanism
that 06 lacks.

**12 — reading and bridge.** Add the review's W2 here: Newman's flow is the
Gaussian law of shifts \(H_t(x)=\tfrac18\mathbb E\,\xi(\tfrac12+V+\tfrac{ix}2)\),
\(V\sim N(0,t/2)\), against the two-point law used by the main repository's
shifted-positivity program. De Bruijn's strip theorem is the only proved
bridge.

**13 — reading only.** The required stable preparation theorem is
RH-strength.

**14 — close.** The Volterra flow holds for every even measure under the
Gaussian weight; it has no theta-specific input.

**15 — merge into 18.** Adelic compatibility is the Hecke algebra at every
prime. 18 §5 and 19 show what this means as a screen: each Hecke relation
at a single prime \(q\) is satisfied by every control \(\Phi_{c,p}\) with
\(p\ne q\), all of which have \(\Lambda_{c,p}>0\). Only the relations at
all primes together can be load-bearing.

**16 — close.** Radial positivity is Bochner positive-definiteness of
\(H_t(|z|)\), which is generic.

**17 — close as a completed benchmark.** The winding count is real-zero
counting in topological form, and the benchmark found no cost advantage.
Keep the checker and records; reopen only for a demonstrably hard cell or a
boundary homotopy that saves work.

## The two new folders

**18, rank-two automorphic lift.** This is the review's direction A. It
absorbs 09, 07 and 15, carries the wild card W1 (the horocyclic-to-geodesic
family) as a deferred task, and executes the "09-to-06" allocation of the
Codex pass. First results: a cusp-only formula for \(\mathscr L_0\) and
\(\mathscr L_1\) at every Newman time; the two-coset identity as the Hecke
correspondence at 2, at every time; and the control test, showing that any
finite set of Hecke relations is shared by a control with
\(\Lambda>0\). Stop rule: close after one more bounded task (A4) unless a
positive-definite structure appears.

**19, Euler-factor controls.** This is the review's §1.3 control family,
promoted to a shared screen with the three-controls protocol. First
results: the exact Newman flow of every control; a one-point Laguerre
witness criterion (any real point with \(\mathscr L_0<0\) proves
\(\Lambda_{c,p}>t\), and witnesses exist close to the last collision); a
numerical table of \(\Lambda_{c,p}\); and the formal expansion
\(\Lambda_{c,p}=t_m-S_2t_m^2+\cdots\), confirmed numerically, with
\(t_m=4\log(1/c)/(\log p)^2\) and \(S_2=\xi''(\tfrac12)/(2\xi(\tfrac12))\).

## If you accept

1. Move 04, 07, 09, 10, 11, 14, 15, 16 and 17 to `inactive/`, adding each to
   its index with a pointer to the principal home in the table above.
2. Add one line to 01 and 02 stating that each is paused at its gate.
3. Update the active overview and the portfolio README to the working set
   above.

I can carry these out on request.
