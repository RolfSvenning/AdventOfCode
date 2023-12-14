import numpy as np
import copy

A = np.array([[*r.strip()] for r in open("2023/input/14.txt")])

### <----------------------- PART ONE -----------------------> ###
def tiltNorth(A):
    n = A.shape[0]
    for c in range(A.shape[1]):
        lastH = 0
        countO = 0
        for i in range(n):
            if A[i, c] == "O": 
                    countO += 1
            if A[i, c] == "#" or i == n - 1: 
                    for j in range(countO):
                        A[lastH + j, c] = "O"
                    for j in range(lastH + countO, i + (i == n - 1 and A[i, c] == "O")):
                        A[j, c] = "."
                    lastH = i + 1
                    countO = 0
    return A

def load(A):
    return sum(A.shape[1] - a for a, _ in list(zip(*np.where(A == "O"))))

A_ = copy.deepcopy(A)
tiltNorth(A_)
print("PART ONE: ", load(A_))

### <----------------------- PART TWO -----------------------> ###
def cycle(A):
    for _ in range(4):
        tiltNorth(A)
        A = np.rot90(A, 3)
    return A

def h(x): 
    return tuple(zip(*np.where(x == "O")))

i = 0
S = {}
C = 1000000000
while i < C:
    S[h(A)] = i
    A = cycle(A)
    i = i + 1
    if h(A) in S.keys():
        cycleLength = i - S[h(A)]
        i = i + cycleLength * ((C - i) // cycleLength)

print("PART TWO: ", load(A))