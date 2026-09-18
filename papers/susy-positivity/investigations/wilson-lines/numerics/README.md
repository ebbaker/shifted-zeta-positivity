# Small checks and retained records

## Active endpoint-matter continuation

[check_endpoint_matter.py](check_endpoint_matter.py) supplies **154 finite checks**
in seven groups: parity kernels, difference energy, subtracted transform,
weight variation, semicircle Clifford algebra, shifted determinant and generator,
and the cutoff logarithm. Its [preserved record](records/endpoint-matter-checks.json)
is replayed by the separate [continuation registry](../validation/endpoint_matter.py):

```sh
python3 numerics/check_endpoint_matter.py
python3 validation/endpoint_matter.py check --replay
```

It uses only the standard library and writes JSON to standard output. These
checks support the two new research notes; they are not yet registered as
manuscript contents. On manuscript integration, migrate them into `drafts.py`
and rebuild and review the manuscript normally.

**Baseline audit:** all 1067 legacy cases pass their internal tolerances in the
18 September runtime, but strict legacy replay differs in five floating-point
error diagnostics across two programs. The original records remain unchanged.
[The audit](records/endpoint-baseline-replay-audit.json) records every difference.
Package/snapshot identity checks still pass. A successful numerical check is
not a proof of any physical interpretation discussed in the notes.

## Legacy manuscript checks

This program supports the written calculations in the
[manuscript](../manuscript.pdf) and [the notes](../notes/README.md). It uses
Python's standard library only and prints JSON to standard output; it does not
write or overwrite a record. Exact rational algebra is labelled separately from
floating-point work.

| Programme | Preserved record | Scope |
|---|---|---|
| [check_causal_commutation.py](check_causal_commutation.py) | [causal-commutation-checks.json](records/causal-commutation-checks.json) | 206 checks in seven groups: that truncation to an interval is multiplicative on causal kernels, $P_LAP_LBP_L=P_LABP_L$, as an exact rational matrix identity; that truncated causal convolutions commute, exactly, with the control that truncated non-causal ones do not, so that causality is what the argument uses; that the causal pole kernel $4\cosh(\omega x)\cosh(x/2)\mathbf 1_{x>0}$ symmetrizes to $2\cosh(\omega(x-y))\cosh(\frac{x-y}2)$ and at zero shift to $2|C(f)|^2-2|S(f)|^2$; that the same symbol has exactly vanishing real part on the imaginary axis; the hyperbolic identity as a finite matrix identity at three shifts and three lengths; the endpoint algebra in exact rational arithmetic ($G_{\omega,L}B_L=0$, the one-sided commutator $[G,B_L]=-B_LG$, and the integrated form of $\partial_LG_{\omega,L}=B_LG_{\omega,L}$); and a Blaschke resonance model in which each factor is exactly unimodular and $|b-1|^2$ is exactly the Lorentzian $4\omega^2/(\omega^2+(\tau-\gamma)^2)$, with its mass and the summed group delay checked in floating point. |

| [check_sampling_forms.py](check_sampling_forms.py) | [sampling-forms-checks.json](records/sampling-forms-checks.json) | 336 checks in five groups, supporting the [frame-bound note](../notes/FRAME_BOUND_AND_THE_DENSITY_20260917.md): the sine-basis closed forms $S_{jk}$ and $E_j^{\pm}$ against direct quadrature; the three families of archimedean integrals against $n(r)=e^{-r/2}/(1-e^{-2r})$, summed in closed form through $\psi$ and $\psi'$ at $\tfrac14$ plus a geometric remainder, against quadrature, together with $\int_L^\infty e^{-r/2}n(r)\,dr=\operatorname{artanh}(e^{-L})$; the assembled matrix element $Q_{jk}$ against a direct sum over one hundred published zero ordinates plus a smooth tail (agreement $1.8\times10^{-4}$, limited by the tail, so this checks the assembly and not the arithmetic of $\zeta$); the sampling budget, $D(L)=2e^{L}-\tfrac74$ exactly and the count crossover $T_*=2\pi e^{L+1}$; and the convention bookkeeping against [arXiv:2608.24827](https://arxiv.org/abs/2608.24827), whose prime mass $A_{L}$ at its $L$ is this investigation's comb at $2L$. |

Run from the investigation directory:

```sh
python3 numerics/check_causal_commutation.py
python3 numerics/check_sampling_forms.py
python3 validation/drafts.py check --replay
```

Counts refer to finite test cases, not independent theorems.

