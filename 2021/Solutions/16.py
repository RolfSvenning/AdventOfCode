from collections import deque
from functools import reduce

class State:
    def __init__(self, ltID, operatorID, lenBits, nrPacks, lastStart, typeID):
        self.ltID = ltID
        self.operatorID = operatorID
        self.lenBits = lenBits
        self.nrPacks = nrPacks
        self.lastStart = lastStart
        self.typeID = typeID

    def __str__(self):
        return 'MyState(' + str(self.ltID) + ',' + str(self.operatorID) + ',' + str(self.lenBits) + ',' + str(self.nrPacks) + ',' + str(self.lastStart) + ')'
    
    def done(self):
        if self.lenBits == 0: return True
        if self.nrPacks == 0: return True
        return False

def versionToFun(s, ls): # FOR PART TWO
    res = 0
    match s:
        case "ID0": res = sum(ls)
        case "ID1": res = reduce(lambda a,x: a * x, ls)
        case "ID2": res = min(ls)
        case "ID3": res = max(ls)
        case "ID5": res = int(ls[1] > ls[0])
        case "ID6": res = int(ls[1] < ls[0])
        case "ID7": res = int(ls[1] == ls[0])
    return res

def part_one_and_two():
    h = open("2021/input/16.txt").readline().strip()
    b = "".join([format(int(s, 16), "04b") for s in h])
    n = len(b)
    operatorID = 0
    i = 0
    ops = deque()
    states = []
    versionSum = 0
    while(i < n):
        version = int(b[i:i+3], 2)
        typeID = int(b[i+3:i+6], 2)
        i += 6
        versionSum += version
        if states != [] and states[-1].nrPacks != None:
            states[-1].nrPacks -= 1

        if typeID == 4: # LITERAL VALUE
            litval = []
            for j in range(i, n, 5):
                group = b[j:j+5]
                litval.append(group[1:])
                if group[0] == "0":
                    i = j + 5
                    break
            
            if states != []:
                ops.append(int("".join(litval),2))
                if states[-1].lenBits != None:
                    states[-1].lenBits -= i - states[-1].lastStart
                    states[-1].lastStart = i
                while states[-1].done():
                        tops = []
                        while ops:
                            op = ops.pop()
                            if type(op) == int:
                                tops.append(op)
                            else:
                                assert op =="ID" + str(states[-1].typeID)
                                ops.append(versionToFun(op, tops))
                                break
                        states.pop()
                        if states == []:
                            break
                        if states[-1].lenBits != None:
                            states[-1].lenBits -= i - states[-1].lastStart
                            states[-1].lastStart = i
                            
            if states == []: # NO MORE PACKAGES LEFT
                break
            continue 

        # ELSE OPERATOR PACKET
        ops.append("ID" + str(typeID))
        ltID = int(b[i])
        lenBits = nrPacks = None
        if ltID == 0:
            lenBits = int(b[i+1:i+1+15], 2)
            i += 1 + 15
        else:
             nrPacks = int(b[i+1:i+1+11], 2)
             i += 1 + 11
        if states != []:
            if states[-1].lenBits != None:
                states[-1].lenBits -= i - states[-1].lastStart
                states[-1].lastStart = i
        states.append(State(ltID,operatorID,lenBits,nrPacks, i, typeID))
        operatorID += 1

    print("Part one, sum of version: ", versionSum)
    print("Part two, result of evaluating expression: ", ops[0])
   

if __name__ == '__main__':
    part_one_and_two() 