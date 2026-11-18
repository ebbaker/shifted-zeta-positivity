# The pair equation, interaction equation, and aggregate inputs

17 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Chat0007, **Review Volterra manuscript results**,
thread `01a1eb96-c257-77a3-96be-ee1cb0279757`, turn
`01a1ebbf-948c-72e3-8c26-397b88609fbe`. The guarded registry records an empty
model-configuration list; actual model and reasoning effort are unavailable.
No collaborator was dispatched.

**Expository discussion only.** This answers Edward's request to explain
the equations and the phrase “existing counts and broad moments” in
[discussion20][discussion20]. It selects no new estimate, performs no new
control experiment, changes no scientific status, and leaves B12
unactivated. Statements below retain the manuscript's internally assessed
scope; this is not independent specialist validation.

Read the [result index][results], especially [cluster18][cluster] and
[controls12][controls], and the [avoid index][avoid], especially
[classification01][a01], [premises02][a02], [scope07][a07] and
[separate-estimate losses12][a12]. The documentary control screen in
discussion20 remains applicable. In particular, the quartic collision
control passes favorable interaction but fails the strict incoming-cost
condition; the exact-count examples concern a fixed-slice analytic class
and do not supply a canonical common-time heat family.

Equation numbers refer to the current 75-page integrated [manuscript][master],
*Jacobi dynamics, signed error, and cluster transport for the Newman heat
flow*, by Edward Baker. The reading PDF and the retained build PDF both
match the SHA-256 in [build record24][build]; every current manuscript source
listed in that record also matches its recorded final hash. Equation numbers
were read from that build's auxiliary file. This check performs no rebuild
or source evaluation.

## Pair coordinates and physical time

The field in (2.2) is

\[
H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\qquad \partial_tH_t=-\partial_z^2H_t.
\]

Here \(t\) is physical Newman time. Increasing \(t\) has the negative
Laplacian sign in this convention. Transport toward time zero from a
positive anchor uses decreasing \(t\). The probability-normalized field
in (10.10) has an additional scalar term; that term does not move zeros
and drops out of the pair law.

Suppose a conjugation-invariant contour encloses exactly two zero
occurrences, with multiplicity, and an independently established
zero-free collar separates them from the exterior. The contour moments
in (10.13) define analytic coordinates through a double. In root notation,
(10.14) is

\[
c=\frac{z_++z_-}{2},\qquad
D=\left(\frac{z_+-z_-}{2}\right)^2.
\]

This is an algebraic square, and \(c,D\in\mathbb R\). A real distinct pair
\(c\pm r\) has \(D=r^2>0\), a nonreal conjugate pair \(c\pm ib\) has
\(D=-b^2<0\), and a real double has \(D=0\). Thus the real gap is
\(2\sqrt D\) when \(D>0\). The contour formulation avoids the singularity
of individually labeled roots at a collision.

Deflate the selected pair:

\[
H_t(z)=Q_t(z)A_t(z),\qquad Q_t(z)=(z-c)^2-D,
\qquad g=A_z/A.
\]

