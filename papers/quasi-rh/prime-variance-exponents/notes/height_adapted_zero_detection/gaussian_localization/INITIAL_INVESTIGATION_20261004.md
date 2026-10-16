# Gaussian inverse tests and finite interval detection

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration. The exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel same-model analysis and internal cross-review are not independent
specialist refereeing.

Status: exact identities, analytic kernel and tail bounds, an application of
the Kolesnik--Straus theorem, and a conditional finite-box detector.
The inverse constants and local zero-count constant have not been numerically
certified. No new arithmetic saving, numerical zero certificate, or zero-free
region is proved. Broader mathematical novelty has not been established.

The first useful result is that a Gaussian inverse of the prepared scalar
has a weighted physical norm bounded uniformly in carrier height. The pole
restored by inverse division can be subtracted exactly. A finite-window
identity still has tail costs, but its unseen pole moment can be expressed
using the known total moment and a finite prefix. Linking the two Gaussian
parameters turns the zero residues into an ordinary power sum, which handles
clusters without a separation or exposed-zero hypothesis.

The [investigation index](README.md) gives the sequence of follow-up work.
The starting coefficient lemmas and inverse scout are in the parent
[detector note](../DETECTOR_LEMMAS_20261004.md) and
[assessment](../PRIORITIZED_ASSESSMENT_20261004.md). All transform signs and
normalizations below are fixed explicitly.

## The full prepared Mellin transform

Retain \(q=7/3\), \(A=e^{-1/4}\), \(C=2e^{1/4}\), the probe
\(h(v)=(1-16v^2)^8\) on \(|v|<1/4\), and the prepared family
\(g_t,w_t,\ell_t,D_t\) from the parent overview. Put

\[
S_t(x)=x\lambda_t(x)=\frac1q\sum_{n\ge2}\Lambda(n)\ell_t(n/x),
\qquad f_t(y)=S_t(e^y).
\tag{1}
\]

The shell kernel is supported in \([A,C]\), so \(f_t(y)=0\) for
\(y\le\log(2/C)=-1/4\). This is the complete physical lower cap;
the shell observable can be nonzero below \(x=1\).

For \(\Re s>1\), absolute convergence and \(u=n/x\) give exactly

