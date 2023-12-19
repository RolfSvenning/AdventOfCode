import re
import copy
from functools import reduce

W, P = open("2023/input/19.txt").read().split("\n\n")
W = {k:v[:-1] for w in W.split("\n") for k, v in [w.split("{")]}
P = [re.findall("\d+", p) for p in P.split("\n")]

### <----------------------- PART ONE -----------------------> ###
C = {"x": 0, "m": 1, "a": 2, "s": 3}

def f(p, w):
    if w in "AR": return sum(map(int, p)) * (w == "A")
    for r in W[w].split(","):
        if not ":" in r: return f(p, r)
        test, w2 = r.split(":")
        test = p[C[test[0]]] + test[1:]
        if eval(test):
            return f(p, w2)

print("PART ONE: ", sum(f(p, "in") for p in P))

### <----------------------- PART TWO -----------------------> ###
def f2(p, w):
    if w == "A": return [p] * all(a <= b for a, b in p)
    if w == "R": return []
    res = []
    p2 = copy.deepcopy(p)
    for r in W[w].split(","):
        if not ":" in r: res += f2(p2, r)
        else:
            test, w2 = r.split(":")
            p3 = copy.deepcopy(p2)
            match test[1]:
                case ">": 
                    p2[C[test[0]]][1] = min(int(test[2:]), p2[C[test[0]]][1])
                    p3[C[test[0]]][0] = max(int(test[2:]) + 1, p2[C[test[0]]][0])
                case "<": 
                    p2[C[test[0]]][0] = max(int(test[2:]), p2[C[test[0]]][0])
                    p3[C[test[0]]][1] = min(int(test[2:]) - 1, p3[C[test[0]]][1])
            res += f2(p3, w2)
    return res


def m(acc, l): 
    return m((l[0][1] - l[0][0] + 1) * acc, l[1:]) if l else acc

p = [[1, 4000] for _ in range(4)]
res = f2(p, "in") 
print("PART TWO: ", reduce(lambda x, y: x + y, [m(1, r) for r in res]))
