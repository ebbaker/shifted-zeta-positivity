# Topology of positive limits and the fixed compression obstruction

29 September 2026. Prepared for Edward Baker with LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. This is an independent same-model
mathematical and primary-source scope review, not human refereeing. No
numerical certificates were recalculated for this analysis.

## 1. Primary-source scope

[Connes–Consani, Theorem 7 and equations (83)–(84)](https://arxiv.org/html/2006.13771v1#S4)
provide the smoothed cutoff-1 archimedean trace and its correction. Their
[Appendix C, Proposition 1](https://arxiv.org/html/2006.13771v1#A3) allows a
fixed finite set of prescribed Mellin zeros disjoint from the nontrivial
zeta zeros, including the pole-neutral conditions. The short-support
dominance theorem is not an arbitrary-support theorem.

[CCM, Sections 4.6–4.8, equation (57), and Theorem 4.6](https://arxiv.org/html/2310.18423v2#S4.SS6)
identify the finite-place transport and establish a topological Hilbert-space
isomorphism for each finite set of places. Section 4.8 explicitly retains
the dependence of the inner product on that set. These results do not give
a convergence theorem for the repository's smoothed traces as all primes
are included. The cutoff parameter and the finite place set are distinct
parameters. [Quasi-inner functions and local factors](https://arxiv.org/html/2008.10974)
supplies another finite-place operator framework; its inductive maps do not
by themselves establish trace convergence of the ordinary orthogonal
projections used here. This review found no such limit theorem in these
specific sources; it does not claim an exhaustive literature survey.

## 2. Exact direct target

For the actual finite-place projections P_S, put

    B_S[f]=||C_f P_S||_HS^2 >=0.

For a fixed pole-neutral compact smooth source f, the audited comparison is

    B_S[f]-Q[f]=E_infinity[f]+Delta_S[f]+W[f].

The full arithmetic prime-power sum W[f] has only finitely many nonzero
terms. Its stabilization when S contains the active primes does not imply
stabilization of B_S. A direct large-place target is therefore

    Delta_S[f] -> -E_infinity[f]-W[f].

No finite-stage residual sign is required. Controlling a signed sum of
place increments and identifying this endpoint would be substantive work;
merely proving convergence to an unnamed limit would not suffice.

## 3. Fixed bounded compression cannot realize the global target

### Proposition

Let H=L2(R,dx), let C_f be convolution with a compact smooth source, and let
P be a fixed orthogonal projection on H. Assume C_f P is Hilbert–Schmidt for
every compact smooth pole-neutral source f. Then

    ||C_f P||_HS^2 = Q[f]

cannot hold for every such source on arbitrarily large supports.

The assertion also applies to a fixed bounded positive contraction T with
the form Tr(C_f T C_f*)=||C_f T^(1/2)||_HS^2.

### Proof: absolute continuity of a fixed compression

Use Fourier measure dt/(2pi), and let E_J be the corresponding frequency
spectral projection. For an orthonormal basis (e_n), Tonelli gives

    nu_P(J)=Tr(P E_J P)
           =sum_n integral_J |Fourier(Pe_n)(t)|^2 dt/(2pi),

    ||C_fP||_HS^2 = integral |fhat(t)|^2 dnu_P(t).

Thus nu_P is absolutely continuous with respect to Lebesgue measure. It
is locally finite: at every real frequency t one can choose a prepared
source f=P0 h, P0=-d^2/dx^2+1/4, whose Fourier transform is nonzero there.
The Fourier multiplier w(t)=t^2+1/4 never vanishes on the real line. A finite
cover of a compact frequency interval gives sources f_1,...,f_k for which
sum |fhat_i|^2 is bounded below on that interval. Their finite traces then
bound its nu_P mass.

### Proof: polynomial growth needed for uniqueness

Fix a compact support interval K with nonempty interior. The linear map

    h in C_K^infinity -> C_(P0 h) P in S2

has closed graph. Indeed convergence in C_K^infinity gives operator-norm
convergence of the convolution operators, whereas S2 convergence implies
operator-norm convergence as well. The two limits must agree. By the
closed graph theorem this map is continuous for finitely many smooth
seminorms on K.

Choose phi in C_K^infinity such that |phihat(s)| is bounded below for
|s|<=1, and apply this bound to h_t(x)=exp(itx)phi(x). The seminorms grow
at most polynomially in |t|. On [t-1,t+1],

    |Fourier(P0 h_t)(s)|=w(s)|phihat(s-t)|

is uniformly bounded below. Hence nu_P([t-1,t+1]) has at most polynomial
growth. In particular nu_P is a tempered measure. This argument avoids
assuming a uniform global L2 bound for the source-to-Hilbert–Schmidt map.

### Proof: arithmetic identification forces atoms

Suppose the proposed identity holds on all pole-neutral compact tests.
Its positive left side implies RH by the restricted Weil criterion.
Under RH, the explicit formula then gives

    Q[f]=sum_gamma multiplicity(gamma) |fhat(gamma)|^2
         =integral |fhat(t)|^2 dmu(t),

where mu is the nonzero discrete zero-counting measure. This use of RH is
a consequence of the assumed identity, not an assumption in the proposition.
The classical zero-counting bound makes mu tempered.

For every h in C_c^infinity, substitute f=P0h and polarize. This gives

    integral overline(hhat(t)) khat(t) d[w^2(nu_P-mu)](t)=0

for every h,k in C_c^infinity. Let sigma=w^2(nu_P-mu), a tempered
distribution. Its inverse Fourier transform annihilates every convolution
of the form h_tilde*k, with h_tilde(x)=overline(h(-x)). Taking h to be a
compact smooth approximate identity shows that it annihilates every
compact smooth k. Thus sigma=0. Since w is everywhere positive on R,
nu_P=mu. This contradicts absolute continuity of nu_P and the nonzero
atomic measure mu.

For a bounded positive T, replace P in the measure construction by
T^(1/2); the same proof applies.

### Scope and relation to the existing program

This is not a new broad impossibility claim against positive limits. It
excludes a fixed bounded compression on the ordinary logarithmic L2 space
as the final exact all-support realization. It is closely related to the
existing no-closable-factor theorem in Section 9 of
[the positive-factorizations manuscript](../../../previous/positive-factorizations/manuscript.tex):
both reflect the singular sampling measure required by the global arithmetic
form. No novelty claim is made. Fixed-support realizations and singular
limits of positive forms remain possible.

Additional fixed permitted Mellin zeros do not remove the obstruction:
the corresponding source-preparation multiplier can only vanish at a finite
set of frequencies disjoint from the required zeta-zero atoms. The same
polarization argument identifies the weighted measures away from that set.

## 4. Why state-space trace compactness is the wrong mandatory gate

Strong convergence P_j->P alone does not imply convergence of
||C_fP_j||_HS. A simple example is rank-one projections onto spatial
translations of a fixed compact bump. They converge strongly to zero,
but convolution commutes with translations, so their smoothed traces are
a fixed positive number for an appropriate f.

For comparison, the following *sufficient* trace-passage lemma is valid.
If P_j converges weakly to a positive contraction T and, for finite-rank
E_N increasing strongly to I,

    lim_N sup_j Tr((I-E_N) C_f P_j C_f*)=0,

then finite-rank compression followed by the tail bound gives

    Tr(C_fP_jC_f*) -> Tr(C_f T C_f*).

The limit is finite, as follows by monotone approximation/Fatou. However,
imposing this condition for all prepared sources while requiring the limit
to be Q would contradict Section 3. Thus this valid sufficient lemma must
not become a mandatory gate for the direct program. It asks for a fixed
ordinary-state realization that the target cannot have.

## 5. Rank-one model of the needed spectral concentration

Choose a smooth compactly supported function phi in frequency space with
integral |phi|^2 dt/(2pi)=1. Define a normalized wavepacket by

    psihat_j(t)=sqrt(j) phi(j(t-gamma)),
    P_j=|psi_j><psi_j|.

Then psi_j tends weakly to zero, so P_j tends strongly to zero. Nevertheless

    nu_j=|psihat_j(t)|^2 dt/(2pi) -> delta_gamma

vaguely, and for every compact smooth source

    ||C_fP_j||_HS^2 -> |fhat(gamma)|^2.

This is a model of concentration of absolutely continuous positive
frequency measures into an atom. It is not an arithmetic construction and
does not use supposed real ordinates to define a zeta proof. It shows that
a zero strong projection limit is compatible with a nonzero, potentially
relevant positive trace limit.

The appropriate sufficient topology is vague convergence of positive
frequency measures, together with source-weighted frequency tail control:

    lim_T sup_j integral_(|t|>T) |fhat(t)|^2 dnu_j(t)=0

for each required fixed source. The limiting distribution must be identified
through the arithmetic expression. It must not be defined as a sum over
assumed real zeta zeros.

## 6. A controlled regularized baseline and its limitation

For fixed sigma>1 define

    D_(S,sigma)=product_(p in S) (I-p^(-sigma)U_log p).

Absolute summability of sum_p p^(-sigma) gives operator-norm convergence
to a bounded invertible D_sigma, including bounded inverses. There is a
uniform positive lower bound for A_(S,sigma)=P D*D P on Ran P. Therefore
the actual orthogonal projections onto D_(S,sigma)Ran P have a limit, and

    C_f J_(S,sigma)
      =D_(S,sigma)(C_fP) A_(S,sigma)^(-1/2)

converges in S2 for each compact smooth source. The resulting positive form
is a fixed bounded-compression form B_sigma, which Section 3 proves cannot
already equal Q globally. This baseline is unconditional but is not the
arithmetic endpoint. A successful continuation toward sigma=1/2 cannot
retain all of this ordinary-state trace compactness.

## 7. Independent audit of the zeta-phase endpoint observation

Let R_+=1_(0,infinity) in logarithmic position, let J be reflection, and
write the archimedean cosine involution in Fourier coordinates as

    F_infinity=m_infinity(t) J,
    m_infinity(t)=L_infinity(1/2-it)/L_infinity(1/2+it).

For real sigma define, almost everywhere,

    F_sigma=m_infinity(t) [zeta(sigma-it)/zeta(sigma+it)] J.

The multiplier is unimodular and obeys m(-t)=overline(m(t)), so F_sigma
is a unitary involution. Isolated zeros or poles on a vertical line affect
only a null set. For sigma>1 the absolutely convergent positive-delay
Dirichlet series for D_sigma and D_sigma^(-1) preserve R_+ in both
directions. Consequently

    F_sigma=D_sigma F_infinity D_sigma^(-1),
    D_sigma K=Ran R_+ intersect F_sigma Ran R_+.

At sigma=1/2, the functional equation gives

    zeta(1/2+it)/zeta(1/2-it)=m_infinity(t)

off its discrete zero set. Hence F_(1/2)=J almost everywhere. Bounded
multiplier convergence gives F_sigma->J strongly as sigma decreases to
1/2. If P_sigma is the orthogonal projection onto
Ran R_+ intersect F_sigma Ran R_+, put Q_sigma=F_sigma R_+ F_sigma.
Then Q_sigma->R_- strongly, and

    0 <= P_sigma <= R_+ Q_sigma R_+ ->0 strongly.

Thus P_sigma->0 strongly. By Section 5 this does not settle its smoothed
traces. For 1/2<sigma<=1 the intersection projection is well-defined, but
the D_sigma similarity and trace finiteness have not been established by
this argument. Those cannot be inherited from the sigma>1 baseline.

## 8. Dense prepared sources: distinguish convergence from positivity

For each fixed support interval let X_L be the closure of pole-neutral
compact smooth tests in the known logarithmic form norm. The arithmetic
form Q_L is continuous there. A countable dense prepared-source class can
be built from smooth h and f=P0h using the same-support preparation, with
rational linear combinations and an exhaustion by compact subintervals.

If positive forms P_j satisfy P_j[g]->Q[g] for every g in such a dense
class, then Q[g]>=0 there and continuity of Q gives positivity on all of
X_L. No uniform bound on P_j is needed for that sign implication. An
analytic theorem covering the entire dense class is required; finitely
many diagonal basis checks are insufficient.

To obtain convergence P_j[f]->Q[f] itself for every f from dense-class
convergence, a sufficient additional condition is

    P_j[f] <= C_L ||f||_log^2

uniformly in j. Positivity supplies Cauchy–Schwarz for the polarized forms,
so this gives equicontinuity and the standard dense-approximation argument.
The constant may depend on L. Neither this bound nor the dense-class
convergence has been proved for the critical large-place candidate.

## Outcome

The direct program should search for spectral concentration and an
arithmetically identified weak limit, not insist on a fixed final ordinary
L2 projection. The finite-place and sigma>1 constructions give independently
positive candidates and controlled baselines. The next critical obligations
are trace finiteness in the intended limiting family, source-weighted
frequency control, and arithmetic identification of the limit. No residual
sign, global trace limit, or RH theorem is claimed here.
