# Internal assessment: fixed-order recurrence and matched completion

26 October 2026. Prepared for **Edward Baker** with substantial LLM
assistance, **gpt-6.1-sol, actual effort ultra**, recurrence chat0001,
thread `01a17690-2e5f-77b1-a3a4-9c31f72c117d`.

**Same-model internal analytical assessment**, including a read-only
same-model audit of Bell coefficients, remainder and tails. It is not
independent specialist, human or cross-model validation. No numerical or
symbolic campaign. Reviewed [Note03][note], the frozen R02 request,
accepted R01 proof/review/disposition, ansatz Note16 and the classical
imports already checked in R01; [inputs][inputs] identify versions.

Accept `K(p)=2p`, `sigma(p)=p+3/4`, no logarithmic losses, for each fixed
integer p>=1 on [1,2], full buffered (3,1) norm. Material checks:

- R2.2--4 are finite partition identities. Grouping by factor count gives
  binom(j-1,k-1)/k!, so no multiplicity is missing.
- R2.5 bounds f^(r)/r! before Bell expansion. The latter supplies
  2^(m+k)A^kD^(m-k) and polynomial degree m+k. Taylor's integral remainder
  cancels m!; R2.7 has no extra factorial missing. At m=3 it is R01.
- Every local polynomial moment is integrated before summing the full
  initial population; this keeps the X^1/4 cost without log powers.
  The separate evolved-population shell sum and shifted Hermite moments
  are paid in R2.8--12, rather than assumed uniformly bounded per n.
- K=2p pays exactly the displayed initial RS exponent, with Gamma and
  exponential constants retained. The exact transfer and bounded real
  completion persist. The theorem does not claim K is necessary for
  the actual error, only sufficient/minimal for this allowance.
- H_p is an explicit coarse X>=1 tail majorant. Its degree 2p, all
  coefficient combinatorics and both derivative costs stay in A_art,p.
  R2.15 pays true moderate, artificial and true remote tails at the
  same rate. For p=2 it specializes to R01's gates.
- Enlarged-chart Cauchy and differentiated kernels pay the requested
  norm. Direct-time local degree is 2p+4. The exact residual and its
  first spatial derivative vanish for the frozen construction.

R2.16 is an explicit majorant for order dependence. It is not a
numerically optimized constant, evaluated onset or growing-p proof.
The low-order comparison retains K=1 for the older target-centered
result; its weaker total allowance is not rewritten. Failed outer-scale
and insufficient-K allowances remain scoped failures, not lower bounds.

**Disposition — Analysis, Sol:** R02-AN01 r1 CLOSED; bounded fixed-order
R02 question Complete. R03 may consume Note03 for every fixed p and
K=2p; the p=2 fallback is unnecessary. R03 enters analysis only after
this assessment, the proof and packet disposition have been installed.
Parent HDA-A02 Partial, HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled
remain unchanged. No manuscript or physical-transfer integration.

[note]: ../notes/03_FIXED_ORDER_FLUCTUATION_HIERARCHY_20261026.md
[inputs]: ../numerics/R02_ANALYTICAL_INPUTS_20261026.json
