from functools import cache

T, D = open("2024/Input/19.txt").read().split("\n\n")
T, D = T.split(", "), D.split("\n")

### <----------------------- PART ONE -----------------------> ###

@cache
def f(d, f1):
    return True if not d else f1(f(d[:-i], f1) for i in range(1, len(d) + 1) if d[-i:] in T)
    
print("PART ONE: ", any(f(d, any) for d in D))

### <----------------------- PART TWO -----------------------> ###

print("PART TWO: ", sum(f(d, sum) for d in D))



