# VCD-GT-GR-E05 r1 — Initial proof assessment

17 November 2026, America/New_York. Prepared for **Edward Baker** with OpenAI
Codex LLM assistance. Requested dispatch **gpt-6.1-sol / ultra**. Actual serving
model and reasoning effort were unavailable to this assessor. Separate-agent
internal assessment using shared repository premises, by an agent who did
not author either proof.

**E02 and E03 accepted within their frozen scopes.** The assessment took one
proof pass. No required correction was found. Both [E05 proof pins][request]
matched and the four common input pins in the [E02][e02request] and
[E03][e03request] requests matched. The exact identities and regularity are
ready for B02 as representation inputs under [Classification01][class].
Use the [result index][results], [Cluster18][cluster] and [avoid index][avoid]
for their status and the [Shared premises05][shared] rule for the review
boundary.

The common domain is the unchanged complete \(H_t=-H_{zz}\) on the
separately paid compact count-two tube \(I\subset[0,1/2]\), using the
inherited strip, count, product and safe-line inputs. Fix \(T\ge64\),
\(L=\log T\), \(\ell=L^{-1}\), \(\max(2,4\sqrt d)\le a\le L\) and
\(r_0=a\ell\), with \(c\in[T,2T]\), \(|D|\le d\ell^2\le r_0^2/16\).
Include both signs of \(D\), all occurrence multiplicities and endpoints
by continuation from the paid interval. The targets have \(|z-c|\le
r_0/4\) and every exterior occurrence has \(|w_j|\ge r_0\). The closures
and regularity tests below concern the classes explicitly named. [E01
audit][e01] · [Parent Note41][n41] · [Assessment19][a19] · [Scope07][scope]

## E02 — Complete integer moments and resolvent

