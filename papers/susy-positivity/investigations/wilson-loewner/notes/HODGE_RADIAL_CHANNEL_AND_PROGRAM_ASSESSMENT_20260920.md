# After radial non-descent: the Hodge alternative and the spectrum it loses

Date: 20 September 2026. Prepared for Edward Baker.
Model: OpenAI GPT-6 (Codex; developer-provided identity).
Effort setting: not exposed in this session; not inferred.
Status: internal analytical follow-up and finite checks; specialist review
outstanding. No manuscript revision or new arithmetic positivity result.

## Main conclusion

The new radial-descent obstruction withstands the present internal audit in
its stated scope: ordinary spatial dilation does not preserve arbitrary
closed representatives in the fixed Higgs localization complex. Its explicit
non-closure witness is stronger than a mere noncommuting-generator argument.

There is a legitimate qualification. In the free conformal theory one can
first choose canonical Hodge representatives. The resulting protected
Hilbert space has a well-defined restricted radial Hamiltonian. This does
not contradict the previous note, which explicitly left that possibility
open. The calculation below determines what this alternative retains:

**For an elementary scalar, Hodge projection retains only the lowest spatial
mode. Every higher one-particle angular mode contributing to the arithmetic
gamma tower is removed. The ordinary-adjoint endpoint response of the
normalized retained scalar is a single exponential, not a tower.**

The protected space also contains composite states with an infinite spectrum.
Their counting character can be filtered to resemble the even arithmetic
ladder. That does not make the elementary endpoint couple to those states,
nor identify a character with a response function. This distinction gives
the next physical proposal a more precise test.

## 1. What was reviewed and reproduced

Read and checked:

- `notes/SPATIAL_RADIAL_DESCENT_OBSTRUCTION_20260920.md` and its handoff;
- the preceding predictive hemisphere calculation and checker;
- current manuscript/supplementary conventions and the separate cumulative
  append handoff in `../critical-path/notes/`;
- the primary supersymmetry/Hodge formulas [D, (3.1)–(3.5)] and the free
  hypermultiplet boundary algebra [G, §4.3.2].

The 83 radial-descent checks pass on replay, and the replay is byte-identical
to the saved record in this environment. Of these, 57 are rational/algebraic
and 26 floating-point. The checks validate the implemented algebra and
normalizations, not the external supersymmetry transformations. Before this
addition, the live package inventory and all four manuscript snapshots also
passed their identity checks.

In the centered frame the scalar family is

\[
 O(t)=q_1(t)+\frac{t}{2r}q_2(t),\qquad
 \mathcal Qq_2(t)=\chi(t),\qquad
 \mathcal Qq_1(t)=-\frac{t}{2r}\chi(t).
\]

Keeping the polarization of the specified insertion fixed under ordinary
dilation gives

\[
 \mathcal Q[D,O(t)]=-\frac{t}{2r}\chi(t).
 \tag{1}
\]

For nonzero interior \(t\), the free fermionic state gives a witness of
non-closure. The finite transformation evaluates the old polarization
against the annihilator at the moved point, producing the same mismatch.
The centered stereographic formula in the new note avoids confusing
dilation about an endpoint with dilation about the hemisphere center.

The robust conclusion is failure of the *unprojected operation on all
representatives*. It is not a theorem that every possible action on selected
cohomology representatives is trivial. Likewise the exact compensated
generator \(D-R_H\) acts trivially on the tested classes, but this statement
does not say that \(D\) itself has zero eigenvalues on canonical primaries.
Those distinctions are needed in any high-level account of the result.

## 2. Canonical representatives permit a different radial evolution

In radial quantization, use the positive physical Hilbert-space adjoint.
For either of the two nilpotent Higgs charges, [D, (3.4)] identifies its
positive Hodge operator, up to a positive constant, with

\[
 B_H=D-R_H\succeq0.
 \tag{2}
\]

Here \(R_H\) is the adapted Cartan generator; it is not the field-space
Mellin operator. The cohomology has canonical representatives in
\(\mathcal H_H=\ker B_H\). The free theory has a joint energy/R-charge
eigenbasis, so \(D\) commutes with the orthogonal spectral projection
\(P_H=1_{\{0\}}(B_H)\). Consequently

\[
 T_H(u)=e^{-uD}|_{\mathcal H_H},\qquad u\geq0,
 \tag{3}
\]

is a genuine contraction semigroup. On this space \(D=R_H\), not zero.
The result follows from the ordinary self-adjoint radial Hamiltonian and
does not exponentiate a bound along a nonnormal arithmetic flow.

This does not repair (1). For a non-harmonic closed representative, acting
by \(D\) before reducing can leave the kernel of \(\mathcal Q\). Choosing
the Hodge representative first is a different, specified procedure. It also
does not prove that the hemisphere field-coordinate norm is an isometric
realization of the physical radial norm for arbitrary states.

Using the individual nilpotent charges and their common canonical
representatives suffices for this bounded control. No additional Hodge
theorem for arbitrary equivariant or extended-operator modules is assumed.

