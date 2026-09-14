# Verification scripts — psi_omega_margin (Ψ_ω)

Standalone recomputation scripts for the paper's identities, asymptotics, tables, and
extensions. Each prints its results to stdout; the expected outputs are the numbers quoted in
`../psi_omega_margin.tex` (Section "Numerical verification" and the Dirichlet section) and in
`../supplementary/DERIVATION_AND_VERIFICATION.md`. No zeros of ζ are used except where a script
explicitly sums over them as a cross-check; the substantive asymptotic tests are driven from the
prime side.

```
pip install -r requirements.txt      # mpmath, numpy
python3 c1_xi_values.py              # a few seconds
python3 c2_zero_sums.py             # ~1–2 min (zeta zeros via mpmath.zetazero)
python3 c3_prime_side.py           # ~1–2 min (sieves Λ(n) to e^15 ≈ 3.3·10^6)
python3 c4_series_identity.py     # a few seconds
python3 c5_window.py             # a few seconds
python3 c6_window_kv.py         # a few seconds
python3 c7_dirichlet.py        # ~1 min (finds Dirichlet L-zeros by sign changes)
python3 c8_prime_side_chi.py  # ~1–2 min (sieves Λ(n)χ(n) to e^15)
```

| script | what it checks | paper location |
|---|---|---|
| `c1_xi_values.py` | `(ξ′/ξ)(½+ω)`, its derivative, `B(0)=0.04620998623…`; slope/ω monotone; the withdrawn `u*` roots (documents the correction discussed in the derivation record) | Prop 1.1, Cor "linear margin", margin table |
| `c2_zero_sums.py` | `A(ω), B(ω)` by direct zero sum + Riemann–von Mangoldt tail vs the closed forms; `Σ_ρ (Im ρ)⁻⁴ = 7.4346·10⁻⁵` (the `t₀` constant) | Prop 1.1, Thm "threshold", Table AB |
| `c3_prime_side.py` | prime-side `Ψ_ω(t)` (formula with Λ(n), n^{−½−ω}) vs the asymptotic main term, **no zeros used**; reproduces Suzuki's `Ψ(0.464002)=0.03966175656…`; `Ψ(0)=0` | Thm "asymptotic", Table asym |
| `c4_series_identity.py` | per-γ identity (integral definition ⟷ series) and the exponential decomposition of the remainder, to 30/28 digits at complex γ | Thm "asymptotic" (eqn Rclean) |
| `c5_window.py` | the S-only unconditional positivity window `(t₋, t₊)` from RH verified to 3·10¹² | Prop "window", Table window (`E≡S` column) |
| `c6_window_kv.py` | the zero-free-damped window `E(t)` (MTY regions) and the endpoint law `t₊ ≈ 0.72(½−ω)⁻²` | Prop "window", Table window, endpoint remark |
| `c7_dirichlet.py` | `ξ(s,χ)` functional-equation/reality checks; zero lists and counts for q = 3,4,5; closed forms vs zero sums; conductor trend; positivity of a real (Siegel) zero pair | Dirichlet section, Tables conductor/χ |
| `c8_prime_side_chi.py` | the Γ-block transform lemma (to 10⁻²²) and the prime-side `Ψ_{ω,χ}` vs its main term | Dirichlet section, Prop "χ prime-side", Table χprime |

The scripts are the ones used for the 27 August 2026 recomputation. They supersede an earlier set
(`w1`–`w4`, first-round derivation and checks) whose results they reproduce and extend.

[Shifted-zeta program](../../README.md) · [All manuscripts](../../../README.md)
