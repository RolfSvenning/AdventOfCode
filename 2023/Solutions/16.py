import numpy as np

A = np.array([[*r.strip()] for r in open("2023/input/16.txt")])
n, m = A.shape

### <----------------------- PART ONE -----------------------> ###
def beam(p, q):
    V = set()
    S = [(p, q)]
    while S:
        p, q = S.pop()
        x, y = q
        if x < 0 or x >= n or y < 0 or y >= m or (*q, *(q - p)) in V: continue 
        V.add((*q, *(q - p)))
        match A[tuple(q)]:
            case ".": S.append((q, q + q - p))
            case "|": 
                if (q - p)[1] == 0: S.append((q, q + q - p))
                else:
                    S.append((q, q + np.array((-1, 0))))
                    S.append((q, q + np.array(( 1, 0))))
            case "-": 
                if (q - p)[0] == 0: S.append((q, q + q - p))
                else:
                    S.append((q, q + np.array((0, -1))))
                    S.append((q, q + np.array((0,  1))))
            case "/":  S.append((q, q + -(q - p)[::-1]))
            case "\\": S.append((q, q +  (q - p)[::-1]))
    return len(set((a, b) for a, b, _, _ in V))

print("PART ONE: ", beam(np.array((0, -1)), np.array((0, 0))))

### <----------------------- PART TWO -----------------------> ###
R1 = [beam(np.array((i, -1)), np.array((i, 0))) for i in range(n)]
R2 = [beam(np.array((i, m)), np.array((i, m - 1))) for i in range(n)]
C1 = [beam(np.array((-1, i)), np.array((0, i))) for i in range(m)]
C2 = [beam(np.array((n, i)), np.array(( 0, i))) for i in range(m)]

print("PART TWO: ", max(R1 + R2 + C1 + C2))
