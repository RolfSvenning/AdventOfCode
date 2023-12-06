import re
from functools import reduce
from sympy import solve, var
from math import ceil, floor

Ts, Ds = [list(map(int, re.findall("\d+", l))) for l in open("2023/input/06.txt").readlines()]
T, D = [int("".join([str(l) for l in L])) for L in [Ts, Ds]]

### <----------------------- PART ONE & TWO -----------------------> ###
def f(t, d):
    i = var('i')
    i1, i2 = solve((t - i) * i - d, i)
    return 1 + ((ceil(i2) - 1) - (1 + floor(i1)))

print("PART ONE: ", reduce(lambda x, y: x * y, [f(t, d) for t, d in zip(Ts, Ds)]))
print("PART TWO ", f(T, D))