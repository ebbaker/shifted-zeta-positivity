# A spatial join inside a zero-free gap: exact defects and local allowances

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **gpt-6-astra (Codex), actual effort xhigh**,
verified from turn metadata. Chat 0014, thread
`01a17115-c0a2-7571-97ce-9ed35f9f41ee`.

**Status: nonholomorphic identities and local transition estimates proved
in-note; same-assistant checking only.** This is the selected analytical
return to [HDA-18-A01 r1](../research-progress/handoffs/HDA-18-A01.md).
It supplies a smooth spatial construction and explicit defect envelopes
on its transition bands. It does **not** yet supply the complete
full-filter-support comparison, an effective core, or an all-time join.
The next bounded task is [HDA-18-AN01 r1](../research-progress/handoffs/HDA-18-AN01.md).

The gain is to support the nonholomorphic terms in a **zero-free gap of
the explicit outer model**. There the denominator is paid by the field,
rather than a lower bound for the shrinking regulator. The support has
width O(1/log X), and the new filtered spatial defects tend to zero with
the available outer field error. This is an approximation estimate under
[avoid 01](../../../../avoid/01_restating_the_target.md), not an RH criterion.
See the [result index](../../../../result-summaries/README.md),
[heat-flow cluster](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[control register](../../../../result-summaries/12_collision_controls_and_screening.md),
and [avoid index](../../../../avoid/README.md), particularly
[scope](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and
[cancellation](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

## 1. Fixed contract and the bounded domain

Keep the canonical H, H_t=-H_zz, H(0,z)=xi((1+iz)/2)/8, the physical
q=epsilon_g^2, eta>0, and the fixed kernel K=k_ell k_h. No harmonic
offset, mass normalization, changed regulator or new source is introduced.
The approximation below need not be holomorphic. Its density and current
are explicitly defined using its **actual Wirtinger derivatives**; no
holomorphic identities are assumed for it.

Fix t0>64 and a compact J=[t0-delta,t0+delta] contained in (64,infinity).
For example t0=96 and delta=1 specify a regime, not a certified onset.
Fix |y|<=Y for observations and Y_b=Y+h+2 for all analytic work.
Let P be the full saddle of Notes 30–31, on its established exterior
branch. Take a large positive model gap center X with
Theta_*(t0,X)=n*pi, and put L=log(2+X).

Here is a finite geometric gate, rather than an implicit appeal to a gap:
choose sigma=c/L such that the closed vertical band

    |x-X|<=2 sigma, |y|<=Y_b

stays a fixed scaled distance from all of P's enlarged root collars.
Require on that band and a neighborhood, throughout I,

    |P| >= c0 A,        A=|S_t((1+iz)/2)|+|S_t((1-iz)/2)|,
    |partial_z^j P| <= C_j L^j A,               0<=j<=3.       (GS1)

The A here is a carrier sum, not |P|. Notes 30 FS22 and 31 PE9–PE11
give this gate eventually: phase spacing is comparable to 1/L; the
real part of the phase changes by O(Y_b^2/X) on the vertical strip;
the two carrier arms give |cos Theta|/cosh(Im Theta) bounded below
between the collars. The outer roots have bounded speed V on J.
Shrinking to the **fixed** slab

    I=[t0-tau,t0+tau],
    0<tau<=min(delta, c_gap/((V+1)L))                         (GS2)

preserves a band with a positive collar margin. Constants c,c_gap are
chosen below the available phase-gap margins. A fixed-width time slab
independent of X is not claimed: this elementary fixed-band construction
has tau=O(1/L). A moving band is a subsequent task.

Include the reflected band at -X. Supply all field and source estimates
on the full rectangle I x {|x|<=X+ell+2 sigma+2, |y|<=Y_b}, with
an open analytic neighborhood. Extend it if the actual collar disks need
more room. Observation supports meeting a band must include their whole
ell,h buffers, including every intersecting collar. No estimate restricted
to the band alone is a complete convolution comparison.

Choose a single time-independent positive finite source, with entire
exact-heat field G=H_f. On the two band neighborhoods require

    |partial_z^j(G-P)| <= mu L^j A,             0<=j<=3,
    |E_P|<=d A, |(E_P)_z|<=C d L A, E_P=P_t+P_zz.           (GS3)

Also require |partial_z^j(H-P)|<=mu L^j A on these neighborhoods.
Constants can be absorbed into mu. Notes 30–31 supply this H-P part
with mu=O_J(X^-2), d=O_J(X^-3). It is sufficient to make the
finite-source errors against H at most X^-2 L^j times the minimum
carrier on the relevant compact buffer. That minimum is positive.
Notes 20/37 give existence of such finite source accuracy; they do not
give an accepted mesh, affordable complexity or certified constants here.
Accuracy on the remaining core is an additional HDA-17 input.

## 2. The actual joined field and its two defects

Let lambda(x) be smooth, real, zero inside the two bands, one outside,
and transition monotonically on each [X-sigma,X+sigma] and its reflection.
It is constant on neighborhoods of the band endpoints. Use an even lambda
and let l_k bound |lambda^(k)|, k=1,2,3; l_k=C_k sigma^-k.
Write D0=P-G only where P is defined. Define

    F=G                 on the inner region,
    F=G+lambda D0       on the bands,
    F=P                 on the exterior.                         (GS4)

Flat cutoffs make this a smooth field on the full horizontal strip, C1
in time with the needed mixed derivatives. P is never evaluated in its
unproved central domain. The real/even symmetries are retained.
Set B=F_bar_z and E=F_t+F_zz. On a band, exactly,

    B=lambda' D0/2,
    B_z=lambda'' D0/4+lambda' (D0)_z/2,
    B_bar_z=lambda'' D0/4,
    B_zz=lambda''' D0/8+lambda'' (D0)_z/2
                              +lambda' (D0)_zz/2,
    E=lambda E_P+lambda' (D0)_z+lambda'' D0/4.              (GS5)

Outside the bands B=0 and E is respectively 0 or E_P. The absence of
lambda_t is a property of this fixed-band construction. It cannot be
carried to a moving band without adding lambda_t D0.

Require mu<=c0/2. Then |F-P|<=mu A and hence

    |F|>=c0 A/2                                             (GS6)

throughout the bands, even though q can be arbitrarily small there.
This premise, not positivity of q alone, pays the following estimates.

## 3. Exact equations for a nonholomorphic field

These identities hold for any sufficiently smooth F and q=q(t,x)>0.
Put a=F_z, c=F_zz, D=|F|^2+q, S=log D, w=q/D, r=log q, and

    rho=q|a|^2/(pi D^2),   j=q c conjugate(a)/(pi D^2),
    V_m=w^m c conjugate(F)/D, Z=E conjugate(F)/D,
    C_reg=[2 grad w dot grad r+w Delta r-w(1-w)|grad r|^2]/(4pi),
    b=r_t+(r_xx+r_x^2)/2,  mathcal B=bw,
    mathcal S=(1-2w)(r_t rho+grad r dot (Re j,Im j)).        (GS7)

The regulator curvature and the new compatibility curvature are separate:

    T_C= q|B|^2/(pi D^2)
         +(2/pi) Re(B_z conjugate(F)/D-a B conjugate(F)^2/D^2),
    C_tot=C_reg+T_C,
    Xi=8 Re(a conjugate(B)/D)+4 Re(F conjugate(B_bar_z)/D),
    T_J=-B_zz conjugate(F)/D+c B conjugate(F)^2/D^2.          (GS8)

Direct differentiation gives

    Delta S=4pi(rho+C_tot),
    pi j=partial_bar_z V_0+(partial_bar_z r)V_1+T_J,
    S_x^2-S_y^2=4 Re V_0-square S+(r_xx+r_x^2)w+Xi,
    S_t=-2 Re V_0+r_t w+2 Re Z,                            (GS9)

where square=partial_x^2-partial_y^2. For example
D_z=a conjugate(F)+F conjugate(B)+q_z and
D_zbar=|a|^2+|B|^2+2 Re(B_z conjugate(F))+q_zbar prove
the first identity. Differentiating V_0 proves the second. The equality
square D=4 Re(c conjugate(F))+8 Re(a conjugate(B))
+4 Re(F conjugate(B_bar_z))+q_xx proves the third. No heat equation
or vanishing B is used in these three calculations.

Define U=K*S, R=K*rho, J=K*j and **the actual covariance**

    Q=K*(S_x^2-S_y^2)-(U_x^2-U_y^2).                     (GS10)

It is neither the average of component covariances nor an equation-defined
unknown. Put T_U=Xi/2+2 Re Z. The full potential and density equations are

    U_t=-1/2(square U+U_x^2-U_y^2+Q)+K*mathcal B+K*T_U,
    Delta U=4pi(R+K*C_tot),
    R_t=-1/2 square R-Delta(U_x^2-U_y^2+Q)/(8pi)
        +Delta(K*mathcal B)/(4pi)
        -K*(C_tot)_t-1/2 square(K*C_tot)+Delta(K*T_U)/(4pi).
                                                               (GS11)

Both curvature derivatives remain; Xi/2 is an additional potential defect.
For current balance, direct differentiation instead gives

    rho_t+div j=mathcal S+D_E+D_B,
    D_E=2q Re(E_z conjugate(a))/(pi D^2)-4rho Re Z,
    D_B=2q Re(c conjugate(B_z))/(pi D^2)
            -4q Re(F conjugate(B)c conjugate(a))/(pi D^3).
                                                               (GS12)

Here div j means div(Re j,Im j). To check GS12, use
div j=2 Re(partial_z j), a_t=-c_z+E_z, and
S_z=(a conjugate(F)+F conjugate(B))/D+w r_z.
The c_z terms cancel, followed by the a conjugate(F) terms. The remaining
two B terms are exactly D_B. Thus the filtered equation is
R_t+div J=K*mathcal S+K*(D_E+D_B).

These equations have a fixed source anchor and actual boundary traces:
F equals the source-defined G on the inner side and the specified P on
the outer side, with smooth matching at both band edges. No independent
boundary values are prescribed to force the equations. This generalized
rho is an approximation observable; no zero-count interpretation for a
nonholomorphic field is asserted.

## 4. Explicit local allowances without an inverse regulator floor

All ratios in this section are taken **only where GS6 holds**. Put

    A1=|a|/|F|, A2=|c|/|F|, b0=|B|/|F|,
    b1=|B_z|/|F|, bb=|B_bar_z|/|F|, b2=|B_zz|/|F|,
    e0=|E|/|F|, e1=|E_z|/|F|,
    gamma=q/|F|^2, theta=gamma/(1+gamma)^2 <=1/4.

The following are directly evaluable positive envelopes, with the actual
physical q inside gamma:

    pi |T_C| <= theta b0^2+2b1+2 A1 b0,
    |Xi| <=8 A1 b0+4bb,
    |T_J| <=b2+A2 b0,
    |T_U| <=4 A1 b0+2bb+2e0,
    pi |D_B| <=2theta A2 b1+4theta A2 A1 b0/(1+gamma),
    pi |D_E| <=2theta e1 A1+4theta A1^2 e0/(1+gamma).      (GS13)

They follow term by term from GS8/GS12 using D=|F|^2(1+gamma).
There is no epsilon_g^-1. Keeping theta, rather than replacing it by
1/4, is useful for the current defects after the switch.

The time derivative of the new curvature is also paid explicitly.
Let v=|F_t|/|F|, a_t^*=|a_t|/|F|, b_t^*=|B_t|/|F|,
h_t^*=|(B_z)_t|/|F|, and k=2v+|r_t|w. Then |D_t|/D<=k and

    pi |(T_C)_t| <=
      theta[(|r_t|+2k)b0^2+2b0 b_t^*]
      +2[h_t^*+(v+k)b1+a_t^* b0+A1 b_t^*
                                      +2(v+k)A1 b0].       (GS14)

Differentiate the three terms of GS8 before taking magnitudes. In
particular the q derivative contributes |r_t| theta b0^2; it is not
discarded. This formula does not differentiate an error allowance.

For any new defect T supported on the band set Sigma, the full filtering
payment is, at every observation center p,

    |partial^alpha K*T(p)|
       <= integral_Sigma |K_alpha(p-u)| E_T(u) du.          (GS15)

Use GS13 or GS14 for E_T. One may bound this by
||K_alpha||_infinity |Sigma intersect supp K(p-.)| sup E_T.
The intersected planar area is at most 8h sigma for two bands (at most
4h sigma for one). Use Delta K or square K for the corresponding terms
in GS11. Through spatial order two this requires kernel derivatives
through four only. The same estimates cover fixed boundary traces;
normal derivatives use their component sums. These are explicit allowances,
not merely a claim that a Lipschitz constant exists.

## 5. The size of the new terms on the stated slab

From GS3–GS6 and l_k=O(L^k), for mu<=c0/2 and d<=C mu,

    A1=O(L), A2=O(L^2),
    b0=O(mu L), b1+bb=O(mu L^2), b2=O(mu L^3),
    e0=O(d+mu L^2), e1=O(d L+mu L^3).                   (GS16)

For the mixed derivatives use the exact identity
(D0)_t=-(D0)_zz+E_P and its z derivative. It gives
v=O(L^2), a_t^*=O(L^3), b_t^*=O(mu L^3),
h_t^*=O(mu L^4), with the d terms absorbed as indicated. No numerical
or symbolic differentiation of an asymptotic remainder is used.

On J contained in (64,infinity), beta has a positive lower bound.
The compact-time carrier formula has log A=-pi X/8+O_J(log^2 X)
on the fixed strip, with the fixed transverse logarithmic variation
absorbed into that allowance. Therefore GS6 implies on Sigma

    gamma <= C_J exp(-c_J X^2),
    |r_t|w+|r_t|theta <= C_J,
    |r_x|,|r_xx|,|r_t|,|r_tx|,|r_txx| <= C_J(1+X^2).    (GS17)

This is the key after-switch premise. It is not uniform as J approaches
64 and does not cover the moving crossover layer. Neither exponentially
small gamma nor its products are set equal to zero.

Combining GS13–GS17 gives the following **new transition costs**, for
all the kernel derivative orders required in GS11–GS12:

| New term | Pointwise on Sigma | Fixed-filter contribution |
| --- | --- | --- |
| T_C, Xi | C mu L^2 | C mu L |
| T_J | C mu L^3 | C mu L^2 |
| (T_C)_t | C mu L^4 | C mu L^3 |
| T_U on Sigma | C(d+mu L^2) | C(d/L+mu L) |
| D_B and D_E on Sigma | C exp(-cX^2)(mu L^4+d L^2) | C exp(-cX^2)(mu L^3+d L) |

**(GS18).** Fixed-kernel constants are given explicitly by GS15; the
constants in GS16–GS18 depend on the declared field/gap caps, cutoff,
J and buffers. Existing outer E_P terms beyond Sigma are **additional**
and retain Note 31's residual allowance. GS18 does not assert that all
of E is supported on Sigma.

For the attainable relative field budget mu=O_J(X^-2), all newly displayed
nonholomorphic costs tend to zero, with the largest listed allowance
O_J(log^3 X/X^2). This is an informative asymptotic defect estimate; no
numerical onset or efficient source complexity has been obtained.

One can also compare the *local* potential and actual gradient stress on
Sigma directly against H: the common field floor and the jet differences
give |S_F-S_H|<=C mu and
|grad S_F-grad S_H|<=C mu L under GS17. Both gradients are O(L),
so the signed stress difference is bounded by C mu L^2. These local
contributions obey GS15. For the covariance subtract the actual filtered
mean products only after integration; their difference uses the full
mean-gradient errors and caps, still to be assembled below. This is not
a comparison of Q based only on the local transition band.

## 6. The exact remaining consumer and stop

This construction removes the need to divide the **transition defects**
by a global regulator floor. It does not remove the theta comparison on
root collars or on the finite core. A complete filtered comparison must
combine three pieces on every support:

1. G-H on the inner part, with continuous finite-source allowances;
2. P-H on the outer part, with Notes 30–31's actual collar/pole estimates;
3. the band terms above, including T_C, (T_C)_t, Xi, T_J, D_E and D_B.

If tests are partitioned, all derivatives of the partition belong in
their norms. Whole-support theorems cannot simply be applied to truncated
integrals without paying those terms. On collars disjoint from Sigma the
field is holomorphic and equals one component. This suggests reusing
the analytic-unit and signed-pole arguments; it is not recorded here as
a completed proof for the piecewise field. In particular, GS18 plus a
small heat residual does not establish solution accuracy by propagation.

The next tractable deliverable is a single full-support transfer lemma
on GS2, with explicit partition costs, actual Q and all time/curvature
rows. Sol can then decide whether the required finite-source accuracy
and gap constants can be made informative at a finite X. Stop before
numerical theta execution if those requirements are uninstantiated.
Covering a fixed time interval by moving gaps, crossing t=64, joining
the negative endpoint and all-time coverage remain separate tasks.

The local result is a compatibility advance, not HDA-18 acceptance.
HDA-17 remains Partial, HDA-18 Gated and HDA-20 unfulfilled. The existing
manuscript and DRAFT_HISTORY are unchanged by this continuation.

## 7. Checks and control screen

Hand checks: for B=0 all extra terms vanish and GS9–GS12 reduce to
Note 34. For F=conjugate(z), constant q and E=0, rho=j=0 while
T_C=q/[pi(|z|^2+q)^2], giving the correct Delta log(|z|^2+q).
For F=x, constant q, Xi=2/(x^2+q); omitting Xi gives the wrong signed
gradient square, while GS9 gives S_x^2=4x^2/(x^2+q)^2. These are
hand-derived checks, not machine-symbolic or exact-arithmetic execution.

The generic identities permit collisions, including the heat polynomial
z^2-2t. A chosen gap premise fails if its transition covers a zero; no
global collision exclusion follows from the existence of another gap.
Euler-factor controls lack the unchanged canonical completion;
weighted-square/finite-prime controls lack its full coefficients/reflection;
reflected and smooth positive-primitive controls lack the canonical
gamma/source identity; atomic and polynomial controls lack the smooth
canonical source. These are failures of the theta-specific source/outer
inputs, not of GS7–GS15. No new control computation or RH inference.

**Next: Analysis — Sol**, [HDA-18-AN01 r1](../research-progress/handoffs/HDA-18-AN01.md).
Complete the full-support comparison before any numerical widening.
