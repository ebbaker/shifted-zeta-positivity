# Local multipliers and obstructions from finite observations

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: `gpt-6.1-sol` (Codex); reasoning effort **ultra**.
Internal research note, not independent mathematical validation.

This develops the first theta gate of investigation 20. It gives two
precisely delimited obstructions. The first applies even on the genuine
theta Hilbert space, but requires an operator identity on a full core.
The second constructs positive smooth controls preserving any declared
finite collection of integral source observations and local source jets.
Neither excludes a construction that uses the full imaginary Jacobi law
on its actual arithmetic state.

The targets and normalization are those of the
[initial research program](INITIAL_RESEARCH_PROGRAM_20261014.md) and
[Dirac squares note](DIRAC_SQUARES_AND_STATIONARY_LAGUERRE_ENERGY_20261014.md).
The earlier controls, Volterra law, and genuine source logarithmic
derivative estimate used below are in the
[complete-channel continuation](../../02_angular_jacobi_gluing/notes/3_COMPLETE_CHANNEL_VOLTERRA_CONTROLS_20261013.md).
The lower-bound and endpoint ledger for that correction are in the
[positive-anchor continuation](../../02_angular_jacobi_gluing/notes/2_VOLTERRA_RECOVERY_POSITIVE_ANCHOR_AND_TRANSFER_GAP_20261013.md).

## 1. A declared local operator ansatz

Use the genuine even source and its usual normalization,

\[
 d\mu(u)=\tfrac12\Phi_e(u)\,du,
 \quad H_t(x)=\int e^{tu^2}e^{ixu}\,d\mu(u).
\]

The theta source is strictly positive everywhere and has all Gaussian
moments. Let

\[
 \mathcal K=L^2(\mathbb R^2,d\mu\otimes d\mu),\qquad
 W_t(u,v)=e^{t(u^2+v^2)/2}.
\]

Multiplication by `u`, `v`, `u-v`, and `u+v` is self-adjoint on its
maximal multiplication domain. Compactly supported smooth functions form
a common form core for every polynomial multiplier used below. The
physical Laguerre form is

\[
 L_0(H_t;x)=\langle W_t,K_xW_t\rangle,\qquad
 k_x(u,v)=\tfrac12(u-v)^2\cos[x(u+v)].                 \tag{1}
\]

Declare a finite first-order multiplication-square ansatz

\[
 q_{\ell,x}(u,v)
 =\alpha_{\ell,x}(u,v)(u-v)
  +\beta_{\ell,x}(u,v)(u+v)+\gamma_{\ell,x}(u,v),
 \qquad 1\le\ell\le N,                               \tag{2}
\]

with source-derived coefficients and defined form domains. The
obstruction below actually allows arbitrary nonnegative multiplication
squares, so it is independent of the chosen finite coefficient library.
For a linear stationary multiplier take

\[
 b_x(u)=u\sin(xu),\qquad
 M_{t,x}=\int e^{tu^2}m_x(u)\,d\mu(u),
\]

where `m_x` is real, locally essentially bounded and has sufficient
theta-weighted integrability. Its product with `H_t'(x)` has the
symmetrized multiplication kernel

\[
 p_x(u,v)=-\tfrac12\{b_x(u)m_x(v)+m_x(u)b_x(v)\}.
                                                               \tag{3}
\]

Thus the strongest local square completion of this class would require
the quadratic-form identity on the full compact-support core

\[
 K_x=\sum_{\ell=1}^N Q_{\ell,x}^*Q_{\ell,x}+P_x.       \tag{4}
\]

This implies the intended scalar identity on `W_t`, but is strictly
stronger than an identity only after expectation in that one state.

**Theorem 1.** For every real `x != 0` and every locally bounded `m_x`,
`K_x-P_x` has a strictly negative quadratic form on some smooth
compactly supported vector. Consequently (4) is impossible. In fact
`K_x-P_x` cannot equal any positive operator quadratic form, whether or
not that positive operator is a multiplication operator.

