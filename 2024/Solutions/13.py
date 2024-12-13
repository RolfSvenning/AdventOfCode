import re
from sympy import symbols, Eq, solve 

I = [tuple(map(int, re.findall(r"\d+", l))) for l in open("2024/Input/13.txt").read().split("\n\n")]

### <----------------------- PART ONE -----------------------> ###

def f(t, isPartTwo=False):
    x1, y1, x2, y2, x, y = t
    if isPartTwo: x, y = 10000000000000 + x, 10000000000000 + y

    a, b = symbols("a,b")
    eq1 = Eq((a * x1 + b *x2), x)
    eq2 = Eq((a * y1 + b *y2), y)
    sol = solve((eq1, eq2), (a, b))
    return 3 * sol[a] + sol[b] if sol[a] % 1 == 0 and sol[b] % 1 == 0 else 0
    

print("PART ONE: ", sum(f(t) for t in I))

### <----------------------- PART TWO -----------------------> ###

print("PART TWO: ", sum(f(t, True) for t in I))
