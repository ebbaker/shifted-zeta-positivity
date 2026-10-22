# A bounded theta charge certificate and its direct comparison

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from this chat's turn metadata.
Analytic derivation and interval computation; same-assistant assessment,
without independent specialist review.

The first BW-12 experiment certifies relative charge zero on a smooth
complex-time ellipsoid that contains a real theta zero. Its complete
boundary homotopy gap exceeds **0.00007495**. Direct derivative exclusion
on the same domain has the stronger floor **0.00007993** and requires
six source integrals instead of eight. This is a finite method benchmark,
not evidence toward global simplicity. A quadratic heat collision on the
same-sized ellipsoid is correctly assigned charge one.

The [progress register][progress] tracks RCH-01 through RCH-04. Read this
with the [result index][results], [local multiplicity summary][local],
[control register][controls], and [avoid index][avoid], especially
[target classification][a01], [matching controls][a02],
[lifts][a03], and [scoped exclusions][a07]. The inherited local charge and
Hopf normalization are in [Investigation 22 Note 08][g08] and
[BW10 Note 25][n25]. Their review status is unchanged.

## Domain and reference

Use the repository's unchanged normalization
\[
 H(t,z)=\int_0^\infty\Phi(u)e^{tu^2}\cos(zu)\,du,
 \qquad
 \Phi(u)=\sum_{n\ge1}(2\lambda_n^2e^{9u}-3\lambda_ne^{5u})
                     e^{-\lambda_ne^{4u}},\quad \lambda_n=\pi n^2.
 \tag{1}
\]
Every summand is positive for real \(u\ge0\). Double-exponential decay
makes \(H\) jointly entire, with \(H_t=-H_{zz}\). No RH assumption is
used. The earlier [complete theta evaluator][prior] fixes the same
normalization; the present complex-time payments are derived below.

Put
\[
 a=113/4=28.25,\quad T=1/100,\quad R=1/8,\quad w=z-a,
 \qquad B=\{(t,z):|t/T|^2+|w/R|^2<1\}.                 \tag{2}
\]
This is a bounded smooth real four-dimensional ellipsoid, oriented by
\(d\Re t\wedge d\Im t\wedge d\Re z\wedge d\Im z\), with outward
boundary orientation. It requires no corner smoothing or boundary
mesh. Its physical slice is a real ellipse, and its time-zero interval
is \(28.125<z<28.375\). All estimates below also hold on the containing
closed polydisc \(|t|\le T,|w|\le R\).

Let \(h_j=\partial_z^jH(0,a)\), and let real dyadic numbers \(c_j\)
approximate \(h_j\), with \(|h_j-c_j|\le\delta_j\), for \(0\le j\le3\).
The reference boundary map is the restriction of
\[
 F(t,w)=(c_0+c_1w-c_2t,\ c_1+c_2w-c_3t).             \tag{3}
\]
It is the affine Taylor approximation to the vector \((H,H_z)\).
There is no requirement that an arbitrary reference pair itself be the
exact jet of a heat solution. Define the certified lower bound
\[
 b=|c_1|-R|c_2|-T|c_3|.                              \tag{4}
\]
If \(b>0\), the second component of \(F\) is nonzero throughout the
polydisc. Thus \(F\) extends without zeros over \(\overline B\), its
boundary degree is zero, and \(\inf_{\partial B}\|F\|\ge b\).
The reference degree is proved, not estimated from sampled phases.

## Complete Taylor and source payments

For \(j=2,3,4,5\), write
\[
 M_j(T,R)=\int_0^\infty\Phi(u)u^j e^{Tu^2+Ru}\,du.    \tag{5}
\]
Along the segment \((st,sw)\), \(0\le s\le1\), the exponential and
both exponential terms in the cosine are bounded by
\(e^{Tu^2+Ru}\). The second derivative along this segment inserts a
factor bounded by \((|t|u^2+|w|u)^2\). Taylor's integral remainder
therefore gives, for \(j=0,1\),
\[
 \left|\partial_z^jH(t,a+w)-h_j-wh_{j+1}+th_{j+2}\right|
 \le L_j:=\frac{R^2M_{j+2}+2RTM_{j+3}+T^2M_{j+4}}2. \tag{6}
\]
The signs of the time terms follow from the backward heat equation.
With upper enclosures for the moments, use
\[
 e_j=\delta_j+R\delta_{j+1}+T\delta_{j+2}+L_j,
 \qquad e=(e_0^2+e_1^2)^{1/2}.                       \tag{7}
\]
Then \(\|G-F\|\le e\) on the entire closed domain. This pays complex
time, complex position, and interpolation in both variables. No sampled
boundary minimum or unbounded derivative extrapolation is used.

