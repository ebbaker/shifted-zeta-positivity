# Euler-factor control checks

13 October 2026. Prepared for Edward Baker with LLM assistance.
Model: Claude Opus 5.5 (configured identifier `claude-opus-5-5`; the serving
model may differ), Claude Cowork, reasoning effort **max**.

**Correction, 13 October 2026.** Prepared for Edward Baker with LLM
assistance by `gpt-6-astra` (Codex), reasoning effort **ultra**. Original
Claude provenance above is retained. This revision distinguishes tracked
collision times from the global Newman constant and corrects the witness
margin; it introduces no new numerical certificate.

Run, in this directory:

```sh
python3 -I check_euler_factor_controls_claude_20261013.py --output EULER_FACTOR_CONTROLS_RECORD_20261013.json
```

The [checker](check_euler_factor_controls_claude_20261013.py) uses only the
Python standard library and takes about 20 seconds. It prints the
[record](EULER_FACTOR_CONTROLS_RECORD_20261013.json) as deterministic JSON
and exits nonzero if any check fails.

- **Part E, exact rational arithmetic.** Roots of the Euler-factor
  perturbation \(Q_p\) are off the critical circle and reciprocal; the
  Laguerre product rule; the multiplier's Laguerre expression; the algebra
  of the first-order expansion.
- **Part N, double precision.** \(S_2\) and \(\xi(\tfrac12)\) by
  quadrature; the exact flow against direct quadrature; zero tracking and
  Newton on \(H=H_x=0\) for twelve \((p,c)\), with the collision order of
  the three lowest pairs and the expansion ratio for the lowest-pair
  collision time \(T_0(c,p)\); sampled negative Laguerre values below
  \(T_0\) and sampled positive normalized values at \(1.01T_0\);
  numerical \(T_0(1/2,p)\) for all primes \(p\le47\).

Part N uses contour-shifted trapezoid quadrature and Newton iteration. It
is numerical evidence, not an interval certificate; certification of one
witness is the folder's next task. Keep large regenerable data outside Git
under [LARGE_FILES.md](../../../../../LARGE_FILES.md).

## Legacy labels and what the record establishes

The checker and JSON are preserved as historical computational records;
this correction does not change their values, schema or source hash. In
the following legacy labels, `Lambda` means the **numerically tracked
lowest-pair collision time** \(T_0(c,p)\), not an established value of the
global Newman constant \(\Lambda_{c,p}\):

| Historical field or section | Current interpretation |
| --- | --- |
| `N2_lambda_table_and_expansion`, `Lambda` | Numerical \(T_0(c,p)\) and its local expansion diagnostic |
| `Lambda_over_t_m` | \(T_0/t_m\) |
| `(t_m-Lambda)/(S2 t_m^2)` | \((t_m-T_0)/(S_2t_m^2)\) |
| `t_over_Lambda` | \(t/T_0\) |
| `t=1.01*Lambda_min_normalized_L0_on_grid` | Minimum over a finite grid at \(t=1.01T_0\); no global nonnegativity or all-real-zero conclusion |
| `Lambda_by_prime` | Numerical \(T_0(1/2,p)\) by prime |
| `primes_with_Lambda_above_0.2` | Primes with computed \(T_0>0.2\); candidates for certified lower-bound witnesses |
| `pair_collision_times_k0_k1_k2` | Numerical collision times of the three tracked branches only |
| `lowest_pair_collides_last` | Largest computed time among \(k=0,1,2\) only |
| `witness_p41_t0.2`, `L0_over_H2` | Numerical candidate normalized witness; requires outward bounds for a rigorous negative sign |

The same interpretation applies to the checker's title, comments,
variable names and printed descriptions. In particular, its comparison
`0.2 > Lambda` for \(p=43\) checks a numerical estimate of \(T_0\);
it does not show \(\Lambda_{1/2,43}<0.2\). The expansion in the checker
is a formal expansion of that local collision time, not a proved global
asymptotic.

A proved negative value of \(\mathscr L_0\) at time \(t\) implies
\(\Lambda_{c,p}>t\). These double-precision values are evidence for
such a proof, not rigorous lower bounds. Tracking \(k=0,1,2\) does not
control all other zeros. Equality \(T_0=\Lambda_{c,p}\) would require
that every remaining zero, including any inherited from \(H_0\), be
real by \(T_0\).

For an isolated simple-pair collision,
\(H(x)=((x-X)^2+y^2)g(x)\) gives exactly
\[
\mathscr L_0(H;X)=-2y^2g(X)^2+y^4\mathscr L_0(g;X).
\]
With a nonzero uniformly regular \(g\), the raw negative margin tends
to zero even as \(\mathscr L_0/H^2\sim-2/y^2\). Choose certification
precision using the raw margin or a justified nonzero normalization.
