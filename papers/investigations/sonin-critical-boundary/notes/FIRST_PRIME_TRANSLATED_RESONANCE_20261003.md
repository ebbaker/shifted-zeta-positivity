# First-prime translated resonance: positive prepared correction directions

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited subagent reasoning configuration; exact serving
variant and effort label are not exposed to this agent and are not inferred.
Status: analytic theorem checked in a separate same-model internal audit;
no numerical sign is used, no finite threshold is asserted, and no literature
priority claim is made. These checks are not independent specialist refereeing.

Inherited inputs are the [finite Euler identity and strict fixed-place gap](FINITE_EULER_BOUNDARY_IDENTITY_20261003.md),
especially Sections 2--4, and the [critical one-prime cosine expansion](FINITE_EULER_RANK_ONE_ANALYSIS_20261003.md),
Section 1. The latter's residual estimates are not needed for the asymptotic
sign proof below.

## Result and significance

At the critical one-prime phase, the correction need not be nonpositive even
on the prepared, mean-zero class in the first support window. More precisely,
fix a prime p and any L>log p. There are real smooth sources supported in
(-L/2,L/2), exactly satisfying all three conditions

    F = (-d²/dx²+1/4)h,    integral h = 0,
    Fhat(i/2)=Fhat(-i/2)=Fhat(0)=0,

for which K_{ {p},1/2}[F]>0. One can choose either additive parity.
For p=2 and log 2<L<log 3, this is the support-adapted prime set itself;
in particular it applies at L=1. It refutes the proposed mean-functional
upper bound at its first gate. It does not refute K<=B, Q>=0, or RH.

The mechanism is a translated singularity of the *first return*. The higher
returns form a trace-class operator and contribute a continuous correlation
kernel. At u=log p, pairs of dyadic cosine frequencies coincide. Their
rescaled sinc profile is positive on mean-zero packets. At u=0 the crossing
interval shrinks and removes the corresponding singularity. Two equal narrow
packets separated by log p therefore have a positive cross contribution
which dominates their diagonal contributions.

The lacunary profile is not replaced by a logarithm plus a continuous error.
Its bounded log-periodic part is retained through the exact sequence
of widths epsilon=p^{-N}.

## 1. Fixed operators and splitting off the first return

Work in physical coordinates L²(0,infinity;dx), chi=1_(0,1), P=1_(1,infinity).
Let B_n have kernel 2 cos(2 pi p^n xy). The previously established critical
one-prime expansion is

    F_p = -p^{-1} B_{-1} + (1-p^{-1}) sum_{n>=0} B_n,
    ||B_n|| = p^{-n/2}.

Thus the cosine kernel coefficients are c_{-1}=-2/p and
c_n=2(1-1/p) for n>=0. Set C=chi F_p chi, T=chi F_p P and
A=I-C². The inherited finite-place gap is A>=g I for some g>0.
For a smooth source, X=P a_e(D)chi is trace class, and

    K[F] = 2 Re Tr(C A^{-1} T X)
         = 2 Re Tr(C T X) + 2 Re Tr(R X),
    R = C³ A^{-1}T.                                      (1)

This split is legitimate without tracing C².

For n>=0, C_n=chi B_n chi obeys ||C_n||HS<=2 and
||C_n||<=p^{-n/2}. Consequently

    ||C_n||S3³ <= ||C_n|| ||C_n||HS² <= 4 p^{-n/2},
    ||C_n||S3 <= 4^{1/3} p^{-n/6}.

The dyadic expansion converges in Schatten class S3. Its sum equals C,
because it also converges in operator norm. Hence C³ is trace class and so
is R. This is compatible with C itself not being Hilbert--Schmidt.

Return briefly to logarithmic coordinates and write U_u f(x)=f(x-u).
For u>=0 define

    r(u) = Re Tr_chi(R P U_u chi).

The family P U_u chi is uniformly bounded and strongly continuous. A finite
rank approximation to R proves continuity of r: the finite-rank trace is a
finite sum of strongly continuous matrix coefficients, and the remainder is
uniformly bounded by its nuclear norm. In particular r(0)=0. Since

    X = integral_0^infinity Re(kappa_F(u)) P U_u chi du,

in weak operator sense (and the pairing with R is absolutely integrable),
the higher-return term in (1) is

    2 integral_0^infinity Re(kappa_F(u)) r(u) du.

Equivalently, it is the pairing of kappa_F with the real even continuous
kernel r(|u|). Only a bounded fixed interval of u is needed below.

