from collections import defaultdict
import numpy as np

ls = np.array([l.strip() for l in open("2023/Input/21.txt")])
A = np.array([[*l] for l in ls])
n, m = A.shape
sx, sy = np.where(A == "S")[0][0], np.where(A == "S")[1][0]
s = (sx, sy)

### <----------------------- PART ONE -----------------------> ###
def N(x, y):
    for x, y in [(x + dx, y + dy) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]]:
        if 0 <= x < n and 0 <= y < m and A[x, y] != "#": 
            yield (x, y)


def BFS(s, steps, startStep, swapParity=False):
    D = defaultdict(lambda: -1)
    Q = [(startStep, s)]
    for d, a in Q:
        if a in D or d > steps: continue
        D[a] = d
        for b in N(*a):
            Q.append(((d + 1), b))
    return sum((d + swapParity) % 2 == steps % 2 for d in D.values())

print("PART ONE: ", BFS(s, 64, 0))

### <----------------------- PART TWO -----------------------> ###
steps = 26501365 
Nfull = ((steps - sy) // m) - 1
indexSteps = steps - m
middles = [(0, sy), (sx, m - 1), (n - 1, sy), (sx, 0)]
corners = [(n - 1, 0), (0, 0), (0, m - 1), (n - 1, m - 1)]

fullE  =  BFS(s, steps, 0)
fullO  =  BFS(s, steps, 1)
tips   = [BFS(s, steps, indexSteps + 1)           for s in middles]
bigs   = [BFS(s, steps, indexSteps - n + 2 + sx)  for s in corners]
smalls = [BFS(s, steps, indexSteps + 2 + sx)      for s in corners]

def oddsAndEvens(index): 
    return (index + (index + 1) % 2) ** 2, (index + index % 2) ** 2

print("PART TWO: ", oddsAndEvens(Nfull)[0] * fullE + oddsAndEvens(Nfull)[1] * fullO + sum(tips) + (Nfull + 1) * sum(smalls) + Nfull * sum(bigs))
