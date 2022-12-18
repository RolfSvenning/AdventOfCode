import numpy as np

lava = np.array([np.array(l) for l in sorted([[int(x) for x in l.strip().split(",")] for l in open("2022/Input/18.txt").readlines()])])
mins = np.min(lava, axis=0)
maxs = np.max(lava, axis=0)
n = len(lava)
rowsLava = [lava[np.where(lava[:,0] == i)] for i in range(mins[0], maxs[0] + 1)]
        

def absD(p,q):
    return np.sum(np.absolute(p - q))

def partOne():
    surfaceArea = 6 * n
    for i in range(len(rowsLava)):
        for a in rowsLava[i]:
            for b in rowsLava[i]:
                if absD(a, b) == 1: surfaceArea -= 1

            if i + 1 == len(rowsLava): continue
            for b in rowsLava[i + 1]:
                if absD(a, b) == 1: surfaceArea -= 2
    return surfaceArea


surfaceArea = partOne()
print("PART ONE:", surfaceArea) 


def neighbors(p):
    return [tuple([p[j] + delta if i == j else p[j] for j in range(3)]) for i in range(3) for delta in [-1, 1]]


def aroundInput(p):
    return all([(mins[i] - 1 <= p[i] <= maxs[i] + 1) for i in range(3)])


def BFS(start): # for all coords in cube defined by input paddened with one extra layer
    visited = [start]
    setLava = set(tuple(r) for r in lava)
    Q = [start]
    surfaceArea2 = 0

    for p in Q:
        for adj in neighbors(p):
            if adj in setLava: 
                surfaceArea2 += 1
                continue
            if not aroundInput(adj) or adj in visited: continue
            Q.append(adj)
            visited.append(adj)

    return surfaceArea2

print("PART TWO: ", BFS((maxs[0] + 1, maxs[1] + 1, maxs[2] + 1)))