## 2. First-return correlation kernel

For finite dyadic truncations, elementary integration over 0<z<1 gives

    (CT)(x,y) = sum_{n,m>=-1} (c_n c_m/2)
       [sinc(2 pi (p^n x-p^m y))
        +sinc(2 pi (p^n x+p^m y))],                       (2)

where sinc(t)=sin(t)/t, with value 1 at zero. The infinite version will be
used as a locally integrable kernel, not evaluated on resonant curves.

In physical coordinates the source crossing kernel is

    X(y,x)=(xy)^{-1/2} Re(kappa_F(log(y/x))),  y>1>x>0.

Putting y=e^u x gives, for u>0,

    e_1(u)=e^{u/2} integral_{e^{-u}}^1 (CT)(x,e^u x) dx,
    K_1[F]=2 integral_0^infinity Re(kappa_F(u)) e_1(u)du.
                                                               (3)

We extend e_1 evenly. Then K_1[F]=integral_R kappa_F(u)e_1(|u|)du.
The factors of two in (2)--(3) follow respectively from cos cos and from
the defining 2 Re trace. No arbitrary sign enters this kernel.

Here is a justification of the infinite kernel representation. Fix a compact
u interval [0,L]. The integration variable x satisfies e^{-L}<=x<=1.
Only finitely many integer ratios p^k can lie in e^{[0,L]}. Near u=k log p,
the difference terms with n-m=k are the resonant ones. Every other difference
term has |p^n-e^u p^m|>=c p^{max(n,m)}, with c>0 after removing those
finitely many resonant families. All sum-frequency terms have the same type
of lower bound. Their absolute values are therefore bounded by
C p^{-max(n,m)}, and the double sum of these bounds converges. Terms with
index -1 cause no additional infinite resonant family.

For a resonant family, the partial sums are bounded in absolute value by

    C_p (1 + log_+(1/|u-k log p|)),                        (4)

using |sinc t|<=min(1,1/|t|) and splitting where p^m |u-k log p| is one.
The bound is uniform in the truncation and in x in the indicated interval.
It is locally integrable in u. Dominated convergence thus proves convergence
of (3) for every smooth compact correlation. Independently C_N T_N -> CT
in operator norm, so Tr(C_N T_N X)->Tr(CT X) because X is trace class.
These two limits identify the integral kernel expression with the actual
operator trace. Equation (2) is not a pointwise value on a singular curve.

Near zero only n=m is resonant, and the integration interval in (3) has
length 1-e^{-u}=O(u). It follows that

    e_1(u)=O(u(1+|log u|)) as u downarrow 0,                (5)

so its even extension is continuous at zero with value zero.

## 3. Translated resonant component

Set a=log p. Near u=a the resonant pairs are n=m+1, m>=0. Thus

    e_1(u) = s(u)+v(u),                                   (6)
    s(u)=2(1-1/p)² e^{u/2}
         integral_{e^{-u}}^1 Psi(x(p-e^u)) dx,
    Psi(z)=sum_{m>=0} sinc(2 pi p^m z), z!=0,

where v is continuous in a neighborhood of a. This follows from the same
uniformly convergent nonresonant sums as above. The finite pair (n,m)=(0,-1)
is continuous and belongs to v, not s.

Define the bilateral renormalized profile

    Phi(z)= sum_{j>=0} sinc(2 pi p^j z)
          + sum_{j<0} [sinc(2 pi p^j z)-1], z!=0.          (7)

The negative-index series is locally uniformly convergent, and the positive
one is locally uniformly convergent off zero. For z in a fixed bounded set,

    |Phi(z)| <= C(1+|log|z||).

For epsilon=p^{-N}, exact reindexing gives

    Psi(epsilon z)=N+Phi(z)+O(epsilon² z²),                (8)

uniformly on bounded z sets away from the undefined value at zero, with the
error bound valid at the removable difference there. This retains every
log-periodic component.

## 4. Two exactly prepared packets

Choose a real nonzero g in C_c^infinity((-b,b)) with integral g=0, and put
f=-g''. Define a single prepared packet by

    h_epsilon(x)=epsilon g(x/epsilon),
    q_epsilon(x)=(-d²/dx²+1/4)h_epsilon(x)
                =epsilon^{-1} f_epsilon(x/epsilon),
    f_epsilon=f+epsilon² g/4.                             (9)

Each q_epsilon is exactly pole neutral and has exactly zero mean. In
particular integral f_epsilon=0. Its correlation is

    kappa_{q_epsilon}(u)=epsilon^{-1}
                         kappa_{f_epsilon}(u/epsilon).

