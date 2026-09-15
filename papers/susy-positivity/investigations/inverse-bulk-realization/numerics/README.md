# Small algebra checks and retained records

These programs support written calculations in [the notes](../notes/README.md).
They use Python's standard library and print JSON to standard output;
they do not write or overwrite a record. Numerical illustrations are
labelled separately from exact rational algebra.

| Program | Preserved record | Scope |
|---|---|---|
| [check_matching.py](check_matching.py) | [matching-checks.json](records/matching-checks.json) | 153 finite checks of gamma refinement, composition, and the rational-feedback identity. |
| [check_gauge_transfer.py](check_gauge_transfer.py) | [gauge-transfer-checks.json](records/gauge-transfer-checks.json) | 326 finite checks for winding, transfer, branch cusps, and coherent contact; includes a labelled floating-point illustration. |
| [check_sphere_schur.py](check_sphere_schur.py) | [sphere-schur-checks.json](records/sphere-schur-checks.json) | 251 finite checks of rank-one norms, Schur product ratios, common-state interference, and repetition coefficients; includes a labelled overlap illustration. |
| [check_dressed_schur.py](check_dressed_schur.py) | [dressed-schur-checks.json](records/dressed-schur-checks.json) | 587 finite exact checks for magnetic actions, the full prime norm, domain cancellation, and mixed-return coefficients. |
| [check_explicit_formula.py](check_explicit_formula.py) | [explicit-formula-checks.json](records/explicit-formula-checks.json) | 8 labelled floating-point checks: self-computed zeta zero ordinates against published values, and both sides of the explicit formula for smooth inputs on three intervals. |
| [check_channel_bound.py](check_channel_bound.py) | [channel-bound-checks.json](records/channel-bound-checks.json) | 75 evaluations of the interference bound: the two exclusion certificates, the indicator scan, and consistency of the $t=1$ value with the Weil form. |
| [check_mirror_subtraction.py](check_mirror_subtraction.py) | [mirror-subtraction-checks.json](records/mirror-subtraction-checks.json) | 75 checks for the mirror prime reference: exact rational Laurent coefficients and the complementarity sum rule, nonnegativity samples, the prime-free subtraction identity on step inputs, and one-sided Rayleigh quotients. |
| [check_prime_free_archimedean.py](check_prime_free_archimedean.py) | [prime-free-archimedean-checks.json](records/prime-free-archimedean-checks.json) | 78666 checks for the prime-free archimedean inequality: the cell-basis gamma matrix against the step routine, the identity $A_L=Q_L$ below $\log 2$, the parity split, one-sided Galerkin quotients, the two-scalar parity reduction, a step certificate that the bare archimedean form fails at $L=3/4$, the sufficient criterion at every prime breakpoint below $10^6$, and the three algebraic ingredients of the theorem on random step inputs. |

Run from the investigation directory:

```sh
python3 numerics/check_matching.py
python3 numerics/check_gauge_transfer.py
python3 numerics/check_sphere_schur.py
python3 numerics/check_dressed_schur.py
python3 numerics/check_explicit_formula.py
python3 numerics/check_channel_bound.py
python3 numerics/check_mirror_subtraction.py
python3 numerics/check_prime_free_archimedean.py
```

Counts refer to finite test cases, not independent theorems. In the sphere/Schur
check, truncated products retain their end factors and the truncated
state retains the final shifted coefficient. The infinite identities,
their domains, and the source-selection arguments are discussed in the
[sphere/Schur note](../notes/SPHERE_AND_SCHUR_PAIRINGS.md). The
[dressed-return note](../notes/SCHUR_DRESSED_RETURNS_AND_GLUING.md)
gives the subsequent source construction and analytical qualifications;
its check retains the shifted boundary coefficient of every finite vector.

The prime-free archimedean check mixes three kinds of statement and labels them.
Its Galerkin quotients are one sided in the same way as the mirror-subtraction
check: they live in a step subspace, so a negative value certifies that a form
is not positive while a positive value certifies nothing. The certificate at
$L=3/4$ is of the first, conclusive, kind. The scan of the sufficient criterion
over prime breakpoints is a finite floating-point verification of an explicit
elementary inequality, with margins above $0.55$, and it supports a proof of
$A_L\ge 0$ for $L\ge\log 7$; the complementary range $L<\log 7$ is not settled
by it, and nothing here certifies Weil positivity.

The mirror-subtraction check is one-sided by construction: a Rayleigh
quotient above one in the step subspace certifies that a domination fails,
while a value below one is a lower bound and certifies nothing. It supports
the [subtraction-form note](../notes/MIRROR_REFERENCE_AND_SUBTRACTION_FORM.md)
rather than the manuscript.

The explicit-formula and channel-bound programs are floating-point rather than
exact rational. The
explicit-formula check computes zeta zero ordinates from the Hardy function
and is a normalization check only: its ordinates lie on the critical line by
construction, so it is not evidence for RH. The channel-bound check evaluates
finite closed forms for step-function inputs and reports an explicit tail
bound for its one infinite series. The first four programs and their record
contents are unchanged by the reorganization. Keep any future replay output separate from these
preserved records. The checks do not construct a field theory, verify
an infinite-dimensional proof, or certify Weil positivity. No large data
or positivity sweep is part of this investigation; follow
[LARGE_FILES.md](../../../../../LARGE_FILES.md).
