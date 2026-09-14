# Independent recomputation scripts — first-slab positivity

## Current executable check

`verify_stable_volterra_20260909.py` repairs the singularity and overflow
problems in the older script's A4 diagnostics. It has 16 checks covering
piecewise-constant Galerkin sections at shifts 0.3 and 0.5, finite-section
reflection algebra, quadrature and mesh consistency, and four high-precision
Laplace-transfer comparisons. Unexpected failures return a nonzero status.

```bash
python3 -m pip install -r verification/first-slab/scripts/requirements_stable_checks.txt
python3 verification/first-slab/scripts/verify_stable_volterra_20260909.py
```

Run those commands from the repository root. This is ordinary numerical
verification, not an Arb certificate or a proof of an operator-norm bound.
The H and V matrices share the scalar overlap integrals; agreement of their
algebra tests indexing conventions, not an independently derived kernel.

## Historical recomputation records

The two dated scripts below are preserved as historical records. The September
5 script prints failures without turning them into a nonzero exit status and
includes exploratory normalization calculations; it must not be used as a
pass/fail CI gate. Its A4 section is superseded by the executable check above.
The replacement does not rerun or replace the old A1--A3 sections or C1
normalization experiments. The existing normalization-review protocol remains
in force.

Both scripts were written from the definitions printed in the manuscript, with
no access to the primary (Arb) or clean-room implementations. They are
*recomputations*, not certificates: floating/mpmath arithmetic, no interval
enclosure.

| Script | Date | Written against | What it recomputes |
|---|---|---|---|
| `verify_referee_checks_20260831.py` | 31 Aug 2026 | working draft of 31 Aug | `t₀` and the sharp Schur constant; `β*` and the Schur loss (old constant 0.024587 — draft values, superseded); independent 16-mode Legendre reconstruction of the certificate at `L = log 2` (even/odd, with kernel doubled as a control); positivity-horizon sweep in `L` and `ω`; the ω = ½ endpoint anomaly in the pre-correction §4.2 formula. |
| `verify_preprint_checks_20260905.py` | 5 Sept 2026 | preprint v1.0 | Every step of the Prop. 4.2 proof (30+ digits, ω = 0.3 and ½); endpoint lemma (delta mass → −π; `f = 1` comparison); full §6.3 chain incl. `L/2 > t₀` and row-integral monotonicity; degree-4 Taylor remainder bound; `β*`, `d_tail`, both Schur losses; the block-Schur coercivity constants of Lemma 7.1; the Suzuki Mellin normalization (variants of an extracted `g_ω`; inconclusive on the exact display of `g_ω`, conclusive on the Mellin-transform statement). |

Environment: `mpmath 1.4.1`, `numpy 2.4.4`, `scipy 1.17.1` (see `environment/requirements.txt`).
Run time: a few minutes each. The discretised Volterra-identity check in the
second script is unreliable because of the kernel singularity on the
anti-diagonal; the identities were verified by hand instead (see A4 in `../CHECKLIST.md`).

[Shifted-zeta program](../../../papers/shifted-zeta/README.md) · [All manuscripts](../../../papers/README.md)
