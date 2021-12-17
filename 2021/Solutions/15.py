import numpy as np
from heapq import heappop, heappush


def part_one_and_two():
    lines = [[int(n) for n in line] for line in open("2021/input/15.txt").read().split("\n")]
    M = np.array(lines, dtype=int)
    # FOR PART TWO -----------------------------------------------------------------------------------------------------
    M_ = M.copy()
    verticals = []
    for i in range(0,5):
        M_ = M.copy() + i
        for j in range(1,5):
            M_ = np.concatenate((M_, M + i + j), axis=0)
        verticals.append(M_)
    
    M_ = verticals[0]
    for vert in verticals[1:]:
        M_ = np.concatenate((M_, vert), axis=1)

    M = ((M_ - 1) % 9) + 1
    # ------------------------------------------------------------------------------------------------------------------
    n,d = np.shape(M)

    def getNeighbours(x,y):
        return [(a,b) for a,b in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] if 0 <= a < n and 0 <= b < d]

    dist = np.zeros_like(M) + np.sum(M)
    dist[0,0] = 0
    Q = []
    for v in [(i,j) for i in range(n) for j in range(d)]:
        heappush(Q, (dist[v], (v)))

    # DIJKSTRA
    while Q != []:
        ud, u = heappop(Q)
        if u == (n - 1,d - 1):
            break
        for v in getNeighbours(u[0], u[1]):
            uvDist = ud + M[v]
            if uvDist < dist[v]:
                dist[v] = uvDist
                heappush(Q, (uvDist, v))

    print("Part one, shortest path: ", dist[int(n / 5) - 1, int(d / 5) - 1])
    print("Part two (25 times larger board) shortest path: ", dist[-1,-1])

if __name__ == '__main__':
    part_one_and_two() 