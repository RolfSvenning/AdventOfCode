import numpy as np
import itertools
import re

ls = [l.strip() for l in open("2023/input/03.txt").readlines()]
A = np.array([[*l] for l in ls])
n,m = A.shape

### <----------------------- PART ONE -----------------------> ###
def nearSymbol(a, b, r):
    around = set(A[max(0,r-1):min(n, r + 2),max(0, a - 1):min(m, b + 1)].flatten())
    allowed = set([str(v) for v in range(10)] + ["."])
    return len(around - allowed) > 0

def numbersOnLine(l):
    Ns = []
    pos = 0
    while (pos < m):
        pat = re.compile("\d+")
        obj = pat.search(l, pos)
        if obj == None: break
        span, match = obj.span(), obj[0]
        Ns.append((int(match), span))
        pos = span[1]
    return Ns

L = [num for i,l in enumerate(ls) for num,span in numbersOnLine(l) if nearSymbol(*span, i)]
print("PART ONE: ", sum(L))

### <----------------------- PART TWO -----------------------> ###
Gs = []
for i, l in enumerate(ls):
    for j, c in enumerate(l):
        if c != "*": continue
        Ns = list(itertools.chain(*[numbersOnLine(ls[k]) for k in range(max(0, i - 1),min(n, i + 2))]))
        NNs = [num for num, (a,b) in Ns if j in range(a-1,b+1)]
        if len(NNs) == 2: Gs.append(NNs[0] * NNs[1])

print("PART TWO: ", sum(Gs))