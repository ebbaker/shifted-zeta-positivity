# Pair marginals, Montgomery's statistic and Rodgers–Tao's spacing input

8 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance. Actual backend model and effort are
not exposed in the authenticated source. Branch chat0002, thread
`01a1b9b5-ffde-71a3-b103-2fc9a7eeffca`.

**Status: explanatory clarification and classical calculation, not a new
canonical-zero estimate, assessment or research task.** This makes the
author's marginalization proposal precise and supplements
[goal-alignment Note05](05_TND_OC_AUTHOR_GOAL_ALIGNMENT_20261108.md).

## The spacing contradiction

Under their contradiction hypothesis Lambda<0, Rodgers–Tao obtain at
time zero, for a proportion 1-o(1) of the indices in their dyadic window,

\[
x_{j+1}(0)-x_j(0)=\frac{4\pi+o(1)}{\log T}.
\]

Their normalization is x_j(0)=2 gamma_j. Thus normalized consecutive
gaps approach 1 for almost all indices. Section9 invokes the theorem of
Conrey, Ghosh, Goldston, Gonek and Heath-Brown: for any b>0.77, a positive
proportion of consecutive gaps are at most b times the mean. Choosing
b=0.8 contradicts the preceding density-one conclusion. Full GUE
statistics or arbitrarily tiny normalized gaps are not needed.
[Rodgers–Tao v5, section9, especially (93)](https://arxiv.org/html/1801.05914v5#S9).
This records the result as invoked there; the original small-gap proof
has not been independently audited here.

## Integrating out all but two particles

For a symmetric normalized N-particle density p_N, with fixed N>=2,

\[
p_2(z_1,z_2)=\int p_N(z_1,\ldots,z_N)\,dz_3\cdots dz_N,
\qquad \rho_2=N(N-1)p_2.
\]

The first is a two-label probability marginal; the second is the ordered
factorial pair intensity. The same operation works for measures, without
an ordinary density. Indeed, for a finite multiset of actual zeros define

\[
P_N=\frac1{N!}\sum_{\sigma\in S_N}
  \bigotimes_{r=1}^N\delta_{z_{\sigma(r)}}.
\]

Counting the (N-2)! permutations with a given ordered pair in slots 1,2
gives exactly

\[
N(N-1)(\pi_{12})_*P_N=\sum_{j\ne k}\delta_{(z_j,z_k)}.
\]

Thus the proposed marginal exists even for deterministic zeros. Random
labeling supplies no extra estimate. Multiplicity copies are distinct
indices: a zero of multiplicity m contributes m(m-1) geometric-diagonal
pairs. Localization can insert the two weights w(z_1)w(z_2); multiplying
the entire joint law by a product of N weights and renormalizing is a
different operation. For random N, use factorial correlation measures
directly rather than pulling out a fixed N(N-1).

## An explicit model calculation producing the Montgomery density

For CUE eigenangles the symmetric joint density is

\[
p_N(\theta_1,\ldots,\theta_N)=
\frac{1}{N!(2\pi)^N}
\prod_{j<k}|e^{i\theta_j}-e^{i\theta_k}|^2.
\]

Use the orthonormal functions e^{ik theta}/sqrt(2 pi), 0<=k<N.
Expanding the squared Vandermonde determinant and integrating the other
N-2 variables by orthogonality yields

\[
\rho_2(\theta,\psi)=K_N(\theta,\theta)K_N(\psi,\psi)
                         -|K_N(\theta,\psi)|^2,
\quad
K_N(\theta,\psi)=\frac1{2\pi}\sum_{k=0}^{N-1}e^{ik(\theta-\psi)}.
\]

Unfold u=N theta/(2 pi), v=N psi/(2 pi) so the mean density is one.
For fixed separation s=u-v, the geometric sum gives

\[
R_{2,N}(s)=1-\left(\frac{\sin\pi s}{N\sin(\pi s/N)}\right)^2
\longrightarrow
1-\left(\frac{\sin\pi s}{\pi s}\right)^2.
\]

Values at removable singularities are defined by continuity. This is
precisely a pair correlation obtained by marginalizing a full joint law.
The determinantal correlation construction, circle ensemble and sine
kernel are described in [Borodin v1, (2.1), (2.2), Theorem4.1 and section9](https://arxiv.org/pdf/0911.1153v1).
Borodin's simple-process convention is not used to remove multiplicity
copies from the separate empirical-zero construction above. This model
calculation does not identify the joint law of canonical zeta zeros.

## Montgomery's F and the pair density are different representations

With A_T=T log(T)/(2 pi), a_T=log(T)/(2 pi) and w(u)=4/(4+u^2), set

\[
d\mu_T=\frac1{A_T}\sum_{0<\gamma_j,\gamma_k\le T}
w(\gamma_j-\gamma_k)\,
\delta_{a_T(\gamma_j-\gamma_k)}.
\]

Then Montgomery's F(alpha,T) is the Fourier statistic

\[
F(\alpha,T)=\int e^{2\pi i\alpha s}\,d\mu_T(s).
\]

The self-index terms give (N(T)/A_T) delta_0. The conjectural off-diagonal
limiting pair density is 1-(sin(pi s)/(pi s))^2. The original theorem
assumes RH and establishes restricted-frequency information; the full
unrestricted limiting law is conjectural. A pair statistic counts all
distinct pairs, whereas a nearest-neighbor gap statistic additionally
requires that no zero lie between the pair.
[Montgomery, definitions (1)--(4) and conjecture (12)](https://websites.umich.edu/~hlm/paircor1.pdf).

For the present nonreal-zero goal, retain z_1=x_1+iy_1 and z_2=x_2+iy_2
in a localized factorial measure before choosing a separation projection.
Conjugation can produce singular components; a planar density is not
automatic. Recovering an all-real benchmark is a consistency check.
The substantive missing input is an independently controlled formula or
estimate for this canonical pair measure and its evolution, not the
existence of the marginal operation. Neither CUE/GUE nor a planar random
matrix law is thereby assigned to the actual zeros.

## Scope and source receipt

The [sole register](../../research-progress/01_TND_OC_RESEARCH_PROGRESS_20261107.md)
retains E02 accepted, B02 author checking only and E03 pending. No new B
task, numerical campaign or status promotion follows from this answer.
The [result index](../../../../../../../result-summaries/README.md) and
[avoid index](../../../../../../../avoid/README.md), especially
[classification01](../../../../../../../avoid/01_restating_the_target.md),
[control screen12](../../../../../../../result-summaries/12_collision_controls_and_screening.md)
and [scope07](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
remain governing. The identities above are representations/model
calculations, not proposed positivity mechanisms. Collision exclusions
are not asserted: the empirical identity includes collisions, and the
simple CUE model does not supply a premise about canonical collisions.

Primary passages were inspected online on 8 November 2026. Reuse
[parent source-use07](../../../references/07_TND_O_B03_COMPLEX_ZERO_STATISTICS_SOURCE_USE_20261106.md)
and [source-use17](../../../references/17_TND_O_GREEN_CORRELATION_SETUP_SOURCE_USE_20261107.md)
and their existing bibliography entries. No new PDF copy or hash, full
proof audit, independent assessment or new theorem import is claimed.
