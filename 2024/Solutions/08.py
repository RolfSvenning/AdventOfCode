from collections import defaultdict


I = [list(l.strip()) for l in open("2024/Input/08.txt").readlines()]
n, m = len(I), len(I[0])


### <----------------------- PART ONE -----------------------> ###
F = defaultdict(list)
for i in range(n):
    for j in range(m):
        if I[i][j] != ".": F[I[i][j]] += [(i, j)]

def f(freq):
    S = set()
    for i in range(len(F[freq])):
        for j in range(i + 1, len(F[freq])):
            (x1, y1), (x2, y2) = F[freq][i], F[freq][j]
            S |= set([(x2 + x2 - x1, y2 + y2 - y1), (x1 + x1 - x2, y1 + y1 - y2)])

    return S

def valid(i, j):
    return 0 <= i < n and 0 <= j < m

print("PART ONE: ", sum(valid(i, j) for i, j in set().union(*[f(freq) for freq in F.keys()])))


### <----------------------- PART TWO -----------------------> ###

def f2(freq):
    S = set()
    for i in range(len(F[freq])):
        for j in range(i + 1, len(F[freq])):
            (x1, y1), (x2, y2) = F[freq][i], F[freq][j]
            S |= set([(x2 + (x2 - x1) * i, y2 + (y2 - y1) * i) for i in range(-n // (x2 - x1), n // (x2 - x1))])
            S |= set([(x1 + (x1 - x2) * i, y1 + (y1 - y2) * i) for i in range(-n // (x2 - x1), n // (x2 - x1))])
    
    return S


print("PART TWO: ", sum(valid(i, j) for i, j in set().union(*[f2(freq) for freq in F.keys()])))


