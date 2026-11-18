# VCD-GT-CM-E10 r1 — Collision-regular odd and even moment hierarchy

18 November 2026, America/New_York. Prepared for Edward Baker with OpenAI
Codex LLM assistance. Requested executor dispatch **gpt-6.1-sol / ultra**.
Independent actual serving model and reasoning effort metadata were
unavailable.

**Proved in-note on the stated domains, pending E11 assessment.** The
six pins in the [frozen request][request] match. The result is an infinite
relative moment representation. Its fixed-order equations are finite
polynomials regular through \(D=0\). [B04][decision] ·
[Result index][results] · [Cluster18][cluster] · [Avoid index][avoid] ·
[Classification01][class] · [Scope07][scope]

## 1. Hierarchy on the counted tube

Use the unchanged canonical field \(H_t=-H_{zz}\) and the compact
independently paid real count-two tube of [Note41][parent] and
[CM E02][e02]. Freeze \(T\ge64\), \(L=\log T\), \(\ell=1/L\),
\(c\in[T,2T]\), \(\max(2,4\sqrt d)\le a\le L\), \(r_0=a\ell\) and
\(|D|\le d\ell^2\le r_0^2/16\). The two target occurrences
\(c\pm\sqrt D\) lie within \(r_0/4\) of \(c\). The complete exterior
has \(|w_j|\ge r_0\), \(|\Im w_j|\le1\), where \(w_j=\rho_j-c\).
Use physical time throughout and put
\[
 Q(t,w)=w^2-D(t),\quad m_j=Q(t,w_j)^{-1},\quad
 S_n=\sum_j m_j^n\ (n\ge1),\qquad T_n=\sum_j w_jm_j^n\ (n\ge2).
\]
All sums count occurrences with multiplicity and are absolute by the
strip, unit count and collar; \(|Q(t,w_j)|\ge(15/16)|w_j|^2\).
Every one is real by conjugation on the canonical tube. Write \(M=S_1\).
Then
\[
 \begin{aligned}
 D'={}&2-4DS_1,\\
 S_n'={}&2n\sum_{r=1}^{n} S_r S_{n+1-r}
    +2n\sum_{r=2}^{n}\big(T_r T_{n+2-r}+D S_r S_{n+2-r}\big)
    -4n(n+2)S_{n+1}-4n(n+3)D S_{n+2}, \qquad n\ge1,\\
 T_n'={}&2(2n-1)\sum_{r=2}^{n}T_r S_{n+1-r}
    +4nD\sum_{r=2}^{n}T_r S_{n+2-r}
    -4(n^2+n-1)T_{n+1}-4n(n+3)D T_{n+2},\qquad n\ge2 .
 \end{aligned}                                                     \tag{1}
\]
An empty sum is zero. This gives componentwise algebraic closure for
the relative moments of the given heat field together with \(D\).
The absolute midpoint \(c\) retains its own contour drift law.
The displayed rows couple to higher moments. Well-posedness for
arbitrary moment sequences, finite truncations and signed forcing
estimates are outside the result.

## 2. Finite differentiation and exact cancellation

