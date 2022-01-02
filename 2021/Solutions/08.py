import numpy as np


def part_one():
    outputValues = [s for line in open("2021/input/08.txt") for s in line.split("|")[1].strip().split(" ")]
    count_of_1478 = len([s for s in outputValues if len(s) in [2, 4, 3, 7]])
    print("Part one, count of easy digits: ", count_of_1478)


def part_two():
    # Note that input strings are sorted!
    uniqueSignals = [["".join(sorted(s)) for s in line.split("|")[0].strip().split(" ")] for line in open("2021/input/08.txt")]
    outputValues = [["".join(sorted(s)) for s in line.split("|")[1].strip().split(" ")] for line in open("2021/input/08.txt")]

    def decode(uniques, outputs):
        oldToNew = {}
        newToDigit = {}
        digitToNew = {}
        fives_235 = []
        sixes_069 = []
        for s in uniques:
            match len(s):
                case 2:
                    newToDigit[s] = 1
                    digitToNew[1] = s
                case 3:
                    newToDigit[s] = 7
                    digitToNew[7] = s
                case 4:
                    newToDigit[s] = 4
                    digitToNew[4] = s
                case 5:
                    fives_235.append(s)
                case 6:
                    sixes_069.append(s)
                case 7:
                    newToDigit[s] = 8
                    digitToNew[8] = s

        oldToNew["a"] = (set(digitToNew[7]) - set(digitToNew[1])).pop()

        sixes_06 = []
        for s in sixes_069:
            if len(setDiff := (set(s) - (set(digitToNew[4]).union(oldToNew["a"])))) == 1:
                g_new = setDiff.pop()
                oldToNew["g"] = g_new
                digitToNew[9] = s
                newToDigit[s] = 9
            else:
                sixes_06.append(s)
        
        oldToNew["e"] = set(sixes_06[0]).difference(set(digitToNew[4]).union(set([oldToNew["a"], oldToNew["g"]]))).pop()

        for s in sixes_06:
            if (setDiff := set(digitToNew[9]).difference(set(s)).pop()) in set(digitToNew[1]):
                digitToNew[6] = s
                newToDigit[s] = 6
                oldToNew["c"] = setDiff
            else:
                digitToNew[0] = s
                newToDigit[s] = 0
                oldToNew["d"] = setDiff

        for s in fives_235:
            if s == "".join(sorted(oldToNew.values())):
                newToDigit[s] = 2
            elif len(set(s).difference(set(digitToNew[6]))) == 0:
                newToDigit[s] = 5
            else:
                newToDigit[s] = 3

        return int("".join([str(newToDigit[s]) for s in outputs]))

    print("Part two, count of all digits: ", np.sum([decode(a, b) for a,b in zip(uniqueSignals, outputValues)]))


if __name__ == '__main__':
    part_one()
    part_two()