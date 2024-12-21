from functools import cache
import re

I = [l.strip() for l in open("2024/Input/21.txt").readlines()]

### <----------------------- PART ONE & TWO -----------------------> ###

D1 = {str(x): idx for x, idx in [("0", (0, 1)), ("A", (0, 2))] + [(i, (1 + ((i - 1) // 3), (i - 1) % 3)) for i in range(1, 10)]}
D2 = {str(x): idx for x, idx in [("<", (0, 0)), ("v", (0, 1)), (">", (0, 2)), ("^", (1, 1)), ("A", (1, 2))]}
Ds = [D1, D2]

def reduce(xs, i, acc):
    if i == len(xs): return acc
    return reduce(xs, i + 1, [a + p for a in acc for p in xs[i]])

def combine(xs):
    return reduce(xs, 0, [""])

@cache
def shortestPathPair(s, t, Didx): # return shortest paths between 's' and 't' (WITH FEWEST TURNS) 
    D = Ds[Didx]
    (xs, ys), (xt, yt) = D[s], D[t]
    dx, dy = xt - xs, yt - ys
    Ps = []
    if (xs + dx, ys     ) != (0 + Didx, 0): Ps.append(("v" * abs(dx) if dx < 0 else "^" * dx) + ("<" * abs(dy) if dy < 0 else ">" * dy) + "A")
    if (xs,      ys + dy) != (0 + Didx, 0): Ps.append(("<" * abs(dy) if dy < 0 else ">" * dy) + ("v" * abs(dx) if dx < 0 else "^" * dx) + "A")
    return set(Ps)


def allShortestPaths(code, mapIdx):
    code = "A" + code
    return combine([shortestPathPair(code[i],  code[i + 1], mapIdx) for i in range(len(code) - 1)])


def countRepeatedA(path): 
    return sum(len(x) - 1 for x in re.findall("AA+", path))

@cache
def F1(path, depth):
    if depth == 0: return len(path)
    # return min(F3(paths , depth - 1) for paths in F2(p_)) // instead break path into chunks separated by A for caching
    return min(sum(F1(p + "A", depth - 1) for p in path.split("A") if p != "") + countRepeatedA(path) for path in allShortestPaths(path, 1))


def F(code, depth):
    return min(F1(path, depth) for path in allShortestPaths(code, 0)) * int(code[:-1])


print("PART ONE: ", sum(F(code, 2)  for code in I))
print("PART ONE: ", sum(F(code, 25) for code in I))




