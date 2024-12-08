from typing import DefaultDict


### <----------------------- PART ONE -----------------------> ###
R, U = open("2024/input/05.txt").read().split("\n\n")
R = set([tuple(map(int, r.strip().split("|"))) for r in R.split("\n")])
U = [list(map(int, u.strip().split(","))) for u in U.split("\n")]

def valid(u):
    for i in range(len(u)):
        for j in range(i, len(u)):
            if (u[j], u[i]) in R: return False
    return True

print("PART ONE: ", sum(u[len(u) // 2] for u in U if valid(u)))

### <----------------------- PART TWO -----------------------> ###
U2 = [u for u in U if not valid(u)]

def f(u):    
    E = DefaultDict(list)
    D = DefaultDict(int)
    for a, b in [(x, y) for x, y in R if x in u and y in u]:
        E[a] += [b]
        D[a] += 0
        D[b] += 1
    

    # Kahn's algorithm assuming there is a path of length 'n' in the DAG
    P = {}
    x = min(D.items(), key=lambda x: x[1])[0]
    for i in range(len(D)):
        del D[x]
        P[x] = i
        found = 0
        for y in E[x]:
            D[y] -= 1
            if D[y] == 0: 
                x = y
                found += 1
        if not found == 1 and D: print("found: ", found, D)

    return sorted(u, key=lambda x: P[x])[len(u) // 2]


print("PART TWO: ", sum(f(u) for u in U2))

