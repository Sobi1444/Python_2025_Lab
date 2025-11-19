from math import gcd

def _norm(frac):
    a, b = frac
    if b < 0:
        a, b = -a, -b
    g = gcd(a, b)
    return [a // g, b // g]

def add_frac(f1, f2):
    return _norm([f1[0]*f2[1] + f2[0]*f1[1], f1[1]*f2[1]])

def sub_frac(f1, f2):
    return _norm([f1[0]*f2[1] - f2[0]*f1[1], f1[1]*f2[1]])

def mul_frac(f1, f2):
    return _norm([f1[0]*f2[0], f1[1]*f2[1]])

def div_frac(f1, f2):
    return _norm([f1[0]*f2[1], f1[1]*f2[0]])

def is_positive(f):
    a, b = _norm(f)
    return a > 0

def is_zero(f):
    return _norm(f)[0] == 0

def cmp_frac(f1, f2):
    v = f1[0]*f2[1] - f2[0]*f1[1]
    if v < 0: return -1
    if v > 0: return 1
    return 0

def frac2float(f):
    return f[0] / f[1]