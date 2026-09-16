# Small checks and retained records

These programmes support the written calculations in
[the notes](../notes/README.md). They use Python's standard library only and
print JSON to standard output; they do not write or overwrite a record.
Exact rational algebra is labelled separately from floating-point work.

| Programme | Preserved record | Scope |
|---|---|---|
| [check_density_symbol.py](check_density_symbol.py) | [density-symbol-checks.json](records/density-symbol-checks.json) | 77 checks of the density identity $b(\tau^2)+w_0=2\theta'(\tau)$: the series and digamma forms of $b$ with an explicit tail bound, the contact constant against its closed form, the identity against a central difference of $\arg\Gamma$, the four leading coefficients of the asymptotic expansion, the smooth count at three published ordinates, and the sign structure of the symbol including $\tau_*$, the prime ladder and the negative band $\tau_L$. |
| [check_symbol_split.py](check_symbol_split.py) | [symbol-split-checks.json](records/symbol-split-checks.json) | 32295 checks of the symbol split: the closed-form Toeplitz gamma energy against direct quadrature of (2.5), both compression identities as finite matrix identities at seven values of $L$, Cholesky certificates that the subtracted form and the negative-part multiplier are positive and that the new source side is smaller, and one-sided saturation quotients for the two presentations. |
| [check_qweyl_relations.py](check_qweyl_relations.py) | [qweyl-relations-checks.json](records/qweyl-relations-checks.json) | 292 exact rational checks identifying the elementary Schur representation of Section 6.1 as the generalized $q$-Weyl algebra with $P(y)=1+y$: the two product relations, the grading relations, Klyuev's defining relations under the assignment $U=u_-$, $V=u_+$, $Z=v$, and the resulting root data. |
| [check_levy_dirichlet.py](check_levy_dirichlet.py) | [levy-dirichlet-checks.json](records/levy-dirichlet-checks.json) | 11555 checks that the non-pole part of the target is a single jump Dirichlet form: the Lévy--Khinchine decomposition as a matrix identity at five values of $L$, the jump structure of the energy (nonpositive off-diagonal, nonnegative spectrum), Beurling--Deny cone positivity of the resolvent, the destruction of that cone by the rank-two pole term, and the ground-state identity. |

Run from the investigation directory:

```sh
python3 numerics/check_density_symbol.py
python3 numerics/check_symbol_split.py
python3 numerics/check_qweyl_relations.py
python3 numerics/check_levy_dirichlet.py
python3 validation/drafts.py check --replay
```

Counts refer to finite test cases, not independent theorems.

The saturation quotients in the symbol-split check are **one sided** in the same
way as the sibling investigation's compression check: they are Rayleigh
quotients in a 48-cell step subspace, so a value above one would certify that
the domination fails while a value below one certifies nothing. The cell basis
is deliberately coarse, so the absolute values sit far above those of a finer
Fourier--Galerkin space; the ratio between the two presentations is what the
programme is for.

The $q$-Weyl check verifies operator identities on a domain of finite Laurent
states. It identifies the algebra, not the physical adjoints, which Section 6.1
of the sibling manuscript inherits from the doubled representation. It quotes
two theorems of Klyuev and does not reprove them.