- **Finite law and cancellation.** With \(m_j=(w_j^2-D)^{-1}\),
  \(P=\sum_j w_jm_j\) and \(T_3=\sum_j w_jm_j^3\) in the finite
  simple-root calculation, the two target velocities give \(c'=-2P\)
  and \(D'=2-4DM\). The exterior relative velocity has
  \(4w_jm_j+2P\) plus the exterior pair terms. In differentiating
  \(m_j^2\) this yields the unpaired contribution
  \((-12-8DM)S_3-16DS_4-8PT_3\). From
  \(h_{3,jk}=(w_jm_j^3-w_km_k^3)/(w_j-w_k)\), put \(u=w_j,v=w_k,A=m_j,B=m_k\).
  The divided difference is
  \(-AB(A+B)-(D+uv)AB(A^2+AB+B^2)\). Multiplying the negative pair sum by
  eight gives terms \(8(MS_2-S_3)\), \(8D(MS_3+S_2^2/2-3S_4/2)\)
  and \(8(PT_3+T_2^2/2-3(S_3+DS_4)/2)\). The subtractions remove
  the exact diagonals. The \(PT_3\) and \(DMS_3\) terms cancel before
  any limit, giving
  \[
  S_2'=8MS_2-32S_3+4DS_2^2-40DS_4+4T_2^2.
  \]
  In particular no complete sum of \(P\) is needed. [E02 §§1–2][e02]
- **Contour signs, target residues and multiplicity.** On the local
  stationary physical circle write \(u=z-c\), \(Q=u^2-D\) and \(B=F_z/F\).
  For \(f=Q^{-p}\) and \(f=uQ^{-2}\) the contour integral of \(fB\)
  counts the exterior values with a minus sign by decay of the rational
  pole kernel at infinity, and the regularizers integrate to zero.
  The target term for \(Q^{-p}\) is a spatial derivative. For \(uQ^{-2}\)
  the residues of \(2u^2/Q^3\) are \(-1/(8\zeta^3)\) at \(+\zeta\)
  and \(+1/(8\zeta^3)\) at \(-\zeta\) when \(\zeta^2=D\ne0\). At the
  double the sole term is \(2u^{-4}\). The zero sum differentiates as a
  single contour identity, including at the double where its time
  derivative is \(8c'u^{-5}+6D'u^{-6}\). In \(T_2'\), differentiating
  \(uQ^{-2}\) at fixed \(z\) produces
  \(-c'Q^{-2}-2uQ^{-3}Q_t\), with \(Q_t=-2uc'-D'\).
  The contour equations use the full \(B\) and heat derivative.
  Rouché and the first two moment integrals give analytic \(c,D\) and
  analytic contour observables through target and exterior multiples.
  At a finite multiple slice, separating roots and initializing heat
  evolutions at the same slice gives convergence of both sides by
  the fixed contour and exterior clearance. [E02 §§1–2][e02]
- **Complete passage.** Opposite-pair truncations include all ties and
  multiplicities. The strip and closed-slab counts give
  \(\sum_{|\rho|>N}|\rho|^{-2}=O(\log N/N)\) uniformly on \(I\).
  On compact spatial sets this pays the product error and, by Cauchy
  on a larger compact set, its spatial derivatives through order
  three. A finite cover with fixed zero-free circles gives positive
  minima for the \(F,Q\) denominators. The heat jet on each reference
  slice therefore converges uniformly at fixed \(T\). At that slice
  the truncated target factors are the exact target factors and the
  \(S_1,\ldots,S_4,T_2\) tails are absolute and uniform. The passage
  concerns the reference slice and its first heat jet. [E02 §3][e02]
- **Resolvent.** Absolute geometric expansion gives Taylor radius
  \(A_*=\inf_j|w_j^2-D|\ge r_0^2-|D|\ge15r_0^2/16\), with normal
  convergence on compact subdisks of the common guaranteed disk.
  At a finite \(A_*\), local finiteness and the far-tail decay isolate
  a nearest pole whose residue is minus the counted multiplicity of
  that denominator. The default circle at its reference slice
  requires \(|D+\eta|<r_0^2/4\) to enclose both kernel poles. A larger
  circle still inside \(r_0\) works on compact subdisks of the
  guaranteed disk. For any \(|\eta|<A_*\), the section
  \(|Q|=\beta\), \(\max(|D|,|\eta|)<\beta<A_*\), is a smooth simple
  curve with one transverse crossing per ray from \(c\). It encloses
  targets and auxiliary poles, and strict separation allows it to stay
  fixed locally in \(t,\eta\). The contour proof also works when the
  kernel poles coalesce. [E02 §4][e02]

## E03 — Finite Gaussian law and radial reconstruction

- **Slice sums and contours.** The collar, counts and strip give
  absolute uniform slice tails and the conjugation reality of \(S_p\),
  \(G_{s,p}\) and \(A_{s,p}\) for \(p=1,2,3\) and positive \(s\) in a
  fixed compact interval. The finite telescope includes its complete
  residual. At each slice the unit count permits independent left and
  right cuts with distance \(\gg1/\log(2+|v|)\) from every projected zero.
  In the log-derivative subtraction at the same physical abscissa the
  product regularizers cancel. The near shells cost \(O(\log^2
  (2+|v|))\), and the far shells use the absolute inverse-square
  series. The Gaussian horizontal decay then removes each vertical
  edge and the exterior tails are absolute. The lower line goes left
  to right, the upper line right to left. Subtracting the positive
  inner circle leaves the full exterior with positive occurrence
  residues. [E03 §§1–2][e03]
- **Real-time regularity and differentiation.** Safe-line subtraction
  and reciprocal-power shells pay \(h,h_w,h_{ww}\), with
  \(h=H_z(t,c+w)/H(t,c+w)\). Counted contour differentiation bounds
  \(c'=O(L^2/r_0)\), \(D'=O(L^2)\) by using powers \(z-c_*\) on the
  fixed reference circle, and \(h_t=-h_{ww}-2hh_w+c'h_w\) supplies
  the real-time majorant. The horizontal majorant (8) retains
  \(e^{16s_+}e^{-s_-x^2}\), with constants at fixed height, and the
  cleared inner circle pays the local time derivatives by analyticity.
  This yields real-time \(C^1\) with inward endpoint derivatives using
  the limiting contour identity at every slice. For \(f=e^{-sw^2}/Q^p\)
  the unintegrated identity is
  \[
  \partial_t(fh)=(f_t-f_{ww}-c'f_w)h+f_wh^2+
      \partial_w(-fh_w+f_wh-fh^2+c'fh).
  \]
  The total derivative has zero integral on the inner circle and its
  primitive tends to zero at both ends of each safe line. The time
  coefficient is \(f_t=pD'e^{-sw^2}/Q^{p+1}\) at fixed \(s\). A
  varying scale adds \(-s'w^2f\). The law uses the full square. For
  any finite partition of \(M\) including the complement, \(2M^2\)
  retains each cross term \(4M_kM_l\). [E03 §3][e03]
- **Inner residues.** With \(g=h-2w/Q\), the cleared disk contains
  holomorphic \(g\) and \(g_t\) by Cauchy on the larger inner circle.
  Write \(R_n(B)=\mathscr I(B/Q^n)\). The two split roots give the
  order-\(n\) residue formula and at a double the rule is
  \(R_n(B)=[w^{2n-1}]B\). In the target term of \(\mathscr I(fh)\),
  expansion of \(e^{-sw^2}=e^{-sD}e^{-sQ}\) leaves the \(Q^{-1}\)
  term \(2e^{-sD}(-s)^p/p!\) after integrating with \(w\). Its time
  derivative is \(-2sD'e^{-sD}(-s)^p/p!\). The other two differentiated
  contributions are \(pD'R_{p+1}(e^{-sw^2}g)\) and
  \(R_p(e^{-sw^2}g_t)\). Their sum is the full positive inner integral
  to be subtracted from the outer result. [E03 §3][e03]
- **Radial endpoints, conversion and finite cusp.** The scale density
  \(2|w|^2R^{-2}e^{-|w|^2/R^2}\) integrates to one against \(dR/R\)
  for each occurrence and is bounded by \(2/e\). Absolute moment
  tails pay the sum/integral interchange and the \(R\to\infty\)
  endpoint. Clearance pays \(R\downarrow0\). Cluster multiset
  continuity and common tails give radial time continuity. The
  exact \(\Delta_{s,p}=A_{s,p}-G_{s,p}\) has factor
  \(1-e^{2sy^2-2isxy}\) times \(e^{-s|w|^2}/a_j^p\).
  Pairing conjugates produces \(\cos(2sxy+p\arg a_j)\) in the
  holomorphic term. Along the exponential segment the length is
  \(2|wy|\) and the maximum modulus is \(e^{-sx^2+sy^2}\), giving
  the stated bound with vertical amplification. In the finite even
  quartic the separated exterior double has \(D'(0)=2\) by evaluating
  the differentiated factorization at \(b\). For its two exterior
  displacements the Taylor contribution \(2F_{w\bar w}|D|\) has
  \(F_{w\bar w}=sF(2p-1+su^2)>0\) at the double, with the other
  displayed quadratic terms smooth in \(D\). This yields distinct
  one-sided radial derivatives in that polynomial class. The
  holomorphic limit \(s\downarrow0\) is a slice convergence statement.
  [E03 §§1, 4][e03]

## Premise screen and scope

This is preparatory representation work. The [Controls12][controls]
documentary checks agree with [Note44 §7][n44], the [E01 audit][e01] and
[Assessment19][a19]. The heat polynomial collision controls share local
heat and contour algebra and lack canonical growing population. Euler
modifications change theta arithmetic and its endpoint discrepancy.
Weighted-square and finite-source and finite-prime classes lose full
unit-weight reflected theta equality, with the strip failing in the
documented endpoint-defective classes. The reflected super-Gaussian fails
the order premise. Smooth and positive-primitive controls change theta
arithmetic. Atomic and finite-profile controls change the source and lack
canonical population growth. RH-conditional endpoint controls carry RH
and change ordinary Dirichlet arithmetic. Changed observations lose the
physical cosine readout and fractional profiles lack the counted integer
divisor. Equal-count opposite-sign slices supply no canonical common-time
tube. A coarse upper count and local collar can survive several of
these changes. [Premises02][premises]

E02's equal-denominator examples give distinct instantaneous \(S_2'\)
at fixed \(c,D,\mathcal R\) in the generic polynomial heat class. They
establish that class-specific failure of denominator-only determination.
E03's even quartic gives a separated-exterior-double example of failure
of radial \(C^1\) in the finite polynomial class. Canonical closure and
radial time differentiability at canonical exterior mergers remain open.
[Scope07][scope]

## B02 inputs and outstanding estimates

1. Use complete \(M'=2M^2-12S_2-16DS_3\), E02's absolute moment laws
   and spatial companion, and E03's exact split for
   \(\mathcal F=\ell^4(12S_2+16DS_3)\) on the same paid tube. In the
   radial representation substitute \(G=A-\Delta\) with the complete
   signed conversion. [Note41][n41] · [E03 §5][e03]
2. The candidate fixed-physical-\(s\) \(O(L^{-1})\) bound for the
   normalized forcing complement remains a B02 estimate. It concerns
   the difference with its exact Gaussian weight and full exterior
   denominator, with the retained part still requiring its own
   signed estimate. The microscopic candidate \(s\asymp L^2\) must
   pay the actual vertical amplification and phase at the zeros as
   well as any safe-line contour allowance used. The fixed-strip
   \(e^{16s_+}\) majorant gives finite-scale regularity with
   height-dependent constants. [E03 §§1, 3, 5][e03]
3. Compare a joint upper allowance for the complete signed forcing
   with \(KL\), or the complete backward multiplier
   \(\exp(-4\int m\,d\sigma)\) with the inherited bound on a paid
   interval. The accepted parent comparison yields \(O(\sqrt L)\)
   allowance on the negative side after a fixed positive scaled
   buffer, and \(O(L)\exp(O(\sqrt L))\) transport on a fixed scaled
   interval at fixed \(a,d\). Preserve the initial layer, duration,
   incoming \(D\), and endpoint equality. Give the direct comparator
   the same acquired information. A gain on a separate allowance
   leaves an obligation for the full joint consumer. [Assessment19
   §§4–5][a19] · [Joint bounds12][joint]

[request]: ../research-progress/handoffs/VCD-GT-GR-E05-r1.md
[e02request]: ../research-progress/handoffs/VCD-GT-GR-E02-r1.md
[e03request]: ../research-progress/handoffs/VCD-GT-GR-E03-r1.md
[e01]: 02_VCD_GT_GR_E01_INPUT_AUDIT_20261117.md
[e02]: ../notes/02_VCD_GT_GR_E02_CANONICAL_MOMENTS_20261117.md
[e03]: ../notes/03_VCD_GT_GR_E03_GAUSSIAN_EVOLUTION_20261117.md
[n41]: ../../notes/41_VCD_GT_E21_EXACT_INTERACTION_RICCATI_BOUND_20261117.md
[n44]: ../../notes/44_VCD_GT_SCALE_AND_MOMENT_HIERARCHY_DISCUSSION_20261117.md
[a19]: ../../reviews/19_VCD_GT_E22_FIXED_COLLAR_ASSESSMENT_20261117.md
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[shared]: ../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
