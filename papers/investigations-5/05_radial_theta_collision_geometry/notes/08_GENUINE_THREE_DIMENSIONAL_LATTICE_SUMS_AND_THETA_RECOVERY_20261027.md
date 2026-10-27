# Genuine three-dimensional lattice sums and exact theta recovery

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Research conversation: **Review radial theta collision work**, Investigation05 chat0002, thread 01a17ee9-ed08-7271-9f66-04ac5ee516b8.

Edward Baker clarified that the intended construction should start with a different function summed over three-dimensional lattice points, with a simpler summand, and then relate that function to the original theta primitive. Manipulating Phi after keeping its rank-one sum fixed did not answer that request. This note starts with two actual rank-three sums.

**Status: two exact constructive source representations, with analytical proofs and same-assistant checks.** One uses Euclidean lengths on a cubic lattice coset, an alternating lattice character, and the ordinary spherical-average kernel. The other is positive on every point of Z^3 but uses the maximum-coordinate norm and a simple resolvent weight. Neither is an unchanged one-dimensional sum with added spectator coordinates. The tradeoffs are explicit; no new collision estimate or novelty claim is made.

The [result index](../../../../result-summaries/README.md), especially [theta/arithmetic identities](../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [geometric constructions](../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md), and the [avoid index](../../../../avoid/README.md), especially [coordinate lifts](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [scoped conclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [a factor is not the target](../../../../avoid/13_a_factor_is_not_the_target.md), determine the claim level. These are source-realization results, not RH-equivalent criteria or sign mechanisms.

## 1. Target and notation

Retain

\[
A(r)=\sum_{n\ge1}e^{-\pi r^2n^2},\qquad
\Theta(r)=1+2A(r),\qquad
\psi(u)=e^uA(e^{2u}),
\]
\[
\Phi(u)=\tfrac18(\partial_u^2-1)\psi(u),\qquad
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du.
\tag{1}
\]

Here psi is the original theta primitive; it is distinct from the test mode Psi_z introduced in Note07. Both psi and Phi are recovered below. The new definitions themselves do not take Phi or psi as input.

## 2. A Euclidean construction on a cubic lattice coset

Consider the full-rank coset

\[
\mathcal C=(1,0,0)+2\mathbb Z^3,\qquad
v=(2a+1,2b,2c),\quad
R_v=|v|=\sqrt{(2a+1)^2+4b^2+4c^2}.
\]

Define

\[
\boxed{
P(r)=\sum_{a,b,c\in\mathbb Z}
(-1)^c\,\frac{\sin(\pi R_v/2)}{2R_v}\,
e^{-\pi r^2R_v^2},\qquad r>0.
}
\tag{2}
\]

Every coordinate ranges over all integers. The distance is ordinary Euclidean distance. The only additional ingredients are a period-two sign and a radial sine-over-distance factor. There is no theta source inside the summand. Since R_v>=1, the sum and every fixed r-derivative converge absolutely on compact positive r intervals.

The exact reduction is

\[
\boxed{P(r)=\sum_{\substack{n\ge1\\n\ {\rm odd}}}
e^{-\pi r^2n^2}.}
\tag{3}
\]

This is an odd sector, not yet the complete target. Section 4 supplies the complete recovery.

## 3. Why the three-dimensional shells collapse

First omit the sine-over-distance factor and write q=exp(-pi r^2). Product factorization of the actual three-dimensional sum gives

\[
\sum_{a,b,c\in\mathbb Z}(-1)^c q^{(2a+1)^2+4b^2+4c^2}
=\theta_2(0,q^4)\theta_3(0,q^4)\theta_4(0,q^4).
\tag{4}
\]

Jacobi's derivative identity and the theta_1 Fourier series give

\[
\theta_2(0,q^4)\theta_3(0,q^4)\theta_4(0,q^4)
=\theta_1'(0,q^4)
=2\sum_{j\ge0}(-1)^j(2j+1)q^{(2j+1)^2}.
\tag{5}
\]

The prime here is differentiation in the elliptic argument, with the DLMF period-pi convention. The checked sources are [DLMF20.4.6](https://dlmf.nist.gov/20.4.E6) and [20.2.1–4](https://dlmf.nist.gov/20.2); see [annotation05][refs].

Equality of the convergent power series proves the exact signed shell count

\[
C(N):=\sum_{\substack{v\in\mathcal C\\|v|^2=N}}
(-1)^{v_3/2}
=
\begin{cases}
2n\chi_4(n),&N=n^2,\ n\ge1\ {\rm odd},\\
0,&\text{otherwise},
\end{cases}
\tag{6}
\]

where chi_4(n)=(-1)^((n-1)/2) for positive odd n. On a surviving shell,

\[
\frac{\sin(\pi n/2)}{2n}=\frac{\chi_4(n)}{2n};
\]

multiplying by (6) gives exactly one. Every other shell cancels before multiplication. This proves (3), using absolute convergence to group by radius.

The transverse coordinates do real work. At squared radius 5, four points of the form (+/-1,+/-2,0) have positive character, while four (+/-1,0,+/-2) have negative character, giving zero. At squared radius 9, the two axial points (+/-3,0,0) contribute +2 and the eight points (+/-1,+/-2,+/-2) contribute -8. The net -6 times sin(3pi/2)/6 equals one. Retaining only the axial points would give -1/3, not one.

Thus this observation does not project all transverse modes to zero. It uses cancellations among actual three-dimensional shells.

### The radial weight is an ordinary spherical average

Define the three-dimensional heat field

\[
K(s,x)=\sum_{v\in\mathcal C}e^{-\pi s|v|^2}e^{2\pi i v\cdot x},
\qquad
\partial_sK=\frac1{4\pi}\Delta_xK.
\tag{7}
\]

Its Fourier frequencies are the indicated lattice coset. It has an antiperiodic half-translation in the first spatial coordinate and periodic half-translations in the other two. This specifies a parity sector of the flat torus heat equation, not a positive scalar fundamental heat kernel on the whole torus.

With x_0=(0,0,1/4), angular averaging gives

\[
\frac1{4\pi}\int_{S^2}K(r^2,x_0+\omega/4)\,d\omega
=\sum_{v\in\mathcal C}(-1)^{v_3/2}
e^{-\pi r^2|v|^2}j_0(\pi|v|/2).
\]

Since j_0(w)=sin(w)/w,

\[
\boxed{
P(r)=\frac{\pi}{4}\frac1{4\pi}
\int_{S^2}K(r^2,x_0+\omega/4)\,d\omega.
}
\tag{8}
\]

This is a genuine spatial sphere of radius 1/4 in the independently defined three-dimensional heat field. The profile parameter r controls heat time r^2; it is not the radius of that observation sphere. The lattice radius R_v in (2) is Euclidean. These three roles are deliberately kept separate.

## 4. Recovering the complete original primitive

Every positive integer is uniquely 2^j times an odd positive integer, so one recovery is

\[
A(r)=\sum_{j\ge0}P(2^jr).
\tag{9}
\]

All the reduced terms are positive, and convergence follows directly from Gaussian decay. There is also a finite two-scale identity, avoiding the extra sum.

The even/odd decomposition gives

\[
\theta_3(0|ir^2)-\theta_4(0|ir^2)=4P(r).
\]

The modular identity [DLMF20.7.33](https://dlmf.nist.gov/20.7.E33), with positive square root r, gives

\[
\theta_4(0|ir^2)
=r^{-1}\theta_2(0|i/r^2)
=\frac2rP\!\left(\frac1{2r}\right).
\]

Consequently

\[
\boxed{\Theta(r)=4P(r)+\frac2rP\!\left(\frac1{2r}\right),}
\]
\[
\boxed{
\psi(u)=r^{1/2}
\left[2P(r)+\frac1rP\!\left(\frac1{2r}\right)-\frac12\right],
\qquad r=e^{2u}.
}
\tag{10}
\]

This recovers the complete unchanged primitive from the new rank-three definition (2). Applying the fixed source operator in (1) then recovers Phi. Its n^4/n^2 polynomial is not required in the defining three-dimensional heat summand.

The price is explicit: signed lattice weights, a chosen parity sector and spherical observation, and either dyadic scale summation or the two-scale modular combination. The individual terms in (2) are not nonnegative, even though the exact sum P(r) is positive. A simpler summand does not by itself give a simpler sign estimate.

### A direct lattice zeta version, including z

For Re(w)>2 the genuinely three-dimensional series

\[
\mathcal E(w)=
\sum_{v\in\mathcal C}
(-1)^{v_3/2}\frac{\sin(\pi|v|/2)}{2|v|^{w+1}}
\tag{11}
\]

converges absolutely. The same shell identity gives

\[
\mathcal E(w)=\sum_{n\ {\rm odd},\,n\ge1}n^{-w}
=(1-2^{-w})\zeta(w).
\tag{12}
\]

Thus spectral dependence can enter a simple power of the three-dimensional Euclidean radius. With w=(1+iz)/2, analytic continuation gives

\[
H(0,z)=
\frac{w(w-1)\Gamma(w/2)}
{16\pi^{w/2}(1-2^{-w})}\,\mathcal E(w).
\tag{13}
\]

Equation (13) uses the meromorphic continuation fixed by (12). It is not a claim that the raw lattice series (11) converges on Re(w)=1/2. The denominator is nonzero there. At positive Newman time, no termwise heat deformation of (11) is asserted: the Gaussian regularization and completion must be retained.

## 5. A different exact sum: positive weights on all of Z^3

If positivity of every lattice contribution is more important than Euclidean spherical shells, put

\[
M(v)=\max(|v_1|,|v_2|,|v_3|),\qquad
\boxed{
\mathcal C_\infty(r)=
\sum_{v\in\mathbb Z^3}
\frac{e^{-\pi r^2M(v)^2}}{1+12M(v)^2}.
}
\tag{14}
\]

This is a coupled three-coordinate summand: the maximum depends on all coordinates and does not factor into three one-dimensional Gaussian factors. Every point has positive weight. The cube shell M(v)=n contains

\[
(2n+1)^3-(2n-1)^3=24n^2+2
=2(12n^2+1)
\tag{15}
\]

points. Its total weighted contribution is therefore exactly 2 exp(-pi r^2 n^2). Including the origin,

\[
\boxed{\mathcal C_\infty(r)=\Theta(r),\qquad
\psi(u)=\tfrac12 e^u\{\mathcal C_\infty(e^{2u})-1\}.}
\tag{16}
\]

An equivalent construction starts with the unweighted positive sum

\[
Z_\infty(s)=\sum_{v\in\mathbb Z^3}e^{-\pi sM(v)^2}.
\]

The resolvent average

\[
\mathcal C_\infty(r)=\frac{\pi}{12}
\int_0^\infty e^{-\pi a/12}Z_\infty(r^2+a)\,da
\tag{17}
\]

produces precisely the denominator in (14). Tonelli justifies this positive interchange.

One operator interpretation uses the nonnegative Fourier multiplier D with symbol M(v)^2 on the flat three-torus. Then (14) is Tr[(1+12D)^(-1) exp(-pi r^2 D)]. This is not the ordinary Euclidean Laplacian: the symbol uses the maximum norm and is not a quadratic form. No positivity-preserving spatial diffusion claim is made. The inverse quadratic weight compensates cubic-shell multiplicity; the effective profile consequently has the rank-one small-r growth. The geometry has not been made free.

The simple cube-shell polynomial is exactly why this positive construction works. Replacing M(v)^2 by |v|^2 without changing the weight does not work: the nonsquare Euclidean shell |v|^2=2 contributes positively, while the target has no such exponential.

## 6. Comparison with the earlier obstructions and next mathematical question

| Construction | Defining lattice sum | Exact relation to the target | Cost |
| --- | --- | --- | --- |
| Euclidean parity/spherical construction | Full-rank coset in Z^3; Gaussian in ordinary squared length, with a periodic character and spherical-average kernel | Equations (3) and (10) recover the complete primitive | Signed interference and a two-scale or dyadic reconstruction |
| Positive cube-shell construction | All Z^3; maximum-norm Gaussian with one rational resolvent weight | Equations (14)–(16) recover Theta directly | Cubic rather than Euclidean shells; nonlocal spatial operator |

The positive Euclidean full-trace obstruction of Note06 does not cover the first construction, which is signed, or the second, which changes the norm and kernel. Note07 fixes one periodic spatial field and varies the radius of its spherical mean. Here (8) fixes the observation sphere and varies the heat parameter of the underlying field. That is a different family, so its integrability obstruction does not apply.

Both constructions now answer the requested source-realization question in explicit classes. Their defining summands are three-dimensional and do not contain Phi. Whether either is the desired physical model depends on accepting its declared signs, norm or observation; neither is an unweighted positive Euclidean lattice trace.

The [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md) do not permit an exclusion from Gaussian summands or positivity alone. Generic radial inverse marginals still admit the positive double-zero control of Note07. Weighted-square controls change the canonical coefficients/full reflection; Euler-factor controls change the canonical source/conductor; reflected smooth and primitive-compatible controls do not have the unchanged square arithmetic. The special shell identity (6) fixes the canonical odd coefficients, but no independent inequality for their physical transform has been proved here. Existing collision certificates are not rerun.

The next structural task is concrete: determine whether the parity heat field and its selected spherical mean admit a useful coupled identity or signed estimate before carrying out the reduction (10). Alternatively, determine whether the positive resolvent in (14) has a comparison principle relevant to the completed source, retaining its nonlocal symbol. Merely expanding either identity back to (1) supplies no new estimate.

## 7. Verification and provenance

The [checker][checker] enumerates the actual integer coset shells through squared radius 625, checks their signed coefficients and exact surviving weights, verifies cube-shell counts through radius 8, and records the axial-only failure at squared radius 9. A rational bound controls the omitted box in the direct three-dimensional P sums uniformly for r>=1/4. The [record][record] separately labels floating-point evaluations of both constructions and complete-theta recovery as exploratory; they are normalization checks, not proofs or interval certificates.

The infinite Euclidean identity follows from the classical Jacobi formula and coefficient comparison, not from the finite enumeration. The positive cube identity follows from the exact shell polynomial. All checking is same-assistant; no independent review or novelty claim is made.

[Annotation05][refs] records the checked DLMF passages and a related ternary-coset paper discovered during the search. Only the latter's abstract and metadata were inspected; none of its theorems is used. Its versioned public PDF is retained outside Git under the repository reference policy.

This is a fifth bounded RTC-03 return, with two actual changed lattice definitions. The broader collision mechanism remains open; no manuscript milestone, snapshot, new physical region or Newman-bound improvement is claimed.

[refs]: ../references/05_JACOBI_DERIVATIVE_AND_TERNARY_LATTICE_SUMS_20261027.md
[checker]: ../numerics/08_check_genuine_three_dimensional_lattice_sums_20261027.py
[record]: ../numerics/08_GENUINE_THREE_DIMENSIONAL_LATTICE_CHECKS_20261027.json
