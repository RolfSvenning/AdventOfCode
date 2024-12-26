from itertools import combinations
from functools import cache
from collections import defaultdict
from random import randint
import sys


I1, G = open("2024/Input/24.txt").read().split("\n\n")
I1 = {k: int(v) for k, v in [l.split(": ") for l in I1.split("\n")]}
G = {z: gs.split(" ") for gs, z in [l.split(" -> ") for l in G.split("\n")]}
T = {"AND": lambda x, y: x & y, "OR": lambda x, y: x or y, "XOR": lambda x, y: x ^ y}
n = sum(1 for g in I1 if "x" in g)
m = len(G)
print(n, m)
sys.setrecursionlimit(4 * n + 10)

### <----------------------- PART ONE -----------------------> ###

def F(I, G):
    @cache
    def f(g):
        if g in I: return I[g]
        if g in G: 
            g1, op, g2 = G[g]
            return T[op](f(g1), f(g2))
        raise NotImplementedError
    
    res = [f(g) for g in reversed(sorted(G.keys())) if "z" in g]
    return int("".join(str(v) for v in res), 2)

print("PART ONE: ", F(I1, G))

### <----------------------- PART TWO -----------------------> ###

def similarity(a, b):
    return sum(a1 == b1 for a1, b1 in zip(format(a, "0" + str(n) + "b")[-n:], format(b, "0" + str(n) + "b")[-n:]))

def swap(g1, g2, G):
    G[g1], G[g2] = G[g2], G[g1]

def createRandomInt():
    return randint(0, 3**(2 * (n + m)))

def scoreSwaps(G, swaps, candidates, scoringFunction):
    a, b = createRandomInt(), createRandomInt() #x: 000101 y: 111111
    I = createInput(a, b)

    z = scoringFunction(a, b)

    currDist = similarity(z, F(I, G))
    banned = set()
    for g1, g2 in candidates:
        g12 = (g1, g2)
        swap(g1, g2, G)

    # if noCycles(G, g1, g2):
        try: 
            diff = similarity(z, F(I, G)) - currDist
            swaps[g12] += diff
            if swaps[g12] < 0: banned.add(g12)
        except RecursionError: 
            banned.add(g12)

        swap(g1, g2, G)

    candidates -= banned

def createInput(x, y):
    x = format(x, "0" + str(n) + "b")
    y = format(y, "0" + str(n) + "b")

    I = {}
    for i in range(n):
        I["x" + ("0" if i < 10 else "") + str(i)] = int(x[-(i + 1)])
        I["y" + ("0" if i < 10 else "") + str(i)] = int(y[-(i + 1)])

    return I

def dtob(x):
    return format(x, "0" + str(n) + "b")[-n:]

N = 25
ns = [(createRandomInt(), createRandomInt()) for _ in range(N)]
randomInputs = {(a, b): createInput(a, b) for a, b in ns}

def circuitWorks(G, scoringFunction):
    for i, ((a, b), I) in enumerate(randomInputs.items()):
        z = scoringFunction(a, b)
        if similarity(z, F(I, G)) != n: 
            if i > 1: print("fail after try: ", i)
            return False
    return True

def F2(G, swapsMade, candidates):
    q, scoringFunction = 4, lambda a, b: a + b   # <----------- !!! input dependant !!!  (3, &)
    # q, scoringFunction = 3, lambda a, b: a & b   # <----------- !!! input dependant !!!  (3, &)
    if len(swapsMade) >= q: 
        assert len(swapsMade) == q
        if circuitWorks(G, scoringFunction): return swapsMade 
        else:                                return []        
            
    print("swaps made: ", swapsMade)
    swaps = defaultdict(int)

    for i in range(min(50, 1 + len(candidates) // 10)):
        scoreSwaps(G, swaps, candidates, scoringFunction)
        if len(candidates) > 150:
            print("candidates: ", len(candidates))
            print("top sorted swaps: ", sorted(swaps.items(), key = (lambda x: -x[1]))[:5])

    setSwapsMade = set().union(*[set(swap) for swap in swapsMade])
    sortedSwaps  = sorted(swaps.items(), key = (lambda x: -x[1]))

    for (g1, g2), d in sortedSwaps[:10]:
        if (len(swapsMade) <= 2 and d == 0) or (g1, g2) not in candidates: continue
        swap(g1, g2, G)
        res = F2(G, swapsMade + [(g1, g2)], set(c for c in candidates if not (set(g for g in c) & setSwapsMade)))
        swap(g1, g2, G)
        if res: return res
        else: continue
    
    return []

res = F2(G, [], set(tuple(sorted(s)) for s in combinations(G.keys(), 2)))

print("PART TWO ", ",".join(sorted(list(set().union(*[set(swap) for swap in res])))))
