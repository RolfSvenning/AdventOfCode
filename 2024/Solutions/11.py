from functools import cache
I = list(map(int, open("2024/Input/11.txt").readline().split(" ")))


### <----------------------- PART ONE -----------------------> ###

@cache
def f(x, b):
    if b == 0: return 1
    if x == 0: return f(x + 1, b - 1)
    if len(str(x)) % 2 == 0: return f(int(str(x)[:len(str(x)) // 2]), b - 1) + f(int(str(x)[len(str(x)) // 2:]), b - 1)
    return f(2024 * x, b - 1)


print("PART ONE: ", sum(f(x, 25) for x in I))

### <----------------------- PART TWO -----------------------> ###

print("PART TWO: ", sum(f(x, 75) for x in I))
