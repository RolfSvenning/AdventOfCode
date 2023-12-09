from math import lcm

I = open("2023/input/08.txt").readline().strip()
n1 = len(I)

ls =[l.strip().split(" = ") for l in open("2023/input/08.txt").readlines()[2:]]
n2 = len(ls)
D ={k: v[1:9].split(", ") for k, v in ls}
M = {"L": 0, "R": 1}

### <----------------------- PART ONE -----------------------> ###
steps = 0
i = 0
cur = "AAA"
while(i < 100000):
    steps += 1
    ins = I[i % n1]
    cur = D[cur][M[ins]]
    if cur == "ZZZ": break
    i = i + 1
print("PART ONE: ", steps)


### <----------------------- PART TWO -----------------------> ###
S = [k for k in D.keys() if k[-1] == "A"]
initSteps = 4 # in general should be n1 * n2 # to guarantee entering all cycles 

EQ = []
for s in S:
    for i in range(initSteps):
        ins = I[i % n1]
        s = D[s][M[ins]]
        i = (i + 1) % n1

    visited = [(s, i)]
    while(True):
        ins = I[i % n1]
        s = D[s][M[ins]]
        i = (i + 1) % n1
        if (s, i) in visited: break
        visited.append((s, i))

    Z = [visited.index(z) for z in visited if z[0][-1] == "Z"]
    EQ.append((len(visited), Z))

CNs = [c for c,_ in EQ]
lcmCN = lcm(*CNs)

def f(c1, c2):
    l1, z1 = c1
    l2, z2 = c2
    if l1 > l2: return f(c2, c1)
    for k in range(l1 + 1):
        if (z2 + k * l2) % l1 == z1: break
    assert k <= l1 + 1
    assert (z2 + k * l2) == (z2 + k * l2) % lcm(l1, l2) # never walk longer than lcm(l1,l2) I think
    return (lcm(l1, l2), (z2 + k * l2) % lcm(l1, l2)), (z2 + k * l2)


# eq have list of z vals (my input only has one so just take first, otherwise need to adapt code to try all)
def eqToLoop(eq):
    return (eq[0], eq[1][0]) 

curEQ, shift = f(eqToLoop(EQ[0]), eqToLoop(EQ[1]))
for nextEQ in EQ[2:]:
    nextEQ = eqToLoop(nextEQ)
    curEQ, shift = f(curEQ, nextEQ)

print("PART TWO: ", curEQ[1] + initSteps)

# 12030780859465 too low





# PART TWO: naive which doesn't work
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