The eight acquisitions are the four real jets \(h_0,\ldots,h_3\) and
the four positive moments \(M_2,\ldots,M_5\). Each core integral uses
exactly modes \(1\le n\le4\) and \(0\le u\le1\), evaluated by Acb
ball integration at 192-bit precision. The callback is entire; there
are no branch-cut operations. The [python-flint documentation][flint]
specifies the validated integration interface. Requested tolerances
are accuracy goals; the returned radii, rather than those goals, enter
\(\delta_j\). The computation rejects nonfinite or overly wide balls.

Here is the full tail argument, including all omitted modes. For
nonnegative \(T,Y\), the absolute integrand for derivative order \(j\)
is bounded by
\[
 2\lambda_n^2u^j\exp(Tu^2+(9+Y)u-\lambda_ne^{4u}).    \tag{8}
\]
Use \((T,Y)=(0,0)\) for the center jets and \((T,R)\) for the moments.
For \(m=5\), set
\[
 b_m=4\pi m^2-9-Y,\qquad
 q=((m+1)/m)^4 e^{-\pi(2m+1)}.
\]
If \(b_m>0\), \(q<1\), and \(16\pi m^2>2T\), concavity gives
\(Tu^2+(9+Y)u-\pi n^2e^{4u}\le-\pi n^2-b_nu\).
The successive mode ratios are bounded by \(q\); the increasing
\(b_n\) only improves this bound. Consequently
\[
 O_j(T,Y)=\frac{2\pi^2m^4e^{-\pi m^2}j!}
                    {b_m^{j+1}(1-q)}               \tag{9}
\]
bounds the integral of **all** modes \(n\ge5\) on \([0,\infty)\).

For each retained mode, the logarithm of (8), including \(j\log u\),
is concave on \([1,\infty)\) when \(16\lambda_ne^4>2T\). If
\(d_{n,j}=4\lambda_ne^4-9-Y-2T-j>0\), its tangent at one gives
\[
 X_j(T,Y)=\sum_{n=1}^4
       \frac{2\lambda_n^2 e^{T+9+Y-\lambda_ne^4}}{d_{n,j}}. \tag{10}
\]
Thus \(O_j+X_j\) bounds the omitted source integral without a gap or
double counting. Every slope, concavity, and ratio condition is checked
with outward rounding. Center-jet errors add this tail to the returned
quadrature radius. Moment upper bounds add it to the upper endpoint of
the positive core integral. There is no separate discretization error:
the interval quadrature and (6) cover the continuous integrals and domain.

## Certificate and physical coverage

The [receipt][receipt] contains the full balls, per-integral errors and
costs. The following decimals are shortened displays; the implemented
comparisons use outward bounds, not these rounded values.

| Quantity | Computed value or bound |
| --- | --- |
| \(c_0\) | \(1.6903889109070\times10^{-6}\) |
| \(c_1\) | \(-8.7397533525101\times10^{-5}\) |
| \(c_2\) | \(5.0430566946874\times10^{-5}\) |
| \(c_3\) | \(-1.7461315946710\times10^{-5}\) |
| Reference lower bound \(b\) | \(8.0919099497274\times10^{-5}\) |
| Component error \(e_0\) | \(5.8832037946595\times10^{-6}\) |
| Component error \(e_1\) | \(9.8880299673331\times10^{-7}\) |
| Vector error \(e\) | \(5.9657202629561\times10^{-6}\) |
| Boundary gap \(b-e\) | \(>7.495\times10^{-5}\) |
| Direct derivative floor \(b-e_1\) | \(>7.993\times10^{-5}\) |

