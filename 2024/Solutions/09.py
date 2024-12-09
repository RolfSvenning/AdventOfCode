import itertools, re

I = list(itertools.chain(*[[i // 2] * l if i % 2 == 0 else [-1] * l for i, l in enumerate(map(int, open("2024/Input/09.txt").read()))]))
n = len(I)


### <----------------------- PART ONE -----------------------> ###
i, j = I.index(-1), n - 1

while i < j:
    I[i], I[j] = I[j], I[i] 

    while I[j] == -1:
        j = j - 1
    while I[i] != -1:
        i = i + 1


print("PART ONE ", sum(i * v for i, v in enumerate(I[:I.index(-1)])))


### <----------------------- PART TWO -----------------------> ###

I = list(itertools.chain(*[[i // 2] * l if i % 2 == 0 else [-1] * l for i, l in enumerate(map(int, open("2024/Input/09.txt").read()))]))
print("".join(map(str, I)))
for i in reversed(range(max(I) + 1)):
    print(i)
    ni = len([x for x in I if x == i])
    si = I.index(i)

    j = re.search("-" * ni, "".join(map(str, ["-" if x == -1 else "x" for x in I[:si]])))
    if j:
        (a, b) = j.span()
        for ik, k in enumerate(range(a, b)):
            I[si + ik], I[k] = I[k], I[si + ik] 

print("PART TWO ", sum(i * v if v != -1 else 0 for i, v in enumerate(I)))
