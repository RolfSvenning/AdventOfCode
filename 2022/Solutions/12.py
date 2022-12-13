from typing import Tuple
import numpy as np

map = np.array([list(l.strip()) for l in open("2022/Input/12.txt").readlines()])
n, m = np.shape(map)
print(n,m)
start = tuple(x[0] for x in np.where(map == "E"))
print(start)


def neighbours(x, y):
    ns = []
    if 0 <= x - 1 < n and 0 <= y < m: ns += [(x - 1, y)]
    if 0 <= x + 1 < n and 0 <= y < m: ns += [(x + 1, y)]
    if 0 <= x < n and 0 <= y - 1 < m: ns += [(x, y - 1)]
    if 0 <= x < n and 0 <= y + 1 < m: ns += [(x, y + 1)]
    return ns

visited = {start: 0}
print("visited: ", visited)
def BFS(x, y, dist):
    print(f"x={x} y={y} dist={dist}")

    for neighbour in neighbours:
        if neighbour not in visited:
            visited[neighbour] = visited[(x,y)]
            BFS(*neighbour, dist + 1)





BFS(*start, 0)

