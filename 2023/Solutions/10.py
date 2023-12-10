import numpy as np

A = np.array([[*l.strip()] for l in open("2023/Input/10.txt")])

n, m = A.shape
print(A)
print("n, m: ", n, m)
s = np.where(A == "S")
s = (s[0][0], s[1][0])
print("sij: ", s, A[s])


### <----------------------- PART ONE -----------------------> ###

def onlyValid(Ps):
    return [p for p in Ps if 0 <= p[0] < n and 0 <= p[1] < m]

def Ns(p):
    print("s: ", p)
    px, py = p
    above  = [(px - 1, py)] if px > 1      and A[(px - 1, py)] in "|7F" else []
    below  = [(px + 1, py)] if n - 1 > px  and A[(px + 1, py)] in "|LJ" else []
    left   = [(px, py - 1)] if py > 1      and A[(px, py - 1)] in "-FL" else []
    right  = [(px, py + 1)] if m - 1 > py  and A[(px, py + 1)] in "-J7" else []
    Np = above + below + left + right
    assert Np
    print("Ns: ", Np)
    return Np


def N(p):
    px, py = p
    match A[p]:
        case "|":   return [(px - 1, py), (px + 1, py)]
        case "-":   return [(px, py - 1), (px, py + 1)]
        case "L":   return [(px - 1, py), (px, py + 1)]
        case "J":   return [(px - 1, py), (px, py - 1)]
        case "7":   return [(px + 1, py), (px, py - 1)]
        case "F":   return [(px + 1, py), (px, py + 1)]
        case ".":   raise NotImplemented
        case "S":   return Ns(p)
        case _:     raise NotImplemented


def BFS():
    Q = [s]
    V = {s}
    i = 0
    while i < len(Q):
        for p1 in onlyValid(N(Q[i])):
            if p1 in V: continue
            Q.append(p1)
            V.add(p1)
        i = i + 1
    return i, V

cycleLength, V = BFS()
print("PART ONE: ", cycleLength // 2)


### <----------------------- PART TWO -----------------------> ###

# going right means inside is down
# def inside1(p, q):
#     px, py = p
#     qx, qy = q
#     match (qx - px, qy - py):
#         # RIGHT
#         case (0, 1):  return [qx + 1, qy]
#         # LEFT
#         case (0, -1): return [qx - 1, qy]
#         # DOWN
#         case (1, 0):  return [qx, qy - 1]
#          # UP
#         case (-1, 0): return [qx, qy + 1]
#         case _: return NotImplemented

# def N(p):
#     px, py = p
#     xs = [(x, py) for x in range(px - 1, px + 2, 2) if 0 <= x < n]
#     ys = [(px, y) for y in range(py - 1, py + 2, 2) if 0 <= y < m]
#     return xs + ys

# stretch input

B = np.empty((n * 3, m * 3), dtype="str")
B.fill(".")

# list(zip(*[(1,2),(3,4)]))  --->  [(1, 3), (2, 4)]
for i in range(n):
    for j in range(m):
        B[i * 3 + 1, j * 3 + 1] = A[i, j]
        match A[i, j]:
            case "|": 
                B[zip(*Ns((i, j)))] = "|"
            # return [(px - 1, py), (px + 1, py)]
            # case "-":   return [(px, py - 1), (px, py + 1)]
            # case "L":   return [(px - 1, py), (px, py + 1)]
            # case "J":   return [(px - 1, py), (px, py - 1)]
            # case "7":   return [(px + 1, py), (px, py - 1)]
            # case "F":   return [(px + 1, py), (px, py + 1)]
            # case ".":   raise NotImplemented
            # case "S":   return Ns(p)
            case _: continue

print(B)
