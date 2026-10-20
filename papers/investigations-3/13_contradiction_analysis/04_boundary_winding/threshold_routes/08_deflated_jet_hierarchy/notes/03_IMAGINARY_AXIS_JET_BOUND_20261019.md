# BW-08: an imaginary-axis lower bound and its time-face transfer

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Model **gpt-6-astra (Codex)**; actual reasoning
effort **max**, verified from recorded turn metadata.

**Status: restricted analytic result, proved in-note; same-assistant
self-review only.** At an exact double zero a>=20 of an all-real theta
slice at T>0, the deflated fourth-jet quantity satisfies

\[
S_a:=\frac{h_3^2}{9h_2^2}-\frac{h_4}{6h_2}
>\ell(a):=\frac{1}{4a}\log\frac{a+1}{4\pi}-\frac{3}{2a^2}
>\frac{1}{2a^2},\qquad h_j=\partial_x^jH(T,a).                 \tag{1}
\]

This strengthens the predecessor's mirror-only bound. Section 3 transfers
it to a signed, finite-time bound on critical values on the two BW-01 time
faces, with complete derivative remainders through spatial order six.
**This is a stronger necessary condition, not a collision exclusion or a
contradictory winding.** No theta event, numerical theta jet, new covered
region, later witness, improved Newman bound or runtime gain is supplied.
The coefficient improvement in the table refers only to the deflated
lower bound; it is not a multiplier for total curvature or performance.

The [contract][contract] was fixed before the exact control runs. This
implements the quantitative-restriction acceptance rule in the
[opening note][initial], with BW-01 as the named consumer. The inherited
deflation and local degree laws are not claimed as new; no literature
priority is claimed. Read the [result summaries][results], [local laws][laws],
[control cluster][controls] and [patterns to avoid][avoid], especially
[classification][a01], [control premises][a02] and [scope][a07]. The
[review][review] assesses this exact note and the [small record][record].

## 1. Comparing the deflated zero sum with an imaginary-axis observation

Use the unchanged complete source and normalization in
[BW-01 Contract 02][source]. Write F(z)=H(T,z). Its evenness, order one,
and F(0)>0 give the paired product

\[
F(z)=F(0)\prod_{\rho>0}(1-z^2/\rho^2)^{m_\rho}.
\]

All roots here are real by the threshold hypothesis; their positive
representatives have multiplicities m_rho. These standard inputs and the
paired factorization are stated in [Polymath, Section 3][polymath3]. No
unproved assertion about the time-zero zeta zeros is used. The product
and the second-log-derivative sums converge locally away from the roots.
There is no quadratic exponential factor: the order-one premise matters.

Deflate just the two copies at +a, putting g(z)=F(z)/(z-a)^2. The
predecessor's [deflation calculation][predecessor] gives

\[
-(\log g)''(a)=S_a
=\frac{1}{2a^2}
 +\sum_{\rho>0,\,\rho\ne a}m_\rho
 \left\{\frac{1}{(a-\rho)^2}+\frac{1}{(a+\rho)^2}\right\}.       \tag{2}
\]

A local logarithm, or log|g| on the real axis, gives the same derivative.
The first term is the two surviving roots at -a. Define

\[
D_T(b)=\frac{d}{db}\log H(T,ib),\qquad
\frac{D_T(b)}b=\sum_{\rho>0}\frac{2m_\rho}{\rho^2+b^2}.          \tag{3}
\]

For rho!=a the exact difference

\[
\frac{1}{(a-\rho)^2}+\frac{1}{(a+\rho)^2}
-\frac{2}{a^2+\rho^2}
=\frac{8a^2\rho^2}{(a^2-\rho^2)^2(a^2+\rho^2)}>0
\]

allows summation of positive terms. At b=a, the positive root a of
multiplicity two contributes 2/a^2 to (3). Keeping the mirror term in
(2) therefore gives the useful subtraction constant

\[
S_a\ge\frac{D_T(a)}a-\frac{3}{2a^2}.                          \tag{4}
\]

The even quartic attains equality in (4), so the constant cannot be
improved on the general paired-product class without additional input.

## 2. A complete-source lower bound for D_T

For b>0 the theta integral H(T,ib) is strictly positive. Let mu_(T,b)
be the probability measure proportional to
e^(T u^2) Phi(u) cosh(bu) du on u>=0. Direct differentiation yields

\[
D_T(b)=\mathbb E_{T,b}[u\tanh(bu)],\quad
\partial_T D_T(b)=\operatorname{Cov}_{T,b}
                 (u^2,u\tanh(bu))\ge0.                      \tag{5}
\]

Both functions of u are increasing. The covariance is half the double
integral of the product of their increments, hence nonnegative. All
differentiations are dominated on compact parameter sets by the complete
super-exponentially decaying source. This step needs positivity, not
real zeros. In particular, D_T(b)>=D_0(b) for T>=0.

