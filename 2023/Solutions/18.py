import numpy as np

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
        C[p] = 2
        for q in N(p):
            Q.append(q)

s = (1 - nMin, 1 - nMin)
BFS(s)

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

B2 = makeMovesWithCoords(input2)[::-1]

Rs = []
for i in range(len(B2) - 1):
    r = np.array([B2[i], B2[i + 1]]).T
    Rs.append(r)

print("PART TWO: ", int(sum([np.linalg.det(r) for r in Rs]) / 2))
