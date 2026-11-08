# B03 r5: a complete positive Green-strip potential

6 November 2026 America/New_York (7 November UTC). Prepared for **Edward Baker** with substantial Codex assistance. Lead author/checker tool-selected **gpt-6-astra/ultra**. The root coordinator performed the independent read-only derivation under request29 and returned its proof and constants; its backend/model/effort is not inferred here. These are internal shared-premise checks, not specialist review. E16 is to assess the exact resulting note.

**Proved in-note:** a positive, scale-invariant, exponentially localized nonreal-zero potential equals an explicit difference of complete-theta logarithmic averages. Both boundary integrals and the complete zero sum have uniform quantitative tails. Its acquired coarse upper bound does not exclude one defect. This is the second metric already compared in Decision14, independent of E15's Gaussian Laguerre hierarchy; no novelty claim or canonical exclusion is made.

[Request29](../research-progress/handoffs/29_TND_O_B03_R5_GREEN_STRIP_CHECK_REQUEST_20261107.md) and [inputs29](../research-progress/handoffs/29_TND_O_B03_R5_GREEN_STRIP_CHECK_INPUTS_20261107.json) froze the bounded read-only check. Root verified all six inputs before and after its work and changed no file. This lead-owned note records the complete derivation rather than treating the preliminary comparison as a proof. The earlier half-plane suggestion is replaced here by a finite-height infinite strip, whose boundary kernels have exponential horizontal decay.

## 1. Exact statement and normalization

Use the canonical family

\[
 H_0(z)=\tfrac18\xi(\tfrac12+iz/2),\qquad
 H_\lambda(z)=\tfrac12\int_{\mathbb R}e^{\lambda u^2}\Phi(u)e^{izu}\,du,
 \qquad 0\le\lambda\le\tfrac12.
\]

Its zeros, counted with multiplicity, lie in \(|\Im z|\le1\). The complete even product, source majorant and full count from [Note17](17_TND_O_E08_LOCALIZED_TRANSVERSE_CALCULUS_20261107.md) are used; the unit count and safe-line estimate from [Note18](18_TND_O_E10_CANONICAL_MODULUS_AND_SHARPNESS_20261107.md) are used with their paid time-zero endpoints. Write

\[
 a=\pi/8,\qquad K(t)=\frac1{16\cosh(at)},\qquad
 G(d,y)=\operatorname{atanh}\!\left(\frac{\sin(ay)}{\cosh(ad)}\right).
 \tag{1}
\]

Each boundary kernel has mass \(\int K=1/2\). Define

\[
\begin{split}
 J_\lambda(X)={}&\int_{\mathbb R}K(x-X)
       \{\log|H_\lambda(x)|+\log|H_\lambda(x+8i)|\}\,dx\\
       &-\log|H_\lambda(X+4i)|.
\end{split}
 \tag{2}
\]

For every real center \(X\), both boundary integrals are absolutely integrable, including at real multiple zeros, and

\[
 \boxed{J_\lambda(X)=\sum_{j:y_j(\lambda)>0}G(X-x_j(\lambda),y_j(\lambda)).}
 \tag{3}
\]

The upper-zero sum is complete and absolutely convergent. Upper zeros satisfy \(0<y_j\le1\), so every term is strictly positive. There is no contribution from real boundary zeros and no extra harmonic or outer-factor correction. Multiplying the entire field by any nonzero scalar changes the two terms in (2) by the same amount and leaves \(J\) invariant.

This is a positive **one-point nonreal-zero potential**, not a pair-correlation statistic. It differs from the earlier smooth transverse moment and from the signed Gaussian Laguerre defect.

## 2. The finite-factor Green identity

On \(0<\Im z<B\), the strip Green kernel with convention \(-\Delta G_B=2\pi\delta\) is

\[
 G_B(z,\zeta)=\frac12\log
 \frac{\cosh(\pi(\Re z-\Re\zeta)/B)-\cos(\pi(\Im z+\Im\zeta)/B)}
      {\cosh(\pi(\Re z-\Re\zeta)/B)-\cos(\pi(\Im z-\Im\zeta)/B)}.
 \tag{4}
\]

Map the strip to the upper half-plane by \(e^{\pi z/B}\) and use the logarithm of the reflected-distance ratio. This derives (4), its zero boundary values and its logarithmic singularity. The boundary normal derivatives divided by \(2\pi\) give the strip Poisson kernels. At \(B=8\), \(z=X+4i\), the kernels on both horizontal boundaries are precisely \(K(x-X)\), and (4) at an interior zero becomes (1).

