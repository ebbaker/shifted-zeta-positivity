# SUSY positivity: a high-level guide to the research program

11 September 2026; navigation updated 14 September 2026 · About 15–20 minutes

This overview explains the common research objective, how possible approaches fit together, and the choices ahead. Start with the [standalone background](background.pdf) for the shared mathematical framework. The [positive-factorizations attempt](investigations/previous/positive-factorizations/README.md) is one approach within this program; its [manuscript](investigations/previous/positive-factorizations/manuscript.pdf) contains the detailed proofs of that attempt. Its [round-4 review](investigations/previous/positive-factorizations/archive/progress-reports/REVIEW_round4_20260911.md) records subsequent results. The opening sections clarify the RH criterion, the role of the shift, and the connection to storage-depth. Later sections discuss this attempt and the preference to search for a global mechanism. Future approaches belong alongside it under `investigations/<descriptive-name>/`; see the [program guide](README.md).

This overview retains the original research framing and positive-factorizations survey. For later results through ground-state note 20, the standalone finite-response note, and the revised research priorities, use the [current program index](README.md) and [14 September assessment](brainstorm/ASSESSMENT.md).

## 1. The broad research plan

### The question we are trying to answer

The Riemann hypothesis can be expressed as a positivity statement: a particular arithmetic expression, called the **Weil quadratic form**, must assign nonnegative energy to every allowed test function. Here “energy” means a real-valued quadratic expression; we have not established that it is the energy of a physical system.

### The precise RH target: every input and every length, at zero shift

In the shared framework, also used by the positive-factorizations manuscript, the classical criterion reads

\[
\boxed{\mathrm{RH}\ \Longleftrightarrow\quad
Q_{0,L}[f]\geq0\quad\text{for every }L>0
\text{ and every }f\in C_c^\infty((-L/2,L/2)).}
\]

