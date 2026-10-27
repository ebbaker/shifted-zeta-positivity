# Narrow small-time canonical seeds and the improved witness envelope

27 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**.

**Status: proved in-note from the unchanged canonical coefficients and
the published approximation input in [Note02][budget], with separate
same-model internal review.** This completes the narrower-seed bounded
task proposed in [Note03][old]. It improves the supplied witness upper
envelope from exp exp(C_d tau^{-3}) to exp exp(C_d/sqrt(tau)).
The fixed published constants K_1,y_0(1) remain uninstantiated. No
numerical first-zero bound, lower escape rate or regime exclusion follows.

Read the [result index][results], [avoid index][avoid], [control cluster][controls],
[classification rule][classify], [scope rule][scope], [coupled-cost rule][coupled]
and [quantitative-gain rule][gain]. The [review][review],
[chat summary][summary] and [sole register][progress] record the scope.
The result is an improved upper allowance, not a claim of literature
priority or a new proof of known negative-time nonreal-zero existence.

## 1. Actual seed family and main bound

Let h=sqrt(tau), tau_0=2^{-30}, A=32, T=8A=256, and define

\[
 G_\tau(s)=hZ_\tau(1+hs),\qquad
 I(s)=\int_0^\infty e^{-v^2/4-sv}\,dv.
 \tag{N1}
\]

This rescales the same canonical Dirichlet series used in Note02.
Set the following constants, all independent of tau:

\[
 M=\log5+64A^2,\quad
 N=\left\lceil M/\log(8/5)\right\rceil,\quad
 \delta_0=e^{-6M-N\log(16e)},\qquad
 r_j=2A+jA/N\quad(0\le j\le N).
 \tag{N2}
\]

For every 0<tau<=tau_0 at least one disk |s|<=r_j has a zero-free
boundary with |G_tau|>=delta_0 there, and between 1 and N zeros inside,
counted with multiplicity. Therefore at least one actual seed disk

\[
 D_{\tau,j}=\{|w-1|\le hr_j\}
 \tag{N3}
\]

has positive count bounded by N and full boundary floor
delta=delta_0/h. Its common coordinate and scalar envelopes are

\[
 \alpha=1-3Ah\le\Re w\le1+3Ah=:B,
 \quad |\Im w|\le3Ah,\quad
 Z_\tau(\alpha)\le W=C_w/h,\qquad C_w=5e^{9A^2}.
 \tag{N4}
\]

The proof guarantees a good member of a specified finite family; it does
not compute its index or exact zero count. All transport payments below
use the common envelopes N4 and require no such identification.

For every fixed d>0, the canonical H(-tau,.) consequently has a zero
z_tau with |Im z_tau|>=2d and

\[
 R_*(\tau)\le |z_\tau|
 \le\exp\exp(C_d/\sqrt\tau),\qquad 0<\tau\le1.
 \tag{N5}
\]

Here C_d depends only on d, the displayed absolute constants and the
fixed imported K_1,y_0(1). The narrower seeds are proved on (0,tau_0];
Note03 supplies the compact remaining time interval after increasing
C_d. Section5 gives the complete unsimplified new bound. All zeros and
R_* use complex radius; a constructed upper witness is no lower exclusion.

## 2. Uniform sum-to-integral comparison, including derivatives

For k=0,1,2,3 put

\[
 F_{s,k}(x)=(-h\log x)^k
     x^{-1-hs}e^{-h^2\log^2x/4}\quad(x\ge1).
\]

Normal convergence permits differentiation of the series and integral.
Aligning the intervals [n,n+1] gives

\[
 \left|\sum_{n\ge1}F_{s,k}(n)
                -\int_1^\infty F_{s,k}(x)\,dx\right|
 \le\int_1^\infty |F_{s,k}'(x)|\,dx.
 \tag{N6}
\]

