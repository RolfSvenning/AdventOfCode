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
        case num: return num

print("PART ONE:", eval("root"))

### <----------------------- PART TWO -----------------------> ###
def findPath(x, node):
    if x == node: return [x]
    match input[x]:
        case [c1, _, c2]: 
            if   node in (path1 := findPath(c1, node)): return [x] + path1
            elif node in (path2 := findPath(c2, node)): return [x] + path2
    return []


def calcTargetVal(x, par, op, t):
    isLeftChild = x == input[par][0]
    s = (eval(input[par][2]) if isLeftChild else eval(input[par][0]))
    match op:
        case "+": return t - s
        case "-": return t + s if isLeftChild else s - t
        case "*": return t // s
        case "/": return t * s if isLeftChild else s // t


path = findPath("root", "humn")
def findTargetValue(x, targetVal):
    match input[x]:
        case [c1, op, c2]:
            if c1 in path: return findTargetValue(c1, calcTargetVal(c1, x, op, targetVal))
            else         : return findTargetValue(c2, calcTargetVal(c2, x, op, targetVal))
        case _: return targetVal


isLeftChild = input["root"][0] if path[1] == input["root"][0] else input["root"][1]
targetVal = eval(input["root"][2]) if isLeftChild else eval(input["root"][1])
print("PART TWO:", findTargetValue(path[1], targetVal))