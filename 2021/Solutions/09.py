import numpy as np
from heapq import nlargest
from functools import reduce


def part_one_and_two():
    heights1 = [[9] + [int(h) for h in list(line.strip())] + [9] for line in open("2021/input/09.txt")] # for s in line.split("|")[1].strip().split(" ")]
    d = len(list(next(open("2021/input/09.txt")).strip()))
    n = len(heights1)
    heights1.insert(0, [9] * (d + 2))
    heights1.append([9] * (d + 2))
    heights = np.array(heights1)

    sum = 0
    lowPoints = []
    for i in range(1, n + 1):
        for j in range(1, d + 1):
                if heights[i, j] < min(heights[i - 1, j], heights[i + 1, j], heights[i, j - 1], heights[i, j + 1]):
                    sum += heights[i, j] + 1
                    lowPoints.append((i, j))
    print("Part one, sum of risk levels of low points: ", sum)

    basinSizes = []
    for x,y in lowPoints:
        basinSizes.append(findBasin(x, y, np.zeros_like(heights), heights))
    print("Part two, product of 3 largest basins: ", reduce(lambda x, y: x * y, nlargest(3, [s for s,_ in basinSizes])))

def findBasin(x, y, visited, heights):
    visited[x,y] = 1
    topSize, visited = findBasin(x - 1, y, visited, heights) if not visited[x - 1, y] and heights[x - 1, y] != 9 else (0, visited)
    downSize, visited = findBasin(x + 1, y, visited, heights) if not visited[x + 1, y] and heights[x + 1, y] != 9 else (0, visited)
    rightSize, visited = findBasin(x, y + 1, visited, heights) if not visited[x, y + 1] and heights[x, y + 1] != 9 else (0, visited)
    leftSize, visited = findBasin(x, y - 1, visited, heights) if not visited[x, y - 1] and heights[x, y - 1] != 9 else (0, visited)
    return (1 + leftSize + rightSize + topSize + downSize), visited


if __name__ == '__main__':
    part_one_and_two()