import re
import copy

monkeys = open("2022/Input/11.txt").read().strip().split("Monkey ")[1:]
n = len(monkeys)
print("n", n)
monkeys = [[re.findall("\d+|old|[+]|[*]", l) for l in m.strip().split("\n")] for m in monkeys]

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

    def __str__(self):
        return f"Monkey {self.id}: Starting items: {str(self.items)[1:-1]}"

    def addItem(self, item):
        if self.partOne: self.items.append(item)
        else: self.items += [item]


    def throwItems(self):
        self.inspects += len(self.items) #96577
        for item in self.items:
            if self.partOne: 
                newItem = self.op(item) // 3
                worryToTest = newItem
            else: 
                # print(divisors)
                # print(self.items)
                # print(item)
                newItem = [self.op(item[i]) % self.divisors[i] for i in range(n)]
                worryToTest = newItem[self.id]

            if self.test(worryToTest):   self.monkeyTrue.addItem(newItem)
            else:                        self.monkeyFalse.addItem(newItem)
        self.items = []
    
    def changeToPartTwo(self, divisors): 
        self.partOne = False
        self.divisors = divisors
        # print(self.items)
        # print([[item]*4 for item in self.items])
        self.items = [[item] * n for item in self.items] # make a version of the item for each monkey
        

monkeys = [Monkey(*m) for m in monkeys]
for m in monkeys:
    m.monkeyFalse = monkeys[m.monkeyFalse]
    m.monkeyTrue = monkeys[m.monkeyTrue]
monkeys2 = copy.deepcopy(monkeys)
monkeys3 = copy.deepcopy(monkeys)

for r in range(20): # rounds
    for m in monkeys:
        m.throwItems()

print("PART ONE:", sorted([m.inspects for m in monkeys])[-1] * sorted([m.inspects for m in monkeys])[-2])

naive = [100000000000000000000000000000000000000000000] * n
print([m.divis for m in monkeys2])
divisors = [m.divis for m in monkeys2]
print("maxDivis", divisors)
def test(monkeys, divisors):
    for m in monkeys:
            m.changeToPartTwo(divisors)
    for _ in range(10000): # rounds
        for m in monkeys:
            m.throwItems()

test(monkeys2, naive)
test(monkeys3, divisors)



print([m.inspects for m in monkeys2])
# print([m.items for m in monkeys2])
print([m.inspects for m in monkeys3])
# print([m.items for m in monkeys3])

print("PART TWO:", sorted([m.inspects for m in monkeys3])[-1] * sorted([m.inspects for m in monkeys3])[-2])

