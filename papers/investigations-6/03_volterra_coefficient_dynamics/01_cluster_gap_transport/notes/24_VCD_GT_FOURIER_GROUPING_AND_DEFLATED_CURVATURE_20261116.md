# Fourier grouping for the deflated curvature of a zero pair

16 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance, chat0003. Lead actual model/effort are
unavailable. Fixed algebra checks were dispatched **gpt-6.1-sol / ultra**;
separate backend attestation unavailable. The helper contributed formulas
and controls, checked by the lead. No separate independent assessment or
specialist review.

**Discussion and exact algebra, not an acquired canonical sign bound.**
The author suggested positive Fourier blocks, then clarified that the
object of interest is the zero cluster. The appropriate target is the
normalized curvature after removing the counted pair. This note gives its
two-point form, a Fourier numerator at a double, and a control locating the
missing premise. [Synthesis23][previous] remains unchanged.

| Next task | Type / recommendation | Readiness and output |
| --- | --- | --- |
| B06 deflated Fourier grouping | B / Astra — choose a quantitative grouping of the retained phases | Candidate quantity explicit; still needs blocks, domain, a paid signed remainder, normalization and finite-to-complete-field transfer. No numerical packet issued. |
| Fixed algebra check | E / Sol6.1 ultra | Complete helper/lead checks, no source acquisition. |

Read the [result index][results], [controls12][controls],
[coefficient18][coefficients] and [avoid index][avoid], especially
[01][classification], [02][premises], [03][relift], [07][scope] and
[12][joint]. The target identity is supporting algebra. Requiring its
positivity alone would not supply the estimate. Parent B07/E25, E06 and
sibling branches remain unchanged.

## 1. The two-point quantity

