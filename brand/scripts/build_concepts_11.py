#!/usr/bin/env python3
"""Geometric brush delta (N3): sharp corners only, built from primitives. Standard library only.
The outer shape is one polygon. The window is the triangle bounded by three lines at fixed stroke widths."""
import math
from pathlib import Path

OUT = Path(__file__).parent
f = lambda n: f'{n:.1f}'.rstrip('0').rstrip('.')

B, R, L = (96, 30), (218, 216), (30, 216)       # cap corner, right foot, left foot
W_MAIN, W_BRANCH, BASE, NOTCH_Y = 38, 18, 196, 120
dx, dy = R[0] - B[0], R[1] - B[1]
ln = math.hypot(dx, dy)
d = (dx / ln, dy / ln)
n = (-d[1], d[0])                                 # perpendicular, pointing to the left of the stroke
A = (B[0] + n[0] * W_MAIN, B[1] + n[1] * W_MAIN)  # the other end of the flat cap
t = (NOTCH_Y - A[1]) / d[1]
N = (A[0] + d[0] * t, NOTCH_Y)                    # where the thin branch meets the thick stroke
def shifted(p, q, d, side):
  """Line through p, q moved by d to the given side (+1 left of p->q). Returns a point and a direction."""
  dx, dy = q[0] - p[0], q[1] - p[1]
  n = math.hypot(dx, dy)
  nx, ny = -dy / n * side, dx / n * side
  return (p[0] + nx * d, p[1] + ny * d), (dx / n, dy / n)


def cross(a, b):
  (p, u), (q, v) = a, b
  t = ((q[0] - p[0]) * v[1] - (q[1] - p[1]) * v[0]) / (u[0] * v[1] - u[1] * v[0])
  return p[0] + u[0] * t, p[1] + u[1] * t


floor = ((0, BASE), (1, 0))
branch = shifted(L, N, W_BRANCH, 1)
main = shifted(B, R, W_MAIN, 1)
w = [cross(floor, branch), cross(floor, main), cross(branch, main)]
poly = lambda pts: 'M' + 'L'.join(f'{f(x)} {f(y)}' for x, y in pts) + 'Z'
outline = poly([A, B, R, L, N])
body = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256"><title>Axiom concept N4: geometric delta with a flat cap</title>'
        f'<path fill="#000" fill-rule="evenodd" d="{outline}{poly(w)}"/></svg>\n')
(OUT / 'concept-n4-geometric-delta-cap.svg').write_text(body, encoding='utf-8')
print('A', A, 'N', N, 'window', [(round(x), round(y)) for x, y in w])
