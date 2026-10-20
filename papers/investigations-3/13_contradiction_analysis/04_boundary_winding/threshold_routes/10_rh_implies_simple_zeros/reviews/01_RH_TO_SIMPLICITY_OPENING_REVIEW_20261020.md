# Opening review of the conditional simplicity track

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **gpt-6-astra (Codex), reasoning effort ultra**,
as verified by the parent session. Separate same-model internal review;
not specialist review or an exhaustive literature search.

**Verdict: no blocking mathematical correction found in the opening
formulation.** The [brainstorm note][note], [parallel program][program]
and [progress register][progress] correctly distinguish the selected
goal, RH implies simplicity of every nontrivial zeta zero, from the
stronger unconditional alternative. They do not claim a new exclusion
estimate or a proof of the goal. RHS-00–01 can record the opening scope
and inherited transfer as complete; RHS-02–05 remain open.

## Checks

1. **Conditional contradiction.** RH gives all-realness at zero and at
   every positive heat time. A multiple zero at a strictly positive time
   would have nonreal predecessors at a slightly earlier positive time,
   by the local Hermite splitting. Therefore forcing one later multiple
   event would contradict RH. Negative-time nonreal predecessors of the
   assumed event at zero do not. The note correctly separates heat time
   from the zeta ordinate and requires no threshold-attainment theorem.

2. **Every multiplicity.** The local polynomial and double-root drift
   agree with the manuscript. The index is
   \(-\lfloor m/2\rfloor\), whereas the cap between the outermost
   emerging roots has ordinary decrease \((m-1)\pi\). These are different
   quantities. Subtracting bottom from top cap phase gives
   \[
   W_{\rm strip}=-\frac{N-(m-2)}2.
   \]
   Thus an outer-cluster argument needs a strict surplus over
   \((m-1)\pi\). The note correctly avoids assigning the full initial
   event charge to a strip around just an adjacent subpair.

3. **Exact endpoint control.** The shifted even source at \(c=1\)
   gives \(H^{1,p}(0,x)=H(0,x)(1+\cos(b_px))\). The additional factor
   has double real zeros and no nonreal zeros. Under RH, all-real
   preservation gives all-real slices for \(t\ge0\); backward splitting
   at the added repeated roots excludes an earlier all-real slice.
   Its threshold is consequently exactly zero, and every positive-time
   zero is simple. Algebraically, with \(s=1/2+ix/2\),
   \[
   1+\cos(b_px)=\frac12p^{s-1/2}
                    (1+\sqrt p\,p^{-s})^2.
   \]
   This confirms the stated Dirichlet series and changed conductor
   \(p^2\). It screens generic Euler-product and functional-equation
   arguments, while failing unchanged zeta coefficients and conductor
   one. Merely naming those failures is correctly not counted as a
   quantitative distinguishing estimate.

4. **Gaussian identity.** The coefficients in the deficit follow from
   the Hermite expansion with variance \(2s\); the quadratic mode has
   zero coefficient. At a multiple zero all remaining terms are
   nonnegative. Equality would force the cap to be quadratic, impossible
   for the nonzero bounded theta cap. The atomic formula
   \(1+s\sinh(2s)-\cosh(2s)\) and its positive second derivative check
   exactly. The note correctly classifies small-scale negativity at
   every center as an equivalent target, not an intermediate estimate.

5. **Unconditional successor alternative.** The finiteness argument is
   valid for events bounded away from heat time zero. Polymath
   Theorem 1.5(i) gives the uniform height bound
   \(x<\exp(2C/t_1)\) for nonreal predecessors with
   \(t>t_1/2\). Local splitting therefore confines events with
   \(t\ge t_1\); closedness and local isolation make their compact set
   finite. A repeatable strictly later successor mechanism would
   contradict this even without a uniform time increment. The note
   correctly marks that mechanism as unproved and requires it for every
   descendant, not only threshold events.

## Literature and scope

The primary sources support the restrained status wording:
[Bui–Heath-Brown](https://arxiv.org/abs/1302.5018) prove a proportion of
simple zeros under RH, and
[Gao–Zhao](https://arxiv.org/abs/2208.06922) explicitly use RH together
with simplicity. The distinction remains explicit in
[Bui–Florea–Milinovich, §1](https://arxiv.org/html/2310.03949v1).
[Polymath, Proposition 3.1 and Theorem 1.5](https://arxiv.org/html/1904.12438v2)
support the splitting and uniform positive-time confinement used above.
This evidence supports treating the all-zero implication as a substantive
open target; it does not establish priority for the proposed method.

The review follows the [result index][results], [control catalogue][controls]
and [avoid index][avoid]. No new theta sign, finite surplus, all-height
bound or multiplicity exclusion was produced by this review. The first
remaining task is the program's one quantitative arithmetic estimate,
tested on the endpoint control with its own data.

[note]: ../brainstorm/01_RH_IMPLIES_SIMPLICITY_20261020.md
[program]: ../research-overview/01_RH_TO_SIMPLICITY_PROGRAM_20261020.md
[progress]: ../research-progress/01_RH_TO_SIMPLICITY_PROGRESS_20261020.md
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