| [check_delay_test.py](check_delay_test.py) | [delay-test-checks.json](records/delay-test-checks.json) | 525 checks in eight groups, supporting the [delay-test note](../notes/THE_DELAY_TEST_20260917.md), the [expansion note](../notes/THE_ARCHIMEDEAN_EXPANSION_20260917.md) and the [quarter-shift survey note](../notes/THE_QUARTER_SHIFT_SURVEY_20260917.md): the causal symbol of a ray-frame defect two-point function against direct quadrature; its boundary-channel decomposition into primary plus descendants with positive coefficients; the closed form $\mathcal T_\Delta(\tau)=\pi\operatorname{Re}\cot(\pi(\Delta+i\tau))$ for the group delay, its total $\pi(\frac12-\Delta)$, and its identical vanishing at half-integer $\Delta$; the Stieltjes bound $\arg\in(-\frac\pi2,0)$ for arbitrary positive spectral measures, with the accumulated delay below $\frac\pi2$ at every horizon; that $e^{2i\theta}$ is unimodular and $\int_0^T2\theta'=2\theta(T)$ is unbounded; and the two objects that do wind --- the half-line inverted oscillator, exactly $\log\pi$ from the target, and the Liouville reflection amplitude at $4Q\log P$; and the delay expansion, with $\Lambda$ equal to the degree, the sign window $|a-\frac12|<\frac1{2\sqrt3}$, the rigidity bound attained only at $a\in\{\frac14,\frac34\}$, and the two-shift solution that shows its hypothesis is needed. Group H adds the graded invariants: the expansion checked against the delay assembled from $\operatorname{Re}\psi$, including the decisive test on the universal prefactor $(-1)^{m+1}/m$ (the residual left by the correct truncation falls like $\tau^{-6}$, the one left by setting the prefactor to $1$ only like $\tau^{-4}$); the targets $I_{2m}=2^{2m-1}B_{2m}(\frac14)$ in exact rational arithmetic; the degeneracy $B_{2m}(\frac12)=2^{2m}B_{2m}(\frac14)$ exactly to $m=8$; the single-factor formula and its independence of the width; the classification $(a,n)\in\{(\frac14,\pm1),(\frac34,\pm1),(\frac12,\pm\frac12)\}$ with a grid search finding nothing beyond it; every row of the survey table; the closed-form counterexample at $r=\frac{17+\sqrt{33}}{16}$ with $I_4=\frac5{384}$; the two-factor family and the bisection sweep locating exactly the two $I_6$ roots; the Legendre duplication identity behind them in squared form; the modular-surface shift together with the unimodular factor $\frac{2s-2}{2s}$ separating $\Lambda_\zeta$ from $\xi$ and the $+\frac{11}6$ it would produce; and the counterexample at $a=\frac{4-\sqrt5}8$ to the unrestricted rigidity claim, with the scan that finds no common-shift configuration with $n_j\leq6$ matching $I_4$. Standard library only, and deliberately free of $\zeta$ and $\xi$ --- the modular-surface identities that need them are in `exploratory/quarter_shift_survey.py`. |

All three are registered in the `CHECKS` dictionary of
[`validation/drafts.py`](../validation/drafts.py) as of manuscript 0.5;
`drafts.py check --replay` runs all three and requires byte-identical output,
$1067$ cases in total. Strict cross-runtime replay has the qualification recorded above.

Separately, [`exploratory/`](exploratory/README.md) holds programmes that are
**not** registered: they use libraries the conventions exclude and
`drafts.py check --replay` does not run them. At present nine, all requiring `mpmath`: one reproduces the numbers quoted in the
[inner-function note](../notes/INNER_FUNCTION_AND_RESONANCE_20260917.md), and eight
assemble the localized Weil form in a sine basis and produce every table of the
[frame-bound note](../notes/FRAME_BOUND_AND_THE_DENSITY_20260917.md).

The floating-point groups carry worst-case relative errors in the record; they
are matrix identities, not approximations of an analytic quantity, so the errors
are quadrature and rounding only. The resonance group takes the first twelve zero ordinates, truncated to exact
rationals, as **published input data**; the Blaschke identities hold for any
rational $\gamma$, so that group verifies the mechanism of the manuscript's
Section 4 and not the arithmetic, and nothing here computes with $\xi$ or
$\zeta$. The program verifies none of the convergence arguments in the proof of
Theorem 3.1, nothing about operator domains (so it says nothing about
Proposition 8.5), and nothing about the limits of Propositions 7.1 and 7.2. No check here is a
positivity certificate.
