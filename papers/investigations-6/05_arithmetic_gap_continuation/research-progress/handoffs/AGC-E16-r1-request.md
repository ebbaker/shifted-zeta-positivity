# AGC-E16 r1: fixed three-prime ellipse allowance failure

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Contract author explicitly dispatched
**gpt-6-astra / ultra**; independent serving-backend attestation and root
settings unavailable. **Type E; recommended Sol6.1 ultra.** Parent B04 r1.
The mechanism, domain, proof route and completion test are fixed below.
The [sole register](../01_AGC_RESEARCH_PROGRESS_20261119.md) owns status.

**Question:** prove a quantified failure of exactly the finite
three-prime Euler/paired-ellipse lower allowance for the actual
normalized retained-value arithmetic. The expected result is a signed
complete allowance below−1/400 throughout the boundary segment F0.
This is a test of that estimator, not a zero of H or a universal
impossibility claim. No positive-margin assumption completes this task.

## Inputs and frozen domain

Read AGENTS.md, LARGE_FILES.md, GPT_RESEARCH_MODEL_WORKFLOW.md, the
[result index](../../../../../result-summaries/README.md),
[pattern index](../../../../../avoid/README.md), Controls12,
Cluster18, patterns01/02/07/11/12, Notes10–11 and13–16, Review07,
manuscript Section10 and the B04 request/return. Selected primary
inputs are [Polymath v2](https://arxiv.org/html/1904.12438v2),
(9)–(22), retained Corollary6.4, §8.5/Lemma8.5, Proposition9.1 and
Theorem1.2. Reopen only the needed passages; use no numerical constant
from the paper's t=.2 run at the present t=.1.

Prerequisite identities at freezing:

- Note14 SHA-256: `53fbba8135f853c54369b7bf1bddf862b3f49d8450d35ed4821450e41029d376`.
- Note15 SHA-256: `169d6f988dc01e625aa3020f95b5c02cddc5a761c163dd17404b3d0459aa5e3a`.
- Review07 SHA-256: `9078835a9a5eac6b34f307c9c43be75e6e6707fd3293408a869496a5469d0d9b`.
- B04 r1 request SHA-256: `43cdaac6c259022819ba49bfbad30eba8a66e20c8893a36defcaa957b003cec0`.

Keep the literal theta source, t=1/10, normalized retained reference
q=Qval_N/B=f−c and full v=Vval_N/|B|. The intended final strip is
x>=x0=14000+sqrt(24/25),1/5<=y<=sqrt(4/5). The **fixed proof domain** is

    F0: x0<=x<=30000, y=1/5, t=1/10.

There is no numerical sampling of F0. Note16 fixes the definitions of
s=sigma+i*tau, b_n, gamma,kappa,N,E,lambda_d,beta_m,a_m. In particular

    E=product_(p in {2,3,5})(1−b_p p^(−s)),  b_n=exp(log(n)^2/40),
    beta_m=sum_(d|gcd(m,30),m/d<=N)lambda_d b_(m/d),
    a_m=sum_(d|gcd(m,30),m/d<=N)lambda_d(m/d)^y b_(m/d),
    1<=m<=30N,  lambda_d=product_(p|d)(−b_p).

The indicator m/d<=N is compulsory. Do not pretend that b_n is
completely multiplicative or omit the edge terms beyond N.

## Proof obligations

1. **Exact normalized identity and error.** Verify f=P_N/B and
q=f−c with c=J_N A_N(x/2+pi/80)/B. Keep the complete v from Note14,
including both term-error sums and both entire delta payments. Set
S=sum b_n n^(−s),T=sum b_n n^(y−s), U=ES,V=ET and g=|gamma|.
The kappa replacement has payment

       D_kappa=g sum_(n<=N)b_n n^(y−sigma)
                             [exp(|kappa|log n)−1].

   Prove |f−(S+gamma conjugate(T))|<=D_kappa. This is an arithmetic
   replacement payment in addition to the physical source error v.

2. **Paired-ellipse lower bound.** Establish E!=0, g<1 on F0 and
E(S+gamma conjugate(T))=U+rho conjugate(V),
rho=gamma E/conjugate(E). Rotate by half its phase and use

       ||w||_g=sqrt((Re w/(1+g))^2+(Im w/(1−g))^2).

   Since beta_1=a_1=1, derive

       K=(1−g)−sum_(m=2)^(30N) h_m m^(−sigma),
       h_m=max(|beta_m−g a_m|, (1−g)/(1+g)|beta_m+g a_m|),
       ell_E=K/|E|−D_kappa−|c|<=|q|,
       m_E=ell_E−v.

   The inequality remains valid when K is negative. Its definition
   uses exact |E|; substituting an upper bound for that denominator
   is not an allowed signed-lower-bound step. The later use of |E|<8
   bounds this already defined negative allowance from above. State exactly
   the phase identities retained and the cross-index phase constraints
   discarded by the final triangle sum. Derive this modulus inequality
   directly; no distance-to-ray theorem or argument-principle conclusion
   is required.

3. **Analytic rational constants on F0.** Prove

       N>=33, 3/5<sigma<4/5, 0<g<3/5, 0<|E|<8.

   Use Note16's explicit real-alpha bound. With T0=x/2,

       Re alpha(3/5−iT0)−.5log(T0/(2pi))
          <= .39/T0^2−.4/(T0^2+.16)<0.

   Then x/(4pi)<2500<e^8 gives sigma<.8; a crude lower real-alpha
   bound gives sigma>.6. Source(20) gives
   g<=e^(1/250)(x/(4pi))^(−1/10)<3/5. For example use
   x/(4pi)>1000,1000^(1/10)>9/5 and e^(1/250)<27/25,
   each checked by rational inequalities. The factor moduli are less
   than1 because log p<2 and sigma>3/5, proving E!=0 and |E|<8.

4. **Finite exact eight-prime witness.** With
P*={7,11,13,17,19,23,29,31}, prove

       sum_(p in P*)exp(log(p)^2/40)p^(−4/5)>21/20.

   Use the concrete exact-rational route supplied by the root's
   separately dispatched Sol6.1/ultra [preflight](AGC-E16-r0-preflight-return.md).
   Write b_p p^(−4/5)=p^(−1)exp(log(p)/5+log(p)^2/40),
   and P_j(v)=sum_(h=0)^j v^h/h!. The rows are

   | p | lower r for log p | lower v for r/5+r^2/40 | k | j for log-bound denominator |
   | --- | --- | --- | --- | --- |
   | 7 | 19/10 | 47/100 | 228 | 1 |
   | 11 | 23/10 | 59/100 | 163 | 2 |
   | 13 | 5/2 | 13/20 | 147 | 2 |
   | 17 | 14/5 | 3/4 | 124 | 1 |
   | 19 | 29/10 | 79/100 | 115 | 1 |
   | 23 | 31/10 | 43/50 | 102 | 3 |
   | 29 | 33/10 | 93/100 | 87 | 2 |
   | 31 | 17/5 | 193/200 | 84 | 2 |

   Prove e<68/25, then e^r<(68/25)^ceil(r)/P_j(ceil(r)−r)<p,
   r/5+r^2/40>v and P_4(v)/p>k/1000 for each row. Their k sum
   is1050, so strictness gives the target>21/20. These are fixed
   rational checks, not fitted outputs. Integer/rational verification may be recorded
   as a small execution record if needed, but no parameter search,
   transcendental sampling or numerical campaign is authorized. A
   routine rational simplification of these same rows is permitted;
   failure of a row must be documented before any bounded repair.

   Since p<=N and gcd(p,30)=1, beta_p=b_p,a_p=p^y b_p and
   h_p>=(1−g)b_p. Deduce K<−(1−g)/20<−1/50 and therefore

       ell_E<−1/400,  m_E<−1/400 throughout F0.

   The nonnegative version max(0,ell_E)=0 cannot exceed v strictly.
   Do not interpret this as a bound above on |q| or |H|.

5. **Complete direct comparator.** Give the equally informed direct
calculation all coefficients, phases, c and v. Establish
m_dir=|f−c|−v>=m_E. Explain that this estimator itself is available
to direct evaluation. No assertion that m_dir fails, no speed claim,
and no dominance over every interval or grouped-phase estimator.

6. **Coverage and controls.** Treat each natural cutoff independently,
including the one-sided old endpoint and new natural endpoint. N>=33
and the eight unaffected primes hold on both sides of every seam
in F0. If a fixed reference is transferred, retain Note14's exact
signed jump and its full payment. No floor differentiation.

   The full finite-height/tail join remains unacquired. Assign an
   effective X_tail and paid overlap as dependencies of a future
   successful full-strip acquisition; classical eventual two-carrier
   coverage is not new. Prove that the present included-endpoint
   failure cannot be repaired by choosing or moving this join. Do not
   calculate an already-known tail just to fill this interface.
   Preserve the separate initial and intermediate-barrier obligations.

   Screen Controls12 by actual source-identification, convolution/phase
   and strict-floor premises. Finite-prime compatibility alone does
   not imply the complete theta formula. At any included zero a valid
   complete source enclosure forces ell−v<=0. Include the exact
   quadratic at T=1/4 with zero t=.1,z=x_c+i sqrt(3/10),x_c>=x0;
   it supplies the actual strip geometry but not theta arithmetic.
   Retain conditional/event/location qualifiers of each control class.

## Completion, work limit and ownership

One analytical proof pass and one bounded correction pass. Completion
is a complete proof of the stated **allowance** failure, with the eight
exact rational terms, direct comparator, source/cutoff interfaces and
scoped controls. A negative result completes this E task. No numerical
packet or larger multiplier is authorized. If a target constant or
algebraic premise fails, record the exact failed step and return to B04;
do not silently change the information class, domain, source or target.

Write `notes/17_AGC_E16_THREE_PRIME_ELLIPSE_OBSTRUCTION_20261119.md`
and `research-progress/handoffs/AGC-E16-r1-return.md`; one small exact
arithmetic record under numerics/ is permitted if useful. Root owns
the register, all indexes, manuscript and chat history. Preserve earlier
scientific files and pins. Record actual available model/effort and
separate dispatch from serving-backend attestation. A separate nonauthor
assessment is required before accepted status or manuscript milestone.

The result is confined to fixed {2,3,5}, anchor1, individual paired
ellipse radii and separate correction/kappa/source payments. Larger
or adaptive products, signed groups, height-phase constraints and
joint correction/remainder information remain outside this screen.