**Proof.** Put `a=pi/|x|`. At `(u,v)=(0,a)`, both stationary factors
`b_x(u),b_x(v)` vanish, whereas

\[
 k_x(0,a)=-a^2/2.                                    \tag{5}
\]

Choose `r_0 <= a/8` and a finite common essential bound `C` for `|m_x|`
on the two neighborhoods `[-r_0,r_0]` and `[a-r_0,a+r_0]`. Choose

\[
 0<r\le\min\{r_0,\ a/[32(1+C)|x|]\}.
\]

On the rectangle `R=[-r,r] x [a-r,a+r]`,

\[
 |u-v|\ge3a/4,\qquad \cos[x(u+v)]\le-1/2,
 \qquad k_x\le-9a^2/64<-a^2/8.
\]

Also

\[
 |b_x(u)|\le |x|r^2,\qquad
 |b_x(v)|\le(9a/8)|x|r,
 \qquad |p_x|\le2C|x|ar\le a^2/16.
\]

Therefore `k_x-p_x <= -a^2/16` almost everywhere on `R`. Since
`mu` gives positive mass to every open interval, a nonzero smooth vector
supported in the interior of `R` has strictly negative form. This
contradicts positivity in (4). No point evaluation on a null set is used.
The argument permits arbitrary theta-dependent `m_x`; boundedness near
the two nodes is the relevant hypothesis. QED.

The nodal stationary factors, rather than the cosine sign alone, are
what exclude the constrained completion. A putative escape using poles
at these nodes would require a new domain and boundary ledger and is
outside the declared class.

**Derivative-level companion.** The same operator-core obstruction
holds for `j=1` with its correct stationary equation `H_t''=0`.
Its physical multiplier is

\[
 k_{1,x}(u,v)=-\tfrac12uv(u-v)^2\cos[x(u+v)],\qquad
 c_x(u)=u^2\cos(xu),
\]

and a linear stationary product `H_t'' M` has kernel
`p_{1,x}=-(c_x(u)m_x(v)+m_x(u)c_x(v))/2`. At
`u=a=pi/(2|x|)` and `v=3a`, both `c_x` factors vanish whereas

\[
 k_{1,x}(a,3a)=-6a^4<0.                              \tag{5a}
\]

Local boundedness of `m_x` again supplies a positive-mass neighborhood
where `k_{1,x}-p_{1,x}<0`. Thus neither derivative-level target has a
positive operator identity in this local linear stationary-multiplier
class for any `x != 0`. This statement does not impose stationarity
on either individual spectral sector.

**Quantitative remainder payment.** If instead a multiplication-kernel
identity is written

\[
 k_x=\sum_\ell |q_{\ell,x}|^2+p_x+e_x,
\]

then the same rectangle forces

\[
 e_x\le-a^2/16\quad\hbox{a.e. on }R,
 \qquad
 \int (e_x)_- |W_t|^2\,d\mu^2
 \ge\frac{a^2}{16}\int_R e^{t(u^2+v^2)}\,d\mu^2>0.   \tag{6}
\]

This is a strictly positive lower bound on the negative *part* of the
remainder. It does not imply that the total integrated remainder is
negative; cancellation elsewhere is still possible. It explicitly
identifies a payment that every local completion must retain.

**Exact boundary of this no-go.** A gluing defect can vanish after
expectation in the genuine theta state while remaining a nonzero
operator on the full core. Such a defect is not eliminated from (4) by
its one-state vanishing. Nor does (4) test a nonlocal, source-restricted
identity defined only on an arithmetic constrained subspace. Those are
legitimate remaining directions, but their extra restriction must be
displayed. At `x=0`, the obstruction disappears and
`k_0=(u-v)^2/2` is already a positive multiplication square.

## 2. Exact finite-observation controls with a strict wrong stationary sign

