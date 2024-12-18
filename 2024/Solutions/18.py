from collections import deque 
from copy import deepcopy

Bs = [tuple(map(int, l.split(","))) for l in open("2024/Input/18.txt").readlines()]
n = m = 71
M = [list("." * n) for _ in range(n)]

### <----------------------- PART ONE -----------------------> ###

def Ns(x, y, M):
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if not (0 <= x + dx < n):       continue
        if not (0 <= y + dy < m):       continue
        if M[y + dy][x + dx] == "#":    continue
        yield (x + dx, y + dy)

def BFS(M):
    D = {}
    H = deque([((0, 0), 0)])

    while H:
        xy, d = H.popleft()
        if xy in D: continue
        D[xy] = d
        for ns in Ns(*xy, M):
            H.append((ns, d + 1))        
    return D

def f(M):
    M = deepcopy(M)
    for i in range(1024):
        x, y = Bs[i]
        M[y][x] = "#"
    return BFS(M)[(n - 1, m - 1)]
    
print("PART ONE: ", f(M))

### <----------------------- PART TWO -----------------------> ###


i = 0
j = len(Bs)
while i < j - 1:
    mid = (i + j) // 2

    M1 = deepcopy(M)
    for k in range(mid + 1):
        x, y = Bs[k]
        M1[y][x] = "#"

    if (n - 1, m - 1) in BFS(M1):   i = mid
    else:                           j = mid

x, y = Bs[j]
print("PART TWO: ", f"{x},{y}")
        



