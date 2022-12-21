import re

input = [l.strip().split(":") for l in open("2022/Input/21.txt").readlines()]
input = dict([(k,int(v)) if re.match(" \d", v) else (k, re.findall("\S+", v)) for k,v in input])

### <----------------------- PART ONE -----------------------> ###
def performOperation(v1, op, v2):
    match op:
        case "+": return v1 + v2
        case "-": return v1 - v2
        case "*": return v1 * v2
        case "/": return v1 // v2


def eval(x):
    match input[x]:
        case [c1, op, c2]: 
            return performOperation(eval(c1), op, eval(c2))
        case v: return v

print("PART ONE:", eval("root"))

### <----------------------- PART TWO -----------------------> ###
def findPath(x, node):
    if x == node: return [x]
    match input[x]:
        case [c1, _, c2]: 
            if   path1 := findPath(c1, node): return [x] + path1
            elif path2 := findPath(c2, node): return [x] + path2
    return []


def calcTarget(x, par, t):
    isLeftChild = x == input[par][0]
    c1, op, c2 = input[par]
    s = (eval(c2) if isLeftChild else eval(c1))
    match op:
        case "+": return t - s
        case "-": return t + s if isLeftChild else s - t
        case "*": return t // s
        case "/": return t * s if isLeftChild else s // t


path = findPath("root", "humn")
def findTargets(x, t):
    match input[x]:
        case [c1, _, c2]:
            if c1 in path: return findTargets(c1, calcTarget(c1, x, t))
            else         : return findTargets(c2, calcTarget(c2, x, t))
        case _: return t

targetVal = eval(input["root"][2] if path[1] == input["root"][0] else input["root"][0])
print("PART TWO:", findTargets(path[1], targetVal))