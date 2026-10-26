# Internal assessment: R01 second-level comparison

26 October 2026. Prepared for **Edward Baker** with substantial LLM
assistance, **gpt-6.1-sol, actual effort ultra**. Recurrence chat0001,
thread `01a17690-2e5f-77b1-a3a4-9c31f72c117d`.

**Same-model internal analytical assessment.** Two read-only same-model
checks tested the local remainder/full comparison and the classical inputs.
They share the model and premises with the writer; no human, cross-model
or independent specialist review is claimed. No numerical/symbolic work.

Reviewed [R01 mathematical return][note], [frozen request][packet], the
continuation, ansatz Notes05/06/10/12/16 and their linked internal reviews;
opening versions are in [the input record][inputs]. Primary imports were
checked at DLMF 5.11.2 and 5.11(ii), and Polymath 1904.12438v2,
Proposition6.2 (56), with exact prefactor (38). The all-order analytic
majorant is a Cauchy consequence, not an imported convergent asymptotic
series. The underlying Arias coefficient provider is imported through
Polymath, not independently implemented or complexity-audited.

Accept R1.1: `||h-F^[2,4]||^(3,1) <= C_(r,b) X^-11/4` on `[1,2]`.
The following checks are material:

- R1.7 follows by a convergent geometric majorant and the third derivative
  of exp f; it includes q^4, q^5 and q^6, with weight X^-3. Replacing q
  by V before integrating would lose logarithms and is avoided.
- R1.11 retains exactly both arms and all N. Its X^1/4 loss changes
  X^-3 to X^-11/4. No fixed set of modes is substituted.
- The canonical mismatch with K=4 is independently X^-11/4. The
  `Gamma(5/2)1.1^5` and real-window scale are retained. Q, its five
  coefficient functions and adjacent transfer stay inside the bounded
  integral; no coefficient analyticity or derivative import is needed.
- Enlarged buffers precede Cauchy; the degree-eight local moment and
  both inverse-time factors pay direct T differentiation. No derivative
  of a big-O allowance enters the proof.
- True moderate tails retain X^(P-7/4); remote tails retain the lost
  gamma exponential. Artificial tails have only polynomial initial
  data and retain X^1/4. R1.18 explicitly absorbs each at X^-11/4.
- R1.19 and its spatial derivative vanish exactly with frozen data.
  Reconstruction was proved independently before using E_T=E_zz.

The degree-four/weight-two difference and target-centered/frozen
spatial derivatives are correctly distinguished. The older K=1 total
bound remains X^-5/4; residual cancellation alone would not improve it.
The failed outer-relative algebraic allowance is retained as a bound
failure, without an actual-error lower claim.

**Disposition — Analysis, Sol:** R01-AN01 r1 CLOSED, bounded R01 comparison
Complete; accept this version for R02. R02's general-order target is
still unproved at this disposition and is activated only after this
assessment and the return are installed. HDA-A02 remains Partial;
HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled remain unchanged.
No physical transfer, through-zero/growing-time extension, useful runtime,
coefficient-evaluation cost or specialist validation follows.

[note]: ../notes/02_FIRST_FINITE_FLUCTUATION_COMPARISON_20261026.md
[packet]: ../research-progress/handoffs/HDA-R01-AN01.md
[inputs]: ../numerics/R01_ANALYTICAL_INPUTS_20261026.json
