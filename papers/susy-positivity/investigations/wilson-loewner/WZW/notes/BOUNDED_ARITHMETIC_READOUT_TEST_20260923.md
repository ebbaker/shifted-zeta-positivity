# Bounded arithmetic readout test: WZW collar, spectral weights and first delay

**Numerical correction, later on 23 September 2026:** the transformed prime-free kernel correction integral in the diagnostic used `exp(-2*v)` instead of `exp(-(3-2*omega)*v)`. The written convolution formula was correct. The implementation and record have been corrected and the complete suite replayed successfully. See the [modular-scattering note, Section 8](MODULAR_HODGE_SCATTERING_AND_CUSP_COUPLING_TEST_20260923.md) for the derivation, independent regressions and scope; the analytical exclusions are unchanged.


23 September 2026. Prepared for Edward Baker with LLM assistance.

**Model:** GPT-6 (Codex; developer-provided identity).  
**Effort:** not exposed; not inferred.  
**Status:** analytical exclusion of a specified reflected collar readout, with an exact primary spectral calculation and finite diagnostics. No arithmetic realization, full slit-sewing construction, RH result, or independent specialist review is claimed.

This carries out the bounded test authorized after the [research-avenues discussion](RESEARCH_AVENUES_20260923.md). Its purpose is to decide whether a concrete native WZW preparation and readout can supply the arithmetic operator, before attempting general slit sewing.

## 1. Result and scope

The normalized collar on the full boundary module gives a genuine strong identity limit and an exact positive norm balance. With a fixed preparation and its reflected readout, however, its response is self-adjoint. A bounded self-adjoint causal operator on a scalar L2 interval must be a multiplication operator. The nontrivial arithmetic Volterra transfer is not such an operator. Thus this collar construction fails the arithmetic readout test even with the entire affine module retained.

For the selected spin-1/2 primary preparation, an independent calculation gives the exact infinite spectral weights

\[
 d_n=\frac{(3/8)_n}{n!}=1,\frac38,\frac{33}{128},\frac{209}{1024},\ldots.
\]

They are matrix-element weights, not the character multiplicities of the module. They do not match the unit weights of the arithmetic gamma tower. The corresponding two-point kernel has collision order u^(-3/8), whereas the first arithmetic response needs a causal finite part with order 1/u. It is smooth at u=log(2), so it also supplies no first-prime atom or delayed fractional singularity.

These results concern (i) positive Euclidean collar propagation with a fixed reflected preparation/readout and (ii) the specified primary two-point source. They do not exclude general asymmetric slit sewing, oriented scattering, additional fields or defects, or a separately justified singular readout. No general theorem against WZW arithmetic realizations is asserted.

## 2. The independently specified physical preparation

Use the same diagonal SU(2)_2 Cardy theory as the completed pilot: c=3/2, boundary labels 0 and 1/2, and

\[
 \mathcal H=\mathcal H_{0,1/2}=V_{1/2},\qquad h=3/16.
\]

The Hilbert space contains all affine descendants with null states removed. Its positive inner product is the unitary radial/reflected inner product. It is neither the two-dimensional evaluated tensor metric nor an arithmetic L2 norm by definition.

