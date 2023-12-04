import numpy as np
import re
import math
ls = [[re.findall("\d+(?!\d*:)", l1.strip()) for l1 in l.split("|")] for l in open("2023/input/04.txt").readlines() ]

### <----------------------- PART ONE -----------------------> ###
S = [math.floor(2**(len(set(ws) & set(ns)) - 1)) for ws, ns in ls]
print("PART ONE: ", sum(S))

### <----------------------- PART TWO -----------------------> ###
n = len(ls)
C = np.array([1]*n)
for i, (ws, ns) in enumerate(ls):
    C[i + 1:i + 1 + len(set(ws) & set(ns))] += C[i]

print("PART TWO: ", sum(C))