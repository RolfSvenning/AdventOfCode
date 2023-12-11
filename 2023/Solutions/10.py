import numpy as np

A = np.array([[*l.strip()] for l in open("2023/Input/10.txt")])

n1, m1 = A.shape
s = np.where(A == "S")
s = s[0][0], s[1][0]


### <----------------------- PART ONE -----------------------> ###

def onlyValid(Ps):
    return [p for p in Ps if 0 <= p[0] < n1 and 0 <= p[1] < m1]

def Ns(p):
    px, py = p
    above  = [(px - 1, py)] if px > 1      and A[(px - 1, py)] in "|7F" else []
    below  = [(px + 1, py)] if n1 - 1 > px  and A[(px + 1, py)] in "|LJ" else []
    left   = [(px, py - 1)] if py > 1      and A[(px, py - 1)] in "-FL" else []
    right  = [(px, py + 1)] if m1 - 1 > py  and A[(px, py + 1)] in "-J7" else []

    if above and below: A[p] = "|"
    if left and right: A[p] = "-"
    if below and right: A[p] = "F"
    if above and right: A[p] = "L"
    if above and left: A[p] = "J"
    if below and left: A[p] = "7"

    return N(p)


def N(p, c=None):
    px, py = p
    match A[p] if c is None else c:
        case "|":   return [(px - 1, py), (px + 1, py)]
        case "-":   return [(px, py - 1), (px, py + 1)]
        case "L":   return [(px - 1, py), (px, py + 1)]
        case "J":   return [(px - 1, py), (px, py - 1)]
        case "7":   return [(px + 1, py), (px, py - 1)]
        case "F":   return [(px + 1, py), (px, py + 1)]
        case "S":   return Ns(p)
        case _:     raise NotImplemented


def N1(p):
    return onlyValid(N(p))

def BFS(s, fN):
    Q = [s]
    V = {s}
    i = 0
    while i < len(Q):
        for p in fN(Q[i]):
            if p in V: continue
            Q.append(p)
            V.add(p)
        i = i + 1
    return i, V

cycleLength, V = BFS(s, N1)
print("PART ONE: ", cycleLength // 2)

### <----------------------- PART TWO -----------------------> ###
# stretch input
n2, m2 = n1 * 3, m1 * 3
B = np.empty((n2, m2), dtype="str")
B.fill(".")

# list(zip(*[(1,2),(3,4)]))  --->  [(1, 3), (2, 4)]

def M(i, j): return (3 * i + 1, 3 * j + 1)

for p1 in V:
    p1_B = M(*p1)
    B[M(*p1)] = "o"
    # print(N(p1_B, A[p1]))
    # print(tuple(zip(*N(p1_B, A[p1]))))
    for p2 in N(p1_B, A[p1]):
        B[p2] = "x"

def N2(p):
    px, py = p
    xs = [(x, py) for x in range(px - 1, px + 2, 2) if 0 <= x < n2]
    ys = [(px, y) for y in range(py - 1, py + 2, 2) if 0 <= y < m2]
    return [p for p in xs + ys if B[p] == "."]

for dx, dy in [(-1, -1), (1, 1), (1, -1), (-1, 1)]:
    s2 = (M(*s)[0] + dx, M(*s)[1] + dy)
    _, V2 = BFS(s2, N2)
    if (0,0) in V2: continue
    for p in V2:
        B[p] = "å"

    print("PART TWO: ", sum(1 for i in range(n1) for j in range(m1) if B[M(i, j)] == "å"))
