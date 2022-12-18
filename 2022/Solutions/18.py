import numpy as np

input = np.array([np.array(l) for l in sorted([[int(x) for x in l.strip().split(",")] for l in open("2022/Input/18.txt").readlines()])])

minX, maxX = np.min(input[:,0]), np.max(input[:,0])
print("min/max", minX, maxX)
n = len(input)
print("n", n)

rows = [input[np.where(input[:,0] == i)] for i in range(minX, maxX + 1)]
        

def absD(p,q):
    return np.sum(np.absolute(p - q))

def partOne():
    surfaceArea = 6 * n
    for i in range(len(rows)):
        for a in rows[i]:
            for b in rows[i]:
                if absD(a, b) == 1: surfaceArea -= 1

            if i + 1 == len(rows): continue
            for b in rows[i + 1]:
                assert len(a) == 3, a
                assert len(b) == 3
                if absD(a, b) == 1: surfaceArea -= 2
            
            
    print("PART ONE:", surfaceArea) 
    return surfaceArea


surfaceArea = partOne()
# surfaceArea = 4536
 
# maxX, maxY, maxZ = np.max(np.array(max([input[i][c]]) for i in range(n) for c in range(3)))
# print(maxX, maxY, maxZ)


# def BFS(u):
#     visited = [u]
#     D = {(u,u):0}
#     Q = [u]
#     def BFS_visit(v):
#         for w in G1[v].edges:
#             if w in visited: continue
#             D[(u,w)] = D[(u,v)] + 1
#             Q.append(w)
#             visited.append(w)
#     for v in Q:
#         BFS_visit(v)
#     return D

# setInput = set(tuple(input[i]) for i in range(len(input)))
# print("n", len(setInput))

# def trapped(p):
#     for i in range(3):
#         for delta in [-1, 1]:
#             p_ = p[:]
#             p_[i] += delta
#             if tuple(p_) not in setInput:
#                 return 0
#     return 1


# print("trapped [2 2 5]:" , trapped([2,2,5]))

# countTrapped = 0
# for p in input:
#     for i in range(3):
#         for delta in [-1, 1]:
#             p_ = p[:]
#             p_[i] += delta
#             if tuple(p_) not in setInput and trapped(p_.tolist()): 
#                 countTrapped += 1

# print("countTrapped:", countTrapped / 3)
# print("surfaceArea:", surfaceArea)
# print("PART TWO:", surfaceArea - ((countTrapped / 3) * 6))

