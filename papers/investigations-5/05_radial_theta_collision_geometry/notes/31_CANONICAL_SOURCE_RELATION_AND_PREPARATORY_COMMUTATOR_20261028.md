# The fixed canonical source relation and its preparatory commutator

28 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, Investigation05 chat0010, **Continue radial theta collision**.

**Task:** the second bounded **[B] CTF-B02** route, selected before analysis in [Progress04][progress], following [Continuation30][previous]. Keep Note28's equation, complete theta source, mandatory preparatory smoothing and actual marked spectral derivatives. Test one fixed logarithmic-source relation for its use in gradient production.

**Result — proved in-note, with same-assistant checks:** the raw canonical density satisfies an exact first-order radial/spectral relation. The required heat preparation creates a nonzero residual on the unit sphere, with explicit positive lower bounds for a nonempty frequency interval at every real physical time. Its later equation has a nonzero second-order commutator forcing. Dropping the residual creates a false infinite gradient at the sphere, although the actual prepared field is smooth. Extending the canonical coefficient unchanged to the origin creates a separate unweighted L2 domain failure.

**Disposition:** the variant that carries this *fixed relation with zero residual* into Note28's gradient calculation is stopped. This is not an obstruction to estimates retaining the residual, other source relations, weighted domains or time-dependent operators. Broader B02 remains partial. No new physical collision exclusion, threshold bound or numerical acquisition request follows.

The logarithmic-derivative construction is already present, in a different transfer system, in [Note01, Section6][n01]. Its generic availability for positive sources is not new arithmetic information. The new work here is the exact failure of its proposed unchanged propagation in the fixed conservative candidate.

## 1. Frozen data and the source relation

Fix the mark p=(T,A), with T real and A>=0 the **physical frequency**. A is not the squared spectral variable lambda=a²/4 used in parts of the manuscript. Set
\[
 r=|X|,\qquad u=\tfrac12\log r,\qquad q_T(u)=e^{Tu^2}\Phi(u),
\]
\[
 Q_T(r)=4\pi e^{T(\log r)^2/4}
 \sum_{n\ge1}n^2(2\pi n^2r^2-3)e^{-\pi n^2r^2},
 \qquad
 \rho_T(r)=\frac{Q_T(r)}{32\pi\sqrt r}
          =\frac{q_T(u)}{8\pi r^3}.
 \tag{1}
\]
On r>=1 every displayed square term is positive; the sum is complete and every square coefficient remains one. Write ell_T=log rho_T there. All derivatives and moments used below exist by the canonical tails.

Use F_j for the raw physical-frequency derivatives at A:
\[
 F_0=\mathbf1_{r\ge1}\rho_T(r)\cos(Au),\quad
 F_1=-\mathbf1_{r\ge1}u\rho_T(r)\sin(Au),\quad
 F_2=-\mathbf1_{r\ge1}u^2\rho_T(r)\cos(Au).
 \tag{2}
\]
Their preparation is K1 convolution, where
\[
 K_\delta(X)=(4\pi\delta)^{-3/2}e^{-|X|^2/(4\delta)}.
\]
Note28 evolves W=(U,V), with U0=K1*F0 and V0=K1*F1, by
\[
 \partial_sW=L_sW,\qquad
 L_s=\Delta+\alpha(s)(v\cdot\nabla+d),\qquad
 v=X+\frac{X}{1+r^2},\quad d=\operatorname{div}v,
 \qquad \alpha=2G/D.
 \tag{3}
\]
Here E=||W||²=E0>0, G=||grad W||² and D=int d|W|². All spatial integrals without further qualification are over R³. We use only the smooth weighted solution on compact subintervals of its lifespan established in [Note28][n28].

