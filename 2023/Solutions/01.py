import re

### <----------------------- PART ONE -----------------------> ###
ls = [re.findall("\d", l) for l in open("2023/input/01.txt").readlines()]
ds = [int("".join([l[0], l[-1]])) for l in ls]
print("PART ONE: ", sum(ds)) 

### <----------------------- PART ONE -----------------------> ###
ds = "one|two|three|four|five|six|seven|eight|nine"
dsRev = "|".join([s[::-1] for s in ds.split("|")])
D2 = {key: str((i % 9) + 1) for i, key in enumerate(ds.split("|") + dsRev.split("|"))}

ls = [[re.search("\d|" + ds, l)[0], re.search("\d|" + dsRev , l[::-1])[0]] for l in open("2023/input/01.txt").readlines()]
values = [int("".join([D2[s] if s in D2.keys() else s for s in l])) for l in ls]
print("PART TWO: ", sum(values)) 