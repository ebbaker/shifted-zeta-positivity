# All-window mechanism audit: a growing negative block and the termination quantifier

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort are not exposed and are not inferred. This is a separate-agent same-model mathematical audit, not independent specialist refereeing. No larger-window numerical sweep was performed and no existing certificate was changed.

The useful new obstruction is specific: the centered reference form Gamma+J has a negative index growing at least linearly with the support length even after all three fixed source moments are imposed. Consequently a fixed-rank correction cannot make that reference nonnegative on every window. This does not obstruct the desired signed inequality E<=Gamma+J. It shows that the growing low-frequency block is part of the arithmetic problem and cannot be permanently removed by finitely many constraints or modes.

A second result separates existence from cost: the signed finite-frequency scheme is theoretically complete at each fixed window having a strict positive Weil gap. Its arbitrarily expensive eventual success would still not prove that such a gap exists for every window. The final sections state this quantifier precisely.

## 1. Existing obstructions and the scope of this one

The [CCM threshold obstruction update](../../program-meta-analysis/notes/CCM_THRESHOLD_OBSTRUCTION_UPDATE_20260928.md) already excludes a bounded two-sided endpoint comparison in its specified bare archimedean norm, even after its ground-state removal. Its divergent side is negative, so it does not exclude the one-sided upper inequality needed for Weil positivity. That physical space and normalization must not be silently replaced by the present fixed-support source space.

The [Weil-depth program](../../../shifted-zeta/weil-depth/README.md) and the present investigation already supply finite-shift reductions and expose the enormous cost of absolute-amplitude high-frequency floors. Rewriting those reductions as another fixed-window compact sandwich supplies no all-window sign theorem.

Here we use the exact identity from [the all-window strategy](../notes/ALL_WINDOW_STRATEGY_20261003.md), on the unchanged prepared mean-zero source class:

    Q=Gamma+J-E,
    J[F]=integral |Fhat(t)|²/(t²+1/4) dt/(2pi),
    E=W-W_cont=W+J.

Write A=Gamma+J and m(t)=gamma(t)+1/(t²+1/4). The negative-index result below concerns A directly, without CCM threshold normalization and without assuming anything about the sign of Q.

## 2. Three moments do not eliminate the negative reference band

At zero,

    m(0)=4-EulerGamma-pi/2-3log(2)-log(pi)<0.

Thus continuity gives an open interval of negative m. Fix a nonzero real t0 in that interval and a nonzero smooth bump chi supported in (-1/2,1/2). Define

    g_R(x)=R^(-1/2) chi(x/R) exp(i t0 x),
    F_R=(-d²/dx²+1/4) d g_R/dx.

Every F_R has exactly the three required moments zero. The mean vanishes by integration by parts; pairing the preparation operator with exp(plus/minus x/2) also vanishes by integration by parts. No approximate moment correction is used. The Fourier multiplier applied to g_R is i t(t²+1/4), nonzero at t0. After normalization, the Fourier energy concentrates at t0, and Schwartz decay of chihat controls the logarithmically growing multiplier. Therefore

    A[F_R]/||F_R||² -> m(t0)<0.

In particular one may fix R large enough, normalize phi=F_R/||F_R||, and obtain

    supp(phi) in (-R/2,R/2),   A[phi]=-eta<0.

The zero mean excludes one frequency value, not a neighborhood of that value. More generally, any fixed finite set of exponential-polynomial moment or Fourier-evaluation constraints can be enforced by a nonzero constant-coefficient differential polynomial. Modulated dilation at a real frequency outside its finite root set still detects any open negative multiplier band.

## 3. The negative index grows at least linearly

The exact digamma representation gives

    gamma(t)-gamma(0)
      =2 integral_0^infinity e^(-u/2)(1-cos(tu))/(1-e^(-2u)) du.

For two sources with disjoint supports, the local diagonal part does not contribute, so Gamma has off-diagonal convolution kernel

    -e^(-|u|/2)/(1-e^(-2|u|)).

The inverse Fourier transform of 1/(t²+1/4) is e^(-|u|/2). Hence A has the exact off-diagonal kernel

    k_A(u)=-e^(-5|u|/2)/(1-e^(-2|u|)),   u != 0.          (1)

This identity is used only between separated supports, avoiding the singular diagonal distribution. It is also consistent with the pole-neutral leading-tail cancellation in the translated-probe calculation.

