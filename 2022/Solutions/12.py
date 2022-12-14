import numpy as np

heightmap = np.array([list(l.strip()) for l in open("2022/Input/12.txt").readlines()])
n, m = np.shape(heightmap)
start = tuple(x[0] for x in np.where(heightmap == "S"))
end = tuple(x[0] for x in np.where(heightmap == "E"))
heightmap[start] = "a"
heightmap[end] = "z"

### -----------------------> PART ONE -----------------------> ###
def neighbours(x, y):
    ns = []
    if 0 <= x - 1 < n and 0 <= y < m: ns += [(x - 1, y)]
    if 0 <= x + 1 < n and 0 <= y < m: ns += [(x + 1, y)]
    if 0 <= x < n and 0 <= y - 1 < m: ns += [(x, y - 1)]
    if 0 <= x < n and 0 <= y + 1 < m: ns += [(x, y + 1)]
    return ns

def visitNeighbours(x, y):
    res = []
    for neighbour in neighbours(x, y):
        if ord(heightmap[neighbour]) - ord(heightmap[x,y]) > 1: continue
        if neighbour not in visited:
            visited[neighbour] = visited[(x,y)] + 1
            res += [neighbour]
    return res

visited = {start: 0}
Q = [start]
for (x,y) in Q:
    Q += visitNeighbours(x, y)

### -----------------------> PART TWO -----------------------> ###
whereA = np.where(heightmap == "a")
posA = list(zip(list(whereA[0]), list(whereA[1])))
visited = dict([((x,y), 0) for (x,y) in posA])
Q = posA
for (x,y) in Q:
    Q += visitNeighbours(x, y)

print("PART TWO:", visited[end]) #, visited[end]