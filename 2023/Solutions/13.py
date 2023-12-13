import numpy as np

input = [np.array([[*r] for r in l.split("\n")]) for l in open("2023/input/13.txt").read().split("\n\n")]

### <----------------------- PART ONE & TWO -----------------------> ###
def mirror(h, smudge = 0, skip = -1):
    n = len(h)
    for i in range(n - 1):
        d = smudge
        if i == skip: continue
        for j in range(min(i + 1, n - 1 - i)):
            if len(h[i - j].symmetric_difference(h[i + j + 1])) == 1 and d == 1:
                d = d - 1
                continue
            if h[i - j] != h[i + j + 1]: break
        else: return i

def f(A, partTwo = False):
    R = [set(np.where(r == ".")[0]) for r in A]
    C = [set(np.where(c == ".")[0]) for c in A.T]
    ri = mirror(R)
    ci = mirror(C)
    if partTwo: 
        ri = mirror(R, 1, ri)
        ci = mirror(C, 1, ci)
    return 100 * (ri + 1) if ri != None else ci + 1

print("PART ONE: ", sum(f(A) for A in input))
print("PART TWO: ", sum(f(A, partTwo=True) for A in input))
