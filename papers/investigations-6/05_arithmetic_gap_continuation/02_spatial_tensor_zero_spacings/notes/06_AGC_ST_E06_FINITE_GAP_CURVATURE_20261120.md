# Certified acceleration of one finite canonical spacing

20 November 2026, America/New_York. Prepared for Edward Baker with OpenAI Codex LLM assistance. Executor dispatched as gpt-6.2-sol, effort ultra. Serving configuration has no separate attestation. AGC-ST-E06 r1, interval-certified on the stated slab, pending separate replay and assessment.

On \(0\le t\le T=10^{-4}\), let \(a(t)<b(t)\) be the two occurrences of the literal theta field \(H\) in \([26,46]+i[-2,2]\). They are real and simple throughout this slab. For \(g=b-a\), \(D=g^2/4\) and \(K=24D^2S_2+32D^3S_3\), the spatial calculation proves
\[
 K\ge \frac{60625}{27648}>2.19,\qquad g_{tt}>\frac1{180},\qquad
 \frac{g(0)+g(T)}2-g(T/2)>\frac{T^2}{1440}.
\]
The direct comparison gives \(2.71765096905<K<2.78093534325\) uniformly. [Frozen request](../research-progress/handoffs/AGC_ST_E06_REQUEST_R1_20261120.md) · [Outward record](../numerics/01_AGC_ST_E06_FINITE_GAP_CURVATURE_20261120.json)

## Complete wall, physical tubes and source remainder

HDC gives count two with multiplicity, with a wall floor \(>4.94\cdot10^{-7}\) throughout the complex-time square whose real side contains \([0,T]\). JH E08 supplies full-slab physical source tubes for the two distinct real roots. The replay verifies both records and their source and chart identities, including the JH record's HDC hash. We use the physical F_brackets in the full_slab section, including their outward radii. Conservative values as used in the replay are
\[
 28.26939231995<a<28.26945028385,\qquad
 42.04400377743<b<42.04407927790 .
\]
The count identifies the two positions without a global index. [HDC complete wall and count](../../../../investigations-4/12_height_dependent_heat_contours/notes/13_COMPLETE_THETA_WALL_AND_COEFFICIENT_CERTIFICATE_20261023.md) · [JH physical slab](../../01_jacobi_integer_hierarchy/notes/08_AGC_JH_PHYSICAL_TIME_SLAB_20261119.md)