For a linear factor \(z-\zeta\), the harmonic function is
\(\log|z-\zeta|+G_B(z,\zeta)\) when \(\zeta\) lies inside the strip: the singularities cancel. Its boundary values are those of \(\log|z-\zeta|\). Uniqueness among harmonic functions of logarithmic growth gives its Poisson representation. Equivalently, truncate by vertical sides; their harmonic measures decay exponentially while the linear-factor logarithms grow only logarithmically, so those terms vanish. It follows that the boundary Poisson average minus the interior logarithm equals \(G_B\). For a zero outside the strip, the logarithm is already harmonic and the difference is zero. A zero on a horizontal boundary is handled by its locally integrable logarithm, or an exterior limit; it contributes no interior or half-weight atom.

The canonical product is

\[
 H_\lambda(z)=H_\lambda(0)
       \prod_{\zeta\in\mathcal R_\lambda}\left(1-\frac{z^2}{\zeta^2}\right),
 \tag{5}
\]

where \(\mathcal R_\lambda\) contains one representative of each opposite pair, with multiplicity. For each finite complete opposite-paired product, apply the linear-factor identity to \(z-\zeta\), \(z+\zeta\) and the constant. Since both boundary masses sum to one, constant factors cancel exactly. The finite result is (3) restricted to the upper zeros of that product. The next section pays the full-product limit and all boundary interchanges.

## 3. Uniform logarithmic integrability from the complete product

Fix the full-count constant

\[
 N_\lambda(r)\le C r\log(r+2),\qquad r\ge1,
 \tag{6}
\]

from Note17, increasing it if needed. Full-source bounds and positivity give

\[
 m_0=\inf_{0\le\lambda\le1/2}H_\lambda(0)>0,\qquad
 D_0\ge\sup_{\lambda,|z|\le1}|H_\lambda'(z)|<\infty.
\]

Choose \(D_0>0\) and

\[
 r_* =\min(1,m_0/(2D_0)),\quad
 C_0=\sup_\lambda|\log H_\lambda(0)|,\quad
 C_*=C_0+20C(1+|\log r_*|).
 \tag{7}
\]