The factor \(A_t\) is analytic and zero-free in the counted disk. The
regular drift \(K\), defined by the contour in (12.2), equals the divided
difference \(g[z_-,z_+]\), with \(K=g'(c)\) at a double. Write \(M=-K\).
The exterior divisor formula (14.4) gives

\[
M=\sum_{\rho\,\mathrm{exterior}}
  \frac{1}{(z_+-\rho)(z_--\rho)}
 =\sum_{\rho\,\mathrm{exterior}}
  \frac{1}{(\rho-c)^2-D}.
\]

The sum is absolutely convergent and counts multiplicities. It includes
all exterior zeros. Conjugate terms make the sum real. It measures the
difference of exterior influence on the two roots, rather than their
common translation. For \(\rho=c+x+iy\), a nonreal conjugate pair
contributes twice

\[
q(x,y,D)=\frac{x^2-y^2-D}{(x^2-y^2-D)^2+4x^2y^2},
\tag{14.6}
\]

and a real occurrence contributes \(q(x,0,D)\). Its sign depends on the
geometry. In particular, off-axis exterior roots need not contribute
negatively. At a double,

\[
q(x,y,0)=\frac{x^2-y^2}{(x^2+y^2)^2}
        =\frac1{x^2+y^2}-\frac{2y^2}{(x^2+y^2)^2}.
\]

## The pair equation and its backward cost

Equation (12.4) is written as \(D'=2+4KD\), equivalently

\[
D'=2-4MD.
\]

For simple roots the heat equation gives

\[
z_\pm'=\frac{2}{z_\pm-z_\mp}+2g(z_\pm).
\]

Taking the difference and differentiating the squared half-gap gives
the displayed pair law. Proposition 12.2 proves it by contour moments
through a double, so the simple-root calculation is explanatory rather
than a missing hypothesis.

The constant 2 comes from the selected roots' mutual interaction. The
term \(-4MD\) accounts for the exterior's effect on their separation.
For \(D>0\), positive \(M\) reduces the rate of opening in increasing
physical time; the derivative can be negative if \(MD>1/2\). Negative
\(M\) increases that rate. This forward-time interpretation should be
kept separate from the backward transport comparison.

At a double, (10.16) gives

\[
D(t_*)=0,\qquad D'(t_*)=2,\qquad
D(t)=2(t-t_*)+O((t-t_*)^2).
\]

An isolated double therefore has a conjugate pair immediately before
it and a real pair immediately after it in increasing \(t\). The law
allows such a collision at positive time when followed backward. It
does not by itself establish the time-zero reality objective.

For \(t<v\), put

\[
W(t,v)=\exp\!\left(-4\int_t^v M(s)\,ds\right).
\]

Equation (12.9) becomes

\[
W(t,v)D(t)=D(v)-2\int_t^vW(s,v)\,ds.
\]

The right-hand side compares the independently known incoming squared
half-gap \(D(v)\) with a weighted backward time cost. A strict positive
margin proves \(D(t)>0\). If \(M\ge\kappa>0\) throughout the interval,

\[
2\int_t^vW(s,v)\,ds
\le\frac{1-e^{-4\kappa(v-t)}}{2\kappa}.
\]

As \(\kappa\downarrow0\), this allowance tends to \(2(v-t)\).
Positive interaction can reduce the backward cost, but its sign alone
does not compare that cost with the incoming gap. The manuscript's
even-quartic control has positive \(M\) and a collision; it fails the
strict incoming-cost condition. Also, the scalar law is linear in \(D\)
only when \(M\) is supplied: in the full system \(M\) depends on \(D\)
and on the evolving exterior zeros.

## What has been established about \(M\) and \(D\)

The structural results are exact coordinates through a double, the
complete exterior formula, the pair law, and the backward identity.
They require the stated counted-pair geometry. They do not acquire
such a geometry for every potential collision or address every higher
multiplicity cluster.

Appendix B records one complete-source interval certificate centered
near \(14010.1\), on \(0\le t\le0.1\):

\[
0.599329616\le M(t)\le0.615518848,
\]
\[
D(0)\in[0.00142117117778,\,0.00142118228384],
\]
\[
D(0.1)\in[0.17873684703288,\,0.17873685811).
\]

Proposition 12.3 and the recorded geometry give \(D'\ge19/32\), so
the direct endpoint is the interval minimum. The signed transport
comparison using \(M\ge0.59\) independently yields \(D(0)>0.00074055469\).
The direct enclosure is stronger. A later acquisition from 176 moving
real brackets gives \(M>0.5937558081007126288\) without reusing the
measured drift band; the pair's positive \(D\) was already established.
These are internally assessed local certificates, not new global zero
coverage.

At growing height, the far exterior is positive in the domain of
Theorem 15.2. Equation (15.5) gives its main term

\[
M_{\mathrm{far}}\sim\frac{\log(c/(4\pi))}{2\pi R}
\]

when the displayed error is smaller than the main term. At the
manuscript's choice \(R=\sqrt L\), \(L=\log T\), \(c\in[T,2T]\),
equation (15.8) gives

\[
\ell^2M_{\mathrm{far}}
 =\frac{1}{2\pi L^{3/2}}+O(L^{-2}),\qquad \ell=L^{-1}.
\]

Thus the favorable far contribution tends to zero in microscopic
normalization. It does not dominate an uncontrolled near contribution.
Sections 16–17 add quantitative mean, exception, occupation and dynamic
estimates described below. None establishes \(M\ge0\) or \(D\ge0\)
uniformly for every eligible pair at all heights and times.

## The interaction equation and its normalization

With exterior \(w_j=\rho_j-c\), define

\[
m_j=(w_j^2-D)^{-1},\qquad S_p=\sum_jm_j^p,
\qquad M=S_1.
\]

Theorem 17.1 proves

\[
M'=2M^2-12S_2-16DS_3.\tag{17.1}
\]

Differentiating the complete interaction, using the heat flow and
symmetrizing the exterior-exterior terms produces the cancellation
in this identity. Its contour proof covers both signs of \(D\), a
target double and multiple exterior roots.

Freeze \(\ell=1/\log T\) on a height band \(c\in[T,2T]\), and put

\[
\sigma=(t-t_0)/\ell^2,\qquad
\delta=D/\ell^2,\qquad m=\ell^2M,\qquad \mu_j=\ell^2m_j.
\]

Here \(T\) is height and \(t\) is physical time. The normalized scalar
\(m\) differs from the individual physical summand \(m_j\). The nominal
spacing scale is of order \(\ell\); the corresponding squared-gap and
time scale is \(\ell^2\). These scale choices do not assert a lower
bound on every actual zero gap.

Since \(dm/d\sigma=\ell^4M'\), equation (17.5) is

\[
\frac{dm}{d\sigma}=2m^2-\mathcal F,\qquad
\mathcal F=12\sum_j\mu_j^2+16\delta\sum_j\mu_j^3.
\]

The companion gap equation is \(d\delta/d\sigma=2-4m\delta\).
The term \(2m^2\ge0\) pushes the scalar \(m\) upward. The forcing
\(\mathcal F\) is an exact observable of the same exterior configuration;
it is neither an independent input nor a random noise. The squares and
cubes are ordinary complex powers, not absolute powers. Conjugation
makes their sums real, but does not make them nonnegative. Also,
\(\mathcal F\) is distinct from the manuscript's normalized field \(F_t\).
Knowing \(m\) and \(\delta\) alone does not determine the higher sums,
so these two displayed equations are not a closed two-variable system.

On an independently enclosed count-two tube with
\(|D|\le d\ell^2\) and exterior collar \(a\ell\), where
\(T\ge64\) and \(\max(2,4\sqrt d)\le a\le L\), equation (17.4) proves

\[
\sum_j|\mu_j|^p\le B_pL,\qquad
B_p=\frac{14C_{\rm u}(16/15)^p}{a^{2p}},\quad p=1,2,3.
\]

Consequently \(|m|\le B_1L\), \(|\mathcal F|\le C_FL\), where
\(C_F=12B_2+16dB_3\), and

\[
m_\sigma\ge2m^2-C_FL.
\]

For \(h=\sqrt{C_FL/2}\), (17.6) implies

\[
m(\sigma)\ge-h\coth(2h\sigma),\qquad\sigma>0.
\]

After a fixed positive elapsed scaled-time buffer, the allowed negative
part improves from order \(L\) to order \(\sqrt L\), for fixed collar
parameters. This bounds the negative part, not the full absolute size
of \(m\). The integrated estimate (17.7) improves the transport-multiplier
allowance to \(O(L)\exp(O(s\sqrt L))\) over scaled duration \(s\), as in
(17.8), from the count-only \(\exp(O(sL))\). The initial layer is included
in that integrated estimate. Both allowances still grow with height.

The comparison needs an **upper** bound on \(\mathcal F\). Even a
prospective height-independent upper bound would yield an order-one
negative barrier by this same comparison, rather than positivity by
itself. An incoming gap and a persistent counted tube remain separate
requirements. This is an explanation of the existing comparison, not a
proposed or proved new source estimate.

## What “counts and broad moments” means

Write the complete zeros as \(\rho_j=x_j+iy_j\), with multiplicities.
These are deterministic sums over zeros. The moments here concern
imaginary coordinates of zeros, not the source-variable or Jacobi
coefficient moments considered elsewhere in the investigation.

**Counts.** Equations (15.1)–(15.3) supply

\[
N_t(X)=\#\{j:0<x_j\le X\}=G_t(X)+O(\log(2+X)),
\]
\[
G_t(X)=\frac{X}{4\pi}\log\frac{X}{4\pi}-\frac{X}{4\pi}
+\frac{11}{8}+\frac{t}{16}\log\frac{X}{4\pi},
\]
\[
\#\{j:U\le x_j\le U+1\}\le C_{\rm u}\log(2+|U|).
\]

They hold on \(0\le t\le1/2\), with the displayed restrictions on \(X\).
They describe the horizontal projection of every zero, including
nonreal ones. Near height \(T\), a unit interval may contain \(O(L)\)
occurrences under this upper bound. The cumulative discrepancy \(O(L)\)
also exceeds the order-one main-term increment across a microscopic
interval of length \(\ell\). Therefore these inputs do not give a
uniform order-one population bound in every such microscopic interval,
nor do they give the imaginary marks or the geometry conditional on a
selected pair. This is the source of the factor \(L\) in (17.4).

**Broad transverse moments.** Equations (16.4)–(16.5), with
\(L_U=\log U\), \(U\ge8\), fixed \(0<b<1/2\), and \(0<v<1\), give

\[
\#\{j:U\le x_j\le2U,\ |y_j|>v\}
 \le B_bUL_Ue^{-bvL_U},
\]
\[
\sum_{U\le x_j\le2U}|y_j|^k
 \le\frac{k!B_b}{b^k}\frac{U}{L_U^{k-1}},\qquad k\ge1.
\]

For example, the second and third moment allowances are \(O(U/\log U)\)
and \(O(U/(\log U)^2)\). They quantify the total transverse spread on
an entire height band of width \(U\). They do not determine how the
allowed spread is arranged within a microscopic neighborhood of a
particular \(c\). A bounded number of zeros with \(|y|=O(1/\log U)\)
contributes only \(O((\log U)^{-2})\) to the second moment, far below its
whole-band allowance. This scale comparison explains room for exceptional
clusters without constructing an additional canonical example.

The manuscript connects these moments to the signed interaction using
the radial identity (16.7). The potentially adverse part at \(D=0\) is
\(2y^2/|\rho-c|^4\). Its normalized near sum is the observable
\(\Xi_{a,R}(t,c)\) in (16.6), and (16.8) gives the corresponding lower
bound on the signed interaction for either sign of \(D\). Equation
(16.9) improves the mean over ordinary centers \(X\in[T,2T]\) from
\(C_0/a\) using counts alone to \(C_s/a^3\) using transverse moments.
The mean is an integral in \(X\); it is not a pointwise assertion at
the center of each selected pair.

Further consequences are an eligible negative-pair slice count
\(O(TL e^{-2ba/3})\), equation (16.12), and a negative-pair occupation
allowance with leading term \(O(T/L)\) plus the displayed boundary term,
equation (16.15), over fixed physical duration and fixed \(a\).
Occupation measures the integral of the number of negative pairs over
time. These growing allowances do not exclude a single exception, and
the visibility conversion in (17.9) does not remedy that limitation.

Proposition 15.3 gives the sharper information-class check: its
fixed-slice analytic examples have identical projected counts yet

\[
m_+=\tfrac12+O(1/\log c),\qquad
m_-=-\tfrac1{16}+O(1/\log c),\tag{15.9}
\]

and also satisfy the stated broad density and moment upper bounds with
enlarged constants. They do not form the canonical theta heat flow or
a supplied common-time family. The precise exclusion is a sign
deduction from those aggregate inputs alone in that fixed-slice class.

Thus the sharpened question concerns additional information about the
exterior geometry around the selected pair, or its joint evolution with
\(D\), that yields a stronger one-sided or integrated interaction bound
with a quantified effect on the incoming-gap comparison. Discussion20's
recommendation remains a proposed standard for B12; no estimate or
execution request is selected here.

[discussion20]: 20_VCD_GT_MANUSCRIPT_AND_B12_STRATEGY_DISCUSSION_20261117.md
[master]: ../../../manuscript/main.tex
[build]: ../../numerics/24_VCD_GT_RECENT_ANALYTICAL_MANUSCRIPT_BUILD_20261117.json
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
