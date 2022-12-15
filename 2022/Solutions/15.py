import re
from collections import defaultdict


input = [[int(x) for x in re.findall("-*\d+", l)] for l in open("2022/Input/15.txt").readlines()]
ys = [x for s in input for x in [s[1], s[3]]]
n, ymin, ymax = len(input), min(ys), max(ys)

def manhattenDist(r):
    sx, sy, bx, by = r
    return abs(sx - bx) + abs(sy - by)

def returnStartAndEnd(sx, d):
    return [(sx - d, "a"), (sx + d, "b")]

### <--------- find event points in every row ---------> ###
maxDist = max([manhattenDist(r) for r in input])
l = [[] for _ in range(-maxDist, ymax + maxDist)] # input wraps around!

for y in range(n):
    d = manhattenDist(input[y])
    sx, sy, bx, by = input[y]

    l[sy] += returnStartAndEnd(sx, d)
    for j in range(1, d + 1):
        l[sy - j] += returnStartAndEnd(sx, d - j)
        l[sy + j] += returnStartAndEnd(sx, d - j)

B = defaultdict(int)
for bx, by in set([(bx, by) for _, _, bx, by in input]):
    B[by] += 1

### <--------- find possible positions in row ---------> ###
def calcRow(i, rowEventPoints, partTwo=False, xmax=-1, findIndex=False):
    rowEventPoints = sorted(rowEventPoints)
    if partTwo: rowEventPoints = [(fixRange(x, xmax),t) for (x,t) in rowEventPoints]
    covered = 0
    numberOfOpenIntervals = 0
    last = rowEventPoints[0][0] - 1
    for x,t in rowEventPoints:
        if numberOfOpenIntervals > 0:                             
            covered += x - last
        if numberOfOpenIntervals == 0 and x != last and t == "a": 
            covered += 1
        last = x
        if t == "a": numberOfOpenIntervals += 1
        else: # t == "b"
            numberOfOpenIntervals -= 1
            if numberOfOpenIntervals == 0 and findIndex:
                return x + 1
    return covered - B[i] # subtract beacons in row


### <----------------------- PART ONE -----------------------> ###
# r1 = 10       # test input
r1 = 2000000    # real input
print("PART ONE:", calcRow(r1, l[r1]))


### <----------------------- PART TWO -----------------------> ###
def fixRange(x, xmax):
    if x < 0:   return 0
    else:       return min(x, xmax)      

# xmax = 20     # test input
xmax = 4000000  # real input
for y in range(0, min(len(l), xmax + 1)):
    if (calcRow(y, l[y], partTwo=True, xmax=xmax, findIndex=False)) + B[y] != xmax + 1: 
        x = calcRow(y, l[y], partTwo=True, xmax=xmax, findIndex=True)
        print(f"PART TWO (x,y)=({x},{y}): {x * 4000000 + y}")
        break
