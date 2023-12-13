import numpy as np
from math import lcm

ls = [np.array([[*r] for r in l.split("\n")]) for l in open("2023/input/13.txt").read().split("\n\n")]


def h(x):
    I = np.where(x==".")[0]
    return set(I)
    return 2 * min(I) + max(I) + lcm(*I) + int("".join([str(s) for s in I]))

# d number of errors allowed
# e exception, same row as prev found
def mirror(h, d = 0, e = None):
    n = len(h)
    for i in range(n - 1):
        if e != None and i == e: continue
        for j in range(min(i - 0 + 1, n - 1 - i)):
            if h[i - j].symmetric_difference(h[i + j + 1]) == 1 and d == 1: continue
            if h[i - j] != h[i + j + 1] and d == 0: break
        else: return i
    return None
            

# d number of errors allowed
# e exception, same row as prev found
def mirror2(h, smudge = False, e = None):
    n = len(h)
    for i in range(n - 1):
        d = smudge
        if e != None and i == e: 
            print("skipping i: ", i)
            continue
        for j in range(min(i - 0 + 1, n - 1 - i)):
            print(i - j, i + j + 1, n)
            if h[i - j].symmetric_difference(h[i + j + 1]) == 1 and d == 1: 
                print("continuing")
                d = d - 1
                continue
            if h[i - j] != h[i + j + 1]: 
                print("breaking")
                break
        else: return i
    return None

def f(A, partTwo=False):
    n, m = A.shape
    R = [0] * n
    C = [0] * m

    for i, r in enumerate(A):
        R[i] = h(r)

    for i, c in enumerate(A.T):
        C[i] = h(c)

    # print("R: ", R)
    # print("C: ", C)
    r1 = mirror(C)
    r2 = mirror(R)

    # PART TWO
    if partTwo: 
        r1, r2 = f2(r1, r2, R, C)

    # print("r1, r2: ", r1, r2)
    assert (r1 == None or r2 == None)
    return r1 + 1 if r2 == None else 100 * (r2 + 1)

def f2(r1, r2, R, C):
    r1 = mirror2(R, 1, r1)
    r2 = mirror2(C, 1, r2)
    return r1, r2

def solve(partTwo=False):
    res = 0
    for A in ls:
        r = f(A, partTwo)
        # print(r)
        res += r
        # break
    return res

print("PART ONE: ", solve())
print("PART TWO: ", solve(partTwo=True))



# too low 30539