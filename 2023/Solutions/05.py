from os import supports_effective_ids
import re

seeds = list(map(int, re.findall("\d+", open("2023/input/05.txt").readline())))
seedRanges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(int(len(seeds) / 2))]
ls = [re.findall("(\d+) (\d+) (\d+)", l) for l in open("2023/input/05.txt").read().split(":")[2:] ]


for i,maps in enumerate(ls):
    for i,seed in enumerate(seeds):
        for rs in maps:
            foundMap = False
            (d, s, l) = list(map(int, rs))
            if seed in range(s, s + l):
                seeds[i] = d + seed - s
                foundMap = True
            if foundMap: break

print(seeds)
print("PART ONE: ", min(seeds))


print(seedRanges)
for i,maps in enumerate(ls):
    for i,(a,b) in enumerate(seedRanges):
        for rs in maps:
            foundMap = False
            (d, s, l) = list(map(int, rs))
            if seed in range(s, s + l):
                seeds[i] = d + seed - s
                foundMap = True
            if foundMap: break