input = open("2022/Input/10.txt").read().splitlines()

### <---------------- PART ONE ----------------> ###
C = [(1 if c[0] == "n" else 2) for c in input]
n = sum(C) + 1 # total number of cycles (plus 1 to execute last)

E = [0] * n # events where X changes
for i in range(1, len(C)):
    C[i] += C[i - 1] # cumulative sum of cycles 
    if input[i][0] == "a":
        E[C[i]] = int(input[i].split(" ")[1]) # addx int(number)

X = [1] + [0] * (n - 1)
res = 0
for i in range(0, n):
    X[i] += X[i - 1] + E[i]
    if (i + 1 + 20) % 40 == 0:
        res += X[i] * (i + 1)

print("PART ONE:", res)

### <---------------- PART TWO ----------------> ###
CRT = [["."]*40 for _ in range(6)]
for i, x in enumerate(X):
    row, col = i // 40, i % 40
    if x - 1 <= col <= x + 1: CRT[row][col] = "#"

print("PART TWO:")
for row in range(len(CRT)):
    print("".join(CRT[row]))












### <---------------- ALTERNATIVE PART ONE  ----------------> ###
# cycles = sum([1 for o in input if o == "noop"]) + (sum([2 for o in input if o.split(" ")[0] == "addx"]))
# ops = input + ["noop"] * (cycles - len(input))
# n = len(ops)


# X = [1] * n
# Q = [[0,0]]
# res = []

# for i, o in enumerate(ops):
#     priority, c1 = Q[0]
#     lastPriority, _ = Q[-1]

#     match o.split(" "):
#         case ["noop"]:  Q += [[lastPriority + 1, 0]]
#         case _, c2:     Q += [[lastPriority + 2, int(c2)]]

#     X[i] = X[i - 1]
#     if priority == i:
#         X[i] += c1
#         Q.pop(0)

#     if (i + 1 + 20) % 40 == 0:
#         res.append(X[i] * (i + 1))
        
# print("PART ONE:", sum(res))