On the exterior, define the **fixed** source operator
\[
 \mathcal A_T=a(r)(\partial_r-\ell_T'(r)),
 \qquad a(r)=r\log r.
 \tag{4}
\]
Since a/(2r)=u, direct differentiation gives
\[
 \boxed{\mathcal A_TF_0=A F_1,\qquad
        \mathcal A_TF_1=F_1+A F_2.}
 \tag{5}
\]
The second equality is the actual frequency derivative of the first. It does not close on F0,F1.

These equalities also hold distributionally across r=1 for a smooth whole-space extension of the operator: the only jump of F0 contributes its surface delta multiplied by the normal coefficient a(1)=0. The higher derivatives in (2) vanish at the sphere. No surface delta was dropped.

To make that extension explicit, use full canonical reflection to extend rho_T positively to r>0, as in Section6. Choose a smooth cutoff eta with eta=0 for r<=1/2 and eta=1 for r>=3/4, and put
\[
 b(X)=\eta(r)\log r\,X,\qquad
 c_T(r)=-\eta(r)r\log r\,\ell_T'(r),\qquad
 \mathcal A_T=b\cdot\nabla+c_T.
 \tag{6}
\]
For example eta(r)=h(4r-2), where h(t)=0 for t<=0, h(t)=1 for t>=1, and
h(t)=e^{-1/t}/(e^{-1/t}+e^{-1/(1-t)}) for 0<t<1.
This defines smooth coefficients at the origin and preserves (4) on r>=3/4. The transition terms are retained in the commutator below. The extension defines a comparison operator; it changes neither the source nor the PDE. At infinity its coefficients and derivatives have at most polynomial growth, with logarithmic factors.

## 2. Mandatory preparation produces an explicit residual

For a raw density f, integration by parts in the sense of distributions gives the exact heat commutator
\[
\begin{split}
 [\mathcal A_T,K_\delta*]f(X)
  =\int_{\mathbb R^3}\big\{&
   (b(X)-b(Y))\cdot\nabla_XK_\delta(X-Y)\\
   &+[c_T(X)-c_T(Y)+\operatorname{div}b(Y)]
           K_\delta(X-Y)\big\}f(Y)\,dY.
\end{split}
 \tag{7}
\]
In particular the div b term has a plus sign. The distributional identity (5) already accounts for the raw unit-sphere jump.

Let J2,s be the **actual second running-frequency derivative** of the common marked propagator:
\[
 J_{2,s}
 =\left.\partial_a^2j_s^p(T,a)\right|_{a=A},\qquad
 J_{2,0}=K_1*F_2,\qquad \partial_sJ_2=L_sJ_2.
 \tag{8}
\]
The mark p and its alpha path are held fixed when differentiating the running a. Therefore (8) has no alpha_a term. Derivatives of the mark itself have the extra response terms recorded in Note28 and are not substituted here. In general J2,s is not -u²Us.

Define
\[
 \mathcal T_s=(A V_s,\ V_s+A J_{2,s}),\qquad
 \mathcal R_s=\mathcal A_TW_s-\mathcal T_s.
 \tag{9}
\]
By (5),
\[
 \mathcal R_0=
 ([\mathcal A_T,K_1*]F_0,\ [\mathcal A_T,K_1*]F_1).
 \tag{10}
\]
At every unit vector X1, b(X1)=c_T(1)=0. Hence, at every auxiliary time in the smooth lifespan,
\[
 \boxed{\mathcal R_s(1)=
       (-A V_s(1),\ -V_s(1)-A J_{2,s}(1)).}
 \tag{11}
\]
The trace is radial. Equation (11) is independent of the chosen inner extension.

### A quantitative nonzero defect for the actual theta data

For fixed T define positive finite numbers
\[
 L_j(T)=\int_{|Y|\ge1}K_1(X_1-Y)\rho_T(|Y|)u(Y)^j\,dY
 \quad(j=2,4).
 \tag{12}
\]
These are direct complete-theta scalar integrals, not fitted constants. Spherical averaging gives the equivalent one-dimensional formula
\[
 L_j(T)=\int_0^\infty q_T(u)u^j k(e^{2u})\,du,\qquad
 k(r)=(4\pi)^{-3/2}e^{-(1+r^2)/4}
                         \frac{\sinh(r/2)}{r/2}.
 \tag{13}
\]
Both L2 and L4 are strictly positive.

Substitute (2) into (11). The elementary inequalities
|sin x-x|<=|x|³/6 and |cos x-1|<=x²/2 imply
\[
 \left|\mathcal R_{U,0}(1)-A^2L_2\right|
       \le\frac{A^4L_4}{6},
 \qquad
 \left|\mathcal R_{V,0}(1)-2A L_2\right|
       \le\frac23A^3L_4.
 \tag{14}
\]
The first component is A int K1 rho_T u sin(Au); the second is
int K1 rho_T [u sin(Au)+A u²cos(Au)]. This also checks their signs.

Consequently, for every fixed real T,
\[
 \boxed{0<A^2\le\frac{3L_2(T)}{2L_4(T)}
 \quad\Longrightarrow\quad
 \mathcal R_{U,0}(1)\ge\tfrac34A^2L_2>0,\quad
 \mathcal R_{V,0}(1)\ge A L_2>0.}
 \tag{15}
\]
This proves failure for the actual canonical source already after the required preparation, at ordinary small frequencies. It is not inferred only from a different source's control.

For fixed T the first component in (14) is an entire even function of A: the complete theta tail dominates e^{C u} on every compact complex-frequency set. Its quadratic coefficient L2 is nonzero. Its positive real zeros are therefore isolated. Thus this particular boundary defect is nonzero except possibly at a discrete set of positive frequencies, and the zero-residual relation cannot hold on any open frequency interval. We have not determined the defect at a hypothetical event among those exceptional frequencies. This argument does not rule out an event-conditioned estimate.

## 3. The exact residual evolution

Because the same L_s acts on U,V,J2 and A is fixed,
\[
 \boxed{\partial_s\mathcal R_s
  =L_s\mathcal R_s+[\mathcal A_T,L_s]W_s.}
 \tag{16}
\]
With repeated spatial indices summed and c=c_T,
\[
\begin{split}
 [\mathcal A_T,L_s]={}&
 -2(\partial_j b_i)\partial_{ij}
 -(\Delta b+2\nabla c)\cdot\nabla-\Delta c\\
 &+\alpha\big\{
 (b\cdot\nabla v-v\cdot\nabla b)\cdot\nabla
       +b\cdot\nabla d-v\cdot\nabla c\big\}.
\end{split}
 \tag{17}
\]
The terms -Delta c, b.grad d and -v.grad c are multiplication operators. No derivative of alpha appears: this is a spatial commutator, not a mark derivative. Formula (17) includes the derivatives of eta in the inner transition region.

For r>=1,
\[
 \partial_jb_i=\log r\,\delta_{ij}+\frac{X_iX_j}{r^2},
 \qquad \Delta b=\frac{3X}{r^2}.
\]
Its second-order part is therefore
\[
 -2\big((\log r)\Delta+\partial_{rr}\big).
 \tag{18}
\]
On radial functions it equals
-2[(1+log r)partial_rr+(2log r/r)partial_r].
Writing v=lambda(r)X, with lambda=1+1/(1+r²), its first-order Lie coefficient is
\[
 b\cdot\nabla v-v\cdot\nabla b
       =(r\lambda'(r)\log r-\lambda(r))X,
 \qquad \lambda'=-2r/(1+r^2)^2.
 \tag{19}
\]
In particular the forcing is not removed by choosing the source's exact logarithmic derivative: the Hessian term (18) is already nonzero.

If P_{s,q} denotes the common propagator along the fixed mark, the exact inhomogeneous representation is
\[
 \mathcal R_s=P_{s,0}\mathcal R_0+
       \int_0^sP_{s,q}[\mathcal A_T,L_q]W_q\,dq.
 \tag{20}
\]
On compact lifespan intervals the weighted smoothness permits these operations. Neither (17) nor (20) supplies a sign or a smallness estimate for the signed vector forcing. Estimating it consumes second spatial derivatives and source-coefficient weights. The negative Laplacian term in gradient production might help in a *coupled* estimate; no impossibility of that procedure is asserted.

## 4. Why the residual cannot be discarded in the gradient consumer

The consumer fixed by Continuation30 is
\[
 G'=-2N+\frac{2G}{D}\mathcal K,\qquad
 N=\|\Delta W\|_2^2,
 \tag{21}
\]
\[
 \mathcal K=
 2\sum_{\ell=1}^2\int\nabla W_\ell^{\,T}Dv\,\nabla W_\ell
 +\int d|\nabla W|^2-\int(\Delta d)|W|^2.
\]
For r>1, (9) gives the exact identity
\[
 \partial_rW=\ell_T'W+\frac{\mathcal T+\mathcal R}{r\log r},
\]
and radiality yields
\[
 G=4\pi\int_0^1r^2|\partial_rW|^2\,dr+
   4\pi\int_1^\infty r^2
       \left|\ell_T'W+\frac{\mathcal T+\mathcal R}{r\log r}\right|^2\,dr.
 \tag{22}
\]
The whole unit ball remains part of the evolution and of G.

By (11), (mathcal T+mathcal R)(1)=0; smoothness makes this numerator O(r-1) at the sphere. This cancellation keeps (22) finite. On the nonempty interval (15), however,
\[
 \mathcal T_{U,0}(1)=A V_0(1)
             =-\mathcal R_{U,0}(1)\ne0.
\]
Since r log r~r-1, setting mathcal R=0 in (22) would make its first-component exterior integral diverge like int_1^{1+epsilon}(r-1)^(-2)dr. The actual U0,V0 are Schwartz and their gradient energy is finite.

Thus this apparent infinite gradient would be an artifact of omitting the preparation residual, **not** collision amplification. No bound using that replacement is admissible. Separately bounding T/(r log r) and R/(r log r) by ordinary squared norms would also lose a cancellation required for finiteness on (15). A valid estimate must retain their joint boundary behavior, control the actual second spectral derivative, and retain the inner-ball contribution.

This establishes the precise failure of the selected zero-residual substitution. It does not establish that all signed estimates of (21), including ones exploiting cancellations, fail.

## 5. What is and is not specific to the canonical source

The fixed coefficient ell_T' in (4) uses the unchanged **complete** theta sum in (1). For a different positive smooth exterior amplitude rho_* and its own raw F_{*,0},F_{*,1},
\[
 \mathcal A_TF_{*,0}-A F_{*,1}
  =\mathbf1_{r\ge1}\,r\log r\,\rho_*(r)
       \big((\log\rho_*)'(r)-\ell_T'(r)\big)\cos(Au).
 \tag{23}
\]
For any fixed A>=0, (23) vanishes identically on r>1 if and only if
rho_*=C rho_T there. For A>0 the cosine zeros are isolated; continuity fills them in. For A=0 there are no cosine zeros. Normalization fixes C when required.

Accordingly this *literal fixed-coefficient premise* identifies the full source up to scale. That distinction alone proves no estimate along its evolved signed fields. If each positive control is instead assigned its own logarithmic derivative, it satisfies (5) by the same elementary calculation and has the same type of smoothing and evolution defects. Renaming its coefficient as canonical would erase the tested premise.

The [registered control screen][controls] gives the following disposition.

| Control | Premise it fails when (4) is frozen to theta | What still applies |
| --- | --- | --- |
| Exact Gaussian-polynomial source from Notes01,25,28 | Its exterior logarithmic derivative is not ell_T'; its tail in log r is different | Its own source operator obeys (5), (7), (11), (14) and (16); the conservative flow still reaches its proved collision deadline |
| Weighted-square and finite-prime-orbit controls | Their changed square coefficients do not give the complete unit-weight amplitude in (1); endpoint or selected-prime identities do not imply (23)=0 | Positivity, moments and their own logarithmic-source identities do not prevent their recorded events |
| Fully reflected super-Gaussian, smooth shape, positive-primitive and RH-conditional normalized endpoint controls | Full reflection, strong shape or selected primitive data do not make the exterior source a constant multiple of the complete theta source; the recorded controls fail that fixed coefficient premise | Full reflection by itself does not propagate the operator through spatial heat |
| Euler-factor controls | The shifted, conductor-changed source is not the fixed theta amplitude and hence fails (23)=0 | Generic source calculus and conservative propagation remain available |
| Atomic finite-profile controls | They are outside the positive smooth amplitude/logarithmic-derivative formulation | Their existing screening scope is retained; no unjustified application of (4) is made |
| Continuous compact extension of finite-profile controls | It is not the strictly positive complete exterior theta amplitude | Smoothing alone is still not a canonical separating premise |

For the first row the source and exact event are
\[
 \Phi_*(u)=(64u^4+6)e^{-(4+T_c)u^2},\quad T_c=\tfrac14,
 \qquad
 H_*(T_c,a)=\frac{\sqrt\pi}{16}(a^2/4-6)^2e^{-a^2/16},
 \quad A_*=2\sqrt6.
 \tag{24}
\]
Its own version of the raw first-order relation is exact, including at A*. Note28's finite breakdown theorem applies; no relation stated here forbids that event. We do not assert that its boundary residual is nonzero at A* without evaluating it. That is unnecessary: the source-wise relation alone is compatible with the known collision, and the nonzero canonical preparation defect was proved directly in (15).

## 6. The uncut canonical operator has an origin domain problem

The inner extension in (6) is necessary for the stated whole-space smooth-operator calculation. The full source reflection in the radial representation is
\[
 Q_T(r)=r^{-5}Q_T(1/r),\qquad
 \rho_T(r)=r^{-6}\rho_T(1/r).
 \tag{25}
\]
It uses the complete canonical identity, not just a finite list of endpoint derivatives. Since the exterior source is positive, it also defines a positive extension to r>0.

The first square term of the unchanged complete series, with the remaining tail bounded by Gaussian decay, gives
\[
 \rho_T(r)=\frac{\pi}{4}r^{3/2}
 e^{-\pi r^2+(T/4)(\log r)^2}
 \left(1-\frac{3}{2\pi r^2}+O(e^{-3\pi r^2})\right)
 \quad(r\to\infty).
 \tag{26}
\]
The exponentially small remainder may be differentiated with polynomial losses. Apply (25):
\[
 \rho_T(r)=\frac{\pi}{4}r^{-15/2}
 e^{-\pi/r^2+(T/4)(\log r)^2}
 \left(1-\frac{3r^2}{2\pi}+O(e^{-3\pi/r^2})\right)
 \quad(r\downarrow0).
\]
It follows that
\[
 \ell_T'(r)=\frac{2\pi}{r^3}-\frac{15}{2r}
              +\frac{T\log r}{2r}+O(r),
\]
\[
 c_T^{\rm uncut}(r)
 =-\frac{2\pi\log r}{r^2}+\frac{15}{2}\log r
               -\frac{T}{2}(\log r)^2+O(r^2\log r).
 \tag{27}
\]
A smooth radial prepared field satisfies U0(r)=U0(0)+O(r²). If U0(0) is nonzero, the uncut operator therefore has
\[
 \mathcal A_T^{\rm uncut}U_0(r)
   =-\frac{2\pi U_0(0)\log r}{r^2}
       +O((\log r)^2),
 \tag{28}
\]
whose square is not integrable against 4pi r²dr at zero.

This occurs for actual canonical data on an explicit nonempty frequency interval. Define
\[
 O_j(T)=(4\pi)^{-3/2}\int_0^\infty
                q_T(u)u^j e^{-e^{4u}/4}\,du,\qquad j=0,2.
\]
Both are finite and positive. Since cos x>=1-x²/2,
\[
 U_0(0;A)\ge O_0-\frac{A^2O_2}{2}
       \ge\frac{O_0}{2}>0
       \quad\hbox{if }A^2\le O_0/O_2.
 \tag{29}
\]
The smoothed V0 and J2,0 have finite values at zero and cannot cancel the leading singularity in the first component of the uncut residual.

Equations (27)–(29) exclude an uncut unweighted-L2 operator-energy argument on these prepared data. They do not exclude subtraction, different weights or admissible domains. The smooth extension (6) repairs that domain issue, but all its transition terms and the actual inner-ball energy must then be retained. No claim is made that the L2 energy itself concentrates at the origin merely from Note29's carrier-moment collapse.

## 7. Matched information, decision and remaining estimate

The fixed logarithmic derivative stores the entire source. Its raw relation is an exact re-expression of (1), just as the earlier transfer construction in Note01 is generic. The preparation and origin constants in (12), (13) and (29) are direct scalar weighted theta integrals. Their strict positivity already proves the stated failures; computing decimal values would not decide a new collision exclusion.

The directly obtained outputs of this bounded route are:

1. The explicit actual-theta preparation bounds (14)–(15).
2. The complete residual equation (16)–(20), including second spatial derivatives and the actual second running-frequency jet.
3. The finite-gradient boundary cancellation in (22), and the false singularity if that cancellation is removed.
4. The uncut origin domain failure (27)–(29).
5. The exact fixed-source comparison (23) and control dispositions.

No new sign for mathcal K or ND-G mathcal K has been proved. No regularity bound through the collision deadline, positive first-jet floor, enlarged theta domain or cost advantage was acquired. This is a **scoped failed propagation/substitution result**, not a new RH criterion or a universal no-go theorem; see [target classification][a01] and [scope discipline][a07].

**Stop this variant.** Any next B02 attempt using this source operator must begin with a coupled estimate for W, its true second spectral derivative and the nonzero residual, including the sphere cancellation, the commutator's second-order terms and the whole evolving unit ball. It must choose an origin-admissible functional and obtain additional signed theta information rather than impose mathcal R=0. Alternatively another source relation would require a separately declared bounded conceptual choice. Neither choice is executed in this note.

E03 remains gated: no finite numerical quantity has been identified whose acquisition would settle a new estimate. E02's existing saved-data audit remains optional and unchanged. The established statements are eligible for optional E04 manuscript integration after their same-assistant scope is recorded. See [assessment18][review] and [Continuation32][continuation]. No manuscript edit or snapshot, numerical run, independent specialist review or milestone is claimed.

[n01]: 01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md
[n28]: 28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md
[previous]: 30_CONSERVATIVE_CARRIER_COMPARISON_CONTINUATION_20261028.md
[progress]: ../research-progress/04_CONSERVATIVE_THETA_FLOW_RESEARCH_PROGRESS_20261028.md
[review]: ../reviews/18_CANONICAL_SOURCE_RELATION_PROPAGATION_ASSESSMENT_20261028.md
[continuation]: 32_SOURCE_RELATION_COMMUTATOR_CONTINUATION_20261028.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
