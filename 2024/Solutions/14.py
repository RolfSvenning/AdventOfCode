import re
from math import ceil
I = [tuple(map(int, re.findall(r"-*\d+", l))) for l in open("2024/Input/14.txt").readlines()]

### <----------------------- PART ONE -----------------------> ###

n, m = 103, 101     # 101 wide, 103 tall

def f(robots):
    return [((c + vc) % m, (r + vr) % n, vc, vr) for (c, r, vc, vr) in robots]

def f2(robots, seconds):
    if seconds == 0: return robots
    return f2(f(robots), seconds - 1)

def matrixRobots(robots):
    M = [[0] * m for _ in range(n)]
    for c, r, _, _ in robots:
        M[r][c] += 1
    return M

S100 = matrixRobots(f2(I, 100))
res = 1
for n1, n2, m1, m2 in [(0, n // 2, 0, m // 2), (ceil(n / 2), n, 0, m // 2), (0, n // 2, ceil(m / 2), m), (ceil(n / 2), n, ceil(m / 2), m)]:
    res *= sum(sum(row[m1:m2]) for row in S100[n1:n2])

print("PART ONE: ", res)

### <----------------------- PART TWO -----------------------> ###

def plotRobots(robots):
    M = matrixRobots(robots)
    print("\n".join("".join(str(x) for x in r) for r in M) + "\n")

def score(robots):
    return len(set((x, y) for x, y, _, _ in robots if x < n / 2)) # try different values (of n/x) to get the tree entirely on one side

S = list()
robots = I
for i in range(10000): # hits at 7287 17690 28093
    S.append((robots, score(robots), i))
    robots = f(robots)

print("PART TWO: ", sorted(S, key=lambda x: x[1])[-1][2])

# for i, (robots, score, seconds) in enumerate(sorted(S, key=lambda x: x[1])[-20:]):
#     print("iteration i: ", i)
#     print("score: ", score)
#     print("seconds: ", seconds)
#     plotRobots(robots)