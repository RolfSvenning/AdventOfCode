import re
from numpy import floor, ceil

def part_one_and_two():
    # i = re.split("[ ,.=]+", open("2021/input/17.txt").readline().strip())
    lists =  [l.strip() for l in  open("2021/input/18.txt").readlines()]
    
    for i in range(len(lists) - 1):
        l = "[" + lists[0] + "," + lists[1] + "]"
        l = explode(l)
        break

    # print("RESULT: ", lists)

def explode(l):
    print("exploding:","\n" + l)
    depth = 0
    for i in range(len(l)):
        s = l[i]
        assert depth <= 5
        match s:
            case "[": depth += 1
            case "]": depth -= 1
            case ",": continue
            case _: 
                if depth < 5: continue
                assert re.compile('[0-9]').match(s) != None
                j = i + 1
                while l[j] != "]":
                    j += 1
                    # print(l[j])
                # print("i,j: ", i,j)
                ss = l[i:j]
                a,b = ss.split(",")
                assert re.compile('[0-9]+,[0-9]+').match(ss) != None # check that pair does not contain another pair
                if (r := re.compile('[0-9]+').search(l[0:i][::-1])) != None: #looking for digits to the left
                    # print(r[0], r.span())
                    # print(l[:i-r.span()[1]])
                    new  = str(int(a) + int(r[0]))
                    ll = l[:i-r.span()[1]] + new + l[i - r.span()[0]: i - 1]
                else:
                    ll = l[0:i-1]y
                if (r := re.compile('[0-9]+').search(l[j:])) != None: #looking for digits to the right
                    new = str(int(b) + int(r[0]))
                    lr = new + l[j + r.span()[1]:]
                else:
                    lr = "0" + l[j:]

                print(ll + "--" + lr)
                l = ll + "," + lr
                print(l)
                break # exploded
    else:
        return split(l)
    return explode(l)
        

def split(l):
    r = re.compile('[0-9][0-9]+').search(l)
    if r != None:
        print(int(r[0]))
        new = "[" + str(int(floor(int(r[0]) / 2))) + "," + str(int(ceil(int(r[0]) / 2))) + "]"

        lNew = l[:r.span()[0]]  + new + l[r.span()[1]:]
        print(lNew)
        return explode(lNew)
    else:
        return l



if __name__ == '__main__':
    part_one_and_two()