# The target is one jump Dirichlet form; the cone it carries; and what the cone can give

**Author: Claude Opus 5 (Anthropic).** 16 September 2026. Pursues the
Ruelle-Perron-Frobenius / Birkhoff route identified in
[the sweep](EXISTENCE_MECHANISM_SWEEP_20260916.md), §2, and records what Suzuki's
screw-function paper actually proves. Checked by
[`check_levy_dirichlet.py`](../numerics/check_levy_dirichlet.py).

## 0. Summary

1. **The archimedean and prime halves of the target are the continuous and
   atomic parts of one nonnegative Levy measure.** The whole non-pole part of
   `Q_L` is a single **jump Dirichlet form**. One object, not two channels —
   which is what Theorem 7.5 of the sibling manuscript demands.
2. **That form carries a genuine Perron-Frobenius cone**, exactly as
   Beurling-Deny predicts: its resolvent is positivity preserving. Verified.
3. **The rank-two pole term destroys it**, at every `L` and even with a
   comfortably positive constant: 40 to 73 per cent of the inverse's entries go
   negative. A third independent appearance of the pole form as *the*
   obstruction.
4. **And even with a cone, Krein-Rutman and Birkhoff cannot bound what needs
   bounding.** The one cone theorem that bounds a spectral radius is
   **Collatz-Wielandt**, which needs a pointwise supersolution — and that is
   precisely what the pole blocks. This is the verdict on the route.
5. A by-product: Weil positivity on `I_L` is exactly a **ground-state energy**
   statement for the jump form.
6. Suzuki's `A_a` results are unconditional and the manuscript should be citing
   them; his `lambda_a ~ log(1/a) - log(2pi)` is our density symbol evaluated at
   the interval's own frequency scale (§6).

## 1. The target is one jump Dirichlet form

By (2.5)-(2.6) the archimedean symbol is already in Levy-Khinchine form,
`b(tau^2) = int_0^inf 2(1 - cos(tau r)) ngamma(r) dr`. The prime part becomes one
after adding and subtracting its value at `tau = 0`:

```
 Psi_L(tau) = b(tau^2) + w0 - 2 sum_{m log p < L} (log p) p^{-m/2} cos(tau m log p)
            = Phi_L(tau) + gamma_L,
 Phi_L(tau) = int (1 - cos(tau r)) dmu_L(r),
 mu_L       = 2 ngamma(r) dr + 2 sum_{m log p < L} (log p) p^{-m/2} delta_{m log p},
 gamma_L    = w0 - 2 sum_{m log p < L} (log p) p^{-m/2}.
```

`mu_L >= 0`, so `Phi_L` is a continuous negative definite function and its form is
a jump Dirichlet form. Therefore, exactly,

```
 Q_L[f] = E_{mu_L}[E_L f] + gamma_L ||f||^2 + P_L[f].                       (D)
```

Verified as a matrix identity to `1e-17`, with `E_{mu_L}` having nonpositive
off-diagonal entries and nonnegative spectrum.

**This is the best answer I have to the architecture problem.** Theorem 7.5 says
the archimedean and prime data cannot be two positive channels; the previous
note observed that the two halves call for different physical mechanisms (a
density of states, a periodic-orbit sum). (D) says they are not two things at
all: they are the **continuous and atomic parts of a single Levy measure**, and
the source they ask for is a **jump process whose jumps are the primes**, with
`2 (log p) p^{-m/2}` the mass at jump length `m log p`. That is one mechanism.

`gamma_L = w0 - 2 sum_{m log p < L} (log p) p^{-m/2}` is large and negative
(`-6.35` at `L = 1`, `-18.39` at `L = 3`, asymptotically `w0 - 4 e^{L/2}` by the
prime number theorem). It is a different bookkeeping from `c_L` of (7.20), which
uses the mirror contact `2dr/(1+r)` rather than the full `2dr^n`.

## 2. The cone exists, for the jump form

In the cell basis a nonnegative function is a nonnegative coefficient vector, so
a cone-positive operator is an entrywise nonnegative matrix. By Beurling-Deny the
resolvent of a Dirichlet form is positivity preserving, and it is:
`(K + lambda)^{-1}` has **no** negative entries at `lambda = 1` and `lambda = 5`,
at every `L` tested. (Separately, `(K + c_L)^{-1}` is also entrywise nonnegative
wherever it is still positive definite, which fails at `L = 1` — that failure is
the known death of the bare archimedean form at small `L`.)

