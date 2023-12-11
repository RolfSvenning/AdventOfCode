ls = [list(map(int, l.strip().split(" "))) for l in open("2023/Input/09.txt").readlines()]


### <----------------------- PART ONE & TWO -----------------------> ###
def f(A):
    if not A: return 0, 0
    B = [A[i + 1] - A[i] for i in range(len(A) - 1)]
    n, p = f(B)
    return A[-1] + n, A[0] - p

print("PART ONE AND TWO: ", list(sum(p) for p in zip(*[f(l) for l in ls])))