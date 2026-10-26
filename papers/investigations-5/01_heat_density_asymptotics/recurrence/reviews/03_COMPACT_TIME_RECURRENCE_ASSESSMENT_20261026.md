# Internal assessment: compact-time fixed-order recurrence family

26 October 2026. Prepared for **Edward Baker** with substantial LLM
assistance, **gpt-6.1-sol, actual effort ultra**, recurrence chat0001,
thread `01a17690-2e5f-77b1-a3a4-9c31f72c117d`.

**Same-model internal analytical assessment**, including a read-only
same-model check of endpoint constants, mode population and tail gates.
No human, cross-model or independent specialist validation; no numerical
or symbolic campaign. Reviewed [Note04][note], R03-AN01 r1 and its common
contract, saved R01/R02 proofs and assessments, ansatz Note12/Review09
and inherited named classical inputs. [Inputs][inputs] pin versions.

Accept R3.1 with each fixed p>=1, K=2p, fixed 0<tau<=T<=B<infinity,
full target buffers and natural scale X^-(p+3/4), no log loss. No fallback.
Material checks and one routine onset refinement:

- M_m is derived by rescaling the actual complex kernel at variable T,
  then bounding on [tau,B]. It retains exp(Y²/(4tau)+2B); M_m^t retains
  tau^-1,tau^-2 and the two extra moments. Thus direct time is not an
  endpoint substitution into a scalar allowance.
- R02's local Bell remainder is applied only inside its now-checked
  V_B window. Coefficients, full initial population and initial RS
  mismatch retain their previous constants after u>=X/2. The maximal
  local direct-time moment degree is 2p+4.
- The all-mode shell sum retains exp(-tau v_n²/4), the transverse factor
  exp(Y v_n/2), and Z_m's shifted argument. The explicit gate
  D0/X<=1-a0 preserves |Re lambda|<=1; the weaker D0/X<=1 alone would
  not justify exp(R) in the population bound. This refinement is within
  the original contract and is recorded in R3.9.
- The prescribed window gives exp(-bar(B)L²/B)<=exp(-L²), including
  B<1. D_m,J_m retain normalization and kernel factors. Moderate true
  data use height decay, remote data pay the lost gamma exponential,
  and artificial data are finite exponential-polynomials only.
- The onset table retains every p/endpoint constant before absorption;
  its gates are eventual only for fixed declared parameters. K=2p
  keeps the source Gamma factor and all real completion data/partitions.
- Fixed-radius Cauchy gives the spatial norm without log loss. Frozen
  data and commutation prove residual=residual_z=0 separately; the
  direct reconstruction precedes the optional E_T=E_zz cross-check.

The equal-endpoint family is understood by restriction of smooth positive
T functions. Different B windows are compared through the same h; this
does not identify their formulas or supply physical joining.

The failed fixed-order outer allowance is preserved and correctly scoped.
R3.19 explicitly deteriorates with tau,B,p. No joint limit is asserted;
its first unpaid step is the simultaneous bound for constants/onsets
along a chosen parameter range. No continuous-s norm theorem follows
from its formal generating relation. Provider conditioning, working
precision, quadrature and useful runtime remain unproved.

**Disposition — Analysis, Sol:** R03-AN01 r1 CLOSED; requested fixed
compact-family R03 question Complete. Accept the full fixed-order family
as a natural-scale upstream input, retaining the bounded integral and
all modes. R01, R02 and R03 each have saved mathematical returns,
internal assessments and dispositions in dependency order. HDA-A02
Partial, HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled remain.
Recommend a new bounded controlled-order-growth audit by Analysis — Sol;
no fourth task, manuscript or numerical campaign has been started.

[note]: ../notes/04_COMPACT_TIME_RECURRENCE_FAMILY_20261026.md
[inputs]: ../numerics/R03_ANALYTICAL_INPUTS_20261026.json
