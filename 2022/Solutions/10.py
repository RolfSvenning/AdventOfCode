ops = open("2022/Input/10.txt").read().splitlines()
cycles = sum([1 for o in ops if o == "noop"]) + 2 * (sum([1 for o in ops if o.split(" ")[0] == "addx"]))
ops += ["noop"] * (cycles - len(ops))
n = len(ops)

### <---------------- PART ONE ----------------> ###
X = [1] * n
Q = [[0,0]]
res = []

for i, o in enumerate(ops):
    priority, c1 = Q[0]
    lastPriority, _ = Q[-1]

    match o.split(" "):
        case ["noop"]:  Q += [[lastPriority + 1, 0]]
        case _, c2:     Q += [[lastPriority + 2, int(c2)]]

    X[i] = X[i - 1]
    if priority == i:
        X[i] += c1
        Q.pop(0)

    if (i + 1 + 20) % 40 == 0:
        res.append(X[i] * (i + 1))
        
print("PART ONE:", sum(res))

### <---------------- PART TWO ----------------> ###
CRT = [["."]*40 for _ in range(6)]
for i, x in enumerate(X):
    row, col = i // 40, i % 40
    if x - 1 <= col <= x + 1: CRT[row][col] = "#"

print("PART TWO:")
for row in range(len(CRT)):
    print("".join(CRT[row]))