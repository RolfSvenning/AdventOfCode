import sys
from typing import DefaultDict 
sys.setrecursionlimit(2024)

I = [int(l.strip()) for l in open("2024/Input/22.txt").readlines()]

### <----------------------- PART ONE -----------------------> ###

def f(s, t):
    return (s ^ (s * t if t > 1 else s >> 5)) & (16777216 - 1)

def step(s):
    return f(f(f(s, 64), 1 / 32), 2048)

def Frec(s, i):
    if i == 0: return s
    return Frec(step(s), i - 1)

print("PART ONE: ", sum(Frec(x, 2000) for x in I))


### <----------------------- PART TWO -----------------------> ###

def getValuesAndChanges(s, i, acc):
    if i == 0: return acc
    s_ = step(s)
    acc[0].append(s_ % 10 - s % 10)
    acc[1].append(s_ % 10)
    return getValuesAndChanges(s_, i - 1, acc)

def getValueDict(C, V):
    D = DefaultDict(int)
    for i in range(len(C) - 3):
        cs = tuple(C[i] for i in range(i, i + 4))
        if cs in D: continue
        D[cs] = V[i + 3]
    return D

Ds = [getValueDict(*getValuesAndChanges(x, 2000, [[], []])) for x in I]

def valid(ins, k):
    S = 0
    for i in range(k):
        S += ins[i]
        if not (-9 <= S <= 9): return False
    return True

best, cs = 0, None
idxs = [0, 0, 0, 0]
for i1 in range(-9, 10):
    idxs[0] = i1
    for i2 in range(-9, 10):
        idxs[1] = i2
        if not valid(idxs, 2): continue
        for i3 in range(-9, 10):
            idxs[2] = i3
            if not valid(idxs, 3): continue
            for i4 in range(-9, 10):
                idxs[3] = i4
                if not valid(idxs, 4): continue
                S = sum(D[(i1, i2, i3, i4)] for D in Ds)
                if S > best:
                    best, cs = S, (i1, i2, i3, i4)
                    print(S, cs)

print("PART TWO: ", best)

            

