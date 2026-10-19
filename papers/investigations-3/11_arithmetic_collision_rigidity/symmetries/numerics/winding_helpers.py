#!/usr/bin/env python3
"""Generic whole-boundary half-plane and exact polygon winding helpers.

Prepared for Edward Baker, 19 October 2026, with substantial LLM assistance.
Actual authoring model gpt-6.1-sol (Codex), reasoning effort ultra.

The callback supplies COMPLETE Arb balls for the first two coordinates of a
continuous planar field on each closed rectangle. These helpers neither
compute source errors nor assert a heat equation. A zero boundary degree is
only a geometric input to the separately stated collision-index theorem.

API:
  strict_separator(values) -> None or a JSON-friendly half-plane descriptor.
  adaptive_boundary(enclose, box, max_depth=9, max_calls=512) -> record.
  polygon_from_halfplanes(boundary_or_record, box) -> Fraction vertex pairs.
  polygon_winding(vertices) -> exact integer; rejects passage through origin.
  boundary_acceptance(enclose, box, limits=None, **limits) -> JSON record.

box=(tlo,thi,xlo,xhi) consists of exact Fractions, integers or rational strings.
enclose(t0,t1,x0,x1) returns at least two finite Arb balls, with every error
already included. Every accepted segment is a CLOSED segment. Polygon
vertices are chosen from incident half-planes and need no source evaluations.
"""
from __future__ import annotations

from fractions import Fraction

from flint import arb


def _fraction(value):
    if isinstance(value, bool) or isinstance(value, float):
        raise ValueError('exact rational values required; binary floats forbidden')
    if isinstance(value, (Fraction, int, str)):
        try:
            return Fraction(value)
        except (ValueError, TypeError, ZeroDivisionError) as error:
            raise ValueError('invalid exact rational value') from error
    raise ValueError('exact rational values required')


def _box(box):
    if isinstance(box, (str, bytes)) or len(box) != 4:
        raise ValueError('box must be (tlo,thi,xlo,xhi)')
    tlo, thi, xlo, xhi = map(_fraction, box)
    if not (tlo < thi and xlo < xhi):
        raise ValueError('box intervals must have positive width')
    return tlo, thi, xlo, xhi


def _point(point):
    if isinstance(point, (str, bytes)) or len(point) != 2:
        raise ValueError('a point must contain exactly two rational coordinates')
    return tuple(map(_fraction, point))


def _point_record(point):
    return [str(coordinate) for coordinate in point]


def _limits(max_depth, max_calls):
    if (isinstance(max_depth, bool) or not isinstance(max_depth, int)
            or max_depth < 0):
        raise ValueError('max_depth must be a nonnegative integer')
    if (isinstance(max_calls, bool) or not isinstance(max_calls, int)
            or max_calls < 1):
        raise ValueError('max_calls must be a positive integer')
    return max_depth, max_calls


def strict_separator(values):
    """Choose a rigorously strict coordinate half-plane, or return None.

    Only the first two coordinates are observed. Every one must be a finite
    Arb ball. The largest PROVABLY larger lower margin wins; unresolved or
    tied comparisons retain the existing choice. No binary float is used.
    Returned margins are exact rational endpoint strings, not ball midpoints.
    """
    if isinstance(values, (str, bytes)) or len(values) < 2:
        raise ValueError('at least two complete Arb coordinate balls required')
    observed = values[:2]
    if any(not isinstance(value, arb) or not value.is_finite()
           for value in observed):
        raise ValueError('two finite complete Arb coordinate balls required')
    best = None
    best_margin = None
    for component, value in enumerate(observed):
        sign = 1 if value > 0 else (-1 if value < 0 else 0)
        if not sign:
            continue
        margin = value.abs_lower()
        if not (margin.is_finite() and margin.is_exact() and margin > 0):
            raise ValueError('strict coordinate has no positive exact lower margin')
        if best is None or margin > best_margin:
            best = {'component': component, 'sign': sign,
                    'margin_lower': str(Fraction(str(margin.fmpq())))}
            best_margin = margin
    return best


