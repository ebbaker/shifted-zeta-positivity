# Bounded Lean check: the abstract taper tradeoff

20 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Actual model **gpt-6-astra**, reasoning effort **ultra**.
Research checkout read at HEAD **95fb28b**. This is a bounded kernel check,
not a formalization of the analytic investigation or a specialist review.

## Verified statement

In any real inner-product space, assume
\[
\delta>0,\quad \|e\|^2=1,\quad \|r\|^2=\delta,\quad
\langle e,r\rangle=0,\quad
\langle v,e\rangle=-1,\quad
\langle v,r\rangle=\frac{1-\delta}{2}.
\]
Lean checked the exact identity
\[
\left\|v+e-\frac{1-\delta}{2\delta}r\right\|^2
=\|v\|^2-1-\frac{(1-\delta)^2}{4\delta}
\]
and its consequences
\[
\|v\|^2\ge1+\frac{(1-\delta)^2}{4\delta},
\qquad
2(1+\delta)+\|v\|^2
\ge4+\frac{(3\delta-1)^2}{4\delta}\ge4.
\]
The source declarations are:

- BW10.flatTaperResidualIdentity
- BW10.flatTaperNormBound
- BW10.flatTaperCostBound
- BW10.flatTaperCostFloor

The taper interpretation of \(e,r,v,\delta\), all moment identities,
integration by parts, the expression for the local cost \(C_2\), smooth
flat-taper approximation, sharpness/nonattainment, Mellin transfer,
complete arithmetic errors, RH and simplicity are **not formalized** here.
The check verifies the displayed implication from its explicit hypotheses.

## Exact successful check

- Source: [FlatTaperTradeoff.lean](FlatTaperTradeoff.lean).
- Lean: **4.34.1**, aarch64 Linux; compiler commit
  5045d0056413266e57c625dcd7c365b10e377c52.
- Existing mathlib commit:
  **d13f23b723b8a846827a245b89c10fc7d3f11612**.
- Source SHA-256:
  **46191c28a3fdc8bdffd8b59021cfd576602395dcc3f04a6d56a95dbed4b6e06d**.
- Final return code: **0**, with no warnings or errors.
- Compiled scratch object SHA-256:
  **991617cbf0cf33b6f9e962c366fdab3e81b6b56f0ccfd46b6af125383f652ce9**.
- Full command, library paths and kernel output: [lean_check.json](lean_check.json).

For all four declarations, Lean's axiom report contains exactly
**propext, Classical.choice, Quot.sound**, the standard foundations used
by this Lean/mathlib proof. There is no sorryAx, admitted proof step,
or newly declared axiom. The proof uses inner-product identities,
field simplification, polynomial algebra and nonnegativity of a square;
no native decision oracle is invoked.

## Environment and replay

The existing VM rh-replay and its installed cache were used directly.
The replay project at /home/ubuntu/rh-replay-source/lean was read only.
No package, toolchain, project source or project configuration was
installed, built or edited. Source, compiled output and check log were
written only beneath /tmp/bw10-round20-lean in the VM.

The included [run_lean_check.py](run_lean_check.py) invokes the pinned Lean binary directly,
sets LEAN_PATH to the existing compiled library directories, and routes
the output object and JSON report to that scratch directory. It does not
invoke lake or fetch dependencies. To reproduce in this VM, place the
Lean file and runner in that scratch directory and run
python3 /tmp/bw10-round20-lean/run_lean_check.py.

The saved source and successful log provide the mathematical check.
They do not upgrade the unformalized analytic premises or establish
an opposing upper estimate for the unchanged zeta function.

The original successful log is retained unchanged. Before interpreting a
rerun, compare its compiler version, mathlib commit and source hash with
the values above; a changed environment is a different check. Compiled
objects and dependency caches are not committed.
