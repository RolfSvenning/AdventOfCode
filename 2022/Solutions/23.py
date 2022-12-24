import numpy as np
from collections import defaultdict


I = np.array([list(l.strip()) for l in open("2022/Input/23.txt").readlines()])
elves = set((x,y) for x,y in zip(np.where(I == "#")[0], np.where(I == "#")[1]))
n = len(elves)

def isEmptyAround(xy, elves):
    x,y = xy
    return all([(x + dx, y + dy) not in elves if dx != 0 or dy != 0 else 1 for dx in [-1, 0, 1] for dy in [-1, 0, 1]])

def getProposal(xy, elves, first):
    x,y = xy
    order = [[(-1, -1), (-1,  0), (-1, 1)], # N
             [( 1, -1), ( 1,  0),  (1, 1)], # S
             [(-1, -1), ( 0, -1), (1, -1)], # W 
             [(-1,  1), ( 0,  1), (1,  1)]] # E
    for i in range(first, (first + 4)):
        if all([(x + dx, y + dy) not in elves for dx,dy in order[i % 4]]):
            dx, dy = order[i % 4][1]
            return (x + dx, y + dy)
    return xy

r = 1
first = 0
while True:
    # FIRST HALF
    ps = defaultdict(int) # proposals
    for e in elves:
        if isEmptyAround(e, elves): continue
        ps[getProposal(e, elves, first)] += 1
    
    # SECOND HALF
    elves2 = set([e if isEmptyAround(e, elves) or ps[getProposal(e, elves, first)] > 1 else getProposal(e, elves, first) for e in elves])
    if elves == elves2:
        print(f"PART TWO: {r}")
        break
    elves = elves2

    if r == 10:
        xs, ys = [x for x,_ in elves], [y for _,y in elves]
        xmin, xmax, ymin, ymax = min(xs), max(xs), min(ys), max(ys)
        print("PART ONE:", (xmax - xmin + 1) * (ymax - ymin + 1) - n)
    
    r += 1
    first = (first + 1) % 4
    print(f"round: {r}", end="\r") 

# def printElves(elves):
#     xs,ys = [x for x,_ in elves], [y for _,y in elves]
#     xmin, xmax, ymin, ymax = min(xs), max(xs), min(ys), max(ys)
#     A = np.array([["."] * (ymax - ymin + 1) for _ in range (xmax - xmin + 1)])
#     for e in elves:
#         x,y = e
#         A[x + abs(xmin), y + abs(ymin)] = "#"
#     s = "".join(["".join(r) + "\n" for r in A])
#     print(s)
