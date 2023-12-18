import numpy as np
from functools import cmp_to_key

input1 = [[dir, int(c)] for dir, c, _ in [r.strip().split(" ") for r in open("2023/input/18.txt")]]
D = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}
input2 = [(D[int(h[-2])], int(h[2:-2], 16)) for _, _, h in [r.strip().split(" ") for r in open("2023/input/18.txt")]]

### <----------------------- PART ONE -----------------------> ###
def makeMoves(M):
    B = [(0, 0)]
    x, y = 0, 0
    for dir, c in M:
        match dir:
            case "R":   
                B = B + [(x,           y + i + 1  ) for i in range(c)] 
                y = y + c
            case "L": 
                B = B + [(x,           y - (i + 1)) for i in range(c)] 
                y = y - c
            case "D": 
                B = B + [(x + i + 1,   y          ) for i in range(c)] 
                x = x + c
            case "U": 
                B = B + [(x - (i + 1), y          ) for i in range(c)] 
                x = x - c
    return B
    

B1 = makeMoves(input1)
nMin, mMin = [min(ls) for ls in zip(*B1)]
B1 = [(x - nMin, y - mMin) for x, y in B1]
n, m = [max(ls) + 1 for ls in zip(*B1)]
C = np.zeros((n, m), int)
C[tuple(zip(*B1))] = 1

def N(p):
    x, y = p
    return [(x, y) for x, y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y+ 1)] if 0 <= x < n and 0 <= y < m]

def BFS(s):
    V = set()
    Q = [s]
    while Q:
        p = Q.pop()
        if p in V or C[p] == 1: continue
        V.add(p)
        C[p] = 2 # TODO 1 TODO 1 TODO 1 TODO 1 TODO 1
        for q in N(p):
            Q.append(q)

s = (1 - nMin, 1 - nMin)
BFS(s)
# print(C[250:275, 109:130])
# print(C)

print("PART ONE: ", np.sum(C == 1) + np.sum(C == 2))

### <----------------------- PART TWO -----------------------> ###

def makeMoves2(M):
    B = [(0, 0)]
    x, y = 0, 0
    for dir, c in M:
        match dir:
            case "R": y = y + c
            case "L": y = y - c
            case "D": x = x + c
            case "U": x = x - c
        B = B + [[x, y]]
    return B

C = makeMoves2(input2)
C = C + [C[1]]
# print(B2)
# nMin, mMin = [min(ls) for ls in zip(*B2)]
# C = [[y, x] for x, y in C]  # TODO remove?  TODO remove?  TODO remove?  TODO remove? 
print("C:  ", C)

def makesRightTurn(i):
    i = i + 1
    y1, x1 = C[i - 1]
    y2, x2 = C[i]
    y3, x3 = C[i + 1]
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1) > 0

def fix(i):
    return (makesRightTurn(i) and makesRightTurn(i - 1)) - (not makesRightTurn(i) and not  makesRightTurn(i - 1))

def makeMovesWithCoords(M):
    B = [(0, 0)]
    x, y = 0, 0
    for i in range(len(M)):
        dir, c = M[i]

        match dir:
            case "R": y = y + c + fix(i)
            case "L": y = y - c - fix(i)
            case "D": x = x + c + fix(i)
            case "U": x = x - c - fix(i)

        B = B + [[x, y]]
    return B

B2 = makeMovesWithCoords(input2)
print("B2: ", B2)

Rs = []
for i in range(len(B2) - 1):
    r = np.array([B2[i], B2[i + 1]]).T
    # print(r)
    Rs.append(r)
# print(Rs)

# print("PART TWO: ", [np.linalg.det(r) for r in Rs])
print("PART TWO: ", sum([np.linalg.det(r) for r in Rs]) / 2)

#4305 too low
#122109766395552 too low
#122109860712709

# B2 = [(1, 6), (3, 1), (7, 2), (4, 4), (8, 5), (1, 6)]

# def makeMovesWithCoords(M, C):
#     def makesRightTurn(i):
#         y1, x1 = C[i]
#         y2, x2 = C[i + 1]
#         y3, x3 = C[i + 2]
#         return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1) > 0

#     B = [(0, 0)]
#     x, y = 0, 0
#     for i in range(len(M)):
#         # print(i, M[i], C[i], makesRightTurn(i))
#         dir, c = M[i]

#         match dir:
#             case "R": y = y + c + makesRightTurn(i)
#             case "L": y = y - c - makesRightTurn(i)
#             case "D": x = x + c + makesRightTurn(i)
#             case "U": x = x - c - makesRightTurn(i)

#         B = B + [[x, y]]
#     return B

# def intersecting(r, ra):
#     return None

# res = 0
# A = []
# for r in Rs:
#     if not A: 
#         A = [r]
#         res 

#     nextA = []
#     for ra in A:
#         intersect, area = intersecting(r, ra)
#         res += area
#         nextA += intersect
#     A = nextA