So the archimedean-plus-constant part genuinely carries the structure the
Ruelle-Perron-Frobenius mechanism needs.

## 3. The pole destroys it

Adding the rank-two pole form `P_L = u v^T + v u^T`:

| `L` | 0.8 | 1.0 | 1.5 | 2.0 | 3.0 |
|---|---|---|---|---|---|
| negative fraction of `(K + 5)^{-1}` | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| negative fraction of `(K + 5 + P_L)^{-1}` | 0.404 | 0.511 | 0.640 | 0.703 | 0.734 |

and it gets worse with `L`. The mechanism is Sherman-Morrison: adding a rank-one
`sigma w w^T` subtracts `sigma (A^{-1}w)(A^{-1}w)^T / (1 + sigma w^T A^{-1} w)`
from the inverse, and when `A^{-1} >= 0` entrywise and `w >= 0` — as
`cosh(x/2) > 0` is — that subtraction is a nonnegative rank-one, which drives
entries negative. **Even the positive half of the pole form breaks inverse
positivity.** So `A_L^{-1}` is not cone positive, and `A_L^{-1} sum_p Bt_p` is
not a cone map on the pointwise cone.

This is the third independent appearance of the pole form as the obstruction,
after Proposition 7.3 (no orthogonal augmentation) and the parity split (2.17).

## 4. What a cone can and cannot give — the verdict

Four facts, which together settle the route.

**(a) The existence of an invariant cone is automatic and carries no
information.** By Vandergraft's theorem a matrix leaves some proper cone
invariant as soon as its spectral radius is an eigenvalue — which for the
self-adjoint `A_L^{-1/2} B A_L^{-1/2}` is always. So "is there a cone?" is the
wrong question; "is there a *usable* one, supplied by the structure?" is the
right one, and §3 answers no for the pointwise cone.

**(b) Krein-Rutman gives nothing beyond the spectral theorem here.** Its value in
dynamics is that a transfer operator is *not* self-adjoint and has no a priori
spectral theory, so the existence of the leading eigenpair is real content. Our
operator is self-adjoint by construction; the Perron pair exists for free.

**(c) Birkhoff bounds the gap, not the radius.** A contraction ratio
`tanh(Delta/4)` in the Hilbert projective metric controls
`|lambda_2|/|lambda_1|` and the convergence to the leading eigenvector. It says
nothing about `lambda_1` itself, which is the only thing Weil positivity is
about. **This retires the test proposed in the sweep, §2:** the projective
diameter would not have decided anything even had the cone been invariant, and
it is not.

**(d) The one cone theorem that does bound a spectral radius is
Collatz-Wielandt.** For a cone-positive `M`,
`r(M) = inf{ lambda : exists u in int C with M u <= lambda u }`. So a **single
pointwise supersolution** would certify `r <= 1`, converting the operator
inequality `sum_p Bt_p <= A_L` into a pointwise inequality between two explicit
functions. *That* is what a cone is worth here, and it is exactly what §3 blocks.

**Verdict.** The Ruelle-Perron-Frobenius mechanism is not available for this
problem in the pointwise cone, and the reason is the pole term rather than
anything about the primes. The route is not refuted in general — a cone adapted
to the pole directions, or Rugh's complex-cone theory, is untouched — but the
naive and natural version is closed, and the prize (a Collatz-Wielandt pointwise
certificate) is now named precisely enough that one can tell whether a
replacement cone would deliver it.

## 5. A ground-state reformulation

From (D), `lambda_min(E_{mu_L} + P_L ; ||.||^2) = -gamma_L + lambda_min(Q_L)`, so

> **Weil positivity on `I_L` says exactly that the ground-state energy of the
> jump Dirichlet form together with the pole term is at least
> `2 sum_{m log p < L} (log p) p^{-m/2} - w0`.**

Verified: at `L = 1` the ground state is `6.354438` against `-gamma_L = 6.352442`;
at `L = 3`, `18.389021` against `18.387837`. The gap is `lambda_min(Q_L)`, and in
this coarse 48-cell basis it is `~1e-3`.

