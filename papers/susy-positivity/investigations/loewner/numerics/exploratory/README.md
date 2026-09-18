# Exploratory computations

Programmes here are **not registered check programmes**: they use `mpmath`,
which the repository's conventions exclude from registered checks, and nothing
replays them automatically. They exist so that every number quoted in the
notes is reproducible.

| Programme | Record | Supports |
|---|---|---|
| [transfer_kernel.py](transfer_kernel.py) | [transfer_kernel_omega0.1.json](transfer_kernel_omega0.1.json) | The living copy of the programme written for the inherited Wilson-lines note, Sections 4--5: the causal kernel $k_\omega$ of the transfer assembled from the Beta kernel $k^\Gamma_\omega$, the positive comb $\widetilde c_n$ and the rank-two factor $R_\omega$; checks A--G (Laplace transforms, Dirichlet coefficients, $R\widetilde K=K$, complete monotonicity, the first-order law, the kernel table, and the truncated kernel transform against $K_\omega(p)$, which converges geometrically in the cutoff). `python3 transfer_kernel.py 0.1 2.5`, about two minutes. |
| [decomposition_checks.py](decomposition_checks.py) | [decomposition_checks_omega0.1.json](decomposition_checks_omega0.1.json) | The opening note, Section 4: complete monotonicity of $\widehat K_\omega=\frac{p+a}{p-a}\widetilde K_\omega$; $K_\omega=B_b\widehat K_\omega$; the $\omega=\frac12$ endpoint ($\widetilde K_{1/2}$ is the Eisenstein scattering matrix, the comb weights are $\varphi(n)/n$ in exact rationals); the BESQ/Beta reading of $K^\Gamma_\omega$; the EMA identity $k_\omega=\widehat k_\omega-2\,\mathrm{EMA}_b[\widehat k_\omega]$ at the kernel level against the $R_\omega$ assembly; and the first-order comb weights. `python3 decomposition_checks.py 0.1`, under a minute. |
| [contraction_margin.py](contraction_margin.py) | `cm_om{omega}_log3_N{N}.json`, with suffix `_h20` or `_nested{N'}` where used | The [contraction-margin note](../../notes/CONTRACTION_MARGIN_FIRST_RUN_20260917.md): the compressed transfer $V_{\omega,L}$ assembled in the sine basis from the elementary kernel (closed-form one-sided autocorrelations $S_{jk}$, kernel in local coordinates per atom, substitution $\tau=u^{1/\omega}$, tanh--sinh rule with step $1/h$), then $\lVert V_N\rVert$, $\lambda_{\min}(I-V_N^{\mathsf T}V_N)$, the ratio $\lambda_{\min}/2\omega$ to $m_L^{(N)}$ from `weil_sine_basis.py` (Wilson-lines exploratory folder, imported by relative path), the first-order law on $e_1$, the mass $\int_0^Lk_\omega$, and with a fifth argument $N'>N$ the nested defect $I_N-(V_{N'}^{\mathsf T}V_{N'})_{N\times N}$. `python3 contraction_margin.py 0.01 log3 24 16 > cm_om0.01_log3_N24.json`, 40--60 s per run; `L` written as `log3` is parsed exactly and atoms are taken with $\log n<L$ strictly. Records: $\omega\in\{0.002,0.01,0.02,0.05,0.1\}$ at $N=24$, $1/h=16$; $\omega=0.002$ at $1/h=20$; $\omega=0.01,0.1$ at $N=32$; $\omega=0.1$ at $N=16$; nested $24\subset40$ and $24\subset64$ at $\omega=0.1$ and $24\subset64$ at $\omega=0.05$. `cm_om0.01_log3_N16_h12_edgeatom_stale.json` is an early run kept as the example of the edge-atom sliver (note, Section 5); its numbers are superseded. |

Every value is either an identity checked to working precision or a labelled
quadrature; the notes state which. Nothing here is a positivity certificate.

See the [checks index](../README.md).
