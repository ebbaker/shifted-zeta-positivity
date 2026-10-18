#!/usr/bin/env python3
"""Bounded complete-theta jet certificates for overview 02.

Prepared for Edward Baker, 18 October 2026, with substantial LLM assistance.
Authoring model gpt-6.1-sol, actual effort max. Requires python-flint 0.9.0.
This is an internal interval certificate, not an RH or Newman-bound claim.
See notes/02_updated_research_plan/07_* for the complete error derivation.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import platform
import time

import flint
from flint import acb, arb, ctx


def A(value):
    return arb(value.numerator) / value.denominator if isinstance(value, F) else arb(value)


def box(lo, hi):
    lo, hi = F(lo), F(hi)
    if lo > hi:
        raise ValueError('reversed interval')
    return arb(A((lo + hi) / 2), A((hi - lo) / 2))


def rec(value):
    return value.str(35, more=True)


def check(condition, name):
    if not condition:
        raise ArithmeticError(name)


def poly(coefficients, argument):
    result = coefficients[-1]
    for coefficient in reversed(coefficients[:-1]):
        result = result * argument + coefficient
    return result


def square(value):
    """Outward real square, including balls centred exactly at zero.

    python-flint 0.9.0's native arb ** 2 returns NaN on such a ball.
    Squaring exact nonnegative endpoints avoids that failure and retains
    the true nonnegative square range instead of multiplying dependencies.
    """
    if not isinstance(value,arb) or not value.is_finite():
        raise ValueError('a finite real interval is required')
    lower=(value.abs_lower()*value.abs_lower()).lower()
    upper=(value.abs_upper()*value.abs_upper()).upper()
    return arb((lower+upper)/2,((upper-lower)/2).upper())


def coordinate_separator(values):
    if len(values) < 2 or any(not isinstance(value, arb) or not value.is_finite() for value in values):
        raise ValueError('a finite real first jet is required')
    choices = [(value.abs_lower(),j,1 if value>0 else -1)
               for j,value in enumerate(values[:2]) if value>0 or value<0]
    return max(choices,key=lambda item:float(item[0])) if choices else None


def laguerre_excess(values, constant):
    if len(values) != 3 or any(not isinstance(value, arb) or not value.is_finite() for value in values):
        raise ValueError('three finite real jet components are required')
    energy = square(values[0])+square(values[1])
    return square(values[1])-values[0]*values[2]-A(constant)*energy


class Evaluator:
    """One frozen contour and one Taylor centre on a rational rectangle.

    Midpoint jets belong to the finite, cutoff integral, which itself solves
    the heat equation. Mode and source-cutoff tails are paid directly at the
    consumer cell. Higher midpoint jets therefore need no tail substitution.
    """

    def __init__(self, method='shifted', tlo=F(1, 100), thi=F(1, 5),
                 xlo=F(25), xhi=F(45), degree_x=50, degree_t=12,
                 bits=160, modes=4, cutoff=F(1), max_component=2):
        if method not in ('shifted', 'real'):
            raise ValueError('unknown evaluator')
        if not (0 <= tlo <= thi <= F(1, 2) and 0 <= xlo < xhi):
            raise ValueError('unsupported domain')
        if modes != 4 or cutoff != 1:
            raise ValueError('this checked implementation uses four modes and cutoff one')
        ctx.prec = bits
        self.method, self.bits = method, bits
        self.tlo, self.thi, self.xlo, self.xhi = tlo, thi, xlo, xhi
        self.tc, self.xc = (tlo + thi) / 2, (xlo + xhi) / 2
        self.L, self.K = degree_x, degree_t
        self.N, self.U, self.J = modes, cutoff, max_component
        self.maximum_midpoint_order = degree_x + 2 * degree_t + max_component
        self.maximum_remainder_order = degree_x + 2 * (degree_t + 1) + max_component
        self.pi, self.d = arb.pi(), arb.pi() / 16
        self.c = (4 * self.d).cos()
        self.rel_tol, self.abs_tol = arb('1e-28'), arb('1e-35')
        self.calls, self.rejected, self.max_depth = 0, 0, 0
        self.quadrature_callbacks = 0
        self.factorials = [math.factorial(i) for i in range(self.maximum_remainder_order + 1)]
        started = time.monotonic()
        self.admissibility()
        self.midpoints, self.quad_radii = [], []
        self.jet_seconds = []
        for j in range(self.maximum_midpoint_order + 1):
            begin = time.monotonic()
            def integrand(u, analytic):
                self.quadrature_callbacks += 1
                if method == 'shifted':
                    v = u + acb(0, self.d)
                    q = (4 * v).exp()
                    total = acb(0)
                    for n in range(1, self.N + 1):
                        lam = self.pi * n * n
                        total += (2 * lam * lam * q * q - 3 * lam * q) * (-lam * q).exp()
                    return (A(self.tc) * v * v + v + acb(0, A(self.xc)) * v).exp() * total * (acb(0, 1) * v) ** j
                q = (4 * u).exp()
                total = acb(0)
                for n in range(1, self.N + 1):
                    lam = self.pi * n * n
                    total += (2 * lam * lam * q * q - 3 * lam * q) * (-lam * q).exp()
                phase = A(self.xc) * u
                trig = (phase.cos, phase.sin, phase.cos, phase.sin)[j % 4]()
                if j % 4 in (1, 2):
                    trig = -trig
                return (A(self.tc) * u * u + u).exp() * total * u ** j * trig
            value = acb.integral(integrand, 0, A(cutoff), abs_tol=self.abs_tol,
                                 rel_tol=self.rel_tol, eval_limit=200000, depth_limit=30)
            check(value.is_finite(), 'nonfinite midpoint integral ' + str(j))
            if method == 'real':
                check(value.imag.contains(0), 'real integral acquired nonreal component')
            # For real tc,xc the two shifted halves are exact conjugates,
            # including the factors (i(u+id))^j and (-i(u-id))^j.
            self.midpoints.append(value.real.mid())
            self.quad_radii.append(value.real.rad().upper())
            self.jet_seconds.append(time.monotonic() - begin)
        self.integral_seconds = sum(self.jet_seconds)
        self.moments = {Y: self.moment_bound(Y) for Y in (0, 1)}
        self.construction_seconds = time.monotonic() - started
        self._coeff_cache = {}

    def admissibility(self):
        m, Y, T = self.N + 1, 1, A(self.thi)
        b = 4 * self.c * self.pi * m * m - 9 - Y
        ratio = (arb(m + 1) / m) ** 4 * (-self.c * self.pi * (2 * m + 1)).exp()
        check(self.d > 0 and self.d < self.pi / 8, 'source shift outside holomorphic strip')
        check(b > 0 and 8 * self.c * self.pi * m * m >= T and ratio < 1,
              'actual interval shifted-tail admissibility failed')
        self.admissible = {'b_lower': rec(b.lower()), 'time_condition_lower': rec((8*self.c*self.pi*m*m-T).lower()),
                           'ratio_upper': rec(ratio.upper()), 'shift': rec(self.d), 'cos_4d': rec(self.c)}

    def moment_bound(self, Y):
        """Uniform finite-integral absolute derivatives through the required order."""
        T = A(self.thi)
        if self.method == 'real':
            betas = sum(((4*self.pi*n*n-1)*(-self.pi*n*n).exp()
                         for n in range(1, self.N+1)), arb(0))
            # On u in [0,1], u^j<=1; source positivity gives the beta/8 mass.
            return ((T+Y).exp()*betas/8).upper()
        r = arb(3)/4
        check(r+self.d < 1, 'short-range moment split failed')
        order = self.maximum_remainder_order
        def positive_majorant(u, analytic):
            total = acb(0)
            for n in range(1, self.N+1):
                lam = self.pi*n*n
                total += (2*lam*lam+3*lam)*(T*u*u+(9+Y)*u-self.c*lam*(4*u).exp()).exp()
            return total
        core = acb.integral(positive_majorant, 0, r, abs_tol=arb('1e-35'),
                            rel_tol=arb('1e-28'), eval_limit=200000, depth_limit=30)
        check(core.is_finite() and core.imag.contains(0), 'moment-majorant integration failed')
        extra = arb(0)
        for n in range(1, self.N+1):
            lam = self.pi*n*n
            for power in (0, order):
                denom = 4*self.c*lam*(4*r).exp()-9-Y-2*T*r-power/(r+self.d)
                check(denom > 0 and 16*self.c*lam*(4*r).exp() > 2*T,
                      'moment-tail tangent not decaying/concave')
                extra += (2*lam*lam+3*lam)*(r+self.d)**power*(T*r*r+(9+Y)*r-self.c*lam*(4*r).exp()).exp()/denom
        # (u+d)^j<=1 for u<=r, and <=1+(u+d)^order for u>=r.
        # The e^-dx factor is bounded at the LEFT edge of the whole rectangle.
        return ((-self.d*A(self.xlo)).exp()*(core.real+extra)).upper()

    def tails(self, xleft, Y):
        T, pi, m, U = A(self.thi), self.pi, self.N+1, A(self.U)
        mode, source = [], []
        if self.method == 'shifted':
            b = 4*self.c*pi*m*m-9-Y
            ratio = (arb(m+1)/m)**4*(-self.c*pi*(2*m+1)).exp()
            check(b > 0 and ratio < 1 and 8*self.c*pi*m*m >= T, 'cell mode-tail rejection')
            S = (2*(pi*m*m)**2+3*pi*m*m)*(-self.c*pi*m*m).exp()/(1-ratio)
            spectral = (-self.d*A(xleft)).exp()
            for j in range(self.J+1):
                mode.append((spectral*S*sum((math.comb(j,k)*self.d**(j-k)*math.factorial(k)/b**(k+1)
                                            for k in range(j+1)),arb(0))).upper())
                tail = arb(0)
                for n in range(1, self.N+1):
                    lam = pi*n*n
                    denom = 4*self.c*lam*(4*U).exp()-9-Y-2*T*U-j/(U+self.d)
                    check(denom > 0 and 16*self.c*lam*(4*U).exp() > 2*T, 'retained source-tail tangent failed')
                    tail += (2*lam*lam+3*lam)*(U+self.d)**j*(T*U*U+(9+Y)*U-self.c*lam*(4*U).exp()).exp()/denom
                source.append((spectral*tail).upper())
            return mode, source
        ratio = 4*(-pi*(2*self.N+3)).exp()
        check(ratio < 1, 'real mode-tail ratio failed')
        beta_tail = 4*pi*m*m*(-pi*m*m).exp()/(1-ratio)
        tail_mode = (T+Y).exp()*beta_tail/8
        e4 = arb(4).exp()
        source_ratio = 16*(-3*pi*e4).exp()
        check(source_ratio < 1, 'real source-tail ratio failed')
        for j in range(self.J+1):
            denom = 4*pi*e4-9-Y-j-2*T
            check(denom > 0 and 16*pi*e4 > 2*T, 'real source-tail tangent failed')
            tail_source = 2*pi*pi*(T+9+Y-pi*e4).exp()/denom/(1-source_ratio)
            mode.append(tail_mode.upper())
            source.append(tail_source.upper())
        return mode, source

    def coefficients(self, dt, j, time_first):
        if time_first:
            return [poly([(-1)**k*self.midpoints[l+2*k+j]/self.factorials[k]
                          for k in range(self.K+1)],dt)/self.factorials[l]
                    for l in range(self.L+1)]
        return None

    def enclose(self, t0, t1, x0, x1, y0=F(0), y1=F(0)):
        check(self.tlo <= t0 <= t1 <= self.thi and self.xlo <= x0 <= x1 <= self.xhi,
              'cell outside frozen evaluator rectangle')
        check(F(-1) <= y0 <= y1 <= F(1), 'imaginary cell outside validated strip')
        self.calls += 1
        dt = box(t0,t1)-A(self.tc)
        dx = box(x0,x1)-A(self.xc)
        complex_cell = y0 != 0 or y1 != 0
        if complex_cell:
            dx = acb(dx,box(y0,y1))
        Y = 1 if complex_cell else 0
        RX = max(abs(x0-self.xc),abs(x1-self.xc))
        RY = max(abs(y0),abs(y1))
        radius = (A(RX)**2+A(RY)**2).sqrt()
        time_radius = max(abs(t0-self.tc),abs(t1-self.tc))
        time_weights = [A(time_radius)**k/self.factorials[k] for k in range(self.K+1)]
        space_weights = [radius**l/self.factorials[l] for l in range(self.L+1)]
        tail_mode, tail_source = self.tails(x0,Y)
        remainder = self.moments[Y]*(radius**(self.L+1)/self.factorials[self.L+1]
                     +radius.exp()*A(time_radius)**(self.K+1)/self.factorials[self.K+1])
        values, budgets = [], []
        for j in range(self.J+1):
            if t0 == t1:
                key = (t0,j)
                if key not in self._coeff_cache:
                    self._coeff_cache[key] = self.coefficients(dt,j,True)
                central = poly(self._coeff_cache[key],dx)
            else:
                coefficients = [poly([self.midpoints[l+2*k+j]/self.factorials[l]
                                      for l in range(self.L+1)],dx)/self.factorials[k]
                                for k in range(self.K+1)]
                central = poly(coefficients,-dt)
            quadrature = sum((self.quad_radii[l+2*k+j]*time_weights[k]*space_weights[l]
                              for k in range(self.K+1) for l in range(self.L+1)),arb(0)).upper()
            total = (tail_mode[j]+tail_source[j]+quadrature+remainder).upper()
            error_ball = arb(0,total)
            values.append(central+acb(error_ball,error_ball) if complex_cell else central+error_ball)
            budgets.append({'mode':tail_mode[j], 'source':tail_source[j],
                            'quadrature_with_internal_rounding':quadrature,
                            'taylor_propagation':remainder.upper(), 'total_added_error':total,
                            'polynomial_enclosure':central})
        return values,budgets

    def pilot(self, signed_constant=None, max_depth=24, seconds_limit=30, cell_limit=8192):
        start = time.monotonic()
        cells, rejected, depth_used = [], 0, 0
        worst_budget = arb(0)
        def visit(left,right,depth=0):
            nonlocal rejected,depth_used,worst_budget
            check(time.monotonic()-start < seconds_limit and len(cells)+rejected < cell_limit,
                  'pilot time/cell resource limit exceeded')
            depth_used = max(depth_used,depth)
            values,budgets = self.enclose(self.tlo,self.thi,left,right)
            if signed_constant is None:
                selected = coordinate_separator(values)
                margin = selected[0] if selected else None
            else:
                signed = laguerre_excess(values,signed_constant)
                margin = signed.lower() if signed>0 else None
                selected = None
            if margin is not None:
                worst_budget = max(worst_budget,max(row['total_added_error'] for row in budgets[:2]))
                cells.append({'x':[str(left),str(right)],'margin_lower':rec(margin),
                              'component':selected[1] if selected else 'Laguerre-minus-cE',
                              'sign':selected[2] if selected else 1,
                              'H':rec(values[0]),'Hx':rec(values[1]),'Hxx':rec(values[2])})
                return
            rejected += 1
            if depth >= max_depth:
                raise ArithmeticError('pilot subdivision exhausted at '+str((left,right)))
            middle = (left+right)/2
            visit(left,middle,depth+1)
            visit(middle,right,depth+1)
        visit(self.xlo,self.xhi)
        check(F(cells[0]['x'][0])==self.xlo and F(cells[-1]['x'][1])==self.xhi
              and all(a['x'][1]==b['x'][0] for a,b in zip(cells,cells[1:])), 'noncontiguous pilot cover')
        return {'accepted_strips':len(cells),'rejected_parent_strips':rejected,
                'maximum_depth':depth_used,'subdivision_limit':max_depth,
                'minimum_margin_lower':rec(min(arb(row['margin_lower']).lower() for row in cells)),
                'worst_added_coordinate_error':rec(worst_budget),'cells':cells,
                'timing_seconds':time.monotonic()-start,'seconds_limit':seconds_limit,'cell_limit':cell_limit,
                'signed_constant':str(signed_constant) if signed_constant is not None else None}

    def manifest(self):
        return {'method':self.method,'exact_domain':{'t':[str(self.tlo),str(self.thi)],'x':[str(self.xlo),str(self.xhi)],'imaginary':['-1','1']},
                'exact_midpoint':[str(self.tc),str(self.xc)],'m':self.N+1,'retained_modes':list(range(1,self.N+1)),
                'd':'pi/16' if self.method=='shifted' else '0','frozen_parameters':True,
                'source_cutoff':str(self.U),'precision_bits':self.bits,'degree_x':self.L,'degree_t':self.K,
                'maximum_midpoint_derivative':self.maximum_midpoint_order,'maximum_remainder_derivative':self.maximum_remainder_order,
                'admissibility':self.admissible,'absolute_moment_bounds':{str(k):rec(v) for k,v in self.moments.items()},
                'midpoint_integrals':len(self.midpoints),'majorant_integrals':2 if self.method=='shifted' else 0,
                'total_integrals':len(self.midpoints)+(2 if self.method=='shifted' else 0),
                'midpoint_quadrature_callbacks':self.quadrature_callbacks,
                'quadrature_abs_tolerance':'1e-35','quadrature_rel_tolerance':'1e-28','quadrature_eval_limit':200000,'quadrature_depth_limit':30,
                'arithmetic':'Arb/Acb outward ball arithmetic; quadrature radii include its internal rounding. Subsequent parameter and polynomial rounding stays inside outward polynomial enclosures, not an omitted scalar error.',
                'construction_seconds':self.construction_seconds,'midpoint_integral_seconds':self.integral_seconds,
                'midpoint_jets':[rec(value) for value in self.midpoints],
                'midpoint_quadrature_radii':[rec(value) for value in self.quad_radii]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--bits',type=int,default=160)
    parser.add_argument('--execution-model',required=True)
    parser.add_argument('--execution-effort',required=True)
    args = parser.parse_args()
    start = time.monotonic()
    methods = {name:Evaluator(name,bits=args.bits) for name in ('real','shifted')}
    tests = []
    cells = [(F(1,100),F(1,100),F(25),F(25),F(0),F(0)),
             (F(21,200),F(21,200),F(35),F(35),F(0),F(0)),
             (F(1,5),F(1,5),F(45),F(45),F(0),F(0)),
             (F(1,10),F(11,100),F(28),F(29),F(0),F(0)),
             (F(1,100),F(1,5),F(34),F(341,10),F(0),F(0)),
             (F(1,10),F(11,100),F(34),F(341,10),F(2,5),F(3,5))]
    for t in (F(1,100),F(1,5)):
        for x,y in ((F(25),F(1)),(F(35),F(1,2)),(F(45),F(1))):
            cells.append((t,t,x,x,y,y))
    allowance=arb('1e-10')
    allocations={'mode':arb('1e-12'),'source':arb('1e-12'),'quadrature_with_internal_rounding':arb('1e-12'),'taylor_propagation':arb('1e-11')}
    for domain in cells:
        results={name:evaluator.enclose(*domain) for name,evaluator in methods.items()}
        for j in range(3):
            left,right=results['real'][0][j],results['shifted'][0][j]
            check(left.overlaps(right),'matched shifted/real enclosure mismatch')
            for name in methods:
                budget=results[name][1][j]
                check(budget['total_added_error']<allowance,'consumer allowance failed')
                for component,allocation in allocations.items():check(budget[component]<allocation,'component allowance failed '+name+' '+component)
        tests.append({'exact_cell':[str(q) for q in domain],
                      'intersection_all_three':True,
                      'enclosures':{name:[rec(v) for v in result[0]] for name,result in results.items()},
                      'errors':{name:[{k:rec(v) for k,v in row.items()} for row in result[1]] for name,result in results.items()}})
    conjugation=[]
    for evaluator in methods.values():
        plus=evaluator.enclose(F(1,10),F(1,10),F(33),F(33),F(3,4),F(3,4))[0]
        minus=evaluator.enclose(F(1,10),F(1,10),F(33),F(33),F(-3,4),F(-3,4))[0]
        check(all(a.conjugate().overlaps(b) for a,b in zip(plus,minus)),'conjugation diagnostic failed')
        conjugation.append(evaluator.method)
    pilots={name:evaluator.pilot() for name,evaluator in methods.items()}
    output={'date':'2026-10-18','prepared_for':'Edward Baker','llm_assistance':'Substantial LLM assistance; internal interval computation.',
            'authoring_model':'gpt-6.1-sol','authoring_effort':'max','execution_model':args.execution_model,'execution_effort':args.execution_effort,
            'python':platform.python_version(),'python_flint':flint.__version__,
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'methods':{name:evaluator.manifest() for name,evaluator in methods.items()},
            'predeclared_budget':{'coordinate_total_allowance':'1e-10','component_allocations':{name:rec(value) for name,value in allocations.items()},
                                  'reserve':'8.7e-11; subsequent arithmetic is already inside the polynomial ball'},
            'matched_tests':tests,'conjugation_diagnostics_passed':conjugation,
            'heat_equation_contract':'Each retained integral, including its fixed source cutoff, satisfies H_t=-H_zz. Its time Taylor coefficient k uses midpoint jet j+2k with sign (-1)^k; highest remainder order is explicitly bounded.',
            'pilot':pilots,'all_checks_passed':True,'timing_seconds':time.monotonic()-start,
            'scope':'Finite closed rectangle only. No global collision exclusion, Newman bound or computational superiority inferred.'}
    args.output.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'passed':True,'pilot':{name:{k:v for k,v in row.items() if k!='cells'} for name,row in pilots.items()},
                      'construction_seconds':{name:e.construction_seconds for name,e in methods.items()},'seconds':time.monotonic()-start},indent=2))


if __name__=='__main__':
    main()