Now use two identical translates centered at -a/2 and a/2:

    H_epsilon(x)=h_epsilon(x+a/2)+h_epsilon(x-a/2),
    F_epsilon=(-d²/dx²+1/4)H_epsilon.

For small epsilon its support lies in (-L/2,L/2), since a+2b epsilon<L.
It is prepared, mean zero and real. Its correlation is exactly

    kappa_{F_epsilon}(u)=2 kappa_{q_epsilon}(u)
       +kappa_{q_epsilon}(u-a)+kappa_{q_epsilon}(u+a).      (10)

The correlations kappa_{f_epsilon} have fixed compact support, uniformly
bounded L1 norms, and integral zero. They converge smoothly to kappa_f.

Every continuous kernel contributes o(1) when paired with the translated
single-packet correlations: after rescaling, subtract its value at the
packet center and use integral kappa_{f_epsilon}=0. This handles the whole
higher-return term, the v term near ±a, and the first-return self term
near zero. Equation (5) also gives the explicit self estimate
O(epsilon(1+|log epsilon|)). Thus only the s terms near ±a survive.

## 5. Positive exact limit, including the log-periodic part

Consider one cross contribution and substitute u=a+epsilon w. In s(u),
freeze the prefactor at sqrt(p) and the interval at [1/p,1]. The change in
prefactor and endpoints is O(epsilon |w|), while (4) is bounded by
C(1+N+|log|w||). The integrated error is O(epsilon(1+N)), hence tends to
zero. After freezing, apply (8) with

    z_N(x,w)=p x (e^{epsilon w}-1)/epsilon -> p x w.

Evenness of Psi removes the minus sign in p-e^{a+epsilon w}.
For w in the fixed packet-correlation support, z_N is uniformly comparable
to w, while x is bounded away from zero. The N term in (8) vanishes exactly
against kappa_{f_epsilon}. The error O(epsilon² z_N²) tends to zero.
Finally the logarithmic bound for Phi supplies an integrable majorant
C(1+|log|w||). Dominated convergence, rather than a false uniform derivative
bound for the lacunary sum, gives

    lim integral kappa_{q_epsilon}(u-a)s(u)du
       =2(1-1/p)² sqrt(p)
          integral_{1/p}^1 integral_R kappa_f(w)Phi(p x w)dw dx.
                                                               (11)

The inner integral is strictly positive. To see this without assuming a
sign for Phi pointwise, pair the series (7). For alpha>0,

    integral_R kappa_f(w)sinc(alpha w)dw
        =(1/(2 alpha)) integral_{-alpha}^{alpha}|fhat(t)|²dt >=0. (12)

The subtracted constants in (7) vanish because integral kappa_f=0.
Write alpha_j(x)=2 pi p^{j+1}x. Then define

    S_p[f] = integral_{1/p}^1 sum_{j in Z}
             (1/(2 alpha_j(x)))
             integral_{-alpha_j(x)}^{alpha_j(x)}|fhat(t)|²dt dx. (13)

This is finite and strictly positive for f!=0. At j->-infinity,
fhat(0)=0 gives each term O(alpha_j²); at j->+infinity, Plancherel gives
O(alpha_j^{-1}). Both are uniformly summable for 1/p<=x<=1. Positivity is
strict because f is nonzero. Interchanging the negative-index series is
justified by |sinc t-1|<=C t². For the positive-index series, its integral
against the absolute value of a bounded compact correlation is
O((1+log alpha_j)/alpha_j), which is summable. Thus (12)--(13) agree with
the paired Phi distribution, including its log-periodic part.

There are two equal cross contributions in (10). Combining (1)--(13) yields

    K_{ {p},1/2}[F_{p^{-N}}]
       -> 4(1-1/p)² sqrt(p) S_p[-g''] > 0.                (14)

This proves eventual positivity of the actual infinite-operator correction,
without a sampled eigenvalue, a finite inverse replacement, or a numerical
sign assertion. It is an existence theorem with sufficiently large N; no
explicit minimum N is claimed here.

For p=2 the coefficient in (14) is sqrt(2). If a unit L2 norm is desired,
the two packets are disjoint for small epsilon and

    ||F_epsilon||²=2 epsilon^{-1}||f_epsilon||²,
    K[F_epsilon/||F_epsilon||]
       =epsilon * [2(1-1/p)²sqrt(p)S_p[f]/||f||²] + o(epsilon). (15)

