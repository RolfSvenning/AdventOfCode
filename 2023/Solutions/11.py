import numpy as np
import heapq

ls = np.array([l.strip() for l in open("2023/Input/11.txt")])
A = np.array([[*l] for l in ls])

### <----------------------- PART ONE AND TWO -----------------------> ###
def distBetweenRows(A):
    rs = ["".join(r) for r in A.tolist()]
    n, m = len(rs), len(rs[0])
    RS = []
    DR = {}
    r = 0
    i = 0
    for i in range(n):
        if rs[i] == m * ".": 
            continue
        RS.append(rs[i])
        j = i + 1
        while j < n:
            if rs[j] == m * ".": 
                j = j + 1
                continue
            DR[r] = j - i
            r = r + 1
            i = j
            break
                
    return np.array([[*r] for r in RS]), DR

A, RD = distBetweenRows(A)
AT, CD = distBetweenRows(A.T)
A = AT.T

n, m = A.shape

def expand(d, expansion): 
    return (d - 1) * expansion + 1

def N(p):
    px, py = p
    above  = [(RD[px - 1], (px - 1, py))]  if 0 < px      else []    
    below  = [(RD[px], (px + 1, py))]      if px < n - 1  else []    
    left   = [(CD[py - 1], (px, py - 1))]  if 0 < py      else []    
    right  = [(CD[py], (px, py + 1))]      if py < m - 1  else []    
    return above + below + left + right

def Dijkstra(s, expansion):
    D = {s : 0}
    Q = []
    heapq.heappush(Q, (0, s))
    V = set()
    while Q:
        p1, a = heapq.heappop(Q)
        if a in V: continue
        V.add(a)
        D[a] = p1
        for dist, b in N(a):
            p2 = p1 + expand(dist, expansion)
            heapq.heappush(Q, (p2, b))
    return D

SX, SY = np.where(A=="#")
S = list(zip(SX, SY))

def solve(expansion):
    res = 0
    for s in S:
        D = Dijkstra(s, expansion)
        for t in S:
            res += D[t]
    return res // 2

print("PART ONE: ", solve(2))
print("PART TWO: ", solve(1000000))




# print(CD)
# print(N((0,2)))

### <----------------------- PART ONE -----------------------> ###
# ls = np.array([l.strip() for l in open("2023/Input/11.txt")])
# A = np.array([[*l] for l in ls])

# def doubleRows(A):
#     rs = ["".join(r) for r in A.tolist()]
#     m = A.shape[1]
#     lsDoubled = list(itertools.chain.from_iterable([[l, l] if l==(m*".") else [l] for l in rs]))
#     return np.array([[*l] for l in lsDoubled])

# A = doubleRows(A)
# A = doubleRows(A.T)
# A = A.T
# n, m = A.shape

# SX, SY = np.where(A=="#")
# S = list(zip(SX, SY))

# def BFS(s, fN):
#     D = np.zeros_like(A, int)
#     Q = [s]
#     V = {s}
#     i = 0
#     while i < len(Q):
#         for p2 in fN(p1:=Q[i]):
#             if p2 in V: continue
#             Q.append(p2)
#             V.add(p2)
#             D[p2] = D[p1] + 1
#         i = i + 1
#     return D

# def N(p):
#     px, py = p
#     xs = [(x, py) for x in range(px - 1, px + 2, 2) if 0 <= x < n]
#     ys = [(px, y) for y in range(py - 1, py + 2, 2) if 0 <= y < m]
#     return xs + ys

# res = 0
# for i, s in enumerate(S):
#     D = BFS(s, N)
#     for t in S:
#         res += D[t]

# print(res // 2)

# too high 9781156665898