def adaptive_boundary(enclose, box, max_depth=9, max_calls=512):
    """Certify the four oriented faces, with fixed depth and call limits.

    Returns status complete or inconclusive. An inconclusive record can hold
    a partial ordered cover but must never be used as a degree certificate.
    Invalid boxes, limits, callbacks or coordinate balls raise an exception.
    """
    tlo, thi, xlo, xhi = _box(box)
    max_depth, max_calls = _limits(max_depth, max_calls)
    if not callable(enclose):
        raise ValueError('enclose callback must be callable')
    segments = []
    calls = 0
    rejected = 0
    deepest = 0
    failure = None

    def edge(start, end, depth):
        nonlocal calls, rejected, deepest, failure
        deepest = max(deepest, depth)
        if calls >= max_calls:
            failure = {'reason': 'maximum enclosure calls reached',
                       'from': _point_record(start), 'to': _point_record(end),
                       'depth': depth}
            return False
        calls += 1
        values = enclose(min(start[0], end[0]), max(start[0], end[0]),
                         min(start[1], end[1]), max(start[1], end[1]))
        separator = strict_separator(values)
        if separator is not None:
            segments.append({'from': _point_record(start),
                             'to': _point_record(end), **separator,
                             'jet_enclosures': [value.str(38, more=True)
                                                for value in values[:2]],
                             'depth': depth})
            return True
        rejected += 1
        if depth >= max_depth:
            failure = {'reason': 'maximum bisection depth reached',
                       'from': _point_record(start), 'to': _point_record(end),
                       'depth': depth,
                       'jet_enclosures': [value.str(38, more=True)
                                          for value in values[:2]]}
            return False
        midpoint = tuple((a+b)/2 for a, b in zip(start, end))
        return (edge(start, midpoint, depth+1)
                and edge(midpoint, end, depth+1))

    corners = [(tlo, xlo), (thi, xlo), (thi, xhi),
               (tlo, xhi), (tlo, xlo)]
    complete = True
    for start, end in zip(corners, corners[1:]):
        if not edge(start, end, 0):
            complete = False
            break
    return {'status': 'complete' if complete else 'inconclusive',
            'box': [str(v) for v in (tlo, thi, xlo, xhi)],
            'orientation': 'dt wedge dx; lower wall, final time, upper wall, initial time',
            'boundary': segments, 'calls': calls,
            'accepted_segments': len(segments),
            'rejected_parent_segments': rejected,
            'max_depth_reached': deepest,
            'limits': {'max_depth': max_depth, 'max_calls': max_calls},
            'failure': failure}


def _validate_boundary(boundary, box):
    tlo, thi, xlo, xhi = _box(box)
    if isinstance(boundary, dict):
        if boundary.get('status') != 'complete':
            raise ValueError('an incomplete boundary has no certified degree')
        if 'box' in boundary and _box(boundary['box']) != (tlo, thi, xlo, xhi):
            raise ValueError('boundary record box mismatch')
        boundary = boundary.get('boundary')
    if not isinstance(boundary, (list, tuple)) or not boundary:
        raise ValueError('nonempty ordered boundary segment list required')
    parsed = []
    faces = []
    for segment in boundary:
        if not isinstance(segment, dict):
            raise ValueError('boundary segments must be dictionaries')
        try:
            start, end = _point(segment['from']), _point(segment['to'])
            component, sign = segment['component'], segment['sign']
        except KeyError as error:
            raise ValueError('missing boundary segment data') from error
        if (isinstance(component, bool) or component not in (0, 1)
                or not isinstance(component, int)
                or isinstance(sign, bool) or sign not in (-1, 1)
                or not isinstance(sign, int)):
            raise ValueError('invalid coordinate half-plane')
        if 'margin_lower' in segment and _fraction(segment['margin_lower']) <= 0:
            raise ValueError('boundary half-plane margin must be strictly positive')
        if any(not (tlo <= t <= thi and xlo <= x <= xhi)
               for t, x in (start, end)):
            raise ValueError('segment endpoint outside box')
        if start[1] == end[1] == xlo and start[0] < end[0]:
            face = 0
        elif start[0] == end[0] == thi and start[1] < end[1]:
            face = 1
        elif start[1] == end[1] == xhi and start[0] > end[0]:
            face = 2
        elif start[0] == end[0] == tlo and start[1] > end[1]:
            face = 3
        else:
            raise ValueError('segment is not a properly oriented box face')
        parsed.append((start, end, component, sign))
        faces.append(face)
    if parsed[0][0] != (tlo, xlo) or parsed[-1][1] != (tlo, xlo):
        raise ValueError('boundary must start and close at the lower left corner')
    if any(parsed[i][1] != parsed[i+1][0] for i in range(len(parsed)-1)):
        raise ValueError('boundary segments are not exactly contiguous')
    if (faces[0] != 0 or faces[-1] != 3 or set(faces) != {0, 1, 2, 3}
            or any(b not in (a, a+1) for a, b in zip(faces, faces[1:]))):
        raise ValueError('boundary must cover all four faces once in positive order')
    return parsed


