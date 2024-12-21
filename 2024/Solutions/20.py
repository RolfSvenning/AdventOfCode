from collections import defaultdict, deque 

I = [list(l.strip()) for l in open("2024/Input/20.txt").readlines()]
for i in range(len(I)):
    if "S" in I[i]: Sx, Sy = (i, I[i].index("S"))
    if "E" in I[i]: Ex, Ey = (i, I[i].index("E"))

n, m = len(I), len(I[0])

### <----------------------- PART ONE & TWO -----------------------> ###

def Ns(x, y, I):
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if not (0 <= x + dx < n):       continue
        if not (0 <= y + dy < m):       continue
        if I[x + dx][y + dy] == "#":    continue
        yield (x + dx, y + dy)

def BFS(I):
    D = defaultdict(int)
    H = deque([((Sx, Sy), 0)])

    while H:
        xy, d = H.popleft()
        if xy in D: continue
        D[xy] = d
        for ns in Ns(*xy, I):
            H.append((ns, d + 1))  

    return D

def cheat(i, j, s, C, D):
    for dx in range(-s, s + 1):
        for dy in range(-(s - abs(dx)), (s - abs(dx)) + 1):
                if not (0 <= i + dx < n): continue
                if not (0 <= j + dy < m): continue
                C[D[i + dx, j + dy] - D[i, j] - abs(dx) - abs(dy)] += 1
    return C

def f(I, s):
    D = BFS(I)
    C = defaultdict(int)
    for i in range(n): 
        for j in range(m):
            if I[i][j] == "#": continue
            C = cheat(i, j, s, C, D)

    return C


print("PART ONE: ", sum(count for s, count in f(I,  2).items() if s >= 100))
print("PART TWO: ", sum(count for s, count in f(I, 20).items() if s >= 100))


