from functools import cache
I =[list(map(int, list(l.strip()))) for l in open("2024/Input/10.txt")]
n, m = len(I), len(I[0])

### <----------------------- PART ONE -----------------------> ###
def Ns(i, j):
    return [(i + dx, j + dy) for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)] if 0 <= i + dx < n and 0 <= j + dy < m]

def f(i, j):
    if I[i][j] == 9: return set([(i, j)])
    return set().union(*[f(i_, j_) for i_, j_ in Ns(i, j) if I[i][j] + 1 == I[i_][j_]])

print("PART ONE: ", sum(len(f(i, j)) for i in range(n) for j in range(m) if I[i][j] == 0))


### <----------------------- PART TWO -----------------------> ###

@cache
def f2(i, j):
    if I[i][j] == 9: return 1
    return sum(f2(i_, j_) for i_, j_ in Ns(i, j) if I[i][j] + 1 == I[i_][j_])

print("PART TWO: ", sum(f2(i, j) for i in range(n) for j in range(m) if I[i][j] == 0))