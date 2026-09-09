# Independent recomputation scripts — first-slab positivity

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