The normalized positive corrections become small, which helps explain why
fixed low-complexity source tests need not reveal this obstruction.

There is also a quantitative bracket for the positive limiting constant
Lambda_p in (14). Put

    E[f]=integral_R |fhat(t)|²/|t| dt.

This is finite and positive because f is nonzero, has zero mean and is
smooth with compact support. For fixed x and t!=0, the geometric sequence
alpha_j(x) gives

    1/[2(p-1)|t|]
       <= sum_j 1_{|t|<=alpha_j(x)}/(2 alpha_j(x))
       <= p/[2(p-1)|t|].

Tonelli's theorem in (13) and the length 1-1/p of the x interval imply

    [2(1-1/p)²/sqrt(p)] E[f] <= Lambda_p
       <= [2 sqrt(p)(1-1/p)²] E[f].                       (16)

For p=2, E[f]/(2 sqrt(2)) <= Lambda_2 <= E[f]/sqrt(2).
This bound controls the exact limiting profile, not the finite-epsilon
remainder, so it supplies no unstated finite threshold N.

For this particular family one can check the vanishing higher returns
directly, without introducing their continuous correlation kernel:

    Fhat_epsilon(t)=2 cos(a t/2)
                       [fhat(epsilon t)+epsilon² ghat(epsilon t)/4].

This tends to zero pointwise and is uniformly bounded. Dominated Plancherel
therefore gives a_{epsilon,e}(D)->0 strongly, hence X_epsilon->0 strongly
with a uniform operator-norm bound. Pairing with the trace-class R in (1)
shows Tr(R X_epsilon)->0. This is an independent justification of the
higher-return limit used in (14).

## 6. Both parities and arbitrarily large positive subspaces

Choose a real compactly supported even bump phi. Taking g=phi' gives an odd
mean-zero packet profile; the identical pair centered at ±a/2 is globally
odd. Taking g=phi'' gives an even mean-zero profile and a globally even
pair. Both are nonzero and satisfy the theorem.

More generally, let G be any finite-dimensional space of such packet
profiles, with fixed support and zero mean. The map g -> -g'' is injective
on C_c^infinity, and S_p[-g''] is a positive-definite quadratic form on G.
The map g -> F_epsilon is linear. Apply (14) to real basis vectors and their
pairwise sums to obtain entrywise convergence of the finite real symmetric
correction matrix. Its positive-definite limit implies that,
for sufficiently large common N, the correction is positive definite on
the entire image of G. The image has dimension dim G because the two
packets have disjoint supports and the preparation differential operator
(-d²/dx²+1/4) has no compactly supported kernel.

Consequently the prepared, mean-zero correction at any L>log p has
arbitrarily large finite-dimensional positive subspaces. The construction
can be carried out entirely within either parity sector and then
complexified. Indeed for real sources U,V, the exact correction depends on
the real part of the correlation, and Re(kappa_{U+iV})=kappa_U+kappa_V.
Consequently K[U+iV]=K[U]+K[V]; positivity of the real symmetric matrix
is also positivity on its complex span. This is an infinite-positive-index
statement about the smooth source form; it does not presume a bounded
realization on ordinary L2.

A finite-rank penalty cannot dominate that form. Indeed, if k linear
functionals controlled the correction by a nonnegative quadratic form in
their values, a positive subspace of dimension k+1 would contain a nonzero
vector annihilated by all k functionals. The proposed domination would give
K<=0 there, contradicting positive definiteness. In particular, at p=2,
log 2<L<log 3, neither the rank-one mean penalty nor any fixed finite list
of Mellin-moment penalties can repair this support-adapted correction bound.

## 7. Boundaries of the conclusion and next verification

The sign obtained is K>0; it does not assert K>B. The identity Q=B-K still
leaves open whether Q is nonnegative. No claim concerning off-line zeros or
RH follows from the obstruction. The result targets the strong Sonin
comparison and its finite-rank defect variants, at the actual first-prime
support window.

The inherited ingredients are the finite Euler operator identity, its fixed
positive gap, its source smoothing, and the one-prime cosine expansion.
The new derivation isolates the translated first-return singularity, proves
that higher returns are continuous at the correlation level, preserves the
lacunary rescaling profile, and obtains the positive packet limit.

A separate proof audit should check especially: the coefficient in (3),
the uniform integrable majorant in (4), the endpoint-freezing error in (11),
and the finite-dimensional polarization used after (14). An explicit
numerical witness would require quantitative error constants and a finite
threshold N, rather than replacing the asymptotic existence proof by an
uncertified scan.