Use \(F\) for the actual field on a fixed heat-time slice, or for a finite
readout with its own justified count-two tube. Put
\[
 Q(z)=(z-z_1)(z-z_2)=(z-c)^2-D,\qquad A=F/Q,\qquad B=A'/A.
\]
The deflated \(A\) is analytic and zero-free in the counted disk. The
existing drift and its positive-sign counterpart are
\[
 K_F=\frac{B(z_1)-B(z_2)}{z_1-z_2},\qquad
 -K_F=\int_0^1\frac{\mathcal L[A]}{A^2}
       \bigl(z_2+s(z_1-z_2)\bigr)\,ds,\qquad
 \mathcal L[A]=(A')^2-AA''.
 \tag{1}
\]
The segment lies in the deflated zero-free disk. This follows directly
from \(-B'=\mathcal L[A]/A^2\). At a real double \(z_1=z_2=c\),
\[
 \boxed{-K_F=\mathcal L[A](c)/A(c)^2.}
 \tag{2}
\]
For a real separated pair, a lower bound for this normalized expression
along the real segment bounds \(-K_F\). For a conjugate pair \(c\pm ib\),
\(b>0\), the correct statement is instead
\[
 -K_F=-\frac{\operatorname{Im}B(c+ib)}b
 =\frac1{2b}\int_{-b}^{b}
       \operatorname{Re}\frac{\mathcal L[A](c+iy)}{A(c+iy)^2}\,dy.
 \tag{3}
\]
A real-axis inequality alone does not pay this vertical average.

Thus (1) is the same exterior-curvature target used by the previous
conjugate-divisor argument, expressed through the field. Direct algebra
also gives, away from the removable singularities,
\[
 \mathcal L[A]=
 \frac{Q^2\mathcal L[F]-F^2\mathcal L[Q]}{Q^4},\qquad
 \mathcal L[Q]=2((z-c)^2+D).
 \tag{4}
\]
Deflation retains the counted zeros through \(Q\). Separate absolute
bounds on the numerator of (4) can lose the cancellation at those zeros.

## 2. The Fourier numerator at a stipulated real double

Let \(F=G_N=\sum_j\omega_j e^{izx_j}\), with positive normalized weights
and distinct real nodes. At an exact real double \(c\), assume
\(G_N(c)=G_N'(c)=0\), \(G_N''(c)\ne0\). Taylor expansion yields
\[
 A(c)=G_N''(c)/2,\quad A'(c)=G_N'''(c)/6,\quad A''(c)=G_N''''(c)/12,
\]
hence
\[
 \boxed{
 -K_N(c)=\frac{\mathcal P_N(c)}{18G_N''(c)^2},\qquad
 \mathcal P_N=2(G_N''')^2-3G_N''G_N''''.}
 \tag{5}
\]
This is a concrete candidate for Fourier grouping. The useful target
\(-K_N\ge59/100\) at a double requires
\(\mathcal P_N(c)\ge18(59/100)G_N''(c)^2\), plus any transfer payment.
Positivity of the numerator alone pays only a sign.

Symmetrizing the differentiated Fourier products gives exactly
\[
 \mathcal P_N(z)=\frac12\sum_{j,k}\omega_j\omega_k x_j^2x_k^2
       (3x_j^2-4x_jx_k+3x_k^2)e^{iz(x_j+x_k)}.
 \tag{6}
\]
The coefficient polynomial is
\(x_j^2+x_k^2+2(x_j-x_k)^2\ge0\). This means nonnegative spectral
coefficients, not a pointwise sign or a positive-semidefinite matrix
claim. For an even source, combine equal sums \(x_j+x_k\), then combine
opposite sums:
\[
 \mathcal P_N(x)=C_0+2\sum_{\nu>0}C_\nu\cos(\nu x),\qquad
 C_\nu\ge0,\qquad C_0=5\sum_j\omega_j^2x_j^6.
 \tag{7}
\]
The opposite-node pairs supply a positive constant. The other terms
retain correlated phases. Estimating that complete oscillatory remainder
from the actual nodes, weights and applicable zero conditions is the
unpaid step. A separate absolute allowance has not been tested here.

The general Fourier/Laguerre connection is established literature;
[Csordas][csordas], Theorems 2.4 and 3.7, provides orientation. The finite
normalizations above are derived directly, without importing a
continuous-kernel theorem into an atomic measure or copying the
half-line normalization flagged in the [canonical annotation][canonical-ref].

The same algebra applies directly to the complete Fourier integral
\(F(z)=\int e^{izu}\,d\mu(u)\):
\[
 \mathcal P_F(z)=\frac12\iint u^2v^2(3u^2-4uv+3v^2)
                           e^{iz(u+v)}\,d\mu(u)\,d\mu(v).
 \tag{8}
\]
The canonical source's decay pays differentiation and Fubini on compact
complex sets. This direct route avoids a finite-model transfer, while
retaining the same unpaid oscillatory estimate and normalization. For
an absolutely continuous source, the line \(u+v=0\) has product-measure
zero: the discrete constant \(C_0\) is not automatically a positive
constant atom in the complete-source formula. No degree-uniform lower
bound for it is claimed.

## 3. An exact sign control at a double

Positive Jacobi weights, symmetry and an actual double do not force
\(\mathcal P_N(c)>0\). Take
\[
 G(z)=\frac{5+6\cos z+\cos2z}{12}
     =\frac{(1+\cos z)(2+\cos z)}6.
 \tag{9}
\]
The positive masses are \(5/12\) at zero, \(1/4\) at each of \(\pm1\),
and \(1/24\) at each of \(\pm2\). Gram–Schmidt on this symmetric
five-point measure gives an irreducible zero-diagonal Jacobi matrix.
At \(c=\pi\),
\[
 G=G'=0,\quad G''=1/6,\quad G'''=0,\quad G''''=5/6,
 \qquad \mathcal P(c)=-5/12,\quad -K(c)=-5/6.
\]
Multiplying each spectral mass by \(e^{(t-T)x_j^2}\) embeds this slice
at \(t=T\) in the physical heat equation. It is a finite atomic heat
field, not theta. The extra roots \(\cos z=-2\) have imaginary height
\(\operatorname{arcosh}2>1\): this control fails Note21's width-one
premise and does not contradict the accepted divisor estimate.
The scoped exclusion is of an automatic deflated-sign conclusion from
positive weights, reflection and a double alone.

For the broader [control catalog][controls], positive even source
families share applicable reflection and Fourier–Gram identities:
Euler, weighted-square, finite-score/prime, reflected, smooth/primitive,
and atomic/compact-profile examples are not separated by these
identities. The atomic examples fail unchanged theta source structure;
the other source failures retain their recorded scopes. RH-conditional
endpoint constructions retain RH. Changed observation kernels lack the
literal readout; fractional profile relaxations need not supply the
actual Jacobi divisor. The new quantitative deflated inequality has not
been tested on these families. Missing canonical source equality is not
evidence that an untested derived inequality fails.

## 4. Other positive groupings and their limits

The parity matrix \(S=\operatorname{diag}(1,-1,1,-1,\ldots)\) obeys
\(SJ_NS=-J_N\) and \(Se_0=e_0\). Reflection therefore gives
\[
 G_N(z)=\omega_0+2\sum_{\lambda>0}\omega_\lambda\cos(\lambda z),
 \qquad
 1-G_N(x)=4\sum_{\lambda>0}\omega_\lambda\sin^2(\lambda x/2)\ge0.
\]
The zero-node term is absent for even \(N\). The positive blocks in the
second formula pay \(G_N(x)\le1\), not zero geometry. Positive weights
also make the difference kernel \(G_N(t_r-t_s)\) positive semidefinite,
as its quadratic form is a weighted sum of absolute squares.

A nonzero real finite exponential polynomial with zero constant
coefficient cannot be nonnegative everywhere: otherwise
\(P^2\le\|P\|_\infty P\), while long symmetric interval averages give
\(\operatorname{mean}P=0\) and
\(\operatorname{mean}P^2=\sum_\nu|c_\nu|^2>0\).
This applies without commensurable frequencies. It excludes globally
positive literal nonzero-frequency blocks, not local signed groupings.

Fejér's example illustrates the additional organization a square gives:
\[
 \frac1m\left|\sum_{r=0}^{m-1}e^{ir\theta}\right|^2
 =1+2\sum_{k=1}^{m-1}(1-k/m)\cos(k\theta)\ge0.
\]
See [DLMF 1.15.15][fejer], \(m=n+1\). The Jacobi spectral theorem supplies
neither this lattice nor these autocorrelation weights. General squares
can use arbitrary frequencies, but their difference support and
coefficients must still match. Rounding nodes to bins changes the function
and requires an error bound.

The undeflated expression
\[
 \mathcal L[G_N]=\tfrac12\sum_{j,k}\omega_j\omega_k(x_j-x_k)^2
                       e^{iz(x_j+x_k)}
\]
vanishes automatically at a double, so its value there does not measure
the required curvature. Even its strict positivity everywhere need not
give all-real zeros. For the positive symmetric four-atom readout
\(G=(9\cos z+\cos2z)/10\),
\[
 \mathcal L[G](x)=
 \frac{85+(81/2)\cos x+(9/2)\cos3x}{100}\ge2/5,
\]
yet its zero equation includes
\(\cos z=(-9-\sqrt{89})/4<-1\).

## 5. Consequence for this investigation

The corrected suggestion has a precise target: organize (6), or the
full two-point expression (1)–(3), to prove a quantitative lower bound
for normalized deflated curvature. A useful grouping must pay the
oscillatory remainder and the normalization, and distinguish the
five-atom control by an additional proved premise. Equations (5)–(7)
alone are a representation of the problem.

The physical gap law belongs to the actual heat field. Finite
\(G_{N,t}\) need not satisfy it: [Note05][defect]'s model defect and
[Note04][transfer]'s full-coordinate transfer remain necessary.
Any finite-readout estimate must pay the approximation and deflation
geometry before transfer to the canonical tube. An estimate only at a
double does not give the full-slab signed-cost bound. This discussion
acquires no source samples, canonical count, positive margin or numerical
campaign; the next choice remains B06.

[previous]: 23_VCD_GT_JOINT_SOURCE_SYNTHESIS_AND_CONTINUATION_20261116.md
[defect]: 05_VCD_GT_E03_PHYSICAL_MODEL_DEFECT_20261116.md
[transfer]: 04_VCD_GT_E02_COMPLETE_COORDINATE_TRANSFER_20261116.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[coefficients]: ../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[avoid]: ../../../../../avoid/README.md
[classification]: ../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[relift]: ../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[csordas]: https://arxiv.org/html/1309.0055v2
[canonical-ref]: ../../../../investigations-5/05_radial_theta_collision_geometry/references/21_POSITIVE_THETA_PRIMITIVE_LITERATURE_SOURCES_20261031.md#csordas13090055v2
[fejer]: https://dlmf.nist.gov/1.15.E15
