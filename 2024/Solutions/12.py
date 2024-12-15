I = list(list("." + l.strip() + ".") for l in open("2024/Input/12.txt").readlines())
I = [["."] * len(I[0])] + I + [["."] * len(I[0])]
# for l in I:
#     print("".join(l))
n, m = len(I), len(I[0])

### <----------------------- PART ONE -----------------------> ###

def Ns(i, j):
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        yield i + dx, j + dy

def BFS(i_, j_):
    V = set()
    P = []
    Q = [(i_, j_)]
    s = I[i_][j_]
    
    while Q:
        i, j = Q.pop()
        if (i, j) in V: continue
        V.add((i, j))

        for ni, nj in Ns(i, j):
            if I[ni][nj] == s:
                Q.append((ni, nj))
            else:
                P.append((ni, nj))
    return V, P


prices = 0
visited = set()
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if (i, j) in visited: continue
        V, P = BFS(i, j)
        prices += len(V) * len(P)
        visited |= V

print("PART ONE: ", prices)

### <----------------------- PART TWO -----------------------> ###

def f2(V, P):
    visited = set()
    price = 0
    for i, j in V:
        for ni, nj in Ns(i, j):
            if not (ni, nj) in P: continue
            if (i, j, ni, nj) in visited: continue
            price += 1
            # fence is horizontal
            if ni - i != 0:
                for k in range(j, m - 1):
                    if not ((i, k) in V and (ni, k) in P): break
                    visited.add((i, k, ni, k))
                for k in range(j - 1, 0, -1):
                    if not ((i, k) in V and (ni, k) in P): break
                    visited.add((i, k, ni, k))
            # fence is vertical
            else:
                for k in range(i, n - 1):
                    if not ((k, j) in V and (k, nj) in P): break
                    visited.add((k, j, k, nj))
                for k in range(i - 1, 0, -1):
                    if not ((k, j) in V and (k, nj) in P): break
                    visited.add((k, j, k, nj))
    return price


prices = 0
visited = set()
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if (i, j) in visited: continue
        V, P = BFS(i, j)
        prices += len(V) * f2(V, set(P))
        visited |= V

print("PART TWO: ", prices)
