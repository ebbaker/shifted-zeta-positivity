#!/usr/bin/env python3
"""Exact scalar gates for the restarted global-floor consumer.

Prepared for Edward Baker with substantial LLM assistance, 17 October 2026.
Model: gpt-6-astra (Codex); reasoning effort: ultra.

This certifies finite rational inequalities only. It does not certify the
arithmetic hypothesis S(x,3,t)>=6 or the analytic strip-transfer lemma.
"""
from fractions import Fraction as F
from math import factorial
import json


def require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def e_lower(x, n):
    require(x >= 0, 'exact scalar gate failed')
    return sum((x**j / factorial(j) for j in range(n + 1)), F(0))


def e_upper(x, n):
    require(0 <= x < n + 2, 'exact scalar gate failed')
    return e_lower(x, n) + x**(n + 1) / factorial(n + 1) / (1 - x/F(n + 2))


def gate_record(value):
    require(value > 0, 'exact scalar gate failed')
    return {'numerator': str(value.numerator), 'denominator': str(value.denominator),
            'display_only_float': float(value)}


def main():
    C = F(6)
    step = F(1, 10000)
    n = 2150
    T = F(43, 200)
    floor = F(1499, 250)
    k = 4 * floor / 3 - 1
    require(n * step == T and T < F(1, 4), 'exact scalar gate failed')
    require(k == F(2623, 375), 'exact scalar gate failed')
    floor_exp_gate = (C + 2*C*floor) / (13*floor)
    require(floor_exp_gate == F(19488, 19487), 'exact scalar gate failed')
    floor_margin = floor_exp_gate - e_upper(step/2, 8)
    terminal_margin = e_lower(k*T, 20) - (1+k/2)

    record = {
        'prepared_for': 'Edward Baker', 'date_local': '2026-10-17',
        'model': 'gpt-6-astra (Codex)', 'reasoning_effort': 'ultra',
        'llm_assistance': 'Substantial LLM assistance; internal same-model research team',
        'status': 'exact rational scalar gates only; analytic floor and transfer are separate inputs',
        'target': '43/200', 'step': str(step), 'steps': n,
        'required_original_floor': str(C), 'step_floor': str(floor), 'k': str(k),
        'floor_gate_margin': gate_record(floor_margin),
        'terminal_gate_margin': gate_record(terminal_margin),
    }
    print(json.dumps(record, indent=2))


if __name__ == '__main__':
    main()