\[
F_t(s):=\int_{-1/4}^{\infty}f_t(y)e^{-sy}\,dy
=-D_t(s)\frac{\zeta'}{\zeta}(s),
\qquad
D_t(s)=\frac1q\int\ell_t(u)u^{s-1}\,du.
\tag{2}
\]

The last expression equals the detector already defined in the parent:
\(D_t(s)=G_t(1/2-s)K(s-it)/q\), where
\(K(z)=(2^{z+2}-1)/(z+2)\). No asymptotic zero expansion or discarded
initial interval is used in (2).

The exact demodulation \(\ell_t(u)=u^{-it}L_t(u)\) gives a
carrier-uniform bound \(\sup|\ell_t|\le M_h\) for \(|t|\ge100\).
Using \(\Lambda(n)\le\log n\) yields an explicit finite constant
\(B_h\), depending only on the base probe, such that

\[
|f_t(y)|\le B_h e^y(1+y_+),\qquad y\ge-1/4,
\quad y_+=\max(y,0).
\tag{3}
\]

For example take \(B_h=CM_h/q\), since \(\log C<1\). An elementary
upper bound for \(M_h\) follows by bounding the polynomial derivatives
in the exact demodulated amplitude and using
\(N_t\ge |t|^3\|h\|_2\). No PNT estimate is needed for (3).

Classical PNT and integration by parts in the compact prepared prime sum
give \(\int_{-1/4}^{\infty}|\lambda_t(e^y)|\,dy<\infty\) for each
fixed carrier. Letting real \(s\downarrow1\) in (2), by dominated
convergence and the simple pole of zeta, therefore gives

\[
\boxed{\int_{-1/4}^{\infty}\lambda_t(e^y)\,dy=D_t'(1).}
\tag{4}
\]

The exact derivative is

\[
D_t'(1)=\frac{c_tK(1-it)}q
=-\frac{H(-1/2+it)K(1-it)}{2qN_t}\ne0.
\tag{5}
\]

Thus the surviving continuum coefficient is also the total physical moment
needed for pole subtraction. Equation (4) uses an established convergence
input; it is not obtained by termwise integration of the prime sum at one.

## A Gaussian centered at the real detection boundary

Fix \(1/2<b<1\), \(|t|\ge100\), \(k>0\), and \(\mu\in\mathbb R\).
Use

\[
\Phi_{b,t;k,\mu}(s)=
\exp\{k(s-b-it)^2+\mu(s-b-it)\},\qquad
g_k(v)=\frac{e^{-v^2/(4k)}}{\sqrt{4\pi k}}.
\tag{6}
\]

Centering at \(b\) aligns the physical kernel with \(y=\mu\) after
extracting the weight appropriate to a zero at real part \(b\).
For any fixed \(c>1\), define

\[
\mathcal I_{b,t}(k,\mu)=\frac1{2\pi i}\int_{\Re s=c}
-\frac{\zeta'}{\zeta}(s)\Phi_{b,t;k,\mu}(s)\,ds.
\]

The Dirichlet series and Gaussian inversion give the absolutely convergent
prime identity

\[
\boxed{\mathcal I_{b,t}(k,\mu)=
\sum_{n\ge2}\Lambda(n)n^{-b-it}g_k(\mu-\log n).}
\tag{7}
\]

This retains prime powers. It is a full Gaussian prime observable, with
infinite tails still present; truncating it would require another budget.

Let \(\mathcal Z_{b,t}(k,\mu)=\sum_\rho m_\rho\Phi_{b,t;k,\mu}(\rho)\),
over all nontrivial zeros, both ordinate signs, with multiplicities. This
sum is absolutely convergent. Shift the contour only to \(\Re s=-1\):

\[
\mathcal I_{b,t}(k,\mu)-\Phi_{b,t;k,\mu}(1)
=-\mathcal Z_{b,t}(k,\mu)+\mathcal R_{-1}(k,\mu,t).
\tag{8}
\]

The pole at one has positive sign, and zero residues have negative sign.
No trivial zeros are crossed. The exact remainder is the integral over
the fixed line \(-1\). A deliberately loose elementary bound is

\[
|\mathcal R_{-1}|
\le e^{k(1+b)^2-\mu(1+b)}
\left\{\frac{13+4\log(1+|t|)}{2\sqrt{\pi k}}
                  +\frac2{\pi k}\right\}=:E_{-1}.
\tag{9}
\]

One proof uses the functional equation at \(-1+i\xi\):
\(|\zeta'/\zeta(-1+i\xi)|\le13+4\log(1+|\xi|)\).
The cotangent factor has modulus at most one, the reflected Dirichlet
series is bounded on real part two, and the digamma series and recurrence
give \(|\psi(2-i\xi)|\le4+\log(1+|\xi|)\).
Finally \(\log(1+|t+\nu|)\le\log(1+|t|)+|\nu|\) and Gaussian
integration give (9).

An infinite Gaussian sum over trivial-zero residues is invalid: its terms
would eventually grow like \(e^{4kn^2-2n\mu}\). A Gaussian decays
vertically and grows along the far negative real axis. Keep the fixed-line
remainder, or shift across finitely many trivial zeros with a remaining
contour integral. The complete compact-probe explicit formula cannot be
integrated against this Gaussian term by term over its entire physical
range without a separate convergence argument.

## The inverse kernel and the restored pole

For a vertical line \(\sigma>1/2\), \(\sigma\ne1\), put

\[
K_\sigma(v)=\frac1{2\pi i}\int_{\Re s=\sigma}
\frac{e^{k(s-b-it)^2}}{D_t(s)}e^{sv}\,ds.
\tag{10}
\]

The inherited transform property places the zeros of \(H\) on the
imaginary axis. Inverse poles therefore lie on real part \(1/2\),
at preparation points \(0,1/2,1\), and on real part \(-2\) from the
shell factor. There are no inverse poles in \(1/2<\Re s<1\).
On moving from \(c>1\) to \(b\), exactly one pole is crossed:

\[
K_c(v)=K_b(v)+r_1e^v,
\qquad r_1=\frac{e^{k(1-b-it)^2}}{D_t'(1)}.
\tag{11}
\]

In particular the original inverse kernel has an exponential early
physical tail. Its coefficient is strongly suppressed, but global
Gaussian decay is false. The inherited off-axis lower bound for \(H\)
also gives
\(|D_t'(1)|^{-1}\ll_h(1+|t|)^{13}\).

Equations (2), (4), and (11) give the exact pole-subtracted convolution

\[
\boxed{\mathcal I_{b,t}(k,\mu)-\Phi_{b,t;k,\mu}(1)
=\int_{-1/4}^{\infty}\mathcal A_{b,t}(y)
                     q_{b,t,k}(\mu-y)\,dy,}
\tag{12}
\]

where

\[
\mathcal A_{b,t}(y)=e^{(1-b-it)y}\lambda_t(e^y),\qquad
q_{b,t,k}(v)=\frac1{2\pi}\int_{\mathbb R}
 e^{-k\nu^2}R_{b,t}(\nu)e^{i\nu v}\,d\nu,
\quad R_{b,t}(\nu)=D_t(b+i(t+\nu))^{-1}.
\tag{13}
\]

Indeed \(K_b(v)=e^{(b+it)v}q_{b,t,k}(v)\). The convergence of the
full convolution follows by comparing its late part with the \(c>1\)
kernel and the absolutely integrable moment (4). Subtracting the pole
does not justify a finite-window truncation by itself.

## A uniform weighted physical norm

**Analytic kernel lemma.** For fixed \(b\) in a compact subinterval of
\((1/2,1)\),

\[
|R_{b,t}(\nu)|+|R'_{b,t}(\nu)|
\le C_{h,b}(1+|\nu|)^{13},\qquad |t|\ge100.
\tag{14}
\]

The ninth-power inverse bound for \(H\), the first-power inverse shell
bound, and \((1+|t|)/(1+|t+\nu|)\le1+|\nu|\) prove the first part.
The lower bound for \(H\) uses its endpoint expansion at large frequency
and nonvanishing on compact frequency sets. Cauchy estimates on a small
complex neighborhood inside the inverse pole-free strip prove the derivative
bound. These constants are finite but have not been numerically evaluated.
There is no assertion of uniformity as \(b\to1/2\) or \(b\to1\).

For \(\psi(\nu)=e^{-k\nu^2}R_{b,t}(\nu)\), (14) gives
\(\|\psi\|_2\ll_{h,b}k^{-1/4}\) and
\(\|\psi'\|_2\ll_{h,b}k^{1/4}\) when \(k\ge1\).
Weighted Cauchy--Schwarz and Plancherel, optimized over the physical
weight length, yield
\(\|\check\psi\|_1\le(\|\psi\|_2\|\psi'\|_2)^{1/2}\).
Thus

\[
\boxed{M_{b,t}(k):=\|q_{b,t,k}\|_1\le C^{\rm inv}_{h,b},
\qquad k\ge1,\quad |t|\ge100.}
\tag{15}
\]

The constant is independent of the Gaussian width and the carrier.
This is stronger than a vertical inverse integral estimate: it controls
the weighted physical operator. It still does not bound an omitted tail
against a majorant growing faster than the detection weight.

## Finite physical coverage with every pole moment retained

Choose fixed \(d\in(1/2,b)\) and \(c>1\). Define the actual contour
norms

\[
P_\sigma(t,k)=\frac1{2\pi}\int_{\mathbb R}
\frac{e^{k[(\sigma-b)^2-\nu^2]}}
 {|D_t(\sigma+i(t+\nu))|}\,d\nu.
\tag{16}
\]

For \(k\ge1\), the same inverse estimates give
\(P_\sigma(t,k)\le C_{h,\sigma,b}e^{k(\sigma-b)^2}/\sqrt{k}\).
The actual integrals (16) can be used before any uniform constant is
evaluated. Let
\(J=[j_0,j_1]=[\mu-L_-,\mu+L_+]\), with
\(j_0\ge-1/4\), \(j_1\ge0\), and \(L_\pm\ge0\).
The three sufficient omitted-physical budgets are

\[
E_{\rm early}=
\frac{B_hP_d(t,k)}{1-d}(1+(j_0)_+)
                 e^{(1-b)\mu-(1-d)L_-},
\tag{17}
\]

\[
E_{\rm late}=
B_hP_c(t,k)e^{(1-b)\mu-(c-1)L_+}
\left\{\frac{1+j_1}{c-1}+\frac1{(c-1)^2}\right\},
\tag{18}
\]

\[
E_{\rm pole}=
e^{(1-b)\mu+k[(1-b)^2-t^2]}
\left\{1+\frac{B_h}{|D_t'(1)|}
                 [j_1+1/4+(j_1)_+^2/2]\right\}.
\tag{19}
\]

For (17), shift the kernel to \(d\), use
\(|K_d(v)|\le P_d e^{dv}\), and integrate (3) over the finite early
tail. If \(j_0<-1/4\), replace the early budget by zero and begin the
observed interval at the true lower cap.
For (18), use \(K_b=K_c-r_1e^v\) on the late tail; the \(K_c\) part
is integrable against (3). The remaining pole part is a signed moment:

\[
\int_{j_1}^{\infty}\lambda_t(e^y)\,dy
=D_t'(1)-\int_{-1/4}^{j_1}\lambda_t(e^y)\,dy.
\tag{20}
\]

Its modulus is bounded using the known total and (3) on the finite prefix,
which gives (19). No quantitative global PNT norm constant enters this
budget. PNT is still needed to justify the total identity (4).

Combining (8), (12), and (15)--(19) gives the exact detection interface

\[
|\mathcal Z_{b,t}(k,\mu)|
\le M_{b,t}(k)\sup_{y\in J}e^{(1-b)y}|\lambda_t(e^y)|
     +E_{-1}+E_{\rm early}+E_{\rm late}+E_{\rm pole}.
\tag{21}
\]

This keeps the physical lower cap, restored pole, continuum moment, and
fixed-line gamma remainder. It uses a continuous prime-scale interval,
not samples of \(\lambda_t\).

## A zero-side power sum with linked Gaussian parameters

An isolated large coefficient does not prevent phase cancellation, even
after Gaussian localization. Two formal zeros at \(b+\xi+i(t\pm\nu)\)
give exactly

\[
2e^{k(\xi^2-\nu^2)+\mu\xi}
             \cos\{\nu(\mu+2k\xi)\}.
\tag{22}
\]

Choosing \(\nu=\pi/[2(\mu+2k\xi)]\) makes this zero. For
\(\mu\asymp k\gg1\), those points lie much closer to the carrier than
the Gaussian width \(k^{-1/2}\). Gaussian concentration is not a phase
sector argument. The diagnostic is a formal positive-multiplicity
configuration, not a statement about actual zeta zeros.

Instead link \(\mu=a k\) and sample \(k=h\ell\) at consecutive integers
\(\ell\). Then every residue is an ordinary power of
\(z_\rho=\exp\{h[(\rho-b-it)^2+a(\rho-b-it)]\}\).
Repeat the bases according to multiplicity. The Kolesnik--Straus theorem
applies without arbitrary coefficient weights.
The exact theorem is recorded in
[Thorner--Zaman, Theorem 5.2](https://msp.org/ant/2017/11-5/ant-v11-n5-p04-p.pdf);
we use its weaker version without the prefactor 1.007. This is an
application of an established power-sum theorem.

Assume a valid unit-height count, with multiplicities,

\[
\#\{\rho:v<\gamma\le v+1\}\le C_0\log(2+|v|)
\quad(v\in\mathbb R).
\tag{23}
\]

This hypothesis is available with a sufficiently large effective constant;
no numerical \(C_0\) is selected here. Let a hypothetical zero be
\(\rho_*=\beta_*+it\), with \(\beta_*\ge b\). Write
\(\xi_*=\beta_*-b\ge0\). Choose \(a\ge2b\),
\(0<\delta\le b\), and guard radius \(R>0\). The finite cluster
\(\beta>\beta_*-\delta\), \(|\gamma-t|\le R\) contains the reference
zero and has total multiplicity at most

\[
Q_R=C_0(\lceil2R\rceil+1)\log A_R,
\qquad A_R=3+|t|+R.
\tag{24}
\]

Use half-open unit intervals that contain the closed guard interval;
the additional interval in (24) covers boundary ordinates.
Let \(F_a(x)=x^2+ax\). On \([-b,1-b]\) it is increasing.
The nearby left zeros lose at least

\[
H=\delta(a-\delta),
\qquad
F_a(\xi_*)-F_a(\xi_*-\delta)\ge H.
\tag{25}
\]

The guard pays for every remote zero having real part as large as one:

\[
G=R^2-(1-b)^2-a(1-b).
\tag{26}
\]

For \(G>0\), their total modulus relative to
\(e^{kF_a(\xi_*)}\) is at most

\[
Q_Re^{-kH}+2C_0B_R(k)e^{-kG},\qquad
B_R(k)=\frac{\log A_R}{1-q_R}
          +\frac{q_R}{A_R(1-q_R)^2},\quad
q_R=e^{-k(2R+1)}.
\tag{27}
\]

To verify the remote part, split both rays into unit bins, use
\((R+j)^2\ge R^2+(2R+1)j\) for integer \(j\ge0\), and
\(\log(A_R+j)\le\log A_R+j/A_R\). The two-ray factor is two.
No zero separation or regional rightmost-zero input is used; (26) pays
for that absence.

If the cluster has total multiplicity \(n\), its largest power-sum base
has modulus at least the reference base. For any integer \(m\ge1\),
some \(m<\ell\le m+n\) therefore has cluster response at least

\[
e^{kF_a(\xi_*)}
       \left(\frac n{4e(m+n)}\right)^n,
\qquad k=h\ell.
\tag{28}
\]

Choosing a maximal base avoids assuming that the reference zero is
rightmost. Total multiplicity, rather than the number of distinct points,
is charged in this conservative application.

## An explicit initial parameter choice

The following choice is illustrative and deliberately conservative:

\[
b=3/4,\quad a=20,\quad\delta=1/16,\quad R=3,\quad h=4.
\tag{29}
\]

Then \(H=319/256\), \(G=63/16\), and \(A_R=6+|t|\).
Choose an integer \(N\ge\max(1,7C_0\log(6+|t|))\), put \(m=N\),
and set \(\eta_N=(8e)^{-N}\). The cluster loss in (28) is at least
\(\eta_N\): the logarithm of that loss decreases with \(n\le N\).
For the possible samples

\[
k=4(N+1),4(N+2),\ldots,8N,\qquad\mu=20k,
\tag{30}
\]

we have \(q_R\le e^{-56}<1/2\), \(B_R(k)\le3\log A_R\), and
\(2C_0B_R(k)\le Q_R\le N\). The omitted-zero loss divided by the
reference response is therefore at most

\[
N(e^{-k_{\min}H}+e^{-k_{\min}G})
\le2N e^{-(319/64)(N+1)}<\eta_N/8.
\tag{31}
\]

The strict inequality is elementary for every integer \(N\ge1\): use
\(\log(8e)<4\), \(319/64>4.5\),
\(Ne^{-N/2}\le2/e<1\), and \(2e^{-4.5}<1/8\).
Consequently the existence of the reference zero forces, at some sample,

\[
\boxed{|\mathcal Z_{b,t}(k,20k)|\ge\eta_N/2.}
\tag{32}
\]

This is a zero-side theorem using the stated count hypothesis and an
existing power-sum theorem. It permits multiplicities and arbitrarily
close zeros. It does not use an exposed-zero replacement.

For an initial physical budget choose \(d=5/8\), \(c=5/4\),
\(L_-=16k\), \(L_+=26k\). Then
\(J_k=[4k,46k]\), and (16)--(19) give, up to fixed probe constants
and factors polynomial in \(k\),

\[
E_{\rm early}\ll k^{1/2}e^{-63k/64},\qquad
E_{\rm late}\ll k^{1/2}e^{-5k/4},
\tag{33}
\]

\[
E_{\rm pole}\ll_h
e^{-k[t^2-81/16]}\{1+(1+|t|)^{13}(1+k)^2\},
\quad E_{-1}\ll\log(2+|t|)e^{-511k/16}/\sqrt{k}.
\tag{34}
\]

Both early and late exponents beat the loss \(\log(8e)N\) when
\(k\ge4(N+1)\). With the least admissible \(N\), these errors become
smaller than \(\eta_N/4\) for all sufficiently large carrier heights.
The starting height and inverse constants are unevaluated. Equations
(33)--(34) establish compatibility in asymptotic scale, not an explicit
finite-height certificate or a practically affordable prime computation.
The continuous interval needed for all samples can be covered by

\[
J_*=[16(N+1),368N].
\tag{35}
\]

Its corresponding prime scales are \(X=e^y\). Since \(N=O(\log|t|)\),
the scales are polynomial in carrier height, with potentially very large
exponents. These conservative numbers are an opening feasibility check,
not recommended numerical targets.

The same sample schedule, threshold, and upper error exponents apply for
each fixed \(3/4\le b<1\), keeping the other parameters in (29).
The left gap \(H\) is unchanged and the remote gap \(G\) increases.
The physical exponents before substitution are
\(20(1-b)+(b-5/8)^2-6\) and
\(20(1-b)+(5/4-b)^2-13/2\), both decreasing in this range.
The pole and fixed-line remainder exponents likewise decrease. The inverse
norm constants still depend on \(b\), so uniformity as \(b\to1\) is not
claimed. The fixed schedule has not been established here for \(b<3/4\).

## Conditional finite box exclusion

For fixed \(3/4\le b<1\) and a candidate box
\(b\le\beta\le1\), \(|\gamma-t_0|\le\Delta\),
allow every carrier \(t\in[t_0-\Delta,t_0+\Delta]\), all with
\(|t|\ge100\). Choose one integer \(N\) satisfying (24) uniformly
over this carrier interval. Use the samples (30) and their physical
intervals \(J_k\), or the covering interval (35).

Suppose the complete prepared arithmetic observable satisfies

\[
\sup_{y\in J_k}e^{(1-b)y}|\lambda_t(e^y)|\le\varepsilon
\tag{36}
\]

for every covered carrier and sample. If, throughout those parameters,

\[
C^{\rm inv}_{h,b}\varepsilon+
E_{-1}+E_{\rm early}+E_{\rm late}+E_{\rm pole}<\eta_N/2,
\tag{37}
\]

the candidate box contains no zero. Indeed, any such zero supplies its
own exact carrier \(t=\gamma_*\), (32) applies, and (21) contradicts it.
No replacement zero leaves the covered carrier band. The zero-side guard
radius three is an analytic allowance, not an enlargement of the
arithmetic carrier hypothesis beyond the candidate box.

This is a conditional analytic detector. It specifies a finite continuous
prime-scale interval, a full carrier coverage requirement, cluster loss,
and all listed remainders. A numerical implementation still needs a
certified \(C_0\), evaluated inverse constants, and enclosures for (37).
The independent arithmetic hypothesis (36) has not been proved, and may
remain very demanding. It must eventually be compared against the current
classical zero-free inputs before any new-exclusion claim.

## Next research gates and verification

The immediate next work is to evaluate (14)--(16) rigorously and reduce
the coarse widths in (35). An elementary opening fact is
\(\int v^2h/\int h=1/304\), hence
\(H(i\nu)\ge H(0)(1-\nu^2/608)\ge H(0)/19\) for \(|\nu|\le24\).
A central-frequency saddle contour could give a Gaussian core while
separately charging shell poles and remote connectors. That sharper
construction remains proposed; global Gaussian decay must not be assumed.

Then extend the full signed arithmetic reduction over the actual intervals
and carrier family of (36). Retain its continuum, endpoints, and prime
powers. A better kernel changes detection cost; it does not itself
establish the missing arithmetic cancellation.

The linked [diagnostics](../../../numerics/height_adapted_zero_detection/gaussian_localization/README.md)
check exact rational parameters, a formal cancellation example, the ray
power identity, and floating parameter losses. The proof of (31) is
analytic for all integers \(N\ge1\); the numerical sample does not prove
it. No actual zeta zero set or inverse integral is certified numerically.
The [internal review](../../../reviews/height_adapted_zero_detection/gaussian_localization/INITIAL_REVIEW_20261004.md)
records the checks and restrictions.
