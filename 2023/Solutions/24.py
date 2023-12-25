from numpy import sign

ls = [l.strip().split(" @ ") for l in open("2023/Input/24.txt")]
XYs = [[tuple(map(int, k.split(", "))) for k in l] for l in ls ]
n = len(XYs)

def convertToLine(l):
    x, y, _   = l[0]
    dx, dy, _ = l[1]
    a = (dy / dx) if sign(dx) or (not sign(x) and not sign(y)) else -dy / dx
    b = y - a * x
    return a, b

def intersect(l1, l2):
    a1, b1 = l1
    a2, b2 = l2
    if a1 != a2:
        x = (b1 - b2) / (a2 - a1)
        y = a1 * x + b1
        return [(x, y)]
    else: return []
    #y1 = a1x1 + b1
    #y2 = a2x2 + b2
    #b1 - b1 = (a2 - a1)x
    #(b1 - b2) / (a2 - a1) = x

ABs = [convertToLine(XYs[i]) for i in range(n)]

def allIntersects():
    for i in range(n):
        for j in range(i + 1, n):
            li, lj = ABs[i], ABs[j]
            ints = intersect(li, lj)
            if ints:
                # print(li, lj, ints, inArea(ints[0]), validInts(i, j, ints[0]))
                if inArea(ints[0]) and validInts(i, j, ints[0]): 
                    # print("valid", li, lj, ints)
                    yield ints[0]
                # else: print("but not valid")
            # else: print("not valid, parallel", li, lj, ints)


def inArea(ints):
     x, y = ints
     return C1 <= min(x, y) and max(x, y) <= C2

def validInts(i, j, ints):
    xi  = XYs[i][0][0]
    dxi = XYs[i][1][0]
    xj  = XYs[j][0][0]
    dxj = XYs[j][1][0]
    cx  = ints[0]

    iValid = cx >= xi if dxi > 0 else cx < xi
    jValid = cx >= xj if dxj > 0 else cx < xj
    # print("ijValid: ", iValid, jValid)
    return iValid and jValid
    

C1, C2 = 7, 27
# C1, C2 = 200000000000000, 400000000000000

res = [(x, y) for x, y in allIntersects()]
# print(res)
print("PART ONE: ", len(res))
# print("all intersects: ", list(allIntersects()))

# import sympy 
from sympy import solve, symbols
# from sympy.abc import x, y, z

# t = 9
b1, b2, b3, a1, a2, a3, t1, t2, t3= symbols("b1, b2, b3, a1, a2, a3, t1, t2, t3") #, integer=True
# equations = [ a1*t1 - b1 - 2*t1 + 19, 
#              -a2*t1 - b2 + t1 + 13, 
#              -a3*t1 - b3 - 2*t1 + 30]
#              #b1 - 24,
#              #b2 - 13,
#              #b3 - 10,
#              #t1 - 5]
# solutions = solve(equations, b1, b2, b3, a1, a2, a3, t1, t2, t3, dict=True)
# print(solutions)

Bs = [b1, b2, b3]
As = [a1, a2, a3]
Ts = [t1, t2, t3]

def eqs(i):
    for j in range(3):
        x  = XYs[i][0][j]
        dx = XYs[i][1][j]
        yield x + dx * Ts[i] - Bs[j] - As[j]*Ts[i]

EQs = [e for i in range(3) for e in eqs(i)]
print(EQs)
solutions = solve(EQs, b1, b2, b3, a1, a2, a3, t1, t2, t3, dict=True)
print(solutions)
# print(solutions[b1])
print("PART TWO: ", sum(solutions[0][å] for å in [b1, b2, b3]))