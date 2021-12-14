import numpy as np


def part_one_and_two():
    polymer, rules = open("2021/input/14.txt").read().split("\n\n")
    rules = [x.split(" -> ") for x in rules.split("\n")]
    rulesMap = {}
    for l,r in rules:
        rulesMap[l] = r
    
    insertions = []
    for i, (a,b) in enumerate(zip(polymer,polymer[1:])):
        print("ab: ", a + b)
        if (ab := a + b) in rulesMap:
    #         print("TRUE")
    #         print(rulesMap[ab])
            insertions.append((i, rulesMap[ab]))
    print(insertions)


    currIndex = 0
    curr = insertions[0][0]
    res = []
    print("curr: ", curr)
    for i in range(len(polymer)):
        while i <= curr:
            res.append[polymer[i]]
            if i == curr:
                break
        curr = 


        


if __name__ == '__main__':
    part_one_and_two()