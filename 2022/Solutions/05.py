import re

f = open("2022/Input/05.txt").read()
numberOfStacks = int(re.search("\d \n\n", f)[0].strip())
stacks = [[] for _ in range(numberOfStacks)]

for l in open("2022/Input/05.txt").readlines():
    if l[1].isnumeric(): break
    for i in range(0, numberOfStacks):
        i_ = 1 + i * 4
        if l[i_].isalpha():
            stacks[i].append(l[i_])
            
stacks = [list(reversed(s)) for s in stacks]
stacks2 = [list(s) for s in stacks] 

### <---------------- PART ONE & TWO ----------------> ###
for l in open("2022/Input/05.txt").readlines():
    if l[0:4] != "move": continue
    c, f, t = [int(d) for d in re.findall("\d+", l)]
    # PART ONE
    for _ in range(c):
        stacks[t - 1].append(stacks[f - 1].pop()) # stack numbers off by 1 in input
    # PART TWO
    stacks2[t - 1] +=  stacks2[f - 1][-c::]
    stacks2[f - 1]  =  stacks2[f - 1][:-c:]

print("Part one: ", "".join([s.pop() for s in stacks]))
print("Part two: ", "".join([s.pop() for s in stacks2]))