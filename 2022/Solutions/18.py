import numpy as np

input = [np.array([int(x) for x in l.strip().split(",")]) for l in open("2022/Input/18.txt").readlines()]
n = len(input)
print("n", n)


def absD(p,q): 
    return np.sum(np.absolute(p - q))

def partOne():
    surfaceArea = 6 * n
    for a in input:
        for b in input:
            if absD(a, b) == 1: surfaceArea -= 1
            
    print("PART ONE:", surfaceArea) 
    return surfaceArea


surfaceArea = partOne()
# surfaceArea = 4536
 
maxX, maxY, maxZ = np.max(np.array(max([input[i][c]]) for i in range(n) for c in range(3)))
print(maxX, maxY, maxZ)




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