The straight homotopy \(F+s(G-F)\) is nonzero on \(\partial B\).
Therefore its relative charge, with the inherited normalization, is
\[
 Q_B=\deg(G/\|G\|)=\deg(F/\|F\|)=0.                 \tag{11}
\]
The Hopf integral normalization uses target two-sphere area one, as in
[Rudolph, Section 1][hopf], together with the connection in BW10 Note 25.
No numerical integration of that three-form is needed here.

Under the inherited isolation hypotheses, positivity of local complex
intersection numbers turns (11) into joint-zero exclusion. In this pilot
there is also a direct proof of exclusion, independent of any isolation
argument: (4) and (7) give \(|H_z|\ge b-e_1>0\) everywhere in
\(\overline B\).

The domain is not an example chosen only where \(H\) stays away from
zero. With no further integrals, (6) at \(t=0,w=\pm R/2\) yields
\[
 H(0,451/16)>0,\qquad H(0,453/16)<0.                 \tag{12}
\]
The corresponding balls are approximately
\((7.1527\pm1.44)\times10^{-6}\) and
\((-3.7720\pm1.44)\times10^{-6}\). Real symmetry and the derivative
floor imply a unique simple real zero in this bracket. The certificate
covers its surrounding complex-time ellipsoid, including negative and
positive real time. It makes no assertion about arbitrary heights or
other events outside that ellipsoid.

## Matched cost comparison and the limit of this reference

The direct comparison uses the **same** \(c_1,c_2,c_3\), their errors,
and \(M_3,M_4,M_5\), through
\[
 |H_z|\ge |c_1|-R|c_2|-T|c_3|-e_1=b-e_1.           \tag{13}
\]
It needs neither \(h_0\) nor \(M_2\). Both methods use identical
normalization, domain, precision, source cutoff and mode count.

| Acquisition or consumer | Relative-charge pilot | Direct derivative comparator |
| --- | --- | --- |
| Scalar validated source integrals | 8 | 6 |
| Quadrature callbacks in the recorded run | 2,208 | 1,656 |
| Acquisition time in that run | about 0.0358 s | about 0.0215 s for its subset |
| Boundary or interior mesh cells | 0 | 0 |
| Certified comparison margin | \(>0.00007495\) | \(>0.00007993\) |
| Additional conclusion | boundary degree zero | derivative nonzero on the full domain |

The time comparison sums the direct method's required subset of one
shared acquisition; it is **not** a separately timed performance trial.
Process startup, environment preparation, and explanatory root bracketing
are excluded from both acquisition totals. Counts are the more reliable
comparison. The root bracket establishes coverage and is not required
by either exclusion consumer. The direct implementation is a valid
competitor, not a claim of optimal direct cost.

There is a reason the gap comparison must go this way. Whenever the
reference floor is paid by (4) and errors by (7),
\[
 b-\sqrt{e_0^2+e_1^2}\le b-e_1.                    \tag{14}
\]
Making the boundary grid denser or computing the same coefficients more
accurately cannot reverse (14). This is a scoped dominance statement for
this fixed-component reference floor and these error envelopes, not for
all relative-charge methods or all ways of bounding the reference norm.

There is an even simpler preliminary screen. For a constant reference
\(v\ne0\), holomorphicity gives
\[
 \sup_{\overline B}\|G-v\|=\sup_{\partial B}\|G-v\|. \tag{15}
\]
For each interior point choose a unit linear functional attaining the
norm there and apply the scalar maximum-modulus principle. Thus the
same bound \(e<\|v\|\) already gives the direct interior floor
\(\|G\|\ge\|v\|-e\), at the same acquisition cost. This does not rule
out nonconstant references whose full boundary norm supplies information
unavailable from an interior component floor.

## Collision controls

