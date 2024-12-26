I = open("2024/Input/25.txt").read().split("\n\n")

def parse(x):
    L = x.split("\n")
    if L[0][0] == "#": t = "key"
    else: t = "pin"
    C = [sum(y == "#" for y in x) for x in zip(*L[1:-1])]
    return t, C

I = [parse(x) for x in I]
K = [c for t, c in I if t == "key"]
P = [c for t, c in I if t == "pin"]

### <----------------------- PART ONE -----------------------> ###

print("PART ONE: ", sum(max([k1 + p1 for k1, p1 in zip(k, p)]) <= 5 for k in K for p in P))