The earlier investigation 02 controls preserve positivity and arbitrarily
close real-axis source data. The following extension preserves any
declared finite set of source observations *exactly*, and produces a
strict negative stationary margin rather than only an exact joint zero.

Fix any real time `t_0`. For an even source `psi`, write

\[
 H_{\psi,t_0}(x)=\tfrac12\int_{\mathbb R}
          e^{t_0u^2}\psi(u)e^{ixu}\,du.
\]

Declare finitely many real linear integral observations

\[
 \ell_i(\psi)=\int_{\mathbb R}K_i(u)\psi(u)\,du,
 \qquad 1\le i\le r,                                 \tag{7}
\]

where each kernel is locally integrable, and every displayed integral
exists for the base source `Phi_e` and the perturbations below. Also
declare finitely many local source jets `psi^(k)(s_j)`. A complex
observation is treated as two real observations.

**Theorem 2.** There is a sequence of positive even smooth sources
`psi_X`, with every Gaussian moment and with `psi_X/Phi_e - 1` compactly
supported, such that

\[
 \ell_i(\psi_X)=\ell_i(\Phi_e),\qquad
 \psi_X^{(k)}(s_j)=\Phi_e^{(k)}(s_j),                  \tag{8}
\]

for all the declared observations and jets. The perturbations converge
to theta in every fixed relative derivative norm. At arbitrarily large
frequencies `X`, they satisfy

\[
 H_{\psi_X,t_0}(X)=\varepsilon_X>0,
 \quad H'_{\psi_X,t_0}(X)=0,
 \quad H''_{\psi_X,t_0}(X)=\varepsilon_X>0,
 \quad L_0(H_{\psi_X,t_0};X)=-\varepsilon_X^2<0,       \tag{9}
\]

where one can take `epsilon_X=exp(-sqrt(X))`.

**Proof and explicit finite-dimensional construction.** Choose an open
symmetric bounded set `Omega` avoiding neighborhoods of every source
jet point `s_j` and its reflection. Let `V` be the even smooth functions
compactly supported in `Omega`. Restrict the observations to
`q -> ell_i(Phi_e q)` on `V`, discard linear redundancies, and select
`b_1,...,b_s` in `V` with

\[
 \ell_i(\Phi_e b_j)=\delta_{ij}                       \tag{10}
\]

for the remaining independent observations. Their existence is ordinary
finite-dimensional linear algebra on the range of these functionals.
The discarded observations are then automatically preserved as well.

Choose a nonzero nonnegative `phi` in `V`, with support containing an
interval. Put

\[
 F(x)=H_{\Phi_e\phi,t_0}(x),\qquad
 I_{2k}=\tfrac12\int e^{t_0u^2}\Phi_e(u)\phi(u)u^{2k}\,du.
\]

The positive measure in this definition has nonconstant `u^2`, so
`I_0 I_4>I_2^2` by strict Cauchy--Schwarz. Hence, for all sufficiently
small fixed `d>0`,

\[
 F'(d)=-I_2d+O(d^3)\ne0,
 \quad F(d)F''(0)-F(0)F''(d)
      =\tfrac12(I_2^2-I_0I_4)d^2+O(d^4)\ne0.          \tag{11}
\]

For `a` in `{-d,0,d}`, define the exactly observation-null carriers

\[
 q_{a,X}(u)=\phi(u)\cos((X+a)u)
   -\sum_{i=1}^s \ell_i(\Phi_e\phi\cos((X+a)\cdot))\,b_i(u).
                                                               \tag{12}
\]

The observation coefficients tend to zero by the Riemann--Lebesgue
lemma: their integrands `K_i Phi_e phi` are integrable on the common
compact support. The jet constraints hold exactly because all these
functions vanish near the declared nodes.

Let `R_X` be the three-by-three response matrix whose `a` column is

\[
 (H_{\Phi_e q_{a,X},t_0}(X),
  H'_{\Phi_e q_{a,X},t_0}(X),
  H''_{\Phi_e q_{a,X},t_0}(X))^T.
\]

