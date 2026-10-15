---
research_program: ALG
secondary_programs: [PR02, PR02-CORR]
status: exact_closed_form_bridge_pointwise_sign_open
---

# Quaternion forms and the signed theta pairing

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from the current session metadata. Independently prompted internal LLM checks used the same inherited configuration.

The author's January and February 2014 quaternion-form drafts suggest a useful way to preserve the signed observation in [Note 49](../00_research_coordination/49_OCTONIONIC_SIGNED_BOUND_ANALYTIC_CONTINUATION_20261015.md): retain a polarized pairing of differential forms throughout boundary reconstruction. This note proves an explicit closed self-dual realization of the theta jets and their signed Laguerre expression. It supplies a representation, not the missing energy-relative estimate. [Review 30](../../reviews/30_QUATERNION_FORMS_DRAFT_COMPARISON_AND_RELEVANCE_20261015.md) compares the drafts and separates their usable structure from unfinished or problematic integral claims.

## 1. The signed pairing differs from the positive energy

On oriented Euclidean four-space, for a real two-form \(\Omega=\Omega_++\Omega_-\),
\[
\Omega\wedge\Omega
=(|\Omega_+|^2-|\Omega_-|^2)\,\mathrm{vol},\qquad
\Omega\wedge *\Omega
=(|\Omega_+|^2+|\Omega_-|^2)\,\mathrm{vol}.
\tag{1}
\]
This follows from \(*\Omega_\pm=\pm\Omega_\pm\), orthogonality, and the definition of the Hodge star. The wedge pairing has signature \((3,3)\); see also [Krasnov's self-duality discussion, slides 13–14](https://www.maths.nottingham.ac.uk/plp/pmzkk/ihes.pdf). For quaternion-valued forms an invariant real coefficient pairing or conjugation must additionally be specified. We use real forms below to remove that ambiguity.

The drafts' self-dual and anti-self-dual bases, kernel decompositions, and orientation-sensitive terms are therefore relevant. An apparent minus sign between wedge-sector integrals need not make the resulting quantity indefinite: because the anti-self-dual wedge square is already negative, subtracting it gives the positive energy. The actual scalar observation, including its star and conjugation, must be tracked.

For real \(a,b,c\), choose orthonormal self-dual forms \(\sigma_1^+,\sigma_2^+\) and an orthonormal anti-self-dual form \(\sigma_1^-\). The pointwise algebraic form
\[
\Omega=b\sigma_1^++\tfrac12(a-c)\sigma_2^+
+\tfrac12(a+c)\sigma_1^-
\]
satisfies
\[
\Omega\wedge\Omega=(b^2-ac)\,\mathrm{vol},\qquad
|\Omega|^2=b^2+\tfrac12(a^2+c^2).
\tag{2}
\]
Taking \((a,b,c)=(h_j,h_{j+1},h_{j+2})\) realizes \(\mathcal L_j\). The positive norm introduces \(h_{j+2}^2\), which the physical energy \(E=h_0^2+h_1^2\) does not control. Also, this variable-coefficient mixed-Hodge form is not automatically closed. The following construction supplies closed inputs without asserting that it repairs the norm problem.

## 2. A closed self-dual lift of the complete holomorphic jets

Fix real heat time \(t\). On \(\mathbb R^4\) use coordinates \((x,y,u,v)\), Euclidean metric, orientation \(dx\wedge dy\wedge du\wedge dv\), and complex coordinates \(z=x+iy\), \(w=u+iv\). The theta jets \(h_r(t,z)\) are entire in \(z\), as in Note 46. For any holomorphic \(f(z)\), put
\[
\alpha_f=\frac1{\sqrt2}\operatorname{Re}\{f(z)\,dz\wedge dw\}.
\tag{3}
\]
If
\[
A=dx\wedge du-dy\wedge dv,\qquad
B=dx\wedge dv+dy\wedge du,
\]
then \(*A=A\), \(*B=B\), \(A\wedge A=B\wedge B=2\mathrm{vol}\), and \(A\wedge B=0\). Consequently
\[
\alpha_f=(\operatorname{Re}f\,A-\operatorname{Im}f\,B)/\sqrt2,
\qquad *\alpha_f=\alpha_f,
\]
\[
d\alpha_f=0,\qquad
\boxed{\alpha_f\wedge\alpha_g
=\operatorname{Re}(f\overline g)\,\mathrm{vol}.}
\tag{4}
\]
Closedness follows directly from \(d(f(z)dz\wedge dw)=f'(z)dz\wedge dz\wedge dw=0\). Time is an external parameter; \(d\) here differentiates the four spatial coordinates only. This is an auxiliary abelian differential-form lift, not a claim that the original theta field is a nonabelian Yang–Mills connection.

Write \(\alpha_r=\alpha_{h_r(t,\cdot)}\). We obtain
\[
\alpha_{j+1}\wedge\alpha_{j+1}-\alpha_j\wedge\alpha_{j+2}
=\bigl(|h_{j+1}|^2-\operatorname{Re}(h_j\overline{h_{j+2}})\bigr)\mathrm{vol}.
\tag{5}
\]
At \(y=0\), the scalar coefficient is exactly \(\mathcal L_j=h_{j+1}^2-h_jh_{j+2}\). This means evaluation of the ambient coefficient at the physical slice, not pullback of a four-form onto a one-dimensional line. Off the slice (5) is its stated Hermitian extension, not the holomorphic quadratic expression \(h_{j+1}^2-h_jh_{j+2}\).

All inputs in (5) are closed and self-dual. The sign now resides in the coefficient-space matrix
\[
Q=\begin{pmatrix}0&0&-1/2\\0&1&0\\-1/2&0&0\end{pmatrix},
\qquad \operatorname{spec}(Q)=\{1,1/2,-1/2\}.
\tag{6}
\]
A positive kernel for the individual forms therefore does not establish a sign for their \(Q\)-pairing. Estimating its terms separately loses precisely the correlation we need.

There is a boundary identity independent of the old drafts' singular-kernel formulas. Choose a holomorphic primitive \(P_f'=f\) and define \(\beta_f=\operatorname{Re}(P_f(z)dw)/\sqrt2\). Then \(d\beta_f=\alpha_f\). For a smooth bounded four-dimensional domain, with the forms and primitive defined near its closure,
\[
\int_\Omega\alpha_f\wedge\alpha_g
=\int_{\partial\Omega}\beta_f\wedge\alpha_g.
\tag{7}
\]
For the entire theta jets a global primitive exists. Combining (7) with the signs in (5) gives a rigorous signed boundary flux. It remains a bulk integral identity; localization or replacement by the drafts' double-boundary kernel requires its own proof and bounds.

## 3. The current of Note 46 is a polarized form coefficient

Fix a real physical point \((t,x_0)\), a radius \(R>0\), and \(z_\theta=x_0+Re^{i\theta}\). Treat \(a=h_j(t,x_0)\) as a real constant and evaluate (4) with \(f=a\), \(g=h_j(t,z)\). Its coefficient on the spectral circle is
\[
\frac{\alpha_a\wedge\alpha_{h_j}}{\mathrm{vol}}(z_\theta)
=h_j(t,x_0)\operatorname{Re}h_j(t,z_\theta)=\phi_j(\theta).
\tag{8}
\]
The quotient in (8) denotes the coefficient relative to the fixed volume form, not division by physical energy. The full real prefactor and full stationary condition are retained. Thus the older differential-form viewpoint connects exactly to the current already isolated in Note 46.

On \(S_j=\{h_{j+1}=0\}\), let \(q(\theta)=1-\cos2\theta\) and let brackets denote the normalized circle integral. Note 46 proves
\[
\mathcal L_j=-\frac4{R^2}h_j^2+\frac4{R^2}\langle q\phi_j\rangle.
\tag{9}
\]
One useful sufficient target is
\[
\boxed{\langle q\phi_j\rangle\ge-C_j E,\qquad j=0,1,}
\tag{10}
\]
which gives \(\mathcal L_j\ge-4(1+C_j)E/R^2\) for \(C_j\ge0\). Here \(R,1/R,C_j\) must be source-prescribed and locally bounded through candidate events, on the required predecessor-covering domain. A sharper equivalent target for a proposed \(\kappa_j\) is \(\langle q\phi_j\rangle\ge h_j^2-(\kappa_jR^2/4)E\).

The form representation makes it natural to keep the whole signed pairing, allowing positive and negative boundary contributions to cancel. It does not justify replacing (10) with bounds on separate Hodge sectors, separate theta indices, or separate auxiliary norms. For the original staircase, retain Note 46's proved Gaussian-circle tail, full physical factors and full stationarity before using any cutoff comparison.

## 4. Closedness alone cannot supply the missing estimate

The exact backward-heat polynomial \(H(t,z)=z^2-2(t-T)\) has, at \(x=0,t=T-\delta\),
\[
h_0=2\delta,\quad h_1=0,\quad h_2=2,\quad
E=4\delta^2,\quad \mathcal L_0=-4\delta,
\quad \mathcal L_0/E=-1/\delta.
\tag{11}
\]
Every form in (3) remains closed and self-dual throughout this example. For the other branch, \(H=z^3-6(t-T)z\) gives \(h_2=0\), \(h_1=6\delta\), \(h_3=6\), and again \(\mathcal L_1/E=-1/\delta\). These controls prove that the algebra, holomorphic lift, and boundary reproduction alone do not give a locally bounded relative loss. A theta-specific restriction is indispensable.

The focused continuation is to use the complete theta source to estimate the polarized current (8) with its signs intact, or to construct Note 47's branch-specific accretive identity. The January draft's explicit branch-cut accounting is useful as a methodological warning: eliminating regular mixed terms can leave the entire difficulty in a signed defect. Any revived kernel must prove and pay that defect rather than suppress it.

The manuscript, height-112 finite cover, and outer threshold \(61/24\) are unchanged. This is an analytic representation and source assessment; no numerical pilot, new collision exclusion, manuscript snapshot, commit, or tag is asserted.
