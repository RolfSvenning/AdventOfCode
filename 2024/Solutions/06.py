I = [list(l.strip()) for l in open("2024/Input/06.txt").readlines()]
n, m = len(I), len(I[0])
s = 0
for i, l in enumerate(I):
    s = (i, l.index("^")) if "^" in l else s

### <----------------------- PART ONE -----------------------> ###

i, j = s
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
d = 0
S = set()

def cannotStep(i, j, d):
    if i + dir[d][0] in [-1, n] or j + dir[d][1] in [-1, m]: return False
    return I[i + dir[d][0]][j + dir[d][1]] == "#"

while (0 <= i < n and 0 <= j < m):
    S.add((i, j))
    
    while (cannotStep(i, j, d)):
        d = (d + 1) % 4
    i, j = i + dir[d][0], j + dir[d][1]

print("PART ONE: ", len(S))
    
### <----------------------- PART TWO -----------------------> ###

res = 0

for k in range(n):
    for l in range(m):
        if I[k][l] in "^#" or (k, l) not in S: continue
        I[k][l] = "#"
        i, j = s
        d = 0
        V = set()
        
        while (0 <= i < n and 0 <= j < m):
            if (state := (i, j, dir[d][0], dir[d][1])) in V: 
                res += 1
                break
            V.add(state)
            
            while (cannotStep(i, j, d)):
                d = (d + 1) % 4
            i, j = i + dir[d][0], j + dir[d][1]

        I[k][l] = "."

    

print("PART TWO: ", res)





