import numpy as np
import heapq

A = np.array([[*r.strip()] for r in open("2023/input/17.txt")], int)
n, m = A.shape

RIGHT, DOWN, LEFT, UP = (0, 1), (1, 0), (0, -1), (-1, 0)

### <----------------------- PART ONE AND TWO -----------------------> ###
def Dijkstra(s1, s2, Ns, CONS = 3, REQ = 0):
    Q = []
    heapq.heappush(Q, (A[0, 1], s1))
    heapq.heappush(Q, (A[1, 0], s2))
    D = {s1 : A[0, 1], s2 : A[1, 0]}
    V = set()
    while Q:
        dist, p = heapq.heappop(Q)
        if p in V: continue
        if p[0] == (n - 1, m - 1) and p[2] >= REQ: return dist
        V.add(p)
        D[p] = dist
        for q in Ns(p, CONS, REQ):
            heapq.heappush(Q, (dist + A[q[0]], q))

def makeMove(p, move):
    pos, dir, cons = p
    x, y = pos
    dx, dy = move
    return (x + dx, y + dy), move, cons + 1 if dir == move else 1

def N(p, CONS, REQ):
    pos, dir, cons = p
    x, y = pos 
    dx, dy = dir
    if cons < REQ: return [makeMove(p, dir)] if 0 <= x + dx < n and 0 <= y + dy < m else []

    up     = [makeMove(p, UP)   ]  if x > 0       and dir != DOWN   and  (dir != UP    or cons < CONS)  else []
    down   = [makeMove(p, DOWN) ]  if n - 1 > x   and dir != UP     and  (dir != DOWN  or cons < CONS)  else []
    left   = [makeMove(p, LEFT) ]  if y > 0       and dir != RIGHT  and  (dir != LEFT  or cons < CONS)  else []
    right  = [makeMove(p, RIGHT)]  if m - 1 > y   and dir != LEFT   and  (dir != RIGHT or cons < CONS)  else []
    return up + down + left + right

s1 = (0, 1), (0, 1), 1
s2 = (1, 0), (1, 0), 1
print("PART ONE: ", Dijkstra(s1, s2, N))
print("PART TWO: ", Dijkstra(s1, s2, N, CONS = 10, REQ = 4))
