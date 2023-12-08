from math import lcm, gcd
import itertools

I = open("2023/input/08.txt").readline().strip()
n = len(I)
# print(I)

# ls ={k:v for l in open("2023/input/08.txt").readlines()[2:] for k, v in l.strip().split(" = ")}
ls =[l.strip().split(" = ") for l in open("2023/input/08.txt").readlines()[2:]]
# print(ls)
D ={k: v[1:9].split(", ") for k, v in ls}
# print(ls)

# ls =[(k, v[1:9].split(", ")) for l in open("2023/input/08.txt").readlines()[2:] for k, v in l.strip().split(" = ")]
# print(ls)

M = {"L": 0, "R": 1}

# steps = 0
# i = 0
# cur = "AAA"
# while(i < 100000):
#     print(cur)
#     steps += 1
#     ins = I[i % n]
#     cur = D[cur][M[ins]]
#     if cur == "ZZZ": break
#     i = i + 1
# print(steps)


# PART TWO: naive
# steps = 0
# i = 0
# S = set(k for k in D.keys() if k[-1] == "A")
# print("S: ", S)
# print(len(S))
# while(i < 10000000000000000000):
#     steps += 1
#     ins = I[i % n]
#     S = set(D[s][M[ins]] for s in S)
#     if all(s[-1] == "Z" for s in S): break
#     i = i + 1

# print(S)
# print(steps)

#PART TWO: smarter
S = [k for k in D.keys() if k[-1] == "A"]
print("S: ", S)
print(len(S))

EQ = []
for s in S:
    print("---", s)
    # enter cycle
    for i in range(5):
        ins = I[i % n]
        s = D[s][M[ins]]
        i = (i + 1) % n

    visited = [(s, i)]
    while(True):
        ins = I[i % n]
        s = D[s][M[ins]]
        i = (i + 1) % n
        if (s, i) in visited: break
        visited.append((s, i))
    # print("visited: ", visited)
    # print(s)
    Z = [visited.index(z) for z in visited if z[0][-1] == "Z"]
    # print("Z: ", Z)
    EQ.append((len(visited), Z))
print(EQ)

# assert(all(start == 0 for start,_,_ in EQ))

CNs = [c for c,_ in EQ]
lcmCN = lcm(*CNs)

# print(CNs, lcmCN)
# Zs = [z[1] for eq in]
    # break

def f(c1, c2):
    print("c1, c2: ", c1, c2)
    l1, z1 = c1
    l2, z2 = c2
    if l1 > l2: return f(c2, c1)
    # l1 <= l2
    for k in range(l2 + 1): # range l1?
        if (z2 + k * l2) % l1 == z1: break
    print("k: ", k)
    print((z2 + k * l2) % l1)
    assert k != l2
    return (lcm(l1, l2), (z2 + k * l2) % lcm(l1, l2)), (z2 + k * l2)

# print(f((7, 4), (5, 2)))

def shiftCycle(c, shift):
    l, z = c
    newPos = shift % l
    d = z - newPos if z >= newPos else l - newPos + z
    return (l, d)

# print(shiftCycle((11, 5), 32))

def eqToLoop(eq):
    return (eq[0], eq[1][0]) # eq have list of z vals (input only has one)

print("EQ0: ", EQ[0])
curEQ, shift = f(eqToLoop(EQ[0]), eqToLoop(EQ[1]))
for nextEQ in EQ[2:]:
    shiftCycle(eqToLoop(nextEQ), shift)
    curEQ, shift = f(curEQ, next)

    print("curEQ: ", curEQ)
print("curEQ: ", curEQ)