## 3. Exact loss in the one-particle spatial channel

For the highest-H-weight free scalar, a one-particle spherical harmonic has

\[
 D=\ell+\tfrac12,\qquad R_H=\tfrac12,\qquad
 B_H=\ell,\qquad \ell=0,1,2,\ldots.
 \tag{4}
\]

The magnetic multiplicity is \(2\ell+1\). Hodge projection therefore keeps
only \(\ell=0\). The second independent Higgs scalar gives the same
statement for its flavor channel; the opposite H-weight fields do not add
higher harmonic states to this kernel. Spatial derivatives increase \(D\)
without increasing this scalar's H charge.

One can quantify the loss using the manuscript's parity-even axial
covariance. For \(u>0\), averaging aligned and antipodal directions gives

\[
 C_{\rm ev}(u)=\frac12\{C(u,1)+C(u,-1)\}
 =\sum_{n=0}^\infty e^{-(2n+1/2)u}
 =\frac{e^{-u/2}}{1-e^{-2u}}.
 \tag{5}
\]

This is an observable channel with unit coefficients, not a claim that the
full spatial Hilbert space has multiplicity one. The coincident-direction
observations are understood at \(u>0\); their singular limit is not a
normalized vector at \(u=0\).

Hodge projection and its omitted part give, respectively,

\[
 C_H(u)=e^{-u/2},\qquad
 C_{\rm omit}(u)=\frac{e^{-5u/2}}{1-e^{-2u}},\qquad
 \frac{C_{\rm omit}(u)}{C_{\rm ev}(u)}=e^{-2u}.
 \tag{6}
\]

The omitted fraction is approximately 90.48% at \(u=0.05\) and 36.79% at
\(u=0.5\), and tends to one as \(u\downarrow0\). These are fractions of the
specified covariance channel, not norm-loss estimates for arbitrary inputs.
The omitted kernel has the singular behavior

\[
 C_{\rm omit}(u)=\frac1{2u}-\frac34+O(u).
 \tag{7}
\]

In particular, it is exactly the *shape* of the positive tower in the
prime-free arithmetic mode-count test, for \(\Re p>1\):

\[
 S_\Gamma(p)=2\int_0^\infty u e^{-pu}C_{\rm omit}(u)\,du
 =2\sum_{n=1}^\infty\frac1{(p+2n+1/2)^2}.
 \tag{8}
\]

This is an explicit comparison of formulas, not a new physical identification.
The full arithmetic derivative also contains the signed pole term

\[
 (a_0^<)'(p)=S_\Gamma(p)-\frac2{(p-1/2)^2}.
 \tag{9}
\]

Nothing here treats (8) alone as positivity of (9) or of the cumulative
defect. At \(p=2\), the code verifies the exact coarse bound

\[
 \frac14<S_\Gamma(2)<\frac3{10}.
 \tag{10}
\]

Its more precise partial-sum/integral-test bounds are approximately
0.2786608238994 and 0.2786683500740. For \(N\) terms, the omitted remainder
lies strictly between \(1/(p+2N+5/2)\) and \(1/(p+2N+1/2)\); at rational
\(p\) the partial sum and these bounds are rational. Thus (10) is an exact
small comparison, not a floating-point sign inference.

The projected scalar channel has only the \(p+1/2\) denominator, whose
derivative contribution is \(2/\(p+1/2\)^2\). Removing its lowest mode leaves
zero. It cannot produce (8). At large positive \(p\), the required tower is
of order \(1/p\), while that single retained term is of order \(1/p^2\).

## 4. A trace is not the endpoint response

The protected *many-particle* space is larger than its one-particle part.
Let \(A,B\) denote the two independent dimension-one-half highest-H-weight
scalar creators of the free hypermultiplet, with flavor charges \(+1,-1\).
These symbols are not ordinary adjoints of each other. Canonically normalized
states made from \(A^aB^b\) have

\[
 D=(a+b)/2,\quad F=a-b,\quad a,b\geq0.
 \tag{11}
\]

The free Higgs chiral ring is polynomial in these two generators; the
ordinary radial inner products follow by free Wick contraction. There are
\(d+1\) states of total degree \(d\), and the refined character is

\[
 \chi_H(u,y)=\sum_{a,b\geq0}e^{-u(a+b)/2}y^{a-b}
 =\frac1{(1-y e^{-u/2})(1-y^{-1}e^{-u/2})}.
 \tag{12}
\]

At fixed flavor \(F=1\), the states are \(A^{k+1}B^k\), one at each energy
\(k+1/2\). Selecting even \(k\) yields the character in (5), and additionally
removing \(k=0\) yields (6)'s omitted tower. These are *additional selections*
of composite states. Their possible physical meaning must be specified;
the elementary scalar endpoint does not impose them. The flavor condition
and the even-\(k\) selection are recorded to prevent an overly broad claim
that the protected space contains no matching energy ladder at all.

