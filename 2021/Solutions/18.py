import re
from numpy import floor, ceil

def part_one_and_two():
    lists =  [l.strip() for l in  open("2021/input/18.txt").readlines()]
    n = len(lists)
    for i in range(n - 1):
        lists[0] = explode(pairLists(lists[0], lists[i]))
    print("Part one,sum is: ", lSum(eval(lists[0])))

    bestSum = 0
    for i,j in [(i,j) for i in range(n) for j in range(n)]:
        bestSum = max(bestSum, lSum(eval(explode(pairLists(lists[i], lists[j])))))
    print("Part two, sum of best pair: ", bestSum)

def pairLists(l1,l2):
    return "[" + l1 + "," + l2 + "]"

def explode(l): # mutually recursive with split
    depth = 0
    for i in range(len(l)):
        assert depth <= 5
        match s := l[i]:
            case "[": depth += 1
            case "]": depth -= 1
            case ",": continue
            case _: 
                if depth < 5: continue
                j = i + 1
                while l[j] != "]":
                    j += 1
                ss = l[i:j]
                a,b = ss.split(",") #exploding pair a,b
                # looking for digits to the left
                if (r := re.compile('[0-9]+').search(l[0:i][::-1])) != None:
                    new  = str(int(a) + int(r[0][::-1]))
                    ll = l[:i-r.span()[1]] + new + l[i - r.span()[0]: i - 1]
                else:
                    ll = l[0:i-1]
                # looking for digits to the right
                if (r := re.compile('[0-9]+').search(l[j:])) != None: 
                    new = str(int(b) + int(r[0]))
                    lr = l[j + 1:j + r.span()[0]] + new + l[j + r.span()[1]:] # skip first [, then then take [,s to update then rest
                else:
                    lr = l[j + 1:]
                l = ll + "0" + lr
                break
    else:
        return split(l)
    return explode(l)
        

def split(l):
    r = re.compile('[0-9][0-9]+').search(l)
    if r != None:
        new = "[" + str(int(floor(int(r[0]) / 2))) + "," + str(int(ceil(int(r[0]) / 2))) + "]" # 13 -> [6,7]
        return explode(l[:r.span()[0]]  + new + l[r.span()[1]:])
    else:
        return l

def lSum(l):
    if type(l) is int:
        return l
    else:
        return 3 * lSum(l[0]) + 2 * lSum(l[1])


if __name__ == '__main__':
    part_one_and_two()