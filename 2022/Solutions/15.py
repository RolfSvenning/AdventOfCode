import re
from functools import cmp_to_key
from collections import defaultdict


input = [[int(x) for x in re.findall("-*\d+", l)] for l in open("2022/Input/15.txt").readlines()]
ys = [x for s in input for x in [s[1], s[3]]]
n, ymin, ymax = len(input), min(ys), max(ys)
yrange = ymax - ymin + 1

def manhattenDist(l):
    sx, sy, bx, by = l
    return abs(sx - bx) + abs(sy - by)

def returnStartAndEnd(sx, d):
    return [("s", sx - d), ("e", sx + d)]

l = [[] for _ in range(-yrange, 2*yrange)] # input wraps around!
for i in range(n):
    print(i)
    d = manhattenDist(input[i])
    sx, sy, bx, by = input[i]

    l[sy] += returnStartAndEnd(sx, d)
    for j in range(1, d + 1):
        l[sy - j] += returnStartAndEnd(sx, d - j)
        l[sy + j] += returnStartAndEnd(sx, d - j)

def orderOfEventPoints(e1, e2):
    t1, x1 = e1
    _,  x2 = e2
    if x1 == x2: 
        if t1 == "s":   return -1
        else:           return  1
    else:
        if x1 < x2:     return -1
        else:           return  1


B = defaultdict(int)
for bx, by in set([(bx, by) for _, _, bx, by in input]):
    B[by] += 1


# def calcRow(i, rowEventPoints):
#     if len(rowEventPoints) == 0: return 0
#     rowEventPoints = sorted(rowEventPoints, key=cmp_to_key(lambda e1, e2: orderOfEventPoints(e1, e2)))
#     covered = 1
#     numberOfOpenIntervals = 0
#     _, last = rowEventPoints[0]
#     for t,x in rowEventPoints:
#         if numberOfOpenIntervals > 0:
#                     covered += x - last
#         if numberOfOpenIntervals == 0 and x != last and t == "s": 
#             covered += 1
#         last = x
#         # print(covered, x)
#         match t: 
#             case "s": numberOfOpenIntervals += 1
#             case "e": numberOfOpenIntervals -= 1
#             case   _: raise NotImplementedError("should ever happen")
#     return covered - B[i] # subtract beacons


def calcRow(i, rowEventPoints, partTwo=False, xmax=-1, findIndex=False):
    assert len(rowEventPoints) > 0

    rowEventPoints = sorted(rowEventPoints, key=cmp_to_key(lambda e1, e2: orderOfEventPoints(e1, e2)))
    if partTwo: rowEventPoints = [(t, fixRange(x, xmax)) for (t,x) in rowEventPoints]
    covered = 1
    numberOfOpenIntervals = 0
    _, last = rowEventPoints[0]
    for t,x in rowEventPoints:
        if numberOfOpenIntervals > 0:
                    covered += x - last
        if numberOfOpenIntervals == 0 and x != last and t == "s": 
            covered += 1
        last = x
        match t: 
            case "s": numberOfOpenIntervals += 1
            case "e": 
                numberOfOpenIntervals -= 1
                if numberOfOpenIntervals == 0 and findIndex:
                    return x + 1
            case   _: raise NotImplementedError("should ever happen")
    return covered - B[i] # subtract beacons


### -----------------------> PART ONE -----------------------> ###
r1 = 10       # test input
# r1 = 2000000    # real input
print("PART ONE:", calcRow(r1, l[r1]))





### -----------------------> PART TWO -----------------------> ###
def fixRange(x, xmax):
    if x < 0:    return 0
    if x > xmax: return xmax
    return x

xmax = 20     # test input
# xmax = 4000000  # real input
for i in range(0, min(len(l), xmax + 1)):
    if (calcRow(i, l[i], partTwo=True, xmax=xmax, findIndex=False)) + B[i] != xmax + 1: 
        x = calcRow(i, l[i], partTwo=True, xmax=xmax, findIndex=True)
        print("PART TWO x, y:", x, ",", i, " ->", x * 4000000 + i)
        break





