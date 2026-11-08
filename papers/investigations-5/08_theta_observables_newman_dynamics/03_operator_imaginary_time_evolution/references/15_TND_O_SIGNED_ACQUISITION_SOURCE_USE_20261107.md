# B04 r5 / E20: fixed Euler preconditioning and the twisted second moment

7 November 2026, America/New_York. Prepared for Edward Baker with substantial OpenAI Codex assistance. Research lead tool-selected gpt-6-astra/ultra; root recorder configuration unavailable. These are selection records, not backend verification.

**Source:** Sandro Bettin, Vorrapan Chandee and Maksym Radziwiłł, *The mean square of the product of ζ(s) with Dirichlet polynomials*, arXiv:1411.7764v1, submitted 28 November 2014. [Version-pinned metadata](https://arxiv.org/abs/1411.7764v1); [primary converted text](https://arxiv.org/html/1411.7764v1); [PDF](https://arxiv.org/pdf/1411.7764v1). Retrieved 7 November 2026.

**Checked passages:** §1, definition (1.1) and Theorem 1, including its coefficient assumptions, smooth weight and error. Lead and root separately inspected these passages. No full-paper proof audit or novelty assessment. The converted HTML prints an anomalous August 24, 2026 date; the pinned arXiv metadata identifies the version as v1 from 2014. No later revision is inferred.

For a smooth fixed weight φ supported in [1,2], and A(s)=Σ_{n≤N}a_n n^(−s), N=T^θ, θ<17/33, a_n≪n^ε, the theorem gives the twisted second moment with main coefficient Σ a_d conjugate(a_e)/[d,e] and logarithmic factor log(t(d,e)^2/(2πde))+2γ. The remainder is O(T^(3/20+ε)N^(33/20)+T^(1/3+ε)). E20 uses a fixed finite Euler polynomial, zero-padded within a permissible positive θ, and a nonnegative nonzero smooth weight supported strictly inside (1,2). It derives its own gcd factorization and Green-residual implication. No pointwise or moving-polynomial estimate is imported from a fixed-polynomial limit. The introductory sharp-cutoff theorem attributed to earlier authors is not needed.

**Use:** [E20 request36](../research-progress/handoffs/36_TND_O_E20_PAID_QUADRATIC_COMPARISON_REQUEST_20261107.md), and the eventual Decision17. This is an obstruction to fixed finite preconditioners delivering uniform all-center small residuals, not a zero-density theorem or a canonical exclusion bound.

**Reading-copy availability:** a web PDF fetch by the lead failed; root's authorized host download also failed with DNS resolution unavailable. No PDF copy, hash or full reading is claimed. The primary HTML theorem suffices for the stated use. No third-party PDF was put in Git.

## E20 r2 consumer extension after the completed r1 return

The selected BCR Theorem 1 also permits a uniform growing-polynomial consumer when its length and coefficient bound are retained. [Request37](../research-progress/handoffs/37_TND_O_E20_R2_UNIFORM_EULER_LENGTH_REQUEST_20261107.md) uses N=(T/2)^θ, fixed θ<17/33 and coefficients bounded by one. It derives the finite-Euler logarithmic gcd correction and an elementary product lower bound before using the theorem's error uniformly. This is an explicit new use of the same checked statement, not substitution into the earlier fixed-Q consequence. The executor and assessor must check this uniformity. Source15's initial version remains identified in completed inputs36/return36; this appended consumer record is frozen separately in inputs37.
