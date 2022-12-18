import re
import copy
from functools import reduce

monkeys = open("2022/Input/11.txt").read().strip().split("Monkey ")[1:]
monkeys = [[re.findall("\d+|old|[+]|[*]", l) for l in m.strip().split("\n")] for m in monkeys]
n = len(monkeys)

### <----------------------- PART ONE -----------------------> ###
class Monkey():
    def __init__(self, id, items, op, test, monkeyTrue, monkeyFalse):
        self.id = int(id[0])
        self.items = [int(i) for i in items]
        self.op = eval(("lambda old: " + "".join(op)))
        self.test = lambda x: (x % int(test[0])) == 0
        self.monkeyTrue = int(monkeyTrue[0])
        self.monkeyFalse = int(monkeyFalse[0])
        self.inspects = 0
        self.partOne = True
        self.divis = int(test[0])

    def addItem(self, item):
        if self.partOne: self.items.append(item)
        else: self.items += [item]

    def throwItems(self):
        self.inspects += len(self.items)
        for item in self.items:
            if self.partOne: 
                newItem = self.op(item) // 3
                worryToTest = newItem
            else: 
                newItem = [self.op(item[i]) % self.divisors[i] for i in range(n)]
                worryToTest = newItem[self.id]
            if self.test(worryToTest):   self.monkeyTrue.addItem(newItem)
            else:                        self.monkeyFalse.addItem(newItem)
        self.items = []
    
    def changeToPartTwo(self, divisors): 
        self.partOne = False
        self.divisors = divisors
        self.items = [[item] * n for item in self.items] # make a version of the item for each monkey
        
monkeys = [Monkey(*m) for m in monkeys]
for m in monkeys:
    m.monkeyFalse = monkeys[m.monkeyFalse]
    m.monkeyTrue = monkeys[m.monkeyTrue]
monkeys2 = copy.deepcopy(monkeys)

for _ in range(20): # rounds
    for m in monkeys:
        m.throwItems()

print("PART ONE:", reduce(mul := lambda x,y: x*y, sorted([m.inspects for m in monkeys])[-2:]))

### <----------------------- PART TWO -----------------------> ###
divisors = [m.divis for m in monkeys2]
for m in monkeys2:
        m.changeToPartTwo(divisors)

for _ in range(10000): # rounds
    for m in monkeys2:
        m.throwItems()

print("PART TWO:", reduce(mul, sorted([m.inspects for m in monkeys2])[-2:]))