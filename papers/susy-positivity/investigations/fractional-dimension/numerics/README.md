# Checks and records

Check programmes here use the standard library only, print JSON to standard
output, and keep a preserved record under [`records/`](records/). Once this
investigation has a manuscript they are registered in the `CHECKS` dictionary of
its `validation/drafts.py` and replayed with it; until then the records are
preserved but nothing replays them automatically.

| Programme | Preserved record | Scope |
|---|---|---|
| [check_dimension_dictionary.py](check_dimension_dictionary.py) | [dimension-dictionary-checks.json](records/dimension-dictionary-checks.json) | The dictionary of the opening note, 72 cases in four groups: the comb weights against the Jordan totient, $\widetilde c_n=J_d(n)/n^{(d+1)/2}$, for $n<120$ at seven shifts; $J_d(n)$ against brute-force counts of the primitive vectors in $(\mathbb Z/n\mathbb Z)^d$ for $d\in\{1,2,3\}$, $n\leq12$, and $\widetilde c_n=\varphi(n)/n$ at $d=1$ in exact rationals; $J_d$ as the Dirichlet coefficient of $\zeta(u-d)/\zeta(u)$ by Möbius convolution at six $d$, fractional ones included; and the reparametrization $d=2\omega$, $s=(p+b)/2$, including the Gamma factors and the Blaschke pole at $(d+1)/2$. **No value of $\zeta$ or $\xi$ is computed anywhere in it.** Under a second; `python3 numerics/check_dimension_dictionary.py`. |

The archimedean half of the dictionary --- the Riesz integral over
$\mathbb R^{d}$, the sphere area $|S^{d-1}|$, and the push-forward --- is
established and checked in the parent investigation
([`check_beta_realization.py`](../../loewner/numerics/check_beta_realization.py),
group E) and is not duplicated here.

Counts refer to finite test cases, not independent theorems, and no check here
is a positivity certificate.