This is a re-presentation, not a theorem — but it puts the criterion in a form
where spectral-gap technology for **nonlocal Dirichlet forms on an interval** is
the relevant apparatus, which is a large and well-developed literature that this
programme has not touched.

## 6. Suzuki's screw-function paper, read

Read from the PDF of arXiv:2606.09096 (the manuscript's `\bibitem{Suzuki}`,
currently cited only for the normalization in Section 2.1). `A_a` is the
self-adjoint operator on `L^2(-a,a)` with `Q^a_W(v) = <A_a v, v>`; our `I_L`
corresponds to `a = L/2`. **Nothing below assumes RH.**

- **Theorem 1.1.** `A_a` is the Friedrichs extension of a symmetric operator `B_a`.
- **Theorem 1.3.** The lowest eigenvalue `lambda_a` is continuous in `a`.
- **Theorem 1.4.** For sufficiently small `a > 0`, `lambda_a` is **positive and
  simple**, and
  `lambda_a = log(1/a) + mu_1 - log(2 pi) + psi(2) - 1 + O(a)`.
- **Theorem 1.5.** `W(a,theta;z)` is entire, the eigenvalues of `D_{a,theta}` are
  its zeros, and all zeros are real.
- **Corollary 1.6** is a conjecture: a limit `a -> infinity` of `W(a,theta;z)`
  reproducing `xi` would give RH.

**A consistency check that is worth recording.** Our density identity says the
symbol is `2 theta'(tau) = log(tau/2pi) + O(tau^{-2})`. An interval of half-width
`a` has natural frequency scale `tau ~ 1/a`, giving `log(1/a) - log(2 pi)` —
**exactly the first two terms of Suzuki's Theorem 1.4**, constant included. His
small-`a` eigenvalue law is our density symbol evaluated at the interval's own
scale. That is independent corroboration of the density identity from a
completely different route, and it is not in either place.

**What the sibling manuscript should do.** Theorems 1.3 and 1.4 are unconditional
statements about exactly the object of Section 7.6 and of selection rule 7, and
the companion numerical paper (arXiv:2607.24830) reports `lambda_1(a)` positive
and superexponentially decaying. The manuscript cites this paper for a
normalization only. A corrected citation, together with the correction to Section
7.6's saturation figures identified in
[the fixed-point note](FIXED_POINTS_AND_THE_MARGIN_20260916.md), §5, is drafted
and ready; I have not edited `manuscript.tex`, since the working preference is to
finish an investigation before amending it.

## 7. Where this leaves the route

1. **Closed:** the pointwise cone, Birkhoff's diameter test, and any hope that
   Krein-Rutman supplies something the spectral theorem does not.
2. **Open and now precisely stated:** is there a cone, adapted to the pole
   directions, in which `A_L^{-1} sum_p Bt_p` is positive? The prize is a
   Collatz-Wielandt pointwise supersolution. Rugh's complex-cone theory
   (Ann. Math. 171 (2010) 1707-1752) is the tool for indefinite forms.
3. **New and worth pursuing on its own:** the jump-Dirichlet-form presentation
   (D) and the ground-state reformulation of §5. Nonlocal Dirichlet forms on an
   interval have a substantial spectral-gap literature; none of it has been
   applied here. This is the most promising thing to come out of the sweep.
4. **A selection rule follows from (D):** a source must be a jump process whose
   Levy measure is `mu_L` — continuous part `2 ngamma`, atoms `2 (log p) p^{-m/2}`
   at `m log p`. That is sharper than rules 3 and 4 together, and it is one
   condition rather than two.

## 8. Status

- §1's decomposition (D): **proved** (two lines of Levy-Khinchine bookkeeping)
  and verified as a matrix identity to `1e-17`.
- §2 and §3: **numerical**, in one 48-cell discretisation. §2 is predicted by
  Beurling-Deny; §3 is the finding, and the Sherman-Morrison explanation of it is
  mine and is elementary.
- §4(a) cites Vandergraft's theorem, quoted not reproved; (b), (c), (d) are
  standard facts about Krein-Rutman, Birkhoff and Collatz-Wielandt, and the
  verdict drawn from them is mine.
- §5: an exact consequence of (D), verified numerically.
- §6: read from the paper's PDF this session. The consistency check between
  Theorem 1.4 and the density identity is **mine**.