There is no omitted n=1 endpoint: it belongs to the first interval.
Set b=1/h, a=b-T and
q_k(v)=(-v)^k exp[-v^2/4-sv-bv]. The change v=h log x turns the
right side, after multiplication by h, into h integral |q_k'|.
For |s|<=T and Th<=1/2, one has a>=b/2>0. Differentiating q_k,
dropping its Gaussian factor, and integrating powers of v gives

\[
 |G_\tau^{(k)}(s)-I^{(k)}(s)|
 \le h k!a^{-k}\left\{\mathbf1_{k\ge1}
            +\frac{k+1}{2a^2}+\frac{b+T}{a}\right\}.
 \tag{N7}
\]

Since (b+T)/a<=3 and 1/(2a^2)<=2h^2, for h<=1 this yields

\[
 |G_\tau-I|\le5h,\qquad
 |G_\tau^{(k)}-I^{(k)}|
       \le12k!2^k h^{k+1}\quad(1\le k\le3).
 \tag{N8}
\]

On tau<=2^{-30}, Th<=2^{-7}<1/2 and the four allowances are at most
5*2^{-15}, 24*2^{-30}, 96*2^{-45}, 576*2^{-60}, all strictly below
epsilon=2^{-12}. This comparison controls the complete canonical sum;
no finite coefficient truncation or special-function zero is imported.

## 3. Constant scaled zero radius, count and complete wall

Direct Gaussian integration gives