The exact [time-zero xi identity][polymath1] and its functional equation
give H(0,ib)=xi(sigma)/8, sigma=(b+1)/2. For b>=5, sigma>=3 and

\[
D_0(b)=\frac12\left\{\frac1\sigma+\frac1{\sigma-1}
 -\frac12\log\pi+\frac12\psi(\sigma/2)
 +\frac{\zeta'}{\zeta}(\sigma)\right\}.                       \tag{6}
\]

The integral in [DLMF 5.9.13][digamma] proves
psi(x)>log(x)-1/x for x>0: its integrand correction is strictly greater
than -e^(-xt), since 1/(e^t-1)<1/t. Also, the positive Dirichlet series
for -zeta'/zeta, followed by the integral test, gives

\[
0<-\frac{\zeta'}{\zeta}(\sigma)
\le\sum_{n\ge2}\frac{\log n}{n^\sigma}
\le E(\sigma):=2^{-\sigma}
 \left(\log2+\frac{2\log2}{\sigma-1}
                  +\frac{2}{(\sigma-1)^2}\right).            \tag{7}
\]

Here log(x)/x^sigma decreases on [2,infinity) for sigma>=3; (7)
includes the entire tail. Substitution in (6) cancels the 1/sigma term:

\[
D_0(b)>\frac14\log\frac{\sigma}{2\pi}
             +\frac{1}{2(\sigma-1)}-\frac12E(\sigma).
\]

For sigma>=3,
(sigma-1)E(sigma)<(sigma+2)2^(-sigma)<=5/8<1, using log2<1 and
2/(sigma-1)<=1. The last positive correction can thus be discarded:

\[
\boxed{D_T(b)>\tfrac14\log((b+1)/(4\pi))\quad(T\ge0,\ b\ge5).} \tag{8}
\]

Equations (4) and (8) prove the first inequality in (1). The second is
equivalent to a log((a+1)/(4pi))>8. At a=20, use pi<22/7 and
log x>=2(x-1)/(x+1) for x>=1: its left side is greater than
20*(118/235)>8. It increases for a>=20. Thus the improvement covers
the entire claimed height interval, not just the table's four values.

The table gives outward enclosures for ell(a), with deliberately rounded
ratio lower bounds. These are evaluations of an analytic coefficient at
hypothetical parameters, not event measurements. The [checker][checker]
uses exact fractions, alternating arctangent bounds for pi and a
geometrically bounded logarithm series.

| Hypothetical a | Previous 1/(2a^2) | Certified interval for ell(a) | ell / previous exceeds |
| --- | --- | --- | --- |
| 20 | 0.00125 | [0.002668727384426, 0.002668727384427] | 2.13498190 |
| 100 | 0.00005 | [0.005060240674679, 0.005060240674680] | 101.20481349 |
| 1000 | 0.0000005 | [0.001092932633086, 0.001092932633087] | 2185.86526617 |
| 10000 | 0.000000005 | [0.000166970403000, 0.000166970403001] | 33394.08060003 |

The leading size changes from 1/(2a^2) to log(a/(4pi))/(4a).
This is a lower bound; no upper control on S_a is supplied.

## 3. Transfer to the two BW-01 time faces

Choose a rectangle R={|t-T|<=delta, |x-a|<=rho} with 0<delta<T
and 0<rho<a. Let B_j>=sup_R |partial_x^j H| for j=3,...,6.
Set b2=|h2|/2 and impose

\[
B_3\rho+B_4\delta\le |h_2|/2,\qquad B_3\delta<b_2\rho.        \tag{9}
\]

The heat equation gives |Hxx(t,x)-h2|<=B3*rho+B4*delta,
and |Hx(t,a)|<=B3*|t-T|. Thus Hxx has fixed sign and magnitude
at least b2, and Hx has opposite signs on the spatial walls. There is
one real analytic critical curve c(t) in R, with c(T)=a and
|c(t)-a|<=B3*|t-T|/b2. In particular its two selected values lie
on the two time faces, at possibly different spatial positions.

Let V(t)=H(t,c(t)) and v(t)=V(t)/h2, with the constant signed h2
normalizer. Differentiation along Hx=0 gives

\[
c'=H_3/H_2,\quad V'=-H_2,\quad V''=H_4-H_3^2/H_2,
\]
\[
v(T)=0,\quad v'(T)=-1,\quad
v''(T)=-\tfrac13(h_3/h_2)^2-6S_a<-C,
\quad C:=\tfrac13(h_3/h_2)^2+6\ell(a)>0.                     \tag{10}
\]

All H_j in curve identities are evaluated at (t,c(t)). One more
derivative, with no differentiation of a numerical error estimate, is

\[
V'''=-H_6+\frac{3H_3H_5}{H_2}
 -\frac{3H_3^2H_4}{H_2^2}+\frac{H_3^4}{H_2^3}.
\]

Consequently the complete bound

\[
|v'''|\le K:=\frac1{|h_2|}
 \left(B_6+\frac{3B_3B_5}{b_2}
       +\frac{3B_3^2B_4}{b_2^2}+\frac{B_3^4}{b_2^3}\right)     \tag{11}
\]

pays both Taylor remainders. For 0<s<=delta,

\[
v(T+s)+v(T-s)\le-C s^2+\frac K3s^3.
\]

In particular the delivered finite-face restriction is

\[
\boxed{0<s\le\min\{\delta,3C/(2K)\}
\ \Longrightarrow\ v(T+s)+v(T-s)\le-\tfrac C2s^2<0.}          \tag{12}
\]

Omit the second cap if K=0. A weaker fully explicit coefficient C=6ell(a)
also works. Finite complete moments M_j(T+delta) are valid B_j; choosing
rho and then delta sufficiently small ensures (9) at each exact double
event. No uniform positive radius as T approaches zero, a grows or h2
approaches zero is claimed.

The signed restriction is compatible with the ordinary collision:
V'/h2<0 throughout this curve, so v(T-s)>0 and v(T+s)<0.
It neither pays the rest of the boundary nor changes the inherited local
degree -1. BW-01 still needs an independent, incompatible arithmetic
bound; a stronger necessary concavity alone does not supply one.

## 4. Complete-source and numerical-error interface

The proof uses exact full integrals and products. Equations (5)--(8)
have no omitted theta modes, contour shifts or numerical quadrature.
The Euler-series majorant (7) pays its entire infinite tail. The finite
transfer uses actual derivative suprema, bounded by
M_j(b)=integral_0^infinity e^(b u^2) Phi(u) u^j du, b=T+delta.
These finite moments apply for every finite b. This establishes an
analytic transfer, not an acquired numerical theta neighborhood.

For a future numerical realization with b<1, reuse exactly the complete
N=4,U=1 payment in [BW-01 Note 03, section 3][bw01]: for each j<=6,
finite-integral quadrature/rounding plus e^b mathcal B_4/8 plus
mathcal T_6(b). The omitted modes on [0,1] and all-mode exterior on
[1,infinity) are disjoint and exhaustive. Apply that budget separately
to every required moment or signed derivative. For j=2,3,4, event
uncertainties |T-That|<=DeltaT, |a-ahat|<=Deltaa add
M_(j+2)(b)*DeltaT+M_(j+1)(b)*Deltaa, with b covering all paths.
This needs no derivative beyond order six. A moment bound over an
uncertain time interval is taken at its upper endpoint.

For completeness, let |h_j-hhat_j|<=d_j and take a certified rational
L<=ell(a), L>0. If a in [a_-,a_+] with a_->=20, a valid interval
lower bound is log((a_-+1)/(4pi))/(4a_+)-3/(2a_-^2); enclose the
logarithm outwards. The raw necessary restriction is

\[
Q_L=2h_3^2-3h_2h_4-18Lh_2^2>0.
\]

For the same polynomial Qhat_L in the approximated jets, a complete
product allowance is

\[
\begin{aligned}
|Q_L-\widehat Q_L|\le{}&2(2|\widehat h_3|d_3+d_3^2)\\
 &+3(|\widehat h_2|d_4+|\widehat h_4|d_2+d_2d_4)\\
 &+18|L|(2|\widehat h_2|d_2+d_2^2).                           \tag{13}
\end{aligned}
\]

If the chosen interval lower bound is nonpositive, it is unusable for
this positive-C consumer. For normalization, require
q=|hhat2|-d2>0, use b2=q/2, enforce (9) with q in place of |h2|,
and use 1/q in (11). Then C=6L is safe without a measured h3 ratio.
Any computed boundary values require their own complete acquisition and
critical-position allowances; none are represented as measured here.
No inequality Qhat_L+error<=0 has been obtained. Such an independent
opposing upper bound would belong to the [threshold-sign route][sibling];
it is not a consequence of (13).

## 5. Controls and verification

The exact checker evaluates polynomial coefficients, differentiates them,
and separately forms their root sums. It also substitutes the critical
curve through second order into the finite heat polynomial and checks
the second and third derivatives in (10)--(11). Every comparison is
rational; no floating sign or sampled winding decision occurs.

| Control or family | Premise and outcome |
| --- | --- |
| Even quartic (z^2-a^2)^2 | S=1/(2a^2), D(a)=2/a; (4) is sharp. At a=20, D=0.1 fails the new floor >0.128374547688533. The exact xi/positive theta source input is absent. |
| Negative quartic | Same normalized jet and heat-series identities; no sign-normalizer mistake. Logarithmic derivatives use log|P(ib)|; positivity in (5) is not assigned to this control. |
| Degree-eight polynomial (z^2-400)^2(z^2-441)(z^2-484) | All-real slice, double event at a=20. D(a)=358361/1858610 exceeds the scalar floor, and S=742751321/593056800. The bound permits this collision. It has no exact theta source. |
| Positive-kernel threshold controls q and q_(T,a) | Positivity can support (5), but the exact xi identity and unchanged theta source are absent. Apply (2)--(4) only if the stated order-one product premise also holds; no theta lower bound or tail is assigned to them. |
| Weighted-square and finite-prime controls | Unchanged time-zero xi identity fails. The finite weighted-square controls have no all-real heat time; no all-real threshold is supplied for the orbit constructions. Their local events are not substituted into (2) without that premise. |
| Reflected and positive-primitive controls | Positive auxiliary channels or reflection do not give the exact time-zero xi identity. No numerical damping threshold or claim that they violate (8) is made. |
| Euler-factor controls | They fail the unchanged-source identity but **pass the scalar lower bound**, as the exact calculation below shows. A positive threshold is compatible with this necessary restriction. |

For the last row, [the control's own formula][controls] is
H_0^(c,p)(ib)=H_0(ib)(1+c cosh(alpha b)), alpha=(log p)/2, c>0.
Therefore

\[
D_0^{(c,p)}(b)=D_0(b)
 +\frac{c\alpha\sinh(\alpha b)}{1+c\cosh(\alpha b)}>D_0(b).
\]

Their source is positive, so (5) propagates this bound to every T>=0.
**The imaginary-axis floor also holds for the Euler-factor controls; it
does not distinguish theta from every positively colliding family.**
This is an analytical own-source screen, not a new numerical event or a
claim that a particular control's threshold has height >=20 and exact
multiplicity two. The table's premise failures do not imply that their
necessary inequalities have the opposite sign.

For the finite-transfer check, the a=1 quartic has T=1/4, rho=1/8,
delta=1/256, h2=8 and complete B3=27,B4=24,B5=B6=0. Its own
mirror condition gives C=6; (9) holds, and K=741393/512 gives
3C/(2K)=512/82377>delta. The exact pair is -6s^2 and the paid
bound is at most -3s^2 on 0<s<=delta. This tests the transfer with
the control's own curvature, not the theta coefficient outside its range.

The [record][record] includes four polynomial cases, this finite-transfer
check, four outward coefficient enclosures and source SHA-256 hashes.
It binds the uncommitted source versions over Git parent
b39c6cc9b4756bc14c2e500e327169db88571d1f. Hashes identify files;
the written proof and exact inequalities carry the mathematical claims.

## 6. What is completed and what remains

BW-08's first bounded task delivers a quantitative improvement over the
mirror bound and a finite-time transfer to a specified BW-01 observation.
It covers every hypothetical exact double event with T>0 and a>=20;
its analytic constants are event-dependent. The proof only needs an
all-real slice, so it does not exploit the additional minimality of T
as a threshold. This limits what its sign can discriminate.

The next useful task is to test an arithmetic upper bound on Q_L, or
an opposing lower bound on the critical-value face pair, with matched
complete errors against (12) or (13). Another verification of (1) alone adds no
exclusion. No numerical radius, all-height collision exclusion,
multiplicity extension, or later-time contradiction is recorded. The
single [progress register][progress] retains those obligations.

[contract]: 02_IMAGINARY_AXIS_CONTRACT_20261019.md
[initial]: 01_INITIAL_RESEARCH_NOTE_20261019.md
[review]: ../reviews/01_IMAGINARY_AXIS_SELF_REVIEW_20261019.md
[record]: ../numerics/IMAGINARY_AXIS_CONTROLS_20261019.json
[checker]: ../numerics/check_imaginary_axis_bound.py
[source]: ../../01_local_double_winding/notes/02_PAIRED_FACE_CONTRACT_20261019.md
[bw01]: ../../01_local_double_winding/notes/03_PAIRED_FACE_REMAINDER_OBSTRUCTION_20261019.md
[sibling]: ../../../../02_threshold_jet_sign/notes/01_INITIAL_RESEARCH_NOTE_20261019.md
[progress]: ../../../research-progress/01_THRESHOLD_BOUNDARY_WINDING_PROGRESS_20261019.md
[predecessor]: ../../../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex
[results]: ../../../../../../../result-summaries/README.md
[laws]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[polymath1]: https://arxiv.org/html/1904.12438v2#S1
[polymath3]: https://arxiv.org/html/1904.12438v2#S3
[digamma]: https://dlmf.nist.gov/5.9.E13