The established BCFT input is the strip Hamiltonian proportional to L0-c/24 and its boundary-sector interpretation; see [Cardy, Sections 1.2 and 3](https://arxiv.org/html/hep-th/0411189). The WZW weights, charge grading and affine modules are also described in [the WZW TCSA study, Section II](https://arxiv.org/html/1301.0084). The following operator test is derived from this input.

### 2.1 A normalized collar with a fixed scalar reference

Choose dimensionless collar length s>=0. Divide its propagation operator by the amplitude in a unit ground state |h,+>:

\[
 S_s=\frac{e^{-s(L_0-c/24)}}
 {\langle h,+|e^{-s(L_0-c/24)}|h,+\rangle}
 =e^{-sN},\qquad N=L_0-h\ge0.
\]

This specifies the scalar reference exactly. It is a ground-channel collar normalization, not a claim to have reconstructed the pilot's general slit observable. Collar length s is not identified with arithmetic shift, capacity or window length.

The full affine module has finite-dimensional eigenspaces at levels n=0,1,2,... . Therefore S_s is a positive self-adjoint contraction, compact for s>0, with S_0=I and S_s tending strongly to I as s decreases to zero. Compactness follows by cutting off levels above M: the operator-norm tail is at most exp[-s(M+1)]. The identity limit is strong rather than in operator norm; in fact ||I-S_s||=1 for every s>0.

For every state psi in the Hilbert space, the spectral theorem gives

\[
 \|\psi\|^2-\|S_s\psi\|^2
 =2\int_0^s\|N^{1/2}S_r\psi\|^2\,dr.
\]

The integral is well defined even when psi is not in the domain of N^(1/2), by its nonnegative spectral integral. Differentiation at r=0 on arbitrary vectors is not asserted.

### 2.2 A concrete infinite primary packet

Fix a spin component m=+1/2 and a unit highest-weight state |h,m>. Translation of the boundary-changing insertion prepares

\[
 |z,m\rangle=e^{zL_{-1}}|h,m\rangle,\qquad |z|<1.
\]

The global conformal algebra gives

\[
 \|L_{-1}^n|h,m\rangle\|^2=n!(2h)_n,
 \qquad
 |n,m\rangle=\frac{L_{-1}^n|h,m\rangle}{\sqrt{n!(2h)_n}}.
\]

Indeed L1 L(-1)^n|h,m>=n(2h+n-1)L(-1)^(n-1)|h,m>; induction proves the norm formula. Orthogonality of different L0 levels gives

\[
 \langle z,m|w,m\rangle
 =\sum_{n\ge0}d_n(\bar zw)^n=(1-\bar zw)^{-2h}.
\]

This selects a closed global-descendant subspace of the full affine module. Other affine states have not been deleted from the theory; this particular single-insertion preparation has zero component orthogonal to that subspace. Increasing a numerical level cutoff does not create their missing matrix elements.

For normalized level-amplitude input f=(f_n) in ell2, define Jf=sum_n f_n|n,m>. The reflected readout is J*, and

\[
 W_s=J^*S_sJ,\qquad (W_sf)_n=e^{-sn}f_n.
\]

This is a specified infinite-dimensional response with exact initial identity and the preceding norm balance. Its inputs are level amplitudes. Calling them spatial arithmetic inputs would require a further map.

For comparison, smearing the primary with Fourier amplitudes before level normalization instead prepares Bf=sum_n sqrt(d_n)f_n|n,m>. Its reflected Gram operator at zero collar is diag(d_n), not I. Since d_n tends to zero, converting that field smearing into J involves an unbounded inverse Gram factor. The level-amplitude construction is stated separately so that this normalization issue is not hidden in a claim of physical spatial preparation.

## 3. An obstruction that survives every fixed isometric input identification

Give the collar the most favorable norm dictionary: suppose an isometry J_L:L2(0,L)->H has been supplied by some independently specified preparation. With its reflected readout, set

\[
 W_{s,L}=J_L^*S_sJ_L.
\]

Then W_(0,L)=I, W_(s,L) is a positive self-adjoint contraction, and

\[
 \begin{split}
 \|f\|^2-\|W_{s,L}f\|^2
 ={}&2\int_0^s\|N^{1/2}S_rJ_Lf\|^2\,dr\\
 &+\|(I-J_LJ_L^*)S_sJ_Lf\|^2.
 \end{split}
\]

The second term accounts for output in unobserved states. This is an explicit cumulative balance, not positivity inferred from a selected correlator.

**Proposition.** If a bounded self-adjoint operator T on scalar L2(0,L) is causal in the sense that output before a cut a is independent of input after a, then T is multiplication by a real essentially bounded function.

**Proof.** Let P_a multiply by the indicator of (0,a). Causality says P_a T(I-P_a)=0. Taking adjoints gives (I-P_a)TP_a=0, so T commutes with P_a for every a, hence with all measurable-set projections. Put v=T1, which is defined since the interval is finite. Commutation gives T1_E=1_E*v for every measurable E, and then Tf=vf on simple functions. Boundedness forces v to be essentially bounded, and density extends the equality to L2. Self-adjointness makes v real. A compact multiplication operator on this nonatomic interval is zero. In particular, for s>0 a causal W_(s,L) would have to be zero, since S_s is compact. But for nonzero f, <f,W_(s,L)f>=||S_(s/2)J_Lf||^2>0. Therefore W_(s,L) cannot be causal. QED.

The arithmetic transfer is nonzero, causal and nonlocal at every positive shift. Near the origin its kernel has a nonzero positive leading term proportional to u^(omega-1), as shown below. Positive inputs on two suitably small successive disjoint intervals therefore give a nonzero forward pairing and an exactly zero reverse pairing. It cannot be self-adjoint.

This rules out equality W_(s(omega),L)=V_(omega,L) for this reflected collar readout for any positive collar clock s(omega). It does not depend on a particular spatial identification, a finite descendant truncation, or a claim that the arithmetic generator must be instantaneously positive.

Even allowing fixed distinct input and output contractions cannot evade the argument while preserving the exact identity: if ||J||<=1, ||R||<=1 and RJ=I, norm equality first makes J an isometry. Moreover R*f=Jf follows from <R*f,Jf>=||f||^2 and both norm bounds. Hence R=J*. An evasion must change some explicit ingredient: the propagation, the output rule, its dependence on the parameter, or the independently controlled norm dictionary.

## 4. Exact primary spectral response and its arithmetic mismatch

The preceding operator failure is sufficient to reject the collar candidate. We also test the suggestion that descendants of the selected boundary field could supply the arithmetic gamma source. This is a separate source diagnostic; the two-point susceptibility is not identified with the logarithmic generator N of the collar.

For a strip/cylinder coordinate with exponential map z=exp(lambda*w), unit leading plane OPE coefficient and u>0, the two primary Jacobians give

\[
 C_h^\lambda(u)
 =\left[\frac{\lambda}{2\sinh(\lambda u/2)}\right]^{2h}
 =\lambda^{2h}\sum_{n\ge0}d_n e^{-\lambda(n+h)u}.
\]

This formula follows by substituting z1=exp(lambda*u), z2=1 into (z1-z2)^(-2h) and multiplying by both conformal Jacobians. Thus the mode residues and the lowest gap are fixed together by the chosen field.

### 4.1 A charge source can explain a cosh, but not its arithmetic coefficients

As an additional favorable control, introduce a real source chi for the standard Hermitian Cartan charge J0^3 in the propagating channel, replacing lambda*L0 by lambda*L0-2*chi*J0^3. The two spin-1/2 components have charges +/-1/2, and their global descendants retain those charges. Averaging their diagonal two-point amplitudes gives

\[
 C_{h,\chi}^\lambda(u)=C_h^\lambda(u)\cosh(\chi u).
\]

For lambda=2 the displayed primary tower decays at infinity when |chi|<3/8. The diagnostic uses |chi|<=1/4. No contractivity claim for a full charge-deformed sewing map is inferred from this matrix element. The arithmetic comparison chi=omega is only a proposed source dictionary, not a derived identification of geometric time.

Thus paired charges offer a physical way to produce a cosh dependence. They do not select log(n), the von Mangoldt weights, the gamma residues, or the required contact subtraction.

### 4.2 The gamma tower has the wrong residues and collision order

The inherited gamma density is

\[
 n_\Gamma(u)=\frac{e^{-u/2}}{1-e^{-2u}}
 =\sum_{n\ge0}e^{-(2n+1/2)u}.
\]

Matching its level spacing forces lambda=2. The selected WZW primary instead gives

\[
 C_{3/16}^2(u)
 =2^{3/8}\sum_{n\ge0}\frac{(3/8)_n}{n!}e^{-(2n+3/8)u}.
\]

Even granting an external common normalization and an energy offset to align the first mode would leave the residue ratio d1/d0=3/8, rather than 1. The entire infinite sum is used here. Its collision behavior is C(u)~u^(-3/8), whereas 2*n_Gamma(u)~1/u. A finite number of ordinary derivatives of this selected kernel changes the collision powers by integers and cannot turn 3/8 into 1. A nonlocal or singular amputation would be new physical input requiring a domain and norm analysis.

For h<1/2 the exact Laplace susceptibility is

\[
 \mathcal S_h^\lambda(p)
 =\lambda^{2h-1}B(p/\lambda+h,1-2h).
\]

For the selected primary it decays as Gamma(5/8)*p^(-5/8). A subtracted susceptibility therefore has a finite large-real-p limit. The arithmetic source instead has logarithmic growth. Local finite constants and rational pole corrections cannot repair this mismatch.

There is a useful nearby comparison: the spin-one field has h=1/2 and unit binomial weights, but at spacing two its gap is 1 rather than 1/2. It belongs to a different available boundary sector; it is not the selected V_(1/2) preparation. Multiplying its response by an externally chosen exponential could align a tower, but no such offset is derived by this test. Neither this alternative nor a matching module character supplies the full arithmetic source.

## 5. Complete first-window and first-prime benchmarks

These formulas are arithmetic comparison data, inherited from [the earlier fixed-window calculation](../../notes/FIXED_WINDOW_WILSON_RESPONSE_OBSTRUCTION_20260920.md) and [SI S1](../../sections/s_arithmetic.tex). They are not reconstructed from the WZW correlator.

### 5.1 Before log(2)

On L<log(2), the exact zero-shift symbol after absorbing the lowest gamma mode is

\[
 a_0^<(p)=\psi(5/4+p/2)-\log\pi+\frac{2}{p-1/2}.
\]

The first response -G0 has off-diagonal kernel

\[
 b(u)=\frac{2e^{-5u/2}}{1-e^{-2u}}-2e^{u/2},\qquad u>0,
\]

with b(u)=1/u-7/2+O(u). In the hard-delay-cutoff convention the correlated contact is

\[
 c_\epsilon=\log\epsilon+\gamma+\log(2\pi)+O(\epsilon).
\]

The equivalent difference convention has local constant w0=psi(1/4)-log(pi), approximately -5.372183419225665. The growing exponential is part of the exact finite-window response and is not a positive stable covariance mode. It must not be omitted because the window contains no prime delay.

For 0<omega<=1/2 define

\[
 q_\omega(u)=\frac{2\pi^\omega}{\Gamma(\omega)}
 e^{-(5/2-\omega)u}(1-e^{-2u})^{\omega-1}\mathbf1_{u>0}.
\]

The complete prime-free kernel is

\[
 k_\omega^<(u)=q_\omega(u)-2\omega\int_0^u
 e^{(1/2-\omega)(u-v)}q_\omega(v)\,dv,
\]

and near zero

\[
 k_\omega^<(u)\sim A_\omega u^{\omega-1},\qquad
 A_\omega=\frac{(2\pi)^\omega}{\Gamma(\omega)}>0.
\]

The primary two-point candidate fails this first-window source comparison at the collision order already. No independent derivation of its required contact or rational correction has been found. Their absence is recorded rather than repaired by adding arithmetic filters.

### 5.2 Crossing the first prime delay

Let ell=log(2). On the window ell<L<log(3), the inherited integer-comb factorization specializes to the exact identity

\[
 k_\omega(u)=k_\omega^<(u)
 +c_2(\omega)\mathbf1_{u>\ell}k_\omega^<(u-\ell),
 \qquad
 c_2(\omega)=\frac{2^\omega-2^{-\omega}}{\sqrt2}
 =\sqrt2\sinh(\omega\ell).
\]

Thus for positive shift the required response acquires a delayed singular term with leading coefficient c2(omega)*A_omega and power (u-ell)^(omega-1). The logarithmic generator has the atom

\[
 -\sqrt2\log(2)\cosh(\omega\log(2))\,\delta_{\log2}.
\]

The primary kernel C_(h,chi)^lambda is real analytic for every u>0. Its spectral series and all derivatives converge uniformly on compact subsets away from zero. In particular, its integral over (ell-epsilon,ell+epsilon) tends to zero, whereas a generator atom has a nonzero limiting mass. It has neither that atom nor the finite-shift delayed singularity. Retaining all its descendants does not change the conclusion.

## 6. What has been decided

| Requirement | Result for the specified test |
|---|---|
| Physical state space and scalar normalization | Full V_(1/2), with the ground-channel collar normalization specified |
| Strong initial identity | Established for normalized level inputs and, conditionally on a supplied isometry, spatial inputs |
| Positive cumulative norm balance | Established for the reflected collar, including unobserved output |
| Causal arithmetic input/output response | Excluded for the fixed reflected positive collar class |
| Gamma tower and local singularity | Exact primary matrix-element weights and collision order disagree |
| Fixed contact and rational terms | Full target retained; no physical derivation supplied, and finite additions cannot cure the gamma mismatch |
| First prime delay | Exact required coefficient identified; absent from the specified primary response |
| General slit sewing or arithmetic realization | Not constructed or excluded |

The appropriate next physical candidate should therefore have an oriented input/output response, rather than this reflected Euclidean collar compression, and an independently specified mechanism creating discrete real delays. A chiral or scattering readout with additional arithmetic geometry might do this, but must be defined before further descendant calculations. Adding the first prime shift or its coefficient as an external filter would reproduce the target by prescription.

This result supports deferring a general WZW sewing calculation until that new readout is identified. The collar remains a useful control: it shows exactly which identity and norm properties are available, and why those properties alone do not produce the desired arithmetic response.

## 7. Diagnostics and provenance

The [program](../numerics/check_boundary_readout.py) and [record](../numerics/records/boundary-readout-20260923.json) contain 60 passing controls: 13 exact rational and 47 floating. They compare global-algebra norms with conformal-map coefficients, map and spectral formulas with an analytical truncation bound, beta susceptibility with transformed quadrature, collar energy loss with quadrature, the complete arithmetic first variation with finite differences, and the first delay and collision coefficients. The rational checks are finite identities, not certificates for infinite-dimensional operator statements.

For unit L2 indicator inputs on (0,.02) and (.03,.05), omega=.25, the arithmetic forward pairing is nonzero; the reverse pairing is exactly zero by support. Numerical values and quadrature refinement are in the record. The primary response's mass in a width-.0002 window around log(2) is small and tends to zero as the window shrinks; the required generator atom has magnitude about one. The analytical regularity argument, not these samples, establishes absence of an atom.

Replay from the parent Wilson--Loewner directory:

```sh
python3 -B WZW/numerics/check_boundary_readout.py --output /tmp/wzw-boundary-readout-replay.json
```

Python 3 and NumPy suffice. Floating comparisons are diagnostics, not rigorous enclosures. This is a separate 60-case suite, not a replay or expansion of the older arithmetic-source 60 cases or WZW pilot 72 cases. The old records and manuscripts are unchanged. See the [same-assistant audit](../reviews/review_codex_bounded_readout_20260923.md) for claim boundaries and review status.