def polygon_from_halfplanes(boundary, box):
    """Construct an exact homotopic polygon from incident half-planes.

    The incoming and outgoing certified half-planes share the actual endpoint.
    Assign each constrained coordinate its rational sign (+1 or -1), and any
    unconstrained coordinate zero. Opposite signs on one coordinate are
    incompatible and rejected. No actual endpoint field value is evaluated.
    The return value is a list of pairs of Fractions.
    """
    segments = _validate_boundary(boundary, box)
    vertices = []
    for index, segment in enumerate(segments):
        incoming = segments[index-1]
        constraints = {}
        for _, _, component, sign in (incoming, segment):
            if component in constraints and constraints[component] != sign:
                raise ValueError('incident certified half-planes are incompatible')
            constraints[component] = sign
        vertices.append(tuple(Fraction(constraints.get(component, 0))
                              for component in (0, 1)))
    for index, segment in enumerate(segments):
        _, _, component, sign = segment
        if not (sign*vertices[index][component] > 0
                and sign*vertices[(index+1) % len(vertices)][component] > 0):
            raise ValueError('polygon edge leaves its certified strict half-plane')
    return vertices


def polygon_winding(vertices):
    """Exact signed winding about zero, allowing repeated nonzero vertices.

    Positive orientation in the displayed target coordinates has degree +1.
    A vertex at zero or an edge passing through zero is invalid. The half-open
    ray-crossing convention handles vertices on the crossing ray consistently.
    """
    if not isinstance(vertices, (list, tuple)) or not vertices:
        raise ValueError('nonempty rational polygon vertex list required')
    points = [_point(point) for point in vertices]
    if any(x == 0 and y == 0 for x, y in points):
        raise ValueError('polygon has an origin vertex')
    winding = 0
    for (x, y), (X, Y) in zip(points, points[1:]+points[:1]):
        cross = x*Y-X*y
        if cross == 0 and x*X+y*Y <= 0:
            raise ValueError('polygon edge passes through the origin')
        if y <= 0 < Y and cross > 0:
            winding += 1
        elif Y <= 0 < y and cross < 0:
            winding -= 1
    return winding


def boundary_acceptance(enclose, box, limits=None, *, max_depth=9, max_calls=512):
    """Return pass only for a complete, nonzero boundary of exact degree zero.

    A complete boundary with nonzero degree returns nonzero_degree; an
    unresolved segment or exhausted budget returns inconclusive. Invalid
    inputs raise ValueError. Optional limits is a dictionary containing only
    max_depth and/or max_calls. All returned data are JSON-friendly.
    """
    if limits is not None:
        if not isinstance(limits, dict) or set(limits)-{'max_depth', 'max_calls'}:
            raise ValueError('limits must contain only max_depth and max_calls')
        max_depth = limits.get('max_depth', max_depth)
        max_calls = limits.get('max_calls', max_calls)
    result = adaptive_boundary(enclose, box, max_depth=max_depth, max_calls=max_calls)
    result['boundary_status'] = result['status']
    result['vertex_source_evaluations'] = 0
    if result['status'] != 'complete':
        result.update({'degree': None, 'polygon': [], 'accepts_zero_degree': False})
        return result
    vertices = polygon_from_halfplanes(result, box)
    degree = polygon_winding(vertices)
    result.update({'status': 'pass' if degree == 0 else 'nonzero_degree',
                   'degree': degree,
                   'polygon': [_point_record(point) for point in vertices],
                   'accepts_zero_degree': degree == 0})
    return result