Here the input space consists of smooth functions supported strictly inside the interval; complex-valued inputs are allowed. Every smooth compactly supported function on the real line fits inside some such interval. Thus the length parameter simply organizes the full Weil criterion into finite intervals. An unbounded sequence of lengths suffices, because any fixed input eventually fits. [Weil's criterion and its finite-interval formulation, as presented by Suzuki](https://arxiv.org/html/2606.09096v2#S1.SS1).

The notation has three separate roles. **The zero in \(Q_{0,L}\) fixes the shift at \(\omega=0\); \(L\) is the total support length; and \(f\) is the input being tested.** Positivity is a statement about every input, not a single number obtained by choosing \(L\). It means nonnegativity, \(Q[f]\geq0\). A positive bound \(Q_{0,L}[f]\geq m_L\|f\|^2\) is useful for estimates, but the criterion does not require one common positive bound valid for all lengths.

The target is the **full central form** defined in Section 2 of the [positive-factorizations manuscript](investigations/previous/positive-factorizations/manuscript.pdf), with its fixed normalization, gamma and pole terms, and prime contributions. The gamma form \(Q^\gamma_{0,L}\) agrees with it only for \(L\leq\log2\), when no prime delay acts. At longer lengths, a factor for gamma alone does not establish the required Weil positivity.

### Why the papers also contain a shift parameter

The shifted-zeta program introduces an auxiliary family in addition to this central target. Its transfer uses the ratio

\[
\Theta_\omega(z)=
\frac{\xi(1/2-\omega-iz)}{\xi(1/2+\omega-iz)},
\qquad 0<\omega\leq\tfrac12,
\]

where \(\xi\) is the completed zeta function and \(z\) is the spectral variable. The parameter \(\omega\) shifts the two arguments on opposite sides of the central argument. Its finite-interval action is written \(V_{\omega,L}\). Increasing \(L\) allows longer inputs and more prime delays; varying \(\omega\) changes the transfer applied to those inputs. These are distinct operations. See Section 10 of the [positive-factorizations manuscript](investigations/previous/positive-factorizations/manuscript.pdf) and Section 2 of [storage-depth](../shifted-zeta/storage-depth/manuscript/storage_depth.pdf).

Three related objects must be distinguished:

| Object | What its positivity means |
|---|---|
| \(Q_{0,L}\), the central Weil form | The RH criterion requires nonnegative energy for every input at every length. |
| \(Q_{\omega,L}\), the shifted generator form | It controls the instantaneous change of squared norm as the shift varies. Positivity throughout a shift interval is a sufficient way to obtain contraction. |
| \(D_{\omega,L}=I-V_{\omega,L}^*V_{\omega,L}\), the cumulative contraction defect | It measures total input norm squared minus output norm squared. Nonnegativity on every input is equivalent to \(\lVert V_{\omega,L}\rVert\leq1\). |

In the domain and limiting sense specified in the finite-horizon papers, their connection is

\[
\begin{aligned}
\underbrace{\langle f,D_{\omega,L}f\rangle}_{\|f\|^2-\|V_{\omega,L}f\|^2}
&=2\int_0^\omega Q_{s,L}[V_{s,L}f]\,ds,\\[4pt]
Q_{0,L}[f]&=\lim_{\omega\downarrow0}
\frac{\langle f,D_{\omega,L}f\rangle}{2\omega}.
\end{aligned}
\]

for smooth compactly supported inputs. The integration variable \(s\) is a running shift. The first identity accumulates instantaneous energy along the changing input \(V_{s,L}f\). The second recovers the central form from the initial rate of norm loss. Although \(V_{0,L}=I\) and \(D_{0,L}=0\), this derivative need not vanish. These are the shift-energy identity and the central limit used in [Weil-depth](../shifted-zeta/weil-depth/finite_horizon_weil_v0.4.pdf), including its subsection “A diagonal formulation of the all-depth target.”

**RH does not require positivity of the shifted generator for every \(\omega\) and every \(L\).** That would impose an additional requirement. Storage-depth Appendix A records a negative generator direction at \(L=\log7\), \(\omega=10^{-11}\), while the cumulative defect is positive on that same input. These are recorded finite-horizon computations in the paper's working conventions; the positive defect on one input does not establish contraction on all inputs. The example explains why an instantaneous negative value away from zero shift is not a counterexample to the central Weil criterion. [Storage-depth, Appendix A](../shifted-zeta/storage-depth/manuscript/storage_depth.pdf).

### How storage-depth and the positive-factorizations attempt reach the same target

**Storage-depth's proved main route starts with the central form.** It extends certified lower bounds for \(Q_{0,L}\) by splitting a longer interval into old and new regions and controlling their coupling. The inherited estimate \(\|Q_{\omega,L}-Q_{0,L}\|\leq C_L\omega^2\) then turns a strictly positive central lower bound into generator positivity, and hence transfer contraction, for sufficiently small shifts. The allowed shift range can shrink with length. In the current storage-depth manuscript, direct cumulative-storage identities are collected in Appendix A; its main certificates establish central positivity and then derive small-shift consequences. [Storage-depth, Introduction and Section 2](../shifted-zeta/storage-depth/manuscript/storage_depth.pdf).

The transfer formulation supplies another sufficient route to RH:

\[
L_j\longrightarrow\infty,\qquad
0<\omega_j\downarrow0,\qquad
\|V_{\omega_j,L_j}\|\leq1\quad\text{for every }j
\quad\Longrightarrow\quad\mathrm{RH}.
\]

The norm condition covers every input at each selected pair. For a fixed shorter interval, causality transfers contraction from the longer horizons to that interval. The central-limit identity above then gives \(Q_{0,L}[f]\geq0\). This is why \(\omega\) appears in the storage-depth route and disappears from the final criterion: the proof sends it to zero. The implication is proved in [Weil-depth's diagonal proposition](../shifted-zeta/weil-depth/finite_horizon_weil_v0.4.pdf); constructing such an unbounded sequence remains open. If central positivity were already proved for all lengths, one could apply Weil's criterion directly.

**The positive-factorizations attempt seeks a structural explanation of the same central positivity.** Its direct RH target would be an independently defined family of positive amplitude spaces and exact identities

\[
Q_{0,L}[f]=\|A_Lf\|^2\qquad\text{for every }L>0
\text{ and every allowed input }f.
\]

Such identities on all smooth compactly supported inputs would establish RH directly. No shift parameter or passage through a contraction theorem is needed for that implication. Separate factors for each finite interval would suffice if their construction and exact matching were proved at arbitrary lengths; assembling a single closed operator on the whole line is a different, more restrictive problem, addressed by Section 9 of the manuscript.

The paper nevertheless retains \(\omega\) because it also studies the stronger local task of factoring the shifted generator. Section 3 constructs \(Q^\gamma_{\omega,L}[f]=\|\mathcal A_{\omega,L}f\|^2\) for \(L\leq1/4\) and \(0\leq\omega\leq1/2\). This is the full form in that prime-free range. At zero shift it gives central positivity; along the shift family its squared amplitudes enter the cumulative-energy integral above. Section 8's central odd factor and the later shifted odd extension provide further restricted examples. Their length and input restrictions remain essential.

The papers therefore share the same RH target and finite-horizon normalization. Storage-depth develops certified spatial extension estimates; the positive-factorizations attempt seeks an arithmetic construction whose energy identity explains the sign. It can connect directly to Weil positivity, or through a suitably proved transfer-contraction route. Neither paper has established the arbitrary-length result needed to complete either route.

### The construction sought in this program

The goal is to find a construction that explains why this energy has to be nonnegative. The intended chain is:

**Arithmetic data → an independently positive system → an exact identity with the Weil form → a theorem covering arbitrary support length.**

The positive system could involve auxiliary fields, a Hilbert-space projection, or a common collection of amplitudes whose squared sizes give the energy. Its definition must provide the reason for positivity before we identify it with the arithmetic target.

This direction grew out of earlier attempts to use higher-dimensional extensions and physical models to constrain zeta zeros. The enduring lesson was that an enlarged description needs an additional mathematical constraint to accomplish something. The earlier finite-depth program then established restricted positivity results and computational benchmarks. The present program seeks a structure that explains the sign across arbitrary lengths.

### Why supersymmetry enters

Supersymmetric quantum mechanics offers a useful template: start with an operator that produces amplitudes, and define energy as their squared norm. Schematically,

\[
Q[f]=\|Af\|^2.
\]

The right-hand side is automatically nonnegative in a positive Hilbert space. The research challenge is to define the amplitudes from arithmetic and prove that their energy equals the required expression, including every normalization, endpoint term, and prime contribution.

Supersymmetry organizes such a construction once the operator is available. It has not yet supplied the arithmetic rule that selects the operator. The models built so far are linear operator systems; an interacting supersymmetric field theory has not been constructed.

### A few terms used throughout the program

| Term | Meaning in this project |
|---|---|
| **Input or test function** | A function on which we evaluate the arithmetic energy. Positivity must hold for all allowed inputs, including complicated ones. |
| **Length, (L)** | The total width of the interval supporting the input. Larger lengths allow more arithmetic interactions. |
| **Shift, ω** | A separate parameter moving through the shifted-zeta family. Varying the shift and increasing the support length are different operations. |
| **Gamma form** | The part of our target left after omitting the explicit prime sum. In our convention it still includes the normalization and pole terms. |
| **Prime delay** | A coupling between input values separated by the logarithm of a prime power. Such a coupling becomes active when the support is long enough. |
| **Odd / even inputs** | Odd inputs change sign under reflection about the interval center; even inputs remain unchanged. Reflection lets us study these two sectors separately. |
| **Positive factor** | Explicit amplitudes whose squared sizes add up to the target energy. |

### What “global” requires

Every compactly supported input fits inside some finite interval. Consequently, a proof valid for every finite support length would establish Weil positivity. An unbounded sequence of covered lengths would also suffice, because the intervals are nested. A lower bound independent of length is unnecessary. [Weil's criterion in the finite-interval setting](https://arxiv.org/html/2606.09096v2).

The desired result could therefore be a single construction or theorem valid for arbitrary length. Checking finitely many lengths cannot establish that conclusion. Nor does dividing a long input into short pieces solve the problem: the energy contains interactions between the pieces.

**The current strategic preference is to search for the arbitrary-length mechanism first.** Small intervals and the first few prime delays remain useful places to test a specified candidate. Completing the local even-sector calculation is an available project, but it is not a prerequisite for this search. Known parity-restricted versions of Weil's criterion also make all-length odd positivity sufficient for RH; the difficult requirement remains coverage of all lengths. [Suzuki's discussion of Yoshida's criterion](https://arxiv.org/html/2606.09096v2).

## 2. The positive-factorizations attempt: how its manuscript sections fit together

The section numbers below refer to [manuscript v0.2](investigations/previous/positive-factorizations/manuscript.pdf). Its mathematical statements remain the baseline; the later background results and strategic discussion are identified separately.

| Section | High-level summary and role |
|---|---|
| **1. Motivation and the question of mechanism** | Explains the move from additional coordinates and physical analogies toward an independently positive system with an exact arithmetic identity. It establishes the research objective. |
| **2. The forms, domains, and graded convention** | Specifies the precise target and the allowed inputs. This is the accounting framework: changing the constant term, endpoints, or inner product can change the problem. It also explains the supersymmetric organization of a closed factor. |
| **3. An explicit positive factor on a small window** | Constructs an actual sum of positive energies for all inputs on a sufficiently short interval, across the stated shift range. This supplies a working example with the full required normalization. |
| **4. Two restrictions on direct scalar factors** | Shows why simple scalar changes and direct local first-order boundary operators cannot provide certain proposed factorizations. It narrows the class of constructions worth pursuing. |
| **5. A positive auxiliary-field realization of the gamma kinetic term** | Builds the kinetic part by minimizing positive local energies over additional fields. It demonstrates how an enlarged positive system can generate the required nonlocal behavior. Completing the remaining terms is a separate task. |
| **6. A comparison-form obstruction to pairwise factors** | Excludes a broad family of constructions assembled from independent two-point squares. Adding hidden nodes to finite networks of that type retains the restriction. A successful model needs more collective mixing. |
| **7. Coherent couplings and two completion constraints** | Shows, through a toy model, how several amplitudes entering the same square can escape the pairwise restriction. It then identifies problems with a proposed boundary propagator and with attaching primes through a simple extra channel. |
| **8. Reflection folding and an explicit odd-sector completion** | Uses reflection to construct a complete factor on odd inputs in a restricted length range. It also proves that the first prime can rescue a negative gamma direction and identifies the two reflected channels on which the prime has opposite effects. |
| **9. The input space of a global norm identity** | Rules out a single closable norm factor on ordinary whole-line (L^2), with all smooth compactly supported inputs in its domain. This constrains a global operator realization while leaving finite-interval families and other suitable input spaces available. |
| **10. What a useful supersymmetric completion must establish** | States the exact matching and structural requirements for a successful model. Its proposed local milestones should now be read alongside the later preference to search first for an arbitrary-length principle. |
| **Appendices A–C** | Record rational certificates, identity checks, provenance, and remaining review. They support the claims and distinguish proved scalar bounds from numerical diagnostics. |

The overall argument moves from **defining the target**, to **constructing positive ingredients**, to **excluding insufficient models**, and finally to **specifying what a successful completion must explain**. The odd factor is a concrete success within this process. It does not yet supply the rule connecting all lengths and all prime delays.

The newer [shifted odd note](investigations/previous/positive-factorizations/archive/progress-reports/SHIFTED_ODD_FACTOR_round4_20260911.md) extends Section 8 across the shift parameter. The [even-sector note](investigations/previous/positive-factorizations/archive/progress-reports/EVEN_SECTOR_REDUCTION_round4_20260911.md) establishes a positive subspace and isolates the remaining even condition. These results have not been incorporated into the manuscript.

## 3. What is established, what remains, and ideas for proceeding

### What the positive-factorizations attempt has accomplished

**The positive-factorizations attempt has constructed several positive ingredients.** There is an explicit factor for the full form on very short intervals, and an auxiliary-field model for the gamma kinetic term. Reflection then gives a complete odd-sector gamma factor. Round 4 extends that factor uniformly over shifts from 0 to ½, for total lengths up to 0.7. It represents the full Weil form only through the prime-free cutoff, \(L\leq\log 2\), approximately 0.693.

**We have proved that several natural completion strategies fail.** Independent two-point squares cannot reproduce the full target in the demonstrated range. Finite hidden-node networks of that kind do not evade the restriction. Certain boundary and first-prime constructions also fail. These results concern specified classes of models; they do not establish negativity of the Weil form.

**We have made prime cooperation concrete.** On one explicit input at length 1, gamma has negative energy and adding the first prime makes the full energy positive. The signs have exact rational certificates. Folding shows precisely which channel the prime stabilizes and which it destabilizes. A joint model must account for both.

**We have separated a substantial positive part of the even sector.** Even inputs with mean zero have a certified positive lower bound in the stated small-length range. The remaining sign is determined by one scalar measuring how strongly the constant input couples to that subspace. Finding the response to this coupling would let us evaluate or bound the scalar. The response has not been constructed explicitly, and the scalar sign has not been settled by this reduction. An explicit factor for the positive subspace also remains to be supplied.

**We have identified why a tempting even simplification is unsafe.** Replacing the smooth kernel and pole amplitude by constants makes a simple even polynomial have negative energy in the simplified model. Those apparently small details can determine the sign and must be retained or controlled.

These are working mathematical results with written derivations. All three original checkers were replayed successfully. The new scalar certificates also pass, with separate floating-point identity diagnostics. Independent specialist review and a complete priority audit remain outstanding. No all-length positivity theorem or RH proof has been obtained. The new factors do not extend the positivity range already certified by the earlier finite-depth work. See the [review](investigations/previous/positive-factorizations/archive/progress-reports/REVIEW_round4_20260911.md) and [verification record](investigations/previous/positive-factorizations/archive/progress-reports/REPRODUCIBILITY_round4_20260911.md).

### The outstanding challenges

| Challenge | What still needs to be explained |
|---|---|
| **The arithmetic selection rule** | Why a particular positive system produces exactly the gamma, pole, and prime contributions. Positivity of the auxiliary system alone cannot establish the matching. |
| **The first-prime joint construction** | How one common energy controls the channel the prime destabilizes while benefiting from the channel it stabilizes. Gamma cannot be assumed independently positive throughout that interval. |
| **Compatibility across multiple delays** | How several overlapping arithmetic interactions fit the same construction without spending the same positive contribution more than once or creating unwanted mixed terms. |
| **Coverage of arbitrary lengths** | A general identity or extension law that remains valid as additional interactions appear. We currently have no such law. |
| **Almost-zero directions** | Why the increasingly small energies seen in the earlier work arise naturally in the proposed positive system. Every nonnegative component energy must be correspondingly small on those inputs. |
| **The appropriate global setting** | Which input space or family of finite-interval systems supports the intended realization, consistently with the whole-line (L^2) obstruction. |

The hardest unresolved issue is the common structure connecting these requirements. A more accurate even response calculation could resolve a local question while leaving that issue untouched.

### Ideas for proceeding

The next investigation should begin by specifying a candidate positive object and the rule intended to identify it with the arithmetic form at arbitrary length. Three architectures deserve consideration:

1. **A common arithmetic amplitude construction.** Define amplitudes from translations, dilations, or other arithmetic operations and derive their joint squared energy. The key question is whether arithmetic relations force the mixed terms to have exactly the required coefficients.
2. **A positive projection or trace construction.** Start from positivity of a Hilbert-space compression and derive the arithmetic expression, including any correction. Connes and Consani's Sonin-space work provides a relevant example of this architecture; its stated hypotheses and correction terms remain essential. [Archimedean trace-formula paper](https://arxiv.org/html/2006.13771v1).
3. **A positive gluing or evolution law.** Specify energy associated with an interface or added region and prove a rule extending the construction to larger supports. The rule must control interactions across the interface without assuming the enlarged form is already positive.

These are candidate architectures, not global mechanisms we have discovered. They also need to be compared carefully with existing work. Prime stabilization already appears in Connes and Consani's published experiments, so our certified example should be presented as an explicit witness and design constraint. [Spectral triples and zeta-cycles, Sections 2.2–2.4](https://ems.press/content/serial-article-files/44477).

For each candidate, the first-prime and mixed-delay cases can serve as bounded tests of a claimed rule. A useful calculation would reject an inconsistent model, check a proposed exact identity, or distinguish two mechanisms. Its purpose should be stated before undertaking it.

The optional even-response project should be resumed if it helps identify that common structure or test a candidate. Increasing the certified length, refining a numerical margin, or obtaining another local factor would not alone justify making it the main research direction.

**The decision standard for the next step is whether it gives us a reason the arithmetic matching and positivity must persist at arbitrary length.** A proposal can be valuable even if it fails, provided the failure rules out a clear class of mechanisms or identifies the missing structural ingredient.
