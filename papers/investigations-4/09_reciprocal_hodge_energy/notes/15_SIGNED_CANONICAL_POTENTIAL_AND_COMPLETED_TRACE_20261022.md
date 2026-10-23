# Signed canonical potential and completed trace enclosure

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex), reasoning effort ultra**, verified from this turn's metadata.

**Status: fixed canonical signed potential and trace bounds interval-certified; separate same-model proof audits and replays pass.** The signed potential is now acquired on Note10's existing zero-time geometry. Combining it first with Note14's disk mass lower gives a complete trace upper. Reusing all fixed area cells gives a stronger lower and an upper for the bulk, hence a positive two-sided trace enclosure. A separate direct trace calculation is tighter and proves the physical numerator positive throughout this particular interval, without RH. This closes the finite potential/payment question, while stopping a negative-witness attempt on this exact window.

Read the [result index][results], [collision controls][controls] and [avoid index][avoid], particularly patterns01,02,05,07,08,10,11,12,13 and20. This is a quantitative finite estimating result. Known LP signs are not inputs to the acquisitions, and neither positivity nor the trace identity is counted as a new RH criterion. [Review08][review] records the separate same-model audits; no specialist human or cross-model validation is claimed.

## 1. Fixed observable and completed bounds

Keep the unchanged canonical field

\[
 H_0(z)=\xi((1+iz)/2)/8,\qquad J=H_0+iH_0',\qquad
 E=H_0^2+H_0'^2,\quad Q=H_0'^2-H_0H_0''
\]

on the physical real line. Use exactly [Note10][n10]'s C=35,
L=h=4sqrt2, rectangle Omega=(C-L,C+L)x(0,h),
psi=(1-((x-C)/L)^2)^3 and chi=(1-(y/h)^2)^3.
There is no new support, root lookup or geometry optimization. Its complete identity is

