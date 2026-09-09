# Laboratory scripts — defect-depth (Ihara lab)

The finite graph-zeta laboratory in which the paper's mechanisms were found and certified.
`lab_ihara_core.py` is the shared machinery; `lab_ihara_experiments.py` is the concatenated
experiment record through round 5 — split it on the `### FILE:` markers and run each piece as
its own module (each begins `from lab_core import *`, so save the core as `lab_core.py` or
adjust the import). All output goes to stdout; expected values are quoted in the paper's
tables and the laboratory round records.

```
pip install -r requirements.txt      # mpmath, numpy
```

| section of `lab_ihara_experiments.py` | what it checks | paper location |
|---|---|---|
| `v1_validate.py` | core machinery: K4 closed-form ζ_X, Bass identity, Stieltjes-string round trips, q_ω consistency, Ψ growth of a real pair | §2 (setting), App. conventions |
| `e2_census.py` | Ramanujan census of cubic graphs; string tables; IR dominance | §2 (graph model) |
| `e3_universality.py` | per-vertex strings vs the Kesten–McKay universal-cover limit | §2 (background regularity) |
| `e4_e5.py`, `e5_fix.py` | defect anatomy: exc± types, CF anomaly positions, Pick-count staircase and support leak along the ω-flow | §3 (defect classes), §5 |
| `e6_covers.py` | bipartite doubles (Artin-like splitting); violation-position law | §3 |
| `r2a_full_structure.py` | complete Ihara analytic structure: tower completion, graph Γ-factor, completed positive length | §2 |
| `r2c_hankel.py` | Hankel/CF detection depth vs the interval Green function (synthetic defects on a Ramanujan background) | §4, Thm 3 |
| `r3b_zeta.py` | rank-two CD-kernel detection curve on a genuine ζ-ordinate background; time/depth duality | §5–6, Thms 5, 8 |
| `r3_irregular.py` | GM-switching pair: A-cospectral, Ihara-distinct (existence exhibit) | §3 remark |
| `r5_w1.py` | the compactified moment lemma (binomial transform ≡ Taylor jet) and the W1 depth-law table on the genuine a.c. ω>0 measure | Thm 1, Thm 6, Table W1 |

Rounds 4 and 6 also ran inline scripts (crossover scans; amplitude certification, s₀
five-point scan, unscaled real-ζ suite, envelope bracketing) that were recorded in the round
notes but not saved as files; reconstructing them here is a pre-release item (`../STATUS.md`).
Precision: the Hankel-grade runs use mpmath at dps 140–400; `r5_w1.py` takes ~10–20 min.
