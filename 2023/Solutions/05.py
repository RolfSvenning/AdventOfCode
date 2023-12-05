import re

seeds = list(map(int, re.findall("\d+", open("2023/input/05.txt").readline())))
seedRanges = [(seeds[2 * i], seeds[2 * i] + seeds[2 * i + 1]) for i in range(int(len(seeds) / 2))]
ls = [re.findall("(\d+) (\d+) (\d+)", l) for l in open("2023/input/05.txt").read().split(":")[2:] ]

### <----------------------- PART ONE -----------------------> ###
for maps in ls:
    for i, seed in enumerate(seeds):
        for m in maps:
            d, s, l = list(map(int, m))
            if seed in range(s, s + l):
                seeds[i] = d + seed - s
                break

print("PART ONE: ", min(seeds))

### <----------------------- PART TWO -----------------------> ###
def f(r, m):
    a, b = r 
    d, s, l = list(map(int, m))
    def m(i): return d + i - s
    x, y = s, s + l

    if a in range(x, y):
        if b in range(x, y): return [(m(a), m(b))], (-1, -1)
        else:                return [(m(a), m(y))], (y, b)
    else:
        if b in range(x, y): return [(m(x), m(b))], (a, x)
        else:                return [], (a, b)

for maps in ls:
    nextRanges = []
    for r in seedRanges:
        for m in maps:
            intersect, r = f(r, m)
            nextRanges += intersect
        if r[0] != r[1]: nextRanges.append(r)
    seedRanges = nextRanges

print("PART TWO: ", min([a for a, _ in seedRanges]))