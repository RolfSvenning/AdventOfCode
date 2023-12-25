import numpy as np 

A = np.array([[*l.strip()] for l in open("2023/Input/23.txt")])
n, m = A.shape
s = (0, 1)
t = (n - 1, m - 2)
print("s, t: ", A[s], A[t])
print("n * m: ", n * m)

### <----------------------- PART ONE -----------------------> ###
def N(last, p, V=set(), partOne=False):
    x_, y_ = p
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = x_ + dx, y_ + dy
        if not (0 <= x < n and 0 <= y < m and (x, y) != last and A[x, y] != "#" and (x, y) not in V): continue
        if partOne:
            if dy == -1 and A[x, y] == ">": continue
            if dx == -1 and A[x, y] == "v": continue
        yield x, y


def shortcuts(D):
    for i in range(n):
        for j in range(m):
            p = i, j
            Ns = len(list(N(p, p)))
            if D[i][j] or A[p] == "#" or Ns <= 2: continue
            for q in N(p, p):
                last = p
                cur = q
                pathLength = 0
                while len(list(N(last, cur))) == 1:
                    pathLength += 1
                    curNext = list(N(last, cur))[0]
                    last = cur
                    cur = curNext
                if cur == s or cur == t: continue
                i1, j1 = q
                D[i1][j1] = [last, cur, pathLength]
                i2, j2 = last
                D[i2][j2] = [q, p, pathLength]

D = [[[] for _ in range(m)] for _ in range(n)]
shortcuts(D)

res = [0]
def longestPath(last, cur, V, dist):
    x, y = cur
    if D[x][y]:
        last, cur, pathLength = D[x][y]
        if cur in V: return
    else:
        pathLength = 0
        while len(list(N(last, cur, V))) == 1:
            pathLength += 1
            curNext = list(N(last, cur, V))[0]
            last = cur
            cur = curNext

    if cur == t:
        newRes = dist + pathLength
        if res[0] < newRes:
            res[0] = newRes
            print(newRes)
        return 
    
    if len(list(N(last, cur, V))) == 0: return
         
    V.add(cur) 
    for q in N(last, cur, V):        
        longestPath(cur, q, V, 1 + dist + pathLength)
    V.remove(cur)



V = set([s])
print("PART TWO: ", longestPath((0, 0), s, V, 0))

