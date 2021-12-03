import sys


def foldLeft(acc, l, f):
    if l == []:
        return acc
    return foldLeft(f(acc, l[0]), l[1:], f)

def iterativeFold(acc, l, f):
    for i, item in enumerate(l):
        acc = f(acc, l[i])
    return acc

### PART ONE ----------------------------------------------
def sumForEachMove(acc,item):
    move, magnitude = item
    if move == "d":
        acc["depth"] += magnitude
    if move == "u":
        acc["depth"] -= magnitude
    if move == "f":
            acc["forward"] += magnitude
    return acc

def part_one():
    input = [((line.rstrip('\n'))[0], int((line.rstrip('\n'))[-1])) for line in open("2021/input/02.txt")] # converts down 9 -> ("d", 9)
    acc = {"depth": 0, "forward": 0}
    return foldLeft(acc, input, sumForEachMove)

### PART TWO ----------------------------------------------
def sumForAimAndDepth(acc,item):
    move, magnitude = item
    if move == "d":
        acc["aim"] += magnitude
    if move == "u":
        acc["aim"] -= magnitude
    if move == "f":
            acc["forward"] += magnitude
            acc["depth"] += acc["aim"] * magnitude
    return acc

def part_two():
    input = [((line.rstrip('\n'))[0], int((line.rstrip('\n'))[-1])) for line in open("2021/input/02.txt")] # converts down 9 -> ("d", 9)
    acc = {"depth": 0, "forward": 0, "aim": 0}
    return foldLeft(acc, input, sumForAimAndDepth)

if __name__ == "__main__":
    sys.setrecursionlimit(1010)
    acc1 = part_one()
    value1 = acc1["forward"] * (acc1["depth"])
    acc2 = part_two()
    value2 = acc2["forward"] * (acc2["depth"])
    print("Part one: ", value1)
    print("Part two: ", value2)