Translate the fixed normalized negative source phi from Section 2 onto a lattice with spacing D>R. The translates phi_j have disjoint supports, are L2 orthonormal, and each satisfies all three moments: translation merely multiplies each exponential moment by a nonzero scalar. For j!=k, (1) gives

    |A(phi_j,phi_k)|
      <= ||phi||_1² e^(-5(|j-k|D-R)/2)
                    /(1-e^(-2(D-R))).

The off-diagonal row sum of every finite translation Gram matrix is consequently at most

    r(D)=2||phi||_1² e^(5R/2) e^(-5D/2)
          /[(1-e^(-2(D-R)))(1-e^(-5D/2))].               (2)

Choose a fixed D so large that r(D)<eta/2. The diagonal entries are -eta, and the elementary row-sum operator bound shows that A is at most -eta/2 times the identity on the span of any N such translates. Centering their union inside I_L requires only R+(N-1)D<L. Thus, up to the harmless strict-endpoint adjustment,

    negative_index(A restricted to E_L)
      >= floor((L-R)/D),                                 (3)

for L sufficiently large. In particular the negative index is at least cL-O(1), with c=1/D>0. All constants depend on one chosen negative prepared source; no asymptotic prime estimate or RH is used.

If a bounded finite-rank selfadjoint correction C_L made A+C_L nonnegative, its rank would have to be at least this negative index. Indeed, any larger negative subspace intersects ker(C_L) nontrivially. The same conclusion applies to removing finitely many linear conditions: codimension r can remove at most r dimensions from that negative subspace. Therefore neither a fixed number of extra moments nor a fixed-rank low-frequency correction repairs A for unbounded L. A growing finite block remains possible; (3) says its required rank cannot stay fixed.

This is not an obstruction to the one-sided target E<=A. On a negative reference direction, that target demands a correspondingly negative discrepancy. Replacing the discrepancy by its absolute value destroys exactly the sign that could make the target true. A proposed |E|<=eta A fails already because its right side is negative on these directions. This does not rule out a two-sided estimate in a different positive reference norm; that would require a separate argument, such as the correctly scoped existing CCM obstruction.

## 4. Exact dilation and what local continuation supplies

Under the unitary map f(y)=sqrt(L)F(Ly) to (-1/2,1/2),

    Fhat(t)=sqrt(L) fhat(Lt),
    Gamma[F]=integral gamma(s/L)|fhat(s)|² ds/(2pi).

The finite prime-power term is a sum of compressed translations by log(p^m)/L with its unchanged coefficient log(p)/sqrt(p^m). Both prime insertions and repeated prime powers are included. The source space has codimension exactly three for every L>0. Its orthonormal constraint functions are

    1,
    sinh(Ly/2)/sqrt(ns(L)),
    [cosh(Ly/2)-m_L]/sqrt(nc(L)),

where m_L=sinh(L/4)/(L/4), ns(L)=sinh(L/2)/L-1/2, and nc(L)=sinh(L/2)/L+1/2-m_L². These functions and their orthogonal projection depend smoothly on L on every compact subinterval of (0,infinity). There is no growing codimension hidden in the dilation.

Bare compressed translations are strongly continuous in their delay but need not be norm continuous at a support threshold. Sandwiching with a fixed compact logarithmic-energy inverse square root restores norm continuity on a bounded L range: bounded strongly continuous families become norm continuous after multiplication on both sides by fixed compact operators. The archimedean change gamma(s/L)-gamma(s/L0) is a bounded multiplier, locally continuous in the supremum norm. The moment projections form a smooth family of fixed rank. These facts justify a local energy-relative continuation framework after identifying the varying codimension-three spaces; they do not give a favorable global modulus or sign.

Even an explicit local modulus cannot itself prevent finite accumulation. A certified margin delta(L) may approach zero at an unknown finite L*. The scalar continuous family q_L=L*-L illustrates the logic: every L<L* has a strict gap and admits local positive continuation, while steps chosen proportional to that margin can accumulate at L*. Compactness, smoothness, and a valid local perturbation bound do not exclude this event. A global proof must exclude loss of the sign or supply an independent recurrence whose accepted step lengths diverge.

## 5. A completeness lemma for the signed finite-frequency method

Fix L, its complete finite active prime-power multiplier q_L, and lambda>0. Choose T0 so large that q_L(t)>=lambda for |t|>=T0. Let E_L be the closed three-moment L2 source space, with its zero-extension logarithmic form domain. For T>=T0 define the bounded form

    Q_T[F]=lambda||F||²
       +integral_{|t|<=T}(q_L(t)-lambda)|Fhat(t)|² dt/(2pi)
       =lambda||F||²-<F,D_T F>.