\[
 (I,I',I'',I''')(0)=(\sqrt\pi,-2,2\sqrt\pi,-8),\qquad
 |(\log I)'''(0)|=(16-4\pi)/\pi^{3/2}>4/7.
 \tag{N9}
\]

For the last bound, 3<pi<22/7 implies pi^{3/2}<6 and 16-4pi>24/7.
These elementary rational bounds require no numerical evaluation.
Both G_tau(0) and I(0) exceed 1, since G_tau(0)>=sqrt(pi)-5h>1.
In the identity

\[
 (\log f)'''=f'''/f-3f''f'/f^2+2(f')^3/f^3,
\]

the respective perturbations from I to G_tau are at most
9 epsilon, 69 epsilon and 86 epsilon. For example |G_tau'|<3,
|I''|<4 and |I'''|=8, and differences of reciprocal powers on
[1,infinity) have Lipschitz constants1,2,3. Expanding each product gives
9=1+8, 69=3(3+4+2*8), 86=2(19+3*8). Thus

\[
 |(\log G_\tau)'''(0)|>4/7-164\,2^{-12}>1/2.
 \tag{N10}
\]

Completing the square in the integral gives |I(s)|<4 exp(|s|^2).
N8 therefore supplies |G_tau(s)|<=5 exp(|s|^2) on |s|<=T.
If G_tau were zero-free in |s|<A, its analytic logarithm and the
positive-harmonic Fourier-coefficient bound used in Note03 would give

\[
 |(\log G_\tau)'''(0)|
 \le12(\log5+A^2)/A^3<1/2
 \tag{N11}
\]

(use log5<2 and A=32). This contradicts N10, proving a zero inside A.

For completeness, the entire finite-circle floor is acquired as follows.
Growth on 8A and G_tau(0)>1 let Jensen bound the count through5A by N;
approaching outer zero-free radii handles any zero on radius8A.
Choose ell in[4A,5A] avoiding all zero moduli, remove its m<=N zeros
with the disk Blaschke product B_ell, and write g=G_tau/B_ell.
On the outer boundary |B_ell|=1; hence |g|<=e^M and log|g(0)|>=0.
Harnack for M-log|g|, with ratio at most7, gives log|g|>=-6M on3A.

For its zero moduli put p(u)=product_l(u-|a_l|/A). The auxiliary
polynomial p_tilde(u)=p(u)(u-2)^{N-m} is monic of degree N and has
|p_tilde|<=|p| on[2,3]. Its N-th forward difference at the grid2+j/N
is exactly N!/N^N. The absolute binomial weights sum to2^N, so at one
grid point |p_tilde|>=N!/(2^N N^N)>=(2e)^{-N}. On the entire
corresponding circle every Blaschke factor is at least
|u-|a_l|/A|/8. Thus |B_ell|>=(16e)^{-N}; multiplying by the g floor
gives delta_0. Each candidate disk contains the zero inside A. This
proves N2-N3, with every zero and every boundary point accounted for.
The same growth bound at s=-3A gives C_w in N4.

## 4. Sharper full tail and recurrence, using the new seed scale

The old n^{-2} shortcut in Note03 would lose the new gain, since
2-alpha is near1. Instead set the fixed constant

\[
 L=1+24A+\sqrt{8\log(48/\delta_0)},\qquad
 Q=\lceil e^{L/h}\rceil.
 \tag{N12}
\]

Here Q is a coefficient cutoff, distinct from the fixed zero-count N.
The positive summand e^{-tau log^2x/4}x^{-alpha} decreases beyond Q:
tau log Q/2+alpha>=1+h(L/2-3A)>0. Therefore

\[
 T_Q\le\frac1h\int_{h\log Q}^\infty e^{-v^2/4+3Av}\,dv
 \le\frac1h\frac4L e^{-L^2/8}<\frac{\delta_0}{12h}=\delta/12.
 \tag{N13}
\]

Both steps are paid: v>=L>24A gives an exponent at most -v^2/8,
and L>sqrt(8 log(48/delta_0)), L>1 pays the Gaussian tail.
For the finite prime-factor weighted sum use

\[
 \overline S=\frac{\log Q}{\log2}\frac{C_w}{h},\qquad
 \vartheta=\min\left(1,\frac{\delta_0\log2}{6C_w\log Q}\right)
 \ge c_\vartheta h>0,
\]
\[
 c_\vartheta=\min\left(1,\frac{\delta_0\log2}{6C_w(L+1)}\right).
 \tag{N14}
\]

We used log Q<=(L+1)/h and h<=1. Prime phase distances below vartheta
give a translation error <delta/3 by Note02 B6: the finite cost is at
most vartheta overline S<=delta/6 and the full tail costs 2T_Q<delta/6.
Define exactly as in the proved recurrence construction

\[
 m=\pi(Q),\quad P=\prod_{p\le Q}p,\quad
 T_r=64(m+1)/\vartheta^2,\quad k=\lceil T_r\log T_r\rceil,
\]
\[
 A_k=\binom{2k}{k}/4^k,\qquad L_{\rm rec}=8P^k/A_k^m.
 \tag{N15}
\]

The positive Fourier polynomial proof and nonzero-frequency floor
P^{-k} in Note02 apply unchanged. All costs now satisfy

\[
 \log Q=O(h^{-1}),\quad \log k=O(h^{-1}),\quad
 \log P\le Q\log Q\le e^{O(h^{-1})},\quad
 \log L_{\rm rec}\le e^{O(h^{-1})}.
 \tag{N16}
\]

For the last bound retain k log P and m log(2k+1); both fit the
displayed allowance since theta>=c_theta h. This is the complete
recurrence upper bound, not an assertion of optimal return heights.

## 5. Approximation, map, final radius and interval extension

For fixed d>0 use the same published K_1,y_0(1) as in Note03, and put

\[
 Y=1+\max\{2\pi,y_0(1),B^4,\tau/2,
 (6K_1C_w/\delta_0)^5,
 [20\tau\log_+(6K_1h/\delta_0)]^{3/2},
 2\pi e^{4(1/2+d-\alpha)/\tau}\},
\]
\[
 U=Y+6Ah+L_{\rm rec}.
 \tag{N17}
\]

Keep log_+: the raw seed floor delta_0/h need not be below1.
Choose a good phase shift in[Y+3Ah,Y+3Ah+L_rec]. The full translated
disk lies at heights[Y,U], |Re w|<=B, and meets the published real-strip
and lower-height domains. The normalized approximation costs <delta/3,
while translation costs <delta/3. Rouche transfers the positive count
to xi_{-tau}(J(w))/gamma_{-tau}(w). The gamma factor has no zero or pole
there, and J is injective on the convex high region by |J'-1|<=1/2.
Apply J before rotating: z=-i(2J(w)-1). The actual zero has Im z<=-2d
and the completely paid radius allowance is

\[
 R_*(\tau)\le F_\tau:=\left\{
 (2U+\tau\pi/2)^2+
 [1+2B+(\tau/2)\log(\sqrt{B^2+U^2}/(2\pi))]^2
 \right\}^{1/2}.
 \tag{N18}
\]

Here B stays bounded and F_tau=O(U). If 0<d<=1/4, alpha>3/4 on the
declared small-time interval, so the map gate in N17 is at most2pi and
Y has an h-independent upper bound. For arbitrary fixed d>0,
log Y=O_d(h^{-2}); it is not generally O(h^{-1}). This still fits
Y<=exp exp(C_d/h), as does N16. Consequently N18 proves N5 on
0<tau<=tau_0. On tau_0<=tau<=1, Note03 supplies its earlier bound and
tau^{-3}<=tau_0^{-5/2}tau^{-1/2}. Increasing C_d once proves N5 on the
whole stated interval. This extension does not claim the narrower seeds
were acquired beyond tau_0.

The ratio W/delta=C_w/delta_0 and the bounded scaled count are essential
gains. Merely replacing the field error while retaining Note03's old
seed strip or its n^{-2} tail would not justify N16. The large guaranteed
translation height can still send the mapped contour out of any fixed
transverse Book strip; N18 is a complex-radius witness result.

## 6. Control screen and bounded next task

The analytical screen in [Note03 Section7][old] applies with the new
premises explicit. The canonical n^{-w} population and Gaussian damping
give N6-N8. Hermite/quadratic, atomic, reflected/shape/primitive and
finite-tail sources do not supply that ordinary series. Theta-close,
finite-prime and finite-profile controls do not preserve its complete
coefficients. Euler-factor controls change the coefficients/completion;
ones satisfying analogous scaled estimates can also have these
negative-time witnesses despite positive thresholds. Weighted-square
and finite-tail controls lack the all-real interval for an RH population
interpretation, which is unused here. The all-multiple coarse-count
control passes coarse response/wall information and is not excluded by
this existence estimate. None of these missing identities is treated as
an acquired favorable simplicity inequality.

All three canonical regimes remain compatible. In C, inherited compact
escape now has the smaller upper envelope N5. A and B still have compact
witnesses near zero. No lower escape or first-zero statement, positive-T
contradiction, population theorem, physical covariance closure or
numerical certificate is supplied. Constants remain very conservative;
there has been no research numerical execution.

**Next bounded Dobner task:** improve the actual phase recurrence payment
or select and certify one member of this constant scaled seed family on
a declared interval while instantiating the published field constants.
Compare the complete U and mapped domain with N17-N18; a smaller field
term alone is not the next location gain. The [chat summary][summary]
records all results and the separate response-branch ownership.

[budget]: 02_DOBNER_COMPLETE_CONDITIONAL_BUDGET_20261026.md
[old]: 03_SMALL_TIME_CANONICAL_SEEDS_AND_WITNESS_ENVELOPE_20261026.md
[summary]: 06_CHAT0001_RESEARCH_SUMMARY_20261027.md
[review]: ../reviews/03_NARROW_SMALL_TIME_DOBNER_REVIEW_20261027.md
[progress]: ../research-progress/01_THREE_REGIME_DYNAMICS_RESEARCH_PROGRESS_20261026.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[classify]: ../../../../avoid/01_restating_the_target.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[coupled]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[gain]: ../../../../avoid/20_volume_without_a_gain.md