The ball polynomial is the inherited full theta source \(F(t,z)=H(t,z)/H(t,0)\) through time degree 10 and spatial powers \(0,\dots,143\) at 768 bits. Its variables are \(s=t/T,\ w=z-36\). The anchor uses \(\xi((1+iz)/2)/\xi(1/2)\), followed by the physical heat coefficient recurrence and division by the tilted time mass. The positive theta measure gives \(H(t,0)>0\) at real time, and the inherited majorant \(C\) controls \(F\) on \(|t|\le1/20,\ |w|\le24\), with a certified complex-time mass floor. On \(|t|\le T,\ |w|\le15\) the retained polynomial \(P\) has the recomputed remainder
\[
 |F-P|\le E_*=
 C\frac{(1/500)^{11}}{1-1/500}
 +C\frac{(15/24)^{144}}{(1-15/24)(1-1/500)}
 <2.976\cdot10^{-28}.
\]
The retained coefficients are Arb balls, with their radius-weighted sum at radius 15 below \(3.101\cdot10^{-175}\). At both root tubes a unit Cauchy circle fits within \(|w|\le15\), which pays an additional \(j!E_*\) in spatial derivative order \(j\), below \(7.141\cdot10^{-27}\) at fourth order. The evaluation of each retained polynomial derivative uses its first four Taylor terms at the spatial midpoint and a coefficient absolute majorant for the fourth derivative remainder on the connecting segment. The real time ball covers every \(s\in[0,1]\) in every evaluation. [Source and interval driver](../numerics/certify_st_e06.py) · [JH complete source bound](../../01_jacobi_integer_hierarchy/notes/08_AGC_JH_PHYSICAL_TIME_SLAB_20261119.md#the-complete-source-on-the-wide-collar)

## One real exterior occurrence and the complete lower bound

The radius-15 model gives these outward intervals throughout the slab.

| Point | Normalized \(F(t,z)\) |
| --- | --- |
| \(49.9\) | \((1.6038219330,\,1.6045894768)\cdot10^{-7}\) |
| \(50.1\) | \((-9.7422334617,\,-9.7349248705)\cdot10^{-8}\) |

The opposite signs give at least one real occurrence \(\rho_*\in(49.9,50.1)\) at every time. The root tubes give \(13.77455349359<g<13.77468695795\), hence \(13<g<15\), and \((50.1-b)/g<0.584846273<3/5\). That occurrence contributes at least \(k(3/5)\) to \(K\), since the single-occurrence kernel \(k(x)=\tfrac12[x^{-3}-(x+1)^{-3}]\) is decreasing for \(x>0\). [E03 kernel](04_AGC_ST_E03_PAIRED_FORCING_20261120.md#the-paired-head)

The time-zero canonical strip and its forward preservation give \(|\Im\rho|\le1\) for every zero. The complete count and cleared wall therefore exclude every exterior occurrence with \(26\le\Re\rho\le46\). For a right exterior occurrence set \(r=\rho-b\), and for a left one set \(r=a-\rho\). The root tubes give \(w=\Re r>2\) and \(|\Im r|\le1\), with \(Q_\rho=r(r+g)\). [Canonical strip and scaling](../../../03_volterra_coefficient_dynamics/01_cluster_gap_transport/references/03_VCD_GT_STRIP_PRODUCT_SOURCE_USE_20261116.md) · [Polymath v2, Theorem 3.2](https://arxiv.org/pdf/1904.12438v2#page=14)

When \(w\ge1+\sqrt2\), the segment from \(r\) to \(r+g\) stays in the E03 sector \(|\arg|\le\pi/8\), which gives \(\Re k(r/g)\ge0\) by the inverse-fourth integral. When \(2\le w\le1+\sqrt2\), put \(v=(\Im r)^2/w^2\le1/4\). Then
\[
 \Re(r^{-3})=w^{-3}\frac{1-3v}{(1+v)^3}
          \ge \frac{16}{125}w^{-3},\qquad
 |(r+g)^{-3}|\le(w+g)^{-3}\le \frac18 w^{-3}.
\]
The second bound uses \(g>13>w\). The margin \(16/125-1/8=3/1000\) is positive, so the real part of \(k(r/g)=(g^3/2)[r^{-3}-(r+g)^{-3}]\) is nonnegative throughout the remaining short sector. The complete exterior sum is absolute by the canonical large-disk Jensen count \(O(R\log(2+R))\) and the inverse-fourth decay, and real by conjugation. Taking the selected real occurrence once and retaining every other nonnegative real part, with multiplicity, gives \(K\ge k(3/5)=60625/27648\). This argument only needs existence in the exterior sign bracket. [Canonical growth and count](../../manuscript/sections/01_source.tex)

## Direct complete-source comparison

At either target root \(x(t)\), differentiating \(H(t,x(t))=0\) and using \(H_t=-H_{zz}\) gives \(x'=v=H_{zz}/H_z\). Differentiating again gives
\[
 0=H_{zzzz}-2vH_{zzz}+v^2H_{zz}+x''H_z,\qquad
 x''=A=-H_{zzzz}/H_z+2vH_{zzz}/H_z-v^2H_{zz}/H_z .
\]
The ratios are unchanged on replacing \(H\) by \(F\) because the normalization is a positive factor depending only on time. The two evaluations use the same full-slab model and inherited physical tubes as the spatial calculation.

| Spatial jet | At \(a\) | At \(b\) |
| --- | --- | --- |
| \(F_z\) | \((-1.390774241,\,-1.390697924)\cdot10^{-3}\) | \((1.785198136,\,1.785359693)\cdot10^{-5}\) |
| \(F_{zz}\) | \((8.061012921,\,8.061244133)\cdot10^{-4}\) | \((-1.347905283,\,-1.347847107)\cdot10^{-5}\) |
| \(F_{zzz}\) | \((-2.798410165,\,-2.798369175)\cdot10^{-4}\) | \((5.772650740,\,5.772758429)\cdot10^{-6}\) |
| \(F_{zzzz}\) | \((5.969183204,\,5.969222803)\cdot10^{-5}\) | \((-1.303319216,\,-1.303280114)\cdot10^{-6}\) |

Both derivative denominators exclude zero. The outward acceleration difference gives \(0.01051532122<A_b-A_a<0.01090242033\). The inherited complete-gap law \(g_{tt}=16(K-1)/g^3\) therefore yields
\[
 2.71765096905 < 1+\frac{g^3(A_b-A_a)}{16}=K <2.78093534325 .
\]
The outward direct width is below \(0.06328437420\), and the entire interval clears the exact spatial floor \(60625/27648\). The spatial method uses the exterior sign bracket, strip and complete count to give a one-sided floor. The direct method evaluates four jets at each target to give both sides and does not need to acquire the exterior sign bracket. The direct interval gives a stronger lower bound on these data. [Complete-gap acceleration law](../../../03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/manuscript/sections/18_retained_forcing.tex) · [Numerical receipt](../numerics/01_AGC_ST_E06_FINITE_GAP_CURVATURE_20261120.json)

## Curvature consequence and scope

The spatial floor alone gives \(g_{tt}>16(60625/27648-1)/15^3=32977/5832000>1/180\). Hence \(g(t)-t^2/360\) is strictly convex, and its endpoint-average midpoint excess is strictly positive. The contribution of the subtracted quadratic to the excess of \(g\) is \(T^2/1440=1/144000000000\).

The result concerns the actual physical spacing in one counted finite region. At a collision of the targets the certified premise \(g>13\) fails. Euler-factor controls change the analytic exterior and source. Weighted squares and finite-source changes alter normalized coefficients, and finite-prime orbit controls fail full reflection. Reflected and positive-primitive controls lack the theta square expansion. Fixed-event and finite-profile controls lack the full canonical profile or eventual simplicity. RH-conditional endpoint controls fail ordinary Dirichlet arithmetic, and the changed observation kernel fails the physical cosine equation. The sign lemma can hold on eligible control slices. This application uses the recorded canonical wall and source. Its scope is the physical gap curvature, with no conclusion about other heights, global reality, monotonicity of the Jacobi approximation error or the Newman constant. [Collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md) · [Results index](../../../../../result-summaries/README.md) · [Patterns index](../../../../../avoid/README.md) · [Known-coverage checks](../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md)

The record contains verified input and driver hashes, the execution environment, and decimal endpoints rounded outwards. From this branch, run python numerics/certify_st_e06.py with python-flint available to generate one record on stdout. The original run used python-flint 0.9.0 and FLINT 3.6.0. No bracket or precision repair was needed.