All Fourier transforms of `Phi_e b_i e^{t_0u^2}` and
`Phi_e phi e^{t_0u^2}` are Schwartz. The cosine product identity gives
the invertible limit

\[
 R_X\longrightarrow\frac12
 \begin{pmatrix}
  F(d)&F(0)&F(d)\\
  F'(d)&0&-F'(d)\\
  F''(d)&F''(0)&F''(d)
 \end{pmatrix}.                                     \tag{13}
\]

Its determinant is nonzero by (11). Therefore, for all sufficiently
large `X`, solve the *explicit* three-by-three linear system

\[
 c_X=R_X^{-1}\left[
  (\varepsilon_X,0,\varepsilon_X)^T
  -(H_{\Phi_e,t_0}(X),H'_{\Phi_e,t_0}(X),
                        H''_{\Phi_e,t_0}(X))^T\right],
 \quad
 \psi_X=\Phi_e\left(1+\sum_a(c_X)_a q_{a,X}\right).    \tag{14}
\]

The genuine source's heated transform and fixed derivatives are
Schwartz, and the inverse matrices in (14) are uniformly bounded.
Thus `c_X=O_N(X^-N)` for every fixed `N`. The functions `q_{a,X}` are
uniformly bounded and their fixed-order derivatives grow only
polynomially in `X`. It follows that the relative perturbation and
each fixed derivative tend to zero superalgebraically. For large `X`,
its absolute supremum is less than `1/2`, giving `psi_X>0`. Outside
the common compact support `psi_X` equals theta exactly, so all heat
moments and tail properties are retained. Equations (8)--(9) follow
directly from (10), (12), and the solved response system. QED.

Since `H''` is nonzero in (9), the stationary point continues locally
in heat time by the implicit-function theorem, and its strict wrong
sign persists on some open time interval. This proof supplies neither
an effective frequency threshold nor an effective time radius.

**The scalar positive correction survives as well.** If `t_0` is chosen
in `[0,1]`, these controls retain the positive Volterra correction from
investigation 02 on that entire time interval. Indeed its genuine
source estimate is

\[
 \Phi'(u)/\Phi(u)\le13-4\pi e^{4u},\qquad u\ge0.
\]

The relative perturbation and its first derivative tend uniformly to
zero. For large `X`, writing `psi_X=Phi_e(1+q_X)`,
`|q_X'/(1+q_X)|<=1`, hence

\[
 \psi_X'/\psi_X\le14-4\pi e^{4u}<9-4tu
 \quad(0\le t\le1),                                  \tag{15}
\]

because `4u<=e^(4u)-1` makes the gap at least
`(4pi-1)e^(4u)-4>0`. For

\[
 R_\psi(u)=4\pi e^{-5u}\int_u^\infty e^v\psi(v)\,dv,
 \qquad r_{\psi,t}=e^{tu^2}R_\psi,
\]

the exact identity