\[
 T_\psi=\int_{C-L}^{C+L}\psi\frac{Q}{\sqrt E}\,dx
       =P_\phi-M_\phi,\quad
 P_\phi=\int_\Omega |J|\Delta\phi\,dA,\quad
 M_\phi=\int_\Omega\phi\frac{|J'|^2}{|J|}\,dA.
 \tag{1}
\]

The outward endpoints below are deliberately shortened; the receipts retain exact rational endpoints.

| Quantity | Complete enclosure |
| --- | --- |
| Signed potential P_phi | [1.0703357e-4,1.0768889e-4] |
| Whole-rectangle mass M_phi | [8.1471167e-5,9.4362658e-5] |
| Area-derived trace P_phi-M_phi | [1.2670920e-5,2.6217716e-5] |
| Independent direct trace | [1.9523542e-5,1.9794809e-5] |

The potential's [first frozen contract][pc] uses192-bit Arb and at most128x64 followed, only if needed, by256x128 cells. The first8192-cell mesh passes its declared radius target5e-7; no refinement was used. Its exact potential interval is

\[
 P_\phi\in[
 0.00010703357776392685882717378096690,
 0.00010768888298556866975820630447975]. \tag{2}
\]

Using only [Note14][n14]'s previously paid
delta*=53786508896932687935920897387946891/10^40 gives

\[
 \boxed{T_\psi\le P_+-\delta_*
 <1.0231023210\times10^{-4}.} \tag{3}
\]

This is the requested original combination. It improves the potential-only upper by more than5.37865e-6, but remains over five times the direct upper. A mass lower alone supplies no trace lower endpoint: [P_--delta*,P_+-delta*] would be invalid as a trace interval.

After (2)--(3), a [separately declared fixed consumer][bc] reuses exactly the same8192 cells to pay the whole bulk. Its lower exceeds8.1471167782462868e-5, over15.147 times the previous disk lower. An acquired cell floor also permits a bulk upper below9.4362657472936912e-5. Consequently

\[
 \boxed{1.2670920290989947\times10^{-5}
 <T_\psi<2.6217715203105801\times10^{-5}.} \tag{4}
\]

This is a positive area-derived trace estimate from complete potential and bulk bounds. It is weaker than the direct reference, with upper endpoint about1.32448 times its upper and interval width about49.94 times its width. No intrinsic precision or cost advantage is claimed.

## 2. Signed potential quadrature with complete cancellation and errors

Put s=(x-C)/L, v=y/L and w(q)=(1-q^2)^3. The physical scale cancels exactly:

\[
 P_\phi=\int_{-1}^1\int_0^1
  |J(C+L(s+iv))|K(s,v)\,dv\,ds,
 \quad K=w''(s)w(v)+w(s)w''(v). \tag{5}
\]

The kernel has zero integral. On each rational cell its constant and first centered moments are integrated as polynomials, retaining the signs. The needed primitives are

\[
 F(q)=q-q^3+3q^5/5-q^7/7,\quad F'=w,
\]
\[
 G(q)=q^2/2-3q^4/4+q^6/2-q^8/8,\quad G'=qw,
 \qquad A(q)=q w'(q)-w(q),\quad A'=qw''.
\]

For axis center c, use I0=Delta F, I1=Delta G-c I0,
D0=Delta w', D1=Delta A-c D0. The cell kernel moments are

\[
 k_{00}=D_{0,s}I_{0,v}+I_{0,s}D_{0,v},\quad
 k_{10}=D_{1,s}I_{0,v}+I_{1,s}D_{0,v},\quad
 k_{01}=D_{0,s}I_{1,v}+I_{0,s}D_{1,v}. \tag{6}
\]

Arb encloses these exact rational expressions, rather than treating rounded moments as exact. The complete sum of k00 contains zero. An absolute-kernel allowance is used only for the residual: cell area times
sup|w''(s)|sup w(v)+sup w(s)sup|w''(v)| bounds its integral. This coarser cell sum is below7.36107279793; it is an upper, not the exact unsigned kernel integral.

Use the existing [degree64 complete-source oracle][core] on |z-35|<=8,
outer Cauchy radius16. Every coefficient ball remains. Let f=P64+iP64'.
Simultaneous Horner evaluation gives f0,f1,f2 at each physical cell center, and

\[
 D_3=\sum_{k\ge3}k(k-1)(k-2)|f_k|8^{k-3}
\]

bounds |f'''| on the entire source disk. True cell segments remain in that convex disk; the rectangle's corner satisfies L^2+h^2=32+32=64 exactly. Rounding supersets are not assigned new analytic source coverage.

Every first-mesh physical cell radius is r=1/16. Thus

\[
 D_1=|f_1|+r|f_2|+D_3r^2/2,\quad D_2=|f_2|+D_3r
\]

are complete polynomial derivative uppers on the cell. If the derived
m=lower(|f0|-D1 r) is positive, the Hessian of u=|f| has operator norm at most

\[
 B_2=D_2+D_1^2/m. \tag{7}
\]

Indeed a directional second derivative consists of Re(f''v^2 conjugate(f))/|f| plus a nonnegative term bounded by |f'|^2/|f|. Hence the modulus equals its affine center expansion plus a residual of magnitude at most B2 r^2/2. The normalized gradients include L:
g_s=L Re(f1 conjugate(f0))/|f0| and
g_v=L Re(i f1 conjugate(f0))/|f0|.
Integrate u0 k00+g_s k10+g_v k01 and pay the residual against the complete absolute-kernel allowance.

If m is not positive, omit the slopes and use the constant-center rule with root-free error D1 r. This fallback remains valid at arbitrary zeros. In this actual run all8192 cells independently acquire m>3.62267e-6; no fallback is required. This polynomial floor is a conclusion, not a premise of the potential algorithm.

The signed affine sum is1.0736123037474776429e-4. Complete cell residuals add a symmetric allowance below3.276527e-7. Pay the unchanged canonical source once by

\[
 \epsilon_J\|\Delta\phi\|_1
 \le(\epsilon_H+\epsilon_{H'})\frac{12288}{875\sqrt5}
 <8.03934\times10^{-19}. \tag{8}
\]

This uses the valid whole-rectangle modulus Lipschitz inequality and needs no J floor. It is not assigned to the full trace or bulk. All coefficient, summation, elementary-function and rounding errors remain in (2). The compact decimal Arb display uses a coarsely printed center and can show a larger display error; exact endpoints and the internal radius establish the frozen accuracy target.

## 3. Whole-rectangle bulk payment from the same cells

The additional contract was frozen after the positive result (2), preserving that potential receipt and the original disk-lower comparison. It introduces no new mesh, support or coefficient acquisition. For the true J, use complete errors

\[
 \epsilon_J<1.280066\times10^{-19},\qquad
 \epsilon_{J'}\le\epsilon_{H'}+\epsilon_{H''}
 <1.042216\times10^{-18}.
\]

On each cell define

\[
 B=|f_0|_{\rm up}+D_1r+\epsilon_J,\quad
 \ell=\max(0,|f_1|_{\rm lo}-D_2r-\epsilon_{J'}).
\]

Then |J|<=B and |J'|>=ell on the entire cell. Off its zeros,
|J'|^2/|J|>=ell^2/B; local integrability extends the integral inequality. No lower for J is used. The exact nonnegative cutoff integral on that cell is

\[
 W_C=32\,I_{0,s}I_{0,v}>0.
\]

Therefore the complete lower is

\[
 \boxed{M_\phi\ge\sum_C W_C\ell_C^2/B_C.} \tag{9}
\]

The physical factor32 is retained here: unlike the potential's Laplacian measure, the bulk weight alone has no inverse-square scale. Every cell has a positive derivative lower in the actual run. The sum yields the lower in Section1's bulk table without a supplied floor.

For an upper, **separately derive**
a=|f0|lo-D1 r-epsilon_J and b'=|f1|up+D2 r+epsilon_Jprime.
If every a>0, then

\[
 M_\phi\le\sum_C W_C(b'_C)^2/a_C. \tag{10}
\]

All8192 actual cells pass, with canonical |J| floor exceeding3.62267e-6. Otherwise the script reports this upper unavailable while retaining (9); it never discards failing cells. The optional upper thus requires a floor that is actually acquired, whereas (9) does not.

Combining the complete potential interval and (9)--(10) conservatively encloses their shared coefficient correlations and gives (4). This is not a source-to-bulk Lipschitz claim through a collision. The derived floors may collapse in a family approaching one; no uniform endpoint or all-height margin is inferred.

## 4. Independent direct trace and same-data mass intersection

The separate [direct contract][dc] fixes1024 real cells in s in [-1,1], one mesh with no refinement. For H,H',H'' it encloses the degree64 polynomial on each cell by centered quadratic Taylor expansion and complete third-derivative polynomial remainders (through H^(5)); it then adds the complete respective source tails. Complete real interval arithmetic supplies Q/sqrt(E), divided only after each E lower has been proved positive. Integrating psi exactly gives positive cell weights. It assumes neither RH, an LP regime, roots nor a preassigned denominator floor.

The resulting direct enclosure is

\[
 \boxed{T_\psi\in[
 1.9523542402679458754\times10^{-5},
 1.9794808859088084100\times10^{-5}].} \tag{11}
\]

Its relative width is about1.37985%. The complete cell ranges also prove

\[
 E(x)>1.33538\times10^{-11},\qquad
 Q(x)>3.43170\times10^{-12}
 \quad(C-L\le x\le C+L). \tag{12}
\]

These are finite acquired signs, not consequences of regularity or the earlier two-root count. Positivity of P alone would not prove either sign. Formula (11) is strictly inside the area-derived interval (4), so intersection retains (11). Both methods receive the same source data and every shared identity; no general method ordering follows.

Combining independently enclosed P and T with the exact identity also yields

\[
 M_\phi\in[P_--T_+,P_+-T_-]
 \subset[8.7238768\times10^{-5},8.8165341\times10^{-5}]. \tag{13}
\]

This sharper interval is a **same-data consequence of the direct trace and potential**. Feeding it back into (1) does not create an independent trace improvement. Keep it distinct from the independently paid area-cell bounds (9)--(10).

## 5. Controls and precise stopping boundary

A constant J gives P=M=T=0; the kernel's exact zero sum preserves this. For H=cos z, J=e^(-iz) and |J|=e^y. Direct integration gives

\[
 T=\|\psi\|_1,\quad
 M=\|\psi\|_1\int_0^h\chi(y)e^y\,dy,\quad P=T+M.
\]

Twice integrating chi''e^y retains the positive bottom term1, checking the half-plane normal and subtraction sign. Quadratic/Hermite collision controls obey the same Green identity with their own normalization and costs; their endpoint-sensitive trace remains compatible. Note14's smooth positive Gaussian-source control has a negative potential on an appropriate thin strip, so source positivity alone still gives no universal P sign. Euler-factor controls change the canonical arithmetic; weighted-square/finite-prime controls lack the complete canonical/reflection conjunction; reflected/primitive controls lack unchanged square coefficients. None is assigned this actual theta coefficient dataset or an invented LP hypothesis.

The first requested potential bound and original lower-mass combination are completed in (2)--(3), and whole-cell payments give the useful positive trace interval (4). The direct estimate (11) is stronger. By (12), **a negative-Q or negative-T witness on this exact physical interval and nonnegative cutoff is ruled out**. More precision on the same observable cannot turn its actual sign negative. Stop this fixed-window negative-witness attempt; this is not a no-go for other regions, signed observables, correlated estimates or hypothetical endpoint classes.

The observable is amplitude-weighted Q/sqrt(E), not the phase Q/E or BW10's different transverse remainder. A cap-surplus or simplicity claim still requires its actual physical normalization, moving-wall/time payments, event coverage and arithmetic signed input. The new finite floor neither supplies event-independent isolation nor survives a hypothetical degeneration uniformly. No new collision, additional cap pair, RH theorem or simplicity exclusion follows. The manuscript is unchanged.

The [potential script/receipt][pr], [whole-cell bulk script/receipt][br] and [direct script/receipt][dr] are small, replayable records. Separate same-model replays reproduce every potential and bulk receipt field exactly; direct arithmetic and hashes reproduce with timings allowed to vary. [Review08][review] retains these checks, the portable CLI correction for the direct script and the bulk receipt's literal-rational formatting repair. No source or geometry was changed by those output repairs.

[n10]: 10_SIGNED_JET_FLUX_AND_PHASE_TRACE_OBSTACLES_20261022.md
[n14]: 14_CANONICAL_BULK_MASS_LOWER_BOUND_20261022.md
[review]: ../reviews/08_SIGNED_POTENTIAL_AND_TRACE_REVIEW_20261022.md
[pc]: ../numerics/07_SIGNED_POTENTIAL_CONTRACT_20261022.md
[bc]: ../numerics/08_WHOLE_RECTANGLE_BULK_CONTRACT_20261022.md
[dc]: ../numerics/07_DIRECT_TRACE_REFERENCE_CONTRACT_20261022.md
[core]: ../numerics/rhe_actual_theta_core.py
[pr]: ../numerics/07_SIGNED_POTENTIAL_20261022.json
[br]: ../numerics/08_WHOLE_RECTANGLE_BULK_20261022.json
[dr]: ../numerics/07_DIRECT_TRACE_REFERENCE_20261022.json
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
