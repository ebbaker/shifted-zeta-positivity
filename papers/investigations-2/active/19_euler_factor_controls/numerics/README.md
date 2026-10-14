# Euler-factor control checks

13 October 2026. Prepared for Edward Baker with LLM assistance.
Model: Claude Opus 5.5 (configured identifier `claude-opus-5-5`; the serving
model may differ), Claude Cowork, reasoning effort **max**.

**Correction, 13 October 2026.** Prepared for Edward Baker with LLM
assistance by `gpt-6-astra` (Codex), reasoning effort **ultra**. Original
Claude provenance above is retained. This revision distinguishes tracked
collision times from the global Newman constant and corrects the witness
margin; it introduces no new numerical certificate.

<<<<<<< HEAD
## Certified raw witness, 14 October 2026

Prepared for Edward Baker with LLM assistance by `gpt-6-astra` (Codex),
reasoning effort **ultra**.

The new [outward checker](certify_euler_factor_witness.py) proves
\(\Lambda_{1/2,41}>1/5\) at \(x=168413/100000\). The
[execution record](EULER_FACTOR_WITNESS_RECORD_20261014.json) contains
exact dyadic endpoints, the source hash, all three jet enclosures, and
separate theta-index and complete source/control-shift tail payments.
The raw \(\mathscr L_0\) lies strictly between
\(-0.000005299994533574706\) and
\(-0.000005299994533574704\). The
[proof note](../notes/2_CERTIFIED_EULER_FACTOR_WITNESS_20261014.md)
derives the integral and every analytic tail bound.

Requires `python-flint` (tested with version 0.9.0 and Python 3.10.0).
From this directory:

```sh
python3 -B certify_euler_factor_witness.py --output /tmp/euler-factor-witness.json
```

No external data files or machine-specific paths are needed. The script
prints a small JSON record and fails unless all analytic hypotheses,
finite enclosures, and the strictly negative raw sign pass. A second run
at 192 bits with five retained theta terms confirmed the sign and the
same rational display bracket. This establishes one lower bound; it does
not establish any global collision-time equality.

<<<<<<< HEAD
=======
## Historical exploratory checker
=======
>>>>>>> 94745f3 (Merged work from ChatGPT)
## Certified witnesses for the manuscript (14 October 2026)

Prepared for Edward Baker with LLM assistance. Model: Claude Opus 5.5
(`claude-opus-5-5`; the serving model may differ), Claude Cowork,
reasoning effort **max**.

Run, in this directory:

```sh
python3 -I check_euler_control_witnesses_claude_20261014.py --output EULER_CONTROL_WITNESS_CERTIFICATES_20261014.json
```

The [certificate program](check_euler_control_witnesses_claude_20261014.py)
uses only the Python standard library and takes 30 to 45 seconds
(`--quick` checks only \(p=41\), in about two seconds). It writes the
[record](EULER_CONTROL_WITNESS_CERTIFICATES_20261014.json) and exits nonzero
if any check fails. All arithmetic is 60-digit `Decimal` interval arithmetic
with outward rounding; negation is exact, and the default context traps
inexact operations.

- **Part A.** For \(c=\tfrac12\) and fifteen \((p,t,x_0)\), encloses
  \(H,H',H''\) of \(H^{c,p}_t\) at \(x_0\) by half-line trapezoid sums with
  the Trefethen–Weideman strip bound and an analytic tail, and proves
  \(\mathscr L_0<0\). This gives \(\Lambda_{1/2,p}>0.2\) for \(p\le41\) and
  \(\Lambda_{1/2,p}>0.1787854\) for \(p=43,47\). Each case is recomputed
  with \(h=1/32\) as a consistency check.
- **Part B.** Encloses the theta moments \(m_0,m_2,m_4\) at
  \(t=0,\tfrac14\) and \(\mu_4(\tfrac14,3)\).
- **Part C.** Checks that the rounded constants
  \(\bar k,\bar d,\bar\mu\) of the manuscript dominate the certified ratios
  and verifies the inequality (7.9) of the asymptotic theorem at both
  regime corners.
- **Regression checks.** \(\pi\) against 70 known decimals, and
  \(m_0(0)=\xi(\tfrac12)/8\) against an independent value.

The record is identical, apart from timing and the Python version, under
<<<<<<< HEAD
Python 3.10.12 and 3.13.16. The [manuscript](../manuscript/euler_factor_controls.tex)
describes the method; the [internal verification](../reviews/1_MANUSCRIPT_AND_CERTIFICATE_VERIFICATION_CLAUDE_20261014.md)
records the rounding defect found in, and removed from, the first version.

The two certificate programs are independent. Note 2 integrates a
rearranged integral with Arb's validated quadrature; this program uses
decimal intervals and the trapezoid rule with a strip error bound.
Evaluated at Note 2's point, this program's enclosures of
\(H,H',H''\) and \(\mathscr L_0\), each narrower than \(10^{-50}\), lie
inside Note 2's. The verification's addendum gives the command and values.

## Historical exploratory checker (Note 1, 13 October 2026)
=======
Python 3.10.12 and 3.13.16. The [manuscript](../manuscript/euler_factor_controls.pdf)
describes the method; the [internal verification](../reviews/1_MANUSCRIPT_AND_CERTIFICATE_VERIFICATION_CLAUDE_20261014.md)
records the rounding defect found in, and removed from, the first version.

## Floating-point checks of Note 1 (13 October 2026)
>>>>>>> dce5643 (Manuscript for euler control)
>>>>>>> 94745f3 (Merged work from ChatGPT)

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
<<<<<<< HEAD
is numerical evidence, not an interval certificate. The two outward
checkers above certify witnesses without changing this record. Keep large
regenerable data outside Git
=======
<<<<<<< HEAD
is numerical evidence, not an interval certificate. The separate outward
checker above certifies one witness without changing this record. Keep
large regenerable data outside Git
=======
is numerical evidence, not an interval certificate; the certified
witnesses come from the 14 October program above. Keep large regenerable data outside Git
>>>>>>> dce5643 (Manuscript for euler control)
>>>>>>> 94745f3 (Merged work from ChatGPT)
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
