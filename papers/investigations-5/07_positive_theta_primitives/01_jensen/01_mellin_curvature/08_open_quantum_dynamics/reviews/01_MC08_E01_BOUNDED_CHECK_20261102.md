# MC08-E01 bounded internal checking record

2 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Recorded by **gpt-6.1-sol (Codex), reasoning effort ultra**, chat `01a19d66-56e2-7ff2-a549-03561c41f801`, turn `01a19d66-5954-7bd1-a3e4-a07132e0161f`, integrating two read-only checking subtasks using the inherited same-model configuration. The author and checkers share the source and task premises. This is limited same-model internal checking, not specialist or cross-model review, and **does not complete MC08-E03**, which awaits E02.

**Disposition: no blocker found at the stated E01 r1 scope.** The symbol/control checker accepted the full staged return after checking the mathematical claims. The constants checker independently derived the rational source bounds and interval. The exact support program passed, including coefficient-by-coefficient verification of the polynomial identity. The final edit makes the boundary-zero inverse obstruction explicit using approximate eigenvectors; it changes no estimate.

| Frozen artifact | SHA256 |
| --- | --- |
| [Return01](../notes/01_NO_JUMP_ADMISSIBILITY_AUDIT_20261102.md) | `21929f0b5050f699b856aaa899dd1631564aecb2a700a89fa994cbdeeb1fabf5` |
| [Support program](../numerics/mc08_e01_exact_bounds.py) | `0650394605d7fea6af5b27941d3fa458660f20fe18148dfce1604d546ab2ed8e` |
| [Execution record](../numerics/MC08_E01_EXACT_BOUNDS_20261102.json) | `fba2ae5435515676f801c10b7bfe7dd62e46850d2d066fd5571048f69152fb2f` |

The checked chain is: complete-source primitive and canonical endpoint; integration-by-parts normalization; full mode/integration-tail bounds; radius-four zero-free disk and logarithm; half-infinite Toeplitz form and the analytic zero-angle limit; exact coefficient tail at v=1/25; relative margin 1/8000; norm-continuity including the gapless square root; bounded infinite-one-particle CP jump expansion and trace preservation; exact intermediate K_b K_a inverse; cutoff/particle scope and the no-jump probability floor.

The Gaussian and polynomial controls were checked explicitly. The polynomial is dissipative on its zero-free disk and still has a negative two-particle amplitude, so it screens the strengthened dynamical premise. The record does not infer a failure of that premise for the other collision families merely because their canonical-source identity fails.

The accepted scope is a proved-in-note local realization with bounded one-particle completion directly on ell-squared. The interval is not optimized, v=1 is not covered, no full-Fock jump theorem or locality result is established, and no signed-minor/Mellin comparison is obtained. The planned architecture decision and E02/E03 remain necessary.