For the translated quadratic heat model \(H=w^2-2t\), choose
\(F_q=(-2t,2w)\). On the ellipsoid (2),
\[
 \inf_{\partial B}\|F_q\|=2\min(T,R)=1/50,
 \quad\sup_{\partial B}\|G_q-F_q\|=R^2=1/64.
\]
Its gap is exactly \(7/1600>0\). The complex determinant of \(DF_q\)
is \(-4\), whose real determinant is positive, so its degree and the
certified charge are **one**. Direct exclusion must fail at the origin.
A constant degree-zero reference \((1,0)\) fails explicitly at
\((t,w)=(T,0)\): its error is \(51/50>1\). These calculations are
replayed with exact rational arithmetic in the [script][script].

The inherited cubic control \(H=z^3-(4+6t)z+2\) gives
\(z^3=1\), \(t=(-4+3z^2)/6\) at its events. Each Jacobian is
\(-36z^2\ne0\); there are three complex events, with the only real
event at \(t=-1/6\). The replay checks the real event time and the
positive time-zero discriminant 148. This guards against interpreting
all complex charge as forbidden physical charge.

The source-family screens use the inherited proved collision witnesses,
not newly acquired source integrals. On any domain containing one of
those isolated events, a degree-zero boundary approximation must fail
at least one of its certified degree, floor or error premises: a
successful homotopy would contradict the positive local charge. This
argument applies to every finite multiplicity, without substituting
theta moments into a changed source.

| Control family | Premise unavailable from the theta computation |
| --- | --- |
| Polynomial heat controls | The unchanged theta source (1) and its arithmetic coefficients |
| Euler-factor controls | Unchanged Euler data and source (1); their own source errors must be recomputed |
| Weighted-square and finite-prime controls | Unchanged coefficients and full normalized reflection |
| Reflected super-Gaussian control | The canonical integer-square source expansion |
| Smooth shape and positive-primitive controls | The canonical theta arithmetic source, despite their retained shape or primitive data |
| RH-conditional close-source endpoints | Ordinary Dirichlet-series arithmetic; fixed positive tolerance alone cannot exclude their distant doubles |

These are separate preservation lists, as required by the
[control register][controls] and [BW10 source-control note][close]. A
successful certificate in a collision-free subdomain of a control is
permitted. The fresh computational controls here are the quadratic and
cubic; the wider source-family rejection is analytic and inherits the
witnesses' existing status.

## Research decision

RCH-01, RCH-02 and the first RCH-03 comparison are complete **for (2) and
(3)**. The source error is paid, the boundary charge is zero, and direct
exclusion wins both the stated margin and the acquisition count. Stop
optimizing this component-floor reference for an advantage it cannot
have under (14).

A worthwhile next bounded experiment must require both jet components:
for example, a small complex-time domain whose real spatial slice
contains two neighboring simple zeros and the intervening stationary
point. Its polynomial reference would need a separately established
joint degree and a full vector boundary floor; \(H_z\) alone cannot
separate that real interval. Before theta acquisition, specify that
reference, include any unwanted complex-time events, and compare with
direct **joint** exclusion from the same polynomial and errors. This is
a proposed experiment, not an established advantage. RCH-04's
arbitrary-height and multiplicity coverage remains gated; HMC-05 and
HMC-06 retain their existing status.

[progress]: ../research-progress/01_RELATIVE_CHERN_HOPF_CHARGES_PROGRESS_20261021.md
[receipt]: ../numerics/RELATIVE_CHARGE_PILOT_20261021.json
[script]: ../numerics/certify_relative_charge_pilot.py
[prior]: ../../../../../11_arithmetic_collision_rigidity/notes/02_updated_research_plan/07_SHIFTED_EVALUATOR_AND_COMPLETE_ERROR_BUDGET_20261018.md
[g08]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/08_REAL_AND_COMPLEX_COLLISION_MULTIPLICITIES_20261015.md
[n25]: ../../10_rh_implies_simple_zeros/notes/25_MULTIPLICITY_SELECTIVE_CHERN_AND_HOPF_OBSERVATIONS_20261021.md
[close]: ../../10_rh_implies_simple_zeros/notes/05_CLOSE_POSITIVE_SOURCES_AND_NORMALIZED_DOUBLE_ZEROS_20261020.md
[results]: ../../../../../../../result-summaries/README.md
[local]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[flint]: https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.integral
[hopf]: https://arxiv.org/pdf/0912.4974
