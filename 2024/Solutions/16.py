from heapq import heappop, heappush
from collections import defaultdict

I = [list(l.strip()) for l in open("2024/Input/16.txt").readlines()]

for i in range(len(I)):
    if "S" in I[i]:
        Sx, Sy = (i, I[i].index("S"))
    if "E" in I[i]:
        Ex, Ey = (i, I[i].index("E"))

n, m = len(I), len(I[0])

### <----------------------- PART ONE -----------------------> ###

def Ns(x, y, dx, dy):
    m1 =  (1, (x + dx, y + dy, dx, dy))
    m2 =  (1000, (x, y, dy, dx))
    m3 =  (1000, (x, y, -1 * dy, -1 * dx))
    for m in [m1, m2, m3]:
        if I[m[1][0]][m[1][1]] == "#": continue
        yield m

def Dijkstra(start):
    D = defaultdict(lambda: 2000 * n * m)
    H = []
    heappush(H, (0, start)) # x, y, dx, dy
    while H:
        d, state = heappop(H)
        if state in D: continue
        D[state] = d
        x, y, dx, dy = state
        if I[x][y] == "E": return D

        for d2, (x, y, dx, dy) in Ns(*state):
            heappush(H, (d + d2, (x, y, dx, dy)))
    
    return D

D = Dijkstra((Sx, Sy, 0, 1))
print("PART ONE: ", min(D[(Ex, Ey, dx, dy)] for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]))
            

### <----------------------- PART TWO -----------------------> ###

def Ns2(state, D):
    x, y, dx, dy = state
    m1 =  x - dx, y - dy, dx, dy
    m2 =  x, y, dy, dx
    m3 =  x, y, -1 * dy, -1 * dx
    return [m for i, m in enumerate([m1, m2, m3]) if m in D and (D[m] + 1 == D[state] if i == 0 else D[m] + 1000 == D[state])]
        
def DFS(D):
    V = set()
    Q = [(Ex, Ey, dx, dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
    while Q:
        state = Q.pop()
        if state in V: continue
        V.add(state)

        for ns in Ns2(state, D):
            Q.append(ns)
            
    return V

print("PART TWO: ", len(set((i, j) for i, j, _, _ in DFS(D))))