First work with a finite polynomial heat field at a simple-root slice
and an isolated selected pair. Factorization gives the simple-root
velocity \(2\sum_{\eta\ne\rho}(\rho-\eta)^{-1}\). In this finite
calculation alone write \(P=\sum_j w_jm_j\) and \(T_1=P\).
The target velocity average is \(c'=-2P\), since each exterior
occurrence contributes
\((s-w_j)^{-1}+(-s-w_j)^{-1}=-2w_jm_j\) with \(s^2=D\).
The target velocity difference multiplied by \(s\) is \(D'\).
The target-target part gives \(2\), and each exterior term gives
\(-4Dm_j\). At an exterior root the two target contributions give
\(4w_jm_j\). Thus
\[
 D'=2-4DS_1,\qquad
 w_j'=4w_jm_j-c'+2\sum_{k\ne j}\frac1{w_j-w_k}
      =4w_jm_j+2P+2\sum_{k\ne j}\frac1{w_j-w_k}.
 \tag{2}
\]
The drift \(P\) will cancel before complete passage.

For distinct exterior displacements \(u,v\), write
\(A=(u^2-D)^{-1}\), \(B=(v^2-D)^{-1}\),
\(C_k=\sum_{i=0}^{k-1}A^{k-1-i}B^i\) for \(k\ge1\), and \(C_0=0\).
Two divided differences are
\[
 \begin{aligned}
 \mathcal E_k(u,v)&=\frac{A^k-B^k}{u-v}=-(u+v)AB C_k,\\
 \mathcal O_k(u,v)&=\frac{uA^k-vB^k}{u-v}
      =-AB C_{k-1}-(D+uv)AB C_k .
 \end{aligned}                                                     \tag{3}
\]
The first uses \((A-B)/(u-v)=-(u+v)AB\). For the second,
\(x^k=C_kx-AB C_{k-1}\) for \(x=A,B\) by telescoping, and
\((uA-vB)/(u-v)=-(D+uv)AB\). The right sides of (3) have no
pole at \(u=v\) when \(Q(u)Q(v)\ne0\).

Since \(AB C_k=\sum_{r=1}^k A^r B^{k+1-r}\), converting unordered
pair sums to half the ordered off-diagonal sum gives
\[
 \begin{aligned}
 -\sum_{j<k}\mathcal O_{n+1}(w_j,w_k)={}&
  \frac12\sum_{r=1}^{n}(S_r S_{n+1-r}-S_{n+1})\\
 &+\frac D2\sum_{r=1}^{n+1}(S_r S_{n+2-r}-S_{n+2})\\
 &+\frac12\sum_{r=1}^{n+1}
               (T_r T_{n+2-r}-S_{n+1}-D S_{n+2}),\\
 -\sum_{j<k}\mathcal E_h(w_j,w_k)={}&
            \sum_{r=1}^{h}(T_r S_{h+1-r}-T_{h+1}) \qquad(h\ge1).
 \end{aligned}                                                     \tag{4}
\]
The spatial diagonal uses \(w_j^2 m_j^{n+2}=m_j^{n+1}+D m_j^{n+2}\).
In the even divided difference the two terms from \(u+v\) give
the same ordered sum, canceling the factor \(1/2\).

For \(f(w,D)=Q^{-n}\), use \(f_D=nQ^{-n-1}\),
\(f_w=-2nwQ^{-n-1}\) and symmetrize the last terms of (2), obtaining
\[
 S_n'=nD'S_{n+1}-8n(S_{n+1}+D S_{n+2})
       -4nP T_{n+1}-4n\sum_{j<k}\mathcal O_{n+1}(w_j,w_k).
 \tag{5}
\]
The two endpoints \(r=1,n+1\) of the \(T_r T_{n+2-r}\) sum
in (4) supply \(+4nP T_{n+1}\). The matching endpoints in the
\(D S_r S_{n+2-r}\) sum supply \(+4nD S_1 S_{n+1}\), canceling
the interaction part of \(nD'S_{n+1}\). The diagonals and the
target terms in (5) give coefficients
\(-6n-2n^2-2n(n+1)=-4n(n+2)\) for \(S_{n+1}\) and
\(-8n-4n(n+1)=-4n(n+3)\) for \(D S_{n+2}\).

For \(f(w,D)=wQ^{-n}\), \(f_D=nwQ^{-n-1}\) and
\(f_w=(1-2n)Q^{-n}-2nD Q^{-n-1}\). Hence
\[
 \begin{aligned}
 T_n'={}&nD'T_{n+1}+4(1-2n)T_{n+1}-8nD T_{n+2}\\
       &+2P\big[(1-2n)S_n-2nD S_{n+1}\big]\\
       &+2(1-2n)\sum_{j<k}\mathcal E_n(w_j,w_k)
                   -4nD\sum_{j<k}\mathcal E_{n+1}(w_j,w_k).
 \end{aligned}                                                     \tag{6}
\]
The \(r=1\) term of the last line of (4) cancels the two
drift terms in (6). The \(r=n+1\) term in the \(D\)-weighted
sum gives \(+4nDT_{n+1}S_1\), canceling the corresponding part of
\(nD'T_{n+1}\). The coefficients of \(T_{n+1}\) and \(DT_{n+2}\)
are \(2n+4(1-2n)+2n(1-2n)=-4(n^2+n-1)\) and
\(-8n-4n(n+1)=-4n(n+3)\). This proves the odd row of (1).
The relative equations have eliminated \(P\) at finite divisor
size. Absolute convergence of an infinite \(T_1\) is unnecessary.

In particular (1) gives the two inherited laws and the explicit
next spatial law
\[
 \begin{aligned}
 S_1'&=2M^2-12S_2-16D S_3,\\
 S_2'&=8M S_2-32S_3+4D S_2^2-40D S_4+4T_2^2,\\
 \boxed{T_2'=(6M+8D S_2)T_2-20T_3-40D T_4.}
 \end{aligned}                                                     \tag{7}
\]
The \(+4T_2^2\) spatial term is present with its inherited sign.
[Note41 §2][parent] · [GR E02 §§1–3][grproof] · [GR E05][graudit]

## 3. Fixed target contours and passage to the complete field

Fix a reference time \(\tau\). Let \(\Gamma\) be the positive fixed
physical circle centered at \(c(\tau)\) of radius \(r_0/2\), or an
analogous strictly separating circle for a finite polynomial. Put
\(u=z-c(t)\), \(Q=u^2-D(t)\), \(B=F_z/F\) for the field \(F\), and
write \(\langle f\rangle_\Gamma=(2\pi i)^{-1}\oint_\Gamma f(z)\,dz\).
The first two contour moments
\(J_k=\langle z^k B\rangle_\Gamma\) give
\(c=J_1/2,\ D=J_2/2-c^2\). They are holomorphic locally in time
by the strict clearance and the joint source holomorphy. The
fixed circle counts two occurrences by Rouché and contains both
poles of the rational kernels \(f=Q^{-n}\) and \(f=uQ^{-n}\)
at the respective allowed indices. In either case \(f=O(z^{-2})\)
at infinity, so \(\langle f\rangle_\Gamma=0\).
Every exterior divisor pole contributes
\(\langle f/(z-\rho_j)\rangle_\Gamma=-f(\rho_j)\) by the residue
theorem and decay at infinity. The target log derivative \(Q_z/Q\)
has \(\langle f Q_z/Q\rangle_\Gamma=0\) since the product is
\(O(z^{-3})\) and all its poles are enclosed. This last identity
holds for the two target poles together and at their coalescence.
For the canonical product, its inverse-square bound pays uniform
convergence of the once-regularized logarithmic derivative on
\(\Gamma\); any constant regularizer integrates to zero against
\(f\). Thus for finite and canonical fields we have
\[
 S_n=-\langle Q^{-n} B\rangle_\Gamma,\qquad
 T_n=-\langle uQ^{-n} B\rangle_\Gamma .
 \tag{8}
\]
Here \(T_n\) uses \(n\ge2\). The complete contour observables extend
holomorphically in time near the reference slice. Their derivatives
are \(-\langle f_t B+f B_t\rangle_\Gamma\) at fixed \(z\), using
\(Q_t=-2u c'-D'\), \(u_t=-c'\), and
\[
 B_t=-F_{zzz}/F+F_z F_{zz}/F^2 .
 \tag{9}
\]
The target term differentiates to the derivative of an identically
zero integral, also at \(D=0\). This proves collision regularity
without following individual exterior zeros.

At a multiple polynomial slice, perturb the finite factors to
distinct locations and initialize each polynomial's heat evolution
at that slice. Clearance preserves the target count and exterior
separation. Coefficient convergence and (8)–(9), together with the
two target moment contours, give convergence of the coordinates
and derivatives. All surviving terms on the right of (1) are
continuous finite symmetric sums of occurrence values. Thus the
finite identities hold at repeated targets and exterior zeros.
This argument is valid for complex perturbations and the inherited
canonical limit uses conjugation- and reflection-closed truncations.

For \(H\) at each \(\tau\), truncate its complete opposite-paired
product at modulus \(N>4T+8\), keeping all ties, multiplicities,
conjugates and negations. The truncated slice includes the exact
target factors. Initialize its polynomial heat evolution at that
same \(\tau\), using the terminating polynomial exponential.
The accepted \(\sum_{|\rho|>N}|\rho|^{-2}=O(\log N/N)\) tail pays
uniform product convergence on each compact spatial set and,
by Cauchy's formula on a larger set, its first three spatial
derivatives. At the reference slice these pay all the first
time jets in (9). A finite cover by cleared target circles with
compact subcharts gives positive lower bounds for \(|F|\) and
\(|Q|\) on the curves for sufficiently large \(N\). Thus (8)–(9)
and the target moments pass uniformly at fixed \(T\) for each
fixed \(n\). Since \(|w_j|\ge|\rho_j|/2\) in the omitted tail,
the strip/count give value errors \(O(N^{1-2n}\log N)\) for \(S_n\)
and \(O(N^{2-2n}\log N)\) for \(T_n\). These are uniform in real
time on the fixed-height compact tube with constants allowed to
depend on \(n\). Consequently every finite product of moments in a
fixed row of (1) converges. This proves the complete canonical
laws, including inward derivatives at the paid endpoints.
The passage uses only separately initialized slice products and
their first jets. [Note41 §§1–2][parent] · [GR E02 §3][grproof] ·
[GR E05][graudit] · [CM E04 §§1–2][cmreview]

## 4. Mixed integers and the coalescing poles

Let \(p,q\ge0\) be integers with \(p+q\ge2\) and \(s^2=D\).
Put \(k=\max(p,q)\). Including pure-axis powers, each summand is
\[
 \frac1{(w-s)^p(w+s)^q}
   =\frac{(w-s)^{k-p}(w+s)^{k-q}}{Q^k}.
 \tag{10}
\]
Expand the numerator in \(w\) with polynomial coefficients in \(s\).
Its degree is \(2k-p-q\le2k-2\). Every even monomial
\(w^{2j}Q^{-k}=(Q+D)^j Q^{-k}\) sums to
\(\sum_{i=0}^j\binom ji D^{j-i} S_{k-i}\), with \(j\le k-1\).
Every odd monomial sums to
\(\sum_{i=0}^j\binom ji D^{j-i} T_{k-i}\), using
\(w^{2j+1}=w(Q+D)^j\) and \(j\le k-2\). Thus all coefficients
after \(D=s^2\) are polynomials in \(s\), and the smallest indices
are \(1\) for \(S\) and \(2\) for \(T\). Formula (10) is a finite
identity of absolute occurrence sums. Conversely,
\[
 S_n=P_{n,n},\qquad
 T_n=\tfrac12(P_{n-1,n}+P_{n,n-1})\quad(n\ge2).
 \tag{11}
\]
The even moment identity also holds for \(n=1\).

At \(D=0\), both choices of \(s\) tend to zero and \(P_{p,q}\)
takes the common value \(\sum_j w_j^{-p-q}\) by (10).
Interchanging \(s\) and \(-s\) swaps \(p,q\), so symmetric
combinations have polynomial coefficients in \(D\) and hence
regular evolution by (1). An unbalanced individual split can
have a square-root time singularity at \(D=0\). For example
\(P_{2,0}=S_1+2D S_2+2sT_2\). On a \(D\ne0\) label chart
\(s'=D'/(2s)\), and that formula alone gives no derivative at
the coalescence. The following heat control realizes its
singularity with \(T_2\ne0\).

## 5. Exact double check and premise screen

In the real-even quartic heat class take a parameter \(b>0\) and
\[
 F(\tau,z)=(z^2-b^2)^2-\tau(12z^2-4b^2)+12\tau^2 .
\]
The equation \(F_\tau=-F_{zz}\) holds directly. Select the two
occurrences near \(+b\); reflection gives the exterior pair with
center \(-c\) and the same discriminant \(D\). At \(\tau=0\), the
singular coefficients of \(F_\tau/F\) about \(+b\) are
\(-2(z-b)^{-2}-(4/b)(z-b)^{-1}\). Comparing to the derivative of
the target factor gives \(D'(0)=2,\ c'(0)=2/b\), independently
of (1). Set \(u_0=-2b\); the exterior displacements are
\(\bar w\pm s\) with \(\bar w=-2c\) and \(\bar w'(0)=8/u_0\).
The analytic trace of a weight \(f(w,D)\) over this pair is
\(2f(\bar w,D)+D f_{ww}(\bar w,D)+O(D^2)\), by the even Taylor
sum. Its derivative at the double is
\(2\bar w' f_w+2D' f_D+D'f_{ww}\) at \((u_0,0)\). For the even
and odd weights this gives respectively
\[
 S_n'(0)=8n(n-3)u_0^{-2n-2},\qquad
 T_n'(0)=8(n^2-4n+2)u_0^{-2n-1}.
\]
Substituting \(S_r=2u_0^{-2r}\), \(T_r=2u_0^{1-2r}\), \(D=0\)
in (1) gives the same coefficients at every allowed index.
In particular \(T_2(0)=2u_0^{-3}\ne0\). Since \(D'(0)=2\), the
individual \(P_{2,0}\) above has a nonzero square-root term
on either label choice for \(\tau>0\), hence no finite derivative
through this double in the exhibited polynomial class.

This replay uses the inherited [Controls12][controls] screen,
[CM E04 §5][cmreview] and [GR E05][graudit]. Quadratic and quartic
heat controls lack canonical growing counts and can satisfy
(1) through a collision, as tested above. Euler translates
change theta arithmetic and the canonical projected discrepancy;
a coarse upper count can survive. Weighted-square, finite-source,
finite-score and finite-prime controls lose full reflected
unit-weight theta equality, and the documented endpoint-defective
subclasses also fail the fixed strip. The reflected super-Gaussian
fails the order-at-most-one product input. Smooth and
positive-primitive controls change theta arithmetic and have
unpaid strip/count transfer. Atomic and finite-profile controls
lack canonical population growth and full profile. RH-conditional
endpoint mergers change ordinary Dirichlet arithmetic and retain
RH as a premise. Observation changes lose the physical cosine
readout and fractional profiles lack integer occurrences. The
changed static slices lack the unchanged canonical common-time
tube and the scalar equilibrium lacks a divisor. The proof uses
heat evolution and a counted divisor with strict clearance, plus
the complete canonical convergence inputs for the infinite limit.
It claims no collision exclusion or improved signed forcing.
[Premises02][premises] · [Scope07][scope] · [Joint bounds12][joint]

[request]: ../research-progress/handoffs/VCD-GT-CM-E10-r1.md
[decision]: ../brainstorm/notes/04_VCD_GT_CM_B04_SPLIT_POLE_CLOSURE_CONTRACT_20261118.md
[e02]: 03_VCD_GT_CM_E02_COMPLEX_POWER_TIME_LAW_20261117.md
[cmreview]: ../reviews/03_VCD_GT_CM_E04_CONTOUR_PROOFS_ASSESSMENT_20261117.md
[parent]: ../../notes/41_VCD_GT_E21_EXACT_INTERACTION_RICCATI_BOUND_20261117.md
[grproof]: ../../01_gaussian_resolvent_hierarchy/notes/02_VCD_GT_GR_E02_CANONICAL_MOMENTS_20261117.md
[graudit]: ../../01_gaussian_resolvent_hierarchy/reviews/03_VCD_GT_GR_E05_INITIAL_PROOFS_ASSESSMENT_20261117.md
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md