There are no zeros in \(|z|\le r_*\), since the segment integral of \(H'\) gives \(|H_\lambda(z)|\ge m_0/2\). All constants are independent of height and time.

For any real \(q\), \(0\le b\le8\), put \(Q=|q|+12\ge12\). Then

\[
 \int_q^{q+1}|\log|H_\lambda(x+ib)||\,dx
 \le C_* Q\log^2(3Q).
 \tag{8}
\]

In fact the following proof bounds the sum of the absolute factor logarithms. On the interval, \(|x+ib|\le Q\). For representatives \(|\zeta|\le2Q\), split the factor log into two distance logs and \(-2\log|\zeta|\). Each distance's positive log is at most \(\log(3Q)\), and

\[
 \int_q^{q+1}\log^-|x+ib-\zeta|\,dx\le2.
\]

Indeed distance is at least \(|x-\Re\zeta|\), and the integral of \(-\log|t|\) on \((-1,1)\) is two. This bound includes repeated and boundary zeros. The factor therefore costs at most

\[
 4\log(3Q)+4+2|\log r_*|.
\]

There are at most \(CQ\log(2Q+2)\) such representatives, by half the full count. For far representatives \(|\zeta|>2Q\),

\[
 \left|\log\left|1-\frac{z^2}{\zeta^2}\right|\right|
 \le\frac43\frac{Q^2}{|\zeta|^2}.
\]

Partial summation of (6), again taking half the full count, bounds their total by

\[
 \frac23 C Q\{\log(2Q+2)+1\}.
\]

These estimates imply (8) with the deliberately coarse constant (7). They prove absolute local \(L^1\) convergence of the product logarithms. Summing intervals against the exponential kernel gives absolute weighted \(L^1\) convergence as well. At \(X+4i\) the product converges away from every zero. This justifies the finite-factor sum/integral limit in (3); no uncontrolled infinite rectangle or outer term is left.

There is an explicit two-boundary truncation error. For \(R\ge0\), put
\(n=\lfloor R\rfloor\), \(q_0=e^{-a}\), \(S=|X|+13+n\). Then

\[
\begin{split}
 &\int_{|x-X|>R}K(x-X)
   \{|\log|H_\lambda(x)||+|\log|H_\lambda(x+8i)||\}\,dx\\
 &\qquad\le\frac{C_*}{2}e^{-an}S\log^2(3S)
             \frac{1+4q_0+q_0^2}{(1-q_0)^4}.
\end{split}
 \tag{9}
\]

For each shell \(k\le|x-X|<k+1\), use two unit intervals and \(K\le e^{-ak}/8\). Both boundaries double the cost. The remaining estimate follows from
\((S+j)\log^2(3(S+j))\le S\log^2(3S)(1+j)^3\) and
\(\sum_{j\ge0}q_0^j(1+j)^3=(1+4q_0+q_0^2)/(1-q_0)^4\).
Its constants are uniform in \(\lambda,X,R\); the displayed height factor is retained when choosing joint limits.

## 4. Complete-zero tail, positivity and the one-defect margin

Since \(\operatorname{atanh}q\le q/(1-q^2)\) for \(0\le q<1\),

\[
 0<G(d,y)\le K_G y e^{-a|d|},\qquad
 K_G=\frac{2a}{\cos^2a},\qquad0<y\le1.
 \tag{10}
\]

Use Note18's uniform unit-count constant \(A\), all multiplicities included. Let \(Q_X=3+|X|\), \(n=\lfloor R\rfloor\). The omitted upper zeros at \(|x_j-X|>R\) contribute at most

\[
 2AK_G e^{-an}
 \left\{\frac{\log Q_X+\log(n+1)}{1-q_0}
       +\frac{q_0}{(n+1)(1-q_0)^2}\right\}.
 \tag{11}
\]

To obtain this, cover both sides by unit shells, use
\(\log(Q_X+k)\le\log Q_X+\log(k+1)\), and apply
\(\log(n+j+1)\le\log(n+1)+j/(n+1)\). In particular,

\[
 0\le J_\lambda(X)\ll_A\log(3+|X|)
 \tag{12}
\]

uniformly on the complete time interval. The two errors (9) and (11) are different: one truncates boundary log integrals, the other truncates the zero statistic. Both are explicit and may be chosen as height grows.

An upper zero with \(y_j\ge d>0\) and \(|x_j-X|\le r\) contributes at least

\[
 G(X-x_j,y_j)\ge\frac{\sin(a)d}{\cosh(ar)}.
 \tag{13}
\]

Here \(\operatorname{atanh}q\ge q\), and concavity gives \(\sin(ay)\ge y\sin a\) on \([0,1]\). Thus an independently obtained upper bound for (2) strictly below (13) excludes that declared defect class. No such small signed bound has been acquired. Positivity is exact: \(J=0\) for an all-real slice, and \(J>0\) at every center if an upper zero exists. Universal vanishing is therefore an RH-type reformulation on the zeta slice, not an independently established restriction.

## 5. Theta acquisition and collision behavior: what is and is not paid

The complete source gives the finite uniform boundary majorant

\[
 S_8=\int_{\mathbb R}e^{u^2/2+8|u|}\Phi(u)\,du,
 \qquad |H_\lambda(x+ib)|\le S_8/2\quad(0\le b\le8).
\]

Consequently each boundary logarithm has the upper bound \(\log(S_8/2)\). On the existing safe line,

\[
 \log|H_\lambda(X+4i)|
 \ge\log H_\lambda(4i)-A|X|\log(2+|X|),
 \tag{14}
\]

by integrating the real part of the logarithmic derivative from zero. These separate absolute estimates are much too coarse to put (2) below (13), as is the better count-based bound (12). The missing quantity is an accurate **signed logarithmic boundary/interior comparison**, including its relative control near small real-axis values. The exact complete-source representation does not make that comparison automatic.

In particular a finite-source approximation cannot be inserted inside the logarithm near real zeros merely because an absolute \(H\)-tail is small. The complete product and logarithmic integrability above justify the exact formula; they do not supply an unproved approximation margin.

Uniform tails and finite-root continuity imply continuity of \(J_\lambda(X)\) through collisions. They do not give the earlier \(y^2\) moment's Lipschitz law. At a real double event, the upper root on the nonreal side has height proportional to the square root of reverse time; since (1) is linear in \(y\) at zero, its contribution has the same square-root leading scale. No monotonicity or Lipschitz claim is made. Real multiplicities are counted correctly: for \((z-r)^2\), the potential is zero; for \((z-r)^2+d^2\), it is exactly one upper contribution \(G(X-r,d)\). This is an analytic factor check, not a numerical experiment or canonical-control assertion.

The result supplies a second exact bridge between complete theta data and localized nonreal zeros, with a different acquisition problem from the Gaussian derivative hierarchy. It does not establish the missing signed comparison or a collision exclusion. Classical Green–Jensen theory is used with its normalization derived above; no novelty is claimed. [Result index](../../../../../result-summaries/README.md), [controls12](../../../../../result-summaries/12_collision_controls_and_screening.md), [pattern index](../../../../../avoid/README.md), [target classification](../../../../../avoid/01_restating_the_target.md) and [scoped-failure rule](../../../../../avoid/07_scoped_exclusions_read_as_universal.md) retain their meanings.

The read-only root check and lead derivation check covered the sign/normalization, two boundary masses, real-zero logarithms, complete product limit, both tails, defect margin and square-root limitation. One wording correction in the read-only return was made before this note: the harmonic single-factor correction adds G_B to log|z−zeta|; the boundary-minus-interior identity and all constants were unchanged. Root confirmed that correction. This note awaits E16; no source transcript, external numerical constant, third-party file, commit or push was created.
