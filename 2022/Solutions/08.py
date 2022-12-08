import numpy as np
input = np.array([list(map(int, row)) for row in open("2022/Input/08.txt").read().strip().split("\n")])
n, m = np.shape(input)

### <---------------- PART ONE ----------------> ###
V = np.zeros((n + 2, m + 2))
Ttemp = V.copy() - 1
Ttemp[1:n+1, 1:m+1] = input
T = Ttemp

for _ in range(4):
    T_ = T.copy()
    for i in range(1,n+1):
        for j in range(1,m+1):
            T_[i,j] = max(T_[i,j], T_[i,j-1])
            V[i,j] += T_[i,j] > T_[i,j-1]
    T = np.rot90(T)
    V = np.rot90(V)
print("PART ONE:", np.sum(V > 0))

### <---------------- PART TWO ----------------> ###
def scenicScore(x, y, T=input):
    dx_dy = [[0,1], [0,-1], [1,0], [-1,0]]
    acc = 1
    for dx, dy in dx_dy:
        if not(0 <= x + dx < n) or not(0 <= y + dy < m): 
            acc = 0
            break # no trees on one side, border tree.
        r = 1
        while(T[x + dx * r, y + dy * r] < T[x, y]):
            r += 1
            if not(0 <= x + dx * r < n) or not(0 <= y + dy * r < m):
                r -= 1
                break
        acc *= r
    return acc

print("PART TWO:", max([scenicScore(i,j) for i in range(n) for j in range(m)]))