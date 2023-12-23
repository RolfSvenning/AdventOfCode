import copy
from functools import cache
import sys
import numpy as np 

A = np.array([[*l.strip()] for l in open("2023/Input/23.txt")])
# print(A)
n, m = A.shape
s = (0, 1)
t = (n - 1, m - 2)
print("s, t: ", A[s], A[t])
print("n * m: ", n * m)

### <----------------------- PART ONE -----------------------> ###
def N(last, p, V=set()):
    x_, y_ = p
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = x_ + dx, y_ + dy
        if not (0 <= x < n and 0 <= y < m and (x, y) != last and A[x, y] != "#" and (x, y) not in V): continue
        # if dy == -1 and A[x, y] == ">": continue # for part 1
        # if dx == -1 and A[x, y] == "v": continue # for part 1
        yield x, y


B = np.zeros_like(A, int)
sys.setrecursionlimit(5000)

def longestPath(last, cur, V):
    # start = cur
    if cur == t: return 0
    if len(list(N(last, cur, V))) == 0: 
        # B[start] = -(n + m)
        return -(n + m)

    pathLength = 0
    pathV = set()
    while len(list(N(last, cur, V))) == 1:
        print("pathing: ", cur)
        V.add(cur)
        pathV.add(cur)
        pathLength += 1
        last = cur
        cur = list(N(last, cur, V))[0]
    V.add(cur)
    pathV.add(cur)

    if cur == t: return pathLength
    if len(list(N(last, cur, V))) == 0: 
        # B[start] = -(n + m)
        return -(n + m)

    res = 0
    print("-----splitting: ", cur, list(N(last, cur, V)))
    for q in N(last, cur, V):
        print("---splits: ", q)
        V.add(q)
        res = max(res, 1 + longestPath(cur, q, V))
        V.remove(q)
    V = V - pathV    
    # B[start] = max(B[cur], res)
    return res + pathLength

V = set()
print("PART ONE: ", longestPath(s, s, V))

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