\[
 r_{\psi,t}''=e^{tu^2}\left(
 [(2tu-5)^2+2t]R_\psi+
 4\pi e^{-4u}[(9-4tu)\psi-\psi']\right)>0             \tag{16}
\]

then yields

\[
 P_{\psi,t}(x)=x^{-2}\int_0^\infty
       r_{\psi,t}''(u)(1-\cos(xu))\,du>0\quad(x\ne0),
\]

with positivity at zero immediate. The rapid theta tails pay all
boundary terms. Thus the exact finite-observation controls also retain
the complete scalar Volterra law, its positive source, decreasing and
strictly convex heated correction source, and positive Fourier
correction. Their failure remains at the physical stationary product,
not at that auxiliary scalar sign.

**A strict `j=1` control, or both signs in the same source.** The
construction also prescribes derivative jets `(H',H'',H''')` at a
remote frequency. Use offsets `a=0,d,2d` in (12). The limiting response
matrix is

\[
 \frac12\begin{pmatrix}
 0&-F'(d)&-F'(2d)\\
 F''(0)&F''(d)&F''(2d)\\
 0&-F'''(d)&-F'''(2d)
 \end{pmatrix}.                                     \tag{17}
\]

It is invertible for sufficiently small `d>0`, since `F''(0)=-I_2<0`
and

\[
 F'(d)F'''(2d)-F'(2d)F'''(d)
    =(I_2I_6-I_4^2)d^4+O(d^6)>0.                    \tag{18}
\]

Strict Cauchy--Schwarz gives `I_2I_6>I_4^2` for the same interval
support. Solve this response system with target
`(epsilon_X,0,epsilon_X)`. Then exactly

\[
 H'(X)=\varepsilon_X>0,\quad H''(X)=0,\quad
 H'''(X)=\varepsilon_X>0,\quad L_1(H;X)=-\varepsilon_X^2<0.
                                                               \tag{19}
\]

One may impose (9) at `X` and (19) at `2X` on the *same* positive
source. Use six projected carriers, three centered near each remote
frequency, and stack the six derivative observations. The limiting
six-by-six response matrix is block diagonal with blocks (13) and
(17): all cross-block Fourier observations tend to zero because their
frequency separations tend to infinity. It is consequently invertible
for large `X`, and the same coefficient decay, positivity, exact finite
measurement preservation, and correction-positivity arguments apply.
Both stationary points are nondegenerate and persist locally in time.
No effective frequency or time threshold is claimed.

**Analytic-source variant.** If each observation in (7) is absolutely
integrable against `Phi_e`, the construction can retain real analyticity
of the source, at the cost of replacing exact equality to theta outside
a compact set by a common theta tail majorant. Choose
`phi(u)=exp(-u^2) Z(u)^2`, where `Z` is an even polynomial with sufficiently
high-order zeros at every declared jet node and its reflection. Use the
space spanned by `phi(u) cos(omega u)` for real `omega` in place of `V`.
Every member is bounded, even, real analytic, and vanishes to the needed
jet orders. Choose the observation basis `b_i` from that same space.
All carrier integrands are absolutely integrable because their bounded
envelopes multiply `K_i Phi_e`; Riemann--Lebesgue, the two moment
determinants, and the exact response systems apply unchanged. For large
`X`, the relative perturbation is again bounded by `1/2`, so
`Phi_e/2 <= psi_X <= 3Phi_e/2`; all Gaussian moments and the positive
Volterra correction survive. This excludes using real analyticity alone
to repair the finite-observation inference. It still supplies no full
imaginary Jacobi lift.

## 3. Consequence for a finite constrained-square program

An identity or estimate valid for every positive source satisfying only
the finite observations (7)--(8), with zero displayed defects and
nonnegative total remaining payment on the stationary locus, is refuted
by (9). The extension is stronger than closeness of finitely many
measurements: the measurements are exactly unchanged.

This applies to a finite angular or gluing test only after its
source-to-lift map and evaluated defect have been shown to be a linear
observation of the stated integral/jet type. No such representation is
silently assumed. A finite nonlinear constraint, a finite coefficient
ansatz that already restricts the whole source class, or a test of an
analytic identity on an open interval may fall outside this theorem.

Most importantly, the full imaginary Jacobi law is an infinite
arithmetic constraint. These sources are not asserted to obey it.
Its integer coefficient recurrence `c_n=c_{n+1}` and the complete
transported insertion remain possible sources of a genuine
source-specific domination theorem. The two results here identify
what must change: a local multiplication identity on the full paired
core is impossible, and finitely many source observations do not
replace full arithmetic gluing over an unrestricted smooth source
class. A successful construction must visibly use a restricted state
space or a nonlocal gluing payment and must bound its total signed
remainder.

No RH consequence, complete theta stationary sign, or new global
positive factorization is claimed. All results above are proved from
the displayed formulas; no external literature claim is used.
