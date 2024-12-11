from typing import DefaultDict


A, B = list(zip(*[list(map(int, l.strip().split())) for l in open("2024/input/01.txt").readlines()]))

print("PART ONE: ", sum(abs(a - b) for a, b in zip(sorted(A), sorted(B))))

D = DefaultDict(int)
for b in B:
    D[b] += 1

print("PART TWO: ", sum(a * D[a] for a in A))

