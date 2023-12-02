import re
from functools import reduce

# ls = [[re.findall("\d+ r|\d+ g|\d+ b", g) for g in l.strip().split(";")] for l in open("2023/input/02.txt").readlines()]
ls = [[re.findall("\d+ [rgb]", g) for g in l.strip().split(";")] for l in open("2023/input/02.txt").readlines()]
print(ls)
games = [[[d.split(" ") for d in draws] for draws in g] for g in ls]

### <----------------------- PART ONE & TWO -----------------------> ###
possibleSum = 0
powerSum = 0
for i,g in enumerate(games):
    possible = True
    M = [0,0,0]
    for draw in g:
        C = [0,0,0]
        for v,k in draw:
            v = int(v)
            match k:
                case "r": 
                    C[0] = v
                    M[0] = max(M[0],v)
                case "g": 
                    C[1] = v
                    M[1] = max(M[1],v)
                case "b": 
                    C[2] = v
                    M[2] = max(M[2],v)
                case _: raise NotImplementedError

        if any(c > y for c,y in zip(C,[12, 13, 14])): possible = False
          
    powerSum += reduce(lambda x, y: x * y, M, 1)
    if possible: possibleSum += i + 1

print(possibleSum)
print(powerSum)
