import copy
from functools import cache
import sys
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
            if dy == -1 and A[x, y] == ">": continue # for part 1
            if dx == -1 and A[x, y] == "v": continue # for part 1
        yield x, y


# B = np.zeros_like(A, int)
sys.setrecursionlimit(5000)


def shortcuts(D):
    for i in range(n):
        for j in range(m):
            # print(i, j)
            p = i, j
            Ns = len(list(N(p, p)))
            if D[i][j] or A[p] == "#" or Ns <= 2: continue
            # assert(len(list(N(p, p))) != 4)
            for q in N(p, p):
                # assert(len(list(N(p, q))) == 1)
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

for i in range(n):
    for j in range(m):
        if D[i][j]:
            # print(i, j, D[i][j])
            A[i, j] = "O"

res = [0]
def longestPath(last, cur, V, dist):
    # print(cur, V)
    start = cur
    x, y = cur
    if D[x][y]:
        last, cur, pathLength = D[x][y]
        # print("jumping last, cur, pathLength: ", last, cur, pathLength)
        if cur in V: 
            # print("dead end jump")
            return #-(2 * n * m)
    else:
        pathLength = 0
        while len(list(N(last, cur, V))) == 1:
            # print("pathing: ", cur, " next: ", list(N(last, cur, V)))
            pathLength += 1
            curNext = list(N(last, cur, V))[0]
            last = cur
            cur = curNext

    # print("pathing finished with length: ", pathLength)
    if cur == t:
        newRes = dist + pathLength
        if res[0] < newRes:
            res[0] = newRes
            print(newRes)
        return #pathLength
    
    if len(list(N(last, cur, V))) == 0: 
        # print("Dead end: ", cur)
        return #-(2 * n * m)

    rs = []
    # print("-----splitting: ", last, cur, list(N(last, cur, V)))
    V.add(cur) #A[cur] = "#"
    for q in N(last, cur, V):
        # print("---splits: ", q)
        
        rs.append(longestPath(cur, q, V, 1 + dist + pathLength))

    V.remove(cur)

    # print("joining, rs: ", rs)
    return #max(0, max(rs)) + pathLength

V = set([s])
print("PART ONE: ", longestPath((0, 0), s, V, 0))


# print(B)
# 5560 too low
# 5841 too low


# print("V: ", V)
# B[-1] = 99
# print(B[:10,:10])



# print("(3, 3), (3, 2): ", list(N((3, 3), (3, 2))))
# def longestPath(s):
#     S = [(s, s)]
#     D = defaultdict(int)
#     while S:
#         if S[-1][0] == "res":
#         last, cur = S.pop()
#         if cur == t: continue

#         for q in N(last, cur):
#             S.append((cur, q))
#             D[last] = max(D[last], 1 + D[q])
#         # A[cur] = res
#         # print(A)
#     return D[s]

# print(longestPath(s, (1, 1)) + 1)
# # print("(3, 3), (3, 2): ", list(N((3, 3), (3, 2))))



#.#####
#.....#
#.#.#.#
#.....#
#.#.#.#
#.....#
#.#.#.#
#.....#
#.#.#.#
#.....#
#.#.#.#
#.....#
#####.#