import numpy as np
from functools import cmp_to_key
from collections import defaultdict
import copy

B = [[list(map(int, c.split(","))) for c in l] for l in [l.strip().split("~") for l in open("2023/Input/22.txt")] ]
B = sorted(B, key=cmp_to_key(lambda a, b: a[0][2] - b[0][2]))
n, m, k = list(map(lambda x: 1 + max(*x), list(zip(*[c for b in B for c in b]))))
B = [(id + 1, b) for id, b in enumerate(sorted(B, key=cmp_to_key(lambda a, b: a[0][2] - b[0][2])))]   
A = np.zeros((n, m, k), int)
D = np.ones((n, m))

### <----------------------- PART ONE -----------------------> ###
def unpackBrick(b):
    id, b = [*b]
    return [id] + b[0] + b[1]

def placeBrick(b, removing):
    id, x1, y1, z1, x2, y2, z2 = unpackBrick(b)
    A[x1:x2+1, y1:y2+1, z1:z2+1] = 0 if removing else id

def dropBrick(b):
    id, x1, y1, z1, x2, y2, z2 = unpackBrick(b)
    d = int(np.max(D[x1:x2+1, y1:y2+1]))
    z2 = d + z2 - z1
    z1 = d 
    placeBrick(b, True)
    placeBrick((id, [[x1, y1, z1], [x2, y2, z2]]), False)
    D[x1:x2+1, y1:y2+1] = z2 + 1

def supporting():
    for x in range(n):
        for y in range(m):
            for z in range(k - 1):
                a = A[x, y, z]
                b = A[x, y, z + 1]
                if a != 0 and b != 0 and a != b:
                    yield (a, b)

for b in B:
    placeBrick(b , False)
    dropBrick(b)

S = set(s for s in supporting())
supports = defaultdict(lambda: [])
supportCount = defaultdict(int)
for a, b in S:
    supports[a].append(b)
    supportCount[b] += 1

stable = set(id + 1 for id in range(len(B)) if all(supportCount[b] > 1 for b in supports[id + 1]))
print("PART ONE: ", len(stable))

### <----------------------- PART TWO -----------------------> ###
def removeMain(id):
    supportCountCOPY = copy.deepcopy(supportCount)
    def remove(a):
        res = 0
        for b in supports[a]:
            supportCountCOPY[b] -= 1 
            if supportCountCOPY[b] == 0: 
                res += 1 + remove(b)
        return res
    return remove(id)

print("PART TWO: ", sum(removeMain(id + 1) for id in range(len(B))))