For a normalized elementary highest-weight endpoint ket
\(E|0\rangle=|1,0\rangle\), however, the actual ordinary-adjoint radial
matrix element is simply

\[
 G_E(u)=\langle0|E^\dagger T_H(u)E|0\rangle=e^{-u/2},\qquad
 \int_0^\infty e^{-pu}G_E(u)\,du=\frac1{p+1/2}.
 \tag{13}
\]

Normalization can multiply (13) by a constant but cannot add a pole tower.
More generally, any fixed finite polynomial endpoint in this free Hodge
control produces a finite sum of exponentials. A response using an infinite
set of composite states needs an independently specified observable or
boundary coupling with its matrix elements, not just a favorable trace.

Equation (13) uses the physical radial adjoint. It is not an assertion that
the protected tilded endpoint is that adjoint, or that the same-charge
hemisphere bilocal has been embedded isometrically into this control. The
existing hemisphere result \(\widehat\Psi_{\rm pair}\propto\Gamma(s+1)\)
remains valid as a boundary amplitude. Computing a moment of its boundary
field coordinate and computing (13) are different operations.

## 5. Consequences for the overall program

The accomplishments now separate into three precise kinds.

1. **Arithmetic control.** The internally checked EMA calculation controls
   the entire input space at the fixed anchor:
   \(Q_{0,1/2}\succeq I/40\) and
   \(D_{10^{-3},1/2}\succeq0.000049998 I\). The adjoining-window work has
   shown why the scalar floor loses too much directional information:
   \(55<\|Y\|/\delta<72\), while finite actual-metric diagnostics are
   approximately 0.802. Those diagnostics are not an all-input upper bound.
2. **Physical structure.** A specified localized boundary problem really
   yields a one-sided gamma amplitude and an explicitly calculable endpoint
   insertion. Its normalization, ordering and adjoint issues have been
   exposed rather than inferred from a fitted determinant.
3. **A sharper physical obstruction.** The fixed protected representation
   fails direct radial descent. The canonical-Hodge alternative exists,
   but removes the higher one-particle angular modes needed for the tested
   arithmetic comparison. Matching a composite-state character alone
   does not restore the endpoint response.

These are improvements in control of the proposal and in the quality of its
tests. They do not establish a physical realization of the arithmetic
transfer, an arithmetic Loewner driver, a new positivity horizon, an
all-depth theorem, or RH. Smoothing loss and averaging variance have not
been counted as arithmetic positivity.

The direct mathematical next step remains an energy-weighted all-input bound
for cumulative coupling in the existing \(L=1/2,h=1/20,\omega=10^{-3}\)
append. The constant floor should be replaced by metrics retaining the join
energy, with both complements and endpoint memory controlled.

For localization, the next proposal should earn further work by specifying
one of the following and computing its actual response: retained unprotected
angular modes; an enlarged/interface sector transporting the supersymmetry
problem; or a concrete boundary observable that couples to the required
composite states. Its action on states, physical adjoint and spectral weights
must be derived. Another gamma-function or counting-character match alone
will not settle the present obstruction. Specialist review of the centered
charge and boundary-state argument remains the first external audit.

## 6. Reproduction and next-session handoff

From the investigation directory:

```sh
python3 -B numerics/check_hodge_radial_channel.py \
  --output /tmp/hodge-radial-channel-replay.json
python3 -B numerics/check_spatial_radial_descent.py \
  --output /tmp/spatial-radial-descent-replay.json
```

The new standard-library checker enumerates 25 protected degree levels,
checks the Hodge gap of 13 spatial angular levels, compares six exact channel
formulas numerically, and supplies the rational sum/integral comparison in
(10). These finite checks do not establish the supersymmetry input. The
new record is `numerics/records/hodge-radial-channel-checks-20260920.json`;
its provenance companion identifies the reviewed inputs and hashes.

Start the next session with this note, the radial-descent note and its
handoff. Retain the distinction between arbitrary representatives,
canonical Hodge states, boundary-coordinate wavefunctions, trace characters,
and ordinary-adjoint response functions. None can be substituted for another
without a proved map.

The manuscript and historical research notes are preserved. The current
inventory may be extended for these new files without relabeling the
manuscript's 299 diagnostics or its frozen version-0.4 build records.

## Primary references and attribution

- [D] Dedushenko, Pufu and Yacoby, *A one-dimensional theory for Higgs branch
  operators*, arXiv:1610.00740v2, especially the Hodge identity and primary
  representatives in §3.1 and equation (3.4):
  <https://arxiv.org/html/1610.00740v2>.
- [G] Dedushenko, *Gluing II: Boundary Localization and Gluing Formulas*,
  arXiv:1807.04278v3, free-hyper Higgs algebra and hemisphere state in §4.3.2:
  <https://arxiv.org/html/1807.04278v3>.

The Hodge and free chiral-ring inputs are established external results. The
spatial-channel comparison, its elementary response calculation and program
assessment above were prepared with the LLM recorded at the top. This is an
internal follow-up, not independent specialist approval of the program.