Every D_T is compact: it is a finite-band source integral with a bounded weight and a square-integrable kernel on the finite source interval. The forms Q_T increase with T and converge to Q, possibly to +infinity outside its form domain.

**Lemma.** If Q>=delta I on this fixed source space for some delta>0, then for every 0<delta'<min(delta,lambda), a finite T satisfies Q_T>=delta'I.

To prove this, suppose there are T_n tending to infinity and unit sources u_n with Q_Tn[u_n]<delta'. Pass to a weakly convergent subsequence u_n -> u. For any fixed T, monotonicity and compactness of D_T imply

    Q_T[u]+lambda(1-||u||²)<=delta'.

Take T to infinity. This also proves u belongs to the form domain whenever needed, and gives

    delta||u||²+lambda(1-||u||²)<=delta',

contrary to delta'<min(delta,lambda). The argument does not assume norm convergence of the growing signed operators D_T.

For this finite T, Legendre compression and midpoint quadrature converge in operator norm; the analytic full-source tail and integration bounds tend to zero as rank and nodes grow. Strict finite-matrix inequalities can then be checked at finite outward precision. Consequently the signed certificate format, with adjustable finite resources and a positive rational target below the available margin, eventually succeeds whenever the fixed-window form has a strict positive gap.

This is an existence/completeness statement, not an efficient cost estimate. The absolute-amplitude cutoff can still require the previously identified double-exponential scale in L. It also does not prove its own hypothesis Q>=delta I. An exhaustive finite-parameter search is a semidecision procedure for strict positivity at a fixed L, not a proof that every search terminates.

## 6. Conditional strict gaps and finite-zero limitations

Under RH, the established zero-sampling formula gives Q>=0. At fixed L, its zero extension has compact resolvent because its archimedean logarithmic form has compact embedding and the active prime-shift sum is bounded. A strict positive gap follows if its kernel is trivial.

Here that kernel is indeed trivial under RH. If a form-domain F had Q[F]=0, finite partial zero-sampling sums and approximation by the smooth moment-preserving core imply Fhat(gamma)=0 at every distinct zero ordinate. Point evaluation of Fhat is continuous in the fixed-support L2 norm. Under RH the classical multiplicity bound m(rho)=O(log gamma/log log gamma), together with Riemann-von Mangoldt, gives at least a constant times T log log T distinct positive ordinates below T. The bounds are recorded in [Ivic, *On the multiplicity of zeros of the zeta-function*, equations (1.3)-(1.4)](https://arxiv.org/pdf/math/0501434). A nonzero Fourier transform of a compactly supported L2 source is an entire function of finite exponential type; Jensen's formula bounds its zero count in disks by O_F,L(T). The superlinear number of distinct ordinates is impossible. Thus F=0, and compact resolvent gives a fixed-window gap delta_L>0.

This paragraph is conditional on RH and the established sampling/core framework. It supplies no unconditional positivity input. Its purpose is to clarify that shrinking fixed-window gaps are compatible with RH and that theoretical completion of every finite certificate under RH does not settle the reverse direction. No assumption that all zeta zeros are simple is needed.

Nor can a finite list of verified zeros provide a full-source positive gap. Given any finite list of real sample ordinates gamma_j, take a nonzero compact smooth bump chi and apply the constant-coefficient differential operator

    F=(-d²/dx²+1/4) d/dx product_j(d/dx-i gamma_j) chi.

It stays in the same support, retains all three moments, and satisfies Fhat(gamma_j)=0 for every listed ordinate. It is not identically zero, since its Fourier transform is a nonzero polynomial times the nonzero entire transform of chi. Thus the corresponding finite sampling form has a nontrivial infinite-dimensional nullspace. A full-source gap requires control of the omitted sampling tail or a separate arithmetic argument, not merely a larger finite sample list.

## 7. The remaining all-window statement

One sufficient conclusion remains: for an explicitly unbounded sequence L_j, prove Q>=0 on the original three-moment complex source class in I_(L_j). A local relative comparison, compactness at every fixed L, conditional existence of strict gaps, and a complete certifier at each strictly positive window all preserve this obligation.

The new necessary refinement is that the centered low-frequency negative block cannot have fixed rank as L grows. Any centered-discrepancy mechanism must allow its size to grow, retain the negative discrepancy needed on that block, and control its coupling to the complementary energy. The translated-probe criterion developed alongside this audit provides a concrete family of such signed arithmetic tests; pairwise covariance bounds alone do not certify all finite Gram matrices. No all-window sign or recurrence is claimed here.
