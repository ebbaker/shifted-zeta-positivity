# Transport of the first gap after removal of its mean scale

20 November 2026. Mathematical research prepared for Edward Baker with OpenAI Codex assistance. Lead and integration gpt-6.2-astra/ultra, bounded derivations and interval implementation gpt-6.2-sol/ultra. [Decision](../brainstorm/notes/02_EZ_B02_MEAN_CORRECTED_VELOCITY_20261120.md) · [Frozen E03 packet](../research-progress/handoffs/AGC_EZ_E03_REQUEST_R1_20261120.md) · [Live register](../research-progress/02_EZ_ZERO_LOCATIONS_RESEARCH_PROGRESS_20261120.md).

## A signed quantity on a counted edge

Let \(u=x_1(t),v=x_2(t),g=v-u,D=g^2/4\). Use the complete half-line probability at physical time \(t\); let \(a=E_tU\), \(\Delta=U-U'\), and \(E_*\) denote weighting two independent copies by \((U+U')/(2a)\). Set \(m_n=E_*\Delta^n\), \(w=m_2\), \(j(x)=E_*\cos(x\Delta)\). The [current theorem](../manuscript/current.tex) gives \(j'/j\) as the velocity at each labelled zero and \(w=\dot a/a\). Its physical sign agrees with the simple-zero formula \(H_{xx}/H_x\) in D. H. J. Polymath, §3 (31)–(32), for the source and cosine in §1 (3)–(4). [Primary source](https://arxiv.org/html/1904.12438v2#S3).

With \(h=\log j\), the opening [frontier identity](../manuscript/frontier.tex) averages \(h''+w\) on \([u,v]\). Integration in space gives the exact common divided difference
\[
 G(t)=\partial_t\log(ag)=\frac{1}{g}\left[\frac{N(v)}{j(v)}-\frac{N(u)}{j(u)}\right],
 \qquad N(x)= j'(x)+wxj(x).
\]
Thus the leading residual is the same signed fourth cumulant that appears in the curvature method. The spatial sixth derivative of the logarithm can be eliminated entirely by taking the difference at the endpoints *after* the linear cancellation. For \(k=1,2,3\), put
\[
 c_k=(-1)^k\left(\frac{w m_{2k}}{(2k)!}-\frac{m_{2k+2}}{(2k+1)!}\right),\qquad
 Q=\frac{m_{10}}{9!}+\frac{w m_8}{8!}.
\]
Expand the sine in \(j'\) through degree seven and the cosine in \(wxj\) through degree six. Real Taylor remainders through degrees eight and seven respectively give
\[
  |N(x)-\textstyle\sum_{k=1}^3 c_kx^{2k+1}|\le Q|x|^9,\qquad c_1=(m_4-3w^2)/6 .
\]
If \(\beta(x)=1-wx^2/2>0\), then \(\beta(x)\le j(x)\le1\). In particular the cell enclosure sums the three signed products
\[
 c_k\,\frac{v^{2k+1}/j(v)-u^{2k+1}/j(u)}g
\]
and pays at most \(Q(v^9/\beta(v)+u^9/\beta(u))/g\) in absolute error. The remainder uses real difference moments of the full tilted source. No truncation of zero interactions is involved.

## What the 28 moments pay for

Let \(T=1000,\ b=671/500,\ P=U-b,\ s=T-t,\ M_n=E_TP^n\). Only \(M_1,\ldots,M_{28}\) require measurements besides the inherited upper pair. The [opening envelope](../manuscript/finite.tex) covers their entire half-line tails, including omitted square modes. The [anchor integrator](../../01_jacobi_integer_hierarchy/numerics/check_large_time_resummation.py) encloses the finite interval at 224 bits and adds the absolute tail to each numerator and mass. The integration tolerance itself is not used as the error bound. [FLINT integration contract](https://flintlib.org/doc/acb_calc/integrate.html).

For \(F_{s,x}(U)=e^{-s(U^2-b^2)+ixU}\), on any circle of radius \(r>0\) about a real point \(y\), its modulus is bounded by \(e^{s(b^2+r^2)+|x|r}\), since \(-s(\Re z)^2\le0\). The derivative bound of order \(n\), divided by \(n!\), is at most this quantity times \(r^{-n}\). Apply the real integral Taylor remainder on the whole segment from \(b\) to \(U\), which applies also to complex values. With \(z=-2bs+ix\), coefficients of \(e^{zP-sP^2}\) satisfy \(f_{-1}=0,f_0=1,\ nf_n=zf_{n-1}-2s f_{n-2}\). [Cauchy estimate, DLMF §1.9(iii), (1.9.31)](https://dlmf.nist.gov/1.9.E31).

In particular an enclosure for \(L_p=E_T[P^p e^{-s(U^2-b^2)}]\), \(0\le p\le11\), is
\[
 L_p=\sum_{n=0}^{27-p} f_n(s,0) M_{p+n}
   \ \pm\ M_{28}\,e^{s(b^2+r^2)}r^{-(28-p)} .
\]
Here \(p+(28-p)\) is even. This observation covers odd \(p\) without measuring an absolute odd moment. The common normalization yields \(d_p=L_p/L_0,\ d_0=1\). The mean is \(a=b+d_1\) and the variance is \(d_2-d_1^2\). The bracket \(\sum_{i=0}^p(-1)^i{p\choose i}d_i(bd_{p-i}+d_{p-i+1})/a\) equals \(m_p\) for even \(p\), by symmetrization. This is the [opening moment identity](../manuscript/finite.tex), now evaluated through \(p=10\).

For \(X=4\), the centered characteristic function stays in the disk of radius \(\epsilon=X^2\operatorname{Var}_t U/2<1\) about 1, using the real second-order exponential remainder. Its continuous argument therefore stays within \(\delta=\arcsin\epsilon\) of zero. The strict current floor makes the physical phase increasing from zero. If \(aX-\delta>3\pi/2\), the roots are simple and are exactly the levels \(q_1=\pi/2,q_2=3\pi/2\), with \(x_k\in[(q_k-\delta)/a,(q_k+\delta)/a]\). This whole-cell identification makes the signed calculation about the same pair at every time.

## Transport, direct endpoint and direct path

For \(0\le s\), write \(I(s)=\int_0^s G(T-\tau)\,d\tau\). On a union of closed cells, integrate the separate cell intervals with their exact lengths. Then
\[
 D(T-s)=D(T)\left(\frac{a(T)}{a(T-s)}\right)^2 e^{-2I(s)},\qquad
 -\partial_t\log g=w-G .
\]
Strict positivity of the latter expression gives every partial descent the common margin \(D(T-s)\ge D(T)>0\). This includes a stop inside a cell. The squared mean ratio, signed integral width, inherited root radii and exponential are all included in the endpoint enclosure.

The equally informed endpoint arm encloses the *unnormalized* field
\[
 H(T-s,x)\,/\,\big[ Z(T)e^{-sb^2}\big]
 = \Re \!\left(e^{ibx}\sum_{n=0}^{27}f_n(s,x)M_n\right)
 \ \pm\ M_{28}\,e^{s(b^2+r^2)+|x|r}/r^{28}.
\]
Opposite certified signs inside a counted level bracket fix the root, using both sides of each zero. Jointly tilted cosine evaluation spends all 28 moments. For a separate path comparison one also evaluates
\[
 \dot x_k=\frac{E_t[(U^2-b^2)\cos(x_kU)]}{E_t[U\sin(x_kU)]}
\]
on the counted tubes. Subtracting \(b^2 H\) in the numerator is exact at each zero; replacing a full field at uncertain probes by zero would be invalid. The implementation encloses this ratio at every possible actual root in its tube. A sharp direct endpoint alone would say nothing about the intervening derivative.

## Controls and classification

This is a finite estimate with independently measured premises. The exact velocity representation is shared by other positive sources. Any such source passing the actual inequalities on the given tube inherits their local conclusion. [Result index](../../../../../result-summaries/README.md) · [Collision catalogue](../../../../../result-summaries/12_collision_controls_and_screening.md) · [Patterns index](../../../../../avoid/README.md) · [Classification](../../../../../avoid/01_restating_the_target.md) · [Control premises](../../../../../avoid/02_shape_only_arguments_and_the_controls.md) · [Scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

| Control tested against the argument | Premise or strict gate |
| --- | --- |
| Pure cosine; two-atom \(H=e^t\cos x+c\) | The pure cosine gives \(w=G=0\). For the two atoms at \(ce^{-t}=1/2\), \(w=m_4=1/3\), \(u=2\pi/3,v=4\pi/3\), and \(\dot g=2/\sqrt3>0\). Even the quadratic current floor at \(X=v\) is \(1-8\pi^2/27<0\). Direct substitution tests the time orientation. |
| Shifted Euler factors; weighted-square sources; finite theta tails | These have different complete normalized weights. The anchor measurements and complete theta-tail estimate do not transfer. At a literal real double \(H=H_x=0\), both complex half-field and derivative are imaginary, hence \(J=0\) and the strict current gate fails there. |
| Reflected super-Gaussian; smooth-shape and positive-primitive controls | Their shape, reflection or primitive endpoints do not supply the complete integer-square law used to obtain these 28 quantitative enclosures. A double again violates the chart floor at its own location. |
| Finite-prime orbits, finite score or profile matches; fixed-event atomic or compact controls | Matching specified finite observations does not supply these interval and tail estimates at these times and labels. A control matching the actual measurements could obey this same local result and still collide outside its certified window. |
| RH-conditional normalized endpoint control; changed observation | The normalized perturbation lacks ordinary Dirichlet arithmetic and does not carry the theta integral's numerical enclosures. A changed observation fails the literal cosine and the identified real phase levels. |

The [opening control computation](../manuscript/frontier.tex) gives the two-atom motion explicitly. The source-specific assumptions and finite labels are essential for the interpretation.

## E03 result on the original slab

The interval certificate gives \(4.1374\,10^{-10}<G<5.2447\,10^{-10}\) and \(2.28355\,10^{-4}<-(\log g)_t<2.28658\,10^{-4}\) on all of \([999,1000]\). Thus the first gap widens backward while the first gap multiplied by the source mean contracts backward. The positive fourth cumulant lies between \(1.3972\,10^{-10}\) and \(1.7621\,10^{-10}\). The phase surplus beyond the second level exceeds 0.65160 radians and the normalized current exceeds 0.9981707 throughout the chart. [E03 interval record](../numerics/03_SIGNED_PATH_999_1000_20261120.json).

| Quantity | Outward bound or measured width |
| --- | --- |
| Integral of the degree-three divided difference | \([4.2236,5.1516]10^{-10}\) |
| Integral of the degree-five divided difference | \([-7.373,-6.330]10^{-13}\) |
| Integral of the degree-seven divided difference | \([4.519,5.209]10^{-16}\) |
| Integrated spatial remainder, absolute | \(<1.143\,10^{-16}\) |
| Full \(I(1)\) | \([4.2163,5.1453]10^{-10}\) |
| \(a(1000)/a(999)\) | \(1.00022853225375366668\ldots\), interval width \(<3.234\,10^{-49}\) |
| Transported \(D(999)\) | \(1.37162603019040<D<1.37162603044525\), internal width \(<2.549\,10^{-10}\) |
| All-28-moment direct endpoint | \(1.3716260303168938811550439987119261608841527\ldots\), width \(<4.752\,10^{-45}\) |
| Direct physical backward log drift | \(2.28084\,10^{-4}<-(\log g)_t<2.28934\,10^{-4}\) |

The common divided difference reduces the opening transport width by about 28,900-fold. The cubic coefficient enclosure accounts for essentially all of the residual integral width. Both calculations use the same 28 measured powers and source, and the direct endpoint also overlaps the opening full-quadrature holdout. A direct path check also recovers strict physical widening from those data. The normalized sign is certified by the divided difference. E03 supplies the paid basis for the [overlap decision](../brainstorm/notes/03_EZ_B03_OVERLAPPING_CHART_20261120.md).
