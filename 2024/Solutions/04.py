I = [list(l.strip()) for l in open("2024/input/04.txt").readlines()]

n, m = len(I), len(I[0])

def valid(s): 
    return s == "XMAS" or s == "SAMX"

R = 0
for i in range(n):
    for j in range(m):
        # right
        R += valid("".join(I[i][j:j + 4]))
        # down
        R += valid("".join([I[k][j] for k in range(i, min(i + 4, n))]))
        # right + down
        R += valid("".join([I[i + k][j + k] for k in range(0, 4) if i + k < n and j + k < m]))
        # left + down
        R += valid("".join([I[i + k][j - k] for k in range(0, 4) if i + k < n and 0 <= j - k]))

print("PART ONE: ", R)

def valid2(s): 
    return s == "MAS" or s == "SAM"

R = []
for i in range(n):
    for j in range(m):
        # right + down
        if valid2("".join([I[i + k][j + k] for k in range(0, 3) if i + k < n and j + k < m])):   R += [(i + 1, j + 1)]
        # left + down
        if valid2("".join([I[i + k][j - k] for k in range(0, 3) if i + k < n and 0 <= j - k])):  R += [(i + 1, j - 1)]

print("PART TWO: ", len(R) - len(set(R)))

