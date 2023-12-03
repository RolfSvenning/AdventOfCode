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
    return [(int(m[0]), m.span()) for m in re.finditer("\d+", l)]

L = [num for i,l in enumerate(ls) for num,span in numbersOnLine(l) if nearSymbol(*span, i)]
print("PART ONE: ", sum(L))

### <----------------------- PART TWO -----------------------> ###
Gs = []
for i, l in enumerate(ls):
    for j, c in enumerate(l):
        if c != "*": continue
        allNums = list(itertools.chain(*[numbersOnLine(ls[k]) for k in range(max(0, i - 1), min(n, i + 2))]))
        nearNums = [num for num, (a,b) in all if j in range(a-1,b+1)]
        if len(nearNums) == 2: Gs.append(nearNums[0] * nearNums[1])

print("PART TWO: ", sum(Gs))