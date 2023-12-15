import re

S = open("2023/input/15.txt").read().strip().split(",")

### <----------------------- PART ONE -----------------------> ###
def h(s):
    res = 0
    for c in s:
        res = ((res + ord(c)) * 17 )
    return res % 256

print("PART ONE: ", sum(h(s) for s in S))

### <----------------------- PART TWO -----------------------> ###
B = [{} for _ in range(256)]

for s in S:
    l = re.match("[a-z]+", s)[0]
    hs = h(l)
    if "-" in s and l in B[hs].keys(): del B[hs][l]
    else: B[hs][l] = int(s[-1])
    
def focusPower(bi, b):
    return sum((bi + 1) * (i + 1) * l for i, l in enumerate(b.values()))

print("PART TWO: ", sum(focusPower(bi, b) for bi, b in enumerate(B)))